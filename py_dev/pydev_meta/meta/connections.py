from __future__ import annotations
from typing import *

def CentroidScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of an element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100001
		    connection_centroid = connections.CentroidScalarOfConnection(result, connection_id)
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfConnection(result: object, connection_id: int, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_vector` instead.


	This function calculates all centroid vector values of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

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
		It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector value of an element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100001
		    connection_centroid = connections.CentroidVectorOfConnection(result, connection_id)
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.x, centroid.y, centroid.z
		        )  # Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_vector instead.", DeprecationWarning)

def CollectNewConnectionsEnd() -> object:

	"""

	This function ends recording the creation of new connections. This function should be preceded by a corresponding call to script function CollectNewConnectionsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Connections referring to one specific newly created connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import utils
		
		
		def main():
		    connections.CollectNewConnectionsStart()
		    # Read new geometry with connections
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		    new_connections = connections.CollectNewConnectionsEnd()
		    for con in new_connections:
		        print(con.id, con.type, con.subtype, con.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewConnectionsStart() -> int:

	"""

	This function starts recording the creation of new connections. This function should be followed by a corresponding call to script function CollectNewConnectionsEnd().

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import utils
		
		
		def main():
		    connections.CollectNewConnectionsStart()
		    # Read new geometry with connections
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		    new_connections = connections.CollectNewConnectionsEnd()
		    for con in new_connections:
		        print(con.id, con.type, con.subtype, con.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConnectedCentroidScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of a connected element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    connection_centroid = connections.ConnectedCentroidScalarOfConnection(
		        result, connection_id
		    )
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_scalar instead.", DeprecationWarning)

def ConnectedCentroidVectorOfConnection(result: object, connection_id: int, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_vector` instead.


	This function calculates all centroid vector values of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

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
		It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector value of a connected element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    connection_centroid = connections.ConnectedCentroidVectorOfConnection(
		        result, connection_id
		    )
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.x, centroid.y, centroid.z
		        )  # Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_vector instead.", DeprecationWarning)

def ConnectedCornerScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_scalar` instead.


	This function calculates all corner scalar values of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of a connected element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    elem_corner = connections.ConnectedCornerScalarOfConnection(result, connection_id)
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_scalar instead.", DeprecationWarning)

def ConnectedDeformationsOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL) of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Deformation referring to the deformation of a connected node for the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    connection_deforms = connections.ConnectedDeformationsOfConnection(
		        result, connection_id
		    )
		    for deform in connection_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def ConnectedElementsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific connected element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connected_elements = connections.ConnectedElementsOfConnection(
		        model_id, connection_id
		    )
		    for e in connected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def ConnectedElementsOfConnectionByType(model_id: int, connection_id: int, element_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects connected elements with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	element_type : int
		Type of the element (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific connected element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connection_type = constants.SHELL
		    connected_elements = connections.ConnectedElementsOfConnectionByType(
		        model_id, connection_id, connection_type
		    )
		    for e in connected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def ConnectedMaterialsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_materials` instead.


	This function collects connected materials of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific connected material of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connected_materials = connections.ConnectedMaterialsOfConnection(
		        model_id, connection_id
		    )
		    for m in connected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_materials instead.", DeprecationWarning)

