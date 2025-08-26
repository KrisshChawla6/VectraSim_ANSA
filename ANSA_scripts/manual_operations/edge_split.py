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
    
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    base.Not(all_shells)
    base.Or(bad_shells[0])
    
    edge_split()


def edge_split():
    """Split the edge between two selected nodes, reassign and create new surrounding shells with new nodes."""

    base.SetEntityVisibilityValues(DECK, {"NODE": "on"})
    nodes_0 = base.CollectEntities(DECK, None, "NODE", True, filter_visible=True)
    print(len(nodes_0))
    
    base.Neighb('1')
    shells_0 = base.CollectEntities(DECK, None, SHELL_TYPE, True, filter_visible=True)
    

    # Get node entities
    node0 = nodes_0[0]
    node0_coords = node0.get_entity_values(DECK, ("X", "Y", "Z"))
    print(f"Working on node0 with id {node0._id} and coords {node0_coords}")
    
    node1 = nodes_0[1]
    node1_coords = node1.get_entity_values(DECK, ("X", "Y", "Z"))
    print(f"Working on node1 with id {node1._id} and coords {node1_coords}")


    # Get shell entities
    shells_dict = {}
    for shell in shells_0:
        print(f"Working on shell with id {shell._id}")
        shell_id = shell._id
        shell_entities = shell.get_entity_values(DECK, ("N1", "N2", "N3", "N4"))
        
        # if len(shell_entities) == 4:
        #     print(f"Shell {shell_id} is a QUAD with nodes: {shell_entities}")

        shells_dict[shell_id] = shell_entities


    def node_is_shell_node(node, shell_entities):
        """Check if a node is part of the shell entities."""
        is_shell_node = False
        for shell_node in shell_entities.values():
            if shell_node._id == node._id:
                is_shell_node = True
                break
        return is_shell_node

    # Get relevant shells
    relevant_shells = {}
    shared_edge_shells = {}
    for id, shell_entities in shells_dict.items():
        if node_is_shell_node(node0, shell_entities) and node_is_shell_node(node1, shell_entities):
            print(f"Shell {id} contains both nodes")
            shared_edge_shells[id] = shell_entities
        elif node_is_shell_node(node0, shell_entities) or node_is_shell_node(node1, shell_entities):
            print(f"Shell {id} contains node0 or node1")
            relevant_shells[id] = shell_entities
        else:
            print(f"Shell {id} does not contain node0 or node1") 

    print(f"Relevant shells: {relevant_shells}")


    # Create a new node at the average position of node0 and node1
    new_X = (node0_coords["X"] + node1_coords["X"]) / 2
    new_Y = (node0_coords["Y"] + node1_coords["Y"]) / 2
    new_Z = (node0_coords["Z"] + node1_coords["Z"]) / 2
    print(f"New node coordinates: X={new_X}, Y={new_Y}, Z={new_Z}")

    new_node = base.CreateEntity(DECK, "NODE", {"X": new_X, "Y": new_Y, "Z": new_Z})
    print(f"Created new node with ID {new_node._id}")

    def dist(node1: base.Entity, node2: base.Entity):
        """Calculate distance between two nodes."""
        node1 = node1.get_entity_values(DECK, ("X", "Y", "Z"))
        node2 = node2.get_entity_values(DECK, ("X", "Y", "Z"))
        if not node1 or not node2:
            return float('inf')
        return ((node1["X"] - node2["X"]) ** 2 + (node1["Y"] - node2["Y"]) ** 2 + (node1["Z"] - node2["Z"]) ** 2) ** 0.5 

    # Reassign new node to shared_edge shells
    for shell_id, shell_entities in shared_edge_shells.items():
        print(f"Reassigning shell {shell_id} to new node {new_node._id}")
        curr_shell = base.GetEntity(DECK, SHELL_TYPE, shell_id)
        old_shell_vals = curr_shell.get_entity_values(DECK, ("EID", "PID", "N1", "THIC1", "N2", "THIC2", "N3", "THIC3", "N4", "THIC4"))
        node0_pos = None
        node1_pos = None
        for idx, key in enumerate(["N1", "N2", "N3", "N4"]):
            if key not in old_shell_vals:
                continue
            if old_shell_vals[key] == node0:
                node0_pos = idx + 1  # 1-based position
            if old_shell_vals[key] == node1:
                node1_pos = idx + 1
        new_thickness = (old_shell_vals[f"THIC{node0_pos}"] + old_shell_vals[f"THIC{node1_pos}"]) / 2 if node0_pos and node1_pos else None

        if len(shell_entities) == 4:
            shell_nodes = [shell_entities["N1"], shell_entities["N2"], shell_entities["N3"], shell_entities["N4"]]
            opposite_nodes = [node for node in shell_nodes if node not in (node0, node1)]
            if dist(opposite_nodes[0], node0) < dist(opposite_nodes[1], node0):
                node_oppo_0 = opposite_nodes[0]
                node_oppo_1 = opposite_nodes[1]
            else:
                node_oppo_1 = opposite_nodes[0]
                node_oppo_0 = opposite_nodes[1]

            for idx, key in enumerate(["N1", "N2", "N3", "N4"]):
                if node_oppo_0 == shell_entities[key]:
                    oppo_node_id0 = idx + 1
                    break

            opposite_thickness = old_shell_vals["THIC" + str(oppo_node_id0)]

            if dist(node_oppo_0, new_node) < dist(node_oppo_1, new_node):
                node_to_replace = node0
                node_to_replace_thickness = old_shell_vals["THIC" + str(node0_pos)]
            else:
                node_to_replace = node1
                node_to_replace_thickness = old_shell_vals["THIC" + str(node1_pos)]

            node_replaced = None
            if node_to_replace == shell_entities["N1"]:
                shell_entities["N1"] = new_node
                node_replaced = 1
            elif node_to_replace == shell_entities["N2"]:
                shell_entities["N2"] = new_node
                node_replaced = 2
            elif node_to_replace == shell_entities["N3"]:
                shell_entities["N3"] = new_node
                node_replaced = 3
            elif node_to_replace == shell_entities["N4"]:
                shell_entities["N4"] = new_node
                node_replaced = 4
            else:
                print(f"Node {node_to_replace._id} not found in shell {shell_id}")

            # Update current shell
            curr_shell.set_entity_values(DECK, shell_entities)

            # Create new shells with the new node
            new_shell, debug_report = base.CreateEntity(DECK, SHELL_TYPE, {"type": "TRIA", "PID": old_shell_vals["PID"],
                                                             "N1": node_to_replace, "THIC1": node_to_replace_thickness,
                                                             "N2": new_node, "THIC2": new_thickness if new_thickness else old_shell_vals["THIC" + str(node_replaced)],
                                                             "N3": node_oppo_0 if node_to_replace == node0 else node_oppo_1, "THIC3": opposite_thickness}, debug=ansa.constants.REPORT_ALL)
            print(debug_report)
            print(f"Created new shell with ID {new_shell._id}")

        elif len(shell_entities) == 3:
            oppo_node = [n for n in shell_entities.values() if n not in (node0, node1)][0]
            for idx, key in enumerate(["N1", "N2", "N3"]):
                if oppo_node == shell_entities[key]:
                    oppo_node_id0 = idx + 1
                    break

            opposite_thickness = old_shell_vals["THIC" + str(oppo_node_id0)]

            node_replaced = None
            if node0 == shell_entities["N1"]:
                shell_entities["N1"] = new_node
                node_replaced = 1
            elif node0 == shell_entities["N2"]:
                shell_entities["N2"] = new_node
                node_replaced = 2
            elif node0 == shell_entities["N3"]:
                shell_entities["N3"] = new_node
                node_replaced = 3
            else:
                print(f"Node {node0._id} not found in shell {shell_id}")

            # Update current shell
            curr_shell.set_entity_values(DECK, shell_entities)

            # Create new shells with the new node
            new_shell, debug_report = base.CreateEntity(DECK, SHELL_TYPE, {"type": "TRIA", "PID": old_shell_vals["PID"],
                                                             "N1": node0, "THIC1": old_shell_vals["THIC" + str(node0_pos)],
                                                             "N2": new_node, "THIC2": new_thickness if new_thickness else old_shell_vals["THIC" + str(node_replaced)],
                                                             "N3": oppo_node, "THIC3": opposite_thickness}, debug=ansa.constants.REPORT_ALL)
            print(f"Created new shell with ID {new_shell._id}")
            print(debug_report)


def get_bad_shells(shells):
    """Return a list of shells that fail the quality check."""
    return [shell for shell in shells if base.CalculateOffElements(shell)['TOTAL OFF'] != 0]


if __name__ == '__main__':
    main()


