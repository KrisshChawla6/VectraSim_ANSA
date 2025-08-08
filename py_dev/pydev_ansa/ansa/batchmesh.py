from __future__ import annotations
from typing import *

def AddFilterToScenario(field: str, expression: str, value: str, session: object, match: str, case_sensitive: str, filter_name: str) -> int:

	"""

	The function adds a filter to an existing batch mesh scenario (meshing, layers, wrap or volume), much like the way it is done through the batch mesh manager. If the scenario has an active filter, a new row is added to that filter. 
	Otherwise, a new filter is created and is set as active.
	The first, second and third arguments refer to the field, expression and value of the filter respectively.

	Parameters
	----------
	field : str
		Field Name.

	expression : str
		Expression.

	value : str
		The value that the expression will evaluate.

	session : object
		The reference to the Assembly rule.

	match : str, optional
		Determines if all the filter rows must be matched. Use "all" or "any" to change 
		the value.

	case_sensitive : str, optional
		Determines if the filter will be case sensitive. Use "yes" or "no" to change 
		the value.

	filter_name : str, optional
		Give a specific name to a filter.

	Returns
	-------
	int
		Returns 1 if the filter was added successfully, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    scenario = batchmesh.GetNewMeshingScenario("Name", "Test")
		    ret_val = batchmesh.AddFilterToScenario(
		        "MASS", "is greater than", "0.001", scenario
		    )
		    ret_val = batchmesh.AddFilterToScenario(
		        "Module Id",
		        "equals",
		        "A200",
		        scenario,
		        match="all",
		        filter_name="Module_Id_Filter",
		    )
		    ret_val = batchmesh.AddFilterToScenario(
		        "Module Id", "equals", "A100", scenario, match="any", case_sensitive="yes"
		    )


	"""

def AddFilterToSession(field: str, expression: str, value: str, session: object, match: str, case_sensitive: str, filter_name: str) -> int:

	"""

	The function adds a filter to an existing batch mesh session (meshing, layers or volume), much like the way it is done through the batch mesh manager.
	If the session has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.

	Parameters
	----------
	field : str
		Field Name.

	expression : str
		Expression.

	value : str
		The value that the expression will evaluate.

	session : object
		The reference to the Assembly rule entity.

	match : str, optional
		Determines if all the filter rows must be matched. Use "all" or "any" to change 
		the value.

	case_sensitive : str, optional
		Determines if the filter will be case sensitive. Use "yes" or "no" to change 
		the value.

	filter_name : str, optional
		Give a specific name to a filter.

	Returns
	-------
	int
		Returns 1 if the filter was successfully created, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = batchmesh.GetNewSession("MySession")
		    ret_val = batchmesh.AddFilterToSession("MASS", "is greater than", "0.001", session)
		    ret_val = batchmesh.AddFilterToSession(
		        "Module Id",
		        "equals",
		        "A200",
		        session,
		        match="all",
		        filter_name="Module_Id_Filter",
		    )
		    ret_val = batchmesh.AddFilterToSession(
		        "Module Id", "equals", "A300", session, match="all"
		    )
		    ret_val = batchmesh.AddFilterToSession(
		        "Module Id", "equals", "A100", session, match="any", case_sensitive="yes"
		    )


	"""

def AddPartToMeshingScenario(INPUT_ref: object, SCENARIO_ref: object) -> int:

	"""

	This function adds an item or an array of items (part, group, property or volume) to a batch mesh scenario.

	Parameters
	----------
	INPUT_ref : object
		References the item to be added to the senario. The type of the item may be a part,  group, 
		property or volume.

	SCENARIO_ref : object
		References the senario. The senario's type must be in accordance to the type of the item.

	Returns
	-------
	int
		Returns 1 if INPUT and SCENARIO are valid and the items were added, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    scenario = batchmesh.GetNewMeshingScenario("Name", "scenario_with_one_part")
		    part = base.GetPartFromModuleId("1")
		    ret_val = batchmesh.AddPartToMeshingScenario(part, scenario)
		
		    scenario = batchmesh.GetNewMeshingScenario("Name", "scenario_with_all_parts")
		    parts = base.CollectEntities(ansa.constants.NASTRAN, None, "ANSAPART")
		    ret_val = batchmesh.AddPartToMeshingScenario(parts, scenario)
		
		
		# ...or...
		
		
		def main():
		    scenario = batchmesh.GetNewVolumeScenario("Volume_Scenario")
		    volumes = base.CollectEntities(ansa.constants.OPENFOAM, None, "VOLUME")
		    ret_val = batchmesh.AddPartToMeshingScenario(volumes, scenario)


	"""

