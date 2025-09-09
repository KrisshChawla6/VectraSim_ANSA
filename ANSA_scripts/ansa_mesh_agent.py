#
# This is v1 of the ANSA mesh agent, intended to handle the whole pipeline of:
# - Mesh creation
# - Geometry analysis & improvements (using geometry_agent). V2 as standalone agent is under geometry_llm_agent.py
# - Shell quality analysis & improvements (Not yet implemented, please refer to shell_quality_llm_agent.py)
# - File export
#
#
# This file should be made possible to run as an ANSA script
#
# ==========================

import sys

from geometry_agent.io import load_mesh

CONDA_ENV = "C:\\ProgramData\\anaconda3\\Lib\\site-packages"  # Change if necessary. To import external libraries into ANSA environment
sys.path.append(CONDA_ENV)

import os
import json
import numpy as np
from collections import defaultdict

from ansa import base, constants

# ANSA meshing scripts
from meshing_scripts import shell_meshing, mid_surf_meshing

# ANSA File I/O scripts
from geometry_agent.mesh_export.shell_mesh_export import shell_mesh_export
from geometry_agent.mesh_export.mid_mesh_export import mid_mesh_export

# Mesh analysis using external script and Abaqus exports
from geometry_agent import agent as geom_agent

# Mesh improvement using ANSA Improve module
from ansa_improve.advanced_quality_improve import advanced_quality_check

DECK = base.CurrentDeck()
SHELL_TYPE = "ELEMENT_SHELL"
SECTION_SHELL = "SECTION_SHELL"
NEIGHBOR_LEVEL = 1


