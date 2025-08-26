# PYTHON script
import os
import ansa

from ansa import base, constants, mesh, batchmesh

def mid_mesh_export(filepath: str = None) -> str:

    # Get current path of script
    current_dir = os.path.dirname(__file__)

    base.All()
    
    output_path = filepath or os.path.join(current_dir, "mid_mesh.inp")

    base.OutputAbaqus(
        filename=output_path,
        output_element_thickness="at_element_card"
    )

    return output_path


if __name__ == '__main__':
    mid_mesh_export()


