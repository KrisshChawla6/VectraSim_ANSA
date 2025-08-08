from __future__ import annotations
from typing import *
from . import utils

def GetDMRoot() -> str:

	"""

	Returns the path that currently points to DM.

	Returns
	-------
	str
		The function returns a string containing the current DM root.
		A string of length 0 is returned if no DM path is currently set.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    dm_root = base.GetDMRoot()
		    print(dm_root)


	"""

def SetDMRoot(dm_root: str, username: str, password: str, role: str) -> int:

	"""

	Sets the current DM root to the path DM_PATH.

	Parameters
	----------
	dm_root : str
		A string that describes the path of the DM root directory.

	username : str, optional
		Username (For login in the SPDRM vault).

	password : str, optional
		Password (For login in the SPDRM vault).

	role : str, optional
		User role (For setting the user's role to SPDRM).

	Returns
	-------
	int
		Returns 1 if the new DM root has been set successfully and 0 otherwise.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		# Ex.1
		def main():
		    base.SetDMRoot("C:/Users/Local_Work_files/")
		
		
		# Ex.2: Set SPDRM vault as DM Root
		def main():
		    base.SetDMRoot(
		        "http://magneto.localdomain:8080/", username="user1", password="pass1"
		    )
		    # when we want to change the user's role(when supported):
		    base.SetDMRoot(
		        "http://magneto.localdomain:8080/",
		        username="user1",
		        password="pass1",
		        role="Administrator",
		    )


	"""

def IsDMRootConnectionValid(dm_root: str, reconnect: bool) -> int:

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
		from meta import base
		
		
		def main():
		    if base.IsDMRootConnectionValid():
		        print("Connection to current DM is valid.")
		    else:
		        print("Connection to current DM is lost.")
		    # OR:
		    if base.IsDMRootConnectionValid(dm_root="http://ektoras:8080/"):
		        print("Connection to http://ektoras:8080/ is valid.")
		    else:
		        print("Connection to http://ektoras:8080/ is lost.")


	"""

def RemoveDMRoot(dm_root: str) -> int:

	"""
	.. deprecated:: 17.0.0
		Use :py:func:`RemoveRoot` instead.


	Removes the specified DM path or url from the "Set DM Paths" window list.

	Parameters
	----------
	dm_root : str
		The path to the DM to remove.

	Returns
	-------
	int
		Returns 1 if the specified DM root has been removed successfully and 0 otherwise.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    base.RemoveDMRoot("C:/Users/Local_Work_files/")


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:func: RemoveRoot instead.", DeprecationWarning)

def GetDMRootsList() -> object:

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

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    print(base.GetDMRootsList())


	"""

def AddDMObject(type: str, names_values: object, overwrite: bool, link: bool) -> str:

	"""
	.. deprecated:: 19.0.0
		Use `DMObject.add_new` instead.


	This function adds an object to the DM, if it does not already exist.

	Parameters
	----------
	type : str
		The type of the object to be added.

	names_values : object
		A dictionary which holds the object's property and attribute values.

	overwrite : bool, optional
		Set to True if the object should be overwritten, if it already exists in the DM.

	link : bool, optional
		Set to True if you wish create a link to the file that corresponds to the object.

	Returns
	-------
	str
		Returns the server id, as a string, on success, or None on failure.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    # Adds a component to the DM
		
		    # All properties MUST be present in the object's names_values dictionaries
		    names_values = {}
		    names_values["Module Id"] = "Module1"
		    names_values["Version"] = "Version1"
		    names_values["Study Version"] = "Study1"
		    names_values["Representation"] = "Representation1"
		    names_values["Name"] = "Name1"  # Attribute
		
		    component_server_id = base.AddDMObject("Component", names_values)
		
		    if component_server_id:
		        print("Component server_id: " + component_server_id)
		    else:
		        print("AddDMObject failed.")


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use  DMObject.add_new instead.", DeprecationWarning)

