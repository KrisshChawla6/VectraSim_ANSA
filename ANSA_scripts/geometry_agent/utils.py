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
