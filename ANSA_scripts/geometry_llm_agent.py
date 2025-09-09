#
# Agent to perform geometry cleanup, making sure midsurface mesh matches CAD geometry.
# Uses both ANSA built-in functions and Gemini LLM to suggest best repair strategy.
#
# This is currently WIP and it appears the geometry repair task is too complex for current LLMs to handle well.
#
# ==========================

import os

# Set the proxy
proxy = "http://127.0.0.1:10809"  # Replace with your localhost proxy address and port
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

import json
from ansa import base, constants, mesh
import google.generativeai as genai
import re
import warnings

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


def expand_to_neighbors(shells, max_level=NEIGHBOR_LEVEL):
    """Expand visibility to neighbors iteratively."""
    seen = set(shells)
    queue = shells[:]

    while queue:
        all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
        base.Not(all_shells)  # hide all
        base.Or(entities=shells)
        base.Neighb(str(max_level))
        new_visible = base.CollectEntities(
            DECK, None, SHELL_TYPE, True, filter_visible=True
        )
        base.All()  # get visible shells

        # Detect new shells
        new_shells = [s for s in new_visible if s not in seen]
        if not new_shells:
            break
        seen.update(new_shells)
        queue = new_shells

    return list(seen)


def isolate_problematic_mid_cell(target_shell, middle_mesh_violations):
    """Expand to neighbors recursively until no more new bad shells"""
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)

    expanded_shells = expand_to_neighbors([target_shell])
    base.Not(all_shells)
    base.Or(entities=expanded_shells)
    current_visible = base.CollectEntities(
        DECK, None, SHELL_TYPE, True, filter_visible=True
    )

    problematic_cells = set()
    for values in middle_mesh_violations.values():
        problematic_cells.update(values)

    bad_shells_visible = [s for s in current_visible if s._id in problematic_cells]

    prev_len = -1
    while len(bad_shells_visible) > prev_len:
        prev_len = len(bad_shells_visible)
        expanded_shells = expand_to_neighbors(bad_shells_visible)
        base.Not(all_shells)
        base.Or(entities=expanded_shells)
        current_visible = base.CollectEntities(
            DECK, None, SHELL_TYPE, True, filter_visible=True
        )
        bad_shells_visible = [s for s in current_visible if s._id in problematic_cells]

    return bad_shells_visible, current_visible


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
                                "create_nodes",
                                "create_element",
                                "delete_element",
                            ],
                        },
                        "node_id": {"type": "integer"},
                        "node_ids": {"type": "array", "items": {"type": "integer"}},
                        "coords": {
                            "type": "array",
                            "items": {"type": "array", "items": {"type": "number"}},
                        },
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

    SYSTEM = """
		You are a mesh repair agent working inside ANSA.  
		Your task is to repair a midsurface mesh so that it matches the original CAD geometry.  

		You will be given:  
		1. A list of nodes and elements describing the current mesh.  
		2. The results of ANSA's CheckMiddleMesh tool, which highlight problematic elements or regions.  

		### Action definitions:
		1) move_node(node_id, vector[dx,dy,dz], distance s)
		2) split_edge(edge=[nA,nB]) at mid-point (split neighboring cells)
		3) split_quad(element_id) along the SHORTER diagonal into two TRIAs
		4) merge_trias(element_ids=[e1,e2]) into one QUAD
		5) create_nodes(coords=[[x1,y1,z1],[x2,y2,z2],...]) at specified coordinates
		6) create_element(node_ids=[n1,n2,n3,...]) to fill holes or gaps in the mesh
		7) delete_element(element_id) to remove floating or problematic elements

		### Rules for choosing actions:
		Use the following as preferred actions, not hard rules. You may select other actions if context (error combinations, geometry, or connectivity) suggests a different fix. In some cases, the best choice is to take no action if the deviation is acceptable.

		Single-category guidance:
		- align_middle → prefer move_node (adjust node to midsurface)
		- align_thickness → prefer move_node (adjust midsurface position), or create_nodes + create_element if geometry is missing
		- align_empty_areas → prefer create_element (fill hole with TRIA/QUAD)
		- align_empty_perimeters → prefer create_element (close perimeter gap)
		- incompatible → prefer split_quad (fix quad mismatch) or merge_trias (merge small trias into quad)
		- nodal_thickness → prefer move_node (correct node location to reflect thickness)
		- solid_middle → prefer move_node (pull nodes from inside solid to midsurface)
		- solid_boundary → prefer move_node (push nodes inward from boundary to midsurface)
		- missing_mass → prefer create_element (add coverage), or create_nodes + create_element if nodes do not exist
		- unconnected → prefer delete_element (remove floating element) or create_element (stitch with neighbors)
		
		Combination patterns to watch for:

		- align_middle + align_empty_areas → likely missing geometric feature not captured by midsurface; fix with create_nodes + create_element instead of just moving nodes.
		- align_middle + missing_mass → midsurface shifted away from feature, requires new elements to cover thickness.
		- align_empty_perimeters + unconnected → usually a perimeter gap due to broken connectivity; fix with merge_nodes before creating new elements.
		- align_thickness + nodal_thickness → often indicates property mismatch rather than geometry error; update thickness via move_node or accept as no-op.
		- incompatible + unconnected → usually poor mesh transition with connectivity gaps; prefer split_edge or remesh-type fixes.

		### General instructions:
		- Always prefer the smallest, most local fix first.
		- Consider that not all CheckMiddleMesh findings require repair — sometimes the correct action is to skip. If so, there's no need to mention this element in the plan. 
		- Use only the provided node IDs and element IDs.
		- New geometry must be created explicitly via create_nodes or create_element.
		- The required element_id field is to mention the element being act upon, or the element next to which new nodes & elements are created.
		- Do not invent IDs in actions. Make sure the suggested action make sense (e.g. if move_node is suggested for a shell, make sure the node_id is indeed from this shell).
		- Output exactly one JSON action per step — no multiple actions.
		- After each action, CheckMiddleMesh will be re-run and you will receive updated results.
		- Continue proposing repair actions until all critical issues are resolved.

		Output requirements:
		- Return ONLY valid JSON following the provided schema.
		- Each step must include a short 'why' explaining the reasoning.
	"""

    # ---------- Model with structured JSON output ----------
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=SYSTEM,
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=PLAN_SCHEMA,
        ),
    )
    return model


