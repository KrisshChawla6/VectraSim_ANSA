import numpy as np
from scipy.spatial import cKDTree

def build_kdtree(vertices):
    return cKDTree(vertices)

def closest_points(src_vertices, tgt_vertices, tgt_faces, kdtree):
    """
    For each src vertex, find closest point on tgt mesh.
    For skeleton: nearest vertex only. (Later: barycentric projection).
    """
    d, idx = kdtree.query(src_vertices)
    return d, idx