def GetDMObjectAttributeValues(type: str, names_values: object, server_id: str, attributes: object) -> object:

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	This function can return some specified Attribute values of a dm object. The 
	object can be identified by either its server is, or its property values.

	Parameters
	----------
	type : str
		The type of the object (required, if the names_values argument is present).

	names_values : object, optional
		A dictionary which holds the object's property values 
		(all property values must be present for the object's identification).

	server_id : str, optional
		The server id of the object, if it is already known.
		If present, the type and names_values arguments can be omitted.

	attributes : object, optional
		A list in which the user can specify Attribute names, for their values to be returned.
		If this arguments is not present, all the object's values will be returned.

	Returns
	-------
	object
		If the object was found, a dictionary will be returned with the specified attribute values. 
		If the function fails, "None" will be returned.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    property_values = {}
		    property_values["Name"] = "MyName"
		    property_values["Version"] = "A"
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", names_values=property_values, attributes=["SM_Attr"]
		        )
		    )
		
		    # if the server id of this simulation model was already known to be "5472", the function could be called like this:
		    print(base.GetDMObjectAttributeValues("Simulation_Model", server_id="5472"))
		    # or if we are just looking for a specific Attribtue:
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", server_id="5472", attributes=["Last_Edit"]
		        )
		    )


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def SetDMObjectAttributeValues(type: str, names_values: dict, server_id: str, attribute_names_values: dict, attribute_names_types: dict) -> bool:

	"""
	.. deprecated:: 19.0.0
		Use :py:class:`DMObject` instead.


	This function can change Attribute values for a dm object. If an Attribute
	doesn't exist, then this function can also trigger its creation.
	The object can be identified by either its server id, or its property values.

	Parameters
	----------
	type : str
		The type of the object (required, if the names_values argument is present).

	names_values : dict, optional
		A dictionary which holds the object's property values
		(all property values must be present for the object's identification).

	server_id : str, optional
		The server id of the object, if it is already known.
		If present, the type and names_values arguments can be omitted.

	attribute_names_values : dict, optional
		A dictionary which specifies the Attributes to change, in a names-values format.

	attribute_names_types : dict, optional
		A dictionary mapping Attribute names to types. This information will be used
		in case new Attributes will be created and the DM supports typed Attributes.

	Returns
	-------
	bool
		True : If the at least one values was set successfully.
		False: If the function failed to set any value.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    all_values = {}
		    all_values["Name"] = "MyName"
		    all_values["Version"] = "A"
		    all_values["SM_Attr"] = "SM_Attr_Value"  # Attribute
		    base.AddDMObject("Simulation_Model", all_values)
		
		    property_values = {}
		    property_values["Name"] = "MyName"
		    property_values["Version"] = "A"
		
		    base.SetDMObjectAttributeValues(
		        "Simulation_Model",
		        names_values=property_values,
		        attribute_names_values={"SM_Attr": "New_Val"},
		    )
		    # if the server id of this simulation model was already known to be "1", the function could be called like this:
		    # base.GetDMObjectAttributeValues("Simulation_Model", ref_server_id="1", attribute_names_values={"SM_Attr":"New_Val"})
		
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", names_values=property_values, attributes=["SM_Attr"]
		        )
		    )


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def ConnectDMObjectToDMObjects(server_id: str, references: object) -> bool:

	"""

	This function connects dm objects, by referencing. After its execution, 
	the object whose server_id is given as argument, will reference
	the objects specified in the "references" dict.

	Parameters
	----------
	server_id : str
		If the server id of the first object is known, the type and names_values arguments can be ommited.

	references : object
		A dictionary which holds server_id->reference-type pairs.

	Returns
	-------
	bool
		True:  If the new references were made successfully.
		False: If the function failed to make one of the connections.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    dict1 = {}
		    dict1["Name"] = "MyName"
		    dict1["Version"] = "A"
		    dict1["SM_Attr"] = "SM_Attr_Value"  # Attribute
		    sim_model_server_id = base.AddDMObject("Simulation_Model", dict1)
		
		    dict2 = {}
		    dict2["Module Id"] = "Module1"
		    dict2["Version"] = "Version1"
		    dict2["Study Version"] = "Study1"
		    dict2["Representation"] = "Representation1"
		    dict2["Variant"] = "Variant1"
		    dict2["Name"] = "Name1"  # Attribute
		    comp_server_id = base.AddDMObject("Component", dict2)
		
		    print(
		        base.ConnectDMObjectToDMObjects(
		            sim_model_server_id, {comp_server_id: "my_component"}
		        )
		    )


	"""

def GetComponentsAllValues(server_id: str, server_ids: object, type: str) -> object:

	"""
	.. deprecated:: 16.2.0
		Use :py:func:`GetDMObjectAllValues` instead.


	Deprecated: use meta.base.GetDMObjectAllValues instead!!
	
	When connected to a DM, this function returns all the Properties and Attributes 
	for a DM Object in the form of a dictionary.

	Parameters
	----------
	server_id : str, optional
		The DM Object's server id.

	server_ids : object, optional
		A list with DM Object server ids.

	type : str, optional
		If the DM Object's type is known, use this argument to define it.
		Otherwise, the function will try to find the type itself.

	Returns
	-------
	object
		A list with dictionaries for each DM Object that is actually found in DM.

	See Also
	--------
	base.GetDMObjectAllValues

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    list_of_names_values = base.GetComponentsAllValues(
		        server_id="294", type="Subsystem"
		    )
		    for names_values in list_of_names_values:
		        print(names_values)
		    list_of_server_ids = []
		    list_of_server_ids.append("56875")
		    list_of_server_ids.append("56867")
		    list_of_names_values = base.GetComponentsAllValues(server_ids=list_of_server_ids)
		    for names_values in list_of_names_values:
		        print(names_values)


	"""

	import warnings; warnings.warn("Deprecated since version 16.2.0. Use :py:func: GetDMObjectAllValues instead.", DeprecationWarning)

def GetDMObjectAllValues(server_id: str, server_ids: object, type: str) -> object:

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	When connected to a DM, this function returns all the Properties and Attributes 
	for a DM Object in the form of a dictionary.

	Parameters
	----------
	server_id : str, optional
		The DM Object's server id.

	server_ids : object, optional
		A list with DM Object server ids.

	type : str, optional
		If the DM Object's type is known, use this argument to define it.
		Otherwise, the function will try to find the type itself.

	Returns
	-------
	object
		A list with dictionaries for each DM Object that is actually found in DM.

	See Also
	--------
	base.GetAllAttrsFromUniqueRepresentations

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    list_of_names_values = base.GetDMObjectAllValues(server_id="294", type="Subsystem")
		    for names_values in list_of_names_values:
		        print(names_values)
		    list_of_server_ids = []
		    list_of_server_ids.append("56875")
		    list_of_server_ids.append("56867")
		    list_of_names_values = base.GetDMObjectAllValues(server_ids=list_of_server_ids)
		    for names_values in list_of_names_values:
		        print(names_values)


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def GetAvailableLibraryItemsInDM(folder_name: str, search_for: str) -> object:

	"""
	.. deprecated:: 17.0.0
		Use :py:func:`GetAvailableLibraryItems` instead.


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
		from meta import base
		
		
		def main():
		    results = base.GetAvailableLibraryItemsInDM(
		        "batch_mesh_sessions", search_for="*.ansa"
		    )
		    if results:
		        for result in results:
		            print("Found batch_mesh_session: ", result)
		    all_results = base.GetAvailableLibraryItemsInDM("batch_mesh_sessions")
		    if all_results:
		        for result in all_results:
		            print("Found batch_mesh_session: ", result)


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:func: GetAvailableLibraryItems instead.", DeprecationWarning)

