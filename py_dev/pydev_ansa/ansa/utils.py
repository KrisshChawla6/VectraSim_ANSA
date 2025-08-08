from __future__ import annotations
from typing import *

def CreateCurve() -> object:

	"""

	This function creates a new curve object.

	Returns
	-------
	object
		Upon success, it returns a Class object referring to the newly created curve.
		Else, None is returned.

	See Also
	--------
	utils.AddCurveData

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def DeckInfo(filename: str, mode: str, text_format: str, active_options: object, threshold_values: object, parameter_values: object, f11_sync: object) -> int:

	"""

	This function saves a deck info report in a file.

	Parameters
	----------
	filename : str
		The path and the filename to be saved.

	mode : str
		Accepted values: 'VISIBLE', 'SELECTED', 'MODEL' or 
		'WHOLE DB'.

	text_format : str
		Accepted values: 'HTML', 'TEXT', 'CSV' or 'PDF'.

	active_options : object, optional
		A python list of string items. 
		Accepted string values: the values should be equal to the deck info ansa settings keywords or the gui labels in the deck info window.

	threshold_values : object, optional
		A python dictionary.
		The dictionary key is a string equal to the deck info ansa settings keywords or the gui labels in the deck info window.
		The dictionary value is a csv string with the threshold values.

	parameter_values : object, optional
		A python dictionary.
		This argument is used to set the values parameter values in the Model Tab of deck info
		The dictionary key is a string equal to the deck info ansa settings keyword or the gui labels in Model Info column of the deck info window.
		The dictionary value is a single string value or a csv string.
		For parameter values, which support results in tabular form, such as Properties, Includes and Parts, the configuration table field which is going to be the sort criterion and the desired sort order can be specified via a dictionary entry.
		The dictionary key is the gui label in Model Info Column of the deck info window followed by the suffix '_sort'.
		The dictionary value is a string with the gui label of the desired sort criterion as appears in the corresponding Deck Info Configuration Table field followed by the sort order.

	f11_sync : object, optional
		A python dictionary.
		This argument is used to activate the 'Sync from F11' options in the deck info window Shell and Solid Tab. 
		The dictionary key is a string equal to 'Shell' or 'Solid' which indicates the affected quality critiria.
		The allowed dictionary values are 'Selected' or 'All'
		Using this argument may overwrite some options set in the options_values and threshold_values parameters.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # will create a file with name "/home/users/deck_report" of format html.
		    options = ["header_footer", "Materials", "Properties"]
		    # the fisrt item of the list is equal to a deck info ansa settings keyword
		    # the second item is equal to the label in the deck info window
		    thr = {"Aspect": "10,11,12,13,14,15"}
		    # the dictionary key is a string equal to a gui label and the
		    # dictionary value is a csv string
		    param = {"Number Precision": "5", "Graph orientation": "Vertical"}
		    param["Number format"] = "Exponent"
		    param["Text delimiter"] = "XXX"
		    param["Property image"] = "Property Only,MID,Width=300,Height=300"
		    param["Properties"] = "No. , Total, PID, Image"
		    param["Properties_sort"] = "PID,Descending"
		    sync = {"Shell": "Selected", "Solid": "All"}
		
		    m = utils.DeckInfo(
		        "/home/users/deck_report.html", "SELECTED", "HTML", options, thr, param, sync
		    )


	"""

def GetFileInfoFromAnsaDB(ansa_db_file_name: str):

	"""

	Given the path to an ANSA database, this function extracts its file creation information.
	This information is given by 'tag' parameters and values.

	Parameters
	----------
	ansa_db_file_name : str
		The file path.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    file_name = "/home/user/my_ansa_db.ansa"
		    info = utils.GetFileInfoFromAnsaDB(file_name)
		
		    print("Number of information parameters in: '" + file_name + "' = " + len(info))
		    for k, v in info.items():
		        print("'" + k + "': '" + v + "'")


	"""

def GetParametersFromAnsaDB(ansa_file_name: str) -> object:

	"""

	Creates a map with parameter's name as key and parameter's value as data.

	Parameters
	----------
	ansa_file_name : str
		A string to declare the file path.

	Returns
	-------
	object
		Returns a dictionary containing the ansa-parameters (parameter's name as key and parameter's value as data) that are defined in an ANSA database.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    aparams = utils.GetParametersFromAnsaDB("/home/user/my_db.ansa")
		    print("number of parameters in: '" + file_name + "' = " + len(aparams))
		
		    for k, v in aparams.items():
		        print("'" + k + "':     '" + v + "'")


	"""

def Merge(filename: str, filenames: object, directory: str, property_offset: str, material_offset: str, set_offset: str, merge_sets_by_name: bool, paste_nodes_by_name: bool, paste_nodes_by_name_tolerance: float, paste_cons_by_name: bool, merge_parts: bool, autoposition_parts: bool, create_instances: bool, model_action: str, coord_offset: str, node_offset: str, auto_fit_models: bool, propsection_offset: str, eos_offset: str, hourglass_offset: str, function_offset: str) -> int:

	"""

	This function merges a single ANSA database into an existing one, based on a series
	of user defined arguments.

	Parameters
	----------
	filename : str, optional
		Contains the full path to the ANSA database to be
		imported and merged.

	filenames : object, optional
		Contains a list of strings that descibe full paths to
		the ANSA database to be imported and merged.

	directory : str, optional
		Contains the path to a directory, where ANSA will 
		look for any files to be imported and merged.

	property_offset : str, optional
		Determines the action to be taken when property conflicts are noticed 
		during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'keep-old')

	material_offset : str, optional
		Determines the action to be taken when material conflicts are noticed 
		during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'keep-old')

	set_offset : str, optional
		Determines the action to be taken when set conflicts are noticed 
		during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'keep-old')

	merge_sets_by_name : bool, optional
		Determines whether sets are going to be marged based on their name.
		(Default: False)

	paste_nodes_by_name : bool, optional
		Determines whether nodes are going to be pasted based on their name.
		(Default: False)

	paste_nodes_by_name_tolerance : float, optional
		Determines the tolerance to be used when nodes are going to be pasted 
		based on their name. (paste_nodes_by_name=True)

	paste_cons_by_name : bool, optional
		Determines whether cons are going to be pasted based on their name.
		(Default: False)

	merge_parts : bool, optional
		Determines whether conflicting parts are going to be merged or not.
		(Default: False)

	autoposition_parts : bool, optional
		Determines whether multi-instantiated parts will be 
		autopositioned or not.
		(Default: 'off')

	create_instances : bool, optional
		Determines whether two parts with the same Id or name will be merged 
		or a new instance of the part will be created.

	model_action : str, optional
		Accepted values: "overwrite_model", "merge_model", 
		"new_model_in_active_window", "new_model_in_new_window",
		"new_model_in_enabled_windows", "separate_models_in_active_window",
		"separate_models_in_new_window" or
		"separate_models_in_enabled_windows"
		(Default: "merge_model")

	coord_offset : str, optional
		Determines the action to be taken when coordinate system conflicts
		are noticed during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'offset')

	node_offset : str, optional
		Determines the action to be taken when node conflicts
		are noticed during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'offset')

	auto_fit_models : bool, optional
		Determines whether merge models will be autopositioned or not.
		(Default 'true')

	propsection_offset : str, optional
		Determines the action to be taken when prop/section conflicts
		are noticed during the merge.
		Accepted values: 'offset', 'keep-new' or 'keep-old'.
		(Default: 'offset')

	eos_offset : str, optional
		Accepted values: "offset", "keep-old" or "keep-new" 
		(Default: "offset")

	hourglass_offset : str, optional
		Accepted values: "offset", "keep-old" or "keep-new" 
		(Default: "offset")

	function_offset : str, optional
		Accepted values: "offset", "keep-old" or "keep-new" 
		(Default: "offset")

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.Merge(
		        filename="Z:/temp/users/data.ansa",  # Full path to the ANSA database to be merged
		        directory="Z:/temp/users/user1/",  # Full path to a directory that contains ANSA databases to be merged
		        property_offset="keep-new",  # New, incoming, property ids will be kept
		        material_offset="keep-old",  # Old, existing, material ids will be kept
		        set_offset="offset",  # Incoming sets will have their ids offset, in case of conflicts
		        merge_sets_by_name=True,  # Do not merge sets based on their name
		        paste_nodes_by_name=True,  # Paste nodes based on their name
		        paste_nodes_by_name_tolerance=0.02,  # Tolerance to be used when pasting nodes
		        paste_cons_by_name=False,  # Do not paste masegms based on name matches
		        merge_parts=True,  # Marge parts in the case of conflicts
		        autoposition_parts=False,
		    )  # Do not autoposition multi-instantiated parts


	"""

def OpenPartManager(view_mode: str) -> int:

	"""
	.. deprecated:: 17.0.0
		Use :py:func:`OpenModelBrowser` instead.


	Opens the part manager window.

	Parameters
	----------
	view_mode : str, optional
		Accepted values: 'list_view', 'tree_view' or 'icon_view'.

	Returns
	-------
	int
		Always returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open part manager in tree view
		    utils.OpenPartManager("tree_view")


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:func: OpenModelBrowser instead.", DeprecationWarning)

def PrintToFile(filename: str, image_format: str, red: int, green: int, blue: int, transparent: bool, text_axes: bool, gradient: bool) -> int:

	"""
	.. deprecated:: 18.0.0
		Use :py:func:`SnapShot` instead.


	The PrintToFile function grabs the whole screen of ANSA's graphics window and saves it as an image in the specified file.

	Parameters
	----------
	filename : str
		The filename to be saved. This argument is mandatory.
		If filename exists, it will be overwritten.

	image_format : str, optional
		'POSTSCRIPT', 'RGB', 'TIFF', 'JPEG', 'PNG', 'BMP'.

	red : int, optional
		The number of the red component of the background color [0-255].

	green : int, optional
		The number of the green component of the background color [0-255].

	blue : int, optional
		The number of the blue component of the background color [0-255].

	transparent : bool, optional
		True or False, to enable or disable trasparent background.
		(available for png image format only)

	text_axes : bool, optional
		Text and axes visible or not.

	gradient : bool, optional
		Leaves gradient visible or not.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    status = utils.PrintToFile(
		        filename="/home/users/image1.png", image_format="PNG", transparent=True
		    )
		    if status == 0:
		        print("Image saved in /home/users/image1.png")
		
		
		# ...or...
		
		
		def main():
		    status = utils.PrintToFile(
		        filename="/home/users/image1.png", red=100, green=140, blue=210, text_axes=True
		    )
		    if status == 0:
		        print("Image saved in /home/users/image1.png")


	"""

	import warnings; warnings.warn("Deprecated since version 18.0.0. Use :py:func: SnapShot instead.", DeprecationWarning)

def SetDrawingAreaColor(r_int: int, g_int: int, b_int: int) -> int:

	"""

	Sets the RGB values for the color of drawing area to be r, g and b.

	Parameters
	----------
	r_int : int
		The value for red (0 - 255).

	g_int : int
		The value for green (0 - 255).

	b_int : int
		The value for blue (0 - 255).

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.SetDrawingAreaColor(50, 100, 150)


	"""

def VtrapsBubbles(step_type: int, forced_step: float, calculation_angle_rx1: float, calculation_angle_ry1: float, calculation_angle_rz1: float, printout_angle_rx2: float, printout_angle_ry2: float, printout_angle_rz2: float, printout_filename: int, printout_file_format: int) -> object:

	"""

	Script function for the calculation of bubble traps in VTRAPS tool and a printout of the results. 
	User specifies two positions, one for the calculation and one for the display of the results for 
	the image printout.

	Parameters
	----------
	step_type : int
		0 for imposed step 1 for auto step.

	forced_step : float
		The forced step value.

	calculation_angle_rx1 : float
		The x coordinate of the calculation angle.

	calculation_angle_ry1 : float
		The y coordinate of the calculation angle.

	calculation_angle_rz1 : float
		The z coordinate of the calculation angle.

	printout_angle_rx2 : float
		The x coordinate of the printout angle.

	printout_angle_ry2 : float
		The y coordinate of the printout angle.

	printout_angle_rz2 : float
		The z coordinate of the printout angle.

	printout_filename : int
		The path where the printout will be saved.

	printout_file_format : int
		The format of the printout file to save.

	Returns
	-------
	object
		Returns the image file.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.VtrapsBubbles(0, 0.5, 0.0, 2.5, 0.0, 0.0, 90.0, 0.0, "./image.tiff", "TIFF")


	"""

def VtrapsPonds(step_type: int, forced_step: float, calculation_angle_rx1: float, calculation_angle_ry1: float, calculation_angle_rz1: float, printout_angle_rx2: float, printout_angle_ry2: float, printout_angle_rz2: float, printout_filename: str, printout_file_format: str) -> object:

	"""

	Function for the calculation of pond traps in VTRAPS tool and a printout of the results.
	User specifies two positions, one for the calculation and one for the display of the results for the image printout.

	Parameters
	----------
	step_type : int
		0 for imposed step, 1 for auto step.

	forced_step : float
		The forced step value.

	calculation_angle_rx1 : float
		The x coordinate of the calculation angle.

	calculation_angle_ry1 : float
		The y coordinate of the calculation angle.

	calculation_angle_rz1 : float
		The z coordinate of the calculation angle.

	printout_angle_rx2 : float
		The x coordinate of the printout angle.

	printout_angle_ry2 : float
		The y coordinate of the printout angle.

	printout_angle_rz2 : float
		The z coordinate of the printout angle.

	printout_filename : str
		The path where the printout will be saved.

	printout_file_format : str
		The format of the printout file to save.

	Returns
	-------
	object
		Returns the image file.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.VtrapsPonds(0, 0.5, 0.0, 2.5, 0.0, 0.0, 90.0, 0.0, "./image.tiff", "TIFF")


	"""

