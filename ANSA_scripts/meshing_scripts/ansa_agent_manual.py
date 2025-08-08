# PYTHON script
import os
import json
import ansa
from ansa import base, mesh, constants, batchmesh

from mid_surf_meshing import mid_surf_meshing
from solid_meshing import solid_meshing
from shell_meshing import shell_meshing


def main():
    # Get current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get agent JSON input file
    agent_input_file = os.path.join(script_dir, "mesh_agent_input.json")
    input_config = json.load(open(agent_input_file, "r"))

    mesh_type = input_config.get("mesh_type_selected", "cfd_shell")
    mpars_path = input_config.get("ansa_mpars_path", None)
    custom_mpars_inputs = input_config.get("custom_user_inputs", {})
    if len(custom_mpars_inputs) > 0:
        def update_mpars_with_custom_inputs(file_path, updates):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                for key, value in updates.items():
                    if line.strip().startswith(f"{key} ="):
                        lines[i] = f"    {key} = {value}\n"

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)

        update_mpars_with_custom_inputs(mpars_path, custom_mpars_inputs)

    if mesh_type == "cfd_shell":
        print("Running shell meshing...")
        shell_meshing()
    elif mesh_type == "fea_mid":
        print("Running mid-surface meshing...")
        mid_surf_meshing()
    elif mesh_type == "fea_solid":
        print("Running solid meshing...")
        solid_meshing()
    elif mesh_type == "cfd_volume":
        print("Running volume meshing...")
        # volume_meshing()
    else:
        print(f"Unknown mesh type: {mesh_type}. Please check the input configuration.")

    print(input_config)


if __name__ == "__main__":
    main()
