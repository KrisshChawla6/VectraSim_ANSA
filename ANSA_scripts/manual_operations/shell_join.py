# PYTHON script
import ansa

from ansa import base, guitk

DECK = base.CurrentDeck()
SHELL_TYPE = "SHELL"
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
    # base.Not(all_shells)
    # base.Or(bad_shells[0])
    # base.Neighb("1")

    shell_ids = {"shell0_id": None, "shell1_id": None}

    def get_input(data, le0, le1, shell_ids):
        shell_ids = guitk.BCGetUserDataKey(data, "shell_ids")
        shell_ids["shell0_id"] = guitk.BCLineEditGetText(le0)
        shell_ids["shell1_id"] = guitk.BCLineEditGetText(le1)
        guitk.BCSetUserDataKey(data, "shell_ids", shell_ids)

    w = guitk.BCWindowCreate("Simple BCWindow", guitk.constants.BCOnExitHide)
    le0 = guitk.BCLineEditCreate(w, "Shell 0 ID")
    le1 = guitk.BCLineEditCreate(w, "Shell 1 ID")
    guitk.BCPushButtonCreate(w, "Confirm", None)
    guitk.BCShow(w)

    shell_ids["shell0_id"] = int(guitk.BCLineEditGetText(le0))
    shell_ids["shell1_id"] = int(guitk.BCLineEditGetText(le1))

    # shell_ids["shell0_id"] = 157
    # shell_ids["shell1_id"] = 158

    print(f"Selected shells: {shell_ids['shell0_id']}, {shell_ids['shell1_id']}")

    shell0 = base.GetEntity(DECK, SHELL_TYPE, shell_ids["shell0_id"])
    shell1 = base.GetEntity(DECK, SHELL_TYPE, shell_ids["shell1_id"])

    shell_join(shell0, shell1)


def shell_join(shell1: base.Entity, shell2: base.Entity):
    """Join two neighboring shells into one shell, removing the common edge and node."""

    shell1_nodes = shell1.get_entity_values(DECK, ("G1", "G2", "G3", "G4"))
    shell2_nodes = shell2.get_entity_values(DECK, ("G1", "G2", "G3", "G4"))
    if len(shell1_nodes) == 4:
        print(
            f"Error: Shell {shell1._id} is a QUAD. Please select two TRIA shells to join."
        )
        return
    if len(shell2_nodes) == 4:
        print(
            f"Error: Shell {shell2._id} is a QUAD. Please select two TRIA shells to join."
        )
        return

    shell1_id = shell1._id
    shell2_id = shell2._id
    print(f"Working on shells with id {shell1_id} and {shell2_id}")

    def get_shell_and_node_info(shell: base.Entity) -> dict:
        """Get shell nodes and thickness info.

        Args:
            shell (base.Entity): The shell entity.

        Returns:
            dict: Dictionary of shell nodes, thicknesses, and coordinates of each node entity.
        """

        shell_entities = shell.get_entity_values(DECK, ("G1", "G2", "G3", "G4"))
        shell_thickness = shell.get_entity_values(DECK, ("T1", "T2", "T3", "T4"))

        shell_entities_dict = dict()

        for node_key, node_entity in shell_entities.items():
            if node_entity is None:
                shell_entities.pop(node_key)
            else:
                node_dict = {
                    "entity": node_entity,
                    "thickness": shell_thickness[f"T{node_key.strip('G')}"],
                }
                node_entities = node_entity.get_entity_values(DECK, ("X1", "X2", "X3"))
                node_dict.update(node_entities)

            shell_entities_dict[node_entity] = node_dict

        return shell_entities_dict

    shell1_info = get_shell_and_node_info(shell1)
    shell2_info = get_shell_and_node_info(shell2)

    shell1_entities = shell1.get_entity_values(DECK, ("G1", "G2", "G3"))
    shell1_thickness = shell1.get_entity_values(DECK, ("T1", "T2", "T3"))
    shell2_entities = shell2.get_entity_values(DECK, ("G1", "G2", "G3"))
    shell2_thickness = shell2.get_entity_values(DECK, ("T1", "T2", "T3"))

    # Find common nodes
    common_nodes = []
    common_nodes_dict = {}
    for key1, node1 in shell1_entities.items():
        for key2, node2 in shell2_entities.items():
            if node1._id == node2._id:
                common_node = {
                    "node_entity": node1,
                    "thickness": shell1_info[node1]["thickness"],
                }
                common_nodes.append(node1)
                common_nodes_dict[node1] = common_node
                print(f"Common node found: {node1._id}")

    if len(common_nodes) != 2:
        print("Error: Shells do not share exactly two common nodes.")
        return

    # Identify unique nodes
    unique_nodes = [
        node for node in shell1_entities.values() if node not in common_nodes
    ] + [node for node in shell2_entities.values() if node not in common_nodes]

    if len(unique_nodes) != 2:
        print("Error: Unable to identify unique nodes.")
        return

    # Create new shell entity (assuming a quad)
    new_shell, debug_report = base.CreateEntity(
        DECK,
        SHELL_TYPE,
        {
            "type": "CQUAD4",
            "PID": shell1.get_entity_values(DECK, ("EID", "PID"))["PID"],
            "G1": unique_nodes[0],
            "T1": shell1_info[unique_nodes[0]]["thickness"],
            "G2": common_nodes[0],
            "T2": common_nodes_dict[common_nodes[0]]["thickness"],
            "G3": unique_nodes[1],
            "T3": shell2_info[unique_nodes[1]]["thickness"],
            "G4": common_nodes[1],
            "T4": common_nodes_dict[common_nodes[1]]["thickness"],
        },
        debug=ansa.constants.REPORT_ALL,
    )
    print(debug_report)
    print(f"Created new shell with ID {new_shell._id}")

    # Delete old shells
    base.DeleteEntity(shell1)
    base.DeleteEntity(shell2)


def get_bad_shells(shells):
    """Return a list of shells that fail the quality check."""
    return [
        shell for shell in shells if base.CalculateOffElements(shell)["TOTAL OFF"] != 0
    ]


if __name__ == "__main__":
    main()
