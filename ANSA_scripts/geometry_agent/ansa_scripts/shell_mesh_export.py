# PYTHON script
import os
import ansa

from ansa import base, constants, mesh, batchmesh

def shell_mesh_export(filepath: str = None) -> str:
    
    # Get current path of script
    current_dir = os.path.dirname(__file__)

    base.All()
    
    output_path = filepath or os.path.join(current_dir, "mid_mesh.inp")

    base.OutputAbaqus(
        filename=output_path,
    )

    return output_path

if __name__ == '__main__':
    shell_mesh_export()