def AddPartToSession(ITEM_ref: object, SESSION_ref: object) -> int:

	"""

	This function adds an item to a batch mesh session.

	Parameters
	----------
	ITEM_ref : object
		References the item to be added to the session. The type of the item may be a part, group, 
		property or volume.

	SESSION_ref : object
		References the session.The session's type must be in accordance to the type of the item.

	Returns
	-------
	int
		Returns 1 if the numbers referencing the item and the session are valid entities, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    session = batchmesh.GetNewSession("MySession")
		    part = base.GetPartFromModuleId("1")
		    ret_val = batchmesh.AddPartToSession(part, session)


	"""

def AddSessionToMeshingScenario(SESSION_list: object, SCENARIO_ref: object) -> int:

	"""

	The function adds an array of batch mesh sessions to a scenario.

	Parameters
	----------
	SESSION_list : object
		References the the list of sessions to be added to the scenario.It may be either a
		meshing,layers or volume session.

	SCENARIO_ref : object
		References the senario to be used and must be of the same type as the first argument.

	Returns
	-------
	int
		Returns 1 if the SESSION_ARRAY is of proper type, SCENARIO is a valid scenario, according to the type of the array, and all the sessions have been successfully added to the scenario. Otherwise, 0 is returned.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = list()
		    meshing_scenario = batchmesh.GetNewMeshingScenario("Meshing_Scenario")
		    MessingSession = batchmesh.GetNewSession("session1")
		    session.append(MessingSession)
		    batchmesh.AddSessionToMeshingScenario(session, meshing_scenario)
		
		    layers_scenario = batchmesh.GetNewLayersScenario("Layers_Scenario")
		    LayerSession = batchmesh.GetNewLayersSession("session2")
		    session.append(LayerSession)
		    batchmesh.AddSessionToMeshingScenario(session, layers_scenario)


	"""

def DistributeAllItemsToScenarios() -> int:

	"""

	The function distributes all parts/groups/properties of the current database to any meshing and layers scenarios that may exist. The filters for each scenario are taken into account.

	Returns
	-------
	int
		Always returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    batchmesh.DistributeAllItemsToScenarios()


	"""

def GetNewLayersScenario(name: str, search_for: str) -> object:

	"""

	The function creates a new batch mesh layers scenario.

	Parameters
	----------
	name : str, optional
		Define a name for the scenario, or create an 
		untitled one by leaving the argument blank.

	search_for : str, optional
		Type of entities to add to the scenario. Accepted 
		values are "PARTS", "GROUPS", "PIDS".

	Returns
	-------
	object
		Returns a reference to the newly created layers scenario.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    layer_scen = batchmesh.GetNewLayersScenario("Layers_Scenario")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    layer_scen = batchmesh.GetNewLayersScenario()
		
		
		# OR to add PIDS to a scenario:
		
		
		def main():
		    layer_scen = batchmesh.GetNewLayersScenario("Layers_Scenario", "PIDS")


	"""

def GetNewLayersSession(name: str) -> object:

	"""

	This function creates a new batch mesh layer session.

	Parameters
	----------
	name : str, optional
		Define a name for the session, or create an untitled one by leaving the argument blank.

	Returns
	-------
	object
		Returns a reference to the newly created layer session.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    layer_sess = batchmesh.GetNewLayersSession("Layer_Session")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    layer_sess = batchmesh.GetNewLayersSession()


	"""

def GetNewMeshingScenario(name: str, search_for: str) -> object:

	"""

	The function creates a new meshing scenario.

	Parameters
	----------
	name : str, optional
		Define a name for the scenario, or create an 
		untitled one by leaving the argument blank.

	search_for : str, optional
		Change the type of entities to add to the scenario. 
		Accepted values are: "PARTS", "GROUPS" or "PIDS".

	Returns
	-------
	object
		Returns a reference to the newly created meshing scenario.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    mesh_scen = batchmesh.GetNewMeshingScenario("Meshing_Scenario")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    mesh_scen = batchmesh.GetNewMeshingScenario()
		
		
		# OR to add PIDS to a scenario:
		
		
		def main():
		    mesh_scen = batchmesh.GetNewMeshingScenario("Meshing_Scenario", "PIDS")


	"""

