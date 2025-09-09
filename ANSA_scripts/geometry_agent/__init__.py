#
# The ANSA Geometry Agent focuses on the Geometry cleanup part.
#
# The agent is designed to:
# 1. Load solid and mid-surface meshes from INP files.
# 2. Clean and triangulate the meshes.
# 3. Compute geometric differences between the two meshes.
# 4. Diagnose issues based on distance and normal consistency checks.
# 5. Plan fixes for the diagnosed issues.
# 6. Export the issues and suggested fixes to a JSON file.
#
# This geometry agent is a v1 prototype to tackle Geometry cleanup.
# It requires a middle mesh M and a solid mesh G. It then attempts to compute the distances between G and M nodes, trying to identify M regions that does not represent G well.
#

# from .mesh_export.mid_mesh_export import mid_mesh_export
# from .mesh_export.shell_mesh_export import shell_mesh_export
