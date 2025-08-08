from __future__ import annotations
from typing import *

def AddMaterialLimitOnPart(model_id: int, part_type: int, part_id: int, material_limit: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.set_material_limit` instead.


	This function adds material limit on a part with a specific id and type of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	material_limit : float
		Material limit of the part.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	parts.MaterialLimitOfPart, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    material_limit = 1.29
		    ret = parts.AddMaterialLimitOnPart(model_id, part_type, part_id, material_limit)
		    print(ret)
		    mat_limit = parts.MaterialLimitOfPart(model_id, part_type, part_id)
		    print(mat_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.set_material_limit instead.", DeprecationWarning)

def AddNameOnPart(part_id: int, part_name: str, part_type: int, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.set_name` instead.


	This function defines a name for a part of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_name : str
		Name of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

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
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    part_name = "Lower Side"
		    parts.AddNameOnPart(model_id, part_type, part_id, part_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.set_name instead.", DeprecationWarning)

def AdvFiltersOnParts(model_id: int, adv_filters: object, resultset: object, sort: bool) -> object:

	"""

	This function allows the user to collect parts of a model specified by the given id through some advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter entries.

	resultset : object, optional
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
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Parts:all::Keep All")
		    adv_filters.append("intersect:Parts:id:<=199:Keep All")
		
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    collected_parts = parts.AdvFiltersOnParts(model_id, adv_filters, resultset)
		    for p in collected_parts:
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


	"""

def CentroidScalarOfPart(layer: str, part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of a part with specific id and type of a given model.

	Parameters
	----------
	layer : str
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class CentroidScalar referring to the centroid scalar value of an element of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    layer = "top"  # TOP centroid scalar values if both bottom and top values are loaded
		    all_part_centroid = parts.CentroidScalarOfPart(result, part_type, part_id, layer)
		    few_part_centroid = all_part_centroid[0 : min(10, len(all_part_centroid))]
		    for centroid in few_part_centroid:  # list with CentroidScalar objects
		        print(centroid.value)  # centroid scalar value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_centroid_vector` instead.


	This function calculates all centroid vector values of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class CentroidVector referring to the centroid vector value of an element of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    all_part_centroid = parts.CentroidVectorOfPart(result, part_type, part_id)
		    few_part_centroid = all_part_centroid[0 : min(10, len(all_part_centroid))]
		    for centroid in few_part_centroid:  # list with CentroidVector objects
		        print(centroid.value)  # Centroid vector value
		        print(
		            centroid.x, centroid.y, centroid.z
		        )  # Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_centroid_vector instead.", DeprecationWarning)

def CollectNewPartsEnd() -> object:

	"""

	This function ends recording the creation of new parts. This function should be preceded by a corresponding call to script function CollectNewPartsStart().

	Returns
	-------
	object
		It returns a list with the part objects of the corresponding newly created parts.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import utils
		
		
		def main():
		    parts.CollectNewPartsStart()
		
		    # create new parts
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_parts = parts.CollectNewPartsEnd()
		    for p in new_parts:
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


	"""

def CollectNewPartsStart() -> int:

	"""

	This function starts recording the creation of new parts. This function should be followed by a corresponding call to script function CollectNewPartsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import utils
		
		
		def main():
		    parts.CollectNewPartsStart()
		
		    # create new parts
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_parts = parts.CollectNewPartsEnd()
		    for p in new_parts:
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


	"""

def ColorOfPart(part_id: int, part_type: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_color` instead.


	This function finds RGB values and Alpha channel of color of a part of a model with a given id and type.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	window_name : str
		The name of the window of the part. If it is absent then this function will return the color of the part for the first enabled window of the model of the part.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a 4-element list with the RGB and Alpha channel values of the color of the corresponding part of the given model for the specified window.
		The list contains:
		- position 0: R value [0-255]
		- position 1: G value [0-255]
		- position 2: B value [0-255]
		- position 3: Alpha channel [0-255]
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    window_name = "MetaPost"
		    mat_color = parts.ColorOfPart(model_id, part_type, part_id, window_name)
		    if mat_color:
		        print(mat_color[0])  # R value
		        print(mat_color[1])  # G value
		        print(mat_color[2])  # B value
		        print(mat_color[3])  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_color instead.", DeprecationWarning)

def ColorOfPartLayer(part_id: int, part_type: int, serial: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Layer.get_color` instead.


	This function finds the color of a layer given its serial number, id and type of the corresponding part of the model it belongs to.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	serial : int
		Serial number of the layer.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class Color for the corresponding layer.
		Else, None is returned.

	See Also
	--------
	windows.Color, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 2
		    serial_id = 1
		
		    layer_color = parts.ColorOfPartLayer(model_id, part_type, part_id, serial_id)
		    if layer_color:
		        print(layer_color.r)  # R value
		        print(layer_color.g)  # G value
		        print(layer_color.b)  # B value
		        print(layer_color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Layer.get_color instead.", DeprecationWarning)

def CommentsOfPart(part_id: int, part_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_comments` instead.


	This function finds the comments of a part with a specific id and type of a given model. Comments refer to various information which are output in the solver's input file and are read during input by META.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the comments of the part with the specified id and type of the given model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    part_comments = parts.CommentsOfPart(model_id, part_type, part_id)
		    print(part_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_comments instead.", DeprecationWarning)

def CornerScalarOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a part with a specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class CornerScalar referring to one corner scalar values of an element of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    all_part_corner = parts.CornerScalarOfPart(result, part_type, part_id)
		    few_part_corner = all_part_corner[0 : min(10, len(all_part_corner))]
		    for corn in few_part_corner:  # list with CornerScalar objects
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_corner_scalar instead.", DeprecationWarning)

def DeckSubtypeOfPart(part_subtype: int, part_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_deck_subtype` instead.


	This function converts a given META part subtype to the corresponding subtype of a deck of a specified model.

	Parameters
	----------
	part_subtype : int
		Subtype of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string with the name of the part subtype for the deck of the specified model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_subtype = 1
		
		    deck_subtype = parts.DeckSubtypeOfPart(model_id, part_type, part_subtype)
		    print(deck_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_deck_subtype instead.", DeprecationWarning)

def DeckTypeOfPart(part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_deck_type` instead.


	This function converts a given META part type to the corresponding type of a deck of a specified model.

	Parameters
	----------
	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a string with the name of the part type for the deck of the specified model of the corresponding to the given META constant part type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    deck_type = parts.DeckTypeOfPart(model_id, part_type)
		    print(deck_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_deck_type instead.", DeprecationWarning)

def DeformationsOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Deformation referring to the deformation of a node for the specified part.
		Upon failure, an empty list is is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    part_deforms = parts.DeformationsOfPart(result, part_type, part_id)
		    for deform in part_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_deformations instead.", DeprecationWarning)

def DistancePartToGroup(part_model: int, part_result: object, part_type: int, part_id: int, group_model: int, group_result: object, group_name: str, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_group` instead.


	This function calculates the distance or the elongation of a part from a group.

	Parameters
	----------
	part_model : int
		Id of the model of the part.

	part_result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	group_model : int
		Id of the model of the group.

	group_result : object
		An object of class Result that refers to a Resultset of the model of the group.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, default value is 1.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as items referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    distance = parts.DistancePartToGroup(
		        part_model,
		        part_result,
		        part_type,
		        part_id,
		        group_model,
		        group_result,
		        group_name,
		        group_instance,
		    )
		    # distance = parts.DistancePartToGroup(part_model, part_result, part_type, part_id, group_model, group_result, group_name, group_instance, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_group instead.", DeprecationWarning)

def DistancePartToLine(part_model: int, part_result: object, part_type: int, part_id: int, node1_model: int, node1_result: object, line_node1: int, node2_model: int, node2_result: object, line_node2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_line` instead.


	This function calculates the distance or the elongation of a part from a line of a model for a specific resultset.

	Parameters
	----------
	part_model : int
		Id of the model of the part.

	part_result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	node1_model : int
		Id of the model of the 1st node of the line.

	node1_result : object
		An object of class Result that refers to a Resultset of the model of the 1st node of the line.

	line_node1 : int
		Id of the 1st node of the line.

	node2_model : int
		Id of the model of the 2nd node of the line.

	node2_result : object
		An object of class Result that refers to a Resultset of the model of the 2nd node of the line.

	line_node2 : int
		Id of the 2nd node of the line.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as items referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    line_node1 = 1
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    line_node2 = 1
		
		    distance = parts.DistancePartToLine(
		        part_model,
		        part_result,
		        part_type,
		        part_id,
		        node1_model,
		        node1_result,
		        line_node1,
		        node2_model,
		        node2_result,
		        line_node2,
		    )
		    # distance = parts.DistancePartToLine(part_model, part_result, part_type, part_id, node1_model, node1_result, line_node1, node2_model, node2_result, line_node2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_line instead.", DeprecationWarning)

def DistancePartToLineCoords(model_id: int, result: object, part_type: int, part_id: int, point1: object, point2: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_line_coords` instead.


	This function calculates the distance or the elongation of a part from a line. Part is specified by its model, type and id.

	Parameters
	----------
	model_id : int
		Id of the model of the part.

	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	point1 : object
		List with the coordinates of the 1st point of the line.

	point2 : object
		List with the coordinates of the 2nd point of the line.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as items referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    point1 = list()
		    point1.append(-1.25)
		    point1.append(-2.32)
		    point1.append(2.15)
		
		    point2 = list()
		    point2.append(-1.35)
		    point2.append(-0.9)
		    point2.append(3.5)
		
		    distance = parts.DistancePartToLineCoords(
		        part_model, part_result, part_type, part_id, point1, point2
		    )
		    # distance = parts.DistancePartToLineCoords(part_model, part_result, part_type, part_id, point1, point2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_line_coords instead.", DeprecationWarning)

def DistancePartToPart(model_id1: int, result1: object, part_type1: int, part_id1: int, model_id2: int, result2: object, art_type2: int, part_id2: int, elongation: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_part` instead.


	This function calculates the distance or the elongation of a part from another part.

	Parameters
	----------
	model_id1 : int
		Id of the model of the 1st part.

	result1 : object
		An object of class Result that refers to a Resultset of the model of the 1st part.

	part_type1 : int
		Type of the 1st part (META constant).

	part_id1 : int
		Id of the 1st part.

	model_id2 : int
		Id of the model of the 2nd part.

	result2 : object
		An object of class Result that refers to a Resultset of the model of the 2nd part.

	art_type2 : int
		Type of the 2nd part (META constant).

	part_id2 : int
		Id of the 2nd part.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	int
		It returns a list with float numbers as items referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id1 = 0
		    all_resultsets = results.Resultsets(model_id1)
		    result1 = all_resultsets[1]
		    part_type1 = constants.PSHELL
		    part_id1 = 1
		
		    model_id2 = 0
		    all_resultsets = results.Resultsets(model_id2)
		    result2 = all_resultsets[1]
		    part_type2 = constants.PSHELL
		    part_id2 = 2
		
		    distance = parts.DistancePartToPart(
		        model_id1,
		        result1,
		        part_type1,
		        part_id1,
		        model_id2,
		        result2,
		        part_type2,
		        part_id2,
		    )
		    # distance = parts.DistancePartToPart(model_id1, result1, part_type1, part_id1, model_id2, result2, part_type2, part_id2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_part instead.", DeprecationWarning)

def DistancePartToPlane(part_model: int, part_result: object, part_type: int, part_id: int, node1_model: int, node1_result: object, plane_node1: int, node2_model: int, node2_result: object, plane_node2: int, node3_model: int, node3_result: object, plane_node3: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_plane` instead.


	This function calculates the distance or the elongation of a part from a plane of a model for a specific resultset.

	Parameters
	----------
	part_model : int
		Id of the model of the part.

	part_result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	node1_model : int
		Id of the model of the 1st node of the plane.

	node1_result : object
		An object of class Result that refers to a Resultset of the model of the 1st node of the plane.

	plane_node1 : int
		Id of the 1st node of the plane.

	node2_model : int
		Id of the model of the 2nd node of the plane.

	node2_result : object
		An object of class Result that refers to a Resultset of the model of the 2nd node of the plane.

	plane_node2 : int
		Id of the 2nd node of the plane.

	node3_model : int
		Id of the model of the 3rd node of the plane.

	node3_result : object
		An object of class Result that refers to a Resultset of the model of the 3rd node of the plane.

	plane_node3 : int
		Id of the 3rd node of the plane.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    plane_node1 = 1
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node2_result = all_resultsets[1]
		    plane_node2 = 20
		
		    node3_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node3_result = all_resultsets[1]
		    plane_node3 = 55
		
		    distance = parts.DistancePartToPlane(
		        part_model,
		        part_result,
		        part_type,
		        part_id,
		        node1_model,
		        node1_result,
		        plane_node1,
		        node2_model,
		        node2_result,
		        plane_node2,
		        node3_model,
		        node3_result,
		        plane_node3,
		    )
		    # distance = parts.DistancePartToPlane(part_model, part_result, part_type, part_id, node1_model, node1_result, plane_node1, node2_model, node2_result, plane_node2, node3_model, node3_result, plane_node3, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_plane instead.", DeprecationWarning)

def DistancePartToPlaneCoords(model_id: int, result: object, part_type: int, part_id: int, point1: object, point2: object, point3: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_plane_coords` instead.


	This function calculates the distance or the elongation of a part from a plane.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constants).

	part_id : int
		Id of the part.

	point1 : object
		List with the coordinates of the 1st point of the plane.

	point2 : object
		List with the coordinates of the 2nd point of the plane.

	point3 : object
		List with the coordinates of the 3rd point of the plane.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as items referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    point1 = list()
		    point1.append(0)
		    point1.append(0)
		    point1.append(0)
		
		    point2 = list()
		    point2.append(-1.35)
		    point2.append(-0.9)
		    point2.append(3.5)
		
		    point3 = list()
		    point3.append(0.3)
		    point3.append(0.4)
		    point3.append(0.99)
		
		    distance = parts.DistancePartToPlaneCoords(
		        part_model, part_result, part_type, part_id, point1, point2, point3
		    )
		    # distance = parts.DistancePartToPlaneCoords(part_model, part_result, part_type, part_id, point1, point2, point3, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_plane_coords instead.", DeprecationWarning)

def GetColorOfPart(model_id: int, part_type: int, part_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_color` instead.


	This function finds color of a part of a model with a given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	window_name : str
		Name of the window of the part. If it is absent then this function will return the color of the part for the first enabled window of the model of the part.

	Returns
	-------
	object
		It returns a color object with the color of the corresponding part of the  given model for the specified window.
		Else, None is returned.

	See Also
	--------
	windows.Color, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    window_name = "MetaPost"
		    col = parts.GetColorOfPart(model_id, part_type, part_id, window_name)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_color instead.", DeprecationWarning)

def HidePart(model_id: int, part_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.hide` instead.


	This function allows the user to hide a part of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	parts.HideSomeParts

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_id = 1
		    ret = parts.HidePart(model_id, part_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.hide instead.", DeprecationWarning)

def HideSomeParts(model_id: int, part_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.hide_parts` instead.


	This function allows the user to hide some specific parts of a model specified by its id. This function works for enabled windows of active page.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_ids : object
		List with Ids of the parts as integers.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		
		    part_ids = list()
		    all_parts = parts.Parts(model_id)
		    for p in all_parts:
		        part_ids.append(p.id)
		    ret = parts.HideSomeParts(model_id, part_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.hide_parts instead.", DeprecationWarning)

def IdentifiedParts(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_parts` instead.


	This function collects all identified parts of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect identified parts for all the enabled windows of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    identified_parts = parts.IdentifiedParts(model_id)
		    for p in identified_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_parts instead.", DeprecationWarning)

def IdentifiedPartsByType(model_id: int, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function collects all identified parts with a specific type of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constants).

	window_name : str
		Name of the window of the model. If it is absent then this function will collect identified parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    window_name = "MetaPost"
		    identified_parts = parts.IdentifiedPartsByType(model_id, part_type, window_name)
		    for p in identified_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def IdentifyPart(model_id: int, part_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.identify` instead.


	This function allows to identify a part of a model specified by a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	parts.IdentifySomeParts

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_id = 15
		    ret = parts.IdentifyPart(model_id, part_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.identify instead.", DeprecationWarning)

def IdentifySomeParts(model_id: int, part_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_parts` instead.


	This function allows the user to identify some specific parts of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_ids : object
		List with Ids of the parts as integers.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		
		    part_ids = list()
		    all_parts = parts.Parts(model_id)
		    for p in all_parts:
		        part_ids.append(p.id)
		    ret = parts.IdentifySomeParts(model_id, part_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_parts instead.", DeprecationWarning)

def IsPart(part: object) -> int:

	"""

	This function checks whether an object of class Part.

	Parameters
	----------
	part : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Part, 0 otherwise.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    all_entities = list()
		    all_entities.append("A_string")
		    all_entities.append(parts.Parts(model_id)[0])
		
		    for ent in all_entities:
		        if parts.IsPart(ent):
		            p = ent
		            print("This is an object of class Part")
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
		        else:
		            print("This is not an object of class Part")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsPartLayer(layer: object) -> object:

	"""

	This function checks whether an object is of class Layer.

	Parameters
	----------
	layer : object
		Any given object.

	Returns
	-------
	object
		It returns 1 if object is of class Layer, or 0 if object is not of class Layer.

	See Also
	--------
	parts.Layer

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 2
		
		    ents = parts.LayersOfPart(model_id, part_type, part_id)
		    for ent in ents:
		        if parts.IsPartLayer(ent):
		            lr = ent
		            print("This is an object of class Layer")
		            print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		            print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LayerOfPartById(layer_id: int, part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_layers` instead.


	This function finds the layer with a specific id of a given part belonging to the specified model.

	Parameters
	----------
	layer_id : int
		Id of the layer.

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a layer object with the given id.
		Else, None is returned.

	See Also
	--------
	parts.Layer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 2
		    layer_id = 4
		
		    lr = parts.LayerOfPartById(model_id, part_type, part_id, layer_id)
		    if lr:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_layers instead.", DeprecationWarning)

def LayerOfPartBySerial(part_id: int, part_type: int, serial: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_layers` instead.


	This function finds the layer with a specific serial number (serial) of a given part belonging to the specified model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	serial : int
		Serial number of the layer.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a Layer object with the given serial number.
		Else, None is returned.

	See Also
	--------
	parts.Layer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 2
		    serial = 1
		
		    lr = parts.LayerOfPartBySerial(model_id, part_type, part_id, serial)
		    if lr:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_layers instead.", DeprecationWarning)

def LayersOfPart(part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_layers` instead.


	This function collects all layers of a given part belonging to the specified model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Layer referring to one specific layer of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Layer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		
		    layers = parts.LayersOfPart(model_id, part_type, part_id)
		    for lr in layers:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_layers instead.", DeprecationWarning)

def LayersOfPartByName(layer_name: str, part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_layers` instead.


	This function collects all layers with a specific name (layer_name) of a given part belonging to the specified model.

	Parameters
	----------
	layer_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Layer referring to one specific layer of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Layer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    name = "*layer*"
		
		    all_layers = parts.LayersOfPartByName(model_id, part_type, part_id, name)
		    for lr in all_layers:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_layers instead.", DeprecationWarning)

def MaterialLimitOfPart(limit_type: str, part_id: int, part_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_material_limit` instead.


	This function calculates material limit of a part with a specific id and type of a given model.

	Parameters
	----------
	limit_type : str, optional
		Type of the material limit which will be calculated. Its possible values are:
		- 'tension': Part material limit in tension
		- 'compression': Part material limit in compression
		- 'shear': Part material limit in shear.
		If it is absent, then the material limit of the part will be returned.

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	float
		It returns a float value referring to the material limit of the specified part.
		Upon failure, 0.0 is returned.

	See Also
	--------
	parts.AddMaterialLimitOnPart, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    limit_type = "tension"
		    mat_limit = parts.MaterialLimitOfPart(model_id, part_type, part_id, limit_type)
		    print(mat_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_material_limit instead.", DeprecationWarning)

def MaxCoordinatesOfPart(part_id: int, part_type: int, result: object, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constants).

	result : object
		An object of class Result that refers to a Resultset of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 node objects of the corresponding nodes with the maximum coordinates in each direction of the specified part.
		Each index of the list corresponts to the following nodes:
		- 0 = Node with the maximum X coordinate
		- 1 = Node with the maximum Y coordinate
		- 2 = Node with the maximum Z coordinate
		Upon failure, an empty is returned.

	See Also
	--------
	results.Result, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    max_node = parts.MaxCoordinatesOfPart(model_id, part_type, part_id, result)
		    if max_node:
		        max_x_node = max_node[
		            0
		        ]  # Object of class Node for the node with the maximum X coordinate
		        print(max_x_node.x)  # X maximum coordinate
		        print(
		            max_x_node.y, max_x_node.z
		        )  # Coordinates in rest directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = max_node[
		            1
		        ]  # Object of class Node for the node with the maximum Y coordinate
		        print(max_y_node.y)  # Y maximum coordinate
		        print(
		            max_y_node.x, max_y_node.z
		        )  # Coordinates in rest directions of the node with the maximum Y coordinate
		        print(max_y_node.id)  # Id of the node with the maximum Y coordinate
		
		        max_z_node = max_node[
		            2
		        ]  # Object of class Node for the node with the maximum Z coordinate
		        print(max_z_node.z)  # Z maximum coordinate
		        print(
		            max_z_node.x, max_z_node.y
		        )  # Coordinates in rest directions of the node with the maximum Z coordinate
		        print(max_z_node.id)  # Id of the node with the maximum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_coordinates instead.", DeprecationWarning)

def MaxDeformationOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constants).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 deformation objects of the corresponding maximum deformations in each direction for the specified part.
		Each index of list contains:
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    max_deform = parts.MaxDeformationOfPart(result, part_type, part_id)
		    if max_deform:
		        max_x_deform = max_deform[0]  # Object with maximum deformation in direction X
		        print(max_x_deform.x)  # X maximum deformation
		        print(
		            max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformation in rest directions of the node with the maximum X deformation
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[1]  # Object with maximum deformation in direction Y
		        print(max_y_deform.y)  # Y maximum deformation
		        print(
		            max_y_deform.x, max_x_deform.z, max_y_deform.total
		        )  # Deformation in rest directions of the node with the maximum Y deformation
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[2]  # Object with maximum deformation in direction Z
		        print(max_z_deform.z)  # Z maximum deformation
		        print(
		            max_z_deform.x, max_x_deform.y, max_z_deform.total
		        )  # Deformation in rest directions of the node with the maximum Z deformation
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z coordinate
		
		        max_total_deform = max_deform[3]  # Object with maximum TOTAL deformation
		        print(max_total_deform.total)  # TOTAL maximum deformation
		        print(
		            max_total_deform.x, max_total_deform.y, max_total_deform.total
		        )  # Deformations in rest directions on the node with the maximum TOTAL deformation
		        print(
		            max_total_deform.node_id
		        )  # Id of the node with the maximum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_deformations instead.", DeprecationWarning)

def MetaSubtypeOfPart(model_id: int, part_type: int, part_subtype: str) -> int:

	"""

	This function converts a given part subtype of a deck of a given model to the corresponding META subtype.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Deck type of the part.

	part_subtype : str
		Deck subtype of the part.

	Returns
	-------
	int
		It returns an integer referring to the META subtype of the corresponding given part subtype of the specified model.
		Upon failure, it returns 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_subtype = "PShear"
		
		    meta_subtype = parts.MetaSubtypeOfPart(model_id, part_type, part_subtype)
		    print(meta_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaTypeOfPart(model_id: int, part_type: str) -> int:

	"""

	This function converts a given part type of a deck of a given model to the corresponding META part type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : str
		Deck type of the part.

	Returns
	-------
	int
		It returns an integer referring to the META constant of the corresponding given part type of the specified model.
		Upon failure, it returns a negative value.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_type = "PShell"
		
		    meta_type = parts.MetaTypeOfPart(model_id, part_type)
		    print(meta_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MinCoordinatesOfPart(part_id: int, part_type: int, result: object, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 node objects of the corresponding nodes with the minimum coordinates in each direction of the specified part.
		Each index of the list corresponts to the following nodes:
		- 0 = Node with the minimum X coordinate
		- 1 = Node with the minimum Y coordinate
		- 2 = Node with the minimum Z coordinate
		Upon failure, an empty is returned.

	See Also
	--------
	results.Result, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    min_node = parts.MinCoordinatesOfPart(model_id, part_type, part_id, result)
		    if min_node:
		        min_x_node = min_node[
		            0
		        ]  # Object of class Node for the node with the minimun X coordinate
		        print(min_x_node.x)  # X minimun coordinate
		        print(
		            min_x_node.y, min_x_node.z
		        )  # Coordinates in rest directions of the node with the minimun X coordinate
		        print(min_x_node.id)  # Id of the node with the minimun X coordinate
		
		        min_y_node = min_node[
		            1
		        ]  # Object of class Node for the node with the minimun Y coordinate
		        print(min_y_node.y)  # Y minimun coordinate
		        print(
		            min_y_node.x, min_y_node.z
		        )  # Coordinates in rest directions of the node with the minimun Y coordinate
		        print(min_y_node.id)  # Id of the node with the minimun Y coordinate
		
		        min_z_node = min_node[
		            2
		        ]  # Object of class Node for the node with the minimun Z coordinate
		        print(min_z_node.z)  # Z minimun coordinate
		        print(
		            min_z_node.x, min_z_node.y
		        )  # Coordinates in rest directions of the node with the minimun Z coordinate
		        print(min_z_node.id)  # Id of the node with the minimun Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_coordinates instead.", DeprecationWarning)

def MinDeformationOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL), of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 deformation objects of the corresponding minimum deformations in each direction for the specified part.
		Each index of list contains:
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    min_deform = parts.MinDeformationOfPart(result, part_type, part_id)
		    if min_deform:
		        min_x_deform = min_deform[0]  # Object with minimum deformation in direction X
		        print(min_x_deform.x)  # X minimum deformation
		        print(
		            min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformation in rest directions of the node with the minimum X deformation
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[1]  # Object with minimum deformation in direction Y
		        print(min_y_deform.y)  # Y minimum deformation
		        print(
		            min_y_deform.x, min_y_deform.z, min_y_deform.total
		        )  # Deformation in rest directions of the node with the minimum Y deformation
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[2]  # Object with minimum deformation in direction Z
		        print(min_z_deform.z)  # Z minimum deformation
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.total
		        )  # Deformation in rest directions of the node with the minimum Z deformation
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z coordinate
		
		        min_total_deform = min_deform[3]  # Object with minimum TOTAL deformation
		        print(min_total_deform.total)  # TOTAL minimum deformation
		        print(
		            min_total_deform.x, min_total_deform.y, min_total_deform.total
		        )  # Deformations in rest directions on the node with the minimum TOTAL deformation
		        print(
		            min_total_deform.node_id
		        )  # Id of the node with the minimum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_deformations instead.", DeprecationWarning)

def MinMaxCentroidScalarOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CentroidScalar objects of the corresponding minimum and maximum centroid scalar values for the specified part.
		- 0 = MINIMUM centroid scalar
		- 1 = MAXIMUM centroid scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    centroid = parts.MinMaxCentroidScalarOfPart(result, part_type, part_id)
		    if centroid:
		        min_centroid = centroid[
		            0
		        ]  # Object of class CentroidScalar with the minimum centroid scalar value
		        print(min_centroid.value)  # Minimum centroid scalar value
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid scalar value
		        max_centroid = centroid[
		            1
		        ]  # Object of class CentroidScalar with the maximum centroid scalar value
		        print(max_centroid.value)  # Maximum centroid scalar value
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxCentroidVectorOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CentroidVector objects of the corresponding minimum and maximum centroid vector values for the specified part.
		- 0 = MINIMUM centroid vector
		- 1 = MAXIMUM centroid vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		    centroid = parts.MinMaxCentroidVectorOfPart(result, part_type, part_id)
		    if centroid:
		        min_centroid = centroid[
		            0
		        ]  # Object of class CentroidVector with the minimum centroid vector value
		        print(min_centroid.value)  # Minimum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the minimum centroid vector
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid vector value
		        max_centroid = centroid[
		            1
		        ]  # Object of class CentroidVector with the maximum centroid vector value
		        print(max_centroid.value)  # Maximum centroid vector value
		        print(
		            max_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the maximum centroid vector
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_centroid_vector instead.", DeprecationWarning)

def MinMaxCornerScalarOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CornerScalar objects of the corresponding minimum and maximum corner scalar values for the specified part.
		The list contains at index:
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    corner = parts.MinMaxCornerScalarOfPart(result, part_type, part_id)
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
		        print(max_corner.value)  # Maximum corner scalar value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element with the maximum corner scalar value
		        print(
		            max_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_corner_scalar instead.", DeprecationWarning)

def MinMaxNodalScalarOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalScalar objects of the corresponding minimum and maximum nodal scalar values for the specified part.
		The index of the list refers to:
		- 0 = MINIMUM nodal scalar
		- 1 = MAXIMUM nodal scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    nodal = parts.MinMaxNodalScalarOfPart(result, part_type, part_id)
		    if nodal:
		        min_nodal = nodal[0]  # Object with the minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal scalar value
		        print(min_nodal.part_id)  # Id of the part with the minimum nodal scalar value
		
		        max_nodal = nodal[1]  # Object with the maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(max_nodal.part_id)  # Id of the part with the maximum nodal scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxNodalVectorOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector values of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalVector objects of the corresponding minimum
		and maximum nodal vector values for the specified part.
		The list contains at index:
		- 0 = MINIMUM nodal vector
		- 1 = MAXIMUM nodal vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    nodal = parts.MinMaxNodalVectorOfPart(result, part_type, part_id)
		    if nodal:
		        min_nodal = nodal[0]  # Object with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector value
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(min_nodal.part_id)  # Id of the part
		
		        max_nodal = nodal[1]  # Object with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector value
		        print(max_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(max_nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodal_vector instead.", DeprecationWarning)

def NamedColorOfPart(model_id: int, part_type: int, part_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_color` instead.


	This function finds the name of the color of a part of a model with a given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	window_name : str
		Name of the window of the part. If it is absent then this function will return the color of the part for the first enabled window of the model of the part.

	Returns
	-------
	str
		It returns a string with the name of the color of the corresponding part of the given model for the specified window.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    window_name = "MetaPost"
		    named_color = parts.NamedColorOfPart(model_id, part_type, part_id, window_name)
		    print(named_color)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_color instead.", DeprecationWarning)

def NeighbourParts(part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_parts` instead.


	This function collect the neighbour parts of a given part of a specified model. Neighbour parts are these which are directly attached to the specified part.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific neighbour part of the given model and part.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    neighbour_parts = parts.NeighbourParts(model_id, part_type, part_id)
		    for p in neighbour_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_parts instead.", DeprecationWarning)

def NodalScalarOfPart(layer: str, part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a part with specific id and type of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class NodalScalar referring to the nodal scalar values of a node of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    all_part_nodal = parts.NodalScalarOfPart(result, part_type, part_id)
		    few_part_nodal = all_part_nodal[0 : min(10, len(all_part_nodal))]
		    for nodal in few_part_nodal:  # List with objects of class NodalScalar
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfPart(layer: str, part_type: int, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodal_vector` instead.


	This function calculates all nodal vector values of the nodes of a part with specific id and type of a given model.

	Parameters
	----------
	layer : str
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	part_type : int
		Type of the part (META constant).

	result : 
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class NodalVector referring to the nodal vector values of a node of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    all_part_nodal = parts.NodalVectorOfPart(result, part_type, part_id)
		    few_part_nodal = all_part_nodal[0 : min(10, len(all_part_nodal))]
		    for nodal in few_part_nodal:  # List with objects of class NodalVector
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodal_vector instead.", DeprecationWarning)

def NumOfPartsByType(model_id: int, part_type: int) -> int:

	"""

	This function finds the number of the parts of a model with a specific type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	Returns
	-------
	int
		It returns the number of the parts with the specific type for the given model.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    num_of_parts = parts.NumOfPartsByType(model_id, part_type)
		    print(num_of_parts)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PartById(model_id: int, part_type: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds part of a model with a given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	object
		Upon success, it returns a part object with the given id and type.
		Else, None is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    p = parts.PartById(model_id, part_type, part_id)
		    if p:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def Parts(model_id: int) -> object:

	"""

	This function collects all parts of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    all_parts = parts.Parts(model_id)
		    for p in all_parts:
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


	"""

def PartsByComments(model_id: int, part_comments: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds the parts of a model with specific comments.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_comments : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model and part.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_comments = "Roof"
		    all_parts = parts.PartsByComments(model_id, part_comments)
		    for p in all_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PartsByIdAllTypes(model_id: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds all the parts of a model with the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_id = 1
		    collected_parts = parts.PartsByIdAllTypes(model_id, part_id)
		    for p in collected_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PartsByName(model_id: int, part_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds the parts of a model with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_name = "*RAIL*"
		
		    collected_parts = parts.PartsByName(model_id, part_name)
		    for p in collected_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PartsByType(model_id: int, part_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function collects all parts with a specific type of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    all_parts = parts.PartsByType(model_id, part_type)
		    for p in all_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PartsFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect parts of a model specified by the given id through some advanced filters. The execution of the script will stop and a window will open in order for the user to specify its advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    collected_parts = parts.PartsFromAdvFilters(model_id, resultset)
		    for p in collected_parts:
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


	"""

def PartsListToDict(parts: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Part.

	Parameters
	----------
	parts : object
		List with objects of class Part.

	Returns
	-------
	object
		It returns a dictionary whose keys are the ids of the parts and values the corresponding Part objects.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    all_parts = parts.Parts(model_id)
		
		    dict_parts = parts.PartsListToDict(all_parts)
		    for id, p in dict_parts.items():
		        print(id)
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


	"""

def PartsOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all parts of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, default value is 1.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific part of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    group_parts = parts.PartsOfGroup(model_id, group_name, group_instance)
		    for p in group_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def PartsOfGroupByType(model_id: int, group_name: str, part_type: int, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all parts with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	part_type : int
		Type of the part (META constant).

	group_instance : int
		Instance of the group. If it is absent, default value is 1.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific part of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    part_type = constants.PSHELL
		    group_instance = 1
		    group_parts = parts.PartsOfGroupByType(
		        model_id, group_name, part_type, group_instance
		    )
		    for p in group_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def PartsOfMaterial(material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_parts` instead.


	This function collects all parts with a given material for the specified model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific part of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    material_parts = parts.PartsOfMaterial(model_id, material_type, material_id)
		    for p in material_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_parts instead.", DeprecationWarning)

def PartsOfNode(node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_parts` instead.


	This function collects all the parts that contain a given node for a specified model.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific part of the given node.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    node_id = 8243
		    node_parts = parts.PartsOfNode(model_id, node_id)
		    for p in node_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_parts instead.", DeprecationWarning)

def PartsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_parts` instead.


	This function searches for the parts of an overlay run with a given type and a given id.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Type of the overlay run. Possible values:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one part of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_parts = parts.PartsOfOverlayRun(overlay_run_type, overlay_run_id)
		    for p in overlay_run_parts:
		        print(p.id, p.type, p.subtype, p.visible, p.name)
		        print(p.mat_id, p.shell_thick, p.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_parts instead.", DeprecationWarning)

def PartsTypes(model_id: int) -> object:

	"""

	This function collects all types of parts of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with all types of the parts of the given model.
		Each element of the list is an integer referring to one type (META constant) of parts for the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    all_types = parts.PartsTypes(model_id)
		    for part_type in all_types:
		        print(part_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PartsWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds the parts of a model for which comments exist.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to a part of the model for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.CommentsOfPart, parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    parts_with_comments = parts.PartsWithComments(model_id)
		    for p in parts_with_comments:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PartsWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds the parts of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to a part of the model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    parts_with_name = parts.PartsWithName(model_id)
		    for p in parts_with_name:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def PickParts(model_id: int, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_parts` instead.


	This function allows the user to pick parts of a model specified by the given id. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	model_id : int
		Id of the model.

	message : str
		Message displayed to the user.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific picked part of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    message = "Select Parts and press Enter when you are ready"
		    picked_parts = parts.PickParts(model_id, message)
		
		    for p in picked_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_parts instead.", DeprecationWarning)

def RemotePShellPSolidPartsOfNode(level: int, node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_parts` instead.


	This function collects remote parts of type PSHELL and PSOLID of a given node for a specified model.

	Parameters
	----------
	level : int
		An integer equal to or greater than zero which defines the depth of the search for PSHELL and PSOLID parts (e.g. 0 = directly attached to the part, 1 = one element away from the part etc.).

	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific PSHELL and PSOLID parts of the given node.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    node_id = 20
		    level = 1
		    remote_parts = parts.RemotePShellPSolidPartsOfNode(model_id, node_id, level)
		    for p in remote_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_parts instead.", DeprecationWarning)

def ReportNewParts() -> object:

	"""

	This function collects the newly created parts from the last call of script function CollectNewPartsStart(). This function should be preceded by a corresponding call to script function CollectNewPartsStart() and should be followed by a corresponding call to script function CollectNewPartsEnd().

	Returns
	-------
	object
		It returns a list with the part objects of the corresponding newly created parts.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import utils
		
		
		def main():
		    parts.CollectNewPartsStart()
		
		    # create new parts
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_parts = parts.ReportNewParts()
		    for p in new_parts:
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


	"""

def ShellNormalOfPart(part_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_shell_normal` instead.


	This function calculates the shell normal vectors of the elements of a part with type PSHELL and a specific id of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class CentroidVector referring to the shell normal vector of an element of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_id = 1
		    part_normal = parts.ShellNormalOfPart(result, part_id)
		    iter_end = min(10, len(part_normal))
		    for shell_normal in part_normal[
		        0:iter_end
		    ]:  # List with objects of class CentroidVector (shell normal vector)
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_shell_normal instead.", DeprecationWarning)

def ShowPart(model_id: str, part_id: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.show` instead.


	This function allows the user to make visible a part of a model specified by a given id.

	Parameters
	----------
	model_id : str
		Id of the model.

	part_id : str
		Id of the part.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	parts.ShowSomeParts

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_id = 1
		    ret = parts.ShowPart(model_id, part_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.show instead.", DeprecationWarning)

def ShowSomeParts(model_id: int, part_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.show_parts` instead.


	This function allows the user to make visible some specific parts of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_ids : object
		List with Ids of the parts as integers.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		
		    part_ids = list()
		    all_parts = parts.Parts(model_id)
		    for p in all_parts:
		        part_ids.append(p.id)
		    ret = parts.ShowSomeParts(model_id, part_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.show_parts instead.", DeprecationWarning)

def StringPartType(part_type: int) -> str:

	"""

	This function converts a given META part type to its corresponding string representation.

	Parameters
	----------
	part_type : int
		Type of the part (META constant).

	Returns
	-------
	str
		It returns a string with the name of the META part type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    part_type = constants.PSHELL
		    str_part_type = parts.StringPartType(part_type)
		    print(str_part_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdatePart(part: object) -> object:

	"""

	This function updates the attributes of the given part object. Update is based in the fields 'id', 'type' and 'model_id' of the given part object.

	Parameters
	----------
	part : object
		Object of class Part.

	Returns
	-------
	object
		Upon success, it returns the new updated part object.
		Else, None is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import utils
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    p = parts.PartById(model_id, part_type, part_id)
		    if p:
		        # command which alter the attributes of the part object
		        utils.MetaCommand('name pid "pshell_1" 1')
		
		        p = parts.UpdatePart(p)
		
		        if p:  # Update OK
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
		        else:  # Update Failed
		            print("This is not a valid part object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdatePartLayer(layer: object) -> object:

	"""

	This function updates the data of the given layer object. Update is based in the fields 'serial', 'part_type', 'part_id' and 'model_id' of the given layer object.

	Parameters
	----------
	layer : object
		Object of class Layer.

	Returns
	-------
	object
		Upon success, it returns the new updated layer object.
		Else, None is returned.

	See Also
	--------
	parts.Layer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import utils
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    layer_id = 2
		
		    lr = parts.LayerOfPartById(model_id, part_type, part_id, layer_id)
		    if lr:
		        # commands which alter the attributes of the layer object
		        # utils.MetaCommand('...
		
		        lr = parts.UpdatePartLayer(lr)
		
		        if lr:  # Update OK
		            print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		            print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		        else:  # Update Failed
		            print("This is not a valid layer object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleParts(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function collects all visible parts of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_parts = parts.VisibleParts(model_id, window_name)
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def VisiblePartsByType(model_id: int, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function collects all visible parts with a specific type of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    window_name = "MetaPost"
		    visible_parts = parts.VisiblePartsByType(model_id, part_type, window_name)
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def VisiblePartsOfGroup(model_id: int, group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all visible parts of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific visible part of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    window_name = "MetaPost"
		    visible_parts = parts.VisiblePartsOfGroup(model_id, group_name, window_name)
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def VisiblePartsOfGroupByType(model_id: int, group_name: str, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all visible parta with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	part_type : int
		Type of the part (META constant).

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific visible part of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    part_type = constants.PSHELL
		    window_name = "MetaPost"
		    visible_parts = parts.VisiblePartsOfGroupByType(
		        model_id, group_name, part_type, window_name
		    )
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def VisiblePartsOfGroupInstance(model_id: int, group_name: str, group_instance: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all visible parts of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	window_name : str
		Name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific visible part of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    window_name = "MetaPost"
		    visible_parts = parts.VisiblePartsOfGroupInstance(
		        model_id, group_name, group_instance, window_name
		    )
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def VisiblePartsOfGroupInstanceByType(model_id: int, group_name: str, group_instance: int, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_parts` instead.


	This function collects all visible parts with a specific type of a given group instance nelonging to the specified model. Part type must be one of META KEYWORDS. A full META KEYWORD list for parts can be found under library category "betameta_structs". Optional argument "window_name" refers to the name of the window of the model. If optional argument "window_name" is absent then this function will collect visible parts for the active or first enabled window of the model. This function works for the active page.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	part_type : int
		Type of the part (META constant).

	window_name : str
		Name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific visible part of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    part_type = constants.PSHELL
		    window_name = "MetaPost"
		    visible_parts = parts.VisiblePartsOfGroupInstanceByType(
		        model_id, group_name, group_instance, part_type, window_name
		    )
		    for p in visible_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_parts instead.", DeprecationWarning)

def AreaOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_area` instead.


	This function calculates the area of a part with specific id and type of a given model. For line parts (PBAR, PBEAM, PTUBE, PROD, PBEND, PGAP) the area of their cross-section is calculated. For the case of PBEAM parts with multiple cross-sections, the area of the 1st cross-section is calculated. For PSOLID parts the area is calculated as the sum of the external faces of their solid elements.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model. If it is absent, then area will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a float value being the calculated area of the specified part.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		    area = parts.AreaOfPart(all_resultsets[0], part_type, pid)
		    print("area = " + str(area))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_area instead.", DeprecationWarning)

def CogCoordinatesOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_cog_coordinates` instead.


	This function calculates the coordinates of the geometrical center of gravity of a PSHELL or PSOLID part of a given model for a specific resultset.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list containing the coordinates of the geometrical center of gravity of the specified part.
		Upon failure, invalid coordinates [0 0 0] will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    part_id = 1
		
		    cog = parts.CogCoordinatesOfPart(all_resultsets[0], part_type, part_id)
		
		    print(cog[0], cog[1], cog[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_cog_coordinates instead.", DeprecationWarning)

def SetColorOfPart(alpha: int, blue: int, green: int, part_id: int, part_type: int, red: int, window_name: str, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.set_color` instead.


	This function sets color of a part of a model with a given id and a given type.

	Parameters
	----------
	alpha : int
		Alpha channel.

	blue : int
		Blue value.

	green : int
		Green value.

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	red : int
		Red value.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will set the color of the part of the model for the first enabled window.

	model_id : int
		Id of the model.

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
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 54
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    window_name = "MetaPost"
		    ret = parts.SetColorOfPart(
		        model_id, part_type, part_id, red, green, blue, alpha, window_name
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.set_color instead.", DeprecationWarning)

def LaminatesIds(model_id: int) -> object:

	"""

	This function finds the ids of laminates of a model with a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to the number or the id of a laminate of the given model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    all_laminates = parts.LaminatesIds(model_id)
		    for laminate_id in all_laminates:
		        print(laminate_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PartsOfLaminate(laminate_id: int, model_id: int) -> object:

	"""

	This function collects all parts of a given laminate belonging to the specified model.

	Parameters
	----------
	laminate_id : int
		Id of the laminate.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific part of the given laminate.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    laminate_id = 1
		    laminate_parts = parts.PartsOfLaminate(model_id, laminate_id)
		    for p in laminate_parts:
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


	"""

def DistancePartToCutPlane(part_id: int, part_result: object, part_type: int, plane_name: str, part_model: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_distance_from_cut_plane` instead.


	This function calculates the distance or the elongation of a part from an existing cut plane.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constant).

	plane_name : str
		Name of the cut plane.

	part_model : int
		Id of the model of the part.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In index 0 there is the distance in X direction.
		- In index 1 there is the distance in Y direction.
		- In index 2 there is the distance in Z direction.
		- In index 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		    plane_name = "DEFAULT_PLANE_XY"
		    distance = parts.DistancePartToCutPlane(
		        part_model, part_result, part_type, part_id, plane_name
		    )
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_distance_from_cut_plane instead.", DeprecationWarning)

def MassOfPart(part_id: int, part_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_mass` instead.


	This function calculates the mass (including NSM) of a part specified by its id, type, and the model id. For the case of parts with composite materials the mass portion not attributed to NSM is calculated by averaging the density of each composite layer weighted by its relative thickness.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	float
		It returns a float value being the calculated mass of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    pid = 1
		    mass = parts.MassOfPart(model_id, part_type, pid)
		    print("mass = " + str(mass))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_mass instead.", DeprecationWarning)

def MassOfPartNoNsm(part_id: int, part_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_mass_no_nsm` instead.


	This function calculates the mass excluding NSM of a part specified by its id, type, and the owner model id. For the case of parts with composite materials mass is calculated by averaging the density of each composite layer weighted by its relative thickness.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	float
		It returns a float value being the calculated mass of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    pid = 1
		    mass = parts.MassOfPartNoNsm(model_id, part_type, pid)
		    print("mass = " + str(mass))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_mass_no_nsm instead.", DeprecationWarning)

def PartOfElement(model_id: int, element_id: int, element_type: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_parts` instead.


	This function finds the part of an element of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	object
		Upon success, it returns a part object with the part of the element.
		Else, a non valid part object is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import parts
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    p = parts.PartOfElement(model_id, element_type, element_id, second_id)
		    if p:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_parts instead.", DeprecationWarning)

def PreviewCompositeReport(part_id: int, model_id: int, part_type: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.preview_composite_report` instead.


	This function shows a preview of the produced html report for composite parts.

	Parameters
	----------
	part_id : int
		Id of the part.

	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	Returns
	-------
	int
		Upon execution, a report window will be opened.
		If part with composite layers is found the function returns 1.
		Upon failure, the function returns 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 101
		    ret = parts.PreviewCompositeReport(model_id, part_type, part_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.preview_composite_report instead.", DeprecationWarning)

def AreaIntegralOfPart(result: object, part_type, part_id) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_area_integral` instead.


	This function calculates the integral of a resultset over the area of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : 
		Type of the part (META constant).

	part_id : 
		Id of the part.

	Returns
	-------
	float
		It returns a float value as the result of the calculated area integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    part_type = constants.PSHELL
		    part_id = 1
		    areaint = parts.AreaIntegralOfPart(result, part_type, part_id)
		    print(areaint)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_area_integral instead.", DeprecationWarning)

def PartsOfIsofunction(window_name: str, iso_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_parts` instead.


	This function collects all parts from which the given isofunction passes for the specified window.

	Parameters
	----------
	window_name : str
		Window name.

	iso_name : str
		Isofunction name.

	Returns
	-------
	object
		It returns a list where each member is an object of class Part and refers to a part that comprises the isofunction.
		Else, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "IsoFun"
		    iso_parts = parts.PartsOfIsofunction(window_name, iso_name)
		    for p in iso_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_parts instead.", DeprecationWarning)

def PropertyOfPart(model_id: int, part_type: int, part_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_property` instead.


	This function returns the properties of a part with a specific id and belonging to a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	str
		It returns a string referring to the properties of the specified part as they are specified in geometry file.
		Else, a zero value or an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    property_value = parts.PropertyOfPart(model_id, part_type, part_id)
		    print(property_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_property instead.", DeprecationWarning)

def VolumeIntegralOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_volume_integral` instead.


	This function calculates the integral of a resultset over the volume of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then volume integral will refer to the ORIGINAL STATE.

	part_type : int
		Type of part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated volume integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    part_type = constants.PSOLID
		    part_id = 4
		    volume = parts.VolumeIntegralOfPart(result, part_type, part_id)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_volume_integral instead.", DeprecationWarning)

def VolumeOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_volume` instead.


	This function calculates the volume of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated volume of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[0]
		    part_type = constants.PSOLID
		    part_id = 4
		    volume = parts.VolumeOfPart(result, part_type, part_id)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_volume instead.", DeprecationWarning)

def NeighbourPartsOfElement(model_id: int, element_type: int, element_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_parts` instead.


	This function collect the neighbour parts of a given element of a specified model. Neighbour parts are these which are directly attached to the specified part or defined in the geometry file.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Part referring to one specific neighbour part of the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    neighbour_parts = elements.NeighbourPartsOfElement(
		        model_id, element_type, element_id, second_id
		    )
		    for p in neighbour_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_parts instead.", DeprecationWarning)

def PartsBySolverIdAllTypes(model_id: int, part_path: str, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_parts` instead.


	This function finds all the parts of a model with hierarchical structure defined by id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given part is limited.

	part_id : int
		Id of the part.

	Returns
	-------
	object
		This function returns a list with objects of class Node referring to the corresponding parts found.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    model_id = 0
		    part_path = "Truck->14"
		    part_id = 6
		    collected_parts = parts.PartsBySolverIdAllTypes(model_id, part_path, part_id)
		
		    for p in collected_parts:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_parts instead.", DeprecationWarning)

def CornerVectorOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_corner_vector` instead.


	This function calculates all corner vector values of the elements of a part with a specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class CornerVector referring to one corner vector values of an element of the specified part.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    all_part_corner = parts.CornerVectorOfPart(result, part_type, part_id)
		    few_part_corner = all_part_corner[0 : min(10, len(all_part_corner))]
		    for corn in few_part_corner:  # list with CornerScalar objects
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_corner_vector instead.", DeprecationWarning)

def MinMaxCornerVectorOfPart(part_id: int, part_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_corner_vector` instead.


	This function calculates minimum and maximum corner vector value of a part with specific id and type of a given model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CornerVector objects of the corresponding minimum and maximum corner scalar values for the specified part.
		The list contains at index:
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    part_type = constants.PSHELL
		    part_id = 1
		
		    corner = parts.MinMaxCornerVectorOfPart(result, part_type, part_id)
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
		        print(max_corner.value)  # Maximum corner scalar value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_corner_vector instead.", DeprecationWarning)

def AreaWeightedAverageOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_area_weighted_average` instead.


	This function calculates the area weighted average of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated area weighted average of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    area = parts.AreaWeightedAverageOfPart(all_resultsets[1], part_type, pid)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_area_weighted_average instead.", DeprecationWarning)

def VolumeAverageOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_volume_weighted_average` instead.


	This function calculates the volume weighted average of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated volume weighted average of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSOLID
		    pid = 1
		
		    volume = parts.VolumeWeightedAverageOfPart(all_resultsets[1], part_type, pid)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_volume_weighted_average instead.", DeprecationWarning)

def VolumetricFlowOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated volume weighted average of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    volume = parts.VolumetricFlowOfPart(all_resultsets[1], part_type, pid)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_mass_flow` instead.


	This function calculates the mass flow rate of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated mass flow rate of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 6
		
		    mass = parts.MassFlowOfPart(all_resultsets[1], part_type, pid)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_mass_weighted_average` instead.


	This function calculates the mass flow rate of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value being the calculated mass weighted average of the specified part.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    mass = parts.MassWeightedAverageOfPart(all_resultsets[1], part_type, pid)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_mass_weighted_average instead.", DeprecationWarning)

def NormalForceOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_normal_force` instead.


	This function calculates the normal force of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
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
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    normal_force = parts.NormalForceOfPart(all_resultsets[1], part_type, pid)
		    print(normal_force)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_normal_force instead.", DeprecationWarning)

def ShearForceOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_shear_force` instead.


	This function calculates the shear force of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
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
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    shear_force = parts.ShearForceOfPart(all_resultsets[1], part_type, pid)
		    print(shear_force)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_shear_force instead.", DeprecationWarning)

def VectorUniformityIndexOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of a part with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a float value as the result of the calculated vector uniformity index of the part.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    part_type = constants.PSHELL
		    pid = 1
		
		    index = parts.VectorUniformityIndexOfPart(all_resultsets[1], part_type, pid)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_vector_uniformity_index instead.", DeprecationWarning)

def VolumetricFlowOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of a group with specific name of a given model.

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
		It returns a float value being the calculated volumetric flow rate of the specified group.
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
		
		    rate = groups.VolumetricFlowOfGroup(all_resultsets[1], group_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_mass_flow` instead.


	This function calculates the mass flow rate of a group with specific name of a given model.

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
		It returns a float value being the calculated mass flow rate of the specified group.
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
		    group_name = "inlet"
		
		    index = groups.MassFlowOfGroup(all_resultsets[1], group_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_mass_weighted_average` instead.


	This function calculates the weighted average mass flow of a group with specific name of a given model.

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
		It returns a float value being the calculated mass flow rate of the specified group.
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
		
		    mass = groups.MassWeightedAverageOfGroup(all_resultsets[1], group_name)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_mass_weighted_average instead.", DeprecationWarning)

def UniformityIndexOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_uniformity_index` instead.


	This function calculates the uniformity index of a group with specific name of a given model.

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
		It returns a float value being the uniformity index of the specified group.
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
		
		    index = groups.UniformityIndexOfGroup(all_resultsets[1], group_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_uniformity_index instead.", DeprecationWarning)

def VectorUniformityIndexOfGroup(result: object, group_name: str, group_instance: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of a group with specific name of a given model.

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
		It returns a float value being the vector uniformity index of the specified group.
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
		
		    index = groups.VectorUniformityIndexOfGroup(all_resultsets[1], group_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_vector_uniformity_index instead.", DeprecationWarning)

def AttributeOfPart(model_num: int, part_type: int, part_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_num : int
		The number of the model

	part_type : int
		The type of the property

	part_id : int
		The id of the property

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    pid = 200
		    name = "Total_Elements"
		
		    val = parts.AttributeOfPart(model_id, constants.PSHELL, pid, name)
		    print("Value", val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_attributes instead.", DeprecationWarning)

def SetAttributeOfPart(model_num: int, part_type: int, part_id: int, attrib_name: str, attrib_val: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_num : int
		The number of the model

	part_type : int
		The type of the property

	part_id : int
		The id of the property

	attrib_name : str
		Name of the attribute

	attrib_val : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    pid = 200
		    name = "Total"
		    val = "100"
		    parts.SetAttributeOfPart(model_id, constants.PSHELL, pid, name, val)
		    # or
		    name = "n_Total"
		    val = 100
		    attribute_type = "numerical"
		    parts.SetAttributeOfPart(model_id, constants.PSHELL, pid, name, val, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.set_attribute instead.", DeprecationWarning)

def AttributesOfPart(model_id: int, part_type: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_attributes` instead.


	This function collects all attributes of a given part

	Parameters
	----------
	model_id : int
		The number of the model

	part_type : int
		The type of the property

	part_id : int
		The id of the property

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    model_id = 0
		    pid = 200
		
		    all_attributes = parts.AttributesOfPart(model_id, constants.PSHELL, pid)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_attributes instead.", DeprecationWarning)

def CalcPartABCDMatrixThroughThickness(model_num: int, part_type: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_abd_matrix_thickness` instead.


	This function calculates the A,B,C,D matrices through thickness for a stack of a part

	Parameters
	----------
	model_num : int

	part_type : int

	part_id : int

	Returns
	-------
	object
		I returns a 12X3 matrix in the form of a list containing other lists.
		The first 3 lists is the A matrix.
		The next 3 lists is the B matrix.
		The next 3 lists is the C matrix.
		The last 3 lists is the D matrix.
		Upon failure, all the matrix values are 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    # Need some documentation? Run this with F5
		
		    model_id = 0
		    part_id = 4
		    part_type = constants.PSHELL
		
		    ABD_matrix = parts.CalcPartABCDMatrixThroughThickness(model_id, part_type, part_id)
		
		    for tmp_matrix in ABD_matrix:
		        print(tmp_matrix)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_abd_matrix_thickness instead.", DeprecationWarning)

def CalcPartABDMatrix(model_num: int, part_type: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_abd_matrix` instead.


	This function calculates the ABD matrix of the stack of a part .

	Parameters
	----------
	model_num : int

	part_type : int

	part_id : int

	Returns
	-------
	object
		I returns a 6X6 matrix in the form of a list containing other lists.
		Upon failure, all the matrix valuesare 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    # Need some documentation? Run this with F5
		
		    model_id = 0
		    part_id = 4
		    part_type = constants.PSHELL
		
		    ABD_matrix = parts.CalcPartABDMatrix(model_id, part_type, part_id)
		
		    for tmp_matrix in ABD_matrix:
		        print(tmp_matrix)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_abd_matrix instead.", DeprecationWarning)

def IdentifyPartsReset(model_id: int, part_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_parts` instead.


	This function allows the user to reset the identification of all or specific parts of the specified model. It can be called with two different ways. The one is with lists of ids, and the other is with part_ids = 'all'.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_ids : object
		List with Ids of the parts as integers, or string 'all'.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		
		
		def main():
		    part_ids = [1, 2, 3, 4, 5, 6]
		    # or
		    # part_ids = 'all'
		    model_id = 0
		    parts.IdentifyPartsReset(model_id, part_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_parts instead.", DeprecationWarning)

class Part():

	"""

	Class for parts
	
	The type of the part is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corrsponding constant names of constant values.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    p = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    if p:
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
		# method: create_section
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    sec = part.create_section()
		    if sec:
		        print(sec.name, sec.creation_type, sec.sum_point, sec.coord_system)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_abcd_matrix_thickness
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    matrix = part.get_abcd_matrix_thickness()
		    print(matrix)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_abd_matrix
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    matrix = part.get_abd_matrix()
		    print(matrix)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_area(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_area_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_area_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    part_centroid = part.get_centroid_scalar(resultset, specifier)
		    # part_centroid = part.get_centroid_scalar(resultset, specifier, layer = 'top')
		    for centroid in part_centroid:
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element"]
		
		    values, elems = part.get_centroid_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    part_centroid = part.get_centroid_vector(resultset, specifier)
		    # part_centroid = part.get_centroid_vector(resultset, specifier, layer = 'top')
		    # part_centroid = part.get_centroid_vector(resultset, specifier, layer = 'top', principal = 'third')
		    for centroid in part_centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Value and Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element"]
		
		    xyz, magn, elems = part.get_centroid_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_cog_coordinates
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_cog_coordinates(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    col = part.get_color(w)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_comments
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    comments = part.get_comments()
		    print(comments)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    specifier = "min"
		    coords = part.get_coordinates(specifier)
		    # coords = part.get_coordinates(specifier, resultset=res)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    specifier = "min"
		    part_corner = part.get_corner_scalar(res, specifier)
		    # part_centroid = part.get_corner_scalar(res, specifier, layer = 'top')
		    for corn in part_corner:  # Matrix with corner_scalar structs
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
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element", "corner_id"]
		
		    values, elems, corners = part.get_corner_scalar(
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
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    res = m.get_current_resultset()
		    specifier = "min"
		    part_corner = part.get_corner_vector(res, specifier)
		    part_centroid = part.get_corner_vector(res, specifier, layer="top")
		    for corn in part_corner:  # Matrix with corner_scalar structs
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
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    np_specifier = ["xyz", "magnitude", "element", "corner_id"]
		
		    xyz, magn, elems, corners = part.get_corner_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_subtype
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    subtype = part.get_deck_subtype()
		    print(subtype)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_type
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    type = part.get_deck_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_type
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    type = part.get_deck_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=1, type=constants.PSOLID, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    deforms = part.get_deformations(resultset, specifier)
		    for deform in deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    part = parts.Part(id=1, type=constants.PSOLID, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, mag, nodes = part.get_deformations(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(mag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_boundary
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import boundaries
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    boundary = boundaries.Boundary(id=1, type=constants.SPC, second_id=0, model_id=m.id)
		    dist = part.get_distance_from_boundary(res, boundary, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_cut_plane
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    plane = planes.Plane(name="plane_name")
		    dist = part.get_distance_from_cut_plane(res, plane)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import elements
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    elem = elements.Element(id=100, type=constants.SHELL, second_id=-1, model_id=m.id)
		    dist = part.get_distance_from_element(res, elem, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    dist = part.get_distance_from_group(res, group, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=100, model_id=m.id)
		    dist = part.get_distance_from_line(res, node1, res, node2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line_coords
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [-1.25, -2.32, 2]
		    point2 = [-1.35, -0.9, 3.5]
		    dist = part.get_distance_from_line_coords(res, point1, point2)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_node
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node = nodes.Node(id=100, model_id=m.id)
		    dist = part.get_distance_from_node(res, node, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    part2 = parts.Part(id=3, type=constants.PSOLID, model_id=m.id)
		    dist = part.get_distance_from_part(res, part2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=100, model_id=m.id)
		    node3 = nodes.Node(id=1000, model_id=m.id)
		    dist = part.get_distance_from_plane(res, node1, res, node2, res, node3, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [-1.25, -2.32, 2]
		    point2 = [-1.35, -0.9, 3.5]
		    point3 = [0, 0, 0]
		    dist = part.get_distance_from_plane_coords(res, point1, point2, point3)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "all"
		    elems = part.get_elements(specifier)
		    # elems = part.get_elements(specifier, type=constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "outer"
		    elems = part.get_elements(specifier)
		    # elems = part.get_elements(specifier, type=constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    elems = part.get_elements(specifier, window=w)
		    # elems = part.get_elements(specifier, window = w, type=constants.SOLID)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "neighbour"
		    elems = part.get_elements(specifier)
		    # elems = part.get_elements(specifier, type=constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    elems = part.get_elements(specifier, point_coordinates=point)
		    # elems = part.get_elements(specifier, point_coordinates = point , resultset =res)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_boundary
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import boundaries
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    boundary = boundaries.Boundary(id=1, type=constants.SPC, second_id=0, model_id=m.id)
		    elong = part.get_elongation_from_boundary(res, boundary, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_cut_plane
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    plane = planes.Plane(name="plane_name")
		    elong = part.get_elongation_from_cut_plane(res, plane)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import elements
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    elem = elements.Element(id=100, type=constants.SHELL, second_id=-1, model_id=m.id)
		    elong = part.get_elongation_from_element(res, elem, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    group = groups.Group(name="group_name", model_id=m.id)
		    elong = part.get_elongation_from_group(res, group, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=100, model_id=m.id)
		    elong = part.get_elongation_from_line(res, node1, res, node2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line_coords
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [-1.25, -2.32, 2]
		    point2 = [-1.35, -0.9, 3.5]
		    elong = part.get_elongation_from_line_coords(res, point1, point2)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_node
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node = nodes.Node(id=100, model_id=m.id)
		    elong = part.get_elongation_from_node(res, node, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    part2 = parts.Part(id=3, type=constants.PSOLID, model_id=m.id)
		    elong = part.get_elongation_from_part(res, part2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(id=1, model_id=m.id)
		    node2 = nodes.Node(id=100, model_id=m.id)
		    node3 = nodes.Node(id=1000, model_id=m.id)
		    elong = part.get_elongation_from_plane(res, node1, res, node2, res, node3, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane_coords
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [-1.25, -2.32, 2]
		    point2 = [-1.35, -0.9, 3.5]
		    point3 = [0, 0, 0]
		    elong = part.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_layers
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    layers = part.get_layers()
		    # layers = part.get_layers(layer_name = 'name')
		    # layers = part.get_layers(serial_id = '1')
		    # layers = part.get_layers(layer_id = '1')
		    for lr in layers:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    mass = part.get_mass()
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_mass_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_no_nsm
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    mass = part.get_mass_no_nsm()
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_mass_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material_limit
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    lim = part.get_material_limit()
		    print(lim)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_materials
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "all"
		    mats = part.get_materials(specifier)
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    r = part.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import parts
		from meta import models
		from meta import constants
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		
		    part_nodal = part.get_nodal_scalar(resultset, specifier)
		    # part_nodal = part.get_nodal_scalar(resultset, specifier, layer = 'top')
		    for nodal in part_nodal:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "node"]
		
		    values, nodes = mat.get_nodal_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    part_nodal = part.get_nodal_vector(resultset, specifier)
		    # part_nodal = part.get_nodal_vector(resultset, specifier, layer = 'top')
		    for nodal in part_nodal:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    part = parts.Part(id=2, type=constants.PSHELL, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, magn, nodes = part.get_nodal_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "all"
		    # specifier = 'outer'
		    all_nodes = part.get_nodes(specifier)
		    for n in all_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    # specifier = 'visible_outer'
		    all_nodes = part.get_nodes(specifier, window=w)
		    for n in all_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    all_nodes = part.get_nodes(specifier, point_coordinates=point, distance_type="xyz")
		    # all_nodes = part.get_nodes(specifier, point_coordinates = point, distance_type = 'xyz', resultset = res)
		    for n in all_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_force
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_normal_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    specifier = "neighbour"
		    n_parts = part.get_parts(specifier)
		    for p in n_parts:
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
		# method: get_property
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    prop = part.get_property()
		    print(prop)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_force
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_shear_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    centroids = part.get_shell_normal(res)
		    for centroid in centroids:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_uniformity_index
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_vector_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_volume(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_integral
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_volume_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_volumetric_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_weighted_average
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_volume_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = part.hide()
		    print(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = part.identify()
		    print(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: preview_composite_report
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    res = part.preview_composite_report()
		    print(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    res = part.set_attribute(attribute_name, attribute_type, attribute_value)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    # res =  part.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(res)
		    attr = part.get_attributes(attribute_name="attr")
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = part.set_attribute("attr", "string", "test")
		    print(ret)
		    attr = part.get_attributes()
		    attribute_name = "attr"
		    # attr = part.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    color = windows.Color(name="my_color", r=0, g=255, b=255, a=255)
		    ret = part.set_color(color, w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_material_limit
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    material_limit = 12.1
		    ret = part.set_material_limit(material_limit)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    name = "part_name"
		    ret = part.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rendering_material
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    window = windows.Window(name="MetaPost", page_id=0)
		    rendering_material_namestring = "Default Materials/Bronze"
		    ret = part.set_rendering_material(rendering_material_namestring, window)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = part.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    p = parts.Part(id=2, type=constants.PSHELL, model_id=0)
		    can_use = p.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_normal_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=m.id)
		    res = m.get_current_resultset()
		    val = part.get_shear_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the part.

	"""

	model_id: int = None
	"""
	Model id of the part.

	"""

	type: int = None
	"""
	Type of the part (mETA constant).

	"""

	subtype: int = None
	"""
	Subtype of the part.

	"""

	visible: int = None
	"""
	- 1 if part is visible on the active or first enabled window of the active page
	- 0 if part is not visible

	"""

	name: str = None
	"""
	Name of the part.

	"""

	mat_id: int = None
	"""
	The id of the corresponding to the part material.

	"""

	shell_thick: float = None
	"""
	Shell thickness for PSHELL, or -1 for rest types of parts.

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the part.


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the part. Upon failure, it returns None.

		"""


	def get_elements(self, specifier: str, type: int, point_coordinates: object, resultset: object, window: object, range: str) -> object:

		"""

		This method gets the elements of the part.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all elements of the part (default value). Optionally combined with argument: type.
			- 'outer' : all outer elements of part. Outer element is the one whose at least one node belongs to an element of a different part from the given. Optionally combined with argument: type.
			- 'nearest' : nearest element of the part from a specific point. Must be combined with argument: point_coordinates. Optionally combined with argument: resultset.
			- 'neighbour' : all neighbour elements to the part. Neighbour elements are these which are directly attached to the specified part or defined in the geometry file. Optionally combined with argument: type.
			- 'visible' : visible elements of the part. Optionally combined with argument: window.
			- 'range' : Provide a range of Element Ids in the argument range.

		type : int, optional
			The type of the element that the method will return. If absent, elements of all types will returned. Used when the specifier is 'all', 'outer', 'neighbour', 'visible'.

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE. Used only when the specifier is 'nearest'.

		window : object, optional
			An object of class Window. Used when the specifier is 'visible'. If this argument is set, the method will return only the visible elements in this window.

		range : str, optional
			Element Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Element.Upon failure, it returns an empty list.

		"""


	def get_nodes(self, specifier: str, window: object, point_coordinates: object, resultset: object, distance_type: str, range: str) -> object:

		"""

		This method gets the nodes of the part.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodes of the part (default value).
			- 'visible' : visible nodes of the part. Optionally combined with argument: window.
			- 'outer' : outer nodes of the part. Outer node is the one who belongs to an element which does not belong to the given part.
			- 'visible_outer' : visible outer nodes of the part. Optionally combined with argument: window.
			- 'nearest' : nearest node of the part from a specific point. Must be combined with arguments: point_coordinates, distance_type. Optionally combined with argument: resultset.
			- 'range' : Provide a range of Node Ids in the argument range.

		window : object, optional
			An object of class window. This argument is used when specifier is 'visible' or 'visible_outer'. If the specifier has a different value, this argument is ignored. If this argument is set, the method will return only the visible nodes in this window.

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. It is used, if set, when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		distance_type : str, optional
			Type of the distance. It is required when the specifier is 'nearest'. Possible values are:
			- 'xyz': XYZ distance
			- 'xy': XY distance
			- 'yz': YZ distance
			- 'zx': ZX distance
			- 'x': X distance
			- 'y': Y distance
			- 'z': Z distance

		range : str, optional
			Node Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node.Upon failure, it returns an empty list.

		"""


	def get_materials(self, specifier: str) -> object:

		"""

		This method gets the materials of the part.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all materials of part (default value).

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Material.Upon failure it returns an empty list

		"""


	def get_parts(self, specifier: str) -> object:

		"""

		This method gets the parts, that are specified from the first argument.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'neighbour' : get the neighbour parts of the part

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Part.Upon failure, an empty list is returned.

		"""


	def get_layers(self, layer_name: str, serial_id: int, layer_id: int) -> object:

		"""

		This method gets the layers of the part. Provide one or no arguments. If no argument is provided, all layers of the part will be returned.


		Parameters
		----------
		layer_name : str, optional
			Name of the layer. Get the layers which have name that matches layer_name.

		serial_id : int, optional
			Serial number of the layer. Get the layer that has serial number same as serial_id.

		layer_id : int, optional
			Id of the layer. Get the layer that has id same as layer_id.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Layer referring to one specific layer of the part.Upon failure, an empty list is returned.

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of the part.


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the part. Upon failure, it returns None.

		"""


	def get_abd_matrix(self) -> object:

		"""

		This method gets the ABD matrix of the part.


		Returns
		-------
		object
			Upon success, it returns a 6X6 matrix in the form of a list containing other lists.Upon failure, it returns an empty list.

		"""


	def get_abcd_matrix_thickness(self) -> object:

		"""

		This method gets the A,B,C,D matrices through thickness for a stack of the part.


		Returns
		-------
		object
			Upon success, it returns a 12X3 matrix in the form of a list containing other lists.The first 3 lists is the A matrix.The next 3 lists is the B matrix.The next 3 lists is the C matrix.The last 3 lists is the D matrix.Upon failure, it returns an empty list.

		"""


	def get_mass(self) -> float:

		"""

		This method gets the mass of the part.


		Returns
		-------
		float
			Upon success, it returns the mass of the part.Upon failure, it returns None.

		"""


	def get_mass_no_nsm(self) -> float:

		"""

		This method gets the mass of the part, excluding NSM.


		Returns
		-------
		float
			Upon success, it returns a the mass of the part.Upon failure, it returns None.

		"""


	def get_deck_type(self) -> str:

		"""

		This method gets the type of the part.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the type for the deck of the part.Upon failure, None is returned.

		"""


	def get_deck_subtype(self) -> str:

		"""

		This method gets the subtype of the part.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the subtype for the deck of the part.Upon failure, None is returned.

		"""


	def get_property(self) -> str:

		"""

		This method gets the properties of the part, as string.


		Returns
		-------
		str
			Upon success, it returns a string referring to the properties of the specified part as they are specified in geometry file.Upon failure, it returns None.

		"""


	def get_color(self, window: object) -> object:

		"""

		This method gets the color of the part.


		Parameters
		----------
		window : object
			An object of class Window

		Returns
		-------
		object
			Upon success, it returns an object of class Color.Upon failure, it returns None.

		"""


	def get_rendering_materials(self) -> str:

		"""

		This method gets the rendering materials of the part, as string.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the rendering material of the corresponding part of the  given model for the specified window. Upon failure, it returns None

		"""


	def get_coordinates(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the maximum or the minimum coordinates in each direction (X, Y, Z) of the part.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'min' : min coordinates
			- 'max' : max coordinates

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			It returns a list with 3 objects of class Node that correspond to the nodes with the maximum coordinates in each direction of the part.- Index 0 contains the Node with the maximum X coordinate- Index 1 contains the Node with the maximum Y coordinate- Index 2 contains the Node with the maximum Z coordinate. Upon failure, an empty list is returned.

		"""


	def get_deformations(self, resultset: object, specifier: str, numpy: object) -> object:

		"""

		This method gets the deformations of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations (default value)
			- 'max' : max deformation
			- 'min' : min deformation

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
			Upon success, it returns a list with objects of class Deformation. Upon failure, it returns an empty list.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal scalar values of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar (default value)
			- 'max' : max nodal scalar
			- 'min' : min nodal scalar

		layer : str, optional
			Location of the nodal scalar values. Possible values are:
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
			Upon success, it returns a list with objects of class NodalScalar. Upon failure, it returns an empty list.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal vector of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector (default value)
			- 'max' : max nodal vector
			- 'min' : min nodal vector

		layer : str, optional
			Location of the nodal vector values. Possible values are:
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
			Upon success, it returns a list with objects of class NodalVector. Upon failure, it returns an empty list.

		"""


	def get_centroid_scalar(self, resultset: object, specifier: str, layer: str, non_zero: bool, exclude_novalue: bool, numpy: object) -> object:

		"""

		This method gets the centroid scalar of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid scalar (default value)
			- 'max' : max centroid scalar
			- 'min' : min centroid scalar

		layer : str, optional
			Location of the centroid scalar values. Possible values are:
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
			Upon success, it returns a list with objects of class CentroidScalar. Upon failure, it returns an empty list.

		"""


	def get_centroid_vector(self, resultset: object, specifier: str, layer: str, principal: str, numpy: object) -> object:

		"""

		This method gets the centroid vector values of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid vector (default value)
			- 'max' : max centroid vector
			- 'min' : min centroid vector

		layer : str, optional
			Location of the centroid vector values. Possible values are:
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
			Upon success, it returns a list with objects of class CentroidVector. Upon failure, it returns an empty list.

		"""


	def get_corner_scalar(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the corner scalar values of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar (default value)
			- 'max' : max corner scalar
			- 'min' : min corner scalar

		layer : str, optional
			Location of the corner scalar values. Possible values are:
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
			Upon success, it returns a list with objects of class CornerScalar. Upon failure, it returns an empty list.

		"""


	def get_corner_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the corner vector values of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector (default value)
			- 'max' : max corner vector
			- 'min' : min corner vector

		layer : str, optional
			Location of the corner vector values. Possible values are:
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
			Upon success, it returns a list with objects of class CornerVector. Upon failure, it returns an empty list.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vector of the part of type PSHELL.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns an object of class CentroidVector referring to the shell normal vector of the part. Upon failure, None is returned.

		"""


	def get_cog_coordinates(self, resultset: object) -> object:

		"""

		This method gets the coordinates of the geometrical center of gravity of  the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		Returns
		-------
		object
			Upon success, it returns a list containing the coordinates of the geometrical center of gravity of the specified part. Upon failure, an empty list is returned.

		"""


	def get_area(self, resultset: object) -> float:

		"""

		This method gets the area integral of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area integral of the part. Upon failure, it returns None.

		"""


	def get_volume(self, resultset: object) -> float:

		"""

		This method gets the volume of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volume of the part. Upon failure, it returns None.

		"""


	def get_area_integral(self, resultset: object) -> float:

		"""

		This method gets the area integral of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area integral of the part. Upon failure, it returns None.

		"""


	def get_volume_integral(self, resultset: object) -> float:

		"""

		This method gets the volume integral of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volume integral of the part. Upon failure, it returns None.

		"""


	def get_volume_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the volume weighted average of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volume weigthed average. Upon failure, it returns None.

		"""


	def get_area_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the area weighted average of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area weighted average. Upon failure, it returns None.

		"""


	def get_volumetric_flow(self, resultset: object) -> float:

		"""

		This method gets the volumetric flow of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volumetric flow of the part. Upon failure, it returns None.

		"""


	def get_mass_flow(self, resultset: object) -> float:

		"""

		This method gets the mass flow rate of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the mass flow rate of the part. Upon failure, it returns None.

		"""


	def get_mass_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the mass weighted average of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value as the result of the calculated mass weighted average of the part. Upon failure, None will be returned.

		"""


	def get_normal_force(self, resultset: object) -> object:

		"""

		This method gets the normal force of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude. Upon failure, an empty list is returned.

		"""


	def get_shear_force(self, resultset: object) -> object:

		"""

		This method gets the shear force of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""


	def get_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the uniformity index of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated uniformity index of the element. Upon failure, None will be returned.

		"""


	def get_vector_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the vector uniformity index.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value as the result of the calculated vector uniformity index of the part. Upon failure, None will be returned.

		"""


	def get_material_limit(self, material_limit_type: str) -> float:

		"""

		This method gets the material limit of the part.


		Parameters
		----------
		material_limit_type : str, optional
			Type of the material limit which will be calculated. Its possible values are:
			- 'tension': Part material limit in tension
			- 'compression': Part material limit in compression
			- 'shear': Part material limit in shear.

		Returns
		-------
		float
			It returns a float value referring to the material limit of the part. Upon failure, None is returned.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the part.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes.Upon failure, it returns an empty dictionary.

		"""


	def get_distance_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node : object
			An object of class Node.

		node_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node : object
			An object of class Node.

		node_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given element.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		element : object

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		part : object
			An object of class Part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		part : object
			An object of class Part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		group : object
			An object of class Group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given group.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		group : object
			An object of class Group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given group.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given boundary element.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		boundary : object
			An object of class Boundary.

		boundary_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node2.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node2.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the distance of the part from a given line.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_line_coords(self, point1: object, point2: object) -> object:

		"""

		This method gets the elongation of the part from a given line.


		Parameters
		----------
		point1 : object
			List with the coordinates of the first point of the line.

		point2 : object
			List with the coordinates of the second point of the line.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the distance of the part from a given cutplane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		plane : object
			An object of class Plane.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the elongation of the part from a given cutplane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		plane : object
			An object of class Plane.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the distance of the part from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node2.

		node3 : object
			An object of class Node.

		node3_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node3.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node2.

		node3 : object
			An object of class Node.

		node3_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given node3.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the distance of the part from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		point1 : object
			List with the coordinates of the first point of the line.

		point2 : object
			List with the coordinates of the second point of the line.

		point3 : object
			List with the coordinates of the third point of the line.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane_coords(self, resultset: object) -> object:

		"""

		This method gets the elongation of the part from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def set_color(self, color: object, window: object) -> bool:

		"""

		This method sets the color of the part.


		Parameters
		----------
		color : object
			The color of the part.

		window : object
			The window in which the part color will be set.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the part.


		Parameters
		----------
		name : str
			Name of the part.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the part.


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


	def set_rendering_material(self, rendering_material_name: str, window: object) -> bool:

		"""

		This method sets the rendering material of the part. This method works for the active page.


		Parameters
		----------
		rendering_material_name : str
			Name of rendering material.

		window : object
			An object of class Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_material_limit(self, material_limit: float) -> bool:

		"""

		This method sets material limit on the part.


		Parameters
		----------
		material_limit : float
			Material limit of the part.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the part. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the part. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the part. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def preview_composite_report(self) -> bool:

		"""

		This method shows a preview of the produced html report for composite parts.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failuer, it returns False.

		"""


	def create_section(self) -> object:

		"""

		This method creates a section from the part. This method works for the active page.


		Returns
		-------
		object
			Upon success, it returns an object of class Section. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Part entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_normal_moment(self, resultset: object) -> object:

		"""

		This method gets the normal moment of the part.


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

		This method gets the shear moment of the part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""

class Layer():

	"""

	Class for part layers.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    if lr:
		        print(lr.serial, lr.id, lr.part_id, lr.part_type, lr.model_id)
		        print(lr.material_id, lr.name, lr.thickness, lr.theta, lr.ips)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    color = lr.get_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    m = lr.get_material()
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    r = lr.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_part
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    p = lr.get_part()
		    if p:
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
		# method: is_usable
		# PYTHON script
		import meta
		from meta import parts
		from meta import constants
		
		
		def main():
		    lr = parts.Layer(id=1, part_id=57, part_type=constants.PSHELL, model_id=0)
		    can_use = lr.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	serial: int = None
	"""
	Serial number of the layer.

	"""

	id: int = None
	"""
	Id of the layer.

	"""

	part_id: int = None
	"""
	Id of the part of the layer.

	"""

	part_type: int = None
	"""
	Type of the part of the layer.

	"""

	model_id: int = None
	"""
	Model id of the layer.

	"""

	material_id: int = None
	"""
	Id of the material of the layer.

	"""

	name: str = None
	"""
	Name of the layer.

	"""

	thickness: float = None
	"""
	Thickness.

	"""

	theta: float = None
	"""
	Theta.

	"""

	ips: int = None
	"""
	Number of layer integration points.

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the part layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the part layer.  Upon failure, it returns None.

		"""


	def get_part(self) -> object:

		"""

		This method gets the part of the part layer.  


		Returns
		-------
		object
			Upon success, it returns an object of type Part referring to the part of the part layer.  Upon failure, it returns None.

		"""


	def get_material(self) -> object:

		"""

		This method gets the material of the part layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Material referring to the material of the part layer.  Upon failure, it returns None.

		"""


	def get_color(self) -> object:

		"""

		This method gets the color of the part layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the color of the part layer. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Model entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

