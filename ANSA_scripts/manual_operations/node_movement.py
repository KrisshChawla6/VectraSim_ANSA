# PYTHON script
import os
import ansa

from ansa import base, mesh

DECK = base.CurrentDeck()
SHELL_TYPE = "ELEMENT_SHELL"
SHELL_SECTION = "SECTION_SHELL"
TEMP_PROP_NAME = "TMP_POOR_SHELL"

def main():
    # Get current deck
    current_deck = base.CurrentDeck()
    print(current_deck)
    
    parts = base.CollectEntities(DECK, None, "ANSAPART")
    if not parts:
        print("No parts found.")
        return
    print(f"Working on part: {parts[0]._name}")

    shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    if not shells:
        print("No shell elements found.")
        return
    
    bad_shells = get_bad_shells(shells)
    print(bad_shells[0])
    
    
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    base.Not(all_shells)
    base.Or(bad_shells[0])
    
    base.SetEntityVisibilityValues(DECK, {"NODE": "on"})
    nodes_0 = base.CollectEntities(DECK, None, "NODE", True, filter_visible=True)
    print(len(nodes_0))
    
    base.Neighb('1')

    node_movement(nodes_0[0], {"Z": 30})
    
def node_movement(node: base.Entity, new_coords: dict):
    node0 = node
    print(f"Working on node with id {node0._id}")
    print(node0.get_entity_values(DECK, ("X", "Y", "Z")))
    # We can directly set node coords to move them
    node0.set_entity_values(DECK, new_coords)
    print(node0.get_entity_values(DECK, ("X", "Y", "Z")))


def get_bad_shells(shells):
    """Return a list of shells that fail the quality check."""
    return [shell for shell in shells if base.CalculateOffElements(shell)['TOTAL OFF'] != 0]

if __name__ == '__main__':
    main()


