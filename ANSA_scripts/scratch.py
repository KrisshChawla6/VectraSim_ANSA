# PYTHON script
import os
import ansa
from ansa import base, constants, mesh

def main():
    # Need some documentation? Run this with F5

    help_html = os.path.join(ansa.constants.app_root_dir.replace('/', os.path.sep), '..', 'ansa_v23.1.2', 'docs', 'extending', 'python_api', 'html', 'index.html')
    print('Documentation HTML: '+ help_html)

    # Create a temporary property to isolate the bad elements
    current_deck = base.CurrentDeck()
    print(current_deck)
    
    results_list = []

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
        property="id=5",
        ret_ents=True
    )

    print(result.ents)


if __name__ == '__main__':
    main()


