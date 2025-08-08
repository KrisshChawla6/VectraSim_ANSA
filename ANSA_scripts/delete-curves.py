# PYTHON script
import os
import ansa
from ansa import base, constants, mesh

def main():
    # Need some documentation? Run this with F5

    help_html = os.path.join(ansa.constants.app_root_dir.replace('/', os.path.sep), '..', 'ansa_v23.1.2', 'docs', 'extending', 'python_api', 'html', 'index.html')
    print('Documentation HTML: '+ help_html)

    # Get the current deck
    current_deck = base.CurrentDeck()
    print("Current deck:", current_deck)

    # Get the current working part (visible module)
    model = 0
    part = base.CollectEntities(current_deck, None, 'ANSAPART')

    # Call the deletion function
    delete_useless_curves(part)

    # Incorrect
    # mesh.CreateBestMesh()

def delete_useless_curves(part):
    current_deck = base.CurrentDeck()
    
    # Get all curves in the given part
    curves = base.CollectEntities(current_deck, part, 'CURVE')
    
    if not curves:
        print("No curves found.")
        return
        
    # Delete curves
    base.DeleteCurves(curves)
    print(f"Deleted {len(curves)} curves.")
        
if __name__ == '__main__':
    main()


