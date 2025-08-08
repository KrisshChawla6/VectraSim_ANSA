from __future__ import annotations
from typing import *

def GetDiskSpaceStatus() -> object:

	"""

	This function queries the disk status for the home / temporary directories and
	classifies the available disk space according to the thresholds configured for
	'Disk Monitoring'.
	
	The classificiation result can be one of the strings below:

	- UNKNOWN: Classification failed, e.g. because the available disk space could
	           not be queried
	- OK: Available disk space is above any of the configured thresholds
	- WARNING: The available disk space is below the WARNING threshold, but above
	           the CRITICAL threshold
	- CRITICAL: The available disk space is below the CRITICAL threshold
	- FULL: The disk is effectively full: less than 1 MB is available

	Returns
	-------
	object
		This function returns objects of class DiskSpaceStatus, which contain the
		following members
		- homedir_free_space: Free space (measured in bytes) for the user's home
		                      directory 
		- homedir_status: Evaluated status according to the configured 'Home Directory'
		                  threshold for Disk Monitoring (see description for possible 
		                  values)
		- tempdir_free_space: Free space (measured in bytes) for the temporary directory
		                      used by the application
		- tempdir_status: Evaluated status according to the configured 'Caching 
		                  Directory' threshold for Disk Monitoring (see description for
		                  possible values)

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		report = sdm_base.GetDiskSpaceStatus()
		print("Home free space:", report.homedir_free_space)
		print("Home status:", report.homedir_status)
		print("Temp free space:", report.tempdir_free_space)
		print("Temp status:", report.tempdir_status)
		
		if report.homedir_status == "OK" and report.tempdir_status == "OK":
		    print("Disk Status: OK")
		else:
		    print("Disk Status: Non OK")


	"""

def RefreshCurrentTab():

	"""

	This function refreshes current tab in KOMVOS application.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.RefreshCurrentTab()


	"""

def StartIdentifyInViewer() -> bool:

	"""

	This function sends a session command in META viewer in order to start the identify process for items loaded from running application. META viewer should be already launched.   

	Returns
	-------
	bool
		Returns True if command has been sent successfully, 
		        None if viewer has not been launched, 
		        False otherwise.

	See Also
	--------
	sdm_base.StopIdentifyInViewer

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.StartIdentifyInViewer()


	"""

def StopIdentifyInViewer() -> bool:

	"""

	This function sends a session command in META viewer in order to stop the identify process for items loaded from running application.   

	Returns
	-------
	bool
		Returns True if viewer is launched and command was sent.

	See Also
	--------
	sdm_base.StartIdentifyInViewer

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.StopIdentifyInViewer()


	"""

def ShowItemsInViewer(attributes_per_server_ids: object, show_only: bool) -> bool:

	"""

	This function shows in META viewer the items given as input argument from running application.

	Parameters
	----------
	attributes_per_server_ids : object, optional
		This argument is a list of dictionaries of part attributes per server id.

	show_only : bool, optional
		If this argument is set to True, 'Show only' will be applied in viewer. 
		If this argument is omitted, 'Show' will be applied (default).

	Returns
	-------
	bool
		Returns True in case of success.

	See Also
	--------
	sdm_base.HideItemsInViewer

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def showOnlyAllPartsInViewer():
		    sdm_base.SelectAllInCurrentTab()
		    current_tab_info = sdm_base.GetInfoOnSelectedItemsFromCurrentTab(any_type=True)
		    sdm_base.ClearSelectionInCurrentTab()
		    parts_list = list()
		    try:
		        attrs_per_server_ids_list = current_tab_info.get("attributes_per_server_ids")
		        if attrs_per_server_ids_list:
		            for attrs_per_server_id_dict in attrs_per_server_ids_list:
		                for server_id, names_values_dict in attrs_per_server_id_dict.items():
		                    type = names_values_dict.get(
		                        "_DM_Attr_Hidden_Developer_dm_entity_type_"
		                    )
		                    if type == "parts":
		                        parts_list.append(attrs_per_server_id_dict)
		    except:
		        pass
		    sdm_base.ClearViewer()
		    sdm_base.ShowItemsInViewer(attributes_per_server_ids=parts_list, show_only=True)
		    pass


	"""

