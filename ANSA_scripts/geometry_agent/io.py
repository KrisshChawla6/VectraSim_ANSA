#
# Scripts to load INP files quickly, extracting nodes, elements, and nodal thickness.
#
# ==========================

import numpy as np
import concurrent.futures


def parse_node_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 4:
        nid = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
        z = float(parts[3])
        return nid, (x, y, z)
    return None


def parse_elem_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 4:
        eid = int(parts[0])
        nids = [int(n) for n in parts[1:] if n]
        return eid, nids
    return None


def parse_thickness_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 2:
        nid = int(parts[0])
        thick = float(parts[1])
        return nid, thick
    return None


def load_mesh(path):
    """
    Fast parser for INP files to extract nodes and elements, with corresponding ANSA id arrays.

    Arguments:
    path -- path to the INP file

    Returns:
    vertices -- (n,3) numpy array of node coordinates
    faces -- (m,k) numpy array of element connectivity (k depends on element type)
    node_ids -- (n,) numpy array of ANSA node ids
    elem_ids -- (m,) numpy array of ANSA element ids
    thickness -- (n,) numpy array of nodal thickness values, np.nan if not present
    Parallelizes node and element parsing for large files.
    """
    node_lines = []
    elem_lines = []
    thickness_lines = []
    mode = None
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("**"):
                continue
            if line.startswith("*"):
                uline = line.upper()
                if uline.startswith("*NODE"):
                    mode = "node"
                elif uline.startswith("*ELEMENT"):
                    mode = "elem"
                elif uline.startswith("*NODAL THICKNESS"):
                    mode = "thickness"
                else:
                    mode = None
                continue
            if mode == "node":
                node_lines.append(line)
            elif mode == "elem":
                elem_lines.append(line)
            elif mode == "thickness":
                thickness_lines.append(line)

    # Parallel parse nodes
    nodes = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for result in executor.map(parse_node_line, node_lines, chunksize=10000):
            if result is not None:
                nid, xyz = result
                nodes[nid] = xyz

    # Parallel parse elements
    elems = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for result in executor.map(parse_elem_line, elem_lines, chunksize=10000):
            if result is not None:
                eid, nids = result
                elems[eid] = nids

    # Parse thickness (usually much smaller, so no need for parallel)
    nodal_thickness = {}
    for line in thickness_lines:
        result = parse_thickness_line(line)
        if result is not None:
            nid, thick = result
            nodal_thickness[nid] = thick

    node_ids = np.array(list(nodes.keys()))
    node_id_to_index = {nid: idx for idx, nid in enumerate(node_ids)}
    vertices = np.array([nodes[i] for i in node_ids])
    elem_ids = np.array(list(elems.keys()))
    faces = [[node_id_to_index[n] for n in elems[eid]] for eid in elem_ids]
    faces = np.array(faces, dtype=object)
    thickness = np.array([nodal_thickness.get(i, np.nan) for i in node_ids])
    return vertices, faces, node_ids, elem_ids, thickness


if __name__ == "__main__":
    cad_path = "C:\\Users\\HowardWu\\test.inp"
    mid_path = "C:\\Users\\HowardWu\\test_mid.inp"

    vertices_G, faces_G, node_ids_G, elem_ids_G, thickness_G = load_mesh(cad_path)
    vertices_M, faces_M, node_ids_M, elem_ids_M, thickness_M = load_mesh(mid_path)

    print(f"Loaded INP with {len(vertices_G)} vertices and {len(faces_G)} faces.")
    print(f"Loaded INP with {len(vertices_M)} vertices and {len(faces_M)} faces.")
