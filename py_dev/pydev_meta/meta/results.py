from __future__ import annotations
from typing import *

def AddCentroidScalarOnElement(result: object, element_type: int, element_id: int, second_id: int, value: float, layer: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_centroid_scalar` instead.


	This function adds centroid scalar value on an element with specific id and type of a given model. Functions 'StartAddingCentroidScalar', 'StartChangingCentroidScalar' or 'StartAppendingCentroidScalar' must be called with the same argument (result) before starting adding centroid scalar values. Function 'EndAddingCentroidScalar' must be called with the same argument (result) after ending adding centroid scalar values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	value : float
		Centroid scalar value of the element.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    value = 0.354
		
		    new_function_data_name = "Centroid Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartAddingCentroidScalar(
		        result, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    results.AddCentroidScalarOnElement(
		        result, element_type, element_id, second_id, value
		    )
		    results.EndAddingCentroidScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_centroid_scalar instead.", DeprecationWarning)

def AddCentroidScalarOnSomeElements(resultset: object, elements: object, values: object, layer: str) -> bool:

	"""

	This function adds centroid scalar value on some elements with specific id and type of a given model. Functions 'StartAddingCentroidScalar', 'StartChangingCentroidScalar' or 'StartAppendingCentroidScalar' must be called with the same argument (result) before starting adding centroid scalar values. Function 'EndAddingCentroidScalar' must be called with the same argument (result) after ending adding centroid scalar values.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	elements : object
		A list with objects of class Element.

	values : object, optional
		A list of floats as centroid scalar values of the elements.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value'  (default)
		- 'bottom'
		- 'top'

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Corner Vector Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		    corner_vector = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            # create a new CornerVector object and append it into a list.
		            # this will be used to call the AddCornerVectorOnSomeElements with a more simple prototype
		            # corner_vector.append( results.CornerVector(value, vx, vy, vz, e.id, e.second_id, e.type, n.id) )
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartAddingCornerVector(
		        result, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        result,
		        viselems,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    # or
		    # results.AddCornerVectorOnSomeElements(result, elements_types, elements_ids, second_ids, elements_node_ids, elements_corner_values, elements_corner_vx_values, elements_corner_vy_values, elements_corner_vz_values, layer)
		    # or a more simple prototype
		    # results.AddCornerVectorOnSomeElements(result, corner_vector, layer)
		
		    results.EndAddingCornerVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCentroidVectorOnElement(result: object, element_type: int, element_id: int, second_id: int, value: float, xvector: float, yvector: float, zvector: float, layer: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_centroid_vector` instead.


	This function adds a centroid vector value on an element with specific id and type of a given model. Functions 'StartAddingCentroidVector', 'StartChangingCentroidVector' or 'StartAppendingCentroidVector' must be called with the same argument (result) before starting adding centroid vector values. Function 'EndAddingCentroidVector' must be called with the same argument (result) after ending adding centroid vector values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	value : float
		Centroid vector value of the element.

	xvector : float
		Normalized X-direction vector component.

	yvector : float
		Normalized Y-direction vector component.

	zvector : float
		Normalized Z-direction vector component.

	layer : str
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    value = 0.354
		    xvector = 0.6831
		    yvector = 0.6834
		    zvector = -0.2572
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartAddingCentroidVector(
		        result, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    results.AddCentroidVectorOnElement(
		        result, element_type, element_id, second_id, value, xvector, yvector, zvector
		    )
		    results.EndAddingCentroidVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_centroid_vector instead.", DeprecationWarning)

def AddCentroidVectorOnSomeElements(resultset: object, elements: object, values: object, xvector: object, yvector: object, zvector: object, layer: str) -> int:

	"""

	This function adds a centroid vector value on some elements with specific id and type of a given model. Functions 'StartAddingCentroidVector', 'StartChangingCentroidVector' or 'StartAppendingCentroidVector' must be called with the same argument (result) before starting adding centroid vector values. Function 'EndAddingCentroidVector' must be called with the same argument (result) after ending adding centroid vector values.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	elements : object
		A list with objects of class Element.

	values : object
		A list of floats as the magnitude of the centroid vector values of the elements.

	xvector : object
		A list of floats as the normalized X-direction vector components.

	yvector : object
		A list of floats as the normalized Y-direction vector components.

	zvector : object
		A list of floats as the normalized Z-direction vector components.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    region_bounds = "parts"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    allelems = elements.Elements(model_id)
		    for e in allelems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(-0.885)
		        xvector.append(-0.6346)
		        yvector.append(0.25723)
		        zvector.append(-0.68315)
		    results.StartAddingCentroidVector(
		        result, new_function_data_name, layer, region_bounds
		    )
		    ret = results.AddCentroidVectorOnSomeElements(
		        result, allelems, values, xvector, yvector, zvector
		    )
		    print(ret)
		    # or
		    # ret = results.AddCentroidVectorOnSomeElements(result, elements_types, elements_ids, second_ids, values, xvector, yvector, zvector)
		    # print (ret)
		    results.EndAddingCentroidVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCornerScalarOnElement(result: object, element_type: int, element_id: int, second_id: int, node_ids: object, corner_values: object, layer: str, centroid_value: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_corner_scalar` instead.


	This function adds corner scalar values on an element with specific id and type of a given model. Functions 'StartAddingCornerScalar', 'StartChangingCornerScalar' or 'StartAppendingCornerScalar' must be called with the same argument (result) before starting adding corner scalar values. Function 'EndAddingCornerScalar' must be called with the same argument (result) after ending adding corner scalar values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	node_ids : object
		A list with ids of some nodes of the element.

	corner_values : object
		A list of floats as corner scalar values of the element.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	centroid_value : float, optional
		Centroid scalar value of the element. If the automatic calculation of centroid scalar values in function 'StartAddingCornerScalar' has been specified then it will be ignored.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    node_ids = list()
		    corner_values = list()
		    element_nodes = nodes.NodesOfElement(model_id, element_type, element_id, second_id)
		    value = 0.1
		    for n in element_nodes:
		        node_ids.append(n.id)
		        corner_values.append(value)
		        value = value + 0.1
		    results.StartAddingCornerScalar(
		        result, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerScalarOnElement(
		        result, element_type, element_id, second_id, node_ids, corner_values, layer
		    )
		    results.EndAddingCornerScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_corner_scalar instead.", DeprecationWarning)

def AddCornerScalarOnSomeElements(result: object, elements: object, node_ids: object, corner_values: object, layer: str, centroid_values: object) -> bool:

	"""

	This function adds corner scalar values on some elements with specific id and type of a given model. Functions 'StartAddingCornerScalar', 'StartChangingCornerScalar' or 'StartAppendingCornerScalar' must be called with the same argument (result) before starting adding corner scalar values. Function 'EndAddingCornerScalar' must be called with the same argument (result) after ending adding corner scalar values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	elements : object
		A list, of objects of class Element.

	node_ids : object
		List with Ids of the nodes of the elements as integers.

	corner_values : object
		A list that contains a list of corner scalar values for each element as floats.

	layer : str
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	centroid_values : object, optional
		A list of floats as centroid scalar values of the elements. If the automatic calculation of centroid scalar values in function 'StartAddingCornerScalar' has been specified then it will be ignored.

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    corner_scalar = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            # create a new CornerScalar object and append it into a list.
		            # this will be used to call the AddCornerScalarOnSomeElements with a more simple prototype
		            # corner_scalar.append( results.CornerScalar(value, e.id, e.second_id, e.type, n.id) )
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		    results.StartAddingCornerScalar(
		        result, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerScalarOnSomeElements(
		        result, viselems, elements_node_ids, elements_corner_values, layer
		    )
		    # or
		    # results.AddCornerScalarOnSomeElements(result, elements_types, elements_ids, second_ids, elements_node_ids, elements_corner_values, layer)
		    # or a more simple prototype
		    # results.AddCornerScalarOnSomeElements(result, corner_scalar, layer)
		
		    results.EndAddingCornerScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddDeformationOnAllNodes(result: object, new_nodal_data_name: str, all_nodes: object, xdeform: object, ydeform: object, zdeform: object, use_default_postfix: int, small_displacements: int) -> bool:

	"""

	This function adds deformation in each direction (X, Y, Z) on a list of nodes with specific ids of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_nodal_data_name : str
		The new deformation data name of the resultset.

	all_nodes : object
		List, of objects of class Node, that contains all the nodes of the model.

	xdeform : object
		List with X deformation values as floats.

	ydeform : object
		List with Y deformation values as floats.

	zdeform : object
		List with Z deformation values as floats.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	small_displacements : int, optional
		Controls if deformations will be added with small displacements option enabled. Its default value is 0.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_nodal_data_name = "Deformations Data"
		
		    all_node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    for n in all_nodes:
		        all_node_ids.append(n.id)
		        xdeform.append(0.125)
		        ydeform.append(-0.31)
		        zdeform.append(-1.3)
		    results.AddDeformationOnAllNodes(
		        result, new_nodal_data_name, all_nodes, xdeform, ydeform, zdeform
		    )
		    # or
		    # results.AddDeformationOnAllNodes(result, new_nodal_data_name, all_node_ids, xdeform, ydeform, zdeform)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddDeformationOnNode(node_id: int, xdeform: float, ydeform: float, zdeform: float, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.set_deformations` instead.


	This function adds deformation in each direction (X, Y, Z) on a node with specific id of a model. Functions 'StartAddingDeformations', 'StartAppendingDeformations' or 'StartChangingDeformations' must be called with the same argument (result) before starting adding deformations. Function 'EndAddingDeformations' must be called with the same argument (result) after ending adding deformations.

	Parameters
	----------
	node_id : int
		Id of the node.

	xdeform : float
		X deformation value.

	ydeform : float
		Y deformation value.

	zdeform : float
		Z deformation value.

	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node_id = 10
		    xdeform = 0.26
		    ydeform = 1.15
		    zdeform = -0.0024
		
		    new_nodal_data_name = "Deformations Data"
		
		    meta.results.StartAddingDeformations(result, new_nodal_data_name)
		    meta.results.AddDeformationOnNode(result, node_id, xdeform, ydeform, zdeform)
		    meta.results.EndAddingDeformations(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.set_deformations instead.", DeprecationWarning)

def AddDeformationOnSomeNodes(result: object, nodes: object, xdeform: object, ydeform: object, zdeform: object) -> bool:

	"""

	This function adds deformation in each direction (X, Y, Z) on a list of nodes with specific ids of a model. Functions 'StartAddingDeformations', 'StartAppendingDeformations' or 'StartChangingDeformations' must be called with the same argument (result) before starting adding deformations. Function 'EndAddingDeformations' must be called with the same argument (result) after ending adding deformations.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodes : object
		List with of the nodes as objects of class Node.

	xdeform : object
		List with X deformation values as floats.

	ydeform : object
		List with Y deformation values as floats.

	zdeform : object
		List with Z deformation values as floats.

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_nodal_data_name = "Deformations Data"
		
		    node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    visnodes = nodes.VisibleNodes(model_id)
		    for n in visnodes:
		        node_ids.append(n.id)
		        xdeform.append(0.025)
		        ydeform.append(-0.91)
		        zdeform.append(-1.398)
		    results.StartAddingDeformations(result, new_nodal_data_name)
		    results.AddDeformationOnSomeNodes(result, visnodes, xdeform, ydeform, zdeform)
		    # or
		    # results.AddDeformationOnSomeNodes(result, node_ids, xdeform, ydeform, zdeform)
		    results.EndAddingDeformations(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNodalScalarOnAllNodes(resultset: object, new_function_data_name: str, all_nodes: object, values: object) -> int:

	"""

	This function adds nodal scalar values on some specific nodes of a given model.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	all_nodes : object
		List, of objects of class Node, that contains all the nodes of the model.

	values : object
		A list with nodal scalar values as floats.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    model = models.Model(0)
		    all_resultsets = model.get_resultsets()
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		    allnodes = model.get_nodes("all")
		    values = [0.8554] * len(allnodes)
		
		    results.AddNodalScalarOnAllNodes(result, new_function_data_name, allnodes, values)
		    # or
		    # all_node_ids = [n.id for n in allnodes]
		    # results.AddNodalScalarOnAllNodes(result, new_function_data_name, all_node_ids, values)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNodalScalarOnNode(node_id: int, value: float, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.set_nodal_scalar` instead.


	This function adds nodal scalar value on a specific node of a given model. Functions 'StartAddingNodalScalar', 'StartChangingNodalScalar' or 'StartAppendingNodalScalar' must be called with the same argument (result) before starting adding nodal scalar values. Function 'EndAddingNodalScalar' must be called with the same argument (result) after ending adding nodal scalar values.

	Parameters
	----------
	node_id : int
		Id of the node.

	value : float
		Nodal scalar value of the node.

	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		
		    node_id = 10
		    value = 5.326
		
		    results.StartAddingNodalScalar(result, new_function_data_name)
		    results.AddNodalScalarOnNode(result, node_id, value)
		    results.EndAddingNodalScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.set_nodal_scalar instead.", DeprecationWarning)

def AddNodalScalarOnSomeNodes(result: object, nodes: object, values: object) -> int:

	"""

	This function adds nodal scalar values on some specific nodes of a given model. Functions 'StartAddingNodalScalar', 'StartChangingNodalScalar' or 'StartAppendingNodalScalar' must be called with the same argument (result) before starting adding nodal scalar values. Function 'EndAddingNodalScalar' must be called with the same argument (result) after ending adding nodal scalar values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodes : object
		A list with objects of class Node.

	values : object
		A list with nodal scalar values as floats.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		
		    node_ids = list()
		    values = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(25, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.554)
		    results.StartAddingNodalScalar(result, new_function_data_name)
		    results.AddNodalScalarOnSomeNodes(result, some_nodes, values)
		    # or
		    # results.AddNodalScalarOnSomeNodes(result, node_ids, values)
		    results.EndAddingNodalScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNodalVectorOnAllNodes(result: object, new_function_data_name: str, all_nodes: object, values: object, xvector: object, yvector: object, zvector: object, vector_display_type: str) -> bool:

	"""

	This function adds nodal vector values on some specific nodes of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	all_nodes : object
		A list of objects of class Node, containing all the nodes of the model.

	values : object
		A list of floats as the magnitude of the nodal vector values of the nodes.

	xvector : object
		A list of floats as the normalized X-direction vector components.

	yvector : object
		A list of floats as the normalized Y-direction vector components.

	zvector : object
		A list of floats as the normalized Z-direction vector components.

	vector_display_type : str, optional
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    all_node_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    allnodes = nodes.Nodes(model_id)
		    for n in allnodes:
		        all_node_ids.append(n.id)
		        values.append(0.2)
		        xvector.append(0.682)
		        yvector.append(0.0)
		        zvector.append(0.7315)
		    results.AddNodalVectorOnAllNodes(
		        result, new_function_data_name, allnodes, values, xvector, yvector, zvector
		    )
		    # or
		    # results.AddNodalVectorOnAllNodes(result, new_function_data_name, all_node_ids, values, xvector, yvector, zvector)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNodalVectorOnNode(node_id: int, value: float, xvector: float, yvector: float, zvector: float, result: object) -> int:

	"""

	This function adds nodal vector values on a node with a specific id of a given model. Functions 'StartAddingNodalVector', 'StartChangingNodalVector' or 'StartAppendingNodalVector' must be called with the same argument (result) before starting adding nodal vector values. Function 'EndAddingNodalVector' must be called with the same argument (result) after ending adding nodal vector values.

	Parameters
	----------
	node_id : int
		Ids of the nodes.

	value : float
		Nodal vector value.

	xvector : float
		Normalized X-direction vector component.

	yvector : float
		Normalized Y-direction vector component.

	zvector : float
		Normalized Z-direction vector component.

	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    node_id = 10
		    value = 0.356
		    xvector = 0.682
		    yvector = 0.0
		    zvector = 0.7315
		
		    results.StartAddingNodalVector(result, new_function_data_name)
		    results.AddNodalVectorOnNode(result, node_id, value, xvector, yvector, zvector)
		    results.EndAddingNodalVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNodalVectorOnSomeNodes(result: object, nodes: object, values: object, xvector: object, yvector: object, zvector: object) -> int:

	"""

	This function adds nodal vector values on some nodes with a specific id of a given model. Functions 'StartAddingNodalVector', 'StartChangingNodalVector' or 'StartAppendingNodalVector' must be called with the same argument (result) before starting adding nodal vector values. Function 'EndAddingNodalVector' must be called with the same argument (result) after ending adding nodal vector values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodes : object
		A list with objects of class Node.

	values : object
		A list of floats as the magnitude of the nodal vector values of the nodes.

	xvector : object
		A list of floats as the normalized X-direction vector components.

	yvector : object
		A list of floats as the normalized Y-direction vector components.

	zvector : object
		A list of floats as the normalized Z-direction vector components.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    node_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(100, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.2)
		        xvector.append(0.682)
		        yvector.append(0.0)
		        zvector.append(0.7315)
		    results.StartAddingNodalVector(result, new_function_data_name)
		    results.AddNodalVectorOnSomeNodes(
		        result, some_nodes, values, xvector, yvector, zvector
		    )
		    # or
		    # results.AddNodalVectorOnSomeNodes(result, node_ids, values, xvector, yvector, zvector)
		    results.EndAddingNodalVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CentroidScalarListToDict(centroid_scalars: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class CentroidScalar. Key of the dictionary is the element id and member is the corresponding object of class CentroidScalar. 

	Parameters
	----------
	centroid_scalars : object
		List with objects of class CentroidScalar.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the element and member the corresponding CentroidScalar object.
		If a CentroidScalar object with the same element id exist in the given list, then only the first will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	results.Result, results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    layer = "top"
		    all_centroid = models.CentroidScalarOfModel(result)
		    iter_end = min(10, len(all_centroid))
		    less_centroid = all_centroid[0:iter_end]
		    dict_centroid = results.CentroidScalarListToDict(less_centroid)
		    for id, centroid in dict_centroid.items():
		        print(id)
		        print(centroid.value, centroid.element_id)
		        print(centroid.second_id, centroid.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CentroidVectorListToDict(centroids: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class CentroidVector.

	Parameters
	----------
	centroids : object
		List of objects of class CentroidVector.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the element and member the corresponding CentroidVector object.
		If a CentroidVector object with the same element id exist in the given list, then only the first will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_centroid = models.CentroidVectorOfModel(result)
		    iter_end = min(10, len(all_centroid))
		    less_centroid = all_centroid[0:iter_end]
		    dict_centroid = results.CentroidVectorListToDict(less_centroid)
		    for id, centroid in dict_centroid.items():
		        print(id)
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		        print(centroid.x, centroid.y, centroid.z)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ClearResultset(result: object, result_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.clear` instead.


	This function deletes the data of a given resultset. Resultset is specified by its object. 

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	result_type : str, optional
		Type of the data of the resultset. Possible values are:
		- 'deform': Deformation data
		- 'function': Function data.
		If it is absent, then both deformation and function data will be deleted.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    result_type = "function"
		    ret = results.ClearResultset(result, result_type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.clear instead.", DeprecationWarning)

def CollectNewResultsetsEnd() -> object:

	"""

	This function ends recording the creation of new resultsets. This function should be preceded by a corresponding call to script function CollectNewResultsetsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one specific newly created resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		
		
		def main():
		    results.CollectNewResultsetsStart()
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.ReportNewResultsets()
		    for res in new_resultsets:
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		    print("####################################################")
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.CollectNewResultsetsEnd()
		    for res in new_resultsets:
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


	"""

def CollectNewResultsetsStart() -> int:

	"""

	This function starts recording the creation of new resultsets. This function should be followed by a corresponding call to script function CollectNewResultsetsEnd().

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		
		
		def main():
		    results.CollectNewResultsetsStart()
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.ReportNewResultsets()
		    for res in new_resultsets:
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		    print("####################################################")
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.CollectNewResultsetsEnd()
		    for res in new_resultsets:
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


	"""

def CollectResults(result: object, result_type: str) -> object:

	"""

	This function collects results of a given model for a specific resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	result_type : str
		Type of the collected results. Its possible values are:
		- 'deformation' : Collect deformations
		- 'nodal_scalar' : Collect nodal scalar values
		- 'nodal_vector' : Collect nodal vector values
		- 'centroid_scalar' : Collect centroid scalar values
		- 'centroid_vector' : Collect centroid vector values
		- 'corner_scalar' : Collect corner scalar values

	Returns
	-------
	object
		It returns a list where each member of the list is an object referring to one specific result of the given model.
		If both bottom and top values are loaded this function will return the BOTTOM value.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    result_type = "deformation"
		    collected_results = results.CollectResults(result, result_type)
		    iter_end = min(10, len(collected_results))
		    for deform in collected_results[0:iter_end]:
		        print(deform.x, deform.y, deform.z, deform.total)  # X,Y,Z,Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

def CopyAllDeformations(source_result: object, target_result: object, new_nodal_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_deformations` instead.


	This function copies deformations of all nodes for all labels from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_nodal_data_name : str, optional
		The new name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyAllDeformations(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_deformations instead.", DeprecationWarning)

def CopyAllFunction(source_result: object, target_result: object, new_function_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_function` instead.


	This function copies function data (scalar, vector) of all elements for all labels from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_function_data_name : str, optional
		The new name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyAllFunction(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_function instead.", DeprecationWarning)

def CopyAllScalar(source_result: object, target_result: object, new_scalar_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_scalar` instead.


	This function copies scalar data of all elements for all labels from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_scalar_data_name : str, optional
		The new name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyAllScalar(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_scalar instead.", DeprecationWarning)

def CopyAllVector(source_result: object, target_result: object, new_vector_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_vector` instead.


	This function copies vector data of all elements for all labels from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_vector_data_name : str, optional
		The New name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyAllVector(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_vector instead.", DeprecationWarning)

def CopyDeformations(source_result: object, target_result: object, new_nodal_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_deformations` instead.


	This function copies deformations of all nodes from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_nodal_data_name : str
		The New name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyDeformations(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_deformations instead.", DeprecationWarning)

def CopyFunction(source_result: object, target_result: object, new_function_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_function` instead.


	This function copies function data (scalar, vector) of all elements from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_function_data_name : str, optional
		The New name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyFunction(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_function instead.", DeprecationWarning)

def CopyScalar(source_result: object, target_result: object, new_scalar_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_scalar` instead.


	This function copies scalar data of all elements from a resultset to another resultset.
	Both source and target resultsets must belong to the same model.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_scalar_data_name : str, optional
		The New name for the scalar data of the target resultset. If it is absent, then the default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyScalar(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_scalar instead.", DeprecationWarning)

def CopyVector(source_result: object, target_result: object, new_vector_data_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.copy_vector` instead.


	This function copies vector data of all elements from a resultset to another resultset.

	Parameters
	----------
	source_result : object
		An object of class Result that refers to the source Resultset of the model.

	target_result : object
		An object of class Result that refers to the target Resultset of the model.

	new_vector_data_name : str
		The new name for the vector data of the target resultset. If it is absent, then default label name is used.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    source_result = all_resultsets[1]
		    target_result = all_resultsets[4]
		    results.CopyVector(source_result, target_result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.copy_vector instead.", DeprecationWarning)

def CreateCycle(model_id: int, cycle: int) -> int:

	"""

	This function creates a cycle for a model specified by its id.

	Parameters
	----------
	model_id : int
		Model id.

	cycle : int
		Number of the cycle.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 1
		    ret = results.CreateCycle(model_id, cycle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateResultset(cycle: int, name: str, state_id: int, model_id: int) -> object:

	"""

	This function creates a resultset for a given model.

	Parameters
	----------
	cycle : int
		Cycle number of the resultset. It must refer to an existing cycle. If it is absent then resultsets will be created for all the existing cycles of the model.

	name : str
		Name of the resultset.

	state_id : int
		State id.

	model_id : int
		Model id.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    state_id = len(all_resultsets)
		    name = "Script added resultset"
		    cycle = 0
		    new_resultsets = results.CreateResultset(model_id, state_id, name, cycle)
		    for res in new_resultsets:
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


	"""

def CreateResultsetFrequency(model_id: int, frequency: float, name: str, cycle: int) -> object:

	"""

	This function creates a resultset for a given model. Argument "frequency" refers to the state variable frequency.

	Parameters
	----------
	model_id : int
		Model id.

	frequency : float
		Frequency of resultset.

	name : str
		Name of the resultset.

	cycle : int, optional
		Cycle number of the resultset. It must refer to an existing cycle. If it is absent then resultsets will be created for all the existing cycles of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    frequency = 25.22
		    name = "Frequency 25.22"
		    new_resultsets = results.CreateResultsetFrequency(model_id, frequency, name)
		    for res in new_resultsets:
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


	"""

def CreateResultsetTime(model_id: int, time: float, name: str, cycle: int) -> object:

	"""

	This function creates a resultset for a model specified by its id.

	Parameters
	----------
	model_id : int
		Model id.

	time : float
		Time of the resultset.

	name : str
		Name of the resultset.

	cycle : int, optional
		Cycle number of the resultset. It must refer to an existing cycle. If it is absent then resultsets will be created for all the existing cycles of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    time = 25
		    name = "Time 25"
		    new_resultsets = results.CreateResultsetTime(model_id, time, name)
		    for res in new_resultsets:
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


	"""

def CurrentResultset(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_current_resultset` instead.


	This function gets the current resultset of the given model.

	Parameters
	----------
	model_id : int
		Model id.

	Returns
	-------
	object
		Upon success, it returns an object of class Result referring to the current
		resultset of the model.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    res = results.CurrentResultset(model_id)
		    if res:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_current_resultset instead.", DeprecationWarning)

def CurrentResultsetOfWindow(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function gets the current resultset of the given model for a 3D window.

	Parameters
	----------
	model_id : int
		Model id.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns an object of class Result referring to the current resultset of the model.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def Cycles(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_cycles` instead.


	This function collects all cycles of a given model.

	Parameters
	----------
	model_id : int
		Model id.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to one cycle of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_cycles = results.Cycles(model_id)
		    for cycle in all_cycles:
		        print(cycle)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_cycles instead.", DeprecationWarning)

def DeformationLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the resultsets for all deformation labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one deformation label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        deform_labels = results.DeformationLabelsOfResultset(res)
		        for deform_res in deform_labels:
		            print(deform_res.cycle, deform_res.model_id)
		            print(
		                deform_res.name,
		                deform_res.nodal_data_name,
		                deform_res.function_data_name,
		                deform_res.vector_data_name,
		            )
		            print(deform_res.filename, deform_res.subcase, deform_res.state)
		            print(deform_res.step, deform_res.frequency, deform_res.time)
		            print(
		                deform_res.mode, deform_res.eigenvalue, deform_res.imaginary_eigenvalue
		            )
		            print(deform_res.loadstep, deform_res.generate_sequence)
		            print(
		                deform_res.nodal_data_label,
		                deform_res.function_data_label,
		                deform_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def DeformationTypes(filename: str, deck: str) -> object:

	"""

	This function finds the deformation types and the corresponding states for a certain file.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	Returns
	-------
	object
		It returns a list with the deformation types and the corresponding states as strings for the specified file.
		Each member of the list is another list containing in position 0 the deformation type as a string and in the rest positions the name of the states referring to this type.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadDeformations, results.LoadProjectDeformations

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/AbaqusEx7.odb"
		    deck = "ABAQUS"
		    all_types = results.DeformationTypes(filename, deck)
		    for one_type in all_types:
		        total = len(one_type)
		        deform_type = one_type[0]  # Deformation type
		        print(deform_type)
		        for k in range(total):
		            state = one_type[k]
		            print(state, k)  # One state of the above deformation type and its id
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeformationTypesAll(filename: str, deck: str, results_type: str) -> object:

	"""

	This function finds the deformation types, the states and the corresponding information for a file specified by its filename.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	object
		It returns a list with other lists as elements with information for deformation types and states of the specified file. Each member of the list is another list which contains:
		position 0 : String name of the type
		position 1 : List with states names  
		position 2 : List with states ids
		position 3 : List with name of functions
		position 4 : List with the type of the data
		position 5 : List with extra information
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadDeformations, results.LoadProjectDeformations

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/AbaqusEx7.odb"
		    deck = "ABAQUS"
		    all_types = results.DeformationTypesAll(filename, deck)
		    for deformation_type in all_types:
		        type = deformation_type[0]
		        print(type)  # Name of deformation type (e.g. "Displacements")
		        state_names = deformation_type[1]
		        for state_name in state_names:
		            print(state_name)  # Name of state
		        state_ids = deformation_type[2]
		        for state_id in state_ids:
		            print(state_id)  # Id of state
		        functions = deformation_type[3]
		        for one_function in functions:
		            print(one_function)  # Name of function
		        all_data = deformation_type[4]
		        for data in all_data:
		            print(data)  # Type of data
		        extra_info = deformation_type[5]
		        for extra in extra_info:
		            print(extra)  # Extra information
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeformationTypesList(filename: str, deck: str, expression_type: str, results_type: str) -> object:

	"""

	This function finds all the deformation types of a file specified by its filename. Deformation types are string expressions which can be used directly in commands and functions such as LoadDeformations and LoadProjectDeformations.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	expression_type : str, optional
		It controls the format of the output.
		- "read_results_expression": Output in appropriate format for read results commands (e.g. LoadDeformations) (default)
		- "labels_expression": Output in appropriate format for labels manipulation (e.g. ResultsetsByDeformationLabel)

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one deformation type of the specified file.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadDeformations, results.LoadProjectDeformations

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/AbaqusEx7.odb"
		    deck = "ABAQUS"
		    all_types = results.DeformationTypesList(filename, deck)
		    for deformation_type in all_types:
		        print(deformation_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeformationsListToDict(deforms: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Deformation.

	Parameters
	----------
	deforms : object
		Objects of class Deformation.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the node and member the corresponding Deformation object. If deformation with the same element id exist in the given list, then only the first deformation will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_deform = models.DeformationsOfModel(result)
		    iter_end = min(10, len(all_deform))
		    few_deform = all_deform[0:iter_end]
		    dict_deform = results.DeformationsListToDict(few_deform)
		    for id, deform in dict_deform.items():
		        print(id)  # Node Id
		        print(
		            deform.x, deform.y, deform.z, deform.total, deform.node_id
		        )  # X, Y, Z, Total Deformation, Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteCycle(model_id: int, cycle: int) -> int:

	"""

	This function deletes all resultsets of a given model for a specific cycle.

	Parameters
	----------
	model_id : int
		Id of the model.

	cycle : int
		Cycle number.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 1
		    ret = results.DeleteCycle(model_id, cycle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteResultset(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.delete` instead.


	This function deletes a given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    ret = results.DeleteResultset(res)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.delete instead.", DeprecationWarning)

def DisableAppendDeformations() -> int:

	"""

	This function disables the append deformations functionality.

	Returns
	-------
	int
		It always returns integer 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableAppendDeformations()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableAppendScalar() -> int:

	"""

	This function disables the append scalar functionality.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableAppendScalar()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableAppendVector() -> int:

	"""

	This function disables the append vector functionality.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableAppendVector()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableDefaultDeformationsLabel() -> int:

	"""

	This function disables the default naming option for labels of deformations.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableDefaultDeformationsLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableDefaultScalarLabel() -> int:

	"""

	This function disables the default naming option for labels of scalar results.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableDefaultScalarLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableDefaultVectorLabel() -> int:

	"""

	This function disables the default naming option for labels of vector results.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.DisableDefaultVectorLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableAppendDeformations() -> int:

	"""

	This function enables the append deformations functionality.

	Returns
	-------
	int
		It always returns integer 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableAppendDeformations()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableAppendScalar() -> int:

	"""

	This function enables the append scalar functionality.

	Returns
	-------
	int
		It always returns integer 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableAppendScalar()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableAppendVector() -> int:

	"""

	This function enables the append vector functionality.

	Returns
	-------
	int
		It always returns integer 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableAppendVector()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableDefaultDeformationsLabel() -> int:

	"""

	This function enables the default naming option for labels of deformations.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableDefaultDeformationsLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableDefaultScalarLabel() -> int:

	"""

	This function enables the default naming option for labels of scalar results.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableDefaultScalarLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EnableDefaultVectorLabel() -> int:

	"""

	This function enables the default naming option for labels of vector results.

	Returns
	-------
	int
		It always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    results.EnableDefaultVectorLabel()
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingCentroidScalar(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding centroid scalar values on an existing model for a specific resultset. It must be called after ending adding centroid scalar values on elements with functions 'AddCentroidScalarOnElement' and 'AddCentroidScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if centroid scalar values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for centroid scalar values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    value = 0.354
		
		    new_function_data_name = "Centroid Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartAddingCentroidScalar(
		        resultset, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    results.AddCentroidScalarOnElement(
		        resultset, element_type, element_id, second_id, value
		    )
		    results.EndAddingCentroidScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingCentroidVector(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding centroid vector values on an existing model for a specific resultset. It must be called after ending adding centroid vector values on elements with functions 'AddCentroidVectorOnElement' and 'AddCentroidVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if centroid vector values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for centroid vector values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    region_bounds = "parts"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    allelems = elements.Elements(model_id)
		    for e in allelems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(-0.885)
		        xvector.append(-0.6346)
		        yvector.append(0.25723)
		        zvector.append(-0.68315)
		    results.StartAddingCentroidVector(
		        resultset, new_function_data_name, layer, region_bounds
		    )
		    results.AddCentroidVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        values,
		        xvector,
		        yvector,
		        zvector,
		    )
		    results.EndAddingCentroidVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingCornerScalar(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding corner scalar values on an existing model for a specific resultset. It must be called after ending adding corner scalar values on elements with functions 'AddCornerScalarOnElement' and 'AddCornerScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if corner scalar values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for corner scalar values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		    results.StartAddingCornerScalar(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerScalarOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        layer,
		    )
		    results.EndAddingCornerScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingDeformations(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding values for deformations on an existing model for a specific resultset. It must be called after ending adding deformations on nodes with functions 'AddDeformationOnNode' and 'AddDeformationOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if deformation values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for deformation values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_nodal_data_name = "Deformations Data"
		
		    node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    visnodes = nodes.VisibleNodes(model_id)
		    for n in visnodes:
		        node_ids.append(n.id)
		        xdeform.append(0.025)
		        ydeform.append(-0.91)
		        zdeform.append(-1.398)
		    meta.results.StartAddingDeformations(resultset, new_nodal_data_name)
		    meta.results.AddDeformationOnSomeNodes(
		        resultset, node_ids, xdeform, ydeform, zdeform
		    )
		    meta.results.EndAddingDeformations(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingNodalScalar(resultset: object, cut_off: str, cut_off_limit: float) -> int:

	"""

	This function ends the procedure of adding nodal scalar values on an existing model for a specific resultset. It must be called after ending adding nodal scalar values on elements with functions 'AddNodalScalarOnElement' and 'AddNodalScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if nodal scalar values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : float, optional
		The cut-off limit for nodal scalar values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		
		    node_ids = list()
		    values = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(25, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.554)
		    results.StartAddingNodalScalar(resultset, new_function_data_name)
		    results.AddNodalScalarOnSomeNodes(resultset, node_ids, values)
		    results.EndAddingNodalScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingNodalVector(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding nodal vector values on an existing model for a specific resultset. It must be called after ending adding nodal vector values on elements with functions 'AddNodalVectorOnElement' and 'AddNodalVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if nodal vector values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for nodal vector values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    node_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(100, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.2)
		        xvector.append(0.682)
		        yvector.append(0.0)
		        zvector.append(0.7315)
		    results.StartAddingNodalVector(resultset, new_function_data_name)
		    results.AddNodalVectorOnSomeNodes(
		        resultset, node_ids, values, xvector, yvector, zvector
		    )
		    results.EndAddingNodalVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def FilterResultsets(cycle: int, filter: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_filtered_resultsets` instead.


	This function collects states (including generated) that match a specific filter for a model specified by the given model id.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    filtered_resultsets = results.FilterResultsets(model_id, filter)
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_filtered_resultsets instead.", DeprecationWarning)

def FilterResultsetsByDeformationLabel(cycle: int, deformation_label: str, filter: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_filtered_resultsets` instead.


	This function collects states (including generated) with a specific deformation label that match a specific filter for a model specified by the given model id.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	deformation_label : str
		Nodal data label.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resul referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    deformation_label = "Displacements"
		    filtered_resultsets = results.FilterResultsetsByDeformationLabel(
		        model_id, filter, deformation_label
		    )
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_filtered_resultsets instead.", DeprecationWarning)

def FilterResultsetsByFunctionLabel(cycle: int, filter: str, function_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_filtered_resultsets` instead.


	This function collects states (including generated) with a specific function label (scalar or vector) that match a specific filter for a model specified by the given model id.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	function_label : str
		Function data label (scalar or vector).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    function_label = "Stress components,Von Mises,Inner and Outer,Centroid"
		    filtered_resultsets = results.FilterResultsetsByFunctionLabel(
		        model_id, filter, function_label
		    )
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_filtered_resultsets instead.", DeprecationWarning)

def FilterResultsetsByScalarLabel(cycle: int, filter: str, scalar_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_filtered_resultsets` instead.


	This function collects states (including generated) with a specific scalar label that match a specific filter for a model specified by the given model id.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	scalar_label : str
		Scalar data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Centroid"
		    filtered_resultsets = results.FilterResultsetsByScalarLabel(
		        model_id, filter, scalar_label
		    )
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_filtered_resultsets instead.", DeprecationWarning)

def FilterResultsetsByVectorLabel(cycle: int, filter: str, vector_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_filtered_resultsets` instead.


	This function collects states (including generated) with a specific vector label that match a specific filter for a model specified by the given model id.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	vector_label : str
		Vector data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		    filtered_resultsets = results.FilterResultsetsByVectorLabel(
		        model_id, filter, vector_label
		    )
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_filtered_resultsets instead.", DeprecationWarning)

def FilterResultsetsOfWindow(model_id: int, window_name: str, filter: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function collects states (including generated) that match a specific filter for a model specified by the given model id for a specified window.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	filter : str
		Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. subcase==100 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filter = "subcase == 1"
		    window_name = "MetaPost"
		    filtered_resultsets = results.FilterResultsetsOfWindow(
		        model_id, window_name, filter
		    )
		    for res in filtered_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def FunctionLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the resultsets for all function labels (scalar or vector) for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one function label of the corresponding model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        function_labels = results.FunctionLabelsOfResultset(res)
		        for function_res in function_labels:
		            print(function_res.cycle, function_res.model_id)
		            print(
		                function_res.name,
		                function_res.nodal_data_name,
		                function_res.function_data_name,
		                function_res.vector_data_name,
		            )
		            print(function_res.filename, function_res.subcase, function_res.state)
		            print(function_res.step, function_res.frequency, function_res.time)
		            print(
		                function_res.mode,
		                function_res.eigenvalue,
		                function_res.imaginary_eigenvalue,
		            )
		            print(function_res.loadstep, function_res.generate_sequence)
		            print(
		                function_res.nodal_data_label,
		                function_res.function_data_label,
		                function_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GenerateResultsets(result: object, result_type: str, steps: int, type: str, angle: float) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.generate` instead.


	This function generates new resultsets from a given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	result_type : str
		Type of the data of the resultset.Its possible values are:
		- 'deform': deformation data
		- 'function': function data
		- 'all': deformation and function data

	steps : int
		Number of steps that will be generated.

	type : str
		Type of the interpolation. Its possible values are:
		- 'linear': linear
		- 'cos': cosine
		- 'sin': sine

	angle : float, optional
		Angle to fill. It should be specified only if type is 'cos' or 'sin'. If it is absent then the default value is 360.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one resultset of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    result_type = "all"
		    steps = 10
		    type = "cos"
		    angle = 330
		
		    generated_resultsets = results.GenerateResultsets(
		        res, result_type, steps, type, angle
		    )
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.generate instead.", DeprecationWarning)

def GeneratedResultsets(result: object, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the states that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	cycle : int
		Cycle of the resultset.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		
		    generated_resultsets = results.GeneratedResultsets(res)
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GeneratedResultsetsByDeformationLabel(result: object, deformation_label: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the states with a given deformation label that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	deformation_label : str
		Nodal data label.

	cycle : int, optional
		Cycle of the resultset. If it is absent, it finds the generated states for all cycles.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    deformation_label = "Displacements"
		
		    generated_resultsets = results.GeneratedResultsetsByDeformationLabel(
		        res, deformation_label
		    )
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GeneratedResultsetsByFunctionLabel(result: object, function_label: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the states with a given function label (scalar or vector) that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	function_label : str
		Function data label (scalar or vector).

	cycle : int, optional
		Cycle of the resultset. If it is absent, it finds the generated states for all cycles.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    generated_resultsets = results.GeneratedResultsetsByFunctionLabel(
		        res, function_label
		    )
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GeneratedResultsetsByScalarLabel(result: object, scalar_label: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the stateswith a given scalar label that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	scalar_label : str
		Scalar data label.

	cycle : int
		Cycle of the resultset. If it is absent, it finds the generated states for all cycles.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    generated_resultsets = results.GeneratedResultsetsByScalarLabel(res, scalar_label)
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GeneratedResultsetsByVectorLabel(result: object, vector_label: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the stateswith a given vector label that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	vector_label : str
		Vector data label.

	cycle : int
		Cycle of the resultset. If it is absent, it finds the generated states for all cycles.

	Returns
	-------
	object
		It returns a list where ech member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    vector_label = "Stresses,Major Principal,Max of Top Bottom"
		
		    generated_resultsets = results.GeneratedResultsetsByVectorLabel(res, vector_label)
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GeneratedResultsetsOfWindow(result: object, window_name: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the states for a given window that generated from the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	window_name : str
		Name of the window.

	cycle : int
		Cycle of the resultset. If it is absent, it finds the generated states for all cycles.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    window_name = "MetaPost"
		
		    generated_resultsets = results.GeneratedResultsetsOfWindow(res, window_name)
		    for res in generated_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GetResultsetFromDeformationLabel(result: object, deformation_label: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function gets the resultset with the given deformation label for the state specified by the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	deformation_label : str
		Nodal data label

	Returns
	-------
	object
		It returns an object of class Result referring to the resultset with the given deformation label.
		Else, None is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    deformation_label = "Displacements"
		
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        deform_res = results.GetResultsetFromDeformationLabel(res, deformation_label)
		        if deform_res:
		            print(deform_res.cycle, deform_res.model_id)
		            print(
		                deform_res.name,
		                deform_res.nodal_data_name,
		                deform_res.function_data_name,
		                deform_res.vector_data_name,
		            )
		            print(deform_res.filename, deform_res.subcase, deform_res.state)
		            print(deform_res.step, deform_res.frequency, deform_res.time)
		            print(
		                deform_res.mode, deform_res.eigenvalue, deform_res.imaginary_eigenvalue
		            )
		            print(deform_res.loadstep, deform_res.generate_sequence)
		            print(
		                deform_res.nodal_data_label,
		                deform_res.function_data_label,
		                deform_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GetResultsetFromFunctionLabel(result: object, function_label: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function gets the resultset with the given function label (scalar or vector) for the state specified by the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	function_label : str
		Function data label (scalar or vector).

	Returns
	-------
	object
		It returns an object of class Result referring to the resultset with the given function label.
		Else, None is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        function_res = results.GetResultsetFromFunctionLabel(res, function_label)
		        if function_res:
		            print(function_res.cycle, function_res.model_id)
		            print(
		                function_res.name,
		                function_res.nodal_data_name,
		                function_res.function_data_name,
		                function_res.vector_data_name,
		            )
		            print(function_res.filename, function_res.subcase, function_res.state)
		            print(function_res.step, function_res.frequency, function_res.time)
		            print(
		                function_res.mode,
		                function_res.eigenvalue,
		                function_res.imaginary_eigenvalue,
		            )
		            print(function_res.loadstep, function_res.generate_sequence)
		            print(
		                function_res.nodal_data_label,
		                function_res.function_data_label,
		                function_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GetResultsetFromScalarLabel(result: object, scalar_label: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function gets the resultset with the given scalar label for the state specified by the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	scalar_label : str
		Scalar data label.

	Returns
	-------
	object
		It returns an object of class Result referring to the resultset with the given scalar label.
		Else, None is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        scalar_res = results.GetResultsetFromScalarLabel(res, scalar_label)
		        if scalar_res:
		            print(scalar_res.cycle, scalar_res.model_id)
		            print(
		                scalar_res.name,
		                scalar_res.nodal_data_name,
		                scalar_res.function_data_name,
		                scalar_res.vector_data_name,
		            )
		            print(scalar_res.filename, scalar_res.subcase, scalar_res.state)
		            print(scalar_res.step, scalar_res.frequency, scalar_res.time)
		            print(
		                scalar_res.mode, scalar_res.eigenvalue, scalar_res.imaginary_eigenvalue
		            )
		            print(scalar_res.loadstep, scalar_res.generate_sequence)
		            print(
		                scalar_res.nodal_data_label,
		                scalar_res.function_data_label,
		                scalar_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def GetResultsetFromVectorLabel(result: object, vector_label: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function gets the resultset with the given vector label for the state specified by the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	vector_label : str
		Vector data label.

	Returns
	-------
	object
		It returns an object of class Result referring to the resultset with the given vector label.
		Else, None is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        vector_res = results.GetResultsetFromVectorLabel(res, vector_label)
		        if vector_res:
		            print(vector_res.cycle, vector_res.model_id)
		            print(
		                vector_res.name,
		                vector_res.nodal_data_name,
		                vector_res.function_data_name,
		                vector_res.vector_data_name,
		            )
		            print(vector_res.filename, vector_res.subcase, vector_res.state)
		            print(vector_res.step, vector_res.frequency, vector_res.time)
		            print(
		                vector_res.mode, vector_res.eigenvalue, vector_res.imaginary_eigenvalue
		            )
		            print(vector_res.loadstep, vector_res.generate_sequence)
		            print(
		                vector_res.nodal_data_label,
		                vector_res.function_data_label,
		                vector_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def IdOfResultset(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.Result.get_id` instead.


	This function finds the id of the given resultset. The result of this function can be used to change states via a META command.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns an integer referring to the id of the given resultset.
		Upon failure, a negative value is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		
		    resultset_id = results.IdOfResultset(res)
		    print(resultset_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.Result.get_id instead.", DeprecationWarning)

def IsCentroidScalar(centroid_scalar: object) -> int:

	"""

	This function checks whether an object is of class CentroidScalar.

	Parameters
	----------
	centroid_scalar : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class CentroidScalar, 0 otherwise.

	See Also
	--------
	results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "centroid_scalar")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsCentroidScalar(res):
		            centroid = res
		            print("This is an object of class CentroidScalar")
		            print(centroid.value)  # Centroid scalar value
		            print(
		                centroid.element_id, centroid.second_id, centroid.type
		            )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsCentroidVector(centroid_vector: object) -> int:

	"""

	This function checks whether an object is of class CentroidVector.

	Parameters
	----------
	centroid_vector : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class CentroidVector, 0 otherwise.

	See Also
	--------
	results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "centroid_vector")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsCentroidVector(res):
		            centroid = res
		            print("This is an object of class CentroidVector")
		            print(centroid.value)
		            print(centroid.x, centroid.y, centroid.z)
		            print(centroid.element_id, centroid.second_id, centroid.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsCornerScalar(corner_scalar: object) -> int:

	"""

	This function checks whether an object is of class CornerScalar.

	Parameters
	----------
	corner_scalar : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class CornerScalar, 0 otherwise.

	See Also
	--------
	results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "corner_scalar")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsCornerScalar(res):
		            corn = res
		            print("This is an object of class CornerScalar")
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

def IsDeformation(deformation: object) -> int:

	"""

	This function checks whether an object is of class Deformation.

	Parameters
	----------
	deformation : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Deformation, 0 otherwise.

	See Also
	--------
	results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "deformation")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsDeformation(res):
		            deform = res
		            print("This is an object of class Deformation")
		            print(deform.x, deform.y, deform.z, deform.total)  # X,Y,Z Total deformation
		            print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsModalDeformation(modal_deformation: object) -> int:

	"""

	This function checks whether an object is of class ModalDeformation.

	Parameters
	----------
	modal_deformation : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class ModalDeformation, 0 otherwise.

	See Also
	--------
	results.ModalDeformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/NastranEx3.op2"
		    deck = "NASTRAN"
		    states = utils.RangeToList("1-10")
		    data = "Displacements,Translational"
		    node_ids = utils.RangeToList("1-100")
		    complex = "real"
		
		    all_states = results.LoadModalDeformations(
		        model_id, filename, deck, states, data, node_ids, complex
		    )
		    for one_state in all_states:
		        state_id = one_state[0]
		        print(state_id)  # Id of state
		
		        state_name = one_state[1]
		        print(state_name)  # Name of state
		
		        all_deform = one_state[2]  # List with modal deformations
		        for res in all_deform:
		            if results.IsModalDeformation(res):
		                modal_deform = res
		                print(
		                    modal_deform.x, modal_deform.y, modal_deform.z
		                )  # X,Y,Z deformation
		                print(
		                    modal_deform.rx, modal_deform.ry, modal_deform.rz
		                )  # X,Y,Z Rotational deformation
		                print(modal_deform.node_id)  # Node id
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsNodalScalar(nodal_scalar: object) -> int:

	"""

	This function checks whether an object is of class NodalScalar.

	Parameters
	----------
	nodal_scalar : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class NodalScalar, 0 otherwise.

	See Also
	--------
	results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "nodal_scalar")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsNodalScalar(res):
		            nodal = res
		            print("This is an object of class NodalScalar")
		            print(nodal.value)  # Nodal scalar value
		            print(nodal.node_id)  # Id of the node
		            print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsNodalVector(nodal_vector: object) -> int:

	"""

	This function checks whether an object is of class NodalVector.

	Parameters
	----------
	nodal_vector : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class NodalVector, 0 otherwise.

	See Also
	--------
	NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "nodal_vector")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsNodalVector(res):
		            nodal = res
		            print("This is an object of class NodalVector")
		            print(nodal.value)  # Nodal vector value
		            print(
		                nodal.x, nodal.y, nodal.z
		            )  # Normalized coordinates (X, Y, Z) of the nodal vector
		            print(nodal.node_id)  # Id of the node
		            print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsResultset(result: object) -> int:

	"""

	This function checks whether an object is of class Resultset.

	Parameters
	----------
	result : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Resultset, 0 otherwise.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		from meta import models
		
		
		def main():
		    models.CollectNewEntitiesStart()
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    all_entities = models.CollectNewEntitiesEnd()
		    for ent in all_entities:
		        if results.IsResultset(ent):
		            res = ent
		            print(res.cycle, res.model_id)
		            print(
		                res.name,
		                res.nodal_data_name,
		                res.function_data_name,
		                res.vector_data_name,
		            )
		            print(res.filename, res.subcase, res.state)
		            print(res.step, res.frequency, res.time)
		            print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		            print(res.loadstep, res.generate_sequence)
		            print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LayersOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.Result.get_layers` instead.


	This function finds the layers of a given resultset of the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with the names of the layers of the given resultset. Layers refer to the layers of the SHELL elements for which scalar or vector values are loaded (e.g. 'bottom', 'top', 'one').
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		    all_layers = results.LayersOfResultset(res)
		    for layer in all_layers:
		        print(layer)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.Result.get_layers instead.", DeprecationWarning)

def LoadAppendDeformations(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads and appends deformations in an existing model from a file specified by its filename.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Displacements"
		    new_resultsets = results.LoadAppendDeformations(
		        model_id, filename, deck, states, data
		    )
		    for res in new_resultsets:
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


	"""

def LoadAppendProjectDeformations(data: str, filename: str, states: str, model_id: int) -> object:

	"""

	This function loads and appends deformations in an existing model from a project file (.metadb).

	Parameters
	----------
	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Displacements"
		    new_resultsets = results.LoadAppendProjectDeformations(
		        model_id, filename, states, data
		    )
		    for res in new_resultsets:
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


	"""

def LoadAppendProjectScalar(model_id: int, filename: str, states: str, data: str) -> object:

	"""

	This function loads and appends scalar values in an existing model from a project file (.metadb)

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Stresscomponents,MajorPrincipal,InnerandOuter"
		    new_resultsets = results.LoadAppendProjectScalar(model_id, filename, states, data)
		    for res in new_resultsets:
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


	"""

def LoadAppendProjectVector(model_id: int, filename: str, states: str, data: str) -> object:

	"""

	This function loads and append vector values in an existing model from a project file (.metadb).

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Stresscomponents,MajorPrincipal,InnerandOuter"
		    new_resultsets = results.LoadAppendProjectVector(model_id, filename, states, data)
		    for res in new_resultsets:
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


	"""

def LoadAppendScalar(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads and appends scalar values in an existing model.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Stress components,Von Mises,Inner and Outer,Centroid"
		    new_resultsets = results.LoadAppendScalar(model_id, filename, deck, states, data)
		    for res in new_resultsets:
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


	"""

def LoadAppendScalarGetCoordSystems(model_id: int, filename: str, deck: str, state_id: int, data: str, failed_elements: str) -> object:

	"""

	This function loads and appends scalar values in an existing model from a file specified by its filename and gets the coordinate systems of the elements.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	state_id : int
		Id of the state to read.

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	Returns
	-------
	object
		It returns a list with the new resultsets and the coordinate systems of the elements of the specified model.
		In position 0, list contains an object of class Result referring to the newly created state.
		In position 1, list contains a list with objects of class ElementCoordSystem referring to the coordinate system of the element for the corresponding newly created resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, ElementCoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Ansys.rst"
		    deck = "ANSYS"
		    state_id = 1
		    data = "Stresses,Normal-X(GCS),TopandBottom,Centroid"
		    all_data = results.LoadAppendScalarGetCoordSystems(
		        model_id, filename, deck, state_id, data
		    )
		    if len(all_data) == 2:
		        res = all_data[0]  # Struct of type resultset
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		        all_coords = all_data[1]  # List with object of class ElemCoordSystem
		        for ecs in all_coords:
		            print(ecs.id, ecs.second_id, ecs.type, ecs.model_id)
		            print(ecs.origin[0], ecs.origin[1], ecs.origin[2])  # Origin
		            print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		            print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		            print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadAppendVector(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads and append vector values in an existing model from a file specified by its filename.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Stress components,Major Principal,Inner Surface"
		    new_resultsets = results.LoadAppendVector(model_id, filename, deck, states, data)
		    for res in new_resultsets:
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


	"""

def LoadAppendVectorGetCoordSystems(model_id: int, filename: str, deck: str, state_id: int, data: str, failed_elements: str) -> object:

	"""

	This function loads and appends vector values in an existing model from a file.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	state_id : int
		Id of the state to read.

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	Returns
	-------
	object
		It returns a list with the new resultsets and the coordinate systems of the elements of the specified model.
		In position 0, list contains an object  of class Resultset referring to the newly created state.
		In position 1, list contains a list with objects of class ElementCoordSystem referring to the coordinate system of the element for the corresponding newly created resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, coordsystems.ElementCoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Ansys.rst"
		    deck = "ANSYS"
		    state_id = 1
		    data = "Stresses,First Principal,Top"
		    all_data = results.LoadAppendVectorGetCoordSystems(
		        model_id, filename, deck, state_id, data
		    )
		    if len(all_data) == 2:
		        res = all_data[0]  # Struct of type resultset
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		        all_coords = all_data[1]  # List with object of class ElemCoordSystem
		        for ecs in all_coords:
		            print(ecs.id, ecs.second_id, ecs.type, ecs.model_id)
		            print(ecs.origin[0], ecs.origin[1], ecs.origin[2])  # Origin
		            print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		            print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		            print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadDeformations(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads deformations in an existing model from a file.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Displacements"
		    new_resultsets = results.LoadDeformations(model_id, filename, deck, states, data)
		    for res in new_resultsets:
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


	"""

def LoadModalDeformations(model_id: int, filename: str, deck: str, states: object, data: str, node_ids: object, complex: str) -> object:

	"""

	This function loads modal deformations on some nodes from a file.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : object
		List with Ids of states to read.

	data : str
		String expression for data to be loaded (e.g. 'Displacements', 'Eigenvalues').

	node_ids : object
		List with Ids of some specific nodes.

	complex : str
		Defines whether real or imaginary will be loaded.

	Returns
	-------
	object
		It returns a list with the states and the corresponding deformation values for the specified file. Each member of the list is another list which contains:
		- position 0: Id of the state
		- position 1: Name of the state
		- position 2: List with ModalDeformation objects 
		Upon failure, an empty list is returned.

	See Also
	--------
	results.DeformationTypes, results.ModalDeformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/NastranEx3.op2"
		    deck = "NASTRAN"
		    states = utils.RangeToList("1-10")
		    data = "Displacements,Translational"
		    node_ids = utils.RangeToList("1-100")
		    complex = "real"
		
		    all_states = results.LoadModalDeformations(
		        model_id, filename, deck, states, data, node_ids, complex
		    )
		    for one_state in all_states:
		        state_id = one_state[0]
		        print(state_id)  # Id of state
		
		        state_name = one_state[1]
		        print(state_name)  # Name of state
		
		        all_deform = one_state[2]  # List with modal deformations
		        for res in all_deform:
		            if results.IsModalDeformation(res):
		                modal_deform = res
		                print(
		                    modal_deform.x, modal_deform.y, modal_deform.z
		                )  # X,Y,Z deformation
		                print(
		                    modal_deform.rx, modal_deform.ry, modal_deform.rz
		                )  # X,Y,Z Rotational deformation
		                print(modal_deform.node_id)  # Node id
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadProjectDeformations(model_id: int, filename: str, states: str, data: str) -> object:

	"""

	This function loads deformations in an existing model from a project file (.metadb).

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Displacements"
		    new_resultsets = results.LoadProjectDeformations(model_id, filename, states, data)
		    for res in new_resultsets:
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


	"""

def LoadProjectScalar(model_id: int, filename: str, states: str, data: str) -> object:

	"""

	This function loads scalar values in an existing model from a project file (.metadb).

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Stresscomponents,MajorPrincipal,InnerandOuter"
		    new_resultsets = results.LoadProjectScalar(model_id, filename, states, data)
		    for res in new_resultsets:
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


	"""

def LoadProjectVector(model_id: int, filename: str, states: str, data: str) -> object:

	"""

	This function loads vector values in an existing model from a project file (.metadb).

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the project file.

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase'). If data is not a valid expression, default data will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.metadb"
		    states = "all"
		    data = "label:0:Stresscomponents,MajorPrincipal,InnerandOuter"
		    new_resultsets = results.LoadProjectVector(model_id, filename, states, data)
		    for res in new_resultsets:
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


	"""

def LoadScalar(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads scalar values in an existing model from a file specified by its filename.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Stress components,Von Mises,Inner and Outer,Centroid"
		    new_resultsets = results.LoadScalar(model_id, filename, deck, states, data)
		    for res in new_resultsets:
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


	"""

def LoadScalarGetCoordSystems(model_id: int, filename: str, deck: str, state_id: int, data: str, failed_elements: str) -> object:

	"""

	This function loads scalar values in an existing model from a file specified by its filename and gets the coordinate systems of the elements.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	state_id : int
		Id of the state to read.

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	Returns
	-------
	object
		It returns a list with the new resultsets and the coordinate systems of the elements of the specified model.
		In position 0, list contains an object  of class Result referring to the newly created state.
		In position 1, list contains a list with objects of class ElementCoordSystem referring to the coordinate system of the element for the corresponding newly created resultset. 
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, ElementCoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Ansys.rst"
		    deck = "ANSYS"
		    state_id = 1
		    data = "Stresses, Normal-X(GCS), Top and Bottom, Centroid"
		    all_data = results.LoadScalarGetCoordSystems(
		        model_id, filename, deck, state_id, data
		    )
		    if len(all_data) == 2:
		        res = all_data[0]  # Struct of type resultset
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		        all_coords = all_data[1]  # List with object of class ElemCoordSystem
		        for ecs in all_coords:
		            print(ecs.id, ecs.second_id, ecs.type, ecs.model_id)
		            print(ecs.origin[0], ecs.origin[1], ecs.origin[2])  # Origin
		            print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		            print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		            print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadVector(model_id: int, filename: str, deck: str, states: str, data: str, failed_elements: str, ignore_label_settings: bool) -> object:

	"""

	This function loads vector values in an existing model from a file.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	states : str
		Filtering expression for states to read (e.g. 'all', '1-3,10,25-29').

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	ignore_label_settings : bool, optional
		Defined whether the script function will ignore the current settings for new label name. Possible values are:
		- True : Ignores the current settings and set explicitly default option for label names to true
		- False : Use the current settings for label names

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly loaded state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Abaqus.odb"
		    deck = "ABAQUS"
		    states = "all"
		    data = "Stress components,Major Principal,Inner Surface"
		    new_resultsets = results.LoadVector(model_id, filename, deck, states, data)
		    for res in new_resultsets:
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


	"""

def LoadVectorGetCoordSystems(model_id: int, filename: str, deck: str, state_id: int, data: str, failed_elements: str) -> object:

	"""

	This function loads vector values in an existing model from a file and gets the coordinate systems of the elements.

	Parameters
	----------
	model_id : int
		Id of the model.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	state_id : int
		Id of the state to read.

	data : str
		Expression for data to be loaded (e.g. 'Equivalent plastic strain , Corner', 'Point loads, Magnitude', 'Acoustic Results: AllCycles, Pressure, Phase').

	failed_elements : str
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : failed elements are loaded (default)
		- 'nofailed' : failed elements are not loaded

	Returns
	-------
	object
		It returns a list with the new resultsets and the coordinate systems of the elements of the specified model.
		In position 0, list contains an object  of class Result referring to the newly created state.
		In position 1, list contains a list with objects of class ElementCoordSystem referring to the coordinate system of the element for the corresponding newly created resultset. 
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, coordsystems.ElementCoordSystem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/Ansys.rst"
		    deck = "ANSYS"
		    state_id = 1
		    data = "Stresses,First Principal,Top"
		    all_data = results.LoadVectorGetCoordSystems(
		        model_id, filename, deck, state_id, data
		    )
		    if len(all_data) == 2:
		        res = all_data[0]  # Struct of type resultset
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		
		        all_coords = all_data[1]  # List with object of class ElementCoordSystem
		        for ecs in all_coords:
		            print(ecs.id, ecs.second_id, ecs.type, ecs.model_id)
		            print(ecs.origin[0], ecs.origin[1], ecs.origin[2])  # Origin
		            print(ecs.xaxis[0], ecs.xaxis[1], ecs.xaxis[2])  # X-axis
		            print(ecs.yaxis[0], ecs.yaxis[1], ecs.yaxis[2])  # Y-axis
		            print(ecs.zaxis[0], ecs.zaxis[1], ecs.zaxis[2])  # Z-axis
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodalScalarListToDict(nodal_scalars: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class NodalScalar.

	Parameters
	----------
	nodal_scalars : object
		List with objects of class NodalScalar.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the node and member the corresponding NodalScalar object.
		If a NodalScalar object with the same element id exists in the given list, then only the first NodalScalar will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_nodal = models.NodalScalarOfModel(result)  # List with NodalScalar objects
		    fewer_nodal = all_nodal[
		        0 : min(10, len(all_nodal))
		    ]  # List with fewer nodal objects for quicker printing
		    dict_nodal = results.NodalScalarListToDict(fewer_nodal)
		    for id, nodal in dict_nodal.items():
		        print(id)  # Node Id
		        print(nodal.value)  # Nodal scalar value
		        print(
		            nodal.node_id, nodal.part_id
		        )  # Id of the node, Id of the part (-1 if no part exists)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodalVectorListToDict(nodal_vectors: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class NodalVector.

	Parameters
	----------
	nodal_vectors : object
		List with objects of class NodalVector.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the node and member the corresponding NodalVector object.
		If a NodalVector object with the same element id exists in the given list, then only the first NodalVector will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_nodal = models.NodalVectorOfModel(result)  # List with NodalVector objects
		    fewer_nodal = all_nodal[
		        0 : min(10, len(all_nodal))
		    ]  # List with fewer nodal objects for quicker printing
		    dict_nodal = results.NodalVectorListToDict(fewer_nodal)
		    for id, nodal in dict_nodal.items():
		        print(id)  # Node Id
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(
		            nodal.node_id, nodal.part_id
		        )  # Id of the node, Id of the part (-1 if no part exists)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PickCycles(message: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_cycles` instead.


	This function allows the user to select cycles of a model from a given list. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	message : str
		Message displayed to the user.

	model_id : int
		Model id.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to one specific selected cycle of the given model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    message = "Select Cycles and press OK when you are ready"
		    picked_cycles = results.PickCycles(model_id, message)
		    for cycle in picked_cycles:
		        print(cycle)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_cycles instead.", DeprecationWarning)

def PickResultsets(message: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	message : str
		Message displayed to the user.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsets(model_id, message)
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def PickResultsetsByCycle(cycle: int, message: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) with a given cycle from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	cycle : int
		Cycle number.

	message : str
		Message displayed to the user.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset of the given model(s) for the specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsetsByCycle(model_id, cycle, message)
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def PickResultsetsByDeformationLabel(deformation_label: str, message: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) with a specific deformation label from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	deformation_label : str
		Nodal data label.

	message : str
		Message displayed to the user.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset with the given deformation label of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    deformation_label = "Displacements"
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsetsByDeformationLabel(
		        model_id, deformation_label, message
		    )
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def PickResultsetsByFunctionLabel(function_label: str, message: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) with a specific function label (scalar or vector) from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	function_label : str
		Function data label (scalar or vector).

	message : str
		Message displayed to the user.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset with the given function label of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsetsByFunctionLabel(
		        model_id, function_label, message
		    )
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def PickResultsetsByScalarLabel(message: str, scalar_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) with a specific scalar label from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	message : str
		Message displayed to the user.

	scalar_label : str
		Scalar data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset with the given scalar label of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsetsByScalarLabel(
		        model_id, scalar_label, message
		    )
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def PickResultsetsByVectorLabel(model_id: int, vector_label: str, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_resultsets` instead.


	This function allows the user to select resultsets of model(s) with a specific vector label from a given list. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart after the selection of the resultsets from the list.

	Parameters
	----------
	model_id : int
		Id of the model.

	vector_label : str
		Vector data label.

	message : str
		Message displayed to the user.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one specific selected resultset with the given scalar label of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		    message = "Select Resultsets and press OK when you are ready"
		    picked_resultsets = results.PickResultsetsByVectorLabel(
		        model_id, vector_label, message
		    )
		    for res in picked_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_resultsets instead.", DeprecationWarning)

def ReportNewResultsets() -> object:

	"""

	This function collects the newly created resultsets from the last call of script function CollectNewResultsetsStart(). This function should be preceded by a corresponding call to script function CollectNewResultsetsStart() and should be followed by a corresponding call to script function CollectNewResultsetsEnd().

	Returns
	-------
	object
		It returns a listwhere each member of the list is an object of class Result referring to one specific newly created resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import utils
		
		
		def main():
		    results.CollectNewResultsetsStart()
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.ReportNewResultsets()
		    for res in new_resultsets:
		        print(res.cycle, res.model_id)
		        print(
		            res.name, res.nodal_data_name, res.function_data_name, res.vector_data_name
		        )
		        print(res.filename, res.subcase, res.state)
		        print(res.step, res.frequency, res.time)
		        print(res.mode, res.eigenvalue, res.imaginary_eigenvalue)
		        print(res.loadstep, res.generate_sequence)
		        print(res.nodal_data_label, res.function_data_label, res.vector_data_label)
		    print("####################################################")
		
		    # create new resultsets
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.op2")
		    utils.MetaCommand(
		        "read dis Nastran /home/examples/NastranEx2.op2 all Displacements,Translational"
		    )
		
		    new_resultsets = results.CollectNewResultsetsEnd()
		    for res in new_resultsets:
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


	"""

def ResultsetGenerator(result: object, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the state that generated the given resultset. 

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	cycle : int, optional
		Cycle of the resultset.If it is absent, it finds the generator for all cycles.

	Returns
	-------
	object
		It returns a list with the Result object of the generator of the given resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[8]
		
		    generators = results.ResultsetGenerator(result)
		    for res in generators:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def Resultsets(model_id: int, exclude_generated: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects all states (including original and generated states) for all cycles of a model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	exclude_generated : int, optional
		1 to exclude generated states, 0 to include generated states. If it is absent then this function will include generated states in the output.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByCycle(cycle: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given cycle for a specified model.

	Parameters
	----------
	cycle : int
		Cycle number.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    collected_resultsets = results.ResultsetsByCycle(model_id, cycle)
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByCycleAndDeformationLabel(cycle: int, deformation_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given cycle and deformation label for a specified model.

	Parameters
	----------
	cycle : int
		Cycle number.

	deformation_label : str
		Nodal data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    deformation_label = "Displacements"
		    collected_resultsets = results.ResultsetsByCycleAndDeformationLabel(
		        model_id, cycle, deformation_label
		    )
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByCycleAndFunctionLabel(cycle: int, function_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given cycle and function label (scalar or vector) for a specified model.

	Parameters
	----------
	cycle : int
		Cycle number.

	function_label : str
		Function data label (scalar or vector).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		    collected_resultsets = results.ResultsetsByCycleAndFunctionLabel(
		        model_id, cycle, function_label
		    )
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByCycleAndScalarLabel(cycle: int, scalar_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given cycle and scalar label for a specified model.

	Parameters
	----------
	cycle : int
		Cycle number.

	scalar_label : str
		Scalar data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		    collected_resultsets = results.ResultsetsByCycleAndScalarLabel(
		        model_id, cycle, scalar_label
		    )
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByCycleAndVectorLabel(cycle: int, vector_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given cycle and vector label for a specified model.

	Parameters
	----------
	cycle : int
		Cycle number.

	vector_label : str
		Vector data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle = 0
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		    collected_resultsets = results.ResultsetsByCycleAndVectorLabel(
		        model_id, cycle, vector_label
		    )
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByDeformationLabel(deformation_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects all states (including original and generated states) with a specific deformation label for all cycles of a given model.

	Parameters
	----------
	deformation_label : str
		Nodal data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    deformation_label = "Displacements"
		
		    all_resultsets = results.ResultsetsByDeformationLabel(model_id, deformation_label)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByFunctionLabel(function_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects all states (including original and generated states) with a specific function label (scalar or vector) for all cycles of a given model.

	Parameters
	----------
	function_label : str
		Function data label (scalar or vector).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    all_resultsets = results.ResultsetsByFunctionLabel(model_id, function_label)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsById(cycle: int, resultset_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id for a given model.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	resultset_id : int
		Id of the state.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    resultset_id = 1
		
		    selected_resultsets = results.ResultsetsById(model_id, resultset_id)
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByIdAndDeformationLabel(cycle: int, deformation_label: str, resultset_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id and a given deformation label for a specific model.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	deformation_label : str
		Nodal data label.

	resultset_id : int
		Id of the state.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    resultset_id = 2
		    deformation_label = "Displacements"
		
		    selected_resultsets = results.ResultsetsByIdAndDeformationLabel(
		        model_id, resultset_id, deformation_label
		    )
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByIdAndFunctionLabel(cycle: int, function_label: str, resultset_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id and a given function label (scalar or vector) for a given model.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	function_label : str
		Function data label (scalar or vector).

	resultset_id : int
		Id of the state.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    resultset_id = 1
		    function_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    selected_resultsets = results.ResultsetsByIdAndFunctionLabel(
		        model_id, resultset_id, function_label
		    )
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByIdAndScalarLabel(cycle: int, resultset_id: int, scalar_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id and a given scalar label for a given model.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	resultset_id : int
		Id of the state.

	scalar_label : str
		Scalar data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    resultset_id = 1
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    selected_resultsets = results.ResultsetsByIdAndScalarLabel(
		        model_id, resultset_id, scalar_label
		    )
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByIdAndVectorLabel(cycle: int, resultset_id: int, vector_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id and a given vector label for a specified model.

	Parameters
	----------
	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	resultset_id : int
		Id of the state.

	vector_label : str
		Vector data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    resultset_id = 1
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		
		    selected_resultsets = results.ResultsetsByIdAndVectorLabel(
		        model_id, resultset_id, vector_label
		    )
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByScalarLabel(scalar_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects all states (including original and generated states) with a specific scalar label for all cycles of a given model.

	Parameters
	----------
	scalar_label : str
		Scalar data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    scalar_label = "Stress components,Von Mises,Inner and Outer,Corner"
		
		    selected_resultsets = results.ResultsetsByScalarLabel(model_id, scalar_label)
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsByVectorLabel(vector_label: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_resultsets` instead.


	This function collects all states (including original and generated states) with a specific vector label for all cycles of a specific model.

	Parameters
	----------
	vector_label : str
		Vector data label.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    vector_label = "Stress components,Major Principal,Inner and Outer"
		
		    selected_resultsets = results.ResultsetsByVectorLabel(model_id, vector_label)
		    for res in selected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_resultsets instead.", DeprecationWarning)

def ResultsetsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_resultsets` instead.


	This function searches for the resultsets of an overlay run with a given type and id.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one resultset of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_resultsets = results.ResultsetsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for res in overlay_run_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_resultsets instead.", DeprecationWarning)

def ResultsetsOfWindow(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function collects all states (including original and generated states) for all cycles of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		
		    all_resultsets = results.ResultsetsOfWindow(model_id, window_name)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def ResultsetsOfWindowByCycle(model_id: int, window_name: str, cycle: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function collects states (including generated) with a given cycle for a model specified by the given model id for a given window.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	cycle : int
		Cycle of the resultset.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    cycle = 0
		    collected_resultsets = results.ResultsetsOfWindowByCycle(
		        model_id, window_name, cycle
		    )
		    for res in collected_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def ResultsetsOfWindowById(model_id: int, window_name: str, resultset_id: int, cycle: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function collects states (including generated) with a given resultset id for a specified model for a given window.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	resultset_id : int
		Id of the state.

	cycle : int
		Cycle of the resultset. If it is absent, it collects states for all cycles.

	Returns
	-------
	int
		It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    resultset_id = 1
		
		    all_resultsets = results.ResultsetsOfWindowById(model_id, window_name, resultset_id)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def ScalarLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the resultsets for all scalar labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one scalar label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        scalar_labels = results.ScalarLabelsOfResultset(res)
		        for scalar_res in scalar_labels:
		            print(scalar_res.cycle, scalar_res.model_id)
		            print(
		                scalar_res.name,
		                scalar_res.nodal_data_name,
		                scalar_res.function_data_name,
		                scalar_res.vector_data_name,
		            )
		            print(scalar_res.filename, scalar_res.subcase, scalar_res.state)
		            print(scalar_res.step, scalar_res.frequency, scalar_res.time)
		            print(
		                scalar_res.mode, scalar_res.eigenvalue, scalar_res.imaginary_eigenvalue
		            )
		            print(scalar_res.loadstep, scalar_res.generate_sequence)
		            print(
		                scalar_res.nodal_data_label,
		                scalar_res.function_data_label,
		                scalar_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def ScalarTypes(filename: str, deck: str) -> object:

	"""

	This function finds the scalar types and the corresponding states for a file.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	Returns
	-------
	object
		It returns a list where each member of the list is another list containing in position 0 the scalar type as a string and in the rest positions the names of the states referring to this type.
		Scalar types are string expressions (e.g. 'Stresses', 'Strains', 'Accelerations:All Cycles', 'Displacements:Cycle 1').
		States are also string expressions with the first characters referring to the id of the state (e.g '5 STATE 5 ,TIME 4.00000000E+00'). State id can also be retrieved from the position of the state in the list.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadScalar, results.LoadProjectScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.ScalarTypes(filename, deck)
		    for one_type in all_types:
		        total = len(one_type)
		        scalar_type = one_type[0]  # scalar type
		        print(scalar_type)
		        for k in range(total):
		            state = one_type[k]
		            print(state, k)  # One state of the above scalar types and its id
		
		
		if __name__ == "__main__":
		    main()


	"""

def ScalarTypesAll(filename: str, deck: str, results_type: str) -> object:

	"""

	This function finds all the scalar types, the states and the corresponding information for a file.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	object
		It returns a list with other lists as members with information for scalar types and states of the specified file. Each member of the list is another list which contains:
		position 0 : String name of the type
		position 1 : List with states names  
		position 2 : List with states ids
		position 3 : List with name of functions
		position 4 : List with the type of the data
		position 5 : List with extra information
		Upon failure, an empty lst is returned.

	See Also
	--------
	results.LoadScalar, results.LoadProjectScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.ScalarTypesAll(filename, deck)
		    for scalar_type in all_types:
		        type = scalar_type[0]
		        print(type)  # Name of scalar type (e.g. "Stresses")
		        state_names = scalar_type[1]
		        for state_name in state_names:
		            print(state_name)  # Name of state
		        state_ids = scalar_type[2]
		        for state_id in state_ids:
		            print(state_id)  # Id of state
		        functions = scalar_type[3]
		        for one_function in functions:
		            print(one_function)  # Name of function
		        all_data = scalar_type[4]
		        for data in all_data:
		            print(data)  # Type of data
		        extra_info = scalar_type[5]
		        for extra in extra_info:
		            print(extra)  # Extra information
		
		
		if __name__ == "__main__":
		    main()


	"""

def ScalarTypesList(filename: str, deck: str, expression_type: str, results_type: str) -> object:

	"""

	This function finds all the scalar types of a results file.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	expression_type : str, optional
		It controls the format of the output.
		- "read_results_expression": Output in appropriate format for read results commands (e.g. LoadScalar) (default)
		- "labels_expression": Output in appropriate format for labels manipulation (e.g. ResultsetsByScalarLabel)

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	object
		It returns a list with strings as elements referring to the scalar types of the specified file.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadScalar, results.LoadProjectScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.ScalarTypesList(filename, deck)
		    for scalar_type in all_types:
		        print(scalar_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetCurrentResultset(model_id: int, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_current_resultset` instead.


	This function sets the current resultset of a given model.

	Parameters
	----------
	model_id : int
		Model id.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    ret = results.SetCurrentResultset(model_id, result)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_current_resultset instead.", DeprecationWarning)

def SetCurrentResultsetOfWindow(model_id: int, window_name: str, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_current_resultset` instead.


	This function sets the current resultset of a given model for a specific 3D window.

	Parameters
	----------
	model_id : int
		Model id.

	window_name : str
		Name of window.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    ret = results.SetCurrentResultsetOfWindow(model_id, window_name, result)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_current_resultset instead.", DeprecationWarning)

def SetDeformationsLabel(user_label: str) -> int:

	"""

	This function sets the user defined text for labels of deformations to be loaded. This function should be used after the function 'DisableDefaultDeformationsLabel' and before loading deformation results.

	Parameters
	----------
	user_label : str
		User defined label.

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	results.DisableDefaultDeformationsLabel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    user_label = "Deformations on tail"
		    results.SetDeformationsLabel(user_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetScalarLabel(user_label: str) -> int:

	"""

	This function sets the user defined text for scalar labels to be loaded. This function should be used after the function 'DisableDefaultScalarLabel' and before loading scalar results.

	Parameters
	----------
	user_label : str
		User defined label.

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	results.DisableDefaultScalarLabel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    user_label = "Scalar"
		    results.SetScalarLabel(user_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetVectorLabel(user_label: str) -> int:

	"""

	This function sets the user defined text for vector labels to be loaded. This function should be used after the function 'DisableDefaultVectorLabel' and before loading vector results.

	Parameters
	----------
	user_label : str
		User defined label.

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	results.DisableDefaultVectorLabel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    user_label = "Vector"
		    results.SetVectorLabel(user_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingCentroidScalar(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of adding centroid scalar values on an existing model for a specific resultset. This function will reset all the centroid scalar values of the resultset to zero. It must be called before starting adding centroid scalar values on elements using functions 'AddCentroidScalarOnElement' and 'AddCentroidScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom centroid scalar values. Possible values are:
		- 'one_value': One centroid scalar value
		- 'top_and_bot': Top and bottom centroid scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the centroid scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    value = 0.354
		
		    new_function_data_name = "Centroid Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartAddingCentroidScalar(
		        resultset, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    results.AddCentroidScalarOnElement(
		        resultset, element_type, element_id, second_id, value
		    )
		    results.EndAddingCentroidScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingCentroidVector(resultset: object, new_function_data_name: str, layer: str, region_bounds: str, vector_display_type: str, use_default_postfix: int, triple_vector: int) -> int:

	"""

	This function starts the procedure of adding centroid vector values on an existing model for a specific resultset. This function will reset all the centroid vector values of the resultset to zero. It must be called before starting adding centroid vector values on elements using functions 'AddCentroidVectorOnElement' and 'AddCentroidVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom centroid vector values. Possible values are:
		- 'one_value': One centroid vector value
		- 'top_and_bot': Top and bottom centroid vector values

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal vector values for all parts they belong to
		- 'parts': Nodes will have one nodal vector value for each part they belong to
		- 'default': Default GUI selection

	vector_display_type : str, optional
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	triple_vector : int, optional
		Set to 1, only when going to add triple vector. The default value is 0

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    region_bounds = "parts"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    allelems = elements.Elements(model_id)
		    for e in allelems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(-0.885)
		        xvector.append(-0.6346)
		        yvector.append(0.25723)
		        zvector.append(-0.68315)
		    results.StartAddingCentroidVector(
		        resultset, new_function_data_name, layer, region_bounds
		    )
		    results.AddCentroidVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        values,
		        xvector,
		        yvector,
		        zvector,
		    )
		    results.EndAddingCentroidVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingCornerScalar(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, centroid_calc: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of adding corner scalar values on an existing model for a specific resultset. This function will reset all the corner scalar values of the resultset to zero. It must be called before starting adding corner scalar values on elements using functions 'AddCornerScalarOnElement' and 'AddCornerScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom corner scalar values. Possible values are:
		- 'one_value': One corner scalar value
		- 'top_and_bot': Top and bottom corner scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		    results.StartAddingCornerScalar(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerScalarOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        layer,
		    )
		    results.EndAddingCornerScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingDeformations(resultset: object, new_nodal_data_name: str, use_default_postfix: int, small_displacements: int) -> int:

	"""

	This function starts the procedure of adding values for deformations on an existing model for a specific resultset. It must be called before starting adding deformations on nodes with functions 'AddDeformationOnNode' and 'AddDeformationOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_nodal_data_name : str
		The new deformation data name of the resultset.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	small_displacements : int, optional
		Controls if deformations will be added with small displacements option enabled. Its default value is 0.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_nodal_data_name = "Deformations Data"
		
		    node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    visnodes = nodes.VisibleNodes(model_id)
		    for n in visnodes:
		        node_ids.append(n.id)
		        xdeform.append(0.025)
		        ydeform.append(-0.91)
		        zdeform.append(-1.398)
		    meta.results.StartAddingDeformations(resultset, new_nodal_data_name)
		    meta.results.AddDeformationOnSomeNodes(
		        resultset, node_ids, xdeform, ydeform, zdeform
		    )
		    meta.results.EndAddingDeformations(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingNodalScalar(resultset: object, new_function_data_name: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of adding nodal scalar values on an existing model for a specific resultset. It must be called before starting adding nodal scalar values on nodes using the functions 'AddNodalScalarOnNode' and 'AddNodalScalarOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		
		    node_ids = list()
		    values = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(25, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.554)
		    results.StartAddingNodalScalar(resultset, new_function_data_name)
		    results.AddNodalScalarOnSomeNodes(resultset, node_ids, values)
		    results.EndAddingNodalScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingNodalVector(resultset: object, new_function_data_name: str, vector_display_type: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of adding nodal vector values on an existing model for a specific resultset. It must be called before starting adding nodal vector values on nodes using the functions 'AddNodalVectorOnNode' and 'AddNodalVectorOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	vector_display_type : str
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    node_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(100, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.2)
		        xvector.append(0.682)
		        yvector.append(0.0)
		        zvector.append(0.7315)
		    results.StartAddingNodalVector(resultset, new_function_data_name)
		    results.AddNodalVectorOnSomeNodes(
		        resultset, node_ids, values, xvector, yvector, zvector
		    )
		    results.EndAddingNodalVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingCentroidScalar(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of setting centroid scalar values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding centroid scalar values on elements using functions 'AddCentroidScalarOnElement' and 'AddCentroidScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom centroid scalar values. Possible values are:
		- 'one_value': One centroid scalar value
		- 'top_and_bot': Top and bottom centroid scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the centroid scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(1.908)
		    new_function_data_name = "Centroid Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartAppendingCentroidScalar(
		        resultset, new_function_data_name, layer, nodal_calc, region_bounds
		    )
		    results.AddCentroidScalarOnSomeElements(
		        resultset, elements_types, elements_ids, second_ids, values
		    )
		    results.EndAddingCentroidScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingCentroidVector(resultset: object, new_function_data_name: str, layer: str, region_bounds: str, vector_display_type: str, use_default_postfix: int, triple_vector: int) -> int:

	"""

	This function starts the procedure of setting centroid vector values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding centroid vector values on elements using functions 'AddCentroidVectorOnElement' and 'AddCentroidVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom centroid vector values. Possible values are:
		- 'one_value': One centroid vector value
		- 'top_and_bot': Top and bottom centroid vector values

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal vector values for all parts they belong to
		- 'parts': Nodes will have one nodal vector value for each part they belong to
		- 'default': Default GUI selection

	vector_display_type : str, optional
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	triple_vector : int, optional
		Set to 1, only when going to add triple vector. The default value is 0.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Centroid Vector Data"
		    layer = "one_value"
		    region_bounds = "ignore"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    allelems = elements.Elements(model_id)
		    for e in allelems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(-0.885)
		        xvector.append(-0.6346)
		        yvector.append(0.25723)
		        zvector.append(-0.68315)
		    results.StartAppendingCentroidVector(
		        resultset, new_function_data_name, layer, region_bounds
		    )
		    results.AddCentroidVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        values,
		        xvector,
		        yvector,
		        zvector,
		    )
		    results.EndAddingCentroidVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingCornerScalar(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, centroid_calc: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of setting corner scalar values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding corner scalar values on elements using functions 'AddCornerScalarOnElement' and 'AddCornerScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom corner scalar values. Possible values are:
		- 'one_value': One corner scalar value
		- 'top_and_bot': Top and bottom corner scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		    results.StartAppendingCornerScalar(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerScalarOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        layer,
		    )
		    results.EndAddingCornerScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingDeformations(resultset: object, new_nodal_data_name: str, use_default_postfix: int, small_displacements: int) -> int:

	"""

	This function starts the procedure of setting values for deformations on an existing model for a specific resultset as a new deformation data (label). This function will not do any changes to the existing deformation data (labels) of the resultset. It must be called before starting adding deformations on nodes with functions 'AddDeformationOnNode' and 'AddDeformationOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_nodal_data_name : str
		The new deformation data name of the resultset.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	small_displacements : int, optional
		Controls if deformations will be appended with small displacements option enabled. Its default value is 0.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_nodal_data_name = "Deformations Data"
		
		    node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    visnodes = nodes.VisibleNodes(model_id)
		    for n in visnodes:
		        node_ids.append(n.id)
		        xdeform.append(1.025)
		        ydeform.append(-2.91)
		        zdeform.append(-3.398)
		    meta.results.StartAppendingDeformations(resultset, new_nodal_data_name)
		    meta.results.AddDeformationOnSomeNodes(
		        resultset, node_ids, xdeform, ydeform, zdeform
		    )
		    meta.results.EndAddingDeformations(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingNodalScalar(resultset: object, new_function_data_name: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of setting nodal scalar values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding nodal scalar values on nodes using the functions 'AddNodalScalarOnNode' and 'AddNodalScalarOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Scalar Data"
		
		    node_ids = list()
		    values = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(25, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.554)
		    results.StartAppendingNodalScalar(resultset, new_function_data_name)
		    results.AddNodalScalarOnSomeNodes(resultset, node_ids, values)
		    results.EndAddingNodalScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingNodalVector(resultset: object, new_function_data_name: str, vector_display_type: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of setting nodal vector values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding nodal vector values on nodes using the functions 'AddNodalVectorOnNode' and 'AddNodalVectorOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	vector_display_type : str
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Nodal Vector Data"
		
		    node_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    all_nodes = nodes.Nodes(model_id)
		    some_nodes = all_nodes[0 : min(100, len(all_nodes))]
		    for n in some_nodes:
		        node_ids.append(n.id)
		        values.append(0.8)
		        xvector.append(0.682)
		        yvector.append(0.0)
		        zvector.append(0.7315)
		    results.StartAppendingNodalVector(resultset, new_function_data_name)
		    results.AddNodalVectorOnSomeNodes(
		        resultset, node_ids, values, xvector, yvector, zvector
		    )
		    results.EndAddingNodalVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingCentroidScalar(result: object, nodal_calc: str, region_bounds: str) -> int:

	"""

	This function starts the procedure of changing centroid scalar values on an existing model for a specific resultset. This function will keep unchanged the centroid scalar values of the resultset. It must be called before starting changing centroid scalar values on elements using functions 'AddCentroidScalarOnElement' and 'AddCentroidScalarOnSomeElements'.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the centroid scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(2.792)
		    nodal_calc = "avg"
		    region_bounds = "parts"
		
		    results.StartChangingCentroidScalar(result, nodal_calc, region_bounds)
		    results.AddCentroidScalarOnSomeElements(
		        result, elements_types, elements_ids, second_ids, values
		    )
		    results.EndAddingCentroidScalar(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingCentroidVector(resultset: object, region_bounds: str, vector_display_type: str) -> object:

	"""

	This function starts the procedure of changing centroid vector values on an existing model for a specific resultset. This function will keep unchanged the centroid vector values of the resultset. It must be called before starting changing centroid vector values on elements using functions 'AddCentroidVectorOnElement' and 'AddCentroidVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal vector values for all parts they belong to
		- 'parts': Nodes will have one nodal vector value for each part they belong to
		- 'default': Default GUI selection

	vector_display_type : str
		Defines the display type of vectors. Possible values are:
		- 'simple': Simple arrows (default)
		- 'double': Arrows on both ends

	Returns
	-------
	object
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    region_bounds = "parts"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    values = list()
		    xvector = list()
		    yvector = list()
		    zvector = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        values.append(-0.941)
		        xvector.append(-0.6346)
		        yvector.append(0.25723)
		        zvector.append(-0.68315)
		    results.StartChangingCentroidVector(resultset, region_bounds)
		    results.AddCentroidVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        values,
		        xvector,
		        yvector,
		        zvector,
		    )
		    results.EndAddingCentroidVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingCornerScalar(resultset: object, nodal_calc: str, region_bounds: str, centroid_calc: str) -> int:

	"""

	This function starts the procedure of changing corner scalar values on an existing model for a specific resultset. This function will keep unchanged the corner scalar values of the resultset. It must be called before starting changing corner scalar values on elements using functions 'AddCornerScalarOnElement' and 'AddCornerScalarOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.4
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		    results.StartChangingCornerScalar(
		        resultset, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerScalarOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        layer,
		    )
		    results.EndAddingCornerScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingDeformations(result: object) -> int:

	"""

	This function starts the procedure of changing deformation values on an existing model for a specific resultset. This function will keep unchanged the deformations of the resultset. It must be called before starting changing deformations on nodes using functions 'AddDeformationOnNode' and 'AddDeformationsOnSomeNodes'.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node_ids = list()
		    xdeform = list()
		    ydeform = list()
		    zdeform = list()
		
		    visnodes = nodes.VisibleNodes(model_id)
		    for n in visnodes:
		        node_ids.append(n.id)
		        xdeform.append(0.325)
		        ydeform.append(-0.11)
		        zdeform.append(-0.978)
		    meta.results.StartChangingDeformations(result)
		    meta.results.AddDeformationOnSomeNodes(result, node_ids, xdeform, ydeform, zdeform)
		    meta.results.EndAddingDeformations(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StringDeformationLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_string_deformation_labels` instead.


	This function finds all deformation labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one deformation label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        all_labels = results.StringDeformationLabelsOfResultset(res)
		        for deform_label in all_labels:
		            print(deform_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_string_deformation_labels instead.", DeprecationWarning)

def StringFunctionLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_string_scalar_labels` instead.


	This function finds all function labels (scalar or vector) for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one function label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        all_labels = results.StringFunctionLabelsOfResultset(res)
		        for function_label in all_labels:
		            print(function_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_string_scalar_labels instead.", DeprecationWarning)

def StringScalarLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_string_scalar_labels` instead.


	This function finds all scalar labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one scalar label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        all_labels = results.StringScalarLabelsOfResultset(res)
		        for scalar_label in all_labels:
		            print(scalar_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_string_scalar_labels instead.", DeprecationWarning)

def StringVectorLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `Result.get_string_vector_labels` instead.


	This function finds all vector labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one vector label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        all_labels = results.StringVectorLabelsOfResultset(res)
		        for vector_label in all_labels:
		            print(vector_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  Result.get_string_vector_labels instead.", DeprecationWarning)

def VectorLabelsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_resultsets` instead.


	This function finds the resultsets for all vector labels for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one vector label of the corresponding state.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        vector_labels = results.VectorLabelsOfResultset(res)
		        for vector_res in vector_labels:
		            print(vector_res.cycle, vector_res.model_id)
		            print(
		                vector_res.name,
		                vector_res.nodal_data_name,
		                vector_res.function_data_name,
		                vector_res.vector_data_name,
		            )
		            print(vector_res.filename, vector_res.subcase, vector_res.state)
		            print(vector_res.step, vector_res.frequency, vector_res.time)
		            print(
		                vector_res.mode, vector_res.eigenvalue, vector_res.imaginary_eigenvalue
		            )
		            print(vector_res.loadstep, vector_res.generate_sequence)
		            print(
		                vector_res.nodal_data_label,
		                vector_res.function_data_label,
		                vector_res.vector_data_label,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_resultsets instead.", DeprecationWarning)

def VectorTypes(filename: str, deck: str) -> object:

	"""

	This function finds the vector types and the corresponding states for a specified file.

	Parameters
	----------
	filename : str
		Name of the file

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	Returns
	-------
	object
		It returns a list with the vector types and the corresponding states as strings for the specified file. Each member of the list is another list containing in position 0 the vector type as a string and in the rest positions the name of the states referring to this type.
		Vector types are string expressions (e.g. 'Strains', 'Point loads', 'Displacements:All Cycles', 'Reaction forces:Cycle 1' etc.).
		States are also string expressions with the first characters referring to the id of the state (e.g '15 STATE 15 ,TIME 14.00000000E+00' etc.).
		State id can also be retrieved from the position of the state in the list. 
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadVector, results.LoadProjectVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.VectorTypes(filename, deck)
		    for one_type in all_types:
		        total = len(one_type)
		        vector_type = one_type[0]  # vector type
		        print(vector_type)
		        for k in range(total):
		            state = one_type[k]
		            print(state, k)  # One state of the above vector types and its id
		
		
		if __name__ == "__main__":
		    main()


	"""

def VectorTypesAll(filename: str, deck: str, results_type: str) -> int:

	"""

	This function finds the vector types, the states and the corresponding information for a file specified by its filename. Vector types are string expressions (e.g. "Strains", "Point loads", "Displacements:All Cycles", "Reaction forces:Cycle 1" etc.). States are also string expressions with the first characters referring to the id of the state (e.g "15 STATE 15 ,TIME 14.00000000E+00" etc.).

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	int
		It returns a list with other lists as members with information for vector types and states of the specified file. Each member of the list is another list which contains:
		position 0 : String name of the type
		position 1 : List with states names  
		position 2 : List with states ids
		position 3 : List with name of functions
		position 4 : List with the type of the data
		position 5 : List with extra information
		Upon failure, an empty lst is returned.

	See Also
	--------
	results.LoadVector, results.LoadProjectVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.VectorTypesAll(filename, deck)
		    for vector_type in all_types:
		        type = vector_type[0]
		        print(type)  # Name of vector type (e.g. "Stresses")
		        state_names = vector_type[1]
		        for state_name in state_names:
		            print(state_name)  # Name of state
		        state_ids = vector_type[2]
		        for state_id in state_ids:
		            print(state_id)  # Id of state
		        functions = vector_type[3]
		        for one_function in functions:
		            print(one_function)  # Name of function
		        all_data = vector_type[4]
		        for data in all_data:
		            print(data)  # Type of data
		        extra_info = vector_type[5]
		        for extra in extra_info:
		            print(extra)  # Extra information
		
		
		if __name__ == "__main__":
		    main()


	"""

def VectorTypesList(filename: str, deck: str, expression_type: str, results_type: str) -> object:

	"""

	This function finds all the vector types of a file specified by its filename.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name of the file (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	expression_type : str, optional
		It controls the format of the output.
		- "read_results_expression": Output in appropriate format for read results commands (e.g. LoadVector) (default)
		- "labels_expression": Output in appropriate format for labels manipulation (e.g. ResultsetsByVectorLabel)

	results_type : str, optional
		It controls if all or primary results will be returned.
		- "all": All results (default)
		- "primary": Primary results

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one vector type of the specified file.
		List with vector types is sorted.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.LoadVector, results.LoadProjectVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx2.op2"
		    deck = "NASTRAN"
		    all_types = results.VectorTypesList(filename, deck)
		    for vector_type in all_types:
		        print(vector_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CyclesList(filename: str, deck: str) -> object:

	"""

	This function finds all the cycles of a file specified by its filename. Cycles are numbers of type int.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name.

	Returns
	-------
	object
		It returns a list with integers as elements referring to the cycle numbers of the specified file.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/examples/NastranEx1.op2"
		    deck = "NASTRAN"
		    all_cycles = results.CyclesList(filename, deck)
		    for cycle_num in all_cycles:
		        print(cycle_num)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateResultsetWithId(model_id: int, state_id: int, name: str, resultset_id: int, cycle: int) -> object:

	"""

	This function creates a resultset for a specified model. If a resultset with these atributes already exists, this function will fail.

	Parameters
	----------
	model_id : int
		Model id.

	state_id : int
		It refers to the variable subcase of the state.

	name : str
		Name of the resultset. It defines the title (filename, name) of the resultset.

	resultset_id : int
		Id of the resultset after which the new resultset will be added.

	cycle : int, optional
		Cycle of the resultset. It defines the cycle number of the resultset and it must refer to an existing cycle. If it is absent then resultsets will be created for all the existing cycles of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    state_id = 15
		    name = "Script added resultset"
		    resultset_id = (
		        1  # This will place the new resultset at postition 2 on the states list
		    )
		    cycle = 0
		    new_resultsets = results.CreateResultsetWithId(
		        model_id, state_id, name, resultset_id, cycle
		    )
		    for res in new_resultsets:
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


	"""

def CreateResultsetFrequencyWithId(model_id: int, frequency: float, name: str, resultset_id: int, cycle: int) -> object:

	"""

	This function creates a resultset for a given model. If a resultset with these atributes already exists, this function will fail.

	Parameters
	----------
	model_id : int
		Model id.

	frequency : float
		Frequency of resultset. It refers to the variable frequency of the state.

	name : str
		Name of the resultset. It defines the title (filename, name) of the resultset.

	resultset_id : int
		Id of the resultset after which the new resultset will be added.

	cycle : int, optional
		Cycle of the resultset. It defines the cycle number of the resultset and it must refer to an existing cycle. If it is absent then resultsets will be created for all the existing cycles of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    frequency = 25.22
		    name = "Frequency 25.22"
		    resultset_id = (
		        1  # This will place the new resultset at postition 2 on the states list
		    )
		    new_resultsets = results.CreateResultsetFrequencyWithId(
		        model_id, frequency, name, resultset_id
		    )
		    for res in new_resultsets:
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


	"""

def CreateResultsetTimeWithId(model_id: int, time: float, name: str, resultset_id: int, cycle: int) -> object:

	"""

	This function creates a resultset for a given model. If a resultset with these atributes already exists, this function will fail.

	Parameters
	----------
	model_id : int
		Model id.

	time : float
		Time of resultset. It refers to the state variable time.

	name : str
		Name of the resultset. It defines the title (filename, name) of the resultset.

	resultset_id : int
		Id of the resultset after which the new resultset will be added.

	cycle : int, optional
		Cycle of the resultset. It defines the cycle number of the resultset and it must refer to an existing cycle. If optional argument cycle is absent then resultsets will be created for all the existing cycles of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Result referring to one newly created state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    time = 25
		    name = "Time 25"
		    resultset_id = (
		        1  # This will place the new resultset at postition 2 on the states list
		    )
		    new_resultsets = results.CreateResultsetTimeWithId(
		        model_id, time, name, resultset_id
		    )
		    for res in new_resultsets:
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


	"""

def DiscreteCycles(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_cycles` instead.


	This function collects all SOL200 discrete optimization cycles of a given model.

	Parameters
	----------
	model_id : int
		Model id

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to one discrete cycle of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    discrete_cycles = results.DiscreteCycles(model_id)
		    for cycle in discrete_cycles:
		        print(cycle)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_cycles instead.", DeprecationWarning)

def CurrentResultFilename(model_id: int) -> str:

	"""

	This function gets the current result filename of the given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	str
		Upon success, it returns a string referring to the current result filename of the model. 
		Else, an empty string is returned from the function.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    cur_filename = results.CurrentResultFilename(model_id)
		    print(cur_filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCornerVectorOnElement(result: object, element_type: int, element_id: int, second_id: int, node_ids: object, corner_values: object, corner_vx_values: object, corner_vy_values: object, corner_vz_values: object, layer: str, centroid_value: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.set_corner_vector` instead.


	This function adds corner vector values on an element with specific id and type of a given model. Functions 'StartAddingCornerVector', 'StartChangingCornerVector' or 'StartAppendingCornerVector' must be called with the same argument (result) before starting adding corner vector values. Function 'EndAddingCornerVector' must be called with the same argument (result) after ending adding corner vector values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	node_ids : object
		A list with ids of some nodes of the element.

	corner_values : object
		A list of floats as corner scalar values of the element.

	corner_vx_values : object
		A list of floats as corner X component values of the element.

	corner_vy_values : object
		A list of floats as corner Y component values of the element.

	corner_vz_values : object
		A list of floats as corner Z component values of the element.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	centroid_value : object, optional
		Centroid vector values of the element. If the automatic calculation of centroid scalar values in function 'StartAddingCornerVector' has been specified then it will be ignored. The argument is a list of 4 float values . The first is the centroid scalar value, the second the value of X component, the third the value of Y component and the fourth the value of Z component.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    node_ids = list()
		    corner_values = list()
		    corner_vx_values = list()
		    corner_vy_values = list()
		    corner_vz_values = list()
		    element_nodes = nodes.NodesOfElement(model_id, element_type, element_id, second_id)
		    value = 0.1
		    vx = 1.0
		    vy = 0.0
		    vz = 0.0
		    for n in element_nodes:
		        node_ids.append(n.id)
		        corner_values.append(value)
		        corner_vx_values.append(vx)
		        corner_vy_values.append(vy)
		        corner_vz_values.append(vz)
		        value = value + 0.1
		    results.StartAddingCornerVector(
		        result, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerVectorOnElement(
		        result,
		        element_type,
		        element_id,
		        second_id,
		        node_ids,
		        corner_values,
		        corner_vx_values,
		        corner_vy_values,
		        corner_vz_values,
		        layer,
		    )
		    results.EndAddingCornerVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.set_corner_vector instead.", DeprecationWarning)

def AddCornerVectorOnSomeElements(result: object, elements: object, node_ids: object, corner_values: object, corner_vx_values: object, corner_vy_values: object, corner_vz_values: object, layer: str, centroid_values: object) -> bool:

	"""

	This function adds corner vector values on some elements with specific id and type of a given model. Functions 'StartAddingCornerVector', 'StartChangingCornerVector' or 'StartAppendingCornerVector' must be called with the same argument (result) before starting adding corner vector values. Function 'EndAddingCornerVector' must be called with the same argument (result) after ending adding corner vector values.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	elements : object
		A list, of objects of class Element.

	node_ids : object
		List with Ids of the nodes of the elements as integers.

	corner_values : object
		A list that contains a list of corner scalar values for each element as floats.

	corner_vx_values : object
		A list that contains a list of corner X component values for each element as floats.

	corner_vy_values : object
		A list that contains a list of corner Y component values for each element as floats.

	corner_vz_values : object
		A list that contains a list of corner Z component values for each element as floats.

	layer : str
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'one_value' (default)
		- 'bottom'
		- 'top'

	centroid_values : object, optional
		A list of objects as centroid vector values of the elements. Each object is a list of 4 float values.The first is the scalar centroid value, the second the X component value, the third the Y component value and the fourth the Z component value.If the automatic calculation of centroid scalar values in function 'StartAddingCornerVector' has been specified then it will be ignored.

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    new_function_data_name = "Corner Vector Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartAddingCornerVector(
		        result, new_function_data_name, layer, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        result,
		        viselems,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    # or
		    # results.AddCornerVectorOnSomeElements(result, elements_types, elements_ids, second_ids, elements_node_ids, elements_corner_values, elements_corner_vx_values, elements_corner_vy_values, elements_corner_vz_values, layer)
		    results.EndAddingCornerVector(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EndAddingCornerVector(resultset: object, cut_off: str, cut_off_limit: str) -> int:

	"""

	This function ends the procedure of adding corner vector values on an existing model for a specific resultset. It must be called after ending adding corner vector values on elements with functions 'AddCornerVectorOnElement' and 'AddCornerVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	cut_off : str, optional
		Defines if corner vector values will be compressed. Possible values are:
		- 'cut_off_disable': Cut-off values is disabled (default)
		- 'cut_off_values': Cut-off values below a given limit
		- 'cut_off_hidden': Cut-off values of hidden parts

	cut_off_limit : str, optional
		The cut-off limit for corner vector values in case that the argument 'cut-off' is set to 'cut_off_values'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartAddingCornerVector(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    results.EndAddingCornerVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsCornerVector(corner_vector: object) -> int:

	"""

	This function checks whether an object is of class CornerVector.

	Parameters
	----------
	corner_vector : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class CornerVector, 0 otherwise.

	See Also
	--------
	results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    all_results = results.CollectResults(result, "corner_vector")
		    iter_end = min(10, len(all_results))
		    for res in all_results[0:iter_end]:
		        if results.IsCornerVector(res):
		            corn = res
		            print("This is an object of class CornerVector")
		            print(corn.value)  # Corner scalar value
		            print(corn.x)  # Corner X component value
		            print(corn.y)  # Corner Y component value
		            print(corn.z)  # Corner Z component value
		            print(
		                corn.element_id, corn.second_id, corn.type
		            )  # Id, second id and type of the element
		            print(
		                corn.corner
		            )  # Id of the node - corner with this corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAddingCornerVector(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, centroid_calc: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of adding corner vector values on an existing model for a specific resultset. This function will reset all the corner vector values of the resultset to zero. It must be called before starting adding corner vector values on elements using functions 'AddCornerVectorOnElement' and 'AddCornerVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom corner scalar values. Possible values are:
		- 'one_value': One corner scalar value
		- 'top_and_bot': Top and bottom corner scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartAddingCornerVector(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    results.EndAddingCornerVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartAppendingCornerVector(resultset: object, new_function_data_name: str, layer: str, nodal_calc: str, region_bounds: str, centroid_calc: str, use_default_postfix: int) -> int:

	"""

	This function starts the procedure of setting corner vector values on an existing model for a specific resultset as a new function data (label). This function will not do any changes to the existing function data (labels) of the resultset. It must be called before starting adding corner vector values on elements using functions 'AddCornerVectorOnElement' and 'AddCornerVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	new_function_data_name : str
		The new function data name of the resultset.

	layer : str
		Defines if the resultset will contain top and bottom corner scalar values. Possible values are:
		- 'one_value': One corner scalar value
		- 'top_and_bot': Top and bottom corner scalar values

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	use_default_postfix : int, optional
		Controls if postfix ':Script_Created' will be appended to the 'new_function_data_name'. Its default value is 1.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    new_function_data_name = "Corner Scalar Data"
		    layer = "one_value"
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.1
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartAppendingCornerVector(
		        resultset,
		        new_function_data_name,
		        layer,
		        nodal_calc,
		        region_bounds,
		        centroid_calc,
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    results.EndAddingCornerVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingCornerVector(resultset: object, nodal_calc: str, region_bounds: str, centroid_calc: str) -> int:

	"""

	This function starts the procedure of changing corner vector values on an existing model for a specific resultset. This function will keep unchanged the corner vector values of the resultset. It must be called before starting changing corner vector values on elements using functions 'AddCornerVectorOnElement' and 'AddCornerVectorOnSomeElements'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	nodal_calc : str
		Defines the way the nodal scalar values will be calculated from the corner scalar values for each node of the element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'disc': Discontinuities
		- 'prob_err': Probable Error
		- 'norm_max_dif': Normalized Max Difference
		- 'default': Default GUI selection

	region_bounds : str
		Defines if nodes belonging to more than one parts will have different values for each part. Possible values are:
		- 'ignore': Nodes will have the same nodal scalar values for all parts they belong to
		- 'parts': Nodes will have one nodal scalar value for each part they belong to
		- 'default': Default GUI selection

	centroid_calc : str, optional
		Defines the way the centroid scalar values will be calculated from the corner scalar values for each element. Possible values are:
		- 'avg': Average
		- 'max': Maximum
		- 'min': Minimum
		If it is absent, then centroid scalar values must be given by the user in functions 'AddCentroidScalarOnElement' or 'AddCentroidScalarOnSomeElements'.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    nodal_calc = "avg"
		    region_bounds = "parts"
		    centroid_calc = "avg"
		
		    elements_types = list()
		    elements_ids = list()
		    second_ids = list()
		    elements_node_ids = list()
		    elements_corner_values = list()
		    elements_corner_vx_values = list()
		    elements_corner_vy_values = list()
		    elements_corner_vz_values = list()
		
		    viselems = elements.VisibleElements(model_id)
		    for e in viselems:
		        elements_types.append(e.type)
		        elements_ids.append(e.id)
		        second_ids.append(e.second_id)
		        node_ids = list()
		        corner_values = list()
		        corner_vx_values = list()
		        corner_vy_values = list()
		        corner_vz_values = list()
		        element_nodes = nodes.NodesOfElement(model_id, e.type, e.id, e.second_id)
		        value = 0.4
		        vx = 1.0
		        vy = 0.0
		        vz = 0.0
		        for n in element_nodes:
		            node_ids.append(n.id)
		            corner_values.append(value)
		            corner_vx_values.append(vx)
		            corner_vy_values.append(vy)
		            corner_vz_values.append(vz)
		            value = value + 0.1
		        elements_node_ids.append(node_ids)
		        elements_corner_values.append(corner_values)
		        elements_corner_vx_values.append(corner_vx_values)
		        elements_corner_vy_values.append(corner_vy_values)
		        elements_corner_vz_values.append(corner_vz_values)
		    results.StartChangingCornerVector(
		        resultset, nodal_calc, region_bounds, centroid_calc
		    )
		    layer = "one"
		    results.AddCornerVectorOnSomeElements(
		        resultset,
		        elements_types,
		        elements_ids,
		        second_ids,
		        elements_node_ids,
		        elements_corner_values,
		        elements_corner_vx_values,
		        elements_corner_vy_values,
		        elements_corner_vz_values,
		        layer,
		    )
		    results.EndAddingCornerVector(resultset)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LockedResultsetsOfWindow(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_resultsets` instead.


	This function collects all the locked states for all cycles of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Returns a list where each member of the list is an object of class Result referring 
		to one locked state of the corresponding model for a specific cycle.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		
		    all_resultsets = results.LockedResultsetsOfWindow(model_id, window_name)
		    for res in all_resultsets:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_resultsets instead.", DeprecationWarning)

def AttributeOfResultset(resultset: object, attribute_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a Resultset of the model.

	attribute_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if len(all_resultsets):
		        res = all_resultsets[1]
		        name = "Name"
		
		        val = results.AttributeOfResultset(res, name)
		        print("Value", val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_attributes instead.", DeprecationWarning)

def AttributeOfCycle(model_id: int, cycle_id: int, attribute_name: str) -> str:

	"""

	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The number of the model

	cycle_id : int
		The id of cycle

	attribute_name : str
		Name of the attribute

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
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle_id = 2
		    attribute_name = "Deform.max"
		    val = results.AttributeOfCycle(model_id, cycle_id, attribute_name)
		    print("Value: " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeOfCycle(model_num: int, cycle_id: int, attribute_name: int, attribute_value: object, attribute_type: str) -> int:

	"""

	This function sets the value of a specific User Specified attribute referring to a given cycle. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_num : int
		The number of the model.

	cycle_id : int
		The id of the cycle.

	attribute_name : int
		Name of the attribute.

	attribute_value : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str
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
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle_id = 2
		    attribute_name = "test"
		    attribute_value = "value"
		    val = results.SetAttributeOfCycle(
		        model_id, cycle_id, attribute_name, attribute_value
		    )
		    print(val)
		    # or
		    attribute_name = "num_test"
		    attribute_value = 123
		    attribute_type = "numerical"
		    val = results.SetAttributeOfCycle(
		        model_id, cycle_id, attribute_name, attribute_value, attribute_type
		    )
		    print(val)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributesOfCycle(model_num: int, cycle_id: int) -> object:

	"""

	This function collects all attributes of a given cycle

	Parameters
	----------
	model_num : int
		The number of the model

	cycle_id : int
		The id of the node

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given node.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    cycle_id = 2
		    all_attributes = results.AttributesOfCycle(model_id, cycle_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeformationReadOptionsOfResultset(result: object):

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_deformation_read_options` instead.


	This function gets the deformation reading options for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        read_options = results.DeformationReadOptionsOfResultset(res)
		        for option in read_options:
		            print(option[0])
		            print(option[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_deformation_read_options instead.", DeprecationWarning)

def ScalarReadOptionsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_scalar_read_options` instead.


	This function gets the scalar reading options for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is another list which contains in position 0 the name of a reading option and in position 1 the value of a reading option. 
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        read_options = results.ScalarReadOptionsOfResultset(res)
		        for option in read_options:
		            print(option[0])
		            print(option[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_scalar_read_options instead.", DeprecationWarning)

def VectorReadOptionsOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_vector_read_options` instead.


	This function gets the vector reading options for the state of the given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is another list which contains in position 0 the name of a reading option and in position 1 the value of a reading option. 
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        read_options = results.VectorReadOptionsOfResultset(res)
		        for option in read_options:
		            print(option[0])
		            print(option[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_vector_read_options instead.", DeprecationWarning)

def PrimaryResultsList(filename: str, deck: str, expression_type: str) -> object:

	"""

	This function finds all the primary result types of a results file.

	Parameters
	----------
	filename : str
		Name of the file.

	deck : str
		Deck name.

	expression_type : str
		It controls the format of the output.
		- "read_results_expression": Output in appropriate format for read results commands (e.g. LoadScalar) (default)
		- "labels_expression": Output in appropriate format for labels manipulation (e.g. ResultsetsByScalarLabel)

	Returns
	-------
	object
		It returns a list with the primary result types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a list with strings as elements referring to the deformation types of the specified file.
		In position 1, internal lists contain a list with strings as elements referring to the scalar types of the specified file.
		In position 2, internal lists contain a list with strings as elements referring to the vector types of the specified file.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    filename = "/home/car/d3plot"
		    deck = "DYNA"
		    expression_type = "labels_expression"
		    primary_results = results.PrimaryResultsList(filename, deck, expression_type)
		    all_deform = primary_results[0]  # List with deformations results
		    for one_deform in all_deform:
		        print(one_deform)
		    all_scalar = primary_results[1]  # List with scalar results
		    for one_scalar in all_scalar:
		        print(one_scalar)
		    all_vector = primary_results[2]  # List with vector results
		    for one_vector in all_vector:
		        print(one_vector)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCentroidTripleVectorOnElement(resultset: object, element_type: int, element_id: int, second_id: int, value: object, xvector: object, yvector: object, zvector: object, layer: str) -> int:

	"""

	This function adds a triple centroid vector value on an element with specific id and type of a given model. Functions 'StartAddingCentroidVector', 'StartChangingCentroidVector' or 'StartAppendingCentroidVector' must be called with the same argument (result) before starting adding triple centroid vector values. Function 'EndAddingCentroidVector' must be called with the same argument (result) after ending adding centroid vector values.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	value : object
		A list of 3 floats as the magnitude of the centroid vector values for each principal

	xvector : object
		A list of 3 floats as the normalized X-direction of the centroid vector components for each principal

	yvector : object
		A list of 3 floats as the normalized Y-direction of the centroid vector components for each principal

	zvector : object
		A list of 3 floats as the normalized Z-direction of the centroid vector components for each principal

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		
		import meta
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if len(all_resultsets):
		        result = all_resultsets[1]
		
		        element_type = constants.SHELL
		        element_id = 1
		        second_id = -1
		
		        value = [0.354, 0.23, 0.12]
		        xvector = [0.31, 0.5, 0.1]
		        yvector = [0.6834, 0.3, 0.2]
		        zvector = [-0.2572, 0.1, 0.8]
		
		        new_function_data_name = "Centroid Vector Data"
		        layer = "one_value"
		        region_bounds = "parts"
		        vector_display_type = "double"
		        use_default_postfix = 0
		        triple_vector = 1
		        results.StartAddingCentroidVector(
		            result,
		            new_function_data_name,
		            layer,
		            region_bounds,
		            vector_display_type,
		            use_default_postfix,
		            triple_vector,
		        )
		        ret = results.AddCentroidTripleVectorOnElement(
		            result,
		            element_type,
		            element_id,
		            second_id,
		            value,
		            xvector,
		            yvector,
		            zvector,
		        )
		        results.EndAddingCentroidVector(result)
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCentroidTripleVectorOnSomeElements(resultset: object, elements: object, values: object, xvector: object, yvector: object, zvector: object, layer: str) -> int:

	"""

	This function adds a centroid principal vector on some elements with specific id and type of a given model. Functions 'StartAddingCentroidVector', 'StartChangingCentroidVector' or 'StartAppendingCentroidVector' must be called with the same argument (result) before starting adding centroid vector values. Function 'EndAddingCentroidVector' must be called with the same argument (result) after ending adding centroid vector values.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	elements : object
		A list with objects of class Element.

	values : object
		A list that contains a list with three values for each element. The three values corresponds to the value of the first, second and third principal.

	xvector : object
		A list that contains a list with three values for each element. The three values corresponds to the normalized X-direction vector component of the first, second and third principal.

	yvector : object
		A list that contains a list with three values for each element. The three values corresponds to the normalized Y-direction vector component of the first, second and third principal.

	zvector : object
		A list that contains a list with three values for each element. The three values corresponds to the normalized Z-direction vector component of the first, second and third principal.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import models
		from meta import windows
		
		
		def main():
		    model = models.Model(0)
		    all_resultsets = model.get_resultsets()
		    if len(all_resultsets):
		        result = all_resultsets[1]
		        window_m = windows.Window("MetaPost", page_id=0)
		        elems = model.get_elements("visible", window=window_m)
		
		        values = list()
		        xvectors = list()
		        yvectors = list()
		        zvectors = list()
		        size = len(elems)
		        for i in range(0, size):
		            values.append([0.354, 0.23, 0.12])
		            xvectors.append([0.31, 0.5, 0.1])
		            yvectors.append([0.6834, 0.3, 0.2])
		            zvectors.append([-0.2572, 0.1, 0.8])
		        new_function_data_name = "Centroid Vector Data"
		        layer = "one_value"
		        region_bounds = "parts"
		        vector_display_type = "double"
		        use_default_postfix = 0
		        triple_vector = 1
		        results.StartAddingCentroidVector(
		            result,
		            new_function_data_name,
		            layer,
		            region_bounds,
		            vector_display_type,
		            use_default_postfix,
		            triple_vector,
		        )
		        ret = results.AddCentroidTripleVectorOnSomeElements(
		            result, elems, values, xvectors, yvectors, zvectors
		        )
		        results.EndAddingCentroidVector(result)
		
		        print(ret)
		
		
		# or
		
		from meta import constants
		
		def main():
		
		\tmodel_id = 0
		\tall_resultsets = results.Resultsets(model_id)
		\tresult = all_resultsets[1]
		
		\telement_types = [constants.SHELL, constants.SHELL]
		\telement_ids = [1, 2]
		\tsecond_ids = [-1, -1]
		
		\tvalues = [ [0.354, 0.23, 0.12], [0.354, 0.23, 0.12] ]
		\txvectors = [ [0.31, 0.5, 0.1], [0.31, 0.5, 0.1] ]
		\tyvectors = [ [0.6834, 0.3, 0.2], [0.6834, 0.3, 0.2] ]
		\tzvectors = [ [-0.2572, 0.1, 0.8], [-0.2572, 0.1, 0.8] ]
		
		\tnew_function_data_name = 'Centroid Vector Data'
		\tlayer = 'one_value'
		\tregion_bounds = 'parts'
		\tvector_display_type = 'double'
		\tuse_default_postfix = 0
		\ttriple_vector = 1
		\tresults.StartAddingCentroidVector(result, new_function_data_name, layer, region_bounds, vector_display_type, use_default_postfix, triple_vector)
		\tret = results.AddCentroidTripleVectorOnSomeElements(result, element_types, element_ids, second_ids, values, xvectors, yvectors, zvectors);
		\tresults.EndAddingCentroidVector(result)
		\t
		\tprint(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PlotMaxDistanceOfNodesFreqResp(model_id: int, node_id1: int, node_id2: int, real_label: str, imaginary_label: str) -> object:

	"""

	Given two nodes, a label representing real part of complex results, and a label representing imaginary part of complex results, plot the maximum distance of the nodes for each state.

	Parameters
	----------
	model_id : int
		The id of the model.

	node_id1 : int
		The id of the first node.

	node_id2 : int
		The id of the second node.

	real_label : str
		The label representing real results.

	imaginary_label : str
		The label representing imaginary results.

	Returns
	-------
	object
		It returns a curve object, with the frequency on the x axis, and the maximum distance on the y axis.
		Upon failure, a NULL object is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    node_id1 = 669
		    node_id2 = 834
		    real_label = "Complex Displacements,Real"
		    imag_label = "Complex Displacements,Imaginary"
		
		    curve = results.PlotMaxDistanceOfNodesFreqResp(
		        model_id, node_id1, node_id2, real_label, imag_label
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingNodalScalar(resultset: object) -> bool:

	"""

	This function starts the procedure of changing nodal scalar values on an existing model for a specific resultset. This function will keep unchanged the nodal scalar values of the resultset. It must be called before starting changing nodal scalar values on nodes using functions 'Node.set_nodal_scalar' and 'AddNodalScalarOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    nodes = m.get_nodes("identified")
		
		    results.StartChangingNodalScalar(res)
		    for n in nodes:
		        n.set_nodal_scalar(res, 0.09)
		    results.EndAddingNodalScalar(res)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StartChangingNodalVector(resultset: object) -> bool:

	"""

	This function starts the procedure of changing nodal vector values on an existing model for a specific resultset. This function will keep unchanged the nodal vector values of the resultset. It must be called before starting changing nodal vector values on nodes using functions 'Node.set_nodal_vector' and 'AddNodalVectorOnSomeNodes'.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a resultset of the model to which the value is added.

	Returns
	-------
	bool
		It returns True upon success or False upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    nodes = m.get_nodes("identified")
		
		    results.StartChangingNodalVector(res)
		    vec = [1.5, 1, 0, 0]
		    for n in nodes:
		        n.set_nodal_vector(res, vec)
		    results.EndAddingNodalVector(res)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Result():

	"""

	Class for resultsets.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    all_resultsets = m.get_resultsets()
		
		    for res in all_resultsets:
		        print(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    model = res.get_model()
		    if model:
		        print(model.id, model.name, model.label, model.deck)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    specifier = "all"
		    # specifier = 'generator'
		    # specifier = 'generated'
		    results = res.get_resultsets(specifier)
		    # results = res.get_resultsets(specifier, result_type = 'deformation')
		    # results = res.get_resultsets(specifier, result_type = 'scalar')
		    # results = res.get_resultsets(specifier, result_type = 'vector')
		    # results = res.get_resultsets(specifier, result_type = 'function')
		    # windows = m.get_windows()
		    # results = res.get_resultsets(specifier, result_type = 'deformation', label ='Displacements', cycle = 2, windnows[0])
		    print(results)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_filename
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    filename = res.get_filename()
		    print(filename)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    deforms = res.get_deformations()
		    print(deforms)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    nodal_scalars = res.get_nodal_scalar()
		    print(nodal_scalars)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    nodal_vectors = res.get_nodal_vector()
		    print(nodal_vectors)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    centroid_scalars = res.get_centroid_scalar()
		    print(centroid_scalars)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    centroid_vectors = res.get_centroid_vector()
		    print(centroid_vectors)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    corner = res.get_corner_scalar()
		    print(corner)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    corner = res.get_corner_vector()
		    print(corner)
		
		
		if __name__ == "__main__":
		    main()
		# method: has_deformations
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.has_deformations()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: has_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.has_scalar()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: has_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.has_vector()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.is_scalar()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.is_vector()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformation_read_options
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    opts = res.get_deformation_read_options()
		    print(opts)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_scalar_read_options
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    opts = res.get_scalar_read_options()
		    print(opts)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_read_options
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    opts = res.get_vector_read_options()
		    print(opts)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_string_deformation_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    labels = res.get_string_deformation_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_string_scalar_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    labels = res.get_string_scalar_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_string_vector_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    labels = res.get_string_vector_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_id
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    id = res.get_id()
		    print(id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_layers
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    layers = res.get_layers()
		    print(layers)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    attr = res.get_attributes()
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attributes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    attribute_name = "attr_name"
		    attribute_type = "numerical"
		    attribute_value = 1.33
		    ret = res.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: generate
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    result_type = "all"
		    # result_type = 'deform'
		    # result_type = 'function'
		    steps = 10
		    interpolation_type = "linear"
		    # interpolation_type = 'cos'
		    # interpolation_type = 'sin'
		    ret = res.generate(result_type, steps, interpolation_type)
		    # interpolation_type = 'sin'
		    # ret = res.generate(result_type, steps, interpolation_type, angle = 180)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: clear
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.clear()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    ret = res.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: copy_deformations
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    all_resultsets = m.get_resultsets()
		    source = all_resultsets[1]
		    target = all_resultsets[2]
		    specifier = "all"
		    # specifier = 'one'
		    ret = target.copy_deformations(specifier, source)
		    # ret = target.copy_deformations(specifier, source, new_name = 'New_Deformation')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: copy_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    all_resultsets = m.get_resultsets()
		    source = all_resultsets[2]
		    target = all_resultsets[1]
		    specifier = "all"
		    # specifier = 'one'
		    ret = target.copy_scalar(specifier, source)
		    # ret = target.copy_scalar(specifier, source, new_name ='New Scalar')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: copy_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    all_resultsets = m.get_resultsets()
		    source = all_resultsets[2]
		    target = all_resultsets[1]
		    specifier = "all"
		    # specifier = 'one'
		    ret = target.copy_vector(specifier, source)
		    # ret = target.copy_vector(specifier, source, new_name = 'New Vector')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: copy_function
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		
		    all_resultsets = m.get_resultsets()
		    source = all_resultsets[2]
		    target = all_resultsets[1]
		    specifier = "all"
		    # specifier = 'one'
		    ret = target.copy_function(specifier, source)
		    # ret = target.copy_function(specifier, source, new_name = 'New Function')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import models
		from meta import results
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    can_use = res.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	cycle: int = None
	"""
	Cycle number of the resultset.

	"""

	model_id: int = None
	"""
	Model id of the resultset.

	"""

	name: str = None
	"""
	Name of the resultset.

	"""

	nodal_data_name: str = None
	"""
	Nodal data name of the resultset, 'NONE' if it does not exist.

	"""

	function_data_name: str = None
	"""
	Scalar data name of the resulset, 'NONE' if it does not exist.

	"""

	filename: str = None
	"""
	Filename of the resultset.

	"""

	subcase: int = None
	"""
	Subcase of the resultset.

	"""

	state: float = None
	"""
	State of the resultset.

	"""

	step: float = None
	"""
	Step of the resultset.

	"""

	frequency: float = None
	"""
	Frequency of the resultset.

	"""

	time: float = None
	"""
	Time of the resultset.

	"""

	mode: int = None
	"""
	Mode of the resultset.

	"""

	eigenvalue: float = None
	"""
	Eigenvalue of the resultset.

	"""

	imaginary_eigenvalue: float = None
	"""
	Imaginary eigenvalue of the resultset.

	"""

	loadstep: float = None
	"""
	Loadstep of the resultset.

	"""

	generate_sequence: int = None
	"""
	Generate number of the resultset.

	"""

	nodal_data_label: str = None
	"""
	Nodal data label of the resultset, 'NONE' if it does not exist.

	"""

	function_data_label: str = None
	"""
	Scalar data label of the resultset, 'NONE' if it does not exist.

	"""

	vector_data_label: str = None
	"""
	Vector data label of the resultset, 'NONE' if it does not exist.

	"""

	vector_data_name: str = None
	"""
	Vector data name of the resulsett, 'NONE' if it does not exist.

	"""

	internal4: str = None
	"""
	System use only.

	"""

	step_name: str = None
	"""
	Step name

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the result.


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the result. Upon failure, it returns None.

		"""


	def get_resultsets(self, specifier: str, result_type: str, label: str, cycle: int, window: object) -> object:

		"""

		This method gets the resultsets, according to the specifier, for the state of this resultset.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all resultsets (default value). It requires result_type and label arguments to be set.
			- 'generator' : gets the resultset that generated this resultset
			- 'generated' : gets the resultsets that generated from this resultset.

		result_type : str, optional
			If set, the method will get only the resultsets from a specific label, specified by the argument label. Its possible values are:
			-'deformations' : Only resultsets of a deformation label.
			-'scalar' : Only resultsets of a scalar label.
			-'vector' : Only resultsets of a vector label.
			-'function' : Only resultsets of a function label.

		label : str, optional
			The name of the label. If this argument is set, the argument result_type, must also be set.

		cycle : int, optional
			Cycle of the resultset. If set, the method gets the resultsets with cycle equal to cycle

		window : object, optional
			An object of class Window. This argument is used only when the specifier is generated.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Result referring to one resultset of the model.Upon failure, an empty list is returned.

		"""


	def get_filename(self) -> str:

		"""

		This method gets the filename of the resultset.


		Returns
		-------
		str
			Upon success, it returns the filename of the resultset. Upon failure, it returns None.

		"""


	def get_deformations(self) -> object:

		"""

		This method gets the deformation results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_nodal_scalar(self) -> object:

		"""

		This method gets the nodal scalar results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_nodal_vector(self) -> object:

		"""

		This method gets the nodal vector results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_centroid_scalar(self, non_zero: bool, exclude_novalue: bool) -> object:

		"""

		This method gets the centroid scalar results of the resultset.


		Parameters
		----------
		non_zero : bool, optional
			If True, the method will return only the non zero values. The default value is False.

		exclude_novalue : bool, optional
			If True, the method will not return anything for elements that have no value. The default value is False. If non_zero is True, this argument is ignored.

		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_centroid_vector(self) -> object:

		"""

		This method gets the centroid vector results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_corner_scalar(self) -> object:

		"""

		This method gets the corner scalar results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def get_corner_vector(self) -> object:

		"""

		This method gets the corner vector results of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is an object referring to one specific result of the model.If both bottom and top values are loaded this function will return the BOTTOM value.Upon failure, an empty list is returned.

		"""


	def has_deformations(self) -> bool:

		"""

		This method checks if deformations are loaded on the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def has_scalar(self) -> bool:

		"""

		This method checks if scalars are loaded on the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def has_vector(self) -> bool:

		"""

		This method checks if vectors are loaded on the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_scalar(self) -> bool:

		"""

		This method checks if scalar results are loaded on the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_vector(self) -> bool:

		"""

		This method checks if vector results are loaded on the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def get_deformation_read_options(self) -> object:

		"""

		This method gets the deformation reading options for the state of the resultset.


		Returns
		-------
		object
			It returns a dictionary where each key is the name of a reading option and each value, the value of the reading option. Upon failure, an empty dictionary is returned.

		"""


	def get_scalar_read_options(self) -> object:

		"""

		This method gets the scalar reading options for the state of the resultset.


		Returns
		-------
		object
			It returns a dictionary where each key is the name of a reading option and each value, the value of the reading option. Upon failure, an empty dictionary is returned.

		"""


	def get_vector_read_options(self) -> object:

		"""

		This method gets the vector reading options for the state of the resultset.


		Returns
		-------
		object
			It returns a dictionary where each key is the name of a reading option and each value, the value of the reading option. Upon failure, an empty dictionary is returned.

		"""


	def get_string_deformation_labels(self) -> object:

		"""

		This method gets all deformation labels for the state of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is a string referring to one deformation label of the corresponding state.Upon failure, an empty list is returned.

		"""


	def get_string_scalar_labels(self) -> object:

		"""

		This method gets all scalar labels for the state of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is a string referring to one scalar label of the corresponding state.Upon failure, an empty list is returned.

		"""


	def get_string_vector_labels(self) -> object:

		"""

		This method gets all vector labels for the state of the resultset.


		Returns
		-------
		object
			It returns a list where each member of the list is a string referring to one vector label of the corresponding state.Upon failure, an empty list is returned.

		"""


	def get_id(self) -> int:

		"""

		This method gets the id of the resultset. The result of this function can be used to change states via a META command.


		Returns
		-------
		int
			It returns an integer referring to the id of the given resultset.Upon failure, None is returned.

		"""


	def get_layers(self) -> object:

		"""

		This method gets the layers of the resultset.


		Returns
		-------
		object
			It returns a list with the names of the layers of the given resultset. Layers refer to the layers of the SHELL elements for which scalar or vector values are loaded (e.g. 'bottom', 'top', 'one').Upon failure, an empty list is returned.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the resultset.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes.Upon failure, it returns an empty dictionary.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the resultset.


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


	def generate(self, result_type: str, steps: int, interpolation_type: str, angle: float) -> object:

		"""

		This method generates new resultsets from a given resultset.


		Parameters
		----------
		result_type : str
			Type of the data of the resultset. Its possible values are:
			- 'deform': deformation data
			- 'function': function data
			- 'all': deformation and function data

		steps : int
			Number of steps that will be generated.

		interpolation_type : str
			Type of the interpolation. Its possible values are:
			- 'linear': linear
			- 'cos': cosine
			- 'sin': sine

		angle : float, optional
			Angle to fill. It should be specified only if type is 'cos' or 'sin'. If it is absent then the default value is 360.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Result referring to one resultset.Upon failure, an empty list is returned.

		"""


	def clear(self, result_type: str) -> bool:

		"""

		This method deletes the data of the resultset.


		Parameters
		----------
		result_type : str, optional
			Type of the data of the resultset. Possible values are:
			- 'deform': Deformation data
			- 'function': Function data.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This function deletes the resultset.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def copy_deformations(self, specifier: str, resultset: object, new_name: str) -> bool:

		"""

		This method copies deformation data of all nodes from an other resultset.Both source and target resultsets must belong to the same model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : copy the deformations of all labels.
			- 'one' : copy the deformations of the label of the resultset.

		resultset : object
			An object of class Result that refers to the source Resultset of the model.

		new_name : str, optional
			The new name for the deformation data of the target resultset. If it is absent, then the default label name is used.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def copy_scalar(self, specifier: str, resultset: object, new_name: str) -> bool:

		"""

		This method copies scalar data of all elements from an other resultset.Both source and target resultsets must belong to the same model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : copy the scalar of all labels.
			- 'one' : copy the scalar of the label of the resultset.

		resultset : object
			An object of class Result that refers to the source Resultset of the model.

		new_name : str, optional
			The new name for the scalar data of the target resultset. If it is absent, then the default label name is used.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def copy_vector(self, specifier: str, resultset: object, new_name: str) -> bool:

		"""

		This method copies vector data of all elements from an other resultset.Both source and target resultsets must belong to the same model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : copy the vector of all labels.
			- 'one' : copy the vector of the label of the resultset.

		resultset : object
			An object of class Result that refers to the source Resultset of the model.

		new_name : str, optional
			The new name for the vector data of the target resultset. If it is absent, then the default label name is used.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def copy_function(self, specifier: object, resultset: object, new_name: str) -> bool:

		"""

		This method copies function data (scalar and vector) of all elements from an other resultset.Both source and target resultsets must belong to the same model.


		Parameters
		----------
		specifier : object
			Specifier of the method. Its possible values are:
			- 'all' : copy the function of all labels.
			- 'one' : copy the function of the label of the resultset.

		resultset : object
			An object of class Result that refers to the source Resultset of the model.

		new_name : str, optional
			The new name for the data of the target resultset. If it is absent, then the default label name is used.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Result entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Deformation():

	"""

	Class for deformations.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    deforms = models.MaxDeformationOfModel(result)
		    max_deform = models.MaxDeformationOfModel(result)
		    if len(max_deform):
		        max_x_deform = max_deform[0]  # Object with maximum deformation in direction X
		        print(
		            max_x_deform.x, max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the maximum X deformation
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[1]  # Object with maximum deformation in direction Y
		        print(
		            max_y_deform.x, max_y_deform.y, max_y_deform.z, max_y_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the maximum Y deformation
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[2]  # Object with maximum deformation in direction Z
		        print(
		            max_z_deform.x, max_z_deform.y, max_z_deform.z, max_z_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the maximum Z deformation
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z deformation
		
		        max_total_deform = max_deform[3]  # Object with maximum TOTAL deformation
		        print(
		            max_total_deform.x,
		            max_total_deform.y,
		            max_total_deform.z,
		            max_total_deform.total,
		        )  # Deformations in X, Y, Z and Total directions on the node with the maximum TOTAL deformation
		        print(
		            max_total_deform.node_id
		        )  # Id of the node with the maximum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()

	"""


	node_id: int = None
	"""
	Node id.

	"""

	x: float = None
	"""
	X deformation.

	"""

	y: float = None
	"""
	Y deformation.

	"""

	z: float = None
	"""
	Z deformation.

	"""

	total: float = None
	"""
	Total deformation.

	"""
class ModalDeformation():

	"""

	Class for modal deformations

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import results
		
		
		def main():
		    model_id = 0
		    filename = "/home/examples/structure_cavity.op2"
		    deck = "NASTRAN"
		    range = "1-2"
		    states = utils.RangeToList(range)
		    data = "Displacements,Translational"
		    range = "1727-1728"
		    node_ids = utils.RangeToList(range)
		    complex = "real"
		    all_states = results.LoadModalDeformations(
		        model_id, filename, deck, states, data, node_ids, complex
		    )
		    for one_state in all_states:
		        all_deform = one_state[2]  # List with modal deformations
		        for modal_deform in all_deform:
		            print(modal_deform)
		            print(modal_deform.x, modal_deform.y, modal_deform.z)  # X,Y,Z deformation
		            print(
		                modal_deform.rx, modal_deform.ry, modal_deform.rz
		            )  # X,Y,Z Rotational deformation
		            print(modal_deform.node_id)  # Node id
		
		
		if __name__ == "__main__":
		    main()

	"""


	node_id: int = None
	"""
	Node id.

	"""

	x: float = None
	"""
	X deformation.

	"""

	y: float = None
	"""
	Y deformation.

	"""

	z: float = None
	"""
	Z deformation.

	"""

	rx: float = None
	"""
	Rotational X deformation.

	"""

	ry: float = None
	"""
	Rotational Y deformation.

	"""

	rz: float = None
	"""
	Rotational Z deformation.

	"""
class NodalScalar():

	"""

	Class for nodal scalar results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    all_elems = elements.Elements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        elem_nodal = elements.NodalScalarOfElement(result, e.type, e.id, e.second_id)
		        if elem_nodal:
		            for nodal in elem_nodal:
		                print(nodal.value)  # Nodal scalar value
		                print(nodal.node_id)  # Id of the node
		                print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()

	"""


	node_id: int = None
	"""
	Node id.

	"""

	part_id: int = None
	"""
	Id of the part of the nodal scalar value, or -1 for nodes not belonging to a part.

	"""

	value: float = None
	"""
	Scalar value.

	"""
class CentroidScalar():

	"""

	Class for centroid scalar results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    all_elems = elements.Elements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        centroid = elements.CentroidScalarOfElement(result, e.type, e.id, e.second_id)
		        if centroid:
		            print(centroid.value)  # Centroid scalar value of the element
		            print(
		                centroid.element_id, centroid.second_id, centroid.type
		            )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()

	"""


	element_id: int = None
	"""
	Element id.

	"""

	second_id: int = None
	"""
	Element second id.

	"""

	type: int = None
	"""
	Element type.

	"""

	value: float = None
	"""
	Scalar value.

	"""
class CornerScalar():

	"""

	Class for corner scalar results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import elements
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    all_elems = elements.VisibleElements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        corners = elements.CornerScalarOfElement(result, e.type, e.id, e.second_id)
		        for corn in corners:
		            if corn:
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


	value: float = None
	"""
	Scalar value.

	"""

	element_id: int = None
	"""
	Element id.

	"""

	second_id: int = None
	"""
	Element second id.

	"""

	type: int = None
	"""
	Element type.

	"""

	corner: int = None
	"""
	Node id for shell end solid elements, or the fraction of the distance
	from the start to the total distance for line elements.

	"""
class NodalVector():

	"""

	Class for nodal vector results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[13]
		    all_elems = elements.Elements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        elem_nodal = elements.NodalVectorOfElement(result, e.type, e.id, e.second_id)
		        if elem_nodal:
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


	value: float = None
	"""
	Vector magnitude value.

	"""

	x: float = None
	"""
	Normalized coordinate X of vector.

	"""

	y: float = None
	"""
	Normalized coordinate Y of vector.

	"""

	z: float = None
	"""
	Normalized coordinate Z of vector.

	"""

	node_id: int = None
	"""
	Node id.

	"""

	part_id: int = None
	"""
	Id of the part of the node, or -1 for nodes not belonging to a part.

	"""
class CentroidVector():

	"""

	Class for centroid vector results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    all_elems = elements.Elements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        centroid = elements.CentroidVectorOfElement(result, e.type, e.id, e.second_id)
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


	value: float = None
	"""
	Vector magnitude value.

	"""

	x: float = None
	"""
	Normalized coordinate X of vector.

	"""

	y: float = None
	"""
	Normalized coordinate Y of vector.

	"""

	z: float = None
	"""
	Normalized coordinate Z of vector.

	"""

	element_id: int = None
	"""
	Element id.

	"""

	second_id: int = None
	"""
	Element second id.

	"""

	type: int = None
	"""
	Element type.

	"""
class CornerVector():

	"""

	Class for corner vector results.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import elements
		
		
		def main():
		    model_id = 0
		    all_results = results.Resultsets(model_id)
		    result = all_results[1]
		    all_elems = elements.VisibleElements(model_id)
		    iter_end = min(10, len(all_elems))
		    for e in all_elems[0:iter_end]:
		        corners = elements.CornerVectorOfElement(result, e.type, e.id, e.second_id)
		        for corn in corners:
		            if corn:
		                print(corn)
		
		
		if __name__ == "__main__":
		    main()

	"""


	value: float = None
	"""
	Scalar value

	"""

	x: float = None
	"""
	X component value

	"""

	y: float = None
	"""
	Y component value

	"""

	z: float = None
	"""
	Z component value

	"""

	element_id: int = None
	"""
	Element id.

	"""

	second_id: int = None
	"""
	Element second id.

	"""

	type: int = None
	"""
	Element type.

	"""

	corner: float = None
	"""
	Node id for shell end solid elements, or the fraction of the distance
	from the start to the total distance for line elements.

	"""
