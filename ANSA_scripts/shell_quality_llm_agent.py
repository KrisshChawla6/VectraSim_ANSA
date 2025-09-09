#
# Agent to correct shell quality. Uses both ANSA built-in functions and Gemini LLM to suggest best repair strategy.
#
# ==========================

import os

# Set the proxy, necessary for Google Gemini API access in China
proxy = "http://127.0.0.1:10809"  # Replace with your localhost proxy address and port
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

import json
from ansa import base, mesh
import google.generativeai as genai
import re
import warnings
import glob

# ANSA basic manual operations
from manual_operations.edge_split import edge_split
from manual_operations.shell_join import shell_join
from manual_operations.shell_split import split_shell
from manual_operations.node_movement import node_movement

from ansa_improve.advanced_quality_improve import *

DECK = base.CurrentDeck()
SHELL_TYPE = "SHELL"
SECTION_SHELL = "SECTION_SHELL"
NEIGHBOR_LEVEL = 1
QUALITY_CRITERIA = {
    "ASPECT": "aspect_ratio",
    "SKEW": "skewness",
    "WARP": "warping",
    "TAPER": "taper",
    "MIN ANGLE": "min_angle_trias",
    "JACOB": "jacobian",
}


def get_bad_shells(shells):
    """Return shells failing quality check."""
    return [s for s in shells if base.CalculateOffElements(s)["TOTAL OFF"] != 0]


