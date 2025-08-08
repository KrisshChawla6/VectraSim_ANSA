from __future__ import annotations
from typing import *

def AreaOfIsofunction(window_name: str, model_id: int, iso_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_area` instead.


	This function calculates the area of a closed upper or closed lower isofunction of a given model for a specific window. The area is calculated for the current resultset of the model in the given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	model_id : int
		Id of the model.

	iso_name : str
		Name of the isofunction.

	Returns
	-------
	float
		Upon success, it returns as a float the area of the closed isofunction.
		Else, an invalid value of -1000 is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    model_id = 0
		    iso_name = "closed_upper"
		
		    area = isofunctions.AreaOfIsofunction(window_name, model_id, iso_name)
		    print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_area instead.", DeprecationWarning)

def ChangeValueOfIsofunction(window_name: str, iso_name: str, new_value: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_value` instead.


	This function changes the value of an isofunction of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the isofunction.

	new_value : float
		New value of the isofunction.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "isofun1"
		    new_value = 2.6
		
		    ret = isofunctions.ChangeValueOfIsofunction(window_name, iso_name, new_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_value instead.", DeprecationWarning)

def CollectNewIsofunctionsEnd() -> object:

	"""

	This function ends recording the creation of new isofunctions. This function should be preceded by a corresponding call to script function isofunctions.CollectNewIsofunctionsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific newly created isofunction.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import utils
		
		
		def main():
		    isofunctions.CollectNewIsofunctionsStart()
		
		    # create new isofunctions
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.25" 0.25')
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.31" 0.31')
		
		    new_isofunctions = isofunctions.CollectNewIsofunctionsEnd()
		    for iso in new_isofunctions:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewIsofunctionsStart() -> int:

	"""

	This function starts recording the creation of new isofunctions. This function should be followed by a corresponding call to script function isofunctions.CollectNewIsofunctionsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import utils
		
		
		def main():
		    isofunctions.CollectNewIsofunctionsStart()
		
		    # create new isofunctions
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.25" 0.25')
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.31" 0.31')
		
		    new_isofunctions = isofunctions.CollectNewIsofunctionsEnd()
		    for iso in new_isofunctions:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateClosedLowerIsofunction(window_name: str, iso_name: str, iso_type: str, iso_value: float) -> object:

	"""

	This function creates a closed lower isofunction on an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the new isofunction.

	iso_type : str
		Type of the isofunction. Possible values are:
		- 'function' : Function
		- 'xdeform' : X Deformation
		- 'ydeform' : Y Deformation
		- 'zdeform' : Z Deformation
		- 'tdeform' : Total Deformation.

	iso_value : float
		Value of the isofunction.

	Returns
	-------
	object
		Upon success, it returns an object of class Isofunction referring to the newly created isofunction.
		Else, None is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "closed_lower"
		    iso_type = "function"
		    iso_value = 0.22
		
		    iso = isofunctions.CreateClosedLowerIsofunction(
		        window_name, iso_name, iso_type, iso_value
		    )
		    if iso:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateClosedUpperIsofunction(window_name: str, iso_name: str, iso_type: str, iso_value: float) -> object:

	"""

	This function creates a closed upper isofunction.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the new isofunction.

	iso_type : str
		Type of the isofunction. Possible values are:
		- 'function' : Function
		- 'xdeform' : X Deformation
		- 'ydeform' : Y Deformation
		- 'zdeform' : Z Deformation
		- 'tdeform' : Total Deformation.

	iso_value : float
		Value of the new isofunction.

	Returns
	-------
	object
		Upon success, it returns an object of class Isofunction referring to the newly created isofunction.
		Else, None is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "closed_upper"
		    iso_type = "function"
		    iso_value = 0.32
		
		    iso = isofunctions.CreateClosedUpperIsofunction(
		        window_name, iso_name, iso_type, iso_value
		    )
		    if iso:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateDefaultIsofunction(window_name: str, iso_name: str, iso_type: str, iso_value: float) -> object:

	"""

	This function creates a default isofunction on an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the new isofunction.

	iso_type : str
		Type of the isofunction. Possible values are:
		- 'function' : Function
		- 'xdeform' : X Deformation
		- 'ydeform' : Y Deformation
		- 'zdeform' : Z Deformation
		- 'tdeform' : Total Deformation.

	iso_value : float
		Value of the new isofunction.

	Returns
	-------
	object
		Upon success, it returns an object of class Isofunction referring to the newly created isofunction.
		Else, None is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "new_isofun"
		    iso_type = "function"
		    iso_value = 5.4
		
		    iso = isofunctions.CreateDefaultIsofunction(
		        window_name, iso_name, iso_type, iso_value
		    )
		    if iso:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteIsofunction(window_name: str, iso_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.delete` instead.


	This function deletes the isofunction of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the isofunction.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "dnode0.05"
		
		    ret = isofunctions.DeleteIsofunction(window_name, iso_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.delete instead.", DeprecationWarning)

def HideIsofunction(window_name: str, iso_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.hide` instead.


	This function hides the isofunction of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the isofunction.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "dnode0.23"
		
		    ret = isofunctions.HideIsofunction(window_name, iso_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.hide instead.", DeprecationWarning)

def IsIsofunction(isofunction: object) -> object:

	"""

	This function checks whether an object is of class Isofunction.

	Parameters
	----------
	isofunction : object
		Any given object.

	Returns
	-------
	object
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import utils
		from meta import models
		
		
		def main():
		    models.CollectNewEntitiesStart()
		    # create new entities
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.25" 0.25')
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.31" 0.31')
		
		    all_entities = models.CollectNewEntitiesEnd()
		    for ent in all_entities:
		        if isofunctions.IsIsofunction(ent):
		            iso = ent
		            print("This is an object of class Isofunction")
		            print(
		                iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def Isofunctions() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_isofunctions` instead.


	This function collects all isofunctions of all windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific isofunction of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    all_isos = isofunctions.Isofunctions()
		    for iso in all_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_isofunctions instead.", DeprecationWarning)

def IsofunctionsByName(window_name: str, iso_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_isofunctions` instead.


	This function finds isofunctions of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Argument "iso_name" is a string expression representing the name of the isofunction, where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific isofunction of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "fun*"
		    name_isos = isofunctions.IsofunctionsByName(window_name, iso_name)
		    for iso in name_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_isofunctions instead.", DeprecationWarning)

def IsofunctionsListToDict(list_isos: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Isofunction. Key of the dictionary is the isofunction name and value is the corresponding object of type isofunction.

	Parameters
	----------
	list_isos : object
		List with objects of class Isofunction.

	Returns
	-------
	object
		It returns a dictionary whose key is the name of the isofunction and value the corresponding isofunction object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    all_isos = isofunctions.IsofunctionsOfWindow(window_name)
		
		    map_isos = isofunctions.IsofunctionsListToDict(all_isos)
		    for iso_name, iso in map_isos.items():
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsofunctionsOfOverlayRun(overlay_run_type: str, overlay_run_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_isofunctions` instead.


	This function searches for the isofunctions of an overlay run with a given type and a given id.

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
		Upon success, it returns a list where each member of the list is an object of class Isofunction referring to one isofunction of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_isofunctions = isofunctions.IsofunctionsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for iso in overlay_run_isofunctions:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_isofunctions instead.", DeprecationWarning)

def IsofunctionsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_isofunctions` instead.


	This function collects all isofunctions of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific isofunction of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    window_isos = isofunctions.IsofunctionsOfWindow(window_name)
		    for iso in window_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_isofunctions instead.", DeprecationWarning)

def PickIsofunctions(window_name: str, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.pick_isofunctions` instead.


	This function allows the user to pick isofunctions from a window specified by its name. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	window_name : str
		Name of the window.

	message : str
		Message displayed to the user when the function is called.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific picked isofunction of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    message = "Select Isofunctions and press Enter when you are ready"
		    picked_isos = isofunctions.PickIsofunctions(window_name, message)
		    for iso in picked_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.pick_isofunctions instead.", DeprecationWarning)

def ReportNewIsofunctions() -> object:

	"""

	This function collects the newly created isofunctions from the last call of script function isofunctions.CollectNewIsofunctionsStart(). This function should be preceded by a corresponding call to script function isofunctions.CollectNewIsofunctionsStart() and should be followed by a corresponding call to script function isofunctions.CollectNewIsofunctionsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific newly created isofunction.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import utils
		
		
		def main():
		    isofunctions.CollectNewIsofunctionsStart()
		
		    # create new isofunctions
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.25" 0.25')
		    utils.MetaCommand('isofun new window "MetaPost" function "fun0.31" 0.31')
		
		    new_isofunctions = isofunctions.ReportNewIsofunctions()
		    for iso in new_isofunctions:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		    isofunctions.CollectNewIsofunctionsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetSettingsOfAllIsofunctions(window_name: str, iso_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_isofunctions_settings` instead.


	This function controls settings of all isofunctions for a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_settings : object
		Argument "iso_settings" is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. 'options_width,6').
		A list of settings and possible values is:
		- 'options_follow': Auto Cut Geometry (0,1)
		- 'options_fringe': Iso Fringe Options ('enable', 'disable', 'lock', 'unlock')
		- 'options_linewidth': Iso Line Width (float value)
		- 'options_solid': Solid cut options ('both', 'inside')
		- 'options_value': Show/Hide Iso Value (1, 0)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_settings = ["options_follow,1", "options_linewidth,5"]
		    ret = isofunctions.SetSettingsOfAllIsofunctions(window_name, iso_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_isofunctions_settings instead.", DeprecationWarning)

def SetSettingsOfIsofunction(window_name: str, iso_name: str, iso_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.set_settings` instead.


	This function controls settings of a given isofunction.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the isofunction.

	iso_settings : object
		Argument 'iso_settings' is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. 'options_width,6').
		A list of settings and possible values is:
		- 'options_follow': Auto Cut Geometry (0,1)
		- 'options_fringe': Iso Fringe Options ('enable', 'disable', 'lock', 'unlock')
		- 'options_linewidth': Iso Line Width (float value)
		- 'options_solid': Solid cut options ('both', 'inside')
		- 'options_value': Show/Hide Iso Value (1, 0)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "closed_upper"
		    iso_settings = ["options_follow,1", "options_linewidth,1"]
		    ret = isofunctions.SetSettingsOfIsofunction(window_name, iso_name, iso_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.set_settings instead.", DeprecationWarning)

def ShowIsofunction(window_name: str, iso_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.show` instead.


	This function makes visible the isofunction of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	iso_name : str
		Name of the isofunction.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "fun0.31"
		
		    ret = isofunctions.ShowIsofunction(window_name, iso_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.show instead.", DeprecationWarning)

def UpdateIsofunction(isofunction: object) -> object:

	"""

	This function updates the data of the given isofunction object. Update is based in the fields "name" and "window_name" of the given isofunction object.

	Parameters
	----------
	isofunction : object
		The isofunction to be updated.

	Returns
	-------
	object
		Upon success, it returns the new updated object of class Isofunction.
		Else, None is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "fun"
		
		    collected_isos = isofunctions.IsofunctionsByName(window_name, iso_name)
		    if len(collected_isos) > 0:
		        iso = collected_isos[0]
		
		        # commands which alter the data of the isofunction struct
		        utils.MetaCommand(
		            "isofun edit value window " + window_name + " " + iso_name + " 0.05"
		        )
		
		        iso = isofunctions.UpdateIsofunction(iso)
		        if iso:  # Update OK
		            print(
		                iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id
		            )
		        else:  # Update FAILED
		            print("This is not a valid isofunction object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleIsofunctions() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_isofunctions` instead.


	This function collects visible isofunctions of all windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific visible isofunction of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    visible_isos = isofunctions.VisibleIsofunctions()
		    for iso in visible_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_isofunctions instead.", DeprecationWarning)

def VisibleIsofunctionsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_isofunctions` instead.


	This function collects visible isofunctions of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Isofunction referring to one specific visible isofunction of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	isofunctions.IsoFunction

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    visible_isos = isofunctions.VisibleIsofunctionsOfWindow(window_name)
		    for iso in visible_isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_isofunctions instead.", DeprecationWarning)

def VolumeOfIsofunction(window_name: str, model_id: int, iso_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_volume` instead.


	This function calculates the volume of a closed upper or closed lower isofunction of a given model for a specific window.

	Parameters
	----------
	window_name : str
		Name of the window.

	model_id : int
		Id of the model.

	iso_name : str
		Name of the isofunction.

	Returns
	-------
	float
		Upon success, it returns as a float the volume of the closed isofunction.
		Else, an invalid value of -1000 is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    model_id = 0
		    iso_name = "closed_upper"
		
		    volume = isofunctions.VolumeOfIsofunction(window_name, model_id, iso_name)
		    print(volume)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_volume instead.", DeprecationWarning)

def VectorUniformityIndexOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_vector_uniformity_index` instead.


	This function calculates the vector uniformity index of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active windowName of the group.

	Returns
	-------
	float
		It returns a float value as the result of the calculated vector uniformity index of the isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    iso_name = "MyIso"
		
		    index = isofunctions.VectorUniformityIndexOfIsofunction(all_resultsets[1], iso_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_vector_uniformity_index instead.", DeprecationWarning)

def AreaIntegralOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_area_integral` instead.


	This function calculates the area integral of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
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
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if len(all_resultsets):
		        iso_name = "MyIso"
		        window_name = "MetaPost"
		        area = isofunctions.AreaIntegralOfIsofunction(
		            all_resultsets[1], iso_name, window_name
		        )
		        print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_area_integral instead.", DeprecationWarning)

def AreaWeightedAverageOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_area_weighted_average` instead.


	This function calculates the area integral of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the area integral of the specified isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if all_resultsets:
		        iso_name = "MyIso"
		        window_name = "MetaPost"
		        area = isofunctions.AreaWeightedAverageOfIsofunction(
		            all_resultsets[1], iso_name, window_name
		        )
		        print(area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_area_weighted_average instead.", DeprecationWarning)

def VolumetricFlowOfIsofunction(result: object, iso_name: str, window_name: Callable) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_volumetric_flow` instead.


	This function calculates the volumetric flow rate of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : Callable, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the volumetric flow rate of the specified isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    if len(all_resultsets):
		        iso_name = "MyIso"
		        window_name = "MetaPost"
		        rate = isofunctions.VolumetricFlowOfIsofunction(
		            all_resultsets[1], iso_name, window_name
		        )
		        print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_volumetric_flow instead.", DeprecationWarning)

def MassFlowOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_mass_flow` instead.


	This function calculates the mass flow rate of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the mass flow rate of the specified isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    iso_name = "MyIso"
		
		    rate = isofunctions.MassFlowOfIsofunction(all_resultsets[1], iso_name)
		    print(rate)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_mass_flow instead.", DeprecationWarning)

def MassWeightedAverageOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_mass_weighted_average` instead.


	This function calculates the mass weighted average of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value referring to the weighted average masss flow rate of the specified isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    iso_name = "MyIso"
		
		    av = isofunctions.MassWeightedAverageOfIsofunction(all_resultsets[1], iso_name)
		    print(an)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_mass_weighted_average instead.", DeprecationWarning)

def UniformityIndexOfIsofunction(result: object, iso_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_uniformity_index` instead.


	This function calculates the uniformity index of an isofunction with specific name.

	Parameters
	----------
	result : object
		An object of class Result that refers to a Resultset of the model.

	iso_name : str
		Name of the isofunction.

	window_name : str, optional
		Name of the window. If optional argument "window_name" is absent then the result will be calculated for the active window

	Returns
	-------
	float
		It returns a float value as the result of the calculated uniformity index of the isofunction.
		Upon failure, 0 will be returned.

	See Also
	--------
	results.Result

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    iso_name = "MyIso"
		
		    index = isofunctions.UniformityIndexOfIsofunction(all_resultsets[1], iso_name)
		    print(index)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_uniformity_index instead.", DeprecationWarning)

def AttributesOfIsofunction(window_name: str, iso_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_attributes` instead.


	This function collects all attributes of a given isofunction

	Parameters
	----------
	window_name : str
		Name of the window

	iso_name : str
		Name of the isofunction

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
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "test"
		    all_attributes = isofunctions.AttributesOfIsofunction(window_name, iso_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_attributes instead.", DeprecationWarning)

def AttributeOfIsofunction(window_name: str, iso_name: str, attribute_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	iso_name : str
		The name of the isofunction

	attribute_name : str
		The name of the attributes

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
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "test"
		    name = "Value"
		
		    value = isofunctions.AttributeOfIsofunction(window_name, iso_name, name)
		    print("Name: " + name + "\\tValue: " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.get_attributes instead.", DeprecationWarning)

def SetAttributeOfIsofunction(window_name: str, iso_name: str, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.isofunctions.IsoFunction.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given isofunction. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	iso_name : str
		The name of the isofunction.

	attribute_name : str
		The name of the attribute.

	attribute_value : object
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
		from meta import isofunctions
		
		
		def main():
		    window_name = "MetaPost"
		    iso_name = "test"
		
		    name = "iso_attr"
		    val = "val"
		    value = isofunctions.SetAttributeOfIsofunction(window_name, iso_name, name, val)
		    print(value)
		    # or
		    name = "iso_num_attr"
		    val = 123
		    attribute_type = "numerical"
		    value = isofunctions.SetAttributeOfIsofunction(
		        window_name, iso_name, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.isofunctions.IsoFunction.set_attribute instead.", DeprecationWarning)

class IsoFunction():

	"""

	Class for isofunctions.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    if iso:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    ret = iso.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_area(model)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_integral
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    res = results.CurrentResultset(0)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_area_integral(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_area_weighted_average
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_area_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_attributes()
		    # val = iso.get_attributes( attribute_name = 'Value' )
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_flow
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_mass_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_mass_weighted_average
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_mass_weighted_average(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    pg = iso.get_page()
		    if pg:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parts
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    iso_parts = iso.get_parts()
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
		# method: get_uniformity_index
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_uniformity_index(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volume
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import models
		
		
		def main():
		    model = models.Model(0)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_volume(model)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_volumetric_flow
		# PYTHON script
		import meta
		from meta import isofunctions
		from meta import results
		
		
		def main():
		    model_id = 0
		    res = results.CurrentResultset(model_id)
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    val = iso.get_volumetric_flow(res)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    w = iso.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    ret = iso.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    ret = iso.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    attribute_name = "test"
		    attribute_type = "numerical"
		    attribute_value = 30
		    ret = iso.set_attribute(attribute_name, attribute_type, attribute_value)
		    # attribute_type = 'string'
		    # attribute_value = 'my_atrribute'
		    # ret = iso.set_attribute( attribute_name = "test", attribute_type = "string",  attribute_value = 'my_atrribute' )
		    print(ret)
		    attribute_name = "test"
		    val = iso.get_attributes(attribute_name)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    settings = {"options_fringe", "enable"}
		    iso.set_settings(settings)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_value
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    value = 0.5
		    ret = iso.set_value(value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import isofunctions
		
		
		def main():
		    iso = isofunctions.IsoFunction(name="iso1", window_name="MetaPost", page_id=0)
		    can_use = iso.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the isofunction.

	"""

	window_name: str = None
	"""
	Name of the window of the isofunction.

	"""

	type: str = None
	"""
	Type of the isofunction ('function', 'xdeform', 'ydeform', 'zdeform', 'tdeform').

	"""

	value: float = None
	"""
	Value of the isofunction.

	"""

	visible: int = None
	"""
	- 1 is isofunction is visible
	- 0 if it is not visible

	"""

	page_id: int = None
	"""
	Id of the page of the isofunction.

	"""

	def get_window(self) -> object:

		"""

		This method gets the window of the isofunction. 


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the isofunction. Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the isofunction. 


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the isofunction. Upon failure, it returns None.

		"""


	def get_parts(self) -> object:

		"""

		This method gets the parts of the isofunction. 


		Returns
		-------
		object
			Upon success, it returns a list where each member is an object of type Part and refers to a part that comprises the isofunction.Upon failure, an empty list is returned.

		"""


	def get_area(self, model: object) -> float:

		"""

		This method gets the area of a closed upper or closed lower isofunction of a given model. The area is calculated for the current resultset of the model in the isofunction's window.


		Parameters
		----------
		model : object
			Object of type Model.

		Returns
		-------
		float
			Upon success, it returns a float referring to the area of the closed isofunction.Upon failure, it returns None.

		"""


	def get_volume(self, model: object) -> float:

		"""

		This method gets the volume of a closed upper or closed lower isofunction of a given model. 


		Parameters
		----------
		model : object
			Object of type Model.

		Returns
		-------
		float
			Upon success, it returns a float referring to the volume of the closed isofunction. Upon failure, it returns None.

		"""


	def get_area_integral(self, resultset: object) -> float:

		"""

		This method gets the area integral of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float value referring to the area integral of the isofunction. Upon failure, it returns None.

		"""


	def get_area_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the area weighted average of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float referring to the area weighted average of the isofunction.  Upon failure, it returns None.

		"""


	def get_volumetric_flow(self, resultset: object) -> float:

		"""

		This method gets the volumetric flow of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float referring to the volumetric flow of the isofunction. Upon failure, it returns None.

		"""


	def get_mass_flow(self, resultset: object) -> float:

		"""

		This method gets the mass flow of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float referring to the mass flow of the isofunction. Upon failure, it returns None.

		"""


	def get_mass_weighted_average(self, resultset: object) -> float:

		"""

		This method gets the mass weighted average of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float referring to the mass weighted average of the isofunction. Upon failure, it returns None.

		"""


	def get_uniformity_index(self, resultset: object) -> float:

		"""

		This method gets the uniformity index of the isofunction. 


		Parameters
		----------
		resultset : object
			Object of type Result.

		Returns
		-------
		float
			Upon success, it returns a float referring to the uniformity index of the isofunction. Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the isofunction. 


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def set_value(self, value: float) -> bool:

		"""

		This method sets the value of the isofunction.


		Parameters
		----------
		value : float
			New value of the isofunction.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_settings(self, settings: object) -> bool:

		"""

		This method sets the settings of the isofunction.


		Parameters
		----------
		settings : object
			Settings (key-value) of the isofunction.
			A dictionary with string keys and string values:
			- 'options_follow': Auto Cut Geometry (0,1)
			- 'options_fringe': Iso Fringe Options ('enable', 'disable', 'lock', 'unlock')
			- 'options_linewidth': Iso Line Width (float value)
			- 'options_solid': Solid cut options ('both', 'inside')
			- 'options_value': Show/Hide Iso Value (1, 0)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the isofunction. If the given attribute does not exist it is automatically created and its value is set.


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


	def show(self) -> bool:

		"""

		This method shows the isofunction. 


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide(self) -> object:

		"""

		This method hides the isofunction. 


		Returns
		-------
		object
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the isofunction.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META IsoFunction entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

