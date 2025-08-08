from __future__ import annotations
from typing import *

def ClearOverlayRuns(overlay_run_type: str) -> int:

	"""

	This function deletes all the overlay runs.

	Parameters
	----------
	overlay_run_type : str
		Overlay run type. Possible string values:
		- 'session'
		- 'project'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    ret = overlay.ClearOverlayRuns(overlay_run_type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewOverlayRunsEnd(overlay_run_type: str) -> object:

	"""

	This function ends recording the creation of new overlay runs. This function should be preceded by a corresponding call to script function CollectNewOverlayRunsStart().

	Parameters
	----------
	overlay_run_type : str
		Overlay run type. Possible string values:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Overlay referring to one specific newly created overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		from meta import utils
		
		
		def main():
		    overlay_run_type = "session"
		    ovr = overlay.CollectNewOverlayRunsStart(overlay_run_type)
		
		    # create new overlay runs
		    utils.MetaCommand(
		        'read ses overlay "/home/examples/Overlay_session.ses" "/home/examples/NastranEx2.nas,/home/examples/NastranEx2Overlay.nas,/home/examples/NastranEx2.op2,/home/examples/NastranEx2Overlay.op2"'
		    )
		
		    new_overlay_runs = overlay.CollectNewOverlayRunsEnd(overlay_run_type)
		    for ovr in new_overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewOverlayRunsStart(overlay_run_type: str) -> int:

	"""

	This function starts recording the creation of new overlay runs. This function should be followed by a corresponding call to script function CollectNewOverlayRunsEnd().

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		from meta import utils
		
		
		def main():
		    overlay_run_type = "session"
		    ovr = overlay.CollectNewOverlayRunsStart(overlay_run_type)
		
		    # create new overlay runs
		    utils.MetaCommand(
		        'read ses overlay "/home/examples/Overlay_session.ses" "/home/examples/NastranEx2.nas,/home/examples/NastranEx2Overlay.nas,/home/examples/NastranEx2.op2,/home/examples/NastranEx2Overlay.op2"'
		    )
		
		    new_overlay_runs = overlay.CollectNewOverlayRunsEnd(overlay_run_type)
		    for ovr in new_overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsOverlayRun(overlay_run: object) -> int:

	"""

	This function checks whether an object is of class Overlay.

	Parameters
	----------
	overlay_run : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the object is of class Overlay, or 0 if not.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		from meta import models
		
		
		def main():
		    all_overlay_runs = overlay.OverlayRuns()
		
		    entities = list()
		    entities.append("A string")
		    entities.append(all_overlay_runs[1])
		    for ent in entities:
		        if overlay.IsOverlayRun(ent):
		            ovr = ent
		            print("This is an object of class type Overlay")
		            print(ovr.id, ovr.type, ovr.name, ovr.filename)
		        else:
		            print("This is NOT an object of class type Overlay")
		
		
		if __name__ == "__main__":
		    main()


	"""

def OverlayRunById(overlay_run_type: str, overlay_run_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_overlay_runs` instead.


	This function searches for the overlay_run with the given id (overlay_run_id).

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	overlay_run_id : int
		Id of the overlay run.

	Returns
	-------
	object
		Upon success, it returns an object of class Overlay with the given id.
		Else, None is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    ovr = overlay.OverlayRunById(overlay_run_type, overlay_run_id)
		    if ovr:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_overlay_runs instead.", DeprecationWarning)

def OverlayRuns() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_overlay_runs` instead.


	This function collects all overlay runs.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Overlay referring to one specific overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    all_overlay_runs = overlay.OverlayRuns()
		
		    for ovr in all_overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_overlay_runs instead.", DeprecationWarning)

def OverlayRunsByFilename(overlay_run_type: str, overlay_run_filename: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_overlay_runs` instead.


	This function collects all overlay runs with a specific filename.

	Parameters
	----------
	overlay_run_type : str
		Overlay run type. Possible string values:
		- 'session'
		- 'project'.

	overlay_run_filename : str
		Search string for the filename of the overlay run. Wildcards can also be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Overlay referring to one specific overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_filename = "*ex*"
		    overlay_runs = overlay.OverlayRunsByFilename(overlay_run_type, overlay_run_filename)
		
		    for ovr in overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_overlay_runs instead.", DeprecationWarning)

def OverlayRunsByName(overlay_run_type: str, overlay_run_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_overlay_runs` instead.


	This function collects all overlay runs with a specific name.

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	overlay_run_name : str
		Search string for the name of the overlay run. Wildcards can also be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Overlay referring to one specific overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_name = "Run1"
		    overlay_runs = overlay.OverlayRunsByName(overlay_run_type, overlay_run_name)
		
		    for ovr in overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_overlay_runs instead.", DeprecationWarning)

def OverlayRunsByType(overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_overlay_runs` instead.


	This function collects all overlay runs with a specific type.

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class OverlayRun referring to one specific overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_runs = overlay.OverlayRunsByType(overlay_run_type)
		
		    for ovr in overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_overlay_runs instead.", DeprecationWarning)

def OverlayRunsListToDict(overlay_runs: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Overlay.

	Parameters
	----------
	overlay_runs : object
		List of objects of class Overlay.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the overlay run and data is the corresponding Overlay object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    all_overlay_runs = overlay.OverlayRuns()
		    dict_overlay_runs = overlay.OverlayRunsListToDict(all_overlay_runs)
		    for id, ovr in dict_overlay_runs.items():
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PlanesOfOverlayRun(overlay_run_type: str, overlay_run_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_planes` instead.


	This function searches for the planes of an overlay run with a given type and id.

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	overlay_run_id : int
		Id of the overlay run.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one plane of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_planes = planes.PlanesOfOverlayRun(overlay_run_type, overlay_run_id)
		    for pl in overlay_run_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_planes instead.", DeprecationWarning)

def ReportNewOverlayRuns(overlay_run_type: str) -> object:

	"""

	This function collects the newly created overlay runs from the last call of script function CollectNewOverlayRunsStart(). This function should be preceded by a corresponding call to script function CollectNewOverlayRunsStart() and should be followed by a corresponding call to script function CollectNewOverlayRunsEnd().

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		It returns a list with the Overlay objects of the corresponding newly created overlay runs.
		Upon failure, an empty list is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		from meta import utils
		
		
		def main():
		    overlay_run_type = "session"
		    ovr = overlay.CollectNewOverlayRunsStart(overlay_run_type)
		
		    # create new overlay runs
		    utils.MetaCommand(
		        'read ses overlay "/home/examples/Overlay/Overlay.ses" "/home/examples/Overlay/Abaqus.inp,/home/examples/Overlay/AbaqusOverlay.inp,/home/examples/Overlay/Abaqus.odb,/home/examples/Overlay/AbaqusOverlay.odb"'
		    )
		
		    new_overlay_runs = overlay.ReportNewOverlayRuns(overlay_run_type)
		    for ovr in new_overlay_runs:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		    overlay.CollectNewOverlayRunsEnd(overlay_run_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateOverlayRun(overlay_run: object) -> object:

	"""

	This function updates the data of the given Overlay object. Update is based in the field 'id' of the given Overlay object.

	Parameters
	----------
	overlay_run : object
		An object of class Overlay.

	Returns
	-------
	object
		Upon success, it returns the new updated Overlay object.
		Else, None is returned.

	See Also
	--------
	overlay.Overlay

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    ovr = overlay.OverlayRunById(overlay_run_type, overlay_run_id)
		
		    # commands which alter the data of the Overlay object
		    # .......
		
		    ovr = overlay.UpdateOverlayRun(ovr)
		    if ovr:  # Update OK
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		    else:  # Update FAILED
		        print("This is not a valid Overlay object")
		
		
		if __name__ == "__main__":
		    main()


	"""

class Overlay():

	"""

	Class for overlay runs.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    if ovr:
		        print(ovr.id, ovr.type, ovr.name, ovr.filename)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_annotations
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_annot = ovr.get_annotations()
		    for a in overlay_annot:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_boundaries
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_boundaries = ovr.get_boundaries()
		    for b in overlay_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_connections
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_connections = ovr.get_connections()
		    for con in overlay_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinate_systems
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_coords = ovr.get_coordinate_systems()
		    for cs in overlay_coords:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.imported)  # Coordinate System imported
		        print(cs.moving)  # Coordinate System moving
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curves
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_curves = ovr.get_curves()
		    for c in overlay_curves:
		        print(
		            c.id,
		            c.name,
		            c.plot_id,
		            c.visible,
		            c.selected,
		            c.window_name,
		            c.page_id,
		            c.command,
		            c.entity_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_elements = ovr.get_elements()
		    for e in overlay_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_groups
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_groups = ovr.get_groups()
		    for g in overlay_groups:
		        print(
		            g.name,
		            g.id,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.part_type,
		        )
		        print(
		            g.vsc_number,
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_isofunctions
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_iso = ovr.get_isofunctions()
		    for iso in overlay_iso:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_materials
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_materials = ovr.get_materials()
		    for m in overlay_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_nodes = ovr.get_nodes()
		    for n in overlay_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_parts = ovr.get_parts()
		    for p in overlay_parts:
		        print(
		            p.id,
		            p.type,
		            p.subtype,
		            p.visible,
		            p.name,
		            p.mat_id,
		            p.shell_thick,
		            p.model_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_models
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_models = ovr.get_models()
		    for r in overlay_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_planes
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_planes = ovr.get_planes()
		    for pl in overlay_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    overlay_resultsets = ovr.get_resultsets()
		    for res in overlay_resultsets:
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import overlay
		
		
		def main():
		    ovr = overlay.Overlay(id=1, type="session")
		    ret = ovr.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    ret = page.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the overlay run.

	"""

	type: str = None
	"""
	Type of the overlay run ('session', 'project').

	"""

	name: str = None
	"""
	Name of the overlay run.

	"""

	filename: str = None
	"""
	Filename of the overlay run.

	"""

	def get_models(self) -> object:

		"""

		This method gets the models of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Model referring to one model of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_planes(self) -> object:

		"""

		This method gets the planes of the overlay run. 


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Plane referring to one plane of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_isofunctions(self) -> object:

		"""

		This method gets the isofunctions of the overlay run. This method works for the active page.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Isofunction referring to one isofunction of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_groups(self, all_instances: bool) -> bool:

		"""

		This method gets the groups of the overlay run.


		Parameters
		----------
		all_instances : bool, optional
			All instances of group.

		Returns
		-------
		bool
			Upon success, it returns a list where each member of the list is an object of type Group referring to one group of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_resultsets(self) -> object:

		"""

		This method gets the resultsets of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Result referring to one resultset of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_parts(self) -> object:

		"""

		This method gets the parts of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Part referring to one part of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_elements(self) -> object:

		"""

		This method gets the elements of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Element referring to one element of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_nodes(self) -> object:

		"""

		This method gets the nodes of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Node referring to one specific node of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_coordinate_systems(self) -> object:

		"""

		This method gets the coordinate systems of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list with the CoordSystem objects of the coordinate systems of the overlay run.Each item of the list is an object of class type CoordSystem, referring to one coordinate system of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_boundaries(self) -> object:

		"""

		This method gets the boundary elements of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Boundary referring to one boundary element of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_materials(self) -> object:

		"""

		This function gets the materials of the overlay run. 


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Material referring to one material of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_annotations(self) -> object:

		"""

		This method gets the annotations of the overlay run. This method works for the active page.


		Returns
		-------
		object
			Upon failure, it returns a list where each member of the list is an object of type Annotation referring to one annotation of the overlay run.Upon failure, an empty list is returned.

		"""


	def get_curves(self) -> object:

		"""

		This method gets the curves of the overlay run. This method works for the active page.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Curve referring to one curve of the overlay run. Upon failure, an empty list is returned.

		"""


	def get_connections(self) -> object:

		"""

		This method gets the connections of the overlay run.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Connection referring to one connection of the overlay run. Upon failure, an empty list is returned.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Overlay entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