def HideItemsInViewer(attributes_per_server_ids: object) -> bool:

	"""

	 

	Parameters
	----------
	attributes_per_server_ids : object, optional
		This argument is a list of dictionaries of part attributes per server id.

	Returns
	-------
	bool
		Returns True in case of success,
		        False otherwise.

	See Also
	--------
	sdm_base.ShowItemsInViewer

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def hideFunction(attrs_per_server_ids_list):
		    sdm_base.SetViewerHighlightStatus(False)
		    sdm_base.HideItemsInViewer(attributes_per_server_ids=attrs_per_server_ids_list)
		    sdm_base.SetViewerHighlightStatus(True)


	"""

def ClearViewer(clear_all: bool):

	"""

	This function clears the META viewer area.

	Parameters
	----------
	clear_all : bool, optional
		If this argument is set to True, all pages that might be opened will be cleared.
		If this argument is omitted, only 3D model page will be cleared (default).

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def showOnlyPartsInViewer(parts_list):
		    sdm_base.ClearViewer()
		    sdm_base.ShowItemsInViewer(attributes_per_server_ids=parts_list, show_only=True)
		
		
		def clearAllInViewer():
		    sdm_base.ClearViewer(clear_all=True)


	"""

def EnableDrawingStyleInViewer(style: str):

	"""

	This function enables in embedded META viewer the drawing style given as argument.

	Parameters
	----------
	style : str
		This argument is given in order to specify the drawing style that should be enabled in viewer.
		Keywords that can be used (case insensitive) and the corresponding drawing style are:
		Keywords (case insensitive) --> Drawing Style
		----------------------------------------------
		Pid                         --> PID
		Mid                         --> MID
		Ent/Entities                --> ENT
		Submodel/Subsystem/Component--> Submodel
		Simulation Model/BFZG       --> Simulation Model
		Thickness                   --> Thickness
		Unique Thickness            --> Unique Thickness
		Contact Thickness           --> Contact Thickness
		Pcomp Zones                 --> Pcomp Zones
		Status                      --> Status
		Diff                        --> Diff
		
		For custom drawing styles, their name should be given as argument.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.EnableDrawingStyleInViewer("Subsystem")


	"""

def SetViewerHighlightStatus(status: bool):

	"""

	This function is used to enable/disable highlight status and identify synchronization between embedded META viewer and the list in running application.

	Parameters
	----------
	status : bool
		This argument is used to enable/disable highlight status and 
		identify synchronization. Use: 
		    True to enable highlight status or reset,
		    False to disable highlight status.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.SetViewerHighlightStatus(False)


	"""

def SaveJtAsMetadbInViewer(names_values: object) -> bool:

	"""

	This function saves jt files corresponding to the item given as input (from its children items) as one compressed metadb file using META viewer. Meta-data are also saved in metadb file in order to maintain the identify process.

	Parameters
	----------
	names_values : object
		This argument is a dictionary with the attribute names 
		and values that describe the given as input item.

	Returns
	-------
	bool
		Return True for success.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def save_jt_as_metadb_in_viewer(list_of_maps):
		    if len(list_of_maps) > 1:
		        sdm_base.PostMessageInInfoArea(
		            "Save jt as metadb Error: please select just one item."
		        )
		        return
		    names_values = list_of_maps[0]
		    sdm_base.SaveJtAsMetadbInViewer(names_values=names_values)
		    return


	"""

def SelectAllInCurrentTab():

	"""

	This function selects all the items in list view of current tab.

	See Also
	--------
	sdm_base.ClearSelectionInCurrentTab

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.SelectAllInCurrentTab()
		current_tab_info = sdm_base.GetInfoOnSelectedItemsFromCurrentTab(any_type=True)
		sdm_base.ClearSelectionInCurrentTab()


	"""