def SnapShot(filename: str, image_format: str, red: int, green: int, blue: int, transparent: bool, text_axes: bool, gradient: bool, foreground_red: int, foreground_green: int, foreground_blue: int, auto_text_color: bool, image_size: object, copy_to_clipboard: bool) -> int:

	"""

	The SnapShot function grabs the whole screen of ANSA's graphics window and saves it as an image in the specified file.

	Parameters
	----------
	filename : str
		The filename to be saved. This argument is mandatory.
		If filename exists, it will be overwritten.

	image_format : str, optional
		One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	red : int, optional
		The number of the red component of the background color [0-255].

	green : int, optional
		The number of the green component of the background color [0-255].

	blue : int, optional
		The number of the blue component of the background color [0-255].

	transparent : bool, optional
		Enables/disables trasparent background (available for png image format only).

	text_axes : bool, optional
		Text and axes visible or not.

	gradient : bool, optional
		Leaves gradient visible or not.

	foreground_red : int, optional
		The number of the red component of the foreground color [0-255].se

	foreground_green : int, optional
		The number of the green component of the foreground color [0-255].

	foreground_blue : int, optional
		The number of the blue component of the foreground color [0-255].

	auto_text_color : bool, optional
		Automatically change foreground color if it is similar to the background color.

	image_size : object, optional
		Sets the size of the snapshot image. It must be a tuple of two integers, 
		both set to a value greater or equal to 1.

	copy_to_clipboard : bool, optional
		Set this option in order to copy the snapped image directly also to the clipboard

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	See Also
	--------
	SnapShotWidget, SnapShotWindow

	Examples
	--------
	::

		import os.path
		from os.path import expanduser
		import ansa
		from ansa import utils
		
		home = expanduser("~")
		abs_filename_1 = os.path.join(home, "image1.png")
		abs_filename_2 = os.path.join(home, "image2.png")
		
		
		def main():
		    status = utils.SnapShot(abs_filename_1, image_format="PNG", transparent=True)
		    if status == 0:
		        print("Image saved in " + abs_filename_1)
		    status = utils.SnapShot(
		        abs_filename_2, red=100, green=140, blue=210, text_axes=False
		    )
		    if status == 0:
		        print("Image saved in " + abs_filename_2)
		
		
		main()


	"""

def OpenIncludesManager() -> int:

	"""

	Opens the Includes Manager window.

	Returns
	-------
	int
		Always returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenIncludesManager()


	"""

def MainProgressBarSetValue(value: int) -> int:

	"""

	Progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	In gui mode, main progress bar is located at main ANSA window below gl model.
	Ensure the main progress bar is visible (MainProgressBarSetVisible).
	If you set an invalid value or progress bar is not visible, nothing happens.
	In no-gui mode, the value is printed in the terminal. Function is thread safe.
	Note that main progress bar is shared among several users.

	Parameters
	----------
	value : int
		Valid values: 0 - 100.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.MainProgressBarSetVisible(1)
		    utils.MainProgressBarSetValue(33)
		    utils.MainProgressBarSetValue(66)
		    utils.MainProgressBarSetValue(100)
		    utils.MainProgressBarSetVisible(0)


	"""

def MainProgressBarSetVisible(value: int) -> int:

	"""

	The progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	The main progress bar is located at the main ANSA window below the gl model.
	Show the progress bar and update its value (progress) inside your procedure.
	Remember to hide the progress bar after your procedure has finished. Function is thread safe.
	Note that the main progress bar is shared among several users.

	Parameters
	----------
	value : int
		Valid values are 0 to hide and 1 to show the progress bar.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.MainProgressBarSetVisible(1)
		    utils.MainProgressBarSetValue(33)
		    utils.MainProgressBarSetValue(66)
		    utils.MainProgressBarSetValue(100)
		    utils.MainProgressBarSetVisible(0)


	"""

def MainProgressBarSetText(text: str) -> int:

	"""

	Progress bar is used to give the user an indication of the progress of an operation 
	and to reassure them that the application is still running.
	In gui mode, main progress bar is located at main ANSA window below gl model.
	Ensure that the main progress bar is visible (MainProgressBarSetVisible).
	If the progress bar is not visible, nothing happens.
	Note that the main progress bar is shared among several users.

	Parameters
	----------
	text : str
		The text that will be displayed on the progress bar.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.MainProgressBarSetVisible(1)
		    utils.MainProgressBarSetText("Regenerating Mesh")


	"""

def OpenModelBrowser(entity_type: str, view_mode: str, main_tabs: object, current_main_tab: str, info_tabs: object, current_info_tab: str, side_panel: bool, current_side_panel_tab: str, profile: str) -> bool:

	"""

	Opens the Model Browser window.

	Parameters
	----------
	entity_type : str, optional
		The Main tab to make current. This argument is obsolete, use current_main_tab
		instead.
		Accepted values:
		- The tab names as they are shown: 'Parts', 'Configurations', 'Subsystems', etc.
		- The ANSA keywords: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	view_mode : str, optional
		The view mode to show in list for the current Main tab.
		Accepted values: tree_view, flat_view, icon_view or the view names as they are shown.

	main_tabs : object, optional
		A list of Main tabs in the order to show them.
		Accepted values:
		- The tab names as they are shown: 'Parts', 'Configurations', 'Subsystems', etc.
		- The ANSA keywords: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	current_main_tab : str, optional
		The Main tab to make current.
		Accepted values:
		- The tab name as it is shown: 'Parts', 'Configurations', 'Subsystems', etc.
		- The ANSA keyword: 'ANSAPART', 'ANSA_CONFIGURATION', 'ANSA_SUBSYSTEM', etc.

	info_tabs : object, optional
		A list of Info tabs in the order to show them.
		Accepted values:
		- The tab names as they are shown: 'Details', 'Contents', 'Connectivity', etc.

	current_info_tab : str, optional
		The Info tab to make current.
		Accepted values:
		- The tab name as it is shown: 'Details', 'Contents', 'Connectivity', etc.

	side_panel : bool, optional
		The visibility of the Side Panel.
		Accepted values:
		- True: the Side Panel is shown
		- False: the Side Panel is hidden

	current_side_panel_tab : str, optional
		The tab in the Side Panel to make current.
		Accepted values:
		- The tab name as it is shown: 'Table View', 'References'

	profile : str, optional
		The name of the Profile to use.
		Accepted values:
		- Any of the Profile names which exist in the Model Browser Profile settings.

	Returns
	-------
	bool
		Returns True if the Model Browser opened succesfully, otherwise False.

	See Also
	--------
	CloseModelBrowser, ShowModelBrowserColumn, HideModelBrowserColumn

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # just open the Model Browser
		    utils.OpenModelBrowser()
		
		    # open the Model Browser and make current the tab of 'Subsystems'
		    utils.OpenModelBrowser(current_main_tab="Subsystems")
		
		    # open the Model Browser and show the 'Parts' in icon view mode
		    utils.OpenModelBrowser(current_main_tab="Parts", view_mode="icon_view")
		
		    # open the Model Browser using Profile 'NVH'
		    utils.OpenModelBrowser(profile="NVH")
		
		    # open the Model Browser with the Parts and Subsystems Main tabs and make current the tab of 'Subsystems'
		    main_tabs_list = ["Parts", "Subsystems"]
		    utils.OpenModelBrowser(main_tabs=main_tabs_list, current_main_tab="Subsystems")
		
		    # open the Model Browser with the Details and DM Info tabs and make current the 'DM' tab
		    info_tabs_list = ["Details", "DM"]
		    utils.OpenModelBrowser(info_tabs=info_tabs_list, current_info_tab="DM")


	"""

def CloseModelBrowser() -> object:

	"""

	Closes the Model Browser window.

	Returns
	-------
	object
		Always returns None.

	See Also
	--------
	OpenModelBrowser, ShowModelBrowserColumn, HideModelBrowserColumn

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # close the Model Browser window
		    utils.CloseModelBrowser()


	"""

def DatabaseBrowserInfo(deck: int, extra_info: object, simplify: str) -> object:

	"""

	This function provides a dictionary with the Database Browser structure of the current model.

	Parameters
	----------
	deck : int
		The deck for which you get the Database Browser structure.

	extra_info : object, optional
		A list of column names to get extra information
		("visible", "min_id", "max_id")
		
		"visible": get the number of visible entities for each object.
		"min_id": get the minimum entity id for each object. 
		"max_id": get the maximum entity id for each object.

	simplify : str, optional
		Defines the simplification taking place
		("default", "true", "false").
		
		Simplification forces any first level object
		that contains only one child having the 
		same name to be replaced by its child object.
		
		"default": simplification is executed in GUI mode only (default). 
		"true": simplification is always executed.
		"false": simplification is never executed.

	Returns
	-------
	object
		It returns a dictionary with keys the names of the parent items of the
		Database Browser and data objects with members: 
		
		'total': the number of entities for the item
		'children': a dictionary with such objects. 
		'extra_info': a dictionary containing extra information about the object. 
		
		Regarding the 'children' member:
		If an item does not have any children, the dictionary is empty.
		
		Regarding the 'extra_info' member:
		If no 'extra_info' list is provided as input argument, 
		the member 'extra_info' will be missing for every object.
		
		Regarding 'extra_info' keys:
		"visible": the number of visible entities for the item.
		"min_id": the minimum entity id for the item. 
		"max_id": the maximum entity id for the item. 
		For these keys to be listed under the 'extra_info' dict, 
		they need to be included in the input argument list extra_info. 
		
		The example below would print the following:
		
		ELEMENT 1540 {'min_id': 1, 'max_id': 1720}
		  ELEMENT_SOLID 84 {'min_id': 1, 'max_id': 820}
		    HEXA 84 {'min_id': 1, 'max_id': 820}
		  ELEMENT_SHELL 1456 {'min_id': 9, 'max_id': 1720}
		    QUAD 1436 {'min_id': 9, 'max_id': 1720}
		    TRIA 20 {'min_id': 628, 'max_id': 1699}
		PROPERTY 6 {'min_id': 1, 'max_id': 6}
		  LAMINATE 1 {'min_id': 6, 'max_id': 6}
		  SECTION_SHELL 4 {'min_id': 1, 'max_id': 4}
		  SECTION_SOLID 1 {'min_id': 5, 'max_id': 5}
		MATERIAL 4 {'min_id': 1, 'max_id': 103}
		  MAT1 MAT_ELASTIC 4 {'min_id': 1, 'max_id': 103}

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import utils
		from ansa import constants
		
		
		def print_object(name, obj, depth=0):
		    spacer = depth * "  "
		    print(f"{spacer}{name} {obj.total} {obj.extra_info}")
		
		
		def print_hierarchy(hierarchy, depth=0):
		    for k, v in hierarchy.items():
		        print_object(k, v, depth)
		        print_hierarchy(v.children, depth + 1)
		
		
		def print_info(info, key=None):
		    if key:
		        object_info = info.get(key, None)
		        if object_info:
		            print_object(key, object_info)
		            print_hierarchy(object_info.children, 1)
		    else:
		        print_hierarchy(info)
		
		
		def main():
		    base.SetCurrentDeck(constants.LSDYNA)
		    info = utils.DatabaseBrowserInfo(constants.LSDYNA, ["min_id", "max_id"])
		    print_info(info, "ELEMENT")
		    print_info(info, "PROPERTY")
		    print_info(info, "MATERIAL")


	"""

def ReadGUISettings(xml_file_path: str) -> bool:

	"""

	This function applies GUI settings read from the given file.
	WARNING: It will remove any previous settings and custom menus or toolbars.

	Parameters
	----------
	xml_file_path : str
		The absolute or relative path to a GUI settings file, like ANSA.xml, CFD.xml etc.

	Returns
	-------
	bool
		Returns true on successful application of the read GUI settings, false otherwise.

	See Also
	--------
	utils.SaveGUISettings, utils.CurrentGUISettings

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from ansa import utils, guitk
		
		
		def main():
		    initial_settings_file = utils.CurrentGUISettings()
		    print("CURRENT: " + initial_settings_file)
		
		    current_settings_dir = os.path.dirname(os.path.realpath(initial_settings_file))
		    new_settings_file = os.path.join(current_settings_dir, "MySettings.xml")
		    ok = utils.SaveGUISettings(new_settings_file)
		    if ok:
		        print(utils.CurrentGUISettings() + " saved successfully.")
		    else:
		        print("Could not save " + new_settings_file)
		    ok = utils.ReadGUISettings(initial_settings_file)
		    if ok:
		        print(utils.CurrentGUISettings() + " saved successfully.")
		    else:
		        print("Could not read " + initial_settings_file)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SaveGUISettings(xml_file_path: str) -> bool:

	"""

	This function saves the current GUI settings to a file.

	Parameters
	----------
	xml_file_path : str
		The absolute or relative path to a GUI settings file, like ANSA.xml, CFD.xml etc.

	Returns
	-------
	bool
		Returns true on successful saving of the current GUI settings to the given file, false otherwise.

	See Also
	--------
	utils.ReadGUISettings

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from ansa import utils, guitk
		
		
		def main():
		    initial_settings_file = utils.CurrentGUISettings()
		    print("CURRENT: " + initial_settings_file)
		
		    current_settings_dir = os.path.dirname(os.path.realpath(initial_settings_file))
		    new_settings_file = os.path.join(current_settings_dir, "MySettings.xml")
		    ok = utils.SaveGUISettings(new_settings_file)
		    if ok:
		        print(utils.CurrentGUISettings() + " saved successfully.")
		    else:
		        print("Could not save " + new_settings_file)
		    ok = utils.ReadGUISettings(initial_settings_file)
		    if ok:
		        print(utils.CurrentGUISettings() + " saved successfully.")
		    else:
		        print("Could not read " + initial_settings_file)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurrentGUISettings() -> str:

	"""

	This function returns the file path of the current GUI settings file.

	Returns
	-------
	str
		The absolute file path of the current GUI settings file.

	See Also
	--------
	utils.ReadGUISettings, utils.SaveGUISettings

	"""