def GetNewSession(name: str) -> object:

	"""

	This function creates a new batch mesh session.

	Parameters
	----------
	name : str, optional
		Define a name for the session, or create an untitled one by leaving the argument blank.

	Returns
	-------
	object
		Returns a reference to the newly created batch mesh session.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = batchmesh.GetNewSession("Session")
		
		
		# OR to create an Untitled one:
		
		
		def main():
		    session = batchmesh.GetNewSession()


	"""

def GetNewVolumeScenario(name: str, auto_detect: bool, parts: str, include_facets: bool) -> object:

	"""

	The function creates a new batch mesh volume scenario.

	Parameters
	----------
	name : str, optional
		Define a name for the scenario, or create an untitled one by leaving the argument blank.

	auto_detect : bool, optional
		Runs auto-detect. By default it is enabled.

	parts : str, optional
		Determines in which parts, the auto-detected volumes  will be added. Options are: "one_part_for_volume" (default), "one_part_for_all_volumes", "add_to_existing_part".

	include_facets : bool, optional
		Includes facets in auto-detection. By default it is disabled.

	Returns
	-------
	object
		Returns a reference to the newly created volume meshing scenario.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    vol_scen = batchmesh.GetNewVolumeScenario(
		        name="Volume_Scenario",
		        auto_detect=True,
		        parts="one_part_for_all_volumes",
		        include_facets=False,
		    )
		
		
		# OR to create an untitled one:
		
		
		def main():
		    vol_scen = batchmesh.GetNewVolumeScenario()


	"""

def GetNewVolumeSession(name: str) -> object:

	"""

	This function creates a new batch mesh volume session.

	Parameters
	----------
	name : str, optional
		Define a name for the session, or create an 
		untitled one by leaving the argument blank.

	Returns
	-------
	object
		Returns a reference to the newly created volume mesh session.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    vol_ses = batchmesh.GetNewVolumeSession("Volume_Session")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    vol_ses = batchmesh.GetNewVolumeSession()


	"""

def GetNewWrapScenario(name: str, search_for: str) -> object:

	"""

	This function creates a new wrap scenario.

	Parameters
	----------
	name : str, optional
		Define a name for the scenario, or create an untitled 
		one by leaving the argument blank.

	search_for : str, optional
		Type of entities to add to the scenario. Accepted 
		values are: "PARTS", "GROUPS" or "PIDS".

	Returns
	-------
	object
		Returns a reference to the newly created wrapping scenario, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    wrap_scen = batchmesh.GetNewWrapScenario("Wrap_Scenario")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    wrap_scen = batchmesh.GetNewWrapScenario()
		
		
		# OR to add PIDS to a scenario:
		
		
		def main():
		    wrap_scen = batchmesh.GetNewWrapScenario("Wrap_Scenario", "PIDS")


	"""

def GetNewWrapSession(name: str) -> object:

	"""

	This function creates a new batch mesh wrap session.

	Parameters
	----------
	name : str, optional
		Define a name for the session, or create an untitled one by leaving the argument blank.

	Returns
	-------
	object
		Returns a reference to the newly created wrap session, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    wrap_ses = batchmesh.GetNewWrapSession("Wrap_Session")
		
		
		# OR to create an untitled one:
		
		
		def main():
		    wrap_ses = batchmesh.GetNewWrapSession()


	"""

def GetPartsFromMeshingScenario(MESHING_SCENARIO_ref: object) -> object:

	"""

	The function collects all parts, groups or properties belonging to a particular meshing scenario.

	Parameters
	----------
	MESHING_SCENARIO_ref : object
		References the meshing scenario under consideration.

	Returns
	-------
	object
		Returns a list containing all the parts, groups or properties that belong to the specific meshing scenario.
		In case MESHING_SCENARIO is not a valid reference or it does not contain any parts, an empty list is returned.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    scenario = base.NameToEnts("Meshing_Scenario")
		    parts = batchmesh.GetPartsFromMeshingScenario(scenario[0])
		    print(len(parts))


	"""