def ClearSelectionInCurrentTab():

	"""

	This function deselects all items in list view of current tab.

	See Also
	--------
	sdm_base.SelectAllInCurrentTab

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.SelectAllInCurrentTab()
		current_tab_info = sdm_base.GetInfoOnSelectedItemsFromCurrentTab()
		sdm_base.ClearSelectionInCurrentTab()


	"""

def SetColorToItemsInViewer(red: int, green: int, blue: int, alpha: int, model_ids: object, attributes_per_server_ids: object) -> bool:

	"""

	This function sets a specific color in embedded META viewer for the given items.
	Input could be the instance ids of items loaded in viewer (if known) or server 
	ids and attributes describing those items loaded in viewer. 

	Parameters
	----------
	red : int
		Set value for red channel.

	green : int
		Set value for green channel.

	blue : int
		Set value for blue channel.

	alpha : int
		Set value for alpha channel (transparency).

	model_ids : object, optional
		Instance ids describing the items in viewer.

	attributes_per_server_ids : object, optional
		List of maps containing server id (as key) and attributes of each given item.

	Returns
	-------
	bool
		Returns True for success.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		model_ids = [2, 3]
		sdm_base.SetColorToItemsInViewer(100, 100, 0, 255, model_ids=model_ids)


	"""

def GetInfoOnSelectedItemsFromViewer() -> object:

	"""

	This functions is used to get the attribute names and values of the items that are selected in list of running application and have been sent in embedded META viewer.

	Returns
	-------
	object
		Returns a list of maps with server ids as keys and attribute names-values as data.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		attrs_per_server_ids_list = sdm_base.GetInfoOnSelectedItemsFromCurrentTab()
		print(attrs_per_server_ids_list)


	"""

def GetInfoOnSelectedItemsFromCurrentTab(any_type: bool) -> object:

	"""

	This function will return a dictionary that will contain two key/value members:
	'attributes_per_server_ids' is a list that contains all information on the selected items per server id.
	                            Each item in the list is a dictionary with the server id as the key and another 
	                            dictionary as the value. The latter is the names/values map for the specific server id.
	                            In case of instances, more than one entry will exist in the list for each server id. 
	                            They may have different attributes.
	                            
	'child_parent_attributes_per_server_ids' is a list that contains sub_lists.
	                                         Each sub_list has the attributes_per_server_id for the child as the first item 
	                                         and the attributes_per_server_id for the parent as the second.
	                                         It is essentially a child-parent relationship, only each instance is contained 
	                                         more than once.

	Parameters
	----------
	any_type : bool, optional
		True if you wish to collect information for any type of items.

	Returns
	-------
	object
		Returns a dictionary.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def getInfo():
		    sdm_base.SelectAllInCurrentTab()
		    current_tab_info = sdm_base.GetInfoOnSelectedItemsFromCurrentTab()
		    sdm_base.ClearSelectionInCurrentTab()
		    try:
		        attrs_per_server_ids_list = current_tab_info.get("attributes_per_server_ids")
		        child_parent_attributes = current_tab_info.get(
		            "child_parent_attributes_per_server_ids"
		        )
		        if attrs_per_server_ids_list:
		            for attrs_per_server_id_dict in attrs_per_server_ids_list:
		                for server_id, names_values_dict in attrs_per_server_id_dict.items():
		                    if names_values_dict.get("Is Group") == "YES":
		                        group_attributes.append(attrs_per_server_id_dict)
		                    else:
		                        part_attributes.append(attrs_per_server_id_dict)
		    except:
		        pass


	"""

