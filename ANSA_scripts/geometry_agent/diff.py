import trimesh
import numpy as np


def is_degenerate_face(vertices, face, area_tol=1e-12):
    """
    Returns True if the face is degenerate (zero area or collinear).
    """
    idx = [v for v in face if v >= 0]
    if len(idx) < 3:
        return True
    pts = vertices[idx]
    if len(idx) == 3:
        # Triangle: check area
        v1 = pts[1] - pts[0]
        v2 = pts[2] - pts[0]
        area = 0.5 * np.linalg.norm(np.cross(v1, v2))
        return area < area_tol
    elif len(idx) == 4:
        # Quad: check both triangles for area
        v0, v1, v2, v3 = pts
        area1 = 0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0))
        area2 = 0.5 * np.linalg.norm(np.cross(v2 - v0, v3 - v0))
        return (area1 < area_tol) or (area2 < area_tol)
    else:
        # Ngon: fan triangulation, check all triangles
        v0 = pts[0]
        for i in range(1, len(idx) - 1):
            vi = pts[i]
            vj = pts[i + 1]
            area = 0.5 * np.linalg.norm(np.cross(vi - v0, vj - v0))
            if area < area_tol:
                return True
        return False


def clean_mesh(vertices, faces, node_ids, elem_ids, Th):
    """
    Remove vertices with NaN/inf and degenerate faces (faces with <3 unique vertices or near-zero area).
    Returns cleaned vertices, faces, node_ids, and a mapping from old to new vertex indices.
    """
    vertices = np.asarray(vertices)
    faces = np.asarray(faces)
    node_ids = np.asarray(node_ids)
    elem_ids = np.asarray(elem_ids)
    Th = np.asarray(Th)
    # Remove degenerate faces (collinear or near-zero area)
    cleaned_faces = []
    cleaned_elem_ids = []
    for i, face in enumerate(faces):
        unique = []
        seen = set()
        for v in face:
            if v >= 0 and v not in seen:
                unique.append(v)
                seen.add(v)
        if len(unique) >= 3 and not is_degenerate_face(vertices, unique):
            cleaned_faces.append(unique)
            cleaned_elem_ids.append(elem_ids[i])
    faces = np.array(cleaned_faces, dtype=object)
    elem_ids = np.array(cleaned_elem_ids)
    # Add this check:
    for i, face in enumerate(faces):
        if len(face) < 3 or any(v < 0 for v in face) or len(set(face)) < 3:
            raise ValueError(f"Invalid face at index {i}: {face}")
    return vertices, faces, node_ids, elem_ids, Th


def deduplicate_vertices(vertices, faces, node_ids):
    """
    Deduplicate vertices (same xyz), update faces and node_ids.
    Keeps the first ANSA node ID for each unique vertex.
    Returns:
        new_vertices: (n_unique, 3)
        new_faces: (m, k)
        new_node_ids: (n_unique,)
        old_to_new: (n_old,) mapping from old vertex index to new vertex index
    """
    vertices = np.asarray(vertices)
    node_ids = np.asarray(node_ids)
    uniq, idx, inv = np.unique(vertices, axis=0, return_index=True, return_inverse=True)
    new_vertices = uniq
    new_faces = np.array([[inv[v] for v in face] for face in faces], dtype=faces.dtype)
    new_node_ids = node_ids[idx]
    return new_vertices, new_faces, new_node_ids, inv


def triangulate(faces, elem_ids):
    """
    Triangulate faces (tris/quads/ngons) and return:
      tri_faces: (T,3) int indices into the same vertex array
      tri_to_elem_id: (T,) ANSA element id for each triangle
      face_to_tri_range: optional (not used here), could map original face->triangle span
    """
    # faces: list/array of variable-length lists (mixed tris, quads, ngons)
    tri_list = []
    id_list = []
    for eid, poly in zip(elem_ids, faces):
        poly = np.asarray(poly)
        n = len(poly)
        if n == 3:
            tri_list.append([poly[0], poly[1], poly[2]])
            id_list.append(eid)
        elif n == 4:
            # consistent split: (0,1,2) and (0,2,3)
            tri_list.append([poly[0], poly[1], poly[2]])
            id_list.append(eid)
            tri_list.append([poly[0], poly[2], poly[3]])
            id_list.append(eid)
        elif n > 4:
            # fan triangulation for ngons
            for i in range(1, n - 1):
                tri_list.append([poly[0], poly[i], poly[i + 1]])
                id_list.append(eid)
        # ignore faces with <3 nodes (should not happen after cleaning)
    tri_faces = np.asarray(tri_list, dtype=int)
    tri_to_elem_id = np.asarray(id_list, dtype=np.int64)
    return tri_faces, tri_to_elem_id


