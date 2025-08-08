from __future__ import annotations
from typing import *

def AddNameOnElement(element_id: int, element_name: str, element_type: int, second_id: int, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_name` instead.


	This function defines a name for an element of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_name : str
		Name of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

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
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    element_name = "Named shell"
		    elements.AddNameOnElement(
		        model_id, element_type, element_id, second_id, element_name
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_name instead.", DeprecationWarning)

def AddNameOnSomeElements(element_ids: object, element_names: object, element_types: object, second_ids: object, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_name_on_elements` instead.


	This function defines names for some specific elements of a given model.

	Parameters
	----------
	element_ids : object
		List containing ids of the elements as integers.

	element_names : object
		List containing names of the elements as strings.

	element_types : object
		List containing types of the elements (META constant) as integers.

	second_ids : object
		List containing second ids of the elements as integers.

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
		from meta import elements
		
		
		def main():
		    model_id = 0
		
		    visible_elements = elements.VisibleElements(model_id)
		
		    element_types = list()
		    element_ids = list()
		    second_ids = list()
		    element_names = list()
		
		    for e in visible_elements:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		        element_names.append("VISIBLE ELEMENT")
		    elements.AddNameOnSomeElements(
		        model_id, element_types, element_ids, second_ids, element_names
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_name_on_elements instead.", DeprecationWarning)

def AdvFiltersOnElements(model_id: int, adv_filters: object, result: object, sort: bool) -> object:

	"""

	This function allows the user to collect elements of a model specified by the given id through some advanced filters.

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
		It returns a list where each member of the list is an object of class Element referring to one specific element of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Elements:visible::Keep All")
		    adv_filters.append(
		        "intersect:Elements:centroid.func.scalar.max:>200:Each Part Max 1"
		    )
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    collected_elements = elements.AdvFiltersOnElements(model_id, adv_filters, result)
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AreaOfElement(element_id: int, element_type: int, second_id: int, result: object) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_area` instead.


	This function calculates the area of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information or is absent, then area will be calculated for the ORIGINAL STATE.

	Returns
	-------
	float
		It returns a float value referring to the area of the specified element.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.AreaOfElement(result, element_type, element_id, second_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_area instead.", DeprecationWarning)

def CentroidScalarOfElement(result: object, element_type: int, element_id: int, second_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_centroid_scalar` instead.


	This function calculates centroid scalar value of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element.

	layer : str
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns an object of type class CentroidScalar referring to the centroid scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.CentroidScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    centroid = elements.CentroidScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    if centroid:
		        print(centroid.value)  # Centroid scalar value of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfElement(result: object, element_type: int, element_id: int, second_id: int, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_centroid_vector` instead.


	This function calculates centroid vector value of an element with a specific id and type of a given model.

	Parameters
	----------
	result : object
		object of class type Resultset

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element

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
		It returns an object of class type CentroidVector referring to the centroid vector value of the of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.CentroidVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    centroid = elements.CentroidVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		
		    if centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_centroid_vector instead.", DeprecationWarning)

def CollectNewElementsEnd() -> object:

	"""

	This function ends recording the creation of new elements. This function should be preceded by a corresponding call to script function CollectNewElementsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific newly created element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import utils
		
		
		def main():
		    elements.CollectNewElementsStart()
		
		    # Create new elements
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.ReportNewElements()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.CollectNewElementsEnd()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewElementsStart() -> int:

	"""

	This function starts recording the creation of new elements. This function should be followed by a corresponding call to script function CollectNewElementsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import utils
		
		
		def main():
		    elements.CollectNewElementsStart()
		
		    # Create new elements
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.ReportNewElements()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.CollectNewElementsEnd()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CommentsOfElement(element_id: int, element_type: int, second_id: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_comments` instead.


	This function finds the comments of an element with a specific id and type of a given model. Comments refer to various information which are output in the solver's input file and can be available in post-processing.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the comments of the element.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

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
		    element_comments = elements.CommentsOfElement(
		        model_id, element_type, element_id, second_id
		    )
		    print(element_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_comments instead.", DeprecationWarning)

def CornerScalarOfElement(element_id: int, layer: str, second_id: int, result: object, element_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_scalar` instead.


	This function calculates all corner scalar values of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	layer : str
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    layer = (
		        "bottom"  # BOTTOM corner scalar values if both bottom and top values are loaded
		    )
		    elem_corner = elements.CornerScalarOfElement(
		        result, element_type, element_id, second_id, layer
		    )
		    for corn in elem_corner:
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner with this corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_scalar instead.", DeprecationWarning)

def DampingOfDampElement(element_id: int, element_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_damping` instead.


	This function calculates the damping of a damp element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element

	element_type : int
		Type of the element (META constant). Element type must be DAMP1 or DAMP2.

	model_id : int
		Id of the model.

	Returns
	-------
	float
		It returns a float value referring to the damping of the specified damp element.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.DAMP2
		    element_id = 1345
		
		    damping = elements.DampingOfDampElement(model_id, element_type, element_id)
		    print(damping)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_damping instead.", DeprecationWarning)

def DeckSubtypeOfElement(element_subtype: int, element_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_deck_subtype` instead.


	This function converts a given META element subtype to the corresponding subtype of a deck of a specified model.

	Parameters
	----------
	element_subtype : int
		Subtype of the element.

	element_type : int
		Type of the element (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string with the name of the element subtype for the deck of the specified model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.TRIA3
		    element_subtype = 2
		
		    deck_subtype = elements.DeckSubtypeOfElement(
		        model_id, element_type, element_subtype
		    )
		    print(deck_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_deck_subtype instead.", DeprecationWarning)

def DeckTypeOfElement(element_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_deck_type` instead.


	This function converts a given META element type to the corresponding type of the deck of a specified model.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string with the name of the type, for the deck of a specified model, of the corresponding to the given META element type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.TETRA
		    deck_type = elements.DeckTypeOfElement(model_id, element_type)
		    print(deck_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_deck_type instead.", DeprecationWarning)

def DeformationsOfElement(element_id: int, element_type: int, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class type Deformation referring to the deformation of a node for the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    elem_deforms = elements.DeformationsOfElement(
		        result, element_type, element_id, second_id
		    )
		    for deform in elem_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_deformations instead.", DeprecationWarning)

def DistanceElementToElement(model_id_1: int, result_1: object, element_type_1: int, element_id_1: int, second_id_1: int, model_id_2: int, result_2: object, element_type_2: int, element_id_2: int, second_id_2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_element` instead.


	This function calculates the distance or the elongation of an element from another element.

	Parameters
	----------
	model_id_1 : int
		Id of the model of the 1st element.

	result_1 : object
		An object of class Result that refers to a Resultset of the model of the 1st element.

	element_type_1 : int
		Type of the 1st element (META constant).

	element_id_1 : int
		Id of the 1st element.

	second_id_1 : int
		Second id of the 1st element.

	model_id_2 : int
		Id of the model of the 2nd element

	result_2 : object
		An object of class Result that refers to a Resultset of the model of the 2nd element.

	element_type_2 : int
		Type of the 2nd element (META constant).

	element_id_2 : int
		Id of the 2nd element.

	second_id_2 : int
		Second id of the 2nd element.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list of float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id_1 = 0
		    all_resultsets = results.Resultsets(model_id_1)
		    result_1 = all_resultsets[1]
		    element_type_1 = constants.SHELL
		    element_id_1 = 1
		    second_id_1 = -1
		
		    model_id_2 = 0
		    all_resultsets = results.Resultsets(model_id_2)
		    result_2 = all_resultsets[1]
		    element_type_2 = constants.SHELL
		    element_id_2 = 10
		    second_id_2 = -1
		
		    distance = elements.DistanceElementToElement(
		        model_id_1,
		        result_1,
		        element_type_1,
		        element_id_1,
		        second_id_1,
		        model_id_2,
		        result_2,
		        element_type_2,
		        element_id_2,
		        second_id_2,
		    )
		    # distance = elements.DistanceElementToElement(model_id_1, result_1, element_type_1, element_id_1, second_id_1, model_id_2, result_2, element_type_2, element_id_2, second_id_2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_element instead.", DeprecationWarning)

def DistanceElementToGroup(element_model: int, element_result: object, element_type: int, element_id: int, second_id: int, group_model: int, group_result, group_name: str, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_group` instead.


	This function calculates the distance or the elongation of an element from a group of a model.

	Parameters
	----------
	element_model : int
		Id of the model of the element.

	element_result : object
		An object of class Result that refers to a Resultset of the model for the element.

	element_type : int
		Type of the element (META constant)

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element.

	group_model : int
		Id of the model of the group.

	group_result : 
		An object of class Result that refers to a Resultset of the model for the group.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, default value is 1.

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

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 229584
		    second_id = -1
		
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    distance = elements.DistanceElementToGroup(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		        group_model,
		        group_result,
		        group_name,
		        group_instance,
		    )
		    # distance = elements.DistanceElementToGroup(element_model, element_result, element_type, element_id, second_id, group_model, group_result, group_name, group_instance, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_group instead.", DeprecationWarning)

def DistanceElementToLine(element_model: int, element_result: object, element_type: int, element_id: int, second_id: int, node1_model: int, node1_result: object, line_node1: int, node2_model: int, node2_result: object, line_node2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_line` instead.


	This function calculates the distance or the elongation of an element from a line.

	Parameters
	----------
	element_model : int
		Id of the model of the element.

	element_result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	node1_model : int
		Id of the model of the 1st node of the line.

	node1_result : object
		An object of class Result that refers to a Resultset of the model of the 1st node of the line

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
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    line_node1 = 100
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    line_node2 = 200
		
		    distance = elements.DistanceElementToLine(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		        node1_model,
		        node1_result,
		        line_node1,
		        node2_model,
		        node2_result,
		        line_node2,
		    )
		    # distance = elements.DistanceElementToLine(element_model, element_result,  element_type, element_id, second_id, node1_model, node1_result, line_node1, node2_model, node2_result, line_node2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_line instead.", DeprecationWarning)

def DistanceElementToLineCoords(model_id: int, result: object, element_type: int, element_id: int, second_id: int, point1: object, point2: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_line_coords` instead.


	This function calculates the distance or the elongation of an element from a line.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	point1 : object
		List with the coordinates of the 1st point of the line.

	point2 : object
		List with the coordinates of the 2nd point of the line.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    point1 = list()
		    point1.append(0.25)
		    point1.append(2.32)
		    point1.append(3.39)
		
		    point2 = list()
		    point2.append(1.35)
		    point2.append(-4.9)
		    point2.append(2.35)
		
		    distance = elements.DistanceElementToLineCoords(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		        point1,
		        point2,
		    )
		    # distance = elements.DistanceElementToLineCoords(element_model, element_result,  element_type, element_id, second_id, point1, point2, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_line_coords instead.", DeprecationWarning)

def DistanceElementToPart(element_model: int, element_result: object, element_type: int, element_id: int, second_id: int, part_model: int, part_result: object, part_type: int, part_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_part` instead.


	This function calculates the distance or the elongation of an element from a part.

	Parameters
	----------
	element_model : int
		Id of the model of the element.

	element_result : object
		An object of class Result that refers to a Resultset of the model of the element.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	part_model : int
		Id of the model of the part.

	part_result : object
		An object of class Result that refers to a Resultset of the model of the part.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    distance = elements.DistanceElementToPart(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		        part_model,
		        part_result,
		        part_type,
		        part_id,
		    )
		    # distance = elements.DistanceElementToPart( element_model, element_result,  element_type, element_id, second_id, part_model, part_result, part_type, part_id, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_part instead.", DeprecationWarning)

def DistanceElementToPlane(element_model: int, element_result: object, element_type: int, element_id: int, second_id: int, node1_model: int, node1_result: object, plane_node1: int, node2_model: int, node2_result: object, plane_node2: int, node3_model: int, node3_result: object, plane_node3: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_plane` instead.


	This function calculates the distance or the elongation of an element of a model from a plane.

	Parameters
	----------
	element_model : int
		Id of the model of the element.

	element_result : object
		An object of class Result that refers to a Resultset of the model of the element.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	node1_model : int
		Id of the model of the 1st node of the plane.

	node1_result : object
		An object of class Result that refers to a Resultset of the model of the 1st node of the plane.

	plane_node1 : int
		Id of the 1st node of the plane.

	node2_model : int
		Id of the model of the 2nd node of the plane.

	node2_result : object
		An object of class Result that refers to a Resultset of the model of the 2nd node of the plane

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
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    plane_node1 = 10
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    plane_node2 = 100
		
		    node3_model = 0
		    all_resultsets = results.Resultsets(node3_model)
		    node3_result = all_resultsets[1]
		    plane_node3 = 1000
		
		    distance = elements.DistanceElementToPlane(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
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
		    # distance = elements.DistanceElementToPlane(element_model, element_result,  element_type, element_id, second_id, node1_model, node1_result, plane_node1, node2_model, node2_result, plane_node2, node3_model, node3_result, plane_node3, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_plane instead.", DeprecationWarning)

def DistanceElementToPlaneCoords(model_id: int, result: object, element_type: int, element_id: int, second_id: int, point1: object, point2: object, point3: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_plane_coords` instead.


	This function calculates the distance or the elongation of an element from a plane.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

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
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 100687
		    second_id = -1
		
		    point1 = list()
		    point1.append(1.1)
		    point1.append(-1.21)
		    point1.append(2.3)
		
		    point2 = list()
		    point2.append(0)
		    point2.append(1.1)
		    point2.append(-2)
		
		    point3 = list()
		    point3.append(0.3)
		    point3.append(0.4)
		    point3.append(0.99)
		
		    distance = elements.DistanceElementToPlaneCoords(
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		        point1,
		        point2,
		        point3,
		    )
		    # distance = elements.DistanceElementToPlaneCoords(element_model, element_result,  element_type, element_id, second_id, point1, point2, point3, elongation = 1)
		    if distance:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_plane_coords instead.", DeprecationWarning)

def ElementById(element_id: int, element_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the element of a model with a given id and type.

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
		Upon success, it returns an object of class type Element referring to the element of the model with the given id.
		Else, None is returned.

	See Also
	--------
	elements.Element, constants

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
		
		    e = elements.ElementById(model_id, element_type, element_id)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def Elements(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all elements of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		
		    all_elements = elements.Elements(model_id)
		    print("Total number of elements: ", len(all_elements))
		    iter_end = min(10, len(all_elements))
		    for e in all_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsByComments(element_comments: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the elements of a model with specific comments.

	Parameters
	----------
	element_comments : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element with comments.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_comments = "SHELL*"
		    elements_with_coments = elements.ElementsByComments(model_id, element_comments)
		    for e in elements_with_coments:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsById(element_id: int, element_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds elements of a model with a given id and type.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int, optional
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    collected_elements = elements.ElementsById(
		        model_id, element_type, element_id, second_id
		    )
		
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsByIdAllTypes(element_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds elements of a model with a given id.

	Parameters
	----------
	element_id : int
		Id of the element.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_id = 1
		
		    collected_elements = elements.ElementsByIdAllTypes(model_id, element_id)
		
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsByName(element_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the elements of a model with a given name.

	Parameters
	----------
	element_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_name = "*SHELL*"
		
		    collected_elements = elements.ElementsByName(model_id, element_name)
		
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsByType(element_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all elements with a specific type of the model specified by the given id.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    collected_elements = elements.ElementsByType(model_id, element_type)
		    iter_end = min(10, len(collected_elements))
		    for e in collected_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect elements of a model specified by the given id through some advanced filters. The execution of the script will stop and a window will open to specify its advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    collected_elements = elements.ElementsFromAdvFilters(model_id, resultset)
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsListToDict(elems: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Element.

	Parameters
	----------
	elems : object
		List of objects of class Element.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the element and data the corresponding Element object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    type = constants.SHELL
		    all_elems = elements.ElementsByType(model_id, type)
		    few_elems = all_elems[0 : min(10, len(all_elems))]
		    dict_elems = elements.ElementsListToDict(few_elems)
		    for id, e in dict_elems.items():
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all elements of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the group.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    group_elements = elements.ElementsOfGroup(model_id, group_name, group_instance)
		    iter_end = min(10, len(group_elements))
		    for e in group_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def ElementsOfGroupByType(model_id: int, group_name: str, element_type: int, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all elements with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	element_type : int
		Type of the element (META constant).

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the group.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    element_type = constants.SHELL
		    group_elements = elements.ElementsOfGroupByType(
		        model_id, group_name, group_instance
		    )
		    iter_end = min(10, len(group_elements))
		    for e in group_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def ElementsOfMaterial(material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all elements with a given material for the specified model.

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
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    material_elements = elements.ElementsOfMaterial(
		        model_id, material_type, material_id
		    )
		    iter_end = min(10, len(material_elements))
		    for e in material_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def ElementsOfMaterialByType(element_type: int, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all elements with a specific type for a given material belonging to the specified model.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    element_type = constants.SHELL
		    material_elements = elements.ElementsOfMaterialByType(
		        model_id, element_type, material_type, material_id
		    )
		    iter_end = min(10, len(material_elements))
		    for e in material_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def ElementsOfNode(node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_elements` instead.


	This function collects all the elements that contain a given node for a specified model.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where wach member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    node_elements = elements.ElementsOfNode(model_id, node_id)
		    for e in node_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_elements instead.", DeprecationWarning)

def ElementsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_elements` instead.


	This function searches for the elements of an overlay run with a given type and id.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Overlay run type must be one of the string values:
		- 'session'
		- 'project'

	Returns
	-------
	int
		It returns a list where each member of the list is an object of class Element referring to one element of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    all_elements = elements.ElementsOfOverlayRun(overlay_run_type, overlay_run_id)
		    print("Total number of elements: ", len(all_elements))
		    iter_end = min(10, len(all_elements))
		    for e in all_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_elements instead.", DeprecationWarning)

def ElementsOfPart(part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all elements of a given part belonging to the specified model.

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
		It returns a list where each member is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    part_elements = elements.ElementsOfPart(model_id, part_type, part_id)
		    iter_end = min(10, len(part_elements))
		    for e in part_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def ElementsOfPartByType(element_type: int, part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all elements with a specific type for a given part of a specified model.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.QUAD4
		    part_type = constants.PSHELL
		    part_id = 1
		    part_elements = elements.ElementsOfPartByType(
		        model_id, element_type, part_type, part_id
		    )
		    iter_end = min(10, len(part_elements))
		    for e in part_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def ElementsTypes(model_id: int) -> object:

	"""

	This function collects all types of elements of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an integer referring to one type (META constant) of elements for the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_types = elements.ElementsTypes(model_id)
		    for element_type in all_types:
		        print(element_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsTypesOfMaterial(material: object) -> object:

	"""

	This function collects all types of elements with a given material belonging to the specified model.

	Parameters
	----------
	material : object
		An object of class Material.

	Returns
	-------
	object
		It returns a list where each element of the list is an integer referring to one type (META constant) of elements for the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import materials
		
		
		def main():
		    mat = materials.Material(id=2, model_id=0)
		    all_types = elements.ElementsTypesOfMaterial(mat)
		    for element_type in all_types:
		        print(element_type)
		    # or
		
		    all_types = elements.ElementsTypesOfMaterial(mat.model_id, mat.type, mat.id)
		    for element_type in all_types:
		        print(element_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsTypesOfPart(part: object) -> object:

	"""

	This function collects all types of elements of a given part belonging to the specified model.

	Parameters
	----------
	part : object
		An object of class Part.

	Returns
	-------
	object
		It returns a list where each element of the list is an integer referring to one type (META constant) of elements for the specified part.
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
		from meta import elements
		from meta import constants
		
		
		def main():
		    part = parts.Part(id=1, type=constants.PSHELL, model_id=0)
		    all_types = elements.ElementsTypesOfPart(part)
		    for element_type in all_types:
		        print(element_type)
		    # or
		
		    all_types = elements.ElementsTypesOfPart(part.model_id, part.type, part.id)
		    for element_type in all_types:
		        print(element_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the elements of a model for which comments exist.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.CommentsOfElement, elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		
		    elems_with_comments = elements.ElementsWithComments(model_id)
		    for e in elems_with_comments:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the elements of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.NameOfElement, elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    elems_with_name = elements.ElementsWithName(model_id)
		    iter_end = min(10, len(elems_with_name))
		    for e in elems_with_name[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def FailedElements(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all failed elements of a specific state of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    failed_elements = elements.FailedElements(result)
		    for e in failed_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def FailedElementsByType(element_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all failed elements with a specific type of an existing model.

	Parameters
	----------
	element_type : int
		Type of the element (META constants).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.ONROD
		    failed_elements = elements.FailedElementsByType(result, element_type)
		    for e in failed_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def HideElement(model_id: int, element_type: int, element_id: int, second_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.hide` instead.


	This function allows the user to hide an element of a specific model.

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
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	elements.HideSomeElements, constants

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
		    ret = elements.HideElement(model_id, element_type, element_id, second_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.hide instead.", DeprecationWarning)

def HideSomeElements(model_id: int, element_types: object, element_ids: object, second_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.hide_elements` instead.


	This function allows the user to hide some specific elements of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_types : object
		List with integers corresponding to the types of the elements (META constants).

	element_ids : object
		List with integers corresponding to the ids of the elements.

	second_ids : object
		List with integers corresponding to the second ids of the elements.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		
		    element_types = list()
		    element_ids = list()
		    second_ids = list()
		    all_elements = elements.Elements(model_id)
		    iter_end = int(len(all_elements) / 2)
		    for e in all_elements[0:iter_end]:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		    ret = elements.HideSomeElements(model_id, element_types, element_ids, second_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.hide_elements instead.", DeprecationWarning)

def IdentifiedElements(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all identified elements of the model specified by the given id.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect identified elements for all the enabled windows of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    identified_elements = elements.IdentifiedElements(model_id, window_name)
		    for e in identified_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def IdentifiedElementsByType(element_type: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all identified elements with a specific type of the model specified by the given id.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect identified elements for all the enabled windows of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific identified element of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Elements, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.QUAD4
		    window_name = "MetaPost"
		    identified_elements = elements.IdentifiedElementsByType(
		        model_id, element_type, window_name
		    )
		    for e in identified_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def IdentifyElement(model_id: int, element_type: int, element_id: int, second_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.identify` instead.


	This function allows the user to identify an element of a specified model.This function works for enabled windows of active page. If you want to identify a large number of elements you should better usefunction "".

	Parameters
	----------
	model_id : int
		Number - id of the model

	element_type : int
		Type of the element (META KEYWORD)

	element_id : int
		Id of the element

	second_id : int
		Second id of the element

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	elements.IdentifySomeElements, constants

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
		    element_id = 82
		    second_id = -1
		    ret = elements.IdentifyElement(model_id, element_type, element_id, second_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.identify instead.", DeprecationWarning)

def IdentifySomeElements(model_id: int, element_types: object, element_ids: object, second_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_elements` instead.


	This function allows the user to identify some specific elements of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_types : object
		List with integers corresponding to the types of the elements (META constants).

	element_ids : object
		List with integers corresponding to the ids of the elements.

	second_ids : object
		List with integers corresponding to the second ids of the elements.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_types = list()
		    element_ids = list()
		    second_ids = list()
		    all_elements = elements.Elements(model_id)
		    iter_end = min(10, len(all_elements))
		    for e in all_elements[0:iter_end]:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		    ret = elements.IdentifySomeElements(
		        model_id, element_types, element_ids, second_ids
		    )
		    print(ret)
		    # Note: In large models identifying many elements could be very slow
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_elements instead.", DeprecationWarning)

def IsElement(elem: object) -> int:

	"""

	This function checks whether an object is of class type Element.

	Parameters
	----------
	elem : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class type Elem, 0 otherwise.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    all_elems = elements.Elements(model_id)
		    all_entities = list()
		    all_entities.append(all_elems[0])
		    all_entities.append("A string")
		
		    for ent in all_entities:
		        if elements.IsElement(ent):
		            e = ent
		            print("This is an object of class type Elem")
		            print(
		                e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id
		            )
		        else:
		            print("This is NOT an object of class type Elem")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsShellElement(element_type: int) -> int:

	"""

	This function checks whether the given element type refers to a SHELL element.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	Returns
	-------
	int
		It returns 1 if element_type refers to a SHELL element, 0 otherwise.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    element_type = constants.TRIA6
		    if elements.IsShellElement(element_type):
		        print("This is a SHELL element")
		    else:
		        print("This is not a SHELL element")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsSolidElement(element_type: int) -> int:

	"""

	This function checks whether the given element type refers to a SOLID element.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	Returns
	-------
	int
		It returns 1 if element_type refers to a SOLID element, 0 otherwise.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    element_type = constants.PENTA
		    if elements.IsSolidElement(element_type):
		        print("This is a SOLID element")
		    else:
		        print("This is not a SOLID element")
		
		
		if __name__ == "__main__":
		    main()


	"""

def MassOfMassElement(model_id: int, element_type: int, element_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass` instead.


	This function calculates the mass of a mass element with specific id and type of a given model. 

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : int
		Type of the element (META constant). Element type must be MASS1 or MASS2.

	element_id : int
		Id of the element.

	Returns
	-------
	float
		It returns a float value referring to the mass of the specified mass element.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.MASS2
		    element_id = 349011
		    mass = elements.MassOfMassElement(model_id, element_type, element_id)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass instead.", DeprecationWarning)

def MaxCoordinatesOfElement(element_id: str, element_type: str, result: object, second_id: str, model_id: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : str
		Id of the element.

	element_type : str
		Type of the element (META constant).

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	second_id : str
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : str
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 objects of class Node that correspond to the nodes with the maximum coordinates in each direction of the specified element.
		- Index 0 contains the Node with the maximum X coordinate
		- Index 1 contains the Node with the maximum Y coordinate
		- Index 2 contains the Node with the maximum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    nodes = elements.MaxCoordinatesOfElement(
		        model_id, element_type, element_id, second_id, result
		    )
		
		    if nodes:
		        max_x_node = nodes[
		            0
		        ]  # Object of class type Node for the node with the maximum X coordinate
		        print(max_x_node.x)  # X maximum coordinate
		        print(
		            max_x_node.y, max_x_node.z
		        )  # Coordinates in rest directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = nodes[
		            1
		        ]  # Object of class type Node for node with the maximum Y coordinate
		        print(max_y_node.y)  # Y maximum coordinate
		        print(
		            max_y_node.x, max_y_node.z
		        )  # Coordinates in rest directions of the node with the maximum Y coordinate
		        print(max_y_node.id)  # Id of the node with the maximum Y coordinate
		
		        max_z_node = nodes[
		            2
		        ]  # Object of class type Node for the node with the maximum Z coordinate
		        print(max_z_node.z)  # Z maximum coordinate
		        print(
		            max_z_node.x, max_z_node.y
		        )  # Coordinates in rest directions of the node with the maximum Z coordinate
		        print(max_z_node.id)  # Id of the node with the maximum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_coordinates instead.", DeprecationWarning)

def MaxCornerScalarOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_scalar` instead.


	This function calculates maximum corner scalar value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class CornerScalar referring to the maximum corner scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    max_corner = elements.MaxCornerScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    if max_corner:  # Object of  class CornerScalar with the maximum corner scalar value
		        print(max_corner.value)  # Maximum corner scalar value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element
		        print(
		            max_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_scalar instead.", DeprecationWarning)

def MaxDeformationOfElement(element_id: int, element_type: int, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects of the corresponding maximum deformations in each direction for the specified element.
		- Index 0 contains the deformation object for the node with maximum X deformation
		- Index 1 contains the deformation object for the node with maximum Y deformation
		- Index 2 contains the deformation object for the node with maximum Z deformationn
		- Index 3 contains the deformation object for the node with maximum TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    max_deform = elements.MaxDeformationOfElement(
		        result, element_type, element_id, second_id
		    )
		    if max_deform:
		        max_x_deform = max_deform[
		            0
		        ]  # The object of class Deformation for the node with max deformation in X direction
		        print(max_x_deform.x)  # X maximum deformation
		        print(
		            max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformations in rest directions
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[
		            1
		        ]  # The object of class Deformation for the node with max deformation in Y direction
		        print(max_y_deform.y)  # Y maximum deformation
		        print(
		            max_y_deform.x, max_y_deform.z, max_y_deform.total
		        )  # Deformations in rest directions
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[
		            2
		        ]  # The object of class Deformation for the node with max deformation in Z direction
		        print(max_z_deform.z)  # Z maximum deformation
		        print(
		            max_z_deform.x, max_z_deform.y, max_z_deform.total
		        )  # Deformations in rest directions
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z deformation
		
		        max_total_deform = max_deform[
		            3
		        ]  # Object of class Deformation for the node with maximum TOTAL deformation
		        print(max_total_deform.total)  # TOTAL maximum deformation
		        print(
		            max_total_deform.x, max_total_deform.y, max_total_deform.total
		        )  # Deformations in rest directions
		        print(
		            max_total_deform.node_id
		        )  # Id of the node with the maximum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_deformations instead.", DeprecationWarning)

def MaxNodalScalarOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_scalar` instead.


	This function calculates maximum nodal scalar value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class NodalScalar referring to the maximum nodal scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    max_nodal = elements.MaxNodalScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    if max_nodal:  # Object of  class NodalScalar with the maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(
		            max_nodal.part_id
		        )  # Id of the part of the node with the maximum nodal scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_scalar instead.", DeprecationWarning)

def MaxNodalVectorOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_vector` instead.


	This function calculates maximum nodal vector value of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class NodalVector referring to the maximum nodal vector value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    max_nodal = elements.MaxNodalVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		    if max_nodal:  # Object of  class NodalVector with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum vector scalar value
		        print(
		            max_nodal.part_id
		        )  # Id of the part of the node with the maximum nodal vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_vector instead.", DeprecationWarning)

def MetaSubtypeOfElement(model_id: int, element_type: int, element_subtype: str) -> object:

	"""

	This function converts a given element subtype of a deck of a given model to the corresponding META subtype.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : int
		Deck type of the element.

	element_subtype : str
		Deck subtype of the element.

	Returns
	-------
	object
		It returns an integer referring to the META subtype of the corresponding given element subtype of the specified model.
		Upon failure, it returns 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.TETRA
		    element_subtype = "C3D4E"
		    meta_subtype = elements.MetaSubtypeOfElement(
		        model_id, element_type, element_subtype
		    )
		    print(meta_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaTypeOfElement(model_id: int, element_type: str) -> object:

	"""

	This function converts a given element type of a deck of a specified model to the corresponding META type.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : str
		Deck type of the element.

	Returns
	-------
	object
		It returns an integer referring to the META type of the given element type of the specified model.
		Upon failure, a negative value is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_type = "S4R"  # Abaqus element
		    meta_type = elements.MetaTypeOfElement(model_id, element_type)
		    print(meta_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MinCoordinatesOfElement(element_id: str, element_type: str, result: object, second_id: str, model_id: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : str
		Id of the element.

	element_type : str
		Type of the element (META constant).

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	second_id : str
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : str
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 objects of class Node that correspond to the nodes with the minimum coordinates in each direction of the specified element.
		- Index 0 contains the Node with the maximum X coordinate
		- Index 1 contains the Node with the maximum Y coordinate
		- Index 2 contains the Node with the maximum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    nodes = elements.MinCoordinatesOfElement(
		        model_id, element_type, element_id, second_id, result
		    )
		
		    if nodes:
		        min_x_node = nodes[
		            0
		        ]  # Object of class type Node for the node with the minimum X coordinate
		        print(min_x_node.x)  # X minimum coordinate
		        print(
		            min_x_node.y, min_x_node.z
		        )  # Coordinates in rest directions of the node with the minimum X coordinate
		        print(min_x_node.id)  # Id of the node with the minimum X coordinate
		
		        min_y_node = nodes[
		            1
		        ]  # Object of class type Node for node with the minimum Y coordinate
		        print(min_y_node.y)  # Y minimum coordinate
		        print(
		            min_y_node.x, min_y_node.z
		        )  # Coordinates in rest directions of the node with the minimum Y coordinate
		        print(min_y_node.id)  # Id of the node with the minimum Y coordinate
		
		        min_z_node = nodes[
		            2
		        ]  # Object of class type Node for the node with the minimum Z coordinate
		        print(min_z_node.z)  # Z minimum coordinate
		        print(
		            min_z_node.x, min_z_node.y
		        )  # Coordinates in rest directions of the node with the minimum Z coordinate
		        print(min_z_node.id)  # Id of the node with the minimum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_coordinates instead.", DeprecationWarning)

def MinCornerScalarOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_scalar` instead.


	This function calculates minimum corner scalar value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constants).

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class CornerScalar referring to the minimum corner scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    min_corner = elements.MinCornerScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    if min_corner:  # Object of  class CornerScalar with the maximum corner scalar value
		        print(min_corner.value)  # Maximum corner scalar value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_scalar instead.", DeprecationWarning)

def MinDeformationOfElement(element_id: int, element_type: int, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL), of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects of the corresponding minimum deformations in each direction for the specified element.
		- Index 0 contains the deformation object for the node with minimum X deformation
		- Index 1 contains the deformation object for the node with minimum Y deformation
		- Index 2 contains the deformation object for the node with minimum Z deformationn
		- Index 3 contains the deformation object for the node with minimum TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    min_deform = elements.MinDeformationOfElement(
		        result, element_type, element_id, second_id
		    )
		    if min_deform:
		        min_x_deform = min_deform[
		            0
		        ]  # The object of class Deformation for the node with min deformation in X direction
		        print(min_x_deform.x)  # X minimum deformation
		        print(
		            min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformations in rest directions
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[
		            1
		        ]  # The object of class Deformation for the node with min deformation in Y direction
		        print(min_y_deform.y)  # Y minimum deformation
		        print(
		            min_y_deform.x, min_y_deform.z, min_y_deform.total
		        )  # Deformations in rest directions
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[
		            2
		        ]  # The object of class Deformation for the node with min deformation in Z direction
		        print(min_z_deform.z)  # Z minimum deformation
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.total
		        )  # Deformations in rest directions
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z deformation
		
		        min_total_deform = min_deform[
		            3
		        ]  # Object of class Deformation for the node with minimum TOTAL deformation
		        print(min_total_deform.total)  # TOTAL minimum deformation
		        print(
		            min_total_deform.x, min_total_deform.y, min_total_deform.total
		        )  # Deformations in rest directions
		        print(
		            min_total_deform.node_id
		        )  # Id of the node with the minimum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_deformations instead.", DeprecationWarning)

def MinNodalScalarOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_scalar` instead.


	This function calculates minimum nodal scalar value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class NodalScalar referring to the minimum nodal scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    min_nodal = elements.MinNodalScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    if min_nodal:  # Object of  class NodalScalar with the minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal scalar value
		        print(
		            min_nodal.part_id
		        )  # Id of the part of the node with the minimum nodal scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_scalar instead.", DeprecationWarning)

def MinNodalVectorOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_vector` instead.


	This function calculates minimum nodal vector value of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class NodalVector referring to the minimum nodal vector value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    min_nodal = elements.MinNodalVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		    if min_nodal:  # Object of  class NodalVector with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimum vector scalar value
		        print(
		            min_nodal.part_id
		        )  # Id of the part of the node with the minimum nodal vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_vector instead.", DeprecationWarning)

def NameOfElement(element_id: int, element_type: int, second_id: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_name` instead.


	This function finds the name of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the name of the element with the specified id and type of the given model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

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
		    element_name = elements.NameOfElement(model_id, element_type, element_id, second_id)
		    print(element_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_name instead.", DeprecationWarning)

def NeighbourElements(element_id: int, element_type: int, second_id: int, model_id: int, resultset: object, ignore_failed: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collect the neighbour elements of a given element of a specified model. Neighbour elements are these which are directly attached to the specified element or defined in the geometry file. 

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a resultset of the model to which the value is added.

	ignore_failed : int, optional
		Controls if the failed elements will be ignored, or not. Default value is zero (Do not ignore).

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    neighbour_elements = elements.NeighbourElements(
		        model_id, element_type, element_id, second_id
		    )
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def NeighbourElementsByType(element_id: int, element_type: int, neighbour_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collect the neighbour elements with a specific type of a given element of a specified model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	neighbour_type : int
		Type of the neighbour elements.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    neighbour_type = constants.SHELL
		    neighbour_elements = elements.NeighbourElementsByType(
		        model_id, element_type, element_id, second_id, neighbour_type
		    )
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def NeighbourElementsOfMaterial(material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all neighbour elements of a given material belonging to the specified model. Neighbour element is the one which is directly attached to the material through one or more nodes.

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
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    neighbour_elements = elements.NeighbourElementsOfMaterial(
		        model_id, material_type, material_id
		    )
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def NeighbourElementsOfMaterialByType(element_type: int, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all neighbour elements with a specific type of a given material belonging to the specified model. Neighbour element is the one which is directly attached to the material through one or more nodes.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    material_type = constants.MAT1
		    material_id = 1
		    neighbour_elements = elements.NeighbourElementsOfMaterialByType(
		        model_id, element_type, material_type, material_id
		    )
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def NeighbourElementsOfPart(part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all neighbour elements of a given part belonging to the specified model. Neighbour elements are these which are directly attached to the specified part or defined in the geometry file.

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
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    neighbour_elements = elements.NeighbourElementsOfPart(model_id, part_type, part_id)
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def NeighbourElementsOfPartByType(element_type: int, part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all neighbour elements with a specific type of a given part belonging to the specified model. Neighbour elements are these which are directly attached to the specified part or defined in the geometry file. 

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific neighbour element of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.RROD
		    part_type = constants.PSHELL
		    part_id = 1
		    neighbour_elements = elements.NeighbourElementsOfPartByType(
		        model_id, element_type, part_type, part_id
		    )
		    for e in neighbour_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def NodalScalarOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of an element with with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class NodalScalar referring to the nodal scalar value of a node of the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    elem_nodal = elements.NodalScalarOfElement(
		        result, element_type, element_id, second_id
		    )
		    for nodal in elem_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodal_vector` instead.


	This function calculates all nodal vector values of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constants).

	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class NodalVector referring to the nodal values of a node of the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    elem_nodal = elements.NodalVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		    for nodal in elem_nodal:
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodal_vector instead.", DeprecationWarning)

def NumOfElementsByType(model_id: int, element_type: int) -> int:

	"""

	This function finds the number of the elements of a model with a specific type.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : int
		Type of the element (META constant).

	Returns
	-------
	int
		It returns the number of the elements with the specific type for the given model.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.RBE2
		    num_of_elements = elements.NumOfElementsByType(model_id, element_type)
		    print(num_of_elements)
		
		
		if __name__ == "__main__":
		    main()


	"""

def OuterElementsOfMaterial(material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all outer elements of a given material belonging to the specified model. Outer element is the one whose at least one node belongs to an element of a different material from the given.

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
		It returns a list where each element of the list is an object of class Element referring to one specific outer element of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    outer_elements = elements.OuterElementsOfMaterial(
		        model_id, material_type, material_id
		    )
		    for e in outer_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def OuterElementsOfMaterialByType(element_type: int, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function collects all outer elements with a specific type of a given material belonging to the specified model. Outer element is the one whose at least one node belongs to an element of a different material from the given.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific outer element of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.QUAD4
		    material_type = constants.MAT1
		    material_id = 1
		    outer_elements = elements.OuterElementsOfMaterialByType(
		        model_id, element_type, material_type, material_id
		    )
		    for e in outer_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def OuterElementsOfPart(part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all outer elements of a given part belonging to the specified model. Outer element is the one whose at least one node belongs to an element of a different part from the given.

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
		It returns a list where each element of the list is an object of class Element referring to one specific outer element of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    outer_elements = elements.OuterElementsOfPart(model_id, part_type, part_id)
		    for e in outer_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def OuterElementsOfPartByType(element_type: int, part_id: int, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function collects all outer elements with a specific type of a given part belonging to the specified model. Outer element is the one whose at least one node belongs to an element of a different part from the given.

	Parameters
	----------
	element_type : int
		Type of the element (META constants.)

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific outer element of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    part_type = constants.PSHELL
		    part_id = 1
		    outer_elements = elements.OuterElementsOfPartByType(
		        model_id, element_type, part_type, part_id
		    )
		    for e in outer_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def PickElements(message: str, model_id: int, pick_settings: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_elements` instead.


	This function allows the user to pick elements of a model specified by the given id. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	message : str
		Message displayed to the user.

	model_id : int
		Id of the model. If it is equal to -1, then this function will work for all models.

	pick_settings : object, optional
		Argument 'pick_settings' is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. ['front_selection,1', 'polygonal_selection, 1']).
		The names of the pick settings and its possible values are:
		- 'front_selection': Disable/Enable front selection (0,1)
		- 'polygonal_selection': Disable/Enable polygonal selection (0,1)

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    message = "Select Elements and press Enter when you are ready"
		    picked_elements = elements.PickElements(model_id, message)
		    for e in picked_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_elements instead.", DeprecationWarning)

def ReportNewElements() -> object:

	"""

	This function collects the newly created elements from the last call of script function CollectNewElementsStart(). This function should be preceded by a corresponding call to script function CollectNewElementsStart() and should be followed by a corresponding call to script function CollectNewElementsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific newly created element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import utils
		
		
		def main():
		    elements.CollectNewElementsStart()
		
		    # Create new elements
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.ReportNewElements()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		    # Warning: importing large models will delay the execution of the script due to printing
		
		    new_elements = elements.CollectNewElementsEnd()
		    for e in new_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ShellNormalOfElement(element_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_shell_normal` instead.


	This function calculates the shell normal vector of an element of type SHELL with a specific id of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns an object of class CentroidVector referring to the shell normal vector of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_id = 1
		    shell_normal = elements.ShellNormalOfElement(result, element_id)
		    if shell_normal:  # Object of class CentroidVector
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_shell_normal instead.", DeprecationWarning)

def ShowElement(model_id: int, element_type: int, element_id: int, second_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.show` instead.


	This function allows the user to make visible an element of a model specified by its id.

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
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	elements.ShowSomeElements, constants

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
		    ret = elements.ShowElement(model_id, element_type, element_id, second_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.show instead.", DeprecationWarning)

def ShowSomeElements(model_id: int, element_types: object, element_ids: object, second_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.show_elements` instead.


	This function allows the user to make visible some specific elements of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_types : object
		List with integers corresponding to the types of the elements (META constants).

	element_ids : object
		List with integers corresponding to the ids of the elements.

	second_ids : object
		List with integers corresponding to the second ids of the elements.

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
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_types = list()
		    element_ids = list()
		    second_ids = list()
		    all_elements = elements.Elements(model_id)
		    for e in all_elements:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		    ret = elements.ShowSomeElements(model_id, element_types, element_ids, second_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.show_elements instead.", DeprecationWarning)

def StiffnessOfElasElement(element_id: int, element_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_stiffness` instead.


	This function calculates the stiffenss of an ELAS element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant). Element type must be ELAS1 or ELAS2.

	model_id : int
		Id of the model.

	Returns
	-------
	float
		It returns a float value referring to the stiffness of the specified ELAS element.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.ELAS2
		    element_id = 151
		
		    stiffness = elements.StiffnessOfElasElement(model_id, element_type, element_id)
		    print(stiffness)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_stiffness instead.", DeprecationWarning)

def StringElementType(element_type: int) -> int:

	"""

	This function converts a given META element type to its corresponding string representation.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	Returns
	-------
	int
		It returns a string with the name of the META element type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    element_type = 12
		    str_element_type = elements.StringElementType(element_type)
		    print(str_element_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateElement(elem: object) -> object:

	"""

	This function updates the data of the given element. Update is based in the field 'id', 'type', 'second_id' and 'model_id' of the given element object of class Element.

	Parameters
	----------
	elem : object
		Object of class Element.

	Returns
	-------
	object
		Upon success, it returns the new updated Element object.
		Else, None is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import utils
		
		
		def main():
		    model_id = 0
		    type = constants.SHELL
		    id = 1
		    e = elements.ElementById(model_id, type, id)
		    if e:
		        # commands which alter the data of the Element object
		        utils.MetaCommand("erase elem all")
		        e = elements.UpdateElement(e)
		        if e:  # update OK
		            print(
		                e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id
		            )
		        else:  # update FAILED
		            print("This is not a valid Elem object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleElements(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all visible elements of the model specified by the given id.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Elem referring to one specific visible element of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElements(model_id, window_name)
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def VisibleElementsByType(element_type: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function collects all visible elements with a specific type of the model specified by the given id. Element type must be one of META KEYWORDS. A full META KEYWORD list for elements can be found under library category "betameta_structs". Optional argument "window_name" refers to the name of the window of the model. If optional argument "window_name" is absent then this function will collect visible elements for the active or first enabled window of the model. This function works for the active page.

	Parameters
	----------
	element_type : int
		Type of the element (META constant).

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific visible element of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

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
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElementsByType(
		        model_id, element_type, window_name
		    )
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def VisibleElementsOfGroup(model_id: int, group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all visible elements of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific visible element of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElementsOfGroup(
		        model_id, group_name, window_name
		    )
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def VisibleElementsOfGroupByType(model_id: int, group_name: str, element_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all visible elements with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	element_type : int
		Type of the element (META constant).

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific visible element of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    element_type = constants.SHELL
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElementsOfGroupByType(
		        model_id, group_name, element_type, window_name
		    )
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def VisibleElementsOfGroupInstance(model_id: int, group_name: str, group_instance: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all visible elements of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class Element referring to one specific visible element of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElementsOfGroupInstance(
		        model_id, group_name, group_instance, window_name
		    )
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def VisibleElementsOfGroupInstanceByType(model_id: int, group_name: str, group_instance: int, element_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function collects all visible elements with a specific type of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	element_type : int
		Type of the element (META constant).

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list wwhere each element of the list is an object of class Element referring to one specific visible element of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    element_type = constants.SHELL
		    window_name = "MetaPost"
		    visible_elements = elements.VisibleElementsOfGroupInstanceByType(
		        model_id, group_name, group_instance, element_type, window_name
		    )
		    iter_end = min(10, len(visible_elements))
		    for e in visible_elements[0:iter_end]:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def VolumeOfElement(element_id: int, element_type: int, second_id: int, result: object) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_volume` instead.


	This function calculates the volume of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	float
		It returns a float value referring to the volume of the specified element.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SOLID
		    element_id = 1
		    second_id = -1
		    volume = elements.VolumeOfElement(result, element_type, element_id, second_id)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_volume instead.", DeprecationWarning)

def LayersOfElement(element_id: int, element_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_element_layers` instead.


	This function collects all layers of a given element belonging to the specified model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class ElementLayer referring to one specific layer of the given element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.ElementLayer, constants

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
		    element_id = 11939
		    second_id = -1
		
		    element_layers = elements.LayersOfElement(
		        model_id, element_type, element_id, second_id
		    )
		    for elr in element_layers:
		        print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		        print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		        print(elr.id, elr.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_element_layers instead.", DeprecationWarning)

def LayerOfElementBySerial(element_id: int, element_type: int, second_id: int, serial: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_element_layers` instead.


	This function finds the layer with a specific serial number of a given element belonging to the specified model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	serial : int
		Serial number of the layer.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an ElementLayer object with the given serial number.
		Else, None is returned.

	See Also
	--------
	elements.ElementLayer, constants

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
		    element_id = 11939
		    second_id = -1
		    serial = 1
		
		    ent = elements.LayerOfElementBySerial(
		        model_id, element_type, element_id, second_id, serial
		    )
		    if elements.IsElementLayer(ent):
		        elr = ent
		        print("This is an object of class ElementLayer")
		        print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		        print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_element_layers instead.", DeprecationWarning)

def IsElementLayer(element_layer: object) -> int:

	"""

	This function checks whether an object is of class ElementLayer.

	Parameters
	----------
	element_layer : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class ElementLayer, 0 otherwise.

	See Also
	--------
	elements.ElementLayer

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
		    element_id = 11939
		    second_id = -1
		    serial = 1
		
		    ent = elements.LayerOfElementBySerial(
		        model_id, element_type, element_id, second_id, serial
		    )
		    if elements.IsElementLayer(ent):
		        elr = ent
		        print("This is an object of class ElementLayer")
		        print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		        print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateElementLayer(element_layer: object) -> object:

	"""

	This function updates the data of the given ElementLayer object. Update is based in the fields 'serial', 'element_type', 'element_id', 'second_id' and 'model_id' of the given ElementLayer object. A description of class ElementLayer can be found as 'ElementLayer' under library category 'elements'.

	Parameters
	----------
	element_layer : object
		Object of class ElementLayer.

	Returns
	-------
	object
		Upon success, it returns the new updated ElementLayer object.
		Else, None is returned.

	See Also
	--------
	elements.ElementLayer, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import utils
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 11939
		    second_id = -1
		    serial = 1
		
		    elr = elements.LayerOfElementBySerial(
		        model_id, element_type, element_id, second_id, serial
		    )
		    if elr:
		        # commands which alter the attributes of the ElementLayer object
		
		        elr = elements.UpdateElementLayer(elr)
		
		        if elr:  # Update OK
		            print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		            print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		        else:  # Update Failed
		            print("This is not a valid ElementLayer object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def ColorOfElementLayer(element_id: int, element_type: int, second_id: int, serial: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.ElementLayer.get_color` instead.


	This function finds the color of a given layer of a specific element and model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	serial : int
		Sserial number of the layer.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class Color for the corresponding element layer.
		Else, None is returned.

	See Also
	--------
	elements.ElementLayer, constants

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
		    element_id = 11939
		    second_id = -1
		    serial = 1
		
		    layer_color = elements.ColorOfElementLayer(
		        model_id, element_type, element_id, second_id, serial
		    )
		    if layer_color:
		        print(layer_color.r)  # R value
		        print(layer_color.g)  # G value
		        print(layer_color.b)  # B value
		        print(layer_color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.ElementLayer.get_color instead.", DeprecationWarning)

def DistanceElementToCutPlane(element_id: int, element_result: object, element_type: int, plane_name: str, second_id: int, element_model: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_distance_from_cut_plane` instead.


	This function calculates the distance or the elongation of an element of a model from an existing cut plane.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_result : object
		An object of class Result that refers to a Resultset of the model of the element.

	element_type : int
		Type of element (META constant).

	plane_name : str
		Name of the plane.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	element_model : int
		Id of the model of the element.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    plane_name = "DEFAULT_PLANE_XY"
		
		    distance = elements.DistanceElementToCutPlane(
		        element_model, element_result, element_type, element_id, second_id, plane_name
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_distance_from_cut_plane instead.", DeprecationWarning)

def MassOfElement(element_id: int, element_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass` instead.


	This function calculates the mass (including NSM) of an element specified by its id, type, and the owner model id. For the case of elements with composite materials the mass poriton not attributed to NSM is calculated by averaging the density of each composite layer weighted by its relative thickness.

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
	float
		It returns a float value being the calculated mass of the specified element.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	elements.MassOfMassElement, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.QUAD4
		    element_id = 1
		    mass = elements.MassOfElement(model_id, element_type, element_id)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass instead.", DeprecationWarning)

def MassOfElementNoNsm(element_id: int, element_type: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass_no_nsm` instead.


	This function calculates the mass of an element excluding NSM. For the case of elements with composite materials mass is calculated by averaging the density of each composite layer weighted by its relative thickness.

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
	float
		It returns a float value being the calculated mass of the specified element.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    elem_type = constants.QUAD4
		    eid = 1
		    mass = elements.MassOfElementNoNsm(model_id, elem_type, eid)
		    print("mass = " + str(mass))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass_no_nsm instead.", DeprecationWarning)

def SolidSkinOfModel(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_element_faces` instead.


	This function collects the solid skin of all visible elements of the model specified by the given id. 
	

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the solid skin of all the elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of class ElementFace referring to one specific face of a visible element of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.ElementFace

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    all_faces = elements.SolidSkinOfModel(model_id, window_name)
		    few_faces = all_faces[0 : min(10, len(all_faces))]
		    for ef in few_faces:
		        print(ef.id, ef.model_id, ef.type, ef.total_nodes, ef.node_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_element_faces instead.", DeprecationWarning)

def ElementsBySolverId(model_id: int, element_type: int, element_path: str, element_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds elements of a model with hierarchical structure defined by type, id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	element_type : int
		Type of the element (META constant).

	element_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given element is limited.

	element_id : int
		Id of the element.

	second_id : int, optional
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	object
		This function returns a list with objects of class Element referring to the corresponding elements found.

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
		    element_path = "Truck->14"
		    element_id = 822
		    second_id = -1
		
		    collected_elements = elements.ElementsBySolverId(
		        model_id, element_type, element_path, element_id, second_id
		    )
		
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def ElementsBySolverIdAllTypes(model_id: int, element_path: str, element_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds elements of a model with hierarchical structure defined by id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given element is limited.

	element_id : int
		Id of the element.

	Returns
	-------
	object
		This function returns a list with objects of class Element referring to the corresponding elements found.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		
		
		def main():
		    model_id = 0
		    element_path = "Truck->14"
		    element_id = 822
		
		    collected_elements = elements.ElementsBySolverIdAllTypes(
		        model_id, element_path, element_id
		    )
		
		    for e in collected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def MaxCornerVectorOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_vector` instead.


	This function calculates maximum corner vector value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class CornerVEctor referring to the maximum corner scalar value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    max_corner = elements.MaxCornerVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		    if max_corner:  # Object of  class CornerVector with the maximum corner scalar value
		        print(max_corner.value)  # Maximum corner scalar value
		        print(max_corner.x)  # X component corner value
		        print(max_corner.y)  # Y component corner value
		        print(max_corner.z)  # Z component corner value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element
		        print(
		            max_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_vector instead.", DeprecationWarning)

def MinCornerVectorOfElement(element_id: int, element_type: int, layer: str, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_vector` instead.


	This function calculates minimum corner vector value of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constants).

	layer : str, optional
		Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns an object of class CornerVector referring to the minimum corner vector value of the specified element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    min_corner = elements.MinCornerVectorOfElement(
		        result, element_type, element_id, second_id
		    )
		    if min_corner:  # Object of  class CornerScalar with the maximum corner scalar value
		        print(min_corner.value)  # Maximum corner scalar value
		        print(min_corner.x)  # X component corner value
		        print(min_corner.y)  # Y component corner value
		        print(min_corner.z)  # Z component corner value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the maximum corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_vector instead.", DeprecationWarning)

def CornerVectorOfElement(element_id: int, layer: str, second_id: int, result: object, element_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_corner_vector` instead.


	This function calculates all corner vector values of an element with a specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	layer : str
		Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of the specified element.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    layer = (
		        "bottom"  # BOTTOM corner scalar values if both bottom and top values are loaded
		    )
		    elem_corner = elements.CornerVectorOfElement(
		        result, element_type, element_id, second_id, layer
		    )
		    for corn in elem_corner:
		        print(corn.value)  # Corner scalar value
		        print(corn.x)  # X component Corner value
		        print(corn.y)  # Y component Corner value
		        print(corn.z)  # Z component Corner value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner with this corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_corner_vector instead.", DeprecationWarning)

def AreaIntegralOfElement(element_id: int, element_type: int, second_id: int, result: object) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_area_integral` instead.


	This function calculates the integral of a resultset over the area of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model.

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
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 3101
		    second_id = -1
		    area_integral = elements.AreaIntegralOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(area_integral)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_area_integral instead.", DeprecationWarning)

def VolumeIntegralOfElement(element_id: int, element_type: int, second_id: int, result: object) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_volume_integral` instead.


	This function calculates the integral of a resultset over the volume of an element with specific id and type of a given model.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : int
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information or is absent, then area will be calculated for the ORIGINAL STATE.

	Returns
	-------
	float
		It returns a float value as the result of the calculated volume integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SOLID
		    element_id = 40226
		    second_id = -1
		
		    volume_integral = elements.VolumeIntegralOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(volume_integral)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_volume_integral instead.", DeprecationWarning)

def AreaWeightedAverageOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_area_weighted_average` instead.


	This function calculates the weighted area average of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information or is absent, then area will be calculated for the ORIGINAL STATE.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated weighted area average.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 3101
		    second_id = -1
		    area_integral = elements.AreaWeightedAverageOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(area_integral)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_area_weighted_average instead.", DeprecationWarning)

def VolumeWeightedAverageOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_volume_weighted_average` instead.


	This function calculates the weighted volume average of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated weighted area average.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SOLID
		    element_id = 40130
		    second_id = -1
		    volume_integral = elements.VolumeWeightedAverageOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(volume_integral)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_volume_weighted_average instead.", DeprecationWarning)

def VolumetricFlowOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information or is absent, then area will be calculated for the ORIGINAL STATE.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated volumetric flow rate of the element.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.VolumetricFlowOfElement(result, element_type, element_id, second_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass_flow` instead.


	This function calculates the mass flow rate of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		This function calculates the volumetric flow rate of an element with specific id and type of a given model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated mass flow rate of the element.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.MassFlowOfElement(result, element_type, element_id, second_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass_weighted_average` instead.


	This function calculates the mass weighted average of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		This function calculates the volumetric flow rate of an element with specific id and type of a given model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated mass weighted average of the element.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.MassWeightedAverageOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass_weighted_average instead.", DeprecationWarning)

def NormalForceOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_normal_force` instead.


	This function calculates the normal force of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

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
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.NormalForceOfElement(result, element_type, element_id, second_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_normal_force instead.", DeprecationWarning)

def ShearForceOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_shear_force` instead.


	This function calculates the shear force of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

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
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.ShearForceOfElement(result, element_type, element_id, second_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_shear_force instead.", DeprecationWarning)

def UniformityIndexOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_uniformity_index` instead.


	This function calculates the uniformity index of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated uniformity index of the element.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.UniformityIndexOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_uniformity_index instead.", DeprecationWarning)

def VectorUniformityIndexOfElement(result: object, element_type: int, element_id: int, second_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of an element with specific id and type of a given model.

	Parameters
	----------
	result : object
		This function calculates the volumetric flow rate of an element with specific id and type of a given model.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	float
		It returns a float value as the result of the calculated vector uniformity index of the element.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    area = elements.VectorUniformityIndexOfElement(
		        result, element_type, element_id, second_id
		    )
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_vector_uniformity_index instead.", DeprecationWarning)

def UniformityIndexOfPart(result: object, part_type: int, part_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_uniformity_index` instead.


	This function calculates the uniformity index of a part with specific id and type of a given model.

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
		It returns a float value as the result of the calculated uniformity index of the element.
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
		
		    index = parts.UniformityIndexOfPart(all_resultsets[1], part_type, pid)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_uniformity_index instead.", DeprecationWarning)

def SetAttributeOfElement(model_num: int, element_type: int, element_id: int, second_id: int, attrib_name: str, attrib_val: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given element. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_num : int
		The number of the model.

	element_type : int
		The type of the element.

	element_id : int
		The id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	attrib_name : str
		Name of the attribute.

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
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    id = 1
		    name = "test"
		    value = "test_val"
		    val = elements.SetAttributeOfElement(model_id, constants.SHELL, id, -1, name, value)
		    # or
		    name = "num_test"
		    value = 11.1
		    attribute_type = "numerical"
		    val = elements.SetAttributeOfElement(
		        model_id, constants.SHELL, id, -1, name, value, attribute_type
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_attribute instead.", DeprecationWarning)

def AttributeOfElement(model_num: int, element_type: int, element_id: int, second_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_num : int
		The number of the model

	element_type : int
		The type of the element

	element_id : int
		The id of the element

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    id = 1
		    name = "Type"
		    val = elements.AttributeOfElement(model_id, constants.SHELL, id, -1, name)
		    print("Value " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_attributes instead.", DeprecationWarning)

def AttributesOfElement(model_id: int, element_type: int, element_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_attributes` instead.


	This function collects all attributes of a given element

	Parameters
	----------
	model_id : int
		The number of the model

	element_type : int
		The type of the element

	element_id : int
		The id of the element

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    id = 1
		    all_attributes = elements.AttributesOfElement(model_id, constants.SHELL, id, -1)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_attributes instead.", DeprecationWarning)

def MassMatrixOfMassElement(model_id: int, element_type: int, element_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_mass_matrix` instead.


	This function returns the coordinate system id, the mass and he inertia of a mass element with specific id and type of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	element_type : int
		Type of the element (META constant). Element type must be ONM1 or ONM2.

	element_id : int
		Id of the element.

	Returns
	-------
	object
		Returns a list which contains:
		- position 0: The coordinate system id
		- position 1: A list of floats, corresponding to Mass (1st float) and Inertia (all the rest)
		Upon failure, an empty list is returned.

	See Also
	--------
	constants, MassOfMassElement

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.ONM2
		    element_id = 106
		    mass_matrix = elements.MassMatrixOfMassElement(model_id, element_type, element_id)
		    coordinate_system_id = mass_matrix[0]
		    mass = mass_matrix[1][0]
		    inertia = [
		        mass_matrix[1][1],
		        mass_matrix[1][2],
		        mass_matrix[1][3],
		        mass_matrix[1][4],
		        mass_matrix[1][5],
		        mass_matrix[1][6],
		    ]
		
		    print("Coordinate System Id: " + str(coordinate_system_id))
		    print("Mass: " + str(mass))
		    print(
		        "Inertia: I11="
		        + str(inertia[0])
		        + ",  I12="
		        + str(inertia[1])
		        + ",  I22="
		        + str(inertia[2])
		        + ",  I13="
		        + str(inertia[3])
		        + ",  I23="
		        + str(inertia[4])
		        + ",  I33="
		        + str(inertia[5])
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_mass_matrix instead.", DeprecationWarning)

def CogCoordinatesOfElement(result: object, element_type: int, element_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_cog_coordinates` instead.


	This function calculates the coordinates of the geometrical center of gravity of a SHELL or SOLID element of a given model for a specific resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element

	Returns
	-------
	object
		It returns a list containing the coordinates of the geometrical center of gravity of the specified element.
		Upon failure, invalid coordinates [0 0 0] will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    elem_id = 1
		    element_type = constants.SOLID
		
		    cog = elements.CogCoordinatesOfElement(all_resultsets[0], element_type, elem_id)
		
		    print(cog)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_cog_coordinates instead.", DeprecationWarning)

def CogCoordinatesOfSomeElements(resultset: object, elements: object) -> object:

	"""

	This function calculates the coordinates of the geometrical center of gravity of a SHELL or SOLID element of a given model for a specific resultset.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a Resultset of the model

	elements : object
		List containing objects of type Element. Elements should be of the same model as the resultset.

	Returns
	-------
	object
		It returns a list containing the coordinates of the geometrical center of gravity of the specified element.
		Upon failure, empty list [] will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    visible_elements = elements.VisibleElements(model_id)
		
		    cog = elements.CogCoordinatesOfSomeElements(all_resultsets[0], visible_elements)
		    print(cog)
		
		    # or
		
		    element_types = list()
		    element_ids = list()
		
		    for e in visible_elements:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		    cog = elements.CogCoordinatesOfSomeElements(
		        all_resultsets[0], element_types, element_ids
		    )
		    print(cog)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CalcElementABDMatrix(model_num: int, element_type: int, element_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_abd_matrix` instead.


	This function calculates the ABD matrix of the stack of an element .

	Parameters
	----------
	model_num : int

	element_type : int

	element_id : int

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
		from meta import elements
		from meta import constants
		
		
		def main():
		    # Need some documentation? Run this with F5
		    model_id = 0
		    elem_id = 26801
		    elem_type = constants.SHELL
		
		    ABD_matrix = elements.CalcElementABDMatrix(model_id, elem_type, elem_id)
		
		    for tmp_matrix in ABD_matrix:
		        print(tmp_matrix)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_abd_matrix instead.", DeprecationWarning)

def CalcElementABCDMatrixThroughThickness(model_num: int, element_type: int, element_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_abcd_matrix_thickness` instead.


	This function calculates the A,B,C,D matrices through thickness for a stack of an element

	Parameters
	----------
	model_num : int

	element_type : int

	element_id : int

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
		from meta import elements
		from meta import results
		from meta import constants
		
		
		def main():
		    # Need some documentation? Run this with F5
		    model_id = 0
		    elem_id = 26801
		    elem_type = constants.SHELL
		
		    ABD_matrix = elements.CalcElementABCDMatrixThroughThickness(
		        model_id, elem_type, elem_id
		    )
		
		    for tmp_matrix in ABD_matrix:
		        print(tmp_matrix)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_abcd_matrix_thickness instead.", DeprecationWarning)

def ColorOfElement(model_id: int, window_name: str, element_type: int, element_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_color` instead.


	Returns the color of the specified element, for the active style.

	Parameters
	----------
	model_id : int
		The id of the model.

	window_name : str
		The name of the window.

	element_type : int
		The type of the element.

	element_id : int
		The id of the element.

	second_id : int, optional
		The secondary id of the element.

	Returns
	-------
	object
		Returns the color of the element, or None for failure

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    element_type = constants.SHELL
		    element_id = 1
		    color = elements.ColorOfElement(model_id, window_name, element_type, element_id)
		    print(color)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_color instead.", DeprecationWarning)

def IdentifyElementsReset(model_id: int, element_types: object, element_ids: object, second_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_elements` instead.


	This function allows the user to reset the identification of all or specific elements of the specified model. It can be called with two different ways. The one is with lists of ids and types, and the other is with element_ids = 'all' and element_types = constants.ELEMENT_TYPE

	Parameters
	----------
	model_id : int
		Id of the model

	element_types : object
		Either a list with integers corresponding to the types of the elements, or an integer that represents the type of the elements (zero for all element types).

	element_ids : object
		List with integers corresponding to the ids of the elements, or string 'all'.

	second_ids : object, optional
		List with integers corresponding to the ids of the elements.

	Returns
	-------
	object
		This function returns None

	See Also
	--------
	elements.IdentifySomeElements, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import elements
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    ide_elements = elements.IdentifiedElements(model_id, window_name)
		    ids = list()
		    seq_ids = list()
		    types = list()
		
		    for el in ide_elements:
		        ids.append(el.id)
		        seq_ids.append(el.second_id)
		        types.append(el.type)
		    model_id = 0
		    element_types = types
		    element_ids = ids
		    sequential_ids = seq_ids
		    ret = elements.IdentifyElementsReset(
		        model_id, element_types, element_ids, sequential_ids
		    )
		    print(ret)
		    # or
		    # element_types = constants.SHELL
		    # element_ids = 'all'
		    # ret = elements.IdentifyElementsReset(model_id, element_types, element_ids)
		    # print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_elements instead.", DeprecationWarning)

def GatherElements(model_id: int, type: object, search_mode: str, gather_from: str, container: object, source: object, search_radius: float, angle: float) -> object:

	"""

	A function that gathers desired elements from all elements of the model.
	This function works as a script alternative for selecting. The user can gather any element he needs in a similar way as he would select elements from the screen.
	
	The function works in three modes:
	
	Mode A: Proximity
	 The function will gather all elements that are approximated to a user defined selection node, according to a given range.
	Mode B: Connectivity
	 The function will gather all elements that are connected to a starting (user given) element. Two elements are
	 considered connected if they have at least one common node.
	Mode C: Feature angle 
	 The function will gather elenents in a way that mimics the feature angle selection tool of META. A starting node 
	 must also be given.

	Parameters
	----------
	model_id : int
		Id of the model.

	type : object, optional
		Accepted values: "Same" or "All". Choose if the elements that will be returned are going to have the same type with the source element. With option "All", every elements will be returned regardless of their type, or by giving a type (or a list of types) the user can select which types are going to be returned.

	search_mode : str, optional
		Accepted values: "Proximity", "Connectivity" or "Feature_angle". (Default: "Proximity")

	gather_from : str, optional
		Accepted values: "Visible" or "All". Choose the pool from where the function will gather the elements.

	container : object, optional
		As containers the user can give an entity or a list of Parts and Groups.

	source : object, optional
		Starting element (or list of starting elements) (Mode B and Mode C only). Or starting node, or node id for Mode A.

	search_radius : float, optional
		The range around selection point that the function will search to gather elements (Mode A only).

	angle : float, optional
		The desired feature angle in order to execute Mode C.

	Returns
	-------
	object
		Returns a list with gathered elements on success or None on failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import elements
		from meta import parts
		from meta import groups
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1000
		    node_id = 1042800
		    e = elements.ElementById(model_id, element_type, element_id)
		    n = nodes.NodeById(model_id, node_id)
		
		    part = parts.PartById(model_id, constants.PSHELL, 7)
		    group_name = "test"
		    all_instances = 0
		    grs = groups.GroupsByName(model_id, group_name, all_instances)
		    if len(grs):
		        group = grs[0]
		    search_mode = "Connectivity"
		    gather_from = "visible"
		    source = e
		    elems = elements.GatherElements(model_id, search_mode, gather_from, source)
		    # or
		    type = "all"
		    search_mode = "Proximity"
		    container = part
		    source = n
		    search_radius = 100
		    elems = elements.GatherElements(
		        model_id, type, search_mode, container, source, search_radius
		    )
		    # or
		    type = "all"
		    search_mode = "Feature_angle"
		    gather_from = "visible"
		    container = group
		    source = e
		    angle = 10
		    elems = elements.GatherElements(
		        model_id, type, search_mode, gather_from, container, source, angle
		    )
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Element():

	"""

	Class for elements
	
	The type of the element is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corrsponding constant names of constant values.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    e = elements.Element(id=100, type=constants.SOLID, second_id=-1, model_id=0)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    r = elem.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    parts = elem.get_parts()
		    # parts = elem.get_parts( specifier = 'neighbour' )
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
		# method: get_element_layers
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    element_layers = elem.get_element_layers()
		    # element_layers = elem.get_element_layers( serial_id = 1 )
		    for elr in element_layers:
		        print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		        print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		        print(elr.id, elr.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(id=100, type=29, second_id=-1, model_id=model.id)
		    specifier = "all"
		    elem_nodes = elem.get_nodes(specifier)
		    for n in elem_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="Window1", page_id=0)
		    specifier = "visible"
		    window = w
		    elem_nodes = elem.get_nodes(specifier, window)
		    for n in elem_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinate_system
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    res = model.get_current_resultset()
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    specifier = "element"
		    cs = elem.get_coordinate_system(specifier)
		    specifier = "material"
		    # cs = elem.get_coordinate_system(specifier, resultset = res )
		    if cs:
		        print(cs.id)  # Coordinate System id
		        print(cs.type)  # Coordinate System type
		        print(cs.second_id)  # Coordinate System second id
		        print(cs.model_id)  # Coordinate System model id
		
		        print(cs.origin[0], cs.origin[1], cs.origin[2])
		        print(cs.xaxis[0], cs.xaxis[1], cs.xaxis[2])  # X-axis
		        print(cs.yaxis[0], cs.yaxis[1], cs.yaxis[2])  # Y-axis
		        print(cs.zaxis[0], cs.zaxis[1], cs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    m = elem.get_material()
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_name
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    name = "new_name"
		    elem.set_name(name)
		    name = elem.get_name()
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_comments
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.QUAD4, second_id=-1, model_id=0)
		    commnents = elem.get_comments()
		    print(commnents)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_subtype
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.QUAD4, second_id=-1, model_id=0)
		    subtype = elem.get_deck_subtype()
		    print(subtype)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=1100, type=constants.HEXA, second_id=-1, model_id=0)
		    mass = elem.get_mass()
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_no_nsm
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=1100, type=constants.HEXA, second_id=-1, model_id=0)
		    mass = elem.get_mass_no_nsm()
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_stiffness
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.ELAS2, second_id=-1, model_id=model.id
		    )
		    stiff = elem.get_stiffness()
		    print(stiff)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_damping
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.DAMP1, second_id=-1, model_id=0)
		    stiff = elem.get_damping()
		    print(stiff)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_matrix
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=700, type=constants.ONM2, second_id=-1, model_id=0)
		    mass = elem.get_mass_matrix()
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_abd_matrix
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.QUAD4, second_id=-1, model_id=0)
		    matrix = elem.get_abd_matrix()
		    print(matrix)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_abcd_matrix_thickness
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.QUAD4, second_id=-1, model_id=0)
		    matrix = elem.get_abcd_matrix_thickness()
		    print(matrix)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    res = model.get_current_resultset()
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    specifier = "min"
		    coords = elem.get_coordinates(specifier)
		    # coords = elem.get_coordinates(specifier, resultset = res)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    specifier = "min"
		    elem_deforms = elem.get_deformations(resultset, specifier)
		    for deform in elem_deforms:
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
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    specifier = "all"
		    elem_nodal = elem.get_nodal_scalar(resultset, specifier)
		    # elem_nodal = elem.get_nodal_scalar(res, 'max', layer = 'bottom' )
		    for nodal in elem_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    specifier = "all"
		    elem_nodal = elem.get_nodal_vector(resultset, specifier)
		    # specifier = 'max'
		    # elem_nodal = elem.get_nodal_vector(resultset, specifier, layer = 'bottom' )
		    for nodal in elem_nodal:
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    specifier = "min"
		    elem_corner = elem.get_corner_scalar(resultset, specifier)
		    # specifier = 'all'
		    # elem_corner = elem.get_corner_scalar(resultset, specifier , layer = 'top')
		    for corn in elem_corner:
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner with this corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_vector
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    specifier = "min"
		    elem_corner = elem.get_corner_vector(resultset, specifier)
		    # elem_corner = elem.get_corner_vector(resultset, specifier , layer = 'top')
		    for corn in elem_corner:
		        print(corn.value)  # Corner vector value
		        print(corn.x)  # X component Corner value
		        print(corn.y)  # Y component Corner value
		        print(corn.z)  # Z component Corner value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner with this corner vector value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    centroid = elem.get_centroid_scalar(resultset)
		    # centroid = elem.get_centroid_scalar(resultset, layer = 'bottom')
		    if centroid:
		        print(centroid.value)  # Centroid scalar value of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    resultset = model.get_current_resultset()
		    centroid = elem.get_centroid_vector(resultset)
		    # centroid = elem.get_centroid_vector(resultset, layer = 'bottom', principal = 'first')
		    if centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    centroid = elem.get_shell_normal(res)
		    if centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_area(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_volume(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_area_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_integral
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_volume_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_area_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_weighted_average
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_volume_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_volumetric_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=10, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_mass_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=10, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_mass_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_force
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_normal_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_force
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_shear_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_uniformity_index
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SHELL, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_vector_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_cog_coordinates
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    val = elem.get_cog_coordinates(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=12444, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = elem.set_attribute(attribute_name, attribute_type, attribute_value)
		    attr = elem.get_attributes()
		    # attr = elem.get_attributes(attribute_name = 'new_attr')
		    print(ret)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    model = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    color = elem.get_color(win)
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_node
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node = nodes.Node(id=1, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_node(res, node, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_node
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node = nodes.Node(id=1, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_node(res, node, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    elem1 = elements.Element(
		        id=200, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_element(res, elem1, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    elem1 = elements.Element(
		        id=200, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_element(res, elem1, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    part = parts.Part(id=200, type=constants.PSHELL, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_part(res, part, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    part = parts.Part(id=200, type=constants.PSHELL, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_part(res, part, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    group = groups.Group(name="group_name", model_id=model.id)
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_group(res, group, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    group = groups.Group(name="group_name", model_id=model.id)
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_group(res, group, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_boundary
		# PYTHON script
		import meta
		from meta import elements
		from meta import models
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(id=5, type=constants.QUAD4, second_id=-1, model_id=model.id)
		    bound = boundaries.Boundary(
		        id=1, second_id=0, type=constants.SPC1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_boundary(res, bound, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_boundary
		# PYTHON script
		import meta
		from meta import elements
		from meta import models
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(id=5, type=constants.QUAD4, second_id=-1, model_id=model.id)
		    bound = boundaries.Boundary(
		        id=1, second_id=0, type=constants.SPC1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		    dist = elem.get_elongation_from_boundary(res, bound, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_cut_plane
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    plane = planes.Plane(name="plane_name")
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_cut_plane(res, plane)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_cut_plane
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    plane = planes.Plane(name="plane_name")
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_cut_plane(res, plane)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_line(res, node1, res, node2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line
		# PYTHON script
		import meta
		from meta import elements
		from meta import models
		from meta import constants
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_line(res, node1, res, node2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    node3 = nodes.Node(id=300, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_plane(res, node1, res, node2, res, node3, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    node3 = nodes.Node(id=300, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_plane(res, node1, res, node2, res, node3, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line_coords
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    point1 = [0.25, 2.32, 3.39]
		    point2 = [1.35, -4.9, 2.35]
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_line_coords(res, point1, point2)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line_coords
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    point1 = [0.25, 2.32, 3.39]
		    point2 = [1.35, -4.9, 2.35]
		    res = model.get_current_resultset()
		    elong = elem.get_elongation_from_line_coords(res, point1, point2)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    point1 = [0.25, 2.32, 3.39]
		    point2 = [1.35, -4.9, 2.35]
		    point3 = [0.3, 0.4, 1]
		    res = model.get_current_resultset()
		    dist = elem.get_distance_from_plane_coords(res, point1, point2, point3)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane_coords
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.QUAD4, second_id=-1, model_id=model.id
		    )
		    point1 = [0.25, 2.32, 3.39]
		    point2 = [1.35, -4.9, 2.35]
		    point3 = [0.3, 0.4, 1]
		    res = model.get_current_resultset()
		    dist = elem.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    name = "new_name"
		    ret = elem.set_name(name)
		    name = elem.get_name()
		    print(ret)
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=12444, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = elem.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_name = 'new_attr'
		    # attribute_type = 'string'
		    # attribute_value = 'my_atrribute'
		    # ret = elem.set_attribute(attribute_name, attribute_type, attribute_value)
		    attribute_name = "new_attr"
		    attr = elem.get_attributes(attribute_name)
		    print(ret)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_coordinate_system
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import coordsystems
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    coord = coordsystems.CoordSystem(id=1, model_id=model.id)
		    cs = elem.set_coordinate_system(coord)
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
		# method: set_centroid_scalar
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import results
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		
		    new_function_data_name = "Centroid Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    ret = results.StartAddingCentroidScalar(
		        res, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    print(ret)
		    value = 15.5
		    ret = elem.set_centroid_scalar(res, value)
		    layer = "top"
		    # ret = elem.set_centroid_scalar(res, value, layer)
		    print(ret)
		    ret = results.EndAddingCentroidScalar(res)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_centroid_vector
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import results
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    vec = [0.354, 0.6831, 0.6834, -0.2572]
		
		    ret = results.StartAddingCentroidVector(
		        res, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    print(ret)
		    ret = elem.set_centroid_vector(res, vec)
		    print(ret)
		    results.EndAddingCentroidVector(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_corner_scalar
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import results
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		
		    new_function_data_name = "Corner Scalar Data"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		    layer = "one"
		
		    node_ids = list()
		    corner_values = list()
		    element_nodes = elem.get_nodes("all")
		    value = 0.1
		    for n in element_nodes:
		        node_ids.append(n.id)
		        corner_values.append(value)
		        value = value + 0.1
		    ret = results.StartAddingCornerScalar(
		        res, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    print(ret)
		    ret = elem.set_corner_scalar(res, node_ids, corner_values, centroid_value=value)
		    print(ret)
		    ret = results.EndAddingCornerScalar(res)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_corner_vector
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		from meta import results
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    res = model.get_current_resultset()
		
		    new_function_data_name = "Corner Vector Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    node_ids = list()
		    corner_values = list()
		
		    element_nodes = elem.get_nodes("all")
		    value = 0.1
		    vx = 1.0
		    vy = 0.0
		    vz = 0.0
		
		    for n in element_nodes:
		        node_ids.append(n.id)
		        values = [value, vx, vy, vz]
		        value = value + 0.1
		
		        corner_values.append(values)
		    ret = results.StartAddingCornerVector(
		        res, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    print(ret)
		    layer = "one"
		    ret = elem.set_corner_vector(res, node_ids, corner_values)
		    print(ret)
		    ret = results.EndAddingCornerVector(res)
		    print(ret)
		
		    elem.identify()
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    ret = elem.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    ret = elem.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    elem = elements.Element(
		        id=100, type=constants.SOLID, second_id=-1, model_id=model.id
		    )
		    ret = elem.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_type
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elem = elements.Element(id=100, type=constants.QUAD4, second_id=-1, model_id=0)
		    type = elem.get_deck_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    e = elements.Element(id=100, type=constants.SOLID, second_id=-1, model_id=0)
		    can_use = e.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    el = elements.Element(id=2, type=constants.SHELL, model_id=m.id, second_id=-1)
		    res = m.get_current_resultset()
		    val = el.get_normal_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    el = elements.Element(id=2, type=constants.SHELL, model_id=m.id, second_id=-1)
		    res = m.get_current_resultset()
		    val = el.get_shear_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the element.

	"""

	second_id: int = None
	"""
	Second id of the element. Some element types may have a second id which is a number equal to or greater than zero (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	"""

	model_id: int = None
	"""
	Model id of the element.

	"""

	type: int = None
	"""
	Type of the element (mETA constant).

	"""

	subtype: int = None
	"""
	Subtype of the element.

	"""

	visible: int = None
	"""
	- 1 if the element is visible on the active or first enabled window of the active page
	- 0 if the element is not visible

	"""

	part_id: int = None
	"""
	Id of the part the element belongs to, -1 if element belongs to no part.

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the element.


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the node. Upon failure, it returns None.

		"""


	def get_parts(self, specifier: str) -> object:

		"""

		This method gets the part of the element.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible value is:
			- 'neighbour' : get the neigbour parts of the element.
			
			If absent, the method will return the part of the element.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Part.Upon failure it returns an empty list

		"""


	def get_element_layers(self, serial_id: int) -> object:

		"""

		This method gets the layers of the element.


		Parameters
		----------
		serial_id : int, optional
			Serial id of the layer. If absent the method will return all element Layers

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class ElementLayer referring to one specific layer of the element.Upon failure, an empty list is returned.

		"""


	def get_nodes(self, specifier: str, window: object) -> object:

		"""

		This method gets the nodes of the element.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodes of the element (default value).
			- 'visible' : visible nodes of the element. Optionally combined with argument window
			- 'reference' : reference node of the element. For example, RBE2 and RBE3 elements have reference nodes.

		window : object, optional
			An object of class Window. Used only if specifier is: 'visible'. If this argument is set, the method will return only the visible nodes in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node.Upon failure it returns an empty list.

		"""


	def get_coordinate_system(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the coordinate system of the element.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'user' : user defined coordinate. 
			- 'element' : coordinate system of the element.
			- 'material' : coordinate system of the element, according to "Material Orientation" visibility option.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns an ElementCoordSystem object, if specifier is 'element', or 'material, or it returns a CoordSystem object if specifier is 'user'.Upon failure it returns None.

		"""


	def get_material(self) -> object:

		"""

		This method gets the material of the element.


		Returns
		-------
		object
			Upon success, it returns an object of class Material, referring to the material of the element.Upon failure, it returns None.

		"""


	def get_name(self) -> str:

		"""

		This method gets the name of the element.


		Returns
		-------
		str
			Upon success, it returns the name of the element.Upon failure, it returns None

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of an element.


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the element.Upon failure, it returns None.

		"""


	def get_deck_type(self) -> str:

		"""

		This method gets the type of the element.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the type for the deck of the element.Upon failure, None is returned.

		"""


	def get_deck_subtype(self) -> str:

		"""

		This method gets the subtype of the element.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the subtype for the deck of the element.Upon failure, None is returned.

		"""


	def get_stiffness(self) -> float:

		"""

		This method gets the stiffness of the ELAS element.


		Returns
		-------
		float
			It returns a float value referring to the stiffness of the ELAS element.Upon failure, it returns None.

		"""


	def get_damping(self) -> float:

		"""

		This method gets the damping of a damp element.


		Returns
		-------
		float
			Upon success, it returns a float value referring to the damping of the damp element.Upon failure, it returns None.

		"""


	def get_mass_matrix(self) -> object:

		"""

		This method gets the coordinate system id, the mass and the inertia of a the mass element. Element type must be ONM1 or ONM2.


		Returns
		-------
		object
			Upon success, it returns a list which contains:- position 0: The coordinate system id- position 1: A list of floats, corresponding to Mass (1st float) and Inertia (all the rest). Upon failure, an empty list is returned.

		"""


	def get_abd_matrix(self) -> object:

		"""

		This method gets the ABD matrix of the element.


		Returns
		-------
		object
			Upon success, it returns a 6X6 matrix in the form of a list containing other lists.Upon failure, it returns an empty list.

		"""


	def get_abcd_matrix_thickness(self) -> object:

		"""

		This method gets the A,B,C,D matrices through thickness for a stack of the element.


		Returns
		-------
		object
			Upon success, it returns a 12X3 matrix in the form of a list containing other lists.The first 3 lists is the A matrix.The next 3 lists is the B matrix.The next 3 lists is the C matrix.The last 3 lists is the D matrix.Upon failure, it rerurns an empty list.

		"""


	def get_cog_coordinates(self, resultset: object) -> object:

		"""

		This method gets the coordinates of the geometrical center of gravity of  the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list containing the coordinates of the geometrical center of gravity of the specified element.Upon failure, an empty list is returned.

		"""


	def get_color(self, window: object) -> object:

		"""

		This method gets the color of the element, for the active style.


		Parameters
		----------
		window : object
			An object of class Window

		Returns
		-------
		object
			Upon success, it returns an object of class Color.Upon failure, it returns None

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the element.


		Parameters
		----------
		attribute_name : str
			Attribute name

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_mass(self) -> float:

		"""

		This method gets the mass of the element.


		Returns
		-------
		float
			Upon success, it returns the mass of the element.Upon failure, it returns None.

		"""


	def get_mass_no_nsm(self) -> float:

		"""

		This method gets the mass of the element, excluding NSM.


		Returns
		-------
		float
			Upon success, it returns the mass of the element. Upon failure, it returns None.

		"""


	def get_area(self, resultset: object) -> float:

		"""

		This method gets the area of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area of the element.Upon failure, it returns None.

		"""


	def get_volume(self, resultset: object) -> float:

		"""

		This method gets the volume of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model

		Returns
		-------
		float
			Upon success, it returns the volume of the element.Upon failure, it returns None.

		"""


	def get_area_integral(self, resultset: object) -> float:

		"""

		This method gets the area integral of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area integral of the element.Upon failure, it returns None.

		"""


	def get_volume_integral(self, resultset: object) -> float:

		"""

		This method gets the volume integral of the element


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volume integral of the element.Upon failure, it returns None.

		"""


	def get_area_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the area weighted average of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the area weighted average.Upon failure, it returns None.

		"""


	def get_volume_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the volume weighted average of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volume weigthed average.Upon failure, it returns None.

		"""


	def get_volumetric_flow(self, resultset: object) -> float:

		"""

		This method gets the volumetric flow of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the volumetric flow of the element.Upon failure, it returns None.

		"""


	def get_mass_flow(self, resultset: object) -> float:

		"""

		This method gets the mass flow rate of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model

		Returns
		-------
		float
			Upon success, it returns the mass flow rate of the element.Upon failure, it returns None.

		"""


	def get_mass_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the mass weighted average of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			It returns a float value as the result of the calculated mass weighted average of the element. Upon failure, None will be returned.

		"""


	def get_normal_force(self, resultset: object) -> object:

		"""

		This method gets the normal force of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""


	def get_shear_force(self, resultset: object) -> object:

		"""

		This method gets the shear force of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude.Upon failure, an empty list is returned.

		"""


	def get_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the uniformity index of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated uniformity index of the element.Upon failure, None will be returned.

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
			It returns a float value as the result of the calculated vector uniformity index of the element.Upon failure, None will be returned.

		"""


	def get_coordinates(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the maximum or the minimum coordinates in each direction (X, Y, Z) of the element.


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
			It returns a list with 3 objects of class Node that correspond to the nodes with the maximum coordinates in each direction of the specified element.- Index 0 contains the Node with the maximum X coordinate- Index 1 contains the Node with the maximum Y coordinate- Index 2 contains the Node with the maximum Z coordinate. Upon failure, an empty list is returned.

		"""


	def get_deformations(self, resultset: object, specifier: str) -> object:

		"""

		This method gets the deformations of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations (default value).
			- 'max' : max deformation
			- 'min' : min deformation

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Deformation.Upon failure, it returns an empty list.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: object, layer: str) -> object:

		"""

		This method gets the nodal scalar values of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar (default value).
			- 'max' : max nodal scalar
			- 'min' : min nodal scalar

		layer : str, optional
			Location of the nodal scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalScalar. Upon failure, it returns an empty list.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, layer: str) -> object:

		"""

		This method gets the nodal vector values of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector (default value).
			- 'max' : max nodal vector
			- 'min' : min nodal vector

		layer : str, optional
			Location of the nodal vector values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalVector. Upon failure, it returns an empty list.

		"""


	def get_corner_scalar(self, resultset: object, specifier: str, layer: str) -> object:

		"""

		This method gets the corner scalar values of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar (default value).
			- 'max' : max corner scalar
			- 'min' : min corner scalar

		layer : str, optional
			Location of the corner scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class CornerScalar.Upon failure, it returns an empty list.

		"""


	def get_corner_vector(self, resultset: object, specifier: str, layer: str) -> object:

		"""

		This method gets the corner vector values of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector (default value).
			- 'max' : max corner vector
			- 'min' : min corner vector

		layer : str, optional
			Location of the corner vector values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class CornerVector.Upon failure, it returns an empty list.

		"""


	def get_centroid_scalar(self, resultset: object, layer: str) -> object:

		"""

		This method gets the centroid scalar of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the centroid scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns an object of class CentroidScalar, or None if the element has novalue. Upon failure, it returns None.

		"""


	def get_centroid_vector(self, resultset: object, layer: str, principal: str) -> object:

		"""

		This method gets the centroid vector values of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the centroid vector values. Possible values are:
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
			Upon success, it returns a n object of class CentroidVector, or None if the element has novalue. Upon failure, it returns None.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vector of the element of type SHELL.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns an object of class CentroidVector referring to the shell normal vector of the element.Upon failure, None is returned.

		"""


	def get_distance_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the distance of the element from a given node.


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

		This method gets the elongation of the element from a given node.


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

		This method gets the distance of the element from a given element.


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

		This method gets the elongation of the element from a given element.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance of the element from a given part.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the elongation of the element from a given part.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the distance of the element from a given group.


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

		This method gets the elongation of the element from a given element.


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

		This method gets the distance of the node from a given boundary element.


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

		This method gets the elongation of the element from a given boundary element.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the distance of the element from a given line.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the elongation of the node from a given line.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the distance of the element from a line from the given coordinates.


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


	def get_elongation_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the elongation of the element from a line from the given coordinates.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the distance of the element from a given cutplane.


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

		This method gets the elongation of the node from a given plane.


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

		This method gets the distance of the element from a given plane.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the elongation of the element from a given plane.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the distance of the element from a plane from the given coordinates.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the elongation of the element from a plane from the given coordinates.


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
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the element.


		Parameters
		----------
		name : str
			Name of the element.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the element. If the given attribute does not exist it is automatically created and its value is set.


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
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_coordinate_system(self, coordinate_system: object) -> object:

		"""

		This method sets an existing coordinate system on an element.


		Parameters
		----------
		coordinate_system : object
			An object of class CoordSystem.

		Returns
		-------
		object
			Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on the element.Upon failure None is returned.

		"""


	def set_centroid_scalar(self, resultset: object, value: float, layer: str) -> bool:

		"""

		This method sets centroid scalar value on an element. Functions 'StartAddingCentroidScalar', 'StartChangingCentroidScalar' or 'StartAppendingCentroidScalar' must be called with the same argument (result) before starting adding centroid scalar values. Function 'EndAddingCentroidScalar' must be called with the same argument (result) after ending adding centroid scalar values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model to which the value is added.

		value : float
			Centroid scalar value of the element.

		layer : str, optional
			Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		bool
			Upon success it returns True. Upon failure False

		"""


	def set_centroid_vector(self, resultset: object, value: object, layer: str) -> bool:

		"""

		This method sets centroid vector value on an element. Functions 'StartAddingCentroidVector', 'StartChangingCentroidVector' or 'StartAppendingCentroidVector' must be called with the same argument (result) before starting adding centroid vector values. Function 'EndAddingCentroidVector' must be called with the same argument (result) after ending adding centroid vector values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model to which the value is added.

		value : object
			A list with the normalized vector components as floats [value, X-direction vector component, Y-direction vector component, Z-direction vector component]

		layer : str, optional
			Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		bool
			Upon success it returns True. Upon failure False

		"""


	def set_corner_scalar(self, resultset: object, corners: object, values: object, layer: str, centroid_value: float) -> bool:

		"""

		This method sets corner scalar values on an element with specific id and type of a given model. Functions 'StartAddingCornerScalar', 'StartChangingCornerScalar' or 'StartAppendingCornerScalar' must be called with the same argument (result) before starting adding corner scalar values. Function 'EndAddingCornerScalar' must be called with the same argument (result) after ending adding corner scalar values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model to which the value is added.

		corners : object
			A list with ids of some nodes of the element.

		values : object
			A list of floats as corner scalar values of the element.

		layer : str, optional
			Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		centroid_value : float, optional
			Centroid scalar value of the element. If the automatic calculation of centroid scalar values in function 'StartAddingCornerScalar' has been specified then it will be ignored.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_corner_vector(self, resultset: object, corners: object, values: object, layer: str, centroid_value: object) -> bool:

		"""

		This function adds corner vector values on an element with specific id and type of a given model. Functions 'StartAddingCornerVector', 'StartChangingCornerVector' or 'StartAppendingCornerVector' must be called with the same argument (result) before starting adding corner vector values. Function 'EndAddingCornerVector' must be called with the same argument (result) after ending adding corner vector values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model to which the value is added.

		corners : object
			A list with ids of some nodes of the element.

		values : object
			A list that contains lists of 4 float values.
			The first is the centroid scalar value, the second the value of X component, the third the value of Y component and the fourth the value of Z component.

		layer : str, optional
			Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

		centroid_value : object, optional
			Centroid vector values of the element. If the automatic calculation of centroid scalar values in function 'StartAddingCornerVector' has been specified then it will be ignored. The argument is a list of 4 float values . The first is the centroid scalar value, the second the value of X component, the third the value of Y component and the fourth the value of Z component.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Element entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_normal_moment(self, resultset: object) -> object:

		"""

		This method gets the normal moment of the element.


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

		This method gets the shear moment of the element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second element the component Y, the third the component Z and the fourth the magnitude. Upon failure, an empty list is returned.

		"""

class ElementLayer():

	"""

	Class for element layers.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    if elr:
		        print(elr.serial, elr.element_id, elr.element_type, elr.second_id)
		        print(elr.model_id, elr.material_id, elr.thickness, elr.theta)
		        print(elr.id, elr.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    layer_color = elr.get_color()
		    if layer_color:
		        print(layer_color.r)  # R value
		        print(layer_color.g)  # G value
		        print(layer_color.b)  # B value
		        print(layer_color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_element
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    e = elr.get_element()
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    m = elr.get_material()
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    r = elr.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    elr = elements.ElementLayer(
		        serial=1,
		        id=0,
		        element_id=11840,
		        element_type=constants.SHELL,
		        second_id=-1,
		        model_id=0,
		    )
		    can_use = elr.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	serial: int = None
	"""
	Serial number of the element layer.

	"""

	element_id: int = None
	"""
	Id of the element of the layer.

	"""

	element_type: int = None
	"""
	Type of the element of the layer (mETA constant).

	"""

	second_id: int = None
	"""
	Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	"""

	model_id: int = None
	"""
	Model id of the element layer.

	"""

	material_id: int = None
	"""
	Id of the material of the layer.

	"""

	thickness: float = None
	"""
	Thickness.

	"""

	theta: float = None
	"""
	Theta.

	"""

	id: int = None
	"""
	Layer id.

	"""

	name: str = None
	"""
	Name of the layer.

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the element layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the element layer. Upon failure, it returns None.

		"""


	def get_element(self) -> object:

		"""

		This method gets the element of the element layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Element referring to the element of the element layer. Upon failure, it returns None.

		"""


	def get_material(self) -> object:

		"""

		This method gets the material of the element layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Material referring to the material of the element layer. Upon failure, it returns None.

		"""


	def get_color(self) -> object:

		"""

		This method gets the color of the element layer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the color of the element layer. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META ElementLayer entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class ElementFace():

	"""

	Class for element faces.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import constants
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    all_faces = elements.SolidSkinOfModel(model_id, window_name)
		    iter_end = min(10, len(all_faces))
		    for ef in all_faces[0:iter_end]:
		        print(ef.id, ef.model_id, ef.type, ef.total_nodes, ef.node_ids)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the element of the face.

	"""

	model_id: int = None
	"""
	Model id of the element face.

	"""

	type: int = None
	"""
	Type of the element of the face (mETA constants).

	"""

	total_nodes: int = None
	"""
	Number of nodes.

	"""

	node_ids: object = None
	"""
	Ids of the nodes.

	"""
