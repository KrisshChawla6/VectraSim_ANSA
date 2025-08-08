from __future__ import annotations
from typing import *

def AddNameOnCoordSystem(model_id: int, coord_system_id: int, coord_system_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.set_name` instead.


	This function defines a name for a coordinate system of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	coord_system_name : str
		Name of the coordinate system.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 2
		    coord_system_name = "Cylindrical CS id:2"
		    meta.coordsystems.AddNameOnCoordSystem(model_id, coord_system_id, coord_system_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.set_name instead.", DeprecationWarning)

def ApplyCoordSystemOnAllElements(coord_sys_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_coordinate_system_on_elements` instead.


	This function applies an existing coordinate system on all elements of a specified model.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on all elements of the specified model.
		Upon failure none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    cs = coordsystems.ApplyCoordSystemOnAllElements(model_id, coord_sys_id)
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_coordinate_system_on_elements instead.", DeprecationWarning)

def ApplyCoordSystemOnAllNodes(coord_sys_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_coordinate_system_on_nodes` instead.


	This function applies an existing coordinate system on all nodes of a specified model.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on all nodes of the specified model.
		Upon failure none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    cs = coordsystems.ApplyCoordSystemOnAllNodes(model_id, coord_sys_id)
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_coordinate_system_on_nodes instead.", DeprecationWarning)

def ApplyCoordSystemOnElement(coord_sys_id: int, element_id: int, element_type: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_coordinate_system` instead.


	This function applies an existing coordinate system on an element of a specified model.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	element_id : int
		Id of the element.

	element_type : str
		Type of the element (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on the specified element.
		Upon failure none is returned.

	See Also
	--------
	constants, coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import constants
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    element_type = constants.SOLID
		    element_id = 14986
		    cs = coordsystems.ApplyCoordSystemOnElement(
		        model_id, coord_sys_id, element_type, element_id
		    )
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_coordinate_system instead.", DeprecationWarning)

def ApplyCoordSystemOnNode(coord_sys_id: int, node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.set_coordinate_system` instead.


	This function applies an existing coordinate system on a node.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on the specified node.
		Upon failure none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    node_id = 19732
		    cs = coordsystems.ApplyCoordSystemOnNode(model_id, coord_sys_id, node_id)
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.set_coordinate_system instead.", DeprecationWarning)

def ApplyCoordSystemOnVisibleElements(model_id: int, coord_sys_id: int, window_name: str) -> object:

	"""

	This function applies an existing coordinate system on visible elements of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_sys_id : int
		Id of the coordinate system.

	window_name : str, optional
		Name of the window. If "window_name" is absent then this function will apply the coordinate system on visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on visible elements of the given model for the specified window. 
		Upon failure none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    window_name = "MetaPost"
		    cs = coordsystems.ApplyCoordSystemOnVisibleElements(
		        model_id, coord_sys_id, window_name
		    )
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def ApplyCoordSystemOnVisibleNodes(model_id: int, coord_sys_id: int, window_name: str) -> object:

	"""

	This function applies an existing coordinate system on visible nodes of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_sys_id : int
		Id of the coordinate system.

	window_name : str, optional
		Name of the window. If "window_name" is absent then this function will apply the coordinate system on visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on visible nodes of the specified model.
		Upon failure none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 2
		    window_name = "MetaPost"
		    cs = coordsystems.ApplyCoordSystemOnVisibleNodes(
		        model_id, coord_sys_id, window_name
		    )
		
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.visible)  # Coordinate System visibility status
		        print(cs.ref_id)  # Coordinate System reference id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewCoordSystemsEnd() -> object:

	"""

	This function ends recording the creation of new coordinate systems. This function should be preceded by a corresponding call to script function meta.coordsystems.CollectNewCoordSystemsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific newly created CoordSystem.
		Upon failure, an empty list is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import coordsystems
		
		
		def main():
		    coordsystems.CollectNewCoordSystemsStart()
		
		    meta.utils.MetaCommand("model create coord fixed rect 1 15849 15815 15730")
		
		    new_coord_systems = coordsystems.CollectNewCoordSystemsEnd()
		    for cs in new_coord_systems:
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


	"""

def CollectNewCoordSystemsStart() -> int:

	"""

	This function starts recording the creation of new coordinate systems. This function should be followed by a corresponding call to script function meta.coordsystems.CollectNewCoordSystemsEnd().

	Returns
	-------
	int
		It returns an integer, 1, upon success and 0 upon failure.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import coordsystems
		
		
		def main():
		    coordsystems.CollectNewCoordSystemsStart()
		
		    meta.utils.MetaCommand("model create coord fixed rect 1 15849 15815 15730")
		
		    new_coord_systems = coordsystems.CollectNewCoordSystemsEnd()
		    for cs in new_coord_systems:
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


	"""

def CommentsOfCoordSystem(model_id: int, coord_system_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.get_comments` instead.


	This function finds the comments of a coordinate system of a given model. Comments refer to various information which are output in the solver's input file and are available in post-processing.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	Returns
	-------
	str
		It returns a string referring to the comments of the coordinate system with the specified id of the given model.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 1
		    coord_system_comments = meta.coordsystems.CommentsOfCoordSystem(
		        model_id, coord_system_id
		    )
		    print(coord_system_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.get_comments instead.", DeprecationWarning)

def CoordSystemById(coord_sys_id: int, model_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds the coordinate system of a model with a given id.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	model_id : int
		Id of the model.

	result : object, optional
		An object of class Result that refers to a Resultset of the model (it is used for moving coordinates). If it is absent, the moving coordinate system will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns the CoordSystem object with the given id.
		Else none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 5
		    cs = coordsystems.CoordSystemById(model_id, coord_sys_id)
		
		    if cs:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemOfElement(element_id: int, element_type: int, result: object, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_coordinate_system` instead.


	This function finds the element coordinate system of an element of a specified model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then element coordinate system will be calculated for the ORIGINAL STATE.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a ElementCoordSystem object referring to the corresponding coordinate system of the specified element.
		Upon failure, none is returned.

	See Also
	--------
	constants, results.Result, coordsystems.ElementCoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    element_type = constants.SOLID
		    element_id = 16961
		    second_id = -1
		    ecs = coordsystems.CoordSystemOfElement(
		        model_id, element_type, element_id, second_id
		    )
		
		    if ecs:
		        print(ecs.id)  # Coordinate System id
		        print(ecs.second_id)  # Coordinate System type
		        print(ecs.model_id)  # Coordinate System model id
		        print(ecs.type)  # Coordinate System type
		
		        print(ecs.origin[0], ecs.origin[1], ecs.origin[2])
		        print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		        print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		        print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_coordinate_system instead.", DeprecationWarning)

def CoordSystems(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function collects all coordinate systems of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific CoordSystem of the given model.
		Upon failure, none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    all_coord_systems = coordsystems.CoordSystems(model_id)
		
		    for cs in all_coord_systems:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemsByComments(coord_system_comments: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds the coordinate systems of a model with specific comments. 

	Parameters
	----------
	coord_system_comments : str
		Comments of the coordinate system. Wildcards can also be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific CoordSystem of the given model.
		Upon failure, none is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_comments = "*"
		    commentcoords = coordsystems.CoordSystemsByComments(model_id, coord_system_comments)
		
		    for cs in commentcoords:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemsByName(coord_system_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds the coordinate systems of a model with a given name (coord_system_name). 

	Parameters
	----------
	coord_system_name : str
		Name of the coordinate system. Wildcards can also be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific CoordSystem of the given model.
		Upon failure, none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_name = "*"
		    matcoords = coordsystems.CoordSystemsByName(model_id, coord_system_name)
		
		    for cs in matcoords:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemsListToDict(list_coords: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of type CoordSystem.

	Parameters
	----------
	list_coords : object
		List with objects of type CoordSystem.

	Returns
	-------
	object
		It returns a dictionary whose keys are the ids of the coordinate systems and values the corresponding CoordSystem objects.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    all_coords = coordsystems.CoordSystems(model_id)
		
		    dict_coords = coordsystems.CoordSystemsListToDict(all_coords)
		    for coord_id, cs in dict_coords.items():
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def CoordSystemsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_coordinate_systems` instead.


	This function searches for the coordinate systems of an overlay run.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'

	Returns
	-------
	object
		Upon success, it returns a list with the CoordSystem objects of the coordinate systems of  the given overlay run.
		Each item of the list is an object of class type CoordSyste, referring to one coordinate system of the given overlay run.
		A description of class CoordSystem can be found as "CoordSystem" under library category "coordsystems".
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_coord_systems = coordsystems.CoordSystemsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for cs in overlay_run_coord_systems:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemsWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds the coordinate systems of a model for which comments exist. Comments can be retrieved by using function "coordinates.CommentsOfCoordSystem".

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to a coordinate system of the model for which comments exist.
		Upon failure, none is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_systems_with_comments = coordsystems.CoordSystemsWithComments(model_id)
		
		    for cs in coord_systems_with_comments:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemsWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds the coordinate systems of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to a coordinate system of the model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	coordsystems.NameOfCoordSystem, coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_systems_with_name = coordsystems.CoordSystemsWithName(model_id)
		    for cs in coord_systems_with_name:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CreateCoordSystem(coord_sys_id: int, coord_sys_type: str, origin: object, model_id: int, zpoint: object, xzpoint: object) -> object:

	"""

	This function creates a coordinate system on a model.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	coord_sys_type : str
		Argument coord_sys_type defines the type of the coordinate system. It must be one of the string values:
		- 'cylindrical'
		- 'rectangular'
		- 'spherical'.

	origin : object
		A list of floats, containing the origin's x, y and z coordinates.

	model_id : int
		Id of the model.

	zpoint : object
		A list of floats, containing the z-axis point's x, y and z coordinates.

	xzpoint : object
		A list of floats, containing the xz-plane point's x, y and z coordinates.

	Returns
	-------
	object
		Upon success, it returns a CoordSystem object referring to the newly created coordinate system of the specified model
		Else, None is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 15
		    coord_sys_type = "spherical"
		    origin = [12.25, 39.21, 50.22]
		    zpoint = [32.21, 74.54, 55.32]
		    xzpoint = [80, 41.59, 74]
		    cs = coordsystems.CreateCoordSystem(
		        model_id, coord_sys_id, coord_sys_type, origin, zpoint, xzpoint
		    )
		    if cs:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeckTypeOfCoordSystem(model_id: int, coord_system_type: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.get_deck_type` instead.


	This function converts a given META KEYWORD coordinate system type to the corresponding type of the deck of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_type : int
		Type of the coordinate system (META constant).

	Returns
	-------
	str
		It returns a string with the name of the type, for the deck of the specified model, of the corresponding to the given META constant coordinate system type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import constants
		
		
		def main():
		    model_id = 0
		    coord_system_type = constants.CORD1S
		    deck_type = coordsystems.DeckTypeOfCoordSystem(model_id, coord_system_type)
		    print(deck_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.get_deck_type instead.", DeprecationWarning)

def ElementsCoordSystemForScalar(model_id: int, selection: str, coord_system_id: int) -> int:

	"""

	This function defines the element local coordinate system of a specified model for loading scalar resultsets. It should be called before loading resultsets with scalar values in the given model. In case the argument selection has a different value from "system" then the coord_sys_id arguments will be ignored.

	Parameters
	----------
	model_id : int
		Id of the model.

	selection : str
		Type of element coordinate system:
		- 'user' : User defined coordinate system of each element (if it has been applied)
		- 'specify' : A coordinate system specified by its id

	coord_system_id : int, optional
		Id of the coordinate system if selection is 'system'.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    selection = "specify"
		    coord_system_id = 1
		    coordsystems.ElementsCoordSystemForScalar(model_id, selection, coord_system_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def HideCoordSystem(model_id: int, coord_system_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.hide` instead.


	This function allows the user to hide a coordinate system of a model specified by a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	coordsystems.HideSomeCoordSystems

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 2
		    ret = coordsystems.HideCoordSystem(model_id, coord_system_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.hide instead.", DeprecationWarning)

def HideSomeCoordSystems(model_id: int, coord_system_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.hide_coordinate_systems` instead.


	This function hides some specific coordinate systems of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_ids : object
		List of coordinate systems ids (integers).

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		
		    all_coord_systems = coordsystems.CoordSystems(model_id)
		    coord_system_ids = list()
		    for cs in all_coord_systems:
		        coord_system_ids.append(cs.id)
		    ret = coordsystems.HideSomeCoordSystems(model_id, coord_system_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.hide_coordinate_systems instead.", DeprecationWarning)

def IdentifyCoordSystem(model_id: int, coord_system_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.identify` instead.


	This function allows the user to identify a coordinate system of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	coordsystems.IdentifySomeCoordSystems

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 1
		    ret = coordsystems.IdentifyCoordSystem(model_id, coord_system_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.identify instead.", DeprecationWarning)

def IdentifySomeCoordSystems(model_id: int, coord_system_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_coordinate_systems` instead.


	This function allows the user to identify some specific coordinate systems of a model specified by their ids.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_ids : object
		List of Ids of the coordinate systems (integers)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_ids = [1, 5, 6, 7]
		    ret = coordsystems.IdentifySomeCoordSystems(model_id, coord_system_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_coordinate_systems instead.", DeprecationWarning)

def IsCoordSystem(coord_system: object) -> int:

	"""

	This function checks whether an object is of type CoordSystem.

	Parameters
	----------
	coord_system : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of type CoordSystem, else 0.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		
		    all_entities = coordsystems.CoordSystems(model_id)
		    for ent in all_entities:
		        if coordsystems.IsCoordSystem(ent):
		            cs = ent
		            print(
		                cs.id,
		                cs.type,
		                cs.visible,
		                cs.ref_id,
		                cs.imported,
		                cs.moving,
		                cs.model_id,
		            )
		            print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		            print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		            print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		            print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis()
		
		
		if __name__ == "__main__":
		    main()


	"""

def LocalCoordSystemOfNodeGeometry(model_id: int, node_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_coordinate_system` instead.


	This function finds the local coordinate system of a node with a given id (node_id) of a specified model. This coordinate system is used in the geometry (for example the CP field of the GRID card of NASTRAN).

	Parameters
	----------
	model_id : int
		Id of the model.

	node_id : int
		Id of the node.

	Returns
	-------
	object
		Upon success, it returns a CoordSystem object referring to the corresponding local coordinate system of the specified node used in geometry.
		Else, None is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    node_id = 100000
		    cs = coordsystems.LocalCoordSystemOfNodeGeometry(model_id, node_id)
		    if cs:
		        print(cs.id, cs.type, cs.visible, cs.ref_id, cs.model_id)
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_coordinate_system instead.", DeprecationWarning)

def LocalCoordSystemOfNodeResults(model_id: int, node_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_coordinate_system` instead.


	This function finds the local coordinate system of a given node of a specific model. This coordinate system is used in the results. (For example in NASTRAN the CD field in the GRID card.)

	Parameters
	----------
	model_id : int
		Id of the model.

	node_id : int
		Id of the node.

	Returns
	-------
	object
		Upon success, it returns a CoordSystem object referring to the corresponding local coordinate system of the specified node used in results.
		Else, None is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    node_id = 10
		    cs = coordsystems.LocalCoordSystemOfNodeResults(model_id, node_id)
		    if cs:
		        print(cs.id, cs.type, cs.visible, cs.ref_id, cs.model_id)
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_coordinate_system instead.", DeprecationWarning)

def MetaTypeOfCoordSystem(model_id: int, coord_system_type: str) -> int:

	"""

	This function converts a given coordinate system type of a deck of a specified model to the value of the corresponding META constant.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_type : str
		Deck type of the coordinate system.

	Returns
	-------
	int
		It returns the value of the META constant type of the corresponding coordinate system type of the specified model.
		Upon failure, a negative value is returned.

	See Also
	--------
	constants, coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_type = "CORD2C"
		    meta_type = coordsystems.MetaTypeOfCoordSystem(model_id, coord_system_type)
		    print(meta_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NameOfCoordSystem(model_id: int, coord_system_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.get_name` instead.


	This function finds the name of a coordinate system with a specific id of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	Returns
	-------
	str
		It returns a string referring to the name of the coordinate system with the specified id.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 1
		    coord_system_name = coordsystems.NameOfCoordSystem(model_id, coord_system_id)
		    print(coord_system_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.get_name instead.", DeprecationWarning)

def NodesCoordSystemForScalar(model_id: int, selection: str, coord_system_id: int) -> int:

	"""

	This function defines the nodal local coordinate system of a specified model for loading scalar resultsets. It should be called before loading resultsets with scalar values in the given model. 

	Parameters
	----------
	model_id : int
		Id of the model.

	selection : str
		Definition of the nodal local coordinate system. Possible values:
		- 'local' : Local coordinate system of each node
		- 'user' : User defined coordinate system of each node (if it has been applied)
		- 'system' : A coordinate system specified by its id.

	coord_system_id : int, optional
		If selection = 'system' then it is the Id of the coordinate system.
		Else, the coord_system_id will be ignored.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    selection = "system"
		    coord_system_id = 1
		    coordsystems.NodesCoordSystemForScalar(model_id, selection, coord_system_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodesOfCoordSystem(model_id: int, coord_sys_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.get_nodes` instead.


	This function collects the nodes from which a given coordinate system has been created.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_sys_id : int
		Id of the coordinate system.

	Returns
	-------
	object
		It returns a list with the Node objects of the corresponding nodes of the specified coordinate system.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 1
		    coord_system_nodes = coordsystems.NodesOfCoordSystem(model_id, coord_sys_id)
		
		    for n in coord_system_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.get_nodes instead.", DeprecationWarning)

def PickCoordSystems(model_id: int, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_coordinate_systems` instead.


	This function allows the user to pick coordinate systems of a model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	model_id : int
		Id of the model. If model_id is equal to -1, then this function will work for all models.

	message : str
		Argument "message" refers to the message which will be shown to the user when the function is called.

	Returns
	-------
	object
		It returns a where each member of the list is an object of class CoordSystems referring to one specific picked coordinate system of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    message = "Select Coordinate Systems and press Enter when you are ready"
		    picked_coord_systems = coordsystems.PickCoordSystems(model_id, message)
		    for cs in picked_coord_systems:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis()
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_coordinate_systems instead.", DeprecationWarning)

def ReportNewCoordSystems() -> object:

	"""

	This function collects the newly created coordinate systems from the last call of script function CollectNewCoordSystemsStart(). This function should be preceded by a corresponding call to script function CollectNewCoordSystemsStart() and should be followed by a corresponding call to script function CollectNewCoordSystemsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific newly created CoordSystem.
		Upon failure, an empty list is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import utils
		
		
		def main():
		    coordsystems.CollectNewCoordSystemsStart()
		
		    # create new coord_systems
		    meta.utils.MetaCommand("model create coord fixed rect 1 15849 15815 15730")
		
		    new_coord_systems = coordsystems.ReportNewCoordSystems()
		    for cs in new_coord_systems:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		    coordsystems.CollectNewCoordSystemsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ShowCoordSystem(model_id: int, coord_system_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.show` instead.


	This function allows the user to make visible a coordinate system of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_id : int
		Id of the coordinate system.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	coordsystems.ShowSomeCoordSystems

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_id = 1
		    ret = coordsystems.ShowCoordSystem(model_id, coord_system_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.show instead.", DeprecationWarning)

def ShowSomeCoordSystems(model_id: int, coord_system_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.show_coordinate_systems` instead.


	This function allows the user to make visible some specific coordinate systems of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_system_ids : object
		A list of integers Ids of coordinate systems.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		
		    all_coord_systems = coordsystems.CoordSystems(model_id)
		    coord_system_ids = list()
		    for cs in all_coord_systems:
		        coord_system_ids.append(cs.id)
		    ret = coordsystems.ShowSomeCoordSystems(model_id, coord_system_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.show_coordinate_systems instead.", DeprecationWarning)

def StringCoordSystemType(coord_system_type: int) -> str:

	"""

	This function converts a given META coordinate system type constant to its corresponding string representation.

	Parameters
	----------
	coord_system_type : int
		Type of the coordinate system (META constant).

	Returns
	-------
	str
		It returns a string with the name of the META constant coordinate system type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import constants
		
		
		def main():
		    coord_system_type = constants.CORD2R
		    str_coord_system_type = coordsystems.StringCoordSystemType(coord_system_type)
		    print(str_coord_system_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TransformDeformation(coord_sys_id: int, xbase: float, xdeform: float, ybase: float, ydeform: float, zbase: float, zdeform: float, model_id: int, result: object) -> object:

	"""

	This function calculates deformation with respect to an existing coordinate system.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	xbase : float
		X coordinate of base position.

	xdeform : float
		Deformation in X direction.

	ybase : float
		Y coordinate of base position.

	ydeform : float
		Deformation in Y direction.

	zbase : float
		Z coordinate of base position.

	zdeform : float
		Deformation in Z direction.

	model_id : int
		Id of the model.

	result : object, optional
		Resultset at which transformation takes place. It is needed for moving coordinate systems.

	Returns
	-------
	object
		It returns a list with 3 members referring to the transformed deformation (X, Y, Z) with respect to the specified coordinate system.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    xbase = 19.3
		    ybase = 20.15
		    zbase = 19.995
		    xdeform = 20.31
		    ydeform = 18.34
		    zdeform = 19.54
		    coord_sys_id = 1
		
		    transformed = coordsystems.TransformDeformation(
		        model_id, xbase, ybase, zbase, xdeform, ydeform, zdeform, coord_sys_id, result
		    )
		    if transformed:
		        xtrans = transformed[0]  # Transformed X deformation
		        ytrans = transformed[1]  # Transformed Y deformation
		        ztrans = transformed[2]  # Transformed Z deformation
		        print(xtrans, ytrans, ztrans)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TransformNode(coord_sys_id: int, x: float, y: float, z: float, model_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.identify` instead.


	This function calculates the coordinates of a given node with respect to an existing coordinate system.

	Parameters
	----------
	coord_sys_id : int
		Id of the coordinate system.

	x : float
		X coordinate of the node.

	y : float
		Y coordinate of the node.

	z : float
		Z coordinate of the node.

	model_id : int
		Id of the model.

	result : object, optional
		Resultset at which transformation takes place.It is needed for moving coordinate systems.

	Returns
	-------
	object
		Upon success, it returns a list with 3 members referring to the transformed coordinates of the node with respect to the specified coordinate system.
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    x = 40.12
		    y = 50.35
		    z = 61.58
		    coord_sys_id = 1
		    transformed = coordsystems.TransformNode(model_id, x, y, z, coord_sys_id, result)
		    if transformed:
		        xtrans = transformed[0]  # Transformed X coordinate
		        ytrans = transformed[1]  # Transformed Y coordinate
		        ztrans = transformed[2]  # Transformed Z coordinate
		        print(xtrans, ytrans, ztrans)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.identify instead.", DeprecationWarning)

def UpdateCoordSystem(coord: object) -> object:

	"""

	This function updates the data of the given coord_system object. Update is based in the field "id" and "model_id" of the given coord_system object.

	Parameters
	----------
	coord : object
		A CoordSystem object.

	Returns
	-------
	object
		Upon success, it returns the new updated coord_system object.
		Else, None is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import utils
		
		
		def main():
		    model_id = 0
		    id = 1
		    cs = coordsystems.CoordSystemById(model_id, id)
		    if cs:
		        # commands which alter the data of the CoodSystem object
		        utils.MetaCommand("erase coord all")
		
		        cs = coordsystems.UpdateCoordSystem(cs)
		        if cs:
		            print(
		                cs.id,
		                cs.type,
		                cs.visible,
		                cs.ref_id,
		                cs.imported,
		                cs.moving,
		                cs.model_id,
		            )
		            print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		            print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		            print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		            print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def UserCoordSystemOfElement(element_id: int, element_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_coordinate_system` instead.


	This function finds the user defined coordinate system of an element of a specified model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a CoordSystem object referring to the corresponding user defined coordinate system of the specified element.
		Else, None is returned.

	See Also
	--------
	constants, coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SOLID
		    element_id = 16961
		    cs = coordsystems.UserCoordSystemOfElement(model_id, element_type, element_id)
		    if cs:
		        print(cs.id, cs.type, cs.visible, cs.ref_id, cs.model_id)
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_coordinate_system instead.", DeprecationWarning)

def UserCoordSystemOfNode(node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_coordinate_system` instead.


	This function finds the user defined coordinate system of a node of a specified model.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a CoordSystem object referring to the corresponding user defined coordinate system of the specified node.
		Else, None is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    node_id = 885
		    cs = coordsystems.UserCoordSystemOfNode(model_id, node_id)
		    if cs:
		        print(cs.id, cs.type, cs.visible, cs.ref_id, cs.model_id)
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_coordinate_system instead.", DeprecationWarning)

def VisibleCoordSystems(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function collects all visible coordinate systems of the model specified by the given id.

	Parameters
	----------
	window_name : str
		Name of the window.  If it is absent then this function will collect visible coordinate systems for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CoordSystem referring to one specific newly created CoordSystem.
		Upon failure, an empty list is returned.

	See Also
	--------
	coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_coord_systems = coordsystems.VisibleCoordSystems(model_id, window_name)
		    for cs in visible_coord_systems:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordSystemOfElementWithMaterialOrientation(element_id: int, element_type: int, result: object, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_coordinate_system` instead.


	This function finds the element coordinate system of an element of a specified model using the material orientation.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then element coordinate system will be calculated for the ORIGINAL STATE.

	second_id : int
		Second id of the element. Some elements may have a second id (GAP, TUBE, JOINT). For the rest types of elements, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a ElementCoordSystem object referring to the corresponding CoordSystem of the specified element.
		Upon failure, none is returned.

	See Also
	--------
	constants, coordsystems.CoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1000
		    second_id = -1
		    ecs = coordsystems.CoordSystemOfElementWithMaterialOrientation(
		        model_id, element_type, element_id, second_id
		    )
		
		    if ecs:
		        print(ecs.id)  # Coordinate System id
		        print(ecs.type)  # Coordinate System type
		        print(ecs.model_id)  # Coordinate System model id
		        print(ecs.type)  # Coordinate System type
		
		        print(ecs.origin[0], ecs.origin[1], ecs.origin[2])
		        print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		        print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		        print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_coordinate_system instead.", DeprecationWarning)

def CoordSystemsBySolverId(model_id: int, coord_sys_path: str, coord_sys_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinate_systems` instead.


	This function finds elements of a model with hierarchical structure defined by type, id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_sys_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given coordinate system is limited.

	coord_sys_id : int
		Id of the coordinate system.

	Returns
	-------
	object
		This function returns a list with objects of class CoordSystem referring to the corresponding coordinate systems found.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_sys_path = "2"
		    coord_sys_id = 1
		
		    collected_coord_sys = coordsystems.CoordSystemsBySolverId(
		        model_id, coord_sys_path, coord_sys_id
		    )
		
		    for cs in collected_coord_sys:
		        print(
		            cs.id, cs.type, cs.visible, cs.ref_id, cs.imported, cs.moving, cs.model_id
		        )
		        print(cs.origin[0], cs.origin[1], cs.origin[2])  # Origin
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinate_systems instead.", DeprecationWarning)

def CoordinatesOfCoordSystem(model_id: int, coord_sys_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.coordsystems.CoordSystem.get_coordinates` instead.


	This function finds the current coordinates (origin, x-axis, y-axis, z-axis) of a coordinate system of a model with a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	coord_sys_id : int
		Id of the coordinate system.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with the current coordinates of the coordinate system with given id. 
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a list with double numbers referring to the origin of the coordinate system.
		In position 1, internal lists contain a list with double numbers referring to the X-axis of the coordinate system. 
		In position 2, internal lists contain a list with double numbers referring to the Y-axis of the coordinate system.  
		In position 3, internal lists contain a list with double numbers referring to the Z-axis of the coordinate system.  
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import results
		
		
		def main():
		    model_id = 0
		    coord_sys_id = 5
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    one_coord = coordsystems.CoordinatesOfCoordSystem(model_id, coord_sys_id, result)
		    if len(one_coord):
		        origin = one_coord[0]
		        print(origin[0], origin[1], origin[2])
		        x_axis = one_coord[1]
		        print(x_axis[0], x_axis[1], x_axis[2])
		        y_axis = one_coord[2]
		        print(y_axis[0], y_axis[1], y_axis[2])
		        z_axis = one_coord[3]
		        print(z_axis[0], z_axis[1], z_axis[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.coordsystems.CoordSystem.get_coordinates instead.", DeprecationWarning)

def IdentifyCoordSystemsReset(model_id: int, coord_system_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_coordinate_systems` instead.


	This function allows the user to reset the identification of all or specific nodes of the specified model. It can be called with two different ways. The one is with lists of coordiante system's ids, and the other is with coord_system_ids = 'all'.

	Parameters
	----------
	model_id : int
		The id of the model.

	coord_system_ids : object
		List with ids of the coordinate systems, or string 'all'.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    model_id = 0
		    coord_system_ids = [1, 2, 3]
		    # or
		    # coord_system_ids = 'all'
		    coordsystems.IdentifyCoordSystemsReset(model_id, coord_system_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_coordinate_systems instead.", DeprecationWarning)

class CoordSystem():

	"""

	Class for coordinate systems
	
	The type of the coordinate system is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corrsponding constant names of constant values.
	
	A full list of coordinate system types and constants can be derived from the following example.
	This class can be subclassed as shown in the example.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    if cs:
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
		# method: get_comments
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    comm = cs.get_comments()
		    print(comm)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import models
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    m = models.Model(model_id)
		    res = m.get_current_resultset()
		    coord = cs.get_coordinates(res)
		    print(coord)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_type
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    type = cs.get_deck_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    r = cs.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_name
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    name = cs.get_name()
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    coord_system_nodes = cs.get_nodes()
		    for n in coord_system_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    ret = cs.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    ret = cs.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    ret = cs.set_name("my_name")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    ret = cs.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_subtype
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    subtype = cs.get_deck_subtype()
		    print(subtype)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import coordsystems
		
		
		def main():
		    cs = coordsystems.CoordSystem(id=1, model_id=0)
		    can_use = cs.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the coordinate system.

	"""

	model_id: int = None
	"""
	Model number of the coordinate system.

	"""

	type: int = None
	"""
	Type of the coordinate system (mETA constant).

	"""

	origin: object = None
	"""
	Origin.

	"""

	xaxis: object = None
	"""
	X-axis.

	"""

	yaxis: object = None
	"""
	Y-axis.

	"""

	zaxis: object = None
	"""
	Z-axis.

	"""

	visible: int = None
	"""
	- 1 if coordinate system is visible on the active or first
	enabled window of the active page
	- 0 if coordinate system is not visible

	"""

	ref_id: int = None
	"""
	Id of the reference coordsystem, -1 if no reference coordinate system exists.

	"""

	imported: int = None
	"""
	- 1 if coordinate system is imported (part of the solver input file)
	- 0 if it is user-created

	"""

	moving: int = None
	"""
	- 1 if coordinate system is moving with according to the motion of the model's geometry
	- 0 if it is not

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the coordinate system.


		Returns
		-------
		object
			Upon success, it returns an object of class Model.Upon failure, it returns None.

		"""


	def get_nodes(self) -> object:

		"""

		This method gets the nodes of the coordinate system.


		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node. Upon failure, it returns None.

		"""


	def get_deck_type(self) -> str:

		"""

		This method gets the type of the coordinate system as string.


		Returns
		-------
		str
			Upon success, it returns the type of the coordinate as string.Upon failure, it returns None.

		"""


	def get_name(self) -> str:

		"""

		This method gets the name of the coordinate system.


		Returns
		-------
		str
			Upon success, it returns the name of the coordinate. Upon failure, it returns None.

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of the coordinate system.


		Returns
		-------
		str
			Upon success, it returns a string with the comments. Upon failure it returns None.

		"""


	def get_coordinates(self, resultset: object) -> object:

		"""

		This method gets the current coordinates (origin, x-axis, y-axis, z-axis) of the coordinate system.


		Parameters
		----------
		resultset : object
			An object of class Result.

		Returns
		-------
		object
			It returns a list with the current coordinates of the coordinate system with given id. Each member of the list is another list with 3 members.In position 0, internal lists contain a list with double numbers referring to the origin of the coordinate system.In position 1, internal lists contain a list with double numbers referring to the X-axis of the coordinate system. In position 2, internal lists contain a list with double numbers referring to the Y-axis of the coordinate system.  In position 3, internal lists contain a list with double numbers referring to the Z-axis of the coordinate system.  Upon failure, an empty list is returned.

		"""


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the coordinate system.


		Parameters
		----------
		name : str
			The name of the coordinate system.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the coordinate system.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the coordinate system.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the coordinate system.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def get_deck_subtype(self) -> str:

		"""

		This method gets the subtype of the coordinate system as string.


		Returns
		-------
		str
			Upon success, it returns the subtype of the coordinate as string. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META CoordSystem entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_usersys_nodes(self, specifier: str, window: object) -> object:

		"""

		This method gets the nodes which are assigned to a user coordinate system


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the nodes assigned to the user coordinate system (default value).
			- 'visible' : visible nodes assigned to the user coordinate system. Optionally combined with argument: window.

		window : object, optional
			An object of class window. This argument is used only when the specifier is 'visible'. If the specifier has a different value, this argument is ignored. If this argument is set, the method will return only the visible nodes in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node. Upon failure, it returns an empty list.

		"""


	def get_usersys_elems(self, specifier: str, type: int, window: object) -> object:

		"""

		This method gets the elements which are assigned to a user coordinate system


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all elements assigned to the user coordinate system (default value). Optionally combined with argument: type.
			- 'visible' : visible elements assigned to the user coordinate system. Optionally combined with arguments: type, window.

		type : int, optional
			The type of the elements that the method will return. If absent, elements of all types will be returned.

		window : object, optional
			An object of class Window. It is used when the specifier is 'visible'. If this argument is set, the method will return only the visible elements in this window.

		Returns
		-------
		object
			It returns a list, where each element of the list is an object of class Element, referring to one specific element assigned to the user coordinate system. Upon failure, an empty list is returned.

		"""

class ElementCoordSystem():

	"""

	Class for element coordinate systems.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import coordsystems
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SOLID
		    element_id = 41032
		    second_id = -1
		    ecs = meta.coordsystems.CoordSystemOfElement(
		        model_id, element_type, element_id, second_id
		    )
		    print(ecs)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the element.

	"""

	second_id: int = None
	"""
	Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	"""

	model_id: int = None
	"""
	Model id of the element.

	"""

	type: int = None
	"""
	Type of the element (mETA constant).

	"""

	origin: object = None
	"""
	Origin of the coordinate system.

	"""

	xaxis: object = None
	"""
	X-axis of the coordinate system.

	"""

	yaxis: object = None
	"""
	Y-axis of the coordinate system.

	"""

	zaxis: object = None
	"""
	Z-axis of the coordinate system.

	"""

	lcs_id: int = None
	"""
	LCS id for BUSH elements, -1 otherwise.

	"""