def GetDMObjectId(type: str, names_values: object) -> str:

	"""

	Search in DM for a DM Object with specific properties and return its server id.
	The specified properties should describe a unique DM Object. If none or more than
	one DM Object are defined from the specified properties, None is returned.

	Parameters
	----------
	type : str
		the type of the DM Object as it is defined in the dm_structure.xml
		(e.g. 'parts', includes', 'Subsystem', etc.).

	names_values : object
		a {'Property':'Value'} dictionary which describes a unique DM Object.

	Returns
	-------
	str
		Returns the server id of the DM Object on success and None on failure.

	See Also
	--------
	ExportDMObjectHierarchy, ExportDMObject, DeleteDMObject, SetDMObjectAttributeValues, GetDMObjectAttributeValues, ConnectDMObjectToDMObjects, dm.CheckForUpdates

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Module Id": "100", "Version": "0", "Representation": "common"}
		    ret = base.GetDMObjectId("parts", vals)
		    if ret:
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeValueString(names_values: object, type: str, server_id: str, attribute_name: str, attribute_value: str) -> bool:

	"""

	This function can be used to set an attribute value to a DM Object.

	Parameters
	----------
	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	attribute_name : str, optional
		The Attribute's name.
		Although it's an optional argument, it needs to be defined.

	attribute_value : str, optional
		The value that will be set to the Attribute.
		Although it's an optional argument, it needs to be defined.

	Returns
	-------
	bool

	See Also
	--------
	ExportDMObjectHierarchy, ExportDMObject, DeleteDMObject, GetDMObjectId, SetDMObjectAttributeValues, GetDMObjectAttributeValues, ConnectDMObjectToDMObjects

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("parts", vals)
		    if ret:
		        base.SetAttributeValueString(
		            server_id=ret, type="parts", attribute_name="Big_part", attribute_value="NO"
		        )


	"""

def ExportDMObjectHierarchy(output_directory: str, names_values: object, type: str, server_id: str) -> str:

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	When a DM Object can be defined by a DM Object hierarchy, e.g. a Subsystem,
	use this function to download the hierarchy and afterwards read it into ANSA.

	Parameters
	----------
	output_directory : str
		Specifies where the xml will be downloaded.

	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when the 
		names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	Returns
	-------
	str
		Returns the resulting directory on success.

	See Also
	--------
	ExportDMObject, DeleteDMObject, GetDMObjectId

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = meta.base.GetDMObjectId("parts", vals)
		    print(ret)
		    if ret:
		        base.ExportDMObjectHierarchy("C:/home/demo/tmp", server_id=ret)


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def ExportDMObject(output_directory: str, names_values: object, type: str, server_id: str, action: str) -> str:

	"""

	This function can be used to download a DM Object's Representation File from DM.

	Parameters
	----------
	output_directory : str
		Specify where the file/files will be downloaded.

	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when 
		the names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	action : str, optional
		The exported file from the server will be copied to the target directory by default.
		It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
		Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items and Library Files.

	Returns
	-------
	str
		Returns the resulting directory on success.

	See Also
	--------
	ExportDMObjectHierarchy, DeleteDMObject, GetDMObjectId

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("parts", vals)
		    print(ret)
		    if ret:
		        base.ExportDMObject("C:/home/demo/tmp", server_id=ret)


	"""

def DeleteDMObject(names_values: object, type: str, server_id: str, only_representation_file: str) -> int:

	"""
	.. deprecated:: 19.0.0
		Use :py:class:`DMObject` instead.


	Deletes an Object from DM using this function.

	Parameters
	----------
	names_values : object, optional
		A dictionary defining the DM Object.
		When the server_id argument isn't given, the function will search 
		for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when the 
		names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	only_representation_file : str, optional
		Use "YES" when only the Representation File should be deleted and the 
		Object should be kept in the database.

	Returns
	-------
	int
		Returns 1 on success, 0 on failure.

	See Also
	--------
	ExportDMObject, ExportDMObjectHierarchy, GetDMObjectId

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("Subsystems", vals)
		    print(ret)
		    if ret:
		        base.DeleteDMObject(server_id=ret, type="Subsystems")


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def GetAllAttrsFromUniqueRepresentations(server_id: str, server_ids: object, type: str, values: object, ask_sdm: bool, object_id: str, object_ids: object) -> object:

	"""
	.. deprecated:: 17.0.0
		Use :py:func:`GetAttributesFromUniqueRepresentations` instead.


	This function will return all Properties/Attributes for a specific input, 
	either server ids, a filter or a DM Browser window item.

	Parameters
	----------
	server_id : str, optional
		The server id of the object, if it is already known.
		When specified, it will be used to query DM.

	server_ids : object, optional
		A list with server ids. When specified, it will be used to query DM.

	type : str, optional
		The type of the object (required, even though it's optional).

	values : object, optional
		A dictionary which holds a filter (names - values)
		that will be used when no server ids or object ids are defined.

	ask_sdm : bool, optional
		In case of SDM CONSOLE, we can query the already downloaded values
		instead of querying DM.
		It should be used in cases where the query is expected to be very slow.

	object_id : str, optional
		When this function is called through an action in DM Browser or SDM CONSOLE,
		object_id is the GUI item's id. It can be used when we don't know the server_id.

	object_ids : object, optional
		A list with object ids, as described above.

	Returns
	-------
	object
		Returns a list with dictionaries, with the specified attribute values. 
		If the function fails, the list will be empty.

	See Also
	--------
	GetDMObjectAllValues

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("parts", vals)
		    if ret:
		        list_of_dicts = base.GetAllAttrsFromUniqueRepresentations(
		            server_id=ret, type="parts"
		        )
		        len_of_list_of_dicts = len(list_of_dicts)
		        for each_dict in list_of_dicts:
		            print("Representation: ", each_dict["Representation"])


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:func: GetAttributesFromUniqueRepresentations instead.", DeprecationWarning)

def BCSettingsGetUserDefinedValue(keyword: str):

	"""

	Returns the string value of user defined keyword with name keyword
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsSetUserDefinedValue(keyword: str, value: str):

	"""

	Sets value value to user defined keyword keyword. 
	If keyword a\ keyword doesn't exist it will be created.
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup and set the new value.

	value : str
		the new string value of the keyword

	See Also
	--------
	BCSettingsGetUserDefinedValue

	"""

