import ansa
from ansa import base, mesh

DECK = base.CurrentDeck()
SHELL_TYPE = "ELEMENT_SHELL"
SECTION_SHELL = "SECTION_SHELL"
NEIGHBOR_LEVEL = 1


def get_bad_shells(shells):
    """Return shells failing quality check."""
    return [s for s in shells if base.CalculateOffElements(s)['TOTAL OFF'] != 0]


def expand_to_neighbors(shells, max_level=NEIGHBOR_LEVEL):
    """Expand visibility to neighbors iteratively."""
    seen = set(shells)
    queue = shells[:]

    while queue:
        all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
        base.Not(all_shells)  # hide all
        base.Or(entities=shells)
        base.Neighb(str(max_level))
        new_visible = base.CollectEntities(DECK, None, SHELL_TYPE, True, filter_visible=True)
        base.All()  # get visible shells

        # Detect new shells
        new_shells = [s for s in new_visible if s not in seen]
        if not new_shells:
            break
        seen.update(new_shells)
        queue = new_shells

    return list(seen)


def isolate_and_fix(shells_to_fix):
    """Show shells, then apply FixQuality → Reconstruct → Reshape step-by-step.
    Abort early if no bad shells remain after any step.
    """
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    base.Not(all_shells)
    base.Or(entities=shells_to_fix)

    def has_bad_visible_shells():
        visible_shells = base.CollectEntitiesI(DECK, None, SHELL_TYPE, True, filter_visible=True)
        return bool(get_bad_shells(visible_shells))

    print("→ FixQuality...")
    mesh.FixQuality()
    if not has_bad_visible_shells():
        print("  ✓ Clean after FixQuality")
        return

    print("→ Reconstruct...")
    mesh.Reconstruct()
    if not has_bad_visible_shells():
        print("  ✓ Clean after Reconstruct")
        return

    print("→ Reshape...")
    mesh.Reshape()
    if not has_bad_visible_shells():
        print("  ✓ Clean after Reshape")
    else:
        print("  ⚠ Still poor-quality shells after Reshape")


def get_remaining_bad_shells(exclude_shells):
    """Get all bad shells that are not in the excluded set."""
    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    return [s for s in get_bad_shells(all_shells) if s not in exclude_shells]


def advanced_quality_check():
    print("Starting localized mesh fix pipeline...")

    fix_bad_shells_per_area()

def fix_bad_shells_per_area():
    """Iteratively isolate and fix each bad shell area until all are processed."""
    processed_shells = set()

    all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)
    bad_shells_remaining = get_bad_shells(all_shells)

    print(bad_shells_remaining)

    while bad_shells_remaining:
        target_shell = bad_shells_remaining[0]

        print(f"\nTargeting new bad shell: ID={target_shell._id}")

        # 1. Expand to neighbors recursively until no more new bad shells
        expanded_shells = expand_to_neighbors([target_shell])
        base.Not(all_shells)
        base.Or(entities=expanded_shells)
        current_visible = base.CollectEntities(DECK, None, SHELL_TYPE, True, filter_visible=True)

        bad_shells_visible = get_bad_shells(current_visible)
        prev_len = -1
        while len(bad_shells_visible) > prev_len:
            prev_len = len(bad_shells_visible)
            expanded_shells = expand_to_neighbors(bad_shells_visible)
            base.Not(all_shells)
            base.Or(entities=expanded_shells)
            current_visible = base.CollectEntities(DECK, None, SHELL_TYPE, True, filter_visible=True)
            bad_shells_visible = get_bad_shells(current_visible)

        # 2. Apply fix to the isolated visible shells
        print(f"Fixing {len(bad_shells_visible)} poor-quality shells in isolated group...")
        isolate_and_fix(current_visible)

        # 3. Update processed set and re-identify bad shells
        processed_shells.update(current_visible)
        bad_shells_remaining = get_remaining_bad_shells(processed_shells)
        all_shells = base.CollectEntities(DECK, None, SHELL_TYPE, True)

    print("\nAll poor-quality shells processed.")

if __name__ == "__main__":
    advanced_quality_check()