def compute_distances(vertices_G, tri_G, node_ids_G, tri2eid_G,
                     vertices_M, tri_M, node_ids_M, tri2eid_M,
                     thickness_M=None,
                     normal_consistency_cos=0.0):
    """
    Compute:
      - d(M→G) coverage distances (per M vertex) + nearest G element ID
      - d(G→M) coverage distances (per G vertex) + nearest M element ID
      - thickness rays (per M vertex): ±normal intersections → geometric thickness

    Inputs
    ------
    vertices_G : (nG,3)
    tri_G      : (Tg,3) triangle indices into vertices_G
    node_ids_G : (nG,)
    tri2eid_G  : (Tg,)
    vertices_M : (nM,3)
    tri_M      : (Tm,3)
    node_ids_M : (nM,)
    tri2eid_M  : (Tm,)
    thickness_M: (nM,) or None
    normal_consistency_cos: float in [ -1..1 ], e.g. 0.5 (=~60°).
        If >0, we’ll compute cos between M vertex normal and the normal of the
        closest G triangle; downstream can use it to ignore side-wall snaps.

    Returns
    -------
    results : dict
        {
          'M_to_G': {
             'distance': (nM,),                # d(M→G)
             'closest_elem_G': (nM,),          # ANSA elem IDs on G (via tri→elem remap)
             'closest_point_G': (nM,3),        # closest point on G for each M node
             'cosine': (nM,),                  # optional normal consistency (NaN if not computed)
             'node_ids': (nM,),                # ANSA node IDs (M)
          },
          'G_to_M': {
             'distance': (nG,),                # d(G→M)
             'closest_elem_M': (nG,),          # ANSA elem IDs on M (via tri→elem remap)
             'closest_node_M': (nG,),          # ANSA node IDs of closest M vertex for each G node
             'node_ids': (nG,),                # ANSA node IDs (G)
          },
          'thickness': {
             'ray_hits': (nM,),                # 0,1,2 (hits along +n and -n)
             'ray_thickness': (nM,),           # measured thickness (NaN if <2 hits)
             'target_thickness': (nM,),        # passthrough of thickness_M
             'node_ids': (nM,),                # ANSA node IDs (M) 
          },
          'meta': {
             'tri_to_elem_G': (Tg,),           # for debugging/traceability
             'tri_to_elem_M': (Tm,),
          }
        }
    """

    # --- 1) Build trimesh objects on triangulated faces
    mesh_G = trimesh.Trimesh(vertices=vertices_G, faces=tri_G, process=False)
    mesh_M = trimesh.Trimesh(vertices=vertices_M, faces=tri_M, process=False)

    nM = vertices_M.shape[0]
    nG = vertices_G.shape[0]

    # --- 2) d(M→G): closest point on G for each M vertex
    closest_pts_G_for_M, d_MG, tri_id_G_for_M = trimesh.proximity.closest_point(mesh_G, vertices_M)
    # Map triangle id -> ANSA elem id
    closest_elem_G_for_M = tri2eid_G[tri_id_G_for_M]

    # (optional) normal consistency: cos between M vertex normal and that G triangle normal
    cosine = np.full(nM, np.nan, dtype=float)
    if normal_consistency_cos is not None:
        vnormals_M = mesh_M.vertex_normals  # based on triangles
        # face normals on G:
        fnormals_G = mesh_G.face_normals
        g_normals_hit = fnormals_G[tri_id_G_for_M]
        # normalize to be safe
        a = vnormals_M / np.linalg.norm(vnormals_M, axis=1, keepdims=True)
        b = g_normals_hit / np.linalg.norm(g_normals_hit, axis=1, keepdims=True)
        cosine = np.einsum('ij,ij->i', a, b).clip(-1.0, 1.0)

    # --- 3) d(G→M): closest point on M for each G vertex
    _, d_GM, tri_id_M_for_G = trimesh.proximity.closest_point(mesh_M, vertices_G)
    closest_elem_M_for_G = tri2eid_M[tri_id_M_for_G]

    # For each G node, find the closest M vertex of the closest M element (from the triangle hit)
    # tri_M: (Tm, 3) indices into vertices_M
    # node_ids_M: (nM,)
    closest_tri_M = tri_M[tri_id_M_for_G]  # (nG, 3)
    # For each G node, find which of the 3 vertices of the triangle is closest to the G node
    closest_M_vertex_idx = np.empty(len(vertices_G), dtype=int)
    for i, v in enumerate(vertices_G):
        tri_verts = vertices_M[closest_tri_M[i]]  # shape (3, 3)
        dists = np.linalg.norm(tri_verts - v, axis=1)
        min_idx = np.argmin(dists)
        closest_M_vertex_idx[i] = closest_tri_M[i][min_idx]
    closest_M_node_id_for_G = node_ids_M[closest_M_vertex_idx]

    # --- 4) Thickness via ± normal rays from M vertices
    ray_hits = np.zeros(nM, dtype=int)
    ray_thickness = np.full(nM, np.nan, dtype=float)

    # We can compute rays even if thickness_M is None (still useful)
    vnormals_M = mesh_M.vertex_normals
    norms = np.linalg.norm(vnormals_M, axis=1)
    if np.any(norms == 0):
        bad_idx = np.where(norms == 0)[0]
        print(f"Zero-length normals at M vertex indices: {bad_idx}")
        raise ValueError(f"Zero-length normals at M vertex indices: {mesh_M.vertices[bad_idx]}")
    
    origins = vertices_M
    # Build 2*nM rays
    dirs = np.vstack([vnormals_M, -vnormals_M])       # (2nM,3)
    origins2 = np.vstack([origins, origins])          # (2nM,3)

    # Before ray intersection
    if not np.all(np.isfinite(mesh_G.vertices)):
        bad_idx = np.where(~np.isfinite(mesh_G.vertices).any(axis=1))[0]
        print(f"Non-finite vertices in mesh_G at indices: {bad_idx}")
        raise ValueError(f"Non-finite vertices in mesh_G at indices: {bad_idx}")

    if not np.all(np.isfinite(mesh_G.faces)):
        bad_idx = np.where(~np.isfinite(mesh_G.faces).any(axis=1))[0]
        print(f"Non-finite faces in mesh_G at indices: {bad_idx}")
        raise ValueError(f"Non-finite faces in mesh_G at indices: {bad_idx}")

    # Check for degenerate faces (min > max)
    for i, face in enumerate(mesh_G.faces):
        verts = mesh_G.vertices[face]
        mins = verts.min(axis=0)
        maxs = verts.max(axis=0)
        if np.any(mins > maxs):
            print(f"Degenerate face at index {i}: {face}, mins: {mins}, maxs: {maxs}")
            raise ValueError(f"Degenerate face at index {i}: {face}")

    locs, ray_idx, tri_idx = mesh_G.ray.intersects_location(
        ray_origins=origins2,
        ray_directions=dirs,
        multiple_hits=True
    )
    # Efficiently compute nearest-hit distance per ray
    # For each ray r, find min ||hit - origin[r]||
    # First, compute distances for all hits:
    dists_hits = np.linalg.norm(locs - origins2[ray_idx], axis=1)
    # We want the nearest hit per ray: argmin among hits with same ray_idx
    # Get sorting by (ray_idx, distance)
    order = np.lexsort((dists_hits, ray_idx))
    ray_idx_sorted = ray_idx[order]
    dists_sorted = dists_hits[order]
    locs_sorted = locs[order]

    # Keep first occurrence per ray (nearest)
    first_of_ray = np.ones_like(ray_idx_sorted, dtype=bool)
    first_of_ray[1:] = ray_idx_sorted[1:] != ray_idx_sorted[:-1]

    nearest_ray = ray_idx_sorted[first_of_ray]
    nearest_loc = locs_sorted[first_of_ray]

    # Split into + and - rays
    nR = nM
    plus_mask = nearest_ray < nR
    minus_mask = ~plus_mask
    # Initialize arrays for nearest hit points per node
    plus_hit = np.full((nM, 3), np.nan, dtype=float)
    minus_hit = np.full((nM, 3), np.nan, dtype=float)

    # Fill from nearest hits
    plus_ray_ids = nearest_ray[plus_mask]                      # in [0, nM-1]
    plus_hit[plus_ray_ids] = nearest_loc[plus_mask]

    minus_ray_ids = nearest_ray[minus_mask] - nR               # map [nM..2nM-1] -> [0..nM-1]
    minus_hit[minus_ray_ids] = nearest_loc[minus_mask]

    # Count hits per node
    has_plus = ~np.isnan(plus_hit[:, 0])
    has_minus = ~np.isnan(minus_hit[:, 0])
    ray_hits = has_plus.astype(int) + has_minus.astype(int)

    both = has_plus & has_minus
    if np.any(both):
        diff = plus_hit[both] - minus_hit[both]
        ray_thickness[both] = np.linalg.norm(diff, axis=1)

    # --- 5) Package results (arrays + ANSA IDs kept alongside)
    results = {
        'M_to_G': {
            'distance': d_MG,                        # per M vertex
            'closest_elem_G': closest_elem_G_for_M,  # ANSA element IDs on G
            'closest_point_G': closest_pts_G_for_M,  # (nM, 3) closest point on G for each M node
            'cosine': cosine,
            'node_ids': np.asarray(node_ids_M, dtype=np.int64),
        },
        'G_to_M': {
            'distance': d_GM,                        # per G vertex
            'closest_elem_M': closest_elem_M_for_G,  # ANSA element IDs on M
            'closest_node_M': closest_M_node_id_for_G, # ANSA node ID of closest M vertex
            'node_ids': np.asarray(node_ids_G, dtype=np.int64),
        },
        'thickness': {
            'ray_hits': ray_hits,                                # 0/1/2
            'ray_thickness': ray_thickness,                      # NaN if <2 hits
            'target_thickness': (np.asarray(thickness_M)
                                 if thickness_M is not None else
                                 np.full(nM, np.nan, dtype=float)),
            'node_ids': np.asarray(node_ids_M, dtype=np.int64),
        },
        'meta': {
            'tri_to_elem_G': tri2eid_G,   # for debugging/traceability
            'tri_to_elem_M': tri2eid_M,
        }
    }
    return results