def BCSettingsUserDefinedKeywordExists(name: str):

	"""

	Checks if a user defined key with name name exists in BCSettingsHandler structure
	It will only search for a keyword not for a value.
	This function is not supported under VR mode.

	Parameters
	----------
	name : str
		the keyword's name to look up.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsReadFile(filePath: str) -> int:

	"""

	Reads a defaults file, from path filePath.
	
	Settings that will be read from the file, will be applied
	to the running application.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		The path of the defaults file.

	Returns
	-------
	int
		1 if reading was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteFile(filePath: str) -> int:

	"""

	Writes a defaults file, at path filePath. If a filePath is not given,
	\the defaults file will be written in .BETA folder according to which
	\layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If the file already exists, it will be overwritten.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str, optional
		the path where the defaults file will be written.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteGroup(filePath: str, groupName: str) -> int:

	"""

	Writes the settings of Group named groupName, at path filePath.
	\If filePath is empty, the group will be written in defaults file located in .BETA folder
	\according to which layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If file already exists, then the settings of the corresponding group will be updated.
	The rest of the file will remain intact.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		the path where the defaults file will be written.

	groupName : str
		the group name, to write.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteFile

	"""

def ExportDMObjectSubHierarchy():

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def BCSettingsGetDefaultValue(keyword: str):

	"""

	Returns the default value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	See Also
	--------
	BCSettingsGetStartupValue

	"""

def BCSettingsGetStartupValue(keyword: str):

	"""

	Returns the startup value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	See Also
	--------
	BCSettingsGetDefaultValue

	"""

def BCSettingsGetValues(fields: object) -> object:

	"""

	This function returns the values of any keyword supported by .defaults file(s).

	Parameters
	----------
	fields : object
		A tuple of keywords, supported by the .default file(s), whose values will be retrieved.

	Returns
	-------
	object
		On success it returns a dictionary where the keys are the .defaults keywords,
		provided as arguments, and the values are their current application values.
		On failure it returns None.
		NOTE: A value can be either a single string or a list of strings, if the keyword supports multiple instances, i.e. can be set more than once.

	Examples
	--------
	::

		import meta
		from meta import base
		
		ret = base.BCSettingsGetValues(
		    (
		        "Perimeter Corner Angle",
		        "BeforeCompareScriptFunctionName",
		        "free_generator",
		        "NAS_MAT_DBASE",
		        "CalcThickness_target_selection_mode",
		    )
		)
		print("Perimeter Corner Angle  is: ", ret["Perimeter Corner Angle"])


	"""

def BCSettingsSetValues(fields: object) -> int:

	"""

	This function changes values supported by the .defaults file(s) (settings).

	Parameters
	----------
	fields : object
		A dictionary with keys any valid keyword supported by the .defaults file(s) and values a single string or a list of string values.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		import meta
		from meta import base
		
		base.BCSettingsSetValues(
		    {
		        "Perimeter Corner Angle": "35.0",
		        "BeforeCompareScriptFunctionName": "testFunctionName",
		        "free_generator": "true, 1",
		        "NAS_MAT_DBASE": ["my_path1", "my_path2"],
		        "CalcThickness_target_selection_mode": "select_curves",
		    }
		)


	"""

def AddDOEStudy(names_values: object, design_variables: object, responses: object, experiments_object_ids: object) -> str:

	"""

	This function adds a DOE_Study object to the DM.

	Parameters
	----------
	names_values : object
		A dictionary which holds the object's property and attribute values.

	design_variables : object, optional
		A dictionary with key the experiment id and value another dictionary which holds the design variables as name-value pairs.

	responses : object, optional
		A dictionary with key the experiment id and value another dictionary which holds the responses as name-value pairs.

	experiments_object_ids : object, optional
		A dictionary which holds the experiments server ids in DM.

	Returns
	-------
	str
		Returns the server id, as a string, on success, or None on failure.

	Examples
	--------
	::

		import meta
		from meta import dm
		
		
		def main():
		    dvs = {"1": {"Thickness": "1.2"}, "2": {"Thickness": "1.3"}}
		    resps = {"1": {"Displacement": "2.5"}, "2": {"Displacement": "1.2"}}
		    attributes = {"Optimization Task Name": "My_task"}
		
		    server_id = dm.AddDOEStudy(
		        names_values=attributes, design_variables=dvs, responses=resps
		    )
		
		    if server_id:
		        print("DOE_Study server_id: " + server_id)
		    else:
		        print("AddDOEStudy failed.")


	"""

def CanvasList() -> object:

	"""

	Returns a list with all the Canvas objects.

	Returns
	-------
	object
		Returns a list with the Canvas names, or None if there are no Canvas objects.

	Examples
	--------
	::

		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		
		    color = 0xFF0000FF
		    canvas.set_color(color)
		
		    size = 10
		    canvas.point_size(size)
		
		    x = 0
		    y = 0
		    z = -1
		    canvas.point(x, y, z)
		
		    canvas.show()
		
		    names = base.CanvasList()
		    for name in names:
		        print(name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetMETAdefaultsValues(fields: object) -> object:

	"""

	This function returns the values of the given META defaults keywords.

	Parameters
	----------
	fields : object
		A list of META defaults keywords whose values will be retrieved.

	Returns
	-------
	object
		On success it returns a dictionary where the keys are the META defaults keywords
		provided as arguments and the values are their retrieved values stored in META.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    settings = ["identify_format"]
		    ret = base.GetMETAdefaultsValues(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetMETAdefaultsValues(fields: object) -> bool:

	"""

	This function changes the META defaults values.

	Parameters
	----------
	fields : object
		A dictionary with keys the META defaults keywords and values the new default values.

	Returns
	-------
	bool
		Returns True on success and False on failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    ret = base.SetMETAdefaultsValues({"identify_format": "Auto"})
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Canvas():

	"""

	A Canvas object allows you to draw primitives on the GL area.
	
	Available artifacts are:
	* point
	* line, stippled line
	* label
	* arrow
	* triangle, quad
	* sphere, cube and cylinder.
	
	Points and some arrows are not affected by the view's zoom.
	
	It is also possible to draw lines, triangles, cones and labels that will not be affected by the view's zoom.
	Those primitives are named as symbols. Before drawing a symbol the symbol_origin must be set. symbol_origin 
	is the point from which the scale will take place.
	
	The programmer may create Canvas and allow the control to return to ANSA. A Canvas cannot be modified.
	If the User performs a File>New action, all Canvas are deleted.

	See Also
	--------
	CanvasList

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		
		
		if __name__ == "__main__":
		    main()
		# method: arrow
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    start = (2, 0, 2)
		    end = (2, 1, 2)
		    canvas.arrow(start, end)
		    # canvas.arrow(start, end, line_width=2, size_of_tip=0.25, pos_of_tip=0.6, type=0)
		
		
		if __name__ == "__main__":
		    main()
		# method: cube
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    p1 = (3, 0, 4.5)
		    p2 = (4, 0, 4.5)
		    p3 = (4, 1, 4.5)
		    p4 = (3, 1, 4.5)
		    p5 = (3, 0, 5.5)
		    p6 = (4, 0, 5.5)
		    p7 = (4, 1, 5.5)
		    p8 = (3, 1, 5.5)
		    canvas.cube(p1, p2, p3, p4, p5, p6, p7, p8)
		    # canvas.cube(p1,p2,p3,p4,p5,p6,p7,p8, shade = False)
		
		
		if __name__ == "__main__":
		    main()
		# method: cylinder
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    origin = (1.5, 0, 5)
		    direction = (0, 1, 0)
		    radius = 0.5
		    height = 1
		    canvas.cylinder(origin, direction, radius, height)
		    canvas.cylinder(origin, direction, radius, height, shade=False)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    ret = canvas.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    ret = canvas.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: label
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    position = (8, 0, -1)
		    text = "Label"
		    font_size = 100
		    canvas.label(position, text, font_size)
		
		
		if __name__ == "__main__":
		    main()
		# method: line
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    start = (0, 0, 0)
		    end = (1, 0, 0)
		    canvas.line(start, end)
		
		
		if __name__ == "__main__":
		    main()
		# method: line_width
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    start = (0, 0, 0)
		    end = (1, 0, 0)
		    canvas.line(start, end)
		    width = 2
		    canvas.line_width(width)
		
		
		if __name__ == "__main__":
		    main()
		# method: point
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas("MyCanvas")
		    canvas.set_color(0xFF0000FF)
		    canvas.point_size(10)
		    canvas.point(0, 0, -1)
		    canvas.point(1, 0, -1, "square_hollow")
		    canvas.point(2, 0, -1, "circle")
		    canvas.point(3, 0, -1, "circle_hollow")
		    canvas.point(4, 0, -1, "diamond")
		    canvas.point(5, 0, -1, "diamond_hollow")
		    canvas.point(6, 0, -1, "hexa_hollow")
		    canvas.point(7, 0, -1, "cross")
		
		
		if __name__ == "__main__":
		    main()
		# method: point_size
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    size = 10
		    canvas.point_size(size)
		    x = 0
		    y = 0
		    z = -1
		    canvas.point(x, y, z)
		    x = 1
		    # canvas.point(x, y, z, 'square_hollow')
		    # canvas.point(x, y, z, 'circle')
		    # canvas.point(x, y, z, 'circle_hollow')
		    # canvas.point(x, y, z, 'diamond')
		    # canvas.point(x, y, z, 'diamond_hollow')
		    # canvas.point(x, y, z, 'hexa_hollow')
		    # canvas.point(x, y, z, 'cross')
		
		
		if __name__ == "__main__":
		    main()
		# method: quad
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    p1 = (2, 0, 7)
		    p2 = (3, 0, 7)
		    p3 = (3, 1, 7)
		    p4 = (2, 1, 7)
		    canvas.quad(p1, p2, p3, p4)
		    canvas.quad(p1, p2, p3, p4, shade=False)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    start = (0, 0, 0)
		    end = (1, 0, 0)
		    canvas.line(start, end)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    ret = canvas.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: sphere
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    center = (0, 0, 5)
		    radius = 0.5
		    canvas.sphere(center, radius)
		    canvas.sphere(center, radius, shade=False)
		
		
		if __name__ == "__main__":
		    main()
		# method: stippled_line
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    name = "MyCanvas"
		    canvas = base.Canvas(name)
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    start = (0, 0, 1)
		    end = (1, 0, 1)
		    canvas.stippled_line(start, end)
		
		
		if __name__ == "__main__":
		    main()
		# method: symbol_cone
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    x = 5
		    y = 0
		    z = 0
		    canvas.symbol_origin(x, y, z)
		    start = (9, 0, 1)
		    end = (10, 0, 1)
		    radius = 0.5
		    canvas.symbol_cone(start, end, radius)
		
		
		if __name__ == "__main__":
		    main()
		# method: symbol_label
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    x = 5
		    y = 0
		    z = 0
		    canvas.symbol_origin(x, y, z)
		    position = (5, 0, 0)
		    text = "Symbols"
		    canvas.symbol_label(position, text)
		
		
		if __name__ == "__main__":
		    main()
		# method: symbol_line
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    x = 5
		    y = 0
		    z = 0
		    canvas.symbol_origin(x, y, z)
		    start = (5, 0, 1)
		    end = (6, 0, 1)
		    canvas.symbol_line(start, end)
		
		
		if __name__ == "__main__":
		    main()
		# method: symbol_origin
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    x = 5
		    y = 0
		    z = 0
		    canvas.symbol_origin(x, y, z)
		    position = (5, 0, 0)
		    text = "Symbols"
		    canvas.symbol_label(position, text)
		
		
		if __name__ == "__main__":
		    main()
		# method: symbol_triangle
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    x = 5
		    y = 0
		    z = 0
		    canvas.symbol_origin(x, y, z)
		    p1 = (7, 0, 1)
		    p2 = (8, 0, 1)
		    p3 = (7.5, 0, 2)
		    canvas.symbol_triangle(p1, p2, p3)
		
		
		if __name__ == "__main__":
		    main()
		# method: triangle
		# PYTHON script
		import meta
		from meta import base
		
		
		def main():
		    canvas = base.Canvas(name="MyCanvas")
		    color = 0xFF0000FF
		    canvas.set_color(color)
		    p1 = (0, 0, 7)
		    p2 = (1, 0, 7)
		    p3 = (0.5, 1, 7)
		    canvas.triangle(p1, p2, p3)
		    canvas.triangle(p1, p2, p3, shade=False)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the Canvas.

	"""

	def show(self) -> None:

		"""

		Show the Canvas. All Canvas primitives will be drawn on GL area.


		Returns
		-------
		None
			Always returns None.

		"""


	def hide(self) -> None:

		"""

		Hide the Canvas. All Canvas primitives will become invisible.


		Returns
		-------
		None
			Always returns None.

		"""


	def delete(self) -> None:

		"""

		Delete the Canvas.


		Returns
		-------
		None
			Always returns None.

		"""


	def set_color(self, color: int) -> None:

		"""

		Sets the color for the primitives that will follow.


		Parameters
		----------
		color : int
			It must be either an object of class Color, or an integer in hex RGBA format e.g. 0xFF000000 for Red color.

		Returns
		-------
		None
			Always returns None.

		"""


	def point_size(self, size: int) -> None:

		"""

		Set the size of the points that will follow.


		Parameters
		----------
		size : int
			The size of the points.

		Returns
		-------
		None
			Always returns None.

		"""


	def point(self, x: float, y: float, z: float, type: str='square') -> None:

		"""

		Draw a point.


		Parameters
		----------
		x : float
			The x coordinate.

		y : float
			The y coordinate.

		z : float
			The z coordinate.

		type : str, optional
			Available types are 'square', 'square_hollow', 'cross', 
			'circle', 'circle_hollow', 'diamond', 'diamond_hollow', 
			'hexa_hollow' (default = 'square').

		Returns
		-------
		None
			Always returns None.

		"""


	def line_width(self, width: int) -> None:

		"""

		The width of the lines that will follow.


		Parameters
		----------
		width : int
			The width of the lines.

		Returns
		-------
		None
			Always returns None.

		"""


	def line(self, start: tuple, end: tuple) -> None:

		"""

		Draw a line.


		Parameters
		----------
		start : tuple
			A tuple with (x, y, z) coordinates of the line's starting point.

		end : tuple
			A tuple with (x, y, z) coordinates of the line's ending point.

		Returns
		-------
		None
			Always returns None.

		"""


	def stippled_line(self, start: tuple, end: tuple) -> None:

		"""

		Draw a stippled line.


		Parameters
		----------
		start : tuple
			A tuple with (x, y, z) coordinates of the stippled line's starting point.

		end : tuple
			A tuple with (x, y, z) coordinates of the stippled line's ending point.

		Returns
		-------
		None
			Always returns None.

		"""


	def arrow(self, start: tuple, end: tuple, line_width: int=1, size_of_tip: float=0.16, pos_of_tip: float=0.7, type: int=0) -> None:

		"""

		Draw an arrow.


		Parameters
		----------
		start : tuple
			A tuple with (x, y, z) coordinates of the arrow's starting point.

		end : tuple
			A tuple with (x, y, z) coordinates of the arrow's ending point.

		line_width : int, optional
			Width of the arrow.

		size_of_tip : float, optional
			Size of the tip (0 < size_of_tip < 1).

		pos_of_tip : float, optional
			Position of the tip (0 < pos_of_tip < 1).

		type : int, optional
			0: Default arrow.
			1: Dynamic scale with fixed start.
			2: Dynamic scale with fixed end.

		Returns
		-------
		None
			Always returns None.

		"""


	def triangle(self, p1: tuple, p2: tuple, p3: tuple, shade: bool=True) -> None:

		"""

		Draw a triangle.


		Parameters
		----------
		p1 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 1st point.

		p2 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 2nd point.

		p3 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 3rd point.

		shade : bool, optional
			Add shade to the triangle. (Default: True)

		Returns
		-------
		None
			Always returns None.

		"""


	def quad(self, p1: tuple, p2: tuple, p3: tuple, p4: tuple, shade: bool=True) -> None:

		"""

		Draw a quad.


		Parameters
		----------
		p1 : tuple
			A tuple with (x, y, z) coordinates of the quad's 1st point.

		p2 : tuple
			A tuple with (x, y, z) coordinates of the quad's 2nd point.

		p3 : tuple
			A tuple with (x, y, z) coordinates of the quad's 3rd point.

		p4 : tuple
			A tuple with (x, y, z) coordinates of the quad's 4th point.

		shade : bool, optional
			Add shade to the quad. (Default: True)

		Returns
		-------
		None
			Always returns None.

		"""


	def sphere(self, center: tuple, radius: tuple, shade: bool=True) -> None:

		"""

		Always returns None.


		Parameters
		----------
		center : tuple
			A tuple with (x, y, z) coordinates of the sphere's center.

		radius : tuple
			Sphere's radius.

		shade : bool, optional
			Add shade to the sphere. (Default: True)

		Returns
		-------
		None
			Always returns None.

		"""


	def cylinder(self, origin: tuple, direction: tuple, radius: float, height: float, shade: bool=True) -> None:

		"""

		Draw a cylinder.


		Parameters
		----------
		origin : tuple
			A tuple with (x, y, z) coordinates of the cylinder's origin, 
			the center of the bottom circle.

		direction : tuple
			A tuple with (x, y, z) coordinates of the cylinder's direction.

		radius : float
			Cylinder's radius.

		height : float
			Cylinder's height.

		shade : bool, optional
			Add shade to the cylinder. (Default: True)

		Returns
		-------
		None
			Always returns None.

		"""


	def cube(self, p1: tuple, p2: tuple, p3: tuple, p4: tuple, p5: tuple, p6: tuple, p7: tuple, p8: tuple, shade: bool=True) -> None:

		"""


		Parameters
		----------
		p1 : tuple
			A tuple with (x, y, z) coordinates of the cube's 1st point.

		p2 : tuple
			A tuple with (x, y, z) coordinates of the cube's 2nd point.

		p3 : tuple
			A tuple with (x, y, z) coordinates of the cube's 3rd point.

		p4 : tuple
			A tuple with (x, y, z) coordinates of the cube's 4th point.

		p5 : tuple
			A tuple with (x, y, z) coordinates of the cube's 5th point.

		p6 : tuple
			A tuple with (x, y, z) coordinates of the cube's 6th point.

		p7 : tuple
			A tuple with (x, y, z) coordinates of the cube's 7th point.

		p8 : tuple
			A tuple with (x, y, z) coordinates of the cube's 8th point.

		shade : bool, optional
			Add shade to the cube. (Default: True)

		Returns
		-------
		None
			Always returns None.

		"""


	def __init__(self, name: str) -> object:

		"""

		Canvas object constructor.


		Parameters
		----------
		name : str
			The name of the Canvas. If you call the constructor 
			with a name that already exists the existing object will 
			be returned.

		Returns
		-------
		object
			Returns the created Canvas object.

		"""


	def symbol_origin(self, x: float, y: float, z: float) -> None:

		"""

		The point where scaling will take place for the symbols to follow.


		Parameters
		----------
		x : float
			The x coordinate.

		y : float
			The y coordinate.

		z : float
			The z coordinate.

		Returns
		-------
		None
			Always returns None.

		"""


	def symbol_line(self, start: tuple, end: tuple) -> None:

		"""

		Draw a line which is dynamically scaled.


		Parameters
		----------
		start : tuple
			A tuple with (x, y, z) coordinates of the symbol line's starting point.

		end : tuple
			A tuple with (x, y, z) coordinates of the symbol line's ending point.

		Returns
		-------
		None
			Always returns None.

		"""


	def symbol_cone(self, start: tuple, end: tuple, radius: float) -> None:

		"""

		Draw a cone which is dynamically scaled.


		Parameters
		----------
		start : tuple
			A tuple with (x, y, z) coordinates of the cone's starting point.

		end : tuple
			A tuple with (x, y, z) coordinates of the cone's ending point.

		radius : float
			The cone's radius.

		Returns
		-------
		None
			Always returns None.

		"""


	def symbol_triangle(self, p1: tuple, p2: tuple, p3: tuple) -> None:

		"""

		Draw a triangle which is dynamically scaled.


		Parameters
		----------
		p1 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 1st point.

		p2 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 2nd point.

		p3 : tuple
			A tuple with (x, y, z) coordinates of the triangle's 3rd point.

		Returns
		-------
		None
			Always returns None.

		"""


	def symbol_label(self, position: tuple, text: str, font_size: int=12) -> None:

		"""

		Draw a label which is dynamically scaled.


		Parameters
		----------
		position : tuple
			A tuple with (x, y, z) coordinates of the label.

		text : str
			The label's text.

		font_size : int, optional
			The size of the font.

		Returns
		-------
		None
			Always returns None.

		"""


	def label(self, position: tuple, text: str, font_size: int=12) -> None:

		"""

		Draw a label.


		Parameters
		----------
		position : tuple
			A tuple with (x, y, z) coordinates of the label.

		text : str
			The label's text.

		font_size : int, optional
			The size of the font.

		Returns
		-------
		None
			Always returns None.

		"""

def BCSettingsGetUserDefinedValue(keyword: str) -> str:

	"""

	Returns the string value of user defined keyword with name keyword
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsSetUserDefinedValue(keyword: str, value: str) -> int:

	"""

	Sets value value to user defined keyword keyword. 
	If keyword a\ keyword doesn't exist it will be created.
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup and set the new value.

	value : str
		the new string value of the keyword

	Returns
	-------
	int
		1 if value was set successfully to keyword keyword, 0 otherwise.

	See Also
	--------
	BCSettingsGetUserDefinedValue

	"""

def BCSettingsUserDefinedKeywordExists(name: str) -> int:

	"""

	Checks if a user defined key with name name exists in BCSettingsHandler structure
	It will only search for a keyword not for a value.
	This function is not supported under VR mode.

	Parameters
	----------
	name : str
		the keyword's name to look up.

	Returns
	-------
	int
		1 if user defined keyword is found, 0 otherwise.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsReadFile(filePath: str) -> int:

	"""

	Reads a defaults file, from path filePath.
	
	Settings that will be read from the file, will be applied
	to the running application.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		the path of defaults file

	Returns
	-------
	int
		1 if reading was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteFile(filePath: str) -> int:

	"""

	Writes a defaults file, at path filePath. If a filePath is not given,
	\the defaults file will be written in .BETA folder according to which
	\layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If the file already exists, it will be overwritten.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str, optional
		the path where the defaults file will be written.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteGroup(filePath: str, groupName: str) -> int:

	"""

	Writes the settings of Group named groupName, at path filePath.
	\If filePath is empty, the group will be written in defaults file located in .BETA folder
	\according to which layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If file already exists, then the settings of the corresponding group will be updated.
	The rest of the file will remain intact.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		the path where the defaults file will be written.

	groupName : str
		the group name, to write.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteFile

	"""

def BCSettingsGetDefaultValue(keyword: str) -> str:

	"""

	Returns the default value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsGetStartupValue

	"""

def BCSettingsGetStartupValue(keyword: str) -> str:

	"""

	Returns the startup value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsGetDefaultValue

	"""

