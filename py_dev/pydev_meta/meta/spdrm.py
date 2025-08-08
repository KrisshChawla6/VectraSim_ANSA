from __future__ import annotations
from typing import *


class process:
	def getDefinitionWorkflows() -> object:
	
		"""
	
		This function queries the SPDRM that is currently configured for Process 
		Management for all workflows.
	
		Returns
		-------
		object
			The function returns a list of WorkflowDefinition objects
	
		See Also
		--------
		spdrm.process.WorkflowDefinition
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    workflows = spdrm.process.getDefinitionWorkflows()
			    for w in workflows:
			        print("Workflow with Id ({}) and Name ({})".format(w.id, w.name))
	
	
		"""
	
	def instantiateWorkflow(workflow_handle_id: int, input_slot_values: object, input_dir: str) -> int:
	
		"""
	
		This function instantiates a workflow for execution in the remote SPDRM 
		environment.
	
		Parameters
		----------
		workflow_handle_id : int
			Identifier of the workflow definition
	
		input_slot_values : object
			This argument provides the input values to be offered to
			the nodes in the workflow. It is a map having as keys the
			names of the nodes, while the values are dictionaries
			with keys the input slot names and values the input slot
			values.
	
		input_dir : str, optional
			Path to the directory holding the files that will accompany
			the workflow instantiation request.
			When setting input slots for files transferred within this 
			directory, their value should be set to their relative paths 
			within the input directory.
	
		Returns
		-------
		int
			The function returns an integer:
			  On success it returns the handle id of the instantiated workflow.
			  On failure it returns one of the following values:
			  -1    if 'workflow_handle_id' is invalid
			  -2    if 'input_slot_values' are invalid (i.e. the given value does not match the input slot variable type)
			  -10   if Client that runs in background failed to start
			  -20   if script execution encountered error
			  -21   if post-script variables were not correct
			  -40   if BAL is unavailable
			  -41   if resolution of parametric BAL encountered error
			  -100  if the user does not have respective privileges
			  -200  if an internal error has happened
	
		See Also
		--------
		spdrm.process.getDefinitionWorkflows, spdrm.process.abortWorkflow
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    input_slot_values = {"nodeA": {"file": "test_file.txt", "token": "ae9hf687abgk"}}
			    input_dir = "/scratch/test_data/workflow_files"
			    instance_id = spdrm.process.instantiateWorkflow(2062, input_slot_values, input_dir)
	
	
		"""
	
	def getStateOfWorkflow(workflow_id: int) -> object:
	
		"""
	
		This function queries SPDRM for a running workflow and returns information on 
		its current state.
	
		Parameters
		----------
		workflow_id : int
			Identifier of the running workflow
	
		Returns
		-------
		object
			The function returns a list [error_code, workflow_state, workflow_status]:
			error code:        int      0       if input is correct
			                           -1       if the provided workflow_id was not valid
			                           -100     if the user does not have respective privileges
			                           -200     if an internal error has happened
			workflow_state:    string           is a string with the workflow's state (Finished,Running,Ready)
			workflow_status:                    a WorkflowStatus object, providing more information 
			                                    about the current workflow state
	
		See Also
		--------
		spdrm.process.WorkflowStatus
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    workflow_id = 7210
			    ret = spdrm.process.getStateOfWorkflow(workflow_id)
			
			    if ret[0] == 0:
			        print("The state of the workflow is: {}".format(ret[1]))
	
	
		"""
	
	def updateNodeProgress(node_id: int, node_progress: float, user_data: object, dir: str) -> int:
	
		"""
	
		This function is invoked from the ANSA worker, executing a script as part of an
		SPDRM workflow. It reports to the SPDRM server the current progress for the 
		running node.
	
		Parameters
		----------
		node_id : int
			Handle id of the node for which progress is to be
			reported
	
		node_progress : float, optional
			The progress of the specific node, expressed as a 
			number from 0.0 to 1.0
	
		user_data : object, optional
			A string-to-string dictionary, holding arbitrary
			information that relates to the progress of the
			node
	
		dir : str, optional
			Path of a directory that contains files that are
			relevant to the progress of the node
	
		Returns
		-------
		int
			The function returns an integer:
			   0    on success
			  -1    if 'node_id' is invalid
			  -100  if the user does not have respective privileges
			  -200  if an internal error has happened
	
		See Also
		--------
		spdrm.process.getStateOfWorkflow
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    udata = {"phase": "translating"}
			    spdrm.process.updateNodeProgress(2809, node_progress=0.4, user_data=udata)
	
	
		"""
	
	def abortWorkflow(workflow_id: int) -> int:
	
		"""
	
		This function aborts the execution of a remotely running SPDRM workflow
	
		Parameters
		----------
		workflow_id : int
			Identifier of the running workflow
	
		Returns
		-------
		int
			The function returns an integer:
			   0    abort message was successfully signalled to workflow
			  -1    if 'workflow_id' is invalid
			  -100  if the user does not have respective privileges
			  -200  if an internal error has happened
	
		See Also
		--------
		spdrm.process.instantiateWorkflow, spdrm.process.getStateOfWorkflow
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    # Start and immediately abort an SPDRM workflow
			    instance_id = spdrm.process.instantiateWorkflow(2062, input_slot_values={})
			    if instance_id >= 0:
			        spdrm.process.abortWorkflow(instance_id)
	
	
		"""
	
	def getWorkflowFiles(workflow_id: int) -> object:
	
		"""
	
		This function fetches from the SPDRM server all files that have been stored on a
		specific workflow instance.
	
		Parameters
		----------
		workflow_id : int
			Identifier of the workflow instance
	
		Returns
		-------
		object
			The function returns a list [error_code, files_path, files_records]:
			error_code:     int      0       if input is correct
			                        -1       if workflow_id given is invalid
			                        -100     if the user does not have respective privileges
			                        -200     if an internal error has occurred
			files_path:     string           holds the path to the directory where the workflow
			                                 files were downloaded. In there, the different node
			                                 files are stored in directories named after the node
			                                 ids.
			files_records:  object           list of FilesRecord objects, each one of them
			                                 describing an SPDRM entity (node / workflow) +
			                                 all files that have been downloaded from this
			                                 entity
	
		See Also
		--------
		spdrm.process.FilesRecord
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def printFilesRecord(files_record):
			    print("**** Files Record ****")
			    print("Handle Id:", files_record.handle_id)
			    print("Entity Name:", files_record.entity_name)
			    print("Entity Type:", files_record.entity_type)
			    print("Entity Path:", files_record.entity_path)
			    print("Files:", str(files_record.files))
			
			
			def printFilesRecords(files_records):
			    for record in files_records:
			        printFilesRecord(record)
			
			
			def main():
			    workflow_id = 7210
			    ret = spdrm.process.getWorkflowFiles(workflow_id)
			
			    if ret[0] == 0:
			        print("The workflow files have been downloaded in path: {}".format(ret[1]))
			        printFilesRecords(ret[2])
	
	
		"""
	
	def getDefinitionActions(type: str) -> list:
	
		"""
	
		This function queries the current SPDRM for all actions, or for actions of a 
		specific type.
	
		Parameters
		----------
		type : str, optional
			If provided, the function will return the SPDRM actions of the specific type.
			Otherwise, all kinds of SPDRM actions will be returned.
			Allowed values: All, Generic, DMItem, LibraryItem, Container, Validation
			Default value: All
	
		Returns
		-------
		list
			This function returns a list of ActionDefinition objects
	
		See Also
		--------
		spdrm.process.ActionDefinition
	
		Examples
		--------
		::
	
			from meta import spdrm
			
			
			def printActionDefinition(action_def):
			    print("Id               :", action_def.id)
			    print("Name             :", action_def.name)
			    print("File Path        :", action_def.file_path)
			    print("ACLs             :", action_def.acls)
			    print("Script Function  :", action_def.script_function)
			    print("User Id          :", action_def.user_id)
			    print("Gsa Type         :", action_def.gsa_type)
			    print("DM Item Type     :", action_def.dm_item_type)
			    print("SPDRM Applicable :", action_def.spdrm_applicable)
			    print("ANSA Applicable  :", action_def.ansa_applicable)
			    print("META Applicable  :", action_def.ansa_applicable)
			    print("Root level       :", action_def.root_level)
			    print("Grouping path    :", action_def.grouping_path)
			    print("Overload         :", action_def.overload)
			    print("Generic like     :", action_def.generic_like)
			
			
			def main():
			    actions = spdrm.process.getDefinitionActions("Generic")
			    for run_action in actions:
			        printActionDefinition(run_action)
	
	
		"""
	
	def getPexDriver(url: str, pex_path: str) -> object:
	
		"""
	
		This function fetches a PEX Driver for a specific SPDRM server. If a PEX Driver
		to this SPDRM server has been created before it will immediately be reused,
		otherwise a new driver will be created.
	
		Parameters
		----------
		url : str
			URL of the SPDRM Server
	
		pex_path : str
			The path to the PEX application that is to be used with an SPDRM Server is
			advertised by the SPDRM Server itself and thus normally there is no need for
			the user to provide the path to the PEX executable. 
			In case the default PEX executable is to be overridden with a different one, this
			argument is used to provide the path to it.
	
		Returns
		-------
		object
			This function returns a PEXDriver object if one could successfully be created,
			or None if not.
	
		See Also
		--------
		spdrm.process.PexDriver
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    driver = spdrm.process.getPexDriver("http://spdrm-server:4567/")
			    print("Current state of PEX Driver is ", driver.state)
	
	
		"""
	
	class FilesRecord:
	
		"""
	
		The objects of this class are employed when the files of a workflow are to be
		accessed. For each workflow / node that had files downloaded, a FilesRecord 
		object is created. This object holds information on the entity and the files that 
		were downloaded
	
		See Also
		--------
		ansa.spdrm.process.getWorkflowFiles
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def printFilesRecord(files_record):
			    print("**** Files Record ****")
			    print("Handle Id:", files_record.handle_id)
			    print("Entity Name:", files_record.entity_name)
			    print("Entity Type:", files_record.entity_type)
			    print("Entity Path:", files_record.entity_path)
			    print("Files:", str(files_record.files))
			
			
			def printFilesRecords(files_records):
			    for record in files_records:
			        printFilesRecord(record)
			
			
			def main():
			    instance_id = 8963
			    res = spdrm.process.getWorkflowFiles(instance_id)
			    if res[0] == 0:
			        printFilesRecords(res[2])
	
		"""
	
	
		handle_id: int = None
		"""
		The handle id for the SPDRM entity
	
		"""
	
		entity_name: str = None
		"""
		The name of the SPDRM entity
	
		"""
	
		entity_type: str = None
		"""
		The type of the SPDRM entity (node / workflow)
	
		"""
	
		entity_path: str = None
		"""
		The logical path of this entity within the workflow
	
		"""
	
		files: object = None
		"""
		A dictionary where keys are the attribute names and values
		are the absolute paths where the corresponding files have 
		been downloaded to.
	
		"""
	class WorkflowDefinition:
	
		"""
	
		The objects of this class provide information on SPDRM Workflows
	
		See Also
		--------
		spdrm.process.getDefinitionWorkflows
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def main():
			    workflows = spdrm.process.getDefinitionWorkflows()
			    for w in workflows:
			        print("Workflow with Id ({}) and Name ({})".format(w.id, w.name))
	
		"""
	
	
		id: int = None
		"""
		The definition id of the workflow
	
		"""
	
		name: str = None
		"""
		The name of the workflow
	
		"""
	class WorkflowStatus:
	
		"""
	
		An object of this class provides information on the current status of an SPDRM
		Workflow instance.
	
		See Also
		--------
		spdrm.process.getStateOfWorkflow, spdrm.process.RunningNode
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def printRunningNode(node):
			    print("***** Running Node: {} *****".format(node.id))
			    print("  name:", node.name)
			    print("  start_time:", node.start_time)
			    print("  progress:", node.progress)
			    print("  user_data:", str(node.user_data))
			
			
			def printRunningNodes(nodes):
			    for run_node in nodes:
			        printRunningNode(run_node)
			
			
			def printWorkflowStatus(s):
			    print("***** Workflow Status *****")
			    print("  status:", s.status)
			    print("  error_msg:", s.error_msg)
			    print("  progress:", s.progress)
			
			    print("  running nodes: {} nodes".format(len(s.running_nodes)))
			    if len(s.running_nodes):
			        printRunningNodes(s.running_nodes)
			
			
			def main():
			    instance_id = 7054
			    res = spdrm.process.getStateOfWorkflow(instance_id)
			
			    workflow_status = res[2]
			    printWorkflowStatus(workflow_status)
	
		"""
	
	
		status: str = None
		"""
		Describes the current status of the workflow
	
		"""
	
		error_msg: str = None
		"""
		Provides more information in case of negative status
	
		"""
	
		progress: float = None
		"""
		Describes the workflow progress as a number between 0.0
		and 1.0
	
		"""
	
		running_nodes: object = None
		"""
		A list of RunningNode objects, providing details on all
		running workflow nodes.
	
		"""
	class RunningNode:
	
		"""
	
		The objects of this class provide information on a workflow's running nodes.
	
		See Also
		--------
		spdrm.process.WorkflowStatus, spdrm.process.getStateOfWorkflow, sprm.process.updateNodeProgress
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			
			def printRunningNode(node):
			    print("***** Running Node: {} *****".format(node.id))
			    print("  name:", node.name)
			    print("  start_time:", node.start_time)
			    print("  progress:", node.progress)
			    print("  user_data:", str(node.user_data))
			
			
			def printRunningNodes(nodes):
			    for run_node in nodes:
			        printRunningNode(run_node)
			
			
			def printWorkflowStatus(s):
			    print("***** Workflow Status *****")
			    print("  status:", s.status)
			    print("  error_msg:", s.error_msg)
			    print("  progress:", s.progress)
			
			    print("  running nodes: {} nodes".format(len(s.running_nodes)))
			    if len(s.running_nodes):
			        printRunningNodes(s.running_nodes)
			
			
			def main():
			    instance_id = 7054
			    res = spdrm.process.getStateOfWorkflow(instance_id)
			
			    workflow_status = res[2]
			    printWorkflowStatus(workflow_status)
	
		"""
	
	
		id: int = None
		"""
		The node's instance id
	
		"""
	
		name: str = None
		"""
		The name of the node
	
		"""
	
		start_time: str = None
		"""
		Timestamp when the node started running
	
		"""
	
		progress: float = None
		"""
		Describes the node progress as a number between 0.0
		and 1.0
	
		"""
	
		user_data: object = None
		"""
		A string-to-string dictionary holding arbitrary data about
		the progress of the node
	
		"""
	class ActionDefinition:
	
		"""
	
		The objects of this class provide information on SPDRM Actions
	
		See Also
		--------
		spdrm.process.getDefinitionActions
	
		Examples
		--------
		::
	
			from meta import spdrm
			
			
			def printActionDefinition(action_def):
			    print("Id               :", action_def.id)
			    print("Name             :", action_def.name)
			    print("File Path        :", action_def.file_path)
			    print("ACLs             :", action_def.acls)
			    print("Script Function  :", action_def.script_function)
			    print("User Id          :", action_def.user_id)
			    print("Gsa Type         :", action_def.gsa_type)
			    print("DM Item Type     :", action_def.dm_item_type)
			    print("SPDRM Applicable :", action_def.spdrm_applicable)
			    print("ANSA Applicable  :", action_def.ansa_applicable)
			    print("META Applicable  :", action_def.ansa_applicable)
			    print("Root level       :", action_def.root_level)
			    print("Grouping path    :", action_def.grouping_path)
			    print("Overload         :", action_def.overload)
			    print("Generic like     :", action_def.generic_like)
			
			
			def main():
			    actions = spdrm.process.getDefinitionActions("Generic")
			    for run_action in actions:
			        printActionDefinition(run_action)
	
		"""
	
	
		id: int = None
		"""
		The definition id of the action
	
		"""
	
		name: str = None
		"""
		The name of the action
	
		"""
	
		file_path: str = None
		"""
		The path of the action python script
	
		"""
	
		acls: object = None
		"""
		The ACLs (Access Control Lists) of the action are provided 
		as an array of dictionaries
	
		"""
	
		script_function: str = None
		"""
		The function which is used as an entry point for the action
		in the python script
	
		"""
	
		user_id: int = None
		"""
		The id of the action's owner
	
		"""
	
		gsa_type: str = None
		"""
		Information on the type of the action (Generic, DMItem,
		LibraryItem, Container, Validation)
	
		"""
	
		dm_item_type: str = None
		"""
		In case of DM Item scripts, this field provides information on 
		the DM Item types for which the action applies to (Part, Subsystem, etc.)
	
		"""
	
		spdrm_applicable: bool = None
		"""
		Reports whether the specific action is applicable for SPDRM Client
		execution contexts
	
		"""
	
		ansa_applicable: bool = None
		"""
		Reports whether the specific action is applicable for ANSA
		execution contexts
	
		"""
	
		meta_applicable: bool = None
		"""
		Reports whether the specific action is applicable for META
		execution contexts
	
		"""
	
		root_level: bool = None
		"""
		Reports whether the action is shown in root level in the context menu
	
		"""
	
		grouping_path: str = None
		"""
		The group name under which the specific action is shown in the context menu
	
		"""
	
		overload: str = None
		"""
		The action name that is overloaded by the current one
	
		"""
	
		generic_like: bool = None
		"""
		Describes whether this action is shown in the main menu as a generic like action
	
		"""
	class PexDriver:
	
		"""
	
		Objects of this class drive the interface towards an external PEX process.
	
		See Also
		--------
		spdrm.process.getPexDriver
	
		Examples
		--------
		::
	
			import time
			import meta
			from meta import spdrm
			
			
			def main():
			    driver = spdrm.process.getPexDriver("http://spdrm-server:4567/")
			    driver.start()
			
			    while driver.state == 1:
			        time.sleep(1)
			    workflows = driver.getDefinitionWorkflows()
			    print("Number of workflow definitions: ", len(workflows))
			
			    driver.executeScriptAction(2, [123, 456, 789], ["WIP"])
			
			    driver.shutdown()
	
		"""
	
	
		state: int = None
		"""
		This member returns the current state of the external PEX process as an integer:
		0      Initialized
		1      Starting up
		2      Ready / Idle
		3      Shutting Down
		4      Finished
		5      Error
	
		"""
	
		def start(self):
	
			"""
	
			Launches the external PEX process and connects to it
	
	
			"""
	
	
		def shutdown(self) -> bool:
	
			"""
	
			Shuts down the external PEX process
	
	
			Returns
			-------
			bool
				Returns True if the PEX process was in a running state and the shut down signal was successfully delivered.
	
			"""
	
	
		def getDefinitionWorkflows(self) -> object:
	
			"""
	
			Queries for the workflow definitions in the Process Library
	
	
			Returns
			-------
			object
				Returns a list of WorkflowDefinition objects
	
			"""
	
	
		def instantiateWorkflow(self, workflow_handle_id: int, input_slot_values: object, input_dir: str) -> int:
	
			"""
	
			Instantiates a workflow definition for execution in the external PEX process.
	
	
			Parameters
			----------
			workflow_handle_id : int
				Identifier of the workflow definition
	
			input_slot_values : object
				This argument provides the input values to be offered to
				the nodes in the workflow. It is a map having as keys the
				names of the nodes, while the values are dictionaries
				with keys the input slot names and values the input slot
				values.
	
			input_dir : str, optional
				Path to the directory holding the files that will accompany
				the workflow instantiation request.
				When setting input slots for files transferred within this 
				directory, their value should be set to their relative paths 
				within the input directory.
	
			Returns
			-------
			int
				On success it returns the handle id of the instantiated workflow.  On failure it returns one of the following values: -1 if 'workflow_handle_id' is invalid. -2 if 'input_slot_values' are invalid (i.e. the given value does not match the input slot variable type). -100 if the user does not have respective privileges. -200 if an internal error has happened.
	
			"""
	
	
		def getStateOfWorkflow(self, workflow_id: int) -> object:
	
			"""
	
			Queries the external PEX process for a running workflow and returns information on its current state.
	
	
			Parameters
			----------
			workflow_id : int
				Identifier of the running workflow
	
			Returns
			-------
			object
				The function returns a list [error_code, workflow_state, workflow_status]. The 'error code' is an integer with possible values: 0 if input is correct. -1 if the provided workflow_id was not valid. -100 if the user does not have respective privileges. -200 if an internal error has happened. The 'workflow_state' element is a string hold the workflow's state (Finished, Running, Ready). The 'workflow_status' is a WorkflowStatus object, providing more information about the current workflow state.
	
			"""
	
	
		def executeScriptAction(self, action_handle_id: int, dm_item_ids: object, fun_args: object) -> bool:
	
			"""
	
			Launches a Script Action in the external PEX process
	
	
			Parameters
			----------
			action_handle_id : int
				Identifier of the action
	
			dm_item_ids : object, optional
				In case of DMItem Action, this argument provides the ids
				of the items on which the action should be applied, as a
				sequence of integers.
	
			fun_args : object, optional
				The arguments to be provided to the script entry
				function, as a sequence of standard python types.
	
			Returns
			-------
			bool
				Returns True if the script action was successfully launched
	
			"""
	
	def isRootConnectionValid() -> bool:
	
		"""
	
		This function checks if an existing connection to an SPDRM environment for process management is valid.
	
		Returns
		-------
		bool
			The function returns:
			  True     if the connection is valid
			  False    if the connection is invalid
	
		Examples
		--------
		::
	
			def main():
			    if spdrm.process.isRootConnectionValid():
			        print("Connection to current SPDRM back-end for process management is valid.")
			    else:
			        print("Connection to current SPDRM back-end for process management is lost.")
	
	
		"""
	
	def getTicket() -> str:
	
		"""
	
		This function returns the authentication ticket of an existing connection to an SPDRM environment for process management.
	
		Returns
		-------
		str
			The function returns the existing ticket as a string.
	
		"""
	
	def getNodeInputFiles(node_id: int, input_slots: str='all_slots') -> tuple:
	
		"""
	
		This function returns the input files that are passed to a process node that is executed in a remote SPDRM environment via the respective slots.
	
		Parameters
		----------
		node_id : int
			The id of the node
	
		input_slots : str, optional
			Filters the input files depending on the slot type. Accepted values:
			- 'all_slots'
			- 'connected_slots'
	
		Returns
		-------
		tuple
			Returns a tuple containing the export directory, the return code and the error message. Possible return codes:
			*   0: Success
			*  -1: Invalid node id
			* -14: Nothing to export
	
		Examples
		--------
		::
	
			import meta
			from meta import spdrm
			
			# Assuming that a node of a workflow with ID = 14258 is running
			dir, res, msg = meta.spdrm.process.getNodeInputFiles(14258)
			
			if res != 0:
			    print(msg)
			else:
			    print("Exported files in: ", dir)
	
	
		"""
	
	def getAvailableBALs() -> list:
	
		"""
	
		Get all the registered BETA Apps Launchers of an SPDRM environment.
	
		Returns
		-------
		list
			The function returns:
			- a list with the names of the registered BALs as strings, on success
			  (if no BAL is registered, an empty list is returned)
			- a tuple with (error_code, error_description), in case of errors
	
		"""
	
	def getBALApps(bal: str) -> list:
	
		"""
	
		Get all available Applications that are configured in the application.properties configuration file of a BETA Apps Launcher server.
	
		Parameters
		----------
		bal : str
			is the name of the BETA Apps Launcher, as appears in the BETA Apps Launcher Monitor.
	
		Returns
		-------
		list
			The function returns:
			- a list of dictionaries, on sucess
			  Each dictionary contains info of a BAL Application. The keys of each dictionary provide info for the following:
			    - path (e.g. '/mnt/ANSA/ansa64.sh')
			    - title (e.g.'ANSA_v23.1.1')
			    - type (e.g. 'ANSA')
			    - version (e.g. 'v23.1.1')
			- a tuple with (error_code, error_description), in case of errors
	
		See Also
		--------
		spdrm.process.getAvailableBALs
	
		"""
	
	