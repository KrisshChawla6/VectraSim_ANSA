# PYTHON script
import os
import ansa
from ansa import base, constants, mesh

def mid_surf_meshing(**kwargs):
    # Extracting kwargs
    thick = kwargs.get("thick", 1.0)
    elem_type = kwargs.get("elem_type", 3)
    join_distance = kwargs.get("join_distance", 35)
    join_distance_as_percentage = kwargs.get("join_distance_as_percentage", True)
    paste_triple_len = kwargs.get("paste_triple_len", 35)
    paste_triple_len_as_percentage = kwargs.get("paste_triple_len_as_percentage", True)
    collapse_ribs_height = kwargs.get("collapse_ribs_height", 35)
    collapse_ribs_height_as_percentage = kwargs.get("collapse_ribs_height_as_percentage", True)
    intersection_angle = kwargs.get("intersection_angle", 20)
    handle_as_single_solid = kwargs.get("handle_as_single_solid", True)
    part = kwargs.get("part", "use_current")
    ret_ents = kwargs.get("ret_ents", True)


    # Get the current deck
    current_deck = base.CurrentDeck()
    
    search_face = ("FACE",)
    all_faces = base.CollectEntities(current_deck, None, search_face, False)
    result = base.MidSurfAuto(
        thick=1.0,
        faces=all_faces,
        elem_type=3,
        join_distance=35,
        join_distance_as_percentage=True,
        paste_triple_len=35,
        paste_triple_len_as_percentage=True,
        collapse_ribs_height=35,
        collapse_ribs_height_as_percentage=True,
        intersection_angle=20,
        handle_as_single_solid=True,
        get_result_type=True,
        part="use_current",
        ret_ents=True
    )

if __name__ == '__main__':
    mid_surf_meshing()


