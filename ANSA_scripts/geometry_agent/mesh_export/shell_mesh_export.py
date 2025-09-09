# PYTHON script
import os

from ansa import base


def shell_mesh_export(filepath: str = None, **kwargs) -> str:
    # Get current path of script
    current_dir = os.path.dirname(__file__)

    output_path = filepath or os.path.join(current_dir, "mid_mesh.inp")

    base.OutputAbaqus(
        filename=output_path,
        **kwargs,
    )

    return output_path


if __name__ == "__main__":
    shell_mesh_export()
