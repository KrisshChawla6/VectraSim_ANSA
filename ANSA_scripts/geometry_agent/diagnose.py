#
# Diagnose poor geometry representation from results produced by diff.compute_distances.
#
# ==========================

import numpy as np


def diagnose(results, tol_dist_M=1e-3, tol_dist_G=1e-3, tol_thick_rel=0.2, tol_cos=0.5):
    """
    Diagnose miscorrelations from results produced by diff.compute_distances.

    Parameters
    ----------
    results : dict
        Output of compute_distances().
    tol_dist_M : float
        Max allowed mismatch distance (mm). Larger = flagged. For identifying protruding M nodes.
    tol_dist_G : float
        Max allowed mismatch distance (mm). Larger = flagged. For identifying G nodes not being sufficiently covered by M.
    tol_thick_rel : float
        Relative tolerance on thickness mismatch, e.g. 0.2 = ±20%.
    tol_cos : float
        Normal consistency cosine threshold. Vertices with cos < tol_cos
        are considered 'side-wall snapping' and flagged.

    Returns
    -------
    issues : dict of lists
        {
          'M_nodes_far': [node_ids_M], # (k, 1) k is number of bad M nodes
          'M_nodes_far_vec_to_move': [closest_point_G], # (k, 3) vectors to move each bad M node
          'M_nodes_bad_cos': [node_ids_M],
          'M_elems_far': [elem_ids_G],   # G elems mis-hit by M nodes
          'G_nodes_far': [node_ids_G],
          'closest_node_M': [node_ids_G], # Closest M node for each G node
          'G_elems_far': [elem_ids_M],   # M elems mis-hit by G nodes
          'M_nodes_bad_thickness': [node_ids_M],
        }
    """

    # --- Unpack results
    M = results["M_to_G"]
    G = results["G_to_M"]
    T = results["thickness"]

    dMG = np.asarray(M["distance"])
    cos = np.asarray(M["cosine"])
    NidM = np.asarray(M["node_ids"])
    EhitG = np.asarray(M["closest_elem_G"])
    closest_point_G = np.asarray(M.get("closest_point_G", None))
    M_node_coords = M["M_node_coords"]
    M_node_ids = M["M_node_ids"]

    dGM = np.asarray(G["distance"])
    NidG = np.asarray(G["node_ids"])
    EhitM = np.asarray(G["closest_elem_M"])
    # New: Closest M node id for each G node
    closest_node_M = np.asarray(G.get("closest_node_M", None))

    rayhit_t = np.asarray(T["ray_hits"])
    ray_t = np.asarray(T["ray_thickness"])
    tgt_t = np.asarray(T["target_thickness"])
    NidM_th = np.asarray(T["node_ids"])

    issues = {
        "M_nodes_far": [],
        "M_nodes_far_vec_to_move": [],
        "M_nodes_bad_cos": [],
        # 'M_elems_far': [],
        "G_nodes_far": [],
        "closest_node_M": [],
        "G_elems_far": [],
        "M_nodes_bad_thickness": [],
    }

    # --- 1) M→G distance check (thickness-based)
    # For each M node, use its own thickness (from tgt_t, which is aligned with NidM_th)
    # Map NidM to index in NidM_th
    nodeid_to_idx = {nid: idx for idx, nid in enumerate(NidM_th)}
    thickness_M = np.array([tgt_t[nodeid_to_idx.get(nid, 0)] for nid in NidM])

    valid_mask = np.isfinite(dMG) & np.isfinite(thickness_M)
    bad_M = np.where(valid_mask & ((dMG - thickness_M / 2) > tol_dist_M))[0]
    M_nodes_far = NidM[bad_M].tolist()
    M_nodes_far = [
        node_id
        for node_id in M_nodes_far
        if rayhit_t[nodeid_to_idx.get(node_id, 0)] < 2
        or (rayhit_t[nodeid_to_idx.get(node_id, 0)] == 2)
        and ray_t[nodeid_to_idx.get(node_id, 0)]
        > 100 * thickness_M[nodeid_to_idx.get(node_id, 0)]
    ]
    bad_M = [np.where(NidM == node)[0][0] for node in M_nodes_far]
    issues["M_nodes_far"] = NidM[bad_M].tolist()

    # For each bad_M, get the vector from M node to its closest point on G
    if closest_point_G is not None:
        # Get the node IDs of the bad nodes
        bad_node_ids = NidM[bad_M].tolist()
        # Build a mapping from node ID to index in M_node_ids
        id_to_idx = {nid: idx for idx, nid in enumerate(M_node_ids)}
        # Find the indices in M_node_ids for each bad node ID
        bad_indices = [id_to_idx[nid] for nid in bad_node_ids]
        # Now you can index M_node_coords with bad_indices
        vecs = closest_point_G[bad_M] - M_node_coords[bad_indices]
        issues["M_nodes_far_vec_to_move"] = vecs.tolist()
    # issues['M_elems_far'] = np.unique(EhitG[bad_M]).tolist()
    # TODO Problematic: We found the M node that's far away. But we also need to find the spurious element connected to that node. The above finds an Eid for a G face which is not correct

    # --- 2) Normal consistency check
    valid_cos = np.isfinite(cos)
    bad_cos = np.where(valid_cos & (abs(cos) < tol_cos))[0]
    issues["M_nodes_bad_cos"] = NidM[bad_cos].tolist()

    # --- 3) G→M distance check (thickness-based)
    if closest_node_M is not None:
        thickness_G = np.array(
            [tgt_t[nodeid_to_idx.get(nid, 0)] for nid in closest_node_M]
        )
        valid_mask_G = np.isfinite(dGM) & np.isfinite(thickness_G)
        bad_G = np.where(valid_mask_G & ((dGM - thickness_G) > tol_dist_G))[0]
        issues["G_nodes_far"] = NidG[bad_G].tolist()
    else:
        bad_G = np.where(np.isfinite(dGM) & (dGM > tol_dist_G))[0]
        issues["G_nodes_far"] = NidG[bad_G].tolist()
    # export closest node M
    issues["closest_node_M"] = closest_node_M.tolist()
    issues["G_elems_far"] = np.array(EhitM[bad_G]).tolist()
    # TODO: Same problem here

    # --- 4) Thickness check
    valid = np.where(np.isfinite(ray_t) & np.isfinite(tgt_t) & (tgt_t > 0))[0]
    rel_err = np.abs(ray_t[valid] - tgt_t[valid]) / tgt_t[valid]
    bad_th = valid[rel_err > tol_thick_rel]
    issues["M_nodes_bad_thickness"] = NidM_th[bad_th].tolist()

    return issues