def configure_agent():
    API_KEY = "API_KEY"

    # ---------- Configure ----------
    genai.configure(api_key=API_KEY)

    # ---------- Output schema: plan with one or more steps ----------
    # Each step must be exactly one of the four tool calls you support.
    PLAN_SCHEMA = {
        "type": "object",
        "properties": {
            "steps": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "move_node",
                                "split_edge",
                                "split_quad",
                                "merge_trias",
                            ],
                        },
                        "node_id": {"type": "integer"},
                        "vector": {"type": "array", "items": {"type": "number"}},
                        "distance": {"type": "number"},
                        "edge": {"type": "array", "items": {"type": "integer"}},
                        "element_id": {"type": "integer"},
                        "element_ids": {"type": "array", "items": {"type": "integer"}},
                        "why": {"type": "string"},
                    },
                    "required": ["action", "element_id"],
                },
            }
        },
        "required": ["steps"],
    }

    # ---------- System instruction ----------
    # SYSTEM = """
    # You are a LOCAL MESH REPAIR POLICY AGENT.
    # You receive a small patch (tens of elements) with:
    # - nodes: id, coords
    # - elements: id, type (TRIA|QUAD), node ids
    # - violations: (element_id, criterion, value, threshold, is_max_threshold)
    # - history: list of recent actions and their outcomes

    # Your job: propose a minimal sequence of actions (1-3 steps) chosen ONLY from:
    # 1) move_node(node_id, vector[dx,dy,dz], distance s)
    # 2) split_edge(edge=[nA,nB]) at mid-point (split neighboring cells)
    # 3) split_quad(element_id) along the SHORTER diagonal into two TRIAs
    # 4) merge_trias(element_ids=[e1,e2]) into one QUAD

    # Hard constraints:
    # - Reference ONLY node/element IDs that exist in the input.
    # - Do NOT invent geometry. No new nodes except those created implicitly by split tools.

    # Repair Policy Hierarchy:

    # 1. Node movement (default first step)
    # - Use `move_node` when a single node causes JACOB or WARP violations, or when a small adjustment improves multiple violations.
    # - Prefer in-plane or edge-aligned moves, avoid drastic normal changes.
    # - Use incremental displacements. If a history move failed, try the opposite direction.
    # - Select the node with the worst corner angle (<45° or >135°) in the violating element(s).
    # - Prefer moving this node, since adjusting extreme angles toward 90° improves both JACOB and WARP.
    # - Do not move nodes whose corner angles are already near 90° unless all others are equally poor.

    # 2. Splitting (only if movement insufficient)
    # - Use `split_edge` or `split_quad` if node moves cannot resolve violations without creating new ones.
    # - Criteria: QUAD warpage > 15–20°, JACOB < 0.4 with trapped geometry, or aspect ratio > 5:1.
    # - Prefer `split_edge` to balance long edges.
    # - Use `split_quad` if warpage remains high; check resulting TRIAs for angles > 20°.

    # 3. Merging (only when it simplifies mesh)
    # - Use `merge_trias` when two TRIAs share two nodes and form a near-rectangle/parallelogram.
    # - Only merge in flat regions; do not merge across feature edges.
    # - Ensure resulting QUAD has Jacobian > 0.7.

    # 4. General priorities
    # - Fix most critical violations first (low Jacobian, then high warpage).
    # - Apply one fix per violation at a time.
    # - Choose the least invasive change that reduces element count increase and maintains structured topology.

    # Output MUST be valid JSON following the provided schema. Keep 'why' concise for each step.
    # """

    SYSTEM = """
    You are a LOCAL MESH REPAIR POLICY AGENT working in conjunction with ANSA’s optimizer.

    Input:
    - nodes: id, coords
    - elements: id, type (TRIA|QUAD), node ids
    - violations: (element_id, criterion, value, threshold, is_max_threshold)
    - history: list of recent actions and their outcomes

    Available actions (only these):
    1) move_node(node_id, vector[dx,dy,dz], distance s)
    2) split_edge(edge=[nA,nB]) at mid-point (split neighboring cells)
    3) split_quad(element_id) along the SHORTER diagonal into two TRIAs
    4) merge_trias(element_ids=[e1,e2]) into one QUAD

    Hard constraints:
    - Reference ONLY node/element IDs that exist in the input.
    - Do NOT invent geometry. No new nodes except those created implicitly by split tools.
    - Preserve feature/boundary alignment; avoid inverted or zero-area elements.

    Role relative to ANSA:
    - Assume ANSA already attempts continuous smoothing and reshape operations (small node movements to improve quality).  
    - Do NOT duplicate ANSA’s micro-optimization behavior.  
    - Your purpose is to provide *supplementary fixes* where ANSA struggles.

    Repair Policy Hierarchy:

    1. Node movement (only when ANSA smoothing fails or is insufficient)  
    - Identify the node that causes the worst corner angles (<45° or >135°) in the violating element(s).  
    - Prefer moving this node, especially if it participates in multiple failing elements.  
    - Move along in-plane or edge-bisector directions to regularize angles toward ~90°.  
    - Small displacement only; if history shows failure, reverse direction or escalate to split.  

    2. Splitting (primary supplement to ANSA)  
    - Use `split_edge` or `split_quad` when ANSA cannot resolve violations by node moves.  
    - Typical cases: QUAD warpage > 15–20°, JACOB < 0.4 with trapped geometry, or highly stretched aspect ratio (> 5:1).  
    - Prefer `split_edge` for long-edge elements, `split_quad` for warped quads.  
    - Verify resulting TRIAs have acceptable angles (>20°).  

    3. Merging (to simplify mesh)  
    - Use `merge_trias` when two adjacent TRIAs form a near-parallelogram/rectangle.  
    - Only in low-curvature regions; do not merge across features.  
    - Ensure resulting QUAD has Jacobian > 0.7.  

    4. History-aware escalation  
    - If repeated node moves worsen quality → try splitting instead.  
    - If splitting increased skewness → revert and try moving the opposite node.  
    - Always avoid oscillation; prefer escalation over repetition.  

    5. General priorities  
    - Address the most critical violations first: low Jacobian → worst-corner node; high warpage → flatten via move, then split if needed.  
    - Aim for one fix per violation at a time.  
    - Choose the least invasive action that ANSA cannot already achieve by continuous optimization.  

    Output requirements:
    - Return ONLY valid JSON following the provided schema.
    - Each step must include a short 'why' explaining the reasoning.
    """

    # ---------- Model with structured JSON output ----------
    model = genai.GenerativeModel(
        model_name="gemini-2.5-pro",
        system_instruction=SYSTEM,
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=PLAN_SCHEMA,
        ),
    )
    return model


