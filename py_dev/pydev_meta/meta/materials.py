from __future__ import annotations
from typing import *

def AddMaterialLimitOnMaterial(limit_type: str, material_id: int, material_limit: float, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.set_material_limit` instead.


	This function adds material limit on a material of a given model.

	Parameters
	----------
	limit_type : str
		Type of the material limit. Its possible values are:
		- 'tension'
		- 'compression'
		- 'shear'
		- 'x_tension'
		- 'y_tension'
		- 'z_tension'
		- 'x_compression'
		- 'y_compression'
		- 'z_compression'
		- 'shear'
		- 's13'
		- 's23'
		- 'f12'
		- 'f13'
		- 'f23'

	material_id : int
		Id of the material.

	material_limit : float
		Material limit of material.

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
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1000
		    material_limit = 2.345
		    limit_type = "compression"
		    ret = materials.AddMaterialLimitOnMaterial(
		        model_id, material_id, material_limit, limit_type
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.set_material_limit instead.", DeprecationWarning)

def AddNameOnMaterial(material_id: int, material_name: str, material_type: int, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.set_name` instead.


	This function defines a name for a material of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_name : str
		Name of the material.

	material_type : int
		Type of the material (META constant).

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
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1001
		    mat = materials.MaterialById(model_id, material_type, material_id)
		    print(mat.name)
		    material_name = "MATERIAL_50"
		    materials.AddNameOnMaterial(model_id, material_type, material_id, material_name)
		    mat = materials.MaterialById(model_id, material_type, material_id)
		    print(mat.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.set_name instead.", DeprecationWarning)

def AdvFiltersOnMaterials(model_id: int, adv_filters: object, result: object, sort: bool) -> object:

	"""

	This function allows the user to collect materials of a model through some advanced filters.

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
		Controls if the returned list will be sorted. Default value is False.

	Returns
	-------
	object
		It returns a list with materials objects where each member refers to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Materials:all::Keep All")
		    adv_filters.append("intersect:Materials:id:<=100000:Keep All")
		
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    collected_materials = materials.AdvFiltersOnMaterials(model_id, adv_filters, result)
		    iter_end = min(10, len(collected_materials))
		    for m in collected_materials[0:iter_end]:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CentroidScalarOfMaterial(layer: str, material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_scalar` instead.


	This function calculates all centroid scalar values of a material of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CentroidScalar objects where each member of the list refers to the centroid scalar value of an element of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1001
		    material_centroid = materials.CentroidScalarOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_centroid))
		    for centroid in material_centroid[0:iter_end]:  # List with CentroidScalar objects
		        print(centroid.value)  # Centroid scalar value
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfMaterial(result: object, material_type: int, material_id: int, layer: str, principal: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_vector` instead.


	This function calculates all centroid vector values of a material of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

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
		It returns a list with CentroidVector objects where each member of the list refers to the centroid vector value of an element of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1001
		    material_centroid = materials.CentroidVectorOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_centroid))
		    for centroid in material_centroid[0:iter_end]:  # List with CentroidScalar objects
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_vector instead.", DeprecationWarning)

def CollectNewMaterialsEnd() -> object:

	"""

	This function ends recording the creation of new materials. This function should be preceded by a corresponding call to script function meta.materials.CollectNewMaterialsStart().

	Returns
	-------
	object
		It returns a list with the Material objects where each member of the list refers to one specific newly created material.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.CollectNewMaterialsStart, materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import utils
		
		
		def main():
		    materials.CollectNewMaterialsStart()
		
		    # create new materials
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_materials = materials.CollectNewMaterialsEnd()
		    for m in new_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewMaterialsStart() -> int:

	"""

	This function starts recording the creation of new materials. This function should be followed by a corresponding call to script function meta.materials.CollectNewMaterialsEnd().

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	See Also
	--------
	materials.CollectNewMaterialsEnd

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import utils
		
		
		def main():
		    materials.CollectNewMaterialsStart()
		
		    # create new materials
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_materials = materials.CollectNewMaterialsEnd()
		    for m in new_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ColorOfMaterial(window_name: str, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_color` instead.


	This function finds RGB values and Alpha channel of color of a material of a model.

	Parameters
	----------
	window_name : str, optional
		Window of the material's parent model. If optional argument "window_name" is absent then this function will return the color of the material for the first enabled window of the model of the material.

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a 4-members list with the RGB and Alpha channel values of the color of the corresponding material of the given model for the specified window. The list contains:
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
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1001
		    window_name = "MetaPost"
		    mat_color = materials.ColorOfMaterial(
		        model_id, material_type, material_id, window_name
		    )
		    if len(mat_color) > 0:
		        print(mat_color[0])  # R value
		        print(mat_color[1])  # G value
		        print(mat_color[2])  # B value
		        print(mat_color[3])  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_color instead.", DeprecationWarning)

def CommentsOfMaterial(material_id: int, material_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_comments` instead.


	This function finds the comments of a material with a specific id and type of a given model. Comments refer to various information which is output in the solver's input file (e.g. ANSA comments).

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
	str
		It returns a string referring to the comments of the material with the specified id and type of the given model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1001
		    window_name = "MetaPost"
		    material_comments = materials.CommentsOfMaterial(
		        model_id, material_type, material_id
		    )
		    print(material_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_comments instead.", DeprecationWarning)

def CornerScalarOfMaterial(result: object, material_type: int, material_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a given material of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list with CornerScalar objects where each member of the list refers to the corner scalar values of an element of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1001
		    material_corner = materials.CornerScalarOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_corner))
		    for corn in material_corner[0:iter_end]:  # List with CornerScalar objects
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_corner_scalar instead.", DeprecationWarning)

def DeformationsOfMaterial(material_id: int, material_type: int, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of a given of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : 
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with Deformation objects where each member refers to the deformation of a node for the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1001
		    material_deforms = materials.DeformationsOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_deforms))
		    for deform in material_deforms[0:iter_end]:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_deformations instead.", DeprecationWarning)

def GetColorOfMaterial(window_name: str, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_color` instead.


	This function finds color of a given material of a given model.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the material's model. If it is absent then this function will return the color of the material for the first enabled window of the material's model.

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns an object of class Color, with the color of the corresponding material of the given model for the specified window.
		Else, None is returned.

	See Also
	--------
	windows.Color, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1001
		    window_name = "MetaPost"
		    col = materials.GetColorOfMaterial(
		        model_id, material_type, material_id, window_name
		    )
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_color instead.", DeprecationWarning)

def HideMaterial(model_id: int, material_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.hide` instead.


	This function allows the user to hide a material of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_id : int
		Id of the material.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	materials.HideSomeMaterials

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1001
		    ret = materials.HideMaterial(model_id, material_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.hide instead.", DeprecationWarning)

def HideSomeMaterials(model_id: int, material_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.hide_materials` instead.


	This function allows the user to hide some specific materials of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_ids : object
		A list of integers, where each integer corresponds to a material id.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    all_materials = materials.Materials(model_id)
		    material_ids = list()
		    for m in all_materials:
		        material_ids.append(m.id)
		    ret = materials.HideSomeMaterials(model_id, material_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.hide_materials instead.", DeprecationWarning)

def IdentifyMaterial(model_id: int, material_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.identify` instead.


	This function allows the user to identify a material of a model specified by a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_id : int
		Id of the material.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	materials.IdentifySomeMaterials

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    ret = materials.IdentifyMaterial(model_id, material_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.identify instead.", DeprecationWarning)

def IdentifySomeMaterials(model_id: int, material_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_materials` instead.


	This function allows the user to identify some specific materials of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_ids : object
		Ids of the materials.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    all_materials = materials.Materials(model_id)
		    material_ids = list()
		    for m in all_materials:
		        material_ids.append(m.id)
		    ret = materials.IdentifySomeMaterials(model_id, material_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_materials instead.", DeprecationWarning)

def IsMaterial(material: object) -> int:

	"""

	This function checks whether object is of class Material.

	Parameters
	----------
	material : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Material, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import materials
		from meta import utils
		
		
		def main():
		    model_id = 0
		    all_materials = materials.Materials(model_id)
		    all_entities = list()
		    all_entities.append(all_materials[0])
		    all_entities.append(None)
		
		    for ent in all_entities:
		        if materials.IsMaterial(ent):
		            m = ent
		            print("This is a struct of type material")
		            print(m.id, m.type, m.name, m.model_id)
		        else:
		            print("This is not an object of class material")
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialById(material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function returns a material of a model according to its Id.

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
		Upon success, it returns an object of class Material.
		Else, None is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		
		    m = materials.MaterialById(model_id, material_type, material_id)
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialLimitOfMaterial(limit_type: str, material_id: int, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_material_limit` instead.


	This function calculates material limit of a material with a specific id of a given model.

	Parameters
	----------
	limit_type : str
		Type of the material limit. Its possible values are:
		- 'tension'
		- 'compression'
		- 'shear'
		- 'x_tension'
		- 'y_tension'
		- 'z_tension'
		- 'x_compression'
		- 'y_compression'
		- 'z_compression'
		- 'shear'
		- 's13'
		- 's23'
		- 'f12'
		- 'f13'
		- 'f23'

	material_id : int
		Id of the material.

	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the material limit of the specified material.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    limit_type = "compression"
		    mat_limit = materials.MaterialLimitOfMaterial(model_id, material_id, limit_type)
		    print(mat_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_material_limit instead.", DeprecationWarning)

def Materials(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function collects all materials of the model specified.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    all_materials = materials.Materials(model_id)
		    for m in all_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsByComments(material_comments: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds the materials of a model with specific comments.

	Parameters
	----------
	material_comments : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_comments = "MAT*"
		    collected_materials = materials.MaterialsByComments(model_id, material_comments)
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsByIdAllTypes(material_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds materials of a model with a given id.

	Parameters
	----------
	material_id : int
		Id of the material.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    collected_materials = materials.MaterialsByIdAllTypes(model_id, material_id)
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsByName(material_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds the materials of a model with a given name.

	Parameters
	----------
	material_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_name = "*"
		    collected_materials = materials.MaterialsByName(model_id, material_name)
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsByType(material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function collects all materials with a specific type of the given model.

	Parameters
	----------
	material_type : int
		Type of the material (META keyword).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    collected_materials = materials.MaterialsByType(model_id, material_type)
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect materials of a given model through some advanced filters. The execution of the script will stop and a window will open in order for the user to specify its advanced filters.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		
		    collected_materials = materials.MaterialsFromAdvFilters(model_id, resultset)
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialsListToDict(list_materials: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Material.

	Parameters
	----------
	list_materials : object
		List with objects of class Material.

	Returns
	-------
	object
		It returns a dictionary whose keys are the ids of the materials and values the corresponding Material objects.
		Upon failure, an empty dictionary is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    all_materials = materials.Materials(model_id)
		
		    dict_materials = materials.MaterialsListToDict(all_materials)
		    for id, m in dict_materials.items():
		        print(id)
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialsOfGroup(model_id: int, group_name: str, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_materials` instead.


	This function collects all materials of a given group belonging to the specified model. 

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
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    group_name = "My_Group"
		    group_instance = 1
		    group_materials = materials.MaterialsOfGroup(model_id, group_name, group_instance)
		    for m in group_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_materials instead.", DeprecationWarning)

def MaterialsOfGroupByType(model_id: int, group_name: str, material_type: int, group_instance: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_materials` instead.


	This function collects all materials with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	material_type : int
		Type of the material (META constants).

	group_instance : int, optional
		Instance of the group. If it is absent, then default value is 1.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    group_name = "My_Group"
		    material_type = constants.MAT1
		    group_instance = 1
		    group_materials = materials.MaterialsOfGroupByType(
		        model_id, group_name, material_type, group_instance
		    )
		    for m in group_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_materials instead.", DeprecationWarning)

def MaterialsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_materials` instead.


	This function searches for the materials of an overlay run with a given type and a given id .

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
		Upon success, it returns a list where each member of the list is an object of class Material referring to one material of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    overlay_run_materials = materials.MaterialsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for m in overlay_run_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_materials instead.", DeprecationWarning)

def MaterialsOfPart(part_id: str, part_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_materials` instead.


	This function collects all materials of a given part belonging to the specified model.

	Parameters
	----------
	part_id : str
		Id of the part.

	part_type : int
		Type of the part (META constants).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific material of the given part.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    part_type = constants.PSHELL
		    part_id = 1
		    part_materials = materials.MaterialsOfPart(model_id, part_type, part_id)
		    for m in part_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_materials instead.", DeprecationWarning)

def MaterialsTypes(model_id: int) -> object:

	"""

	This function collects all types of materials of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with types of the materials where each member of the list is an integer referring to one type (META constants) of materials for the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    all_types = materials.MaterialsTypes(model_id)
		    for material_type in all_types:
		        print(material_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialsWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds the materials of a model for which comments exist. 

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one material of the model for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.CommentsOfMaterial

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    materials_with_comments = materials.MaterialsWithComments(model_id)
		    for m in materials_with_comments:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaterialsWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds the materials of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to a material of the model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    materials_with_name = materials.MaterialsWithName(model_id)
		    for m in materials_with_name:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def MaxCoordinatesOfMaterial(result: object, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a material with specific id and type of a given model.

	Parameters
	----------
	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 node objects where each member of the list is an object of class Node referring to the node with the maximun coordinate in each direction of the specified material.
		- 0 = Node with the maximum X coordinate
		- 1 = Node with the maximum Y coordinate
		- 2 = Node with the maximum Z coordinate
		Upon failure, an empty list returned.

	See Also
	--------
	results.Result, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1001
		
		    max_node = materials.MaxCoordinatesOfMaterial(
		        model_id, material_type, material_id, result
		    )
		    if len(max_node):
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_coordinates instead.", DeprecationWarning)

def MaxDeformationOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 deformation objects where each member of the list is an object of class Deformation referring to the maximun deformation in each direction for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1001
		
		    max_deform = materials.MaxDeformationOfMaterial(result, material_type, material_id)
		    if len(max_deform):
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
		            max_total_deform.x, max_total_deform.y, max_total_deform.total
		        )  # Deformations in rest directions on the node with the maximum TOTAL deformation
		        print(
		            max_total_deform.node_id
		        )  # Id of the node with the maximum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_deformations instead.", DeprecationWarning)

def MinCoordinatesOfMaterial(result: object, material_id: int, material_type: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a material with specific id and type of a given model.

	Parameters
	----------
	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then minimum coordinates will refer to the ORIGINAL STATE.

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 node objects where each member of the list is an object of class Node referring to the node with the minimun coordinate in each direction of the specified material.
		- 0 = Node with the minimum X coordinate
		- 1 = Node with the minimum Y coordinate
		- 2 = Node with the minimum Z coordinate
		Upon failure, an empty list returned.

	See Also
	--------
	results.Result, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 15
		
		    min_node = materials.MinCoordinatesOfMaterial(
		        model_id, material_type, material_id, result
		    )
		    if len(min_node):
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_coordinates instead.", DeprecationWarning)

def MinDeformationOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL), of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 deformation objects where each member of the list is an object of class Deformation referring to the minimun deformation in each direction for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		
		    min_deform = materials.MinDeformationOfMaterial(result, material_type, material_id)
		    if len(min_deform):
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
		            min_total_deform.x, min_total_deform.y, min_total_deform.total
		        )  # Deformations in rest directions on the node with the minimum TOTAL deformation
		        print(
		            min_total_deform.node_id
		        )  # Id of the node with the minimum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_deformations instead.", DeprecationWarning)

def MinMaxCentroidScalarOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CentroidScalar objects where each member of the list is an object of class CentroidScalar referring to the minimum or maximun centroid scalar value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1001
		    centroid = materials.MinMaxCentroidScalarOfMaterial(
		        result, material_type, material_id
		    )
		    if len(centroid):
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxCentroidVectorOfMaterial(result: object, material_type: int, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constants).

	material_id : int
		Id of the material.

	Returns
	-------
	object
		It returns a list with 2 CentroidVector objects where each member of the list refers to the minimum or maximun centroid vector value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1001
		    centroid = materials.MinMaxCentroidVectorOfMaterial(
		        result, material_type, material_id
		    )
		    if len(centroid):
		        min_centroid = centroid[0]  # Object with the minimum centroid vector value
		        print(min_centroid.value)  # Minimum centroid vector value
		        print(
		            min_centroid.x, min_centroid.y, min_centroid.z
		        )  # Normalized coordinates (X,Y,Z) of the minimum centroid vector
		        print(
		            min_centroid.element_id, min_centroid.second_id, min_centroid.type
		        )  # Id, second id and type of the element with the minimum centroid vector value
		
		        max_centroid = centroid[1]  # Object with the maximum centroid vector value
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_vector instead.", DeprecationWarning)

def MinMaxCornerScalarOfMaterial(result: object, material_type: int, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	object
		It returns a list with 2 CornerScalar objects where each member of the list refers to the minimum or maximun corner scalar value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		    corner = materials.MinMaxCornerScalarOfMaterial(result, material_type, material_id)
		    if len(corner):
		        min_corner = corner[0]  # Object with the minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		
		        max_corner = corner[1]  # Object with the maximum corner scalar value
		        print(max_corner.value)  # Maximum corner scalar value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element with the maximum corner scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_corner_scalar instead.", DeprecationWarning)

def MinMaxNodalScalarOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constants).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalScalar objects where each member refers to the minimum or maximun nodal scalar value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		    nodal = materials.MinMaxNodalScalarOfMaterial(result, material_type, material_id)
		    if len(nodal):
		        min_nodal = nodal[0]  # Object with minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal scalar value
		        print(min_nodal.part_id)  # Id of the part
		
		        max_nodal = nodal[1]  # Object with maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal scalar value
		        print(max_nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxNodalVectorOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector values of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalVector objects where each member of the list refers to the minimum or maximun nodal vector value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		    nodal = materials.MinMaxNodalVectorOfMaterial(result, material_type, material_id)
		    if len(nodal):
		        min_nodal = nodal[0]  # Object with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector value
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(
		            min_nodal.part_id
		        )  # Id of the part of the node with the minimum nodal vector value
		
		        max_nodal = nodal[1]  # Object with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal vector value
		        print(
		            max_nodal.part_id
		        )  # Id of the part of the node with the maximum nodal vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodal_vector instead.", DeprecationWarning)

def NamedColorOfMaterial(window_name: str, material_id: int, material_type: int, model_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_color` instead.


	This function finds the name of the color of a material of a model with a given id and a given type.

	Parameters
	----------
	window_name : str
		Name of the window of the material. If it is absent then this function will return the color of the material for the first enabled window of the model of the material.

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	model_id : int
		Id of the model.

	Returns
	-------
	str
		It returns a string referring to the name of the color of the corresponding material of the given model for the specified window.
		Upon failure, an empty string is returned.

	See Also
	--------
	windows.Color, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    window_name = "MetaPost"
		    named_color = materials.NamedColorOfMaterial(
		        model_id, material_type, material_id, window_name
		    )
		    print(named_color)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_color instead.", DeprecationWarning)

def NeighbourMaterials(model_id: int, material_type: int, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_materials` instead.


	This function collects the neighbour materials of a given material of a specified model. Neighbour materials are these which are directly attached to the specified material.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific neighbour material of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    neighbour_materials = materials.NeighbourMaterials(
		        model_id, material_type, material_id
		    )
		    for m in neighbour_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_materials instead.", DeprecationWarning)

def NodalScalarOfMaterial(layer: str, material_id: int, material_type: int, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a material with specific id and type of a given model.

	Parameters
	----------
	layer : str
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : 
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalScalar referring to one nodal scalar value of a node of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1
		    material_nodal = materials.NodalScalarOfMaterial(result, material_type, material_id)
		    iter_end = min(10, len(material_nodal))
		    for nodal in material_nodal[0:iter_end]:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfMaterial(layer: str, material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_nodal_vector` instead.


	This function calculates all nodal vector values of the nodes of a material with specific id and type of a given model.

	Parameters
	----------
	layer : str
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member is an object of class NodalVector referring to one nodal vector value of a node of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1
		    material_nodal = materials.NodalVectorOfMaterial(result, material_type, material_id)
		    iter_end = min(10, len(material_nodal))
		    for nodal in material_nodal[0:iter_end]:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_nodal_vector instead.", DeprecationWarning)

def NumOfMaterialsByType(material_type: int, model_id: int) -> int:

	"""

	This function finds the number of the materials of a model with a specific type.

	Parameters
	----------
	material_type : int
		Type of the material (META constants).

	model_id : int
		Id of the model.

	Returns
	-------
	int
		It returns the number of the materials with the specific type for the given model.
		Upon failure, 0 is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    num_of_materials = materials.NumOfMaterialsByType(model_id, material_type)
		    print(num_of_materials)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PickMaterials(model_id: int, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.pick_materials` instead.


	This function allows picking the materials of a model specified by the given id. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.

	Parameters
	----------
	model_id : int
		Id of the model. If model_id is equal to -1, then this function will work for all models.

	message : str
		Message displayed to the user when the function is called.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific picked material of the given model(s).
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    message = "Select Materials and press Enter when you are ready"
		    picked_materials = materials.PickMaterials(model_id, message)
		    for m in picked_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.pick_materials instead.", DeprecationWarning)

def PropertyOfMaterial(material_id: int, property_type: str, model_id: int) -> Any:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_property` instead.


	This function returns the property for a material with a specific id and belonging to a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	property_type : str
		Argument 'property_type' defines the type of the property which will be returned. Its possible values are:
		- 'all'
		- 'e'
		- 'e1'
		- 'e2'
		- 'e3'
		- 'n' or 'v' (Nastran/Abaqus notation)
		- 'n12', 'v12' (Nastran/Abaqus notation)
		- 'n13', 'v13'
		- 'n23', 'v23'
		- 'g12'
		- 'g13'
		- 'g23'
		- 'a1'
		- 'a2'
		- 'a3'
		- 'ge'
		- 'tref'
		- 'rho'
		- 'xt'
		- 'xc'
		- 'yt'
		- 'yc'
		- 'zt'
		- 'zc'
		- 's12'
		- 's13'
		- 's23'
		- 'f12'
		- 'f13'
		- 'f23'
		- 'strain_or_stress'
		- 'property_type'

	model_id : int
		Id of the model.

	Returns
	-------
	Any
		If "property_type" is "all", it returns a string referring to the properties of the specified material as they are specified in geometry file.
		If "property_type" is "strain_or_stress", this function will return 1 in the case that the type of limit is strain and 0 in the case that the type of limit is stress.
		For all other valid "property_type" options, it returns a float value referring to the property of the specified material.
		Else, a zero value or an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    property_type = "e"
		    property_value = materials.PropertyOfMaterial(model_id, material_id, property_type)
		    print(property_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_property instead.", DeprecationWarning)

def ReportNewMaterials() -> object:

	"""

	This function collects the newly created materials from the last call of script function meta.materials.CollectNewMaterialsStart(). This function should be preceded by a corresponding call to script function meta.materials.CollectNewMaterialsStart() and should be followed by a corresponding call to script function meta.materials.CollectNewMaterialsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Material referring to one specific newly created material.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import utils
		
		
		def main():
		    materials.CollectNewMaterialsStart()
		
		    # create new materials
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_materials = materials.ReportNewMaterials()
		
		    for m in new_materials:
		        print(m.id, m.type, m.name, m.model_id)
		    materials.CollectNewMaterialsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetPropertyOfMaterial(model_id: int, material_id: int, property_type: str, property_value: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.set_property` instead.


	This function sets a property for a material with a specific id of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_id : int
		Id of the material

	property_type : str
		Type of the property. Its possible values are:
		---MAT1---
		- 'e'
		- 'n' or 'v' (Nastran/Abaqus notation)
		- 'rho'
		---MAT8---
		- 'e1'
		- 'e2'
		- 'e3'
		- 'n12', 'v12' (Nastran/Abaqus notation)
		- 'n13', 'v13'
		- 'n23', 'v23'
		- 'g12'
		- 'g13'
		- 'g23'
		- 'a1'
		- 'a2'
		- 'a3'
		- 'ge'
		- 'tref'
		- 'rho'
		- 'xt'
		- 'xc'
		- 'yt'
		- 'yc'
		- 'zt'
		- 'zc'
		- 's12'
		- 's13'
		- 's23'
		- 'f12'
		- 'f13'
		- 'f23'
		- 'strain_or_stress': strain_or_stress refer to FAILSTRAIN or FAILSTRESS of Abaqus.

	property_value : float
		Value of the property.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    property_type = "e"
		    property_value = 25000
		    ret = materials.SetPropertyOfMaterial(
		        model_id, material_id, property_type, property_value
		    )
		    print(materials.PropertyOfMaterial(model_id, material_id, property_type))
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.set_property instead.", DeprecationWarning)

def ShellNormalOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_shell_normal` instead.


	This function calculates the shell normal vectors of the SHELL elements of a material with a specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CentroidVector referring to the shell normal vector of a SHELL element of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CentroidVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		    material_normal = materials.ShellNormalOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_normal))
		    for shell_normal in material_normal[
		        0:iter_end
		    ]:  # List with the CentroidVector objects (shell normal vector)
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_shell_normal instead.", DeprecationWarning)

def ShowMaterial(model_id: int, material_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.show` instead.


	This function allows the user to make visible a material of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_id : int
		Id of the material.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	materials.ShowSomeMaterials

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_id = 1
		    ret = materials.ShowMaterial(model_id, material_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.show instead.", DeprecationWarning)

def ShowSomeMaterials(model_id: int, material_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.show_materials` instead.


	This function allows the user to make visible some specific materials of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_ids : object
		Ids of the materials.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_ids = list()
		    all_materials = materials.Materials(model_id)
		    for m in all_materials:
		        material_ids.append(m.id)
		    ret = materials.ShowSomeMaterials(model_id, material_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.show_materials instead.", DeprecationWarning)

def StringMaterialType(material_type: int) -> str:

	"""

	This function converts a given META constant material type to its corresponding string representation.

	Parameters
	----------
	material_type : int
		Type of the material (META constant).

	Returns
	-------
	str
		It returns a string referring to the name of the META constant material type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		
		
		def main():
		    material_type = constants.MAT1
		    str_material_type = materials.StringMaterialType(material_type)
		    print(str_material_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateMaterial(material: object) -> object:

	"""

	This function updates the data of the given material object. Update is based in the fields 'id', 'type' and 'model_id' of the given elem object.

	Parameters
	----------
	material : object
		Object of class Material.

	Returns
	-------
	object
		Upon success, it returns the new updated material object.
		Else, None is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		from meta import utils
		
		
		def main():
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    m = materials.MaterialById(model_id, material_type, material_id)
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		        # commands which alter the data of the material struct
		        utils.MetaCommand('name mid "plastic" 1001')
		        m = materials.UpdateMaterial(m)
		        if m:  # Update OK
		            print(m.id, m.type, m.name, m.model_id)
		        else:  # Update FAILED
		            print("This is not a valid material struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaterialOfElement(model_id: int, element_id: int, element_type: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.elements.Element.get_material` instead.


	This function finds the material of an element of a specified model.

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
		Upon success, it returns a material object with the material of the element.
		Else, a non valid material object is returned.

	See Also
	--------
	materials.Material, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import materials
		
		
		def main():
		    model_id = 0
		    element_type = constants.SHELL
		    element_id = 1
		    second_id = -1
		    m = materials.MaterialOfElement(model_id, element_type, element_id, second_id)
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.elements.Element.get_material instead.", DeprecationWarning)

def AreaOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_area` instead.


	This function calculates the area of a matterial with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then area will refer to the ORIGINAL STATE.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated area of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[0]
		    material_type = constants.MAT1
		    material_id = 1
		    area = materials.AreaOfMaterial(result, material_type, material_id)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_area instead.", DeprecationWarning)

def AreaIntegralOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_area_integral` instead.


	This function calculates the integral of a resultset over the area of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then area integral will refer to the ORIGINAL STATE.

	material_type : int
		Type of material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value as the result of the calculated area integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    material_type = constants.MAT1
		    material_id = 1
		    areaint = materials.AreaIntegralOfMaterial(result, material_type, material_id)
		    print(areaint)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_area_integral instead.", DeprecationWarning)

def VolumeOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_volume` instead.


	This function calculates the volume of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then volume will refer to the ORIGINAL STATE.

	material_type : int
		Type of material (META constant).

	material_id : int
		Id of material.

	Returns
	-------
	float
		It returns a float value being the calculated volume of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[0]
		    material_type = constants.MAT1
		    material_id = 1
		    volume = materials.VolumeOfMaterial(result, material_type, material_id)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_volume instead.", DeprecationWarning)

def VolumeIntegralOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_volume_integral` instead.


	This function calculates the integral of a resultset over the volume of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model. If the specified resultset does not contain deformation information, then volume integral will refer to the ORIGINAL STATE.

	material_type : int
		Type of material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated volume integral.
		Upon failure, 0 will be returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    result = results.Resultsets(model_id)[1]
		    material_type = constants.MAT1
		    material_id = 1
		    volint = materials.VolumeIntegralOfMaterial(result, material_type, material_id)
		    print(volint)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_volume_integral instead.", DeprecationWarning)

def MaterialsBySolverIdAllTypes(model_id: int, material_path: str, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_materials` instead.


	This function finds materials of a model with hierarchical structure defined by id and path of encapsulating substructures.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_path : str
		Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given material is limited.

	material_id : int
		Id of the material.

	Returns
	-------
	object
		This function returns a list with objects of class Material referring to the corresponding materials found.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_path = "Truck->13->132"
		    material_id = 2
		    collected_materials = materials.MaterialsBySolverIdAllTypes(
		        model_id, material_path, material_id
		    )
		
		    for m in collected_materials:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_materials instead.", DeprecationWarning)

def CornerVectorOfMaterial(layer: str, material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_vector` instead.


	This function calculates all corner vector values of the elements of a given material of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CornerVector objects where each member of the list refers to the corner vector values of an element of the specified material.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.CornerVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    material_type = constants.MAT1
		    material_id = 1001
		    material_corner = materials.CornerVectorOfMaterial(
		        result, material_type, material_id
		    )
		    iter_end = min(10, len(material_corner))
		    for corn in material_corner[0:iter_end]:  # List with CornerScalar objects
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_vector instead.", DeprecationWarning)

def MinMaxCornerVectorOfMaterial(material_id: int, material_type: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_centroid_vector` instead.


	This function calculates minimum and maximum corner vector value of a material with specific id and type of a given model.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : int
		Type of the material (META constant).

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CornerVector objects where each member of the list refers to the minimum or maximun corner scalar value for the specified material.
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
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    material_type = constants.MAT1
		    material_id = 1
		    corner = materials.MinMaxCornerVectorOfMaterial(result, material_type, material_id)
		    if len(corner):
		        min_corner = corner[0]  # Object with the minimum corner scalar value
		        print(min_corner.value)  # Minimum corner scalar value
		        print(min_corner.x)  # X component corner value
		        print(min_corner.y)  # Y component corner value
		        print(min_corner.z)  # Z component corner value
		        print(
		            min_corner.element_id, min_corner.second_id, min_corner.type
		        )  # Id, second id and type of the element with the minimum corner scalar value
		
		        max_corner = corner[1]  # Object with the maximum corner scalar value
		        print(max_corner.value)  # Maximum corner scalar value
		        print(max_corner.x)  # X component corner value
		        print(max_corner.y)  # Y component corner value
		        print(max_corner.z)  # Z component corner value
		        print(
		            max_corner.element_id, max_corner.second_id, max_corner.type
		        )  # Id, second id and type of the element with the maximum corner scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_centroid_vector instead.", DeprecationWarning)

def AreaWeightedAverageOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_area_weighted_average` instead.


	This function calculates the area weighted average of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated area weighted average of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    area = materials.AreaWeightedAverageOfMaterial(
		        all_resultsets[1], material_type, mid
		    )
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_area_weighted_average instead.", DeprecationWarning)

def VolumeWeightedAverageOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_volume_weighted_average` instead.


	This function calculates the volume weighted average of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated volume weighted average of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    volume = materials.VolumeWeightedAverageOfMaterial(
		        all_resultsets[1], material_type, mid
		    )
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_volume_weighted_average instead.", DeprecationWarning)

def VolumetricFlowOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated volumetric flow rate of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    rate = materials.VolumetricFlowOfMaterial(all_resultsets[1], material_type, mid)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_mass_flow` instead.


	This function calculates the mass flow rate of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated mass flow rate of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    mass = materials.MassFlowOfMaterial(all_resultsets[1], material_type, mid)
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_mass_weighted_average` instead.


	This function calculates the mass weighted average of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value being the calculated mass weighted average of the specified material.
		Upon failure, an invalid value of 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    mass = materials.MassWeightedAverageOfMaterial(
		        all_resultsets[1], material_type, mid
		    )
		    print(mass)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_mass_weighted_average instead.", DeprecationWarning)

def NormalForceOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_normal_force` instead.


	This function calculates the normal force of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the part (META constant).

	material_id : int
		Id of the part.

	Returns
	-------
	float
		It returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    force = materials.NormalForceOfMaterial(all_resultsets[1], material_type, mid)
		    print(force)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_normal_force instead.", DeprecationWarning)

def ShearForceOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_shear_force` instead.


	This function calculates the shear force of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    force = materials.ShearForceOfMaterial(all_resultsets[1], material_type, mid)
		    print(force)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_shear_force instead.", DeprecationWarning)

def VectorUniformityIndexOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value as the result of the calculated vector uniformity index of the material.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    index = materials.VectorUniformityIndexOfMaterial(
		        all_resultsets[1], material_type, mid
		    )
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_vector_uniformity_index instead.", DeprecationWarning)

def UniformityIndexOfMaterial(result: object, material_type: int, material_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_uniformity_index` instead.


	This function calculates the uniformity index of a material with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	material_type : int
		Type of the material (META constant).

	material_id : int
		Id of the material.

	Returns
	-------
	float
		It returns a float value as the result of the calculated uniformity index of the material.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		import meta
		from meta import materials
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    mid = 1
		    material_type = constants.MAT1
		
		    index = materials.UniformityIndexOfMaterial(all_resultsets[1], material_type, mid)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_uniformity_index instead.", DeprecationWarning)

def AttributeOfMaterial(model_id: int, material_id: int, attribute_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The number of the model

	material_id : int
		The id of the material

	attribute_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    mid = 0
		    name = "Total_parts"
		
		    val = materials.AttributeOfMaterial(model_id, mid, name)
		    print("Value " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_attributes instead.", DeprecationWarning)

def SetAttributeOfMaterial(model_num: int, material_id: int, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given material. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_num : int
		The number of the model.

	material_id : int
		The id of the material.

	attribute_name : str
		Name of the attribute.

	attribute_value : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    mid = 0
		
		    name = "attr_name"
		    val = "test"
		    materials.SetAttributeOfMaterial(model_id, mid, name, val)
		    # or
		    name = "num_attr_name"
		    val = 1.1
		    attribute_type = "numerical"
		    materials.SetAttributeOfMaterial(model_id, mid, name, val, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.set_attribute instead.", DeprecationWarning)

def AttributesOfMaterial(model_id: int, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_attributes` instead.


	This function collects all attributes of a given material

	Parameters
	----------
	model_id : int
		The number of the model

	material_id : int
		The id of the material

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    mid = 0
		
		    all_attributes = materials.AttributesOfMaterial(model_id, mid)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_attributes instead.", DeprecationWarning)

def MaterialStiffnessMatrix(model_num: int, material_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.materials.Material.get_stiffness_matrix` instead.


	This function calculates material stiffness matrix in the material coord system along the fiber or E1 or EL direction

	Parameters
	----------
	model_num : int

	material_id : int

	Returns
	-------
	object
		It returns a 3X3 matrix in the form of a list that contains other lists.
		Upon failure, all the list values will all be 0.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import materials
		
		
		def main():
		    model_num = 0
		    material_id = 2
		
		    stiff_mat = materials.MaterialStiffnessMatrix(model_num, material_id)
		
		    for tmp_mat in stiff_mat:
		        print(tmp_mat)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.materials.Material.get_stiffness_matrix instead.", DeprecationWarning)

def IdentifyMaterialsReset(model_id: int, material_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_materials` instead.


	This function allows the user to reset the identification of all or specific materials of the specified model. It can be called with two different ways. The one is with lists of ids, and the other is with material_ids = 'all'.

	Parameters
	----------
	model_id : int
		Id of the model.

	material_ids : object
		List with Ids of the materials as integers, or string 'all'.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    model_id = 0
		    material_ids = [1, 2, 3]
		    # or
		    # material_ids ='all'
		    materials.IdentifyMaterialsReset(model_id, material_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_materials instead.", DeprecationWarning)

class Material():

	"""

	Class for materials
	
	The type of the material is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corresponding constant names of constant values.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    if mat:
		        print(mat.id, mat.type, mat.name, mat.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    r = mat.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    mat_parts = mat.get_parts(specifier)
		    for p in mat_parts:
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
		from meta import materials
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=3, model_id=m.id)
		    specifier = "all"
		    elems = mat.get_elements(specifier)
		    # elems = mat.get_elements(specifier, type=constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "outer"
		    elems = mat.get_elements(specifier)
		    # elems = mat.get_elements(specifier, type=constants.SOLID)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    elems = mat.get_elements(specifier, point_coordinates=point)
		    # elems = mat.get_elements(specifier, point_coordinates = point , resultset = res )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "neighbour"
		    elems = mat.get_elements(specifier)
		    # elems = mat.get_elements(specifier, type=constants.SOLID)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    mat_nodes = mat.get_nodes(specifier)
		    specifier = "outer"
		    # mat_nodes = mat.get_nodes(specifier)
		    for n in mat_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    mat_nodes = mat.get_nodes(specifier, window=w)
		    specifier = "visible_outer"
		    mat_nodes = mat.get_nodes(specifier, window=w)
		    for n in mat_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    res = m.get_current_resultset()
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    mat_nodes = mat.get_nodes(specifier, distance_type="x", point_coordinates=point)
		    # mat_nodes = mat.get_nodes(specifier, \tdistance_type = 'x', point_coordinates , resultset = res)
		    for n in mat_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_materials
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "neighbour"
		    mats = mat.get_materials(specifier)
		    for mat in mats:
		        print(mat.id, mat.type, mat.name, mat.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_comments
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    comm = mat.get_comments()
		    print(comm)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_stiffness_matrix
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    stiff = mat.get_stiffness_matrix()
		    print(stiff)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_property
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    property_type = "e"
		    prop = mat.get_property(property_type)
		    print(prop)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    normal = mat.get_shell_normal(res)
		    for centroid in normal:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    win = windows.Window(name="MetaPost", page_id=0)
		    mat = materials.Material(id=2, model_id=m.id)
		    color = mat.get_color(win)
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = mat.set_attribute(attribute_name, attribute_type, attribute_value)
		    attr = mat.get_attributes()
		    # attribute_name = 'new_attr'
		    # attr = mat.get_attributes(attribute_name)
		    print(ret)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_material_limit
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    material_limit_type = "tension"
		    material_limit = 12.2
		    ret = mat.set_material_limit(material_limit_type, material_limit)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_area(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_volume(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_area_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_integral
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_volume_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_area_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume_weighted_average
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_volume_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_volumetric_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_mass_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_mass_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_force
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_normal_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_force
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_shear_force(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_uniformity_index
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    val = mat.get_vector_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "min"
		    coords = mat.get_coordinates(specifier)
		    # coords = mat.get_coordinates(specifier, resultset)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "max"
		    mat_deforms = mat.get_deformations(resultset, specifier)
		    for deform in mat_deforms:
		        print(deform.x)  # X deformation
		        print(deform.y)  # Y deformation
		        print(deform.z)  # Z deformation
		        print(deform.total)  # Total deformation
		        print(deform.node_id)  # Id of the node
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, mag, nodes = mat.get_deformations(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(mag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=1, model_id=m.id)
		    specifier = "min"
		
		    mat_nodal = mat.get_nodal_scalar(resultset, specifier)
		    # mat_nodal = mat.get_nodal_scalar(resultset, specifier , layer = 'top' )
		    for nodal in mat_nodal:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=1, model_id=m.id)
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
		from meta import models
		from meta import materials
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "min"
		    mat_nodal = mat.get_nodal_vector(resultset, specifier)
		    # mat_nodal = mat.get_nodal_vector(resultset, specifier , layer = 'top' )
		    for nodal in mat_nodal:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, magn, nodes = mat.get_nodal_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import materials
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    mat = materials.Material(id=0, model_id=m.id)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    part_centroid = mat.get_centroid_scalar(resultset, specifier)
		    # part_centroid = part.get_centroid_scalar(resultset, specifier, layer = 'top')
		    for centroid in part_centroid:
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=0, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element"]
		
		    values, elems = mat.get_centroid_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import models
		from meta import materials
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "min"
		    mat_centroid = mat.get_centroid_vector(resultset, specifier)
		    # mat_centroid= mat.get_centroid_vector(resultset, specifier, layer = 'top' )
		    for centroid in mat_centroid:  # List with CentroidScalar objects
		        print(centroid.value)  # Centroid vector value
		        print(
		            centroid.x, centroid.y, centroid.z
		        )  # Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element"]
		
		    xyz, magn, elems = mat.get_centroid_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import models
		from meta import materials
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "min"
		    mat_corner = mat.get_corner_scalar(resultset, specifier)
		    # mat_corner= mat.get_corner_scalar(resultset, specifier, layer = 'top')
		    for corner in mat_corner:
		        print(corner.value)  # Corner scalar value
		        print(
		            corner.element_id, corner.second_id, corner.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    np_specifier = ["value", "element", "corner_id"]
		
		    values, elems, corners = mat.get_corner_scalar(
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
		from meta import materials
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    mat = materials.Material(id=2, model_id=m.id)
		    specifier = "all"
		    mat_corner = mat.get_corner_vector(resultset, specifier)
		    # specifier = 'max'
		    # mat_corner= mat.get_corner_vector(resultset, specifier, layer = 'bottom')
		    for corner in mat_corner:  # List with CornerScalar objects
		        print(corner.value)  # Corner vector value
		        print(
		            corner.x, corner.y, corner.z
		        )  # Normalized coordinates (X, Y, Z) of the corner vector
		        print(
		            corner.element_id, corner.second_id, corner.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    mat = materials.Material(id=2, model_id=m.id)
		    np_specifier = ["xyz", "magnitude", "element", "corner_id"]
		
		    xyz, magn, elems, corners = mat.get_corner_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    name = "mat_name"
		    ret = mat.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = mat.set_attribute(attribute_name, attribute_type, attribute_value)
		    attribute_type = "string"
		    attribute_value = "my_atrribute"
		    # ret = mat.set_attribute(attribute_name, attribute_type, attribute_value)
		    attribute_name = "new_attr"
		    attr = mat.get_attributes(attribute_name)
		    print(ret)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_material_limit
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=1, model_id=m.id)
		    material_limit_type = "tension"
		    material_limit = 12.2
		    ret = mat.set_material_limit(material_limit_type, material_limit)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_property
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    property_type = "e"
		    property_value = 12.2
		    ret = mat.set_property(property_type, property_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    ret = mat.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    ret = mat.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    ret = mat.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material_limit
		# PYTHON script
		import meta
		from meta import materials
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=1, model_id=m.id)
		    material_limit_type = "tension"
		    limit = mat.get_material_limit(material_limit_type)
		    print(limit)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import materials
		
		
		def main():
		    mat = materials.Material(id=2, model_id=0)
		    can_use = mat.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    res = m.get_current_resultset()
		    val = mat.get_normal_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shear_moment
		# PYTHON script
		import meta
		from meta import *
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=2, model_id=m.id)
		    res = m.get_current_resultset()
		    val = mat.get_shear_moment(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import materials
		from meta import constants
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    mat = materials.Material(id=0, model_id=m.id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    col = windows.Color(name="my_color", r=0, g=255, b=255, a=255)
		    ret = mat.set_color(color=col, window=w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Name of the material.

	"""

	model_id: int = None
	"""
	Model number of the material.

	"""

	type: int = None
	"""
	Type of the material (mETA constant).

	"""

	name: str = None
	"""
	Name of the material.

	"""

	def set_color(self, color: object, window: object) -> bool:

		"""

		This method sets the color of the material


		Parameters
		----------
		color : object
			The color of the material

		window : object
			The window in which the material color will be set

		Returns
		-------
		bool

		"""


	def get_parts(self, specifier: str) -> object:

		"""

		This method gets the parts of the material.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : gets all the parts of the material (default value).

		Returns
		-------
		object
			Upon success, it returns a list of objects of class Part. Upon failure, it returns an empty list.

		"""


	def get_elements(self, specifier: str, type: int, point_coordinates: object, resultset: object, range: str) -> object:

		"""

		This method gets the elements of the material.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : gets all the elements of the material (default value). Optionally combined with argument: type.
			- 'outer' : gets the outer elements of the material. Outer element is the one whose at least one node belongs to an element of a different material. Optionally combined with argument: type.
			- 'nearest' : gets the nearest element of the material from a specific point. Must be combined with argument: point_coordinates. Optionally combined with argument: resultset.
			- 'neighbour' : gets the neighbour elements of a given material, belonging to the model. Neighbour element is the one which is directly attached to the material through one or more nodes. Optionally combined with argument: type.
			- 'range' : Provide a range of Element Ids in the argument range.

		type : int, optional
			The type of the element that the method will return. If absent, elements of all types will returned. Used when the specifier is 'all', 'outer', 'neighbour'.

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. If it is absent, then the result will be calculated for the ORIGINAL STATE. Used only when the specifier is 'nearest'.

		range : str, optional
			Element Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list of objects of class Element. Upon failure, it returns an empty list.

		"""


	def get_nodes(self, specifier: str, distance_type: str, point_coordinates: object, resultset: object, window: object, range: str) -> object:

		"""

		This method gets the nodes of the material.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the nodes of the material (default value).
			- 'visible' : visible nodes of the material. Optionally combined with argument: window.
			- 'outer' : outer nodes of the material. Outer node is the one who belongs to an element which does not belong to this material.
			- 'visible_outer' : visible outer nodes of the material. Outer node is the one who belongs to an element which does not belong to this material. Optionally combined with argument: window.
			- 'nearest' : Returns the nearest node to the material. Must be combined with arguments: distance_type, point_coordinates. Optionally combined with argument: resultset.
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

		point_coordinates : object, optional
			Coordinates of the point (list of floats). It is required when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		resultset : object, optional
			An object of class Result that refers to a Resultset of the model. It is used when the specifier is 'nearest'. If the specifier has a different value, this argument is ignored.

		window : object, optional
			An object of class window. This argument is used when specifier is 'visible' or 'visible_outer'. If the specifier has a different value, this argument is ignored. If this argument is set, the method will return only the visible nodes in this window.

		range : str, optional
			Node Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list of objects of class Node. Upon failure, it returns an empty list.

		"""


	def get_materials(self, specifier: str) -> object:

		"""

		This method gets the neighbour materials of the material.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible value is:
			- 'neighbour' : gets the neighbour materials of the material. Neighbour materials are these which are directly attached to the specified material.

		Returns
		-------
		object
			Upon success, it returns a list of objects of class Material. Upon failure, it returns an empty list.

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of the material.


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the material. Upon failure, it returns None.

		"""


	def get_stiffness_matrix(self) -> object:

		"""

		This method gets material stiffness matrix in the material coord system along the fiber or E1 or EL direction


		Returns
		-------
		object
			Upon success, it returns a 3X3 matrix in the form of a list that contains other lists.Upon failure, it returns an empty list.

		"""


	def get_property(self, property_type: str) -> str:

		"""

		This method gets the property for a material with a specific id and belonging to a given model.


		Parameters
		----------
		property_type : str
			Defines the type of the property which will be returned. Its possible values are:
			- 'all'
			- 'e'
			- 'e1'
			- 'e2'
			- 'e3'
			- 'n' or 'v' (Nastran/Abaqus notation)
			- 'n12', 'v12' (Nastran/Abaqus notation)
			- 'n13', 'v13'
			- 'n23', 'v23'
			- 'g'
			- 'g12'
			- 'g13'
			- 'g23'
			- 'a'
			- 'a1'
			- 'a2'
			- 'a3'
			- 'a4'
			- 'a5'
			- 'a6'
			- 'ge'
			- 'tref'
			- 'rho'
			- 'xt'
			- 'xc'
			- 'yt'
			- 'yc'
			- 'zt'
			- 'zc'
			- 's12'
			- 's13'
			- 's23'
			- 'f12'
			- 'f13'
			- 'f23'
			- 'strain_or_stress'
			- 'property_type'

		Returns
		-------
		str
			If "property_type" is "all", it returns a string referring to the properties of the specified material as they are specified in geometry file.If "property_type" is "strain_or_stress", this function will return 1 in the case that the type of limit is strain and 0 in the case that the type of limit is stress.For all other valid "property_type" options, it returns a float value referring to the property of the specified material.Else, None is returned.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vectors of the SHELL elements of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class CentroidVector referring to the shell normal vector of a SHELL element of the specified material. Upon failure, an empty list is returned.

		"""


	def get_area(self, resultset: object) -> float:

		"""

		This method gets the area of the matterial.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated area of the material. Upon failure, it returns None.

		"""


	def get_volume(self, resultset: object) -> float:

		"""

		This method gets the volume of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			It returns a float value being the calculated volume of the material. Upon failure, an invalid value of 0 will be returned.

		"""


	def get_area_integral(self, resultset: object) -> float:

		"""

		This method gets the integral of a resultset over the area of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated area integral.Upon failure, None will be returned.

		"""


	def get_volume_integral(self, resultset: object) -> float:

		"""

		This method gets the integral of a resultset over the volume of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated volume integral.Upon failure, None will be returned.

		"""


	def get_area_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the area weighted average of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated area weighted average of the material.Upon failure, it returns None.

		"""


	def get_volume_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the volume weighted average of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated volume weighted average of the material.Upon failure, it reurns None.

		"""


	def get_mass_flow(self, resultset: object) -> float:

		"""

		This method gets the mass flow rate of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated mass flow rate of the material. Upon failure, it returns None

		"""


	def get_mass_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the mass weighted average of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated mass weighted average of the material.Upon failure, it returns None.

		"""


	def get_normal_force(self, resultset: object) -> object:

		"""

		This method gets the normal force of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude. Upon failure, it returns an empty list.

		"""


	def get_shear_force(self, resultset: object) -> object:

		"""

		This method gets the shear force of a material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a list of floats where the first element is the component X, the second elelement the component Y, the third the component Z and the fourth the magnitude. Upon failure, it returns an empty list.

		"""


	def get_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the uniformity index of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated uniformity index of the material.Upon failure, it returns None.

		"""


	def get_vector_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the vector uniformity index of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value as the result of the calculated vector uniformity index of the material.Upon failure, it returns None.

		"""


	def get_color(self, window: object) -> object:

		"""

		This method gets the color of the material.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		object
			Upon success, it returns an object of class Color. Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the material.


		Parameters
		----------
		attribute_name : str, optional
			Attribute name.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_material_limit(self, material_limit_type: str) -> float:

		"""

		This method gets the material limit of the material.


		Parameters
		----------
		material_limit_type : str
			Type of the material limit. Its possible values are:
			- 'tension'
			- 'compression'
			- 'shear'
			- 'x_tension'
			- 'y_tension'
			- 'z_tension'
			- 'x_compression'
			- 'y_compression'
			- 'z_compression'
			- 'shear'
			- 's13'
			- 's23'
			- 'f12'
			- 'f13'
			- 'f23'

		Returns
		-------
		float
			Upon success, it returns as a float the material limit of the specified material.Upon failure, it returns None.

		"""


	def get_coordinates(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the minimum or maximum coordinates of the material.


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
			Upon success, it returns a list with the minimum or maximum coordinates.Upon failure, it returns an empty list.

		"""


	def get_deformations(self, resultset: object, specifier: str, numpy: object) -> object:

		"""

		This method gets the deformation values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations (default value).
			- 'max' : maximum deformations.
			- 'min' : minimum deformations.

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

		This method gets the nodal scalar values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar (default value).
			- 'max' : maximum nodal scalar.
			- 'min' :  minimum nodal scalar.

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
			Upon success, it returns a list with objects of class NodalScalar. Upon failure, it returns an empty list.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal vector values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector (default value).
			- 'max' : maximum nodal vector.
			- 'min' : minimum nodal vector.

		layer : str, optional
			Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
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

		This method gets the centroid scalar values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid scalar (default value).
			- 'max' : maximum centroid scalar.
			- 'min' : minimum centroid scalar.

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
			Upon success, it returns a list with objects of class CentroidScalar. Upon failure, it returns an empty list.

		"""


	def get_centroid_vector(self, resultset: object, specifier: str, layer: str, numpy: object) -> object:

		"""

		This method gets the centroid vector values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid vector (default value).
			- 'max' : maximum centroid vector.
			- 'min' : minimum centroid vector.

		layer : str, optional
			Location of the centroid vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

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


	def get_corner_scalar(self, resultset: object, specifier: object, layer: str, numpy: object) -> object:

		"""

		This method gets the corner scalar values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar (default value).
			- 'max' : maximum corner scalar.
			- 'min' : minimum corner scalar.

		layer : str, optional
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
			Upon success, it returns a list with objects of class CornerScalar. Upon failure, it returns an empty list.

		"""


	def get_corner_vector(self, resultset: object, specifier: object, layer: str, numpy: object) -> object:

		"""

		This method gets the corner vector values of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : object, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector (default value).
			- 'max' : maximum corner vector.
			- 'min' : minimum corner vector.

		layer : str, optional
			Location of the corner scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
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


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the material.


		Parameters
		----------
		name : str
			Name of the material.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the material.


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


	def set_material_limit(self, material_limit_type: str, material_limit: float) -> bool:

		"""

		This method sets material limit on the material.


		Parameters
		----------
		material_limit_type : str
			Type of the material limit. Its possible values are:
			- 'tension'
			- 'compression'
			- 'shear'
			- 'x_tension'
			- 'y_tension'
			- 'z_tension'
			- 'x_compression'
			- 'y_compression'
			- 'z_compression'
			- 'shear'
			- 's13'
			- 's23'
			- 'f12'
			- 'f13'
			- 'f23'

		material_limit : float
			Material limit of material.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_property(self, property_type: str, property_value: float) -> bool:

		"""

		This method sets a property for the material.


		Parameters
		----------
		property_type : str
			Type of the property. Its possible values are:
			---MAT1---
			- 'e'
			- 'n' or 'v' (Nastran/Abaqus notation)
			- 'rho'
			- 'g'
			- 'ge'
			- 'a'
			---MAT8---
			- 'e1'
			- 'e2'
			- 'e3'
			- 'n12', 'v12' (Nastran/Abaqus notation)
			- 'n13', 'v13'
			- 'n23', 'v23'
			- 'g12'
			- 'g13'
			- 'g23'
			- 'a1'
			- 'a2'
			- 'a3'
			- 'a4'
			- 'a5'
			- 'a6'
			- 'ge'
			- 'tref'
			- 'rho'
			- 'xt'
			- 'xc'
			- 'yt'
			- 'yc'
			- 'zt'
			- 'zc'
			- 's12'
			- 's13'
			- 's23'
			- 'f12'
			- 'f13'
			- 'f23'
			- 'strain_or_stress': strain_or_stress refer to FAILSTRAIN or FAILSTRESS of Abaqus.

		property_value : float
			Value of the property.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the material. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the material. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the material. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def get_volumetric_flow(self, resultset: object) -> float:

		"""

		This method gets the volumetric flow rate of the material.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns a float value being the calculated volumetric flow  of the material. Upon failure, it returns None

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Material entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_normal_moment(self, resultset: object) -> object:

		"""

		This method gets the normal moment of the material.


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


	def set_color(self, color: object, window: object) -> bool:

		"""

		This method sets the color of the material


		Parameters
		----------
		color : object
			The color of the material

		window : object
			The window in which the material color will be set

		Returns
		-------
		bool

		"""

