from __future__ import annotations
from typing import *

def ActivateFringe(window_name: str, fringe_name: str, fringe_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.activate_fringebar` instead.


	This function makes active a fringe bar with a given name on a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	fringe_name : str
		Name of the fringe bar.

	fringe_type : str, optional
		Type of the fringe bar. Its possible values are:
		- 'scalar' (default value)
		- 'vector'.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    fringe_name = "AnimationBar"
		    fringe_type = "scalar"
		    windows.ActivateFringe(window_name, fringe_name, fringe_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.activate_fringebar instead.", DeprecationWarning)

def ActivateWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.activate` instead.


	This function makes active an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a python object of class Window referring to the corresponding active window.
		Else, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "Window1"
		    w = windows.ActivateWindow(window_name)
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.activate instead.", DeprecationWarning)

def ActiveWindow() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function searches for the active window.

	Returns
	-------
	object
		Upon success, it returns an object of class Window referring to the corresponding active window.
		Else, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    w = windows.ActiveWindow()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def ApplyView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.apply_view` instead.


	This function applies a view with a given name on a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "DEFAULT_VIEW_:_+Y+Z_(F4)"
		    ret = windows.ApplyView(window_name, view_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.apply_view instead.", DeprecationWarning)

def CollectNewWindowsEnd() -> object:

	"""

	This function ends recording the creation of new windows. This function should be preceded by a corresponding call to script function meta.windows.CollectNewWindowsStart().

	Returns
	-------
	object
		It returns a list wwhere each object of the list is an object of class Window referring to one specific newly created window.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		from meta import utils
		
		
		def main():
		    # start collecting new windows
		    windows.CollectNewWindowsStart()
		
		    # create new windows
		    utils.MetaCommand("window create Window1")
		    utils.MetaCommand("xyplot create Window2")
		
		    # end collecting new windows and return them
		    new_windows = windows.CollectNewWindowsEnd()
		
		    for w in new_windows:
		        print(w.name)
		        print(w.page_id)
		        print(w.active)
		        print(w.height)
		        print(w.width)
		        print(w.plot2d)
		        print(w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewWindowsStart() -> int:

	"""

	This function starts recording the creation of new windows. This function should be followed by a corresponding call to script function meta.windows.CollectNewWindowsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		from meta import utils
		
		
		def main():
		    # start collecting new windows
		    windows.CollectNewWindowsStart()
		
		    # create new windows
		    utils.MetaCommand("window create Window1")
		    utils.MetaCommand("xyplot create Window2")
		
		    # end collecting new windows and return them
		    new_windows = windows.CollectNewWindowsEnd()
		
		    for w in new_windows:
		        print(w.name)
		        print(w.page_id)
		        print(w.active)
		        print(w.height)
		        print(w.width)
		        print(w.plot2d)
		        print(w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectWindowEntities(window_name: str, entity_type: str) -> object:

	"""

	This function collects entities of the window specified by the given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	entity_type : str
		The type of the entities to be collected. It's possible values are:
		- 'curves': Collect curves
		- 'annotations': Collect annotations
		- 'images': Collect images
		- 'videos': Collect videos
		- 'isofunctions': Collect isofunctions

	Returns
	-------
	object
		For the given window, it returns a list with python objects of a class depending on the entity type.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "Window1"
		    entity_type = "curves"
		    collected_entities = windows.CollectWindowEntities(window_name, entity_type)
		    for c in collected_entities:
		        print(
		            c.id,
		            c.name,
		            c.plot_id,
		            c.visible,
		            c.selected,
		            c.window_name,
		            c.page_id,
		            c.command,
		            c.entity_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def ColorOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_color` instead.


	This function finds background color of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a python object of class Color with the color of the corresponding window.
		Else, None is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    color = windows.ColorOfWindow(window_name)
		    if color:
		        print(color.name, color.r, color.g, color.b, color.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_color instead.", DeprecationWarning)

def ColorsOfFringe(fringe_name: str) -> object:

	"""

	This function collects all colors of a given fringe bar.

	Parameters
	----------
	fringe_name : str
		Name of the fringebar.

	Returns
	-------
	object
		It returns a list with python objects of class Color of the corresponding colors of the given fringe bar.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    fringe_name = "AnimationBar"
		    fringe_colors = windows.ColorsOfFringe(fringe_name)
		    for color in fringe_colors:
		        print(color.name, color.r, color.g, color.b, color.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Create2DPlotWindow(window_name: str) -> object:

	"""

	This function creates a new 2D plot window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a python object of class Window referring to the newly created 2D plot window.
		Upon failure, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "Win2D"
		    w = windows.Create2DPlotWindow(window_name)
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Create3DWindow(window_name: str) -> object:

	"""

	This function creates a new 3D drawing window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a python object of class Window referring to the newly created 3D window.
		Upon failure, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "Win3D"
		    w = windows.Create3DWindow(window_name)
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.delete_view` instead.


	This function deletes a view with a given name of a window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    ret = windows.DeleteView(window_name, view_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.delete_view instead.", DeprecationWarning)

def DeleteWindow(window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.delete` instead.


	This function deletes an existing window.

	Parameters
	----------
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
		from meta import windows
		
		
		def main():
		    window_name = "Win2D"
		    ret = windows.DeleteWindow(window_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.delete instead.", DeprecationWarning)

def DisableWindow(window_name: str, active: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.disable` instead.


	This function disables an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	active : int, optional
		If optional argument "active" is equal to 1 then the current active window option will be deactivated.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    active = 1
		    ret = windows.DisableWindow(window_name, active)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.disable instead.", DeprecationWarning)

def EnableWindow(window_name: str, active: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.enable` instead.


	This function enables an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	active : int, optional
		If optional argument "active" is equal to 1 then the current active window option will be activated.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    active = 1
		    ret = windows.EnableWindow(window_name, active)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.enable instead.", DeprecationWarning)

def EnabledWindows() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function collects all the current existing enabled windows.

	Returns
	-------
	object
		It returns a list with objects of class type Window for each of the current existing enabled windows.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    enabled_windows = windows.EnabledWindows()
		    for w in enabled_windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def ExportView(window_name: str, view_name: str, filename: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.export_view` instead.


	This function exports to a file an existing view of a window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	filename : str
		Name of the file.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    filename = "/home/user/views_file.view"
		    ret = windows.ExportView(window_name, view_name, filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.export_view instead.", DeprecationWarning)

def HtmlDescriptionOfColor(red: int, green: int, blue: int) -> str:

	"""

	This function finds the html description of an existing color with the given RGB values.

	Parameters
	----------
	red : int
		Red value.

	green : int
		Green value.

	blue : int
		Blue value.

	Returns
	-------
	str
		It returns a string with the html descripiton of the existing color with the given RGB values.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    red = 255
		    green = 0
		    blue = 255
		    html_color = windows.HtmlDescriptionOfColor(red, green, blue)
		    print(html_color)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ImportView(filename: str, window_name: str) -> int:

	"""

	This function imports a view from a file on a window specified by its name.

	Parameters
	----------
	filename : str
		Name of the file containing the view.

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    filename = "/home/user/views_file1.view"
		    windows.ImportView(window_name, filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsColor(color: object) -> int:

	"""

	This function checks whether a class is of type Color.

	Parameters
	----------
	color : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is Color clasee, or 0 if not.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    ent = windows.ColorOfWindow(window_name)
		    if windows.IsColor(ent):
		        col = ent
		        print("This is a Color class.")
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsWindow(window: object) -> int:

	"""

	This function checks whether an object is of class type Window.

	Parameters
	----------
	window : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is class of type Window, or 0 if not.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    enabled_windows = windows.EnabledWindows()
		    for win in enabled_windows:
		        if windows.IsWindow(win):
		            print("This is a Window class.")
		            print(
		                win.name,
		                win.page_id,
		                win.active,
		                win.height,
		                win.width,
		                win.plot2d,
		                win.enabled,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def NameOfActiveFringe(window_name: str, fringe_type: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_fringebars_names` instead.


	This function finds the name of the active fringe bar of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	fringe_type : str
		Type of fringebar. Its possible values are:
		- 'scalar': Scalar fringe (default value)
		- 'vector': Vector fringe

	Returns
	-------
	str
		Upon success, it returns a string referring to the name of the active fringe bar of the specified window.
		Upon failure an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    fringe_type = "scalar"
		    fringe_name = windows.NameOfActiveFringe(window_name, fringe_type)
		    print(fringe_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_fringebars_names instead.", DeprecationWarning)

def NamedColorFromRgb(red: int, green: int, blue: int, alpha: int) -> str:

	"""

	This function finds the name of an existing color with the given RGB and Alpha channel values.

	Parameters
	----------
	red : int
		Red value.

	green : int
		Green value.

	blue : int
		Blue value.

	alpha : int
		Alpha channel.

	Returns
	-------
	str
		It returns a string with the name of the existing color with the given RGB and Alpha channel values.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    red = 255
		    green = 0
		    blue = 255
		    alpha = 255
		    named_color = windows.NamedColorFromRgb(red, green, blue, alpha)
		    print(named_color)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfAllFringes() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_fringebars_names` instead.


	This function finds the names of all existing fringe bars of a given window.

	Returns
	-------
	object
		It returns a list where each item of the list is a string referring to the name of an existing fringe bar.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    all_fringes_names = windows.NamesOfAllFringes()
		    for fringe_name in all_fringes_names:
		        print(fringe_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_fringebars_names instead.", DeprecationWarning)

def NamesOfAllViews(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_names` instead.


	This function gets names of all existing views of a window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each item of the list is a string referring to the name of an existing view of the specified window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    all_views_names = windows.NamesOfAllViews(window_name)
		    for view_name in all_views_names:
		        print(view_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_names instead.", DeprecationWarning)

def ReportNewWindows() -> object:

	"""

	This function collects the newly created windows from the last call of script function CollectNewWindowsStart(). This function should be preceded by a corresponding call to script function CollectNewWindowsStart() and should be followed by a corresponding call to script function CollectNewWindowsEnd().

	Returns
	-------
	object
		It returns a list with objects of class Window of the corresponding newly created windows.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		from meta import utils
		
		
		def main():
		    windows.CollectNewWindowsStart()
		
		    # create new windows
		    utils.MetaCommand("window create Window10")
		    utils.MetaCommand("xyplot create Window11")
		
		    new_windows = windows.ReportNewWindows()
		    for w in new_windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		    windows.CollectNewWindowsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def RgbFromNamedColor(named_color: str) -> object:

	"""

	This function finds RGB values and Alpha channel of an existing named color.

	Parameters
	----------
	named_color : str
		Name of the color.

	Returns
	-------
	object
		It returns a list with the RGB and Alpha channel values [0-255] of the corresponding color with the given name.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		import meta
		from meta import windows
		
		
		def main():
		    named_color = "Yellow"
		    rgb_values = windows.RgbFromNamedColor(named_color)
		    if rgb_values:
		        print("Red value: ", rgb_values[0])  # R value
		        print("Greeb value: ", rgb_values[1])  # G value
		        print("Blue value: ", rgb_values[2])  # B value
		        print("Alpha channel value: ", rgb_values[3])  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()


	"""

def RotateView(window_name: str, view_name: str, xrot: float, yrot: float, zrot: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.rotate_view` instead.


	This function rotates a given view of a window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	xrot : float
		Angle of rotation around X axis.

	yrot : float
		Angle of rotation around Y axis.

	zrot : float
		Angle of rotation around Z axis.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "DEFAULT_VIEW_:_+Y+Z_(F4)"
		    xrot = 10.5
		    yrot = 21.54
		    zrot = 113.2
		    windows.RotateView(window_name, view_name, xrot, yrot, zrot)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.rotate_view instead.", DeprecationWarning)

def SaveView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.save_view` instead.


	This function saves the current view of a window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name under which the view will be saved.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "my_view"
		    windows.SaveView(window_name, view_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.save_view instead.", DeprecationWarning)

def SetColorOfWindow(window_name: str, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_color` instead.


	This function sets color of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	red : int
		Red component value.

	green : int
		Green component value.

	blue : int
		Blue component value.

	alpha : int
		Alpha channel value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = windows.SetColorOfWindow(window_name, red, green, blue, alpha)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_color instead.", DeprecationWarning)

def TranslateView(window_name: str, view_name: str, xtrans: float, ytrans: float, ztrans: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.translate_view` instead.


	This function translates a given view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	xtrans : float
		X coordinate of the translation vector.

	ytrans : float
		Y coordinate of the translation vector.

	ztrans : float
		Z coordinate of the translation vector.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "DEFAULT_VIEW_:_+Y+Z_(F4)"
		    xtrans = 10.5
		    ytrans = 21.54
		    ztrans = 113.2
		    ret = windows.TranslateView(window_name, view_name, xtrans, ytrans, ztrans)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.translate_view instead.", DeprecationWarning)

def UpdateWindow(window: object) -> object:

	"""

	This function updates the attributes of a given object of type Window class. Update is based in the fields "name" and "page_id" of the given window object.

	Parameters
	----------
	window : object
		Object of class Window.

	Returns
	-------
	object
		Upon success, it returns the new updated window object.
		Else, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    w = windows.WindowByName(window_name)
		    if w:
		        # commands which alter the data of the window struct
		        utils.MetaCommand("window size 500,500")
		        w = windows.UpdateWindow(w)
		        if w:
		            print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		        else:
		            print("This is not a valid window struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def WindowByName(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function searches for the window with the given name. The full name of the window is required.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns an object of type Window with the given name.
		Else, None is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    w = windows.WindowByName(window_name)
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def Windows() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function collects all the current existing windows.

	Returns
	-------
	object
		It returns a list where each item of the list is an oject of type Window referring to the corresponding window.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    all_windows = windows.Windows()
		    for w in all_windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def WindowsByName(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function searches for the windows with the given name. 

	Parameters
	----------
	window_name : str
		Name of the window. Wildcards can also be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each item of the list is an oject of type Window referring to the corresponding window.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "Win*"
		    collected_windows = windows.WindowsByName(window_name)
		    for w in collected_windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def WindowsOfModel(model_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.models.Model.get_windows` instead.


	This function finds the windows in which the model specified by the given id is loaded.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each item of the list is an oject of type Window referring to the corresponding window.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    model_id = 0
		    windows_of_model = windows.WindowsOfModel(model_id)
		    for w in windows_of_model:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.models.Model.get_windows instead.", DeprecationWarning)

def AspectRatioOfView(window_name: str, view_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_aspect_ratio` instead.


	This function gets the aspect ratio of a view with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	float
		It returns a float referring to the aspect ratio of a view with a given name. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    aspect_ratio = windows.AspectRatioOfView(window_name, view_name)
		    print(aspect_ratio)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_aspect_ratio instead.", DeprecationWarning)

def BackClippingDistanceOfView(window_name: str, view_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_back_clipping_distance` instead.


	This function gets the back clipping distance of a view.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	float
		It returns a float referring to the back clipping distance of a view with a given name.
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    back_clipping_distance = windows.BackClippingDistanceOfView(window_name, view_name)
		    print(back_clipping_distance)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_back_clipping_distance instead.", DeprecationWarning)

def CameraPositionOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_camera_position` instead.


	This function gets the camera position (X,Y,Z) of a view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list where each member of the list is a float referring to the X, Y and Z coordinates of the camera position of the given view..
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		
		    camera_position = windows.CameraPositionOfView(window_name, view_name)
		    if camera_position:
		        xpos = camera_position[0]
		        print(xpos)  # X camera position of view
		        ypos = camera_position[1]
		        print(ypos)  # Y camera position of view
		        zpos = camera_position[2]
		        print(zpos)  # Z camera position of view
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_camera_position instead.", DeprecationWarning)

def FollowModeOfView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_follow_mode` instead.


	This function gets the follow mode of a view of a window with a given name (view_name).

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	int
		It returns 1 if follow mode of the view with the given name is active, 
		or 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		
		    view_name1 = "View1"
		    meta.utils.MetaCommand("view camera position foff")
		    meta.utils.MetaCommand("view camera reference foff")
		    meta.utils.MetaCommand('view save "' + view_name1 + '"')
		
		    view_name2 = "View2"
		    meta.utils.MetaCommand("view camera position fon")
		    meta.utils.MetaCommand("view camera reference fon")
		    meta.utils.MetaCommand('view save "' + view_name2 + '"')
		
		    follow_mode1 = windows.FollowModeOfView(window_name, view_name1)
		    print("Follow mode for View1: ", follow_mode1)
		    follow_mode2 = windows.FollowModeOfView(window_name, view_name2)
		    print("Follow mode for View2: ", follow_mode2)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_follow_mode instead.", DeprecationWarning)

def FrontClippingDistanceOfView(window_name: str, view_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_front_clipping_distance` instead.


	This function gets the front clipping distance of a view.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	float
		It returns a float referring to the front clipping distance of a view with a given name. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    front_clipping_distance = windows.FrontClippingDistanceOfView(
		        window_name, view_name
		    )
		    print(front_clipping_distance)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_front_clipping_distance instead.", DeprecationWarning)

def LockNodeIdsOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_lock_node_ids` instead.


	This function gets the lock node ids of a view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to the lock node ids of the view.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View3"
		
		    lock_node_ids = windows.LockNodeIdsOfView(window_name, view_name)
		    if lock_node_ids:
		        nid1 = lock_node_ids[0]
		        print(nid1)  # 1st node
		        nid2 = lock_node_ids[1]
		        print(nid2)  # 2nd node
		        nid3 = lock_node_ids[2]
		        print(nid3)  # 3rd node
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_lock_node_ids instead.", DeprecationWarning)

def MultiLockCameraDisplacementsOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_multi_lock_camera_displacements` instead.


	This function gets the multi lock camera displacements of a view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list where each member of the list is a float referring to the multi lock camera displacements of a view of a window with a given name.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		
		    multi_lock = windows.MultiLockCameraDisplacementsOfView(window_name, view_name)
		    if multi_lock:
		        multi_lock1 = multi_lock[0]
		        print(multi_lock1)
		        multi_lock2 = multi_lock[1]
		        print(multi_lock2)
		        multi_lock3 = multi_lock[2]
		        print(multi_lock3)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_multi_lock_camera_displacements instead.", DeprecationWarning)

def MultiLockCameraHeadRotationsOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_multi_lock_camera_head_rotations` instead.


	This function gets the multi lock camera head rotations of a view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list with three members, where each member of the list is a float referring to the multi lock camera head rotations of the given view.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		
		    multi_rot = windows.MultiLockCameraHeadRotationsOfView(window_name, view_name)
		    if multi_rot:
		        multi_rot1 = multi_rot[0]
		        print(multi_rot1)
		        multi_rot2 = multi_rot[1]
		        print(multi_rot2)
		        multi_rot3 = multi_rot[2]
		        print(multi_rot3)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_multi_lock_camera_head_rotations instead.", DeprecationWarning)

def MultiLockOfView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_multi_locks` instead.


	This function gets the multi lock of a view of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	int
		It returns 1 if multi lock of the view with the given name is active, 
		or 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    multi_lock = windows.MultiLockOfView(window_name, view_name)
		    print(multi_lock)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_multi_locks instead.", DeprecationWarning)

def NodeLocksOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_node_locks` instead.


	This function gets the node locks of a view of a window with a given name. 

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to node locks of the view.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "view0"
		
		    node_locks = windows.NodeLocksOfView(window_name, view_name)
		    if node_locks:
		        nid1 = node_locks[0]
		        print(nid1)
		        nid2 = node_locks[1]
		        print(nid2)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_node_locks instead.", DeprecationWarning)

def PerspectiveModeOfView(window_name: str, view_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_perspective_mode` instead.


	This function gets the perspective mode of a view of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	int
		It returns 1 if perspective mode of the view with the given name is active, 
		or 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    perspective_mode = windows.PerspectiveModeOfView(window_name, view_name)
		    print(perspective_mode)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_perspective_mode instead.", DeprecationWarning)

def ReferencePositionOfView(window_name: str, view_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_reference_position` instead.


	This function gets the reference position (X,Y,Z) of a view of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	object
		It returns a list with three members, where each member of the list is a float referring to the X, Y and Z coordinates of the reference position of the view.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		
		    reference_position = windows.ReferencePositionOfView(window_name, view_name)
		    if reference_position:
		        xpos = reference_position[0]
		        print(xpos)  # X reference position of view
		        ypos = reference_position[1]
		        print(ypos)  # Y reference position of view
		        zpos = reference_position[2]
		        print(zpos)  # Z reference position of view
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_reference_position instead.", DeprecationWarning)

def UpVectorOfView() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_view_up_vector` instead.


	This function gets the up vector (X,Y,Z) of a view of a window. 

	Returns
	-------
	object
		It returns a list with three members, where each member of the list is a float referring to the X, Y and Z coordinates of the view.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    meta.utils.MetaCommand('view save "' + view_name + '"')
		    up_vector = windows.UpVectorOfView(window_name, view_name)
		    if up_vector:
		        xvec = up_vector[0]
		        print(xvec)
		        yvec = up_vector[1]
		        print(yvec)
		        zvec = up_vector[2]
		        print(zvec)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_view_up_vector instead.", DeprecationWarning)

def ViewingAngleOfView(window_name: str, view_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_viewing_angle` instead.


	This function gets the viewing angle of a view.

	Parameters
	----------
	window_name : str
		Name of the window.

	view_name : str
		Name of the view.

	Returns
	-------
	float
		It returns a float referring to the viewing angle of a view with a given name. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    view_name = "View1"
		    viewing_angle = windows.ViewingAngleOfView(window_name, view_name)
		    print(viewing_angle)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_viewing_angle instead.", DeprecationWarning)

def ParamPointFromId(window_name: str, param_point_id: int, result: object) -> object:

	"""

	This function finds a parametric point with a given id at a specific window. Function takes a Resultset as an argument to define from which label the values are taken from.

	Parameters
	----------
	window_name : str
		Name of the window.

	param_point_id : int
		Id of the parametric point.

	result : object
		An object of class Result that refers to a Resultset of the model.

	Returns
	-------
	object
		Returns an object of class ParamPoint that matches the parametric point with the given id at the specified window.

	See Also
	--------
	windows.ParamPoint

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import windows
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		
		    print("Id:", pnt.id)
		    print(
		        "Elem : id:",
		        pnt.elem_id,
		        " Type :",
		        pnt.elem_type,
		        " Subtype :",
		        pnt.elem_subtype,
		        " Seq Id :",
		        pnt.elem_seqid,
		        " Model :",
		        pnt.elem_model,
		    )
		    print("Pos X,Y,Z :", pnt.x, ",", pnt.y, ",", pnt.z)
		    print("Disp X,Y,Z,Tot :", pnt.dx, ",", pnt.dy, ",", pnt.dz, ",", pnt.dt)
		    print("Scalar top,bottom :", pnt.stop, ",", pnt.sbot)
		    print("Vector top,bottom :", pnt.vtop, ",", pnt.vbot)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PointsOfParamPath(param_path_name: str, window_name: str, result: object) -> object:

	"""

	This function returns a matrix with the parametric points and their values that belong to a given path  at a given window.

	Parameters
	----------
	param_path_name : str
		Name of the Parametric Point Path.

	window_name : str
		Name of the window.

	result : object
		An object of class Resultset.

	Returns
	-------
	object
		Returns a matrix with objects of class ParamPoint that match the parametric points that belong to the given path at the given window.

	See Also
	--------
	windows.ParamPoint

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import results
		from meta import windows
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    param_path_name = "LINE_PATH_1"
		    all_points = windows.PointsOfParamPath(param_path_name, window_name, result)
		    for pnt in all_points:
		        print("Id:", pnt.id)
		        print(
		            "Elem : id:",
		            pnt.elem_id,
		            " Type :",
		            pnt.elem_type,
		            " Subtype :",
		            pnt.elem_subtype,
		            " Seq Id :",
		            pnt.elem_seqid,
		            " Model :",
		            pnt.elem_model,
		        )
		        print("Pos X,Y,Z :", pnt.x, ",", pnt.y, ",", pnt.z)
		        print("Disp X,Y,Z,Tot :", pnt.dx, ",", pnt.dy, ",", pnt.dz, ",", pnt.dt)
		        print("Scalar top,bottom :", pnt.stop, ",", pnt.sbot)
		        print("Vector top,bottom :", pnt.vtop, ",", pnt.vbot)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MinScalarLimitOfWindow(window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_scalar_limit` instead.


	This function gets the minimum limit of the scalar fringe of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the minimum limit of the scalar fringe of the given window. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    min_scalar_limit = windows.MinScalarLimitOfWindow(window_name)
		    print(min_scalar_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_scalar_limit instead.", DeprecationWarning)

def MaxScalarLimitOfWindow(window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_scalar_limit` instead.


	This function gets the maximum limit of the scalar fringe of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the maximum limit of the scalar fringe of the given window. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    max_scalar_limit = windows.MaxScalarLimitOfWindow(window_name)
		    print(max_scalar_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_scalar_limit instead.", DeprecationWarning)

def MinVectorLimitOfWindow(window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_vector_limit` instead.


	This function gets the minimum limit of the vector fringe of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the minimum limit of the vector fringe of the given window. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    min_vector_limit = windows.MinVectorLimitOfWindow(window_name)
		    print(min_vector_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_vector_limit instead.", DeprecationWarning)

def MaxVectorLimitOfWindow(window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_vector_limit` instead.


	This function gets the maximum limit of the vector fringe of a given window. This function works for the active page.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the maximum limit of the scalar fringe of the given window. 
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    max_vector_limit = windows.MaxVectorLimitOfWindow(window_name)
		    print(max_vector_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_vector_limit instead.", DeprecationWarning)

def SetScalarLimitsOfWindow(window_name: str, min_scalar_limit: float, max_scalar_limit: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_scalar_limits` instead.


	This function sets the limits of the scalar fringe of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	min_scalar_limit : float
		Minimum limit of scalar fringe.

	max_scalar_limit : float
		Maximum limit of scalar fringe.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    min_scalar_limit = 20
		    max_scalar_limit = 80
		    ret = windows.SetScalarLimitsOfWindow(
		        window_name, min_scalar_limit, max_scalar_limit
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_scalar_limits instead.", DeprecationWarning)

def SetVectorLimitsOfWindow(window_name: str, min_vector_limit: float, max_vector_limit: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_vector_limits` instead.


	This function sets the limits of the vector fringe of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	min_vector_limit : float
		Minimum limit of vector fringe.

	max_vector_limit : float
		Maximum limit of vector fringe.

	Returns
	-------
	int
		It returns an integer, 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    min_vector_limit = 15.2
		    max_vector_limit = 20.9
		    ret = windows.SetVectorLimitsOfWindow(
		        window_name, min_vector_limit, max_vector_limit
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_vector_limits instead.", DeprecationWarning)

def Locks() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_locks` instead.


	This function gets names of all locked views of the Lock Manager.

	Returns
	-------
	object
		It returns a list where each entry is a string referring to the name of an existing locked view of the Lock Manager.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    all_locks = windows.Locks()
		    for lock in all_locks:
		        print(lock)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_locks instead.", DeprecationWarning)

def AttributesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_attributes` instead.


	It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
	In position 0, internal lists contain a string referring to the name of the attribute.
	In position 1, internal lists contain a string referring to the value of the attributes.
	Upon failure, an empty list is returned.

	Parameters
	----------
	window_name : str
		The name of the window

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    all_attributes = windows.AttributesOfWindow(window_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_attributes instead.", DeprecationWarning)

def SetAttributeOfWindow(window_name: str, attrib_name: str, attrib_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	attrib_name : str
		Name of the attribute.

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		
		    name = "name"
		    value = "value"
		    value = windows.SetAttributeOfWindow(window_name, name, value)
		    print(value)
		    # or
		    name = "num_name"
		    value = 123
		    attribute_type = "numerical"
		    value = windows.SetAttributeOfWindow(window_name, name, value, attribute_type)
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_attribute instead.", DeprecationWarning)

def AttributeOfWindow(window_name: str, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_attributes` instead.


	Upon success, it returns a string with the value of the given argument.
	Else, an empty string is returned

	Parameters
	----------
	window_name : str
		The name of the window

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    name = "Plot_2D"
		    value = windows.AttributeOfWindow(window_name, name)
		    print("Value: " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_attributes instead.", DeprecationWarning)

def AttributeOfParamPath(window_name: str, ppath_name: str, attrib_name: str) -> str:

	"""

	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	ppath_name : str
		The name of the parametric point path

	attrib_name : str
		The name of the attribute

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    path_name = "LINE_PATH_1"
		    name = "Type"
		    value = windows.AttributeOfParamPath(window_name, path_name, name)
		    print("Value " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeOfParamPath(window_name: str, ppath_name: str, attrib_name: str, attrib_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_parametric_path_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given parametric point path. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window

	ppath_name : str
		The name of the parametric point path

	attrib_name : str
		Name of the attribute

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    path_name = "LINE_PATH_1"
		    name = "name"
		    val = "val"
		    value = windows.SetAttributeOfParamPath(window_name, path_name, name, val)
		    print(value)
		
		    name = "n_name"
		    val = 123
		    attribute_type = "numerical"
		    value = windows.SetAttributeOfParamPath(
		        window_name, path_name, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_parametric_path_attribute instead.", DeprecationWarning)

def AttributesOfParamPath(window_name: str, ppath_name: str) -> object:

	"""

	It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
	In position 0, internal lists contain a string referring to the name of the attribute.
	In position 1, internal lists contain a string referring to the value of the attributes.
	Upon failure, an empty list is returned.

	Parameters
	----------
	window_name : str
		The name of the window

	ppath_name : str
		Name of the parametric point path.

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    path_name = "LINE_PATH_1"
		    all_attributes = windows.AttributesOfParamPath(window_name, path_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributeOfAngle(window_name: str, angle_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_angle_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	angle_id : int
		The id of the angle

	attrib_name : str
		The name of the attribute

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    angle_id = 1
		    name = "Info"
		    value = windows.AttributeOfAngle(window_name, angle_id, name)
		    print("Value " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_angle_attributes instead.", DeprecationWarning)

def AttributeOfDistance(window_name: str, distance_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_distance_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	distance_id : int

	attrib_name : str
		The name of the attribute

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    distance_id = 1
		    name = "Info"
		    value = windows.AttributeOfDistance(window_name, distance_id, name)
		    print("Value " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_distance_attributes instead.", DeprecationWarning)

def AttributeOfParametricPoint(window_name: str, ppoint_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.ParamPoint.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	ppoint_id : int
		The id of the parametric point

	attrib_name : str
		The name of the attribute

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    ppoint_id = 1
		    name = "Type"
		    value = windows.AttributeOfParametricPoint(window_name, ppoint_id, name)
		    print("Value " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.ParamPoint.get_attributes instead.", DeprecationWarning)

def SetAttributeOfParametricPoint(window_name: str, ppoint_id: int, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.ParamPoint.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given parametric point. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	ppoint_id : int
		The id of the parametric point.

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

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    ppoint_id = 14
		    name = "attr"
		    val = "val"
		    value = windows.SetAttributeOfParametricPoint(window_name, ppoint_id, name, val)
		    print(value)
		    # or
		    name = "n_attr"
		    val = 123
		    attribute_type = "numerical"
		    value = windows.SetAttributeOfParametricPoint(
		        window_name, ppoint_id, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.ParamPoint.set_attribute instead.", DeprecationWarning)

def SetAttributeOfDistance(window_name: str, distance_id: int, attribute_name: str, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_distance_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given distance. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	distance_id : int
		The id of the distance.

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

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    distance_id = 1
		    name = "attr"
		    val = "val"
		    value = windows.SetAttributeOfDistance(window_name, distance_id, name, val)
		    print(value)
		    # or
		    name = "attr"
		    val = 12.3
		    attribute_type = "numerical"
		    value = windows.SetAttributeOfDistance(
		        window_name, distance_id, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_distance_attribute instead.", DeprecationWarning)

def SetAttributeOfAngle(window_name: str, angle_id: int, attrib_name: str, attrib_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_angle_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given angle. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	angle_id : int
		The id of the angle.

	attrib_name : str
		Name of the attribute.

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    angle_id = 1
		    name = "attr"
		    val = "val"
		    value = windows.SetAttributeOfAngle(window_name, angle_id, name, val)
		    print(value)
		    # or
		    name = "n_attr"
		    val = 12.2
		    attribute_type = "numerical"
		    value = windows.SetAttributeOfAngle(
		        window_name, angle_id, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_angle_attribute instead.", DeprecationWarning)

def AttributesOfParametricPoint(window_name: str, ppoint_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.ParamPoint.get_attributes` instead.


	This function collects all attributes of a given parametric point

	Parameters
	----------
	window_name : str
		The name of the window

	ppoint_id : int
		The id of the parametric point

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    ppoint_id = 14
		
		    all_attributes = windows.AttributesOfParametricPoint(window_name, ppoint_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.ParamPoint.get_attributes instead.", DeprecationWarning)

def AttributesOfDistance(window_name: str, distance_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_distance_attributes` instead.


	This function collects all attributes of a given distance

	Parameters
	----------
	window_name : str
		The name of the window

	distance_id : int
		The id of the distance

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    distance_id = 15
		    all_attributes = windows.AttributesOfDistance(window_name, distance_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_distance_attributes instead.", DeprecationWarning)

def AttributesOfAngle(window_name: str, angle_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_angle_attributes` instead.


	This function collects all attributes of a given angle

	Parameters
	----------
	window_name : str
		The name of the window

	angle_id : int
		The id of the angle

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
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    angle_id = 1
		    all_attributes = windows.AttributesOfAngle(window_name, angle_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_angle_attributes instead.", DeprecationWarning)

def PickRegion(mode: str) -> object:

	"""

	This function enters pick mode and waits for the user to select a region in an OpenGL window. Once a selection is made, the function returns a list that contains the coordinates of the selected box.

	Parameters
	----------
	mode : str, optional
		Its possible values are:
		  - "absolute" : the values of the selected box correspond to the pixels on the screen.
		  - "normalized" : the values of the selected box are normalized as to the width and the height of the window.
		The default value is "absolute" and, in both cases, the origin of the coordinate system is the top-left corner of the window.

	Returns
	-------
	object
		It returns a list of floating numbers that correspond to the coordinates of the selected box.
		  -The first element of the list is the left (x) coordinate.
		  -The second element of the lsit is the top (y) coordinate.
		  -The third element of the list is the width of the selected box.
		  -The fourth element of the list is the height of the selected box.
		
		If mode is "normalized", all values are between 0 and 1.
		If the user exits pick mode without selecting a region, width and height will be equal to -1.
		In single pick, width and height will be 0.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import windows
		
		
		def main():
		    mode = "normalized"
		    coords = windows.PickRegion(mode)
		    if coords:
		        print(
		            "Left x:",
		            coords[0],
		            " Top y:",
		            coords[1],
		            "Width:",
		            coords[2],
		            "Height:",
		            coords[3],
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetScalarFringeSettings(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_fringe_settings` instead.


	This function displays the settings of the scalar fringe in the given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a dictionary with the settings of the scalar fringe. Each pair of key and value of the dictionary contains one setting. The key will always be a string.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    settings = windows.GetScalarFringeSettings(window_name)
		    for k in settings:
		        print("{:>30}".format(k), ":", settings[k])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_fringe_settings instead.", DeprecationWarning)

def GetVectorFringeSettings(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_fringe_settings` instead.


	This function displays the settings of the vector fringe in the given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a dictionary with the settings of the scalar fringe. Each pair of key and value of the dictionary contains one setting. The key will always be a string.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    settings = windows.GetVectorFringeSettings(window_name)
		    for k in settings:
		        print("{:>30}".format(k), ":", settings[k])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_fringe_settings instead.", DeprecationWarning)

def SetScalarFringeSettings(window_name: str, settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_fringe_settings` instead.


	This function adjusts the settings of the scalar fringe in the given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	settings : object
		Argument 'settings' is a dictionary which contains strings as members with the name and value of each setting separated by comma (e.g. 'format, auto'). The names of the scalar fringe settings and their possible values are:
		- 'format' : Precision type ('auto', 'fixed', 'scientific')
		- 'digits' : Number of digits (integer value)
		- 'color_background' : Background color (string value)
		- 'color_description' : Color of the description (string value)
		- 'color_footer' : Color of the footer (string value)
		- 'color_outline' : Color of the outline (string value)
		- 'color_fringeoutline' : Color of the fringe outline (string value)
		- 'color_title' : Color of the title (string value)
		- 'color_values' : Color of the values (string value)
		- 'expand' : Expand fringebar colors ('on', 'off')
		- 'font_description' : Description font (string value)
		- 'font_footer' : Footer font (string value)
		- 'font_title' : Title font (string value)
		- 'font_values' : Values font (string value)
		- 'footer_function' : Set footer function ('all', 'visible')
		- 'footer_minmaxids' : Show min-max entity ids ('on', 'off')
		- 'footer_tdeform' : Show T Deform function in footer ('on', 'off')
		- 'footer_xdeform' : Show X Deform function in footer ('on', 'off')
		- 'footer_ydeform' : Show Y Deform function in footer ('on', 'off')
		- 'footer_zdeform' : Show Z Deform function in footer ('on', 'off')
		- 'horizontal' : Set horizontal orientation ('on', 'off')
		- 'invert' : Invert color order ('on', 'off')
		- 'mode_novaluecolor' : Display No Value elements with no value color ('on', off')
		- 'position_x' : Set fringe position in X axis (value from 0 to 1)
		- 'position_y' : Set fringe position in Y axis (value from 0 to 1)
		- 'rangebehaviour : Set fringe range behaviour ('enable', 'disable')
		- 'text_description' : Set description text (string value)
		- 'text_novalue' : Set No Value Color text (string value)
		- 'type_title': Set Title type ('user', 'currentlabel')
		- 'text_title' : Set Title text (string value)
		- 'height' : Set fringe height (value from 0 to 1)
		- 'width' : Set fringe width (value from 0 to 1)
		- 'spacing' : Set spacing between fringe parts (number of pixels)
		- 'textalign_colors' : Set position of values relative to fringe ('left', 'right')
		- 'textalign_description' : Set description text alignment ('center', 'left', right')
		- 'textalign_footer' : Set footer text alignment ('center', 'left', right')
		- 'textalign_title' : Set title text alignment ('center', 'left', right')
		- 'textalign_values' : Set values text alignment ('center', 'left', right')
		- 'textposition_description' : Set description text position ('top', 'bottom')
		- 'textposition_title' : Set title text position ('top', 'bottom')
		- 'textposition_values_center' : Set values in center for non linear fringe ('on', off')
		- 'visibility_background' : Show background color ('on', off')
		- 'visibility_colors' : Show color bar ('on', off')
		- 'visibility_comparecharvisible' : Show '<' and '>' on color bar ('on', off')
		- 'visibility_description' : Show description ('on', off')
		- 'visibility_footer' : Show footer min-max function ('on', off')
		- 'visibility_fringeoutline' : Show color bar outline ('on', off')
		- 'visibility_novaluecolor' : Show no value color indication ('on', off')
		- 'visibility_outline' : Show outline ('on', off')
		- 'visibility_title' : Show title ('on', off')
		- 'visibility_values' : Show values ('on', off')
		- 'color_fringebar_scalarset' : Set current Scalar fringe (fringe name)
		- 'srange_set' : Set min max range ('min_value, max_value')

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    settings = {"format": "auto"}
		    ret = windows.SetScalarFringeSettings(window_name, settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_fringe_settings instead.", DeprecationWarning)

def SetVectorFringeSettings(window_name: str, settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_fringe_settings` instead.


	This function adjusts the settings of the vector fringe in the given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	settings : object
		Argument 'settings' is a dictionary which contains strings as members with the name and value of each setting separated by comma (e.g. 'format, auto'). The names of the scalar fringe settings and their possible values are:
		- 'format' : Precision type ('auto', 'fixed', 'scientific')
		- 'digits' : Number of digits (integer value)
		- 'color_background' : Background color (string value)
		- 'color_description' : Color of the description (string value)
		- 'color_footer' : Color of the footer (string value)
		- 'color_outline' : Color of the outline (string value)
		- 'color_fringeoutline' : Color of the fringe outline (string value)
		- 'color_title' : Color of the title (string value)
		- 'color_values' : Color of the values (string value)
		- 'expand' : Expand fringebar colors ('on', 'off')
		- 'font_description' : Description font (string value)
		- 'font_footer' : Footer font (string value)
		- 'font_title' : Title font (string value)
		- 'font_values' : Values font (string value)
		- 'footer_function' : Set footer function ('all', 'visible')
		- 'footer_minmaxids' : Show min-max entity ids ('on', 'off')
		- 'footer_tdeform' : Show T Deform function in footer ('on', 'off')
		- 'footer_xdeform' : Show X Deform function in footer ('on', 'off')
		- 'footer_ydeform' : Show Y Deform function in footer ('on', 'off')
		- 'footer_zdeform' : Show Z Deform function in footer ('on', 'off')
		- 'horizontal' : Set horizontal orientation ('on', 'off')
		- 'invert' : Invert color order ('on', 'off')
		- 'position_x' : Set fringe position in X axis (value from 0 to 1)
		- 'position_y' : Set fringe position in Y axis (value from 0 to 1)
		- 'text_description' : Set description text (string value)
		- 'type_title': Set Title type ('user', 'currentlabel')
		- 'text_title' : Set Title text (string value)
		- 'height' : Set fringe height (value from 0 to 1)
		- 'width' : Set fringe width (value from 0 to 1)
		- 'spacing' : Set spacing between fringe parts (number of pixels)
		- 'textalign_colors' : Set position of values relative to fringe ('left', 'right')
		- 'textalign_description' : Set description text alignment ('center', 'left', right')
		- 'textalign_footer' : Set footer text alignment ('center', 'left', right')
		- 'textalign_title' : Set title text alignment ('center', 'left', right')
		- 'textalign_values' : Set values text alignment ('center', 'left', right')
		- 'textposition_description' : Set description text position ('top', 'bottom')
		- 'textposition_title' : Set title text position ('top', 'bottom')
		- 'textposition_values_center' : Set values in center for non linear fringe ('on', off')
		- 'visibility_background' : Show background color ('on', off')
		- 'visibility_colors' : Show color bar ('on', off')
		- 'visibility_comparecharvisible' : Show '<' and '>' on color bar ('on', off')
		- 'visibility_description' : Show description ('on', off')
		- 'visibility_footer' : Show footer min-max function ('on', off')
		- 'visibility_fringeoutline' : Show color bar outline ('on', off')
		- 'visibility_outline' : Show outline ('on', off')
		- 'visibility_title' : Show title ('on', off')
		- 'visibility_values' : Show values ('on', off')
		- 'color_fringebar_vectorset' : Set current Scalar fringe (fringe name)
		- 'vrange_set' : Set min max range ('min_value, max_value')

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    window_name = "MetaPost"
		    settings = {"format": "auto"}
		    ret = windows.SetVectorFringeSettings(window_name, settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_fringe_settings instead.", DeprecationWarning)

def CopyWindow(source_page_id: int, source_window_name: int, target_page_id: int, target_window_names: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.copy` instead.


	This function copy-pastes a given existing window. 

	Parameters
	----------
	source_page_id : int
		This function copy-pastes a given existing window.

	source_window_name : int
		Name of the source window.

	target_page_id : int
		Id of the target page.

	target_window_names : object
		List with the target window names.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    source_page_id = 0
		    source_window_name = "MetaPost"
		    target_page_id = 0
		    target_window_names = ["Window1", "Window2"]
		    ret = windows.CopyWindow(
		        source_page_id, source_window_name, target_page_id, target_window_names
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.copy instead.", DeprecationWarning)

class Color():

	"""

	Class for color.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    color = windows.Color(r=255, g=255, b=0, a=255)
		    print(color, color.r, color.g, color.b, color.a)
		    color = windows.Color(name="Green")
		    print(color, color.r, color.g, color.b, color.a)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the color.

	"""

	r: int = None
	"""
	Red value [0,255]

	"""

	g: int = None
	"""
	Green value [0,255]

	"""

	b: int = None
	"""
	Blue value [0,255]

	"""

	a: int = None
	"""
	Alpha value [0,255]

	"""
class Window():

	"""

	Class for windows.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    # win = windows.Window(active=True)
		    print(win)
		    print(
		        win.name,
		        win.active,
		        win.width,
		        win.height,
		        win.plot2d,
		        win.enabled,
		        win.page_id,
		    )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_page
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    page = win.get_page()
		    print(page)
		    print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_models
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    models = win.get_models(specifier)
		    for model in models:
		        print(model)
		        print(model.name, model.label, model.deck, model.active)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import windows
		from meta import models
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    model = models.Model(0)
		    specifier = "all"
		    results = win.get_resultsets(specifier, model)
		    print(results)
		    for res in results:
		        print(res)
		        print(
		            res.cycle,
		            res.model_id,
		            res.name,
		            res.nodal_data_name,
		            res.function_data_name,
		            res.filename,
		            res.subcase,
		            res.state,
		            res.step,
		            res.frequency,
		            res.time,
		            res.mode,
		            res.eigenvalue,
		            res.imaginary_eigenvalue,
		            res.loadstep,
		            res.generate_sequence,
		            res.nodal_data_label,
		            res.function_data_label,
		            res.vector_data_label,
		            res.step_name,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_isofunctions
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    isos = win.get_isofunctions(specifier)
		    for iso in isos:
		        print(iso)
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_images
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    images = win.get_images(specifier)
		    for image in images:
		        print(image)
		        print(
		            image.name,
		            image.window_name,
		            image.width,
		            image.height,
		            image.filename,
		            image.zorder,
		            image.visible,
		            image.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_videos
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    videos = win.get_videos(specifier)
		    for video in videos:
		        print(video)
		        print(
		            video.name,
		            video.window_name,
		            video.width,
		            video.height,
		            video.filename,
		            video.zorder,
		            video.visible,
		            video.page_id,
		            video.frames,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_annotations
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    annots = win.get_annotations(specifier)
		    for annot in annots:
		        print(annot)
		        print(
		            annot.id,
		            annot.window_name,
		            annot.text,
		            annot.text,
		            annot.origin_text,
		            annot.visible,
		            annot.selected,
		            annot.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_annotation_groups
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    annot_groups = win.get_annotation_groups()
		    for annot_group in annot_groups:
		        print(annot_group)
		        print(annot_group.name, annot_group.window_name, annot_group.page_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_plots
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    plots = win.get_plots(specifier)
		    for plot in plots:
		        print(plot)
		        print(plot.id, plot.window_name, plot.active, plot.type, plot.page_id)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_curve_groups
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    curve_groups = win.get_curve_groups()
		    for curve_group in curve_groups:
		        print(curve_group)
		        print(
		            curve_group.name,
		            curve_group.plot_id,
		            curve_group.window_name,
		            curve_group.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    for curve in curves:
		        print(curve)
		        print(
		            curve.id,
		            curve.plot_id,
		            curve.window_name,
		            curve.name,
		            curve.visible,
		            curve.selected,
		            curve.page_id,
		            curve.command,
		            curve.entity_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_plot_axes
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    axes = win.get_plot_axes(specifier)
		    for axis in axes:
		        print(axis)
		        print(
		            axis.id,
		            axis.type,
		            axis.plot_id,
		            axis.window_name,
		            axis.active,
		            axis.visible,
		            axis.min_value,
		            axis.max_value,
		            axis.page_id,
		            axis.log_on,
		            axis.db_type,
		            axis.db_factor,
		            axis.range_lock,
		        )
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_scalar_limit
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "max"
		    limit = win.get_scalar_limit(specifier)
		    print(limit)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_vector_limit
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "max"
		    limit = win.get_vector_limit(specifier)
		    print(limit)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_color
		# PYTHON script
		
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    col = win.get_color()
		    print(col)
		    print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_view_names
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    names = win.get_view_names()
		    print(names)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_locks
		# PYTHON script
		
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    locks = win.get_locks()
		    print(locks)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_plot_layout
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    layout = win.get_plot_layout()
		    print(layout)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_fringe_names
		# PYTHON script
		
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "active"
		    names = win.get_fringe_names(specifier, fringe_type="vector")
		    print(names)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    attr = win.get_attributes()
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_angle_attributes
		# PYTHON script
		
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    angle_id = 2
		    attr = win.get_angle_attributes(angle_id)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_distance_attributes
		# PYTHON script
		
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    distance_id = 1
		    attr = win.get_distance_attributes(distance_id)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_parametric_point_attributes
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    param_point_id = 3
		    attr = win.get_parametric_point_attributes(param_point_id)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_camera_position
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    pos = win.get_view_camera_position(view_name)
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_reference_position
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    pos = win.get_view_reference_position(view_name)
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_up_vector
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    vec = win.get_view_up_vector(view_name)
		    print(vec)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_front_clipping_distance
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    dist = win.get_view_front_clipping_distance(view_name)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_back_clipping_distance
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    dist = win.get_view_back_clipping_distance(view_name)
		    print(dist)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_viewing_angle
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    angle = win.get_viewing_angle(view_name)
		    print(angle)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_perspective_mode
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    mode = win.get_view_perspective_mode(view_name)
		    print(mode)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_aspect_ratio
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    ratio = win.get_view_aspect_ratio(view_name)
		    print(ratio)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_follow_mode
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    mode = win.get_view_follow_mode(view_name)
		    print(mode)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_camera_node_locks
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    locks = win.get_camera_node_locks(view_name)
		    print(locks)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_multi_locks
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    locks = win.get_view_multi_locks(view_name)
		    print(locks)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_lock_node_ids
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    locks = win.get_view_lock_node_ids(view_name)
		    print(locks)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_multi_lock_camera_displacements
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    val = win.get_view_multi_lock_camera_displacements(view_name)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_view_multi_lock_camera_head_rotations
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    val = win.get_view_multi_lock_camera_head_rotations(view_name)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_fringe_settings
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    fringe_type = "scalar"
		    sett = win.get_fringe_settings(fringe_type)
		    print(sett)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_current_resultset
		# PYTHON script
		import meta
		from meta import windows
		from meta import models
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    m = models.Model(0)
		    all_res = m.get_resultsets()
		    ret = win.set_current_resultset(m, all_res[1])
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_scalar_limits
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    scalar_limits = (100, 500)
		    ret = win.set_scalar_limits(scalar_limits)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_vector_limits
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    vector_limits = (100, 500)
		    ret = win.set_vector_limits(vector_limits)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_color
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    color = windows.Color(name="Black")
		    ret = win.set_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    attribute_name = "test"
		    attribute_type = "string"
		    attribute_value = "123"
		    ret = win.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_angle_attribute
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    angle_id = 2
		    attribute_name = "test"
		    attribute_type = "string"
		    attribute_value = "123"
		    ret = win.set_angle_attribute(
		        angle_id, attribute_name, attribute_type, attribute_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_distance_attribute
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    distance_id = 1
		    attribute_name = "test"
		    attribute_type = "string"
		    attribute_value = "123"
		    ret = win.set_distance_attribute(
		        distance_id, attribute_name, attribute_type, attribute_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_parametric_point_attribute
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    param_point_id = 3
		    attribute_name = "test"
		    attribute_type = "string"
		    attribute_value = "123"
		    ret = win.set_parametric_point_attribute(
		        param_point_id, attribute_name, attribute_type, attribute_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_fringe_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    fringe_type = "scalar"
		    settings = {"format": "scientific"}
		    ret = win.set_fringe_settings(fringe_type, settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: activate
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.activate()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: delete
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    ret = win.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: copy
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    page = win.get_page()
		    window_names = ["copied_1", "copied_2"]
		    ret = win.copy(page, window_names)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: enable
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.enable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: disable
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.disable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: activate_fringe
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    fringe_name = "AnimationBar"
		    fringe_type = "scalar"
		    ret = win.activate_fringe(fringe_name, fringe_type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: apply_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    ret = win.apply_view("view_name")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: save_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    ret = win.save_view("view_name")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: delete_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    ret = win.delete_view(view_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: translate_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    translation_vector = [100, 0, 0]
		    ret = win.translate_view(view_name, translation_vector)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: rotate_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    rotation_angles = [0.1, 0.1, 0.1]
		    ret = win.rotate_view(view_name, rotation_angles)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: import_view
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    filename = "view_file"
		    ret = win.import_view(filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: pick_isofunctions
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		
		    message = "Select Isofunctions and press Enter when you are ready"
		    ret = win.pick_isofunctions(message)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: pick_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    message = "Select Curves and press middle mouse button when you are ready"
		    ret = win.pick_curves(message)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: pick_points
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		
		    message = "Select Curves and press middle mouse button when you are ready"
		    ret = win.pick_points(message, all_curves=True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: hide_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    ret = win.hide_curves(curves)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: show_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    ret = win.show_curves(curves)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: select_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    ret = win.select_curves(curves)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: deselect_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    ret = win.deselect_curves(curves)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: delete_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    specifier = "all"
		    curves = win.get_curves(specifier)
		    ret = win.delete_curves(curves)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_isofunctions_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    settings = {"options_linewidth": "10"}
		    ret = win.set_isofunctions_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_annotations_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    settings = {"background_color": "Red"}
		    ret = win.set_annotations_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_images_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    settings = {"filter": "blue"}
		    ret = win.set_images_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_videos_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    settings = {"filter": "blue"}
		    ret = win.set_videos_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_plots_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    settings = {"border_width": 10}
		    ret = win.set_plots_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_curves_settings
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    settings = {"style": 10}
		    ret = win.set_curves_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_novalue_color
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    color = win.get_novalue_color()
		    print(color)
		    print(color.name, color.r, color.g, color.b, color.a)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_novalue_color
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    # utils.MetaCommand('options palettescolors autosave disable')
		    color = windows.Color(name="Red")
		    ret = win.set_novalue_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_size
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    size = win.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: is_maximized
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.is_maximized()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: is_minimized
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.is_minimized()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: is_docked
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.is_docked()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_size
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    size = (750, 500)
		    ret = win.set_size(size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: maximize
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.maximize()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: minimize
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.minimize()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: restore
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.restore()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: undock
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.undock()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: dock
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.dock()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_plot_layout
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    layout = 3
		    win.set_plot_layout(layout)
		    layout = win.get_plot_layout()
		    print(layout)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_top_down
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    tdown = win.get_top_down()
		    print(tdown)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: pick_plots
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    message = "Select Plots and press middle mouse button when you are ready"
		    picked = win.pick_plots(message)
		    print(picked)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: pick_3d_positions
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    message = "Pick 3d positions and press Enter when you are ready"
		    picked = win.pick_3d_positions(message)
		    print(picked)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_text
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="Window1", page_id=0)
		    evaluated = False
		    html = True
		    txt = win.get_text(evaluated, html)
		    print(txt)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_param_point_list
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    param_point_list = win.get_param_point_list()
		    for pnt in param_point_list:
		        print(pnt)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: save_image
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    file = "image.png"
		    win.save_image(file)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: save_video
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    file = "my_vid.gif"
		    win.save_video(file, format="gif")
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_parametric_point_paths
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    specifier = "all"
		    ppaths = win.get_parametric_point_paths(specifier)
		    print(ppaths)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: hide_annotations
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    annots = win.get_annotations()
		    win.hide_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: show_annotations
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    annots = win.get_annotations()
		    win.show_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: delete_annotations
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    annots = win.get_annotations()
		    win.delete_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_view_side_vector
		# PYTHON script
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    view_name = "view_name"
		    vec = win.get_view_side_vector(view_name)
		    print(vec)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: get_best_views
		# PYTHON script
		from meta import windows
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    w = windows.Window(name="MetaPost", page_id=0)
		    identified_elements = m.get_elements("identified", window=w)
		    dict_views = w.get_best_views(identified_elements)
		    print(dict_views)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: save_curves
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window("Window1", 0)
		    curves = win.get_curves()
		
		    win.save_curves(curves, "curves.csv", "keyword")
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_screen_position
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window("MetaPost", 0)
		    screen_pos = win.get_screen_position(891.656, -584.206, 1024.14)
		    print(screen_pos)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Id of the page of the window.

	"""

	active: int = None
	"""
	1 if window is active, 0 if window is not active.

	"""

	width: int = None
	"""
	Width of the window.

	"""

	height: int = None
	"""
	Height of the window.

	"""

	plot2d: int = None
	"""
	1 if it is a plot2d window, 0 if window is not a plot2d (a 3d window).

	"""

	enabled: int = None
	"""
	1 if window is enabled, 0 if window is not enabled.

	"""

	page_id: int = None
	"""
	Id of the page of the window.

	"""

	def save_curves(self, curves: object, filename: str, format: str) -> object:

		"""

		This method allows the user to save the window curves.


		Parameters
		----------
		curves : object
			A list of python curves.

		filename : str
			The filename.

		format : str
			The format of the file. Accepted values are:
			'atfx',
			'column',
			'diadem',
			'exportmove',
			'isoegv',
			'isotr13499',
			'isots13499',
			'isov11',
			'keyword',
			'pamcrashascii',
			'pamfunct',
			'tabled',
			'unv58'

		Returns
		-------
		object
			Returns None.

		"""


	def get_models(self, specifier: str) -> object:

		"""

		This method gets the models which are loaded in a given 3D window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all models of the window (default value).
			- 'visible' : visible models of the window.

		Returns
		-------
		object
			Uppon success, it returns a list where each member of the list is an object of class Model.Upponn failure, an empty list is returned.

		"""


	def get_resultsets(self, specifier: str, model: object, id: int, filter: str, cycle: int) -> object:

		"""

		This method gets the states for all cycles of a specific model.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'all' : all states of the model
			- 'locked' : locked states of the model
			- 'current' : state of the model
			- 'filter' : filtered states

		model : object
			An object of class Model. All the returned states will belong to this model.

		id : int, optional
			Id of the resultset. If set, the method gets the resultsets with resultset id equal to id.

		filter : str, optional
			The filter that will be applied to the states. This argument is used only when the specifier is 'filter'

		cycle : int, optional
			Cycle of the resultset. If set, the method gets the resultsets with cycle equal to cycle

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Result referring to one state of the corresponding model for a specific cycle.Upon failure, an empty list is returned.

		"""


	def get_isofunctions(self, specifier: str) -> object:

		"""

		This method gets the isofunctions of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all isofunctions of the window (default value).
			- 'visible' : visible isofunctions of the window.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Isofunction referring to one specific isofunction of the window.Upon failure, an empty list is returned.

		"""


	def get_images(self, specifier: str) -> object:

		"""

		This method gets the images of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all images of the window (default value).
			- 'visible' : visible images of the window.
			- 'selected' : selected images of the window.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Image referring to one specific image of the window.Upon failure, an empty list is returned.

		"""


	def get_videos(self, specifier: str) -> object:

		"""

		This method gets the videos of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all selected videos of the window (default value).
			- 'visible' : selected videos of the window.
			- 'selected' : selected videos of the window.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Video referring to one specific video of the window.Upon failure, an empty list is returned.

		"""


	def get_annotations(self, specifier: str) -> object:

		"""

		This method gets the annotations of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all annotations of the window (default value).
			- 'visible' : visible annotations of the window.
			- 'selected' : selected annotations of the window.
			- 'visible_on_screen' : visible on screen annotations of the window.
			- 'hidden_on_screen' : hidden on screen annotations of the window.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Annotation referring to one specific annotation of the window.Upon failure, an empty list is returned.

		"""


	def get_annotation_groups(self) -> object:

		"""

		This method gets the annotation groups of the window.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class AnnotationGroup referring to one specific annotation group of the window.Upon failure, an empty list is returned.

		"""


	def get_plots(self, specifier: str, plot_type: str) -> object:

		"""

		This method gets the plots of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all plots of the window (default value).
			- 'active' : active plots of the window.
			- 'visible' : visible plots of the window.

		plot_type : str, optional
			Type of the plot. Possible values are:
			- 'plain'
			- 'realimag'
			- 'magphase'
			- 'polar'
			- 'dna'
			- 'mac'
			- 'horizontal'
			- 'colormap'
			- '3dmac'
			- 'waterfall'
			- 'nyquist'

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Plot referring to one specific plot of the window. Upon failure, an empty list is returned.

		"""


	def get_curve_groups(self) -> object:

		"""

		This method gets the curve groups of the window.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the window.Upon failure, an empty list is returned.

		"""


	def get_plot_axes(self, specifier: str, plot_axis_type: str, plot_axis_id: int) -> object:

		"""

		This method gets the plot axes of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all plot axes of the window (default value).
			- 'visible' : visible plot axes of the window.
			- 'active' : active plot axes of the window.
			- 'visibleplots' : plot axes of the window, that are on visible plots.

		plot_axis_type : str, optional
			Type of the axis. Its possible values are:
			- 'xaxis': X axis
			- 'yaxis': Y axis
			- 'zaxis': Z axis
			- 'caxis': Y complex axis

		plot_axis_id : int, optional
			Id of the axis.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of the window.Upon failure, an empty list is returned.

		"""


	def get_curves(self, specifier: str, name: str, curve_id: int) -> object:

		"""

		This method gets the curves of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all curves of the window (default value).
			- 'visible' : visible curves of the window.
			- 'selected' : selected curves of the window.
			- 'byid' : curves chosen by id.
			- 'byname' : curves chosen by name.
			- 'visibleplots' : all curves of the window that are on visible plots.

		name : str, optional
			curve name in case specifier = 'byname' is used

		curve_id : int, optional
			curve id in case specifier = 'byid' is used

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Curve referring to one specific curve of the window.Upon failure, an empty list is returned.

		"""


	def get_scalar_limit(self, specifier: str) -> float:

		"""

		This method gets the limit of the scalar fringe of the window. This function works for the active page.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'min' : minimum limit
			- 'max' : maximum limit

		Returns
		-------
		float
			It returns a float referring to the limit of the scalar fringe of the window. Upon failure, it returns 0.

		"""


	def get_vector_limit(self, specifier: str) -> float:

		"""

		This method gets the limit of the vector fringe of the window. This function works for the active page.


		Parameters
		----------
		specifier : str
			Specifier of the method. Its possible values are:
			- 'min' : minimum limit
			- 'max' : maximum limit

		Returns
		-------
		float
			It returns a float referring to the limit of the vector fringe of the window. Upon failure, it returns 0.

		"""


	def get_color(self) -> object:

		"""

		This method gets the background color of the window.


		Returns
		-------
		object
			Upon success, it returns a python object of class Color with the color of the corresponding window.Upon failure, None is returned.

		"""


	def get_view_names(self) -> object:

		"""

		This method gets names of all existing views of the window. This method works for the active page.


		Returns
		-------
		object
			Upon success, it returns a list where each item of the list is a string referring to the name of an existing view of the specified window.Upon failure, an empty list is returned.

		"""


	def get_locks(self) -> object:

		"""

		This method gets names of all locked views of the Lock Manager.


		Returns
		-------
		object
			Upon success, it returns a list where each entry is a string referring to the name of an existing locked view of the Lock Manager.Upon failure, an empty list is returned.

		"""


	def get_plot_layout(self) -> int:

		"""

		This method gets the plot layout number of the window.
		ID  -> Layout
		 1  -> 1 x 1
		 2  -> 2 x 1
		 3  -> 1 x 2
		 4  -> 2 x 2
		 5  -> 1 x 3
		 6  -> 3 x 1
		 7  -> 1 x 4
		 8  -> 4 x 1
		 9  -> 1 & 2 x 1
		10  -> 2 x 1 & 1
		11  -> 1 & 1 x 2
		12  -> 1 x 2 & 1
		13  -> 1 & 3 x 1
		14  -> 3 x 1 & 1
		15  -> 1 & 1 x 3
		16  -> 1x 3 & 1
		17  -> 2 x 3
		18  -> 3 x 2
		19  -> 3 x 3
		20  -> 4 x 4
		21  -> 4 x 3
		22  -> 3 x 4
		23  -> 4 x 2
		24  -> 2 x 4


		Returns
		-------
		int
			Upon succes, it returns an integer referring to the plot layout number of the given window.   Upon failure, it returns None.

		"""


	def get_fringe_names(self, specifier: str) -> object:

		"""

		This method gets the names of all existing fringe bars of the window.This method works for the active page.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all fringe bar names (default value).
			- 'active' : name of the active fringe bar.

		Returns
		-------
		object
			Upon success, it returns a list where each item of the list is a string referring to the name of an existing fringe bar.Upon failure, an empty list is returned.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the window.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_distance_attributes(self, distance_id: int, attribute_name: str) -> object:

		"""

		This method gets the attributes of the specified distance of the window.


		Parameters
		----------
		distance_id : int
			The id of the distance.

		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_angle_attributes(self, angle_id: int, attribute_name: str) -> object:

		"""

		This method gets the attributes of the specified angle of the window.


		Parameters
		----------
		angle_id : int
			The id of the angle.

		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_parametric_point_attributes(self, param_point_id: int, attribute_name: str) -> object:

		"""

		This method gets the attributes of the specified parametric point of the window.


		Parameters
		----------
		param_point_id : int
			The id of the parametric point.

		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_view_camera_position(self, view_name: str) -> object:

		"""

		This method gets the camera position (X,Y,Z) of a view of the window.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is a float referring to the X, Y and Z coordinates of the camera position of the given view.Upon failure, an empty list is returned.

		"""


	def get_view_reference_position(self, view_name: str) -> object:

		"""

		This method gets the reference position (X,Y,Z) of a view of a window.


		Parameters
		----------
		view_name : str
			The name of the view

		Returns
		-------
		object
			Upon success, it returns a list with three members, where each member of the list is a float referring to the X, Y and Z coordinates of the reference position of the view.Upon failure, an empty list is returned.

		"""


	def get_view_up_vector(self, view_name: str) -> object:

		"""

		This method gets the up vector (X,Y,Z) of a view of the window. 


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		object
			Upon success, it returns a list with three members, where each member of the list is a float referring to the X, Y and Z coordinates of the view.Upon failure, an empty list is returned.

		"""


	def get_view_front_clipping_distance(self, view_name: str) -> object:

		"""

		This method gets the front clipping distance of a view.


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		object
			It returns a float referring to the front clipping distance of a view with a given name. Upon failure, it returns 0.

		"""


	def get_view_back_clipping_distance(self, view_name: str) -> float:

		"""

		This method gets the back clipping distance of a view.


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		float
			Upon success, it returns a float referring to the back clipping distance of a view with a given name.Upon failure, it returns None.

		"""


	def get_viewing_angle(self, view_name: str) -> object:

		"""

		This method gets the viewing angle of a view.


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		object
			It returns a float referring to the viewing angle of a view with a given name. Upon failure, it returns None.

		"""


	def get_view_perspective_mode(self, view_name: str) -> bool:

		"""

		This method gets the perspective mode of a view of a window with a given name.


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		bool
			Upon success, it returns 1 if perspective mode of the view with the given name is active, or 0 otherwise.

		"""


	def get_view_aspect_ratio(self, view_name: str) -> float:

		"""

		This method gets the aspect ratio of a view with a given name.


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		float
			It returns a float referring to the aspect ratio of a view with a given name. Upon failure, it returns None.

		"""


	def get_view_follow_mode(self, view_name: str) -> float:

		"""

		This method gets the follow mode of the view.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		float
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def get_camera_node_locks(self, view_name: str) -> object:

		"""

		This method gets the node locks of the camera. 


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		object
			It returns a list where each member of the list is an integer referring to node locks of the view. Upon failure, an empty list is returned.

		"""


	def get_view_multi_locks(self, view_name: str) -> str:

		"""

		This method gets the multi lock of the view.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		str
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def get_view_lock_node_ids(self, view_name: str) -> object:

		"""

		This method gets the lock node ids of the view.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an integer referring to the lock node ids of the view.Upon failure, an empty list is returned.

		"""


	def get_view_multi_lock_camera_displacements(self, view_name: str) -> object:

		"""

		This method gets the multi lock camera displacements of the view.


		Parameters
		----------
		view_name : str
			Name of the view

		Returns
		-------
		object
			It returns a list where each member of the list is a float referring to the multi lock camera displacements of a view of a window with a given name.Upon failure, an empty list is returned.

		"""


	def get_view_multi_lock_camera_head_rotations(self, view_name: str) -> object:

		"""

		This function gets the multi lock camera head rotations of the view.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		object
			It returns a list with three members, where each member of the list is a float referring to the multi lock camera head rotations of the view.Upon failure, an empty list is returned.

		"""


	def get_fringe_settings(self, fringe_type: str) -> object:

		"""

		This function displays the settings of the fringe in the given window.


		Parameters
		----------
		fringe_type : str
			The type of the fringe. The accepted values are 'scalar' and 'vector'.

		Returns
		-------
		object
			It returns a dictionary with the settings of the fringe. Each pair of key and value of the dictionary contains one setting. The key will always be a string.Upon failure, an empty list is returned.

		"""


	def set_current_resultset(self, model: object, resultset: object) -> bool:

		"""

		This method sets the current resultset of a given model for the window. This method works for the active page.


		Parameters
		----------
		model : object
			An object of class Model.

		resultset : object
			An object of class Result.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_scalar_limits(self, scalar_limits: object) -> bool:

		"""

		This method sets the limits of the scalar fringe of the window.


		Parameters
		----------
		scalar_limits : object
			A list with 2 doubles (min, max).

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_vector_limits(self, vector_limits: object) -> bool:

		"""

		This method sets the limits of the vector fringe of the window.


		Parameters
		----------
		vector_limits : object
			A list with 2 doubles (min, max).

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_color(self, color: object) -> bool:

		"""

		This method sets the color of the window


		Parameters
		----------
		color : object
			An object of class Color

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the window.


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


	def set_distance_attribute(self, distance_id: int, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the specified distance of the window.


		Parameters
		----------
		distance_id : int
			The id of the distance.

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


	def set_angle_attribute(self, angle_id: int, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the specified angle of the window.


		Parameters
		----------
		angle_id : int
			The id of the angle.

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


	def set_parametric_point_attribute(self, param_point_id: int, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the specified parametric point of the window.


		Parameters
		----------
		param_point_id : int
			The id of the parametric point

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


	def set_fringe_settings(self, fringe_type: str, settings: dict) -> bool:

		"""

		This method adjusts the settings of the fringe in the window.


		Parameters
		----------
		fringe_type : str
			The type of the fringe. The accepted values are 'scalar' and 'vector'.

		settings : dict
			Argument 'settings' is a dictionary which contains strings as members with the name and value of each setting separated by comma (e.g. 'format, auto'). The names of the fringe settings and their possible values are:
			- 'format' : Precision type ('auto', 'fixed', 'scientific')
			- 'digits' : Number of digits (integer value)
			- 'color_background' : Background color (string value)
			- 'color_description' : Color of the description (string value)
			- 'color_footer' : Color of the footer (string value)
			- 'color_outline' : Color of the outline (string value)
			- 'color_fringeoutline' : Color of the fringe outline (string value)
			- 'color_title' : Color of the title (string value)
			- 'color_values' : Color of the values (string value)
			- 'expand' : Expand fringebar colors ('on', 'off')
			- 'font_description' : Description font (string value)
			- 'font_footer' : Footer font (string value)
			- 'font_title' : Title font (string value)
			- 'font_values' : Values font (string value)
			- 'footer_function' : Set footer function ('all', 'visible')
			- 'footer_minmaxids' : Show min-max entity ids ('on', 'off')
			- 'footer_tdeform' : Show T Deform function in footer ('on', 'off')
			- 'footer_xdeform' : Show X Deform function in footer ('on', 'off')
			- 'footer_ydeform' : Show Y Deform function in footer ('on', 'off')
			- 'footer_zdeform' : Show Z Deform function in footer ('on', 'off')
			- 'horizontal' : Set horizontal orientation ('on', 'off')
			- 'invert' : Invert color order ('on', 'off')
			- 'position_x' : Set fringe position in X axis (value from 0 to 1)
			- 'position_y' : Set fringe position in Y axis (value from 0 to 1)
			- 'text_description' : Set description text (string value)
			- 'type_title': Set type of title ('user', 'currentlabel')
			- 'text_title' : Set Title text (string value)
			- 'height' : Set fringe height (value from 0 to 1)
			- 'width' : Set fringe width (value from 0 to 1)
			- 'spacing' : Set spacing between fringe parts (number of pixels)
			- 'textalign_colors' : Set position of values relative to fringe ('left', 'right')
			- 'textalign_description' : Set description text alignment ('center', 'left', right')
			- 'textalign_footer' : Set footer text alignment ('center', 'left', right')
			- 'textalign_title' : Set title text alignment ('center', 'left', right')
			- 'textalign_values' : Set values text alignment ('center', 'left', right')
			- 'textposition_description' : Set description text position ('top', 'bottom')
			- 'textposition_title' : Set title text position ('top', 'bottom')
			- 'textposition_values_center' : Set values in center for non linear fringe ('on', off')
			- 'visibility_background' : Show background color ('on', off')
			- 'visibility_colors' : Show color bar ('on', off')
			- 'visibility_comparecharvisible' : Show '<' and '>' on color bar ('on', off')
			- 'visibility_description' : Show description ('on', off')
			- 'visibility_footer' : Show footer min-max function ('on', off')
			- 'visibility_fringeoutline' : Show color bar outline ('on', off')
			- 'visibility_outline' : Show outline ('on', off')
			- 'visibility_title' : Show title ('on', off')
			- 'visibility_values' : Show values ('on', off')
			- 'style' : Set style ('onelement', 'onnode')
			
			There are also the following possible values for scalar fringe bar:
			- 'mode_novaluecolor' : Display No Value elements with no value color ('on', off')
			- 'rangebehaviour : Set fringe range behaviour ('enable', 'disable')
			- 'text_novalue' : Set No Value Color text (string value)
			- 'visibility_novaluecolor' : Show no value color indication ('on', off')
			- 'color_fringebar_scalarset' : Set current Scalar fringe (fringe name)
			- 'srange_set' : Set min max range ('min_value, max_value')
			
			And the following possible values for vector fringe bar:
			- 'color_fringebar_vectorset' : Set current Vector fringe (fringe name)
			- 'vrange_set' : Set min max range ('min_value, max_value')

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def activate(self) -> bool:

		"""

		This method makes active the window. It works only in the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the window. It works only in the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def copy(self, page: object, window_names: object) -> bool:

		"""

		This method copy-pastes a given existing window. 


		Parameters
		----------
		page : object
			An object of class page.

		window_names : object
			List with the target window names.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def enable(self, enable_active: bool, only: bool) -> bool:

		"""

		This method enables the window. It works for the active page.


		Parameters
		----------
		enable_active : bool, optional
			If optional argument 'enable_active' is True then the current active window option will be activated.

		only : bool, optional
			If optional argument 'only' is True then this window will be enabled. All windows that were enabled will be disabled.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def disable(self, disable_active: bool) -> bool:

		"""

		This method disables the window. It works for the active page.


		Parameters
		----------
		disable_active : bool, optional
			If optional argument 'disable_active' is True then the current active window option will be deactivated.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def activate_fringe(self, fringe_name: str, fringe_type: str) -> bool:

		"""

		This method makes active a fringe bar with a given name the window. It works for the active page.


		Parameters
		----------
		fringe_name : str
			Name of the fringe.

		fringe_type : str
			Type of the fringe bar. Its possible values are:
			- 'scalar'
			- 'vector'.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def apply_view(self, view_name: str) -> bool:

		"""

		This method applies a view with a given name on a window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def save_view(self, view_name: str) -> bool:

		"""

		This method saves the view of the window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete_view(self, view_name: str) -> bool:

		"""

		This method deletes the view of the window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def translate_view(self, view_name: str, translation_vector: object) -> bool:

		"""

		This method translates the view of the window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		translation_vector : object
			A list with three floats, with the translation coordinates (X, Y, Z)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def rotate_view(self, view_name: str, rotation_angles: object) -> bool:

		"""

		This method rotates the view of the window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		rotation_angles : object
			A list with three floats, for the rotation around each axis (X, Y, Z)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def export_view(self, view_name: str, filename: str) -> bool:

		"""

		This method exports to a file the view of the window. It works only for the active page.


		Parameters
		----------
		view_name : str
			Name of the view.

		filename : str
			The name of the file.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def import_view(self, filename: str) -> bool:

		"""

		This method imports a view from a file. It works only for the active page.


		Parameters
		----------
		filename : str
			The name of the file.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def pick_isofunctions(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick isofunctions from the window. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Isofunction referring to one specific picked isofunction of the window.Upon failure, an empty list is returned.

		"""


	def pick_curves(self, message: str, settings: object) -> object:

		"""

		This methid allows the user to pick curves from the 2d plot window. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Curve referring to one specific picked curve of the 2d plot window.Upon failure, an empty list is returned.

		"""


	def pick_points(self, message: str, all_curves: bool, curve_type: str) -> object:

		"""

		This method allows the user to pick points and from all or one curve from the 2d plot window. The execution of the script will stop and it will restart when Enter is pressed. If the option all_curves is set to false, then the following actions must be performed once the selection process has begun:1. Left-Click on Curve to select a curve. 2. Middle-Click to confirm selection. 3. Middle-Click to select the points of the curve. 4. Enter to exit the function. If all_curves is not set, or set to False, then the following actions must be performed once the selection process has begun: 1. Middle-Click to select the points of the curve. 2. Enter to exit the function. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user when the function is called.

		all_curves : bool, optional
			If all_curves is True, then points from all curves can be selected

		curve_type : str, optional
			Type of the curve. Possible values are:
			- 'real' (default)
			- 'imaginary'
			- 'magnitude'
			- 'phase'

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Point referring to one specific picked point. Upon failure, an empty list is returned.

		"""


	def set_isofunctions_settings(self, settings: object) -> bool:

		"""

		This method sets settings to all isofunctions of the window. This method works for the active page.


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


	def set_annotations_settings(self, settings: object, annotations: object) -> bool:

		"""

		This method sets settings to all annotations of the window. This method works for the active page.


		Parameters
		----------
		settings : object
			Settings (key-value) of the annotation.
			A dictionary with string keys and string values:
			- 'anchor_none': Anchor none
			- 'anchor_pointer': Anchor relative to pointer (float value,float value)
			- 'anchor_scrbotleft': Anchor relative to bottom left of screen (float value,float value)
			- 'anchor_scrbotright': Anchor relative to bottom right of screen (float value,float value)
			- 'anchor_scrtopright': Anchor relative to top right pointer (float value,float value)
			- 'anchor_scrtopleft': Anchor relative to top left pointer (float value,float value)
			- 'background_auto_color': Background automatic color
			- 'background_color': Background color (string value)
			- 'background_function_color': Function used for coloring ('default', 'funcval', 'scalfuncval', 'vecfuncval', 'cmax', 'cmin', 'dispx', 'dispy', 'dispz', 'disptot')
			- 'background_expression_color': Expression or annotation variable used for coloring (string value)
			- 'background_transparency': Background transparency (float value)
			- 'border_color': Border color (string value)
			- 'border_color_pident': Border pid/curve color (0,1)
			- 'border_padding': Border padding (float value)
			- 'border_width': Border width (float value)
			- 'border_rounded': Style of border corners (0,1)
			- 'hide_shadowed': Hide Shadowed Option (0,1)
			- 'line_color': Line color (string value)
			- 'line_width': Line width (float value)
			- 'model_visibility': Model dependent visibility (0,1)
			- 'planecut_height': Plane cut height (integer value)
			- 'planecut_width': Plane cut width (integer value)
			- 'planecut_rotate': Rotate plane cut (float value)
			- 'planecut_draw': Draw plane cur (0,1)
			- 'pointer_color': Pointer color (string value)
			- 'pointer_color_pident': Pointer pid/curve color (0,1)
			- 'pointer_size': Pointer size (float value)
			- 'pointer_style': Pointer style ('arrow', 'box', 'circle', 'cross', 'none', 'x')
			- 'pointer_visibility': Show pointer (0,1)
			- 'position_xy': Position (float value, float value)
			- 'size': Size (integer value)
			- 'text_align': Text alignment ('center', 'left', 'right')
			- 'text_color': Text color (string value)
			- 'text_color_pident': Text pid/curve color (0,1)
			- 'title_color': Title color (string value)
			- 'title_color_pident': Title pid/curve color
			- 'title_font': Title font (string value)
			- 'title_format': Title format ('auto', 'fixed', 'scientific')
			- 'title_htmltext': Title html text (string value)
			- 'title_precision': Title precision digits (integer value)
			- 'title_text': Title text
			- 'title_vertical': Draw vertical text (0,1)
			- 'title_visibility': Title visibility ('auto', 'on', 'off')
			- 'circular': Circular shape (0,1)
			- 'circular_size': Circular Shape Size (integer value)
			- 'circular_multiplier': Circular Shape Size Multiplier (integer value)
			- 'circular_initial': Limit to initial (0,1)

		annotations : object, optional
			The annotations of the window that are going to be affected.
			Acceptable values are:
			- 'all' : all the annotations (default value).
			- 'selected' : the selected annotations.
			- 'visible' : the visible annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_images_settings(self, settings: object) -> bool:

		"""

		This method sets settings to all images of the window. This method works for the active page.


		Parameters
		----------
		settings : object
			Settings (key-value) of the image.
			A dictionary with string keys and string values:
			 - 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
			- 'align_hoffset': Horizontan offset (float)
			- 'align_voffset': Vertical offset (float)
			- 'autoscale': Scale with window resize (0,1)
			- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
			- 'filter_transparent': Transparency (integer)
			- 'pixel_aspect': Pixel Aspect ratio (float)
			- 'zorder': Z order (integer)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_videos_settings(self, settings: object) -> bool:

		"""

		This method sets settings to all videos of the window. This method works for the active page.


		Parameters
		----------
		settings : object
			Settings (key-value) of the image.
			A dictionary with string keys and string values:
			- 'align': Align Video to Window ('bottom', 'top', 'left', 'right', 'center')
			- 'align_hoffset': Horizontan offset (float)
			- 'align_voffset': Vertical offset (float)
			- 'autoscale': Scale with window resize (0,1)
			- 'filter': Video Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
			- 'filter_transparent': Transparency (integer)
			- 'swaprgb': Swap Video Colors (0,1)
			- 'pixel_aspect': Pixel Aspect ratio (float)
			- 'zorder': Z order (integer)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_plots_settings(self, settings: object) -> bool:

		"""

		This method sets settings to all plots of the window. This method works for the active page.


		Parameters
		----------
		settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'border_width' : 3 , 'legend' : 1, 'border_color' : 'blue'}). The names of the plot settings and its possible values are:
			- 'border_width': Border line width (integer value)
			- 'border_color': Border color (string value)
			- 'complex_height': Complex plot height (integer value)
			- 'curves_palette': Color palette for selected curves (string value)
			- 'dna_palette': Palette for dna plot (string value)
			- 'mac_palette': Palette for mac plot (string value)
			- 'legend': Legend (0,1)
			- 'locktitles': Lock titles from read file (0,1)
			- 'margin_up': Plot up margin (float value)
			- 'margin_down': Plot down margin (float value)
			- 'margin_left': Plot left margin (float value)
			- 'margin_right': Plot right margin (float value)
			- 'plot_palette_counter': Plot palette counter
			- 'plot_type': Plot type ('plain', 'magphase', 'realimag', 'polar', 'horiz', 'dna', 'mac', 'horizontal', 'colormap', '3dmac', 'waterfall', 'nyquist')
			- 'point_show': Show model point (0,1)
			- 'polar_size': Polar size (0,1)
			- 'show_current': Show only current line (0,1)
			- 'sync_value': Show model value and sync line (0,1)
			- 'model_value': Show model value (0,1)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_curves_settings(self, settings: object) -> bool:

		"""

		This method sets settings to all curves of the window. This method works for the active page.


		Parameters
		----------
		settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'options_width' : 6 , 'assign_xaxis' : 2 , 'curve_color' : 'blue'}). The names of the curve settings and its possible values are:
			- 'assign_xaxis': Set X axis assignment (integer value)
			- 'assign_yaxis': Set Y axis assignment (integer value)
			- 'baroffset': Use X axis offset for bars (0,1)
			- 'bartype': Convert curve to bar chart (0,1)
			- 'barwidth': Bar width (integer value)
			- 'curve_color': Curve color (string value)
			- 'entity_id': Change id of entity (integer value)
			- 'entity_ip': Change integration point of entity (integer value)
			- 'entity_secid': Change secondary id of entity (integer value)
			- 'entity_type': Change entity type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe',
			- 'seatbelt', 'section', 'shell', 'solid', 'spc')
			- 'entity_sectype': Change entity secondary type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', 'force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe', 'seatbelt', 'section', 'shell', 'solid', 'spc')
			- 'fill': Fill bar type curve (0,1)
			- 'linewidth': Curve width (integer value)
			- 'mark': Curve mark (string value)
			- 'mark_number': Curve mark number (integer value)
			- 'point_precision_digits': Point precision digits (integer value)
			- 'point_precision_type': Point precision type ('auto', 'fixed', 'sciauto', 'scientific')
			- 'point_size': Point size (integer value)
			- 'follow_identify': Curve style follows identify format
			- 'point_font': Point font (string value)
			- 'point_size': Point size (integer value)
			- 'point_style': Point style (integer value)
			- 'style': Curve style (integer value)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show_curves(self, curves: object) -> bool:

		"""

		This function allows the user to make visible some specific curves of the 2d plot window.


		Parameters
		----------
		curves : object
			A list with objects of class Curve.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def hide_curves(self, curves: object) -> bool:

		"""

		This function allows the user to hide some specific curves of the 2d plot window.


		Parameters
		----------
		curves : object
			A list with objects of class Curve.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def select_curves(self, curves: object) -> bool:

		"""

		This function allows the user to select some specific curves of the 2d plot window.


		Parameters
		----------
		curves : object
			A list with objects of class Curve.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def deselect_curves(self, curves: object) -> bool:

		"""

		This function allows the user to deselect some specific curves of the 2d plot window.


		Parameters
		----------
		curves : object
			A list with objects of class Curve.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete_curves(self, curves: object) -> bool:

		"""

		This function allows the user to delete some specific curves of the 2d plot window. This method works for the active page.


		Parameters
		----------
		curves : object
			A list with objects of class Curve.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def get_type(self) -> str:

		"""

		This method gets the type of the window.


		Returns
		-------
		str
			Upon success, it returns the type of the window. For a 3d window, it returns '3d' for a 2d window it returns '2d' and for a text window it returns 'text'.

		"""


	def get_novalue_color(self) -> object:

		"""

		This method gets the novalue color of the scalar fringebar in the window.


		Returns
		-------
		object
			Upon success, it returns an object of class Color, that represents the no value color of the scalar fringebar. Upon failure it return None.

		"""


	def set_novalue_color(self, color: object) -> bool:

		"""

		This method sets the novalue color of the scalar fringebar in the window.


		Parameters
		----------
		color : object
			An object of class Color.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure it returns False.

		"""


	def get_size(self) -> object:

		"""

		This method gets the size of the window.


		Returns
		-------
		object
			It returns a list of two integers. The first is the window width and the second the window height

		"""


	def is_maximized(self) -> bool:

		"""

		This method returns if the window is maximized or not.


		Returns
		-------
		bool
			If the window is maximized, it returns True. Else it returns False.

		"""


	def is_minimized(self) -> bool:

		"""

		This method returns if the window is minimized or not.


		Returns
		-------
		bool
			If the window is minimized, it returns True. Else it returns False.

		"""


	def is_docked(self) -> bool:

		"""

		This method returns if the window is docked or not.


		Returns
		-------
		bool
			If the window is docked, it returns True. Else it returns False.

		"""


	def set_size(self, size: object) -> bool:

		"""

		This method sets the size of the window. It works for the active page.


		Parameters
		----------
		size : object
			A tuple, or a list with two integers. The first is the height and the second the width.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def maximize(self) -> bool:

		"""

		This method maximizes the window. It works only for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def minimize(self):

		"""

		This method minimizes the window. It works only for the active page.


		"""


	def restore(self) -> bool:

		"""

		This method restores the window. If it is maximized, it will un-maximize it, and if it is minimized, it will un-minimize it. It works only for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def dock(self) -> bool:

		"""

		This method docks the window. It works only for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def undock(self) -> bool:

		"""

		This method un-docks the window. It works only for the active page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_plot_layout(self, layout: int) -> bool:

		"""

		This method sets the layout of a 2d plot window


		Parameters
		----------
		layout : int
			An integer for different layout types (1-24)

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	@classmethod
	def get_top_down(cls) -> bool:

		"""

		This method gets the "top to bottom" property of the window.


		Returns
		-------
		bool
			If the plots layout begins from top left corner, it returns True. Else it returns False.

		"""


	def pick_plots(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick plots from the 2d plot window. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Plot referring to one specific picked Plot of the 2d plot window. Upon failure, an empty list is returned.

		"""


	def pick_3d_positions(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick 3d positions in a 3d window. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed. This method works for the active page.


		Parameters
		----------
		message : str
			Message displayed to the user when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is a tuple of x, y, z coordinates refering to a picked position. Upon failure, an empty list is returned.

		"""


	def get_text(self, evaluated: bool, html: bool) -> str:

		"""

		Get text from Text Editor


		Parameters
		----------
		evaluated : bool, optional
			If false then the unevalulated text is returned. If true then the evaluated is returned. Optional value is true.

		html : bool, optional
			If false then the plain text is returned. If true then the html text is returned. Optional value is false.

		Returns
		-------
		str
			The  text of the Text Editor window.

		"""


	def get_param_point_list(self, model_number: int, resultset: object) -> object:

		"""


		Parameters
		----------
		model_number : int, optional
			If defined, the list will only contain parametric points that belong to that model

		resultset : object, optional
			The parametric point values and attributes are defined by the resultset provided

		Returns
		-------
		object
			A list with parametric point objects is returned.Upon failure the list is empty

		"""


	def save_image(self, file: str, format: str, size: str, orientation: str, background: str) -> object:

		"""

		This method allows the user to save the window as an image.


		Parameters
		----------
		file : str
			The filename of the image.

		format : str, optional
			The format of the file. Accepted values are:
			- 'png'
			- 'jpeg'
			- 'gif'
			- 'bmp'
			- 'eps'
			- 'ppm'
			- 'rgb'
			- 'tiff'
			Default value is 'png'.

		size : str, optional
			The size of the image. Accepted values are:
			- any tuple of two integers as (width, height)
			- 'current_size'
			- 'A0'
			- 'A1'
			- 'A2'
			- 'A3'
			- 'A4'
			- 'A5'
			- 'Letter'
			- 'Legal'
			- 'Executive'
			- 'Tabloid'
			- 'PAL(720x576)'
			- 'NTSC(720x480'
			- strings in 'widthxheight' format.
			The default value is 'current_size'.

		orientation : str, optional
			The orientation of the image. Accepted values are:
			- portrait
			- landscape

		background : str, optional
			The color of the image background. Accepted values are:
			- transparent : transparent backgrount
			- window_color : the color of the window.
			- Color name (e.g. 'White').
			Default value is 'White'

		Returns
		-------
		object
			Returns None.

		"""


	def save_video(self, file: str, format: str, size: str, orientation: str, background: str, loop_direction: str, loops: int) -> object:

		"""

		This method allows the user to save a video of the window.


		Parameters
		----------
		file : str
			The filename of the video.

		format : str, optional
			The format of the file. Accepted values are:
			- 'avi'
			- 'mpeg2'
			- 'mpeg4'
			- 'gif'
			Default value is 'mpeg4'.

		size : str, optional
			The size of the image. Accepted values are:
			- any tuple of two integers as (width, height)
			- 'current_size'
			- 'A0'
			- 'A1'
			- 'A2'
			- 'A3'
			- 'A4'
			- 'A5'
			- 'Letter'
			- 'Legal'
			- 'Executive'
			- 'Tabloid'
			- 'PAL(720x576)'
			- 'NTSC(720x480'
			- strings in 'widthxheight' format.
			The default value is 'current_size'.

		orientation : str, optional
			The orientation of the image. Accepted values are:
			- portrait
			- landscape

		background : str, optional
			The color of the image background. Accepted values are:
			- transparent : transparent backgrount
			- window_color : the color of the window.
			- Color name (e.g. 'White').
			Default value is 'White'

		loop_direction : str, optional
			The direction of the states loop. Accepted values are:
			- 'forward'
			- 'backward'
			- 'forward_and_backward'
			Default value is 'forward'.

		loops : int, optional
			The number of the loops of the video. Default value is 1.

		Returns
		-------
		object
			Returns None.

		"""


	def get_parametric_point_paths(self, specifier: str) -> object:

		"""

		This method gets the Parametric Point Paths of the window.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all parametric point paths of window (default value).

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class ParametricPointPath referring to one specific parametric point path of the window. Upon failure, an empty list is returned.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Window entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def delete_annotations(self, annotations: object) -> object:

		"""

		This methods deletes annotations of the window.


		Parameters
		----------
		annotations : object
			The annotations of the window that are going to be deleted.
			Acceptable values are:
			- 'all' : deletes all the annotations.
			- 'visible' : deletes the visible annotations.
			- 'selected' : deletes the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""


	def show_annotations(self, annotations: object) -> object:

		"""

		This method shows annotations of the window.


		Parameters
		----------
		annotations : object
			The annotations of the window that are going to be shown.
			Acceptable values are:
			- 'all' : shows all the annotations.
			- 'selected' : shows the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""


	def hide_annotations(self, annotations: object) -> object:

		"""

		This method hides annotations of the window.


		Parameters
		----------
		annotations : object
			The annotations of the window that are going to be hidden.
			Acceptable values are:
			- 'all' : hides all the annotations.
			- 'visible' hides the visible annotations.
			- 'selected' : hides the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""


	def get_view_side_vector(self, view_name: str) -> object:

		"""

		This method gets the side vector (X,Y,Z) of a view of the window. 


		Parameters
		----------
		view_name : str
			The name of the view.

		Returns
		-------
		object
			Upon success, it returns a list with three members, where each member of the list is a float referring to the X, Y and Z. Upon failure, an empty list is returned.

		"""


	def get_screen_position(self, x_pos: float, y_pos: float, z_pos: float) -> object:

		"""

		This method takes a 3d position on window and returns the corresponding relative screen coordinates.


		Parameters
		----------
		x_pos : float
			X position of window coordinates

		y_pos : float
			Y position of window coordinates

		z_pos : float
			Z position of window coordinates

		Returns
		-------
		object
			It returns a list of two integers. The first is the relative horizontal screen coordinate and the second the relative vertical screen coordinate.

		"""


	def get_best_views(self, elements: object) -> dict:

		"""

		This method gets the names of all the newly created views by the command "view best seek elements ...". This method works for the active page.


		Parameters
		----------
		elements : object
			A list of element objects.

		Returns
		-------
		dict
			Upon success, it returns a dictionary having as keys the names of the newly created views of the specified window and as values a list of the element ids belonging to that view. Upon failure, an empty dictionary is returned.

		"""


	def save_curves(self, curves: object, filename: str, format: str) -> object:

		"""

		This method allows the user to save the window curves.


		Parameters
		----------
		curves : object
			A list of curves.

		filename : str
			The filename.

		format : str
			The format of the file. Accepted values are:
			'atfx',
			'column',
			'diadem',
			'exportmove',
			'isoegv',
			'isotr13499',
			'isov11', 'isots13499',
			'keyword',
			'pamcrashascii',
			'pamfunct',
			'tabled',
			'unv58'

		Returns
		-------
		object
			Returns None.

		"""

class ParamPoint():

	"""

	Class for param_points. 

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		from meta import results
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    print(pnt)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import results
		from meta import windows
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    win = pnt.get_window()
		    print(win)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import windows
		from meta import results
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    pag = pnt.get_page()
		    print(pag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import windows
		from meta import results
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    attribute_name = "Type"
		    attr = pnt.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import results
		from meta import windows
		
		
		def main():
		    model_id = 0
		    param_point_id = 1
		    all_resultsets = results.Resultsets(model_id)
		    result = all_resultsets[1]
		    window_name = "MetaPost"
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    attribute_type = "numerical"
		    attribute_name = "extra"
		    attribute_value = 30
		    ret = pnt.set_attribute(attribute_type, attribute_name, attribute_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import models
		from meta import windows
		
		
		def main():
		    m = models.Model(0)
		    window_name = "MetaPost"
		    param_point_id = 1
		    result = m.get_current_resultset()
		    pnt = windows.ParamPointFromId(window_name, param_point_id, result)
		    ret = pnt.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        name="LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    ret = ppath.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    win = windows.Window(name="MetaPost", page_id=0)
		    ret = win.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the param point

	"""

	elem_id: int = None
	"""
	Element Id where param point is on

	"""

	elem_type: int = None
	"""
	Element Type where param point is on

	"""

	elem_seqid: int = None
	"""
	Second id of the element. Some element types may have a second id (e.g. GAP, TUBE, JOINT). For the rest element types, the value of second_id is -1.

	"""

	elem_subtype: int = None
	"""
	Element subtype where param point is on

	"""

	elem_model: int = None
	"""
	Element model number where param point is on

	"""

	x: float = None
	"""
	X coordinate of the param point

	"""

	y: float = None
	"""
	Y coordinate of the param point

	"""

	z: float = None
	"""
	Z coordinate of the param point

	"""

	dx: float = None
	"""
	Disp X coordinate of the param point

	"""

	dy: float = None
	"""
	Disp Y coordinate of the param point

	"""

	dz: float = None
	"""
	Disp Z coordinate of the param point

	"""

	dt: float = None
	"""
	Total disp coordinate of the param point

	"""

	stop: float = None
	"""
	Scalar Top value of param point

	"""

	sbot: float = None
	"""
	Scalar Bottom value of param point

	"""

	vtop: float = None
	"""
	Vector Top value of param point

	"""

	vbot: float = None
	"""
	Vector Bottom value of param point

	"""

	orig_x: float = None
	"""
	Unprojected position X of parametric point as defined at parametric path.

	"""

	orig_y: float = None
	"""
	Unprojected position Y of parametric point as defined at parametric path.

	"""

	orig_z: float = None
	"""
	Unprojected position Z of parametric point as defined at parametric path.

	"""

	def get_window(self) -> object:

		"""

		This method gets the window of the parametric point. 


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the parametric point. Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the parametric point. 


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the parametric point. Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the parametric point.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is another list referring to one specific attribute of the parametric point.  In position 0, internal lists contain a string referring to the name of the attribute. In position 1, internal lists contain a string referring to the value of the attributes. Upon failure, an empty list is returned.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the parametric point. If the given attribute does not exist it is automatically created and its value is set.


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


	def get_deformations(self, resultset: object) -> object:

		"""

		This method gets the deformations of the parametric point, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		Returns
		-------
		object
			Upon success, it returns a tuple with the deformations (dtotal, dx, dy, dz). Upon failure, it returns None.

		"""


	def get_scalar(self, resultset: object, layer: str) -> float:

		"""

		This method gets the nodal value of the parametric point, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the scalar values on surface. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		float
			Upon success, it returns the scalar value of the parametric point. Upon failure, it returns None.

		"""


	def get_vector(self, resultset: object, layer: str) -> object:

		"""

		This method gets the vector values of the node, for the specified resultset.


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		layer : str, optional
			Location of the vector values on surface. Possible values are:
			- 'bottom' (default)
			- 'top'

		Returns
		-------
		object
			Upon success, it returns a tuple with the deformations (vtotal, vx, vy, vz). Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META ParamPoint entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class ParametricPointPath():

	"""

	Class for Parametric Point Paths.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    print(ppath)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    page = ppath.get_page()
		    print(page)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    win = ppath.get_window()
		    print(win)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    attr = ppath.get_attributes()
		
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    ok = ppath.set_attribute("test", "string", "123")
		    print(ok)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    ppath.delete()
		
		
		if __name__ == "__main__":
		    main()
		# method: get_fitting_circle
		# PYTHON script
		import meta
		from meta import windows
		
		
		def main():
		    ppath = windows.ParametricPointPath(
		        "LINE_PATH_1", window_name="MetaPost", page_id=0
		    )
		    circle = ppath.get_fitting_circle()
		
		    print(circle)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the Parametric Point Path.

	"""

	def get_window(self) -> object:

		"""

		This method gets the window of the parametric point path.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the parametric point path. Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the parametric point path. 


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the parametric point path. Upon failure, it returns None.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the parametric point path.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is another list referring to one specific attribute of the parametric point path. In position 0, internal lists contain a string referring to the name of the attribute. In position 1, internal lists contain a string referring to the value of the attributes. Upon failure, an empty list is returned.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the parametric point path. If the given attribute does not exist it is automatically created and its value is set.


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


	def delete(self) -> object:

		"""

		This method deletes the Parametric Point Path.


		Returns
		-------
		object
			Returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META ParametricPointPath entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def get_fitting_circle(self) -> object:

		"""

		This method caclulates the fitting circle for the parametric  path points and returns the center,normal and radius of that circle.


		Returns
		-------
		object
			Upon success, it returns a python dictionary that contains center, normal and radius information. The item with 'center' key is a python array of 3 values which define the circle center.The item with 'normal' key is a python array of 3 values which define the circle normal.The item with 'radius' key is a float number that defines the radius  of the circle.

		"""