def GetPartsFromSession(SESSION_ref: object) -> object:

	"""

	This function collects all the parts, groups or properties that are included in a specific session or area.

	Parameters
	----------
	SESSION_ref : object
		References the meshing session or area under consideration.

	Returns
	-------
	object
		Returns a list containing all the parts, groups or properties that belong to the specific session or area.
		In case the SESSION or area is not a valid reference or it does not contain any parts, an empty list is returned.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    session = base.NameToEnts("Session")
		    parts_matrix = batchmesh.GetPartsFromSession(session[0])
		    print(len(parts_matrix))


	"""

def GetSessionMeshParamsName(session_ref: object) -> str:

	"""

	Gets the name of batch meshing sessions' parameters.

	Parameters
	----------
	session_ref : object
		References the meshing session under consideration.

	Returns
	-------
	str
		Returns the name of the session parameters.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    scenario = base.NameToEnts("Meshing_Scenario")
		    sessions_matrix = batchmesh.GetSessionsFromMeshingScenario(scenario[0])
		    for session in sessions_matrix:
		        params_name = batchmesh.GetSessionMeshParamsName(session)
		        print(params_name)


	"""

def GetSessionQualityCriteriaName(session_ref: object) -> str:

	"""

	Gets the name of batch meshing sessions' quality criteria.

	Parameters
	----------
	session_ref : object
		References the meshing session under consideration.

	Returns
	-------
	str
		Returns the name of the session quality criteria.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    scenario = base.NameToEnts("Meshing_Scenario")
		    sessions_matrix = batchmesh.GetSessionsFromMeshingScenario(scenario[0])
		    for session in sessions_matrix:
		        quality_criteria_name = batchmesh.GetSessionQualityCriteriaName(session)
		        print(quality_criteria_name)


	"""

def GetSessionsFromMeshingScenario(MESHING_SCENARIO_ref: object) -> object:

	"""

	The function collects all sessions belonging to a particular meshing scenario.

	Parameters
	----------
	MESHING_SCENARIO_ref : object
		References the meshing senario under consideration.

	Returns
	-------
	object
		Returns a list containing all the sessions that belong to the specific meshing scenario.
		In case MESHING_SCENARIO is not a valid reference or it does not contain any sessions, an empty list is returned.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    scenario = base.NameToEnts("Meshing_Scenario")
		    sessions_matrix = batchmesh.GetSessionsFromMeshingScenario(scenario[0])
		    print(len(sessions_matrix))


	"""

def ImportMeshingFiles(filename: str, property_conflicts: str, material_conflicts: str, set_conflicts: str, coord_conflicts: str, node_conflicts: str) -> int:

	"""

	This function opens an ansa file containing parts/groups previously saved with the SaveMeshingSession function and replaces them with parts/groups of the current database that may match them.

	Parameters
	----------
	filename : str
		The path of the ansa file to be imported.

	property_conflicts : str, optional
		"Offset" creates a new entity.
		"KeepOld" keeps the old value.
		"KeepNew" keeps the new value. (Default)

	material_conflicts : str, optional
		"Offset" creates a new entity.
		"KeepOld" keeps the old value.
		"KeepNew" keeps the new value. (Default)

	set_conflicts : str, optional
		"Offset" creates a new entity. (Default)
		"KeepOld" keeps the old value.
		"KeepNew" keeps the new value.

	coord_conflicts : str, optional
		"Offset" creates a new entity. (Default)
		"KeepOld" keeps the old value.
		"KeepNew" keeps the new value.

	node_conflicts : str, optional
		"Offset" creates a new entity. (Default)
		"KeepOld" keeps the old value.
		"KeepNew" keeps the new value.

	Returns
	-------
	int
		Returns 1 if session is a valid file with read permission, and 0 if it is invalid or the file does not exist.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    status = batchmesh.ImportMeshingFiles(
		        "/ansa/meshing_files.ansa",
		        property_conflicts="KeepOld",
		        material_conflicts="KeepNew",
		        set_conflicts="Offset",
		        coord_conflicts="Offset",
		        node_conflicts="Offset",
		    )


	"""

def IsolateAndCopyParameters(ITEM_ref: object) -> float:

	"""

	This function isolates entities of ITEM and copies mesh parameters and quality criteria of ITEM
	to the respective fields of Shell Mesh Parameters and Quality Criteria. ITEM can be either Session
	or Box.

	Parameters
	----------
	ITEM_ref : object
		References the meshing session under consideration.

	Returns
	-------
	float
		Returns 1 if the ITEM is of proper type, is isolated and parameters are successfully copied. Otherwise, 0 is returned.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		from ansa import constants
		
		
		def main():
		    sessions_array = base.CollectEntities(
		        constants.NASTRAN, None, "BATCH_MESH_SESSION", False
		    )
		    for session in sessions_array:
		        if session._id == 2:
		            batchmesh.IsolateAndCopyParameters(session)


	"""

