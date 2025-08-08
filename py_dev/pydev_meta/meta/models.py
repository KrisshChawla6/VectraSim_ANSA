from __future__ import annotations
from typing import *

def ActiveModels() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_models` instead.


	This function collects all the current active loaded 3D models.

	Returns
	-------
	object
		It returns a list with model objects where each member of the list refers to the corresponding active loaded 3D model.
		Upon failure an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    act_models = models.ActiveModels()
		    for mdl in act_models:
		        print(mdl.id, mdl.name)
		        print(mdl.label, mdl.deck, mdl.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_models instead.", DeprecationWarning)

def AddLabelOnModel(label: str, model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_label` instead.


	This function adds a label on an existing model.

	Parameters
	----------
	label : str
		Label of the model.

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
		from meta import models
		
		
		def main():
		    model_id = 0
		    label = "GEOM_MODEL 3"
		    models.AddLabelOnModel(model_id, label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_label instead.", DeprecationWarning)

def AvailableGeometriesOfAnimatorDB(filename: str) -> object:

	"""

	This function gets the available geometries of a given Animator DB file. The results of this function can be used as input in script function "LoadAnimatorDBModel".

	Parameters
	----------
	filename : str
		Name of the Animator DB file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to one specific available geometry of the given Animator DB file.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    filename = "/home/examples/Car_with_Spiders_static.a3db"
		    all_geom = AvailableGeometriesOfAnimatorDB(filename)
		    for avail_geom in all_geom:
		        print(avail_geom)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AvailableGeometriesOfProject(filename: str) -> object:

	"""

	This function gets the available geometries of a given project file (.metadb). The results of this function can be used as input in script function "LoadProjectModel".

	Parameters
	----------
	filename : str
		Name of the project file.

	Returns
	-------
	object
		It returns a list with where each member of the list is a string referring to one specific available geometry of the given project file.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    filename = "/home/examples/Ex1.metadb"
		    all_geom = models.AvailableGeometriesOfProject(filename)
		    for avail_geom in all_geom:
		        print(avail_geom)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CentroidScalarOfModel(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_scalar` instead.


	This function calculates all centroid scalar values for a model specified by its id.

	Parameters
	----------
	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CentroidScalar objects where ach member of the list refers to the centroid scalar value of an element of the specified model.
		Upon failure, an empty list is returned.

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
		
		    layer = "bottom"
		    # Bottom centroid scalar values in case both bottom and top centroid scalar values are loaded
		    all_centroid = models.CentroidScalarOfModel(result, layer)
		
		    for i in range(1, min(len(all_centroid), 10)):
		        print(all_centroid[i].value, all_centroid[i].element_id)
		        print(all_centroid[i].second_id, all_centroid[i].type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_scalar instead.", DeprecationWarning)

def CentroidScalarOfModelNonZero(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_scalar` instead.


	This function calculates non zero centroid scalar values for a model specified by its id.

	Parameters
	----------
	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CentroidScalar objects where each member of the listrefers to the non zero centroid scalar value of an element of the specified model.
		Upon failure, an empty list is returned.

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
		
		    layer = "bottom"
		    # Bottom centroid scalar values if both bottom and top centroid scalar values are loaded
		    all_centroid = models.CentroidScalarOfModelNonZero(result, layer)
		    for i in range(1, min(len(all_centroid), 10)):
		        print(all_centroid[i].value, all_centroid[i].element_id)
		        print(all_centroid[i].second_id, all_centroid[i].type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_scalar instead.", DeprecationWarning)

def CentroidVectorOfModel(layer: str, principal: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_vector` instead.


	This function calculates all centroid vector values of an existing model.

	Parameters
	----------
	layer : str, optional
		Location of the centroid vector values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	principal : str, optional
		Principal order of the centroid vector tensor values. It should be specified only when tensor results have been loaded. Possible values are:
		- 'first': first principal (default)
		- 'second': second principal
		- 'third': third principal

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CentroidVector objects where each member of the list refers to the centroid vector value of an element of the specified model.
		Upon failure, an empty list is returned.

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
		    for i in range(1, min(len(all_centroid), 10)):
		        print(
		            all_centroid[i].value,
		            all_centroid[i].element_id,
		            all_centroid[i].second_id,
		            all_centroid[i].type,
		        )
		        print(all_centroid[i].x, all_centroid[i].y, all_centroid[i].z)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_vector instead.", DeprecationWarning)

def CentroidVectorOfModelNonZero(layer: str, principal: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_vector` instead.


	This function calculates non zero centroid vector values of an existing model.

	Parameters
	----------
	layer : str, optional
		Location of the centroid vector values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	principal : str, optional
		Principal order of the centroid vector tensor values. It should be specified only when tensor results have been loaded. Possible values are:
		- 'first': first principal (default)
		- 'second': second principal
		- 'third': third principal

	result : object, optional
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CentroidVector objects where each member of the list refers to the non zero centroid vector value of an element of the specified model.
		Upon failure, an empty list is returned.

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
		    all_centroid = models.CentroidVectorOfModelNonZero(result)
		    for i in range(1, min(len(all_centroid), 10)):
		        print(
		            all_centroid[i].value,
		            all_centroid[i].element_id,
		            all_centroid[i].second_id,
		            all_centroid[i].type,
		        )
		        print(all_centroid[i].x, all_centroid[i].y, all_centroid[i].z)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_vector instead.", DeprecationWarning)

def CollectEntities(entity_type: str, mode: str, window_name: str) -> object:

	"""

	This function collects entities of META.

	Parameters
	----------
	entity_type : str
		Type of the collected entities. Its possible values are:
		- 'models' : Collect models
		- 'pages' : Collect pages
		- 'windows' : Collect windows
		- 'resultsets' : Collect resultsets
		- 'parts' : Collect parts
		- 'materials' : Collect materials
		- 'nodes' : Collect nodes
		- 'elements' : Collect elements
		- 'boundaries' : Collect boundary elements
		- 'groups' : Collect groups
		- 'coord_systems' : Collect coordinate systems
		- 'plots' : Collect plots
		- 'curves' : Collect curves
		- 'points' : Collect points
		- 'annotations' : Collect annotations
		- 'images' : Collect images
		- 'videos' : Collect videos
		- 'planes' : Collect planes
		- 'isofunctions' : Collect isofunctions

	mode : str, optional
		Option for collecting all, visible, or identified entities. Its possible values are:
		"all" : All entities (default option)
		"visible" : Visible entities
		"identified" : Identified entities

	window_name : str, optional
		The name of the window, on which are the visible/identified entities

	Returns
	-------
	object
		It returns a list with where each member of the list is an object referring to one specific entity of META.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    entity_type = "materials"
		    collected_materials = models.CollectEntities(entity_type)
		    print("Materials")
		    for m in collected_materials:
		        print(m.id, m.name)
		    entity_type = "parts"
		    # collected_parts = models.CollectEntities(entity_type, 'visible', window_name ='MetaPost')
		    collected_parts = models.CollectEntities(
		        entity_type, "identified", window_name="MetaPost"
		    )
		    print("Parts")
		    for p in collected_parts:
		        print(p.id, p.name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectModelEntities(entity_type: str, model_id: int, mode: str, window_name: str) -> object:

	"""

	This function collects entities of the model specified by the given id. 

	Parameters
	----------
	entity_type : str
		Type of the collected entities. Its possible values are:
		- 'parts' : Collect parts
		- 'materials' : Collect materials
		- 'nodes' : Collect nodes
		- 'elements' : Collect elements
		- 'boundaries' : Collect boundary elements
		- 'groups' : Collect groups
		- 'coord_systems' : Collect coordinate systems

	model_id : int
		Id of the model.

	mode : str, optional
		Option for collecting all, visible, or identified entities. Its possible values are:
		"all" : All entities (default option)
		"visible" : Visible entities
		"identified" : Identified entities

	window_name : str, optional
		The name of the window, on which are the visible/identified entities

	Returns
	-------
	object
		It returns a list with objects where each member of the list is an object referring to one specific entity of the given model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    entity_type = "parts"
		    collected_entities = models.CollectModelEntities(model_id, entity_type)
		    for p in collected_entities:
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

def CollectNewEntitiesEnd() -> object:

	"""

	This function ends recording the creation of new entities. This function should be preceded by a corresponding call to script function CollectNewEntitiesStart().

	Returns
	-------
	object
		It returns a list with objects where each member of the list is an object referring to one specific entity of META.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		from meta import annotations
		from meta import visuals
		
		
		def main():
		    models.CollectNewEntitiesStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 1 "Empty Annotation"')
		    utils.MetaCommand('annotation add 2 "Empty Annotation"')
		
		    # create new images
		    utils.MetaCommand('image read image0 "/home/examples/Ex1.png"')
		    utils.MetaCommand('image read image1 "/home/examples/Ex2.png"')
		
		    new_entities = models.CollectNewEntitiesEnd()
		    for ent in new_entities:
		        if annotations.IsAnnotation(ent):
		            a = ent
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		        elif visuals.IsImage(ent):
		            img = ent
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewEntitiesStart() -> int:

	"""

	This function starts recording the creation of new entities. This function should be followed by a corresponding call to script function CollectNewEntitiesEnd().

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
		from meta import utils
		from meta import annotations
		from meta import visuals
		
		
		def main():
		    models.CollectNewEntitiesStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 1 "Empty Annotation"')
		    utils.MetaCommand('annotation add 2 "Empty Annotation"')
		
		    # create new images
		    utils.MetaCommand('image read image0 "/home/examples/Ex1.png"')
		    utils.MetaCommand('image read image1 "/home/examples/Ex2.png"')
		
		    new_entities = models.CollectNewEntitiesEnd()
		    for ent in new_entities:
		        if annotations.IsAnnotation(ent):
		            a = ent
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		        elif visuals.IsImage(ent):
		            img = ent
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewModelsEnd() -> object:

	"""

	This function ends recording the creation of new models. This function should be preceded by a corresponding call to script function CollectNewModelsStart().

	Returns
	-------
	object
		It returns a list with model objects where each member of the list refers to one specific newly created model.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		
		
		def main():
		    models.CollectNewModelsStart()
		
		    # create new models
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/user/1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/user/2.nas")
		
		    new_models = models.CollectNewModelsEnd()
		    for r in new_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewModelsStart() -> int:

	"""

	This function starts recording the creation of new models. This function should be followed by a corresponding call to script function CollectNewModelsEnd().

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
		from meta import utils
		
		
		def main():
		    models.CollectNewModelsStart()
		
		    # create new models
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/user/1.nas")
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/user/2.nas")
		
		    new_models = models.CollectNewModelsEnd()
		    for r in new_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ColorOfModel(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_color` instead.


	This function finds color of a model.

	Parameters
	----------
	window_name : str, optional
		Name of the window. If it is absent then this function will return the color of the model for the first enabled window.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns a color object with the color of the corresponding model for the specified window.
		Else, a non valid color object is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    col = models.ColorOfModel(model_id, window_name)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_color instead.", DeprecationWarning)

def CornerScalarOfModel(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_scalar` instead.


	This function calculates all corner scalar values of the elements of a model.

	Parameters
	----------
	layer : str, optional
		Location of the corner scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CornerScalar objects where each member of the list refers to the corner scalar values of an element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

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
		
		    layer = "bottom"
		    # Bottom centroid scalar values in case both bottom and top centroid scalar values are loaded
		    all_corner = models.CornerScalarOfModel(result, layer)
		
		    for i in range(1, min(len(all_corner), 10)):
		        print(all_corner[i].value)  # Corner scalar value
		        print(
		            all_corner[i].element_id, all_corner[i].second_id, all_corner[i].type
		        )  # Id, second id and type of the element
		        print(
		            all_corner[i].corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_scalar instead.", DeprecationWarning)

def CornerScalarOfModelNonZero(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_scalar` instead.


	This function calculates non zero corner scalar values of the elements of a model.

	Parameters
	----------
	layer : str, optional
		Location of the centroid scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with CornerScalar objects where each member of the list is refers to the non zero corner scalar values of an element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

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
		
		    layer = "bottom"
		    # Bottom centroid scalar values in case both bottom and top centroid scalar values are loaded
		    all_corner = models.CornerScalarOfModelNonZero(result, layer)
		
		    for i in range(1, min(len(all_corner), 10)):
		        print(all_corner[i].value)  # Corner scalar value
		        print(
		            all_corner[i].element_id, all_corner[i].second_id, all_corner[i].type
		        )  # Id, second id and type of the element
		        print(
		            all_corner[i].corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_scalar instead.", DeprecationWarning)

def DeformationLabelsOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_deformation_labels` instead.


	This function finds all deformation labels for given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with strings, where each member refers to one deformation label of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_labels = models.DeformationLabelsOfModel(model_id)
		    for deform_label in all_labels:
		        print(deform_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_deformation_labels instead.", DeprecationWarning)

def DeformationsOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of a model. Deformations refer to a resultset specified by its object.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with deformation objects where each member of the list refers to a deformation of a node for the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

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
		    for i in range(1, min(len(all_deform), 10)):
		        print(
		            all_deform[i].x,
		            all_deform[i].y,
		            all_deform[i].z,
		            all_deform[i].total,
		            all_deform[i].node_id,
		        )  # X, Y, Z, Total Deformation, Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_deformations instead.", DeprecationWarning)

def DeformationsOfModelNonZero(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_deformations` instead.


	This function calculates non zero deformations for each direction (X, Y, Z, TOTAL), of a model. Deformations refer to a resultset specified by its object.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with deformation objects where each member of the list is refers to a non zero deformation of a node for the given model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.Deformation

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
		
		    all_deform = models.DeformationsOfModelNonZero(result)
		    for i in range(1, min(len(all_deform), 10)):
		        print(
		            all_deform[i].x,
		            all_deform[i].y,
		            all_deform[i].z,
		            all_deform[i].total,
		            all_deform[i].node_id,
		        )  # X, Y, Z, Total Deformation, Id of the node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_deformations instead.", DeprecationWarning)

def DeleteModel(model_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.delete` instead.


	This function deletes an existing model.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Defines the window from which the model will be removed. If it is absent then model will be deleted from all windows in which is loaded.

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
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    ret = models.DeleteModel(model_id, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.delete instead.", DeprecationWarning)

def FunctionLabelsOfModel(model_id: int) -> object:

	"""

	This function finds all function labels (scalar or vector) for given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with all function labels where each member of the list is a string referring to one function label of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_labels = models.FunctionLabelsOfModel(model_id)
		    for function_label in all_labels:
		        print(function_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def HasDeformations(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.has_deformations` instead.


	This function checks if deformations are loaded on a resultset of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

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
		    result = all_resultsets[1]
		
		    has_deform = models.HasDeformations(result)
		    print(has_deform)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.has_deformations instead.", DeprecationWarning)

def HasScalar(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.has_scalar` instead.


	This function checks if scalar results are loaded on a state specified by a resultset of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

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
		    result = all_resultsets[1]
		
		    has_scalar = models.HasScalar(result)
		    print(has_scalar)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.has_scalar instead.", DeprecationWarning)

def HasVector(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.has_vector` instead.


	This function checks if vector results are loaded on a state specified by a resultset of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

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
		    result = all_resultsets[1]
		
		    has_vector = models.HasVector(result)
		    print(has_vector)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.has_vector instead.", DeprecationWarning)

def IsModel(model: object) -> int:

	"""

	This function checks whether an object is of class Model.

	Parameters
	----------
	model : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Model, 0 otherwise.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		
		
		def main():
		    objects = list()
		    objects.append(models.Models()[0])
		    objects.append(None)
		
		    for ob in objects:
		        if models.IsModel(ob):
		            print("This is an object of class Models")
		            print(ob.id, ob.name, ob.label, ob.deck, ob.active)
		        else:
		            print("This is not an object of class Models")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsScalar(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.is_scalar` instead.


	This function checks if scalar results are loaded on a specific resultset of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

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
		    result = all_resultsets[1]
		
		    is_scalar = models.IsScalar(result)
		    print(is_scalar)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.is_scalar instead.", DeprecationWarning)

def IsVector(result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.is_vector` instead.


	This function checks if vector results are loaded on a specific resultset of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

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
		    result = all_resultsets[1]
		
		    is_vector = models.IsVector(result)
		    print(is_vector)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.is_vector instead.", DeprecationWarning)

def LayerIntegrationPointsOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_layer_integration_points` instead.


	This function finds the layer integration points of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with the layer integration points of the specified model.
		Each member of the list is a string referring to one layer integration point of the given model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		
		    layer_integration_points = models.LayerIntegrationPointsOfModel(model_id)
		    for str in layer_integration_points:
		        print(str)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_layer_integration_points instead.", DeprecationWarning)

def LayersOfModel(layer_type: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_layers` instead.


	This function finds the layers of a model with a given id (model_id). 

	Parameters
	----------
	layer_type : str
		Type of the layer. Possible values are:
		- 'Layer'
		- 'GlobalLayer'
		- 'NamedLayer'

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the number or the id of a layer of the given model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    layer_type = "NamedLayer"
		
		    all_layers = models.LayersOfModel(model_id, layer_type)
		    for str in all_layers:
		        print(str)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_layers instead.", DeprecationWarning)

def LoadAnimatorDBModel(filename: str, label: str, window_name: str) -> object:

	"""

	This function loads the geometry of a 3D model from an Animator file with a given filename.

	Parameters
	----------
	filename : str
		Filepath of the Animator DB file.

	label : str
		Label of the geometry that will be loaded.

	window_name : str
		Name of the window that the model will be loaded into.

	Returns
	-------
	object
		Upon success, it returns an object of class Model referring to the currently loaded model.
		Else, a non valid Model object is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    window_name = "MetaPost"
		    filename = "/home/geo/proj5.a3db"
		    label = "0"
		    r = models.LoadAnimatorDBModel(window_name, filename, label)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadModel(window_name: str, filename: str, deck: str, failed_elements: str, initial_data: str) -> object:

	"""

	This function loads the geometry of a 3D model from a file with a given filename. The model is being loaded in an existing 3D window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	filename : str
		Name of the file.

	deck : str
		Deck name of the model (e.g. 'AUTO', 'NASTRAN', 'DYNA', 'ABAQUS', 'PAMCRASH', 'ANSYS', 'RADIOSS', etc.). The names can be found in betameta_structs.META_KEYWORDS

	failed_elements : str, optional
		Defines whether failed elements are loaded. Possible values are:
		- 'failed' : Failed elements are loaded - default value if absent
		- 'nofailed' : Failed elements are not loaded

	initial_data : str, optional
		Defines whether initial data (e.g. strains, stresses, partition data) are loaded
		- 'on' : Initial data are loaded as states - default value if absent
		- 'off' : Initial data are not loaded

	Returns
	-------
	object
		Upon success, it returns an object of class Model referring to the currently loaded model.
		Else, a non valid Model object is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    window_name = "MetaPost"
		    filename = "/home/examples/AbaqusEx8.inp"
		    deck = "ABAQUS"
		    r = models.LoadModel(window_name, filename, deck)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadProjectModel(filename: str, label: str, window_name: str) -> object:

	"""

	This function loads the geometry of a 3D model from a META project file (.metadb).

	Parameters
	----------
	filename : str
		Filepath of the project file.

	label : str
		Label of the geometry.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns an object of class Model referring to the currently loaded model.
		Else, a non valid Model object is returned.

	See Also
	--------
	models.AvailableGeometriesOfProject, models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    window_name = "MetaPost"
		    filename = "/home/examples/Ex1.metadb"
		    label = "label"
		    r = models.LoadProjectModel(window_name, filename, label)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MaxCoordinatesOfModel(result: object, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a given model. Maximum coordinates refer to the position of the nodes for a given resultset.

	Parameters
	----------
	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 Node objects where each member of the list is an object of class Node referring to the node with the maximun coordinate in each direction of the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    max_node = models.MaxCoordinatesOfModel(model_id, result)
		    if len(max_node):
		        max_x_node = max_node[0]  # Object of class Node with the maximum X coordinate
		        print(
		            max_x_node.x, max_x_node.y, max_x_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = max_node[1]  # Object of class Node with the maximum Y coordinate
		        print(
		            max_y_node.x, max_y_node.y, max_y_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the maximum Y coordinate
		        print(max_y_node.id)  # Id of the node with the maximum Y coordinate
		
		        max_z_node = max_node[2]  # Object of class Node with the maximum Z coordinate
		        print(
		            max_z_node.x, max_z_node.y, max_z_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the maximum Z coordinate
		        print(max_z_node.id)  # Id of the node with the maximum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinates instead.", DeprecationWarning)

def MaxDeformationOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects where each member of the list is an object of class Deformation referring to the maximum deformation in each direction for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_deformations instead.", DeprecationWarning)

def MinCoordinatesOfModel(result: object, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a given model.

	Parameters
	----------
	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then minimum coordinates will refer to the ORIGINAL STATE.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with 3 Node objects where each member of the list is an object of class Node referring to the node with the minimun coordinate in each direction of the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    min_node = models.MinCoordinatesOfModel(model_id, result)
		    if len(min_node):
		        min_x_node = min_node[0]  # Object of class Node with the minimum X coordinate
		        print(
		            min_x_node.x, min_x_node.y, min_x_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the minimum X coordinate
		        print(min_x_node.id)  # Id of the node with the minimum X coordinate
		
		        min_y_node = min_node[1]  # Object of class Node with the minimum Y coordinate
		        print(
		            min_y_node.x, min_y_node.y, min_y_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the minimum Y coordinate
		        print(min_y_node.id)  # Id of the node with the minimum Y coordinate
		
		        min_z_node = min_node[2]  # Object of class Node with the minimum Z coordinate
		        print(
		            min_z_node.x, min_z_node.y, min_z_node.z
		        )  # Coordinates in X, Y, Z directions of the node with the minimum Z coordinate
		        print(min_z_node.id)  # Id of the node with the minimum Z coordinate
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_coordinates instead.", DeprecationWarning)

def MinDeformationOfModel(result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL), of a model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 4 Deformation objects where each member of the list is an object of class Deformation referring to the minimum deformation in each direction for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    min_deform = models.MinDeformationOfModel(result)
		    if len(min_deform):
		        min_x_deform = min_deform[0]  # Object with minimum deformation in direction X
		        print(
		            min_x_deform.x, min_x_deform.y, min_x_deform.z, min_x_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the minimum X deformation
		        print(min_x_deform.node_id)  # Id of the node with the minimum X deformation
		
		        min_y_deform = min_deform[0]  # Object with minimum deformation in direction Y
		        print(
		            min_y_deform.x, min_y_deform.y, min_y_deform.z, min_y_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the minimum Y deformation
		        print(min_y_deform.node_id)  # Id of the node with the minimum Y deformation
		
		        min_z_deform = min_deform[0]  # Object with minimum deformation in direction Z
		        print(
		            min_z_deform.x, min_z_deform.y, min_z_deform.z, min_z_deform.total
		        )  # Deformations in X, Y, Z and Total directions on the node with the minimum Z deformation
		        print(min_z_deform.node_id)  # Id of the node with the minimum Z deformation
		
		        min_total_deform = min_deform[0]  # Object with minimum TOTAL deformation
		        print(
		            min_total_deform.x,
		            min_total_deform.y,
		            min_total_deform.z,
		            min_total_deform.total,
		        )  # Deformations in X, Y, Z and Total directions on the node with the minimum TOTAL deformation
		        print(
		            min_total_deform.node_id
		        )  # Id of the node with the minimum TOTAL deformation
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_deformations instead.", DeprecationWarning)

def MinMaxCentroidScalarOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_scalar` instead.


	This function calculates minimum and maximum centroid scalar value for a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CentroidScalar objects where each member of the list refers to the minimum or maximun centroid scalar value for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    centroid = models.MinMaxCentroidScalarOfModel(result)
		    if centroid:
		        min_centroid = centroid[0]  # Object with minimum centroid scalar value
		        print(
		            min_centroid.value,
		            min_centroid.element_id,
		            min_centroid.second_id,
		            min_centroid.type,
		        )  # Minimum centroid scalar value, Id, second id and type of the element with the minimum centroid scalar value
		
		        max_centroid = centroid[1]
		        # Object with maximum centroid scalar value
		        print(
		            max_centroid.value,
		            max_centroid.element_id,
		            max_centroid.second_id,
		            max_centroid.type,
		        )  # Maximum centroid scalar value, Id, second id and type of the element with the maximum centroid scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_scalar instead.", DeprecationWarning)

def MinMaxCentroidVectorOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_centroid_vector` instead.


	This function calculates minimum and maximum centroid vector values of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CentroidVector objects where each member of the list refers to the minimum or maximun centroid vector value for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    centroid = models.MinMaxCentroidVectorOfModel(result)
		    if centroid:
		        min_centroid = centroid[0]  # Object with minimum centroid vector value
		        print(
		            min_centroid.value,
		            min_centroid.element_id,
		            min_centroid.second_id,
		            min_centroid.type,
		        )  # Minimum centroid vector value, Id, second id and type of the element with the minimum centroid vector value
		
		        max_centroid = centroid[1]
		        # Object with maximum centroid vector value
		        print(
		            max_centroid.value,
		            max_centroid.element_id,
		            max_centroid.second_id,
		            max_centroid.type,
		        )  # Maximum centroid vector value, Id, second id and type of the element with the maximum centroid vector value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_centroid_vector instead.", DeprecationWarning)

def MinMaxCornerScalarOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_scalar` instead.


	This function calculates minimum and maximum corner scalar value of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CornerScalar objects where each member of the list refers to the minimum or maximun corner scalar value for the specified model.
		        0 = MINIMUM corner scalar
		        1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerScalar

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
		
		    corner = models.MinMaxCornerScalarOfModel(result)
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
		        print(
		            max_corner.value,
		            max_corner.element_id,
		            max_corner.second_id,
		            max_corner.type,
		            max_corner.corner,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_scalar instead.", DeprecationWarning)

def MinMaxNodalScalarOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_scalar` instead.


	This function calculates minimum and maximum nodal scalar value for a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalScalar objects where each member of the list refers to the minimum or maximun nodal scalar value for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    nodal = models.MinMaxNodalScalarOfModel(result)
		    if len(nodal):
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_scalar instead.", DeprecationWarning)

def MinMaxNodalVectorOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_vector` instead.


	This function calculates minimum and maximum nodal vector values of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 NodalVector objects where each member of the list refers to the minimum or maximun nodal vector value for the specified model.
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
		from meta import models
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    nodal = models.MinMaxNodalVectorOfModel(result)
		    if len(nodal):
		        min_nodal = nodal[0]  # Object with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector value
		        print(min_nodal.node_id)  # Id of the node with the minimum nodal vector value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		        max_nodal = nodal[1]  # Object with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximum nodal vector value
		        print(max_nodal.node_id)  # Id of the node with the maximum nodal vector value
		        print(max_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_vector instead.", DeprecationWarning)

def ModelById(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_models` instead.


	This function searches for the model with the given model number.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		Upon success, it returns the model object with the given model number.
		Else, a non valid model object is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    r = models.ModelById(0)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_models instead.", DeprecationWarning)

def ModelByName(filename: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_models` instead.


	This function searches for the model with the given filename.

	Parameters
	----------
	filename : str
		Full absolute path of the file of the model.

	Returns
	-------
	object
		Upon success, it returns the model object with the given filename.
		Else, a non valid model object is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    filename = "/home/examples/EpilysisEx5.op2"
		    r = models.ModelByName(filename)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_models instead.", DeprecationWarning)

def Models() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_models` instead.


	This function collects all the currently loaded 3D models.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Model referring to the corresponding loaded 3D model.
		If no model is loaded, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    all_models = models.Models()
		    for r in all_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_models instead.", DeprecationWarning)

def ModelsByName(filename: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_models` instead.


	This function searches for the model with the given filename.

	Parameters
	----------
	filename : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Model referring to one specific model.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    filename = "*.cdb"
		    collected_models = models.ModelsByName(filename)
		    for r in collected_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_models instead.", DeprecationWarning)

def ModelsIn3DWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_models` instead.


	This function finds the models which are loaded in the 3D window.

	Parameters
	----------
	window_name : str
		Full name of the window.

	Returns
	-------
	object
		On success, it returns a list with Model objects where each member of the list refers to the corresponding model.
		On failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    window_name = "MetaPost"
		    window_models = models.ModelsIn3DWindow(window_name)
		    for r in window_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_models instead.", DeprecationWarning)

def ModelsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_models` instead.


	This function searches for the models of an overlay run with a given type.

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
		It returns a list where each member of the list is an object of class Model referring to one model of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_models = models.ModelsOfOverlayRun(overlay_run_type, overlay_run_id)
		    for r in overlay_run_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_models instead.", DeprecationWarning)

def NodalScalarOfModel(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with the NodalScalar objects where each member of the list refers to one nodal scalar value of a node of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

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
		
		    all_nodal = models.NodalScalarOfModel(result)  # Matrix with nodal_scalar structs
		    iter_end = min(10, len(all_nodal))
		    for nodal in all_nodal[0:iter_end]:
		        print(
		            nodal.value, nodal.node_id, nodal.part_id
		        )  # Nodal scalar value, Id of the node, Id of the part (-1 if no part exists)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_scalar instead.", DeprecationWarning)

def NodalScalarOfModelNonZero(layer: str, result) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_scalar` instead.


	This function calculates non zero nodal scalar values of the nodes of a given model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	result : 
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalScalar referring to one non-zero nodal scalar value of a node of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar

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
		
		    all_nodal = models.NodalScalarOfModelNonZero(
		        result
		    )  # Matrix with nodal_scalar structs
		    iter_end = min(10, len(all_nodal))
		    for nodal in all_nodal[0:iter_end]:
		        print(
		            nodal.value, nodal.node_id, nodal.part_id
		        )  # Nodal scalar value, Id of the node, Id of the part (-1 if no part exists)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfModel(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_vector` instead.


	This function calculates all nodal vector values of an existing model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalVector referring to one nodal vector value of a node of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

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
		
		    all_nodal = models.NodalVectorOfModel(result)  # Matrix with nodal_vector structs
		    iter_end = min(10, len(all_nodal))
		    for nodal in all_nodal[0:iter_end]:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_vector instead.", DeprecationWarning)

def NodalVectorOfModelNonZero(layer: str, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_nodal_vector` instead.


	This function calculates non zero nodal vector values of an existing model.

	Parameters
	----------
	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalVector referring to one non-zero nodal vector value of a node of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector

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
		
		    all_nodal = models.NodalVectorOfModelNonZero(
		        result
		    )  # Matrix with nodal_vector structs
		    iter_end = min(10, len(all_nodal))
		    for nodal in all_nodal[0:iter_end]:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_nodal_vector instead.", DeprecationWarning)

def NumOfModels() -> int:

	"""

	This function finds the number of the current loaded 3D models.

	Returns
	-------
	int
		It returns the number of the loaded 3D models.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    num_of_models = models.NumOfModels()
		    print(num_of_models)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PickModels(message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.pick_models` instead.


	This function allows the user to pick models from the existing windows. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.

	Parameters
	----------
	message : str
		Message displayed to the user which will be shown to the user when the function is called.

	Returns
	-------
	object
		It returns a list with Model objects where each member of the list is refers to one specific picked model.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    message = "Select Models and press Enter when you are ready"
		    picked_models = models.PickModels(message)
		    for r in picked_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.pick_models instead.", DeprecationWarning)

def ProjectedFrontalAreaOfModel(window_name: str, model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_projected_frontal_area` instead.


	This function finds the projected frontal area of a model's visible entities according to current view.

	Parameters
	----------
	window_name : str, optional
		Name of the window of the model. If it is absent then this function will return the projected frontal area of the model for the first enabled window.

	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the projected frontal area of the corresponding model for the specified window.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    proj_frontal_area = models.ProjectedFrontalAreaOfModel(model_id, window_name)
		    print(proj_frontal_area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_projected_frontal_area instead.", DeprecationWarning)

def ReferenceAreaOfModel(model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_reference_area` instead.


	This function finds the reference area of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the reference area of the corresponding model with the given id. 
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    ref_area = models.ReferenceAreaOfModel(model_id)
		    print(ref_area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_reference_area instead.", DeprecationWarning)

def ReferenceDensityOfModel(model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_reference_density` instead.


	This function finds the reference density of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the reference density of the corresponding model with the given id.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    ref_density = models.ReferenceDensityOfModel(model_id)
		    print(ref_density)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_reference_density instead.", DeprecationWarning)

def ReferenceLengthOfModel(model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_reference_length` instead.


	This function finds the reference length of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the reference length of the corresponding model with the given id.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    ref_length = models.ReferenceLengthOfModel(model_id)
		    print(ref_length)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_reference_length instead.", DeprecationWarning)

def ReferencePressureOfModel(model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_reference_pressure` instead.


	This function finds the reference pressure of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the reference pressure of the corresponding model with the given id.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    ref_pressure = models.ReferencePressureOfModel(model_id)
		    print(ref_pressure)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_reference_pressure instead.", DeprecationWarning)

def ReferenceVelocityOfModel(model_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_reference_velocity` instead.


	This function finds the reference velocity of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	float
		Upon success, it returns as a float the reference velocity of the specified model.
		Else, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    ref_veloc = models.ReferenceVelocityOfModel(model_id)
		    print(ref_veloc)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_reference_velocity instead.", DeprecationWarning)

def ReportNewEntities() -> object:

	"""

	This function collects the newly created entities from the last call of script function CollectNewEntitiesStart(). This function should be preceded by a corresponding call to script function CollectNewEntitiesStart() and should be followed by a corresponding call to script function CollectNewEntitiesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object referring to one specific entity of META.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		from meta import annotations
		from meta import visuals
		
		
		def main():
		    models.CollectNewEntitiesStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 1 "Empty Annotation"')
		    utils.MetaCommand('annotation add 2 "Empty Annotation"')
		
		    # create new images
		    utils.MetaCommand('image read image0 "/home/examples/Ex1.png"')
		    utils.MetaCommand('image read image1 "/home/examples/Ex2.png"')
		
		    new_entities = models.ReportNewEntities()
		    for ent in new_entities:
		        if annotations.IsAnnotation(ent):
		            a = ent
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		        elif visuals.IsImage(ent):
		            img = ent
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		            )
		    models.CollectNewEntitiesEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReportNewModels() -> object:

	"""

	This function collects the newly created models from the last call of script function CollectNewModelsStart(). This function should be preceded by a corresponding call to script function CollectNewModelsStart() and should be followed by a corresponding call to script function CollectNewModelsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Model referring to one specific newly created model.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		
		
		def main():
		    models.CollectNewModelsStart()
		
		    # create new models
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_models = models.ReportNewModels()
		    for r in new_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		    models.CollectNewModelsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetColorOfModel(model_id: int, red: int, green: int, blue: int, alpha: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_color` instead.


	This function sets color of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	red : int
		Red value.

	green : int
		Green value.

	blue : int
		Blue value.

	alpha : int
		Alpha channel value.

	window_name : str
		Name of the window.

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
		
		
		def main():
		    model_id = 0
		    red = 100
		    green = 255
		    blue = 255
		    alpha = 255
		    window_name = "MetaPost"
		    ret = models.SetColorOfModel(model_id, red, green, blue, alpha, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_color instead.", DeprecationWarning)

def ShellNormalOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_shell_normal` instead.


	This function calculates the shell normal vectors of the SHELL elements of a model. It takes into account the displaced structure according to a given resultset with deformations available.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list with the CentroidVector objects where each member of the list refers to the shell normal vector of a SHELL element of the specified model.
		Upon failure, an empty list is returned.

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
		
		    all_normal = models.ShellNormalOfModel(
		        result
		    )  # List with CentroidVector objects (shell normal vector)
		    iter_end = min(10, len(all_normal))
		    for shell_normal in all_normal[0:iter_end]:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_shell_normal instead.", DeprecationWarning)

def UpdateModel(model: object) -> object:

	"""

	This function updates the data of the given Model object. Update is based in the field 'id' of the given Model object.

	Parameters
	----------
	model : object
		Object of class Model.

	Returns
	-------
	object
		Upon success, it returns the new updated Model object.
		Else, a non valid Model object is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    r = models.ModelById(model_id)
		
		    # commands which alter the data of the model struct
		    utils.MetaCommand("model active empty")
		
		    r = models.UpdateModel(r)
		    if r:  # Update OK
		        print(r.id, r.name, r.label, r.deck, r.active)
		    else:  # Update FAILED
		        print("This is not a valid model object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def AreaOfModel(type: str, result: object) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_area` instead.


	This function calculates the area of a model. Model area is calculated as the sum of the areas of all SHELL and/or SOLID parts depending on the 'type' argument.

	Parameters
	----------
	type : str
		Determines the types of parts included in the estimation of the model area. Possible values are:
		- 'SHELL': Only shell elements are taken into account
		- 'SOLID': Only solid elements are taken into account
		- 'ALL': Both shell and solid elements are taken into account

	result : object
		An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then area will be calculated for the ORIGINAL STATE.

	Returns
	-------
	float
		It returns a float value being the area of the model calculated as the sum of the areas of all parts of the specified type (shell and/or solid).
		Upon failure, an invalid value of -1000 will be returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import models
		
		
		def main():
		    model_id = 0
		    type = "SHELL"
		    all_resultsets = results.Resultsets(model_id)
		    area = models.AreaOfModel(all_resultsets[0], type)
		    print("area = " + str(area))
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_area instead.", DeprecationWarning)

def StringFromAdvFilters(initial_filter: str, model_id: int) -> object:

	"""

	This function allows the user to specify the advanced filter for a given model. The execution of the script will stop and a window will open in order for the user to specify its advanced filters.

	Parameters
	----------
	initial_filter : str, optional
		Defines the initial advanced filter setting (e.g 'add:Elements:visible::Keep All').

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with the strings of the selected advanced filters. The first entry refers to state selection. The second entry is the advanced filter text as it would appear in a META command.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_filters = models.StringFromAdvFilters(model_id)
		    for filter in all_filters:
		        print(filter)
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleModelsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_models` instead.


	This function finds the visible models which are loaded in a given 3D window.

	Parameters
	----------
	window_name : str
		Full name of the 3d window

	Returns
	-------
	object
		On success, it returns a list where each member of the list is an object of class Model referring to the corresponding visible model.
		On failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    window_name = "MetaPost"
		    visible_models = models.VisibleModelsOfWindow(window_name)
		    for r in visible_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_models instead.", DeprecationWarning)

def VectorLabelsOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_vector_labels` instead.


	This function finds all vector labels for a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with all vector labels where each member of the list is a string referring to one vector label of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_labels = models.VectorLabelsOfModel(model_id)
		    for vector_label in all_labels:
		        print(vector_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_vector_labels instead.", DeprecationWarning)

def ScalarLabelsOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_scalar_labels` instead.


	This function finds all scalar labels for a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list with all scalar labels where each member of the list is a string referring to one scalar label of the corresponding model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_labels = models.ScalarLabelsOfModel(model_id)
		    for scalar_label in all_labels:
		        print(scalar_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_scalar_labels instead.", DeprecationWarning)

def CommentOfProject(filename: str) -> str:

	"""

	This function gets the comment of a given project file (.metadb). 

	Parameters
	----------
	filename : str
		Filename of the project file.

	Returns
	-------
	str
		It returns a string referring to the comment of the given project file.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    filename = "/home/examples/Ex1.metadb"
		    project_comment = models.CommentOfProject(filename)
		    print(project_comment)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CornerVectorOfModel(layer: str, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_vector` instead.


	This function calculates all corner vector values of the elements of a model.

	Parameters
	----------
	layer : str, optional
		Location of the corner scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns a list with CornerVector objects where each member of the list refers to the corner vector values of an element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

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
		
		    layer = "bottom"
		    # Bottom centroid vector values in case both bottom and top centroid vector values are loaded
		    all_corner = models.CornerVectorOfModel(result, layer)
		
		    for i in range(1, min(len(all_corner), 10)):
		        print(all_corner[i].value)  # Corner scalar value
		        print(all_corner[i].x)  # Corner X component value
		        print(all_corner[i].y)  # Corner Y component value
		        print(all_corner[i].z)  # Corner Z component value
		        print(
		            all_corner[i].element_id, all_corner[i].second_id, all_corner[i].type
		        )  # Id, second id and type of the element
		        print(
		            all_corner[i].corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_vector instead.", DeprecationWarning)

def MinMaxCornerVectorOfModel(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_vector` instead.


	This function calculates minimum and maximum corner vector value of a model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list with 2 CornerVector objects where each member of the list refers to the minimum or maximun corner scalar value for the specified model.
		        0 = MINIMUM corner scalar
		        1 = MAXIMUM corner scalar
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

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
		
		    corner = models.MinMaxCornerVectorOfModel(result)
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
		        print(
		            max_corner.value,
		            min_corner.x,
		            min_corner.y,
		            min_corner.z,
		            max_corner.element_id,
		            max_corner.second_id,
		            max_corner.type,
		            max_corner.corner,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_vector instead.", DeprecationWarning)

def CornerVectorOfModelNonZero(layer: str, result: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_corner_vector` instead.


	This function calculates all non zero corner vector values of the elements of a model.

	Parameters
	----------
	layer : str, optional
		Location of the corner scalar values. It should be specified only if both top and bottom values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	int
		It returns a list with CornerVector objects where each member of the list refers to the non zero corner vector values of an element of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.CornerVector

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
		
		    layer = "bottom"
		    # Bottom centroid vector values in case both bottom and top centroid vector values are loaded
		    all_corner = models.CornerVectorOfModelNonZero(result, layer)
		
		    for i in range(1, min(len(all_corner), 10)):
		        print(all_corner[i].value)  # Corner scalar value
		        print(all_corner[i].x)  # Corner X component value
		        print(all_corner[i].y)  # Corner Y component value
		        print(all_corner[i].z)  # Corner Z component value
		        print(
		            all_corner[i].element_id, all_corner[i].second_id, all_corner[i].type
		        )  # Id, second id and type of the element
		        print(
		            all_corner[i].corner
		        )  # Id of the node - corner for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_corner_vector instead.", DeprecationWarning)

def PickModelsFromList(message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.pick_models_from_list` instead.


	This function allows the user to select models from a given list. The execution of the script will stop and it will restart after the selection of the models from the list.

	Parameters
	----------
	message : str
		Message displayed to the user.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Model referring to one specific selected model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    message = "Select Models and press Enter when you are ready"
		    picked_models = models.PickModelsFromList(message)
		    for r in picked_models:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.pick_models_from_list instead.", DeprecationWarning)

def BoundingRectangleOfModel(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_bounding_rectangle` instead.


	This function finds the bounding rectangle of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a list where it contains in position 0 and 1 the screen X,Y coordinates [0,1] of the bottom left corner of the rectangle and in position 2 and 3 the screen X,Y coordinates of the top right corner of the rectangle. 
		Else, a list with zero length is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    rect = models.BoundingRectangleOfModel(model_id, window_name)
		    print(rect)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_bounding_rectangle instead.", DeprecationWarning)

def AttributeOfModel(model_id: int, attribute_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	model_id : int
		The number of the model

	attribute_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    attrib_name = "Deck"
		    val = models.AttributeOfModel(model_id, attrib_name)
		    print("Value: " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_attributes instead.", DeprecationWarning)

def SetAttributeOfModel(model_id: int, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	model_id : int
		The number of the model.

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
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		
		    attrib_name = "group.test_attrib"
		    value = "test_value"
		    models.SetAttributeOfModel(model_id, attrib_name, value)
		    # or
		    n_attrib_name = "group.n_test_attrib"
		    n_value = 0.1
		    attribute_type = "numerical"
		    models.SetAttributeOfModel(model_id, n_attrib_name, n_value, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.set_attribute instead.", DeprecationWarning)

def AttributesOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_attributes` instead.


	This function collects all attributes of a given model

	Parameters
	----------
	model_id : int
		The number of the model

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    all_attributes = models.AttributesOfModel(model_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_attributes instead.", DeprecationWarning)

def SetAttributeOfResultset(resultset: object, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given state. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	resultset : object
		An object of class Result that refers to a Resultset of the model.

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
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if len(all_resultsets):
		        res = all_resultsets[1]
		        name = "group.name"
		        value = "value"
		        results.SetAttributeOfResultset(res, name, value)
		        # or
		        name = "group.n_name"
		        value = 1.1
		        attribute_type = "numerical"
		        results.SetAttributeOfResultset(res, name, value, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.set_attribute instead.", DeprecationWarning)

def AttributesOfResultset(result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.results.Result.get_attributes` instead.


	This function collects all attributes of a given state

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

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
		    res = all_resultsets[1]
		    name = "group.name"
		    value = "value"
		
		    all_attributes = results.AttributesOfResultset(res)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.results.Result.get_attributes instead.", DeprecationWarning)

def ProjectedFrontalHoleAreaOfModel(model_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_projected_frontal_hole_area` instead.


	This function finds the projected frontal hole area of a model.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will return the projected frontal area of the model for the first enabled window.

	Returns
	-------
	float
		Upon success, it returns as a float the projected frontal hole area of the corresponding model for the specified window.
		Else, a zero value is returned.

	See Also
	--------
	ProjectedFrontalAreaOfModel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    proj_frontal_hole_area = models.ProjectedFrontalHoleAreaOfModel(
		        model_id, window_name
		    )
		    print(proj_frontal_hole_area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_projected_frontal_hole_area instead.", DeprecationWarning)

def GetHiddenOversetElements(resultset: object, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_elements` instead.


	This function returns a list with all the dead elements of the model's background and component volume meshes for the current state. If the model does not contain overset meshes or there exist no dead element, the function returns NULL.

	Parameters
	----------
	resultset : object
		is an object of class Result needed for the current state

	model_id : int
		is the Model id

	Returns
	-------
	object
		Upon success, it returns a list with all the dead elements of overset meshes. Otherwise it returns NULL.

	See Also
	--------
	EnableOversetCalc, DisableOversetCalc, HasOversets

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import models
		from meta import results
		from meta import elements
		
		
		def main():
		    window_name = "MetaPost"
		
		    model_filename = " /home/examples/oversets.cas"
		    results_filename = "/home/examples/oversets.dat"
		    deck = "FLUENT"
		    r = models.LoadModel(window_name, model_filename, deck)
		
		    states = "all"
		    data = "Pressure"
		    new_resultsets = results.LoadScalar(r.id, results_filename, deck, states, data)
		    all_resultsets = results.Resultsets(r.id)
		    res = all_resultsets[1]
		    results.SetCurrentResultset(r.id, res)
		    crn_res = results.CurrentResultset(r.id)
		
		    m = models.GetHiddenOversetElements(crn_res, r.id)
		
		    element_types = list()
		    element_ids = list()
		    second_ids = list()
		    all_elements = elements.Elements(r.id)
		
		    for e in all_elements:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		    elements.ShowSomeElements(r.id, element_types, element_ids, second_ids)
		
		    element_types.clear()
		    element_ids.clear()
		    second_ids.clear()
		
		    for e in m:
		        element_types.append(e.type)
		        element_ids.append(e.id)
		        second_ids.append(e.second_id)
		    elements.HideSomeElements(r.id, element_types, element_ids, second_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_elements instead.", DeprecationWarning)

def HasOversets(model_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.has_oversets()` instead.


	This function checks if the passing model as argument with id: model_id contains oversets. 

	Parameters
	----------
	model_id : int
		is the Model id

	Returns
	-------
	int
		This function returns 1 for models containing oversets. Otherwise it returns 0.

	See Also
	--------
	GetHiddenOversetElements, EnableOversetCalc, DisableOversetCalc

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import models
		
		
		def main():
		    act_models = models.ActiveModels()
		    r = act_models[0]
		
		    hasOversets = models.HasOversets(r.id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.has_oversets() instead.", DeprecationWarning)

def EnableOversetCalc() -> int:

	"""

	This function enables the oversets calculation.

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	DisableOversetCalc, HasOversets, GetHiddenOversetElements

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import models
		
		
		def main():
		    status = models.EnableOversetCalc()
		
		
		if __name__ == "__main__":
		    main()


	"""

def DisableOversetCalc() -> int:

	"""

	This function disables the oversets calculation.

	Returns
	-------
	int
		It always returns 0.

	See Also
	--------
	EnableOversetCalc, HasOversets, GetHiddenOversetElements

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import models
		
		
		def main():
		    status = models.DisableOversetCalc()
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectEntitiesI(entity_type: str, specifier: str, window: object) -> object:

	"""

	Creates an iterable with the entities of specific type. It offers better speed and less memory usage when it is just needed to iterate the result of CollectEntities.

	Parameters
	----------
	entity_type : str
		Type of the collected entities. Its possible values are:
		- 'nodes' : Collect nodes
		- 'elements' : Collect elements

	specifier : str, optional
		Option for collecting all, visible, or identified entities. Its possible values are:
		"all" : All entities (default option)
		"visible" : Visible entities
		"identified" : Identified entities

	window : object, optional
		The Window, on which are the visible/identified entities

	Returns
	-------
	object
		Upon success this function returns a Python iterator to the entities that are specified from the arguments.
		Upon failure returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    entity_type = "nodes"
		    nodes_iter = models.CollectEntitiesI(entity_type)
		
		    for n in nodes_iter:
		        print(n)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Model():

	"""

	Class for models.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    r = models.Model(0)
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    val = m.get_area(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_boundaries
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    bounds = m.get_boundaries(specifier)
		    # bounds = m.get_boundaries(specifier, boundary_type = constants.SPC )
		    # bounds = m.get_boundaries(specifier, boundary_type = constants.SPC , boundary_id = 1)
		    # bounds = m.get_boundaries(specifier, boundary_type = constants.SPC , boundary_id = 1, second_id = 5)
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "identified"
		    bounds = m.get_boundaries(specifier, window=w)
		    # bounds = m.get_boundaries(specifier, window = w, boundary_type = constants.SPC )
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    bounds = m.get_boundaries(specifier, window=w)
		    # bounds = m.get_boundaries(specifier, window = w, boundary_type = constants.SPC )
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    specifier = "with_name"
		    bounds = m.get_boundaries(specifier)
		    # bounds = m.get_boundaries(specifier, name = 'bound_name' )
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    specifier = "with_comments"
		    bounds = m.get_boundaries(specifier)
		    # bounds = m.get_boundaries(specifier, comment = 'bound_comment' )
		    for b in bounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_bounding_rectangle
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    rect = m.get_bounding_rectangle(w)
		    print(rect)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_centroid = m.get_centroid_scalar(resultset, specifier)
		    # specifier = 'all'
		    # model_centroid = m.get_centroid_scalar(resultset, specifier, non_zero = True)
		    # specifier = 'min'
		    # model_centroid = m.get_centroid_scalar(resultset, specifier, layer = 'top' )
		    for centroid in model_centroid:
		        print(centroid.value, centroid.element_id, centroid.second_id, centroid.type)
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["value", "element"]
		
		    values, elems = m.get_centroid_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_centroid_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_centroid = m.get_centroid_vector(resultset, specifier)
		    # specifier = 'all'
		    # model_centroid = m.get_centroid_vector(resultset, specifier, non_zero = True)
		    # specifier = 'min'
		    # model_centroid = m.get_centroid_vector(resultset, specifier, layer = 'top' )
		    for centroid in model_centroid:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Value and Normalized coordinates (X, Y, Z) of the centroid vector
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element"]
		
		    xyz, magn, elems = m.get_centroid_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(elems)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    col = m.get_color(w)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_connections
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    all_connections = m.get_connections(specifier)
		    # specifier = 'visible'
		    # all_connections = m.get_connections(specifier, connection_id = 0)
		    # all_connections = m.get_connections(specifier, connection_type = constants.SEAMLINE)
		    # all_connections = m.get_connections(specifier, connection_subtype = constants.CBAR)
		    # specifier = 'gebs'
		    # all_connections = m.get_connections(specifier)
		    # specifier = 'connectors'
		    # all_connections = m.get_connections(specifier)
		    for con in all_connections:
		        print(con.id, con.type, con.subtype, con.model_id, con.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    specifier = "min"
		    coords = m.get_coordinates(specifier)
		    # coords = m.get_coordinates(specifier, resultset=res)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    coord_systems = m.get_coordinate_systems(specifier)
		    # coord_systems = m.get_coordinate_systems(specifier, coordinate_system_id = 1)
		    for cs in coord_systems:
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
		    res = m.get_current_resultset()
		    coord_systems = m.get_coordinate_systems(specifier, resultset=res)
		    for cs in coord_systems:
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    coord_systems = m.get_coordinate_systems(specifier, window=w)
		    for cs in coord_systems:
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
		    specifier = "with_name"
		    coord_systems = m.get_coordinate_systems(specifier)
		    # coord_systems = m.get_coordinate_systems(specifier, name = 'coord_name')
		    for cs in coord_systems:
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
		    specifier = "with_comments"
		    coord_systems = m.get_coordinate_systems(specifier)
		    # coord_systems = m.get_coordinate_systems(specifier, comment = 'coord_comment')
		    for cs in coord_systems:
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
		# method: get_corner_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_corner = m.get_corner_scalar(resultset, specifier)
		    # specifier= 'all'
		    # model_corner = m.get_corner_scalar(resultset, specifier, non_zero = True)
		    # specifier = min
		    # model_corner = m.get_corner_scalar(resultset, specifier, layer = 'top' )
		    for corn in model_corner:
		        print(corn.value)  # Corner scalar value
		        print(
		            corn.element_id, corn.second_id, corn.type
		        )  # Id, second id and type of the element
		        print(
		            corn.corner
		        )  # Id of the node - corner with this corner scalar value for shell and solid elements, or the fraction of the distance from the start to the total distance for line elements
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["value", "element", "corner_id"]
		
		    values, elems, corners = m.get_corner_scalar(
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
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_corner = m.get_corner_vector(resultset, specifier)
		    specifier = "all"
		    # model_corner = m.get_corner_vector(resultset, specifier, non_zero = True)
		    # specifier = 'min'
		    # model_corner = m.get_corner_vector(resultset, specifier, layer = 'top' )
		    for corn in model_corner:
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
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "element", "corner_id"]
		
		    xyz, magn, elems, corners = m.get_corner_vector(
		        resultset, specifier, numpy=np_specifier
		    )
		    print(xyz)
		    print(magn)
		    print(elems)
		    print(corners)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_current_resultset
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		
		    res = m.get_current_resultset()
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
		# method: get_cycles
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    cycles = m.get_cycles(specifier)
		    print(cycles)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformation_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    labels = m.get_deformation_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    deforms = m.get_deformations(resultset, specifier)
		    # deforms = m.get_deformations(resultset, specifier, non_zero = True )
		    for deform in deforms:
		        print(deform.x, deform.y, deform.z, deform.total, deform.node_id)
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, mag, nodes = m.get_deformations(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(mag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_element_faces
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    elem_faces = m.get_element_faces(w)
		    for ef in elem_faces:
		        print(ef.id, ef.model_id, ef.type, ef.total_nodes, ef.node_ids)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    elems = m.get_elements(specifier)
		    # elems = m.get_elements(specifier, element_type = constants.SOLID)
		    # elems = m.get_elements(specifier, element_id = 1007 )
		    # elems = m.get_elements(specifier, element_type = constants.SOLID, element_id = 1007, second_id = -1 )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "identified"
		    elems = m.get_elements(specifier, window=w)
		    # elems = m.get_elements(specifier, window =w, element_type = constants.SOLID)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    elems = m.get_elements(specifier, window=w)
		    # elems = m.get_elements(specifier, window =w, element_type = constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    res = m.get_current_resultset()
		    specifier = "failed"
		    elems = m.get_elements(specifier, resultset=res)
		    # elems = m.get_elements(specifier, resultset = res, element_type = constants.SOLID )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    point = [-1.1, -2.1, 0]
		    specifier = "nearest"
		    elems = m.get_elements(specifier, point_coordinates=point)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "neighbour"
		    elems = m.get_elements(specifier, element_type=constants.SOLID)
		    # elems = m.get_elements(specifier, element_type = constants.SOLID, element_id = 1007 )
		    # elems = m.get_elements(specifier, ignore_failed = True )
		    # elems = m.get_elements(specifier, ignore_failed = True, neighbour_type = constants.SHELL )
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "hidden_overset"
		    elems = m.get_elements(specifier)
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		    specifier = "with_name"
		    elems = m.get_elements(specifier)
		    # elems = m.get_elements(specifier, name = 'elem_name' )
		    # elems = m.get_elements('with_name', comment = 'elem_comment')
		    for e in elems:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_filtered_resultsets
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    filter = "Subcase = 3"
		    resultsets = m.get_filtered_resultsets(filter)
		    # resultsets = m.get_filtered_resultsets(filter, result_type = 'deformation' )
		    # resultsets = m.get_filtered_resultsets(filter', result_type = 'deformation', label = 'label_name' )
		    # resultsets = m.get_filtered_resultsets(filter, cycle = 0)
		    for res in resultsets:
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
		# method: get_groups
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    grs = m.get_groups(specifier)
		    # grs = m.get_groups(specifier, all_instances = True)
		    # grs = m.get_groups(specifier, all_instances = True , name = 'BOUNDARY*')
		    # grs = m.get_groups(specifier, group_type = 'boundary')
		    # grs = m.get_groups(specifier, group_part_type = 'ansapart')
		    for g in grs:
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "identified"
		    grs = m.get_groups(specifier, window=w)
		    # grs = m.get_groups(specifier, window = w, all_instances = True)
		    # grs = m.get_groups(specifier, window = w, group_type = 'part' )
		    for g in grs:
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    grs = m.get_groups(specifier, window=w)
		    # grs = m.get_groups(specifier, window = w, all_instances = True)
		    # grs = m.get_groups(specifier, window = w, group_type = 'part' )
		    for g in grs:
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
		    specifier = "with_comments"
		    grs = m.get_groups(specifier)
		    # grs = m.get_groups(specifier, all_instances = True )
		    # grs = m.get_groups(specifier, comment = 'comment*' )
		    for g in grs:
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
		# method: get_layer_integration_points
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_layer_integration_points()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_layers
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    layer_type = "Layer"
		    # layer_type = 'GlobalLayer'
		    # layer_type = 'NamedLayer'
		    layers = m.get_layers(layer_type)
		    print(layers)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_materials
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    mats = m.get_materials(specifier)
		    # mats = m.get_materials(specifier, material_id = 2)
		    # mats = m.get_materials(specifier, material_type = constants.MAT1)
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		    specifier = "with_comments"
		    mats = m.get_materials(specifier)
		    # mats = m.get_materials(specifier, comment = 'mat_comment' )
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		    specifier = "with_name"
		    mats = m.get_materials(specifier)
		    # mats = m.get_materials(specifier, name = 'mat_name' )
		    for m in mats:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_nodal = m.get_nodal_scalar(resultset, specifier)
		    specifier = "all"
		    # model_nodal = m.get_nodal_scalar(resultset, specifier, non_zero = True)
		    specifier = "min"
		    # model_nodal = m.get_nodal_scalar(resultset, specifier, layer = 'top' )
		    for nodal in model_nodal:  # List with NodalScalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["value", "node"]
		
		    values, nodes = m.get_nodal_scalar(resultset, specifier, numpy=np_specifier)
		    print(values)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    as_list_of_objects()
		    as_numpy_arrays()
		
		
		def as_list_of_objects():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "min"
		    model_nodal = m.get_nodal_vector(resultset, specifier)
		    # specifier = 'all'
		    # model_nodal = m.get_nodal_vector(resultset, specifier, non_zero = True)
		    # specifier = 'max'
		    # model_nodal = m.get_nodal_vector(resultset, specifier, layer = 'top' )
		    for nodal in model_nodal:  # List with NodalVector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		def as_numpy_arrays():
		    m = models.Model(0)
		    resultset = m.get_current_resultset()
		    specifier = "all"
		    np_specifier = ["xyz", "magnitude", "node"]
		
		    xyz, magn, nodes = m.get_nodal_vector(resultset, specifier, numpy=np_specifier)
		    print(xyz)
		    print(magn)
		    print(nodes)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    model_nodes = m.get_nodes(specifier)
		    # model_nodes = m.get_nodes(specifier, node_id = 146)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    model_nodes = m.get_nodes(specifier, window=w)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "identified"
		    model_nodes = m.get_nodes(specifier, window=w)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "free"
		    model_nodes = m.get_nodes(specifier)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "follow"
		    model_nodes = m.get_nodes(specifier)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "with_name"
		    model_nodes = m.get_nodes(specifier)
		    # model_nodes = m.get_nodes(specifier, name = 'node_name' )
		    # model_nodes = m.get_nodes(specifier, field10 = 'field' )
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "with_comments"
		    model_nodes = m.get_nodes(specifier)
		    # model_nodes = m.get_nodes(specifier, comment = 'node_comment')
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "visible_with_name"
		    w = windows.Window(name="MetaPost", page_id=0)
		    model_nodes = m.get_nodes(specifier, window=w)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    specifier = "visible_with_comments"
		    w = windows.Window(name="MetaPost", page_id=0)
		    model_nodes = m.get_nodes(specifier, window=w)
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		    point = [-1.1, -2.1, 0]
		    res = m.get_current_resultset()
		    specifier = "nearest"
		    model_nodes = m.get_nodes(specifier, point_coordinates=point, distance_type="xyz")
		    # model_nodes = m.get_nodes('nearest', point_coordinates = point , distance_type = 'xyz' , resultset = res )
		    for n in model_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    model_parts = m.get_parts(specifier)
		    model_parts = m.get_parts(specifier, part_id=5)
		    # model_parts = m.get_parts(specifier, part_type = constants.PSOLID )
		    for p in model_parts:
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
		    specifier = "identified"
		    model_parts = m.get_parts(specifier, window=w)
		    model_parts = m.get_parts(specifier, window=w, part_type=constants.PSOLID)
		    for p in model_parts:
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
		    model_parts = m.get_parts(specifier, window=w)
		    # model_parts = m.get_parts(specifier, window = w , part_type = constants.PSOLID )
		    for p in model_parts:
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
		    specifier = "with_comments"
		    model_parts = m.get_parts(specifier)
		    # model_parts = m.get_parts(specifier, comment = 'part_comment' )
		    for p in model_parts:
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
		    specifier = "with_name"
		    model_parts = m.get_parts(specifier)
		    # model_parts = m.get_parts(specifier, name = 'part_name' )
		    for p in model_parts:
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
		# method: get_projected_frontal_area
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = m.get_projected_frontal_area(w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_projected_frontal_hole_area
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = m.get_projected_frontal_hole_area(w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_reference_area
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_reference_area()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_reference_density
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_reference_density()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_reference_length
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_reference_length()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_reference_pressure
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_reference_pressure()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_reference_velocity
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.get_reference_velocity()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		
		    resultsets = m.get_resultsets()
		    # resultsets = m.get_resultsets( exclude_generated = True )
		    # resultsets = m.get_resultsets( result_type = 'deformations' , label = 'my_label' )
		    # resultsets = m.get_resultsets( id = 1 )
		    # resultsets = m.get_resultsets( cycle = 0 )
		    for res in resultsets:
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
		# method: get_scalar_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    labels = m.get_scalar_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_sections
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    all_sections = m.get_sections()
		    # all_sections = m.get_sections( name = 'from_vis' )
		    for sec in all_sections:
		        print(sec.name, sec.creation_type, sec.sum_point, sec.coord_system)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shell_normal
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    centroids = m.get_shell_normal(res)
		    for centroid in centroids:
		        print(
		            centroid.value, centroid.x, centroid.y, centroid.z
		        )  # Centroid vector value and direction of the element
		        print(
		            centroid.element_id, centroid.second_id, centroid.type
		        )  # Id, second id and type of the element
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_labels
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    labels = m.get_vector_labels()
		    print(labels)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_windows
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    windows = m.get_windows()
		    for w in windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: has_oversets
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    val = m.has_oversets()
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_boundaries
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    bounds = m.get_boundaries(specifier)
		
		    ret = m.hide_boundaries(bounds)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    coords = m.get_coordinate_systems(specifier)
		    ret = m.hide_coordinate_systems(coords)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    shells = m.get_elements(specifier, element_type=constants.SHELL)
		    ret = m.hide_elements(shells)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_materials
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    mats = m.get_materials(specifier)
		    ret = m.hide_materials(mats)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_parts
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    psolids = m.get_parts(specifier, part_type=constants.PSOLID)
		    ret = m.hide_parts(psolids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_boundaries
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    bounds = m.get_boundaries(specifier, boundary_type=constants.FORCE)
		    ret = m.identify_boundaries(bounds)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    coords = m.get_coordinate_systems(specifier)
		    ret = m.identify_coordinate_systems(coords)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    elems = m.get_elements(specifier, element_type=constants.TRIA3)
		    ret = m.identify_elements(elems)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_groups
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    grs = m.get_groups(specifier, name="*PILLAR*")
		    ret = m.identify_groups(grs)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_materials
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    mats = m.get_materials(specifier)
		    ret = m.identify_materials(mats)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_nodes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "free"
		    free_nodes = m.get_nodes(specifier)
		    ret = m.identify_nodes(free_nodes)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify_parts
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "with_name"
		    pids = m.get_parts(specifier, name="DOOR*")
		    ret = m.identify_parts(pids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Coordinate systems and press Enter when you are ready"
		
		    picked = m.pick_coordinate_systems(message)
		    for cs in picked:
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
		# method: pick_cycles
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Select Cycles and press OK when you are ready"
		    picked = m.pick_cycles(message)
		    print(picked)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_elements
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Elements and press Enter when you are ready"
		    picked = m.pick_elements(message)
		    # settings = {'element_type:[constants.RBE2, constants.RBE3]}
		    # picked = m.pick_elements(message, settings)
		    for e in picked:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_groups
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Groups and press Enter when you are ready"
		    group_type = "part"
		    # group_type = 'include'
		    # group_type = 'set'
		    picked = m.pick_groups(message, group_type)
		    for g in picked:
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
		# method: pick_materials
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Materials systems and press Enter when you are ready"
		    picked = m.pick_materials(message)
		    for m in picked:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_nodes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Nodes and press Enter when you are ready"
		    picked = m.pick_nodes(message)
		    for n in picked:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_parts
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Pick Parts and press Enter when you are ready"
		    picked = m.pick_parts(message)
		    for p in picked:
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
		# method: pick_resultsets
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    message = "Select Resultsets and press OK when you are ready"
		    picked = m.pick_resultsets(message)
		    # picked = m.pick_resultsets(message, result_type = 'scalar' )
		    # picked = m.pick_resultsets(message, result_type = 'scalar' , label = 'my_label' )
		    # picked = m.pick_resultsets(message, cycle = 0 )
		    for res in picked:
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
		# method: reset_identify_boundaries
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_boundaries()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_coordinate_systems()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_elements
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_elements()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_groups
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_groups()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_materials
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_materials()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_nodes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_nodes()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset_identify_parts
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    ret = m.reset_identify_parts()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: select_groups
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    group_type = "part"
		    # group_type = 'set'
		    # group_type = 'boundary'
		    # group_type = 'connection'
		    # group_type = 'include'
		    grs = m.select_groups(group_type)
		    # grs = m.select_groups(group_type, all_instances = True )
		    for g in grs:
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
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = m.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_type = 'numerical'
		    # attribute_value = 11.2
		    # ret = m.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = m.get_attributes(attribute_name="attr")
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = m.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = m.get_attributes()
		    attribute_name = "attr"
		    # attr = m.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    color = windows.Color(name="color_name", r=0, b=255, g=255, a=255)
		    ret = m.set_color(color, w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_coordinate_system_on_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		from meta import coordsystems
		
		
		def main():
		    m = models.Model(0)
		    coordinate_system = coordsystems.CoordSystemById(m.id, 1)
		    specifier = "all"
		    cs = m.set_coordinate_system_on_elements(specifier, coordinate_system)
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    cs = m.set_coordinate_system_on_elements(specifier, coordinate_system, window=w)
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
		# method: set_coordinate_system_on_nodes
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		from meta import coordsystems
		
		
		def main():
		    m = models.Model(0)
		    model_id = m.id
		    coord_sys_id = 1
		    coordinate_system = coordsystems.CoordSystemById(model_id, coord_sys_id)
		
		    specifier = "all"
		
		    cs = m.set_coordinate_system_on_nodes(specifier, coordinate_system)
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
		    w = windows.Window(name="MetaPost", page_id=0)
		    specifier = "visible"
		    cs = m.set_coordinate_system_on_nodes(specifier, coordinate_system, window=w)
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
		# method: set_current_resultset
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    all_res = m.get_resultsets()
		    res = all_res[1]
		    ret = m.set_current_resultset(res)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_label
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    label = "NewName"
		    ret = m.set_label(label)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name_on_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    elems = m.get_elements(specifier, element_type=constants.SOLID)
		    names = list()
		    for e in elems:
		        name = "elem_name_" + str(e.id)
		        names.append(name)
		    ret = m.set_name_on_elements(elems, names)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name_on_nodes
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    all_nodes = m.get_nodes(specifier)
		    names = list()
		    for n in all_nodes:
		        name = "node_name_" + str(n.id)
		        names.append(name)
		    ret = m.set_name_on_nodes(all_nodes, names)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_boundaries
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    bounds = m.get_boundaries(specifier)
		    ret = m.show_boundaries(bounds)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_coordinate_systems
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    coords = m.get_coordinate_systems(specifier)
		    ret = m.show_coordinate_systems(coords)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_elements
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    shells = m.get_elements(specifier, element_type=constants.SOLID)
		    ret = m.show_elements(shells)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_materials
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    mats = m.get_materials(specifier)
		    ret = m.show_materials(mats)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_parts
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    psolids = m.get_parts(specifier, part_type=constants.PSOLID)
		    ret = m.show_parts(psolids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import models
		from meta import constants
		
		
		def main():
		    m = models.Model(0)
		    specifier = "all"
		    all_parts = m.get_parts(specifier)
		    print(all_parts)
		
		
		if __name__ == "__main__":
		    main()
		# method: activate
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    m.activate()
		
		
		if __name__ == "__main__":
		    main()
		# method: deactivate
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    m.deactivate()
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    can_use = m.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Filename of the model.

	"""

	label: str = None
	"""
	Label of the model.

	"""

	deck: str = None
	"""
	Deck name of the model.

	"""

	active: int = None
	"""
	- 1 if model is active
	- 0 if model is not active

	"""

	def get_resultsets(self, exclude_generated: bool, result_type: str, label: str, id: int, cycle: int) -> object:

		"""

		This method gets the resultsets of the model.


		Parameters
		----------
		exclude_generated : bool, optional
			It controls if the method will exclude the generated states or not. If True the generated states will be excluded. If False or absent, the generated states will be included.

		result_type : str, optional
			If set, the method will get only the resultsets from a specific label, specified by the argument label. If this argument is set, the argument label, must also be set. Its possible values are:
			-'deformations' : Only resultsets of a deformation label.
			-'scalar' : Only resultsets of a scalar label.
			-'vector' : Only resultsets of a vector label.
			-'function' : Only resultsets of a function label.

		label : str, optional
			The name of the label. If this argument is set, the argument result_type, must also be set.

		id : int, optional
			Id of the resultset. If set, the method gets the resultsets with resultset id equal to id.

		cycle : int, optional
			Cycle of the resultset. If set, the method gets the resultsets with cycle equal to cycle

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Result. Upon failure, it returns an empty list.

		"""


	def get_current_resultset(self) -> object:

		"""

		This method gets the current resultset of the model.


		Returns
		-------
		object
			Upon succcess, it returns an object of class Result referring to the current resultset of the model. Upon failure, it returns None.

		"""


	def get_filtered_resultsets(self, filter: str, result_type: str, label: str, cycle: int) -> object:

		"""

		This method gets the resultsets of the model, that match a specific filter.


		Parameters
		----------
		filter : str
			Filter expression. It may contain a substring of the name of the state or a conditional expression constructed by using any of the state variables (e.g. Subcase = 4 ). Generally, you can use the same filters as the ones in the text field "Filter" in window "States".

		result_type : str, optional
			If set, the method will get only the resultsets from a specific label, specified by the argument label. Its possible values are:
			-'deformation' : Only resultsets of a deformation label.
			-'scalar' : Only resultsets of a scalar label.
			-'vector' : Only resultsets of a vector label.
			-'function' : Only resultsets of a function label.

		label : str, optional
			The name of the label. If this argument is set, the argument result_type, must also be set.

		cycle : int, optional
			Cycle of the resultset. If set, the method gets the resultsets with cycle equal to cycle

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Result. Upon failure, it returns an empty list.

		"""


	def get_cycles(self, specifier: str) -> object:

		"""

		This method gets the cycles of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all cycles of the model (default value).
			- 'discrete' : all SOL200 discrete optimization cycles of the model.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an integer referring to one cycle of the corresponding model. Upon failure, an empty list is returned.

		"""


	def get_groups(self, specifier: str, all_instances: bool, name: str, comment: str, group_type: str, group_part_type: str, window: object, module_id: str, id: int) -> object:

		"""

		This method gets the groups of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the groups of the model. Optionally combined with arguments: all_instances, name, group_type, group_part_type (default value).
			- 'identified' : identified groups of the model. Optionally combined with arguments: window, all_instances, group_type.
			- 'visible' : visible groups of the model. Optionally combined with arguments: window, all_instances, group_type.
			- 'with_comments' : all groups with comments.  Optionally combined with arguments: all_instances, comment.

		all_instances : bool, optional
			Defines if all instances of groups with the same name will be returned from the method. If it is absent, the default value is False. Used in all specifier values.

		name : str, optional
			Used only when specifier is 'all'. A string search expression where wildcards can be used ("*", "?", "[...]"). If set the method will get only the groups, which have name that matches the expression.

		comment : str, optional
			Used only when specifier is 'with_comments'. A search string expression where wildcards can be used ("*", "?", "[...]"). If set the method will get only the groups, which have comments that matches the expression.

		group_type : str, optional
			Used when the specifier is 'all', 'identified', 'visible'. If set the method will get only the groups that have the specified type. Its possible values are:
			- 'part'
			- 'set'
			- 'boundary'
			- 'connection'
			- 'include'

		group_part_type : str, optional
			Used only when the specifier is 'all'. Its possible values are:
			-'ansapart'
			-'ansagroup'

		window : object, optional
			An object of class Window. Optionally used when specifier is 'visible' or 'identified'. If this argument is set, the method will return only the visible parts in this window.

		module_id : str, optional
			The Module Id of the group. If this argument is given then the method will return only the groups that have the specified Module Id.

		id : int, optional
			The Id of the group. If this argument is given then the method will return only the groups that have the specified Id.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Group. Upon failure, it returns an empty list.

		"""


	def get_parts(self, specifier: str, part_id: int, part_type: int, window: object, name: str, comment: str, range: str) -> object:

		"""

		This method gets the parts of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the parts of the model. Optionally combined with arguments: part_id, part_type (default value).
			- 'identified' : identified parts of the model. Optionally combined with arguments: window, part_id, part_type.
			- 'visible' : visible parts of the model. Optionally combined with arguments: window, part_id, part_type.
			- 'with_comments' : parts with comments. Optionally combined with argument: comment.
			- 'with_name' : parts with name. Optionally combined with argument: name.
			- 'range' : Provide a range of Part Ids in the argument range.

		part_id : int, optional
			Id of the part. Used when the specifier is 'all'. If set, the method gets the parts that have id equal to part_id.

		part_type : int, optional
			Type of the part. Used when the specifier is 'all', 'visible', 'identified'. If set, the method gets the parts of type part_type.

		window : object, optional
			An object of class Window. Used when specifier is 'visible' or 'identified'. If this argument is set, the method will return only the visible parts in this window.

		name : str, optional
			Name of the part. Used only if specifier is 'with_name'. If set, then the method will get the parts that matches the expression. Otherwise the method will get all the parts that have name.

		comment : str, optional
			Comment of the part. Used only if specifier is 'with_comments'. If set, then the method will get the parts that matches the expression. Otherwise the method will get all the parts that have comment.

		range : str, optional
			Part Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Part. Upon failure, it returns an empty list.

		"""


	def get_elements(self, specifier: str, element_type: int, element_id: int, second_id: int, window: object, resultset: object, solver_element_path: str, name: str, comment: str, point_coordinates: object, ignore_failed: bool, neighbour_type: int, range: str) -> object:

		"""

		This method gets the elements of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the elements of the model. Optionally combined with arguments: element_type, element_id, second_id, solver_element_path (default value).
			- 'identified' : identified elements of the model. Optionally combined with argument: window.
			- 'visible' : visible elements of the model. Optionally combined with argument: window.
			- 'failed' : failed elements of the model. Must be combined with argument: resultset.
			- 'nearest' : nearest element of the model from a specific point. Must be combined with argument: point_coordinates.
			- 'neighbour' : neighbour elements of the model. Optionally combined with arguments: element_type, element_id, ignore_failed, neighbour_type.
			- 'hidden_overset' : dead elements of the model's background and component volume meshes for the current state.
			- 'with_name' : elements with name. Optionally combined with argument: name.
			- 'with_comments' : elements with comments. Optionally combined with argument: comment.
			- 'range' : Provide a range of Element Ids in the argument range.
			- 'iterator' : The method will return a Python Iterator for iterating all Elements of Model.

		element_type : int, optional
			Type of the element. If set, the method will return only the elements of this type. This argument is used when the specifier is 'all', 'identified', 'visible', 'failed' or'neighbour'.

		element_id : int, optional
			Id of the element. If set, the method will return only the elements that have id equal to element_id. This argument is used when the specifier is 'all' or 'neighbour'

		second_id : int, optional
			Second id of the element. If set, the method will return only the elements that have the specified second id. This argument is used only when the specifier is 'all' or 'neighbour' and the arguments element_id and element_type have been set.

		window : object, optional
			An object of the class Window. This argument is used when the specifier is 'visible' or 'identified'. If this argument is set, the method will return only the visible elements in this window.

		resultset : object, optional
			An object of the class Result. This argument is required when the specifier is 'failed'.

		solver_element_path : str, optional
			Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given element is limited. This argument can be used only if the specifier is 'all'

		name : str, optional
			Name of the element. If set, the method will return only the elements, which have name that matches the expression. This argument is used only when the specifier is 'with_names'. If absent, the method with specifier 'with_names', will get all the elements that have name.

		comment : str, optional
			Comment of the element. If set, the method will return only the elements, which have comment that matches the expression. This argument is used only when the specifier is 'with_comments'. If absent, the method with specifier 'with_comments', will get all the elements that have comment.

		point_coordinates : object, optional
			A list with coordinates of the point. This argument is required when the specifier is 'nearest'

		ignore_failed : bool, optional
			This argument is used only when the specifier is 'neighbour'. Controls if the failed elements will be ignored, or not. Default value is False (Do not ignore).

		neighbour_type : int, optional
			This argument is used only when the specifier is 'neighbour'. Type of the neighbour elements.

		range : str, optional
			Element Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Group. Upon failure, it returns an empty list.

		"""


	def get_element_faces(self, window: object) -> object:

		"""

		This method gets the element faces of the model.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class ElementFace. Upon failure, it returns an empty list.

		"""


	def get_nodes(self, specifier: str, node_id: int, window: object, name: str, field10: str, comment: str, solver_node_path: str, resultset: object, distance_type: str, point_coordinates: object, range: str) -> object:

		"""

		This method gets the nodes of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodes of model. Optionally combined with arguments: node_id, solver_node_path (default value).
			- 'visible' : visible nodes of model. Optionally combined with argument: window.
			- 'identified' : identified nodes of the model. Optionally combined with argument: window.
			- 'free' : free nodes of the model.
			- 'follow' : follow nodes of the model.
			- 'with_name' : nodes with name. Optionally combined with arguments: name, field10.
			- 'with_comments' : nodes with comments. Optionally combined with argument: comment.
			- 'visible_with_name' : visible nodes with name. Optionally combined with argument: window.
			- 'visible_with_comments' : visible nodes with comments. Optionally combined with argument: window.
			- 'nearest' : nearest node from a specific point. Must be combined with arguments: point_coordinates, distance_type. Optionally combined with argument: resultset.
			- 'range' :  Provide a range of Node Ids in the argument range.
			- 'iterator' : The method will return a Python Iterator for iterating all Nodes of Model.

		node_id : int, optional
			Node id. It is used only when the specifier is 'all'. If specified, the method gets only the node with the specified id.

		window : object, optional
			An object of class Window. This argument is used when the specifier is 'visible' or 'identified', 'visible_with_comments', 'visible_with_name'. If this argument is set, the method will return only the visible nodes in this window.

		name : str, optional
			Name of the node. It is used only when the specifier is 'with_name'. If set, the method will get only the nodes with name, that matches to the given expression. Otherwise, it will return all the nodes that have name.

		field10 : str, optional
			Field10 of the node. It is used only when the specifier is 'with_name'. If set, the method will get only the nodes that have field10, that matches to the given expression. Otherwise, it will return all the nodes that have field10.

		comment : str, optional
			Comment of the node. It is used only when the specifier is 'with_comments'. If set, the method will get only the nodes with comment, that matches to the given expression. Otherwise, it will return all the nodes that have comment.

		solver_node_path : str, optional
			Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given node is limited. This argument is used only when the specifier is 'all'.

		resultset : object, optional
			An object of class Result. It is used only when the specifier is 'nearest'. If it is absent, then the result will be calculated for the ORIGINAL STATE.

		distance_type : str, optional
			Type of the distance. This argument is required when the specifier is 'nearest'. In other cases, it is ignored. Possible values are:
			- 'xyz': XYZ distance
			- 'xy': XY distance
			- 'yz': YZ distance
			- 'zx': ZX distance
			- 'x': X distance
			- 'y': Y distance
			- 'z': Z distance

		point_coordinates : object, optional
			A list with the XYZ-coordinates of the point. This argument is required when the specifier is 'nearest'. In other cases, it is ignored.

		range : str, optional
			Node Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Node. Upon failure, it returns an empty list.

		"""


	def get_coordinate_systems(self, specifier: str, coordinate_system_id: int, resultset: object, coordinate_system_solver_path: str, window: object, name: str, comment: str) -> object:

		"""

		This method gets the coordinates systems of the model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all the coordinate systems of the model (default value). Optionally combined with arguments: coordinate_system_id, resultset, coordinate_system_solver_path.
			- 'visible' : visible coordinate systems of the model. Must be combined with argument: window. 
			- 'with_name' : coordinate systems with name. Optionally combined with argument: name.
			- 'with_comments' : coordinate systems with comments. Optionally combined with argument: comment

		coordinate_system_id : int, optional
			Id of the coordinate system. Used only when the specifier is 'all'. If set, the method will return the coordinate system with the specified id.

		resultset : object, optional
			An object of class Result. It is used for moving coordinates. If it is absent, the moving coordinate system will be calculated for the ORIGINAL STATE. It is used only if the specifier is 'all'.

		coordinate_system_solver_path : str, optional
			Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given coordinate system is limited. It is used only if the specifier is 'all'.

		window : object, optional
			An object of class Window. This argument is required when the specifier is 'visible'.

		name : str, optional
			Name of the coordinate system. It is used only when the specifier is 'with_name'. If set, the method will get only the coordinate systems with name, that matches to the given expression. Otherwise, it will return all the coordinate systems that have name.

		comment : str, optional
			Comment of the coordinate system. It is used only when the specifier is 'with_comments'. If set, the method will get only the coordinate systems  with comment, that matches to the given expression. Otherwise, it will return all the coordinate systems that have comment.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class CoordSystem. Upon failure, it returns an empty list.

		"""


	def get_boundaries(self, specifier: str, boundary_type: int, boundary_id: int, second_id: int, window: object, name: str, comment: str, range: str) -> object:

		"""

		This method gets the boundary elements of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the boundary elements of the model (default value). Optionally combined with arguments: boundary_type, boundary_id, second_id.
			- 'identified' : identified boundary elements of the model. Optionally combined with arguments: window, boundary_type.
			- 'visible' : visible boundary elements of the model. Optionally combined with arguments: window, boundary_type.
			- 'with_name' : boundary elements with name. Optionally combined with argument: name.
			- 'with_comments' : boundary elements with comments. Optionally combined with argument: comment.
			- 'range' : Provide a range of Boundary element Ids in the argument range.

		boundary_type : int, optional
			The type of the boundary element. If the argument is set, the method will get only boundary elements of the specified type. It is used when specifier is 'all', 'visible' or 'identified'.

		boundary_id : int, optional
			The id of the boundary element.  If the argument is set, the method will get only boundary elements with the specified id. It is used when specifier is 'all'.

		second_id : int, optional
			The second id of the boundary element.  If the argument is set, the method will get only boundary elements with the specified second id. It is used when specifier is 'all', and the arguments boundary_type and boundary_id are set.

		window : object, optional
			An object of class Window. It is used when the specifier is 'visible' or 'identified'. If this argument is set, the method will return only the visible boundaries in this window.

		name : str, optional
			Name of the boundary element. It is used only when the specifier is 'with_name'. If set, the method will get only the boundary element with name, that matches to the given expression. Otherwise, it will return all the boundary elements that have name.

		comment : str, optional
			Comment of the boundary element. It is used only when the specifier is 'with_comments'. If set, the method will get only the boundary elements with comment, that matches to the given expression. Otherwise, it will return all the boundary elements that have comment.

		range : str, optional
			Part Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Boundary. Upon failure, it returns an empty list.

		"""


	def get_materials(self, specifier: str, material_id: int, material_type: int, material_solver_path: str, name: str, comment: str, range: str) -> object:

		"""

		This method gets the materials of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the materials of the model (default value). Optionally combined with arguments: material_id, material_type, material_solver_path.
			- 'with_comments' : materials with comments. Optionally combined with argument: comment.
			- 'with_name' : materials with name. Optionally combined with argument: name.
			- 'range' : Provide a range of Material Ids in the argument range.

		material_id : int, optional
			The id of the material.  If the argument is set, the method will get only materials with the specified id. It is used when specifier is 'all'.

		material_type : int, optional
			The type of the material. If the argument is set, the method will get only materials of the specified type. It is used when specifier is 'all'.

		material_solver_path : str, optional
			Path to parent substructure. It is formatted as '[Id/Name]->...->[Id/Name]' and contains one or more substructure ids or names separated by '->'. It defines a series of nested substructures ordered from the outer to the innermost in which the search of the given material is limited. It is used when specifier is 'all'.

		name : str, optional
			Name of the material. It is used only when the specifier is 'with_name'. If set, the method will get only the materials with name, that matches to the given expression. Otherwise, it will return all the materials that have name.

		comment : str, optional
			Comment of the material. It is used only when the specifier is 'with_comments'. If set, the method will get only the materials with comment, that matches to the given expression. Otherwise, it will return all the materials that have comment.

		range : str, optional
			Material Ids. The specifier must be set to 'range'.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Material. Upon failure, it returns an empty list.

		"""


	def get_connections(self, specifier: str, connection_id: int, connection_type: int, connection_subtype: int, window: object) -> object:

		"""

		This method gets the connections of the model.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all the connections of the model (default value). Optionally combined with arguments: connection_id, connection_type, connection_subtype.
			- 'visible' : visible connections of the model. Optionally combined with arguments: window, connection_id, connection_type, connection_subtype.
			- 'gebs' : all the gebs of the model.
			- 'connectors' : all the connectors of the model.

		connection_id : int, optional
			The id of the connection. If set, the method will get only the connections with the specified id. Used only when the specifier is 'all'.

		connection_type : int, optional
			The type of the connection. If set, the method will get only the connections with the specified type. Used only when the specifier is 'all'.

		connection_subtype : int, optional
			The subtype of the connection. If set, the method will get only the connections with the specified subtype. Used only when the specifier is 'all'.

		window : object, optional
			An object of class Window. Used when the specifier is 'visible'. If this argument is set, the method will return only the visible connections in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Connection. Upon failure, it returns an empty list.

		"""


	def get_windows(self) -> object:

		"""

		This method gets the windows that are loaded in the model. This method works for the active page.


		Returns
		-------
		object
			Upon success, it returns a list with objects of class Window. Upon failure, it returns an empty list.

		"""


	def get_sections(self, name: str) -> object:

		"""

		This method gets the sections of the model.


		Parameters
		----------
		name : str, optional
			If set, the method gets only the section with the specified name. Otherwise, it returns all sections.

		Returns
		-------
		object
			Upon success, it returns a list with objects of class Section. Upon failure, it returns an empty list.

		"""


	def get_area(self) -> float:

		"""

		This method gets the area of the model.


		Returns
		-------
		float
			Upon success, it returns a float value being the area of the model calculated as the sum of the areas of all parts of the specified type (shell and/or solid).Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the model.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes.Upon failure, it returns an empty dictionary.

		"""


	def get_color(self, window: object) -> object:

		"""

		This method gets the color of the model.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		object
			Upon success, it returns an object of class Color, refering to the color of the model. Upon failure, it returns None.

		"""


	def get_projected_frontal_area(self, window: object) -> float:

		"""

		This method gets the projected frontal area of a model's visible entities according to current view. This method works for the active page.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		float
			Upon success, it returns as a float the projected frontal area of the corresponding model for the specified window.Upon failure, it returns None.

		"""


	def get_projected_frontal_hole_area(self, window: object) -> float:

		"""

		This method gets the projected frontal hole area of a model.  This method works for the active page.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		float
			Upon success, it returns as a float the projected frontal hole area of the corresponding model for the specified window.Upon failure, it returns None.

		"""


	def get_bounding_rectangle(self, window: object) -> object:

		"""

		This method gets the bounding rectangle of a model.  This method works for the active page.


		Parameters
		----------
		window : object
			An object of class Window.

		Returns
		-------
		object
			Upon success, it returns a list where it contains in position 0 and 1 the screen X,Y coordinates [0,1] of the bottom left corner of the rectangle and in position 2 and 3 the screen X,Y coordinates of the top right corner of the rectangle. Upon failure, it returns an empty list.

		"""


	def get_reference_velocity(self) -> float:

		"""

		This method gets the reference velocity of a model.


		Returns
		-------
		float
			Upon success, it returns as a float the reference velocity of the specified model. Upon failure it returns None.

		"""


	def get_reference_density(self) -> float:

		"""

		This method gets the reference density of a model.


		Returns
		-------
		float
			Upon success, it returns as a float the reference density of the corresponding model with the given id.Upon failure, it returns None.

		"""


	def get_reference_area(self) -> float:

		"""

		This method gets the reference area of a model.


		Returns
		-------
		float
			Upon success, it returns as a float the reference area of the corresponding model with the given id. Upon failure, it returns None.

		"""


	def get_reference_length(self) -> float:

		"""

		This method gets the reference length of a model.


		Returns
		-------
		float
			Upon success, it returns as a float the reference length of the corresponding model with the given id.Upon failure, it returns None.

		"""


	def get_reference_pressure(self) -> float:

		"""

		This method gets the reference pressure of a model.


		Returns
		-------
		float
			Upon success, it returns as a float the reference pressure of the corresponding model with the given id.Upon failure, it returns None.

		"""


	def get_deformation_labels(self) -> object:

		"""

		This method gets all deformation labels for given model.


		Returns
		-------
		object
			Upon success, it returns a list with strings, where each member refers to one deformation label of the corresponding model.Upon failure, an empty list is returned.

		"""


	def get_scalar_labels(self) -> object:

		"""

		This method gets all scalar labels for a given model.


		Returns
		-------
		object
			Upon success, it returns a list with all scalar labels where each member of the list is a string referring to one scalar label of the corresponding model.Upon failure, an empty list is returned.

		"""


	def get_vector_labels(self) -> object:

		"""

		This method gets all vector labels for a given model.


		Returns
		-------
		object
			Upon success, it returns a list with all vector labels where each member of the list is a string referring to one vector label of the corresponding model.Upon failure, an empty list is returned.

		"""


	def get_layer_integration_points(self) -> object:

		"""

		This method gets the layer integration points of a model.


		Returns
		-------
		object
			It returns a list with the layer integration points of the specified model. Each member of the list is a string referring to one layer integration point of the given model.Upon failure, an empty list is returned.

		"""


	def has_oversets(self) -> bool:

		"""

		This method checks if the model contains oversets. 


		Returns
		-------
		bool
			It returns True if the model has oversets. Otherwise, it returns False.

		"""


	def get_coordinates(self, specifier: str) -> object:

		"""

		This method gets maximum or minimum coordinates in each direction (X, Y, Z) of a given model. Coordinates refer to the position of the nodes for a given resultset.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'min' : minimum coordinates.
			- 'max' : maximum coordinates.

		Returns
		-------
		object
			Upon success, it returns a list with 3 Node objects where each member of the list is an object of class Node referring to the node with the maximun coordinate in each direction of the specified model.- 0 = Node with the maximum X coordinate- 1 = Node with the maximum Y coordinate- 2 = Node with the maximum Z coordinateUpon failure, an empty list is returned.

		"""


	def get_deformations(self, resultset: object, specifier: str, non_zero: bool, numpy: object) -> object:

		"""

		This method gets the deformations of the model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations (default value)
			- 'max' : max deformation
			- 'min' : min deformation

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

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
			It returns a list where each element of the list is an object of class type Deformation referring to the deformation of a node for the given model.Upon failure, an empty list is returned.

		"""


	def get_shell_normal(self, resultset: object) -> object:

		"""

		This method gets the shell normal vectors of the SHELL elements of the model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model. If it does not contain deformation information, then shell normal vectors will be calculated for the ORIGINAL STATE.

		Returns
		-------
		object
			Upon success, it returns a list with the CentroidVector objects where each member of the list refers to the shell normal vector of a SHELL element of the specified model.Upon failure, an empty list is returned.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: str, non_zero: bool, layer: str, numpy: object) -> object:

		"""

		This method gets the nodal scalar values of the model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar (default value)
			- 'max' : max nodal scalar
			- 'min' : min nodal scalar

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

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
			It returns a list with the NodalScalar objects where each member of the list refers to one nodal scalar value of a node of the specified model. Upon failure, an empty list is returned.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, non_zero: bool, layer: str, numpy: object) -> object:

		"""

		This function calculates the nodal vector values of the model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal vector (default value)
			- 'max' : max nodal vector
			- 'min' : min nodal vector

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

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
			It returns a list where each member of the list is an object of class NodalVector referring to one nodal vector value of a node of the specified model.Upon failure, an empty list is returned.

		"""


	def get_centroid_scalar(self, resultset: object, specifier: str, non_zero: bool, layer: str, exclude_novalue: bool, numpy: object) -> object:

		"""

		This method gets all centroid scalar values for a model specified by its id.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid scalar (default value)
			- 'max' : max centroid scalar
			- 'min' : min centroid scalar

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

		layer : str, optional
			Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
			- 'bottom' (default)
			- 'top'

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
			It returns a list with CentroidScalar objects where each member of the list refers to the centroid scalar value of an element of the specified model.Upon failure, an empty list is returned.

		"""


	def get_centroid_vector(self, resultset: object, specifier: str, non_zero: bool, layer: str, numpy: object) -> object:

		"""

		This method gets all centroid scalar values of the elements of a model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all centroid vector (default value)
			- 'max' : max centroid vector
			- 'min' : min centroid vector

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

		layer : str, optional
			Location of the centroid scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
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
			It returns a list with CornerScalar objects where each member of the list refers to the corner scalar values of an element of the specified model.Upon failure, an empty list is returned.

		"""


	def get_corner_scalar(self, resultset: object, specifier: str, non_zero: bool, layer: str, numpy: object) -> object:

		"""

		This method gets all corner scalar values of the elements of a model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner scalar (default value)
			- 'max' : max corner scalar
			- 'min' : min corner scalar

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

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
			It returns a list with CornerScalar objects where each member of the list refers to the corner scalar values of an element of the specified model.Upon failure, an empty list is returned.

		"""


	def get_corner_vector(self, resultset: object, specifier: str, non_zero: bool, layer: str, numpy: object) -> object:

		"""

		This method gets all corner vector values of the elements of a model.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all corner vector (default value)
			- 'max' : max corner vector
			- 'min' : min corner vector

		non_zero : bool, optional
			If True, the method will return only the non zero deformations. The default value is False.

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
			It returns a list with CornerVector objects where each member of the list refers to the corner vector values of an element of the specified model.Upon failure, an empty list is returned.

		"""


	def get_layers(self, layer_type: str) -> object:

		"""

		This method gets the layers of the model.


		Parameters
		----------
		layer_type : str
			Type of the layer. Possible values are:
			- 'Layer'
			- 'GlobalLayer'
			- 'NamedLayer'

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is a string referring to the number or the id of a layer of the given model.Upon failure, an empty list is returned.

		"""


	def set_current_resultset(self, resultset: object) -> bool:

		"""

		This method sets the current resultset of the model. This method works for the active page.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_label(self, label: str) -> bool:

		"""

		This method sets the label of the model.


		Parameters
		----------
		label : str
			The label of the model.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_color(self, color: object, window: object) -> bool:

		"""

		This method sets color of a model.


		Parameters
		----------
		color : object
			An object of class Color.

		window : object
			An object of class Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete(self) -> object:

		"""

		This method deletes the model.


		Returns
		-------
		object
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the model.


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


	def select_groups(self, group_type: str, all_instances: bool) -> object:

		"""

		This method allows the user to select group(s) of the model from a given list. The execution of the script will stop and it will restart after the selection of the groups from the list.


		Parameters
		----------
		group_type : str
			Type of groups to be listed. Its possible values are:
			- 'part'
			- 'set'
			- 'boundary'
			- 'connection'
			- 'include'

		all_instances : bool, optional
			Controls if all instances of groups with the same name will be returned from the method. If it is absent, then the default value is False.

		Returns
		-------
		object
			Upon success, it returns a list where each item of the list is an object of class Group referring to one specific selected group of the model.Upon failure, an empty list is returned.

		"""


	def identify_groups(self, groups: object) -> bool:

		"""

		This method allows the user to identify groups of a model. This method works for the active page.


		Parameters
		----------
		groups : object
			A list of objects of class Group.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_parts(self, parts: object) -> bool:

		"""

		This method allows the user to identify parts of a model. This method works for the active page.


		Parameters
		----------
		parts : object
			A list of objects of class Part.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_elements(self, elements: object) -> bool:

		"""

		This method allows the user to identify elements of a model. This method works for the active page.


		Parameters
		----------
		elements : object
			A list of objects of class Element.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_nodes(self, nodes: object) -> bool:

		"""

		This method allows the user to identify nodes of a model. This method works for the active page.


		Parameters
		----------
		nodes : object
			A list of objects of class Node.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_coordinate_systems(self, coordinate_systems: object) -> bool:

		"""

		This method allows the user to identify coordinate systems of a model. This method works for the active page.


		Parameters
		----------
		coordinate_systems : object
			A list of objects of class CoordSystem.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_boundaries(self, boundaries: object) -> bool:

		"""

		This method allows the user to identify boundary elements of a model.


		Parameters
		----------
		boundaries : object
			A list of objects of class Boundary.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify_materials(self, materials: object) -> bool:

		"""

		This method allows the user to identify materials of a model. This method works for the active page.


		Parameters
		----------
		materials : object
			A list of objects of class Material.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_groups(self, groups: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific groups of the model. This method works for the active page.


		Parameters
		----------
		groups : object, optional
			A list of objects of class Group. If Absent, the method will reset the identification of all groups.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_parts(self, parts: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific parts of the model. This method works for the active page.


		Parameters
		----------
		parts : object, optional
			A list of objects of class Part. If Absent, the method will reset the identification of all parts.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_elements(self, elements: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific elements of the model. This method works for the active page.


		Parameters
		----------
		elements : object, optional
			A list of objects of class Element. If Absent, the method will reset the identification of all elements.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_nodes(self, nodes: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific nodes of the model. This method works for the active page.


		Parameters
		----------
		nodes : object, optional
			A list of objects of class Node. If Absent, the method will reset the identification of all nodes.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_coordinate_systems(self, coordinate_systems: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific coordinate systems of the model. This method works for the active page.


		Parameters
		----------
		coordinate_systems : object, optional
			A list of objects of class CoordSystem. If Absent, the method will reset the identification of all coordinate systems.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_boundaries(self, boundaries: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific boundary elements of the model. This method works for the active page.


		Parameters
		----------
		boundaries : object, optional
			A list of objects of class Boundary. If Absent, the method will reset the identification of all boundaries.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def reset_identify_materials(self, materials: object) -> bool:

		"""

		This methods allows the user to reset the identification of all or specific materials of the model. This method works for the active page.


		Parameters
		----------
		materials : object, optional
			A list of objects of class Material. If Absent, the method will reset the identification of all materials.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def pick_resultsets(self, message: str, result_type: str, label: str, cycle: int) -> object:

		"""

		This method allows the user to select resultsets of the model from a given list. The execution of the script will stop and it will restart after the selection of the resultsets from the list.


		Parameters
		----------
		message : str
			Message displayed to the user.

		result_type : str, optional
			If set, the method will get only the resultsets from a specific label, specified by the argument label. Its possible values are:
			-'deformation' : Only resultsets of a deformation label.
			-'scalar' : Only resultsets of a scalar label.
			-'vector' : Only resultsets of a vector label.
			-'function' : Only resultsets of a function label.

		label : str, optional
			The name of the label. If this argument is set, the argument result_type, must also be set.

		cycle : int, optional
			Cycle of the resultset. If set, the method gets the resultsets with cycle equal to cycle

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Result referring to one specific selected resultset of the model. Upon failure, an empty list is returned.

		"""


	def pick_cycles(self, message: object) -> object:

		"""

		This method allows the user to select cycles of the model from a given list. The execution of the script will stop and it will restart after the selection of the resultsets from the list.


		Parameters
		----------
		message : object
			Message displayed to the user.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of integers referring to one specific selected cycle of the model. Upon failure, an empty list is returned.

		"""


	def pick_groups(self, message: str, group_type: str, settings: object) -> object:

		"""

		This method allows the user to pick groups of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user.

		group_type : str
			Type of the group. Its possible values are:
			- 'part'
			- 'include'
			- 'set'

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			
			The setting is False by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Group referring to one group of the model. Upon failure, an empty list is returned.

		"""


	def pick_parts(self, message: object, settings: object) -> object:

		"""

		This method allows the user to pick parts of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : object
			Message displayed to the user.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			
			The setting is False by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Part referring to one part of the model. Upon failure, an empty list is returned.

		"""


	def pick_elements(self, message: str, settings: dict) -> object:

		"""

		This method allows the user to pick elements of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user.

		settings : dict, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pairs are:
			- 'front_selection', boolean : controls if frontal selection will turned on, or off.
			- 'polygonal_selection', boolean : controls if polygonal selection will turned on, or off.
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			- 'element_type', constant or list of constants: if set, the user will be able to pick elements only of type 'element_type'
			
			All settings are disabled by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Element referring to one element of the model. Upon failure, an empty list is returned.

		"""


	def pick_nodes(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick nodes of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pairs are:
			- 'front_selection', boolean : controls if frontal selection will turned on, or off.
			- 'polygonal_selection', boolean : controls if polygonal selection will turned on, or off.
			- 'reset_picked', boolean : controls if node identification of the picked nodes will be reset after pick.
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			- 'pick_ordered', boolean : controls if the nodes will be returned with the order the have been picked.
			
			All settings are False by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Node referring to one node of the model. Upon failure, an empty list is returned.

		"""


	def pick_coordinate_systems(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick coordinate systems of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			
			The setting is False by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class CoordSystem referring to one coordinate system of the model. Upon failure, an empty list is returned.

		"""


	def pick_materials(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick materials of the model. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			
			The setting is False by default.

		Returns
		-------
		object
			Upon succeess, it returns a list where each member of the list is an object of class Material referring to one material of the model. Upon failure, an empty list is returned.

		"""


	def show_parts(self, parts: object, show_only: bool) -> bool:

		"""

		This method shows some parts of the model. This method works for the active page.


		Parameters
		----------
		parts : object
			A list of objects of class Part.

		show_only : bool, optional
			If True, the method will hide everything, and show only the specified parts. Default value is False.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show_elements(self, elements: object, show_only: bool) -> bool:

		"""

		This method shows some elements of the model. This method works for the active page.


		Parameters
		----------
		elements : object
			A list of objects of class Element.

		show_only : bool, optional
			If True, the method will hide everything, and show only the specified elements. Default value is False.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show_coordinate_systems(self, coordinate_systems: object, show_only: bool) -> bool:

		"""

		This method shows some coordinate systems of the model. This method works for the active page.


		Parameters
		----------
		coordinate_systems : object
			A list of objects of class CoordSystem.

		show_only : bool, optional
			If True, the method will hide everything, and show only the specified CoordSystems. Default value is False.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show_boundaries(self, boundaries: object, show_only: bool) -> bool:

		"""

		This method shows some boundary elements of the model. This method works for the active page.


		Parameters
		----------
		boundaries : object
			A list of objects of class Boundary.

		show_only : bool, optional
			If True, the method will hide everything, and show only the specified boundary elements. Default value is False.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show_materials(self, materials: object, show_only: bool) -> bool:

		"""

		This method shows some materials of the model. This method works for the active page.


		Parameters
		----------
		materials : object
			A list of objects of class Material.

		show_only : bool, optional
			If True, the method will hide everything, and show only the specified materials. Default value is False.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_parts(self, parts: object) -> bool:

		"""

		This method hides some parts of the model. This method works for the active page.


		Parameters
		----------
		parts : object
			A list of objects of class Part.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_elements(self, elements: object) -> bool:

		"""

		This method hides some elements of the model. This method works for the active page.


		Parameters
		----------
		elements : object
			A list of objects of class Elements.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_coordinate_systems(self, coordinate_systems: object) -> bool:

		"""

		This method hides some coordinate systems of the model. This method works for the active page.


		Parameters
		----------
		coordinate_systems : object
			A list of objects of class CoordSystem.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_boundaries(self, boundaries: object) -> bool:

		"""

		This method hides some boundary elements of the model. This method works for the active page.


		Parameters
		----------
		boundaries : object
			A list of objects of class Boundary.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_materials(self, materials: object) -> bool:

		"""

		This method hides some materials of the model. This method works for the active page.


		Parameters
		----------
		materials : object
			A list of objects of class Material.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_name_on_elements(self, elements: object, names: object) -> bool:

		"""

		This method sets names for some specific elements of the model.


		Parameters
		----------
		elements : object
			A list of objects of class Elements.

		names : object
			A list of names of elements as strings.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_name_on_nodes(self, nodes: object, names: object) -> bool:

		"""

		This method sets names for some specific nodes of the model.


		Parameters
		----------
		nodes : object
			A list of objects of class Nodes.

		names : object
			A list of names of elements as strings.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_coordinate_system_on_elements(self, specifier: str, coordinate_system: object, window: object) -> bool:

		"""

		This method sets an existing coordinate system to the elements of the model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : apply CoordSystem to all elements.
			- 'visible' : apply CoordSystem to visible elements. Must be combined with argument window.

		coordinate_system : object
			An object of class CoordSystem.

		window : object, optional
			An object of class Window. Required when specifier is 'visible'.

		Returns
		-------
		bool
			Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied to elements of the model.Upon failure, None is returned.

		"""


	def set_coordinate_system_on_nodes(self, specifier: str, coordinate_system: object, window: object) -> bool:

		"""

		This method sets an existing coordinate system to the nodes of the model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : apply CoordSystem to all elements.
			- 'visible' : apply CoordSystem to visible elements. Must be combined with argument window.

		coordinate_system : object
			An object of class CoordSystem.

		window : object, optional
			An object of class Window. Required when specifier is 'visible'.

		Returns
		-------
		bool
			Upon success, it returns an object of class CoordSystem referring to the corresponding coordinate system applied to nodes of the model.Upon failure, None is returned.

		"""


	def activate(self) -> object:

		"""

		This method makes the model active.


		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def deactivate(self) -> object:

		"""

		This method deactivates the model.


		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Model entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_mass(self, resultset: object) -> float:

		"""

		This method gets the mass of the model, which is calculated as the sum of mass of elements. This function might deviate from the actual model mass information since it relieson information read by META.


		Parameters
		----------
		resultset : object, optional
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the mass of the Model. Upon failure, it returns None.

		"""


	def get_mass_no_nsm(self, resultset: object) -> float:

		"""

		This method gets the mass of the model, which is calculated as the sum of mass of elements excluding non-structural mass. This function might deviate from the actual model mass information since it relieson information read by META.


		Parameters
		----------
		resultset : object, optional
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		float
			Upon success, it returns the mass of the Model. Upon failure, it returns None.

		"""

