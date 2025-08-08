# PYTHON script
import os
import ansa
from ansa import base, mesh, constants, batchmesh

def solid_meshing(**kwargs):
    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    
    # Get the current deck
    current_deck = base.CurrentDeck()
    print("Current deck:", current_deck)
    
    vol = mesh.VolumesDetect()

    ents = base.CollectEntities(current_deck, None, "VOLUME")
    mesh.VolumesMeshV(ents, "HEXAPOLY")

    # For some reason batchmeshing is not working for solids
    # base.All()
    # vol_scen = batchmesh.GetNewVolumeScenario()
    # solids = base.CollectEntities(current_deck, None, "SOLID")
    # print(solids)
    # mesh.CreateShellsOnSolidsPidSkin(solids)
    # parts = base.CollectEntities(current_deck, None, "ANSAPART")
    # print(parts)
    # ret_val = batchmesh.AddPartToMeshingScenario(parts, vol_scen)
    
    # # New meshing session
    # session = batchmesh.GetNewVolumeSession("MySession")
    # part = parts[0]
    # ret_val = batchmesh.AddPartToSession(part, session)
    # batchmesh.AddSessionToMeshingScenario(session, vol_scen)

    # # Read mesh parameters from .ansa_mpar file
    # mpar_path = os.path.join(script_dir, ".ansa_mpar")
    # print(mpar_path)
    # ret_val = batchmesh.ReadSessionMeshParams(session, mpar_path)
    # print(ret_val)
    
    # status = batchmesh.RunMeshingScenario(vol_scen)

if __name__ == '__main__':
    solid_meshing()