def ConnectedMaterialsOfConnectionByType(model_id: int, connection_id: int, material_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_materials` instead.


	This function collects connected materials with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model

	connection_id : int
		Id of the connection.

	material_type : int
		Type of the material (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific connected material of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    mat_type = constants.MAT1
		    connected_materials = connections.ConnectedMaterialsOfConnectionByType(
		        model_id, connection_id, mat_type
		    )
		    for m in connected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_materials instead.", DeprecationWarning)

def ConnectedNodalScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str
		Bottom or top nodal scalar values.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalScalar referring to the nodal scalar values of a connected node of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    connected_nodal = connections.ConnectedNodalScalarOfConnection(
		        result, connection_id
		    )
		    for nodal in connected_nodal:  # List with nodal_scalar structs
		        print(nodal.value, nodal.node_id, nodal.part_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_scalar instead.", DeprecationWarning)

def ConnectedNodalVectorOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_vector` instead.


	This function calculates all nodal vector values of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalVector referring to the nodal vector values of a connected node of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    connected_nodal = connections.ConnectedNodalVectorOfConnection(
		        result, connection_id
		    )
		    for nodal in connected_nodal:
		        print(nodal.value, nodal.x, nodal.y, nodal.z)
		        print(nodal.node_id, nodal.part_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_vector instead.", DeprecationWarning)

def ConnectedNodesOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodes` instead.


	This function collects connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific connected node of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connected_nodes = connections.ConnectedNodesOfConnection(model_id, connection_id)
		    for n in connected_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodes instead.", DeprecationWarning)

def ConnectedPartsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects connected parts of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific connected part of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connected_parts = connections.ConnectedPartsOfConnection(model_id, connection_id)
		    for p in connected_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def ConnectedPartsOfConnectionByType(model_id: int, connection_id: int, part_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all connected parts with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	part_type : int
		Type of the part (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific connected part of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    type = constants.PSHELL
		    connected_parts = connections.ConnectedPartsOfConnectionByType(
		        model_id, connection_id, type
		    )
		    for p in connected_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def ConnectionById(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function finds the connection of a model with a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		Upon success, it returns an object of class Connection with the given id.
		Else, None is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    con = connections.ConnectionById(model_id, connection_id)
		    if con:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def Connections(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all connections of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member is an object of class Connection referring to one specific connection of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_connections = connections.Connections(model_id)
		    for con in all_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def ConnectionsBySubtype(model_id: int, connection_subtype: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all connections with a specific subtype of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_subtype : int
		Subtype of the connection (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Connection referring to one specific connection of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_subtype = constants.RBE3_HEXA_RBE3
		    collected_connections = connections.ConnectionsBySubtype(
		        model_id, connection_subtype
		    )
		    for con in collected_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def ConnectionsByType(model_id: int, connection_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all connections with a specific type of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_type : int
		Type of the connection (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Connection referring to one specific connection of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_type = constants.POINT
		    collected_connections = connections.ConnectionsByType(model_id, connection_type)
		    for con in collected_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def ConnectionsByTypeAndSubtype(model_id: int, connection_type: int, connection_subtype: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all connections with a specific type and subtype of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_type : int
		Type of the connection (META constant).

	connection_subtype : int
		Subtype of the connection (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Connection referring to one specific connection of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_type = constants.POINT
		    connection_subtype = constants.RBE3_HEXA_RBE3
		    collected_connections = connections.ConnectionsByTypeAndSubtype(
		        model_id, connection_type, connection_subtype
		    )
		    for con in collected_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def ConnectionsListToDict(connections: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Connection.

	Parameters
	----------
	connections : object
		Objects of class Connection.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the connection and data the corresponding Connection object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_connections = connections.Connections(model_id)
		    dict_connections = connections.ConnectionsListToDict(all_connections)
		    for id, con in dict_connections.items():
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConnectionsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_connections` instead.


	This function searches for the connections of an overlay run with a given type and id.

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
		It returns a list where each member of the list is an object of class Connection referring to one connection of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    overlay_run_connections = connections.ConnectionsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for con in overlay_run_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_connections instead.", DeprecationWarning)

def CornerScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of an element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    elem_corner = connections.CornerScalarOfConnection(result, connection_id)
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_scalar instead.", DeprecationWarning)

def DeformationsOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL) of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Deformation referring to the deformation of a node for the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100096
		    connection_deforms = connections.DeformationsOfConnection(result, connection_id)
		    for deform in connection_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def ElementsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all elements of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connection_elements = connections.ElementsOfConnection(model_id, connection_id)
		    for e in connection_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def ElementsOfConnectionByType(model_id: int, connection_id: int, element_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all elements with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	element_type : int
		Type of the element (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    element_type = constants.SOLID
		    connection_elements = connections.ElementsOfConnectionByType(
		        model_id, connection_id, element_type
		    )
		    for e in connection_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def IsConnection(connection: object) -> int:

	"""

	This function checks whether an object is of class Connection.

	Parameters
	----------
	connection : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the object is of class Connection, 0 otherwise.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    objects = list()
		    objects.append("a_string")
		    objects.append(connections.Connections(model_id)[0])
		
		    for obj in objects:
		        if connections.IsConnection(obj):
		            print("This is an object of class Connection")
		            print(obj.id, obj.type, obj.subtype, obj.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_materials` instead.


	This function collects all materials of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model

	connection_id : int
		Id of the connection

	Returns
	-------
	object
		It returns a list with material objects where each member of the list is an object of class Material referring to one specific material of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100096
		    connection_materials = connections.MaterialsOfConnection(model_id, connection_id)
		    for m in connection_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_materials instead.", DeprecationWarning)

def MaterialsOfConnectionByType(model_id: int, connection_id: int, material_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_materials` instead.


	This function collects all materials with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model

	connection_id : int
		Id of the connection

	material_type : int
		Type of the material (META KEYWORD)

	Returns
	-------
	object
		It returns a list with material objects where each member of the list is an object of class Material referring to one specific material of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100096
		    material_type = constants.MAT1
		
		    connection_materials = connections.MaterialsOfConnectionByType(
		        model_id, connection_id, material_type
		    )
		    for m in connection_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_materials instead.", DeprecationWarning)

def MaxConnectedDeformationOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL) of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects where each member of the list is refers to the maximun deformation in each direction for the connected nodes of the specified connection.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    max_deform = connections.MaxConnectedDeformationOfConnection(result, connection_id)
		    if max_deform:
		        max_x_deform = max_deform[0]  # Struct with maximum deformation in direction X
		        print(max_x_deform.x)  # X maximum deformation
		        print(
		            max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformations in rest directions on the node with the maximum X deformation
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[1]  # Struct with maximum deformation in direction Y
		        print(max_y_deform.y)  # Y minimum deformation
		        print(
		            max_y_deform.x, max_y_deform.z, max_y_deform.total
		        )  # Deformations in rest directions on the node with the maximum Y deformation
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[2]  # Struct with maximum deformation in direction Z
		        print(max_z_deform.z)  # Z maximum deformation
		        print(
		            max_z_deform.x, max_z_deform.y, max_z_deform.total
		        )  # Deformations in rest directions on the node with the maximum Z deformation
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z deformation
		
		        max_total_deform = max_deform[3]  # Struct with maximum TOTAL deformation
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def MaxDeformationOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL) of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects where each member of the list refers to the maximun deformation in each direction for the specified connection.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    max_deform = connections.MaxDeformationOfConnection(result, connection_id)
		    if max_deform:
		        max_x_deform = max_deform[0]  # Struct with maximum deformation in direction X
		        print(max_x_deform.x)  # X maximum deformation
		        print(
		            max_x_deform.y, max_x_deform.z, max_x_deform.total
		        )  # Deformations in rest directions on the node with the maximum X deformation
		        print(max_x_deform.node_id)  # Id of the node with the maximum X deformation
		
		        max_y_deform = max_deform[1]  # Struct with maximum deformation in direction Y
		        print(max_y_deform.y)  # Y minimum deformation
		        print(
		            max_y_deform.x, max_y_deform.z, max_y_deform.total
		        )  # Deformations in rest directions on the node with the maximum Y deformation
		        print(max_y_deform.node_id)  # Id of the node with the maximum Y deformation
		
		        max_z_deform = max_deform[2]  # Struct with maximum deformation in direction Z
		        print(max_z_deform.z)  # Z maximum deformation
		        print(
		            max_z_deform.x, max_z_deform.y, max_z_deform.total
		        )  # Deformations in rest directions on the node with the maximum Z deformation
		        print(max_z_deform.node_id)  # Id of the node with the maximum Z deformation
		
		        max_total_deform = max_deform[3]  # Struct with maximum TOTAL deformation
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def MinConnectedDeformationOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL) of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects of the corresponding 
		minimum deformations in each direction for the connected nodes of the specified connection.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    min_deform = connections.MinConnectedDeformationOfConnection(result, connection_id)
		    if min_deform:
		        min_x_deform = min_deform[0]  # Struct with minimum deformation in direction X
		        print(min_x_deform.x)  # X minimum deformation
		        print(
		            min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformations in rest directions on the node with the minimum X deformation
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[1]  # Struct with minimum deformation in direction Y
		        print(min_y_deform.y)  # Y minimum deformation
		        print(
		            min_y_deform.x, min_y_deform.z, min_y_deform.total
		        )  # Deformations in rest directions on the node with the minimum Y deformation
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[2]  # Struct with minimum deformation in direction Z
		        print(min_z_deform.z)  # Z minimum deformation
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.total
		        )  # Deformations in rest directions on the node with the minimum Z deformation
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z deformation
		
		        min_total_deform = min_deform[3]  # Struct with minimum TOTAL deformation
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def MinDeformationOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL) of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection

	Returns
	-------
	object
		It returns a list with 4 Deformation objects of the corresponding 
		minimum deformations in each direction for the specified connection.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    min_deform = connections.MinDeformationOfConnection(result, connection_id)
		    if min_deform:
		        min_x_deform = min_deform[0]  # Struct with minimum deformation in direction X
		        print(min_x_deform.x)  # X minimum deformation
		        print(
		            min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformations in rest directions on the node with the minimum X deformation
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[1]  # Struct with minimum deformation in direction Y
		        print(min_y_deform.y)  # Y minimum deformation
		        print(
		            min_y_deform.x, min_y_deform.z, min_y_deform.total
		        )  # Deformations in rest directions on the node with the minimum Y deformation
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[2]  # Struct with minimum deformation in direction Z
		        print(min_z_deform.z)  # Z minimum deformation
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.total
		        )  # Deformations in rest directions on the node with the minimum Z deformation
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z deformation
		
		        min_total_deform = min_deform[3]  # Struct with minimum TOTAL deformation
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_deformations instead.", DeprecationWarning)

def MinMaxCentroidScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CentroidScalar objects of the corresponding minimum
		and maximum centroid scalar values for the specified connection.
		- 0 = MINIMUM centroid scalar
		- 1 = MAXIMUM centroid scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    centroid = connections.MinMaxCentroidScalarOfConnection(result, connection_id)
		    if centroid:
		        min_centroid = centroid[0]  # Struct with minimum centroid scalar value
		        print(min_centroid.value)  # Minimum centroid scalar value
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid scalar value
		
		        max_centroid = centroid[1]  # Struct with maximum centroid scalar value
		        print(max_centroid.value)  # Maximum centroid scalar value
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxCentroidVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CentroidVector objects of the corresponding minimum and maximum centroid vector values for the specified connection.
		- 0 = MINIMUM centroid vector
		- 1 = MAXIMUM centroid vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    centroid = connections.MinMaxCentroidVectorOfConnection(result, connection_id)
		    if centroid:
		        min_centroid = centroid[0]  # Struct with minimum centroid vector value
		        print(min_centroid.value)  # Minimum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the minimum centroid vector
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid vector value
		
		        max_centroid = centroid[1]  # Struct with maximum centroid vector value
		        print(max_centroid.value)  # Maximum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the maximum centroid vector
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_vector instead.", DeprecationWarning)

def MinMaxConnectedCentroidScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CentroidScalar objects of the corresponding minimum and maximum centroid scalar values for the connected elements the specified connection.
		- 0 = MINIMUM centroid scalar
		- 1 = MAXIMUM centroid scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    centroid = connections.MinMaxConnectedCentroidScalarOfConnection(
		        result, connection_id
		    )
		    if centroid:
		        min_centroid = centroid[0]  # Struct with minimum centroid scalar value
		        print(min_centroid.value)  # Minimum centroid scalar value
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid scalar value
		
		        max_centroid = centroid[1]  # Struct with maximum centroid scalar value
		        print(max_centroid.value)  # Maximum centroid scalar value
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxConnectedCentroidVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CentroidVector objects of the corresponding minimum and maximum centroid vector values for the connected elements of the specified connection.
		- 0 = MINIMUM centroid vector
		- 1 = MAXIMUM centroid vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    centroid = connections.MinMaxConnectedCentroidVectorOfConnection(
		        result, connection_id
		    )
		    print(centroid)
		    if centroid:
		        min_centroid = centroid[0]  # Struct with minimum centroid vector value
		        print(min_centroid.value)  # Minimum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the minimum centroid vector
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid vector value
		
		        max_centroid = centroid[1]  # Struct with maximum centroid vector value
		        print(max_centroid.value)  # Maximum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the maximum centroid vector
		        print(
		            max_centroid.element_id, max_centroid.second_id, max_centroid.type
		        )  # Id, second id and type of the element with the maximum centroid vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_centroid_vector instead.", DeprecationWarning)

def MinMaxConnectedCornerScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of the connected of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CornerScalar objects of the corresponding minimum
		and maximum corner scalar values for the connected elements of the specified connection.
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    corner = connections.MinMaxConnectedCornerScalarOfConnection(result, connection_id)
		    if corner:
		        min_corner = corner[0]  # Struct with minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the minimum corner scalar value for shells and solids elements, or the fraction of the distance from the start to the total distance for line elements
		
		        max_corner = corner[1]  # Struct with the maximum corner scalar value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_scalar instead.", DeprecationWarning)

def MinMaxConnectedNodalScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value of the connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 NodalScalar objects of the corresponding minimum and maximum nodal scalar values for the connected nodes of the specified connection.
		- 0 = MINIMUM nodal scalar
		- 1 = MAXIMUM nodal scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    nodal = connections.MinMaxConnectedNodalScalarOfConnection(result, connection_id)
		    if nodal:
		        min_nodal = nodal[0]  # Struct with minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal scalar value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Struct with maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(max_nodal.part_id)  # Id of the part or -1 if no parts exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxConnectedNodalVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector value of the connected nodes of a given connection belonging to the specified model. Nodal vector values refer to a resultset specified by its object.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 NodalVector objects of the corresponding minimum and maximum nodal vector values for the connected nodes of the specified connection.
		- 0 = MINIMUM nodal vector
		- 1 = MAXIMUM nodal vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    nodal = connections.MinMaxConnectedNodalVectorOfConnection(result, connection_id)
		    if nodal:
		        min_nodal = nodal[0]  # Struct with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Struct with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal vector value
		        print(max_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_vector instead.", DeprecationWarning)

def MinMaxCornerScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CornerScalar objects of the corresponding minimum and maximum corner scalar values for the specified connection.
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    corner = connections.MinMaxCornerScalarOfConnection(result, connection_id)
		    if corner:
		        min_corner = corner[0]  # Struct with minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		        print(
		            min_corner.corner
		        )  # Id of the node - corner with the minimum corner scalar value for shells and solids elements, or the fraction of the distance from the start to the total distance for line elements
		
		        max_corner = corner[1]  # Struct with the maximum corner scalar value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_scalar instead.", DeprecationWarning)

def MinMaxNodalScalarOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 NodalScalar objects of the corresponding minimum and maximum nodal scalar values for the specified connection.
		- 0 = MINIMUM nodal scalar
		- 1 = MAXIMUM nodal scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    nodal = connections.MinMaxNodalScalarOfConnection(result, connection_id)
		    if nodal:
		        min_nodal = nodal[0]  # Struct with minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal scalar value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Struct with maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(max_nodal.part_id)  # Id of the part or -1 if no parts exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxNodalVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector value of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 NodalVector objects of the corresponding minimum and maximum nodal vector values for the specified connection.
		- 0 = MINIMUM nodal vector
		- 1 = MAXIMUM nodal vector
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    nodal = connections.MinMaxNodalVectorOfConnection(result, connection_id)
		    if nodal:
		        min_nodal = nodal[0]  # Struct with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Struct with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal vector value
		        print(max_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_vector instead.", DeprecationWarning)

def NodalScalarOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list with the NodalScalar objects of the corresponding nodal scalar values of the elements of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    connection_nodal = connections.NodalScalarOfConnection(result, connection_id)
		    for nodal in connection_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodal_vector` instead.


	This function calculates all nodal vector values of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list with the NodalVector objects of the corresponding nodal vector values of the elements of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    connection_nodal = connections.NodalVectorOfConnection(result, connection_id)
		    for nodal in connection_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodal_vector instead.", DeprecationWarning)

def NodesOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodes` instead.


	This function collects all nodes of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific node of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connection_nodes = connections.NodesOfConnection(model_id, connection_id)
		    for n in connection_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodes instead.", DeprecationWarning)

def PartsOfConnection(model_id: int, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all parts of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    connection_parts = connections.PartsOfConnection(model_id, connection_id)
		    for p in connection_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def PartsOfConnectionByType(model_id: int, connection_id: int, part_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all parts with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	part_type : int
		Type of the part (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    type = constants.PSOLID
		    connection_id = 100007
		    connection_parts = connections.PartsOfConnectionByType(
		        model_id, connection_id, type
		    )
		    for p in connection_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def ReportNewConnections() -> object:

	"""

	This function collects the newly created connections from the last call of script function CollectNewConnectionsStart(). This function should be preceded by a corresponding call to script function CollectNewConnectionsStart() and should be followed by a corresponding call to script function CollectNewConnectionsEnd().

	Returns
	-------
	object
		It returns a list with the Connection objects of the corresponding newly created
		connections.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import utils
		
		
		def main():
		    connections.CollectNewConnectionsStart()
		
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_connections = connections.ReportNewConnections()
		    for con in new_connections:
		        print(con.id, con.type, con.subtype, con.model_id)
		    print("##############################")
		
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_connections = connections.CollectNewConnectionsEnd()
		    for con in new_connections:
		        print(con.id, con.type, con.subtype, con.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StringConnectionSubtype(connection_type: int) -> str:

	"""

	This function converts a given META connection subtype to its corresponding string representation.

	Parameters
	----------
	connection_type : int
		Type of connection (META constant).

	Returns
	-------
	str
		It returns a string with the name of the META connection subtype.
		Upon failure, None is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import connections
		
		
		def main():
		    connection_subtype = constants.RBE3_HEXA_RBE3
		    str_connection_subtype = connections.StringConnectionSubtype(connection_subtype)
		    print(str_connection_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StringConnectionType(connection_type: int) -> object:

	"""

	This function converts a given META connection type to its corresponding string representation.

	Parameters
	----------
	connection_type : int
		Type of the connection (META constant).

	Returns
	-------
	object
		It returns a string with the name of the META connection type.
		Upon failure, None is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import connections
		
		
		def main():
		    connection_type = constants.POINT
		    str_connection_type = connections.StringConnectionType(connection_type)
		    print(str_connection_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleConnectedElementsOfConnection(model_id: int, connection_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all visible connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific visible connected element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    connected_elements = connections.VisibleConnectedElementsOfConnection(
		        model_id, connection_id, window_name
		    )
		    for e in connected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def VisibleConnectedElementsOfConnectionByType(model_id: int, connection_id: int, element_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all visible connected elements with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of model.

	connection_id : int
		Id of connection.

	element_type : int
		Type of element (META constant).

	window_name : str
		Optional argument "window_name" refers to the name of the window of the model. If optional argument "window_name" is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Elem referring to one specific visible connected element of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    element_type = constants.SHELL
		    visible_connected_elements = connections.VisibleConnectedElementsOfConnectionByType(
		        model_id, connection_id, element_type, window_name
		    )
		    for e in visible_connected_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def VisibleConnectedNodesOfConnection(model_id: int, connection_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodes` instead.


	This function collects all visible connected nodes of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible connected node of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    connected_nodes = connections.VisibleConnectedNodesOfConnection(
		        model_id, connection_id, window_name
		    )
		    for n in connected_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodes instead.", DeprecationWarning)

def VisibleConnectedPartsOfConnection(model_id: int, connection_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all visible connected parts of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Number - id of the model

	connection_id : int
		Id of the connection.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect the visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific visible connected part of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    connected_parts = connections.VisibleConnectedPartsOfConnection(
		        model_id, connection_id, window_name
		    )
		    for p in connected_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def VisibleConnectedPartsOfConnectionByType(model_id: int, connection_id: int, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all visible connected parts with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	part_type : int
		Type of the part (META constant).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect the visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific visible connected part of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    part_type = constants.PSHELL
		    connected_parts = connections.VisibleConnectedPartsOfConnectionByType(
		        model_id, connection_id, part_type, window_name
		    )
		    for p in connected_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def VisibleElementsOfConnection(model_id: int, connection_id: int, window_name: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all visible elements of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	window_name : int
		Refers to the name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific visible element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    connection_elements = connections.VisibleElementsOfConnection(
		        model_id, connection_id, window_name
		    )
		    for e in connection_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def VisibleElementsOfConnectionByType(model_id: int, connection_id: int, element_type: int, window_name: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_elements` instead.


	This function collects all visible elements with a specific type of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	element_type : int
		Type of the element (META constant).

	window_name : int
		Refers to the name of the window of the model. If it is absent then this function will collect visible elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Element referring to one specific visible element of the given connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100007
		    element_type = constants.SOLID
		    window_name = "MetaPost"
		    connection_elements = connections.VisibleElementsOfConnectionByType(
		        model_id, connection_id, element_type, window_name
		    )
		    for e in connection_elements:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_elements instead.", DeprecationWarning)

def VisibleNodesOfConnection(model_id: int, connection_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_nodes` instead.


	This function collects all visible nodes of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	window_name : str
		Refers to the name of the window of the model. If it is absent then this function will collect the visible nodes for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Node referring to one specific visible node of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    visible_nodes = connections.VisibleNodesOfConnection(
		        model_id, connection_id, window_name
		    )
		    for n in visible_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_nodes instead.", DeprecationWarning)

def VisiblePartsOfConnection(model_id: int, connection_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all visible parts of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where ach member of the list is an object of class Part referring to one specific visible part of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    connection_id = 100004
		    window_name = "MetaPost"
		    connection_parts = connections.VisiblePartsOfConnection(
		        model_id, connection_id, window_name
		    )
		    for p in connection_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def VisiblePartsOfConnectionByType(model_id: int, connection_id: int, part_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_parts` instead.


	This function collects all visible parts of a given connection belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	connection_id : int
		Id of the connection.

	part_type : int
		Type of the part (META constant).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible parts for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific visible part of the given connection for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    model_id = 0
		    connection_id = 100007
		    part_type = constants.PSOLID
		    window_name = "MetaPost"
		    connection_parts = connections.VisiblePartsOfConnectionByType(
		        model_id, connection_id, part_type, window_name
		    )
		    for p in connection_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_parts instead.", DeprecationWarning)

def Connectors(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all connectors of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with the Connection objects of the corresponding CONNECTORS of
		the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_connectors = connections.Connectors(model_id)
		    for con in all_connectors:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def Gebs(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_connections` instead.


	This function collects all GEBs of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Connection referring to one specific GEB of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	connections.Connection

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_connectors = connections.Gebs(model_id)
		    for con in all_connectors:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_connections instead.", DeprecationWarning)

def ConnectedCornerVectorOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_vector` instead.


	This function calculates all corner vector values of the connected elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the corner vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerVector referring to one corner vector value of a connected element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    elem_corner = connections.ConnectedCornerVectorOfConnection(result, connection_id)
		    for corn in elem_corner:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_vector instead.", DeprecationWarning)

def CornerVectorOfConnection(result: object, connection_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_vector` instead.


	This function calculates all corner vector values of the elements of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	layer : str, optional
		Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CornerVector referring to one corner vector value of an element of the specified connection.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, connections.Connection, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    elem_corner = connections.CornerVectorOfConnection(result, connection_id)
		    for corn in elem_corner:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_vector instead.", DeprecationWarning)

def MinMaxConnectedCornerVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_vector` instead.


	This function calculates minimum and maximum corner vector value of the connected of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CornerVector objects of the corresponding minimum
		and maximum corner scalar values for the connected elements of the specified connection.
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100004
		    corner = connections.MinMaxConnectedCornerVectorOfConnection(result, connection_id)
		    if corner:
		        min_corner = corner[0]  # Struct with minimum corner scalar value
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
		
		        max_corner = corner[1]  # Struct with the maximum corner scalar value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_vector instead.", DeprecationWarning)

def MinMaxCornerVectorOfConnection(result: object, connection_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.connections.Connection.get_corner_vector` instead.


	This function calculates minimum and maximum corner vector value of a given connection belonging to the specified model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	connection_id : int
		Id of the connection.

	Returns
	-------
	object
		It returns a list with the 2 CornerVector objects of the corresponding minimum and maximum corner scalar values for the specified connection.
		- 0 = MINIMUM corner scalar
		- 1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import connections
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    connection_id = 100007
		    corner = connections.MinMaxCornerVectorOfConnection(result, connection_id)
		    if corner:
		        min_corner = corner[0]  # Struct with minimum corner scalar value
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
		
		        max_corner = corner[1]  # Struct with the maximum corner scalar value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.connections.Connection.get_corner_vector instead.", DeprecationWarning)

class Connection():

	"""

	Class for connections
	
	The type of the connection is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corrsponding constant names of constant values.
	Connections also have subtypes.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    if con:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    connection_centroid = con.get_centroid_scalar(resultset, specifier)
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    con = connections.Connection(id=100001, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element"]
		
		    values, elems = con.get_centroid_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    connection_centroid = con.get_centroid_vector(resultset, specifier)
		    for centroid in connection_centroid:
		        print(centroid.value)  # Centroid vector value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    con = connections.Connection(id=100001, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element"]
		
		    xyz, magn, elems = con.get_centroid_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "max"
		    connection_corner = con.get_corner_vector(resultset, specifier)
		    for corner in connection_corner:
		        print(corner.value)  # Corner vector value
		        print(
		            corner.element_id, corner.second_id, corner.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    con = connections.Connection(id=100001, model_id=m.id)
		    np_specifier = ["xyz", "magnitude", "element", "corner_id"]
		
		    xyz, magn, elems, corners = con.get_corner_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "max"
		    connection_corner = con.get_corner_scalar(resultset, specifier)
		    for corner in connection_corner:
		        print(corner.value)  # Corner scalar value
		        print(
		            corner.element_id, corner.second_id, corner.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    con = connections.Connection(id=100001, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element", "corner_id"]
		
		    values, elems, corners = con.get_corner_scalar(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(values)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import connections
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    connection_deforms = con.get_deformations(resultset, specifier)
		    for deform in connection_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		from meta import windows
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    specifier = "all"
		    elems = con.get_elements(specifier)
		    # elems = con.get_elements(specifier, type = constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    elems = con.get_elements(specifier, window=w)
		    # elems = con.get_elements(specifier, type = constants.SOLID , window = w )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_materials
		# PYTHON script
		import meta
		from meta import connections
		from meta import constants
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    specifier = "all"
		    mats = con.get_materials(specifier)
		    # mats = con.get_materials(specifier, type = constants.MAT1 )
		    # specifier = 'connected'
		    # mats = con.get_materials(specifier)
		    # mats = con.get_materials(specifier, type = constants.MAT1 )
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    r = con.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    connection_nodal = con.get_nodal_scalar(resultset, specifier)
		    for nodal in connection_nodal:
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    con = connections.Connection(id=100001, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "node"]
		
		    values, nodes = con.get_nodal_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import connections
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    connection_nodal = con.get_nodal_vector(resultset, specifier)
		    for nodal in connection_nodal:
		        print(nodal.value)  # Nodal vector value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    con = connections.Connection(id=100001, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, magn, nodes = con.get_nodal_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    specifier = "all"
		    connection_nodes = con.get_nodes("all")
		    for n in connection_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import connections
		from meta import windows
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    specifier = "all"
		    connection_nodes = con.get_nodes(specifier)
		    # connection_nodes = con.get_nodes('connected')
		    for n in connection_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    window = w
		    connection_nodes = con.get_nodes(specifier, window=w)
		    # specifier = 'visible_connected'
		    # connection_nodes = con.get_nodes(specifier, window = w )
		    for n in connection_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import connections
		from meta import windows
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    specifier = "all"
		    connection_parts = con.get_parts(specifier)
		    specifier = "connected"
		    # connection_parts = con.get_parts('connected')
		    for p in connection_parts:
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
		    specifier = "visible"
		    connection_parts = con.get_parts(specifier, window=w)
		    # specifier = 'visible_connected'
		    # connection_parts = con.get_parts(specifier, window = w )
		    for p in connection_parts:
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
		# method: get_curve_points
		# PYTHON script
		import meta
		from meta import connections
		from meta import models
		from meta import utils
		
		
		def main():
		    utils.MetaCommand("groups storecurvepoints enable")
		    utils.MetaCommand("read geom Abaqus /home/user/my_model\t.inp")
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		    points = con.get_curve_points()
		    print("points=", points)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import connections
		
		
		def main():
		    con = connections.Connection(id=100001, model_id=0)
		    can_use = con.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import models, connections
		
		
		def main():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = con.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = con.get_attributes()
		    # attribute_name ='attr'
		    attr = con.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_user_attributes
		# PYTHON script
		import meta
		from meta import models, connections
		
		
		def main():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		
		    attribute_name = "attr"
		    attribute_value = "test"
		    ret = con.set_user_attribute(attribute_name, attribute_value)
		    print(ret)
		    attr = con.get_user_attributes()
		    # attribute_name ='attr'
		    # attr = con.get_user_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import models, connections
		
		
		def main():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = con.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_name = 'attr'
		    # attribute_type = 'numerical'
		    # attribute_value = 11.2
		    # ret =  con.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attribute_name = "attr"
		    attr = con.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_user_attribute
		# PYTHON script
		import meta
		from meta import models, connections
		
		
		def main():
		    m = models.Model(0)
		    con = connections.Connection(id=100001, model_id=m.id)
		
		    attribute_name = "attr"
		    attribute_value = "test"
		    ret = con.set_user_attribute(attribute_name, attribute_value)
		    print(ret)
		    attribute_name = "attr"
		    attr = con.get_user_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the connection.

	"""

	model_id: int = None
	"""
	Model number of the connection.

	"""

	type: int = None
	"""
	Type of the connection (ANSA connection type).

	"""

	subtype: int = None
	"""
	Subtype of the connection (FE-representation).

	"""

	def get_model(self) -> object:

		"""

		This method gets the model of the connection.


		Returns
		-------
		object
			Upon success, it returns an object of class Model. Upon failure, it returns None.

		"""


	def get_elements(self, specifier: str, type: int, window: object) -> object:

		"""

		This method gets the elements of the group.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all elements of the connection (default value). Optionally combined with argument: type.
			- 'visible' : visible elements of the connection. Must be combined with argument: window. Optionally combined with argument: type.

		type : int, optional
			The type of the element that the method will return. If absent, elements of all types will returned.

		window : object, optional
			An object of class Window. It is used when the specifier is 'visible'. If this argument is set, the method will return only the visible elements in this window.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class Element referring to one specific element of the connection. Upon failure, an empty list is returned.

		"""


	def get_nodes(self, specifier: str, window: object) -> object:

		"""

		This method gets the nodes of the connection.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the nodes of the connection (default value).
			- 'visible' : visible nodes of the connection. Optionally combined with argument: window.
			- 'connected' : connected nodes.
			- 'visible_connected' : visible connected nodes. Optionally combined with argument: window.

		window : object, optional
			An object of class window. This argument is used only when the specifier is 'visible' or 'visible_connected'. If the specifier has a different value, this argument is ignored. If this argument is set, the method will return only the visible nodes in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node. Upon failure, it returns an empty list.

		"""


	def get_parts(self, specifier: str, window: object) -> object:

		"""

		This method gets the parts of the connection.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all parts of the connection (default value).
			- 'visible' : visible parts of the connection. Optionally combined with argument: window.
			- 'connected' : connected parts of the connection.
			- 'visible_connected' : connected visible parts of the connection. Optionally combined with argument: window.

		window : object, optional
			An object of class window. It is used when the specifier is 'visible' or 'visible_connected'. If this argument is set, the method will return only the visible parts in this window.

		Returns
		-------
		object
			It returns a list where each element of the list is an object of class Part referring to one specific part of the connection. Upon failure, an empty list is returned.

		"""


	def get_materials(self, specifier: str, type: int) -> object:

		"""

		This method gets the materials of the connections.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all materials of the connection (default value). Optionally combined with argument: type.
			- 'connected' : connected materials to the connection. Optionally combined with argument: type.

		type : int, optional
			The type of the material that the method will return. If absent, materials of all types will returned.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Material. Upon failure, it returns an empty list.

		"""


	def get_deformations(self, resultset: object, specifier: str, numpy: object) -> object:

		"""

		This method gets deformations for each direction (X, Y, Z, TOTAL), of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations of the connection (default value).
			- 'max' : maximum deformation of the connection.
			- 'min' : minimum deformation of the connection.
			- 'connected' : all deformations of the connected nodes of the connection.
			- 'max_connected' : maximum deformation of the connected nodes of the connection.
			- 'min_connected' : minimum deformation of the connected nodes of the connection.

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
			It returns a list where each element of the list is an object of class type Deformation referring to the deformation of a node of the connection. Upon failure, an empty list is returned.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: object, numpy: object) -> object:

		"""

		This method gets the nodal scalar values of the nodes of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar of the connection (default value).
			- 'max' : maximum nodal scalar of the connection.
			- 'min' : minimum nodal scalar of the connection.
			- 'connected' : all nodal scalar of the connected nodes of the connection.
			- 'max_connected' : maximum nodal scalar of the connected nodes of the connection.
			- 'min_connected' : minimum nodal scalar of the connected nodes of the connection.

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
			It returns a list where each element of the list is an object of class type NodalScalar referring to the nodal scalar values of a node of the connection. Upon failure, an empty list is returned.

		"""


	def get_nodal_vector(self, resultset: object, specifier: object, numpy: object) -> object:

		"""

		This method gets the nodal vector values of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector of the connection (default value).
			- 'max' : maximum nodal vector of the connection.
			- 'min' : minimum nodal vector of the connection.
			- 'connected' : all nodal vector of the connected nodes of the connection.
			- 'max_connected' : maximum nodal vector of the connected nodes of the connection.
			- 'min_connected' : minimum nodal vector of the connected nodes of the connection.

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
			It returns a list where each item of the list is an object of class type NodalVector referring to the nodal vector values of a node of the connection. Upon failure, an empty list is returned.

		"""


	def get_centroid_scalar(self, resultset: object, specifier: object, layer: str, non_zero: bool, exclude_novalue: bool, numpy: object) -> object:

		"""

		This method gets the centroid scalar values of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid scalar of the connection (default value).
			- 'max' : maximum centroid scalar of the connection.
			- 'min' : minimum centroid scalar of the connection.
			- 'connected' : all centroid scalar of the connected elements of the connection.
			- 'max_connected' : maximum centroid scalar of the connected elements of the connection.
			- 'min_connected' : minimum centroid scalar of the connected elements of the connection.

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
			It returns a list where each member of the list is an object of class CentroidScalar referring to the centroid scalar values of an element of the connection. Upon failure, an empty list is returned.

		"""


	def get_centroid_vector(self, resultset: object, specifier: object, numpy: object) -> object:

		"""

		This method gets the centroid vector values of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid vector of the connection (default value).
			- 'max' : maximum centroid vector of the connection.
			- 'min' : minimum centroid vector of the connection.
			- 'connected' : all centroid vector of the connected elements of the connection.
			- 'max_connected' : maximum centroid vector of the connected elements of the connection.
			- 'min_connected' : minimum centroid vector of the connected elements of the connection.

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
			It returns a list where each member of the list is an object of class CentroidVector referring to the centroid vector values of an element of the connection. Upon failure, an empty list is returned.

		"""


	def get_corner_scalar(self, resultset: object, specifier: object, numpy: object) -> object:

		"""

		This method gets the corner scalar values of the elements of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar of the connection (default value).
			- 'max' : maximum corner scalar of the connection.
			- 'min' : minimum corner scalar of the connection.
			- 'connected' : all corner scalar of the connected elements of the connection.
			- 'max_connected' : maximum corner scalar of the connected elements of the connection.
			- 'min_connected' : minimum corner scalar of the connected elements of the connection.

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
			It returns a list where each member of the list is an object of class CornerScalar referring to one corner scalar value of an element of the connection. Upon failure, an empty list is returned.

		"""


	def get_corner_vector(self, resultset: object, specifier: object, numpy: object) -> object:

		"""

		This method gets the corner vector values of the elements of the connection.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector of the connection (default value).
			- 'max' : maximum corner vector of the connection.
			- 'min' : minimum corner vector of the connection.
			- 'connected' : all corner vector of the connected elements of the connection.
			- 'max_connected' : maximum corner vector of the connected elements of the connection.
			- 'min_connected' : minimum corner vector of the connected elements of the connection.

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
			It returns a list where each member of the list is an object of class CornerVector referring to one corner vector value of an element of the connection. Upon failure, an empty list is returned.

		"""


	def get_curve_points(self) -> object:

		"""

		This method gets the coordinates of the points that descibe a connection curve that has been read from ANSA Comments. Note that this information is available only when the setting "Store curve points for connection" has been activated before reading the model's geometry.


		Returns
		-------
		object
			Returns a list, containg lists of coordinates [x, y, z] of the connection curve's points

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Connection entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the connection.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_user_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the user attributes of the connection.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: str) -> bool:

		"""

		This function sets the value of a specific User Specified attribute referring to a given connection. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. Its possible values are:
			-'string': String
			-'numerical': Number

		attribute_value : str
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

