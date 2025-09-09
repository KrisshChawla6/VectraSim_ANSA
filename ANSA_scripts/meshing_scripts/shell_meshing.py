# PYTHON script
import os

from ansa import base, batchmesh


def shell_meshing(**kwargs):
    # Extracting kwargs
    mpar_file = kwargs.get("mpar_file", ".ansa_mpar")

    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)

    # Get the current deck
    current_deck = base.CurrentDeck()

    # Show all
    base.All()

    # Using the batchmesh module
    # New meshing scenario
    scenario = batchmesh.GetNewMeshingScenario("Name", "scenario_with_all_parts")
    parts = base.CollectEntities(current_deck, None, "ANSAPART")
    ret_val = batchmesh.AddPartToMeshingScenario(parts, scenario)

    # New meshing session
    session = batchmesh.GetNewSession("MySession")
    part = parts[0]
    ret_val = batchmesh.AddPartToSession(part, session)
    batchmesh.AddSessionToMeshingScenario(session, scenario)

    # Read mesh parameters from .ansa_mpar file
    mpar_path = os.path.join(script_dir, mpar_file)
    ret_val = batchmesh.ReadSessionMeshParams(session, mpar_path)
    print(ret_val)

    ret_val = batchmesh.RunMeshingScenario(scenario)
    print(ret_val)

    base.SaveFileAsStep("test.stp")


if __name__ == "__main__":
    shell_meshing()