def BuildSubsystemPopulateWithChildrenAndSave(subsystem_properties: object, attributes_per_server_ids: object, child_parent_attributes_per_server_ids: object, child_type: str) -> bool:

	"""

	This function will save a subsystem hierarchy to the current DM.

	Parameters
	----------
	subsystem_properties : object
		This is the first argument, where a dictionary with the 
		subsystem's properties must be entered.

	attributes_per_server_ids : object
		Second argument, where a list with names/values per server 
		ids must be entered. The input here can be used directly 
		from the function GetInfoOnSelectedItemsFromCurrentTab.

	child_parent_attributes_per_server_ids : object
		This is the third argument, where the hierarchy is described 
		in a list with lists! Again, the input can be used directly 
		from the function GetInfoOnSelectedItemsFromCurrentTab.

	child_type : str, optional
		This is a variable argument that defines the kind of children 
		existing in the hierarchy,e.g. "parts" or "includes". By 
		default "parts" are created.

	Returns
	-------
	bool
		Returns True if everything went OK, 
		        False if the command failed.

	See Also
	--------
	sdm_base.GetInfoOnSelectedItemsFromCurrentTab, sdm_base.GetNewSubmodelAttributesWindow

	Examples
	--------
	::

		# If the viewer has been opened and we picked some items:
		import sdm
		from sdm import sdm_base
		
		ret = sdm_base.GetInfoOnSelectedItemsFromCurrentTab()
		if ret != None:
		    attributes_per_server_ids = ret["attributes_per_server_ids"]
		    child_parent_attributes_per_server_ids = ret[
		        "child_parent_attributes_per_server_ids"
		    ]
		    properties = sdm_base.GetNewSubmodelAttributesWindow(window_title="Save Subsystem")
		    if properties == None:
		        return
		    ret_val = sdm_base.BuildSubsystemPopulateWithChildrenAndSave(
		        properties, attributes_per_server_ids, child_parent_attributes_per_server_ids
		    )


	"""

def BuildSimulationModelWithChildrenAndSave(names_values: object, attributes_per_server_ids: object, child_parent_attributes_per_server_ids: object) -> bool:

	"""

	This function will save a simulation model hierarchy to the current DM.

	Parameters
	----------
	names_values : object
		This is the first argument, where a dictionary with the simulation 
		model's properties must be entered.

	attributes_per_server_ids : object
		This is the second argument, where a list with names/values per server 
		ids must be entered. The input here can be used directly from the 
		function GetInfoOnSelectedItemsFromCurrentTab.

	child_parent_attributes_per_server_ids : object
		This is the third argument, where the hierarchy is described in a list 
		with lists! Again, the input can be used directly from the function 
		GetInfoOnSelectedItemsFromCurrentTab.

	Returns
	-------
	bool
		Returns True if everything went OK, 
		        False if the command failed.

	See Also
	--------
	sdm_base.GetInfoOnSelectedItemsFromCurrentTab, sdm_base.BuildSubsystemPopulateWithChildrenAndSave

	Examples
	--------
	::

		# If the viewer has been opened and we picked some items:
		import sdm
		from sdm import sdm_base
		
		ret = sdm_base.GetInfoOnSelectedItemsFromCurrentTab()
		if ret != None:
		    attributes_per_server_ids = ret["attributes_per_server_ids"]
		    child_parent_attributes_per_server_ids = ret[
		        "child_parent_attributes_per_server_ids"
		    ]
		    properties = sdm_base.GetNewSimulationModelAttributesWindow(
		        window_title="Save Simulation Model"
		    )
		    if properties == None:
		        return
		    ret_val = sdm_base.BuildSimulationModelWithChildrenAndSave(
		        properties, attributes_per_server_ids, child_parent_attributes_per_server_ids
		    )


	"""

def OpenProgressReport(filename: str) -> int:

	"""

	This function opens a progress report file in KOMVOS Progress Report viewer.

	Parameters
	----------
	filename : str
		This argument is the name of the file we want to open.

	Returns
	-------
	int
		Returns 1 if file opens,
		        0 if file is already opened.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.OpenProgressReport("/home/user/progress_report.xlsx")


	"""

