# Imports, can be changed as needed
import os
from .io import load_mesh
from .diff import clean_mesh, triangulate
from .diff import compute_distances
from .diagnose import diagnose
import utils as geom_agent_utils

import numpy as np
import json


def run_agent(cad_path, mid_path, current_dir: str = "", **kwargs):
    """
    Run the geometry agent pipeline. 

    This pipeline imports CAD and mid-surface mesh inp files, performs mesh cleaning and triangulation, and computes geometry differences between the two meshes.

    Args:
        cad_path (str): Path to the CAD mesh file.
        mid_path (str): Path to the mid-surface mesh file.
        current_dir (str): Directory for the working ansa file.

    Returns:
        None
        (Function will export issues.json in the current_dir)
    """
    # 1. Load mesh
    Vm_orig, Fm_orig, NidM_orig, EidM_orig, ThM_orig = load_mesh(mid_path)
    Vg_orig, Fg_orig, NidG_orig, EidG_orig, ThG_orig = load_mesh(cad_path)

    # 2. Prepare mesh for compute_distances

    # Clean degenerate faces
    Vg, Fg, NidG, EidG, ThG = clean_mesh(Vg_orig, Fg_orig, NidG_orig, EidG_orig, ThG_orig)
    Vm, Fm, NidM, EidM, ThM = clean_mesh(Vm_orig, Fm_orig, NidM_orig, EidM_orig, ThM_orig)

    # Compute singular edges
    M_singular_edges = geom_agent_utils.find_singular_edges(Fm, NidM)
    
    # Triangulate
    tri_G, tri2eid_G = triangulate(Fg, EidG)
    tri_M, tri2eid_M = triangulate(Fm, EidM)

    # Filter degenerate triangles
    area_tol = kwargs.get('area_tol', 1e-10)
    tri_G, valid_G = geom_agent_utils.filter_degenerate_tris(Vg, tri_G, area_tol)
    tri2eid_G = tri2eid_G[valid_G]
    tri_M, valid_M = geom_agent_utils.filter_degenerate_tris(Vm, tri_M, area_tol)
    tri2eid_M = tri2eid_M[valid_M]

    # Remove unreferenced vertices and track removed node IDs
    Vg, tri_G, NidG, G_removed_nodes, ThG = geom_agent_utils.remove_unreferenced(Vg, tri_G, NidG, ThG)
    Vm, tri_M, NidM, M_removed_nodes, ThM = geom_agent_utils.remove_unreferenced(Vm, tri_M, NidM, ThM)

    G_removed_nodes_idx = np.where(np.isin(NidG_orig, G_removed_nodes))[0]
    M_removed_nodes_idx = np.where(np.isin(NidM_orig, M_removed_nodes))[0]

    # Delete element with removed nodes
    elem_G_w_removed_nodes = [i for i, face in enumerate(Fg_orig) if any(node_idx in face for node_idx in G_removed_nodes_idx)]
    elem_M_w_removed_nodes = [i for i, face in enumerate(Fm_orig) if any(node_idx in face for node_idx in M_removed_nodes_idx)]

    Fg = Fg[~np.isin(np.arange(Fg.shape[0]), elem_G_w_removed_nodes)]
    Fm = Fm[~np.isin(np.arange(Fm.shape[0]), elem_M_w_removed_nodes)]
    EidG = EidG[~np.isin(np.arange(EidG.shape[0]), elem_G_w_removed_nodes)]
    EidM = EidM[~np.isin(np.arange(EidM.shape[0]), elem_M_w_removed_nodes)]

    # 3. Compute distances
    normal_consistency_cos = kwargs.get('normal_consistency_cos', 0.5)
    results = compute_distances(
        vertices_G=Vg, tri_G=tri_G, node_ids_G=NidG, tri2eid_G=tri2eid_G,
        vertices_M=Vm, tri_M=tri_M, node_ids_M=NidM, tri2eid_M=tri2eid_M,
        thickness_M=ThM,
        normal_consistency_cos=normal_consistency_cos
    )

    # Add removed node info to results
    results['M_removed_nodes'] = M_removed_nodes
    results['G_removed_nodes'] = G_removed_nodes
    results['elem_G_w_removed_nodes'] = EidG_orig[elem_G_w_removed_nodes].tolist()
    results['elem_M_w_removed_nodes'] = EidM_orig[elem_M_w_removed_nodes].tolist()

    # Add node coordinates and node ids for downstream diagnose vector calculation
    results['M_to_G']['M_node_coords'] = Vm
    results['M_to_G']['M_node_ids'] = NidM
    results['G_to_M']['G_node_coords'] = Vg
    results['G_to_M']['G_node_ids'] = NidG


    # 4. Diagnose and categorize issues
    tol_dist_M = kwargs.get('tol_dist_M', 0.1)  # 0.1 mm tolerance for M->G distance
    tol_dist_G = kwargs.get('tol_dist_G', 2.0)  # 2.0 mm tolerance for G->M distance
    tol_thickness = kwargs.get('tol_thickness', 0.2)  # 0.2 relative tolerance for thickness
    issues = diagnose(results,
                  tol_dist_M=tol_dist_M,
                  tol_dist_G=tol_dist_G,
                  tol_thick_rel=tol_thickness,
                  tol_cos=normal_consistency_cos)

    # Add removed node info to issues
    issues['M_removed_nodes'] = M_removed_nodes
    issues['G_removed_nodes'] = G_removed_nodes
    issues['elem_G_w_removed_nodes'] = EidG_orig[elem_G_w_removed_nodes].tolist()
    issues['elem_M_w_removed_nodes'] = EidM_orig[elem_M_w_removed_nodes].tolist()

    print("M_nodes_far:", issues['M_nodes_far'])
    print("M_nodes_far_vec_to_move:", issues['M_nodes_far_vec_to_move'])
    print("G_nodes_far:", issues['G_nodes_far'])
    print('M_removed_nodes:', issues['M_removed_nodes'])

    # Convert M_singular_edges entries (n1, n2) to int from int32
    issues["M_singular_edges"] = [(int(n1), int(n2)) for n1, n2 in M_singular_edges]

    # Save issues to json file
    issues_filename = kwargs.get('issues_filename', 'issues.json')
    with open(os.path.join(current_dir, issues_filename), 'w') as f:
        json.dump(issues, f, indent=4)