def propose_repair_plan(
    model, mesh_patch: dict, history: list, max_steps: int = 2
) -> dict:
    """
    Ask Gemini for a plan that satisfies PLAN_SCHEMA.
    """
    input_payload = {"mesh": mesh_patch, "history": history}
    prompt = (
        "Given the following local mesh patch and history, propose up to "
        f"{max_steps} step(s) to resolve the violations. "
        "Return only JSON that conforms to the schema.\n\n"
        + json.dumps(input_payload, separators=(",", ":"))
    )

    # Count input tokens
    response_tokens = model.count_tokens(prompt)
    print(f"Input tokens: {response_tokens.total_tokens}")
    if response_tokens.total_tokens > 8000:
        warnings.warn("Input prompt is very long")
    if response_tokens.total_tokens > 100000:
        raise ValueError("Input prompt exceeds token limit")

    resp = model.generate_content(prompt, stream=False)
    return json.loads(resp.text)


def repair_mesh(
    mesh_data: dict, current_itr: int = 1, max_steps: int = 2, element_idx: int = None
):
    global current_dir
    model = configure_agent()
    history = []
    if element_idx is not None:
        file_name_prefix = f"export_{element_idx}"

        # Get all local files with file_name_prefix_actions, e.g. export_61_actions_1.json, export_61_actions_2.json
        action_files = glob.glob(
            os.path.join(
                current_dir,
                "export",
                f"{file_name_prefix}_actions_*.json",
            )
        )

        print(action_files)
        for action_file in action_files:
            with open(action_file, "r") as f:
                actions = json.load(f)
                history.extend(actions.get("steps", []))

        print(history)

    it = current_itr
    print(f"\n=== Iteration {it} ===")
    if not mesh_data.get("violations"):
        print("✅ Mesh has no violations. Done.")
        return mesh_data, history

    strategy = controller_decision(mesh_data.get("violations", []), history)
    print(f"Controller chose: {strategy}")

    if strategy == "ansa_fix":
        mesh.FixQuality()
        plan = {
            "steps": [
                {"action": "ansa_fix", "element_id": None, "why": "Standard ANSA fix"}
            ]
        }
    elif strategy == "ansa_reshape":
        mesh.Reshape()
        plan = {
            "steps": [
                {"action": "ansa_reshape", "element_id": None, "why": "ANSA reshape"}
            ]
        }
    elif strategy == "ansa_reconstruct":
        mesh.Reconstruct()
        plan = {
            "steps": [
                {
                    "action": "ansa_reconstruct",
                    "element_id": None,
                    "why": "ANSA reconstruct",
                }
            ]
        }
    elif strategy == "llm":
        plan = propose_repair_plan(model, mesh_data, history, max_steps=max_steps)
    else:
        plan = {"steps": []}

    # plan = propose_repair_plan(model, mesh_data, history, max_steps=max_steps)
    # print("Proposed plan:\n", json.dumps(plan, indent=2))

    # Export suggested action into json file
    with open(
        os.path.join(
            os.path.dirname(__file__),
            os.path.join(
                current_dir,
                "export",
                f"export_{element_idx}_actions_{it}.json",
            ),
        ),
        "w",
    ) as f:
        json.dump(plan, f, indent=2)

    if not strategy == "llm":
        return mesh_data, history

    try:
        execute_agent_actions(element_idx, it)
        print(f"Actions on element {element_idx} at iteration {it} succeeded.")
        mesh.FixQuality()
    except Exception as e:
        print(
            f"Error occurred while executing actions on element {element_idx} at iteration {it}: {e}"
        )

    return mesh_data, history


