# PYTHON script
import sys

CONDA_ENV = 'C:\\ProgramData\\anaconda3\\Lib\\site-packages'
sys.path.append(CONDA_ENV)

import PIL
import trimesh

import os
import ansa
import json
import numpy as np

from ansa import base, constants, mesh

# ANSA file I/O scripts
from ansa_mesh_agent.io import load_mesh


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
    from collections import defaultdict
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
        angles = np.arctan2(vecs_2d[:,1], vecs_2d[:,0])
        order = np.argsort(angles)
        ordered_vecs = vecs_2d[order]
        # 5. Sum angles between consecutive ordered vectors
        angle_sum = 0.0
        for i in range(len(ordered_vecs)):
            v1 = ordered_vecs[i]
            v2 = ordered_vecs[(i+1)%len(ordered_vecs)]
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


def main():
    base.All()

    current_model = base.GetCurrentAnsaModel()

    if not current_model:
        base.Open(model_path)
        current_model = base.GetCurrentAnsaModel()

    # Parse model_path to get current directory
    # model_path = "D:\OneDrive - Stanford\VectraSim files\Lucid\CAD from Lucid\Air_FTB_CAD.step.ansa"
    # current_dir = os.path.dirname(model_path)
    # cad_path = os.path.join(current_dir, "shell_mesh.inp")
    # mid_path = os.path.join(current_dir, "mid_surf_mesh.inp")
    cad_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\Air_FTB_CAD_G_mesh.inp"
    mid_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\Air_FTB_CAD_M_mesh_no_intersection.inp"

    Vg, Fg, NidG, EidG, ThG = load_mesh(cad_path)
    Vm, Fm, NidM, EidM, ThM = load_mesh(mid_path)

    


    # Import json file of issues
    with open("D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\issues.json", "r") as f:
        issues = json.load(f)

    M_nodes_far = issues["M_nodes_far"]
    G_nodes_far = issues["G_nodes_far"]
    M_nodes_bad_thickness = issues["M_nodes_bad_thickness"]

    base.All()
    

    # 1. Correct meshes with spurious M nodes

    # 2. Correct meshes with spurious G nodes
    
    # Find corners in the mid-surface mesh (Vm, Fm, NidM)
    mid_corners = find_mesh_corners(Vm, Fm, NidM, angle_threshold_deg=120)
    print("Mid-surface mesh corner node ids:", mid_corners)

    if len(G_nodes_far) > 0:
        # Find indices of G_nodes_far in NidG
        G_indices = [np.where(NidG == nid)[0][0] for nid in G_nodes_far]

        # Get coordinates of G_nodes_far nodes
        G_coords = Vg[G_indices]

        # For Z=0 and Z=1
        furthest_nodes = {}
        for z_val in [0, 1]:
            # Indices where Z matches
            z_mask = np.isclose(G_coords[:, 2], z_val)
            if not np.any(z_mask):
                furthest_nodes[z_val] = None
                continue
            G_z_coords = G_coords[z_mask]
            G_z_indices = np.array(G_indices)[z_mask]
            # For each candidate, compute min distance to Vm nodes
            dists = np.linalg.norm(G_z_coords[:, None, :] - Vm[None, :, :], axis=2)
            min_dists = dists.min(axis=1)
            # Find the index of the node with the largest min distance
            furthest_idx = np.argmax(min_dists)
            furthest_node_id = NidG[G_z_indices[furthest_idx]]
            furthest_nodes[z_val] = {"id": furthest_node_id, "coords": G_z_coords[furthest_idx]}

        print("Furthest G_nodes_far node with Z=0:", furthest_nodes[0]["id"])
        print("Furthest G_nodes_far node with Z=1:", furthest_nodes[1]["id"])

        # Now furthest node on the upper and lower surfaces are found, create a new node that's the middle point
        new_node = base.CreateEntity(
            base.CurrentDeck(),
            "NODE",
            {
                "X": 0.5 * (furthest_nodes[0]["coords"][0] + furthest_nodes[1]["coords"][0]),
                "Y": 0.5 * (furthest_nodes[0]["coords"][1] + furthest_nodes[1]["coords"][1]),
                "Z": 0.5 * (furthest_nodes[0]["coords"][2] + furthest_nodes[1]["coords"][2]),
            },
        )

        # Find the closest corners to the new point, to create the new element
        # Coordinates of the new node
        new_node_coords = np.array([
            0.5 * (furthest_nodes[0]["coords"][0] + furthest_nodes[1]["coords"][0]),
            0.5 * (furthest_nodes[0]["coords"][1] + furthest_nodes[1]["coords"][1]),
            0.5 * (furthest_nodes[0]["coords"][2] + furthest_nodes[1]["coords"][2]),
        ])

        # Compute distances from all Vm nodes to the new node
        dists_to_new = np.linalg.norm(Vm - new_node_coords, axis=1)
        corner_indices = [np.where(NidM == nid)[0][0] for nid in mid_corners]
        dists_to_new = dists_to_new[corner_indices]

        # Find the index/indices of the closest node(s)
        closest_indices = np.argsort(dists_to_new)  # sorted indices, closest first
        # For just the single closest node:
        closest_index = np.argmin(dists_to_new)

        print("Indices of closest nodes in Vm:", closest_indices[:2])  # e.g., first 2 closest
        
        shell1 = base.CollectEntities(base.CurrentDeck(), None, "ELEMENT_SHELL")[0]

        # Create a new element connecting the new node to the closest corner nodes
        new_shell = base.CreateEntity(
            base.CurrentDeck(),
            "ELEMENT_SHELL",
            {
                "type": "TRIA", 
                "PID": shell1.get_entity_values(base.CurrentDeck(), ("EID", "PID"))["PID"],
                "N1": mid_corners[closest_indices[0]],
                "N2": mid_corners[closest_indices[1]],
                "N3": new_node._id,
            }
        )
        

    # 3. Correct meshes with bad M node thickness


if __name__ == "__main__":
    main()
