from __future__ import annotations
from typing import *

def ChangeEdgeVectorOfPlane(plane_name: str, xedge: float, yedge: float, zedge: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_edge_vector` instead.


	This function changes the edge vector (X, Y, Z) of a specific plane.

	Parameters
	----------
	plane_name : str
		Name of plane.

	xedge : float
		X component of edge vector.

	yedge : float
		Y component of edge vector.

	zedge : float
		Z component of edge vector.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "plane_axis2"
		    xedge = 0
		    yedge = 1
		    zedge = 0
		    ret = planes.ChangeEdgeVectorOfPlane(plane_name, xedge, yedge, zedge)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_edge_vector instead.", DeprecationWarning)

def ChangeNormalVectorOfPlane(plane_name: str, xnorm: float, ynorm: float, znorm: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_normal_vector` instead.


	This function changes the normal vector (X, Y, Z) of an specific plane.

	Parameters
	----------
	plane_name : str
		Name of plane.

	xnorm : float
		X component of normal vector.

	ynorm : float
		Y component of normal vector.

	znorm : float
		Z component of normal vector.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "plane_axis2"
		    xedge = 0
		    yedge = 1
		    zedge = 0
		    ret = planes.ChangeNormalVectorOfPlane(plane_name, xedge, yedge, zedge)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_normal_vector instead.", DeprecationWarning)

def ChangeOriginOfPlane(plane_name: str, xorig: float, yorig: float, zorig: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_origin` instead.


	This function changes the origin (X, Y, Z) of an specific plane.

	Parameters
	----------
	plane_name : str
		Name of plane.

	xorig : float
		X coordinate of origin.

	yorig : float
		Y coordinate of origin.

	zorig : float
		Z coordinate of origin.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "Plane1"
		    xorig = 1.26
		    yorig = 7.52
		    zorig = 3.59
		    ret = planes.ChangeOriginOfPlane(plane_name, xorig, yorig, zorig)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_origin instead.", DeprecationWarning)

def CollectNewPlanesEnd() -> object:

	"""

	This function ends recording the creation of new planes. This function should be preceded by a corresponding call to script function meta.planes.CollectNewPlanesStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific newly created plane.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import utils
		
		
		def main():
		    planes.CollectNewPlanesStart()
		
		    # create new planes
		    utils.MetaCommand("plane new default xy")
		    utils.MetaCommand("plane new default yz")
		
		    new_planes = planes.CollectNewPlanesEnd()
		    for pl in new_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewPlanesStart() -> int:

	"""

	This function starts recording the creation of new planes. This function should be followed by a corresponding call to script function meta.planes.CollectNewPlanesEnd().

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import utils
		
		
		def main():
		    planes.CollectNewPlanesStart()
		
		    # create new planes
		    utils.MetaCommand("plane new default xy")
		    utils.MetaCommand("plane new default yz")
		
		    new_planes = planes.CollectNewPlanesEnd()
		    for pl in new_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def ColorOfPlane(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_color` instead.


	This function finds the color of a specific plane.

	Parameters
	----------
	plane_name : str
		Name of the plane

	Returns
	-------
	object
		Upon success, it returns a color object with the color of the corresponding plane.
		Else, None is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    col = planes.ColorOfPlane(plane_name)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_color instead.", DeprecationWarning)

def CreatePlane(plane_name: str, xorig: float, yorig: float, zorig: float, xnorm: float, ynorm: float, znorm: float) -> object:

	"""

	This function creates a new plane with a specific name. If a plane with the given name already exists, then this function will fail.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	xorig : float
		X coordinate of the origin.

	yorig : float
		Y coordinate of the origin.

	zorig : float
		Z coordinate of the origin.

	xnorm : float
		X coordinate of normal vector.

	ynorm : float
		Y coordinate of normal vector.

	znorm : float
		Z coordinate of normal vector.

	Returns
	-------
	object
		Upon success, it returns an object of class Plane referring to the newly created plane.
		Else, None is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "new_plane"
		    xorig = 1.234
		    yorig = 15.46
		    zorig = -3.2
		    xnorm = 0
		    ynorm = 1
		    znorm = 0
		    pl = planes.CreatePlane(plane_name, xorig, yorig, zorig, xnorm, ynorm, znorm)
		    if pl:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeletePlane(plane_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.delete` instead.


	This function deletes an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_YZ"
		    ret = planes.DeletePlane(plane_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.delete instead.", DeprecationWarning)

def EdgeVectorOfPlane(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_edge_vector` instead.


	This function calculates the edge vector (X, Y, Z) of an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	Returns
	-------
	object
		Upon success, it returns a list with 3 elements referring to the X, Y and Z coordinates of the edge vector of the specified plane.
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_YZ"
		    edge_vector = planes.EdgeVectorOfPlane(plane_name)
		    if len(edge_vector):
		        xedge = edge_vector[0]  # X coordinate of edge vector
		        yedge = edge_vector[1]  # Y coordinate of edge_vector
		        zedge = edge_vector[2]  # Z coordinate of edge_vector
		        print(xedge, yedge, zedge)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_edge_vector instead.", DeprecationWarning)

def HidePlane(plane_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.hide` instead.


	This function hides an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window in which the plane will be identified. If optional argument "window_name" is absent then plane will be hidden in all windows.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    window_name = "MetaPost"
		    ret = planes.HidePlane(plane_name, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.hide instead.", DeprecationWarning)

def HideSomePlanes(plane_names: object, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.hide_planes` instead.


	This function allows the user to hide some specific planes specified by their names. 

	Parameters
	----------
	plane_names : object
		List with names of planes to be hidden.

	window_name : str, optional
		Name of the window in which the plane will be identified. If optional argument "window_name" is absent then plane will be hidden in all windows.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    all_planes = planes.Planes()
		    plane_names = list()
		    for pl in all_planes:
		        plane_names.append(pl.name)
		    ret = planes.HideSomePlanes(plane_names, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.hide_planes instead.", DeprecationWarning)

def IdentifiedPlanes(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_planes` instead.


	This function collects identified planes for a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific identified plane for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    identified_planes = planes.IdentifiedPlanes(window_name)
		    for pl in identified_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_planes instead.", DeprecationWarning)

def IdentifyPlane(plane_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.identify` instead.


	This function identifies an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str
		Name of the window in which the plane will be identified. If optional argument "window_name" is absent then plane will be identified in all windows.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    window_name = "MetaPost"
		    ret = planes.IdentifyPlane(plane_name, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.identify instead.", DeprecationWarning)

def IdentifySomePlanes(plane_names: object, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.identify_planes` instead.


	This function allows the user to identify some specific planes specified by their names.

	Parameters
	----------
	plane_names : object
		Names of the planes.

	window_name : str, optional
		Name of the window in which the plane will be identified. If optional argument "window_name" is absent then plane will be identified in all windows.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    plane_names = list()
		    all_planes = planes.Planes()
		    for pl in all_planes:
		        plane_names.append(pl.name)
		    ret = planes.IdentifySomePlanes(plane_names, window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.identify_planes instead.", DeprecationWarning)

def IsPlane(plane: object) -> int:

	"""

	This function checks whether an object is of class Plane.

	Parameters
	----------
	plane : object
		Any given object.

	Returns
	-------
	int
		It returns an integer, 1 if object is of class Plane, or 0 if object is not of class Plane.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import models
		from meta import utils
		
		
		def main():
		    models.CollectNewEntitiesStart()
		    # create new entities
		    utils.MetaCommand("plane new default xy")
		    utils.MetaCommand("plane new default yz")
		
		    all_entities = models.CollectNewEntitiesEnd()
		    for ent in all_entities:
		        if planes.IsPlane(ent):
		            pl = ent
		            print("This is an object of class Plane.")
		            print(pl.name, pl.clip_type)
		            print(pl.origin[0], pl.origin[1], pl.origin[2])
		            print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		            print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsPlaneIdentified(plane_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.is_identified` instead.


	This function checks if an existing plane is identfied on a specified window.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 if the plane is identified, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    window_name = "MetaPost"
		
		    identified = planes.IsPlaneIdentified(plane_name, window_name)
		    print(identified)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.is_identified instead.", DeprecationWarning)

def IsPlaneVisible(plane_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.is_visible` instead.


	This function gets visibility of an existing plane on a specified window.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 if the plane is visible, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    window_name = "MetaPost"
		
		    visible = planes.IsPlaneVisible(plane_name, window_name)
		    print(visible)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.is_visible instead.", DeprecationWarning)

def NamesOfAllPlanes() -> object:

	"""

	This function get names of all currently existing planes.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of an existing plane.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    all_planes = planes.NamesOfAllPlanes()
		    for plane_name in all_planes:
		        print(plane_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfVisiblePlanes(window_name: str) -> object:

	"""

	This function get names of all existing visible planes.

	Parameters
	----------
	window_name : str, optional
		Name of the window. If "window_name" is absent then this function will return the name of the plane if it is visible at least in one window.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of an existing visible plane.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    visible_planes = planes.NamesOfVisiblePlanes(window_name)
		    for plane_name in visible_planes:
		        print(plane_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NormalVectorOfPlane(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_normal_vector` instead.


	This function calculates the normal vector (X, Y, Z) of an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	Returns
	-------
	object
		Upon success, it returns a list with 3 members referring to the X, Y and Z coordinates of the normal vector of the specified plane.
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_YZ"
		    normal_vector = planes.NormalVectorOfPlane(plane_name)
		    if len(normal_vector):
		        xnorm = normal_vector[0]  # X coordinate of normal vector
		        ynorm = normal_vector[1]  # Y coordinate of normal_vector
		        znorm = normal_vector[2]  # Z coordinate of normal_vector
		        print(xnorm, ynorm, znorm)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_normal_vector instead.", DeprecationWarning)

def OriginOfPlane(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_origin` instead.


	This function calculates the origin (X, Y, Z) of an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	Returns
	-------
	object
		Upon success, it returns a list with 3 members referring to the X, Y and Z coordinates of the origin of the specified plane.
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    origin = planes.OriginOfPlane(plane_name)
		    if len(origin):
		        xorig = origin[0]  # X coordinate of origin
		        yorig = origin[1]  # Y coordinate of origin
		        zorig = origin[2]  # Z coordinate of origin
		        print(xorig, yorig, zorig)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_origin instead.", DeprecationWarning)

def Planes() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_planes` instead.


	This function collects all planes.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific plane.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    all_planes = planes.Planes()
		    for pl in all_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_planes instead.", DeprecationWarning)

def PlanesListToDict(list_planes: object) -> object:

	"""

	This function constructs a dictionary from a given list with members of class Plane.

	Parameters
	----------
	list_planes : object
		List with members of class Plane.

	Returns
	-------
	object
		It returns a dictionary whose key is the name of the plane and value is the corresponding plane object of class Plane.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    all_planes = planes.Planes()
		    dict_planes = planes.PlanesListToDict(all_planes)
		    for plane_name, pl in dict_planes.items():
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReportNewPlanes() -> object:

	"""

	This function collects the newly created planes from the last call of script function meta.planes.CollectNewPlanesStart(). This function should be preceded by a corresponding call to script function meta.planes.CollectNewPlanesStart() and should be followed by a corresponding call to script function meta.planes.CollectNewPlanesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific newly created plane.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import utils
		
		
		def main():
		    planes.CollectNewPlanesStart()
		
		    # create new planes
		    utils.MetaCommand("plane new default xy")
		    utils.MetaCommand("plane new default yz")
		
		    new_planes = planes.ReportNewPlanes()
		    for pl in new_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		    planes.CollectNewPlanesEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetColorOfPlane(plane_name: str, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_color` instead.


	This function sets color of a given plane.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	red : int
		Red color component value.

	green : int
		Green color component value.

	blue : int
		Blue color component value.

	alpha : int
		Alpha color component value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "Plane1"
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = planes.SetColorOfPlane(plane_name, red, green, blue, alpha)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_color instead.", DeprecationWarning)

def SetSettingsOfAllPlanes(plane_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.set_planes_settings` instead.


	This function control settings of all planes.

	Parameters
	----------
	plane_settings : object
		Argument 'plane_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6').
		The names of the plane settings and their possible values are:
		- 'toggleopts_auto': Auto Cut Geometry (0,1)
		- 'toggleopts_clip': Clip Geometry by Plane (0,1)
		- 'toggleopts_deform': Section deform (0,1) 'toggleopts_hidden': Hidden section visibility (0,1)
		- 'toggleopts_pcolor': Get Part color (0,1) 'toggleopts_pcolor': Project Section on Plane (0,1)
		- 'toggleopts_sectionclip': Clip Geometry by Section (0,1)
		- 'toggleopts_showmesh': Show Mesh (0,1)
		- 'toggleopts_slice': Cut Slice (0,1)
		- 'toggleopts_stateauto': Auto Cut Geometry when load state changes (0,1)
		- 'toggleopts_thickshells': Follow thich shells style (0,1)
		- 'toggleopts_transp': Plane Transparency (0,1)
		- 'toggleopts_undeformcut': Cut undeformed Geometry (0,1)
		- 'options_cut': Cut ('all', 'autovisible', 'visible')
		- 'options_draw2plane': Section drawn in Plane (0,1)
		- 'options_follow': Plane Follow Node ('normal', 'orig', 'perpendicular')
		- 'options_fringe': Fringe Options ('enable', 'disable', 'lock', 'unlock', 'cplot', 'nplot', 'vplot', 'elemdata', 'onelement', 'onnode', 'unode', 'vnode', 'wnode', 'dnode', 'follow')
		- 'options_grid': Grid Options (0,1)
		- 'options_lock2vis': Cut only visible Parts (0,1)
		- 'options_offset': Plane Offset Value (float value)
		- 'options_onlysection': Draw only Section (0,1)
		- 'options_scale': Plane Scale factor (float value)
		- 'options_sectioncolor': Set section color ('auto', 'plane', 'pid', 'mid', 'model')
		- 'options_slicewidth': Plane Slice Width (float value)
		- 'options_solid': Solid Cut Options ('both', 'inside', 'skin')
		- 'options_style': Plane Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_undeformstyle': Plane Undeform Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_width': Plane Line Width (float value)

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_settings = list()
		    plane_settings.append("toggleopts_stateauto,1")
		    plane_settings.append("toggleopts_undeformcut,1")
		    plane_settings.append("options_width,6")
		    ret = planes.SetSettingsOfAllPlanes(plane_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.set_planes_settings instead.", DeprecationWarning)

def SetSettingsOfPlane(plane_name: str, plane_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_settings` instead.


	This function controls settings of a given plane.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	plane_settings : object
		Argument 'plane_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6').
		The names of the plane settings and their possible values are:
		- 'toggleopts_auto': Auto Cut Geometry (0,1)
		- 'toggleopts_clip': Clip Geometry by Plane (0,1)
		- 'toggleopts_deform': Section deform (0,1) 'toggleopts_hidden': Hidden section visibility (0,1)
		- 'toggleopts_pcolor': Get Part color (0,1) 'toggleopts_pcolor': Project Section on Plane (0,1)
		- 'toggleopts_sectionclip': Clip Geometry by Section (0,1)
		- 'toggleopts_showmesh': Show Mesh (0,1)
		- 'toggleopts_slice': Cut Slice (0,1)
		- 'toggleopts_stateauto': Auto Cut Geometry when load state changes (0,1)
		- 'toggleopts_thickshells': Follow thich shells style (0,1)
		- 'toggleopts_transp': Plane Transparency (0,1)
		- 'toggleopts_undeformcut': Cut undeformed Geometry (0,1)
		- 'options_cut': Cut ('all', 'autovisible', 'visible')
		- 'options_draw2plane': Section drawn in Plane (0,1)
		- 'options_follow': Plane Follow Node ('normal', 'orig', 'perpendicular')
		- 'options_fringe': Fringe Options ('enable', 'disable', 'lock', 'unlock', 'cplot', 'nplot', 'vplot', 'elemdata', 'onelement', 'onnode', 'unode', 'vnode', 'wnode', 'dnode', 'follow')
		- 'options_grid': Grid Options (0,1)
		- 'options_lock2vis': Cut only visible Parts (0,1)
		- 'options_offset': Plane Offset Value (float value)
		- 'options_onlysection': Draw only Section (0,1)
		- 'options_scale': Plane Scale factor (float value)
		- 'options_sectioncolor': Set section color ('auto', 'plane', 'pid', 'mid', 'model')
		- 'options_slicewidth': Plane Slice Width (float value)
		- 'options_solid': Solid Cut Options ('both', 'inside', 'skin')
		- 'options_style': Plane Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_undeformstyle': Plane Undeform Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_width': Plane Line Width (float value)

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    plane_settings = list()
		    plane_settings.append("toggleopts_stateauto,1")
		    plane_settings.append("toggleopts_undeformcut,1")
		    plane_settings.append("options_width,6")
		    plane_settings.append("options_style,dashdotline")
		    ret = planes.SetSettingsOfPlane(plane_name, plane_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_settings instead.", DeprecationWarning)

def ShowPlane(plane_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.show` instead.


	This function make visible an existing plane specified by its name.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If "window_name" is absent then plane will be shown in all windows.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_YZ"
		    window_name = "MetaPost"
		    planes.ShowPlane(plane_name, window_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.show instead.", DeprecationWarning)

def ShowSomePlanes(plane_names: object, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.show_planes` instead.


	This function allows the user to show some specific planes specified by their names.

	Parameters
	----------
	plane_names : object
		Names of the planes.

	window_name : str, optional
		Name of the window. If "window_name" is absent then plane will be shown in all windows.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    plane_names = list()
		    all_planes = planes.Planes()
		    for pl in all_planes:
		        plane_names.append(pl.name)
		        planes.ShowSomePlanes(plane_names, window_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.show_planes instead.", DeprecationWarning)

def UpdatePlane(plane: object) -> object:

	"""

	This function updates the data of the given plane object. Update is based in the field "name" of the given plane object.

	Parameters
	----------
	plane : object
		Object of class Plane.

	Returns
	-------
	object
		Upon success, it returns the new updated plane object.
		Else, None is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import utils
		
		
		def main():
		    collected_planes = planes.Planes()
		    if len(collected_planes) > 0:
		        pl = collected_planes[0]
		    # commands which alter the data of the plane struct
		    utils.MetaCommand(
		        "plane edit perpendicular 0.780869/0.000000/-0.624695 DEFAULT_PLANE_XY "
		    )
		
		    pl = planes.UpdatePlane(pl)
		    if pl:  # Update OK
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		    else:  # Update FAILED
		        print("This is not a valid plane struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisiblePlanes(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_planes` instead.


	This function collects visible planes for a given window. This function works for the active page.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific visible plane for the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    window_name = "MetaPost"
		    visible_planes = planes.VisiblePlanes(window_name)
		    for pl in visible_planes:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_planes instead.", DeprecationWarning)

def PartsOfPlane(plane_name: str, window_name: str, model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_parts` instead.


	This function collects the parts of a model which a plane cuts through.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	window_name : str
		Name of the window.

	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Part referring to one specific part of a model which a plane cuts through.
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
		from meta import planes
		
		
		def main():
		    plane_name = "DEFAULT_PLANE_XY"
		    window_name = "MetaPost"
		    model_id = 0
		    plane_parts = planes.PartsOfPlane(plane_name, window_name, model_id)
		    for p in plane_parts:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_parts instead.", DeprecationWarning)

def AreaOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_area` instead.


	This function calculates the area of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the area of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    area = planes.AreaOfPlane(all_resultsets[1], plane_name)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_area instead.", DeprecationWarning)

def AreaIntegralOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_area_integral` instead.


	This function calculates the area integral of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the area integral of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    area = planes.AreaIntegralOfPlane(all_resultsets[1], plane_name)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_area_integral instead.", DeprecationWarning)

def AreaWeightedAverageOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_area_weighted_average` instead.


	This function calculates the area integral of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the area integral of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    area = planes.AreaWeightedAverageOfPlane(all_resultsets[1], plane_name)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_area_weighted_average instead.", DeprecationWarning)

def VolumetricFlowOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the volumetric flow rate of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    rate = planes.VolumetricFlowOfPlane(all_resultsets[1], plane_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_mass_flow` instead.


	This function calculates the mass flow rate of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the mass flow rate of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    rate = planes.MassFlowOfPlane(all_resultsets[1], plane_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_mass_weighted_average` instead.


	This function calculates the mass weighted average of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the weighted average masss flow rate of the specified plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    rate = planes.MassWeightedAverageOfPlane(all_resultsets[1], plane_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_mass_weighted_average instead.", DeprecationWarning)

def UniformityIndexOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_uniformity_index` instead.


	This function calculates the uniformity index of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value as the result of the calculated uniformity index of the plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    rate = planes.UniformityIndexOfPlane(all_resultsets[1], plane_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_uniformity_index instead.", DeprecationWarning)

def VectorUniformityIndexOfPlane(result: object, plane_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of a plane with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	plane_name : str
		Name of the plane.

	window_name : str, optional
		Name of the window.

	Returns
	-------
	float
		It returns a float value as the result of the calculated vector uniformity index of the plane.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    plane_name = "DEFAULT_PLANE_XY"
		
		    rate = planes.VectorUniformityIndexOfPlane(all_resultsets[1], plane_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_vector_uniformity_index instead.", DeprecationWarning)

def SetAttributeOfPlane(plane_name: str, attrib_name: str, attrib_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	plane_name : str
		The name of the plane.

	attrib_name : str
		The name of the attribute.

	attrib_value : object
		Value of the attribute. It can be either a number or a string.

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
		from meta import planes
		
		
		def main():
		    plane_name = "plane"
		
		    name = "plane_attr"
		    val = "val"
		    value = planes.SetAttributeOfPlane(plane_name, name, val)
		    print(value)
		    # or
		    name = "plane_num_attr"
		    val = 12.3
		    attribute_type = "numerical"
		    value = planes.SetAttributeOfPlane(plane_name, name, val, attribute_type)
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.set_attribute instead.", DeprecationWarning)

def AttributeOfPlane(plane_name: str, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	plane_name : str
		The name of the plane

	attrib_name : str
		The name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "plane"
		    name = "Clip"
		    value = planes.AttributeOfPlane(plane_name, name)
		    print("Value: " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_attributes instead.", DeprecationWarning)

def AttributesOfPlanes(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_attributes` instead.


	This function collects all attributes of a given plane

	Parameters
	----------
	plane_name : str
		The name of the plane

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
		from meta import planes
		
		
		def main():
		    plane_name = "plane"
		    all_attributes = planes.AttributesOfPlane(plane_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_attributes instead.", DeprecationWarning)

def SettingsOfPlane(plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.get_settings` instead.


	This function displays the settings of a given plane.

	Parameters
	----------
	plane_name : str
		Name of the plane

	Returns
	-------
	object
		It returns a list with the settings of the given plane. Each member of the list is a string which contains as strings separated by comma the name and the value of the setting.  
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_name = "my_plane"
		    settings = planes.SettingsOfPlane(plane_name)
		    print(settings)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.get_settings instead.", DeprecationWarning)

def IdentifyPlanesReset(plane_names: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.reset_identify_planes` instead.


	This function allows the user to reset the identification of all or specific planes. It can be called with two different ways. The one is with lists of plane names, and the other is with plane_names = 'all'.

	Parameters
	----------
	plane_names : object
		List with names of the planes as strings, or string 'all'

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    plane_names = ["plane", "plane1", "plane2"]
		    # or
		    # plane_names = 'all'
		    planes.IdentifyPlanesReset(plane_names)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.reset_identify_planes instead.", DeprecationWarning)

class Plane():

	"""

	Class for planes.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    if pl:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()
		# method: create_section
		# PYTHON script
		import meta
		from meta import planes
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    sec = pl.create_section(m)
		    if sec:
		        print(sec.name, sec.creation_type, sec.sum_point, sec.coord_system)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    ret = pl.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_area(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    name = "MetaPost"
		    page_id = 0
		    w = windows.Window(name, page_id)
		    val = pl.get_area_integral(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_area_weighted_average(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    color = pl.get_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_boundary
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    b = boundaries.Boundary(id=1, second_id=10, model_id=0, type=constants.SPC)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_distance_from_boundary(b, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_element
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import elements
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    e = elements.Element(id=12387, second_id=-1, model_id=0, type=constants.SOLID)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_distance_from_element(e, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_group
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import groups
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    g = groups.Group(name="group1", model_id=0)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_distance_from_group(g, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_node
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import nodes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    n = nodes.Node(id=100, model_id=0)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_distance_from_node(n, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_distance_from_part
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import parts
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    p = parts.Part(id=2, model_id=0, type=constants.PSOLID)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_distance_from_part(p, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_edge_vector
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    edge_vector = pl.get_edge_vector()
		    print(edge_vector)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_boundary
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    b = boundaries.Boundary(id=1, second_id=10, model_id=0, type=constants.SPC)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_elongation_from_boundary(b, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_element
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import elements
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    e = elements.Element(id=12387, second_id=-1, model_id=0, type=constants.SOLID)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_elongation_from_element(e, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_group
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import groups
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    g = groups.Group(name="group1", model_id=0)
		    res = results.CurrentResultset(model_id)
		
		    val = pl.get_elongation_from_group(g, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_node
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import nodes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    n = nodes.Node(id=100, model_id=0)
		    res = results.CurrentResultset(model_id)
		    val = pl.get_elongation_from_node(n, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elongation_from_part
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import parts
		from meta import constants
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    p = parts.Part(id=2, model_id=0, type=constants.PSOLID)
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    val = pl.get_elongation_from_part(p, res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import planes
		from meta import results
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_mass_flow(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_mass_weighted_average(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_normal_vector
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    normal_vector = pl.get_normal_vector()
		    print(normal_vector)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_origin
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    origin = pl.get_origin()
		    print(origin)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    plane_parts = pl.get_parts(w, m)
		    for p in plane_parts:
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
		# method: get_settings
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    settings = pl.get_settings()
		    print(settings)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_uniformity_index(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_vector_uniformity_index
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_vector_uniformity_index(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		from meta import models
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    m = models.Model(0)
		    res = m.get_current_resultset()
		    w = windows.Window(name="MetaPost", page_id=0)
		    val = pl.get_volumetric_flow(res, w)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = pl.hide()
		    # ret = pl.hide(window = w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = pl.show()
		    # ret = pl.show(window = w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: identify
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = pl.identify()
		    # ret = pl.identify(window = w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_identified
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = pl.is_identified(window=w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_visible
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    w = windows.Window(name="MetaPost", page_id=0)
		    ret = pl.is_visible(window=w)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import planes
		from meta import windows
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    col = windows.Color(r=0, g=255, b=255, a=255)
		    ret = pl.set_color(col)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_edge_vector
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    vec = [-0.91758, -0.396854, -0.0235381]
		    ret = pl.set_edge_vector(vec)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_normal_vector
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    vec = [-0.284893, 0.615106, 0.735173]
		    ret = pl.set_normal_vector(vec)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_origin
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    orig = [102.3, 25.6, 30.8]
		    ret = pl.set_origin(orig)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    settings = {"toggleopts_auto": "1"}
		    ret = pl.set_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = pl.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_name = 'attr'
		    # attribute_type = 'numerical'
		    # attribute_value = 11.2
		    # ret = pl.set_attribute('attr', 'numerical', 11.2)
		    print(ret)
		    attribute_name = "attr"
		    attr = pl.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attribute
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    attribute_name = "attr"
		    attribute_type = "string"
		    attribute_value = "test"
		    ret = pl.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = pl.get_attributes()
		    # attr = pl.get_attributes(attribute_name = 'attr')
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import planes
		
		
		def main():
		    pl = planes.Plane(name="plane1")
		    can_use = pl.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the plane.

	"""

	clip_type: str = None
	"""
	Clip type ('plane', 'section', 'none').

	"""

	origin: object = None
	"""
	Origin of plane.

	"""

	normal_vector: object = None
	"""
	Normal vector of plane.

	"""

	edge_vector: object = None
	"""
	Edge vector of plane.

	"""

	def get_parts(self, window: object, model: object) -> object:

		"""

		This method gets the parts of a model which the plane cuts through.


		Parameters
		----------
		window : object
			Object of type Window.

		model : object
			Object of type Model.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of type Part referring to one specific part of a model which the plane cuts through. Upon failure, an empty list is returned.

		"""


	def is_visible(self, window: object) -> bool:

		"""

		This method checks if the plane is visible in a given window. 


		Parameters
		----------
		window : object
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returnes True if plane is visible or False if plane is not visible. Upon failure, it returns False.

		"""


	def is_identified(self, window: object) -> bool:

		"""

		This method checks if the plane is identified in a window. 


		Parameters
		----------
		window : object
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returns True if plane is identified, or False if plane is not identified. Upon failure, it returns False.

		"""


	def get_origin(self) -> object:

		"""

		This method gets the origin (X, Y, Z) of the plane. 


		Returns
		-------
		object
			Upon success, it returns a list with 3 float members referring to the X, Y and Z coordinates of the origin of the plane. Upon failure, an empty list is returned.

		"""


	def get_normal_vector(self) -> object:

		"""

		This method gets the normal vector (X, Y, Z) of the plane.  


		Returns
		-------
		object
			Upon success, it returns a list with 3 float members referring to the X, Y and Z coordinates of the normal vector of the plane.  Else, an empty list is returned.

		"""


	def get_edge_vector(self) -> object:

		"""

		This method gets the edge vector (X, Y, Z) of the plane. 


		Returns
		-------
		object
			Upon success, it returns a list with 3 elements referring to the X, Y and Z coordinates of the edge vector of the plane. Upon failure, an empty list is returned.

		"""


	def get_color(self) -> object:

		"""

		This method gets the color of the plane. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the color of the plane. Upon failure, it returns None.

		"""


	def get_settings(self) -> object:

		"""

		This function gets the settings of the plane. 


		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the settings as string and as values the value of the settings as string. Upon failure, it returns an empty dictionary.

		"""


	def get_area(self, resultset: object, window: object) -> float:

		"""

		This method gets the area of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float value referring to the area of the plane. Upon failure, it returns None.

		"""


	def get_area_integral(self, resultset: object, window: object) -> float:

		"""

		This method gets the area integral of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the area integral of the plane.Upon failure, it returns None.

		"""


	def get_area_weighted_average(self, resultset: object, window: object) -> float:

		"""

		This method gets the area weighted average of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the area weighted average of the plane. Upon failure, it returns None.

		"""


	def get_volumetric_flow(self, resultset: object, window: object) -> float:

		"""

		This method gets the volumetric flow of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the volumetric flow of the plane. Upon failure, it returns None.

		"""


	def get_mass_flow(self, resultset: object, window: object) -> float:

		"""

		This method gets the mass flow of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the mass flow of the plane. Upon failure, it returns None.

		"""


	def get_mass_weighted_average(self, resultset: object, window: object) -> float:

		"""

		This method gets the mass weighted average. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the mass weighted average of the plane. Upon failure, it returns None.

		"""


	def get_uniformity_index(self, resultset: object, window: object) -> float:

		"""

		This method gets the uniformity index of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the uniformity index of the plane. Upon failure, it returns None.

		"""


	def get_vector_uniformity_index(self, resultset: object, window: object) -> float:

		"""

		This method gets the vector uniformity index of the plane. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		window : object
			Object of type Window.

		Returns
		-------
		float
			Upon success, it returns a float referring to the vector uniformity index of the plane. Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the plane. 


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is another list referring to one specific attribute of the plane. In position 0, internal lists contain a string referring to the name of the attribute.In position 1, internal lists contain a string referring to the value of the attributes.Upon failure, an empty list is returned.

		"""


	def get_distance_from_node(self, node: object, node_resultset: object) -> object:

		"""

		This method gets the distance of the plane from a given node. 


		Parameters
		----------
		node : object
			Object of type Node.

		node_resultset : object
			Object of type Result.

		Returns
		-------
		object
			Upon success, it returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_node(self, node: object, node_resultset: object) -> float:

		"""

		This method gets the elongation of the plane from a given node. 


		Parameters
		----------
		node : object
			Object of type Node.

		node_resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a list with float numbers as members  referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_element(self, element: object, element_resultset: object) -> float:

		"""

		This method gets the distance of the plane from a given element. 


		Parameters
		----------
		element : object
			Object of type Element.

		element_resultset : object
			Object of type Result.

		Returns
		-------
		float
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_element(self, element: object, element_resultset: object) -> object:

		"""

		This method gets the elongation of the plane from a given element. 


		Parameters
		----------
		element : object
			Object of type Element.

		element_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_part(self, part: object, part_resultset: object) -> object:

		"""

		This method gets the distance of the plane from a given part. 


		Parameters
		----------
		part : object
			Object of type Part.

		part_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_part(self, part: object, part_resultset: object) -> object:

		"""

		This method gets the elongation of the plane from the given part. 


		Parameters
		----------
		part : object
			Object of type Part.

		part_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_group(self, group: object, group_resultset: object) -> object:

		"""

		This method gets the distance of the plane from a given group. 


		Parameters
		----------
		group : object
			Object of type Group.

		group_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_group(self, group: object, group_resultset: object) -> object:

		"""

		This method gets the elongation of the plane from a given group. 


		Parameters
		----------
		group : object
			Object of type Group.

		group_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def get_distance_from_boundary(self, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the distance of the plane from a given boundary element. 


		Parameters
		----------
		boundary : object
			Object of type Boundary.

		boundary_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding distance in each direction (X, Y, Z, TOTAL).- In position 0 there is the distance in X direction.- In position 1 there is the distance in Y direction.- In position 2 there is the distance in Z direction.- In position 3 there is the TOTAL distance.Upon failure, an empty list is returned.

		"""


	def get_elongation_from_boundary(self, boundary: object, boundary_resultset: object) -> object:

		"""

		This method gets the elongation of the plane from a given boundary element. 


		Parameters
		----------
		boundary : object
			Object of type Boundary.

		boundary_resultset : object
			Object of type Result.

		Returns
		-------
		object
			It returns a list with float numbers as members referring to the corresponding elongation in each direction (X, Y, Z, TOTAL).- In position 0 there is the elongation in X direction.- In position 1 there is the elongation in Y direction.- In position 2 there is the elongation in Z direction.- In position 3 there is the TOTAL elongation.Upon failure, an empty list is returned.

		"""


	def set_color(self, color: object) -> bool:

		"""

		This method sets the color of the plane. This method works for the active page.


		Parameters
		----------
		color : object
			Object of type Color.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_origin(self, origin: object) -> bool:

		"""

		This method sets the origin (X, Y, Z) of the plane. This method works for the active page.


		Parameters
		----------
		origin : object
			Origin of the plane.
			A list with doubles: 
			[0]: X coordinate
			[1]: Y coordinate
			[2]: Z coordinate

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_normal_vector(self, normal_vector: object) -> bool:

		"""

		This method sets the normal vector (X, Y, Z) of the plane. This method works for the active page. The method normalizes the vector.


		Parameters
		----------
		normal_vector : object
			Normal vector of the plane. 
			A list with doubles:
			[0]: X component
			[1]: Y component
			[2]: Z component

		Returns
		-------
		bool
			Upon success, it returns True. Upon success, it returns False.

		"""


	def set_edge_vector(self, edge_vector: object) -> bool:

		"""

		This function sets the edge vector (X, Y, Z) of the plane. This method works for the active page. The method normalizes the vector.


		Parameters
		----------
		edge_vector : object
			Edge vector of the plane. 
			A list with doubles:
			[0]: X component
			[1]: Y component
			[2]: Z component

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_settings(self, settings: object) -> bool:

		"""

		This method sets the settings of the plane. This method works for the active page.


		Parameters
		----------
		settings : object
			Settings (key-value) of the plane.
			A dictionary with string keys and string values:
			- 'toggleopts_auto': Auto Cut Geometry (0,1)
			- 'toggleopts_clip': Clip Geometry by Plane (0,1)
			- 'toggleopts_deform': Section deform (0,1)
			- 'toggleopts_hidden': Hidden section visibility (0,1)
			- 'toggleopts_pcolor': Get Part color (0,1)  
			- 'toggleopts_pcolor': Project Section on Plane (0,1)
			- 'toggleopts_sectionclip': Clip Geometry by Section (0,1)
			- 'toggleopts_showmesh': Show Mesh (0,1)
			- 'toggleopts_slice': Cut Slice (0,1)
			- 'toggleopts_stateauto': Auto Cut Geometry when load state changes (0,1)
			- 'toggleopts_thickshells': Follow thich shells style (0,1)
			- 'toggleopts_transp': Plane Transparency (0,1)
			- 'toggleopts_undeformcut': Cut undeformed Geometry (0,1)
			- 'options_cut': Cut ('all', 'autovisible', 'visible')
			- 'options_draw2plane': Section drawn in Plane (0,1)
			- 'options_follow': Plane Follow Node ('normal', 'orig', 'perpendicular')
			- 'options_fringe': Fringe Options ('enable', 'disable', 'lock', 'unlock', 'cplot', 'nplot', 'vplot', 'elemdata', 'onelement', 'onnode', 'unode', 'vnode', 'wnode', 'dnode', 'follow')
			- 'options_grid': Grid Options (0,1)
			- 'options_lock2vis': Cut only visible Parts (0,1)
			- 'options_offset': Plane Offset Value (float value)
			- 'options_onlysection': Draw only Section (0,1)
			- 'options_scale': Plane Scale factor (float value)
			- 'options_sectioncolor': Set section color ('auto', 'plane', 'pid', 'mid', 'model')
			- 'options_slicewidth': Plane Slice Width (float value)
			- 'options_solid': Solid Cut Options ('both', 'inside', 'skin')
			- 'options_style': Plane Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
			- 'options_undeformstyle': Plane Undeform Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
			- 'options_width': Plane Line Width (float value)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the plane. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. 
			Its possible values are:
			'string': String
			'numerical': Number

		attribute_value : object
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self, window: object) -> bool:

		"""

		This method shows the plane. This method works for the active page.


		Parameters
		----------
		window : object, optional
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self, window: object) -> bool:

		"""

		This method hides the plane. This method works for the active page.


		Parameters
		----------
		window : object, optional
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def identify(self, window: object) -> bool:

		"""

		This method identifies the plane. This method works for the active page.


		Parameters
		----------
		window : object, optional
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the plane. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def create_section(self, model: object) -> object:

		"""

		This method creates a section from the plane. This method works for the active page.


		Parameters
		----------
		model : object
			Object of type Model.

		Returns
		-------
		object
			Upon success, it returns an object of type Section referring to newly created section. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Model entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