def ReadSessionMeshParams(SESSION_ref: object, FILENAME_str: int) -> int:

	"""

	This function reads mesh parameters from a specific file and assigns them to a batch mesh session or area (wrap, layers).

	Parameters
	----------
	SESSION_ref : object
		References the batch mesh session accepting the values.
		It may also reference a wrap or layers area.

	FILENAME_str : int
		The path of the file containing the parameters.

	Returns
	-------
	int
		Returns 1 if SESSION is a valid reference and the file exists, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = batchmesh.GetNewSession("Some_Session")
		    ret_val = batchmesh.ReadSessionMeshParams(session, "/ansa/params.ansa_mpar")
		    print(ret_val)


	"""

def ReadSessionQualityCriteria(SESSION_ref: object, FILENAME_str: int) -> int:

	"""

	This function reads quality criteria from a specific file for batch mesh sessions.
	The first argument refers to the batch mesh session accepting the values. 
	The second argument is the path of the file containing the criteria.

	Parameters
	----------
	SESSION_ref : object
		References the the batch mesh session accepting the values.

	FILENAME_str : int
		The path of the file containing the criteria.

	Returns
	-------
	int
		Returns 1 if session is a valid batch mesh session and the file exists, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = batchmesh.GetNewSession("Some_Session")
		    ret_val = batchmesh.ReadSessionQualityCriteria(session, "/ansa/qual.ansa_qual")
		    print(ret_val)


	"""

def RunAllMeshingScenarios(time_limit: int) -> int:

	"""

	The function runs all active meshing scenarios of database, which may be meshing, layers or volume scenario.

	Parameters
	----------
	time_limit : int, optional
		Time limit in minutes. If execution time exceeds TIME_LIMIT, 
		the process is halted.

	Returns
	-------
	int
		Returns:
		0, If all scenarios are dectivated.
		1, If at least one scenario has run.
		2, If at least one scenario hasn't run.
		-1, If the process is halted due to the time limit being exceeded or due to Pause-Break key being pressed.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    batchmesh.RunAllMeshingScenarios(60)


	"""

def RunMeshingScenario(session: object, time_limit: int) -> int:

	"""

	The function runs all sessions in a batch mesh scenario.

	Parameters
	----------
	session : object
		References the scenario that will be run, which may be a meshing, layers, wrap 
		or volume scenario.

	time_limit : int, optional
		Time limit in minutes. If execution time exceeds TIME_LIMIT, process is halted.

	Returns
	-------
	int
		Returns:
		0, If SCENARIO is deactivated.
		1, If SCENARIO has run.
		2, If SCENARIO hasn't run.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    mesh_scen = batchmesh.GetNewMeshingScenario("MyScenario")
		    status = batchmesh.RunMeshingScenario(mesh_scen, 10)


	"""

def RunSession(session: object, time_limit: int) -> int:

	"""

	This function runs a batch mesh session.

	Parameters
	----------
	session : object
		References the session that will be run, which may be meshing, layers or volume
		scenario.

	time_limit : int, optional
		Time limit in minutes. If execution time exceeds TIME_LIMIT, process is halted.

	Returns
	-------
	int
		Returns:
		0, If SESSION isn't active.
		1, If SESSION has run.
		2, If SESSION hasn't run.
		-1, If the process is halted due to the time limit being exceeded or due to Pause-Break key being pressed.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    session = batchmesh.GetNewSession("MySession")
		    status = batchmesh.RunSession(session, 10)


	"""