def SnapShotWidget(filename: str, image_format: str, widget: object) -> int:

	"""

	The SnapShotWidget function grabs widget child of a window and saves it as an image in the specified file.

	Parameters
	----------
	filename : str
		The filename to be saved. This argument is mandatory.
		If filename exists, it will be overwritten.

	image_format : str, optional
		One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	widget : object, optional
		The returned value of the function that create the widget.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	See Also
	--------
	SnapShot, SnapShotWindow

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from os.path import expanduser
		from ansa import guitk
		from ansa import utils
		
		home = expanduser("~")
		abs_filename_widget = os.path.join(home, "widget.png")
		
		
		def main():
		    win = guitk.BCWindowCreate("BCWindow Example", guitk.constants.BCOnExitDestroy)
		
		    pbut = guitk.BCPushButtonCreate(win, "Snap Ok-Cancel widget", None, None)
		    dbb = guitk.BCDialogButtonBoxCreate(win)
		    guitk.BCButtonSetClickedFunction(pbut, clickFunction, dbb)
		    guitk.BCShow(win)
		
		
		def clickFunction(b, dbb):
		    status = utils.SnapShotWidget(abs_filename_widget, image_format="PNG", widget=dbb)
		    if status == 0:
		        print("Image saved in " + abs_filename_widget)
		    return 0
		
		
		if __name__ == "__main__":
		    main()


	"""

def SnapShotWindow(filename: str, image_format: str, window_title: str) -> int:

	"""

	The SnapShotWindow function takes a snapshot of a window and saves it as an image in the specified file.

	Parameters
	----------
	filename : str
		The filename to be saved. This argument is mandatory.
		If filename exists, it will be overwritten.

	image_format : str, optional
		One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	window_title : str, optional
		The window title.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	See Also
	--------
	SnapShot, SnapShotWidget

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from os.path import expanduser
		from ansa import guitk
		from ansa import utils
		
		home = expanduser("~")
		abs_filename_window = os.path.join(home, "window.png")
		
		
		def main():
		    win = guitk.BCWindowCreate("BCWindow Example", guitk.constants.BCOnExitDestroy)
		
		    pbut = guitk.BCPushButtonCreate(win, "Snap window", None, None)
		    dbb = guitk.BCDialogButtonBoxCreate(win)
		    guitk.BCButtonSetClickedFunction(pbut, clickFunction, dbb)
		    guitk.BCShow(win)
		
		
		def clickFunction(b, dbb):
		    status = utils.SnapShotWindow(
		        abs_filename_window, image_format="PNG", window_title="BCWindow Example"
		    )
		    if status == 0:
		        print("Image saved in " + abs_filename_window)
		    return 0
		
		
		if __name__ == "__main__":
		    main()


	"""

def ShowModelBrowserColumn(column_name: str, position: int) -> object:

	"""

	Shows the column with specific name in the current Tab of Model Browser window in specific position.

	Parameters
	----------
	column_name : str
		The name of the column to show.

	position : int, optional
		Determines in which position to show the column.

	Returns
	-------
	object
		Always returns None

	See Also
	--------
	HideModelBrowserColumn, OpenModelBrowser, CloseModelBrowser

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenModelBrowser(entity_type="Parts")
		    utils.ShowModelBrowserColumn(column_name="Visible", position=0)
		    utils.ShowModelBrowserColumn(column_name="Module Id", position=1)
		    utils.ShowModelBrowserColumn(column_name="Name")


	"""

def HideModelBrowserColumn(column_name: str) -> object:

	"""

	Hides the column with specific name from the current Tab of Model Browser window.

	Parameters
	----------
	column_name : str
		The name of the column to hide.

	Returns
	-------
	object
		Always returns None

	See Also
	--------
	ShowModelBrowserColumn, OpenModelBrowser, CloseModelBrowser

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenModelBrowser(entity_type="Parts")
		    utils.HideModelBrowserColumn(column_name="Module Id")


	"""

def SetDrawingForegroundColor(r: int, g: int, b: int) -> object:

	"""

	Sets the RGB values of the foreground color of the drawing area to be r, g and b.

	Parameters
	----------
	r : int
		The value for red (0 - 255).

	g : int
		The value for green (0 - 255).

	b : int
		The value for blue (0 - 255).

	Returns
	-------
	object
		Always returns None.

	See Also
	--------
	DrawingForegroundColor, SetDrawingAreaColor

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.SetDrawingForegroundColor(10, 255, 150)


	"""

def DrawingForegroundColor() -> object:

	"""

	Returns the RGB values of the foreground color of the drawing area.

	Returns
	-------
	object
		A tuple of three values which are the RGB components of the foreground color.

	See Also
	--------
	SetDrawingForegroundColor

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    rgb = utils.DrawingForegroundColor()
		    print("RGB values: ", rgb)


	"""

def AddCurveToPlot(plot: object, curve: object):

	"""

	This function adds new curves to a created plot. 
	Can be used for one curve: AddCurveToPlot(plot, curve)
	or for multiple curves at once: AddCurveToPlot(plot, [curve1, curve2, curve3...])
	

	Parameters
	----------
	plot : object
		This argument is the plot.

	curve : object
		This argument is the curve to be added (single one) or a list of curves (for multiple curves).

	See Also
	--------
	utils.CreateCurve, utils.CreatePlot

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		
		run_curve1 = utils.CreateCurve()
		r_g_b1 = [200, 0, 0]
		curve_coords1 = [(1, 0.6), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve1, coords=curve_coords1)
		utils.SetCurveProperties(run_curve1, type="Bar", color=r_g_b1, offset_on=True)
		
		run_curve2 = utils.CreateCurve()
		r_g_b2 = [0, 0, 200]
		curve_coords2 = [(1, 0.2), (2, 3), (3, 2.5)]
		utils.AddCurveData(run_curve2, coords=curve_coords2)
		utils.SetCurveProperties(run_curve2, type="Bar", color=r_g_b2, offset_on=True)
		
		utils.AddCurveToPlot(plot, [run_curve1, run_curve2])
		utils.DeleteCurve(run_curve1)
		utils.DeleteCurve(run_curve2)
		
		utils.DeletePlot(plot)


	"""

def SetCurveProperties(curve: object, type: str, color: object, width: int, label: str, marker_style: str, marker_size: int, dash_style: str, offset_on: bool, curve_attributes: object, curve_points_attributes: object):

	"""

	This function sets properties to a created curve. Argument options:

	- type: Line or Bar
	- color: [r,g,b]
	- width
	- label 
	- marker_style: None, Cross, Plus, WhiteSquare, BlackSquare, Diamond, Circle, TriangleUp, TriangleDown
	- marker_size: integer 
	- dash_style: Solid, SparseShortDot, SparseDot, SparseLongDot, Dash, ThickDash, DashDot, ShortDot, Dot, LongDot, 
	        DenseShortDot, DenseDot, DenseLongDot 
	- offset: True or False
	- curve_attributes: {"Module id":"Karosseriegerippe", "CarLine":"LU",...} 
	- curve_points_attributes: { 0:attr_map_for_point0, 1:attr_map_for_point1, 2:attr_map_for_point2 ... }
	

	Parameters
	----------
	curve : object
		This argument is the curve to add properties to.

	type : str, optional
		This argument is the curve type.

	color : object, optional
		This argument is a list of 3 integers (0-255 for r, g, b channels) 
		to define color.

	width : int, optional
		This argument is the curve width.

	label : str, optional
		This argument is a label (to be seen in legend).

	marker_style : str, optional
		This argument is the marker style.

	marker_size : int, optional
		This argument is the marker size. Default value is 5.

	dash_style : str, optional
		This argument is the dash style.

	offset_on : bool, optional
		This argument enables or disables offset (True or False).

	curve_attributes : object, optional
		This argument is a dictionary with attribute name-values.

	curve_points_attributes : object, optional
		This argument is a dictionary with attribute name-values for curve's points. 
		Dictionary has as key an integer and as data a map of name-values.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		run_curve = utils.CreateCurve()
		r_g_b = [0, 0, 220]
		curve_coords = [(1, 0.2), (2, 1.3), (3, 0.9), (4, 2.1)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		curve_attrs = {"Module Id": "44", "Project": "New"}
		curve_points_attrs = {
		    0: {"Id": "01", "Name": "Phase1"},
		    1: {"Id": "02", "Name": "Phase2"},
		    2: {"Id": "03", "Name": "Phase3"},
		    3: {"Id": "04", "Name": "Phase4"},
		}
		utils.SetCurveProperties(
		    run_curve,
		    type="Line",
		    color=r_g_b,
		    offset_on=True,
		    label="Line Curve",
		    dash_style="DashDot",
		    curve_attributes=curve_attrs,
		    curve_points_attributes=curve_points_attrs,
		)
		utils.AddCurveToPlot(plot, run_curve)
		
		utils.DeleteCurve(run_curve)
		utils.DeletPlot(plot)


	"""

def SetYAxisProperties(plot: object, title: str, unit: str, min_max: object, num_of_steps: int, step_labels: object, show_values_on_axis: bool) -> None:

	"""

	This function sets properties for the Y axis of a plot. For example: SetYAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)

	Parameters
	----------
	plot : object
		This argument is the relevant plot.

	title : str, optional
		This argument is the title shown for Y axis.

	unit : str, optional
		This argument is the unit used for Y axis. It would be shown beside the title.

	min_max : object, optional
		This argument is a pair of 2 numbers (integers or floats) to set minimum and 
		maximum values of Y axis.

	num_of_steps : int, optional
		This argument sets the number of steps to be used.

	step_labels : object, optional
		This argument is a dictionary of integer:string pairs, where key is the step 
		index and value is the label we want to use for this step. If user hasn't set 
		the number of steps to be used, number of steps is set by the number of given 
		labels plus 1.

	show_values_on_axis : bool, optional
		This argument is used to set if values should be visible on axis (True or False).

	Returns
	-------
	None
		Always returns None.

	See Also
	--------
	utils.SetXAxisProperties

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="Bar_Curve", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)


	"""

def SetXAxisProperties(plot: object, title: str, unit: str, min_max: object, num_of_steps: int, step_labels: object, show_values_on_axis: bool):

	"""

	This function sets properties for the X axis of a plot. For example: SetXAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)

	Parameters
	----------
	plot : object
		This argument is the relevant plot.

	title : str, optional
		This argument is the title shown for X axis.

	unit : str, optional
		This argument is the unit used for X axis. It would be shown beside the title.

	min_max : object, optional
		This argument is a pair of 2 numbers (integers or floats) to set minimum and 
		maximum values of X axis.

	num_of_steps : int, optional
		This argument sets the number of steps to be used.

	step_labels : object, optional
		This argument is a dictionary of integer:string pairs, where key is the step 
		index and value is the label we want to use for this step. If user hasn't set 
		the number of steps to be used, number of steps is set by the number of given 
		labels plus 1.

	show_values_on_axis : bool, optional
		This argument is used to set if values should be visible on axis (True or False).

	See Also
	--------
	utils.SetYAxisProperties

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="Bar_Curve", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)


	"""

def SetPlotProperties(plot: object, title: str, show_legend: bool, legend_position: str, show_grid: bool):

	"""

	This function sets properties for the given plot. Available values:

	- legend_position: TopRight, TopLeft, BottomRight, BottomLeft
	- show_legend: True/False
	- show_grid: True/False

	Parameters
	----------
	plot : object
		This argument is the relevant plot to set properties to.

	title : str, optional
		This argument is the title to give to the plot.

	show_legend : bool, optional
		Flag to set if legend should be shown or not (True/False). Legend is given as 
		curve label (see function utils.SetCurveProperties).

	legend_position : str, optional
		This argument sets the position of legend: TopRight, TopLeft, BottomRight, 
		BottomLeft.

	show_grid : bool, optional
		Flag to set if grid should be shown or not (True/False).

	See Also
	--------
	utils.CreatePlot

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="common", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		utils.SetPlotProperties(
		    plot,
		    title="My Mass Plot",
		    show_legend=True,
		    legend_position="TopRight",
		    show_grid=True,
		)


	"""

def CreatePlot() -> object:

	"""

	This function creates a new plot.

	Returns
	-------
	object
		Upon success, it returns a Class object referring to the newly created plot.
		Else, None is returned.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="common", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		utils.SetPlotProperties(
		    plot,
		    title="My Mass Plot",
		    show_legend=True,
		    legend_position="TopRight",
		    show_grid=True,
		)
		
		utils.DeletePlot(plot)


	"""

def DeletePlot(plot: object):

	"""

	This function deletes the plot object given as argument. 

	Parameters
	----------
	plot : object
		This argument is the plot that is going to be deleted.

	See Also
	--------
	utils.CreatePlot

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		plot = utils.CreatePlot()
		utils.DeletePlot(plot)


	"""

def RecentFilesRecordingSetEnabled(enabled: bool):

	"""

	Enables or disables the recording of recent files (that appear in the history of File>Input Recent and File>Open Recent).

	Parameters
	----------
	enabled : bool
		set to False in odrer to dsable recording, otherwise True.

	See Also
	--------
	RecentFilesRecordingIsEnabled

	Examples
	--------
	::

		# PYTHON script
		import ansa
		from ansa import base
		from ansa import utils
		
		
		def main():
		    prev = utils.RecentFilesRecordingIsEnabled()
		    utils.RecentFilesRecordingSetEnabled(False)
		    # Open files here
		    base.Open("/home/user/Final_Model.ansa")
		    base.Open("/home/user/Initial_Model.ansa")
		    base.InputNastran("/home/user/my_nas_model.nas")
		    utils.RecentFilesRecordingSetEnabled(prev)
		
		
		if __name__ == "__main__":
		    main()


	"""

def RecentFilesRecordingIsEnabled() -> bool:

	"""

	Checks if the recording of recent files (the ones that appear in the history of File>Input Recent and File>Open Recent) is on or off. When off, any files accessed by File>Open and File>Input actions aren't recorded.

	Returns
	-------
	bool
		True if the recording of recent files is enabled or False otherwise.

	See Also
	--------
	RecentFilesRecordingSetEnabled

	Examples
	--------
	::

		# PYTHON script
		import ansa
		from ansa import base
		from ansa import utils
		
		
		def main():
		    prev = utils.RecentFilesRecordingIsEnabled()
		    utils.RecentFilesRecordingSetEnabled(False)
		    # Open files here
		    base.Open("/home/user/Final_Model.ansa")
		    base.Open("/home/user/Initial_Model.ansa")
		    base.InputNastran("/home/user/my_nas_model.nas")
		    utils.RecentFilesRecordingSetEnabled(prev)
		
		
		if __name__ == "__main__":
		    main()


	"""

