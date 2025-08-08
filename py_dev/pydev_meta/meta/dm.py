from __future__ import annotations
from typing import *
from datetime import datetime

def AddAttachmentToFolder(entity: object, server_id: str, folder_name: str, filename: str, attribute_name: str, entity_type: str, link: bool) -> int:

	"""

	This function can be used to:

	- add a file under a folder in the Library Items,
	- attach a file/folder under a DM Object's attribute of type Attached File/Directory
	  respectively. If this attribute does not exist, it is created as Additional Attribute.
	A DM root should have been specified.

	Parameters
	----------
	entity : object, optional
		the ANSA entity to be found in the connected
		DM root. The file/folder will be attached under
		an attribute of this object (if found in DM).

	server_id : str, optional
		the server id of the object contained to the
		connected DM root. The file/folder will be
		attached under an attribute of this object.

	folder_name : str, optional
		the name of the folder in the Library Items,
		where the specified file will be attached.
		For DM Objects in file-based DM, a sub-folder
		with this name will be created, and the file
		will be placed there.

	filename : str
		the full path of the file/folder to be attached.

	attribute_name : str, optional
		the name of the DM Object's attribute where the
		specified file/folder will be attached.

	entity_type : str, optional
		the type of the DM object.

	link : bool, optional
		enables the ability to link a folder and not copy
		its contents under a DM Object's attribute. By
		default, the contents are copied (False).

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	DeleteAttachment, DownloadAttachment

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import dm
		
		
		def main():
		    # 1st Use Case: Create a folder under the Library Items and attach a file to that
		    create_folder = dm.CreateNewSubFolder(folder_name="batch_mesh_sessions")
		    file_path = "/full/path/of/file/or/folder/to/attach/"
		    attach_file = dm.AddAttachmentToFolder(
		        folder_name="batch_mesh_sessions", filename=file_path
		    )
		
		    # Alternatively, attach a file under a sub-folder
		    attach_file = dm.AddAttachmentToFolder(
		        folder_name="batch_mesh_sessions/crash", filename=file_path
		    )
		    attach_file = dm.AddAttachmentToFolder(
		        folder_name="LIBRARY_ITEMS/batch_mesh_sessions", filename=file_path
		    )
		
		    # 2nd Use Case: File-based DM - Create a sub-folder under an attribute of DM Object
		    # and place the file there.
		    file_path = "/full/path/of/file/or/folder/to/attach/"
		    part = base.GetPartFromModuleId("100")
		    create_subfolder = base.CreateNewSubFolder(
		        entity=part, folder_name="Additional_Results", attribute_name="Results"
		    )
		    attach_file = dm.AddAttachmentToFolder(
		        entity=part,
		        folder_name="Additional_Results",
		        filename=file_path,
		        attribute_name="Results",
		    )
		
		    # Alternatively, the file could be placed directly under the DM Object's attribute
		    attach_file = dm.AddAttachmentToFolder(
		        entity=part, filename=file_path, attribute_name="Results"
		    )
		    attach_file = dm.AddAttachmentToFolder(
		        server_id="200", filename=file_path, attribute_name="Results"
		    )
		
		    # 3rd Use Case: SPDRM - Attach a file/folder under an attribute of type Attached
		    # File/Directory respectively. If this attribute does not exist (was not specified
		    # in the dm_structure.xml), it is created as Additional Attribute.
		    folder_path = "/full/path/of/file/or/folder/to/attach/"
		    attach_file = dm.AddAttachmentToFolder(
		        server_id="200", filename=folder_path, attribute_name="Results"
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteAttachment(entity: object, server_id: str, folder_name: str, filename: str, entity_type: str) -> int:

	"""

	When connected to a DM, this function allows for an existing attachment to a DM object to be deleted. 
	If no DM Object is specified, a library item can be deleted.

	Parameters
	----------
	entity : object, optional
		When this argument is given, the ANSA entity will be searched in DM and if found, 
		the attachment will be deleted from the corresponding DM Object.

	server_id : str, optional
		The DM Object's server id, whose attachment will be deleted.

	folder_name : str, optional
		A subfolder with this name will be deleted.

	filename : str, optional
		The filename which will be deleted.

	entity_type : str, optional
		If the server_id is given as an argument, one may define the Object's type by 
		using this argument.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	AddAttachmentToFolder, DownloadAttachment

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import dm
		
		
		def deleteAnAttachedFolder():
		    part = base.GetPartFromModuleId("4282")
		    dm.DeleteAttachment(entity=part, folder_name="VBT_Info")
		    dm.DeleteAttachment(entity=part, folder_name="DA/Translated_files")
		    dm.DeleteAttachment(entity=part)
		
		    # in case we know the Object's server id:
		    file_ret = dm.DeleteAttachment(server_id="100", folder_name="Folder1")
		    # or:
		    file_ret = dm.DeleteAttachment(
		        server_id="100", entity_type="parts", folder_name="Folder1"
		    )
		
		    # In order to delete a file under "batch_mesh_sessions" folder:
		    dm.DeleteAttachment(
		        folder_name="batch_mesh_sessions", filename="example_7mm.ansa_qual"
		    )


	"""

def DownloadAttachment(entity: object, server_id: str, folder_name: str, output_folder: str, subfolder_name: str, filename: str, entity_type: str, attribute_name: str, action: str) -> int:

	"""

	Downloads the attachments of an object contained to the defined DM root. A DM root
	should have been specified.

	Parameters
	----------
	entity : object, optional
		the ANSA entity to be found in the connected
		DM root. The attachments of this object (if
		found in DM) will be downloaded.

	server_id : str, optional
		the server id of the object contained to the
		connected DM root. The attachments of this
		object will be downloaded.

	folder_name : str, optional
		the name of the folder which contains the
		attachments.

	output_folder : str
		the full path of the folder where the attachments
		will be downloaded.

	subfolder_name : str, optional
		the name of the subfolder to be downloaded.

	filename : str, optional
		the name of the file to be downloaded.

	entity_type : str, optional
		the type of the DM object.

	attribute_name : str, optional
		the name of attribute which contains the
		attachments.

	action : str, optional
		The exported file from the server will be copied to the target directory by default.
		It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
		Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items and Library Files.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	DeleteAttachment, AddAttachmentToFolder, DMObject.download_attachment

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import dm
		
		
		def main():
		    part = base.GetPartFromModuleId("100")
		    dm.DownloadAttachment(
		        entity=part,
		        output_folder="/full/path/of/output/folder/",
		        attribute_name="Image_JT",
		    )
		
		    dm.DownloadAttachment(
		        server_id="200",
		        output_folder="/full/path/of/output/folder/",
		        attribute_name="Image_PNG",
		    )
		
		    # Download attachements from SPDRM-based DM
		    dm.DownloadAttachment(
		        server_id="300",
		        subfolder_name="/relative/path/to/the/top/level/folder/",
		        output_folder="/full/path/of/output/folder/",
		        attribute_name="Results",
		    )
		    dm.DownloadAttachment(
		        server_id="400",
		        filename="/relative/path/to/the/top/level/folder/filename.ext",
		        output_folder="/full/path/of/output/folder/",
		        attribute_name="Results",
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateAttachedFolder(entity: object, server_id: str, attribute_name: str, entity_type: str) -> int:

	"""

	Creates an empty attached folder under an existing object in DM. New files/folders
	can be added as attachments in that folder afterwards. A DM root should have been
	specified.

	Parameters
	----------
	entity : object, optional
		the ANSA entity to be found in the connected
		DM root. The new folder will be attached under
		this object (if found in DM).

	server_id : str, optional
		the server id of the object contained to the
		connected DM root. The new folder will be
		attached under this object.

	attribute_name : str, optional
		the name of the folder to be attached.

	entity_type : str, optional
		the type of the DM object.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	CreateNewSubFolder, DeleteAttachment, DownloadAttachment, AddAttachmentToFolder

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import dm
		
		
		def main():
		    part = base.GetPartFromModuleId("100")
		    dm.CreateAttachedFolder(entity=part, attribute_name="Info")
		
		    dm.CreateAttachedFolder(server_id="200", attribute_name="Info")
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateNewSubFolder(entity: object, server_id: str, folder_name: str, attribute_name: str, entity_type: str) -> int:

	"""

	Creates an empty subfolder in an existing attached folder of a DM object. New
	files/folders can be added as attachments in that subfolder afterwards. A DM root
	should have been specified. This function can also be used to create subfolders
	for library items in DM (e.g."batch_mesh_sessions").

	Parameters
	----------
	entity : object, optional
		the ANSA entity to be found in the connected
		DM root. The new subfolder will be attached
		under this object (if found in DM).

	server_id : str, optional
		the server id of the object contained to the
		connected DM root. The new subfolder will
		be attached under this object.

	folder_name : str
		the name of the subfolder to be attached.

	attribute_name : str, optional
		the name of the parent attribute/folder where
		the new subfolder will be created. The default
		value id 'DA'.

	entity_type : str, optional
		the type of the DM object.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	CreateAttachedFolder, DeleteAttachment, DownloadAttachment, AddAttachmentToFolder

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import dm
		
		
		def main():
		    part = base.GetPartFromModuleId("100")
		    dm.CreateNewSubFolder(
		        entity=part, folder_name="New_Subfolder", attribute_name="VIP"
		    )
		
		    dm.CreateNewSubFolder(
		        server_id="200", folder_name="New_Subfolder", attribute_name="VIP"
		    )
		
		    dm.CreateNewSubFolder(folder_name="batch_mesh_sessions")
		
		
		if __name__ == "__main__":
		    main()


	"""

def DownloadLibraryItem(library: str, output_folder: str, filename: str, action: str) -> int:

	"""

	This function is used to download a file from the DM library items, e.g. a "batch_mesh_session".  

	Parameters
	----------
	library : str
		The library item's type.

	output_folder : str, optional
		The folder where the item will be copied.
		Although it's an optional argument, it needs to be defined.

	filename : str, optional
		The library item's name.
		Although it's an optional argument, it needs to be defined.

	action : str, optional
		The exported file from the server will be copied to the target directory by default.
		It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
		Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	GetAvailableLibraryItems

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    results = dm.GetAvailableLibraryItems("batch_mesh_sessions", search_for="*.ansa")
		    for result in results:
		        dm.DownloadLibraryItem(
		            "batch_mesh_sessions",
		            output_folder="C:\\\\Users\\\\demo\\\\Desktop\\\\ttt\\\\",
		            filename=result,
		        )


	"""

def GetAvailableLibraryItems(folder_name: str, search_for: str) -> object:

	"""

	This function can be used to get a list with all the items in a library in DM,
	e.g. all "batch_mesh_sessions" or specific "batch_mesh_sessions" that match a 
	search pattern.

	Parameters
	----------
	folder_name : str
		The library's name.

	search_for : str, optional
		This can be a search pattern that will be used for the query.

	Returns
	-------
	object
		Returns a list with all the library item names.

	See Also
	--------
	dm.DownloadLibraryItem

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    results = dm.GetAvailableLibraryItems("batch_mesh_sessions", search_for="*.ansa")
		    if results:
		        for result in results:
		            print("Found batch_mesh_session: ", result)
		    all_results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
		    if all_results:
		        for result in all_results:
		            print("Found batch_mesh_session: ", result)


	"""

def IsConnectionValid(dm_root: str, reconnect: bool) -> int:

	"""

	The function is used to check if the connection to the url-based DM root is actually valid.
	If no arguments are given, the current DM is checked.
	If a "dm_root" argument pair is given, then that url will be checked.

	Parameters
	----------
	dm_root : str, optional
		When this argument is given, then that url will be checked.

	reconnect : bool, optional
		Set to True, if you automatically wish to try and reconnect if the connection is invalid.

	Returns
	-------
	int
		Returns 1 if the connection is valid, or 0 if it is invalid or no DM root has been defined.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    if dm.IsConnectionValid():
		        print("Connection to current DM is valid.")
		    else:
		        print("Connection to current DM is lost.")
		    # OR:
		    if dm.IsConnectionValid(dm_root="http://ektoras:8080/"):
		        print("Connection to http://ektoras:8080/ is valid.")
		    else:
		        print("Connection to http://ektoras:8080/ is lost.")


	"""

def GetRoot() -> str:

	"""

	Returns the path that currently points to DM.

	Returns
	-------
	str
		Returns a string containing the current DM root.
		A string of length 0 is returned if no DM path is currently set.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm_root = dm.GetRoot()
		    print(dm_root)


	"""

def SetRoot(dm_root: str, username: str, password: str, role: str, ticket: str) -> int:

	"""

	Sets the current DM root to the path DM_PATH.

	Parameters
	----------
	dm_root : str
		A string that describes the path of the DM root directory.

	username : str, optional
		Username (For login to web based DMs).

	password : str, optional
		Password (For login to web based DMs).

	role : str, optional
		User role (For setting the user's role to web based DMs).

	ticket : str, optional
		Ticket (For login to web based DMs). This argument is provided
		when the connection should employ an already available ticket,
		and there is no need to authenticate with username / password.

	Returns
	-------
	int
		Returns 1 if the new DM root has been set successfully and 0 otherwise.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.SetRoot("C:/Users/Local_Work_files/")
		
		
		# Set SPDRM vault as DM Root
		def main():
		    dm.SetRoot("http://magneto.localdomain:8080/", username="user1", password="pass1")
		    # when we want to change the user's role(when supported):
		    dm.SetRoot(
		        "http://magneto.localdomain:8080/",
		        username="user1",
		        password="pass1",
		        role="Administrator",
		    )


	"""

def RemoveRoot(dm_root: str) -> int:

	"""

	Removes the specified DM path or url from the "Set DM Paths" window list.

	Parameters
	----------
	dm_root : str
		The DM path in question.

	Returns
	-------
	int
		Returns 1 if the specified DM root has been removed successfully and 0 otherwise.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.RemoveRoot("C:/Users/Local_Work_files/")


	"""

def GetRootsList() -> object:

	"""

	Returns the whole DM Roots list, with all the info about which DM is current or 
	is enabled for "Check DM Updates".

	Returns
	-------
	object
		Returns None in case no DM paths found or a list of dictionaries containing the information of each DM Root.
		The keys in each dictionary are shown in the following example:
		
		[{'updates_enabled': True, 'is_current': True, 'dm_root': '//mnt/DM1/'},
		 {'updates_enabled': True, 'is_current': False, 'dm_root': '//mnt/DM2/'},
		 {'updates_enabled': False, 'is_current': False, 'dm_root': 'http://dm3:8989/'}]

	See Also
	--------
	ShowDMPathsWindow

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    print(dm.GetRootsList())


	"""

def GetAcceptedValuesForAttribute(type: str, attribute_name: str, return_accepted_values_from_rules: bool) -> object:

	"""

	Given a type and an attribute's name, this function will return the accepted 
	values, as they are defined in the dm_structure.xml or hardcoded, if they exist.

	Parameters
	----------
	type : str
		The type whose Attribute the values are requested. The specified type
		can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
		through the Data Model (e.g. Loadcase).

	attribute_name : str
		The Attribute's name. It can either be a Primary or Secondary Attribute.

	return_accepted_values_from_rules : bool, optional
		Defines if the returned accepted values will be based on the specified rules (True) or if they will be ignored (False)
		Default value: False

	Returns
	-------
	object
		If 'return_accepted_values_from_rules' is False, the function returns a list with the accepted values as strings, if they exist, otherwise returns an empty list.
		If 'return_accepted_values_from_rules' is True, the function returns a list [accepted_values, base_object_type, base_property_name],
		where:
		    'accepted_values' is a dictionary with keys the values of the property of the base object and values the accepted values according to the specified rules.
		    'base_object_type' is a string with the type of the base object
		    'base_property_name' is a string with the property of the base object
		If the Attribute or the Type don't exist, or if any other DM error occurs, None is returned.

	See Also
	--------
	dm.HasAttributeConditionRule, dm.IsAttributeRuleGenerated

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def example1():
		    dm.SetRoot("http://ektoras:7080/", username="admin", password="admin")
		    accepted_values = dm.GetAcceptedValuesForAttribute("parts", "Status")
		    print(accepted_values)
		
		
		def example2():
		    dm_item_type = "Module"
		    attribute = "Group"
		
		    if dm.HasAttributeConditionRule(dm_item_type, attribute):
		        ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, True)
		        print(
		            "The accepted values of the "
		            + attribute
		            + " are specified from the "
		            + ret[2]
		            + " value of the "
		            + ret[1]
		            + " as follows:"
		        )
		        for val in ret[0].keys():
		            print("------------------------------------------------------------")
		            print("When " + ret[2] + " = " + val + ", the accepted values are:")
		            for accepted_val in ret[0][val]:
		                print(accepted_val)
		    else:
		        ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, False)
		        print("The accepted values of the " + attribute + " attribute are:")
		        for val in ret:
		            print(val)


	"""

def GetAttachmentAttributeValues(server_id: str, filename: str, entity_type: str) -> object:

	"""

	This function will collect all attributes and their values for a DM Object's attachment.

	Parameters
	----------
	server_id : str
		The DM Object's server id.

	filename : str
		The attachment's filename, relative to the DM Object.

	entity_type : str, optional
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	Returns
	-------
	object
		Returns a dictionary with attribute names/values as the key/data.
		If nothing is found, None is returned.

	See Also
	--------
	dm.SetAttachmentAttributeValues

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    result = dm.GetAttachmentAttributeValues(
		        server_id="ABy4Ww:Cuo", filename="DA/job_definition.xml"
		    )
		    if result:
		        print(result)


	"""

def SetAttachmentAttributeValues(server_id: str, filename: str, entity_type: str, names_values: object) -> int:

	"""

	This function will set values for attributes for a DM Object's attachment.

	Parameters
	----------
	server_id : str, optional
		The DM Object's server id.
		Although it's an optional argument, it needs to be defined.

	filename : str, optional
		The attachment's filename, relative to the DM Object.

	entity_type : str, optional
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	names_values : object, optional
		A dictionary which holds the attributes to be set, along with their values.

	Returns
	-------
	int
		Returns 1 on success, or 0 on failure.

	See Also
	--------
	dm.GetAttachmentAttributeValues

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    result = dm.SetAttachmentAttributeValues(
		        server_id="ABy4Ww:Cuo",
		        filename="DA/job_definition.xml",
		        names_values={"TEST": "1"},
		    )
		    print("Function returned: ", str(result))
		
		    result = dm.GetAttachmentAttributeValues(
		        server_id="ABy4Ww:Cuo", filename="DA/job_definition.xml"
		    )
		    if result:
		        print(result)


	"""

def GetAttributesFromUniqueRepresentations(server_id: Any, type: str, values: object, ask_sdm: bool, object_id: Any) -> object:

	"""

	This function will return all Properties/Attributes for a specific input, 
	either server ids, a filter or a DM Browser window item.

	Parameters
	----------
	server_id : Any, optional
		The server id of the DM Object, or a list with server ids, if it is already known.
		Required even though it's optional.

	type : str, optional
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	values : object, optional
		A dictionary which holds a filter (names - values)
		that will be used when no server ids or object ids are defined.

	ask_sdm : bool, optional
		In case of SDM CONSOLE, we can query the already downloaded values
		instead of querying DM. It should be used in cases where the query is expected 
		to be very slow.

	object_id : Any, optional
		When this function is called through an action in DM Browser or SDM CONSOLE,
		object_id is the GUI item's id, or a list with object ids. It can be used when 
		we don't know the server_id.

	Returns
	-------
	object
		Returns a list with dictionaries, with the specified attribute values. 
		If the function fails, the list will be empty.

	See Also
	--------
	DMObject

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = dm.GetObjectId("parts", vals)
		    if ret:
		        list_of_dicts = dm.GetAttributesFromUniqueRepresentations(
		            server_id=ret, type="parts"
		        )
		        len_of_list_of_dicts = len(list_of_dicts)
		        for each_dict in list_of_dicts:
		            print("Representation: ", each_dict["Representation"])


	"""

def GetSubHierarchyChildIds(names_values: object, server_id: str, child_server_id: str, hierarchy: str, get_group_ids: bool) -> object:

	"""

	Use this function to get server ids for the children of a DM Object, but at an inner level in the hierarchy.

	Parameters
	----------
	names_values : object, optional
		A dictionary which holds the DM Object's property values
		(all property values must be present for the object's identification).

	server_id : str, optional
		The server id of the DM Object, if it is already known.
		If present, the type and names_values arguments can be omitted.

	child_server_id : str, optional
		The child server id whose subhierarchy will be searched.
		It is used along with the 'hierarchy' argument.

	hierarchy : str, optional
		The "Hierarchy" value for the child whose subhierarchy will be searched.
		It is used along with the 'child_server_id' argument.

	get_group_ids : bool, optional
		If set to True (default), server ids for Groups will also be returned.
		Otherwise, only items that have no children will be returned.

	Returns
	-------
	object
		Returns a list with server ids for DM Objects that exist in the subhierarchy.

	See Also
	--------
	GetComponentsChildIds

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    result = dm.GetSubHierarchyChildIds(
		        server_id="ABy4Ww:Cuo",
		        child_server_id="AAQlbA:Cuo",
		        hierarchy="P4E7656_A-_10_A_F16-KOGR-4100-001-VORDERBAU-ROHKAROSSERI/",
		    )
		    print(str(result))
		    # will print: ['AAQlbA:Cuo', 'ABwdqw:Cuo', 'ABwqjw:Cuo']


	"""

def GetComponentsChildIds(server_id: str, get_group_ids: bool, ask_sdm: bool, object_id: int) -> list:

	"""

	Use this function to get server ids for the children of a DM Object.

	Parameters
	----------
	server_id : str, optional
		The DM Object's server id.
		Required even though it's optional.

	get_group_ids : bool, optional
		When this is True (default), server ids for Groups will also be returned.
		Otherwise, only items that have no children will be returned.

	ask_sdm : bool, optional
		In case of SDM CONSOLE, we can query the already downloaded values 
		instead of querying DM. It should be used in cases where the query is expected to be very slow.

	object_id : int, optional
		When this function is called through an action in DM Browser or SDM CONSOLE,
		object_id is the GUI item's id. It can be used when
		we don't know the server_id.

	Returns
	-------
	list
		A list with server ids for DM Objects that exist in the hierarchy.

	See Also
	--------
	dm.GetSubHierarchyChildIds

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    result = dm.GetComponentsChildIds(server_id="ABy4Ww:Cuo", get_group_ids=False)
		    print(len(result))
		    # will print: 55
		
		    result = dm.GetComponentsChildIds(server_id="ABy4Ww:Cuo")
		    print(len(result))
		    # will print: 67


	"""

def ExecuteSimManagerQuery(query_string: str, dm_root: str, progress_bar: object) -> List[dict]:

	"""

	Runs a query using the SimManager's REST API functionality.
	It is about requesting data for a set of objects. 

	Parameters
	----------
	query_string : str
		type=[OT]&expr=[EL]&view=[VIEW1]&view=[VIEW2]&pageSize=[SIZE]&page=[PAGE]
		oid=[OID]&expr=[EL]
		query=[QUERY_SPEC]
		query=[QUERY_SPEC]&f=[EL1]&f=[EL2]
		
		type: Object type, Is the type of the objects on which the expression is evaluated 
		      (optional, but either type, oid, or query are required).	
		expr: EL expression, Is an EL expression being evaluated on the object type.
		      It's optional. If missing, "this" is assumed. The expression can be a filter
		      (e.g. [name == 'ABC*'], or a navigation expression (e.g. results.keyResults), 
		      or any combination of both. Sorting is also supported.	
		view: View, Is the name of a view. It defines the fields being returned for each 
		      object. If multiple views are specified, then fields of the first valid view in 
		      the list will be returned. It's optional. If missing, "Default" is assumed.	
		pageSize: Integer, Defines the maximum number of objects to be returned.
		          It's optional. If missing, "100" is assumed.
		page: Integer, Defines the which page of the data is returned if there are more 
		      than SIZE objects. It's optional. If missing, "1" is assumed.		
		oid: Object id, Is the ID of an object (id:tid). It can be used instead of an object 
		     type as a starting point. Then the expression will be evaluated in this object.
		query: Query, A serialized query definition 
		       (optional, but either type, oid, or query are required).
		f: EL expression, Instead of providing the name of a view, fields can be specified 
		   defining a new "view". Those fields could be any kind of EL expression.

	dm_root : str, optional
		The target DM root(URL). If not provided, the current DM is assumed.

	progress_bar : object, optional
		The progress can be shown in a BCProgressBar,
		created with guitk.BCProgressBarCreate.

	Returns
	-------
	List[dict]
		Returns a list of dictionaries, with name/value pairs.

	See Also
	--------
	LaunchSimManagerAction, ExportFileFromSimManager, UploadFileToSimManagerVault

	Examples
	--------
	::

		#!/usr/bin/env python
		import os
		
		
		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		def main():
		    if module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    dm.SetRoot(
		        "http://sim-manager-psa:9495/cb2/", username="aroubies", password="aroubies"
		    )
		    results = dm.ExecuteSimManagerQuery(
		        "type=Project&expr=[name=='/CAE']&view=Detailed"
		    )
		    if results:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' returned "
		            + str(len(results))
		            + " total results!"
		        )
		        project_id = results[0].get("_server_id_")
		        if project_id:
		            arguments = {"project": project_id}  # AkmSDQ:AOk
		            print(
		                "LaunchSimManagerAction 'Search' in Project "
		                + str(project_id)
		                + "  returned "
		                + str(dm.LaunchSimManagerAction("Search", arguments))
		            )
		            arguments = {"project": "AkmSDQ:AOks"}
		            print(
		                "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned "
		                + str(dm.LaunchSimManagerAction("Search", arguments))
		            )
		    else:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' failed!"
		        )
		    results = dm.ExecuteSimManagerQuery(
		        "type=Project&expr=[name=='/CAE1']&view=Detailed"
		    )
		    if results:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' returned "
		            + str(len(results))
		            + " total results!"
		        )
		    else:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' failed!"
		        )


	"""

def LaunchSimManagerAction(action_name: str, arguments: object, dm_root: str, return_process_id: bool, progress_bar: object, json: str) -> Any:

	"""

	Launches an Action in SimManager, using the REST API functionality.

	Parameters
	----------
	action_name : str
		The Action's name, e.g. "Search".

	arguments : object
		A dictionary with the Action's parameters.
		The values need to be percent encoded.

	dm_root : str, optional
		The target DM root(URL). If not provided, the current DM is assumed.

	return_process_id : bool, optional
		In case you need the process id returned, this argument should be set to True.

	progress_bar : object, optional
		The progress can be shown in a BCProgressBar,
		created with guitk.BCProgressBarCreate.

	json : str, optional
		User can provide their own JSON string which will be passed to the Action.
		No validation occurs, it's up to the user to make sure the JSON is valid.

	Returns
	-------
	Any
		If the Action runs successfully, True is returned.
		Otherwise, False is returned.
		If the argument return_process_id=True, the process id is returned. If it fails, 
		None will be returned.

	See Also
	--------
	ExecuteSimManagerQuery, ExportFileFromSimManager, UploadFileToSimManagerVault

	Examples
	--------
	::

		#!/usr/bin/env python
		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		if module_exists("ansa"):
		    import meta
		    from meta import dm
		elif module_exists("ansa"):
		    import meta
		    from meta import dm
		import urllib
		from urllib import parse
		
		
		def _getObjectIdByName(objectName, objectType):
		    expr = "type=" + objectType + "&expr=[name=='" + objectName + "']&f=objectId"
		    results = dm.ExecuteSimManagerQuery(expr)
		    objectId = ""
		    if results and len(results) == 1:
		        objectId = results[0].get("Id")
		    return objectId
		
		
		def _addUserToProject(user_info, project_id, role_name):
		    # First get all the Users that are assigned to this Project because it's needed for the next call:
		    existing_users = dm.ExecuteSimManagerQuery(
		        "type=ProjectSubject&expr=[projectDomain[domain.name == 'Default'].project.objectId=='%s' AND subject.type.name=='User' AND role.name!='Project-Visitor']&page=1&pageSize=1000&f=subject.name&f=role&f=role.objectId&f=role.type.objectId&f=subject.objectId&f=subject.type.objectId"
		        % project_id.split(":")[0]
		    )
		    role_id = _getObjectIdByName(role_name, "Role")
		    arguments = dict()
		    arguments["project"] = project_id
		    arguments["projectToUpdate"] = project_id
		    arguments["propagate"] = "true"
		    arguments["varSets"] = "userAndRole"  # needed for the list below
		    users_list = list()
		    for user in existing_users:
		        user_dict = {
		            "user": user.get("User"),
		            "role": user.get("role.objectId") + ":" + user.get("role.type.objectId"),
		        }
		        users_list.append(user_dict)
		    selected_user_dict = {"user": selected_user.get("Name"), "role": role_id}
		    users_list.append(selected_user_dict)
		    arguments["users"] = users_list
		    return dm.LaunchSimManagerAction("AssignUsersToProjectSimActivity", arguments)
		
		
		def _CreateNewComment(project, parent_oid, title, text, comment_type):
		    if not text or text.isspace():
		        text = "-"
		    project_id = _getObjectIdByName(project, "Project")
		    arguments = {
		        "project": project_id,
		        "object": parent_oid,
		        "title": urllib.parse.quote(title),
		        "text": urllib.parse.quote(text),
		        "commentType": comment_type,
		    }
		
		    return dm.LaunchSimManagerAction("CreateCommentSimActivity", arguments)
		
		
		def main():
		    dm.SetRoot(
		        "http://sim-manager-psa:9495/cb2/", username="aroubies", password="aroubies"
		    )
		    results = dm.ExecuteSimManagerQuery(
		        "type=Project&expr=[name=='/CAE']&view=Detailed"
		    )
		    if results:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' returned "
		            + str(len(results))
		            + " total results!"
		        )
		        project_id = results[0].get("Id")
		        if project_id:
		            arguments = {"project": project_id}  # AkmSDQ:AOk
		            print(
		                "LaunchSimManagerAction 'Search' in Project "
		                + str(project_id)
		                + "  returned "
		                + str(dm.LaunchSimManagerAction("Search", arguments))
		            )
		            arguments = {"project": "AkmSDQ:AOks"}
		            print(
		                "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned "
		                + str(dm.LaunchSimManagerAction("Search", arguments))
		            )
		            arguments = {"project": "AkmSDQ:AOks"}
		            print(
		                "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned the id: "
		                + str(
		                    dm.LaunchSimManagerAction(
		                        "Search", arguments, return_process_id=True
		                    )
		                )
		            )
		    else:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' failed!"
		        )
		    results = dm.ExecuteSimManagerQuery(
		        "type=Project&expr=[name=='/CAE1']&view=Detailed"
		    )
		    if results:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' returned "
		            + str(len(results))
		            + " total results!"
		        )
		    else:
		        print(
		            "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' failed!"
		        )
		    ##########################################################################################################
		    # In order to pass DynamicProperties to the Action Arguments:
		
		    project_id = _getObjectIdByName("/Data/Car/Stamp-X-Mapping", "Project")
		    phase_id = _getObjectIdByName("ALU", "ProjectPhase")
		    template_id = _getObjectIdByName(
		        "DCMCrashMappingTemplate", "EnterpriseWorkRequestTemplate"
		    )
		    name = "TRALALA5"
		
		    dynamic_properties_list = list()
		    dynamic_property_dict = {
		        "objectTypeName": "String",
		        "AttrName": "Product Line",
		        "AttrType": "String",
		        "DynamicString": "L6",
		    }
		    dynamic_properties_list.append(dynamic_property_dict)
		    dynamic_property_dict = {
		        "objectTypeName": "String",
		        "AttrName": "Derivat",
		        "AttrType": "String",
		        "DynamicString": "G31",
		    }
		    dynamic_properties_list.append(dynamic_property_dict)
		    dynamic_property_dict = {
		        "objectTypeName": "DCMPartModel",
		        "AttrName": "Parts",
		        "AttrType": "DbObjectList",
		        "DynamicDbObjectList": "Aegt2g:Cuo,AegwRQ:Cuo,Aegp3Q:Cuo,AegwTg:Cuo,AegwXQ:Cuo",
		    }
		    dynamic_properties_list.append(dynamic_property_dict)
		
		    arguments = {
		        "project": project_id,
		        "phase": phase_id,
		        "template": template_id,
		        "name": name,
		        "DynamicProperties": dynamic_properties_list,
		    }
		    dm.LaunchSimManagerAction("PublishWorkRequest", arguments)
		
		
		def main():
		    json = {"name":"PublishWorkRequest","label":"Publish WorkRequest","params":{"template":{"name":"template","value":[""],"label":"Template","required":true,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestTemplate","array":false},"DynamicProperties":{"varSets":{"DynamicProperties":{"params":{"DynamicDocument":{"name":"DynamicDocument","required":false,"type":"FILE","array":false},"AttrName":{"name":"AttrName","required":false,"type":"STRING","array":false},"AttrType":{"name":"AttrType","required":false,"type":"STRING","array":false},"DynamicDbObjectList":{"name":"DynamicDbObjectList","required":false,"type":"ONE_REFERENCE","objectType":"SDMBase","array":true},"DynamicBoolean":{"name":"DynamicBoolean","required":false,"type":"BOOLEAN","array":false},"DynamicString":{"name":"DynamicString","required":false,"type":"STRING","array":false},"DynamicDbObject":{"name":"DynamicDbObject","required":false,"type":"ONE_REFERENCE","objectType":"SDMBase","array":false},"DynamicDouble":{"name":"DynamicDouble","required":false,"type":"DOUBLE","array":false},"DynamicLong":{"name":"DynamicLong","required":false,"type":"LONG","array":false},"DynamicFile":{"name":"DynamicFile","required":false,"type":"FILE","array":false},"objectTypeName":{"name":"objectTypeName","required":false,"type":"STRING","array":false},"DynamicDate":{"name":"DynamicDate","required":false,"type":"DATE","array":false}},"values":[{"AttrName":["Product Line"],"AttrType":["String"],"DynamicString":["L6"],"objectTypeName":["String"]},{"AttrName":["Derivat"],"AttrType":["String"],"DynamicString":["G31"],"objectTypeName":["String"]},{"AttrName":["Parts"],"AttrType":["DbObjectList"],"DynamicDbObjectList":["Aegt2g:Cuo","AegwRQ:Cuo","Aegp3Q:Cuo","AegwTg:Cuo","AegwXQ:Cuo"],"objectTypeName":["DCMPartModel"]}]},"DynamicMeasure":{"values":[],"params":{"MeasureName":{"name":"MeasureName","required":false,"type":"STRING","array":false},"Quantity":{"name":"Quantity","required":false,"type":"DOUBLE","array":false},"QuantityType":{"name":"QuantityType","required":false,"type":"STRING","array":false},"Unit":{"name":"Unit","required":false,"type":"STRING","array":false},"objectTypeName":{"name":"objectTypeName","required":false,"type":"STRING","array":false}}}},"name":"DynamicProperties","value":[],"label":"DynamicProperties","required":false,"type":"LIST","array":false},"startDate":{"name":"startDate","value":[],"label":"Start Date","required":false,"type":"DATE","array":false},"edit":{"name":"edit","value":[],"label":"Edited Object","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"finishDate":{"name":"finishDate","value":[],"label":"Finish Date","required":false,"type":"DATE","array":false},"parent":{"name":"parent","value":[],"label":"Parent","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"workRequest":{"name":"workRequest","value":[],"label":"Work Request","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"type":{"name":"type","value":[],"label":"Work Request Template Type","required":false,"type":"ONE_REFERENCE","objectType":"ObjectType","array":false},"phase":{"name":"phase","value":["Czw:AJk"],"label":"Phase","required":false,"type":"ONE_REFERENCE","objectType":"ProjectPhase","filter":"[isActive=='true']","array":false},"project":{"name":"project","value":[""],"label":"Project","required":true,"type":"ONE_REFERENCE","objectType":"Project","array":false},"inputs":{"name":"inputs","value":[],"label":"Inputs","required":false,"type":"ONE_REFERENCE","objectType":"SDMObject","array":true},"description":{"name":"description","value":[],"label":"Description","required":false,"type":"STRING","array":false},"name":{"name":"name","value":["TRALALA5"],"label":"Name","required":true,"type":"STRING","array":false},"copy":{"name":"copy","value":[],"label":"Copied Object","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"autoRelease":{"name":"autoRelease","value":[],"label":"Auto Release","required":false,"type":"BOOLEAN","array":false}},"execution":"LocalImmediate","version":"1.5.1"}
		    dm.LaunchSimManagerAction("PublishWorkRequest", json=json)


	"""

def GetConnectedUsername(dm_root: str) -> str:

	"""

	The function is used to return the username that was used to connect to the url-based DM.
	If no arguments are given, the current DM is checked.
	If a "dm_root" argument pair is given, then that url will be checked.

	Parameters
	----------
	dm_root : str, optional
		When this argument is given, then that url will be checked.

	Returns
	-------
	str
		Returns the Username.
		If something goes wrong, None will be returned.

	See Also
	--------
	IsConnectionValid

	Examples
	--------
	::

		# no imports needed in this stage
		
		
		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		def main():
		    if module_exists("ansa"):
		        import meta
		        from meta import base, dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import base, dm
		    dm.SetRoot("http://ektoras:8080/", username="aroubies", password="aroubies")
		    print("Connected user: ", dm.GetConnectedUsername())


	"""

def GetLogFileText() -> str:

	"""

	This function assembles logging data from the current My_DM.log file, as well
	as the previously rotated, compressed archives and returns it as a single
	string.
	
	When the lock cannot be acquired, a Runtime exception is thrown. The reason may
	be a transient failure (other operations are running which need to lock the log
	file), or a stale lock file. Stale lock files may be remnants of abnormally
	terminated processes, whose locks have not expired yet.

	Returns
	-------
	str
		Returns a string holding all My_DM.log data.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		try:
		    log_data = dm.GetLogFileText()
		    print(log_data)
		except:
		    print("Couldn't get logging data from My_DM.log")


	"""

def GetLibraryItemAttributeValues(library: str, filename: str) -> object:

	"""

	This function will collect all attributes and their values for a library item File.
	It needs to be a generic Library Item file.

	Parameters
	----------
	library : str
		The library's name, e.g. "batch_mesh_sessions".

	filename : str
		The file's filename, relative to the library, e.g. "test1/test2/file.txt".

	Returns
	-------
	object
		Returns a dictionary with attribute names/values as the key/data.
		If nothing is found, an empty dictionary is returned.

	See Also
	--------
	DownloadLibraryItem, GetAvailableLibraryItems

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.SetRoot("http://spdrm-dev:40080/", username="admin", password="admin")
		    results = dm.GetAvailableLibraryItems("spdrm_scripts")
		    if results:
		        print(results)
		        for result in results:
		            try:
		                print(
		                    result
		                    + ":   "
		                    + str(dm.GetLibraryItemAttributeValues("spdrm_scripts", result))
		                    + "\\n"
		                )
		            except:
		                pass
		    results = dm.GetAvailableLibraryItems("tmp_library_items")
		    if results:
		        print(results)
		        for result in results:
		            try:
		                print(
		                    result
		                    + ":   "
		                    + str(dm.GetLibraryItemAttributeValues("tmp_library_items", result))
		                    + "\\n"
		                )
		            except:
		                pass
		    dm.SetRoot("//mnt/raid_disk/titanas/roubies/DMs/DM_BIG/")
		    results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
		    if results:
		        print(results)
		        for result in results:
		            try:
		                print(
		                    result
		                    + ":   "
		                    + str(
		                        dm.GetLibraryItemAttributeValues("batch_mesh_sessions", result)
		                    )
		                    + "\\n"
		                )
		            except:
		                pass
		    dm.SetRoot("http://sim-manager:9495/cb2/", username="admin", password="admin")
		    results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
		    if results:
		        print(results)
		        for result in results:
		            try:
		                print(
		                    result
		                    + ":   "
		                    + str(
		                        dm.GetLibraryItemAttributeValues("batch_mesh_sessions", result)
		                    )
		                    + "\\n"
		                )
		            except:
		                pass


	"""

def PrintToLogFile(text: str, with_timestamp: bool):

	"""

	Prints a line of text to My_DM.log. 
	
	If 'with_timestamp' is set to 'True', additional timestamp and user data are printed along with 'text'.
	If 'with_timestamp' is set to 'False', only 'text' is printed.

	Parameters
	----------
	text : str
		The line of text to be printed in the My_DM.log.

	with_timestamp : bool, optional
		Determines wether to print additional timestamp and user data along with 'text'.
		(Default: True)

	See Also
	--------
	GetLogFileText, ClearLogFile

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.PrintToLogFile(
		        "My text to be printed in the My_DM.log", True
		    )  # print with timestamp data


	"""

def ClearLogFile(clear_archived_files: bool) -> bool:

	"""

	Clears the contents of the My_DM.log.
	
	If 'clear_archived_files' is set to True, archived log files (if any) are also deleted.
	If 'clear_archived_files' is set to False, only the contents of the current log file are cleared.
	By default, 'clear_archived_files' is True.

	Parameters
	----------
	clear_archived_files : bool, optional
		Determines wether to clear the archived DM log files along with the current.
		(Default: True)

	Returns
	-------
	bool
		Returns:
		True: If both the current log file and the archived were successfully cleared.
		False: If any of the log files failed to be cleared.

	See Also
	--------
	GetLogFileText

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.ClearLogFile(
		        False
		    )  # clears all the contents of the current My_DM.log but not the archived log files (if any)


	"""

def GetDMTypeAttributes(type: str, hardcoded: bool) -> object:

	"""

	Gets the secondary attributes of a particular DM object type  
	(e.g. part, include etc.)

	Parameters
	----------
	type : str
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).
		
		In case of file-based DM with no dm_structure.xml, 
		the accepted values for the argument "type" are:
		"parts", "includes", "configurations", "subsystems",
		"simulation_model", "simulation_run", "report",
		"session", "loadcase", "dm_library_item"

	hardcoded : bool, optional
		The Hardcoded Attributes are not returned by default.
		In order to retrieve those as well, this argument needs to be True.

	Returns
	-------
	object
		Returns a list of secondary attributes. Each secondary attribute in the list 
		is a dictionary of key:value (strings) pairs for all the supported attribute 
		member properties:
		
		'name': the name of the attribute
		'type': the type of the attribute
		'format': the max number of digits allowed by the attribute format, as a string
		'prefix': the prefix for the attribute value
		'default_value': the default value of the attribute
		'accepted_values': a comma seperated list of the attribute's accepted values 
		'colors_for_accepted_values': a comma seperated list of accepted values colors
		'allow_null': 'YES'/'NO', whether the attribute accepts empty (null) values
		'read_only': 'YES'/'NO', whether the attribute is ReadOnly

	See Also
	--------
	dm.GetDMTypeProperties

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    sec_attributes = dm.GetDMTypeAttributes("parts")
		    for attr_dict in sec_attributes:
		        print(attr_dict)


	"""

def GetDMTypeProperties(type: str) -> object:

	"""

	Gets the properties (primary attributes) of a particular DM object type 
	(e.g. part, include etc.)

	Parameters
	----------
	type : str
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).
		
		In case of file-based DM with no dm_structure.xml, 
		the accepted values for the argument "type" are:
		"parts", "includes", "configurations", "subsystems",
		"simulation_model", "simulation_run", "report",
		"session", "loadcase", "dm_library_item"

	Returns
	-------
	object
		Returns a list of properties. Each property in the list is a dictionary of 
		key:value (strings) pairs for all the supported property member attributes:
		
		'name': the name of the property
		'type': the type of the property
		'format': the max number of digits allowed by the property format, as a string
		'prefix': the prefix for the property value
		'default_value': the default value of the property
		'accepted_values': a comma seperated list of the property's accepted values 
		'colors_for_accepted_values': a comma seperated list of accepted values colors
		'allow_null': 'YES'/'NO', whether the property accepts empty (null) values
		'read_only': 'YES'/'NO', whether the property is ReadOnly

	See Also
	--------
	dm.GetDMTypeAttributes

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    properties = dm.GetDMTypeProperties("parts")
		    for prop_dict in properties:
		        print(prop_dict)


	"""

def ExportFileFromSimManager(server_id: str, expr: str, extension: str, dm_root: str, progress_bar: object) -> str:

	"""

	Exports a file using the SimManager's REST API functionality.
	This is about exporting files from the vault.
	The server transfers the file in its original format and will supply 
	a MIME type based on the extension of the file name.

	Parameters
	----------
	server_id : str
		Is the ID of an object (id:tid). It can be used instead of an object type as a starting point. Then the expression will be evaluated in this object.

	expr : str
		Is the EL epxression leading from the given object to the file to be transfered. Care has to be taken that only one file is referenced, e.g. files.model, file.pom_ExportedData.

	extension : str
		The extension that will be added to the downloaded file.
		SimManager will not add any extension, therefore it's up to the user to define it.

	dm_root : str, optional
		The target DM root(URL). If not provided, the current DM is assumed.

	progress_bar : object, optional
		The progress can be shown in a BCProgressBar,
		created with guitk.BCProgressBarCreate.

	Returns
	-------
	str
		Returns the exported filename, usually in a temporary location.
		Returns None in case of failure.

	See Also
	--------
	LaunchSimManagerAction, ExecuteSimManagerQuery, UploadFileToSimManagerVault

	Examples
	--------
	::

		#!/usr/bin/env python
		import os
		
		
		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		def main():
		    if module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    dm.SetRoot("http://sim-manager:9495/cb2/", username="aroubies", password="aroubies")
		    # export file from a Model
		    print(
		        dm.ExportFileFromSimManager(
		            server_id="AecJ6Q:CuE", expr="files.model", extension="ansa"
		        )
		    )
		    # export file from a Process
		    print(
		        dm.ExportFileFromSimManager(
		            server_id="A3l8Ow:AN4", expr="file.pom", extension="xml"
		        )
		    )


	"""

def GetLibraryItemTypes(dm_root: str) -> object:

	"""

	This function returns a list containing the names of all the Rich Library Item
	types that can exist for the DM.

	Parameters
	----------
	dm_root : str, optional
		When this argument is given, then that DM will be used.
		Otherwise, the current DM root is used.

	Returns
	-------
	object
		Returns a list containing strings.
		An empty list is returned if no Rich Library Item types are defined.
		If something goes wrong, None is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import dm
		
		print(dm.GetLibraryItemTypes())
		print(dm.GetLibraryItemTypes(dm_root="C:/test/"))


	"""

def GetObjectHierarchyIds(server_id: str) -> object:

	"""

	This function provides hierarchy related information for all directly contained
	DM objects. With 'directly contained', it is meant that a single query on the
	Server ID provided as argument will only be done. No recursive, follow-up
	queries on children objects will be done, in order to check whether they 
	contain children of their own.
	
	For example, when a Simulation Model gets queried with this function, all 
	contained Subsystems will be returned only, without any information about 
	possible groups or parts within the subsystems.
	
	On the other hand, when a Subsystem gets queried, all contained groups / parts
	will be returned (which may form arbitrary subhierarchies).

	Parameters
	----------
	server_id : str
		The DM Object's server id.

	Returns
	-------
	object
		This function returns a list of tuples. For each contained DM object, a tuple of
		the form (server_id, parent_server_id) is to be found in the list.

	See Also
	--------
	dm.GetComponentsChildIds

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    hier = dm.GetObjectHierarchyIds(server_id="A2w7qg:Cuo")
		    print(hier)
		    # [('A2w9Sg:Cuo', 'A2w9Rw:Cuo'), ('A2w9Rw:Cuo', 'A2w7qg:Cuo'), ...]


	"""

def RunDMSession(server_id: str, session_id: str):

	"""

	Run a DM Session on a certain DM server id

	Parameters
	----------
	server_id : str
		The server id on which the session will run

	session_id : str
		The id of the session

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.RunDMSession(server_id="48", session_id="79")
		
		
		if __name__ == "__main__":
		    main()


	"""

def HasAttributeConditionRule(type: str, attribute_name: str) -> bool:

	"""

	Given a type and an attribute's name, this function will check whether a condition rule is defined.

	Parameters
	----------
	type : str
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	attribute_name : str
		The Attribute's name. It can either be a Primary or Secondary Attribute.

	Returns
	-------
	bool
		Returns True if the attribute has a condition rule. Otherwise, it returns False.

	See Also
	--------
	dm.GetAcceptedValuesForAttribute, dm.IsAttributeRuleGenerated

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm_item_type = "Module"
		    attribute = "Group"
		
		    if dm.HasAttributeConditionRule(dm_item_type, attribute):
		        ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, True)
		        print(
		            "The accepted values of the "
		            + attribute
		            + " are specified from the "
		            + ret[2]
		            + " value of the "
		            + ret[1]
		            + " as follows:"
		        )
		        for val in ret[0].keys():
		            print("------------------------------------------------------------")
		            print("When " + ret[2] + " = " + val + ", the accepted values are:")
		            for accepted_val in ret[0][val]:
		                print(accepted_val)
		    else:
		        ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, False)
		        print("The accepted values of the " + attribute + " attribute are:")
		        for val in ret:
		            print(val)


	"""

def IsAttributeRuleGenerated(type: str, attribute_name: str) -> bool:

	"""

	Given a type and an attribute's name, this function will check whether the value of this attribue is auto-generated by a rule.

	Parameters
	----------
	type : str
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	attribute_name : str
		The Attribute's name. It can either be a Primary or Secondary Attribute.

	Returns
	-------
	bool
		Returns True if the attribute value is auto-generated by a rule. Otherwise, it returns False.

	See Also
	--------
	dm.GetAcceptedValuesForAttribute, dm.HasAttributeConditionRule

	"""

def GetAttributeValueFromGenerationRule(type: str, attribute_name: str, attribute_values: object) -> str:

	"""

	Given a type, an attribute's name and the attribute values, this function will 
	return the generated value that is defined by the rule in the dm_structure.xml.

	Parameters
	----------
	type : str
		The type whose Attribute the value is requested. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

	attribute_name : str
		The Attribute' s name. It can either be a Primary or Secondary Attribute.

	attribute_values : object
		A dictionary containing the attribute name-values dictionary per attribute type that determine the value of the input attribute. e.g. {'Parts' : {'Name': 'my_name', 'Module Id':''001'}, 'Subsystems : {'Name':'subsystem_name', 'Version':A}}

	Returns
	-------
	str
		The generated attribute value.
		If the attribute is not rule generated it will return None.
		If not all required attribute values are given in 'attribute_values' the default values will be selected.
		If the argument 'attribute_values' is not a dict with dicts as value it will return None.

	See Also
	--------
	dm.IsAttributeRuleGenerated, dm.GetAttributeGenerationRule

	Examples
	--------
	::

		import os
		import meta
		from meta import dm
		
		
		def main():
		    attr_type = "Module"
		    attribute = "Name"
		
		    if dm.IsAttributeRuleGenerated(type=attr_type, attribute_name=attribute):
		        rule = dm.GetAttributeGenerationRule(type=attr_type, attribute_name=attribute)
		        values = {
		            "Subsystems": {"Module Id": 1000, "Version": "AAA", "Study Version": "0001"}
		        }
		        new_val = dm.GetAttributeValueFromGenerationRule(
		            type=attr_type, attribute_name=attribute, attribute_values=values
		        )


	"""

def ShowDMPathsWindow() -> str:

	"""

	Shows the "Set DM Paths" window.

	Returns
	-------
	str
		Returns a string containing the current DM root if it succeeds.
		Returns None in case of "Cancel" or failure to add a DM.

	See Also
	--------
	GetRoot, SetRoot, GetRootsList

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm_root = dm.ShowDMPathsWindow()
		    print(dm_root)


	"""

def GetAttributeGenerationRule(type: str, attribute_name: str) -> object:

	"""

	Given a type and an attribute's name, this function will return the generation
	rule, if exists.

	Parameters
	----------
	type : str
		The type whose Attribute the generation rule is requested. The specified type
		can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
		through the Data Model (e.g. Loadcase).

	attribute_name : str
		The Attribute's name. It can either be a Primary or Secondary Attribute.

	Returns
	-------
	object
		A dictionary with key the attribute type and value a list of the attribute names 
		that determine the value of the input attribute.
		e.g. {'Subsystems': ['Module Id', 'Version', 'Study Version']}
		If the attribute is not rule generated, it will return None.

	See Also
	--------
	dm.IsAttributeRuleGenerated, dm.GetAttributeValueFromGenerationRule

	Examples
	--------
	::

		import os
		import meta
		from meta import dm
		
		
		def main():
		    attr_type = "Module"
		    attribute = "Name"
		
		    if dm.IsAttributeRuleGenerated(type=attr_type, attribute_name=attribute):
		        rule = dm.GetAttributeGenerationRule(type=attr_type, attribute_name=attribute)
		        values = {
		            "Subsystems": {"Module Id": 1000, "Version": "AAA", "Study Version": "0001"}
		        }
		        new_val = dm.GetAttributeValueFromGenerationRule(
		            type=attr_type, attribute_name=attribute, attribute_values=values
		        )


	"""

def ExportDMStructureXml(filename: str) -> bool:

	"""

	Exports the current Data Model to an XML file in the user defined directory. 

	Parameters
	----------
	filename : str, optional
		The full path directory (including the filename) where the XML file will be exported.
		If filename is not defined the XML file will replace the dm_structure.xml of the current DM.

	Returns
	-------
	bool
		Funtion returns a boolean  defining the result of the function.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import dm
		
		
		def main():
		    # Save to Current DM XML file (Warning:Using the bellow function will overwrite your current dm_structure.xml)
		    result = dm.ExportDMStructureXml()
		    print(result)
		    # Save to a user defined location
		    result = dm.ExportDMStructureXml(filename="/path/to/export/your_xml_file.xml")
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAcceptedValuesForAttribute(type: str, attr_name: str, accepted_values: str) -> bool:

	"""

	Changes the Accepted Values of an Attribute if the Type of that specific Attribute allows it.

	Parameters
	----------
	type : str
		The name of the object that contains the Attribute whose Accepted Values will change.

	attr_name : str
		The name of the Attribute whose Accepted Values will change.

	accepted_values : str
		The Accepted values that will be applied to the Attribute.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	GetAcceptedValuesForAttribute

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Change Accepted Values
		    result = dm.SetAcceptedValuesForAttribute(
		        type="type", attr_name="attr_name", accepted_values="the,new,accepted,values"
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetDefaultValueForAttribute(type: str, attr_name: str, default_value: str) -> bool:

	"""

	Changes the Default Value of an Attribute if the Type of that specific Attribute allows it.

	Parameters
	----------
	type : str
		The name of the object that contains the Attribute whose Default Value will change.

	attr_name : str
		The name of the Attribute whose Default Value will change.

	default_value : str
		The Default Value that will be applied to the Attribute.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	GetDefaultValueForAttribute

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Change Default Value
		    dm.SetDefaultValueForAttribute(
		        type="type", attr_name="attr_name", default_value="new_default_value"
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetDefaultValueForAttribute(type: str, attr_name: str) -> str:

	"""

	Returns the current Default Value of an Attribute.

	Parameters
	----------
	type : str
		The name of the object that contains the Attribute whose Default Value will be returned.

	attr_name : str
		The name of the Attribute whose Default Value will be returned.

	Returns
	-------
	str
		Function returns a string with the Default Value of the Attribute contained in the Object Type.

	See Also
	--------
	SetDefaultValueForAttribute

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import dm
		
		
		def main():
		    def_val = dm.GetDefaultValueForAttribute(type="type", attr_name="attr_name")
		    print(def_val)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateGenerationRule(type: str, rule_name: str, disc_chars: str, generated_value: str, rejected_characters: str, generator_name: str, generator_value: str, trim_empty_values: bool=False) -> bool:

	"""

	This function is used in order to create a new Generation Rule for the current DM.

	Parameters
	----------
	type : str
		The name of the object that will contain the created Generation Rule.

	rule_name : str
		The name of the Generation Rule that will be created.

	disc_chars : str, optional
		The Discarded values of the Generation Rule.

	generated_value : str, optional
		The Generated Value of the Generation Rule.

	rejected_characters : str, optional
		The discarded characters of the Generation Rule.

	generator_name : str, optional
		The Generator Name of the Generation Rule condition.

	generator_value : str, optional
		The Generator Value of the Generation Rule condition.

	trim_empty_values : bool, optional
		If True the trailing empty sections of the Generated Value are trimmed.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	DeleteGenerationRule, SetGeneratedValueOfGenerationRule, GetGeneratedValueOfGenerationRule

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Create Generation Rule
		    result = dm.CreateGenerationRule(
		        type="ANSA_SUBSYSTEM",
		        rule_name="Name",
		        generated_value="[Module Id]_[Project]_[Phase]",
		        generator_name="Discipline",
		        generator_value="CRASH",
		        trim_empty_values=True,
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteGenerationRule(type: str, rule_name: str, generator_name: str, generator_value: str) -> bool:

	"""

	This function is used in order to delete a Generation Rule for the current DM.

	Parameters
	----------
	type : str
		The name of the object that contains the Generation Rule about to be deleted.

	rule_name : str
		The name of the Generation Rule that will be deleted.

	generator_name : str, optional
		The Generator Name of the Generation Rule condition.

	generator_value : str, optional
		The Generator Value of the Generation Rule condition.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	CreateGenerationRule, SetGeneratedValueOfGenerationRule, GetGeneratedValueOfGenerationRule

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Delete Generation Rule (Assuming that the object and the rule exists)
		    result = dm.DeleteGenerationRule(
		        type="ANSA_SUBSYSTEM",
		        rule_name="Name",
		        generator_name="Discipline",
		        generator_value="CRASH",
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetGeneratedValueOfGenerationRule(type: str, rule_name: str, generator_name: str, generator_value: str) -> str:

	"""

	Returns the current Generated Value of a Generated Rule.

	Parameters
	----------
	type : str
		The name of the object that contains the Generation Rule.

	rule_name : str
		The name of the Generation Rule whose Generated Value will be returned.

	generator_name : str, optional
		The Generator Name of the Generation Rule condition.

	generator_value : str, optional
		The Generator Value of the Generation Rule condition.

	Returns
	-------
	str
		Function returns a string with the Generated Value of the Generation Rule contained in the Object Type.

	See Also
	--------
	CreateGenerationRule, DeleteGenerationRule, SetGeneratedValueOfGenerationRule

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Get Generated Value of Generation Rule
		    result = dm.GetGeneratedValueOfGenerationRule(
		        type="type",
		        rule_name="rule_name",
		        generator_name="Discipline",
		        generator_value="CRASH",
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetGeneratedValueOfGenerationRule(type: str, rule_name: str, generated_value: str, generator_name: str, generator_value: str) -> bool:

	"""

	Using this function you can change the Generated Value of an existing Generation Rule.

	Parameters
	----------
	type : str
		The name of the object that contains the Generation Rule.

	rule_name : str
		The name of the Generation Rule whose Generated Value will be modified.

	generated_value : str
		The new Generated Value of the Generation Rule.

	generator_name : str, optional
		The Generator Name of the Generation Rule condition.

	generator_value : str, optional
		The Generator Value of the Generation Rule condition.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	CreateGenerationRule, DeleteGenerationRule, GetGeneratedValueOfGenerationRule

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Set Generated Value of Generation Rule
		    result = dm.SetGeneratedValueOfGenerationRule(
		        type="ANSA_SUBSYSTEM",
		        rule_name="Name",
		        generated_value="[Module Id]_[Project]_[Phase]",
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateConditionRule(type: str, rule_name: str, generator_name: str, generator_value: str, accepted_values: str) -> bool:

	"""

	This function is used in order to create a new Condition Rule for the current DM.

	Parameters
	----------
	type : str
		The name of the object that will contain the created Condition Rule.

	rule_name : str
		The name of the Condition Rule that will be created.

	generator_name : str
		The Generator Name of the Condition Rule.

	generator_value : str, optional
		The Generator Value of the Condition Rule.

	accepted_values : str, optional
		The Accepted Values of the Condiition Rule.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	DeleteConditionRule, GetGeneratorValuesOfConditionRules, SetGeneratorValueOfConditionRule

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Create Condition Rule
		    result = dm.CreateConditionRule(
		        type="type",
		        rule_name="rule_name",
		        generator_name="generator_name",
		        generator_value="generator_value",
		        accepted_values="accepted_values",
		    )
		    print(result)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteConditionRule(type: str, rule_name: str, generator_value: str) -> bool:

	"""

	This function is used in order to delete a Condition Rule for the current DM.

	Parameters
	----------
	type : str
		The name of the object that contains the Condition Rule about to be deleted.

	rule_name : str
		The name of the Condition Rule that will be deleted.

	generator_value : str
		The Generator Value of the Condition Rule.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	CreateConditionRule, GetGeneratorValuesOfConditionRules, SetGeneratorValueOfConditionRule

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Delete Condition Rule
		    dm.DeleteConditionRule(
		        type="type", rule_name="rule_name", generator_value="new_generator_value"
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetGeneratorValuesOfConditionRules(type: str, rule_name: str) -> object:

	"""

	This function returns all the Generator Values used by a specific rule name.
	Multiple Condition Rules can have the same rule and generator name but different generator values.

	Parameters
	----------
	type : str
		The type of the object that will contain Condition Rules.

	rule_name : str
		The name of the Condition Rules that contain the Generator Values.

	Returns
	-------
	object
		Returns a list of strings with the generator values of the specific Condition Rule contained in the specific Object Type

	See Also
	--------
	CreateConditionRule, DeleteConditionRule, SetGeneratorValueOfConditionRule

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Get Generator Values of the Condition Rules contained in a specific type with a specific rule_name
		    dm.GetGeneratorValuesOfConditionRules(
		        type="parts", rule_name="RepresentationRule01"
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetGeneratorValueOfConditionRule(type: str, rule_name: str, old_generator_value: str, generator_value: str) -> bool:

	"""

	This Function is used in order to change the Generator Value of a specific Condition Rule.

	Parameters
	----------
	type : str
		The type of the object that contains the Condition Rule about to be modified.

	rule_name : str
		The name of the Condition Rule that will be modified.

	old_generator_value : str
		The old value of the Generator Value. This value is needed because multiple Condition Rules can have the same rule name.

	generator_value : str
		The new value of the Generator Value.

	Returns
	-------
	bool
		Function returns a boolean variable defining the result of the function.

	See Also
	--------
	CreateConditionRule, DeleteConditionRule, GetGeneratorValuesOfConditionRules

	Examples
	--------
	::

		# Python Script
		import meta
		from meta import dm
		
		
		def main():
		    # Set Generator Value of Condition Rule
		    dm.SetGeneratorValueOfConditionRule(
		        type="type",
		        rule_name="rule_name",
		        old_generator_value="old_generator_value",
		        generator_value="new_generator_value",
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def UploadFileToSimManagerVault(file_path: str, sim_activity_name: str, file_param_name: str, object_type: str, progress_bar: object) -> str:

	"""

	Uploads a file to the SimManager vault and retrieves the vault id.

	Parameters
	----------
	file_path : str
		The file that will be uploaded to SimManager.

	sim_activity_name : str
		The activity's name is needed for SimManager 2014.

	file_param_name : str
		The name of the FILE parameter in the SimActivity.

	object_type : str
		The object type of the object to which the file will be attached. 
		If there is no target object type, use "Project".

	progress_bar : object, optional
		The progress can be shown in a BCProgressBar,
		created with guitk.BCProgressBarCreate.

	Returns
	-------
	str
		If the file is successfully added, the vault id will be returned.
		Returns None in case of failure.

	See Also
	--------
	ExportFileFromSimManager, LaunchSimManagerAction, ExecuteSimManagerQuery

	Examples
	--------
	::

		import meta
		
		
		def main():
		    selected_import_file = meta.utils.SelectOpenFile(0)
		    if not selected_import_file:
		        return
		    selected_import_file = selected_import_file[0]
		
		    ret_vault_id = meta.dm.UploadFileToSimManagerVault(
		        selected_import_file, "Import", "importFile", "Project"
		    )
		    print(ret_vault_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetObjectTypeFromAnsaKeyword(keyword: str, dm_root: str) -> str:

	"""

	This function returns the DM object type of dm_root that corresponds to the input ANSA keyword.
	If dm_root is not defined, the current DM root is used.

	Parameters
	----------
	keyword : str
		The input ANSA keyword.

	dm_root : str, optional
		When this argument is given, then that DM will be used.
		Otherwise, the current DM root is used.

	Returns
	-------
	str
		Returns the DM object type. If no object type is found, it returns None.

	See Also
	--------
	dm.GetAnsaKeywordFromObjectType

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    ansa_keyword = "ANSAPART"
		    dm_object = dm.GetObjectTypeFromAnsaKeyword(ansa_keyword)
		    print("The returned dm_object is: " + dm_object)
		
		    ansa_keyword = dm.GetAnsaKeywordFromObjectType(dm_object)
		    print("The returned ansa_keyword is: " + ansa_keyword)


	"""

def GetAnsaKeywordFromObjectType(type: str, dm_root: str) -> str:

	"""

	This function returns the ANSA keyword that corresponds to the input DM object type of dm_root.
	If dm_root is not defined, the current DM root is used.

	Parameters
	----------
	type : str
		The input DM object type.

	dm_root : str, optional
		When this argument is given, then that DM will be used.
		Otherwise, the current DM root is used.

	Returns
	-------
	str
		Returns the ANSA keyword. If no ANSA keyword is found, it returns None.

	See Also
	--------
	dm.GetObjectTypeFromAnsaKeyword

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    ansa_keyword = "ANSAPART"
		    dm_object = dm.GetObjectTypeFromAnsaKeyword(ansa_keyword)
		    print("The returned dm_object is: " + dm_object)
		
		    ansa_keyword = dm.GetAnsaKeywordFromObjectType(dm_object)
		    print("The returned ansa_keyword is: " + ansa_keyword)


	"""

def GetDMReferences(server_id: str, ref_server_id: str, ref_type: str, find_sim_runs_through_contents: bool=False) -> object:

	"""

	This function queries the DM for all references that satisfy certain criteria.
	Each of the 4 optional arguments provides a filtering criterion:
	* server_id
	  Server ID of the object doing the referring (reference source). This argument
	  defines the object that is using some other objects.
	* ref_server_id
	  Server ID of the object being referred-to (reference target). This argument
	  defines the object that is being used by some other objects.
	* ref_type
	  Reference type
	* find_sim_runs_through_contents
	  Flag indicating whether Simulation Runs' history references 
	  based on its contents should be searched.
	  
	When multiple arguments are provided, then the corresponding criteria are 
	combined with an AND logical operator.

	Parameters
	----------
	server_id : str, optional
		When present, the DM References query will
		search for references that originate from
		the object with this specific Server ID
		(Object is user)

	ref_server_id : str, optional
		When present, the DM References query will
		search for references that point to the
		object with this specific Server ID.
		(Object is being used)

	ref_type : str, optional
		When present, the DM References query will
		search for references of the specific type.

	find_sim_runs_through_contents : bool, optional
		When True, if the Server ID refers to a Simulation Run,
		the DM References query will search for references of 
		history type based on the contained Simulation Model 
		and Loadcase.

	Returns
	-------
	object
		Returns the list of DMReferences that satisfy the provided criteria

	See Also
	--------
	dm.DMReference, dm.RemoveDMReference

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def removeStrongReferences():
		    # Remove all manually added strong references
		    strong_refs = dm.GetDMReferences(ref_type="strong")
		    for ref in strong_refs:
		        print(
		            "Removing strong reference from {} to {}".format(
		                ref.server_id, ref.ref_server_id
		            )
		        )
		        dm.RemoveDMReference(ref)
		
		
		def getPreviousDMO(dmo_server_id):
		    # Get the previous DM Object that have a history link with the current one
		    # (Current DM Object with Id = dmo_server_id, was created based on this)
		
		    dmo = dm.DMObject(server_id=dmo_server_id)
		    if not dmo.is_valid():
		        print(
		            "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
		        )
		        return None
		
		    refs = dm.GetDMReferences(server_id=dmo_server_id, ref_type="history")
		
		    for ref in refs:
		        print("Current DM Object Id: ", ref.server_id)
		        print("Previous DM Object Id: ", ref.ref_server_id)
		
		
		def getNextDMOs(dmo_server_id):
		    # Get the next DM Objects that have a history link with the current one
		    # (DM Objects that were created from the DM Object with Id = dmo_server_id)
		
		    dmo = dm.DMObject(server_id=dmo_server_id)
		    if not dmo.is_valid():
		        print(
		            "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
		        )
		        return None
		
		    refs = dm.GetDMReferences(ref_server_id=dmo_server_id, ref_type="history")
		
		    for ref in refs:
		        print("Current DM Object Id: ", ref.server_id)
		        print("Next DM Object Id(s): ", ref.ref_server_id)
		
		
		def getRunAncestors(dmo_server_id):
		    # Get the previous Sim Run that have a history link with the current one,
		    # searching through the contents of the current Sim Run (Sim Model, Loadcase)
		    # (Current Sim Run with Id = dmo_server_id, was created based on this)
		    dmo = dm.DMObject(server_id=dmo_server_id)
		    if not dmo.is_valid():
		        print(
		            "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
		        )
		        return None
		
		    refs = dm.GetDMReferences(
		        server_id=dmo_server_id, ref_type="history", find_sim_runs_through_contents=True
		    )
		    for ref in refs:
		        print("Current Sim Run Id: ", ref.server_id)
		        print("Previous Sim Run Id: ", ref.ref_server_id)
		
		
		def getSolverFileTypeSubs(dmo_server_id):
		    # Get the Solver File Type Subsystems
		    # that were produced from Subsystem with ANSA File Type
		    sub = dm.DMObject(server_id=dmo_server_id)
		    if not sub.is_valid():
		        print(
		            "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
		        )
		        return None
		
		    refs = dm.GetDMReferences(ref_server_id=dmo_server_id, ref_type="repr_derivation")
		    for ref in refs:
		        print("Current Subsystem Id: ", ref.ref_server_id)
		        print("Subsystem with Solver File Type Id: ", ref.server_id)


	"""

def RemoveDMReference(reference: object) -> bool:

	"""

	This function deletes a Reference from the DM

	Parameters
	----------
	reference : object
		DMReference object, describing the reference to be removed

	Returns
	-------
	bool
		Returns True when the removal operation was successful, regardless of whether an
		actual reference existed / got deleted from the DM or not. It is certain though
		that such a reference no longer exists.

	See Also
	--------
	dm.DMReference, dm.GetDMReferences

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Remove all manually added strong references
		    strong_refs = dm.GetDMReferences(ref_type="strong")
		    for ref in strong_refs:
		        print(
		            "Removing strong reference from {} to {}".format(
		                ref.server_id, ref.ref_server_id
		            )
		        )
		        dm.RemoveDMReference(ref)


	"""

def AddClusterMember(path: str, nickname: str) -> bool:

	"""

	This function inserts a new, read only member into the currently configured
	Cluster DM.

	Parameters
	----------
	path : str
		DM Root of the DM that will be backing the new
		cluster member.

	nickname : str, optional
		String to be used as nickname for the new
		cluster member. May contain the latin letters, 
		digits, the underscore and dash characters.
		If this argument is not provided, the new
		cluster member's nickname will be auto generated
		from the path argument.

	Returns
	-------
	bool
		Returns True if the new member was successfully admitted into the cluster.

	See Also
	--------
	dm.DMClusterMember, dm.GetClusterMembers, dm.RemoveClusterMember

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.SetRoot("cluster://home/user/DMs/main/")
		    dm.AddClusterMember("/home/user/DMs/library/rlis/")
		    dm.AddClusterMember("/home/user/DMs/library/subsystems/", "subs")


	"""

def GetClusterMembers() -> object:

	"""

	This function fetches information about all the cluster members existing in the
	currently configured Cluster DM.

	Returns
	-------
	object
		Returns all cluster members as a list of DMClusterMember objects.

	See Also
	--------
	dm.AddClusterMember, dm.DMClusterMember

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def getFlagsString(flags):
		    flags_strings = []
		
		    # Iterate through all defined flags even though all combinations are not
		    # possible, e.g. a member cannot be both Primary and Read Only.
		    if flags & dm.constants.PRIMARY_MEMBER:
		        flags_strings.append("Primary")
		    if flags & dm.constants.READ_ONLY_MEMBER:
		        flags_strings.append("Read Only")
		    return ", ".join(flags_strings)
		
		
		def main():
		    # A Cluster DM is configured as current DM Root
		    members = dm.GetClusterMembers()
		    for member in members:
		        print("Path      :", member.path)
		        print("Nickname  :", member.nickname)
		        print("Identifier:", member.identifier)
		        print("Flags     :", getFlagsString(member.flags))


	"""

def RemoveClusterMember(path: str) -> bool:

	"""

	This function removes an existing, read only member from the currently 
	configured Cluster DM, provided that there are no cluster level dependencies on
	it.

	Parameters
	----------
	path : str
		DM Root of the cluster member to be removed.

	Returns
	-------
	bool
		Returns True if the member was successfully removed from the cluster.

	See Also
	--------
	dm.DMClusterMember, dm.AddClusterMember, dm.GetClusterMembers

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm.SetRoot("cluster://home/user/DMs/main/")
		    dm.RemoveClusterMember("/home/user/DMs/library/rlis/")


	"""

def InitializeDMForDOE(dm_root: str) -> bool:

	"""

	This function initializes the Filebased DM with the necessary Properties
	and Attributes for use with DOE.
	It will only update the DM when it's empty.

	Parameters
	----------
	dm_root : str, optional
		The function works on the current DM, unless this
		argument is specified.

	Returns
	-------
	bool
		False when the DM isn't empty.
		True if the DM is empty and the initialization is successful.

	Examples
	--------
	::

		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		def main():
		    if module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    print(dm.InitializeDMForDOE())


	"""

def GetTicket(dm_root: str) -> str:

	"""

	This function returns the authentication ticket that is currently being used in
	a connection to a remote, web based DM (SPDRM or SimManager).

	Parameters
	----------
	dm_root : str, optional
		The URL of the remote, web based DM. If this argument
		is not provided, the Current DM Root will be used.

	Returns
	-------
	str
		Returns the authentication ticket as a string.

	See Also
	--------
	dm.SetRoot

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def amin():
		    dm.SetRoot("http://magneto.localdomain:8080/", username="user1", password="pass1")
		    ticket = dm.GetTicket()
		    print("Ticket used in Current DM Connection:", ticket)


	"""

def GetFeatureItemTypes(dm_root: str) -> object:

	"""

	This function returns a list containing the names of all the Feature Item types
	that can exist for the DM.

	Parameters
	----------
	dm_root : str, optional
		When this argument is given, then that DM will 
		be used. Otherwise, the current DM root is used.

	Returns
	-------
	object
		Returns a list containing strings.
		An empty list is returned if no Feature Item types are defined.
		If an error occurs, None is returned.

	See Also
	--------
	dm.GetLibraryItemTypes

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import dm
		
		print(dm.GetFeatureItemTypes())
		print(dm.GetFeatureItemTypes(dm_root="C:/test/"))


	"""

def GetMultiDMReferences(server_ids: object, ref_types: object, recursive: bool, returned_ents: int) -> object:

	"""

	This function queries the DM for all references that involve multiple Server IDs
	and for possibly multiple reference types. The query can be recursive and it is
	user selectable whether the query should search for the objects being used or
	are using the Server IDs provided as arguments

	Parameters
	----------
	server_ids : object
		Sequence of strings, holding the Server IDs for
		which references will be queried.

	ref_types : object, optional
		Sequence of strings, holding the Reference Types
		for which reference will be queried. If empty, 
		then all types of references will be returned.
		Default value: Empty list

	recursive : bool, optional
		This value defines whether references should be
		recursively queried, using the provided server ids
		as starting points.
		Default value: False

	returned_ents : int, optional
		This value defines whether references originating
		from or terminating into the provided Server IDs
		should be queried.
		Default value: dm.constants.DM_REF_FROM

	Returns
	-------
	object
		Returns the list of DMReferences that satisfy the provided criteria

	See Also
	--------
	dm.DMReference, dm.GetDMReferences

	Examples
	--------
	::

		import meta
		from meta import dm
		
		server_ids = ["main:6", "lib:3"]
		ref_types = ["history"]
		refs = dm.GetMultiDMReferences(
		    server_ids, ref_types, returned_ents=dm.constants.DM_REF_FROM, recursive=True
		)
		
		for ref in refs:
		    print(ref)


	"""

def RebuildFromDisk(dm_root: str) -> bool:

	"""

	The DM's database file is updated by scanning the DM directory contents.

	Parameters
	----------
	dm_root : str, optional
		The function works on the current DM, unless this
		argument is specified.

	Returns
	-------
	bool
		False when the DM isn't Filebased.
		True if the DM is Filebased.

	Examples
	--------
	::

		def module_exists(module_name):
		    try:
		        __import__(module_name)
		    except ImportError:
		        return False
		    else:
		        return True
		
		
		def main():
		    if module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    elif module_exists("ansa"):
		        import meta
		        from meta import dm
		    print(dm.RebuildFromDisk())


	"""

def IsIntermodularConnectivityLinksFeatureSupported() -> bool:

	"""

	The function is used to check if intermodular_connectivity_links 
	feature is supported by current DM schema.

	Returns
	-------
	bool
		Returns True if feature is supported, or False if not supported.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    if dm.IsIntermodularConnectivityLinksFeatureSupported():
		        print("Feature supported.")
		    else:
		        print("Feature not supported.")


	"""

def QueryDMTypes(rich_library_items: bool, feature_items: bool) -> object:

	"""

	Collect all object types that exist in DM.
	Only the DM Schema types are returned unless the optional arguments are specified,
	in which case Rich Library Items or Feature Items will also be returned
	(if found).

	Parameters
	----------
	rich_library_items : bool, optional
		Optional boolean argument to determine if Rich Library Items will also be returned.

	feature_items : bool, optional
		Optional boolean argument to determine if Feature Items will also be returned.

	Returns
	-------
	object
		Returns a list containing the found object types.
		None is returned when the DM is not properly initialized.

	See Also
	--------
	GetDMSchemaTypes

	Examples
	--------
	::

		import meta
		from meta import dm
		
		# only get the DM Schema types:
		print(dm.QueryDMTypes())
		
		# return also Rich Library Items and Feature Items:
		print(dm.QueryDMTypes(rich_library_items=True, feature_items=True))


	"""

def GetDMSchemaTypes(dm_root: str) -> object:

	"""

	Collect all the DM Schema object types that can exist for the DM.

	Parameters
	----------
	dm_root : str, optional
		When this argument is given, then that DM will be used.
		Otherwise, the current DM root is used.

	Returns
	-------
	object
		Returns a list containing the object types.
		If something goes wrong, None is returned.
		Example return values:
		
		['parts', 'includes', 'configurations', 'Subsystems', 'Simulation_Model', 'LoadCase', 'Simulation_Run', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'Report']
		['parts', 'includes', 'configurations', 'Simulation_Model', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'Component', 'Run', 'Loadcase', 'Report']
		['parts', 'includes', 'configurations', 'Subsystems', 'Simulation_Model', 'LoadCase', 'Simulation_Run', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'CAE_Top_Node', 'Input_Deck', 'Report']

	See Also
	--------
	GetFeatureItemTypes, GetLibraryItemTypes

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import dm
		
		print(dm.GetDMSchemaTypes())
		print(dm.GetDMSchemaTypes(dm_root="C:/test/"))


	"""

def GetLastErrorMessage() -> str:

	"""

	Returns the last error message from DM operations.

	Returns
	-------
	str
		Returns a string containing the last error message.
		An empty string is returned when no error exists.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		print(dm.GetLastErrorMessage())


	"""

def GetConnectionStatus() -> int:

	"""

	The function performs a ping operation on the connected SPDRM DM.
	A valid SPDRM DM root should have been specified first.

	Returns
	-------
	int
		Returns the ping value in milliseconds on success or an exception on error.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    ping_val = dm.GetConnectionStatus()
		    print(ping_val)


	"""

class DMObject():

	"""

	A class that handles communication with DM and functionality regarding Objects in DM.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    new_dict = {
		        "Module Id": "981483828A",
		        "Version": "R1114567893_---",
		        "Study Version": "0",
		        "File Type": "ANSA",
		        "Representation": "CRASH",
		    }
		    new_object = dm.DMObject(names_values=new_dict, type="parts")
		    print(new_object.server_id)
		
		
		# method: add_new
		import meta
		from meta import dm
		
		
		def main():
		    # add_new (with a Representation File):
		    names_values = {
		        "Module Id": "Module1",
		        "Study Version": "0",
		        "Representation": "Representation1",
		        "Name": "Name1",
		        "File Type": "Nastran",
		        "Project": "Project1",
		        "Release": "Rel1",
		        "Variant": "Var1",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_server_id = new_object.add_new(
		        filename="C:/home/demo/tmp/representation_file.nas"
		    )
		    if new_server_id:
		        print("New server_id: ", new_server_id)
		    else:
		        print("add_new failed.")
		    # add_new (with no Representation File):
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_server_id = new_object.add_new()
		    if new_server_id:
		        print("New server_id: ", new_server_id)
		    else:
		        print("add_new failed.")
		
		
		# method: connect
		import meta
		from meta import dm
		
		
		def main():
		    dict2 = {
		        "Module Id": "Module1",
		        "Version": "Version1",
		        "Study Version": "0",
		        "Representation": "Representation1",
		        "Variant": "Variant1",
		        "Name": "Name1",
		    }
		    object2 = dm.DMObject(names_values=dict2, type="Subsystems")
		    print(object2.connect({object2.server_id: "my_component"}))
		
		    part1 = dm.DMObject(server_id="1057023", type="parts")
		    part2 = dm.DMObject(server_id="1057026", type="parts")
		    print(part2.connect({part1.server_id: "strict"}))
		
		
		# method: export
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_object.export("C:/home/demo/tmp")
		    new_object.export("C:/home/demo/tmp", export_type="hierarchy")
		
		
		# method: get_all_values
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    values = new_object.get_all_values()
		    print(values)
		
		
		# method: get_attribute_values
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_object.set_attribute_values(
		        attributes_values={"TEST": "New_Val", "TEST_NUM": "23.43"},
		        attributes_types={"TEST_NUM": "DOUBLE"},
		    )
		    print(new_object.get_attribute_values(attributes=["TEST", "TEST_NUM"]))
		
		
		# method: get_conflict_options
		import meta
		from meta import dm
		
		
		def main():
		    new_dict1 = {
		        "Module Id": "PCANSAWIN7_8580_12",
		        "Version": "A1",
		        "Representation": "Connections",
		        "Project": "Training",
		        "Phase": "BBG",
		    }
		    new_object1 = dm.DMObject(names_values=new_dict1, type="parts")
		    print(new_object1.get_conflict_options())
		
		    new_dict2 = {
		        "Module Id": "PCANSAWIN7_8580_13",
		        "Version": "A1",
		        "Representation": "Connections",
		        "Project": "Training",
		        "Phase": "BBG",
		    }
		    new_object2 = dm.DMObject(names_values=new_dict2, type="parts")
		    print(new_object2.get_conflict_options())
		
		    # For conflicts with a partially deleted Object in SPDRM:
		    new_vals = {
		        "Project": "BJA",
		        "File": "32_FR_LH_DOOR_BJA_ABCP_DELETED__001_001",
		        "Milestone": "ABCP",
		        "Representation_Version": "001",
		        "Representation": "DMU",
		        "File Type": "PamCrash",
		        "Study_Version": "001",
		        "Diversity": "DELETED",
		        "Purpose": "MODEL",
		        "Module Id": "32_FR_LH_DOOR",
		        "Loadcase Diversity": "-",
		    }
		    new_vals["Representation_Version"] = "001"
		    obj = dm.DMObject(names_values=new_vals, type="Module")
		    print("Partially deleted")
		    print(obj.server_id)
		    if not obj.server_id:
		        print(obj.ghost_id)
		        if obj.ghost_id:
		            obj = dm.DMObject(server_id=obj.ghost_id, type="Module")
		            print(obj.get_conflict_options())
		
		
		# method: get_contained_objects
		import meta
		from meta import dm
		
		
		def main():
		    object = dm.DMObject(server_id="1082", type="Simulation_Run")
		    print(str(object.get_contained_objects("Report")))
		    object = dm.DMObject(server_id="2270", type="Simulation_Model")
		    print(str(object.get_contained_objects("Report")))
		    print(str(object.get_contained_objects("Simulation_Run")))
		
		
		# method: get_contents
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    contents = new_object.get_contents()
		    print(contents)
		
		
		# method: get_references
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    ref = new_object.get_references(2)
		    print(ref)
		
		
		# method: get_representation_file
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    rf = new_object.get_representation_file()
		    print(rf)
		
		
		# method: get_type
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    type = new_object.get_type()
		    print(type)
		
		
		# method: remove
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_object.remove()
		    new_object.remove("YES")
		
		
		# method: set_attribute_values
		import meta
		from meta import dm
		
		
		def main():
		    names_values = {
		        "Module Id": "Module2",
		        "Study Version": "0",
		        "Representation": "Representation2",
		        "Name": "Name2",
		        "File Type": "Nastran",
		        "Project": "Project2",
		        "Release": "Rel2",
		        "Variant": "Var2",
		        "Discipline": "Crash",
		    }
		    new_object = dm.DMObject(names_values=names_values, type="Subsystems")
		    new_object.set_attribute_values(
		        attributes_values={"TEST": "New_Val", "TEST_NUM": "23.43"},
		        attributes_types={"TEST_NUM": "DOUBLE"},
		    )
		    print(new_object.get_attribute_values(attributes=["TEST", "TEST_NUM"]))
		
		
		# method: get_attachment_values
		import meta
		from meta import dm
		
		
		def main():
		    simulation_model = dm.DMObject(server_id="7", type="Simulation_Model")
		    attachments = simulation_model.get_attachment_values()
		
		
		if __name__ == "__main__":
		    main()
		# method: is_valid
		import meta
		
		dmobj = meta.dm.DMObject(server_id="6", type="Subsystem")
		print(dmobj.is_valid())

	"""


	names_values: object = None
	"""
	A dictionary with DM Properties that completely defines the Object.
	It needs the Object type as well.

	"""

	type: str = None
	"""
	The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase). Required when creating an Object with
	specified "names_values".

	"""

	server_id: str = None
	"""
	The Object's server id, its unique id in DM.
	If the value is empty, should the script ask for it, the DM will be queried for the 
	"names_values" and retrieve the value.

	"""

	ghost_id: str = None
	"""
	When an Object is partially deleted, the server_id is None
	and the ghost_id has the Id.
	The ghost_id can be used to create a new DMObject and get
	conflict options for saving it in DM.
	When the Object doesn't exist, both the server_id and 
	ghost_id are None.
	When the Object exists, the ghost_id will be equal to
	the server_id.

	"""

	@classmethod
	def export(cls, output_directory: str, export_type: str, child_server_id: str, hierarchy: str, action: str, export_contents: bool) -> str:

		"""

		Download the Object's Representation File or hierarchy to a XML file.


		Parameters
		----------
		output_directory : str
			Specify where the file/files will be downloaded.

		export_type : str, optional
			Accepted values: "hierarchy", "sub_hierarchy", blank.
			When this argument is omitted, the Representation File(s) 
			will be exported.
			When the argument is "hierarchy", an XML file with the Object's 
			hierarchy will be exported.
			When the argument is "sub_hierarchy", an XML file with 
			a subhierarchy will be exported.
			It is used along with the "child_server_id" and "hierarchy" 
			arguments.

		child_server_id : str, optional
			The child server id whose subhierarchy will be exported.
			It is used along with the 'hierarchy' argument.

		hierarchy : str, optional
			The "Hierarchy" value for the child whose subhierarchy will be 
			exported. It is used along with the 'child_server_id' argument.

		action : str, optional
			The exported file from the server will be copied to the target directory by default.
			It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
			Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items.

		export_contents : bool, optional
			Define whether the DM item's contents will be included while exporting. The default value is retrieved from the "dm_export_include_contents" keyword in ANSA Settings (by default it is set True).

		Returns
		-------
		str
			The resulting directory is returned on success.

		"""


	@classmethod
	def remove(cls, only_representation_file: str) -> int:

		"""

		Delete the Object from DM.


		Parameters
		----------
		only_representation_file : str, optional
			Use "YES" when only the Representation File should be 
			deleted and the Object should be kept in the database.

		Returns
		-------
		int
			1 if the function was successful.0 for failure.

		"""


	@classmethod
	def set_attribute_values(cls, attributes_values: object, attributes_types: object) -> bool:

		"""

		This function can change Attribute values for the Object.


		Parameters
		----------
		attributes_values : object
			A dictionary which specifies the Attributes to change, 
			in a names-values format.

		attributes_types : object, optional
			A dictionary mapping attribute names to types. This
			information will be used in case new attributes will be
			created and the DM supports typed attributes.

		Returns
		-------
		bool
			True : If the at least one values was set successfully.False: If the function failed to set any value.

		"""


	@classmethod
	def get_attribute_values(cls, attributes: object) -> object:

		"""

		This function can return some specified Attribute values of a Object.


		Parameters
		----------
		attributes : object, optional
			A list in which the user can specify Attribute names, 
			for their values to be returned. If this arguments is not 
			present, all the object's values will be returned.

		Returns
		-------
		object
			If the object was found, a dictionary will be returned with the specified attribute values.If the function fails, "None" will be returned.

		"""


	@classmethod
	def get_all_values(cls) -> object:

		"""

		This function will return all the Properties and Attributes for the Object in the form of a dictionary.


		Returns
		-------
		object
			A list with a dictionary for the Object that is actually found in DM.

		"""


	@classmethod
	def connect(cls, references: object) -> bool:

		"""

		This function connects DM Objects, by referencing. After its execution,the Object will reference the Objects specified in the "references" dict.Remarks:The "reference_type" values specified in the "references" dict can be any arbitrary string. However, when using SPDRM v1.4.0 or later as the data management backbone, certain values are reserved and can be used only when the conditions below are satisfied:-- adaptation      : Input/Output dependency link between a Loadcase Template (RLI) and a Loadcase (DM Item).-- creation        : Input/Output dependency link between a Session and a Report.-- repr_derivation : Lifecycle generic link between DM Items with identical properties, apart from the File Type (e.g ANSA and NASTRAN). At least one should have File Type = ANSA.                     Moreover, the following values are reserved for system generated links and should not be used as "reference_type":-- history         : System lifecycle link for DM Items of same type with different versioning properties and identical non-versioning ones.-- changeset       : System link between a changeset and a DM Item when saving a changeset from ANSA


		Parameters
		----------
		references : object
			A dictionary which holds server_id->reference-type pairs.
			Please see the REMARKS section for more information on the "reference_type" accepted values.

		Returns
		-------
		bool
			True : If the new references were made successfully.False: If the function failed to make one of the connections.

		"""


	@classmethod
	def add_new(cls, overwrite: bool, link: bool, get_repr_file_siblings: bool, filename: str, spin_up_attribute: str) -> object:

		"""

		This function adds an Object to DM, if it does not already exist.


		Parameters
		----------
		overwrite : bool, optional
			Set to True if the object should be overwritten if it
			already exists in the DM. (Default: False)

		link : bool, optional
			Set to True if you wish create a link to the file that 
			corresponds to the object. (Default: False)

		get_repr_file_siblings : bool, optional
			Set to True if you wish to copy along all files that exist
			in the same directory as the representation file.
			Applicable for Subsystems, Simulation Models, Load 
			Cases and Simulation Runs, when a non-ANSA file
			is set as representation file.
			(Default: False)

		filename : str, optional
			When the data model doesn't specify a "File" Property/Attribute for the Object, a Representation File can be added using this argument.
			For example, when adding a Subsystem to a Filebased DM, the file will be stored in DM by adding a filename to this method.

		spin_up_attribute : str, optional
			The primary attribute to spin-up. The 'overwrite' attribute should be set to False. By default, the 'spin_up_attribute' is not specified and the 'overwrite' = False, which means that the process will be skipped if the object already exists in DM.

		Returns
		-------
		object
			None: If an error occured.server_id string: If the object was successfully saved.

		"""


	@classmethod
	def get_representation_file(cls) -> str:

		"""

		This function will return the absolute file path to the DMObject's Representation File. In case of a server-based DM, e.g. SPDRM, SimManager,the file will be downloaded locally, to a temporary location, only the first time it is asked for. All following calls to the function will return the same file path, so long as the DMObject isn't updated. The temporary files deletion is handled automatically.


		Returns
		-------
		str
			If the Representation File exists and is successfully found, it's absolute file path will be returned.Otherwise, "None" will be returned.

		"""


	@classmethod
	def get_conflict_options(cls) -> object:

		"""

		When trying to upload an object to DM, one can get the conflict options when the object already exists in DM.


		Returns
		-------
		object
			Returns a list with the available conflict options, only if the object already exists in DM.Otherwise, it returns None.

		"""


	def get_contained_objects(self, type: str) -> object:

		"""

		This function will query DM and collect all Objects of the specified type contained under this DM Object.


		Parameters
		----------
		type : str
			The type of the DM Object that will be queried for. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

		Returns
		-------
		object
			Return a list of DMObject objects.

		"""


	def set_contents(self, server_ids: object) -> bool:

		"""

		This function sets the contents of the object (e.g. the Subsytems belonging to a Simulation Model).


		Parameters
		----------
		server_ids : object
			The server ids identifying the objects to be set as contents.

		Returns
		-------
		bool
			True : If the object contents were set successfully. False : If the object contents couldn't be set.

		"""


	def get_contents(self) -> object:

		"""

		Get the list of objects that are contents of the object


		Returns
		-------
		object
			Returns the server ids of the object contents

		"""


	def get_references(self, returned_ents: int=0, find_sim_runs_through_contents: bool=False) -> object:

		"""

		Get the objects which:- use this DM Object,- are used by this DM Object,- use and are used by this DM Object.


		Parameters
		----------
		returned_ents : int, optional
			define the requested objects:
			0 to get the objects which use this DM Object,
			1 to get the objects which are used by this DM Object,
			2 to get the objects which use and are used by this DM Object.
			By default, the objects, which use this DM Object, are returned.

		find_sim_runs_through_contents : bool, optional
			When True, if the DM Object is a Simulation Run,
			search for references of history type based 
			on the contained Simulation Model and Loadcase.

		Returns
		-------
		object
			Returns a list with the requested objects.

		"""


	@classmethod
	def get_type(cls) -> str:

		"""

		Use this method to query DM for the DMObject's type.


		Returns
		-------
		str

		"""


	@classmethod
	def download_attachment(cls, output_folder: str, folder_name: str, subfolder_name: str, filename: str, attribute_name: str, action: str) -> str:

		"""

		Downloads an attached file/folder of the DMObject.


		Parameters
		----------
		output_folder : str
			the full path of the folder where the attachment will be downloaded.

		folder_name : str, optional
			the name of the folder which contains the attachment.

		subfolder_name : str, optional
			the name of the sub-folder to be downloaded.

		filename : str, optional
			the name of the file to be downloaded.

		attribute_name : str, optional
			the name of attribute which contains the attachment.

		action : str, optional
			The exported file from the server will be copied to the target directory by default.
			It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
			Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items.

		Returns
		-------
		str
			Returns the full path of the downloaded attachment on success and None on failure.

		"""


	@classmethod
	def get_attachment_values(cls) -> object:

		"""

		In case of Filebased DMs, this function returns absolute paths for attachments that aren't declared in the data model and will not be returned by dm.DMObject.get_all_values. In case of SPDRM, this function may return absolute or relative paths for these attachments, depending on SPDRM configuration.


		Returns
		-------
		object
			Returns a dictionary with the attribute name as the key and the absolute file path as the value.

		"""


	@classmethod
	def is_valid(cls) -> bool:

		"""

		Use this method to check if the DMObject initialized with a server_id is actually valid and existing in DM.


		Returns
		-------
		bool

		"""

class DMReference():

	"""

	DM objects can refer to other objects within the same DM. Such relationships are
	described by 3 data fields:
	* DM Object that is doing the referring, i.e. is using another object
	* DM Object that is being referred to, i.e. is being used by another object
	* Reference type
	
	Instances of the DMReference class encapsulate all information needed to 
	describe such a reference between DM Objects.
	
	Based on the reference type, references can be classified as strong / weak:
	Objects cannot be deleted if there are any outstanding strong references
	pointing to them. Weak references on the other hand do not obstruct the deletion
	of the referred-to objects.
	
	Even though the reference type can be any arbitrary string, there are predefined
	reference types accomodating standard use cases. The predefined reference types
	are:
	* adaptation
	  Used for adapted DM objects to point to their standalone counterparts (e.g.
	  LoadCases) (strong)
	* creation
	  Used for DM objects to point to the DM object that triggered their creation
	  (e.g. Reports pointing to the META Session) (strong)
	* history
	  Used to show how objects have evolved over time and track their origins:
	  recent objects point to their immediate ancestors (weak)
	* repr_derivation
	  Used for automatically saved FE representation objects to point to the
	  original ANSA representation objects (weak)
	* changeset
	  Used for connecting an object in the DM, with the changeset that ordered its
	  creation (strong)
	* training
	  Used to show how data were used in ML training sessions: the generated 
	  predictor object points to the Simulation Run objects used during training
	  (weak)
	* modular_environment_profile
	  Used to show what configuration was used during the save of an object (strong)
	* strong
	  Generic strong reference. Recommended for user created references
	* weak
	  Generic weak reference. Recommended for user created references

	See Also
	--------
	dm.GetDMReferences, dm.RemoveDMReference

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Remove all manually added strong references
		    strong_refs = dm.GetDMReferences(ref_type="strong")
		    for ref in strong_refs:
		        print(
		            "Removing strong reference from {} to {}".format(
		                ref.server_id, ref.ref_server_id
		            )
		        )
		        dm.RemoveDMReference(ref)

	"""


	server_id: str = None
	"""
	Server ID of the object that is doing the referring,
	i.e. using the other object.

	"""

	ref_server_id: str = None
	"""
	Server ID of the object that is being referred to
	i.e. is being used by the other object.

	"""

	ref_type: str = None
	"""
	Field describing the type of the reference

	"""

	def __init__(self, server_id: str, ref_server_id: str, ref_type: str) -> object:

		"""

		DMReference object constructor, initializing all members


		Parameters
		----------
		server_id : str
			See respective member definition

		ref_server_id : str
			See respective member definition

		ref_type : str
			See respective member definition

		Returns
		-------
		object
			Returns the created DMReference object

		"""

class DMClusterMember():

	"""

	DMClusterMember objects describe a DM Cluster membership, providing information
	on which the backing DMs are and how they are employed within the cluster.

	See Also
	--------
	dm.AddClusterMember, dm.GetClusterMembers

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def getFlagsString(flags):
		    flags_strings = []
		
		    # Iterate through all defined flags even though all combinations are not
		    # possible, e.g. a member cannot be both Primary and Read Only.
		    if flags & dm.constants.PRIMARY_MEMBER:
		        flags_strings.append("Primary")
		    if flags & dm.constants.READ_ONLY_MEMBER:
		        flags_strings.append("Read Only")
		    return ", ".join(flags_strings)
		
		
		def main():
		    # A Cluster DM is configured as current DM Root
		    members = dm.GetClusterMembers()
		    for member in members:
		        print("Path      :", member.path)
		        print("Nickname  :", member.nickname)
		        print("Identifier:", member.identifier)
		        print("Flags     :", getFlagsString(member.flags))

	"""


	path: str = None
	"""
	DM Root of the DM that is backing this cluster member.

	"""

	nickname: str = None
	"""
	String that will be used to tag DM Object fields (e.g.
	Server IDs, Paths) in order to identify the contributing
	member.
	Can contain latin letters, digits, the underscore and dash
	characters.

	"""

	identifier: str = None
	"""
	String that is fetched from the member DM the first time
	it is admitted into the cluster. Used to validate
	subsequent insertions of the DM into the cluster.

	"""

	flags: int = None
	"""
	Bitfield describing properties of the cluster member. The
	supported flags are defined as constants:
	* dm.PRIMARY_MEMBER
	  This member is the primary one for the cluster (i.e.
	  used for both reading / writing)
	* dm.READ_ONLY_MEMBER
	  This member is used only for reading

	"""

	def __init__(self, path: str, nickname: str, identifier: str, flags: int) -> object:

		"""

		DMClusterMember object constructor, initializing all members


		Parameters
		----------
		path : str
			See respective member definition

		nickname : str
			See respective member definition

		identifier : str
			See respective member definition

		flags : int
			See respective member definition

		Returns
		-------
		object
			Returns the created DMClusterMember object

		"""

def QueryForAllResults(type: str) -> object:

	"""

	Get the attributes of all the items of a specific type in DM.

	Parameters
	----------
	type : str
		is the type of the DM item.

	Returns
	-------
	object
		Return a list with dictionaries. One dictionary with all the attributes for each
		DM item.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import dm
		
		
		def main():
		    type = "parts"
		    all_parts = dm.QueryForAllResults(type)
		    if all_parts:
		        for part_info in all_parts:
		            for key in part_info.keys():
		                print("attribute::", key, "value::", part_info[key])
		
		
		if __name__ == "__main__":
		    main()


	"""

def OpenDMObjectsInNewTab(server_ids: object, type: str, view: str, dm_system: str, tab_name: str, expand_all: bool, open_in_viewer: bool, open_in_reports_table: bool):

	"""

	This function can be used to open one or more hierarchies of any DM Object type,
	in a new tab, in DM Browser.

	Parameters
	----------
	server_ids : object, optional
		A list with DM Object server ids.

	type : str, optional
		The type of the DM Object, as it is defined through the Data Model
		(e.g. Loadcase).

	view : str, optional
		The new Tab's view, e.g. "Default", "Flat" or a user defined in the
		dm_views.xml. When undefined, the function will return False.

	dm_system : str, optional
		The DM root that will be queried.

	tab_name : str, optional
		The new tab will be given this name.

	expand_all : bool, optional
		If set to True, all items in the new tab will be expanded.

	open_in_viewer : bool, optional
		If set to True, all items in the new tab will be loaded to the meta viewer.

	open_in_reports_table : bool, optional
		If set to True, Reports Table will also be launched for all  the items in the
		new tab that is opened. In case the requested Type is not supported in
		Reports Table (SimulationModel, LoadCase, SimulationRun) or no Reports
		are found in DM for the requested server_ids, the scipt function will just 
		open the server_ids in a new tab and no Reports Table tabs will be opened.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    server_ids = ["689861"]
		    view = "Flat"
		    type = "Run"
		    ret = dm.OpenDMObjectsInNewTab(server_ids, view, type, open_in_reports_table=True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def QueryDMObjects(query: object, type: str, free_text_targets: object) -> dict:

	"""

	Search in DM for objects which satisfy the specified query.

	Parameters
	----------
	query : object
		The query can be expressed in one of the following forms:
		* A list of [<attribute_name>, <condition>, <value>] lists which
		  specify the query. For Attributes of Versioning Scheme Counter
		  type (e.g. Team Version, Study Version, etc.) the "Latest"
		  keyword is supported as follows:
		  [<versioning_attribute_name>, "equals", "Latest"]
		* A BetaQL string
		* A "free text" query string

	type : str, optional
		The type of the DM Object. The specified type can be ANSA type
		(e.g. ANSA_LOADCASE) or the DM type defined through the Data
		Model (e.g. Loadcase).

	free_text_targets : object, optional
		A list of the targets used in free text search queries 
		(e.g. ["All"] or ["Simulation_Run", "Report"])

	Returns
	-------
	dict
		Returns a dictionary with the following keys and values:
		key = 'error'
		value = 0(Success), 1(Nothing found), 2(No DM Root was set), 3(No access to DM Root),
		        4(Error in filters)
		key = 'output'
		value = A list with the DM objects which satisfy the query.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    type = "ANSA_SUBSYSTEM"
		    query = [["Project", "contains", "XX"], ["Representation", "equals", "NVH"]]
		    results = dm.QueryDMObjects(query, type)
		    if results["error"] == 0:
		        for dm_object in results["output"]:
		            print("DM Object Id : ", dm_object.server_id)
		
		            # Equivalent query to the previous one, this time expressed as a BetaQL string
		    query = "Project contains XX and Representation = NVH"
		    results = dm.QueryDMObjects(query, type)
		    if results["error"] == 0:
		        for dm_object in results["output"]:
		            print("DM Object Id : ", dm_object.server_id)
		
		            # Free text query
		    free_text_query = "models with project venza"
		    targets_list = ["All"]
		    results = dm.QueryDMObjects(query=free_text_query, free_text_targets=targets_list)
		    if results["error"] == 0:
		        for dm_object in results["output"]:
		            print("DM Object Id : ", dm_object.server_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetConnectedUserRole() -> str:

	"""

	Get the current role of the user who is connected to SPDRM-based DM root.

	Returns
	-------
	str
		Returns the User Role.
		None is returned in case of error (e.g. the user is not connected to DM root).

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm_root = "http://spdrm:8080/"
		    username = "analyst_01"
		    password = "analyst_01"
		    role = "Analyst"
		    ret = dm.SetRoot(dm_root, username, password, role)
		    print(ret)
		    print("The current role of the connected user is ", dm.GetConnectedUserRole())
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetUserRoles(dm_root: str, username: str, password: str) -> object:

	"""

	Get the available roles of a user in an SPDRM-based DM root.

	Parameters
	----------
	dm_root : str
		The url of the SPDRM-based DM root.

	username : str
		The username of the user.

	password : str
		The password of the user.

	Returns
	-------
	object
		Returns a list with the available user roles.
		None is returned in case of error.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dm_root = "http://spdrm:40080"
		    username = "user_01"
		    password = "user_01"
		    user_roles = dm.GetUserRoles(dm_root, username, password)
		    if user_roles:
		        print("The available roles are:")
		        for role in user_roles:
		            print(role)
		
		
		if __name__ == "__main__":
		    main()


	"""

def RefreshContents() -> None:

	"""

	Refresh the side panel in DM Browser or KOMVOS,
	equivalent to the right click action "Refresh".

	Returns
	-------
	None

	Examples
	--------
	::

		import meta
		from meta import dm
		
		dm.RefreshContents()


	"""

class DMFilter():

	"""

	A DMFilter object represents a query in DM for DM Objects of a specified type that fulfill a condition. 
	The execution of a DM Filter results a list of DM Objects.

	See Also
	--------
	dm.GetDMFilters

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    # Create
		    filter = dm.DMFilter(name="MyFilter", object_type="Subsystems")
		
		    # Edit
		    filter.name = "FirstIteration"
		    filter.expression = "Iteration=001"
		
		    # Save in DM
		    filter.save()
		
		    # Execute
		    res = filter.exec()
		
		    # Delete
		    filter.delete()
		
		    # Check existence in DM##
		    filter.exists()

	"""


	id: int = None
	"""
	Id of the filter. (Read only)

	"""

	name: str = None
	"""
	Name of the filter.

	"""

	user: str = None
	"""
	The user that created the filter. (Read only)

	"""

	object_type: str = None
	"""
	The type of the DM Objects to be queried.

	"""

	secondary_type: str = None
	"""
	The secondary type of the DM Objects to be queried.

	"""

	expression: str = None
	"""
	The condition expression the query must fulfill.

	"""

	description: str = None
	"""
	The user-specified description over the filter.

	"""

	mode: int = None
	"""
	DM FIlter's mode.
	  - Basic
	  - Advanced (default)

	"""

	syntax: int = None
	"""
	DM FIlter's syntax.
	  - BetaQL
	  - FreeText (default)

	"""

	access: int = None
	"""
	DM Filter's access from users.
	  - Private (default)
	  - ViewOnly
	  - ViewAndEdit

	"""

	creation_date: datetime = None
	"""
	DM Filter's creation datetime. (Read only)

	"""

	modification_date: datetime = None
	"""
	DM Filter's modification datetime. (Read only)

	"""

	last_edit_user: str = None
	"""
	The last user who edited the DM Filter. (Read only)

	"""

	def __init__(self, name: str, object_type: str, secondary_type: str) -> object:

		"""

		DMFilter object constructor, initializing all members


		Parameters
		----------
		name : str
			See respective member definition

		object_type : str
			See respective member definition

		secondary_type : str, optional
			See respective member definition

		Returns
		-------
		object
			Returns the created DMFilter object

		"""

def GetDMFilters(owned_only: bool=False) -> list:

	"""

	This function queries the DM for either all non-private filters or only those that are created by the user.

	Parameters
	----------
	owned_only : bool, optional
		If True, get only the DM Filters that are created by the user.

	Returns
	-------
	list
		Returns the list of DMFilter items that satisfy the provided expression.

	See Also
	--------
	dm.DMFilter

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def getOwnedOnlyDMFilters():
		    dm_filters_list = dm.GetDMFilters(owned_only=True)
		    for dm_filter in dm_filters_list:
		        print(dm_filter)


	"""

def CreateTempFolder(folder_name: str) -> str:

	"""

	The function creates a temporary folder in the user temp directory. 
	The folder is deleted upon program exit.

	Parameters
	----------
	folder_name : str
		A secondary folder to be created nested inside the temporary folder.

	Returns
	-------
	str
		Returns the path to the created folder on success, or an exception on error.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    first_temp_folder = dm.CreateTempFolder()
		    second_temp_folder = dm.CreateTempFolder("my_second_test_dir")
		
		    print("First temp folder is: " + first_temp_folder)
		    print("Second temp folder is: " + second_temp_folder)
		
		
		if __name__ == "__main__":
		    main()


	"""

