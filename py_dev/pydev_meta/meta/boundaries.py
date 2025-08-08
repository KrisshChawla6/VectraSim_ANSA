from __future__ import annotations
from typing import *

def AddNameOnBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int, boundary_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.set_name` instead.


	This function defines a name for a boundary element of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	boundary_name : str
		Name of the boundary element.

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
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    old_boundary_name = boundaries.NameOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    print("Old boundary name:", old_boundary_name)
		
		    boundary_name = "SPC_on_crankshaft"
		    boundaries.AddNameOnBoundary(
		        model_id, boundary_type, boundary_id, second_id, boundary_name
		    )
		
		    new_boundary_name = boundaries.NameOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    print("New boundary name:", new_boundary_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.set_name instead.", DeprecationWarning)

def AdvFiltersOnBoundaries(model_id: int, adv_filters: object, resultset: object, sort: bool) -> object:

	"""

	This function allows the user to collect boundary elements of a model through some advanced filters.  Results of advanced filters refer to a resultset specified by its object. 

	Parameters
	----------
	model_id : int
		Id of the model

	adv_filters : object
		A list with the advanced filters as string expressions. Their syntax is the same with the commands referring to advanced filters.

	resultset : object, optional
		Object of class Result or string referring to the states selection of advanced filter. 
		Its possible values are:
		- object of class Result
		- 'current': Current state
		- 'all': All states 
		- 'locked': Locked states
		- range of states' ids (e.g. 1-10,13)
		If this argument is absent then results of advanced filters will refer to the ORIGINAL STATE.

	sort : bool
		Boolean that controls if the returned list will be sorted. Default value is false.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		from meta import results
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Elements:visible::Keep All")
		    adv_filters.append("intersect:Elements:id:>1:Keep All")
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		    collected_boundaries = boundaries.AdvFiltersOnBoundaries(
		        model_id, adv_filters, resultset
		    )
		    for b in collected_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Boundaries(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all boundary elements of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member is an object of class Boundary referring to one specific boundary element of the given model.
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
		    all_boundaries = boundaries.Boundaries(model_id)
		    iter_end = min(10, len(all_boundaries))
		    for b in all_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesByComments(model_id: int, boundary_comments: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds the boundary elements of a model with specific comments (boundary_comments). Argument 'boundary_comments" is a string expression where wildcards can be used ("*", "?", "[...]").

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_comments : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		    boundary_comments = "*SPC*"
		    matbounds = boundaries.BoundariesByComments(model_id, boundary_comments)
		    for b in matbounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesById(model_id: int, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds boundary elements of a model with a given id, second id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int, optional
		Second id of the boundary element. If it is absent, then the function will collect all boundary elements with boundary_id for all second_ids.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		    boundary_type = constants.SPC1
		    boundary_id = 1
		    second_id = 0
		    collected_boundaries = boundaries.BoundariesById(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    for b in collected_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesByIdAllTypes(model_id: int, boundary_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds boundary elements of a model with a given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_id : int
		Id of the boundary element.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		    boundary_id = 1
		    collected_boundaries = boundaries.BoundariesByIdAllTypes(model_id, boundary_id)
		    for b in collected_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesByName(model_id: int, boundary_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds the boundary elements of a model with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific element of the given model.
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
		    boundary_name = "Subcase*"
		    matbounds = boundaries.BoundariesByName(model_id, boundary_name)
		    for b in matbounds:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesByType(model_id: int, boundary_type: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all boundary elements with a specific type of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary (META constant).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    collected_boundaries = boundaries.BoundariesByType(model_id, boundary_type)
		    iter_end = min(10, len(collected_boundaries))
		    for b in collected_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesFromAdvFilters(model_id: int, resultset: object) -> object:

	"""

	This function allows the user to collect boundary elements of a model specified by the given id through some advanced filter. The execution of the script will stop and a window will open in order for the user to specify its advanced filter.

	Parameters
	----------
	model_id : int
		Id of the model.

	resultset : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then the result of advanced filter will refer to current settings of the Advanced Filter window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element of the given model.
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
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    resultset = all_resultsets[1]
		    collected_boundaries = boundaries.BoundariesFromAdvFilters(model_id, resultset)
		    for b in collected_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def BoundariesOfOverlayRun(overlay_run_type: str, overlay_run_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_boundaries` instead.


	This function searches for the boundary elements of an overlay run with a given type and id.

	Parameters
	----------
	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'

	overlay_run_id : int
		Id of the overlay run.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one boundary element of the given overlay run.
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
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    overlay_run_boundaries = boundaries.BoundariesOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for b in overlay_run_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_boundaries instead.", DeprecationWarning)

