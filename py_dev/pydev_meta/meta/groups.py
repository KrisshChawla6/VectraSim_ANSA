from __future__ import annotations
from typing import *

def AddBoundariesOnGroup(model_id: int, group_name: str, boundaries_types: object, boundaries_ids: object, second_ids: object, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.add_boundaries` instead.


	This function adds some specific boundary elements of a model on an existing group.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	boundaries_types : object
		List with the types of boundary elements  to add (META constant).

	boundaries_ids : object
		List with the ids of boundary elements to add.

	second_ids : object
		List with the second ids of boundary elements to add.

	group_instance : int, optional
		Instance of the group. If it is absent, the default value is 1.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    vis_bounds = boundaries.VisibleBoundaries(model_id)
		    boundaries_types = list()
		    boundaries_ids = list()
		    second_ids = list()
		    for b in vis_bounds:
		        boundaries_types.append(b.type)
		        boundaries_ids.append(b.id)
		        second_ids.append(b.second_id)
		    groups.AddBoundariesOnGroup(
		        model_id,
		        group_name,
		        boundaries_types,
		        boundaries_ids,
		        second_ids,
		        group_instance,
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.add_boundaries instead.", DeprecationWarning)

def AddElementsOnGroup(model_id: int, group_name: str, elements_types: object, elements_ids: object, second_ids: object, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.add_elements` instead.


	This function adds some specific elements of a model on an existing group.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group to add.

	elements_types : object
		List with the types of elements (META constants).

	elements_ids : object
		List with the ids of elements to add.

	second_ids : object
		List with the second ids of elements to add.

	group_instance : int
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	int
		It returns an integer, 1 upon success or 0 upon failure

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    vis_elems = elements.VisibleElements(model_id)
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    for e in vis_elems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		    groups.AddElementsOnGroup(
		        model_id, group_name, elements_types, elements_ids, second_ids, group_instance
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.add_elements instead.", DeprecationWarning)

def AddMaterialsOnGroup(model_id: int, group_name: str, materials_ids: object, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.add_materials` instead.


	This function adds some specific materials of a model on an existing group.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	materials_ids : object
		List with the ids of materials to add.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import groups
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    material_type = constants.MAT1
		    collected_materials = materials.MaterialsByType(model_id, material_type)
		    materials_ids = list()
		    for m in collected_materials:
		        materials_ids.append(m.id)
		    groups.AddMaterialsOnGroup(model_id, group_name, materials_ids, group_instance)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.add_materials instead.", DeprecationWarning)

def AddNodesOnGroup(model_id: int, group_name: str, nodes_ids: object, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.add_nodes` instead.


	This function adds some specific nodes of a model on an existing group.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	nodes_ids : object
		List with the ids of nodes to add.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    ide_nodes = nodes.IdentifiedNodes(model_id)
		    nodes_ids = list()
		    for n in ide_nodes:
		        nodes_ids.append(n.id)
		    groups.AddNodesOnGroup(model_id, group_name, nodes_ids, group_instance)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.add_nodes instead.", DeprecationWarning)

def AddPartsOnGroup(model_id: int, group_name: str, parts_types: object, parts_ids: object, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.add_parts` instead.


	This function adds some specific parts of a model on a group with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	parts_types : object
		List with the types of parts (META constant).

	parts_ids : object
		List with the ids of parts to add.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    ide_parts = parts.IdentifiedParts(model_id)
		    parts_types = list()
		    parts_ids = list()
		    for p in ide_parts:
		        parts_types.append(p.type)
		        parts_ids.append(p.id)
		    groups.AddPartsOnGroup(model_id, group_name, parts_types, parts_ids, group_instance)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.add_parts instead.", DeprecationWarning)

def AdvFiltersOnCreateGroup(model_id: int, group_name: str, filter_entities: str, adv_filters: object, resultset: object) -> object:

	"""

	This function allows the user to collect entities of a model specified by its id through some advanced filters and create a group with these entities.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	filter_entities : str
		Argument 'filter_entities' is a string which refers to the type of the entities. Its possible values are:
		- 'parts'
		- 'materials'
		- 'elements'
		- 'boundaries'
		- 'nodes'
		In any other case, advanced filters will refer to elements.

	adv_filters : object
		Contains the advanced filters as a list of string expressions. Their syntax is the same with the commands referring to advanced filters.

	resultset : object, optional
		Object of class Result or string referring to the states selection of advanced filter. 
		Its possible values are:
		- object of class Result
		- 'current': Current state
		- 'all': All states 
		- 'locked': Locked states
		- range of states' ids (e.g. 1-10,13)
		If this argument is absent then results of advanced filters will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Group referring to the newly created group.
		Else, None is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "AdvFilterGroup"
		    filter_entities = "parts"
		    adv_filters = ["add:Parts:all::Keep All", "intersect:Parts:id:<=199:Keep All"]
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    g = groups.AdvFiltersOnCreateGroup(
		        model_id, group_name, filter_entities, adv_filters, resultset
		    )
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

def AdvFiltersOnGroups(model_id: int, adv_filters: object, result: object, sort: bool) -> object:

	"""

	This function allows the user to collect groups of a model through some advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter.

	result : object, optional
		Object of class Result or string referring to the states selection of advanced filter. 
		Its possible values are:
		- object of class Result
		- 'current': Current state
		- 'all': All states 
		- 'locked': Locked states
		- range of states' ids (e.g. 1-10,13)
		If this argument is absent then results of advanced filters will refer to the ORIGINAL STATE.

	sort : bool, optional
		Controls if the returned list is sorted or not. Default value is False.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one specific group of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import groups
		
		
		def main():
		    adv_filters = ["add:Parts:all::Keep All", "intersect:Parts:id:<=199:Keep All"]
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    collected_groups = groups.AdvFiltersOnGroups(model_id, adv_filters, result)
		    for g in collected_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

def BoundariesOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all boundary elements of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Refers to the instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    group_boundaries = boundaries.BoundariesOfGroup(
		        model_id, group_name, group_instance
		    )
		    iter_end = min(10, len(group_boundaries))
		    for b in group_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def BoundariesOfGroupByType(model_id: int, group_name: str, boundary_type: int, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all boundary elements with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	boundary_type : int
		Type of the boundary element (META constants).

	group_instance : int, optional
		Refers to the instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    boundary_type = constants.SPC1
		
		    group_boundaries = boundaries.BoundariesOfGroupByType(
		        model_id, group_name, boundary_type, group_instance
		    )
		    iter_end = min(10, len(group_boundaries))
		    for b in group_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def CentroidScalarOfGroup(result: object, group_name: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_centroid = groups.CentroidScalarOfGroup(result, group_name)
		    iter_end = min(10, len(group_centroid))
		    for centroid in group_centroid[0:iter_end]:  # Matrix with centroid_scalar structs
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_scalar instead.", DeprecationWarning)

def CentroidScalarOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of a given group instance belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_centroid = groups.CentroidScalarOfGroupInstance(
		        result, group_name, group_instance
		    )
		    iter_end = min(10, len(group_centroid))
		    for centroid in group_centroid[0:iter_end]:  # Matrix with centroid_scalar structs
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfGroup(result: object, group_name: str, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_vector` instead.


	This function calculates all centroid vector values of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	principal : str, optional
		Principal order of the centroid vector tensor values. It should be specified only when tensor results have been loaded. Possible values are:
		- 'first': first principal (default)
		- 'second': second principal
		- 'third': third principal

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_centroid = groups.CentroidVectorOfGroup(result, group_name)
		    iter_end = min(10, len(group_centroid))
		    for centroid in group_centroid[0:iter_end]:  # Matrix with centroid_scalar structs
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Value and Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_vector instead.", DeprecationWarning)

def CentroidVectorOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_vector` instead.


	This function calculates all centroid vector values of a given group instance belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	principal : str, optional
		Principal order of the centroid vector tensor values. It should be specified only when tensor results have been loaded. Possible values are:
		- 'first': first principal (default)
		- 'second': second principal
		- 'third': third principal

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_centroid = groups.CentroidVectorOfGroupInstance(
		        result, group_name, group_instance
		    )
		    iter_end = min(10, len(group_centroid))
		    for centroid in group_centroid[0:iter_end]:  # Matrix with centroid_scalar structs
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Value and Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_vector instead.", DeprecationWarning)

def CollectNewGroupsEnd() -> object:

	"""

	This function ends recording the creation of new groups. This function should be preceded by a corresponding call to script function CollectNewGroupsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one specific newly created group.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import utils
		
		
		def main():
		    groups.CollectNewGroupsStart()
		
		    # create new groups
		    utils.MetaCommand("groups create pid")
		
		    new_groups = groups.CollectNewGroupsEnd()
		    for g in new_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CollectNewGroupsStart() -> int:

	"""

	This function starts recording the creation of new groups. This function should be followed by a corresponding call to script function CollectNewGroupsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import utils
		
		
		def main():
		    groups.CollectNewGroupsStart()
		
		    # create new groups
		    utils.MetaCommand("groups create pid")
		
		    new_groups = groups.CollectNewGroupsEnd()
		    for g in new_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CornerScalarOfGroup(result: object, group_name: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_corner = groups.CornerScalarOfGroup(result, group_name)
		    iter_end = min(10, len(group_corner))
		    for corn in group_corner[0:iter_end]:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_scalar instead.", DeprecationWarning)

def CornerScalarOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a given group instance belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to the corner scalar values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_corner = groups.CornerScalarOfGroupInstance(
		        result, group_name, group_instance
		    )
		    iter_end = min(10, len(group_corner))
		    for corn in group_corner[0:iter_end]:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_scalar instead.", DeprecationWarning)

def CreateEmptyGroup(model_id: int, group_name: str, overwrite: int) -> object:

	"""

	This function creates an empty group with a given name in an existing model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	overwrite : int, optional
		Optional argument 'overwrite' refers to the case where a group with the given name exists. Its possible values are:
		- 0 : It does not overwrite the existing group (default)
		- 1 : It overwrites the existing group

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		
		    g = groups.CreateEmptyGroup(model_id, group_name)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromAdvFilters(model_id: int, group_name: str, resultset: object) -> object:

	"""

	This function creates a group with a given name by specifying some advanced filters on a window. The execution of the script will stop and a window will open in order for the user to specify its advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to to current settings of the Advanced Filter window.

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    g = groups.CreateGroupFromAdvFilters(model_id, group_name, resultset)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromBoundaries(model_id: int, group_name: str, boundaries: object) -> object:

	"""

	This function creates a group with a given name from some specific boundary elements of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	boundaries : object
		A list of object of class Boundary. The objects should be from the model specified by the argument model_id.

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    group_name = "My_Group"
		
		    vis_bounds = boundaries.VisibleBoundaries(model_id)
		    g = groups.CreateGroupFromBoundaries(model_id, group_name, vis_bounds)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		    # or
		    group_name = "My_Group_old"
		
		    boundaries_types = list()
		    boundaries_ids = list()
		    second_ids = list()
		    for b in vis_bounds:
		        boundaries_types.append(b.type)
		        boundaries_ids.append(b.id)
		        second_ids.append(b.second_id)
		    g = groups.CreateGroupFromBoundaries(
		        model_id, group_name, boundaries_types, boundaries_ids, second_ids
		    )
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromElements(model_id: int, group_name: str, elements: object) -> object:

	"""

	This function creates a group with a given name from some specific elements of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	elements : object
		List of objects of class Element.

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import elements
		
		
		def main():
		    model_id = 0
		    vis_elems = elements.VisibleElements(model_id)
		
		    group_name = "MyGroup"
		    g = groups.CreateGroupFromElements(model_id, group_name, vis_elems)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		    # or
		
		    group_name = "MyGroup_old"
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    for e in vis_elems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		    g = groups.CreateGroupFromElements(
		        model_id, group_name, elements_types, elements_ids, second_ids
		    )
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromMaterials(model_id: int, group_name: str, materials: object) -> object:

	"""

	This function creates a group with a given name from some specific materials of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	materials : object
		List of objects of class Material

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    materials = model.get_materials("all")
		    group_name = "MyGroup"
		
		    g = groups.CreateGroupFromMaterials(model.id, group_name, materials)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		    # or
		    group_name = "MyGroup_old"
		    materials_ids = [mat.id for mat in materials]
		    g = groups.CreateGroupFromMaterials(model.id, group_name, materials_ids)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromNodes(model_id: int, group_name: str, nodes: object) -> object:

	"""

	This function creates a group with a given name from some specific nodes of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	nodes : object
		A list of objects of class Node.

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		from meta import windows
		
		
		def main():
		    model = models.Model(0)
		    win = windows.Window("MetaPost", page_id=0)
		    group_name = "MyGroup"
		
		    nodes = model.get_nodes("identified", window=win)
		    g = groups.CreateGroupFromNodes(model.id, group_name, nodes)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		    # or
		    group_name = "MyGroup_old"
		    nodes_ids = [n.id for n in nodes]
		    g = groups.CreateGroupFromNodes(model.id, group_name, nodes_ids)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateGroupFromParts(model_id: int, group_name: str, parts: object) -> object:

	"""

	This function creates a group with a given name (group_name) from some specific parts of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	parts : object
		List of objects of class Part.

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the newly created group.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import parts
		
		
		def main():
		    model_id = 0
		    vis_parts = parts.VisibleParts(model_id)
		
		    group_name = "MyGroup"
		    g = groups.CreateGroupFromParts(model_id, group_name, vis_parts)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		            g.is_color_active,
		        )
		    # or
		
		    group_name = "MyGroup_old"
		    parts_types = list()
		    parts_ids = list()
		    for p in vis_parts:
		        parts_types.append(p.type)
		        parts_ids.append(p.id)
		    g = groups.CreateGroupFromParts(model_id, group_name, parts_types, parts_ids)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

def CreateSubgroup(model_id: int, child_group_name: str, parent_group_name: str, move_link: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.set_subgroup` instead.


	This function makes a given group subgroup of another existing group.

	Parameters
	----------
	model_id : int
		Id of the model.

	child_group_name : str
		Name of the child group.

	parent_group_name : str
		Name of the parent group.

	move_link : str, optional
		Defines if the child group will be moved or linked to its new position. Its possible values are:
		- 'move' : Move child group from its initial postion (default value)
		- 'link' : Child group will keep its old position

	Returns
	-------
	object
		Upon success, it returns a Group object referring to the subgroup.
		Else, a non valid Group object is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    child_group_name = "Subgroup"
		    parent_group_name = "Parent_Group"
		    # move_link = 'move'
		    move_link = "link"
		
		    g = groups.CreateSubgroup(model_id, child_group_name, parent_group_name, move_link)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		            g.vsc_number,
		        )
		        print(
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.set_subgroup instead.", DeprecationWarning)

def DeformationsOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of a given group belonging to the specified model. 

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class type Deformation referring to the deformation of a node for the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_deforms = groups.DeformationsOfGroup(result, group_name)
		    iter_end = min(10, len(group_deforms))
		    for deform in group_deforms[0:iter_end]:
		        print(deform.x, deform.y, deform.z, deform.total, deform.node_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_deformations instead.", DeprecationWarning)

def DeleteGroup(model_id: int, group_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.delete` instead.


	This function deletes a group of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    ret = groups.DeleteGroup(model_id, group_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.delete instead.", DeprecationWarning)

def DeleteGroupInstance(model_id: int, group_name: str, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.delete` instead.


	This function deletes a group instance of a model with a given name and instance.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    ret = groups.DeleteGroupInstance(model_id, group_name, group_instance)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.delete instead.", DeprecationWarning)

def DistanceGroupToGroup(model_id1: int, result1: object, group_name1: str, model_id2: int, result2: object, group_name2: str, group_instance1: int, group_instance2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_group` instead.


	This function calculates the distance or the elongation of a group from another group.

	Parameters
	----------
	model_id1 : int
		Id of the model of the 1st group.

	result1 : object
		An object of class Result that refers to a Resultset of the model for the first group.

	group_name1 : str
		Name of the 1st group.

	model_id2 : int
		Id of the model of the 2nd group.

	result2 : object
		An object of class Result that refers to a Resultset of the model for the second group.

	group_name2 : str
		Name of the 2nd group.

	group_instance1 : int, optional
		Instance of the 1st group. If it is absent, default value is 1.

	group_instance2 : int, optional
		Instance of the 2nd group. If it is absent, default value is 1.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as list elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id1 = 0
		    all_resultsets = results.Resultsets(model_id1)
		    result1 = all_resultsets[1]
		    group_name1 = "MyGroup1"
		    group_instance1 = 1
		
		    model_id2 = 0
		    all_resultsets = results.Resultsets(model_id2)
		    result2 = all_resultsets[1]
		    group_name2 = "MyGroup2"
		    group_instance2 = 1
		
		    distance = groups.DistanceGroupToGroup(
		        model_id1,
		        result1,
		        group_name1,
		        model_id2,
		        result2,
		        group_name2,
		        group_instance1,
		        group_instance2,
		    )
		    # distance = groups.DistanceGroupToGroup(model_id1, result1, group_name1, model_id2, result2, group_name2, group_instance1, group_instance2, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_group instead.", DeprecationWarning)

def DistanceGroupToLine(group_model: int, group_result: object, group_name: str, node1_model: int, node1_result: object, line_node1: int, node2_model: int, node2_result: object, line_node2: int, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_line` instead.


	This function calculates the distance or the elongation of a group from a line.

	Parameters
	----------
	group_model : int
		Id of the model of the group.

	group_result : object
		An object of class Result that refers to a Resultset of the model for the group.

	group_name : str
		Name of the group.

	node1_model : int
		Id of the model of the 1st node of the line.

	node1_result : object
		An object of class Result that refers to a Resultset of the model for the group for the 1st node of the line.

	line_node1 : int
		Id of the 1st node of the line.

	node2_model : int
		Id of the model of the 2nd node of the line.

	node2_result : object
		An object of class Result that refers to a Resultset of the model for the group for the 2st node of the line.

	line_node2 : int
		Id of the 2nd node of the line.

	group_instance : int
		Instance of the group.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as list elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    line_node1 = 160237
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    line_node2 = 160065
		
		    distance = groups.DistanceGroupToLine(
		        group_model,
		        group_result,
		        group_name,
		        node1_model,
		        node1_result,
		        line_node1,
		        node2_model,
		        node2_result,
		        line_node2,
		        group_instance,
		    )
		    # distance = groups.DistanceGroupToLine(group_model, group_result, group_name, node1_model, node1_result, line_node1, node2_model, node2_result, line_node2, group_instance, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_line instead.", DeprecationWarning)

def DistanceGroupToLineCoords(model_id: int, result: object, group_name: str, point1: object, point2: object, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_line_coords` instead.


	This function calculates the distance or the elongation of a group from a line. Group is specified by its model, name and instance (model_id, group_name, group_instance). Line is specified by the coordinates of two points.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	point1 : object
		The coordinates of the 1st point of the line.

	point2 : object
		The coordinates of the 2nd point of the line.

	group_instance : int
		Instance of the group.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as list elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    point1 = list()
		    point1.append(0.2)
		    point1.append(-1.39)
		    point1.append(2.15)
		
		    point2 = list()
		    point2.append(-1.35)
		    point2.append(-0.4)
		    point2.append(1.5)
		
		    distance = groups.DistanceGroupToLineCoords(
		        model_id, result, group_name, point1, point2, group_instance
		    )
		    # distance = groups.DistanceGroupToLineCoords(model_id, result, group_name, point1, point2, group_instance, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_line_coords instead.", DeprecationWarning)

def DistanceGroupToPlane(group_model: int, group_result: object, group_name: str, node1_model: int, node1_result: object, plane_node1: int, node2_model: int, node2_result: object, plane_node2: int, node3_model: int, node3_result: object, plane_node3: int, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_plane` instead.


	This function calculates the distance or the elongation of a group from a plane.

	Parameters
	----------
	group_model : int
		Id of the model of the group.

	group_result : object
		An object of class Result that refers to a Resultset of the model for the group.

	group_name : str
		Name of the group.

	node1_model : int
		Id of the model of the 1st node of the plane.

	node1_result : object
		An object of class Result that refers to a Resultset of the model for the 1st node of the plane.

	plane_node1 : int
		Id of the 1st node of the plane.

	node2_model : int
		Id of the model of the 2nd node of the plane.

	node2_result : object
		An object of class Result that refers to a Resultset of the model for the 2nd node of the plane.

	plane_node2 : int
		Id of the 2nd node of the plane.

	node3_model : int
		Id of the model of the 3rd node of the plane.

	node3_result : object
		An object of class Result that refers to a Resultset of the model for the 3rd node of the plane.

	plane_node3 : int
		Id of the 3rd node of the plane.

	group_instance : int
		Instance of the group.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as list elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		-  position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    plane_node1 = 160065
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    plane_node2 = 160031
		
		    node3_model = 0
		    all_resultsets = results.Resultsets(node3_model)
		    node3_result = all_resultsets[1]
		    plane_node3 = 160237
		
		    distance = groups.DistanceGroupToPlane(
		        group_model,
		        group_result,
		        group_name,
		        node1_model,
		        node1_result,
		        plane_node1,
		        node2_model,
		        node2_result,
		        plane_node2,
		        node3_model,
		        node3_result,
		        plane_node3,
		        group_instance,
		    )
		    # distance = groups.DistanceGroupToPlane(group_model, group_result, group_name, node1_model, node1_result, plane_node1, node2_model, node2_result, plane_node2, node3_model, node3_result, plane_node3, group_instance, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_plane instead.", DeprecationWarning)

def DistanceGroupToPlaneCoords(model_id: int, result: object, group_name: str, point1: object, point2: object, point3: object, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_plane_coords` instead.


	This function calculates the distance or the elongation of a group from a plane specified by point coordinates.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	point1 : object
		The coordinates of the 1st point of the plane.

	point2 : object
		The coordinates of the 2nd point of the plane.

	point3 : object
		The coordinates of the 3rd point of the plane.

	group_instance : int
		Instance of the group.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as members referring to the corresponding
		distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    point1 = list()
		    point1.append(-1.1)
		    point1.append(-2.1)
		    point1.append(0)
		
		    point2 = list()
		    point2.append(0)
		    point2.append(0)
		    point2.append(0)
		
		    point3 = list()
		    point3.append(0.3)
		    point3.append(0.4)
		    point3.append(0.5)
		
		    distance = groups.DistanceGroupToPlaneCoords(
		        group_model, group_result, group_name, point1, point2, point3, group_instance
		    )
		    # distance = groups.DistanceGroupToPlaneCoords(group_model, group_result, group_name, point1, point2, point3, group_instance, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_plane_coords instead.", DeprecationWarning)

def Groups(all_instances: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function collects all the groups of a model specified by the given id.

	Parameters
	----------
	all_instances : int, optional
		Optional argument 'all_instances' defines if all instances of groups with the same name will be returned from the function. If it is absent, the default value is 0.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the corresponding model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    all_instances = 1
		    model_id = 0
		    all_groups = groups.Groups(model_id, all_instances)
		    for g in all_groups:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def GroupsByName(all_instances: int, group_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function searches for the groups with the given name in the list of groups of the model.

	Parameters
	----------
	all_instances : int, optional
		Defines if all instances of groups with the same name will be returned from the function. If it is absent, then default value is 0.

	group_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    all_instances = 1
		    group_name = "*Grou*"
		    collected_groups = groups.GroupsByName(model_id, group_name, all_instances)
		    for g in collected_groups:
		        print(
		            g.name,
		            g.id,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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
		            g.part_type,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def GroupsByType(all_instances: int, group_type: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function searches for the groups with the given type in the list of groups of the model with the given id.

	Parameters
	----------
	all_instances : int
		Defines if all instances of groups with the same name will be returned from the function. If it is absent, then the default value is 0.

	group_type : str
		Type of the group. Its possible values are:
		- 'part'
		- 'set'
		- 'boundary'
		- 'connection'
		- 'include'

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_type = "part"
		    all_instances = 1
		    collected_groups = groups.GroupsByType(model_id, group_type, all_instances)
		    for g in collected_groups:
		        print(
		            g.name,
		            g.id,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def GroupsFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect groups of a model specified by the given id through some advanced filters. The execution of the script will stop and a window will open in order for the user to specify its advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the given model for the specified avanced filters.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    collected_groups = groups.GroupsFromAdvFilters(model_id, resultset)
		    for g in collected_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

def GroupsOfOverlayRun(all_instances: int, overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_groups` instead.


	This function searches for the groups of an overlay run with a given type and a given id.

	Parameters
	----------
	all_instances : int
		Defines if all instances of groups with the same name will be returned from the function. If it is absent, then default value is 0.

	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_groups = groups.GroupsOfOverlayRun(overlay_run_type, overlay_run_id)
		    for g in overlay_run_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_groups instead.", DeprecationWarning)

def GroupsOfSubgroup(model_id: int, subgroup_name: str, level: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parent_groups` instead.


	This function searches for the parent groups of a subgroup with a given name in the list of the groups of the model with the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	subgroup_name : str
		Name of the subgroup.

	level : int
		Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - 3 levels up etc.). If argument level is absent, then this function will search up all levels for parent groups.

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is an object of class Group referring to one parent group of the given subgroup of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "ChildGroup"
		    level = 1
		    parent_groups = groups.GroupsOfSubgroup(model_id, group_name, level)
		    for g in parent_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parent_groups instead.", DeprecationWarning)

def GroupsOfSubgroupInstance(model_id: int, subgroup_name: str, subgroup_instance: int, level: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parent_groups` instead.


	This function searches for the parent groups of a subgroup with a given name and instance in the list of the groups of the model with the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	subgroup_name : str
		Name of the subgroup.

	subgroup_instance : int
		Instance of the group.

	level : int
		Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - three levels up etc.). If it is absent, then this function will search up all levels for parent groups.

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is an object of class Group referring to one parent group of the given subgroup of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "ChildGroup"
		    group_instance = 1
		    level = 1
		    parent_groups = groups.GroupsOfSubgroupInstance(
		        model_id, group_name, group_instance, level
		    )
		    for g in parent_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parent_groups instead.", DeprecationWarning)

def IsGroup(group: object) -> int:

	"""

	This function checks whether an object is of type Group.

	Parameters
	----------
	group : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class type Group, or 0 if it is not.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import utils
		
		
		def main():
		    models.CollectNewEntitiesStart()
		    # create new entities
		    utils.MetaCommand("groups create pid")
		
		    all_entities = models.CollectNewEntitiesEnd()
		    for ent in all_entities:
		        if groups.IsGroup(ent):
		            g = ent
		            print("This is an object of type Group")
		            print(
		                g.name,
		                g.id,
		                g.model_id,
		                g.module_id,
		                g.version,
		                g.representation,
		                g.study_version,
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
		                g.part_type,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaxCoordinatesOfGroup(model_id: int, group_name: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a group belonging to a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	result : object
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class type Node referring to the node with the maximun coordinate in each direction of the specified group.
		- 0 = Node with the maximum X coordinate
		- 1 = Node with the maximum Y coordinate
		- 2 = Node with the maximum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    max_node = groups.MaxCoordinatesOfGroup(model_id, group_name, result)
		    if max_node:
		        max_x_node = max_node[0]  # Object of the node with the maximum X coordinate
		        print(max_x_node.x)  # X maximum coordinate
		        print(
		            max_x_node.y, max_x_node.z
		        )  # Coordinates in rest directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = max_node[1]  # Object of the node with the maximum Y coordinate
		        print(max_y_node.y)  # Y maximum coordinate
		        print(
		            max_y_node.x, max_y_node.z
		        )  # Coordinates in rest directions of the node with the maximum Y coordinate
		        print(max_y_node.id)  # Id of the node with the maximum Y coordinate
		
		        max_z_node = max_node[2]  # Object of the node with the maximum Z coordinate
		        print(max_z_node.z)  # Z maximum coordinate
		        print(
		            max_z_node.x, max_z_node.y
		        )  # Coordinates in rest directions of the node with the maximum Z coordinate
		        print(max_z_node.id)  # Id of the node with the maximum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_coordinates instead.", DeprecationWarning)

def MaxCoordinatesOfGroupInstance(model_id: int, group_name: str, group_instance: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a group belonging to a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list with 3 Node objects where each element of the list refers to the node with the maximun coordinate in each direction of the specified group.
		- 0 = Node with the maximum X coordinate
		- 1 = Node with the maximum Y coordinate
		- 2 = Node with the maximum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    max_node = groups.MaxCoordinatesOfGroupInstance(
		        model_id, group_name, group_instance, result
		    )
		    if max_node:
		        max_x_node = max_node[0]  # Object of the node with the maximum X coordinate
		        print(max_x_node.x)  # X maximum coordinate
		        print(
		            max_x_node.y, max_x_node.z
		        )  # Coordinates in rest directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = max_node[1]  # Object of the node with the maximum Y coordinate
		        print(max_y_node.y)  # Y maximum coordinate
		        print(
		            max_y_node.x, max_y_node.z
		        )  # Coordinates in rest directions of the node with the maximum Y coordinate
		        print(max_y_node.id)  # Id of the node with the maximum Y coordinate
		
		        max_z_node = max_node[2]  # Object of the node with the maximum Z coordinate
		        print(max_z_node.z)  # Z maximum coordinate
		        print(
		            max_z_node.x, max_z_node.y
		        )  # Coordinates in rest directions of the node with the maximum Z coordinate
		        print(max_z_node.id)  # Id of the node with the maximum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_coordinates instead.", DeprecationWarning)

def MaxDeformationOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 4 deformation objects where each item of the list refers to the maximum deformation in each direction for the specified group.
		- Index 0 = X deformation
		- Index 1 = Y deformation
		- Index 2 = Z deformation
		- Index 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    max_deform = groups.MaxDeformationOfGroup(result, group_name, group_instance)
		    if max_deform:
		        max_x_deform = max_deform[0]  # Object with maximum deformation in direction X
		        print(max_x_deform.x)  # X maximum deformation
		        print(
		            max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformations in rest directions on the node with the maximum X deformation
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[1]  # Object with maximum deformation in direction Y
		        print(max_y_deform.y)  # Y maximum deformation
		        print(
		            max_y_deform.x, max_y_deform.z, max_y_deform.total
		        )  # Deformations in rest directions on the node with the maximum Y deformation
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[2]  # Object with maximum deformation in direction Z
		        print(max_z_deform.z)  # Z maximum deformation
		        print(
		            max_z_deform.x, max_z_deform.y, max_z_deform.total
		        )  # Deformations in rest directions on the node with the maximum Z deformation
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z deformation
		
		        max_total_deform = max_deform[3]  # Object with maximum TOTAL deformation
		        print(max_total_deform.total)  # TOTAL maximum deformation
		        print(
		            max_total_deform.x, max_total_deform.y, max_total_deform.z
		        )  # Deformations in rest directions on the node with the maximum TOTAL deformation
		        print(
		            max_total_deform.node_id
		        )  # Id of the node with the maximum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_deformations instead.", DeprecationWarning)

def MinCoordinatesOfGroup(model_id: int, group_name: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a group belonging to a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	result : object
		An object of class Result that refers to a Resultset of the model. If it is absent, then minimum coordinates will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list with 3 Node objects where each element of the list refers to the node with the minimun coordinate in each direction of the specified group.
		- 0 = Node with the minimum X coordinate
		- 1 = Node with the minimum Y coordinate
		- 2 = Node with the minimum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    min_node = groups.MinCoordinatesOfGroup(model_id, group_name, result)
		    if min_node:
		        min_x_node = min_node[0]  # Object of the node with the minimum X coordinate
		        print(min_x_node.x)  # X minimum coordinate
		        print(
		            min_x_node.y, min_x_node.z
		        )  # Coordinates in rest directions of the node with the minimum X coordinate
		        print(min_x_node.id)  # Id of the node with the minimum X coordinate
		
		        min_y_node = min_node[1]  # Object of the node with the minimum Y coordinate
		        print(min_y_node.y)  # Y minimum coordinate
		        print(
		            min_y_node.x, min_y_node.z
		        )  # Coordinates in rest directions of the node with the minimum Y coordinate
		        print(min_y_node.id)  # Id of the node with the minimum Y coordinate
		
		        min_z_node = min_node[2]  # Object of the node with the minimum Z coordinate
		        print(min_z_node.z)  # Z minimum coordinate
		        print(
		            min_z_node.x, min_z_node.y
		        )  # Coordinates in rest directions of the node with the minimum Z coordinate
		        print(min_z_node.id)  # Id of the node with the minimum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_coordinates instead.", DeprecationWarning)

def MinCoordinatesOfGroupInstance(model_id: int, group_name: str, group_instance: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a group belonging to a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, then the default value is 1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 3 Node objects where each element of the list refers to the node with the minimun coordinate in each direction of the specified group.
		- 0 = Node with the minimum X coordinate
		- 1 = Node with the minimum Y coordinate
		- 2 = Node with the minimum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    min_node = groups.MinCoordinatesOfGroupInstance(
		        model_id, group_name, group_instance, result
		    )
		    if min_node:
		        min_x_node = min_node[0]  # Object of the node with the minimum X coordinate
		        print(min_x_node.x)  # X minimum coordinate
		        print(
		            min_x_node.y, min_x_node.z
		        )  # Coordinates in rest directions of the node with the minimum X coordinate
		        print(min_x_node.id)  # Id of the node with the minimum X coordinate
		
		        min_y_node = min_node[1]  # Object of the node with the minimum Y coordinate
		        print(min_y_node.y)  # Y minimum coordinate
		        print(
		            min_y_node.x, min_y_node.z
		        )  # Coordinates in rest directions of the node with the minimum Y coordinate
		        print(min_y_node.id)  # Id of the node with the minimum Y coordinate
		
		        min_z_node = min_node[2]  # Object of the node with the minimum Z coordinate
		        print(min_z_node.z)  # Z minimum coordinate
		        print(
		            min_z_node.x, min_z_node.y
		        )  # Coordinates in rest directions of the node with the minimum Z coordinate
		        print(min_z_node.id)  # Id of the node with the minimum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_coordinates instead.", DeprecationWarning)

def MinDeformationOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL), of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 4 deformation objects where each item of the list is an object of class Deformation referring to the minimun deformation in each direction for the specified group.
		- Index 0 = X deformation
		- Index 1 = Y deformation
		- Index 2 = Z deformation
		- Index 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    min_deform = groups.MinDeformationOfGroup(result, group_name, group_instance)
		    if min_deform:
		        min_x_deform = min_deform[0]  # Object with minimum deformation in direction X
		        print(min_x_deform.x)  # X minimum deformation
		        print(
		            min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformations in rest directions on the node with the minimum X deformation
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[1]  # Object with minimum deformation in direction Y
		        print(min_y_deform.y)  # Y minimum deformation
		        print(
		            min_y_deform.x, min_y_deform.z, min_y_deform.total
		        )  # Deformations in rest directions on the node with the minimum Y deformation
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[2]  # Object with minimum deformation in direction Z
		        print(min_z_deform.z)  # Z minimum deformation
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.total
		        )  # Deformations in rest directions on the node with the minimum Z deformation
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z deformation
		
		        min_total_deform = min_deform[3]  # Object with minimum TOTAL deformation
		        print(min_total_deform.total)  # TOTAL minimum deformation
		        print(
		            min_total_deform.x, min_total_deform.y, min_total_deform.z
		        )  # Deformations in rest directions on the node with the minimum TOTAL deformation
		        print(
		            min_total_deform.node_id
		        )  # Id of the node with the minimum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_deformations instead.", DeprecationWarning)

def MinMaxCentroidScalarOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 CentroidScalar objects where each item refers to the minimum or maximun centroid scalar value for the specified group.
		- Index 0 = MINIMUM centroid scalar
		- Index 1 = MAXIMUM centroid scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    centroid = groups.MinMaxCentroidScalarOfGroup(result, group_name, group_instance)
		    if centroid:
		        min_centroid = centroid[0]  # Object with minimum centroid scalar value
		        print(min_centroid.value)  # Minimum centroid scalar value
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid scalar value
		
		        max_centroid = centroid[1]  # Object with maximum centroid scalar value
		        print(max_centroid.value)  # Maximum centroid scalar value
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxCentroidVectorOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 CentroidVector objects where each item of the list refers to the minimum or maximun centroid vector value for the specified group.
		- Index 0 = MINIMUM centroid vector
		- Index 1 = MAXIMUM centroid vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    centroid = groups.MinMaxCentroidVectorOfGroup(result, group_name, group_instance)
		    if centroid:
		        min_centroid = centroid[0]  # Object with the minimum centroid vector value
		        print(min_centroid.value)  # Minimum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the minimum centroid vector
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid vector value
		
		        max_centroid = centroid[1]  # Struct with the maximum centroid vector value
		        print(max_centroid.value)  # Maximum centroid vector value
		        print(
		            max_centroid.x, max_centroid.y, max_centroid.z
		        )  # Normalized coordinates (X, Y ,Z) of the maximun centroid vector
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_centroid_vector instead.", DeprecationWarning)

def MinMaxCornerScalarOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 CornerScalar objects where each item of the list is refers to the minimum or maximun corner scalar value for the specified group.
		- Index 0 = MINIMUM corner scalar
		- Index 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    corner = groups.MinMaxCornerScalarOfGroup(result, group_name, group_instance)
		    if corner:
		        min_corner = corner[0]  # Object with the minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the minimum corner scalar value for shells and solids elements, or the fraction of the distance from the start to the total distance for line elements
		
		        max_corner = corner[1]  # Object with the maximum corner scalar value
		        print(max_corner.value)
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element with the maximum corner scalar value
		        print(
		            max_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_scalar instead.", DeprecationWarning)

def MinMaxNodalScalarOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 NodalScalar objects where each item of the list refers to the minimum or maximun nodal scalar value for the specified group.
		- Index 0 = MINIMUM nodal vector
		- Index 1 = MAXIMUM nodal vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    nodal = groups.MinMaxNodalScalarOfGroup(result, group_name, group_instance)
		    if nodal:
		        min_nodal = nodal[0]  # Object with minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal scalar value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Object with maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(max_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxNodalVectorOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector values of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 NodalVector objects where each item of the list refers to the minimum or maximun nodal vector value for the specified group.
		- Index 0 = MINIMUM nodal vector
		- Index 1 = MAXIMUM nodal vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    nodal = groups.MinMaxNodalVectorOfGroup(result, group_name, group_instance)
		    if nodal:
		        min_nodal = nodal[0]  # Object with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Object with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal vector value
		        print(max_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_vector instead.", DeprecationWarning)

def NodalScalarOfGroup(result: object, group_name: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class type NodalScalar referring to the nodal scalar values of a node of the specified group.
		Upon failure, an empty list is returned.rned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    layer = "top"  # TOP nodal scalar values if both bottom and top values are loaded
		    group_nodal = groups.NodalScalarOfGroup(result, group_name, layer)
		    iter_end = min(10, len(group_nodal))
		    for nodal in group_nodal[0:iter_end]:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_scalar instead.", DeprecationWarning)

def NodalScalarOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class type NodalScalar referring to the nodal scalar values of a node of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    layer = "top"  # TOP nodal scalar values if both bottom and top values are loaded
		    group_nodal = groups.NodalScalarOfGroupInstance(
		        result, group_name, group_instance, layer
		    )
		    iter_end = min(10, len(group_nodal))
		    for nodal in group_nodal[0:iter_end]:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfGroup(result: object, group_name: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_vector` instead.


	This function calculates all nodal vector values of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each item of the list is an object of class type NodalVector referring to the nodal vector values of a node of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_nodal = groups.NodalVectorOfGroup(result, group_name)
		    iter_end = min(10, len(group_nodal))
		    for nodal in group_nodal[0:iter_end]:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_vector instead.", DeprecationWarning)

def NodalVectorOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodal_vector` instead.


	This function calculates all nodal vector values of a given group instance belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each item of the list is an object of class type NodalVector referring to the nodal vector values of a node of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_nodal = groups.NodalVectorOfGroupInstance(result, group_name, group_instance)
		    iter_end = min(10, len(group_nodal))
		    for nodal in group_nodal[0:iter_end]:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodal_vector instead.", DeprecationWarning)

def ReportNewGroups() -> object:

	"""

	This function collects the newly created groups from the last call of script function CollectNewGroupsStart(). This function should be preceded by a corresponding call to script function CollectNewGroupsStart() and should be followed by a corresponding call to script function CollectNewGroupsEnd().

	Returns
	-------
	object
		Upon success, it returns a list where each item of the list is an object of class Group referring to one specific newly created group.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import utils
		
		
		def main():
		    groups.CollectNewGroupsStart()
		
		    # Create new groups
		    utils.MetaCommand("groups define MyGroup2")
		
		    new_groups = groups.ReportNewGroups()
		    for g in new_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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
		    groups.CollectNewGroupsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectGroups(all_instances: int, group_type: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.select_groups` instead.


	This function allows the user to select group(s) of model(s) from a given list. The execution of the script will stop and it will restart after the selection of the groups from the list.

	Parameters
	----------
	all_instances : int, optional
		Optional argument 'all_instances' defines if all instances of groups with the same name will be returned from the function. If it is absent, then the default value is 0.

	group_type : str
		Type of groups to be listed. Its possible values are:
		- 'part'
		- 'set'
		- 'boundary'
		- 'connection'
		- 'include'

	model_id : int
		Id of the model. If model_id is equal to -1, then this function will work for all models.

	Returns
	-------
	object
		Upon success, it returns a list where each item of the list is an object of class Group referring to one specific selected group of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_type = "set"
		    all_instances = 0
		
		    selected_groups = groups.SelectGroups(model_id, group_type, all_instances)
		    for g in selected_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.select_groups instead.", DeprecationWarning)

def SetUserDefinedAttributeOfGroup(model_id: int, group_name: str, attribute_name: str, attribute_value: str, group_instance: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.set_user_attribute` instead.


	This function sets a value into a user defined attribute of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	attribute_name : str
		Name of the attribute.

	attribute_value : str
		Value of the attribute.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	int
		Upon success, it returns 1, otherwise it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    attribute_name = "Max_Plastic_Strain"
		    attribute_value = "0.743"
		    group_instance = 1
		
		    ret = groups.SetUserDefinedAttributeOfGroup(
		        model_id, group_name, attribute_name, attribute_value, group_instance
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.set_user_attribute instead.", DeprecationWarning)

def ShellNormalOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_shell_normal` instead.


	This function calculates the shell normal vectors of the SHELL elements of a group belonging to a specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

	group_name : str
		Name of the group.

	group_instance : int
		Optional argument 'group_instance' refers to the instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list with CentroidVector objects where each item of the list refers to the shell normal vector of a SHELL element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_normal = groups.ShellNormalOfGroup(result, group_name, group_instance)
		    iter_end = min(10, len(group_normal))
		    for shell_normal in group_normal[
		        0:iter_end
		    ]:  # List with CentroidVector objects (shell normal vector)
		        print(shell_normal.value)  # Magnitude of the shell normal vector (always 1)
		        print(
		            shell_normal.x, shell_normal.y, shell_normal.z
		        )  # Normalized coordinates (X, Y, Z) of the shell normal vector
		        print(
		            shell_normal.element_id, shell_normal.second_id, shell_normal.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_shell_normal instead.", DeprecationWarning)

def SubgroupsOfGroup(model_id: int, group_name: str, level: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_subgroups` instead.


	This function searches for the subgroups of a group with a given name in the list of the groups of the model with the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	level : int, optional
		Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - three levels up etc.). If it is absent, then this function will search up all levels for parent groups.

	Returns
	-------
	object
		Upon success, it returns a list with Group objects where each item of the list refers to one subgroup of the given group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "ParentGroup"
		    level = 1
		    subgroups = groups.SubgroupsOfGroup(model_id, group_name, level)
		    for g in subgroups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_subgroups instead.", DeprecationWarning)

def SubgroupsOfGroupInstance(model_id: int, group_name: str, group_instance: int, level: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_subgroups` instead.


	This function searches for the subgroups of a group instance with a given name in the list of the groups of the model with the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	level : int, optional
		Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - three levels up etc.). If it is absent, then this function will search up all levels for parent groups.

	Returns
	-------
	object
		Upon success, it returns a list with Group objects where each item of the list refers to one subgroup of the given group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "ParentGroup"
		    group_instance = 1
		    level = 1
		    subgroups = groups.SubgroupsOfGroupInstance(
		        model_id, group_name, group_instance, level
		    )
		    for g in subgroups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_subgroups instead.", DeprecationWarning)

def UpdateGroup(group: object) -> object:

	"""

	This function updates the data of the given Group object. Update is based in the fields 'name' and 'model_id' of the given Group object.

	Parameters
	----------
	group : object
		The given group to update.

	Returns
	-------
	object
		Upon success, it returns the new updated Group object.
		Else, a none is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import utils
		
		
		def main():
		    model_id = 0
		    group_name = "ChildGroup"
		    parent_group_name = "ParentGroup"
		    utils.MetaCommand("groups define " + group_name)
		    utils.MetaCommand("groups define " + parent_group_name)
		
		    collected_groups = groups.GroupsByName(model_id, group_name)
		    if collected_groups:
		        initial_group_object = collected_groups[0]
		
		        # utils.MetaCommand('groups attribute ' + group_name + ' 1 rename "Name" ' + group_name + '1')
		        utils.MetaCommand("groups instmove " + group_name + ' 1 "ParentGroup" 1')
		
		        g = groups.UpdateGroup(initial_group_object)
		        if g:  # Update OK
		            print(
		                g.name,
		                g.id,
		                g.model_id,
		                g.module_id,
		                g.version,
		                g.representation,
		                g.study_version,
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
		                g.part_type,
		            )
		        else:  # Update FAILED
		            print("This is not a valid group struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def UserDefinedAttributeOfGroup(model_id: int, group_name: str, attribute_name: str, group_instance: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_user_attributes` instead.


	This function collects a user defined attribute of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	attribute_name : str
		Name of the attribute.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	str
		It returns a string referring to the value of the user defined attribute of the given group.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    attribute_name = "Max_Plastic_Strain"
		    group_instance = 1
		
		    value = groups.UserDefinedAttributeOfGroup(
		        model_id, group_name, attribute_name, group_instance
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_user_attributes instead.", DeprecationWarning)

def UserDefinedAttributesOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_user_attributes` instead.


	This function collects all user defined attributes of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with the user defined attributes of the given group for the specified model. Each item of the list is another list which contains:
		- index 0: Name of the attribute
		- index 1: Value of the attribute
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    all_attributes = groups.UserDefinedAttributesOfGroup(
		        model_id, group_name, group_instance
		    )
		
		    for one_attribute in all_attributes:
		        attribute_name = one_attribute[0]
		        attribute_value = one_attribute[1]
		        print(attribute_name)
		        print(attribute_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_user_attributes instead.", DeprecationWarning)

def CogCoordinatesOfGroup(result: object, group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_cog_coordinates` instead.


	This function calculates the coordinates of the geometrical center of gravity of all the shell and solid elements of a group of a given model for a specific resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	Returns
	-------
	object
		It returns a list containing the coordinates of the geometrical center of gravity of the specified group.
		Upon failure, invalid coordinates [0 0 0] will be returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    group_name = "MyGroup"
		
		    cog = groups.CogCoordinatesOfGroup(all_resultsets[0], group_name)
		
		    print(str(cog[0]))
		    print(str(cog[1]))
		    print(str(cog[2]))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_cog_coordinates instead.", DeprecationWarning)

def DistanceGroupToCutPlane(group_model: int, group_result: object, group_name: str, plane_name: str, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_distance_from_cut_plane` instead.


	This function calculates the distance or the elongation of a group from an existing cut plane.

	Parameters
	----------
	group_model : int
		Id of the model of the group.

	group_result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	plane_name : str
		Name of plane.

	group_instance : int, optional
		Instance of the Group

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    plane_name = "DEFAULT_PLANE_XY"
		
		    distance = groups.DistanceGroupToCutPlane(
		        group_model, group_result, group_name, plane_name
		    )
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_distance_from_cut_plane instead.", DeprecationWarning)

def CommentOfGroup(model_id: str, group_name: str, group_instance: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_comment` instead.


	This function finds the comment of a given group belonging to the specified model. 

	Parameters
	----------
	model_id : str
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	str
		It returns a string referring to the comment of the given group.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    group_comment = groups.CommentOfGroup(model_id, group_name, group_instance)
		    print(group_comment)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_comment instead.", DeprecationWarning)

def GroupsWithComments(model_id: int, all_instances: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function finds all the groups with comments of a model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	all_instances : int, optional
		0 - Only the first instance of the group will be returned. (default)
		1 - All instances of groups with the same name will be returned from the function.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group with comment of the corresponding model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    all_instances = 1
		    model_id = 0
		    all_groups = groups.GroupsWithComments(model_id, all_instances)
		    for g in all_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def GroupsByComment(model_id: int, group_comment: str, all_instances: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function finds the groups of a model with specific comment.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_comment : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	all_instances : int, optional
		0 - Only the first instance of the group will be returned. (default)
		1 - All instances of groups with the same name will be returned from the function.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the corresponding model.
		Upon failure, an empty list is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    all_instances = 1
		    model_id = 0
		    group_comment = "*comment*"
		    all_groups = groups.GroupsByComment(model_id, group_comment, all_instances)
		    for g in all_groups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def AreaOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_area` instead.


	This function calculates the area of a group with specific name of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then area will refer to the ORIGINAL STATE.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If absent, default value is 1.

	Returns
	-------
	float
		It returns a float value being the calculated area of the specified group.
		Upon failure, an invalid value of 0 will be returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[0]
		    group_name = "MyGroup"
		    group_instance = 1
		    area = groups.AreaOfGroup(result, group_name, group_instance)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_area instead.", DeprecationWarning)

def AreaIntegralOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_area_integral` instead.


	This function calculates the integral of a resultset over the area of a group with specific name of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then area integral will refer to the ORIGINAL STATE.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If absent, default value is 1.

	Returns
	-------
	float
		It returns a float value being the calculated area integral of the specified group.
		Upon failure, an invalid value of 0 will be returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    group_name = "MyGroup"
		    group_instance = 1
		    areaint = groups.AreaIntegralOfGroup(result, group_name, group_instance)
		    print(areaint)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_area_integral instead.", DeprecationWarning)

def VolumeOfGroup(result: object, group_name: int, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_volume` instead.


	This function calculates the volume of a group with specific name and instance of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : int
		Name of the group.

	group_instance : int
		Instance of the group.

	Returns
	-------
	float
		It returns a float value being the calculated volume of the specified group.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[0]
		    group_name = "MyGroup"
		    group_instance = 1
		    volume = groups.VolumeOfGroup(result, group_name, group_instance)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_volume instead.", DeprecationWarning)

def VolumeIntegralOfGroup(result: object, group_name: str, group_instance: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_volume_integral` instead.


	This function calculates the integral of a resultset over the volume of a group with specific name and instance of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then volume integral will refer to the ORIGINAL STATE.

	group_name : str
		Name of the group.

	group_instance : str
		Instance of the group.

	Returns
	-------
	float
		It returns a float value being the calculated volume integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    group_name = "MyGroup"
		    group_instance = 1
		    volume = groups.VolumeIntegralOfGroup(result, group_name, group_instance)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_volume_integral instead.", DeprecationWarning)

def CornerVectorOfGroup(result: object, group_name: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_vector` instead.


	This function calculates all corner vector values of the elements of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	layer : str, optional
		Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerVector referring to one corner vector value of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_corner = groups.CornerVectorOfGroup(result, group_name)
		    iter_end = min(10, len(group_corner))
		    for corn in group_corner[0:iter_end]:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(corn.x)  # Corner X component value
		        print(corn.y)  # Corner Y component value
		        print(corn.z)  # Corner Z component value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_vector instead.", DeprecationWarning)

def CornerVectorOfGroupInstance(result: object, group_name: str, group_instance: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_vector` instead.


	This function calculates all corner vector values of the elements of a given group instance belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	layer : str, optional
		Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerVector referring to the corner vector values of an element of the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    group_corner = groups.CornerVectorOfGroupInstance(
		        result, group_name, group_instance
		    )
		    iter_end = min(10, len(group_corner))
		    for corn in group_corner[0:iter_end]:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(corn.x)  # Corner X component value
		        print(corn.y)  # Corner Y component value
		        print(corn.z)  # Corner Z component value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_vector instead.", DeprecationWarning)

def MinMaxCornerVectorOfGroup(result: object, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_corner_vector` instead.


	This function calculates minimum and maximum corner vector value of a given group belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then the default value is 1.

	Returns
	-------
	object
		It returns a list with 2 CornerVector objects where each item of the list is refers to the minimum or maximun corner scalar value for the specified group.
		- Index 0 = MINIMUM corner scalar
		- Index 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    group_name = "MyGroup"
		    group_instance = 1
		    corner = groups.MinMaxCornerVectorOfGroup(result, group_name, group_instance)
		    if corner:
		        min_corner = corner[0]  # Object with the minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(min_corner.x)  # X component corner value
		        print(min_corner.y)  # Y component corner value
		        print(min_corner.z)  # Z component corner value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the minimum corner scalar value for shells and solids elements, or the fraction of the distance from the start to the total distance for line elements
		
		        max_corner = corner[1]  # Object with the maximum corner scalar value
		        print(max_corner.value)
		        print(max_corner.x)  # X component corner value
		        print(max_corner.y)  # Y component corner value
		        print(max_corner.z)  # Z component corner value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element with the maximum corner scalar value
		        print(
		            max_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_corner_vector instead.", DeprecationWarning)

def AreaWeightedAverageOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_area_weighted_average` instead.


	This function calculates the area weigthed averaged of a group with specific name of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If absent, default value is 1.

	Returns
	-------
	float
		It returns a float value being the calculated area weighted average of the specified group.
		Upon failure,  0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    group_name = "MyGroup"
		
		    area = groups.AreaWeightedAverageOfGroup(all_resultsets[1], group_name)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_area_weighted_average instead.", DeprecationWarning)

def VolumeWeightedAverageOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_volume_weighted_average` instead.


	This function calculates the volume weigthed averaged of a group with specific name of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If absent, default value is 1.

	Returns
	-------
	float
		It returns a float value being the calculated volume weighted average of the specified group.
		Upon failure,  0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    group_name = "MyGroup"
		
		    volume = groups.VolumeWeightedAverageOfGroup(all_resultsets[1], group_name)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_volume_weighted_average instead.", DeprecationWarning)

def NormalForceOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_normal_force` instead.


	This function calculates the normal force of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Type of the part (META constant).

	group_instance : int, optional
		Id of the part.

	Returns
	-------
	float
		It returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    group_name = "MyGroup"
		
		    index = groups.NormalForceOfGroup(all_resultsets[1], group_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_normal_force instead.", DeprecationWarning)

def ShearForceOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_shear_force` instead.


	This function calculates the shear force of a group with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If absent, default value is 1.

	Returns
	-------
	float
		It returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    group_name = "MyGroup"
		
		    index = groups.ShearForceOfGroup(all_resultsets[1], group_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_shear_force instead.", DeprecationWarning)

def IdentifiedGroups(model_id: int, window_name: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function collects all identified groups of a specific model for a specific window.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    identified_groups = groups.IdentifiedGroups(model_id, window_name)
		    for g in identified_groups:
		        print(g.name, g.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def IdentifiedGroupsByType(model_id: int, window_name: str, group_type: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function collects all identified groups of a given type, for a specific model and a specific window.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	group_type : str
		Type of the group. Its possible values are:
		                         - 'part'
		                         - 'set'
		                         - 'include'

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    group_type = "part"
		    identified_groups = groups.IdentifiedGroupsByType(model_id, window_name, group_type)
		    for g in identified_groups:
		        print(g.name, g.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def IsGroupIdentified(model_id: int, group_name: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.is_identified` instead.


	This function checks if an existing group is identfied on a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		The name of the group.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "GroupName"
		    is_identified = groups.IsGroupIdentified(model_id, group_name)
		    print("Is group " + group_name + " identified: " + str(is_identified))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.is_identified instead.", DeprecationWarning)

def IdentifyGroup(model_id: int, group_name: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.identify` instead.


	This function allows to identify a group of a model specified by a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "GroupName"
		    ret = groups.IdentifyGroup(model_id, group_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.identify instead.", DeprecationWarning)

def IdentifySomeGroups(model_id: int, group_names: object):

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_groups` instead.


	This function allows the user to identify some specific groups of a model specified by their names.

	Parameters
	----------
	model_id : int
		The id of the model.

	group_names : object
		List with names of the groups as strings.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_names = []
		    group_names.append("GroupName1")
		    group_names.append("GroupName2")
		    ret = groups.IdentifySomeGroups(model_id, group_names)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_groups instead.", DeprecationWarning)

def ColorOfGroup(model_id: int, group_name: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_color` instead.


	This function finds RGB values and Alpha channel of color of a group of a model with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		The name of the group.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "GroupName"
		    color = groups.ColorOfGroup(model_id, group_name)
		    if color:
		        print(color[0], color[1], color[2], color[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_color instead.", DeprecationWarning)

def GetColorOfGroup(model_id: int, group_name: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_color` instead.


	This function finds color of a group of a model with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		The name of the group.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "GroupName"
		    color = groups.ColorOfGroup(model_id, group_name)
		    if color:
		        print(color[0], color[1], color[2], color[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_color instead.", DeprecationWarning)

def PickGroups(model_id: int, group_type: str, message: str):

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_groups` instead.


	This function allows the user to pick groups of a model specified by the given name. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_type : str
		Type of the group. Its possible values are:
		                         - 'part'
		                         - 'include'
		                         - 'set'

	message : str
		Message displayed to the user.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import groups
		
		
		def main():
		    model_id = -1
		    group_type = "part"
		    message = "Pick an ansapart and press enter"
		    groups_list = groups.PickGroups(model_id, group_type, message)
		    for g in groups_list:
		        print(g.name, g.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_groups instead.", DeprecationWarning)

def GroupsByPartType(model_id: int, group_part_type: str, all_instances: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function finds the groups of a model that are of type 'part', with specific part type.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_part_type : str
		'ansapart' or 'ansagroup'

	all_instances : int
		0 - Only the first instance of the group will be returned. (default)
		1 - All instances of groups with the same name will be returned from the function.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    all_instances = 1
		    model_id = 0
		    group_part_type = "ansapart"
		    all_groups = groups.GroupsByPartType(model_id, group_part_type, all_instances)
		    for g in all_groups:
		        print(
		            g.name,
		            g.id,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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
		            g.part_type,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def AttributeOfGroup(model_id: int, group_name: str, attribute_name: str, instance: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The id of the model

	group_name : str
		The name of the group

	attribute_name : str
		The name of the attribute

	instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "SET1"
		    instance = "Category"
		    val = groups.AttributeOfGroup(model_id, group_name, instance)
		    print("Value: " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_attributes instead.", DeprecationWarning)

def SetAttributeOfGroup(model_id: int, group_name: str, attribute_name: str, attribute_value: object, instance: int, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given group. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_id : int
		The number of the model.

	group_name : str
		The name of the group.

	attribute_name : str
		Name of the attribute.

	attribute_value : object
		Value of the attribute. It can be either a number or a string.

	instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "SET1"
		    attribute_name = "Test"
		    attribute_value = "Value"
		    val = groups.SetAttributeOfGroup(
		        model_id, group_name, attribute_name, attribute_value
		    )
		    print(val)
		    # or
		    attribute_name = "num_test"
		    attribute_value = 1.1
		    instance = 2
		    attribute_type = "numerical"
		    val = groups.SetAttributeOfGroup(
		        model_id, group_name, attribute_name, attribute_value, instance, attribute_type
		    )
		    print(val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.set_attribute instead.", DeprecationWarning)

def AttributesOfGroup(model_id: int, group_name: str, instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_attributes` instead.


	This function collects all attributes of a given group

	Parameters
	----------
	model_id : int
		The id of the model

	group_name : str
		The name of the group

	instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_name = "SET1"
		
		    all_attributes = groups.AttributesOfGroup(model_id, group_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_attributes instead.", DeprecationWarning)

def VisibleGroups(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function collects all visible groups of the model specified by the given id.

	Parameters
	----------
	window_name : str
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one specific group of the given model for the specified window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_groups = groups.VisibleGroups(model_id, window_name)
		    for g in visible_groups:
		        print(g.name, g.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def VisibleGroupsByType(model_id: int, group_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_groups` instead.


	This function collects all visible groups of a specific type, for the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_type : str
		Type of the group. Its possible values are:
		- 'part'
		- 'set'
		- 'boundary'
		- 'connection'
		- 'include'

	window_name : str
		Refers to the name of the window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Group referring to one group of the specific type, for the specified model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_groups = groups.VisibleGroupsByType(model_id, "part", window_name)
		    for g in visible_groups:
		        print(g.name, g.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_groups instead.", DeprecationWarning)

def IdentifyGroupsReset(model_id: int, group_names: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_groups` instead.


	This function allows the user to reset the identification of all or specific groups of the specified model. It can be called with two different ways. The one is with lists of group names, and the other is with group_names = 'all'.

	Parameters
	----------
	model_id : int
		The id of the model.

	group_names : object
		List with names of the groups as strings, or string 'all'

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    model_id = 0
		    group_names = ["group1", "group2", "group3", "group4"]
		    # or
		    # group_names = 'all')
		    groups.IdentifyGroupsReset(model_id, group_names)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_groups instead.", DeprecationWarning)

def GroupsOfElements(model_id: int, elements: object) -> object:

	"""

	This function finds the groups that contains the specified elements of the given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	elements : object
		List of objects of class Element.

	Returns
	-------
	object
		It returns a list that contains a list of group objects for every given element.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    win = windows.Window("MetaPost", page_id=0)
		    specifier = "visible"
		    elems = model.get_elements(specifier, window=win)
		    model_id = model.id
		    grs = groups.GroupsOfElements(model_id, elems)
		    print(grs)
		
		    # or
		    # model_id = 0
		    # element_types = [e.type for e in elems]
		    # element_ids = [e.id for e in elems]
		    # second_ids = [e.second_id for e in elems]
		
		    # grs = groups.GroupsOfElements(model_id, element_types, element_ids, second_ids)
		    # print(grs)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Group():

	"""

	Class for groups.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    g = groups.Group(name="group_name", model_id=0)
		    if g:
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
		
		# method: get_model
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    r = group.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_parent_groups
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    pgroups = group.get_parent_groups()
		    # level = 2
		    # pgroups = group.get_parent_groups(level)
		    for r in pgroups:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_subgroups
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    child = groups.Group(name="child", model_id=m.id)
		    ret = group.set_subgroup(child)
		    print(ret)
		    subgroups = group.get_subgroups()
		    # level = 2
		    # subgroups = group.get_subgroups(level)
		    for g in subgroups:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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
		
		
		# method: get_parts
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    parts = group.get_parts(specifier)
		    # parts = group.get_parts('all', type = constants.PSOLID)
		    for p in parts:
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    # specifier = 'visible'
		    # parts = group.get_parts(specifier, window = w)
		    # parts = group.get_parts(specifier, window = w, type = constants.PSOLID)
		    for p in parts:
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
		
		# method: get_elements
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    elems = group.get_elements(specifier)
		    # type=constants.SOLID
		    # elems = group.get_elements(specifier, type)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    elems = group.get_elements(specifier, window=w)
		    # elems = group.get_elements(specifier, window = w, type=constants.SOLID)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    elems = group.get_elements(specifier, point_coordinates=point)
		    # elems = group.get_elements(specifier, point_coordinates = point, resultset =res )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    group_nodes = group.get_nodes(specifier)
		    for n in group_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    group_nodes = group.get_nodes(specifier, window=w)
		    # specifier = 'identified'
		    # group_nodes = group.get_nodes(specifier, window = w )
		    for n in group_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    group_nodes = group.get_nodes(
		        specifier, distance_type="xyz", point_coordinates=point
		    )
		    # group_nodes = group.get_nodes(specifier, distance_type = 'xyz', point_coordinates = point, resultset = res)
		    for n in group_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_boundaries
		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    group = groups.Group(name="group_name", model_id=0)
		    specifier = "all"
		    bounds = group.get_boundaries(specifier)
		    print(bounds)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_materials
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    mats = group.get_materials()
		    # type=constants.MAT1
		    # mats = group.get_materials(type)
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: is_identified
		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    group = groups.Group(name="group_name", model_id=0)
		    ret = group.is_identified()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_comment
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    comment = group.get_comment()
		    print(comment)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_user_attributes
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    attribute_name = "attr"
		    attribute_value = "test"
		    ret = group.set_user_attribute(attribute_name, attribute_value)
		    print(ret)
		    attr = group.get_user_attributes()
		    # attribute_name ='attr'
		    # attr = group.get_user_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = group.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = group.get_attributes()
		    # attribute_name ='attr'
		    # attr = group.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group1 = groups.Group(name="group_name", model_id=m.id)
		    group2 = groups.Group(name="group_name2", model_id=m.id)
		    dist = group1.get_distance_from_group(res, group2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group1 = groups.Group(name="group_name", model_id=m.id)
		    group2 = groups.Group(name="group_name2", model_id=m.id)
		    elong = group1.get_elongation_from_group(res, group2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_node
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node = nodes.Node(id=100, model_id=m.id)
		    dist = group.get_distance_from_node(res, node, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_node
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node = nodes.Node(id=100, model_id=m.id)
		    elong = group.get_elongation_from_node(res, node, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    elem = elements.Element(id=100, type=constants.SHELL, second_id=-1, model_id=m.id)
		    dist = group.get_distance_from_element(res, elem, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    elem = elements.Element(id=100, type=constants.SHELL, second_id=-1, model_id=m.id)
		    elong = group.get_elongation_from_element(res, elem, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    dist = group.get_distance_from_part(res, part, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    elong = group.get_elongation_from_part(res, part, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_boundary
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    bound = boundaries.Boundary(id=1, type=constants.SPC, second_id=0, model_id=m.id)
		    dist = group.get_distance_from_boundary(res, bound, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_boundary
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    bound = boundaries.Boundary(id=1, type=constants.SPC, second_id=0, model_id=m.id)
		    elong = group.get_elongation_from_boundary(res, bound, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_cut_plane
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    plane = planes.Plane(name="plane_name")
		    dist = group.get_distance_from_cut_plane(res, plane)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_cut_plane
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    plane = planes.Plane(name="plane_name")
		    elong = group.get_elongation_from_cut_plane(res, plane)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_line
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=10, model_id=m.id)
		    dist = group.get_distance_from_line(res, node1, res, node2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_line
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=10, model_id=m.id)
		    elong = group.get_elongation_from_line(res, node1, res, node2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_plane
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=10, model_id=m.id)
		    node3 = nodes.Node(id=100, model_id=m.id)
		    dist = group.get_distance_from_plane(res, node1, res, node2, res, node3, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_plane
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=10, model_id=m.id)
		    node3 = nodes.Node(id=100, model_id=m.id)
		    elong = group.get_elongation_from_plane(res, node1, res, node2, res, node3, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_line_coords
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    point1 = [-1.1, -2.1, 0]
		    point2 = [0, 0, 0]
		    dist = group.get_distance_from_line_coords(res, point1, point2)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_line_coords
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    point1 = [-1.1, -2.1, 0]
		    point2 = [0, 0, 0]
		    val = group.get_elongation_from_line_coords(res, point1, point2)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    point1 = [-1.1, -2.1, 0]
		    point2 = [0, 0, 0]
		    point3 = [0.1, 0.2, 0.3]
		    dist = group.get_distance_from_plane_coords(res, point1, point2, point3)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_elongation_from_plane_coords
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    point1 = [-1.1, -2.1, 0]
		    point2 = [0, 0, 0]
		    point3 = [0.1, 0.2, 0.3]
		    elong = group.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    coords = group.get_coordinates(specifier)
		    # specifier = 'min'
		    # coords =  group.get_coordinates(specifier, resultset=res)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "min"
		    group_deforms = group.get_deformations(resultset, specifier)
		    for deform in group_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "min"
		    group_nodal = group.get_nodal_scalar(resultset, specifier)
		    # specifier = 'max'
		    # group_nodal =  group.get_nodal_scalar(resultset, specifier, layer = 'top')
		    for nodal in group_nodal:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "node"]
		
		    values, nodes = group.get_nodal_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    resultset = res
		    specifier = "min"
		    group_nodal = group.get_nodal_vector(resultset, specifier)
		    # specifier = 'max'
		    # group_nodal =  group.get_nodal_vector(resultset, specifier, layer = 'top')
		    for nodal in group_nodal:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, magn, nodes = group.get_nodal_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "min"
		    group_centroid = group.get_centroid_scalar(resultset, specifier)
		    # specifier = 'max'
		    # group_centroid =  group.get_centroid_scalar(resultset, specifier, layer = 'top')
		    for centroid in group_centroid:
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element"]
		
		    values, elems = group.get_centroid_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "min"
		    group_centroid = group.get_centroid_vector(resultset, specifier)
		    # specifier = 'max'
		    # group_centroid =  group.get_centroid_vector(resultset, specifier, layer = 'top')
		    # group_centroid =  group.get_centroid_vector(resultset, specifier, layer = 'top', principal = 'second')
		    for centroid in group_centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Value and Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element"]
		
		    xyz, magn, elems = group.get_centroid_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    resultset = res
		    specifier = "min"
		    group_corner = group.get_corner_scalar(resultset, specifier)
		    # specifier = 'max'
		    # group_centroid =  group.get_corner_scalar(resultset, specifier, layer = 'top')
		    for corn in group_corner:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element", "corner_id"]
		
		    values, elems, corners = group.get_corner_scalar(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(values)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_corner_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import groups
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    resultset = res
		    specifier = "min"
		    group_corner = group.get_corner_vector(resultset, specifier)
		    # specifier = 'max'
		    # group_corner =  group.get_corner_vector(resultset, specifier, layer = 'top')
		    for corn in group_corner:  # Matrix with corner_scalar structs
		        print(corn.value)  # Corner scalar value
		        print(corn.x)  # Corner X component value
		        print(corn.y)  # Corner Y component value
		        print(corn.z)  # Corner Z component value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the elementprint(corn.element_id, corn.second_id, corn.type)
		        print(
		            corn.corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    group = groups.Group(name="group_name", model_id=m.id)
		    np_specifier = ["xyz", "magnitude", "element", "corner_id"]
		
		    xyz, magn, elems, corners = group.get_corner_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="bolts", model_id=m.id)
		    centroids = group.get_shell_normal(res)
		    for centroid in centroids:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_cog_coordinates
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_cog_coordinates(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_node_cog_coordinates
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_node_cog_coordinates(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_area
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_area(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_volume
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_volume(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_area_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_volume_integral
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_volume_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_area_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_volumetric_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_volume_weighted_average
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_volume_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_mass_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_mass_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_normal_force
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_normal_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_shear_force
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_shear_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_vector_uniformity_index
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    val = group.get_vector_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = group.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_name = 'attr'
		    # attribute_type = 'numerical'
		    # attribute_value = 11.2
		    # ret =  group.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attribute_name = "attr"
		    attr = group.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_user_attribute
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    attribute_name = "attr"
		    attribute_value = "test"
		    ret = group.set_user_attribute(attribute_name, attribute_value)
		    print(ret)
		    attribute_name = "attr"
		    attr = group.get_user_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_subgroups
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    child = groups.Group(name="child", model_id=m.id)
		    g = group.set_subgroup(child)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
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
		
		# method: add_parts
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "visible"
		    vis_parts = m.get_parts(specifier, window=win)
		    val = group.add_parts(vis_parts)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: add_elements
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "visible"
		    vis_elems = m.get_elements(specifier, window=win)
		    val = group.add_elements(vis_elems)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_boundaries
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    bounds = group.get_boundaries(specifier)
		    # type = constants.MPC
		    # bounds = group.get_boundaries(specifier, type)
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    bounds = group.get_boundaries(specifier, window=w)
		    # specifier = 'visible'
		    # bounds = group.get_boundaries(specifier, type = constants.MPC, window = w )
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: add_nodes
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "identified"
		    nodes = m.get_nodes(specifier, window=win)
		    val = group.add_nodes(nodes)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: add_materials
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		from meta import windows
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    specifier = "all"
		    mats = m.get_materials(specifier, material_type=constants.MAT1)
		    val = group.add_materials(mats)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: create_section
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    sec = group.create_section()
		    if sec:
		        print(sec.name, sec.creation_type, sec.sum_point, sec.coord_system)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: delete
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    ret = group.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: identify
		# PYTHON script
		import meta
		from meta import groups
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group = groups.Group(name="group_name", model_id=m.id)
		    ret = group.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: is_usable
		# PYTHON script
		import meta
		from meta import groups
		
		
		def main():
		    g = groups.Group(name="group_name", model_id=0)
		    can_use = g.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_normal_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    gr = groups.Group(name="my_group", model_id=m.id)
		    res = m.get_current_resultset()
		    val = gr.get_normal_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_shear_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    gr = groups.Group(name="my_group", model_id=m.id)
		    res = m.get_current_resultset()
		    val = gr.get_shear_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the group.

	"""

	model_id: int = None
	"""
	Model id of the group.

	"""

	module_id: str = None
	"""
	Module id.

	"""

	version: str = None
	"""
	Version.

	"""

	representation: str = None
	"""
	Representation.

	"""

	study_version: str = None
	"""
	Study version.

	"""

	vsc_number: str = None
	"""
	VSC number.

	"""

	target_mass: float = None
	"""
	Target mass.

	"""

	user_group: str = None
	"""
	User group.

	"""

	pid_offset: int = None
	"""
	Pid offset.

	"""

	freeze: int = None
	"""
	Freeze.

	"""

	type: str = None
	"""
	Type of the group ('part', 'set', 'boundary', 
	'connection', 'include').

	"""

	instance: int = None
	"""
	Instance of the group.

	"""

	is_color_active: int = None
	"""
	Is color active option of group

	"""

	part_type: str = None
	"""
	In case of part ( type == 'part' ), defines 
	the type of part ('ansagroup','ansapart'). 
	Else, an empty string is returned.

	"""

	id: int = None
	"""
	Id of the set ( -1 if no id is available )

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the group.


		Returns
		-------
		object
			Upon success, it returns an object of class Model. Upon failure, it returns None.

		"""


	def get_parent_groups(self, level: object) -> object:

		"""

		This method gets the parent groups of the group.


		Parameters
		----------
		level : object, optional
			Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - 3 levels up etc.). If argument level is absent, then this function will search up all levels for parent groups.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Group referring to one parent group of the given subgroup of the specified model.Upon failure, an empty list is returned.

		"""


	def get_subgroups(self, level: int) -> object:

		"""

		This method gets the subgroups of the group.


		Parameters
		----------
		level : int, optional
			Defines the depth of searching for parent groups (1 - one level up, 2 - two levels up, 3 - three levels up etc.). If it is absent, then this function will search up all levels for parent groups.

		Returns
		-------
		object
			Upon success, it returns a list with Group objects where each item of the list refers to one subgroup of the given group of the specified model.Upon failure, an empty list is returned.

		"""


	def get_parts(self, specifier: str, type: int, window: object) -> object:

		"""

		This method gets the parts of the group.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all parts of the group. Optionally combined with argument: type.
			- 'visible' : visible parts of the group. Optionally combined with arguments: window, type.

		type : int, optional
			The type of the part that the method will return. If absent, parts of all types will returned.

		window : object, optional
			An object of class window. It is used when the specifier is 'visible'. If this argument is set, the method will return only the visible parts in this window.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class Part referring to one specific part of the given group.Upon failure, an empty list is returned.

		"""


	def get_elements(self, specifier: str, type: int, window: object, point_coordinates: object, resultset: object, range: str) -> object:

		"""

		This method gets the elements of the group.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all elements of the group (default value).
			- 'visible' : visible elements of the group.
			- 'nearest' : nearest element of the part from a specific point.Specifier of the method. Its possible values are:
			- 'all' : all elements of the group.
			- 'visible' : visible elements of the group.
			- 'nearest' : nearest element of the part from a specific point.
			- 'range' : Provide a range of Element Ids in the argument range.

		type : int, optional
			The type of the element that the method will return. Used when the specifier is 'all', 'visible', 'nearest'. If absent, elements of all types will returned.

		window : object, optional
			An object of class Window. Used only if specifier is 'visible'. If this argument is set, the method will return only the visible elements in this window.

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE. Used only when the specifier is 'nearest'.

		range : str, optional
			Element Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class Element referring to one specific element of the group. Upon failure, an empty list is returned.

		"""


	def get_nodes(self, specifier: str, distance_type: str, window: object, point_coordinates: object, resultset: object, range: str) -> object:

		"""

		This method gets the nodes of the group.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the nodes of the group (default value).
			- 'visible' : visible nodes of the group. Optionally combined with argument: window.
			- 'identified' : identified nodes of the group. Optionally combined with argument: window.
			- 'nearest' : nearest node of the group from a specific point. Must be combined with arguments: distance_type, point_coordinates.  Optionally combined with argument: resultset.
			- 'range' : Provide a range of Node Ids in the argument range.

		distance_type : str, optional
			Type of the distance. Possible values are:
			- 'xyz': XYZ distance
			- 'xy': XY distance
			- 'yz': YZ distance
			- 'zx': ZX distance
			- 'x': X distance
			- 'y': Y distance
			- 'z': Z distance
			It is required when the specifier is 'nearest'.

		window : object, optional
			An object of class window. This argument is used when specifier is 'visible' or 'identified'. If the specifier has a different value, this argument is ignored. If this argument is set, the method will return only the visible nodes in this window.

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. It is used when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		range : str, optional
			Node Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node. Upon failure, it returns an empty list.

		"""


	def get_boundaries(self, specifier: str, type: int, window: object) -> object:

		"""

		This method gets the boundary elements of the group.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all boundary elements of the group. Optionally combined with argument: type.
			- 'visible' : visible boundary elements of the group. Optionally combined with arguments: window, type.

		type : int, optional
			The type of the boundary element that the method will return. If absent, boundary elements of all types will returned.

		window : object, optional
			An object of class Window. This argument is used when the specifier is 'visible'. If this argument is set, the method will return only the visible boundaries in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Boundary. Upon failure, it returns an empty list.

		"""


	def get_materials(self, type: int) -> object:

		"""

		This method gets the materials of the group.


		Parameters
		----------
		type : int, optional
			The type of the material that the method will return. If absent, materials of all types will returned.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Material. Upon failure, it returns an empty list.

		"""


	def is_identified(self) -> object:

		"""

		This method checks if the group is identfied.


		Returns
		-------
		object
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def get_color(self, window: object) -> object:

		"""

		This method gets the color of the group.


		Parameters
		----------
		window : object, optional
			An object of class Window.

		Returns
		-------
		object
			It returns an object of class Color.

		"""


	def get_comment(self) -> str:

		"""

		This method gets the comments of the group.


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the group. Upon failure, it returns None.

		"""


	def get_user_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the user attributes of the group.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the group.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_distance_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the distance from a group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		group : object
			An object of class group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model of the given group.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the elongation from a group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		group : object
			An object of class Group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model of the given group.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the distance from a node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node : object
			An object of class Node.

		node_resultset : object
			An object of class Result that refers to a Resultset of the model of the given node.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the elongation from a node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node : object
			An object of the class Node.

		node_resultset : object
			An object of class Result that refers to a Resultset of the model of the given node.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the distance from an element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		element : object
			An object of class Element.

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the elongation from an element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		element : object
			An object of class Element.

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance from a part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		part : object
			An object of class part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the elongation from a part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		part : object
			An object of class part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the distance from a boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		boundary : object
			An object of class Boundary.

		boundary_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given boundary element.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the elongation from a boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		boundary : object
			An object of class Boundary.

		boundary_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given boundary element.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the distance from a cutplane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		plane : object
			An object of the class Plane.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the elongation from a cut plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		plane : object
			An object of class Plane.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the distance from a line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node2.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the elongation from a line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node2.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the distance from a plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node2.

		node3 : object
			An object of class Node.

		node3_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node3.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the elongation from a plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node2.

		node3 : object
			An object of class Node.

		node3_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node3.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the distance from a line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		point1 : object
			List with the coordinates of the first point of the line.

		point2 : object
			List with the coordinates of the second point of the line.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the elongation from a line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		point1 : object
			List with the coordinates of the first point of the line.

		point2 : object
			List with the coordinates of the second point of the line.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the distance from a plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		point1 : object
			List with the coordinates of the first point of the plane.

		point2 : object
			List with the coordinates of the second point of the plane.

		point3 : object
			List with the coordinates of the third point of the plane.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance. Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the elongation from a plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		point1 : object
			List with the coordinates of the first point of the plane.

		point2 : object
			List with the coordinates of the second point of the plane.

		point3 : object
			List with the coordinates of the third point of the plane.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation. Upon failure, an empty list is returned.

		"""


	def get_coordinates(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the maximum or the minimum coordinates in each direction (X, Y, Z) of the group.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar of the group.
			- 'max' : maximum nodal scalar of the group.
			- 'min' : minimum nodal scalar of the group.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			It returns a list with 3 objects of class Node that correspond to the nodes with the maximum coordinates in each direction of the specified group.- Index 0 contains the Node with the maximum X coordinate- Index 1 contains the Node with the maximum Y coordinate- Index 2 contains the Node with the maximum Z coordinate. Upon failure, an empty list is returned.

		"""


	def get_deformations(self, resultset: object, specifier: str, numpy: object) -> object:

		"""

		This method gets deformations for each direction (X, Y, Z, TOTAL), of the group belonging to the specified model. 


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar of the group.
			- 'max' : maximum nodal scalar of the group.
			- 'min' : minimum nodal scalar of the group.

		numpy : object, optional
			Specifier for returning deformations as numpy arrays. If not set the method will return a list of Deformation objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'xyz': returns a numpy array of three numpy arrays for x, y, z, values.
			'magnitude': returns a numpy array for magnitude values.
			'node': returns a list of Node objects.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class type Deformation referring to the deformation of a node for the group.Upon failure, an empty list is returned.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal scalar values of the nodes of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar of the group.
			- 'max' : maximum nodal scalar of the group.
			- 'min' : minimum nodal scalar of the group.

		layer : str, optional
			Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		numpy : object, optional
			Specifier for returning nodal scalar results as numpy arrays. If not set the method will return a list of NodalScalar objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'value': returns a numpy array for nodal scalar values.
			'node': returns a list of Node objects.
			'part_id': returns a numpy array for property ids.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class type NodalScalar referring to the nodal scalar values of a node of the group. Upon failure, an empty list is returned.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal vector values of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector of the group.
			- 'max' : maximum nodal vector of the group.
			- 'min' : minimum nodal vector of the group.

		layer : str, optional
			Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		numpy : object, optional
			Specifier for returning nodal vectors results as numpy arrays. If not set the method will return a list of NodalVector objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'xyz': returns a numpy array of three numpy arrays for x, y, z, values.
			'magnitude': returns a numpy array for magnitude values.
			'node': returns a list of Node objects.
			'part_id': returns a numpy array for property ids.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each item of the list is an object of class type NodalVector referring to the nodal vector values of a node of the group. Upon failure, an empty list is returned.

		"""


	def get_centroid_scalar(self, resultset: object, specifier: str, layer: str, non_zero: bool, exclude_novalue: bool, numpy: object) -> object:

		"""

		This method gets the centroid scalar values of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all centroid scalar of the group.
			- 'max' : maximum centroid scalar of the group.
			- 'min' : minimum centroid scalar of the group.

		layer : str, optional
			Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		non_zero : bool, optional
			If True, the method will return only the non zero values. The default value is False.

		exclude_novalue : bool, optional
			If True, the method will not return anything for elements that have no value. The default value is False. If non_zero is True, this argument is ignored.

		numpy : object, optional
			Specifier for returning centroid scalar results as numpy arrays. If not set the method will return a list of CentroidScalar objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'value': returns a numpy array for centroid scalar values.
			'element': returns a list of Element objects.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of an element of the group. Upon failure, an empty list is returned.

		"""


	def get_centroid_vector(self, resultset: object, specifier: str, layer: str, principal: str, numpy: object) -> object:

		"""

		This method gets the centroid vector values of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all centroid vector of the group.
			- 'max' : maximum centroid vector of the group.
			- 'min' : minimum centroid vector of the group.

		layer : str, optional
			Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		principal : str, optional
			Principal order of the centroid vector tensor values. It should be specified only when tensor results have been loaded. Possible values are:
			- 'first': first principal (default)
			- 'second': second principal
			- 'third': third principal

		numpy : object, optional
			Specifier for returning centroid vector results as numpy arrays. If not set the method will return a list of CentroidVector objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'xyz': returns a numpy array of three numpy arrays for x, y, z, values.
			'magnitude': returns a numpy array for magnitude values.
			'element': returns a list of Element objects.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector values of an element of the group. Upon failure, an empty list is returned.

		"""


	def get_corner_scalar(self, resultset: object, specifier: object, layer: str, numpy: object) -> object:

		"""

		This method gets the corner scalar values of the elements of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar of the group.
			- 'max' : maximum corner scalar of the group.
			- 'min' : minimum corner scalar of the group.

		layer : str
			Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		numpy : object, optional
			Specifier for returning corner scalar results as numpy arrays. If not set the method will return a list of CornerScalar objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'value': returns a numpy array for centroid scalar values.
			'element': returns a list of Element objects.
			'corner_id': returns a numpy array for corner ids.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of an element of the group. Upon failure, an empty list is returned.

		"""


	def get_corner_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the corner vector values of the elements of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector of the group.
			- 'max' : maximum corner vector of the group.
			- 'min' : minimum corner vector of the group.

		layer : str, optional
			Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		numpy : object, optional
			Specifier for returning corner vector results as numpy arrays. If not set the method will return a list of CornerVector objects.
			This argument accepts a list of strings, which controls what this method will return. The possible values are:
			'xyz': returns a numpy array of three numpy arrays for x, y, z, values.
			'magnitude': returns a numpy array for magnitude values.
			'element': returns a list of Element objects.
			'corner_id': returns a numpy array for corner ids.
			If more than one arguments are set, then a tuple will be returned.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class CornerVector referring to one corner vector value of an element of the group. Upon failure, an empty list is returned.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vectors of the SHELL elements of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list with CentroidVector objects where each item of the list refers to the shell normal vector of a SHELL element of the group.Upon failure, an empty list is returned.

		"""


	def get_cog_coordinates(self, resultset: object) -> object:

		"""

		This method gets the coordinates of the geometrical center of gravity of all the shell and solid elements of the group for the specific resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon succes, it returns a list containing the coordinates of the geometrical center of gravity of the group.Upon failure, it returns None.

		"""


	def get_area(self, resultset: object) -> float:

		"""

		This method gets the area of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated area of the specified group.Upon failure, None will be returned.

		"""


	def get_volume(self, resultset: object) -> float:

		"""

		This method gets the volume of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated volume of the group.Upon failure, None will be returned.

		"""


	def get_area_integral(self, resultset: object) -> float:

		"""

		This method gets the integral of a resultset over the area of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated area integral of the group.Upon failure, None will be returned.

		"""


	def get_volume_integral(self, resultset: object) -> float:

		"""

		This method gets the integral of a resultset over the volume of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated volume integral.Upon failure, None will be returned.

		"""


	def get_area_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the area weigthed averaged of a group with specific name of a given model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated area weighted average of the group.Upon failure, None will be returned.

		"""


	def get_volume_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the volume weigthed averaged of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated volume weighted average of the group.Upon failure, None will be returned.

		"""


	def get_volumetric_flow(self, resultset: object) -> float:

		"""

		This method gets the volumetric flow rate of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated volumetric flow rate of the group.Upon failure, None will be returned.

		"""


	def get_mass_flow(self, resultset: object) -> float:

		"""

		This method gets the mass flow rate of a group with specific name of a given model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated mass flow rate of the group.Upon failure, None will be returned.

		"""


	def get_mass_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the weighted average mass flow of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated mass flow rate of the group.Upon failure, None will be returned.

		"""


	def get_normal_force(self, resultset: object) -> object:

		"""

		This method gets the normal force of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			It returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""


	def get_shear_force(self, resultset: object) -> object:

		"""

		This method gets the shear force of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			It returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""


	def get_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the uniformity index of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the uniformity index of the group.Upon failure, None will be returned.

		"""


	def get_vector_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the vector uniformity index of a group with specific name of a given model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value being the vector uniformity index of the group.Upon failure, None will be returned.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This function sets the value of a specific User Specified attribute referring to a given group. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. Its possible values are:
			-'string': String
			-'numerical': Number

		attribute_value : object
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_user_attribute(self, attribute_name: str, attribute_value: str) -> object:

		"""

		This method sets a value into a user defined attribute of the group.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_value : str
			Value of the attribute.

		Returns
		-------
		object
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_subgroup(self) -> object:

		"""


		Returns
		-------
		object

		"""


	def identify(self) -> bool:

		"""

		This method allows to identify the group. This method works only for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the group.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def add_parts(self, parts: object) -> bool:

		"""

		This method adds some specific parts on the group.


		Parameters
		----------
		parts : object
			A list of objects of class Part, that will be added to the group.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def add_elements(self, elements: object) -> bool:

		"""

		This method adds some specific elements on the group.


		Parameters
		----------
		elements : object
			A list of objects of class Element, that will be added to the group.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def add_boundaries(self, boundaries: object) -> bool:

		"""

		This method adds some specific boundary elements on the group.


		Parameters
		----------
		boundaries : object
			A list of objects of class Boundary, that will be added to the group.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def add_nodes(self, nodes: object) -> bool:

		"""

		This method adds some specific nodes on the group.


		Parameters
		----------
		nodes : object
			A list of objects of class Node, that will be added to the group.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def add_materials(self, materials: object) -> bool:

		"""

		This method adds some specific materials of a model on an existing group.


		Parameters
		----------
		materials : object
			A list of objects of class Material, that will be added to the group.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def create_section(self) -> object:

		"""

		This method creates a section from the group.


		Returns
		-------
		object
			It returns an object of class Section, if creation was successful, otherwise None.

		"""


	def set_subgroup(self, group: object, link: bool) -> object:

		"""

		This method sets a given group subgroup of the group.


		Parameters
		----------
		group : object
			The child group.

		link : bool, optional
			Defines if the child group will be moved or linked to its new position. If True, the group will be linked to its new position. Else it will be moved. The default value is False.

		Returns
		-------
		object
			Upon success, it returns a Group object referring to the subgroup.Else, None is returned.

		"""


	def get_node_cog_coordinates(self, resultset: object):

		"""

		This method gets the coordinates of the geometrical center of gravity of all the nodes of the group for the specific resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Group entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_normal_moment(self, resultset: object) -> object:

		"""

		This method gets the normal moment of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude. Upon failure, an empty list is returned.

		"""


	def get_shear_moment(self, resultset: object) -> object:

		"""

		This method gets the shear moment of the group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""