def check_middle_mesh():
    global current_dir

    faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
    shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")

    options = {
        "align_middle": "5%",
        "align_thickness": "5%",
        "align_empty_areas": "",
        "align_empty_perimeters": "",
        "incompatible": "50%",
        "nodal_thickness": "50%",
        "solid_middle": "5%",
        "solid_boundary": "5%",
        "missing_mass": "Loose",
    }

    ret = mesh.CheckMiddleMesh(
        shells,
        faces,
        options,
        check_for_unconnected=True,
        return_ents=True,
        min_nodal_thick=0.0,
    )

    ret_dict = {}

    for key in ret.keys():
        if key == "unconnected":
            ret_dict[key] = [ent._id for ent_list in ret[key] for ent in ent_list]
            continue

        ret_dict[key] = [ent._id for ent in ret[key]]

    with open(os.path.join(current_dir, "check_middle_mesh.json"), "w") as f:
        json.dump(ret_dict, f)

    return os.path.join(current_dir, "check_middle_mesh.json")


def repair_mesh(mesh_data: dict, mid_mesh_check: dict, max_steps: int = 2):
    global current_dir
    model = configure_agent()

    input_payload = {
        "mesh_data": mesh_data,
        "mid_mesh_check": mid_mesh_check,
    }

    prompt = (
        "Given the following middle surface mesh and result from CheckMiddleMesh, propose up to "
        f"{max_steps} step(s) to resolve the issues. "
        "Return only JSON that conforms to the schema.\n\n"
        + json.dumps(input_payload, separators=(",", ":"))
    )

    with open(os.path.join(current_dir, "repair_prompt.txt"), "w") as f:
        f.write(prompt)

    tokens = model.count_tokens(prompt)
    print(f"Input tokens: {tokens.total_tokens}")
    if tokens.total_tokens > 10000:
        warnings.warn("Input prompt is very long")
    if tokens.total_tokens > 30000:
        raise ValueError("Input prompt exceeds model context length")

    response = model.generate_content(prompt, stream=False)
    print(response.text)
    return json.loads(response.text)