def BoundariesOfResultset(result: object) -> object:

	"""

	This function collects all boundary elements belonging to a given resultset.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific boundary element belonging to the given resultset. 
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import results
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    res = results.CurrentResultsetOfWindow(model_id, window_name)
		    if res:
		        result_boundaries = boundaries.BoundariesOfResultset(res)
		        for b in result_boundaries:
		            print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def BoundariesTypes(model_id: int) -> object:

	"""

	This function collects all types of boundary elements of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to one type (META constant) of boundary elements for the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    all_types = boundaries.BoundariesTypes(model_id)
		    for boundary_type in all_types:
		        print(boundary_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def BoundariesWithComments(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds the boundary elements of a model for which comments exist.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one boundary element of the model for which comments exist.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.CommentsOfBoundary, boundaries.Boundary

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    boundaries_with_comments = boundaries.BoundariesWithComments(model_id)
		    for b in boundaries_with_comments:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def BoundariesWithName(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function finds the boundary elements of a model for which a name has been defined.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to a boundary element of the model for which a name has been defined.
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.NameOfBoundary, boundaries.Boundary

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    boundaries_with_name = boundaries.BoundariesWithName(model_id)
		    for b in boundaries_with_name:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def CollectNewBoundariesEnd() -> object:

	"""

	This function ends recording the creation of new boundary elements. This function should be preceded by a corresponding call to script function meta.boundaries.CollectNewBoundariesStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific newly created boundary.
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
		from meta import utils
		
		
		def main():
		    boundaries.CollectNewBoundariesStart()
		
		    # create new boundaries
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_boundaries = boundaries.CollectNewBoundariesEnd()
		    for b in new_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewBoundariesStart() -> int:

	"""

	This function starts recording the creation of new boundary elements. This function should be followed by a corresponding call to script function meta.boundaries.CollectNewBoundariesEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import utils
		
		
		def main():
		    boundaries.CollectNewBoundariesStart()
		
		    # create new boundaries
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_boundaries = boundaries.CollectNewBoundariesEnd()
		    for b in new_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CommentsOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_comments` instead.


	This function finds the comments of a boundary element with a specific id and type of a given model. Comments refer to various information which are output in the solver's input file.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	Returns
	-------
	str
		It returns a string referring to the comments of the boundary element.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_id = 1
		    second_id = 0
		    boundary_comments = boundaries.CommentsOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    print(boundary_comments)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_comments instead.", DeprecationWarning)

def DeckSubtypeOfBoundary(model_id: int, boundary_type: int, boundary_subtype: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_deck_subtype` instead.


	This function converts a given META boundary element subtype to the corresponding subtype of a deck of a specified model. A full list of deck names can be found in the User's Guide.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_subtype : int
		Subtype of the boundary element.

	Returns
	-------
	str
		It returns a string with the name of the boundary element subtype for the deck of the specified model.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_subtype = 1
		    deck_subtype = boundaries.DeckSubtypeOfBoundary(
		        model_id, boundary_type, boundary_subtype
		    )
		    print(deck_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_deck_subtype instead.", DeprecationWarning)

def DeckTypeOfBoundary(model_id: int, boundary_type: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_deck_type` instead.


	This function converts a given META boundary element type to the corresponding type of the deck of a specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	Returns
	-------
	str
		It returns a string with the name of the type, for the deck of the specified model, of
		the corresponding to the given META boundary element type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    deck_type = boundaries.DeckTypeOfBoundary(model_id, boundary_type)
		    print(deck_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_deck_type instead.", DeprecationWarning)

def DeformationsOfBoundary(result: object, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_deformations` instead.


	This function calculates deformations for each direction (X, Y, Z, TOTAL), of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Deformation referring to the deformation of a node for the specified boundary element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    boundary_type = constants.FORCE
		    boundary_id = 1
		    second_id = 1
		    boundary_deforms = boundaries.DeformationsOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
		    for deform in boundary_deforms:
		        print(deform.x, deform.y, deform.z, deform.total, deform.node_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_deformations instead.", DeprecationWarning)

def DistanceBoundaryToBoundary(model_id1: int, result1: object, boundary_type1: int, boundary_id1: int, second_id1: int, model_id2: int, result2: object, boundary_type2: int, boundary_id2: int, second_id2: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_boundary` instead.


	This function calculates the distance or the elongation of a boundary element from another boundary element.

	Parameters
	----------
	model_id1 : int
		Id of the model of the 1st boundary element.

	result1 : object
		An object of class Result that refers to a Resultset of the model of the 1st boundary element.

	boundary_type1 : int
		Type of the 1st boundary element (META constant).

	boundary_id1 : int
		Id of the 1st boundary element.

	second_id1 : int
		Second id of the 1st boundary element.

	model_id2 : int
		Id of the model of the 2nd boundary element.

	result2 : object
		An object of class Result that refers to a Resultset of the model of the 2nd boundary element.

	boundary_type2 : int
		Type of the 2nd boundary element (META constant).

	boundary_id2 : int
		Id of the 2nd boundary element.

	second_id2 : int
		Second id of the 2nd boundary element.

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
	boundaries.Boundary, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id1 = 0
		    all_resultsets = results.Resultsets(model_id1)
		    result1 = all_resultsets[1]
		    boundary_type1 = constants.SPC1
		    boundary_id1 = 1
		    second_id1 = 2
		
		    model_id2 = 0
		    all_resultsets = results.Resultsets(model_id2)
		    result2 = all_resultsets[1]
		    boundary_type2 = constants.SPC1
		    boundary_id2 = 2
		    second_id2 = 3
		
		    distance = boundaries.DistanceBoundaryToBoundary(
		        model_id1,
		        result1,
		        boundary_type1,
		        boundary_id1,
		        second_id1,
		        model_id2,
		        result2,
		        boundary_type2,
		        boundary_id2,
		        second_id2,
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_boundary instead.", DeprecationWarning)

def DistanceBoundaryToElement(boundary_model: int, boundary_result, boundary_type: int, boundary_id: int, boundary_second_id: int, element_model: int, element_result, element_type: int, element_id: int, element_second_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_element` instead.


	This function calculates the distance or the elongation of a boundary element from an element of a model for a specific resultset.

	Parameters
	----------
	boundary_model : int
		Id of the model of the boundary element.

	boundary_result : 
		An object of class Result that refers to a Resultset of the model of the boundary element.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	boundary_second_id : int
		Second id of the boundary element.

	element_model : int
		Id of the model of the element.

	element_result : 
		An object of class Result that refers to a Resultset of the model of the element.

	element_type : int
		Type of the element (META constant).

	element_id : int
		Id of the element.

	element_second_id : int
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
	boundaries.Boundary, elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    boundary_second_id = 1
		
		    element_model = 0
		    all_resultsets = results.Resultsets(element_model)
		    element_result = all_resultsets[1]
		    element_type = constants.SHELL
		    element_id = 139
		    element_second_id = -1
		
		    distance = boundaries.DistanceBoundaryToElement(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
		        boundary_second_id,
		        element_model,
		        element_result,
		        element_type,
		        element_id,
		        element_second_id,
		    )
		    # distance = boundaries.DistanceBoundaryToElement(boundary_model, boundary_result, boundary_type, boundary_id, boundary_second_id, element_model, element_result, element_type, element_id, element_second_id, elongation =1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_element instead.", DeprecationWarning)

def DistanceBoundaryToGroup(boundary_model: int, boundary_result: object, boundary_type: int, boundary_id: int, second_id: int, group_model: int, group_result: object, group_name: str, group_instance: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_group` instead.


	This function calculates the distance or the elongation of a boundary element from a group.

	Parameters
	----------
	boundary_model : int
		Id of the model of the boundary element.

	boundary_result : object
		An object of class Result that refers to a Resultset of the model for the boundary.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	group_model : int
		Id of the model of the group.

	group_result : object
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
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    collected_boundaries = boundaries.BoundariesByType(boundary_model, boundary_type)
		    boundary_id = collected_boundaries[0].id
		    second_id = collected_boundaries[0].second_id
		
		    group_model = 0
		    all_resultsets = results.Resultsets(group_model)
		    group_result = all_resultsets[1]
		    group_name = "MyGroup"
		
		    distance = boundaries.DistanceBoundaryToGroup(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
		        second_id,
		        group_model,
		        group_result,
		        group_name,
		    )
		    # distance = boundaries.DistanceBoundaryToGroup(boundary_model, boundary_result, boundary_type, boundary_id, second_id, group_model, group_result, group_name, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_group instead.", DeprecationWarning)

def DistanceBoundaryToLine(boundary_model: int, boundary_result: object, boundary_type: int, boundary_id: int, second_id: int, node1_model: int, node1_result, line_node1: int, node2_model: int, node2_result, line_node2: int, elongation: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_line` instead.


	This function calculates the distance or the elongation of a boundary element from a line.

	Parameters
	----------
	boundary_model : int
		Id of the model of the boundary element.

	boundary_result : object
		An object of class Result that refers to a Resultset of the model of the boundary.

	boundary_type : int
		Type of the boundary (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

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
	int
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
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    line_node1 = 624
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    line_node2 = 659
		
		    distance = boundaries.DistanceBoundaryToLine(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
		        second_id,
		        node1_model,
		        node1_result,
		        line_node1,
		        node2_model,
		        node2_result,
		        line_node2,
		    )
		    # distance = boundaries.DistanceBoundaryToLine(boundary_model, boundary_result, boundary_type, boundary_id, second_id, node1_model, node1_result, line_node1, node2_model, node2_result, line_node2, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_line instead.", DeprecationWarning)

def DistanceBoundaryToLineCoords(model_id: int, result: object, boundary_type: int, boundary_id: int, second_id: int, point1: object, point2: object, elongation: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_line_coords` instead.


	This function calculates the distance or the elongation of a boundary element from a line.

	Parameters
	----------
	model_id : int
		Id of the model.

	result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	point1 : object
		List with the coordinates of the 1st point of the line.

	point2 : object
		List with the coordinates of the 2nd point of the line.

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
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    point1 = list()
		    point1.append(0.25)
		    point1.append(2.32)
		    point1.append(3.39)
		    point2 = list()
		    point2.append(1.35)
		    point2.append(-4.9)
		    point2.append(2.35)
		
		    distance = boundaries.DistanceBoundaryToLineCoords(
		        model_id, result, boundary_type, boundary_id, second_id, point1, point2
		    )
		    # distance = boundaries.DistanceBoundaryToLineCoords(model_id, result, boundary_type, boundary_id, second_id, point1, point2, elongation)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_line_coords instead.", DeprecationWarning)

def DistanceBoundaryToPart(boundary_model: int, boundary_result: object, boundary_type: int, boundary_id: int, second_id: int, part_model: int, result: object, part_type: int, part_id: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_part` instead.


	This function calculates the distance or the elongation of a boundary element from an element.

	Parameters
	----------
	boundary_model : int
		Id of the model of the boundary element.

	boundary_result : object
		An object of class Result that refers to a Resultset of the model of the boundary element.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	part_model : int
		Id of the model of the part.

	result : object
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
	boundaries.Boundary, parts.Part, results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    part_model = 0
		    all_resultsets = results.Resultsets(part_model)
		    part_result = all_resultsets[1]
		    part_type = constants.PSHELL
		    part_id = 1120
		
		    distance = boundaries.DistanceBoundaryToPart(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
		        second_id,
		        part_model,
		        part_result,
		        part_type,
		        part_id,
		    )
		    # distance = boundaries.DistanceBoundaryToPart(boundary_model, boundary_result, boundary_type, boundary_id, second_id, part_model, part_result, part_type, part_id, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_part instead.", DeprecationWarning)

def DistanceBoundaryToPlane(boundary_model: int, boundary_result: object, boundary_type: int, boundary_id: int, second_id: int, node1_model: int, node1_result, plane_node1: int, node2_model: int, node2_result: object, plane_node2: int, node3_model: int, node3_result: object, plane_node3: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_plane` instead.


	This function calculates the distance or the elongation of a boundary element from a plane.

	Parameters
	----------
	boundary_model : int
		Id of the model of the boundary element.

	boundary_result : object
		An object of class Result that refers to a Resultset of the model of the boundary element.

	boundary_type : int
		Type of boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	node1_model : int
		Id of the model of the 1st node of the plane.

	node1_result : 
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
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
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
		from meta import results
		from meta import constants
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    node1_model = 0
		    all_resultsets = results.Resultsets(node1_model)
		    node1_result = all_resultsets[1]
		    plane_node1 = 354
		
		    node2_model = 0
		    all_resultsets = results.Resultsets(node2_model)
		    node2_result = all_resultsets[1]
		    plane_node2 = 847
		
		    node3_model = 0
		    all_resultsets = results.Resultsets(node3_model)
		    node3_result = all_resultsets[1]
		    plane_node3 = 578
		
		    distance = boundaries.DistanceBoundaryToPlane(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
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
		    # distance = boundaries.DistanceBoundaryToPlane(boundary_model, boundary_result, boundary_type, boundary_id, second_id, node1_model, node1_result, plane_node1, node2_model, node2_result, plane_node2, node3_model, node3_result, plane_node3, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_plane instead.", DeprecationWarning)

def DistanceBoundaryToPlaneCoords(model_id: int, result, boundary_type: int, boundary_id: int, second_id: int, point1: object, point2: object, point3: object, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_plane_coords` instead.


	This function calculates the distance or the elongation of a boundary element from a plane.

	Parameters
	----------
	model_id : int
		Id of the model of the boundary element.

	result : 
		An object of class Result that refers to a Resultset of the model of the boundary element.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

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
		It returns a list with float numbers as elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
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
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    point1 = [1.1, -1.21, -2.3]
		    point2 = [0, 1.1, -2]
		    point3 = [0.3, 0.4, 0.99]
		
		    distance = boundaries.DistanceBoundaryToPlaneCoords(
		        model_id, result, boundary_type, boundary_id, second_id, point1, point2, point3
		    )
		    # distance = boundaries.DistanceBoundaryToPlaneCoords(model_id, result, boundary_type, boundary_id, second_id, point1, point2, point3, elongation = 1)
		    if len(distance) != 0:
		        dist_x = distance[0]  # Distance in direction X
		        dist_y = distance[1]  # Distance in direction Y
		        dist_z = distance[2]  # Distance in direction Z
		        dist_total = distance[3]  # Total distance
		        print(dist_x, dist_y, dist_z, dist_total)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_plane_coords instead.", DeprecationWarning)

def HideBoundary(model_id: int, boundary_type: int, boundary_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.hide` instead.


	This function allows the user to hide a boundary element of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	boundaries.HideSomeBoundaries, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_id = 1
		    ret = boundaries.HideBoundary(model_id, boundary_type, boundary_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.hide instead.", DeprecationWarning)

def HideSomeBoundaries(model_id: int, boundary_types: object, boundary_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.hide_boundaries` instead.


	This function allows the user to hide some specific boundary elements of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_types : object
		A list with types of the boundary elements (META constants).

	boundary_ids : object
		A list with ids of the boundary elements.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	boundaries.Boundary, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    boundary_types = list()
		    boundary_ids = list()
		    all_boundaries = boundaries.Boundaries(model_id)
		    for b in all_boundaries:
		        boundary_types.append(b.type)
		        boundary_ids.append(b.id)
		    ret = boundaries.HideSomeBoundaries(model_id, boundary_types, boundary_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.hide_boundaries instead.", DeprecationWarning)

def IdentifiedBoundaries(model_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all identified boundary elements of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect identified boundary elements for all the enabled windows of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific identified boundary element of the given model for the specified window.
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
		    window_name = "MetaPost"
		    identified_boundaries = boundaries.IdentifiedBoundaries(model_id, window_name)
		    iter_end = min(10, len(identified_boundaries))
		    for b in identified_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def IdentifiedBoundariesByType(model_id: int, boundary_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all identified boundary elements with a specific type of a specific model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constants).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect identified boundary elements for all the enabled windows of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific identified boundary element of the given model for the specified window.
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
		    boundary_type = constants.SPC1
		    window_name = "MetaPost"
		    identified_boundaries = boundaries.IdentifiedBoundariesByType(
		        model_id, boundary_type, window_name
		    )
		    iter_end = min(10, len(identified_boundaries))
		    for b in identified_boundaries[0:iter_end]:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def IdentifyBoundary(model_id: int, boundary_type: int, boundary_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.identify` instead.


	This function allows the user to identify a boundary element of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	boundaries.IdentifySomeBoundaries, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_id = 1
		    ret = boundaries.IdentifyBoundary(model_id, boundary_type, boundary_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.identify instead.", DeprecationWarning)

def IdentifySomeBoundaries(model_id: int, boundary_types: object, boundary_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.identify_boundaries` instead.


	This function allows the user to identify some specific boundary elements of a model model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_types : object
		List with types of boundary elements (META constants).

	boundary_ids : object
		List with ids of the boundary elements.

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
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    boundary_types = list()
		    boundary_ids = list()
		    all_boundaries = boundaries.Boundaries(model_id)
		    for b in all_boundaries:
		        boundary_types.append(b.type)
		        boundary_ids.append(b.id)
		    ret = boundaries.IdentifySomeBoundaries(model_id, boundary_types, boundary_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.identify_boundaries instead.", DeprecationWarning)

def IsBoundary(boundary: object) -> int:

	"""

	This function checks whether an object is of class Boundary.

	Parameters
	----------
	boundary : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Boundary, 0 otherwise.

	See Also
	--------
	boundaries.Boundary

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import models
		from meta import utils
		
		
		def main():
		    model_id = 0
		    ObjectList = list()
		    ObjectList.append("a_string")
		    ObjectList.append(boundaries.Boundaries(model_id)[0])
		
		    for ent in ObjectList:
		        if boundaries.IsBoundary(ent):
		            b = ent
		            print("This is an object of class Boundary")
		            print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		        else:
		            print("This is not an object of class Boundary")
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadsOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_loads` instead.


	This function calculates the loads of a boundary element with a specific id and type of a given model. In the case that boundary element is of type FORCE or MOMENT, position 0 of the returned list contains the magnitude and positions 1, 2 and 3 contains the components.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	Returns
	-------
	object
		It returns a list of floats referring to the loads of the boundary element.
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
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    boundary_loads = boundaries.LoadsOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    for load in boundary_loads:
		        print(load)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_loads instead.", DeprecationWarning)

def MaxCoordinatesOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_coordinates` instead.


	This function calculates maximum coordinates in each direction (X, Y, Z) of a boundary element with specific id and type of a given model.

	Parameters
	----------
	model_id : int
		Id of model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	result : object, optional
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list with 3 where each member of the list is an object of class Node referring to the node with the maximun coordinate in each direction of the specified boundary element.
		- 0 = Node with the maximum X coordinate
		- 1 = Node with the maximum Y coordinate
		- 2 = Node with the maximum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    max_node = boundaries.MaxCoordinatesOfBoundary(
		        model_id, boundary_type, boundary_id, second_id, result
		    )
		    if len(max_node):
		        max_x_node = max_node[0]  # Object of the node with the maximum X coordinate
		        print(max_x_node.x)  # X maximum coordinate
		        print(
		            max_x_node.y, max_x_node.z
		        )  # Coordinates in rest directions of the node with the maximum X coordinate
		        print(max_x_node.id)  # Id of the node with the maximum X coordinate
		
		        max_y_node = max_node[1]  # Object of the node with the minimum Y coordinate
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_coordinates instead.", DeprecationWarning)

def MaxDeformationOfBoundary(result, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_deformations` instead.


	This function calculates maximum deformation for each direction (X, Y, Z, TOTAL), of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element

	second_id : int
		Second id of the boundary element

	Returns
	-------
	object
		It returns a list with 4 where each member of the list is an object of class Deformation referring to the maximun deformation in each direction for the specified boundary element.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    max_deform = boundaries.MaxDeformationOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_deformations instead.", DeprecationWarning)

def MaxNodalScalarOfBoundary(result: object, boundary_type: int, boundary_id: int, second_id: str, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_scalar` instead.


	This function calculates maximum nodal scalar value of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : str
		Second id of the boundary element.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		Upon success, it returns an object of class NodalScalar referring to the maximum nodal scalar value of the specified boundary element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    layer = "bottom"  # BOTTOM maximum nodal scalar value if both bottom and top values are loaded
		    max_nodal = boundaries.MaxNodalScalarOfBoundary(
		        result, boundary_type, boundary_id, second_id, layer
		    )
		    if max_nodal:  # Struct with the maximum nodal scalar value
		        print(max_nodal.value)  # Maximum nodal scalar value
		        print(max_nodal.node_id)  # Id of the node with the maximun nodal scalar value
		        print(max_nodal.part_id)  # Id of the part of the maximum nodal scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_scalar instead.", DeprecationWarning)

def MaxNodalVectorOfBoundary(result: object, boundary_type: int, boundary_id: int, second_id: int, layer: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_vector` instead.


	This function calculates maximum nodal vector value of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	layer : int, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns an object of class NodalVector referring to the maximum nodal vector value of the specified boundary element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import results
		from meta import constants
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    max_nodal = boundaries.MaxNodalVectorOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
		    if max_nodal:  # Object with the maximum nodal vector value
		        print(max_nodal.value)  # Maximum nodal vector value
		        print(
		            max_nodal.x, max_nodal.y, max_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the maximun nodal vector value
		        print(max_nodal.node_id)  # Id of the node with the maximun nodal vector value
		        print(max_nodal.part_id)  # Id of the part or -1 of no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_vector instead.", DeprecationWarning)

def MetaSubtypeOfBoundary(model_id: int, boundary_type: int, boundary_subtype: str) -> int:

	"""

	This function converts a given boundary element subtype of a deck of a given model to the corresponding META keyword subtype.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Deck type of the boundary.

	boundary_subtype : str
		Deck subtype of the boundary.

	Returns
	-------
	int
		It returns an integer, referring to the META constant subtype of the corresponding
		given boundary subtype of the specified model.
		Upon failure, it returns 0.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0  # Abaqus model for this example
		    boundary_type = constants.MPC
		    boundary_subtype = "Equation"
		
		    meta_subtype = boundaries.MetaSubtypeOfBoundary(
		        model_id, boundary_type, boundary_subtype
		    )
		    print(meta_subtype)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaTypeOfBoundary(model_id: int, boundary_type: str) -> int:

	"""

	This function converts a given boundary element type of a deck of a specified model to the corresponding META type.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : str
		Deck type of the boundary element.

	Returns
	-------
	int
		It returns an integer, equal to the META constant of the corresponding boundary element type of the specified model.
		Upon failure, a negative value is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		
		
		def main():
		    model_id = 0  # Abaqus model in this example
		    boundary_type = "Equation"
		    meta_type = boundaries.MetaTypeOfBoundary(model_id, boundary_type)
		    print(meta_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MinCoordinatesOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int, result: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_coordinates` instead.


	This function calculates minimum coordinates in each direction (X, Y, Z) of a boundary element with specific id and type of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	result : object
		An object of class Result that refers to a Resultset of the model. If it is absent, then maximum coordinates will refer to the ORIGINAL STATE.

	Returns
	-------
	object
		It returns a list with 3 objects where each member of the list is an object of class Node referring to the node with the minimun coordinate in each direction of the specified boundary element.
		- 0 = Node with the minimum X coordinate
		- 1 = Node with the minimum Y coordinate
		- 2 = Node with the minimum Z coordinate
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, nodes.Node, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    min_node = boundaries.MinCoordinatesOfBoundary(
		        model_id, boundary_type, boundary_id, second_id, result
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_coordinates instead.", DeprecationWarning)

def MinDeformationOfBoundary(result, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_deformations` instead.


	This function calculates minimum deformation for each direction (X, Y, Z, TOTAL) of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	Returns
	-------
	object
		It returns a list with 4 where each member of the list is an object of class Deformation referring to the minimun deformation in each direction for the specified boundary element.
		- 0 = X deformation
		- 1 = Y deformation
		- 2 = Z deformation
		- 3 = TOTAL deformation
		Upon failure, an empty list is returned.

	See Also
	--------
	boundaries.Boundary, results.Result, results.Deformation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    min_deform = boundaries.MinDeformationOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_deformations instead.", DeprecationWarning)

def MinNodalScalarOfBoundary(result, boundary_type: int, boundary_id: int, second_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_scalar` instead.


	This function calculates minimum nodal scalar value of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns an object of class NodalScalar referring to the minimum nodal scalar value of the specified boundary element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    min_nodal = boundaries.MinNodalScalarOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
		    if min_nodal:  # Object with the minimum nodal scalar value
		        print(min_nodal.value)  # Minimum nodal scalar value
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal scalar value
		        print(
		            min_nodal.part_id
		        )  # Id of the part of the node with the minimum nodal scalar value
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_scalar instead.", DeprecationWarning)

def MinNodalVectorOfBoundary(result, boundary_type: int, boundary_id: int, second_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_vector` instead.


	This function calculates minimum nodal vector value of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	layer : str, optional
		Location of the nodal vector values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns an object of class NodalVector referring to the maximum nodal vector value of the specified boundary element.
		Upon failure, None is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    min_nodal = boundaries.MinNodalVectorOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
		    if min_nodal:  # Object with the minimum nodal vector value
		        print(min_nodal.value)  # Minimum nodal vector value
		        print(
		            min_nodal.x, min_nodal.y, min_nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the minimun nodal vector
		        print(min_nodal.node_id)  # Id of the node with the minimun nodal vector value
		        print(min_nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_vector instead.", DeprecationWarning)

def NameOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_name` instead.


	This function finds the name of a boundary element with a specific id and type of a given model.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

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
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		
		    old_boundary_name = boundaries.NameOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    print(old_boundary_name)
		
		    boundary_name = "SPC_on_crankshaft"
		    boundaries.AddNameOnBoundary(
		        model_id, boundary_type, boundary_id, second_id, boundary_name
		    )
		
		    new_boundary_name = boundaries.NameOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    print(new_boundary_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_name instead.", DeprecationWarning)

def NodalScalarOfBoundary(result, boundary_type: int, boundary_id: int, second_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_scalar` instead.


	This function calculates all nodal scalar values of the nodes of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : 
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list wwhere each member of the list is an object of class NodalScalar referring to one nodal scalar values of a node of the specified boundary element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalScalar, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    boundary_nodal = boundaries.NodalScalarOfBoundary(
		        result, boundary_type, boundary_id, second_id
		    )
		    for nodal in boundary_nodal:  # Matrix with nodal_scalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_scalar instead.", DeprecationWarning)

def NodalVectorOfBoundary(result: object, boundary_type: int, boundary_id: int, second_id: int, layer: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_nodal_vector` instead.


	This function calculates all nodal vector values of the nodes of a boundary element with specific id and type of a given model.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	layer : str, optional
		Location of the nodal scalar values. It should be specified only if both bottom and top values are loaded. Possible values are:
		- 'bottom' (default)
		- 'top'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class NodalVector referring to one nodal vector value of a node of the specified boundary element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, results.NodalVector, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    layer = (
		        "bottom"  # BOTTOM nodal vector values if both bottom and top values are loaded
		    )
		    boundary_nodal = boundaries.NodalVectorOfBoundary(
		        result, boundary_type, boundary_id, second_id, layer
		    )
		    for nodal in boundary_nodal:  # Matrix with nodal_vector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_nodal_vector instead.", DeprecationWarning)

def NumOfBoundariesByType(model_id: int, boundary_type: int) -> int:

	"""

	This function finds the number of the boundary elements of a model with a specific type.

	Parameters
	----------
	model_id : int
		Id of the model

	boundary_type : int
		Type of the boundary element (META constant).

	Returns
	-------
	int
		It returns the number of the boundary elements with the specific type for the given model.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    num_of_boundaries = boundaries.NumOfBoundariesByType(model_id, boundary_type)
		    print(num_of_boundaries)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReportNewBoundaries() -> object:

	"""

	This function collects the newly created boundary elements from the last call of script function meta.boundaries.CollectNewBoundariesStart(). This function should be preceded by a corresponding call to script function meta.boundaries.CollectNewBoundariesStart() and should be followed by a corresponding call to script function meta.boundaries.CollectNewBoundariesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific newly created boundary.
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
		from meta import utils
		
		
		def main():
		    boundaries.CollectNewBoundariesStart()
		
		    # create new boundaries
		    utils.MetaCommand("model active empty")
		    utils.MetaCommand("read geom Nastran /home/examples/NastranEx2.nas")
		
		    new_boundaries = boundaries.ReportNewBoundaries()
		    for b in new_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    boundaries.CollectNewBoundariesEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ResultsetsOfBoundary(model_id: int, boundary_type: int, boundary_id: int, second_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_resultsets` instead.


	This function collects all resultsets of a boundary element with a given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	second_id : int
		Second id of the boundary element.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Resultset referring to one specific resultset of the given boundary element.
		Upon failure, an empty list is returned.

	See Also
	--------
	results.Result, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    boundary_results = boundaries.ResultsetsOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    for res in boundary_results:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_resultsets instead.", DeprecationWarning)

def ShowBoundary(model_id: int, boundary_type: int, boundary_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.show` instead.


	This function sets visible a boundary element of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_type : int
		Type of the boundary element (META constant).

	boundary_id : int
		Id of the boundary element.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	boundaries.ShowSomeBoundaries, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    model_id = 0
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    ret = boundaries.ShowBoundary(model_id, boundary_type, boundary_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.show instead.", DeprecationWarning)

def ShowSomeBoundaries(model_id: int, boundary_types: object, boundary_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.show_boundaries` instead.


	This function allows the user to make visible some specific boundary elements of a model specified by its id.

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_types : object
		List with the types of boundary elements (META constants).

	boundary_ids : object
		List with the ids of the boundary elements.

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
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    all_boundaries = boundaries.Boundaries(model_id)
		
		    boundary_types = list()
		    boundary_ids = list()
		    for b in all_boundaries:
		        boundary_types.append(b.type)
		        boundary_ids.append(b.id)
		    ret = boundaries.ShowSomeBoundaries(model_id, boundary_types, boundary_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.show_boundaries instead.", DeprecationWarning)

def StringBoundaryType(boundary_type: int) -> str:

	"""

	This function converts a given META boundary element type to its corresponding string representation.

	Parameters
	----------
	boundary_type : int
		Type of the boundary element (META constant).

	Returns
	-------
	str
		It returns a string with the name of the META boundary element type.
		Upon failure, an empty string is returned.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary_type = constants.MPC
		    str_boundary_type = boundaries.StringBoundaryType(boundary_type)
		    print(str_boundary_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateBoundary(bound) -> object:

	"""

	This function updates the data of the given boundary object. Update is based in the field 'id', 'type' and 'model_id' of the given boundary object.

	Parameters
	----------
	bound : 
		An object of class Boundary.

	Returns
	-------
	object
		Upon success, it returns the new updated boundary object.
		Else, None is returned.

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
		from meta import utils
		
		
		def main():
		    model_id = 0
		    type = constants.FORCE
		    id = 2
		    second_id = 112
		    collected_boundaries = boundaries.BoundariesById(model_id, type, id, second_id)
		    if len(collected_boundaries):
		        b = collected_boundaries[0]
		    # commands which alter the data of the boundary object
		    utils.MetaCommand("add elem all")
		
		    b = boundaries.UpdateBoundary(b)
		    if b:  # Update OK
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		    else:  # Update FAILED
		        print("This is not a valid boundary object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleBoundaries(window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all visible boundary elements of the given model specified.

	Parameters
	----------
	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given model for the specified window.
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
		    window_name = "MetaPost"
		    all_boundaries = boundaries.VisibleBoundaries(model_id, window_name)
		
		    for b in all_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def VisibleBoundariesByType(boundary_type: int, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_boundaries` instead.


	This function collects all visible boundary elements with a specific type of the given model.

	Parameters
	----------
	boundary_type : int
		Type of the boundary (META constant).

	window_name : str, optional
		Optional argument "window_name" refers to the name of the window of the model. If optional argument "window_name" is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	model_id : int
		Id of the model

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given model for the specified window.
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
		    boundary_type = constants.FORCE
		    window_name = "MetaPost"
		    all_boundaries = boundaries.VisibleBoundariesByType(
		        model_id, boundary_type, window_name
		    )
		
		    for b in all_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_boundaries instead.", DeprecationWarning)

def VisibleBoundariesOfGroup(model_id: int, group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all visible boundary elements of a given group belonging to the specified model. 

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given group for the specified window.
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
		    window_name = "MetaPost"
		    visible_boundaries = boundaries.VisibleBoundariesOfGroup(
		        model_id, group_name, window_name
		    )
		    for b in visible_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def VisibleBoundariesOfGroupByType(model_id: int, group_name: str, boundary_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all visible boundary elements with a specific type of a given group belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	boundary_type : int
		Type of the boundary element (META constants).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given group for the specified window.
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
		    boundary_type = constants.FORCE
		    window_name = "MetaPost"
		    visible_boundaries = boundaries.VisibleBoundariesOfGroupByType(
		        model_id, group_name, boundary_type, window_name
		    )
		    for b in visible_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def VisibleBoundariesOfGroupInstance(model_id: int, group_name: str, group_instance: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all visible boundary elements of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Group instance.

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given group for the specified window.
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
		    window_name = "MetaPost"
		    visible_boundaries = boundaries.VisibleBoundariesOfGroupInstance(
		        model_id, group_name, group_instance, window_name
		    )
		    for b in visible_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def VisibleBoundariesOfGroupInstanceByType(model_id: int, group_name: str, group_instance: int, boundary_type: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.get_boundaries` instead.


	This function collects all visible boundary elements with a specific type of a given group instance belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	group_instance : int
		Group instance.

	boundary_type : int
		Type of the boundary element (META constant).

	window_name : str, optional
		Refers to the name of the window of the model. If it is absent then this function will collect visible boundary elements for the active or first enabled window of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Boundary referring to one specific visible boundary element of the given group for the specified window.
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
		    boundary_type = constants.FORCE
		    window_name = "MetaPost"
		    visible_boundaries = boundaries.VisibleBoundariesOfGroupInstanceByType(
		        model_id, group_name, group_instance, boundary_type, window_name
		    )
		    for b in visible_boundaries:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.get_boundaries instead.", DeprecationWarning)

def DistanceBoundaryToCutPlane(boundary_id: int, boundary_result: object, boundary_type: int, plane_name: str, second_id: int, boundary_model: int, elongation: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_distance_from_cut_plane` instead.


	This function calculates the distance or the elongation of a boundary element from an existing cut plane.

	Parameters
	----------
	boundary_id : int
		Id of the boundary element.

	boundary_result : object
		An object of class Result that refers to a Resultset of the model.

	boundary_type : int
		Type of boundary element (META constant).

	plane_name : str
		Name of the cut plane.

	second_id : int
		Second id of the boundary element.

	boundary_model : int
		Id of the model of the boundary element.

	elongation : int, optional
		0 for distance, 1 for elongation. Default value is 0.

	Returns
	-------
	object
		It returns a list with float numbers as elements referring to the corresponding distance in each direction (X, Y, Z, TOTAL).
		- In position 0 there is the distance in X direction.
		- In position 1 there is the distance in Y direction.
		- In position 2 there is the distance in Z direction.
		- In position 3 there is the TOTAL distance.
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
		from meta import results
		from meta import constants
		
		
		def main():
		    boundary_model = 0
		    all_resultsets = results.Resultsets(boundary_model)
		    boundary_result = all_resultsets[1]
		    boundary_type = constants.FORCE
		    boundary_id = 2
		    second_id = 112
		    plane_name = "DEFAULT_PLANE_ZX"
		
		    distance = boundaries.DistanceBoundaryToCutPlane(
		        boundary_model,
		        boundary_result,
		        boundary_type,
		        boundary_id,
		        second_id,
		        plane_name,
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_distance_from_cut_plane instead.", DeprecationWarning)

def DegreesOfFreedomOfBoundary(boundary_id: int, boundary_type: int, second_id: int, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.boundaries.Boundary.get_dofs` instead.


	This function calculates the degrees of freedom of an spc boundary element with a specific id and type of a given model.

	Parameters
	----------
	boundary_id : int
		Id of the boundary element.

	boundary_type : int
		Type of the boundary element (META constants).

	second_id : int
		Second id of the boundary element.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list of integers referring to the degrees of freedom of the spc boundary element.
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
		    boundary_type = constants.SPC1
		    boundary_id = 2
		    second_id = 1
		    dofs = boundaries.DegreesOfFreedomOfBoundary(
		        model_id, boundary_type, boundary_id, second_id
		    )
		    for dof in dofs:
		        print(dof)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.boundaries.Boundary.get_dofs instead.", DeprecationWarning)

def IdentifyBoundariesReset(model_id: int, boundary_types: object, boundary_ids: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.reset_identify_boundaries` instead.


	This function allows the user to reset the identification of all or specific elements of the specified model.
	It can be called with two different ways. The one is with lists of ids and types, and the other is with boundary_ids = 'all' and boundary_types = constants.BOUNDARY_TYPE

	Parameters
	----------
	model_id : int
		Id of the model.

	boundary_types : object
		Either a list with integers corresponding to the types of the boundary elements, or an integer that represents the type of the elements (zero for all boundary element types)

	boundary_ids : object
		List with integers corresponding to the ids of the boundary elements, or string 'all'.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import constants
		from meta import boundaries
		
		
		def main():
		    model_id = 0
		    boundary_types = [constants.FORCE, constants.PLOAD4]
		    boundary_ids = [1, 2]
		    # or
		    # boundary_ids = 'all'
		    boundaries.IdentifyBoundariesReset(model_id, boundary_types, boundary_ids)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.reset_identify_boundaries instead.", DeprecationWarning)

class Boundary():

	"""

	Class for boundary elements
	
	The type of the boundary element is described through an integer index number corresponding to specific META constant.
	There are functions available that report the corrsponding constant names of constant values.
	Boundary elements also have subtypes and second ids.
	
	A full list of boundary element types and constants can be derived from the following example.
	This class can be subclassed as shown in the example.

	See Also
	--------
	constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    b = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    if b:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_model
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    r = boundary.get_model()
		    if r:
		        print(r.id, r.name, r.label, r.deck, r.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import windows
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    specifier = "all"
		    b_nodes = boundary.get_nodes(specifier)
		    for n in b_nodes:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		        w = windows.Window(name="MetaPost", page_id=0)
		        specifier = "visible"
		        b_nodes = boundary.get_nodes(specifier, window=w)
		        for n in b_nodes:
		            print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    resultsets = boundary.get_resultsets()
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
		# method: get_name
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    name = boundary.get_name()
		    print(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_comments
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    comments = boundary.get_comments()
		    print(comments)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_type
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    deck_type = boundary.get_deck_type()
		    print(deck_type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deck_subtype
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    deck_subtype = boundary.get_deck_subtype()
		    print(deck_subtype)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_loads
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=1, model_id=0, type=constants.FORCE)
		    load = boundary.get_loads()
		    print(load)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_boundary
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    boundary2 = boundaries.Boundary(
		        id=1, second_id=1, model_id=model.id, type=constants.FORCE
		    )
		
		    res = model.get_current_resultset()
		
		    dist = boundary.get_distance_from_boundary(res, boundary2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_boundary
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    boundary2 = boundaries.Boundary(
		        id=1, second_id=1, model_id=model.id, type=constants.FORCE
		    )
		
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_boundary(res, boundary2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import elements
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    element = elements.Element(
		        id=100, model_id=model.id, type=constants.SOLID, second_id=-1
		    )
		
		    res = model.get_current_resultset()
		
		    dist = boundary.get_distance_from_element(res, element, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import elements
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    element = elements.Element(
		        id=100, model_id=model.id, type=constants.SOLID, second_id=-1
		    )
		
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_element(res, element, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    part = parts.Part(id=1, model_id=model.id, type=constants.PSHELL)
		
		    res = model.get_current_resultset()
		
		    dist = boundary.get_distance_from_part(res, part, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import parts
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    part = parts.Part(id=1, model_id=model.id, type=constants.PSHELL)
		
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_part(res, part, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    group = groups.Group(name="group_name", model_id=0)
		
		    res = model.get_current_resultset()
		
		    dist = boundary.get_distance_from_group(res, group, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import groups
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    group = groups.Group(name="group_name", model_id=0)
		    res = model.get_current_resultset()
		    elong = boundary.get_elongation_from_group(res, group, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_cut_plane
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    plane = planes.Plane(name="plane_name")
		    res = model.get_current_resultset()
		    dist = boundary.get_distance_from_cut_plane(res, plane)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_cut_plane
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import planes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    plane = planes.Plane(name="plane_name")
		    res = model.get_current_resultset()
		    elong = boundary.get_elongation_from_cut_plane(res, plane)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = boundary.get_distance_from_line(res, node1, res, node2, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = boundary.get_elongation_from_line(res, node1, res, node2, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    node3 = nodes.Node(id=300, model_id=model.id)
		    res = model.get_current_resultset()
		    dist = boundary.get_distance_from_plane(res, node1, res, node2, res, node3, res)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		from meta import nodes
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    node1 = nodes.Node(id=100, model_id=model.id)
		    node2 = nodes.Node(id=200, model_id=model.id)
		    node3 = nodes.Node(id=300, model_id=model.id)
		    res = model.get_current_resultset()
		    elong = boundary.get_elongation_from_plane(res, node1, res, node2, res, node3, res)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_line_coords
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, 0.31]
		    res = model.get_current_resultset()
		
		    dist = boundary.get_distance_from_line_coords(res, point1, point2)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_line_coords
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, 0.31]
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_line_coords(res, point1, point2)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    point3 = [1.35, 2.49, -3.3]
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_plane_coords
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    point3 = [1.35, 2.49, -3.3]
		    res = model.get_current_resultset()
		
		    elong = boundary.get_elongation_from_plane_coords(res, point1, point2, point3)
		    print(elong)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_coordinates
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    specifier = "min"
		    coords = boundary.get_coordinates(specifier)
		    for n in coords:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_deformations
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    res = model.get_current_resultset()
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    resultset = res
		    specifier = "max"
		    boundary_deforms = boundary.get_deformations(resultset, specifier)
		    for deform in boundary_deforms:
		        print(deform.x, deform.y, deform.z, deform.total, deform.node_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_scalar
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    res = model.get_current_resultset()
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		
		    resultset = res
		    specifier = "min"
		    nodal_scalar = boundary.get_nodal_scalar(resultset, specifier)
		    # specifier = 'max'
		    # nodal_scalar = boundary.get_nodal_scalar(res, specifier, layer = 'top' )
		    for nodal in nodal_scalar:  # List with nodal_scalar objects
		        print(nodal.value)  # Nodal scalar value
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodal_vector
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    res = model.get_current_resultset()
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		
		    resultset = res
		    specifier = "min"
		    nodal_vector = boundary.get_nodal_vector(resultset, specifier)
		    # specifier = 'all'
		    # nodal_vector = boundary.get_nodal_vector(res, specifier, layer = 'top' )
		    for nodal in nodal_vector:  # List with nodal_vector objects
		        print(nodal.value)  # Nodal vector value
		        print(
		            nodal.x, nodal.y, nodal.z
		        )  # Normalized coordinates (X, Y, Z) of the nodal vector
		        print(nodal.node_id)  # Id of the node
		        print(nodal.part_id)  # Id of the part or -1 if no part exists
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    name = "boundary_name"
		    ret = boundary.set_name("boundary_name")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    ret = boundary.identify()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    ret = boundary.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=0, model_id=model.id, type=constants.FORCE
		    )
		    ret = boundary.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=0, model_id=model.id, type=constants.FORCE
		    )
		    ret = boundary.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_dofs
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    boundary = boundaries.Boundary(id=1, second_id=1, model_id=0, type=constants.SPC)
		    dofs = boundary.get_dofs()
		    print(dofs)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_plane_coords
		# PYTHON script
		import meta
		from meta import boundaries
		from meta import constants
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    boundary = boundaries.Boundary(
		        id=1, second_id=100, model_id=model.id, type=constants.SPC
		    )
		    point1 = [0.25, 1.32, 7.39]
		    point2 = [0.35, 4.49, -2.3]
		    point3 = [1.35, 2.49, -3.3]
		    res = model.get_current_resultset()
		    dist = boundary.get_distance_from_plane_coords(res, point1, point2, point3)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import constants
		from meta import boundaries
		
		
		def main():
		    bound = boundaries.Boundary(id=1, second_id=100, model_id=0, type=constants.SPC)
		    can_use = bound.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the boundary element.

	"""

	second_id: int = None
	"""
	Second id of the boundary element.

	"""

	model_id: int = None
	"""
	Model number of the boundary element.

	"""

	type: int = None
	"""
	Type of the boundary element.

	"""

	subtype: int = None
	"""
	Subtype of the boundary element.

	"""

	visible: int = None
	"""
	- 1 if boundary element is visible on the active or first enabled window of the active page
	- 0 if boundary element is not visible

	"""

	def get_model(self) -> object:

		"""

		This method returns the model of the boundary element.


		Returns
		-------
		object
			Upon success, it returns an object of type Model referring to the model of the node. Upon failure, it returns None.

		"""


	def get_nodes(self, specifier: str, window: object) -> object:

		"""

		This methods gets the nodes of the boundary element.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : gets all nodes (default value).
			- 'visible' : gets visible nodes. Optionally combined with argument window.

		window : object, optional
			An object of class Window that refers to the window. If this argument is set, the method will return only the visible nodes in this window.

		Returns
		-------
		object
			Upon success, it returns a list with objects of type Node. Upon failure, it returns an empty list.

		"""


	def get_resultsets(self) -> object:

		"""

		This method gets all resultsets of the boundary element.


		Returns
		-------
		object
			Upon success, it returns a list with objects of type Result. Upon failure, it returns an empty list.

		"""


	def get_name(self) -> str:

		"""

		This method gets the name of the boundary element.


		Returns
		-------
		str
			Upon success, it returns the name of the boundary element. Upon failure, it returns None.

		"""


	def get_comments(self) -> str:

		"""

		This method gets the comments of the boundary element.


		Returns
		-------
		str
			Upon success, it returns a string with all comments of the node. Upon failure, it returns None.

		"""


	def get_deck_type(self) -> str:

		"""

		This method gets the type of the boundary element.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the type for the deck of the boundary element.Upon failure, None is returned.

		"""


	def get_deck_subtype(self) -> str:

		"""

		This method gets the subtype of the boundary element.


		Returns
		-------
		str
			Upon success, it returns a string with the name of the subtype for the deck of the boundary element.Upon failure, None is returned.

		"""


	def get_loads(self) -> object:

		"""

		This method gets the loads of the boundary element. In the case that boundary element is of type FORCE or MOMENT, position 0 of the returned list contains the magnitude and positions 1, 2 and 3 contains the components.


		Returns
		-------
		object
			It returns a list of floats referring to the loads of the boundary element. Upon failure, an empty list is returned.

		"""


	def get_dofs(self) -> object:

		"""

		This method gets the degrees of freedom of the spc boundary element.


		Returns
		-------
		object
			Upon success, it returns a list of integers referring to the degrees of freedom of the spc boundary element.Upon failure, an empty list is returned.

		"""


	def get_distance_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		boundary : object
			An object of the class Boundary.

		boundary_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given boundary element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_boundary(self, resultset: object, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the elongation of the boundary element from a given boundary element. 


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		boundary : object
			An object of the class Boundary.

		boundary_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given boundary element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		element : object
			An object of the class Element.

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_element(self, resultset: object, element: object, element_resultset: object) -> object:

		"""

		This method gets the elongation of the boundary element from a given element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		element : object
			An object of the class Element

		element_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given element.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		part : object
			An object of the class Part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_part(self, resultset: object, part: object, part_resultset: object) -> object:

		"""

		This method gets the elongation of the boundary element from a given part.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		part : object
			An object of the class Part.

		part_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given part.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		group : object
			An object of the class group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given group.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_group(self, resultset: object, group: object, group_resultset: object) -> object:

		"""

		This method gets the elongation of the boundary element from a given group.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		group : object
			An object of the class group.

		group_resultset : object
			An object of class Result that refers to a Resultset of the model, of the given group.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the distance of the boundary element from a given cutplane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		plane : object
			An object of the class Plane.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_cut_plane(self, resultset: object, plane: object) -> object:

		"""

		This method gets the elongation of the boundary element from a given cut plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		plane : object
			An object of the class Plane

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_line(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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

		This method gets the elongation of the boundary element from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		node1 : object
			An object of class Node.

		node1_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		node2 : object
			An object of class Node.

		node2_resultset : object
			An object of class Result that refers to a Resultset of the model, of the node1.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_plane(self, resultset: object, node1: object, node1_resultset: object, node2: object, node2_resultset: object, node3: object, node3_resultset: object) -> object:

		"""

		This method gets the distance of the boundary element from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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

		This method gets the elongation of the boundary element from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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

		This method gets the distance of the boundary element from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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

		This method gets the elongation of the boundary element from a given line.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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

		This method gets the distance of the boundary element from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

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


	def get_elongation_from_plane_coords(self, resultset: object, point1: object, point2: object, point3: int) -> object:

		"""

		This method gets the elongation of the boundary element from a given plane.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model, of the boundary element.

		point1 : object
			List with the coordinates of the first point of the line.

		point2 : object
			List with the coordinates of the second point of the line.

		point3 : int
			List with the coordinates of the third point of the line.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_coordinates(self, specifier: str, resultset: object) -> object:

		"""

		This method gets the coordinates in each direction (X, Y, Z) of the boundary element.


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
			Upon success, it returns a list with 3 objects where each member of the list is an object of class Node referring to the node with the minimun or maximum coordinate in each direction of the specified boundary element.- 0 = Node with the minimum/maximum X coordinate- 1 = Node with the minimum/maximum Y coordinate- 2 = Node with the minimum/maximum Z coordinate. Upon failure, an empty list is returned.

		"""


	def get_deformations(self, resultset: object, specifier: str) -> object:

		"""

		This method gets the deformations of the boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all deformations (default value).
			- 'max' : max deformation in each direction
			- 'min' : min deformation in each direction

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Deformation referring to the deformation of a node for the boundary element.Upon failure, an empty list is returned.

		"""


	def get_nodal_scalar(self, resultset: object, specifier: str, layer: str) -> object:

		"""

		This method gets the nodal scalar values for the boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar values (default value).
			- 'max' : max nodal scalar value
			- 'min' : min nodal scalar value

		layer : str, optional
			Location of the nodal scalar values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalScalar.Upon failure it returns an empty list.

		"""


	def get_nodal_vector(self, resultset: object, specifier: str, layer: str) -> object:

		"""

		This method gets the nodal vector values for the boundary element.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all nodal scalar (default value).
			- 'max' : max nodal scalar
			- 'min' : min nodal scalar

		layer : str, optional
			Location of the nodal vector values. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a list with objects of class NodalVector.Upon failure it returns an empty list.

		"""


	def set_name(self, name: str) -> bool:

		"""

		This method sets the name of the boundary element.


		Parameters
		----------
		name : str
			Name of the boundary element

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify(self) -> bool:

		"""

		This method identifies the boundary element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the boundary element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the boundary element. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Boundary entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