def OpenNewTab(name: str, index: int, make_current: bool, icon: str, frame: object) -> object:

	"""

	This functions opens a new tab in KOMVOS application.

	Parameters
	----------
	name : str, optional
		This argument is the title of the tab that will be created.

	index : int, optional
		This argument specifies the index of the tab. If index is out of range, 
		the tab is simply appended. Otherwise it is inserted at the specified position.

	make_current : bool, optional
		This argument specifies if this tab should be current or not.
		By default, tab is made current.

	icon : str, optional
		This argument is an image name, if user wishes to use an icon for the new tab.

	frame : object, optional
		This argument is a frame, if user wishes to use an existing one.

	Returns
	-------
	object
		Returns the created tab as an object, if everything went ok, None otherwise.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.OpenNewTab(name="NEW", index=-1, make_current=False)


	"""

def PostMessageInInfoArea(message: str) -> bool:

	"""

	This function prints a message in application's Info area.

	Parameters
	----------
	message : str
		This is the message that will be printed in Info area.

	Returns
	-------
	bool
		Returns True for success.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		sdm_base.PostMessageInInfoArea("This is my message for Info area.")


	"""

def CreateNewSubmodelWindow(assign_values: object, paint_names: object) -> int:

	"""

	This function pops up an 'Insert new Subsystem' window in order to create a new subsystem.
	Furthermore, after 'OK' button pressed, function opens a new tab with the new hierarchy.

	Parameters
	----------
	assign_values : object, optional
		This argument is a dictionary containing attribute names-values, 
		in case user wants to pre-assign them.

	paint_names : object, optional
		This argument is a list of attribute names that user wishes to 
		paint with different color (red).

	Returns
	-------
	int
		Returns 0

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		name_values = {"Module Id": "12", "Study Version": "1"}
		paint_attrs = ["Variant", "Release"]
		sdm_base.CreateNewSubmodelWindow(assign_values=name_values, paint_names=paint_attrs)


	"""

def CreateNewSimulationModelWindow(assign_values: object, paint_names: object, create_new_entry: bool) -> object:

	"""

	This function pops up an 'Insert new Simulation Model' window in order to create a new simulation model. 
	Furthermore, after 'OK' button pressed, function opens a new tab with the new hierarchy.

	Parameters
	----------
	assign_values : object, optional
		This argument is a dictionary with attribute name-values, 
		in case user wants to pre-assign them.

	paint_names : object, optional
		This argument is a list of attribute names that user wishes 
		to paint with different color (red).

	create_new_entry : bool, optional
		This argument dictates whether an actual Simulation Model will be created after 'OK' has been pressed.

	Returns
	-------
	object
		In case of success, returns a dictionary with the attribute name-values of the created simulation model.
		Otherwise, it returns None.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		name_values = {"Name": "MY_NEW_SIMULATION_MODEL"}
		paint_attrs = ["Release"]
		ret = sdm_base.CreateNewSimulationModelWindow(
		    assign_values=name_values, paint_names=paint_attrs, create_new_entry=False
		)
		print(ret)


	"""

def ProgressBarSetAttributes(label: str, current_step: int, visible: bool, total_steps: int) -> bool:

	"""

	This function creates a progress bar for running application.

	Parameters
	----------
	label : str, optional
		This argument sets the label of the progress bar.

	current_step : int, optional
		This argument sets current step for the progress bar.

	visible : bool, optional
		This arguments makes progress bar visible (True) or not (False).

	total_steps : int, optional
		This argument sets total steps of the progress bar.

	Returns
	-------
	bool
		Returns True for success.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		ret = sdm_base.ProgressBarSetAttributes(
		    label="Progress", current_step=5, visible=True, total_steps=100
		)
		print(ret)


	"""

def GetNewSubmodelAttributesWindow(window_title: str, names_values: object) -> object:

	"""

	This function pops up a window with submodel's attributes in order to create and 
	save in DM a new one.

	Parameters
	----------
	window_title : str, optional
		This argument sets the title of the window.

	names_values : object, optional
		This argument is a dictionary with attribute name-values, 
		in case user wishes to pre-assign them.

	Returns
	-------
	object
		Returns a dictionary with the attribute name-values of the new submodel in case of success,
		        None or NULL otherwise.

	See Also
	--------
	sdm_base.BuildSubsystemPopulateWithChildrenAndSave

	Examples
	--------
	::

		import time
		import sdm
		from sdm import sdm_base
		
		start_tot_time = time.time()
		module_id = "24"
		properties = sdm_base.GetNewSubmodelAttributesWindow(
		    window_title="Save Module in DM", names_values={"Module Id": module_id}
		)
		print(properties)
		end_tot_time = time.time()
		print(" time spent: ", end_tot_time - start_tot_time)


	"""