def FringeBarUnpinPosition(type: str) -> object:

	"""

	The FringeBarUnpinPosition function unpins the fringebar of type 'type'. If the fringebar is not previously pinned, this function has no effect.

	Parameters
	----------
	type : str, optional
		One of: ['GENERAL' | 'DEFORMATION' | 'SURFACE_INFO' | 'IGA_INFO']
		If empty, 'GENERAL' will be used by default.

	Returns
	-------
	object
		Always returns None.

	See Also
	--------
	FringeBarPinPosition

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.FringeBarUnpinPosition("SURFACE_INFO")
		    utils.FringeBarUnpinPosition()
		
		
		main()


	"""

def FringeBarPinPosition(position: int, type: str, coordinates: object) -> object:

	"""

	The FringeBarPinPosition function pins the fringebar of type 'type' to the specified position of the GL area. This will be applied to all GL windows.

	Parameters
	----------
	position : int
		The position where fringebar should be pinned:
		- utils.constants.BCPositionDefault : Factory defaults or values read from XML
		- utils.constants.BCPositionTopLeft : The top-left corner of the GL area
		- utils.constants.BCPositionTopRight : The top-right corner of the GL area
		- utils.constants.BCPositionTopHCenter : The top and horizontal-center of the GLarea.
		- utils.constants.BCPositionBottomLeft : The bottom-left corner of the GL area
		- utils.constants.BCPositionBottomRight : The bottom-right corner of the GL area
		- utils.constants.BCPositionBottomHCenter : The bottom and horizontal-center of
		the GL area.
		- utils.constants.BCPositionLeftVCenter : The left and vertical-center of the GL area
		- utils.constants.BCPositionRightVCenter : The right and vertical-center of the GL area
		- utils.constants.BCPositionCenter : The center of the GL area
		- utils.constants.BCPositionCustom : Use this in combination with argument 'coordinates'
		to pin the fringebar to a user-defined position

	type : str, optional
		One of: ['GENERAL' | 'DEFORMATION' | 'SURFACE_INFO' | 'IGA_INFO']
		If empty, 'GENERAL' will be used by default.

	coordinates : object, optional
		User-defined position. It must be a tuple of two real values, both set in range [0., 1]
		which maps the percentage of the GL area. Use this only when argument 'position'
		is set to utils.constants.BCPositionCustom.
		Pin-point of the fringebar is meant the top-left corner of its geometry.
		If custom coordinates cause fringebar geometry to exceed GL area's boundaries the fringebar will be automatically fitted.

	Returns
	-------
	object
		Always returns None.

	See Also
	--------
	FringeBarUnpinPosition

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.FringeBarPinPosition(
		        utils.constants.BCPositionCustom, coordinates=(0.5, 0.5), type="DEFORMATION"
		    )
		    utils.FringeBarPinPosition(
		        utils.constants.BCPositionBottomRight, type="SURFACE_INFO"
		    )
		    utils.FringeBarPinPosition(utils.constants.BCPositionBottomLeft)
		
		
		main()


	"""

def EncryptBytes(data: object, password: str) -> object:

	"""

	The EncryptBytes function encryptes bytes object using a password

	Parameters
	----------
	data : object
		A bytes object to encrypt.

	password : str
		The password used for encryption.

	Returns
	-------
	object
		Returns the encrypted bytes object.

	See Also
	--------
	ansa.utils.DecryptBytes

	Examples
	--------
	::

		from ansa import utils
		import base64
		
		
		def _encrypt_string(input, password) -> str:
		    input = input.encode()
		    output = utils.EncryptBytes(input, password)
		    output = base64.b64encode(output)
		    output = output.decode()
		    return output
		
		
		def _decrypt_string(input, password) -> str:
		    input = input.encode()
		    input = base64.b64decode(input)
		    output = utils.DecryptBytes(input, password)
		    output = output.decode()
		    return output
		
		
		def main():
		    plain_str = "String to encrypt"
		    print("plain_str =", plain_str)
		    encrypted_str = _encrypt_string(plain_str, "ansa123")
		    print("encrypted_str =", encrypted_str)
		    try:
		        decrypted_str = _decrypt_string(encrypted_str, "ansa123")
		    except:
		        print("Invalid password")
		        return
		    print("decrypted_str =", decrypted_str)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DecryptBytes(data: object, password: str) -> object:

	"""

	The DecryptBytes function decryptes bytes object using a password

	Parameters
	----------
	data : object
		A bytes object to decrypt.

	password : str
		The password used for decryption.

	Returns
	-------
	object
		Returns the decrypted bytes object.

	See Also
	--------
	ansa.utils.EncryptBytes

	Examples
	--------
	::

		from ansa import utils
		import base64
		
		
		def _encrypt_string(input, password) -> str:
		    input = input.encode()
		    output = utils.EncryptBytes(input, password)
		    output = base64.b64encode(output)
		    output = output.decode()
		    return output
		
		
		def _decrypt_string(input, password) -> str:
		    input = input.encode()
		    input = base64.b64decode(input)
		    output = utils.DecryptBytes(input, password)
		    output = output.decode()
		    return output
		
		
		def main():
		    plain_str = "String to encrypt"
		    print("plain_str =", plain_str)
		    encrypted_str = _encrypt_string(plain_str, "ansa123")
		    print("encrypted_str =", encrypted_str)
		    try:
		        decrypted_str = _decrypt_string(encrypted_str, "ansa123")
		    except:
		        print("Invalid password")
		        return
		    print("decrypted_str =", decrypted_str)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DetectThermalLinks(dist: float, entities: object, excl_angle: int, self_link: bool) -> object:

	"""

	Detects possible thermal links between SHELL PARTs, based on a given search distance and viewing angle.
	It follows the method used by the ANSA "Thermal Link Wizard".
	A pair of SHELL PARTs that is already linked with thermal link, won't be considered for a second link.

	Parameters
	----------
	dist : float
		A search distance (threshold), in which two entities will be considered for thermal links

	entities : object, optional
		A collection of SHELL PARTs that will be considered for thermal links. 
		Entities other than those are not considered.
		Accepted values: "all", "visible", or a container of SHELL PARTs, or SHELL PART ids.
		(Default: "all")

	excl_angle : int, optional
		An exclusion angle for nearly-perpendicular shells, to reduce the detection 
		of links with bad quality.
		A pair of shells whose angle is in [90-excl_angle, 90+excl_angle], won't be considered
		for the detection of thermal links.
		Accepted values:  integers in [0, 90]. 0 allows all elements, 90 allows only parallel.
		(Default: 3)

	self_link : bool, optional
		A flag that can be used to allow the detection of thermal links of a part with itself.
		If True, it allows searching/detection between elements belonging to the same SHELL PART.
		(Default: False)

	Returns
	-------
	object
		Upon sucessful completion, it returns a python list, whose items are the detected possible thermal links (if any),
		as they would have been produced by the "Thermal Link Wizard" tool.
		Each such item is a python dictionary, with the Wizard's column names as keys.
		
		In case of an error, it returns None.

	Examples
	--------
	::

		import os
		import ansa
		from ansa import utils
		
		
		def DetectAndCreateThermalLinksOncurrentModel():
		    # this function can work on visible, all, or a custom collection, of SHELL_PARTs of the current model.
		    # ans = utils.DetectThermalLinks(0.15, [1,3,5])     # searches only in SHELL_PARTs with IDs 1,3,5
		    # ans = utils.DetectThermalLinks(0.15)              # searches entire model
		    ans = utils.DetectThermalLinks(0.15, "visible")  # searches only visible entities
		
		    for entry in ans:
		        # you wouldn't really want to create all suggested links, so you should filter
		        # the entries here.
		        # e.g. :
		        # if entry['Coverage (%)'] < 3:
		        # \tcontinue
		
		        print(entry)
		        CreateThermalLinkFromWizardEntry(entry, 0.15)
		        # entry['First end ID']
		        # entry['Second end ID']
		        # entry['First end name']
		        # entry['Second end name']
		        # entry['Orientation']
		        # entry['Min Distance']
		        # entry['Coverage (%)']
		        # entry['Links to itself']
		        # entry['Shares edge']
		
		
		def CreateThermalLinkFromWizardEntry(entry, dist):
		    Name = entry["First end name"] + " To " + entry["Second end name"]
		    vals = {
		        "Type": "Face To Face",
		        "First End": "Part",
		        "Second End": "Part",
		        "First End Part": entry["First end ID"],
		        "Second End Part": entry["Second end ID"],
		        "Offset Distance": dist,
		        "Name": Name,
		    }
		    orient = {}
		    if entry["Orientation"] == "Back To Front":
		        orient["First End Face"] = "Back"
		        orient["Second End Face"] = "Front"
		    elif entry["Orientation"] == "Front To Back":
		        orient["First End Face"] = "Front"
		        orient["Second End Face"] = "Back"
		    elif entry["Orientation"] == "Back To Back":
		        orient["First End Face"] = "Back"
		        orient["Second End Face"] = "Back"
		    else:
		        orient["First End Face"] = "Front"
		        orient["Second End Face"] = "Front"
		    vals.update(orient)
		
		    elem, msg = base.CreateEntity(
		        constants.TAITHERM, "THERMAL LINK", vals, debug=constants.REPORT_ALL
		    )
		    if not elem:
		        print(msg)
		    return elem
		
		
		def main():
		    # here you could use base.Open("/path/to/file.ansa")
		    # or base.InputTaitherm("/path/to/file.tdf", model_action="overwrite_model")
		    # to open and work on a file of your choice.
		    DetectAndCreateThermalLinksOncurrentModel()


	"""

class UnitSystem():

	"""

	A unit conversion system.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import utils
		
		
		def main():
		    unit_system = utils.UnitSystem(length="kilometer")
		    base.InputStereoLithography("/home/user/file.stl", unit_system=unit_system)
		
		    del unit_system

	"""


	length: str = None
	"""
	The length unit.

	"""

	mass: str = None
	"""
	The mass unit.

	"""

	time: str = None
	"""
	The time unit.

	"""

	temperature: str = None
	"""
	The temperature unit.

	"""

	kinetics_force: str = None
	"""
	The force unit for kinetics

	"""

	@classmethod
	def __init__(cls, length: str, mass: str, time: str, temperature: str, kinetics_force: str) -> object:

		"""

		UnitSystem object constructor.


		Parameters
		----------
		length : str, optional
			The length unit. Valid values are: "meter", millimeter", 
			"inch", "feet", "mile", "kilometer", "mil", "micron", 
			"centimeter", "microinch".
			(Default: "milimeter")

		mass : str, optional
			The mass unit. Valid values are: "kilogram", "gram", 
			"tonne", "pound".
			(Default: "tonne")

		time : str, optional
			The time unit. Valid values are: "second", "millisecond", 
			"minute", "hour".
			(Default: "second")

		temperature : str, optional
			The temperature unit. Valid values are: "kelvin", 
			"degree Celsius", "degree Fahrenheit".
			(Default: "kelvin")

		kinetics_force : str, optional
			The force unit for kinetics

		Returns
		-------
		object
			Returns the created UnitSystem object.

		"""


	def set_current(self, unit_system: object, apply_to_settings: bool, apply_to_models: bool):

		"""

		Sets ANSA's current unit system


		Parameters
		----------
		unit_system : object
			A UnitSystem object. If this argument is set to None,
			ANSA's unit system is disabled.

		apply_to_settings : bool, optional
			If set to True, units will be applied on ANSA settings. If set
			to False settings will not change. True by default.

		apply_to_models : bool, optional
			If set to True a unit conversion will be performed from the 
			current UnitSystem to the new UnitSystem. If set to 
			False no conversion will take palce. False by default.

		"""


	def get_current(self) -> object:

		"""

		Returns ANSA's current unit system or None if there is none defined


		Returns
		-------
		object
			Returns a UnitSystem object

		"""

