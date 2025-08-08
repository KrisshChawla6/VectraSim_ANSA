from __future__ import annotations
from typing import *

def AddNameOnNode(node_id: int, node_name: int, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.set_name` instead.


	This function defines a name for a node of a given model.

	Parameters
	----------
	node_id : int
		Id of the node.

	node_name : int
		Name of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    node_name = "FIXED_GRID 164"
		    nodes.AddNameOnNode(model_id, node_id, node_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.set_name instead.", DeprecationWarning)

def AddNameOnSomeNodes(node_ids: int, node_names: int, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_name_on_nodes` instead.


	This function defines names for some specific nodes of a given model.

	Parameters
	----------
	node_ids : int
		List with ids of the nodes.

	node_names : int
		List with node names.

	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    visnodes = nodes.VisibleNodes(model_id)
		    node_ids = list()
		    node_names = list()
		    for n in visnodes:
		        node_ids.append(n.id)
		        node_names.append("VISIBLE GRID")
		    nodes.AddNameOnSomeNodes(model_id, node_ids, node_names)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_name_on_nodes instead.", DeprecationWarning)

def AdvFiltersOnNodes(model_id: int, adv_filters: object, result: object, sort: bool) -> object:

	"""

	This function allows the user to collect nodes of a model specified by the given id through some advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	adv_filters : object
		A list with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filters.

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
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Nodes:id:<1000:Keep All")
		    adv_filters.append("intersect:Nodes:nodefunc:>100:Keep All")
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    collected_nodes = nodes.AdvFiltersOnNodes(model_id, adv_filters, result)
		    for n in collected_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToXAxis(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global X-axis.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToXAxis(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToXYPlane(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global XY plane.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToXYPlane(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToYAxis(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global Y-axis.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToYAxis(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToYZPlane(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global YZ plane.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToYZPlane(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToZAxis(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global Z-axis.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToZAxis(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleLineToZXPlane(node2_data: object, node1_data: object) -> float:

	"""

	This function calculates the angle of a line defined by 2 nodes of some existing models for some specific resultsets and the global ZX plane.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    angle = nodes.AngleLineToZXPlane(node1_data, node2_data)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleOfNodes(node1_data: object, node2_data: object, node3_data: object, projection: str) -> float:

	"""

	This function calculates the angle of 3 nodes of some existing models for some specific resultsets.

	Parameters
	----------
	node1_data : object
		List with data of the 1st node.

	node2_data : object
		List with data of the 2nd node.

	node3_data : object
		List with data of the 3rd node.

	projection : str, optional
		Projection of the angle.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle of the 3 nodes in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    node3_data = list()
		
		    node3_data.append(1849)
		    node3_data.append(model_id)
		    node3_data.append(result)
		
		    projection = "normal"
		
		    angle = nodes.AngleOfNodes(node1_data, node2_data, node3_data, projection)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AngleOfVectors(node2_data: object, node3_data: object, node4_data: object, projection: str, node1_data: object) -> float:

	"""

	This function calculates the angle of 2 vectors specified by their nodes.

	Parameters
	----------
	node2_data : object
		List with data of the 2nd node.

	node3_data : object
		List with data of the 3rd node.

	node4_data : object
		List with data of the 4th node.

	projection : str
		Projection of the angle.

	node1_data : object
		List with data of the 1st node.

	Returns
	-------
	float
		Upon success, it returns a float value referring to the angle of the 2 vectors in degrees.
		Upon failure, an invalid value of -1000 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node1_data = list()
		    node1_data.append(1278)
		    node1_data.append(model_id)
		    node1_data.append(result)
		
		    node2_data = list()
		    node2_data.append(1956)
		    node2_data.append(model_id)
		    node2_data.append(result)
		
		    node3_data = list()
		    node3_data.append(1849)
		    node3_data.append(model_id)
		    node3_data.append(result)
		
		    node4_data = list()
		    node4_data.append(1852)
		    node4_data.append(model_id)
		    node4_data.append(result)
		
		    projection = "xy"
		    angle = nodes.AngleOfVectors(
		        node1_data, node2_data, node3_data, node4_data, projection
		    )
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ApplyFollowNodes(follow_nodes: object, model_id: int) -> int:

	"""

	This function applies follow nodes on the model specified by the given id.

	Parameters
	----------
	follow_nodes : object
		A list of node ids as integers to follow.

	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    follow_nodes = list()
		    follow_nodes.append(1269)
		    follow_nodes.append(1376)
		    follow_nodes.append(1580)
		    nodes.ApplyFollowNodes(model_id, follow_nodes)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewNodesEnd() -> object:

	"""

	This function ends recording the creation of new nodes. This function should be preceded by a corresponding call to script function CollectNewNodesStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific newly created node.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import utils
		
		
		def main():
		    nodes.CollectNewNodesStart()
		
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		
		    new_nodes = nodes.ReportNewNodes()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_nodes = nodes.CollectNewNodesEnd()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewNodesStart() -> int:

	"""

	This function starts recording the creation of new nodes. This function should be followed by a corresponding call to script function CollectNewNodesEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import utils
		
		
		def main():
		    nodes.CollectNewNodesStart()
		
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		
		    new_nodes = nodes.ReportNewNodes()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_nodes = nodes.CollectNewNodesEnd()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CommentsOfNode(node_id: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_comments` instead.


	This function finds the comments of a node with a specific id of a given model. Comments refer to various information which are output in the solver's input file.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the comments of the node with the specified id of the given model.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    node_comments = nodes.CommentsOfNode(model_id, node_id)
		    print(node_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_comments instead.", DeprecationWarning)

def CoordinatesOfNode(result: object, node_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_coordinates` instead.


	This function calculates the coordinates in each direction (X, Y, Z) of a node of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	node_id : int
		Id of the node.

	Returns
	-------
	object
		It returns a Node object of the specified node with the calculated coordinates.
		Upon failure, None is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node_id = 1
		    n = nodes.CoordinatesOfNode(result, node_id)
		    if n:
		        print(n.x)  # X coordinate
		        print(n.y)  # Y coordinate
		        print(n.z)  # Z coordinate
		        print(n.id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_coordinates instead.", DeprecationWarning)

def DeformationOfNode(node_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_deformations` instead.


	This function calculates deformation for each direction (X, Y, Z, TOTAL), for a node with specific id of a given model.

	Parameters
	----------
	node_id : int
		Id of the node.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a Deformation object of the corresponding deformation for the specified node.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node_id = 1
		    deform = nodes.DeformationOfNode(result, node_id)
		    if deform:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_deformations instead.", DeprecationWarning)

def DistanceNodeToElement(node_model: int, node_result, node_id: int, element_model: int, element_result: object, element_type: int, element_id: int, second_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_element` instead.


	This function calculates the distance or the elongation of a node from an element.

	Parameters
	----------
	node_model : int
		Id of the model of the node.

	node_result : 
		An object of class Result that refers to a Resultset of the model of the node.

	node_id : int
		Id of the node.

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
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		from meta import constants
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1
		
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		
		    distance = nodes.DistanceNodeToElement(
		        node_model,
		        node_result,
		        node_id,
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        second_id,
		    )
		    # distance = nodes.DistanceNodeToElement(node_model, node_result, node_id, element_model, element_result, element_type, element_id, second_id, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_element instead.", DeprecationWarning)

def DistanceNodeToGroup(node_model: int, node_result, node_id: int, group_model: int, group_result, group_name: str, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_group` instead.


	This function calculates the distance or the elongation of a node from a group.

	Parameters
	----------
	node_model : int
		Id of the model of the node.

	node_result : 
		An object of class Result that refers to a Resultset of the model of the node.

	node_id : int
		Id of the node.

	group_model : int
		Id of the model of the group.

	group_result : 
		An object of class Result that refers to a Resultset of the model of the node.

	group_name : str
		Name of the group.

	group_instance : int, optional
		Instance of the group. If it is absent, default value is 1.

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
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1
		
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		    group_instance = 1
		
		    distance = nodes.DistanceNodeToGroup(
		        node_model,
		        node_result,
		        node_id,
		        group_model,
		        group_result,
		        group_name,
		        group_instance,
		    )
		    # distance = nodes.DistanceNodeToGroup(node_model, node_result, node_id, group_model, group_result, group_name, group_instance, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_group instead.", DeprecationWarning)

def DistanceNodeToLine(node_model: int, node_result, node_id: int, node1_model: int, node1_result, line_node1: int, node2_model: int, node2_result, line_node2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_line` instead.


	This function calculates the distance or the elongation of a node from a line.

	Parameters
	----------
	node_model : int
		Id of the model of the node.

	node_result : 
		An object of class Result that refers to a Resultset of the model of the node.

	node_id : int
		Id of the node.

	node1_model : int
		Id of the model of the 1st node of the line.

	node1_result : 
		An object of class Result that refers to a Resultset of the model of the 1st node of the line.

	line_node1 : int
		Id of the 1st node of the line.

	node2_model : int
		Id of the model of the 2nd node of the line.

	node2_result : 
		An object of class Result that refers to a Resultset of the model of the 2nd node of the line.

	line_node2 : int
		Id of the 2nd node of the line.

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
		from meta import nodes
		from meta import results
		from meta import constants
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    line_node1 = 1734
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    line_node2 = 1836
		
		    distance = nodes.DistanceNodeToLine(
		        node_model,
		        node_result,
		        node_id,
		        node1_model,
		        node1_result,
		        line_node1,
		        node2_model,
		        node2_result,
		        line_node2,
		    )
		    # distance = nodes.DistanceNodeToLine(node_model, node_result, node_id, node1_model, node1_result, line_node1, node2_model, node2_result, line_node2, elongation =1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_line instead.", DeprecationWarning)

def DistanceNodeToLineCoords(model_id: int, result: object, node_id: int, point1: object, point2: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_line_coords` instead.


	This function calculates the distance or the elongation of a node from a line.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	node_id : int
		Id of the node.

	point1 : object
		List with the coordinates of the 1st point of the line.

	point2 : object
		List with the coordinates of the 2nd point of the line.

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
		from meta import nodes
		from meta import results
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1
		    point1 = list()
		
		    point1.append(0.25)
		    point1.append(1.32)
		    point1.append(7.39)
		
		    point2 = list()
		
		    point2.append(0.35)
		    point2.append(4.49)
		    point2.append(-2.3)
		
		    distance = nodes.DistanceNodeToLineCoords(
		        node_model, node_result, node_id, point1, point2
		    )
		    # distance = nodes.DistanceNodeToLineCoords(node_model, node_result, node_id, point1, point2, elongation =1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_line_coords instead.", DeprecationWarning)

def DistanceNodeToNode(model1_id: int, result1: object, node1_id: int, model2_id: int, result2: object, node2_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_node` instead.


	This function calculates the distance or the elongation of a node from another node.

	Parameters
	----------
	model1_id : int
		Id of the model of the 1st node.

	result1 : object
		An object of class Result that refers to a Resultset of the model of the 1st node.

	node1_id : int
		Id of the 1st node.

	model2_id : int
		Id of the model of the 2nd node.

	result2 : object
		An object of class Result that refers to a Resultset of the model of the 2nd node.

	node2_id : int
		Id of the 2nd node.

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
		from meta import nodes
		from meta import results
		from meta import constants
		
		
		def main():
		    model1_id = 0
		    all_resultsets = results.Resultsets(model1_id)
		    result1 = all_resultsets[1]
		    node1_id = 1239
		
		    model2_id = 0
		    all_resultsets = results.Resultsets(model2_id)
		    result2 = all_resultsets[1]
		    node2_id = 1483
		
		    distance = nodes.DistanceNodeToNode(
		        model1_id, result1, node1_id, model2_id, result2, node2_id
		    )
		    # distance = nodes.DistanceNodeToNode(model1_id, result1, node1_id, model2_id, result2, node2_id, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_node instead.", DeprecationWarning)

def DistanceNodeToPart(node_model: int, node_result: object, node_id: int, part_model: int, part_result: object, part_type: int, part_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_part` instead.


	This function calculates the distance or the elongation of a node from a part.

	Parameters
	----------
	node_model : int
		Id of the model of the node.

	node_result : object
		An object of class Result that refers to a Resultset of the model of the node.

	node_id : int
		Id of the node.

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
		It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
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
		from meta import nodes
		from meta import results
		from meta import constants
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1
		
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1
		
		    distance = nodes.DistanceNodeToPart(
		        node_model, node_result, node_id, part_model, part_result, part_type, part_id
		    )
		    # distance = nodes.DistanceNodeToPart(node_model, node_result, node_id, part_model, part_result, part_type, part_id, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_part instead.", DeprecationWarning)

def DistanceNodeToPlane(node_model: int, node_result: object, node_id: int, node1_model: int, node1_result: object, plane_node1: int, node2_model: int, node2_result: object, plane_node2: int, node3_model: int, node3_result: object, plane_node3: int, elongation: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_plane` instead.


	This function calculates the distance or the elongation of a node from a plane.

	Parameters
	----------
	node_model : int
		Id of the model of the node.

	node_result : object
		An object of class Result that refers to a Resultset of the model of the node.

	node_id : int
		Id of the node.

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
	int
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
		from meta import nodes
		from meta import results
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 239
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    plane_node1 = 1731
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    plane_node2 = 1832
		
		    node3_model = 0
		    all_resultsets = results.Resultsets(node3_model)
		    node3_result = all_resultsets[1]
		    plane_node3 = 1539
		
		    distance = nodes.DistanceNodeToPlane(
		        node_model,
		        node_result,
		        node_id,
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
		    # distance = nodes.DistanceNodeToPlane(node_model, node_result, node_id, node1_model, node1_result, plane_node1, node2_model, node2_result, plane_node2, node3_model, node3_result, plane_node3, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_plane instead.", DeprecationWarning)

def DistanceNodeToPlaneCoords(model_id: int, result, node_id: int, point1: object, point2: object, point3: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_plane_coords` instead.


	This function calculates the distance or the elongation of a node from a plane.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : 
		An object of class Result that refers to a Resultset of the model.

	node_id : int
		Id of the node.

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
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    node_id = 136
		
		    point1 = list()
		    point1.append(0.25)
		    point1.append(1.32)
		    point1.append(7.39)
		
		    point2 = list()
		    point2.append(0.35)
		    point2.append(4.49)
		    point2.append(-2.3)
		
		    point3 = list()
		    point3.append(1.35)
		    point3.append(2.49)
		    point3.append(-3.3)
		
		    distance = nodes.DistanceNodeToPlaneCoords(
		        model_id, result, node_id, point1, point2, point3
		    )
		    # distance = nodes.DistanceNodeToPlaneCoords(model_id, result, node_id, point1, point2, point3, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_plane_coords instead.", DeprecationWarning)

def FollowNodes(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function collects all follow nodes of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific follow node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    follow_nodes = nodes.FollowNodes(model_id)
		    for n in follow_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def FreeNodes(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function collects all free nodes of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific free node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    free_nodes = nodes.FreeNodes(model_id)
		    for n in free_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def IdentifiedNodes(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function collects all identified nodes of the model specified by the given id.

	Parameters
	----------
	window_name : str
		Name of the window of the model. If it is absent then this function will collect identified nodes for all the enabled windows of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific identified node of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    identified_nodes = nodes.IdentifiedNodes(model_id, window_name)
		    for n in identified_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def IdentifiedNodesOfGroup(model_id: int, group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function collects all identified nodes of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect identified nodes for all the enabled windows of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific identified node of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    window_name = "MetaPost"
		    identified_nodes = nodes.IdentifiedNodesOfGroup(model_id, group_name, window_name)
		    for n in identified_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def IdentifiedNodesOfGroupInstance(model_id: int, group_name: str, group_instance: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function collects all identified nodes of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect identified nodes for all the enabled windows of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific identified node of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    window_name = "MetaPost"
		    identified_nodes = nodes.IdentifiedNodesOfGroupInstance(
		        model_id, group_name, group_instance, window_name
		    )
		    for n in identified_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def IdentifyNode(model_id: int, node_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.identify` instead.


	This function allows the user to identify a node of a model specified by a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	node_id : int
		Id of the node.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	nodes.IdentifySomeNodes

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    ret = nodes.IdentifyNode(model_id, node_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.identify instead.", DeprecationWarning)

def IdentifySomeNodes(model_id: int, node_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_nodes` instead.


	This function allows the user to identify some specific nodes of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	node_ids : object
		List with ids of the nodes.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_nodes = nodes.Nodes(model_id)
		    node_ids = list()
		    iter_end = min(10, len(all_nodes))
		    for n in all_nodes[0:iter_end]:
		        node_ids.append(n.id)
		    ret = nodes.IdentifySomeNodes(model_id, node_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_nodes instead.", DeprecationWarning)

def IsNode(node: object) -> int:

	"""

	This function checks whether an object is of class node.

	Parameters
	----------
	node : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Node, 0 otherwise.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    all_nodes = nodes.Nodes(model_id)
		    all_entities = list()
		    all_entities.append(all_nodes[0])
		    all_entities.append("A string")
		    for ent in all_entities:
		        if nodes.IsNode(ent):
		            n = ent
		            print("This is an object of class Node")
		            print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		        else:
		            print("This is NOT an object of class Node")
		
		
		if __name__ == "__main__":
		    main()


	"""

def NameOfNode(node_id: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_name` instead.


	This function finds the name of a node with a specific id of a given model.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the name of the node with the specified id
		of the given model.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    node_name = nodes.NameOfNode(model_id, node_id)
		    print(node_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_name instead.", DeprecationWarning)

def NearestElementOfGroup(point_coords: object, model_id: int, group_name: str, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function finds the nearest element of a given group from a specific point.

	Parameters
	----------
	point_coords : object
		Coordinates of the point.

	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	result : 
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Element referring to the nearest element of the given group from the specified point.
		Upon failure, None is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		
		    e = nodes.NearestElementOfGroup(coords, model_id, group_name)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def NearestElementOfGroupInstance(point_coords: object, model_id: int, group_name: str, group_instance: int, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_elements` instead.


	This function finds the nearest element of a given group instance from a specific point.

	Parameters
	----------
	point_coords : object
		Coordinates of the point.

	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	result : 
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Element referring to the nearest element of the given group from the specified point.
		Upon failure, None is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		
		    e = nodes.NearestElementOfGroupInstance(
		        coords, model_id, group_name, group_instance
		    )
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_elements instead.", DeprecationWarning)

def NearestElementOfMaterial(material_id: int, material_type: int, model_id: int, result: object, point_coords: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_elements` instead.


	This function finds the nearest element of a given material from a specific point.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	point_coords : object, optional
		A list with coordinates of the point.

	Returns
	-------
	object
		It returns an object of class Element referring to the nearest element of the given material from the specified point.
		Upon failure, a non valid Elem object is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		
		    e = nodes.NearestElementOfMaterial(coords, model_id, material_type, material_id)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_elements instead.", DeprecationWarning)

def NearestElementOfModel(model_id: int, result: object, point_coords: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function finds the nearest element of a given model from a specific point.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	point_coords : object
		List with coordinates of the point.

	Returns
	-------
	object
		Upon success, it returns an object of class Element referring to the nearest element of the given model from the specified point.
		Upon failure, a non valid Elem object is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		
		    e = nodes.NearestElementOfModel(coords, model_id)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def NearestElementOfPart(model_id: int, part_id: int, part_type, result: object, point_coords: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_elements` instead.


	This function finds the nearest element of a given part from a specific point.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	part_type : 
		Type of the part (META constant).

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	point_coords : object
		Coordinates of the point (list of floats).

	Returns
	-------
	object
		It returns an object of class Element referring to the nearest element of the 
		given part from the specified point.
		Upon failure, a non valid Elem object is returned.

	See Also
	--------
	results.Result, elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		
		    e = nodes.NearestElementOfPart(coords, model_id, part_type, part_id)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_elements instead.", DeprecationWarning)

def NearestNodeOfGroup(point_coords: object, model_id: int, group_name: str, distance_type: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function finds the nearest node of a given group from a specific point.

	Parameters
	----------
	point_coords : object
		A list with the XYZ-coordinates of the point.

	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	distance_type : str
		Type of the distance. Possible values are:
		- 'xyz': XYZ distance
		- 'xy': XY distance
		- 'yz': YZ distance
		- 'zx': ZX distance
		- 'x': X distance
		- 'y': Y distance
		- 'z': Z distance

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Node referring to the nearest node of the given group from the specified point.
		Upon failure, a non valid Node object is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		    distance_type = "xyz"
		
		    n = nodes.NearestNodeOfGroup(coords, model_id, group_name, distance_type)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def NearestNodeOfGroupInstance(point_coords: object, model_id: int, group_name: str, group_instance: int, distance_type: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function finds the nearest node of a given group instance from a specific point.

	Parameters
	----------
	point_coords : object
		A list with the XYZ-coordinates of the point.

	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	distance_type : str
		Type of the distance. Possible values are:
		- 'xyz': XYZ distance
		- 'xy': XY distance
		- 'yz': YZ distance
		- 'zx': ZX distance
		- 'x': X distance
		- 'y': Y distance
		- 'z': Z distance

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Node referring to the nearest node of the given group from the specified point.
		Upon failure, a non valid Node object is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		    distance_type = "xyz"
		
		    n = nodes.NearestNodeOfGroupInstance(
		        coords, model_id, group_name, group_instance, distance_type
		    )
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def NearestNodeOfMaterial(point_coords: object, model_id: int, material_type: int, material_id: int, distance_type: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodes` instead.


	This function finds the nearest node of a given material from a specific point.

	Parameters
	----------
	point_coords : object
		A list with the XYZ-coordinates of the point.

	model_id : int
		Id of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	distance_type : str
		Type of the distance. Possible values are:
		- 'xyz': XYZ distance
		- 'xy': XY distance
		- 'yz': YZ distance
		- 'zx': ZX distance
		- 'x': X distance
		- 'y': Y distance
		- 'z': Z distance

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns an object of class Node referring to the nearest node of the given group from the specified point.
		Upon failure, None is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		    distance_type = "xyz"
		
		    n = nodes.NearestNodeOfMaterial(
		        coords, model_id, material_type, material_id, distance_type
		    )
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodes instead.", DeprecationWarning)

def NearestNodeOfModel(distance_type: str, model_id: int, result, point_coords: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nearest node of a given model from a specific point.

	Parameters
	----------
	distance_type : str
		Type of the distance. Possible values are:
		- 'xyz': XYZ distance
		- 'xy': XY distance
		- 'yz': YZ distance
		- 'zx': ZX distance
		- 'x': X distance
		- 'y': Y distance
		- 'z': Z distance

	model_id : int
		Id of the model.

	result : 
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	point_coords : object
		A list with the XYZ-coordinates of the point.

	Returns
	-------
	object
		It returns an object of class Node referring to the nearest node of the given group from the specified point.
		Upon failure, None is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		    distance_type = "xyz"
		
		    n = nodes.NearestNodeOfModel(coords, model_id, distance_type)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NearestNodeOfPart(distance_type: str, model_id: int, part_id: int, part_type: int, result, point_coords: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodes` instead.


	This function finds the nearest node of a given part from a specific point.

	Parameters
	----------
	distance_type : str, optional
		Type of the distance. Possible values are:
		- 'xyz': XYZ distance
		- 'xy': XY distance
		- 'yz': YZ distance
		- 'zx': ZX distance
		- 'x': X distance
		- 'y': Y distance
		- 'z': Z distance

	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	part_type : int
		Type of the part (META constant).

	result : , optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	point_coords : object
		Coordinates of the point.

	Returns
	-------
	object
		Upon success, it returns an object of class Node referring to the nearest node of the given group from the specified point.
		Upon failure, a non valid Node object is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    coords = list()
		    coords.append(-73.799500)
		    coords.append(-110)
		    coords.append(3.000000)
		    distance_type = "xyz"
		
		    n = nodes.NearestNodeOfPart(coords, model_id, part_type, part_id, distance_type)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodes instead.", DeprecationWarning)

def NodalScalarOfNode(layer: str, node_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_nodal_scalar` instead.


	This function calculates nodal scalar value(s) of a node with a specific id of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	node_id : int
		Id of the node.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalScalar referring to the nodal scalar value of the specified node.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    node_id = 1
		    layer = "bottom"  # BOTTOM values if both bottom and top values are loaded
		    all_nodal = nodes.NodalScalarOfNode(result, node_id, layer)
		    for nodal in all_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfNode(layer: str, node_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_nodal_vector` instead.


	This function calculates nodal vector values of a node with a specific id of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	node_id : int
		Id of the node.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalVector referring to the nodal vector value of the specified node.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    node_id = 7747
		    all_nodal = nodes.NodalVectorOfNode(result, node_id)
		    for nodal in all_nodal:
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_nodal_vector instead.", DeprecationWarning)

def NodeById(node_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds node of a model with a given id.

	Parameters
	----------
	node_id : int
		Id of the node.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class Node with the given id.
		Else, None is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    n = nodes.NodeById(model_id, node_id)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def Nodes(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function collects all nodes of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_nodes = nodes.Nodes(model_id)
		    iter_end = min(10, len(all_nodes))
		    for n in all_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NodesByComments(node_comments: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model with specific comments.

	Parameters
	----------
	node_comments : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_comments = "GSM*"
		    matnodes = nodes.NodesByComments(model_id, node_comments)
		    for n in matnodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NodesByField10(node_field10: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model with a given field10 value.

	Parameters
	----------
	node_field10 : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_field10 = "*"
		    matnodes = nodes.NodesByField10(model_id, node_field10)
		    for n in matnodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NodesByName(node_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model with a given name.

	Parameters
	----------
	node_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_name = "*GRID*"
		    named_nodes = nodes.NodesByName(model_id, node_name)
		    for n in named_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NodesFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect nodes of a model specified by the given id through an advanced filter. The execution of the script will stop and a window will open in order to specify the advanced filter.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		    collected_nodes = nodes.NodesFromAdvFilters(model_id, resultset)
		    for n in collected_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodesListToDict(nodes: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Node.

	Parameters
	----------
	nodes : object
		List with objects of class Node.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the node and member the corresponding Node object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    all_nodes = nodes.IdentifiedNodes(model_id)
		    dict_nodes = nodes.NodesListToDict(all_nodes)
		    for node_id, n in dict_nodes.items():
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodesOfBoundary(boundary_id: int, boundary_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodes` instead.


	This function collects all nodes of a boundary element with a given id and type.

	Parameters
	----------
	boundary_id : int
		Id of the boundary element.

	boundary_type : int
		Type of the boundary element (META constant).

	second_id : int
		Second id of the boundary element.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given boundary element.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    boundary_nodes = nodes.NodesOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    for n in boundary_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodes instead.", DeprecationWarning)

def NodesOfElement(element_id: int, element_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodes` instead.


	This function collects all nodes of an element with a given id and type.

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
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given element.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    element_nodes = nodes.NodesOfElement(model_id, element_type, element_id, second_id)
		    for n in element_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodes instead.", DeprecationWarning)

def NodesOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function collects all nodes of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    group_nodes = nodes.NodesOfGroup(model_id, group_name, group_instance)
		    iter_end = min(10, len(group_nodes))
		    for n in group_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def NodesOfMaterial(model_id: int, material_type, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodes` instead.


	This function collects all nodes with a given material belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_type : 
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    material_nodes = nodes.NodesOfMaterial(model_id, material_type, material_id)
		    iter_end = min(10, len(material_nodes))
		    for n in material_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodes instead.", DeprecationWarning)

def NodesOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_nodes` instead.


	This function searches for the nodes of an overlay run with a given type and id.

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
		It returns a list wwhere each member of the list is an object of class Node referring to one specific node of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    overlay_run_nodes = nodes.NodesOfOverlayRun(overlay_run_type, overlay_run_id)
		    iter_end = min(10, len(overlay_run_nodes))
		    for n in overlay_run_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_nodes instead.", DeprecationWarning)

def NodesOfPart(part_id: int, part_type, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodes` instead.


	This function collects all nodes of a given part belonging to the specified model.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : 
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    part_nodes = nodes.NodesOfPart(model_id, part_type, part_id)
		    iter_end = min(10, len(part_nodes))
		    for n in part_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodes instead.", DeprecationWarning)

def NodesWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model for which comments exist.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.CommentsOfNode, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    nodes_with_comments = nodes.NodesWithComments(model_id)
		    for n in nodes_with_comments:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NodesWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.NameOfNode, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    nodes_with_name = nodes.NodesWithName(model_id)
		    for n in nodes_with_name:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def NumOfNodes(model_id: int) -> int:

	"""

	This function finds the number of the nodes of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns the number of the nodes for the given model.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    num_of_nodes = nodes.NumOfNodes(model_id)
		    print(num_of_nodes)
		
		
		if __name__ == "__main__":
		    main()


	"""

def OuterNodesOfMaterial(model_id: int, material_type, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodes` instead.


	This function collects all outer nodes of a given material belonging to the specified model. Outer node is the one who belongs to an element which does not belong to the given material.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_type : 
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific outer node of the given material.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    outer_nodes = nodes.OuterNodesOfMaterial(model_id, material_type, material_id)
		    for n in outer_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodes instead.", DeprecationWarning)

def OuterNodesOfPart(part_id: int, part_type, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodes` instead.


	This function collects all outer nodes of a given part belonging to the specified model. Outer node is the one who belongs to an element which does not belong to the given part.

	Parameters
	----------
	part_id : int
		Id of the part.

	part_type : 
		Type of the part (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific outer node of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 1
		    part_type = constants.PSHELL
		    part_id = 1
		    outer_nodes = nodes.OuterNodesOfPart(model_id, part_type, part_id)
		    iter_end = min(10, len(outer_nodes))
		    for n in outer_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodes instead.", DeprecationWarning)

def PickNodes(model_id: int, message: str, pick_settings: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_nodes` instead.


	This function allows the user to pick nodes of a model specified by the given id. If model_id is equal to -1, then this function will work for all models. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	model_id : int
		Id of the model. If it is equal to -1, then the function will work for all models.

	message : str
		Message displayed to the user.

	pick_settings : object, optional
		Argument 'pick_settings' is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. ['front_selection,1', 'polygonal_selection, 1', 'reset_picked, 1']).
		The names of the pick settings and its possible values are:
		- 'front_selection': Disable/Enable front selection (0,1)
		- 'polygonal_selection': Disable/Enable polygonal selection (0,1)
		- 'reset_picked': Resets identification of picked nodes, when turned on (0,1)
		- 'pick_ordered' : Controls if the nodes will be returned with the picked order (0,1)
		- 'one_pick' : Picks without middle click, if turned on (0,1)

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific picked node of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    message = "Select Nodes and press Enter when you are ready"
		    picked_nodes = nodes.PickNodes(model_id, message)
		    for n in picked_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_nodes instead.", DeprecationWarning)

def ReferenceNodeOfElement(element_id: int, element_type, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodes` instead.


	This function finds the reference node of an element with a given id and type. For example, RBE2 and RBE3 elements have reference nodes.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : 
		Type of the element (META constant).

	second_id : int
		Second id of the element.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class Node referring to the corresponding reference node of the element.
		Upon failure, a None is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.RBE2
		    element_id = 1
		    second_id = -1
		    n = nodes.ReferenceNodeOfElement(model_id, element_type, element_id, second_id)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodes instead.", DeprecationWarning)

def ReportNewNodes() -> object:

	"""

	This function collects the newly created nodes from the last call of script function CollectNewNodesStart(). This function should be preceded by a corresponding call to script function CollectNewNodesStart() and should be followed by a corresponding call to script function CollectNewNodesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific newly created node.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import utils
		
		
		def main():
		    nodes.CollectNewNodesStart()
		
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		
		    new_nodes = nodes.ReportNewNodes()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    # create new nodes
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_nodes = nodes.CollectNewNodesEnd()
		    iter_end = min(10, len(new_nodes))
		    for n in new_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ShellNormalOfNode(node_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_shell_normal` instead.


	This function calculates the shell normal vector of a node with a specific id of a given model. The calculation is based on the shell normal vectors of the shell elements which the node belongs to.

	Parameters
	----------
	node_id : int
		Id of the node.

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then nodal normal vectors will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns an object of class NodalVector referring to the shell normal vector of the specified node.
		Upon failure, a non valid NodalVector object is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    node_id = 1
		    shell_normal = nodes.ShellNormalOfNode(result, node_id)
		    if shell_normal:  # Struct with the shell normal vector
		        print(shell_normal.value)  # Magnitude of the shell normal vector (always 1)
		        print(
		            shell_normal.x, shell_normal.y, shell_normal.z
		        )  # Normalized coordinates (X, Y, Z) of the shell normal vector
		        print(shell_normal.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_shell_normal instead.", DeprecationWarning)

def UnsetFollowNodes(model_id: int) -> int:

	"""

	This function unsets follow nodes on the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    ret = nodes.UnsetFollowNodes(model_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateNode(node: object) -> object:

	"""

	This function updates the data of the given Node object. Update is based in the fields 'id' and 'model_id' of the given Node object.

	Parameters
	----------
	node : object
		Object of class Node.

	Returns
	-------
	object
		Upon success, it returns the new updated Node object.
		Else, a non valid Node object is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_id = 1
		    n = nodes.NodeById(model_id, node_id)
		    if n:
		        # commands which alter the data of the node struct
		        # ...
		        n = nodes.UpdateNode(n)
		        if n:  # Update OK
		            print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		        else:  # Update FAILED
		            print("This is not a valid node struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleNodes(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function collects all visible nodes of the model specified by the given id.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node of the given model for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodes(model_id, window_name)
		    iter_end = min(10, len(visible_nodes))
		    for n in visible_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfBoundary(boundary_id: int, boundary_type, second_id: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodes` instead.


	This function collects all visible nodes of a boundary element with a given id and type.

	Parameters
	----------
	boundary_id : int
		Id of the boundary element

	boundary_type : 
		: META Keyword Type of the boundary element

	second_id : int
		Second id of the boundary element.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node of the given boundary element for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodesOfBoundary(
		        model_id, boundary_type, boundary_id, second_id, window_name
		    )
		    for n in visible_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfElement(element_id: int, element_type, second_id: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_nodes` instead.


	This function collects all visible nodes of an element with a given id (element_id) and a given type. Some elements may have a second id (GAP, TUBE, JOINT). For the rest types of elements, the value of second_id is -1. Element type must be one of META KEYWORDS. A full META KEYWORD list for elements can be found under library category "Meta help". Optional argument "window_name" refers to the n

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : 
		Type of the element (META constant).

	second_id : int
		Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node of the given element for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodesOfElement(
		        model_id, element_type, element_id, second_id, window_name
		    )
		    for n in visible_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfGroup(model_id: int, group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function collects all visible nodes of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodesOfGroup(model_id, group_name, window_name)
		    iter_end = min(10, len(visible_nodes))
		    for n in visible_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfGroupInstance(model_id: int, group_name: str, group_instance: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_nodes` instead.


	This function collects all visible nodes of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Instance of the group.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each memeber of the list is an object of class Node referring to one specific visible node of the given group for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "MyGroup"
		    group_instance = 1
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodesOfGroupInstance(
		        model_id, group_name, group_instance, window_name
		    )
		    iter_end = min(10, len(visible_nodes))
		    for n in visible_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfMaterial(model_id: int, material_type: int, material_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodes` instead.


	This function collects all visible nodes with a given material belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node with the given material for the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    window_name = "MetaPost"
		    visible_nodes = nodes.VisibleNodesOfMaterial(
		        model_id, material_type, material_id, window_name
		    )
		    iter_end = min(10, len(visible_nodes))
		    for n in visible_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodes instead.", DeprecationWarning)

def VisibleNodesOfPart(part_id: int, part_type: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodes` instead.


	This function collects all visible nodes of a given part belonging to the specified model. Part type must be one of META KEYWORDS. A full META KEYWORD list for parts can be found under library category "Meta help". 

	Parameters
	----------
	part_id : int
		Id of the material.

	part_type : int
		Type of the material (META constant).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node with the given part for the specified group.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    window_name = "MetaPost"
		
		    visible_nodes = nodes.VisibleNodesOfPart(model_id, part_type, part_id, window_name)
		    iter_end = min(10, len(visible_nodes))
		    for n in visible_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodes instead.", DeprecationWarning)

def VisibleNodesWithComments(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the visible nodes of a model for which comments exist.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the model. If it is absent then this function will work for visible nodes for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to a visible node of the model for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    vis_nodes_with_comments = nodes.VisibleNodesWithComments(model_id, window_name)
		    for n in vis_nodes_with_comments:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def VisibleNodesWithName(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the visible nodes of a model for which a name has been defined.

	Parameters
	----------
	window_name : str
		Name of the window of the model. If it is absent then this function will work for visible nodes for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to a visible node of the model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.NameOfNode, nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    vis_nodes_with_name = nodes.VisibleNodesWithName(model_id, window_name)
		    for n in vis_nodes_with_name:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def VisibleOuterNodesOfMaterial(model_id: int, material_type, material_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodes` instead.


	This function collects the visible outer nodes of a given material belonging to the specified model. Outer node is the one who belongs to an element which does not belong to the given material.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_type : 
		Type of the material (META constant).

	material_id : int
		Id of the material.

	window_name : str
		Name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible outer node of the given material for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    window_name = "MetaPost"
		    vis_outer_nodes = nodes.VisibleOuterNodesOfMaterial(
		        model_id, material_type, material_id, window_name
		    )
		    for n in vis_outer_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodes instead.", DeprecationWarning)

def VisibleOuterNodesOfPart(model_id: int, part_type: int, part_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_nodes` instead.


	This function collects the visible outer nodes of a given part belonging to the specified model. Outer node is the one who belongs to an element which does not belong to the given part.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the material (META constant).

	part_id : int
		Id of the material.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible outer node of the given part for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSOLID
		    part_id = 2
		    window_name = "MetaPost"
		    vis_outer_nodes = nodes.VisibleOuterNodesOfPart(
		        model_id, part_type, part_id, window_name
		    )
		    iter_end = min(10, len(vis_outer_nodes))
		    for n in vis_outer_nodes[0:iter_end]:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_nodes instead.", DeprecationWarning)

def DistanceNodeToCutPlane(node_id: int, node_result, plane_name: str, node_model: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_distance_from_cut_plane` instead.


	This function calculates the distance or the elongation of a node from an existing cut plane.

	Parameters
	----------
	node_id : int
		Id of the node.

	node_result : 
		An object of class Result that refers to a Resultset of the model of the node.

	plane_name : str
		Name of the cut plane.

	node_model : int
		Id of the model of the node.

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
		from meta import nodes
		from meta import results
		
		
		def main():
		    node_model = 0
		    all_resultsets = results.Resultsets(node_model)
		    node_result = all_resultsets[1]
		    node_id = 1278
		    plane_name = "DEFAULT_PLANE_XY"
		    distance = nodes.DistanceNodeToCutPlane(
		        node_model, node_result, node_id, plane_name
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_distance_from_cut_plane instead.", DeprecationWarning)

def CalcAngleOfVectors(vec_2: object, vec_3: object, vec_1: object) -> float:

	"""

	This function computes the angle of two or three 3D vectors.

	Parameters
	----------
	vec_2 : object
		A list defining the second vector.

	vec_3 : object, optional
		A list defining the third vector.

	vec_1 : object
		A list defining the first vector.

	Returns
	-------
	float
		Returns the angle of vectors in radians. When the input list has two vectors the angle is mathematically defined to be between '0' and 'PI' (inclusive). When the input list has three vectors the angle is mathematically defined to be between '0' and '2PI' (inclusive). When the input list is not correct the function returns the error value '-PI' .

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import calc
		
		
		def main():
		    vec1 = [-17.0, 72.0, 0.0]
		    vec2 = [61.0, -43, 0.0]
		    vec3 = [0.0, 0.0, 10.0]
		    m = calc.CalcAngleOfVectors(
		        vec1, vec2
		    )  # The return angle in radians is '2.41668002'
		    m = calc.CalcAngleOfVectors(
		        vec1, vec2, vec3
		    )  # The return angle in radians is '3.86650528'
		
		
		if __name__ == "__main__":
		    main()


	"""

def NodesBySolverId(model_id: int, node_path: str, node_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodes` instead.


	This function finds the nodes of a model with hierarchical structure defined by id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Id of the model.

	node_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given node is limited.

	node_id : int
		Id of the node.

	Returns
	-------
	object
		This function returns a list with objects of class Node referring to the corresponding nodes found.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_path = "Truck->14"
		    node_id = 1046
		    collected_nodes = nodes.NodesBySolverId(model_id, node_path, node_id)
		
		    for n in collected_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodes instead.", DeprecationWarning)

def ALCPointsFromFilename(filename: str) -> object:

	"""

	This function finds A/LC points of a "*.alc_aux" or "*.map" file.

	Parameters
	----------
	filename : str
		Path to file.

	Returns
	-------
	object
		It returns a list with the A/LC points of the given file.
		Each element of the list is another list with 10 elements as follows:
		        In position 0, a string referring to the name of the A/LC point.
		        In position 1, a string referring to A/LC point ids.
		        In position 2, a string referring to A/LC dofs.
		        In position 3, a string referring to all A/LC Set names.
		        In position 4, a string referring to A/LC coordinate X(If defined).
		        In position 5, a string referring to A/LC coordinate Y(If defined).
		        In position 6, a string referring to A/LC coordinate Z(If defined).
		        In position 7, a string referring to A/LC search distance (If defined).
		        In position 8, a string referring to A/LC coordinate system id (If defined).
		        In position 9, a string referring to A/LC type (LC Set, A Point, LC Point).
		Upon failure, a list with zero length is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    filename = "/home/examples/alc_point_example/door/door.alc_aux"
		    all_alcp = nodes.ALCPointsFromFilename(filename)
		    print(
		        "Name\\tIds\\tDof\\tSetNames\\tCoord X\\tCoord Y\\tCoord Z\\tSearch Distance\\tCsys Id\\tType"
		    )
		    for alcp in all_alcp:
		        print(
		            alcp[0],
		            "\\t",
		            alcp[1],
		            "\\t",
		            alcp[2],
		            "\\t",
		            alcp[3],
		            "\\t",
		            alcp[4],
		            "\\t",
		            alcp[5],
		            "\\t",
		            alcp[6],
		            "\\t",
		            alcp[7],
		            "\\t",
		            alcp[8],
		            "\\t",
		            alcp[9],
		            "\\t",
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def SortNodeList(model_id: int, nodes_list: object, first_node_id: int, direction_node_id: int, sort_component: str) -> object:

	"""

	This function sorts all nodes of a given list according to component option.

	Parameters
	----------
	model_id : int
		Id of the model.

	nodes_list : object
		A list of either node ids (integers) or a list of objects of class Node.

	first_node_id : int
		Defines the first node of the sorted list, or the start of the path in case of a circular one. If it is equal to 0, then it is ignored and the whole list is sorted.

	direction_node_id : int
		Specifies the second node id, the one that will define the direction of sorting. It is useful for circular paths. If it is equal to zero, then it will be ignored and no direction node will be used.

	sort_component : str
		Defines the component according to which the initial list is sorted.
		'X' or 'x' : Sorting is done according to x coordinate of nodes.
		'Y' or 'y' : Sorting is done according to y coordinate of nodes.
		'Z' or 'z' : Sorting is done according to z coordinate of nodes.
		'D' or 'd' : Sorting is done according to distance between nodes.
		Any other value: Sorting is done according to distance between nodes.

	Returns
	-------
	object
		It returns a sorted list, where each member of the list is an object of class Node referring to one specific given node of the 'nodes_list' argument.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    group_name = "Model_0>SHELL_PART_197"
		    group_instance = 1
		    nodes_list = nodes.NodesOfGroup(model_id, group_name, group_instance)
		    first_node_id = 7
		    direction_node_id = 79
		    sort_component = "x"
		    sort_nodes = nodes.SortNodeList(
		        model_id, nodes_list, first_node_id, direction_node_id, sort_component
		    )
		    for n in sort_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributesOfNode(model_id: int, node_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_attributes` instead.


	This function collects all attributes of a given node

	Parameters
	----------
	model_id : int
		The number of the model

	node_id : int
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
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    id = 1
		    all_attributes = nodes.AttributesOfNode(model_id, id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_attributes instead.", DeprecationWarning)

def AttributeOfNode(model_id: int, node_id: int, attribute_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The number of the model

	node_id : int
		The id of the node

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
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    id = 1
		    attribute_name = "Position.x"
		    val = nodes.AttributeOfNode(model_id, id, attribute_name)
		    print("Value: " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.get_attributes instead.", DeprecationWarning)

def SetAttributeOfNode(model_num: int, node_id: int, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.nodes.Node.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given node. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_num : int
		The number of the model.

	node_id : int
		The id of the node.

	attribute_name : str
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
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    id = 200
		    name = "Total"
		    val = "100"
		    nodes.SetAttributeOfNode(model_id, id, name, val)
		    # or
		    name = "n_Total"
		    val = 100
		    attribute_type = "numerical"
		    nodes.SetAttributeOfNode(model_id, id, name, val, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.nodes.Node.set_attribute instead.", DeprecationWarning)

def AttributesOfALCPoint(model_id: int, alc_name: str) -> object:

	"""

	This function collects all attributes of a given alc point

	Parameters
	----------
	model_id : int
		The number of the model

	alc_name : str
		The name of the alc point

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given alc point.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		import meta
		from meta import nodes
		
		
		def main():
		    alcname = "alc"
		    model_id = 0
		
		    all_attributes = nodes.AttributesOfALCPoint(model_id, alcname)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributeOfALCPoint(model_id: int, alc_name: str, attrib_name: str) -> str:

	"""

	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The number of the model

	alc_name : str
		The name of the alc point

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	Examples
	--------
	::

		import meta
		from meta import nodes
		
		
		def main():
		    model = 0
		    alcname = "alc_point"
		    attr_name = "Created"
		
		    val = nodes.AttributeOfALCPoint(model, alcname, attr_name)
		    print("Value " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeOfALCPoint(model_id: int, alc_name: str, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""

	This function sets the value of a specific User Specified attribute referring to a given alc point. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_id : int
		The number of the model.

	alc_name : str
		The name of the alc point.

	attribute_name : str
		Name of the attribute.

	attribute_value : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int

	Examples
	--------
	::

		import meta
		from meta import nodes
		
		
		def main():
		    model = 0
		    alcname = "alc_point"
		
		    attr_name = "New"
		    val = "Attribute"
		    val = nodes.SetAttributeOfALCPoint(model, alcname, attr_name, val)
		    print(val)
		    # or
		    attr_name = "N_New"
		    val = 12
		    val = nodes.SetAttributeOfALCPoint(model, alcname, attr_name, val, "numerical")
		    print(val)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NearestElementsOfModel(point_coordinates: object, model_id: int, resultset: object) -> object:

	"""

	This function finds the nearest elements of a given model from specific points.

	Parameters
	----------
	point_coordinates : object
		List with coordinates of the points.

	model_id : int
		The Id of the model

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		Upon success, it returns a list of objects of class Element referring to the nearest element of the given model for each specified point.
		Upon failure, a non valid Elem object is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import materials
		from meta import constants
		
		
		def main():
		    out = "elems_bench.txt"
		    file = open(out, "w")
		    # elements start
		    coords = list()
		    material_type = constants.MAT1
		    material_id = 0
		    material_nodes = nodes.NodesOfMaterial(1, material_type, material_id)
		    count = 0
		    for n in material_nodes:
		        tmp = list()
		        tmp.append(n.x)
		        tmp.append(n.y)
		        tmp.append(n.z)
		        coords.append(tmp)
		        if count > 9:
		            break
		        count += 1
		    elems_list = nodes.NearestElementsOfModel(point_coordinates=coords, model_id=0)
		    print(elems_list)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IdentifyNodesReset(model_id: int, node_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_nodes` instead.


	This function allows the user to reset the identification of all or specific nodes of the specified model. It can be called with two different ways. The one is with lists of ids, and the other is with node_ids = 'all'.

	Parameters
	----------
	model_id : int
		Id of the model.

	node_ids : object
		List with ids of the nodes, or string 'all'.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		import meta
		from meta import nodes
		
		
		def main():
		    model_id = 0
		    node_ids = list(range(1, 60))
		    # or
		    # node_ids = 'all'
		    nodes.IdentifyNodesReset(model_id, node_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_nodes instead.", DeprecationWarning)

class Node():

	"""

	Class for nodes.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_comments
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		
		    comments = n.get_comments()
		    print(comments)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    coords = n.get_coordinates(res)
		    if coords:
		        print(coords.id, coords.x, coords.y, coords.z, coords.visible, coords.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    deform = n.get_deformations(res)
		    if deform:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_cut_plane
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    plane = planes.Plane(name="DEFAULT_PLANE_YZ")
		    val = n.get_distance_from_cut_plane(res, plane)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    elem = elements.Element(id=12471, type=constants.SOLID, second_id=-1, model_id=m.id)
		
		    val = n.get_distance_from_element(res, elem, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import groups
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    group = groups.Group(name="bolts", model_id=m.id)
		
		    val = n.get_distance_from_group(res, group, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(id=200, model_id=m.id)
		    node2 = nodes.Node(id=250, model_id=m.id)
		    val = n.get_distance_from_line(res, node1, res, node2, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line_coords
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		
		    val = n.get_distance_from_line_coords(res, point1, point2)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_node
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node2 = nodes.Node(id=200, model_id=m.id)
		
		    val = n.get_distance_from_node(res, node2, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		
		    val = n.get_distance_from_part(res, part, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node2 = nodes.Node(id=200, model_id=m.id)
		    node2 = nodes.Node(id=210, model_id=m.id)
		    node3 = nodes.Node(id=220, model_id=m.id)
		    val = n.get_distance_from_plane(res, node2, res, node2, res, node3, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    point3 = [1.35, 2.49, -3.3]
		    val = n.get_distance_from_plane_coords(res, point1, point2, point3)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    elems = n.get_elements()
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_cut_plane
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import planes
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    plane = planes.Plane(name="DEFAULT_PLANE_YZ")
		    val = n.get_elongation_from_cut_plane(res, plane)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import elements
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    elem = elements.Element(id=12471, type=constants.SOLID, second_id=-1, model_id=m.id)
		    val = n.get_elongation_from_element(res, elem, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import groups
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    group = groups.Group(name="bolts", model_id=m.id)
		    val = n.get_elongation_from_group(res, group, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node1 = nodes.Node(200, m.id)
		    node2 = nodes.Node(250, m.id)
		    val = n.get_elongation_from_line(res, node1, res, node2, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line_coords
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    val = n.get_elongation_from_line_coords(res, point1, point2)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_node
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node2 = nodes.Node(id=200, model_id=m.id)
		    val = n.get_elongation_from_node(res, node2, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import parts
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    part = parts.Part(id=2, type=constants.PSOLID, model_id=m.id)
		    val = n.get_elongation_from_part(res, part, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    node2 = nodes.Node(id=200, model_id=m.id)
		    node2 = nodes.Node(id=210, model_id=m.id)
		    node3 = nodes.Node(id=220, model_id=m.id)
		    val = n.get_elongation_from_plane(res, node2, res, node2, res, node3, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane_coords
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    point3 = [1.35, 2.49, -3.3]
		    val = n.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    r = n.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_name
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    name = "New node name"
		    ret = n.set_name(name)
		    print(ret)
		    name = n.get_name()
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    nodal_scalar = n.get_nodal_scalar(res)
		    for nodal in nodal_scalar:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		
		    nodal_scalar = n.get_nodal_scalar(res)
		    # nodal_scalar = n.get_nodal_scalar(res, layer = 'top' )
		    for nodal in nodal_scalar:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    nodal_vector = n.get_nodal_vector(res)
		    # nodal_vector = n.get_nodal_vector(res, layer = 'top' )
		    for nodal in nodal_vector:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    specifier = "all"
		    parts = n.get_parts(specifier)
		    # specifier = 'remote'
		    # parts = n.get_parts(specifier, level = 1)
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
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    res = m.get_current_resultset()
		    nodal = n.get_shell_normal(res)
		    if nodal:
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    ret = n.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = n.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_name = 'new_attr'
		    # attribute_type = 'string'
		    # attribute_value = 'my_atrribute'
		    # ret = n.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attribute_name = "new_attr"
		    attr = n.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = n.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = n.get_attributes()
		    # attribute_name = 'new_attr')
		    # attr = n.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_coordinate_system
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import coordsystems
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    coord = coordsystems.CoordSystem(id=1, model_id=m.id)
		    cs = n.set_coordinate_system(coord)
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
		# method: set_name
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    name = "New node name"
		    ret = n.set_name(name)
		    print(ret)
		    name = n.get_name()
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_nodal_scalar
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import results
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    new_function_data_name = "Nodal Scalar Data"
		    resultset = m.get_current_resultset()
		
		    results.StartAddingNodalScalar(resultset, new_function_data_name)
		    value = 15
		    val = n.set_nodal_scalar(resultset, value)
		    print(val)
		    results.EndAddingNodalScalar(resultset)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_nodal_vector
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import results
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    new_function_data_name = "Nodal Vector Data"
		    res = m.get_current_resultset()
		    vec = [0.2, 0.682, 0, 0.7315]
		    results.StartAddingNodalVector(res, new_function_data_name)
		    val = n.set_nodal_vector(res, vec)
		    print(val)
		    results.EndAddingNodalVector(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinate_system
		# PYTHON script
		import meta
		from meta import nodes
		from meta import models
		from meta import coordsystems
		
		
		def main():
		    m = models.Model(0)
		    n = nodes.Node(id=161, model_id=m.id)
		    coord = coordsystems.CoordSystem(id=1, model_id=m.id)
		    set_cs = n.set_coordinate_system(coord)
		    specifier = "user"
		    cs = n.get_coordinate_system(specifier)
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
		# method: transform
		# PYTHON script
		import meta
		from meta import nodes
		from meta import coordsystems
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    x = 40.12
		    y = 50.35
		    z = 61.58
		    coord_sys_id = 1005213
		    n = nodes.Node(id=205656, model_id=model_id)
		    cs = coordsystems.CoordSystem(coord_sys_id, model_id)
		    transformed = n.transform(cs, result)
		    if transformed:
		        xtrans = transformed[0]  # Transformed X coordinate
		        ytrans = transformed[1]  # Transformed Y coordinate
		        ztrans = transformed[2]  # Transformed Z coordinate
		        print(xtrans, ytrans, ztrans)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import nodes
		
		
		def main():
		    n = nodes.Node(id=1, model_id=0)
		    can_use = n.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the node.

	"""

	model_id: int = None
	"""
	Model id of the node.

	"""

	x: float = None
	"""
	X coordinate of node.

	"""

	y: float = None
	"""
	Y coordinate of node.

	"""

	z: float = None
	"""
	Z coordinate of node.

	"""

	visible: int = None
	"""
	- 1 if node is visible on the active or first enabled window of the active page
	- 0 if node is not visible

	"""

	def get_elements(self) -> object:

		"""

		This method gets all the elements that contain the node.


		Returns
		-------
		object
			Upon success, it returns a list with objects of type Element. Upon failure, it returns an empty list.

		"""


	def get_parts(self, specifier: str, level: int) -> object:

		"""

		This method gets the parts of the node.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			-'all' : all parts that include this node (default value).
			-'remote' : collects remote parts of type PSHELL and PSOLID of the node. Must be combined with argument: level.

		level : int, optional
			An integer equal to or greater than zero which defines the depth of the search for PSHELL and PSOLID parts (e.g. 0 = directly attached to the part, 1 = one element away from the part etc.). This argument is required when specifier is 'remote'

		Returns
		-------
		object
			Upon success, it returns a list with objects of type Part. Upon failure, it returns an empty list.

		"""


	def get_model(self) -> object:

		"""

		This method returns the model of the node


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the node. Upon failure, it returns None.

		"""


	def get_coordinate_system(self, specifier: str) -> object:

		"""

		This method gets the coordinate system of the node


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'user' : user defined coordinate
			- 'local_geometry' : coordinate system used in geometry
			- 'local_results' : coordinate system used in results.

		Returns
		-------
		object
			Upon success, it returns a CoordSystem object. Upon failure it returns None

		"""


	def get_name(self) -> str:

		"""

		This method gets the name of the node.


		Returns
		-------
		str
			Upon success, it returns the name of the node. Upon failure, it returns None.

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of the node


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the node. Upon failure, it returns None.

		"""


	def get_coordinates(self, resultset: object) -> object:

		"""

		This method gets the coordinates of the node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a Node object, with the caluclated coordinates for the resultset. Upon failure it returns None.

		"""


	def get_deformations(self, resultset: object) -> object:

		"""

		This method gets the deformation of the node, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a Deformation object, with the deformations of the node for the resultset. Upon failure it returns None.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vector of the node. The calculation is based on the shell normal vectors of the shell elements which the node belongs to.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a NodalVector object, referring to the shell normal vector of the specified node. Upon failure it returns None.

		"""


	def get_nodal_scalar(self, resultset: object, layer: str) -> object:

		"""

		This method gets the nodal scalar value of the node, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the nodal scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalScalar. Upon failure, it returns an empty list.

		"""


	def get_nodal_vector(self, resultset: object, layer: str) -> object:

		"""

		This method gets the nodal vector value of the node, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the nodal scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalVector. Upon failure, it returns an empty list.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the node.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_distance_from_node(self, resultset: object, node: object, node_resultset: object) -> object:

		"""

		This method gets the distance of the node from a given node.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the node.

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

		This method gets the elongation of the node from a given node. 


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

		This method gets the distance of the node from a given element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the node.

		element : object
			An object of class Element.

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance of the node from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the node.

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

		This method gets the elongation of the node from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the node.

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

		This method gets the distance of the node from a given group.


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


	def get_elongation_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the elongation of the node from a given element.


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


	def get_elongation_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the elongation of the node from a given group.


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


	def get_distance_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the distance of the node from a given cutplane.


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


	def get_distance_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the distance of the node from a given line.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned

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


	def get_distance_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the distance of the node from a given plane.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned

		"""


	def get_elongation_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the elongation of the node from a given plane.


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


	def get_distance_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the distance of the node from a line from the given coordinates.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned

		"""


	def get_elongation_from_line_coords(self, resultset: object, point1: object, point2: object) -> object:

		"""

		This method gets the elongation of the node from a line from the given coordinates.


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


	def get_distance_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the distance of the node from a plane from the given coordinates.


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
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned

		"""


	def get_elongation_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: object) -> object:

		"""

		This method gets the elongation of the node from a plane from the given coordinates.


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


	def set_deformations(self, resultset: object, value: object) -> bool:

		"""

		This method sets deformation in each direction (X, Y, Z) on the node. Functions 'StartAddingDeformations', 'StartAppendingDeformations' or 'StartChangingDeformations' must be called with the same argument (result) before starting adding deformations. Function 'EndAddingDeformations' must be called with the same argument (result) after ending adding deformations.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		value : object
			A list with the deformations as floats (X, Y, Z)

		Returns
		-------
		bool
			Upon success it returns True. Upon failure False

		"""


	def set_nodal_scalar(self, resultset: object, value: float) -> bool:

		"""

		This method sets nodal scalar value the node. Functions 'StartAddingNodalScalar', 'StartChangingNodalScalar' or 'StartAppendingNodalScalar' must be called with the same argument (result) before starting adding nodal scalar values. Function 'EndAddingNodalScalar' must be called with the same argument (result) after ending adding nodal scalar values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		value : float
			The value.

		Returns
		-------
		bool
			Upon success it returns True. Upon failure False

		"""


	def set_nodal_vector(self, resultset: object, value: object) -> bool:

		"""

		This method sets nodal vector values on a node with a specific id of a given model. Functions 'StartAddingNodalVector', 'StartChangingNodalVector' or 'StartAppendingNodalVector' must be called with the same argument (result) before starting adding nodal vector values. Function 'EndAddingNodalVector' must be called with the same argument (result) after ending adding nodal vector values.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		value : object
			A list with the normalized vector components as floats [value, X-direction vector component, Y-direction vector component, Z-direction vector component]

		Returns
		-------
		bool
			Upon success it returns True. Upon failure False.

		"""


	def set_coordinate_system(self, coordinate_system: object) -> object:

		"""

		This method sets an existing coordinate system on a node.


		Parameters
		----------
		coordinate_system : object
			An object of class CoordSystem.

		Returns
		-------
		object
			Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied on the node.Upon failure None is returned.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the node. If the given attribute does not exist it is automatically created and its value is set.


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


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the node.


		Parameters
		----------
		name : str
			Name of the node.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def transform(self, coordinate_system: object, resultset: object) -> object:

		"""

		This method calculates the coordinates of a given node with respect to an existing coordinate system.


		Parameters
		----------
		coordinate_system : object
			An object of class CoordSystem.

		resultset : object, optional
			Resultset at which transformation takes place. It is needed for moving coordinate systems.

		Returns
		-------
		object
			Upon success, it returns a list with 3 members referring to the transformed coordinates of the node with respect to the specified coordinate system.Else, an empty list is returned.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the node. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def __init__(self, id: int, model_id: int) -> object:

		"""

		Node object constructor. If the node with the specified id does not exist for the specified model, the constructor will raise an exception.


		Parameters
		----------
		id : int
			Node id.

		model_id : int
			Model id.

		Returns
		-------
		object
			Returns the created Node object.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Node entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

