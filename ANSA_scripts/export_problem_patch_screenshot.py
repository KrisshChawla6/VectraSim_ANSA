# 
# This file generates screenshots of isolated problematic mid-mesh cells for geometry clean up.
# 
# ========================================================================

import os
import ansa


import json
from ansa import base, constants, mesh, utils

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

VIEW_ANGLE_FKEY = ["F1", "F2", "F3", "F4", "F5", "F6"]


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


def main():
    # Parse model_path to get current directory
    model_path = "D:\OneDrive - Stanford\VectraSim files\Lucid\CAD from Lucid\Reduced_Set\SPOILER_KUNSTSTOFF_LH.ansa"
    global current_dir

    current_dir = os.path.dirname(model_path)
    print(current_dir)

    # Identify bad shells
    middle_mesh_violations_file = check_middle_mesh()

    base.All()
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)

    middle_mesh_violations = {}
    with open(middle_mesh_violations_file, "r") as f:
        middle_mesh_violations = json.load(f)

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

        shell_visited = set()
        for shell in bad_shells:
            if shell not in shell_visited:
                shell_visited.update([shell])
            else:
                continue

            bad_shells_visible, current_visible = isolate_problematic_mid_cell(
                shell, middle_mesh_violations
            )

            base.ZoomAll()

            for fkey in VIEW_ANGLE_FKEY:
                # Set view angles
                base.SetViewAngles(f_key=fkey)

                # Show bad shell patch
                base.Not(all_shells)
                base.Or(entities=current_visible)
                utils.SnapShot(os.path.join(current_dir, f"isolated_bad_shells_{fkey}_MESH.png"), "PNG")

                # Show geometry
                base.SetEntityVisibilityValues(DECK, {"FACE": "on"})
                base.All()
                utils.SnapShot(os.path.join(current_dir, f"isolated_bad_shells_{fkey}_GEOM.png"), "PNG")
                base.SetEntityVisibilityValues(DECK, {"FACE": "off"})

            print(
                f"Isolated {len(bad_shells_visible)} bad shells out of {len(current_visible)} visible shells"
            )



if __name__ == "__main__":
    main()
