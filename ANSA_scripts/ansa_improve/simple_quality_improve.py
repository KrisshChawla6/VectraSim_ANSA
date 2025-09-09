#
# This script improves mesh quality for the whole mesh together, using ANSA improvement methods
#
# ==========================

from ansa import base, mesh

DECK = base.CurrentDeck()
SHELL_TYPE = "ELEMENT_SHELL"
SHELL_SECTION = "SECTION_SHELL"
TEMP_PROP_NAME = "TMP_POOR_SHELL"


def get_bad_shells(shells):
    """Return a list of shells that fail the quality check."""
    return [
        shell for shell in shells if base.CalculateOffElements(shell)["TOTAL OFF"] != 0
    ]


def find_or_create_temp_property():
    """Return the temporary property used for isolating bad shells."""
    props = base.CollectEntities(DECK, None, SHELL_SECTION)
    for prop in props:
        if prop._name == TEMP_PROP_NAME:
            return prop
    return base.CreateEntity(DECK, SHELL_SECTION, {"Name": TEMP_PROP_NAME})


def assign_shells_to_property(shells, prop):
    """Assign given shells to the provided property."""
    for shell in shells:
        base.SetEntityCardValues(DECK, shell, {"PID": prop._id})


def isolate_bad_shells(bad_shells):
    """Assign bad shells to a temporary property and isolate them visually."""
    temp_prop = find_or_create_temp_property()
    assign_shells_to_property(bad_shells, temp_prop)

    # Hide all properties and isolate the temp one
    base.SetEntityVisibilityValues(DECK, {SHELL_SECTION: "off"})
    base.Or(keyword=SHELL_SECTION, id=temp_prop._id)
    base.Neighb("3")


def restore_shells_property(shells, target_pid=None):
    """Reassign the given shells to the specified property."""
    if target_pid is None:
        # Use the first SECTION_SHELL if not specified
        props = base.CollectEntities(DECK, None, SHELL_SECTION)
        if not props:
            raise RuntimeError("No shell property found to restore shells.")
        target_pid = props[0]._id

    for shell in shells:
        base.SetEntityCardValues(DECK, shell, {"PID": target_pid})


def fix_bad_shells_together(shells, fix_sequence):
    """Apply a sequence of mesh fixing functions to improve quality."""
    for fix_func in fix_sequence:
        bad_shells = get_bad_shells(shells)
        if not bad_shells:
            print("All elements pass quality checks.")
            return

        print(f"{fix_func.__name__}(): Fixing {len(bad_shells)} poor-quality shells...")
        isolate_bad_shells(bad_shells)
        restore_shells_property(bad_shells)
        fix_func()
        base.All()

    # Final check
    bad_shells = get_bad_shells(shells)
    print(f"Final off-quality shells: {len(bad_shells)}")
    if bad_shells:
        print("Some poor-quality elements remain.")
        isolate_bad_shells(bad_shells)
    else:
        print("All elements pass quality checks.")


def main():
    parts = base.CollectEntities(DECK, None, "ANSAPART")
    if not parts:
        print("No parts found.")
        return
    print(f"Working on part: {parts[0]._name}")

    shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    if not shells:
        print("No shell elements found.")
        return

    print(f"Total shells: {len(shells)}")

    # Define the fix sequence
    fix_sequence = [mesh.FixQuality, mesh.Reconstruct, mesh.Reshape]

    fix_bad_shells_together(shells, fix_sequence)


if __name__ == "__main__":
    main()