def SaveMeshingSession(session: object, filename: str, only_failed: int, single_seperate: str) -> int:

	"""

	This function saves a session with its parts in the same way it is saved from the right click option
	in the Batch Mesh Manager window.

	Parameters
	----------
	session : object
		References the session that will be saved, which may be meshing, layers or
		volume scenario.

	filename : str
		The name with which the session will be saved.

	only_failed : int, optional
		The option to save only failed parts, TYPE: integer, VALUES: 0 or 1. If the
		option is omitted, only failed parts are saved.

	single_seperate : str, optional
		Values are 'SINGLE' and 'SEPARATE'.

	Returns
	-------
	int
		Returns 1 on success, or 0 if the input entity is not a meshing session.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    sessions = base.NameToEnts("Session")
		    ret = batchmesh.SaveMeshingSession(
		        sessions[0], "/home/user/test_save/", 0, "SEPARATE"
		    )
		
		    
		\tOther possible options:
		\t- SaveMeshingSession(session, "/home/user/test_save/test.ansa")
		\t- SaveMeshingSession(session, "/home/user/test_save/test.ansa",0)
		\t- SaveMeshingSession(session, "/home/user/test_save/test.ansa",0,"SINGLE")
		\t- SaveMeshingSession(session, "/home/user/test_save/",0,"SEPARATE")
		\t


	"""

def SaveSessionMeshParams(SESSION_ref: object, FILENAME_str: str) -> int:

	"""

	This function saves the mesh parameters of a batch mesh session or area (wrap, layers) to a specified file.

	Parameters
	----------
	SESSION_ref : object
		References the session whose parameters will be saved, which may be
		meshing, layers or volume scenario.
		It may also reference a wrap or layers area.

	FILENAME_str : str
		The path of the file where the parameters will be written.

	Returns
	-------
	int
		Returns 1 if SESSION is a valid batch mesh session reference and the file is accessible, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    session = base.NameToEnts("Session")
		    batchmesh.SaveSessionMeshParams(session, "/ansa/params.ansa_mpar")


	"""

def SaveSessionQualityCriteria(SESSION_ref: object, FILENAME_str: str) -> int:

	"""

	This function saves the quality criteria of a batch mesh session to a specified file.

	Parameters
	----------
	SESSION_ref : object
		References the session whose criteria will be saved, which may be
		meshing, layers or volume scenario.

	FILENAME_str : str
		The path of the file where the criteria will be written.

	Returns
	-------
	int
		Returns 1 if SESSION is a valid batch mesh session reference and the file is accessible, or 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    session = base.NameToEnts("Session")
		    batchmesh.SaveSessionQualityCriteria(session, "/ansa/qual.ansa_qual")


	"""

def WriteStatistics(SESSION_ref: object, FILENAME_str: str) -> int:

	"""

	This function saves the statistics report of a batch mesh session or meshing scenario to a file.

	Parameters
	----------
	SESSION_ref : object
		References the session or the meshing scenario that will be saved.

	FILENAME_str : str
		The path where the file will be saved.

	Returns
	-------
	int
		Returns 0 if the SESSION is not a valid reference or if the file cannot be accessed, 
		2 if the session has status "Completed" without errors and 1 otherwise.
		If the file exists it is overwritten.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		
		
		def main():
		    session = base.NameToEnts("Session")
		    ret_val = batchmesh.WriteStatistics(session[0], "/home/m.vasiladioti/stats.html")
		    print(ret_val)


	"""

def SetSessionVisibility(session: object, visibility: str) -> int:

	"""

	This function sets the visibility of the session.
	The session can be either (Mesh, Layers, Volume, Wrap) Session or (Mesh) Box.
	It can be shown, hidden or it can be isolated (shown alone).
	The session's visibility can be controlled by the respective parameter in the arguments list.

	Parameters
	----------
	session : object
		Specific session or box object.

	visibility : str
		"Show" to show the session.
		"Hide" to hide it.
		"ShowOnly" to isolate it.

	Returns
	-------
	int
		Returns 0 if invalid arguments were specified, 1 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		from ansa import constants
		
		
		def main():
		    sessions_array = base.CollectEntities(
		        constants.NASTRAN, None, "BATCH_MESH_SESSION", False
		    )
		    for session in sessions_array:
		        if session._name == "Default_Session":
		            batchmesh.SetSessionVisibility(session, visibility="ShowOnly")


	"""