def execute_agent_actions(test_idx: int, itr: int):
    global current_dir

    # Read in json file of suggested actions:
    with open(
        os.path.join(
            current_dir,
            "export",
            f"export_{test_idx}_actions_{itr}.json",
        ),
        "r",
    ) as f:
        actions = json.load(f)
        print(actions)

    for step in actions.get("steps", []):
        print(step)

        # Execute each step using ANSA API
        if step["action"] == "move_node":
            node_to_move = base.GetEntity(DECK, "GRID", step["node_id"])
            node_coords = base.GetEntityCardValues(
                DECK, node_to_move, ("X1", "X2", "X3")
            )
            node_movement(
                node_to_move,
                {
                    "X1": node_coords["X1"] + step["vector"][0],
                    "X2": node_coords["X2"] + step["vector"][1],
                    "X3": node_coords["X3"] + step["vector"][2],
                },
            )
        elif step["action"] == "split_edge":
            edge_split()
        elif step["action"] == "split_quad":
            element_to_split = base.GetEntity(DECK, SHELL_TYPE, step["element_id"])
            split_shell(element_to_split)
        elif step["action"] == "merge_trias":
            shell1 = base.GetEntity(DECK, SHELL_TYPE, step["element_ids"][0])
            shell2 = base.GetEntity(DECK, SHELL_TYPE, step["element_ids"][1])
            shell_join(shell1, shell2)
        else:
            print(f"Unknown action: {step['action']}")


def controller_decision(violations: list, history: list) -> str:
    """
    Decide which repair strategy to use:
      - 'ansa_fix'      → mesh.FixQuality()
      - 'ansa_reshape'  → mesh.Reshape()
      - 'ansa_reconstruct' → mesh.Reconstruct()
      - 'llm'           → call Gemini agent

    Decision is based on violation severity, clustering, and history.
    """
    if not violations:
        return None

    # Count severity
    jacob_low = [
        v for v in violations if v["criterion"].upper() == "JACOB" and v["value"] < 0.4
    ]
    warp_high = [
        v for v in violations if v["criterion"].upper() == "WARP" and v["value"] > 15
    ]
    aspect_bad = [
        v for v in violations if v["criterion"].upper() == "ASPECT" and v["value"] > 5
    ]

    # History-aware: if ANSA failed before on this patch
    if any(h["action"].startswith("ansa") for h in history):
        return "llm"

    # Simple rules
    if len(jacob_low) == 0 and len(warp_high) == 0:
        # Mild issues → let ANSA handle
        return "ansa_fix"

    if jacob_low and len(jacob_low) > 3:
        # Many severe Jacobian violations → LLM may help
        return "llm"

    if warp_high and len(warp_high) > 2:
        # Many warped quads → LLM split may help
        return "llm"

    if aspect_bad and len(aspect_bad) > 5:
        return "ansa_reconstruct"

    return "ansa_fix"