def main(model_path: str = None):
    base.All()

    debug = True

    current_model = base.GetCurrentAnsaModel()

    if not current_model:
        base.Open(model_path)
        current_model = base.GetCurrentAnsaModel()

    # Parse model_path to get current directory
    model_path = (
        "D:\OneDrive - Stanford\VectraSim files\Lucid\CAD from Lucid\Reduced_Set\SPOILER_KUNSTSTOFF_LH.ansa"
        if not model_path
        else model_path
    )
    global current_dir

    current_dir = os.path.dirname(model_path)
    print(current_dir)

    # Output current middle mesh
    # base.All()
    # middle_mesh_file = base.OutputAbaqus(os.path.join(current_dir, "middle_mesh.inp"), "all")
    # inp_text_io = open(os.path.join(current_dir, "middle_mesh.inp"), "r").read()

    def parse_inp_and_combine(inp_text):
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
                    node_ids = [int(x) for x in line.split(",")[1:] if x.strip()]
                    etype = (
                        "CQUAD4"
                        if element_type
                        and element_type.startswith("S4")
                        and len(node_ids) == 4
                        else "CTRIA3"
                    )
                    elements.append({"id": eid, "type": etype, "nodes": node_ids})

        return {
            "nodes": nodes,
            "elements": elements,
        }

    # mesh_data = parse_inp_and_combine(inp_text_io)

    middle_mesh_violations_file = check_middle_mesh()

    middle_mesh_violations = {}
    with open(middle_mesh_violations_file, "r") as f:
        middle_mesh_violations = json.load(f)

    align_empty_perimeters = middle_mesh_violations["align_empty_perimeters"]

    # Identify bad shells
    problematic_cells = set()
    for key in middle_mesh_violations.keys():
        problematic_cells.update(middle_mesh_violations[key])
    current_visible = base.CollectEntities(
        DECK, None, SHELL_TYPE, True, filter_visible=True
    )
    bad_shells = [s for s in current_visible if s._id in problematic_cells]

    bad_shells_count = []

    while bad_shells:
        bad_shells_count.append(len(bad_shells))

        repair_actions = []

        shell_visited = set()
        for shell in bad_shells:
            if shell not in shell_visited:
                shell_visited.update([shell])
            else:
                continue

            bad_shells_visible, current_visible = isolate_problematic_mid_cell(
                shell, middle_mesh_violations
            )

            # Output current middle mesh
            middle_mesh_file = base.OutputAbaqus(
                os.path.join(current_dir, "middle_mesh.inp"), "visible"
            )
            inp_text_io = open(os.path.join(current_dir, "middle_mesh.inp"), "r").read()
            mesh_data = parse_inp_and_combine(inp_text_io)

            middle_mesh_violations_visible = {
                key: [
                    id
                    for id in middle_mesh_violations[key]
                    if base.GetEntity(DECK, SHELL_TYPE, id) in current_visible
                ]
                for key in middle_mesh_violations.keys()
            }

            try:
                actions = repair_mesh(
                    mesh_data, middle_mesh_violations_visible, max_steps=2
                )
                repair_actions.append(actions)

                try:
                    execute_agent_actions(actions)
                    print(f"Actions on element {shell._id} succeeded.")
                    mesh.FixQuality()
                except Exception as e:
                    print(
                        f"Error occurred while executing actions on element {shell._id}: {e}"
                    )
            except Exception as e:
                print(f"Error during repair_mesh: {e}")
                continue

        action_dict = {
            "steps": [
                repair_actions[i]["steps"]
                for i in range(len(repair_actions))
                if "steps" in repair_actions[i]
            ]
        }
        with open(os.path.join(current_dir, "repair_actions.json"), "w") as f:
            json.dump(action_dict, f, indent=2)


def execute_agent_actions(actions: dict):
    global current_dir

    # Read in json file of suggested actions:
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
        elif step["action"] == "create_nodes":
            for coord in step["coords"]:
                base.CreateEntity(
                    DECK,
                    "GRID",
                    {
                        "X1": coord[0],
                        "X2": coord[1],
                        "X3": coord[2],
                    },
                )
        elif step["action"] == "create_element":
            if len(step["node_ids"]) == 3:
                base.CreateEntity(
                    DECK,
                    SHELL_TYPE,
                    {
                        "PID": 1,  # Assuming property ID 1 exists
                        "N1": step["node_ids"][0],
                        "N2": step["node_ids"][1],
                        "N3": step["node_ids"][2],
                        "type": "CTRIA3",
                    },
                )
            elif len(step["node_ids"]) == 4:
                base.CreateEntity(
                    DECK,
                    SHELL_TYPE,
                    {
                        "PID": 1,  # Assuming property ID 1 exists
                        "N1": step["node_ids"][0],
                        "N2": step["node_ids"][1],
                        "N3": step["node_ids"][2],
                        "N4": step["node_ids"][3],
                        "type": "CQUAD4",
                    },
                )
            else:
                print(
                    f"Invalid number of nodes for create_element: {len(step['node_ids'])}"
                )
        elif step["action"] == "delete_element":
            element_to_delete = base.GetEntity(DECK, SHELL_TYPE, step["element_id"])
            base.DeleteEntities([element_to_delete])
        else:
            print(f"Unknown action: {step['action']}")


if __name__ == "__main__":
    main()
