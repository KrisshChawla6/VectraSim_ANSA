#
# Dummy planning module to fix geometry problems for the geometry agent
#
# ==========================


def choose_fix(patch, issue_type="missing_feature"):
    """
    Map issue -> fix type
    """
    if issue_type == "missing_feature":
        return {"action": "imprint_and_remesh", "target_patch": patch}
    else:
        return {"action": "noop"}
