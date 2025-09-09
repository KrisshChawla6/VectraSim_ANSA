import numpy as np
from collections import defaultdict


def filter_degenerate_tris(vertices, tri_faces, area_tol=1e-10):
    """
    Remove degenerate triangles (zero area or collinear).
    Returns filtered tri_faces and a mask of valid triangles.
    """
    valid = []
    for i, face in enumerate(tri_faces):
        pts = vertices[face]
        v1 = pts[1] - pts[0]
        v2 = pts[2] - pts[0]
        area = 0.5 * np.linalg.norm(np.cross(v1, v2))
        if area >= area_tol:
            valid.append(i)
    valid = np.array(valid, dtype=int)
    return tri_faces[valid], valid


def find_singular_edges(faces, node_ids):
    """
    Find singular (boundary) edges in a mesh.
    Returns a list of (nid1, nid2) tuples, where nid1 < nid2.
    """
    edge_count = defaultdict(int)
    # faces: (m, k) array of indices into node_ids (can be variable length)
    for face in faces:
        # For each face, get all unique edge pairs
        n = len(face)
        for i in range(n):
            a = node_ids[face[i]]
            b = node_ids[face[(i + 1) % n]]
            edge = tuple(sorted((a, b)))
            edge_count[edge] += 1
    # Singular edges: those that appear only once
    singular_edges = [edge for edge, count in edge_count.items() if count == 1]
    return singular_edges


def remove_unreferenced(vertices, tri_faces, node_ids, thickness):
    used = np.unique(tri_faces.flatten())
    all_idx = np.arange(vertices.shape[0])
    removed_idx = np.setdiff1d(all_idx, used)
    removed_node_ids = node_ids[removed_idx].tolist()
    old_to_new = -np.ones(vertices.shape[0], dtype=int)
    old_to_new[used] = np.arange(len(used))
    new_vertices = vertices[used]
    new_thickness = thickness[used]
    new_node_ids = node_ids[used]
    new_tri_faces = np.array(
        [[old_to_new[v] for v in tri] for tri in tri_faces], dtype=int
    )
    return new_vertices, new_tri_faces, new_node_ids, removed_node_ids, new_thickness


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
