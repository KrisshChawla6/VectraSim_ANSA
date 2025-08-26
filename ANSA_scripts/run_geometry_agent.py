# Test file used to execute geometry_agent

import os
from geometry_agent import agent as geom_agent

def run_mesh_analysis(**kwargs):
    # cad_path = "C:\\Users\\HowardWu\\test.inp"
    # mid_path = "C:\\Users\\HowardWu\\test_mid.inp"
    # cad_path = "D:\\OneDrive - Stanford\\VectraSim files\\CAE part example\\Complex\\complex_mesh_G.inp"
    # mid_path = "D:\\OneDrive - Stanford\\VectraSim files\\CAE part example\\Complex\\complex_mesh_M.inp"

    # cad_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\Air_FTB_CAD_G_mesh.inp"
    # mid_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\Air_FTB_CAD_M_mesh_no_intersection.inp"

    cad_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\shell_mesh.inp"
    mid_path = "D:\\OneDrive - Stanford\\VectraSim files\\Lucid\\CAD from Lucid\\mid_surf_mesh.inp"

    geom_agent.run_agent(cad_path, mid_path, os.path.dirname(cad_path), **kwargs)

if __name__ == "__main__":
    run_mesh_analysis()