def GetNewSimulationModelAttributesWindow(window_title: str, names_values: object) -> object:

	"""

	This function pops up a window with simulation model's attributes in order to create and 
	save in DM a new one.

	Parameters
	----------
	window_title : str, optional
		This argument sets a title for the window,

	names_values : object, optional
		This argument is a dictionary with attribute name-values, 
		in case user wishes to pre-assign them.

	Returns
	-------
	object
		Returns a dictionary with the attribute name-values of the new simulation model in case of success,
		        None or NULL otherwise.

	See Also
	--------
	sdm_base.BuildSimulationModelWithChildrenAndSave

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		values = {"Project": "TEST", "Name": "NEW_SIM_MODEL"}
		properties = sdm_base.GetNewSimulationModelAttributesWindow(
		    window_title="Save Simulation Model in DM", names_values=values
		)
		if properties:
		    print(" OK ")
		    print(properties)


	"""

def FullyBuildItemsInCurrentTab(server_ids: object, object_ids: object, attributes: object):

	"""

	This function builds given items in current tab to the furthest. At least one of input arguments must be filled.
	Input arguments can be added as a list or as a single value. 
	For example:

	- server_ids = [server_id1, server_id2...] or server_id (a single one)
	- object_ids = [row_id1, row_id2....] or row_id (a single one)
	- attributes = [attr_map_of_item1, attr_map_of_item2....] or attr_map_of_item (a single one)
	Function returns the list of attributes of the items it built, since after the building they may very well be different.

	Parameters
	----------
	server_ids : object, optional
		This argument can be a list of server ids (for multiple items) or a single server id 
		(string).

	object_ids : object, optional
		This argument can be a list of row ids (for multiple items) or a single row id (integer).

	attributes : object, optional
		This argument can be a list of dictionaries with attribute name-values (for more than one 
		items) or a single dictionary with attribute name-values (for a single one).

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		server_id = "97"
		ret1 = sdm_base.FullyBuildItemsInCurrentTab(server_ids=server_id)
		print(ret1)
		
		row_ids = [41, 31]
		ret2 = sdm_base.FullyBuildItemsInCurrentTab(object_ids=row_ids)
		print(ret2)


	"""

def ApplicationInformation() -> str:

	"""

	This function reports build and runtime information of the running KOMVOS process.
	This includes the KOMVOS version, its build date, and information about the architecture 
	of the application and the underling operating system. The function takes no arguments. 
	The report is similar to:
	+------------------------------------------------------------
	                         K O M V O S                       
	 version:  21.1.0, compiled: Oct  5 2020, 15:12:45
	 built:    64-bit, sn: 27a41e6c8c0b
	 platform: Linux x86_64 4.18.5-1.el7.elrepo.x86_64 little-endian
	 company:  BETA CAE Systems S.A.(licsrv)
	+------------------------------------------------------------
	
	Information also available through KOMVOS > Help > About KOMVOS.

	Returns
	-------
	str
		Returns a string containing the build/runtime information.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		
		
		def main():
		    s = sdm_base.ApplicationInformation()
		    print(s)


	"""