def main(model_path: str = None):
    base.All()

    debug = True

    current_model = base.GetCurrentAnsaModel()

    if not current_model:
        base.Open(model_path)
        current_model = base.GetCurrentAnsaModel()

    # Parse model_path to get current directory
    print(constants.FILENAME)
    model_path = (
        "D:\OneDrive - Stanford\VectraSim files\Lucid\CAD from Lucid\Air_FTB_CAD.step.ansa"
        if not model_path
        else model_path
    )
    current_dir = os.path.dirname(model_path)

    if not debug:
        print("Debug mode is off")
    else:  # Move this to suitable line for skipping certain part of the code during debugging
        # A. Meshing
        # A1. Mesh model as shell
        shell_mesh_file = "shell_mesh.inp"
        shell_mesh_inp_path = os.path.join(current_dir, shell_mesh_file)
        if os.path.exists(shell_mesh_inp_path):
            # Check if mesh already exists
            print(
                f"Mesh file {shell_mesh_file} already exists in {current_dir}. Skipping shell meshing."
            )
        else:
            shell_mesh = shell_meshing()
            shell_mesh_inp_path = shell_mesh_export(shell_mesh_inp_path)
            base.Open(model_path)  # Re-open the original geometry

        # A2. Mesh model as mid surface
        mid_surf_mesh_filename = "mid_surf_mesh.inp"
        mid_mesh_inp_path = os.path.join(current_dir, mid_surf_mesh_filename)
        if os.path.exists(mid_mesh_inp_path):
            # Check if mesh already exists
            print(
                f"Mesh file {mid_surf_mesh_filename} already exists in {current_dir}. Skipping mid surface meshing."
            )
        else:
            mid_surf_mesh = mid_surf_meshing()
            mid_mesh_inp_path = mid_mesh_export(mid_mesh_inp_path)

        # B. Perform geometry analysis & correction
        base.All()
        current_model = base.GetCurrentAnsaModel()

        # B1. Identify and delete intersections
        intersection_elements = base.CheckIntersections(True, False, False)
        if intersection_elements:
            base.DeleteEntity(intersection_elements)
            mid_mesh_inp_path = mid_mesh_export(
                os.path.join(current_dir, mid_surf_mesh_filename)
            )

        # B2. Build trimesh model and perform analysis for geometry coverage
        geom_agent.run_agent(shell_mesh_inp_path, mid_mesh_inp_path, current_dir)

        # Read in issues.json file 1st time
        with open(os.path.join(current_dir, "issues.json"), "r") as f:
            issues = json.load(f)

        (
            M_nodes_far,
            M_nodes_far_vec_to_move,
            M_nodes_bad_cos,
            G_nodes_far,
            G_elems_far,
            M_nodes_bad_thickness,
            closest_node_M,
            M_removed_nodes,
            elem_M_w_removed_nodes,
        ) = extract_issues()

        while M_nodes_far or G_nodes_far or M_nodes_bad_thickness:
            review_issues()

            # Export corrected mid mesh for re-evaluation
            mid_mesh_inp_path = mid_mesh_export(
                os.path.join(current_dir, mid_surf_mesh_filename)
            )
            geom_agent.run_agent(shell_mesh_inp_path, mid_mesh_inp_path, current_dir)

            # Re-import issues.json
            with open(os.path.join(current_dir, "issues.json"), "r") as f:
                issues = json.load(f)

        def extract_issues():
            # Process issues as needed
            M_nodes_far = issues.get("M_nodes_far", [])
            M_nodes_far_vec_to_move = issues.get("M_nodes_far_vec_to_move", [])
            M_nodes_bad_cos = issues.get("M_nodes_bad_cos", [])
            G_nodes_far = issues.get("G_nodes_far", [])
            G_elems_far = issues.get(
                "G_elems_far", []
            )  # Caveat: G_elems_far refers to ** M elements ** that fail dG->M checks
            M_nodes_bad_thickness = issues.get("M_nodes_bad_thickness", [])
            closest_node_M = issues.get("closest_node_M", [])
            M_removed_nodes = issues.get("M_removed_nodes", [])
            elem_M_w_removed_nodes = issues.get("elem_M_w_removed_nodes", [])

            return (
                M_nodes_far,
                M_nodes_far_vec_to_move,
                M_nodes_bad_cos,
                G_nodes_far,
                G_elems_far,
                M_nodes_bad_thickness,
                closest_node_M,
                M_removed_nodes,
                elem_M_w_removed_nodes,
            )

        def review_issues():
            (
                M_nodes_far,
                M_nodes_far_vec_to_move,
                M_nodes_bad_cos,
                G_nodes_far,
                G_elems_far,
                M_nodes_bad_thickness,
                closest_node_M,
                M_removed_nodes,
                elem_M_w_removed_nodes,
            ) = extract_issues()

            # Delete elements that can be degenerate (when triangulated) from the model
            for elem in elem_M_w_removed_nodes:
                element = base.GetEntity(DECK, SHELL_TYPE, elem)
                if element:
                    base.DeleteEntity(element)

            # C. Correcting the mesh
            all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)

            # C1. Correct poor geometry coverage
            base.SetEntityVisibilityValues(DECK, {"NODE": "enable"})

            if M_nodes_far:
                for idx, node_id in enumerate(M_nodes_far):
                    print(node_id)
                    node = base.GetEntity(DECK, "NODE", node_id)
                    # Move node
                    coords = node.get_entity_values(DECK, ("X", "Y", "Z"))
                    curr_X = coords["X"]
                    curr_Y = coords["Y"]
                    curr_Z = coords["Z"]
                    vec_to_move = M_nodes_far_vec_to_move[idx]
                    new_X, new_Y, new_Z = [
                        curr_X + vec_to_move[0],
                        curr_Y + vec_to_move[1],
                        curr_Z + vec_to_move[2],
                    ]
                    base.SetEntityCardValues(
                        DECK, node, {"X": new_X, "Y": new_Y, "Z": new_Z}
                    )

            if G_nodes_far:
                # Read in CAD surface mesh
                cad_path = os.path.join(current_dir, shell_mesh_file)
                Vg_orig, Fg_orig, NidG_orig, EidG_orig, ThG_orig = load_mesh(cad_path)

                # Read in singular edges
                singular_edges = issues["M_singular_edges"]

                for idx, node_id in enumerate(G_nodes_far):
                    closest_M = closest_node_M[idx]
                    print(f"Closest M node for G node {node_id}: {closest_M}")

                    node = base.GetEntity(DECK, "NODE", closest_M)
                    elem = base.GetEntity(DECK, SHELL_TYPE, G_elems_far[idx])

                    base.Not(all_shells)
                    base.Or(entities=node)
                    base.Or(entities=elem)
                    base.Neighb("1")

                    # TODO:
                    # The following currently connects all visible singular edges to the G node in question via TRIA elements.
                    # However, given in each region there could be multiple G nodes being marked, one should use one/a few best G nodes as new nodes to create connecting elements.
                    # Or this could also require corrections that simply change the thickness of the elements
                    #
                    visib_nodes = base.CollectEntities(
                        DECK, None, "NODE", True, filter_visible=True
                    )
                    visib_nodes_ids = [n._id for n in visib_nodes]

                    print(visib_nodes_ids)

                    visib_singular_edges = []
                    for n1, n2 in singular_edges:
                        if n1 in visib_nodes_ids and n2 in visib_nodes_ids:
                            visib_singular_edges.append((n1, n2))

                    print(visib_singular_edges)

                    G_node_idx = np.where(NidG_orig == node_id)[0][0]
                    G_node_coords = Vg_orig[G_node_idx]

                    print(G_node_coords)

                    new_node = base.CreateEntity(
                        DECK,
                        "NODE",
                        {
                            "X": G_node_coords[0],
                            "Y": G_node_coords[1],
                            "Z": G_node_coords[2],
                        },
                    )

                    for n1, n2 in visib_singular_edges:
                        new_elem = base.CreateEntity(
                            DECK,
                            SHELL_TYPE,
                            {
                                "type": "TRIA",
                                "PID": elem.get_entity_values(DECK, ("EID", "PID"))[
                                    "PID"
                                ],
                                "N1": n1,
                                "N2": n2,
                                "N3": new_node._id,
                            },
                        )

                    # TODO:
                    # Need to find a way to check for poor mesh coverage.
                    # 	For the shown M submesh rerun the coverage checks?
                    # Then need a way to understand gaps and fill the holes -> agent need to understand 3D geometry
                    #
                    # if (problem still exist):
                    # 	Apply correction to M to better represent G

            base.SetEntityVisibilityValues(DECK, {"NODE": "off"})
            base.All()

        # C. Perform mesh quality analysis & correction
        base.All()
        advanced_quality_check()