class FileCacher():

	"""

	The FileCacher object provides access to the application wide File Caching
	service. It allows the addition / lookup / deletion of files from the cache
	store.
	
	Since the cache store has a finite size, older cache entries are evicted (when
	needed) in order to accommodate new ones. If a user wants to be sure that a file
	found in the cache will continue to be available for a certain duration, then
	the corresponding cache entry needs to be supervised using a FileCacherWatchdog.
	
	The ResultCode is an integer that is used by the methods of this class to 
	report the outcome of an operation. The values it holds are:
	
	- 0: Success.
	- 1: Out of disk space.
	- 2: Source file not found.
	- 3: Cache entry already exists.
	- 4: Cache backend failure.
	
	This class employs the following custom Objects:
	
	CacheDmAddResult
	
	This object conveys the result of a DM cache entry addition (i.e. method
	add_dm_file). Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- path: Path of the integrated file within the cache store.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	
	CacheKeylessAddResult
	
	This object conveys the result of a keyless cache entry addition (i.e. method
	add_keyless_file). Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- path: Path of the integrated file within the cache store.
	- identity: Identifies this entry in the cache store; can be used for later lookups.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	         
	CacheLookedUpFile
	
	This object returns the information for a single cache entry after a lookup. Its
	members are:
	
	- path: Path of the looked up file within the cache store.
	- timestamp: Time which is considered 'Last Edit' for this file.
	- token: Object of type CacheToken which refers to this specific cache entry in the store.
	         
	CacheLookupResult
	
	This object holds the result of a lookup operation. Its members are:
	
	- result_code: Result of the operation. See ResultCode definition on the meaning of each value.
	- files: Sequence of CacheLookedUpFile objects, one per cache entry returned by the lookup.
	         
	CacheToken
	
	This object points to a specific cache entry and is used to uniquely refer to:
	
	- the cache entry inserted via an add operation.
	- a specific cache entry returned by a lookup operation.
	
	The user is not supposed to create objects of this class, but should provide
	a token return by the File Cacher itself. CacheToken objects are provided as
	arguments to operations that accept references to concrete cache entries (e.g.
	deletion mark or Watchdog supervise --- see also FileCacherWatchdog)

	See Also
	--------
	FileCacherWatchdog

	Examples
	--------
	::

		import time
		import ansa
		from ansa import utils
		
		
		def main():
		    file_cacher = utils.FileCacher()
		
		    print("File Cacher enabled:", file_cacher.is_up())
		
		    path = "C:/temp/representation.ansa"
		    server_id = "u3js9f2"
		    file_type = "RepresentationFile"
		    timestamp = int(time.time())
		
		    add_result = file_cacher.add_dm_file(path, server_id, file_type, timestamp)
		    print("Addition result code:", add_result.result_code)
		
		    lookup_result = file_cacher.lookup_dm_file(server_id, file_type)
		    print("Lookup result code:", lookup_result.result_code)
		    print("Num of entries found:", len(lookup_result.files))
		    print("Path of first entry:", lookup_result.files[0].path)
		
		    token = lookup_result.files[0].token
		    file_cacher.deletion_mark(token)

	"""


	def is_up(self) -> bool:

		"""

		Checks if the File Caching service is currently active or not.


		Returns
		-------
		bool
			True is returned if File Caching services are available; otherwise (e.g. service deactivated by configuration or couldn't start up due to a fault) False is returned.

		"""


	def add_dm_file(self, path: str, server_id: str, file_type: str, timestamp: int, dm_root: str, importance: str, gather_siblings: bool, delete_source: bool) -> object:

		"""

		Add a file to the store as cached copy of a remote DM file.


		Parameters
		----------
		path : str
			Path of the file / directory to be added into
			the cache store.

		server_id : str
			Server side identifier of the DM Object, to which
			this file relates.

		file_type : str
			Describes the file usage / type within the
			specific DM Object.

		timestamp : int
			Last edit timestamp for this file.

		dm_root : str, optional
			Path / URL of the DM root.
			Default value: Current DM root

		importance : str, optional
			Importance level to be attached to the cache
			entry. One of 'NORMAL', 'HIGH' or
			'VERY_HIGH'.
			Default value: 'NORMAL'

		gather_siblings : bool, optional
			Defines whether the other files coexisting in the
			same folder as the one to be cached will be also
			integrated in the cache store or not.
			Default value: False

		delete_source : bool, optional
			Defines whether the source file shall be deleted
			after successful addition to the cache store.
			Default value: False

		Returns
		-------
		object
			This method returns an object of type CacheDmAddResult (see class description for more details).

		"""


	def lookup_dm_file(self, server_id: str, file_type: str, dm_root: str, timestamp_policy: str) -> object:

		"""

		Lookup if a cached copy of a remote DM file is available.


		Parameters
		----------
		server_id : str
			Server side identifier of the DM Object, to which
			this file relates.

		file_type : str
			Describes the file usage / type within the
			specific DM Object.

		dm_root : str, optional
			Path / URL of the DM root.
			Default value: Current DM root

		timestamp_policy : str, optional
			Describes which cache entries to return, in case
			entries with different timestamps satisfy the
			lookup. Either 'ALL' or 'LATEST_ONLY'
			Default value: 'LATEST_ONLY'

		Returns
		-------
		object
			This method returns an object of type CacheLookupResult (see class description for more details).

		"""


	def add_keyless_file(self, path: str, importance: str, gather_siblings: str, delete_source: str) -> int:

		"""

		Add a file in the cache store for which no key is available, but the caching service will generate a (unique) key for it.


		Parameters
		----------
		path : str
			Path of the file / directory to be added into
			the cache store.

		importance : str, optional
			Importance level to be attached to the cache
			entry. One of 'NORMAL', 'HIGH' or
			'VERY_HIGH'.
			Default value: 'NORMAL'

		gather_siblings : str, optional
			Defines whether the other files coexisting in the
			same folder as the one to be cached will be also
			integrated in the cache store or not.
			Default value: False

		delete_source : str, optional
			Defines whether the source file shall be deleted
			after successful addition to the cache store.
			Default value: False

		Returns
		-------
		int
			This method returns an object of type CacheKeylessAddResult (see class description for more details).

		"""


	def lookup_keyless_file(self, identity: str) -> int:

		"""

		Lookup if a file added as a keyless cache entry is available.


		Parameters
		----------
		identity : str
			Identifies this entry in the cache store (was
			assigned during addition by the File Cacher
			itself).

		Returns
		-------
		int
			This method returns an object of type CacheLookupResult (see class description for more details).

		"""


	def deletion_mark(self, token: object) -> int:

		"""

		Mark a cache entry for deletion.


		Parameters
		----------
		token : object
			Object of type CacheToken, referencing the cache
			entry in the store. This object has been provided
			by the File Cacher after an add / lookup file
			operation.

		Returns
		-------
		int
			This method returns a ResultCode describing the operation result (see class description for more details).

		"""

class FileCacherWatchdog():

	"""

	Since the cache store has a finite size, older cache entries are evicted (when
	needed) in order to accommodate new ones. The FileCacherWatchdog object protects 
	one or more cache entries against getting removed from the cache store. This
	way, a user can be certain that cached files will not disappear when they are
	needed / used.
	
	This class employs the following custom Objects:
	
	CacheToken
	This object points to a specific cache entry and is used to uniquely refer to
	- the cache entry inserted via an add operation
	- a specific cache entry returned by a lookup operation
	The user is not supposed to create objects of this class, but should provide
	a token return by the File Cacher itself. CacheToken objects are provided as
	arguments to operations that accept references to concrete cache entries (e.g.
	supervise or deletion mark --- see also FileCacher)

	See Also
	--------
	FileCacher

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    file_cacher = utils.FileCacher()
		    file_cacher_watchdog = utils.FileCacherWatchdog()
		
		    path = "C:/temp/representation.ansa"
		    add_result = file_cacher.add_keyless_file(path, importance="HIGH")
		
		    identity = add_result.identity
		
		    lookup_result = file_cacher.lookup_keyless_file(identity)
		
		    token = lookup_result.files[0].token
		    file_cacher_watchdog.supervise(token)
		
		    # Use the file in the cache store for as long as it is needed
		
		    file_cacher_watchdog.clear()

	"""


	def supervise(self, token: object) -> object:

		"""

		Add a cache entry reference into the list of supervised ones.


		Parameters
		----------
		token : object
			Object of type CacheToken, referencing the cache
			entry in the store. This object has been provided
			by the File Cacher after an add / lookup file
			operation.

		Returns
		-------
		object
			Always returns None.

		"""


	def clear(self) -> object:

		"""

		Clear the list of protected cache entries.


		Returns
		-------
		object
			Always returns None.

		"""

def ShowLog(title_string: str) -> int:

	"""

	This function opens a monitor window and waits for the user to close it. It is similar to
	OpenMonitor only this one waits for the user to close the window before it continues with
	the execution of the script. This makes it useful for displaying a process log and letting
	the user decide if he wants to continue with the execution of the script.

	Parameters
	----------
	title_string : str
		The log window title to show.

	Returns
	-------
	int
		The function returns 1 if OK is pressed and 0 if Cancel is pressed.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.PrintMonitor("User text to display")
		    utils.ShowLog("Window title")


	"""

def XlsxClose(file: object) -> int:

	"""

	Closes the defined ".xlsx" file.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns 0 if the ".xlsx" is not found, or 1 on success.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxCreate() -> object:

	"""

	Creates a new empty xlsx_file.

	Returns
	-------
	object
		Returns a reference to the xlsx_file that is created, or None on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxGetCellValue(file: object, sheet: object, row: int, column: int) -> str:

	"""

	Returns the cell value from the specified row and column, from an .xlsx file ("Sheet1, Sheet2,..").

	Parameters
	----------
	file : object
		A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet name.

	row : int
		The row of the shell.

	column : int
		The column of the cell.

	Returns
	-------
	str
		Returns the value as string, or None if the cell is empty.

	See Also
	--------
	XlsxOpen, XlsxCreate, XlsxInsertSheet, XlsxGetCellValueByName, XlsxSetCellValue, XlsxSetCellValueByName, XlsxSave, XlsxSheetsCount, XlsxMaxSheetCell, XlsxClose

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxInsertSheet(file: object) -> int:

	"""

	Inserts a new empty sheet in the xlsx_file given.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxMaxSheetCell(file: object, sheet: object) -> object:

	"""

	Gets the cell with max row-column in the defined sheet, in the defined file.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet's name.

	Returns
	-------
	object
		Returns a list with 2 elements [row, column], or None if the sheet is empty.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxOpen(filename: str) -> object:

	"""

	Opens an existing xlsx_file and gets a reference to it.

	Parameters
	----------
	filename : str
		The path to the ".xlsx" filename.

	Returns
	-------
	object
		Returns a reference to the xlsx_file object.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSave(file: object, filename: object) -> int:

	"""

	Saves all changes in an opened xlsx_file.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	filename : object, optional
		The path where the ".xlsx" file will be saved.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSetCellValue(file: object, sheet: object, row: int, column: int, value: object) -> int:

	"""

	Sets a value in a cell, in the specified row and column, from sheet ("Sheet1, Sheet2,..") in the selected .xlsx file.

	Parameters
	----------
	file : object
		A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet name.

	row : int
		The row of the shell.

	column : int
		The column of the shell.

	value : object
		A string with the setting value.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	See Also
	--------
	XlsxOpen, XlsxCreate, XlsxInsertSheet, XlsxGetCellValue, XlsxGetCellValueByName, XlsxSetCellValueByName, XlsxSave, XlsxSheetsCount, XlsxMaxSheetCell, XlsxClose

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSheetsCount(file: object) -> int:

	"""

	Gets the count of sheets in the file given.

	Parameters
	----------
	file : object
		A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns the number of sheets, or 0 if the xlsx_file is empty.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxGetCellValueByName(file: object, sheet: object, index: object) -> Any:

	"""

	Gets value from cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..").

	Parameters
	----------
	file : object
		A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : object
		The sheet name.

	index : object
		The cell index.

	Returns
	-------
	Any
		Returns the value as a string, or 0 if the cell is empty.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSetCellValueByName(file: object, sheet: str, index: str, value: str) -> int:

	"""

	Sets a value in a cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..") in the file given.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : str
		A string with the sheet name.

	index : str
		A string with the cell index.

	value : str
		A string with the setting value.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def ClearMonitor() -> int:

	"""

	This function clears the monitor output.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)
		
		    utils.ClearMonitor()
		
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def CloseMonitor() -> int:

	"""

	This function closes the monitor window.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    # utils.CloseMonitor()
		    # Run this function with and without commenting the above line


	"""

def LinesOfMonitor() -> int:

	"""

	This function returns the lines of text in the monitor window.

	Returns
	-------
	int
		Returns an integer describing the number of lines in the monitor window.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def OpenMonitor(title: str) -> int:

	"""

	This function opens a monitor window.
	It can be used to redirect the output of a script, ie to create log of a job.
	The window that opens features a text editor where the script can print and then you can 
	add your comments and save the text.

	Parameters
	----------
	title : str, optional
		The title of the monitor window.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def OpenMonitorNoEdit(title: str) -> int:

	"""

	This function opens a monitor window with the edit area in readonly mode.
	It can be used to redirect output of a script, ie to create log of a job.
	The window that opens features a text editor where thescript can print but you 
	cannot add your comments to save with the text.
	There is an optional argument, the title of the monitor window.

	Parameters
	----------
	title : str
		The title of the monitor window.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitorNoEdit("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)


	"""

