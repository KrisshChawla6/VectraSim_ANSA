# PYTHON script
import ansa

from ansa import base

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
    base.Not(all_shells)
    base.Or(bad_shells[0])

    base.SetEntityVisibilityValues(DECK, {"GRID": "on"})
    nodes_0 = base.CollectEntities(DECK, None, "GRID", True, filter_visible=True)
    print(len(nodes_0))

    base.Neighb("1")
    shells_0 = base.CollectEntities(DECK, None, SHELL_TYPE, True, filter_visible=True)

    # Get shell entities
    for shell in bad_shells:
        print(f"Working on shell with id {shell._id}")
        split_shell(shell)


def split_shell(shell: base.Entity):
    """Splitting a QUAD shell into two TRIA shells"""

    shell_entities = shell.get_entity_values(DECK, ("G1", "G2", "G3", "G4"))

    if len(shell_entities) != 4:
        print(f"Shell {shell._id} is not a QUAD, cannot split.")
        return

    complete_shell_entities = shell.get_entity_values(
        DECK, ("EID", "PID", "G1", "T1", "G2", "T2", "G3", "T3", "G4", "T4")
    )

    def dist(node1: base.Entity, node2: base.Entity):
        """Calculate distance between two nodes."""
        node1 = node1.get_entity_values(DECK, ("X1", "X2", "X3"))
        node2 = node2.get_entity_values(DECK, ("X1", "X2", "X3"))
        if not node1 or not node2:
            return float("inf")
        return (
            (node1["X1"] - node2["X1"]) ** 2
            + (node1["X2"] - node2["X2"]) ** 2
            + (node1["X3"] - node2["X3"]) ** 2
        ) ** 0.5

    diag1 = dist(shell_entities["G1"], shell_entities["G3"])
    diag2 = dist(shell_entities["G2"], shell_entities["G4"])

    if diag1 < diag2:
        # Split along G1-G3 diagonal
        new_shell1, debug_report = base.CreateEntity(
            DECK,
            SHELL_TYPE,
            {
                "type": "CTRIA3",
                "PID": complete_shell_entities["PID"],
                "G1": shell_entities["G1"],
                "T1": complete_shell_entities["T1"],
                "G2": shell_entities["G2"],
                "T2": complete_shell_entities["T2"],
                "G3": shell_entities["G3"],
                "T3": complete_shell_entities["T3"],
            },
            debug=ansa.constants.REPORT_ALL,
        )
        print(debug_report)
        print(f"Created new shell with ID {new_shell1._id}")

        new_shell2, debug_report = base.CreateEntity(
            DECK,
            SHELL_TYPE,
            {
                "type": "CTRIA3",
                "PID": complete_shell_entities["PID"],
                "G1": shell_entities["G1"],
                "T1": complete_shell_entities["T1"],
                "G2": shell_entities["G3"],
                "T2": complete_shell_entities["T3"],
                "G3": shell_entities["G4"],
                "T3": complete_shell_entities["T4"],
            },
            debug=ansa.constants.REPORT_ALL,
        )
        print(debug_report)
        print(f"Created new shell with ID {new_shell2._id}")

        base.DeleteEntity(shell)
        print(f"Deleted original shell {shell._id}")
    else:
        # Split along G2-G4 diagonal
        new_shell1, debug_report = base.CreateEntity(
            DECK,
            SHELL_TYPE,
            {
                "type": "CTRIA3",
                "PID": complete_shell_entities["PID"],
                "G1": shell_entities["G2"],
                "T1": complete_shell_entities["T2"],
                "G2": shell_entities["G3"],
                "T2": complete_shell_entities["T3"],
                "G3": shell_entities["G4"],
                "T3": complete_shell_entities["T4"],
            },
            debug=ansa.constants.REPORT_ALL,
        )
        print(debug_report)
        print(f"Created new shell with ID {new_shell1._id}")

        new_shell2, debug_report = base.CreateEntity(
            DECK,
            SHELL_TYPE,
            {
                "type": "CTRIA3",
                "PID": complete_shell_entities["PID"],
                "G1": shell_entities["G1"],
                "T1": complete_shell_entities["T1"],
                "G2": shell_entities["G2"],
                "T2": complete_shell_entities["T2"],
                "G3": shell_entities["G4"],
                "T3": complete_shell_entities["T4"],
            },
            debug=ansa.constants.REPORT_ALL,
        )
        print(debug_report)
        print(f"Created new shell with ID {new_shell2._id}")

        base.DeleteEntity(shell)
        print(f"Deleted original shell {shell._id}")


def get_bad_shells(shells):
    """Return a list of shells that fail the quality check."""
    return [
        shell for shell in shells if base.CalculateOffElements(shell)["TOTAL OFF"] != 0
    ]


if __name__ == "__main__":
    main()