if __name__ == "__main__":
    main()


def find_mesh_corners(vertices, faces, node_ids, angle_threshold_deg=120):
    """
    Find node ids at corners of a mesh based on local angle threshold.

    Arguments:
    vertices -- (n,3) numpy array of node coordinates
    faces -- (m,k) numpy array of element connectivity (indices into vertices)
    node_ids -- (n,) numpy array of ANSA node ids
    angle_threshold_deg -- angle threshold in degrees for corner detection

    Returns:
    corner_node_ids -- list of node ids at corners
    """
    node_neighbors = defaultdict(set)
    # faces contains indices into vertices (and node_ids)
    for face in faces:
        for i, ni in enumerate(face):
            for j, nj in enumerate(face):
                if j != i:
                    node_neighbors[ni].add(nj)
    corner_node_ids = []
    for idx in node_neighbors:
        p0 = vertices[idx]
        neighbors = list(node_neighbors[idx])
        if len(neighbors) < 2:
            continue
        # Compute neighbor vectors
        vectors = [vertices[n] - p0 for n in neighbors]
        # Project to best-fit plane
        # 1. Compute normal using PCA (SVD)
        vecs = np.stack(vectors)
        vecs_mean = np.mean(vecs, axis=0)
        uu, dd, vv = np.linalg.svd(vecs - vecs_mean)
        normal = vv[-1]
        # 2. Build orthonormal basis (u,v) in the plane
        u = vv[0]
        v = vv[1]
        # 3. Project vectors to plane and get 2D coordinates
        vecs_2d = np.stack([[np.dot(vec, u), np.dot(vec, v)] for vec in vectors])
        # 4. Compute angles for sorting
        angles = np.arctan2(vecs_2d[:, 1], vecs_2d[:, 0])
        order = np.argsort(angles)
        ordered_vecs = vecs_2d[order]
        # 5. Sum angles between consecutive ordered vectors
        angle_sum = 0.0
        for i in range(len(ordered_vecs)):
            v1 = ordered_vecs[i]
            v2 = ordered_vecs[(i + 1) % len(ordered_vecs)]
            norm1 = np.linalg.norm(v1)
            norm2 = np.linalg.norm(v2)
            if norm1 == 0 or norm2 == 0:
                continue
            cos_angle = np.dot(v1, v2) / (norm1 * norm2)
            cos_angle = np.clip(cos_angle, -1.0, 1.0)
            angle = np.degrees(np.arccos(cos_angle))
            angle_sum += angle
        if not round(angle_sum, 2) == 360:
            # If angle_sum is not 360 degrees, we are over-counting the largest angle twice.
            angle_sum = angle_sum / 2
        if angle_sum < 180.0:
            corner_node_ids.append(node_ids[idx])
    return corner_node_ids