def GenerateSimulationModelBasedOnTemplates(sim_model_attributes: object, simulation_model_template_filename: str, model_structure: str, submodel_templates: object, tree_settings: object) -> str:

	"""

	This function will save a new Simulation Model by doing the following:
	* Input a PLMXML file
	* Save a Simulation Model by applying a Template
	* Create Subsystems by applying respective Templates on the PLMXML structure

	Parameters
	----------
	sim_model_attributes : object
		A dictionary with the name/values pairs for 
		the Properties and Attributes of the Simulation Model.

	simulation_model_template_filename : str
		The Template that will be applied to the new Simulation Model.
		An absolute file path or
		a filename relative to the Templates/SimulationModels folder can be used.

	model_structure : str
		The PLMXML file that will be read.

	submodel_templates : object
		A dictionary with pairs of the following type:
		Subsystem Module Id : Subsystem Template Name
		Each Template will be applied to the Subsystem with the respective Module Id.

	tree_settings : object
		An object of type "base.InputProductTreeSettings()" for defining the settings 
		when reading the file.

	Returns
	-------
	str
		Returns the newly saved Simulation Model's server id.
		None is returned if something goes wrong and if the Model isn't saved successfully.

	See Also
	--------
	sdm_base.BuildSimulationModelWithChildrenAndSave, sdm_base.GetNewSimulationModelAttributesWindow

	Examples
	--------
	::

		import os
		from random import seed
		from random import randint
		import sdm
		from sdm import sdm_base
		from sdm import base
		
		
		value = randint(0, 100000)
		bfzg_names_values = {
		    "PRISMA Number": str(value),
		    "Product Line": "LR",
		    "Derivat": "RR11",
		    "Project Phase": "BENCHMARK",
		}
		bfzg_names_values["Variant"] = "KOM-940A"
		bfzg_names_values["Drive"] = "-"
		bfzg_names_values["Steering"] = "-"
		bfzg_names_values["Country"] = "-"
		bfzg_names_values["Transmission"] = "-"
		bfzg_names_values["Engine"] = "-"
		bfzg_names_values["Version"] = "A-_01_A"
		bfzg_names_values["Study Version"] = "0"
		bfzg_names_values["File Type"] = "ANSA"
		bfzg_names_values["Name"] = "KOM-940"
		bfzg_template = "//jirafiles/jiradata/attachments/KOM/00001-10000/940/EK30_SUV.xml"
		model_structure = "//jirafiles/jiradata/attachments/KOM/00001-10000/940/_jira_/P1GHKY1_A_4_A_ST_SNAPPK.plmxml"
		submodel_dict = {
		    "Karosseriegerippe": "BIW_standard.xml",
		    "Normaldach": "Frontklappe_standard.xml",
		}
		settings = base.InputProductTreeSettings()
		settings.use_plmxml_parser = "Vismockup"
		settings.read_plmxml_attributes = "All"
		settings.should_open_window = False  # PTEditor
		settings.part_name_convert = False
		settings.post_actions_script_path = "$DCM_GUI_HOME/cad4cae_plmxml.py"
		settings.post_actions_script_function = "RunPostTreatmentAttributesForConversionService"
		settings.compress_parts = True
		settings.keep_different_versions_per_part_number = True
		ret = sdm_base.GenerateSimulationModelBasedOnTemplates(
		    sim_model_attributes=bfzg_names_values,
		    simulation_model_template_filename=bfzg_template,
		    model_structure=model_structure,
		    submodel_templates=submodel_dict,
		    tree_settings=settings,
		)
		print(ret)
		dm.OpenDMObjectsInNewTab(
		    server_ids=[ret], type="ANSA_SIMULATION_MODEL", view="Default", expand_all=True
		)


	"""

def SDMProgressBarSetVisible():

	"""
	.. deprecated:: 21.1.0
		Use :py:func:`ProgressBarSetAttributes` instead.


	SDMProgressBarSetVisible

	See Also
	--------
	ProgressBarSetAttributes

	Examples
	--------
	::

		SDMProgressBarSetVisible


	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use :py:func: ProgressBarSetAttributes instead.", DeprecationWarning)

def SDMProgressBarSetTotalSteps():

	"""
	.. deprecated:: 21.1.0
		Use :py:func:`ProgressBarSetAttributes` instead.


	See Also
	--------
	ProgressBarSetAttributes

	Examples
	--------
	::

		SDMProgressBarSetTotalSteps


	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use :py:func: ProgressBarSetAttributes instead.", DeprecationWarning)