def PrintMonitor(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring.
	It is almost identical to the 'print' function with the addition of the three color arguments.

	Parameters
	----------
	txt : str
		The text to print.

	r_int : int
		Red color integer.

	g_int : int
		Green color integer.

	b_int : int
		Blue color integer.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def ReadMonitor(line: int) -> str:

	"""

	This function reads a specific line from monitor window. The line is described by its index, 
	the first line having index 0 and the last LinesOfMonitor()-1.

	Parameters
	----------
	line : int
		The line number.

	Returns
	-------
	str
		Returns the contents of the 'line' or an empty string if the index is less than 0, 
		or greater than the number of lines.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", i, ", text:", txt)


	"""

def SaveMonitor(filename: str) -> int:

	"""

	This function saves the contents of the monitor window in html format.

	Parameters
	----------
	filename : str
		The filename of the file to be saved.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	SaveMonitorToTxt

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", str(i), ", text:", txt)
		    utils.SaveMonitor("/home/user/file.txt")


	"""

def SelectOpenDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for input.

	Parameters
	----------
	startin : str
		The path of the starting directory.

	Returns
	-------
	str
		Returns the selected directory on success, otherwise an empty string.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    dir = utils.SelectOpenDir("/home/user/")
		    print("Selected dir: ", dir)


	"""

def SelectOpenFile(flag: int, *filters: str) -> List[str]:

	"""

	This function opens the file manager and lets the user select one or more files. 
	If the flag is 0 then a single file selection is permitted, while if it is set to 1 
	a multi selection is performed. 
	The user can also type an optional list of file types for filtering.

	Parameters
	----------
	flag : int
		If set to 0, a single file selection is allowed.
		If set to 1, a multi file selection is allowed.

	*filters : str
		File types for filtering. (See example)

	Returns
	-------
	List[str]
		Returns a list containing the file name(s) selected on success.
		On error, or if ESCAPE is pressed, returns an empty list.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    m = utils.SelectOpenFile(0, "Ansa files (*.ansa)", "Foo files (*.foo)")
		    print(m[0])


	"""

def SelectOpenFileIn(initdir: str, flag: int, filters: str) -> object:

	"""

	This function opens the file manager and lets the user select one or more files.
	You can provide the directory in which to start. 
	If you type an empty string ("") or 0 the argument is ignored and the last accessed directory is used instead.
	If flag is 0 then a single file selection is permitted, if it is set to 1 a multi selection is performed.
	The user can also type an optional list of file types for filtering

	Parameters
	----------
	initdir : str
		The initial directory where the file manager will open.
		If set to ' ', the last accessed directory will be used.

	flag : int
		If set to 0, a single file selection is allowed.
		If set to 1, a multi file selection is allowed.

	filters : str, optional
		File types for filtering. (See example)

	Returns
	-------
	object
		Returns a list containing the file name(s) selected, on success.
		On error, or if ESCAPE was pressed, returns an empty list.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    m = utils.SelectOpenFileIn("/home/userdir/", 0)
		    print(m[0])
		    m = utils.SelectOpenFileIn(
		        "/home/userdir/", 0, "Ansa files (*.ansa)", "Foo files (*.foo)"
		    )
		    print(m[0])


	"""

def SelectSaveDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for output.

	Parameters
	----------
	startin : str
		The path of the starting directory.

	Returns
	-------
	str
		Returns the selected directory on success, otherwise an empty string.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    dir = utils.SelectSaveDir("/home/user/")
		    print("Selected dir: ", dir)


	"""

def SelectSaveFile(filter: str='') -> List[str]:

	"""

	This function opens the file manager and lets the user select a file name to save. 
	The 'filter' argument is optional and if provided it is used to filter the displayed files.

	Parameters
	----------
	filter : str, optional
		File types for filtering. (See example)

	Returns
	-------
	List[str]
		Returns a list containing the file name selected on success.
		On error, or if ESCAPE is pressed, returns an empty list.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    m = utils.SelectSaveFile()
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFile("*.ansa")
		    print(m[0])


	"""

def SelectSaveFileIn(init_dir: str, filter: str) -> object:

	"""

	This function opens the file manager and lets the user select a file name to save.
	The 'init_dir' argument lets you specify the directory in which the file manager will open.
	An empty string ("") or a 0 can be passed to open the file manager in the last accessed directory.
	The 'filter' argument is optional and if provided it is used to filter the displayed files.

	Parameters
	----------
	init_dir : str
		The folder to start in.

	filter : str, optional
		File types for filtering. (See example)

	Returns
	-------
	object
		Returns a list containing the file name selected, on success.
		On error, or if ESCAPE was pressed, returns an empty list.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    m = utils.SelectSaveFileIn("/home/userdir/datafiles")
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFileIn("", "*.ansa")
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFileIn(0, "*.ansa")
		    print(m[0])


	"""

def PrintMonitorHtml(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring. It prints html code in 
	monitor window with the addition of the three color arguments.

	Parameters
	----------
	txt : str
		The html code to print.

	r_int : int
		Red color integer.

	g_int : int
		Green color integer.

	b_int : int
		Blue color integer.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    utils.PrintMonitorHtml("<b>some text</b>", 255, 0, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def SaveMonitorToTxt(filename: str) -> int:

	"""

	This function saves the contents of the monitor window in plain text format.

	Parameters
	----------
	filename : str
		The path and the filename where the text will be saved.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	SaveMonitor

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", str(i), ", text:", txt)
		    utils.SaveMonitorToTxt("/home/user/file.txt")


	"""

def XlsxMergeCells(file: object, sheet: str, row1: int, column1: int, row2: int, column2: int) -> object:

	"""

	Merges the specified cells of an ".xlsx" file.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cells' sheet.

	row1 : int
		The row number of the top left cell.

	column1 : int
		The column number of the top left cell.

	row2 : int
		The row number of the bottom right cell.

	column2 : int
		The column number of the bottom right cell.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxMergeCells(file, sheet, 2, 2, 4, 4)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellBorder(file: object, sheet: str, row: int, column: int, borders: str, style: str, color: str) -> object:

	"""

	Set the borders of a cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell.

	column : int
		The column number of the cell.

	borders : str
		The specified border. The accepted values are "left", "right",
		"top", "bottom", and any combination of them by using the "|"
		(e.g. "top|bottom").

	style : str
		The style of the line. The accepted values are "dashdot",
		"dashdotdot", "dashed", "dotted", "double", "hair", "medium",
		"mediumdashdot", "mediumdashdotdot", "mediumdashed", "none",
		"thick", "thin", and "slantdashdot".

	color : str
		The RGB color of the line in comma separated string.
		(e.g. "100, 100, 100").

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBorder(file, sheet, 2, 2, "top|bottom", "double", "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellBackgroundColor(file: object, sheet: str, row: int, column: int, color: str) -> object:

	"""

	Sets the background color of a cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell.

	column : int
		The column number of the cell.

	color : str
		The RGB background color of the cell in a comma separated string.
		(e.g. "100, 100, 100").

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBackgroundColor(file, sheet, 2, 2, "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxGetSheetName(file: object, index: int) -> str:

	"""

	Gets the name of a sheet by its index.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	index : int
		The index of the sheet of the specified file.

	Returns
	-------
	str
		Returns the name of the sheet on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBorder(file, sheet, 2, 2, "top|bottom", "double", "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAdjustRowHeight(file: object, sheet: str, row: int) -> object:

	"""

	Adjusts the height of a row.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number starting from 0.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAdjustRowHeight(file, sheet, 1)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAdjustColumnWidth(file: object, sheet: str, column: int) -> object:

	"""

	Adjusts the width of a column.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	column : int
		The column number starting from 0.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAdjustColumnWidth(file, sheet, 1)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellFontStyle(file: object, sheet: str, row: int, column: int, style: str) -> object:

	"""

	Sets the font style in a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	style : str
		The specified font style. The accepted values are "bold", "italic", "underline" 
		and any combination of them by using the symbol "|". (e.g. "bold|italics")

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxSetCellFontStyle(file, sheet, 1, 1, "bold|italic")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAlignCellVertically(file: object, sheet: str, row: int, column: int, alignment: str) -> object:

	"""

	Aligns vertically a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	alignment : str
		The alignment type. The accepted values are "top", "bottom" and "center".

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAlignCellVertically(file, sheet, 1, 1, "center")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAlignCellHorizontally(file: object, sheet: str, row: int, column: int, alignment: str) -> object:

	"""

	Aligns horizontally a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	alignment : str
		The alignment type. The accepted values are "left", "right" and "center".

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAlignCellHorizontally(file, sheet, 1, 1, "center")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellFontColor(file: object, sheet: str, row: int, column: int, color: str) -> object:

	"""

	Sets the font color in a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	color : str
		The RGB font color of the cell in a comma separated string. (e.g. "100, 100, 100")

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxSetCellFontColor(file, sheet, 1, 1, "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def CreateWindowsLinkFile(target: str, link_file_path: str, mount_mapping_table: object) -> bool:

	"""

	This function creates a Windows Link file (Shortcut) pointing to an arbitrary
	destination. This function is not necessary to be executed in a Windows
	environment: Windows Link files can be created by a Linux running process, and
	are usable in the Windows domain.
	The condition for this interoperability is that the link target is a path that
	is visible from both Windows / non-Windows environments and paths can be 
	converted across environments by doing prefix substitutions (see description of
	mount_mapping_table below).

	Parameters
	----------
	target : str
		Destination of the link file, i.e. the path where the created
		shortcut will point to. This path is expressed in its native form,
		i.e. it must be a meaningful path in the environment where this
		python function will be executed.

	link_file_path : str
		Path where the Windows Link file will be created. The file name 
		provided with this path must have a '.lnk' extension.

	mount_mapping_table : object, optional
		A sequence of utils.MountMapping objects, which will be used for
		transforming the link target path from its native form into one that 
		is usable in the Windows domain.
		If the function is executed in a non Windows environment, a non empty 
		Mount Mapping Table must be available, so that the unix paths can
		be converted into paths that are meaningful in the Windows domain.
		If the function is executed in a Windows environment, there are no
		requirements for such a Mount Mapping Table. However, if the
		generated Link files are to be used in the Unix domain, then an
		appropriately configured Mount Mapping Table is highly recommended.
		If no Mount Mapping Table is provided as argument, then the global
		Mount Mapping Table configured in the ANSA defaults settings is used.

	Returns
	-------
	bool
		This function returns 'True' if the Link file was succesfully created and 'False'
		if the creation failed.

	See Also
	--------
	MountMapping

	Examples
	--------
	::

		import os
		import ansa
		
		
		def main():
		    mount_mapping_table = []
		    mount_mapping_table.append(utils.MountMapping("/mnt/win_disk_1", r"\\\\nas\\disk1"))
		    mount_mapping_table.append(
		        utils.MountMapping("/mnt/net_scratch", r"\\\\team_server\\scratch")
		    )
		
		    utils.CreateWindowsLinkFile(
		        "/mnt/win_disk_1/results/report.pdf", "report.pdf.lnk", mount_mapping_table
		    )


	"""

def SendEmail(fields: object) -> int:

	"""

	Send an email based on the input arguments.

	Parameters
	----------
	fields : object
		This is a dictionary that contains all inputs necessary for sending the email.
		Available options for the input dictionary are:
		"email agent": The application used for sending the email, e.g. "thunderbird", "outlook" or "no email agent".
		"email agent path": The path to the application,.
		"thunderbird application path": The path to Thunderbird application.
		"outlook application path": The path to the Outlook application.
		"email attachment folder": All files in this folder will be attached to the message.
		"From:": The sender's email address.
		"To:": The recipients' email addresses.
		"Subject:": The subject of the message.
		"Body:": The actual message that will be the body.
		"signature": If you want a signature to be appended to the body.
		"use gui": If you want a GUI to popup. By default this is "no".
		
		In case of a "no email agent" the following options are needed:
		"server name": The outgoing mail server (SMTP), e.g. "smtp.gmail.com"
		"connection security": Connection security, e.g. "None", "SSL", "STARTTLS"
		"authentication type": The authentication method, e.g. "Plain", "Login", "NTLM"
		"port": The port used for the connection, e.g. 465
		
		In case of authentication, you may need to use a username/password with the "Username" and "Password" keys.

	Returns
	-------
	int
		Always return 0.

	Examples
	--------
	::

		import ansa
		
		message_to_send = {}
		message_to_send["server name"] = "localhost"
		message_to_send["connection security"] = "None"
		message_to_send["authentication type"] = "Plain"
		message_to_send["port"] = "25"
		message_to_send["email agent"] = "Custom"
		message_to_send["use gui"] = "no"
		message_to_send["Subject:"] = "Download Resulted with empty parts"
		text_for_message = "This is a list of parts with missing representations..."
		message_to_send["Body:"] = text_for_message
		message_to_send["From:"] = "user@mail.local"
		message_to_send["To:"] = "other_user@mail.local"
		ansa.utils.SendEmail(message_to_send)


	"""

def AddCurveData(curve: object, coords: object):

	"""

	This function adds coordinates data to curve. For example: 
	AddCurveData(curve, [(x1,y1), (x2,y2), (x3,y3), ...])

	Parameters
	----------
	curve : object
		This argument is the created curve.

	coords : object, optional
		This argument is a list of pairs of floats.

	See Also
	--------
	utils.CreateCurve

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def DeleteCurve(curve: object):

	"""

	This function deletes the curve given as argument.
	
	

	Parameters
	----------
	curve : object
		This argument is the curve given to be deleted.

	See Also
	--------
	utils.CreateCurve

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def GetMaterialPalette():

	"""

	This function gets a dictionary with material names and colors as described in palettes.xml or from a hardcoded palette (if not set in xml file). Dictionary has as keys the material type string and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'N/A Material Name': [100, 100, 100], 'Composite': [255, 165, 0], 'Silicon': [208, 238, 238], 'Steel': [70, 130, 180], 'Glass': [177, 211, 231], 'Multi-Material': [255, 0, 255], 'Plastic': [255, 0, 0], 'Aluminium': [0, 128, 0], 'Rubber': [255, 20, 147], 'Magnesium': [255, 215, 0], 'N/A Material Type': [169, 169, 169]}

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		material_type = "Steel"
		r_g_b = [0, 0, 0]
		
		material_colors_map = utils.GetMaterialPalette()
		if material_type in material_colors_map:
		    r_g_b = material_colors_map[material_type]
		else:
		    if "N/A Material Type" in material_colors_map:
		        r_g_b = material_colors_map["N/A Material Type"]
		print(r_g_b)


	"""

def GetCustomAttributePalette(keyword: str):

	"""

	This function gets a color palette for the attribute given as argument. It returns a dictionary with attribute names and colors as described in palettes.xml, if available. Otherwise, for some cases, it returns a dictionary from a hardcoded palette (cases like: Subsystem, Material, Diff, Status). Dictionary has as keys the attribute names and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'Doors': [105, 65, 225], 'Roof': [255, 127, 0], 'Unused': [255, 255, 205], 'Frontsystem': [0, 139, 139], 'BiW': [178, 34, 34]}

	Parameters
	----------
	keyword : str
		This argument is the custom attribute keyword for the palette.

	See Also
	--------
	utils.GetMaterialPalette

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		palette = utils.GetCustomAttributePalette("Subsystem")
		print(palette)
		
		palette = utils.GetCustomAttributePalette("Status")
		print(palette)


	"""

def GetGlobalMountMappingTable() -> object:

	"""

	This function returns all the Mount Mappings that are currently stored in the
	global Mount Mapping table.

	Returns
	-------
	object
		This function return a list of MountMapping objects

	See Also
	--------
	utils.MountMapping, utils.SetGlobalMountMappingTable

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def printMountMappingTable(mount_mapping_table):
		    for mapping in mount_mapping_table:
		        print(
		            "Mapping {} <--> {}".format(
		                mapping.unix_mount_path, mapping.win_server_share
		            )
		        )
		
		
		def main():
		    table = utils.GetGlobalMountMappingTable()
		
		    printMountMappingTable(table)
		
		    # Append entries to global mount mapping table
		    table.append(utils.MountMapping("/mnt1/disk_1", r"\\\\nas\\disk1"))
		    table.append(utils.MountMapping("/mnt2/net_scratch", r"\\\\team_server\\scratch"))
		    utils.SetGlobalMountMappingTable(table)
		
		    printMountMappingTable(table)


	"""

def SetGlobalMountMappingTable(mount_mapping_table: object):

	"""

	This function sets the Global Mount Mapping Table with the sequence of Mount
	Mappings received as argument.

	Parameters
	----------
	mount_mapping_table : object
		Sequence of MountMapping objects that will be stored
		in the Global Mount Mapping Table

	See Also
	--------
	utils.MountMapping, utils.GetGlobalMountMappingTable

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def printMountMappingTable(mount_mapping_table):
		    for mapping in mount_mapping_table:
		        print(
		            "Mapping {} <--> {}".format(
		                mapping.unix_mount_path, mapping.win_server_share
		            )
		        )
		
		
		def main():
		    table = utils.GetGlobalMountMappingTable()
		
		    printMountMappingTable(table)
		
		    # Append entries to global mount mapping table
		    table.append(utils.MountMapping("/mnt1/disk_1", r"\\\\nas\\disk1"))
		    table.append(utils.MountMapping("/mnt2/net_scratch", r"\\\\team_server\\scratch"))
		    utils.SetGlobalMountMappingTable(table)
		
		    printMountMappingTable(table)


	"""

def LaunchLingeringMLWorker(context_dir: str, cmd: object, env: str, dbg: bool) -> bool:

	"""

	This function launches a lingering ML Toolkit worker process. The command 
	provided by the user will be launched as a process within an ML Toolkit
	environment and its stdin / stdout channels will be exposed over a TCP socket.
	By reading the details stored within the context directory, clients are able
	to connect to this TCP socket and communicate with the worker process.

	Parameters
	----------
	context_dir : str
		Path where the context holding directory will be
		created. The context holding directory will be set
		as readable only for the user launching the
		lingering worker, and will hold all information
		(e.g. port / authentication token) necessary for a
		client to connect to it.

	cmd : object
		A sequence of strings containing the command plus all 
		arguments describing how the lingering worker is to be
		launched.

	env : str, optional
		Provides the name of the ML Toolkit environment, into
		which the lingering workers should be launched.
		Default value: 'consolidated'

	dbg : bool, optional
		Describes whether debug mode should be employed. If
		True, then the context directory will not be deleted 
		on worker shut down. Also, the log file will include
		more information, that could assist troubleshooting.
		Default value: False

	Returns
	-------
	bool
		Returns True when the launch was successfully initiated.

	See Also
	--------
	utils.LingeringMLInstance, utils.LingeringMLClient

	Examples
	--------
	::

		import time
		
		import ansa
		from ansa import utils
		
		
		def createLingeringMLInstance(dir):
		    try:
		        inst = utils.LingeringMLInstance(dir)
		    except Exception as e:
		        print("Lingering ML Instance failed with exception {}".format(str(e)))
		        inst = None
		    return inst
		
		
		def loopForLingeringInstance(dir, max_attempts):
		    for _ in range(max_attempts):
		        inst = createLingeringMLInstance(dir)
		        if inst:
		            return inst
		        time.sleep(1)
		    return None
		
		
		def main():
		    context_dir = "/home/main_user/tmp/adapter_context"
		    cmd = ["python", "/home/main_user/ml_scripts/calc_worker.py"]
		    launch_res = utils.LaunchLingeringMLWorker(context_dir, cmd)
		
		    if not launch_res:
		        return
		    inst = loopForLingeringInstance(context_dir, 10)
		    inst.write("Input: 1, 2, 3, 4\\n")
		
		    try:
		        response = inst.read(10)
		        print("Worker responded with: {}".format(response))
		    except TimeoutError:
		        print("Read timed-out!")


	"""

def XlsxRenameSheet(file: object, current_name: str, new_name: str):

	"""

	Renames the specified sheet in the xlsx_file given.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	current_name : str
		The current name of the sheet.

	new_name : str
		The new name that will be given to the sheet.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    # open xlsx_file
		    xl_file = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # insert new empty sheet
		    utils.XlsxRenameSheet(xl_file, "Sheet1", "Data")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_file, "Data", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_file, "Data", "A2", "10")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_file, "/home/user/mysheet.xlsx")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_file)


	"""

class Messenger():

	"""

	Class for handling messages in python scripts.
	Messenger is a unique object (singleton) in the program, every messenger instance points to the same object.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import constants
		from ansa import session
		from ansa import utils
		
		
		def basic_example():
		    m = utils.Messenger()
		    m.echo(False)  # No messages are shown on the ANSA Info Window
		    base.InputNastran("laminate.nas")
		    m.print("Input finished")  # Print only the messages that are needed
		    m.echo(True)  # Reset mode
		    return
		
		
		def get_and_print_buffer_to_file():
		    m = utils.Messenger()
		    m.echo(False)  # No messages are shown on the ANSA Info Window
		    m.start_buffering()  # Capture the print buffer of the program
		
		    print("Test")
		    session.New("discard")
		
		    base.InputNastran("laminate.nas")
		    m.stop_buffering()  # End the capture the print buffer of the program
		    m.print(
		        "Input finished"
		    )  # Messenger prints are always shown in the ANSA info window
		    ret_buf = m.get_buffer()
		
		    fp = open("output_buf.txt", "w")
		    for item in ret_buf:
		        fp.write(item + "\\n")
		    fp.close()
		
		    m.echo(True)
		    return
		
		
		def print_to_stdout_only():
		    m = utils.Messenger()
		    m.pyprint_capture(False)  # All program prints will be printed in the terminal
		    # can be used for de-bug purposes
		    session.New("discard")
		    base.InputNastran("laminate.nas")
		    m.print("Input finished")
		    m.pyprint_capture(True)
		    return
		
		
		def html_examples():
		    m = utils.Messenger()
		
		    m.print("<b>Bold Text</b>", format="html")
		    m.print("<i>Italic Text</i>", format="html")
		    m.print("<p>This is a paragraph text.</p>", format="html")
		    m.print("<br />", format="html")
		    m.print("<p>This is a paragraph text.</p>", format="html")
		    m.print("<hr>", format="html")  # Line works only in ANSA Info
		    m.print(
		        '<table border="1"><tr><td>One</td><td>Two</td></tr></table>', format="html"
		    )

	"""


	def start_buffering(self):

		"""

		Starts the messenger's buffering. No action if buffering has already started.


		"""


	def stop_buffering(self):

		"""

		Stops the messenger's buffering. No action if buffering hasn't started.


		"""


	def print(self, message: str, format: str):

		"""

		Prints a text message in ansa info, stdout (and script editor's output).The message can have one of two formats: txt format or html format.


		Parameters
		----------
		message : str
			The message we want to print.

		format : str, optional
			The message's format.
			Options are:
			-"txt" (default)
			-"html"

		"""


	def echo(self, mode: bool):

		"""

		This function affects only the printing messages destination, not the buffering functionality.Setting Echo to true, every message will be printed in ANSA Info (or script Editor output) and in stdout.(Default behavior) Setting Echo to false, messages won't be printed in any output, except of script-error messages that will be printed in stdout.


		Parameters
		----------
		mode : bool
			The messengers Echo mode.

		"""


	def pyprint_capture(self, mode: bool):

		"""

		This function affects only the printing messages destination, not the buffering functionality. Setting capture to true (default setting), every call to Python's native print function, will have the data printed both in ANSA Info (or script Editor output) and in stdout, (provided  Echo is also set to true). When seting capture to false, messages will be printed only in stdout, effectively reverting any changes made to Python's native print statement by ANSA.


		Parameters
		----------
		mode : bool
			The messenger's capture mode.

		"""


	def get_buffer(self) -> object:

		"""

		Returns a list of strings with all the buffered messages.


		Returns
		-------
		object
			A list of strings with all the buffered messages.

		"""


	def clear(self):

		"""

		This function clears the messenger's buffer.


		"""

class QualityAssurance():

	"""

	QualityAssurance class is a group of methods that can be used to collect statistical data from your program
	This data can be execution times, memory usage or any kind of values.
	The programmer should create one Quality assurance object and use the methods to collect info from the program.
	
	
	A process stands for a block of code. start_process and stop_process declare the limits of the block. 
	A block can contain other blocks and like that a tree struct of blocks can be created. 
	Execution times are wall-times of these blocks of code. 
	
	Each of these processes can contain also a set of values. These values are stored per line. So at a running block the
	programmer can add a line (with a name) and at the current line can add values(with name also).
	
	Also when the output of this mechanism is used for comparison reasons the programmer can add restrictions to set different
	compare rules per value or process.
	
	For memory measurements it is recommended to use GetProcessSystemMetrics instead.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import utils
		
		
		def main():
		    qa = utils.QualityAssurance()
		
		    q1 = qa.start_process("MeshPart")
		
		    # My program to mesh a part
		    # Preparations for mesh
		
		    q2 = qa.start_process("MeshCore")
		
		    # A function that mesh the part
		
		    qa.add_new_line("mesh_data")
		    qa.add_value("elements_number", 1421)
		    qa.add_current_memory_usage_value("mem_used_after_mesh")
		
		    qa.stop_process(q2)
		    qa.stop_process(q1)

	"""


	def start_process(self, process_name: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float) -> object:

		"""

		Declare the start of a QA process.


		Parameters
		----------
		process_name : str
			The name of the process.

		run_if : bool, optional
			Condition to start the process.

		compare_val : float, optional
			A custom compare ratio (decimal) for the time of the 
			process (global value if omitted).

		down_limit : float, optional
			A custom down compare limit value for the time of the 
			process (global value if omitted).

		up_limit : float, optional
			A custom upper compare limit value for the time of the 
			process (global value if omitted).

		Returns
		-------
		object
			Returns an object that should be used to declare the stop of the block.

		"""


	def stop_process(self, running_process: object):

		"""

		Declare the end of a QA process.


		Parameters
		----------
		running_process : object
			The object that was returned from start_process.

		"""


	def add_new_line(self, name: str, run_if: bool):

		"""

		Add a new line on running process.


		Parameters
		----------
		name : str
			The name of the line.

		run_if : bool, optional
			Condition to add the line.

		"""


	def add_value(self, value_name: str, value: object, run_if: bool, compare_val: float, down_limit: float, up_limit: float, compare_val_absolute: float, decimal_places: int):

		"""

		add a value on the current line.


		Parameters
		----------
		value_name : str
			The name of the value.

		value : object
			The value. Can be float, integer or string.

		run_if : bool, optional
			Condition to add the value.

		compare_val : float, optional
			A custom compare ratio (decimal) for the current value 
			(global value if omitted).

		down_limit : float, optional
			A custom down compare limit for the current value 
			(global value if omitted).

		up_limit : float, optional
			A custom upper compare limit for the current value 
			(global value if omitted).

		compare_val_absolute : float, optional
			A custom absolute compare limit for the current value 
			(global value if omitted).

		decimal_places : int, optional
			Number of decimal places for a float value.

		"""


	def start_recording_to_file(self, record_times_flag: bool, run_if: bool):

		"""

		Start to record the output of the Quality assurance mechanism to a file.


		Parameters
		----------
		record_times_flag : bool, optional
			If false it would ignore the times for the processes.

		run_if : bool, optional
			Condition to start recording.

		"""


	def stop_recording_to_file(self, file_name_to_save: str, run_if: bool):

		"""

		Stop the recording to file and save a Quality assurance txt file.


		Parameters
		----------
		file_name_to_save : str, optional
			A file name for the newly created txt file of quality 
			assurance report.

		run_if : bool, optional
			Condition to run stop recording.

		"""


	def set_default_values(self, compare_time: float, compare_double: float, compare_int: float, compare_memory: float, down_limit_time: float, down_limit_double: float, down_limit_ints: int, down_limit_memory: float, up_limit_time: float, up_limit_double: float, up_limit_ints: int, up_limit_memory: float, compare_double_absolute: float, compare_ints_absolute: int, compare_time_absolute: float, compare_memory_absolute: float):

		"""

		Set the deafault compare values for the quality assurance mechanism.


		Parameters
		----------
		compare_time : float, optional
			Set the default compare ratio for times.

		compare_double : float, optional
			Set the default compare ratio for floats.

		compare_int : float, optional
			Set the default compare ratio for integers.

		compare_memory : float, optional
			Set the default compare ratio for memory values.

		down_limit_time : float, optional
			Set the default down limit for comparing times.

		down_limit_double : float, optional
			Set the default down limit for comparing floats.

		down_limit_ints : int, optional
			Set the default down limit for comparing integers.

		down_limit_memory : float, optional
			Set the default down limit for comparing memory values.

		up_limit_time : float, optional
			Set the default upper limit for comparing times.

		up_limit_double : float, optional
			Set the default upper limit for comparing floats.

		up_limit_ints : int, optional
			Set the default upper limit for comparing integers.

		up_limit_memory : float, optional
			Set the default upper limit for comparing memory values.

		compare_double_absolute : float, optional
			Set the default absolute limit for comparing doubles.

		compare_ints_absolute : int, optional
			Set the default absolute limit for comparing integers.

		compare_time_absolute : float, optional
			Set the default absolute limit for comparing times.

		compare_memory_absolute : float, optional
			Set the default absolute limit for comparing memory.

		"""


	def add_current_memory_usage_value(self, value_name_current_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float, compare_val_absolute: float) -> float:

		"""

		Add as value the current memory usage of the program. 


		Parameters
		----------
		value_name_current_memory : str
			The name of the value.

		run_if : bool, optional
			Condition to add the value.

		compare_val : float, optional
			A custom compare ratio (decimal) for current memory value.

		down_limit : float, optional
			A custom down limit for current memory value.

		up_limit : float, optional
			A custom upper limit for current memory value.

		compare_val_absolute : float, optional
			A custom absolute compare limit for the current value

		Returns
		-------
		float
			Returns the current memory usage of the program

		"""


	def add_peak_memory_usage_value(self, value_name_peak_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float, compare_val_absolute: float) -> float:

		"""

		Add as value the peak memory usage of the program.


		Parameters
		----------
		value_name_peak_memory : str
			The name of the value.

		run_if : bool, optional
			Condition to add the value.

		compare_val : float, optional
			A custom compare ratio (decimal) for current memory 
			value.

		down_limit : float, optional
			A custom down limit for current memory value.

		up_limit : float, optional
			A custom up limit for current memory value.

		compare_val_absolute : float, optional
			A custom absolute compare limit for the current value

		Returns
		-------
		float
			Returns the peak memory usage of the program

		"""


	def freeze(self, freeze_if: bool):

		"""

		Freeze the quality assurance mechanism. All actions are ignored after that.


		Parameters
		----------
		freeze_if : bool, optional
			Condition to freeze the mechanism.

		"""


	def unfreeze(self, unfreeze_if: bool):

		"""

		Unfreeze the quality assurance mechanism.


		Parameters
		----------
		unfreeze_if : bool, optional
			Condition to unfreeze the mechanism.

		"""


	def start_lap(self, clock_name: str, run_if: bool) -> object:

		"""

		A clock will start to run and it will stop at stop_lap.The laps have names.When running process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps. 


		Parameters
		----------
		clock_name : str
			The name of the clock.

		run_if : bool, optional
			Condition to start the lap.

		Returns
		-------
		object
			An object that will be given sto stop_lap method.

		"""


	def stop_lap(self, running_clock: object):

		"""

		The method to stop a lap.


		Parameters
		----------
		running_clock : object
			The object that start_lap had returned.

		"""


	def start_lap_on_master(self, clock_name: str, run_if: bool):

		"""

		A clock will start to run and it will stop at stop_lap.The laps have names.When the master process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps.


		Parameters
		----------
		clock_name : str
			The name of the clock.

		run_if : bool, optional
			Condition to start the lap.

		"""

class MountMapping():

	"""

	The objects of this class describe how paths can be converted between their
	Windows and Unix forms. When network storage is visible from both Windows / Linux 
	workstations, these objects describe how the server shares used in the Windows
	domain correspond to the mount paths used in the Linux domain.

	Examples
	--------
	::

		import os
		import ansa
		
		
		def main():
		    mount_mapping_table = []
		    mount_mapping_table.append(utils.MountMapping("/mnt/win_disk_1", r"\\\\nas\\disk1"))
		    mount_mapping_table.append(
		        utils.MountMapping("/mnt/net_scratch", r"\\\\team_server\\scratch")
		    )
		
		    utils.CreateWindowsLinkFile(
		        "/mnt/win_disk_1/results/report.pdf", "report.pdf.lnk", mount_mapping_table
		    )

	"""


	unix_mount_path: str = None
	"""
	The mount path which is used for making the same network
	drive visible in the Linux domain.

	"""

	win_server_share: str = None
	"""
	The server share with which a specific network drive is
	visible in the Windows domain.

	"""

	def __init__(self, unix_mount_path: str, win_server_share: str) -> object:

		"""

		Object constructor of the class


		Parameters
		----------
		unix_mount_path : str
			The mount path which is used for making the same network drive visible in the Linux domain.

		win_server_share : str
			The server share with which a specific network drive is
			visible in the Windows domain.

		Returns
		-------
		object

		"""

class LingeringMLInstance():

	"""

	Objects of this class enable the communication with lingering ML Toolkit worker
	instances, by providing access to their stdin / stdout channels.

	See Also
	--------
	utils.LingeringMLClient

	Examples
	--------
	::

		from ansa import utils
		
		inst = utils.LingeringMLInstance("/home/main_user/tmp/adapter_context")
		inst.write("Input: 1, 2, 3, 4\\n")
		
		try:
		    response = inst.read(10)
		    print("Worker responded with: {}".format(response))
		except TimeoutError:
		    print("Read timed-out!")
		except IOError:
		    print("Read IO Error!")

	"""


	def __init__(self, path: str):

		"""


		Parameters
		----------
		path : str
			Path to the directory that has been used by the launcher
			of lingering ML Toolkit worker instances to store context
			information.

		"""


	def read(self, timeout: int) -> str:

		"""

		Reads from the lingering ML Toolkit worker instance's stdout channel. A TimeoutError exception is raised, when the timeout expires and no data were read. An IOError exception is raised, when the WebSocket connection was dropped before any data could be read.


		Parameters
		----------
		timeout : int, optional
			Defines the maximum time interval to block, waiting
			for incoming data. 
			Default value: 0 (non-blocking)

		Returns
		-------
		str
			Returns string with the data read

		"""


	def write(self, data: str):

		"""

		Write to the Lingering ML Toolkit worker instance's stdin channel.


		Parameters
		----------
		data : str
			Data to be written

		"""


	def has_error(self) -> bool:

		"""

		Checks whether the connection is in erroneous state


		Returns
		-------
		bool
			Returns True when an error has occurred.

		"""


	def disconnect(self):

		"""

		Disconnects from the Lingering ML Toolkit worker instance


		"""

class LingeringMLClient():

	"""

	Objects of this class enable the communication with lingering ML Toolkit worker
	instances using a higher level protocol, compared to LingeringMLInstance or
	BALStreamsCommunicator objects.
	
	Specifically, instead of providing raw access to the stdin / stdout channels of
	the worker instance, in this case it is possible to exchange python objects. 
	Also, message acknowledgement happens behind the scenes so that no messages get
	lost.
	
	In order to use LingeringMLClient, the worker must implement the Server part of
	this protocol.

	See Also
	--------
	utils.LingeringMLInstance, utils.BALStreamsCommunicator

	Examples
	--------
	::

		from ansa import utils
		
		inst = utils.LingeringMLInstance("/home/main_user/tmp/adapter_context")
		client = utils.LingeringMLClient(inst)
		
		op = "add"
		num_a = 34
		num_b = 60
		
		print("Sending operation '{} {} {}' to worker".format(num_a, op, num_b))
		user_data = {"op": op, "a": num_a, "b": num_b}
		client.send_msg(user_data)
		
		try:
		    msg = client.get_msg(10)
		    print("Worker responded with: {}".format(str(msg)))
		except TimeoutError:
		    print("Timeout without any messages received")
		
		client.close_worker()

	"""


	def __init__(self, endpoint: object):

		"""


		Parameters
		----------
		endpoint : object
			An active LingeringMLInstance or BALStreamsCommunicator object

		"""


	def get_msg(self, timeout: int, unit: str) -> object:

		"""

		Read a user message from the Lingering ML Toolkit worker. A TimeoutError exception is raised, when the timeout expires and no message was received.


		Parameters
		----------
		timeout : int, optional
			Defines the maximum time interval to block, waiting
			for incoming messages. 
			Default value: 0 (non-blocking)

		unit : str, optional
			Defines the unit of time used to be seconds or milliseconds. 
			Default value: "s" (seconds)
			Accepted values: "s" (seconds), "ms" (milliseconds)

		Returns
		-------
		object
			Returns an arbitrary object, sent by the remote end.

		"""


	def send_msg(self, user_msg: object):

		"""

		Send a message to the Lingering ML Toolkit worker instance.


		Parameters
		----------
		user_msg : object
			Arbitrary object to be transmitted to the remote end. Object must be picklable.

		"""


	def close_worker(self):

		"""

		Signal the remote Lingering ML Toolkit worker instance to shut down.


		"""

class DMHasher():

	"""

	The DMHasher object provides access to the hasing mechanism that is employed for
	the calculation of hashes in DM Objects.

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		hasher = utils.DMHasher()
		
		
		def main():
		    string_dict = {"key1": "value1", "key2": "value2"}
		    hasher.add_dict(string_dict)
		
		    print("Hash of dictionary = ", hasher.get_result())

	"""


	def add_dict(self, string_dict: object):

		"""

		Inserts a string-to-string dictionary into the hashcalculation.


		Parameters
		----------
		string_dict : object
			String-to-string dictionary to be added in the
			hash calculation

		"""


	def get_result(self) -> str:

		"""

		Get the hash string according to the data that have beenadded into the hasher thus far.


		Returns
		-------
		str
			String with the hashing result

		"""

class BALStreamsCommunicator():

	"""

	Objects of this class enable the communication with processes running within a 
	Beta Apps Launcher (BAL) environment, by providing an interface to their 
	stdin / stdout channels.

	See Also
	--------
	utils.LingeringMLClient

	Examples
	--------
	::

		import ansa
		from ansa import utils
		
		
		def main():
		    comm = utils.BALStreamsCommunicator(
		        "wss://server:9876/bal/f7a0a71f-3ab9-4336-a31f-9b5a41a10185_192-9-121-76_9595"
		    )
		    comm.write("Input: 1, 2, 3, 4")
		
		    try:
		        response = comm.read(10)
		        print("Output: ", response)
		    except TimeoutError:
		        print("Read timed-out!")
		    except IOError:
		        print("Read IO Error!")

	"""


	def __init__(self, url: str, auth_token: str):

		"""


		Parameters
		----------
		url : str
			URL to the WebSocket service that BAL has 
			opened for the specific process

		auth_token : str, optional
			Authentication Token to be used for authorizing
			the WebSocket connection. Argument is mandatory
			for connections to SPDRM servers with version greater 
			or equal to 1.8.0

		"""


	def read(self, timeout: int) -> str:

		"""

		Reads from the stdout channel of the BAL process. A TimeoutError exception is raised, when the timeout expires and no data were read. An IOError exception is raised, when the WebSocket connection was dropped before any data could be read.


		Parameters
		----------
		timeout : int
			Defines the maximum time interval to block, waiting
			for incoming data.
			Default value: 0 (non-blocking)

		Returns
		-------
		str
			Returns string with the data read

		"""


	def write(self, data: str):

		"""

		Write to the stdin channel of the BAL process.


		Parameters
		----------
		data : str
			Data to be written

		"""


	def has_error(self) -> bool:

		"""

		Checks whether the connection is in erroneous state


		Returns
		-------
		bool
			Returns True when an error has occurred.

		"""


	def disconnect(self):

		"""

		Disconnects from the WebSocket interface towards the process stdin / stdout.


		"""

class ParallelJobsDispatcher():

	"""

	Objects of this class enable the dispatching of parallel python script jobs to BETA app workers.
	
	Each parallel job is depicted through a python file, either pre-existing or created just-in-time temporarily.

	Examples
	--------
	::

		from ansa import utils
		
		
		def main():
		    scripts = [
		        "/home/user/python_scripts/disp_script1.py",
		        "/home/user/python_scripts/disp_script2.py",
		        "/home/user/python_scripts/disp_script3.py",
		        "/home/user/python_scripts/disp_script4.py",
		        "/home/user/python_scripts/disp_script5.py",
		        "/home/user/python_scripts/disp_script6.py",
		    ]
		
		    launch_command = "/home/user/apps/ansa_v22.1.x/ansa64.sh"
		
		    dispatcher = utils.ParallelJobsDispatcher(
		        command=launch_command, max_num_workers=4, keep_workers_hot_time_limit=10
		    )
		    results = dispatcher.run(scripts)
		
		    # get some new scripts and run them on the same workers
		    results = dispatcher.run(scripts)
		
		
		if __name__ == "__main__":
		    main()

	"""


	def __init__(self, command: str, max_num_workers: int, keep_workers_hot_time_limit: int, script_function_to_call: str, redirection_logs_path: str, job_time_limit: int, worker_launch_time_limit: int, worker_initialization_script: str, database_handling: str) -> object:

		"""


		Parameters
		----------
		command : str
			Launch command of Beta app.

		max_num_workers : int, optional
			The maximum number of workers to use simultaneously.
			Default value: 2

		keep_workers_hot_time_limit : int, optional
			How much time in minutes, a worker will stay alive and wait for future jobs when a batch of jobs finishes.
			Default value: 0 (no waiting)

		script_function_to_call : str, optional
			Which script function to call in user provided (job) scripts.
			Default value: "main"

		redirection_logs_path : str, optional
			A directory to deposit workers' console redirection files into.
			Default value: a temporary directory that will be deleted after execution

		job_time_limit : int, optional
			Any job that exceeds this time limit(minutes) during execution, will cause its worker's death.
			Default value: 60

		worker_launch_time_limit : int, optional
			How much time to wait(minutes) for a worker to get launched and communicate back.
			Default value: 5

		worker_initialization_script : str, optional
			An initialization script to execute on each worker just after launch.
			Default value: None

		database_handling : str, optional
			Whether the database should be kept or reset before a script job is executed.
			Default value: "reset" (do not keep database)
			Accepted values: "reset" (do not keep database), "keep" (keep database)

		Returns
		-------
		object

		"""


	def run(self, script_paths: list) -> list:

		"""

		Runs the provided python scripts on the workers that have been launched at the construction of ParallelJobsDispatcher.


		Parameters
		----------
		script_paths : list
			List of python script paths to run on workers.

		Returns
		-------
		list
			Returns a list with info and results for every job executed.

		"""

def PushScriptProgressToPeer(progress_percentage: int, summary: str, details: str, current_step: int, total_steps: int) -> None:

	"""

	Sends a Script Progress update to the remote peer that requested a remote script execution

	Parameters
	----------
	progress_percentage : int
		The overall progress percentage. Expected value in range [0,100]

	summary : str
		Brief summary of Script Progress update

	details : str, optional
		More details regarding the current execution

	current_step : int, optional
		Indicates the current execution stage of the running script

	total_steps : int, optional
		Indicates the total number of execution stages of the running script

	Returns
	-------
	None

	"""

def GetProcessSystemMetrics(measurement_type: str, measurement_units: str="MB", memory_heap_measurement: bool=False) -> dict:

	"""

	Returns metrics (memory) about the process and system.

	Parameters
	----------
	measurement_type : str
		Specify the measurement type.
		Supported values: "memory"

	measurement_units : str, optional
		Specify the measurement units for memory measurements.
		Supported values: "bytes", "KB", "MB", "GB".

	memory_heap_measurement : bool, optional
		Set to True in order to enable measurement of the heap memory usage. Might add delay when called too frequently.

	Returns
	-------
	dict
		Returns a dict with the required measurements. On failure an empty dict is returned.

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from ansa import utils
		
		
		def main():
		    dict_metrics = utils.GetProcessSystemMetrics("memory")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "KB")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "bytes", True)
		    for item in dict_metrics.items():
		        print(item)
		
		
		if __name__ == "__main__":
		    main()


	"""