def CopySessionParameters(session: object, mesh_parameters: bool, quality_criteria: bool) -> int:

	"""

	This function copies the mesh parameters and quality criteria of a session to the 
	respective fields of global (Shell or Solid) Mesh Parameters and Quality 
	Criteria. 'session' can be either Session (Mesh, Layers, Volume, Wrap) or Box 
	(Mesh). The Mesh Parameters and the Quality Criteria can be handled
	independently with the use of the respective flags in the arguments list. If no
	optional arguments are specified nothing happens.

	Parameters
	----------
	session : object
		A reference to a Session (Mesh, Layers, Volume, Wrap) 
		or a Box (Mesh) object.

	mesh_parameters : bool, optional
		True or False to specify if the mesh parameters will be 
		copied or not.

	quality_criteria : bool, optional
		True or False to specify if the quality criteria will be
		 copied or not.

	Returns
	-------
	int
		Returns 0 if invalid arguments are specified, 1 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import base
		from ansa import constants
		
		
		def main():
		    sessions_array = base.CollectEntities(
		        constants.NASTRAN, None, "BATCH_MESH_SESSION", False
		    )
		    for session in sessions_array:
		        if session._name == "Default_Session":
		            batchmesh.CopySessionParameters(
		                session, mesh_parameters=True, quality_criteria=True
		            )


	"""

def GetNewLayersArea(parent_session: object, name: str, first_height: float, first_height_method: str, growth_factor: float, zero_thickness: bool, layers_prop_name: str, number_of_layers: int, additional_outer_layers: int, orthogonal_layers: int, smooth_top_cap: bool, switch_to_variable_growth_rate: bool, varibable_growth_rates: str) -> object:

	"""

	This function adds a new layers area in a layers scenario, in the Batch Mesh Manager.

	Parameters
	----------
	parent_session : object
		References the session where layers area will be added.

	name : str, optional
		The name of the mesh parameters of created area.

	first_height : float, optional
		First layer height value of the mesh parameters of created area.

	first_height_method : str, optional
		Determines whether first layer height value is expressed as an absolute value
		or as a factor (aspect) of the local element length.
		Accepted values "aspect" or "absolute".

	growth_factor : float, optional
		Growth rate of layers.

	zero_thickness : bool, optional
		Will grow layers for both sides of zero thickness walls.

	layers_prop_name : str, optional
		Property name of generated solid elements.

	number_of_layers : int, optional
		Number of layers to be generated

	additional_outer_layers : int, optional
		Additional outer layers to be generated in aspect mode

	orthogonal_layers : int, optional
		Number of layers on which no vector smoothing will be applied

	smooth_top_cap : bool, optional
		Apply smooth top cap or not

	switch_to_variable_growth_rate : bool, optional
		If true then variable growth rate will be applied

	varibable_growth_rates : str, optional
		The variable growth rates as a string

	Returns
	-------
	object
		Returns a reference to the newly created layers area.
		In case of an error, the function returns None.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    layers_ses = []
		    scen = batchmesh.GetNewLayersScenario("new_layers_scenario")
		    sess = batchmesh.GetNewLayersSession("new_layers_session")
		    layers_ses.append(sess)
		    batchmesh.AddSessionToMeshingScenario(layers_ses, scen)
		    area = batchmesh.GetNewLayersArea(
		        sess, "area_params", 1.25, "absolute", 1.25, True, "new_layers_prop"
		    )


	"""

def GetNewWrapArea(parent_session: object, name: str, min_len: float, max_len: float, part_pid_proximity: bool, self_proximity: bool, reduction_factor: float, curvature_min_len: float, proximity_min_len: float) -> object:

	"""

	This function adds a new wrap area in a wrap scenario, in the Batch Mesh Manager.

	Parameters
	----------
	parent_session : object
		References the session where the wrap area will be added.

	name : str, optional
		The name of the mesh parameters of the created area.

	min_len : float, optional
		Area specific minimum length value.

	max_len : float, optional
		Area specific maximum length value.

	part_pid_proximity : bool, optional
		Enables proximity refinement between different parts/properties.

	self_proximity : bool, optional
		Enables self-proximity refinement in a part/property.

	reduction_factor : float, optional
		Further reduction factor of local minimum length.

	curvature_min_len : float, optional
		Area specific minimum curvature length value.

	proximity_min_len : float, optional
		Area specific minimum proximity length value.

	Returns
	-------
	object
		Returns a reference to the newly created wrap area.
		In case of an error, the function returns None.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    wrap_ses = []
		    scen = batchmesh.GetNewWrapScenario("new_wrap_scenario")
		    sess = batchmesh.GetNewWrapSession("new_wrap_session")
		    wrap_ses.append(sess)
		    batchmesh.AddSessionToMeshingScenario(wrap_ses, scen)
		    area = batchmesh.GetNewWrapArea(sess, "area_params", 20.0, 40.0, True, True, 1.2)


	"""