def SDMProgressBarSetStep():

	"""
	.. deprecated:: 21.1.0
		Use :py:func:`ProgressBarSetAttributes` instead.


	SDMProgressBarSetStep

	See Also
	--------
	ProgressBarSetAttributes

	Examples
	--------
	::

		SDMProgressBarSetStep


	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use :py:func: ProgressBarSetAttributes instead.", DeprecationWarning)

def SDMProgressBarSetLabel():

	"""
	.. deprecated:: 21.1.0
		Use :py:func:`ProgressBarSetAttributes` instead.


	SDMProgressBarSetLabel

	See Also
	--------
	sdm_base.ProgressBarSetAttributes

	Examples
	--------
	::

		SDMProgressBarSetLabel


	"""

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use :py:func: ProgressBarSetAttributes instead.", DeprecationWarning)

def ShowPlotInViewer(plot: object, window_name: str, page_name: str):

	"""

	This function starts META viewer for running application (if not already started), 
	and shows there the created plot given as input.

	Parameters
	----------
	plot : object
		This argument is the created plot we want to show in viewer.

	window_name : str, optional
		This argument is the window name in viewer.

	page_name : str, optional
		This argument is the name of the page added in viewer.

	See Also
	--------
	CreatePlot, SetPlotProperties, DeletePlot

	Examples
	--------
	::

		# KOMVOS
		import sdm
		from sdm import sdm_base, utils
		
		plot = utils.CreatePlot()
		utils.SetPlotProperties(plot, title="My plot", legend_position="TopRight")
		sdm_base.ShowPlotInViewer(plot, window_name="Plot", page_name="Plot's page")
		utils.DeletePlot(plot)


	"""

def InsertFrameInTabWidget(frame: object, position: str="side", about_to_close_tab_function: Callable=None, about_to_close_tab_function_data: Any=None) -> Any:

	"""

	Inserts a frame as a new tab to the right-side or the bottom tab widgets.
	It's automatically set as current.

	Parameters
	----------
	frame : object
		The frame to insert as a tab to the respective tab widget.

	position : str, optional
		The respective tab widget, valid values are: "side" and "bottom".

	about_to_close_tab_function : Callable, optional
		The function that will be called before the tab closes. See BC_TABWIDGET_ABOUT_TO_CLOSE_TAB_FUNCTION for details.
		integer BC_TABWIDGET_ABOUT_TO_CLOSE_TAB_FUNCTION(tw, tab, data)
		The function to be called when tab of B_TabWidget tw is about to removed.
		WARNING: If you need to delete a GUI object (button, list view item etc) inside your call back function, do NOT delete it directly but with the use of a timer (BCTimerSingleShot).
		
		Arguments
		
		tw      object    the BCTabWidget.
		tab     object    the tab to be removed.
		data    anything  anything that may be required in function.
		
		Return 1 in case you want to canel closing the tab; 0 otherwise.

	about_to_close_tab_function_data : Any, optional
		any user data required by function about_to_close_tab_function.

	Returns
	-------
	Any
		returns None.

	Examples
	--------
	::

		import sdm
		from sdm import sdm_base
		from sdm import guitk
		
		
		def destroyWindowTimed(temp_window):
		    guitk.BCDestroyLater(
		        temp_window
		    )  # Prefer DestroyLater than Destroy because it's safer to use.
		    return 0
		
		
		temp_window = guitk.BCWindowCreateNoHandler(
		    "Inspect DVs and Responses Window", guitk.constants.BCOnExitDestroy
		)
		frame = guitk.BCFrameCreate(temp_window)
		guitk.BCSetName(frame, "Inspect DVs and Responses")
		BCBoxLayout = guitk.BCBoxLayoutCreate(frame, guitk.constants.BCVertical)
		sdm.sdm_base.InsertFrameInTabWidget(frame, "side")
		guitk.BCTimerSingleShot(0, destroyWindowTimed, temp_window)
		guitk.BCShow(temp_window)


	"""