def main(model_path: str = None):
    base.All()

    debug = True

    current_model = base.GetCurrentAnsaModel()

    if not current_model:
        base.Open(model_path)
        current_model = base.GetCurrentAnsaModel()

    # Parse model_path to get current directory
    model_path = (
        "D:\OneDrive - Stanford\VectraSim files\Lucid\CAD from Lucid\Reduced_Set\LIFTGATE SPOILER LWR INNER[1]_meshed.ansa"
        # "D:\OneDrive - Stanford\VectraSim files\CAE part example\Medium\Back Door BIW_meshed.ansa"
        if not model_path
        else model_path
    )
    global current_dir

    current_dir = os.path.dirname(model_path)
    print(current_dir)

    if not debug:
        print("Debug mode is off")
        # C. Perform mesh quality analysis & correction
        base.All()

        # Identify and delete intersections
        intersection_elements = base.CheckIntersections(True, False, False)
        if intersection_elements:
            base.DeleteEntity(intersection_elements)

        advanced_quality_check()

    else:  # Move this to suitable line for skipping certain part of the code during debugging
        all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)

        status = mesh.ReadQualityCriteria(
            "D:\OneDrive - Stanford\VectraSim files\ANSA\default.ansa_qual"
        )

        # Identify bad shells
        bad_shells = get_bad_shells(all_shells)
        print(len(all_shells))

        it = 0

        bad_shells_count = []

        while bad_shells:
            bad_shells_count.append(len(bad_shells))

            if it >= 5:
                print("Max iterations reached")
                break

            it = it + 1
            print(f"Found {len(bad_shells)} bad shells.")

            shell_visited = set()
            for shell in bad_shells:
                if shell not in shell_visited:
                    shell_visited.update([shell])
                else:
                    continue

                print(shell._id)

                bad_shells_visible, current_visible = isolate_problematic_cell(shell)

                shell_visited.update(bad_shells_visible)

                base.SetEntityVisibilityValues(DECK, {"GRID": "enable"})
                shell_quality = base.CalculateOffElements(shell, details=True)

                element_quality_dict = {}
                visib_entities = base.CollectEntities(
                    DECK, None, SHELL_TYPE, True, filter_visible=True
                )

                for elem in visib_entities:
                    elem_quality = base.ElementQuality(elem, QUALITY_CRITERIA.keys())
                    element_quality_dict[elem._id] = elem_quality

                # Export visible shells for LLM agent processing
                filename = os.path.join(
                    current_dir, "export", f"export_{shell._id}.inp"
                )
                visible_export_path = base.OutputAbaqus(filename, "visible")
                print(f"Exported visible shell {shell._id} to {visible_export_path}")

                inp_text_io = open(filename, "r").read()

                def parse_quality_thresholds(quality_file_path):
                    """Parse ANSA mesh quality file and extract the 'Failed' threshold and threshold type for each shell criterion."""
                    thresholds = {}
                    with open(quality_file_path, "r") as f:
                        in_shell_criteria = False
                        for line in f:
                            if line.strip().startswith("# Criterion [shells]"):
                                in_shell_criteria = True
                                continue
                            if in_shell_criteria:
                                if line.strip().startswith(
                                    "# "
                                ) and not line.strip().startswith(
                                    "# Criterion [shells]"
                                ):
                                    break
                                m = re.match(
                                    r"^([a-zA-Z0-9 _%]+)\[shells\]\s*=\s*(.*)", line
                                )
                                if m:
                                    crit_name = (
                                        m.group(1).strip().lower().replace(" ", "_")
                                    )
                                    rest = m.group(2)
                                    # Extract value flag (after 2nd |, before next ,)
                                    value_flag_match = re.search(
                                        r"\|\s*([01]\.)\s*,", rest
                                    )
                                    is_max_threshold = None
                                    if value_flag_match:
                                        is_max_threshold = (
                                            value_flag_match.group(1) == "0."
                                        )
                                    # Find all occurrences of -1\./<value>,
                                    matches = re.findall(r"-1\./\s*([-\d.eE]+)", line)
                                    failed_column = (
                                        float(matches[1]) if len(matches) >= 2 else None
                                    )
                                    thresholds[crit_name] = {
                                        "threshold": failed_column,
                                        "is_max_threshold": is_max_threshold,
                                    }
                    return thresholds

                def parse_inp_and_combine(inp_text, element_quality_dict):
                    nodes = []
                    elements = []
                    node_section = False
                    element_section = False
                    element_type = None

                    node_pattern = re.compile(
                        r"^\s*(\d+),\s*([-\d.eE]+),\s*([-\d.eE]+),\s*([-\d.eE]+)"
                    )
                    elem_pattern = re.compile(r"^\s*(\d+),\s*([\d,\s]+)")

                    for line in inp_text.splitlines():
                        if line.strip().startswith("*NODE"):
                            node_section = True
                            element_section = False
                            continue
                        if line.strip().startswith("*ELEMENT"):
                            node_section = False
                            element_section = True
                            # Get element type
                            m = re.search(r"TYPE=(\w+)", line)
                            element_type = m.group(1) if m else None
                            continue
                        if line.strip().startswith("*"):
                            node_section = False
                            element_section = False
                            continue

                        if node_section:
                            m = node_pattern.match(line)
                            if m:
                                nid = int(m.group(1))
                                coords = [
                                    float(m.group(2)),
                                    float(m.group(3)),
                                    float(m.group(4)),
                                ]
                                nodes.append({"id": nid, "coords": coords})
                        elif element_section:
                            m = elem_pattern.match(line)
                            if m:
                                eid = int(m.group(1))
                                node_ids = [
                                    int(x) for x in line.split(",")[1:] if x.strip()
                                ]
                                etype = (
                                    "CQUAD4"
                                    if element_type
                                    and element_type.startswith("S4")
                                    and len(node_ids) == 4
                                    else "CTRIA3"
                                )
                                elements.append(
                                    {"id": eid, "type": etype, "nodes": node_ids}
                                )

                    # Violations: flatten element_quality_dict to the required format
                    violations = []
                    for eid, qual in element_quality_dict.items():
                        for crit, val in zip(QUALITY_CRITERIA.keys(), qual):
                            if val == "error":
                                continue
                            tinfo = thresholds.get(QUALITY_CRITERIA[crit], {})
                            violations.append(
                                {
                                    "element_id": eid,
                                    "criterion": crit,
                                    "value": val,
                                    "threshold": tinfo.get("threshold"),
                                    "is_max_threshold": tinfo.get("is_max_threshold"),
                                }
                            )

                    return {
                        "nodes": nodes,
                        "elements": elements,
                        "violations": violations,
                    }

                status = mesh.ReadQualityCriteria(
                    "D:\OneDrive - Stanford\VectraSim files\ANSA\default.ansa_qual"
                )

                # Parse thresholds from mesh quality file
                quality_file_path = (
                    "D:\OneDrive - Stanford\VectraSim files\ANSA\default.ansa_qual"
                )
                thresholds = parse_quality_thresholds(quality_file_path)

                parsed = parse_inp_and_combine(inp_text_io, element_quality_dict)

                # Filter violations
                def filter_violations(parsed):
                    filtered = []
                    # Build a lookup for element type by id
                    elem_type_lookup = {
                        e["id"]: e["type"] for e in parsed.get("elements", [])
                    }
                    for v in parsed["violations"]:
                        threshold = v.get("threshold")
                        is_max = v.get("is_max_threshold")
                        value = v.get("value")
                        elem_type = elem_type_lookup.get(v["element_id"])
                        # Remove ASPECT violations for CQUAD4 elements
                        if (
                            v.get("criterion", "").upper() == "ASPECT"
                            and elem_type == "CQUAD4"
                        ):
                            continue
                        # Remove if threshold or is_max_threshold is None or not a number/bool
                        if threshold is None or is_max is None:
                            continue
                        try:
                            threshold = float(threshold)
                            value = float(value)
                        except Exception:
                            continue
                        if is_max is True and value > threshold:
                            filtered.append(v)
                        elif is_max is False and value < threshold:
                            filtered.append(v)
                    parsed["violations"] = filtered

                filter_violations(parsed)

                json_filename = os.path.join(
                    current_dir, "export", f"export_{shell._id}.json"
                )
                with open(json_filename, "w") as json_file:
                    json.dump(parsed, json_file, indent=4)

                print(f"Exported element {shell._id}")

                # Now run through Gemini API to get suggested actions and feedback loop
                with open(
                    os.path.join(
                        os.path.dirname(__file__),
                        os.path.join(
                            current_dir,
                            "export",
                            f"export_{shell._id}.json",
                        ),
                    ),
                    "r",
                ) as f:
                    mesh_data = json.load(f)

                try:
                    mesh_data, _ = repair_mesh(
                        mesh_data, current_itr=it, max_steps=2, element_idx=shell._id
                    )
                except Exception as e:
                    print(f"Error occurred while repairing mesh: {e}")
                    continue

            all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
            bad_shells = get_bad_shells(all_shells)

        print("All bad shells visited.")

        base.All()
        mesh.FixQuality()

        bad_shells = get_bad_shells(all_shells)
        bad_shells_count.append(len(bad_shells))

        print(bad_shells_count)


if __name__ == "__main__":
    main()