def GetBatchMeshItemActiveState(batch_mesh_item: object) -> bool:

	"""

	This function provides the active state of a batch mesh item.

	Parameters
	----------
	batch_mesh_item : object
		The batch mesh item whose status will be provided.

	Returns
	-------
	bool
		Returns True or False depending on the item's active state.

	See Also
	--------
	batchmesh.SetBatchMeshItemActiveState

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import batchmesh
		from ansa import constants
		
		
		def main():
		    bm_items = base.CollectEntities(
		        constants.NASTRAN,
		        None,
		        [
		            "BATCH_MESH_SESSION_GROUP",
		            "BATCH_MESH_SESSION",
		            "BATCH_MESH_BOX",
		            "BATCH_MESH_LAYERS_SCENARIO",
		            "BATCH_MESH_LAYERS_SESSION",
		            "BATCH_MESH_LAYERS_AREA",
		            "BATCH_MESH_WRAP_SCENARIO",
		            "BATCH_MESH_WRAP_SESSION",
		            "BATCH_MESH_WRAP_AREA",
		            "BATCH_MESH_VOLUME_SCENARIO",
		            "BATCH_MESH_VOLUME_SESSION",
		        ],
		    )
		    for item in bm_items:
		        state = batchmesh.GetBatchMeshItemActiveState(item)
		        if state == False:
		            batchmesh.SetBatchMeshItemActiveState(item, active_state=True)


	"""

def SetBatchMeshItemActiveState(batch_mesh_item: object, active_state: bool) -> object:

	"""

	This function sets the active state of a batch mesh item.

	Parameters
	----------
	batch_mesh_item : object
		The batch mesh item whose status will be changed.

	active_state : bool
		The desired active status.

	Returns
	-------
	object
		Always returns none.

	See Also
	--------
	batchmesh.GetBatchMeshItemActiveState

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import batchmesh
		from ansa import constants
		
		
		def main():
		    bm_items = base.CollectEntities(
		        constants.NASTRAN,
		        None,
		        [
		            "BATCH_MESH_SESSION_GROUP",
		            "BATCH_MESH_SESSION",
		            "BATCH_MESH_BOX",
		            "BATCH_MESH_LAYERS_SCENARIO",
		            "BATCH_MESH_LAYERS_SESSION",
		            "BATCH_MESH_LAYERS_AREA",
		            "BATCH_MESH_WRAP_SCENARIO",
		            "BATCH_MESH_WRAP_SESSION",
		            "BATCH_MESH_WRAP_AREA",
		            "BATCH_MESH_VOLUME_SCENARIO",
		            "BATCH_MESH_VOLUME_SESSION",
		        ],
		    )
		    for item in bm_items:
		        state = batchmesh.GetBatchMeshItemActiveState(item)
		        if state == False:
		            batchmesh.SetBatchMeshItemActiveState(item, active_state=True)


	"""

def GetNewBox(parent_session: object, contents: object) -> object:

	"""

	This function adds a box in a batch mesh session, in the Batch Mesh Manager.

	Parameters
	----------
	parent_session : object
		References the session where the box will be added.

	contents : object
		A list of items suitable for a batch mesh box. Accepted item types are BCBOX and MORPHBOX.

	Returns
	-------
	object
		Returns a reference to the newly created box.
		In case of an error, the function returns None.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		from ansa import constants
		
		
		def main():
		    session = batchmesh.GetNewSession()
		    contents = base.CollectEntities(
		        constants.NASTRAN, None, ["BCBOX", "MORPHBOX", "SIZE BOX"]
		    )
		    box = batchmesh.GetNewBox(session, contents)


	"""

def DraftRunAllMeshingScenarios(time_limit: int) -> int:

	"""

	The function runs all active meshing scenarios of database.

	Parameters
	----------
	time_limit : int, optional
		Time limit in minutes. If execution time exceeds TIME_LIMIT, 
		the process is halted.

	Returns
	-------
	int
		Returns:
		0, If all meshing scenarios are dectivated.
		1, If at least one meshing scenario has run.
		2, If at least one meshing scenario hasn't run.
		-1, If the process is halted due to the time limit being exceeded or due to Pause-Break key being pressed.

	Examples
	--------
	::

		import ansa
		from ansa import batchmesh
		
		
		def main():
		    batchmesh.DraftRunAllMeshingScenarios(60)


	"""

