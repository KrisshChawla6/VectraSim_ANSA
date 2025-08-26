# This must run *inside* ANSA Python environment
import ansa

def apply_fix(plan):
    action = plan["action"]
    if action == "imprint_and_remesh":
        patch = plan["target_patch"]
        # TODO: select faces in patch, project feature, remesh
        print("Would remesh patch:", patch)
    else:
        pass
