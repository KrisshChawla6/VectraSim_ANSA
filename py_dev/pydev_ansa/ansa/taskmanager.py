from __future__ import annotations
from typing import *

def AparameterTaskItemLinkToAparameter(task_item_ref: object, ansa_parameter_ref: object, expression: str) -> int:

	"""

	Associates an A_PARAMETER task item of a design variable in the optimization task with an A_PARAMETER.

	Parameters
	----------
	task_item_ref : object
		The task item object.

	ansa_parameter_ref : object
		APARAM object.

	expression : str, optional
		expression to be used when executing the item from the optimization task. Use "$DV" to get Current Value of the Design variable.

	Returns
	-------
	int
		Returns 0 on success, -1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import taskmanager
		from ansa import constants
		
		
		def main():
		    name = "new_parameter"
		    create_vals = {"Name": name, "value": 15}
		    param = base.CreateEntity(constants.NASTRAN, "A_PARAMETER", create_vals)
		    expr = "=" + name
		    prop = base.GetEntity(constants.NASTRAN, "PSHELL", 1)
		    vals = {"T": expr}
		    base.SetEntityCardValues(constants.NASTRAN, prop, vals)
		
		    opt_task = taskmanager.CreateTaskItem("Optimization item", None)
		    prepro = taskmanager.CreateTaskItem("Pre-Processing", opt_task)
		    design_variable_task_item = taskmanager.CreateTaskItem("Design Variable", prepro)
		    param_task_item = taskmanager.CreateTaskItem(
		        "A_PARAMETER", design_variable_task_item
		    )
		    taskmanager.AparameterTaskItemLinkToAparameter(
		        param_task_item, param, expression="$DV+1"
		    )


	"""

def ChangeTaskItem(task_item_ref: object) -> int:

	"""

	The function changes the status of a task item from checked to unchecked.

	Parameters
	----------
	task_item_ref : object
		The task item whose status will be switched to unchecked.
		Can be obtained using GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	int
		Return Value:
		0: The Task Item unupdated succesfuly.
		1: The Task Item failed to unupdate.
		-1: No such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Get all task items named "MyModelAssembly"
		    model_assembly = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    # Uncheck the first item in the model_assembly list
		    ret_val = taskmanager.ChangeTaskItem(model_assembly[0])
		    print(ret_val)


	"""

def ClearBreakTaskItem(task_item_ref: object) -> int:

	"""

	Parameters
	----------
	task_item_ref : object
		The Task Item to remove the break from.
		It can be obtained by a call to GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	int
		1: the break on the Task Item was removed.
		-1: no such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    model_assembly = taskmanager.GetTaskItemsByName("My Model Assembly")
		    taskmanager.ClearBreakTaskItem(model_assembly[0])


	"""

def CreateTaskItem(task_item_type: str, target_task_item_ref: object) -> object:

	"""

	The function creates a new task item in Task Manager. The item type must be given
	exactly as it is displayed in the type field of Task Manager, e.g "Common Model", 
	"Trim Item", "Read XML file" etc. The new item will be created under the 
	target task item.

	Parameters
	----------
	task_item_type : str
		String that determines the type of the task item to be created.

	target_task_item_ref : object
		Target task item. The task item under which the newly created one will be placed.

	Returns
	-------
	object
		Returns a reference to the newly created item, or None in case of error.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Start with an empty task tree
		    # Create a Common Model task item
		    new_item = taskmanager.CreateTaskItem("Common Model", None)
		
		    # Create a Model Assembly task item under the Common Model
		    new_item2 = taskmanager.CreateTaskItem("Model Assembly", new_item)


	"""

def DeleteTaskItem(task_item: object, delete_results: str) -> int:

	"""

	The function deletes the defined task item.

	Parameters
	----------
	task_item : object
		The task item that will be deleted. Can be obtained by using GetTaskItemsByName() or 
		GetTaskItemsByType().

	delete_results : str, optional
		Accepted values: "on" or "off". 
		(Default: "off")

	Returns
	-------
	int
		Returns:
		0: The Task Item was deleted succesfuly.
		1: The Task Item failed to delete.
		-1: No such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Get task items named "Refinement"
		    items = taskmanager.GetTaskItemsByName("Refinement")
		
		    for item in items:
		        # delete collected task items
		        taskmanager.DeleteTaskItem(item)


	"""

def DisableTaskItem(task_item_ref: object) -> int:

	"""

	The function disables (marks as skipped) the prescribed task item.

	Parameters
	----------
	task_item_ref : object
		The task item which will disbaled. Can be obtained using GetTaskItemsByName() or 
		 GetTaskItemsByType().

	Returns
	-------
	int
		Returns:
		0: The Task Item was succesfuly disabled.
		1: The Task Item failed to disable.
		-1: No such Task Item existed.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items of type "Abaqus Standard Load Case"
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		    for loadcase in loadcases:
		        # Disable collected task items
		        taskmanager.DisableTaskItem(loadcase)


	"""

def EditCommentsTaskItem(task_item_ref: object, comment: str) -> int:

	"""

	The function sets a comment to the comments field of a task item.

	Parameters
	----------
	task_item_ref : object
		The task item whose comments field will be edited. Can be
		obtained by using GetTaskItemsByName() or GetTaskItemsByType().

	comment : str
		The string that will be inserted as a comment.

	Returns
	-------
	int
		1: The comment on the Task Item was set.
		-1: No such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items whose name is "MyModelAssembly"
		    tasks = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    for task in tasks:
		        # Edit the Comments field of the collected items
		        taskmanager.EditCommentsTaskItem(task, "This is a test comment")


	"""

def EnableTaskItem(task_item_ref: object) -> int:

	"""

	The function enables (unmark as skipped) the prescribed task item. 

	Parameters
	----------
	task_item_ref : object
		The task item which will be enabled. Can be obtained by using 
		the GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	int
		Returns:
		0, if the Task Item was successfully enabled.
		1, if the Task Item failed to enable.
		-1, if there is no such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items of type "Abaqus Standard Load Case"
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		
		    for loadcase in loadcases:
		        # Enable collected task items
		        taskmanager.EnableTaskItem(loadcase)


	"""

def ExecTaskItemMenuFun(task_item_ref: object, item_subfunction_name: str) -> int:

	"""

	Executes any subfunction of a task item context menu. The subfunction name must be given 
	exactly as it is displayed in the context menu.

	Parameters
	----------
	task_item_ref : object
		The task item from the context menu of which, a subfunction will be selected.

	item_subfunction_name : str
		The name of the subfunction.

	Returns
	-------
	int
		Returns 0 on success and -1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items named "ModelAssembly"
		    common = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    # Execute the "Convert From Model" option of the context menu
		    taskmanager.ExecTaskItemMenuFun(common[0], "Convert From Model")


	"""

def GetAllTaskItems() -> object:

	"""

	Returns all task items regardless of their type/name.

	Returns
	-------
	object
		Returns a list with the elements of all task items.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetAllTaskItems()
		    for item in items:
		        name = taskmanager.GetTaskItemName(item)
		        print(name)


	"""

def GetCommentsTaskItem(task_item_ref: object) -> str:

	"""

	The function obtains the entry of the comment field of a task item.

	Parameters
	----------
	task_item_ref : object
		The task item whose comment field will be obtained. Can be obtained 
		by a call to GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	str
		Returns a string that contains the comment of the task item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items in the task tree
		    tasks = taskmanager.GetAllTaskItems()
		
		    for task in tasks:
		        if taskmanager.GetCommentsTaskItem(task):
		            # Print the comment if it exists
		            print(taskmanager.GetCommentsTaskItem(task))
		        else:
		            # Print "Empty Comment" otherwise
		            print("Empty Comment")


	"""

def GetRootTaskManager() -> object:

	"""

	Function that returns a reference to the task manager root.

	Returns
	-------
	object
		Returns a reference to the root task manager.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		from ansa import base
		from ansa import constants
		
		
		def main():
		    # Get a reference to task manager root
		    task_manager = taskmanager.GetRootTaskManager()
		
		    # Collect all Shell elements placed under control of the task manager
		    shells = base.CollectEntities(constants.NASTRAN, task_manager, "SHELL", True)
		
		    # Print message
		    print("Number of solids: ", len(shells))


	"""

def GetRunningTaskItem() -> object:

	"""

	Gets a reference to the element of the running task item. The running item is a script.
	It can be used in cases where a script item is placed inside a task more than once and 
	performs every time that is called different actions.

	Returns
	-------
	object
		Returns a reference to the running task item, or None if the running item is not found.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    script_task_item = taskmanager.GetRunningTaskItem()
		    print(taskmanager.GetTaskItemName(script_task_item))


	"""

def GetTaskItemChildren(task_item_ref: object, method: int) -> object:

	"""

	The function gets the children of the selected parent task item.

	Parameters
	----------
	task_item_ref : object
		The task item whose children will be obtained.

	method : int
		The method that will be used.
		Valid types:
		-1: Returns all children.
		-0: Returns first level children.

	Returns
	-------
	object
		Returns a list that contains the repsective task items.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Get task items named "Common Model"
		    common = taskmanager.GetTaskItemsByName("Common Model")
		
		    # Get 1st level children of the fist instance of "Common Model"
		    children = taskmanager.GetTaskItemChildren(common[0], 0)
		
		    for child in children:
		        print(taskmanager.GetTaskItemName(child))


	"""

def GetTaskItemName(task_item: object) -> str:

	"""

	The function obtains the name of the prescribed task item.

	Parameters
	----------
	task_item : object
		The task item whose name will be obtained.

	Returns
	-------
	str
		Returns a string containing the name of the task item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect "Abaqus Standard Load Case" task items
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		
		    for loadcase in loadcases:
		        # Get the name of each task item in the list
		        loadcase_name = taskmanager.GetTaskItemName(loadcase)
		        print(loadcase_name)


	"""

def GetTaskItemStatus(task_item_ref: object) -> int:

	"""

	The function obtains the status of the defined task item.

	Parameters
	----------
	task_item_ref : object
		The task item whose status will be obtained.

	Returns
	-------
	int
		Returns one of the following integers:
		0: The Task Item is not updated (not ticked).
		1: The Task Item is updated (ticked).
		2: The Task Item is disabled.
		-1: No such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all "Abaqus Standard Load Case" task items
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		    for loadcase in loadcases:
		        # Get the status of each task item in the list
		        status = taskmanager.GetTaskItemStatus(loadcase)
		        print(status)


	"""

def GetTaskItemType(task_item_ref: object) -> str:

	"""

	The function obtains the type of the prescribed task item.

	Parameters
	----------
	task_item_ref : object
		The task item whose type will be obtained.

	Returns
	-------
	str
		Returns a string representing the type of the given task item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all the task items named "Common Model"
		    common = taskmanager.GetTaskItemsByName("Common Model")
		    # Collect the 1st level children of the first instance of "Common Model"
		    children = taskmanager.GetTaskItemChildren(common[0], 0)
		
		    for child in children:
		        # For each task item in the list get and print its type
		        print(taskmanager.GetTaskItemType(child))


	"""

def GetTaskItemsByName(name: str) -> object:

	"""

	The function collects all task item of a specific name.

	Parameters
	----------
	name : str
		The name of the task items to be collected.

	Returns
	-------
	object
		Returns a list of all the matched Task Items.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items named "MyModelAssembly"
		    items = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    for item in items:
		        # Print the type of each task item in the list
		        print(taskmanager.GetTaskItemType(item))


	"""

def GetTaskItemsByType(type: str) -> object:

	"""

	The function collects all the task items of a specific type.

	Parameters
	----------
	type : str
		The type of the task items to be collected. Must be set exactly as it 
		is written in the type field of the Task Manager.

	Returns
	-------
	object
		Returns a list of all the matched Task Items.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task items of type "Abaqus Standard Load Case"
		    items = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		
		    for item in items:
		        # Print the Name of each task item in the list
		        print(taskmanager.GetTaskItemName(item))


	"""

def MorphparameterTaskItemLinkToMorphparameter(task_item_ref: object, morph_parameter_ref: object, after_morph_action: str, expression: str) -> int:

	"""

	Associates a MORPHPARAMETER task item of a design variable in the optimization task with a morph PARAMETER.

	Parameters
	----------
	task_item_ref : object
		A task item object.

	morph_parameter_ref : object
		A morph parameter object.

	after_morph_action : str, optional
		Can have 2 values "Reconstruct" or "Smooth"

	expression : str, optional
		expression to be used when executing the item from the optimization task. Use "$DV" to get Current Value of the Design variable.

	Returns
	-------
	int
		Returns 0 on success, 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		from ansa import base
		from ansa import constants
		
		
		def main():
		    param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 1)
		    opt_task = taskmanager.CreateTaskItem("Optimization item", None)
		    prepro = taskmanager.CreateTaskItem("Pre-Processing", opt_task)
		    design_variable_task_item = taskmanager.CreateTaskItem("Design Variable", prepro)
		    param_task_item = taskmanager.CreateTaskItem(
		        "MORPH PARAMETER", design_variable_task_item
		    )
		
		    taskmanager.MorphparameterTaskItemLinkToMorphparameter(param_task_item, param)


	"""

def MoveTaskItem(task_item_ref_to_move: object, target_task_item_ref: object, drop_position: str) -> int:

	"""

	Moves the given task item into another item.

	Parameters
	----------
	task_item_ref_to_move : object
		The task item that will be moved.

	target_task_item_ref : object
		The task item under which the moving 
		task item will be placed.

	drop_position : str, optional
		drop_position can have 3 options
		"OnTarget", "BelowTarget" and "AboveTarget"

	Returns
	-------
	int
		1 : Succesfully moved.
		0 : Failed to move.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Get task items named "MyModelAssembly"
		    model_assembly = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    # Get task items named "User Script"
		    tasks = taskmanager.GetTaskItemsByName("User Script")
		
		    for task in tasks:
		        # Place each item in the list under the first instance of model_assembly
		        taskmanager.MoveTaskItem(task, model_assembly[0])


	"""

def OpenTaskManager() -> int:

	"""

	Opens the Task manager window.

	Returns
	-------
	int
		Always returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    taskmanager.OpenTaskManager()


	"""

def ReadTask(task_filename: str) -> int:

	"""

	The function reads a specific task.

	Parameters
	----------
	task_filename : str
		A string that describes the path and the filename of the ANSA 
		database that contains the task. It can be DM relative.

	Returns
	-------
	int
		Always returns 0.

	See Also
	--------
	taskmanager.SaveTask

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    taskmanager.ReadTask("DM:/Tasks/CommonModel.ansa")


	"""

def RunAllTasks() -> int:

	"""

	Runs all tasks that exist in database.

	Returns
	-------
	int
		Returns:
		0: If all Task Items updated (run) succesfuly.
		1: If any Task Item failed to update (run).

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    taskmanager.RunAllTasks()


	"""

def SetBreakTaskItem(item: object) -> int:

	"""

	Parameters
	----------
	item : object
		The Task Item to set a break on it can be obtained by a call to 
		GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	int
		Returns:
		 1: If the break on the Task Item was set.
		-1: If no such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		    for loadcase in loadcases:
		        taskmanager.SetBreakTaskItem(loadcase)


	"""

def SetOutputTaskItemName(task_item_ref: object, new_name_str: str) -> int:

	"""

	This function changes the Output Task Item's exported file name.

	Parameters
	----------
	task_item_ref : object
		A reference to the task item.

	new_name_str : str
		The new path and file name of the exported file.

	Returns
	-------
	int
		Returns:
		 0, on success.
		 1, if failed to name the exported file.
		-1, if there is no such Task Item.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Collect all task item of "Output" type
		    OutputItems = taskmanager.GetTaskItemsByType("Output")
		
		    for OutputItem in OutputItems:
		        # Set a path and file name for each item in the list
		        taskmanager.SetOutputTaskItemName(OutputItem, "c:/temp/users/folder/data.inp")


	"""

def SetTaskItemName(task_item_ref: object, new_name_str: str) -> int:

	"""

	The function renames a task item.

	Parameters
	----------
	task_item_ref : object
		The task item that will be renamed.

	new_name_str : str
		The new name of the task item.

	Returns
	-------
	int
		Returns:
		 0: On sucess. 
		 1: On failure to rename the Task Item.
		-1: If no such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    counter = 1
		    loadcase_name = "Load_position_"
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		
		    for loadcase in loadcases:
		        name = loadcase_name + str(counter)
		        taskmanager.SetTaskItemName(loadcase, name)
		        counter += 1


	"""

def SetToscaOptResultsDir(task_item_ref: object, directory_str: str) -> int:

	"""

	Parameters
	----------
	task_item_ref : object
		The Task Item (GENERATE_REPORT_FILE or RUN_SMOOTH).

	directory_str : str
		The directory with the optimization results.

	Returns
	-------
	int
		Returns:
		 0: On success.
		 1: On failure name the exported file.
		-1: If no such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    RunSmoothItems = taskmanager.GetTaskItemsByType("RUN_SMOOTH")
		    for item in RunSmoothItems:
		        taskmanager.SetToscaOptResultsDir(item, "C:/temp/users/folder/data.inp")


	"""

def UpdateTaskItem(task_item_ref: object) -> int:

	"""

	The function runs the specified task item.

	Parameters
	----------
	task_item_ref : object
		The task item to be executed. Can be obtained by using 
		the functions GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	int
		Returns:
		 0, The Task Item was succesfuly updated.
		 1, The Task Item failed to update.
		-1, No such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    # Get all task items named "MyModelAssembly"
		    model_assembly = taskmanager.GetTaskItemsByName("MyModelAssembly")
		
		    # Run the first item in the model_assembly list
		    ret_val = taskmanager.UpdateTaskItem(model_assembly[0])
		    print(ret_val)


	"""

def GetTaskUserScriptData(task_item: object) -> object:

	"""

	Gets the data of a task manager user script.

	Parameters
	----------
	task_item : object
		The task item whose data will be returned.

	Returns
	-------
	object
		Returns a dictionary containing the following information for 
		the given task manager user script:
		module file name:   (module_fname)
		function name:      (function_name)
		arguments:          (arguments)

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetTaskItemsByType("User Script")
		
		    for item in items:
		        data = taskmanager.GetTaskUserScriptData(item)
		        print("Function name:", data["function_name"])


	"""

def SetTaskUserScriptData(task_item: object, script_data: object) -> int:

	"""

	Sets the data to a task manager user script.

	Parameters
	----------
	task_item : object
		The task item of which the data will be edited.

	script_data : object
		A dictionary containing the information to be set
		The entries of the dictionary are:
		-module_fname: module file name
		-function_name: function name
		-arguments: arguments
		-store_results: "on" "off"

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetTaskItemsByType("User Script")
		
		    for item in items:
		        data = {
		            "module_fname": "/home/user/an_ansa_python_mod.py",
		            "function_name": "my_function",
		            "arguments": "100,200",
		        }
		        taskmanager.SetTaskUserScriptData(item, data)


	"""

def SaveTask(filename: str) -> int:

	"""

	The function saves all the task items of the TaskManager.

	Parameters
	----------
	filename : str
		A string that describes the path and the filename of the ANSA 
		database, that the task items will be saved.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	See Also
	--------
	taskmanager.ReadTask

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    taskmanager.SaveTask("/home/user/Tasks/CommonModel.ansa")


	"""

def TaskTemplateItem(template_name: str, template_reference: str, template_arguments: str, template_tip: str, template_icon: str) -> None:

	"""

	A decorator that adds a User Script task item.
	It must be placed above the definition of the function which you want to be executed
	when called.

	Parameters
	----------
	template_name : str
		The name of the Task item

	template_reference : str, optional
		The name of the specific Task item's context menu to show

	template_arguments : str, optional
		The arguments to pass in the created User Script

	template_tip : str, optional
		The tip to show on the User Script task item

	template_icon : str, optional
		The icon to show on the User Script task item

	Returns
	-------
	None

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		
		
		@ansa.taskmanager.TaskTemplateItem("TemplateFun1")
		def TemplateFun1main():
		    # function code
		    pass
		
		
		# will be available only for "Pre-Processing" items
		@ansa.taskmanager.TaskTemplateItem("TemplateFun2", "Pre-Processing")
		def TemplateFun2main():
		    # function code
		    pass
		
		
		# will be available only for "Pre-Processing" items with "Script_args"
		@ansa.taskmanager.TaskTemplateItem("TemplateFun3", "Pre-Processing", '"Script_args"')
		def TemplateFun3main(args):
		    # function code
		    pass
		
		
		# will be available only for "Pre-Processing" items with "Script_args" and tooltip "Script_tool_tip"
		@ansa.taskmanager.TaskTemplateItem(
		    "TemplateFun4", "Pre-Processing", '"Script_args"', '"Script_tool_tip"'
		)
		def TemplateFun4main(args):
		    # function code
		    pass
		
		
		# will be available only for "Pre-Processing" items with "Script_args" and tooltip "Script_tool_tip" and icon "gear_small.svg"
		@ansa.taskmanager.TaskTemplateItem(
		    "TemplateFun5",
		    "Pre-Processing",
		    '"Script_args"',
		    '"Script_tool_tip"',
		    "gear_small.svg",
		)
		def TemplateFun5main(args):
		    # function code
		    pass


	"""

def SetSolverItemData(solver_item: object, solver_type: str, output_item: object, solver_command: str, solver_options: str, solver_session: str) -> int:

	"""

	Sets the data to a task manager solver item

	Parameters
	----------
	solver_item : object
		The Solvet task item

	solver_type : str
		Solver type string, it can be one of:
		'Epilysis'
		'NASTRAN'
		'LS-DYNA'
		'PAM-CRASH'
		'ABAQUS'
		'RADIOSS'
		'ANSYS'
		'FLUENT'
		'FLUENT-2D'
		'STAR'
		'UH3D'
		'CFD++'
		'OPENFOAM'
		'PERMAS'
		'MOLDEX3D'
		'TAITHERM'
		'SESTRA'
		'THESEUS'
		'SC/TETRA'
		'TAU'
		'CGNS'
		'CGNS-2D'
		'OPTISTRUCT'
		'MARC'
		'ACTRAN'
		'KINETICS
		'User defined'

	output_item : object, optional
		Output item to use for solving

	solver_command : str, optional
		Solver command to use

	solver_options : str, optional
		Solver options

	solver_session : str, optional
		Session file for CFD Solvers

	Returns
	-------
	int
		Return -1 for error, 0 for success and 1 for failure

	Examples
	--------
	::

		import os
		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetTaskItemsByType("Optimization item")
		
		    solver_item = taskmanager.CreateTaskItem("Solver", items[0])
		
		    output_task_item = taskmanager.GetTaskItemsByName("./biw_final.nas")
		    taskmanager.SetSolverItemData(
		        solver_item=solver_item,
		        solver_type="NASTRAN",
		        output_item=output_task_item[0],
		        solver_command="./nastran",
		        solver_options=' "./biw_final.nas" bat=no',
		    )


	"""

def SetPostProcessingItemData(post_item: object, post_command: str, post_session: str, post_directory: str, post_response: str, post_options: str) -> int:

	"""

	Sets the data to a task manager Post-Processing item

	Parameters
	----------
	post_item : object
		The Post-Processing task item

	post_command : str, optional
		The Meta command, will use the default if empty

	post_session : str, optional
		The session file, will look in current directory if empty

	post_directory : str, optional
		The output directory, current if empty

	post_response : str, optional
		The meta response file

	post_options : str, optional
		the Meta command options

	Returns
	-------
	int
		Return -1 for error, 0 for success and 1 for failure

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetTaskItemsByType("Optimization item")
		    post_item = taskmanager.CreateTaskItem("Post-Processing", items[0])
		    taskmanager.SetPostProcessingItemData(
		        post_item=post_item,
		        post_command="./meta_post64.sh",
		        post_session="./max_stress.ses",
		        post_directory="./",
		        post_response="max_stress.ses.results",
		        post_options=" -noses -nolog -b -foregr -s $SES $DIR  $RES",
		    )


	"""

def LCPointsFisrtTorsionalWizard(nodes_lc_points: object) -> object:

	"""

	Wizard to create LC_POINTS to be used in order to calculate the First Torsional Mode

	Parameters
	----------
	nodes_lc_points : object, optional
		A nodes list to create the LC_POINTS

	Returns
	-------
	object
		A list with the created LC_POINTS

	Examples
	--------
	::

		import os
		import ansa
		
		
		def main():
		    lcPoints = taskmanager.LCPointsFisrtTorsionalWizard(None)


	"""

def GetTaskItemParents(task_item_ref: object, parent_level: bool) -> object:

	"""

	Function to get the parents of the given item

	Parameters
	----------
	task_item_ref : object
		The task item to get its parents

	parent_level : bool, optional
		True: Returns all parents.
		False: Returns first level parents.
		default value True

	Returns
	-------
	object
		A list with the parent items

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from ansa import taskmanager
		
		
		def main():
		    items = taskmanager.GetTaskItemsByType("User Script")
		
		    for item in items:
		        parents = taskmanager.GetTaskItemParents(item)
		        print(parents)
		    for item in items:
		        parents = taskmanager.GetTaskItemParents(item, False)
		        print(parents)


	"""

def SetTaskItemIcon(task_item: object, icon_name: str) -> int:

	"""

	The function sets an icon to a task item.

	Parameters
	----------
	task_item : object
		The task item which icon will be changed

	icon_name : str
		The icon path or the icon name for the embedded icons

	Returns
	-------
	int
		Returns:
		 0: On sucess. 
		 1: On failure to set the icon
		-1: If no such Task Item exists.

	Examples
	--------
	::

		import ansa
		from ansa import taskmanager
		
		
		def main():
		    counter = 1
		    loadcase_name = "Load_position_"
		    loadcases = taskmanager.GetTaskItemsByType("Abaqus Standard Load Case")
		
		    for loadcase in loadcases:
		        taskmanager.SetTaskItemIcon(loadcase, "C:\\data\\icons\\loadcase_icons.png")
		        counter += 1


	"""

def SetResponseItemData(response_item: object, ansa_entity: object, ansa_field: str) -> int:

	"""

	Sets the data to a task manager Response item

	Parameters
	----------
	response_item : object
		The response item

	ansa_entity : object
		The ansa entity to retrive response

	ansa_field : str
		The ansa field to monitor

	Returns
	-------
	int
		Return -1 for error, 0 for success and 1 for failure

	Examples
	--------
	::

		import os
		import ansa
		from ansa import base, constants, taskmanager
		
		
		def main():
		    main_items = ansa.taskmanager.GetTaskItemsByName("OPTIMIZATION_TASK_1")
		    if len(main_items) == 1:
		        opt_task_m = main_items[0]
		        taskmanager.ExecTaskItemMenuFun(opt_task_m, "Definition")
		    else:
		        opt_task_m = taskmanager.CreateTaskItem("Optimization item", None)
		        setName = taskmanager.SetTaskItemName(opt_task_m, "OPTIMIZATION_TASK_1")
		    opt_task_pre = taskmanager.CreateTaskItem("Pre-Processing", opt_task_m)
		    item = taskmanager.CreateTaskItem("Response Item", opt_task_pre)
		    setName = taskmanager.SetTaskItemName(item, "MEASUREMENT_1_RESULT")
		
		    p_aent = base.GetEntity(ansa.base.CurrentDeck(), "MEASUREMENT", 1)
		    ansa_field = "RESULT"
		    taskmanager.SetResponseItemData(item, p_aent, ansa_field)


	"""

def GetEntityFieldFromAnsaParam(ansa_param: object) -> object:

	"""

	The function returns the entity and the field referenced from the A_PARAMETER

	Parameters
	----------
	ansa_param : object
		The task item whose fields will be obtained. Can be obtained 
		by a call to GetTaskItemsByName() or GetTaskItemsByType().

	Returns
	-------
	object
		Returns a dictionary with [entity, card_field]

	Examples
	--------
	::

		# PYTHON script
		import os
		from ansa import *
		
		
		def main():
		    a_params = taskmanager.GetTaskItemsByType("A_PARAMETER")
		    for ap in a_params:
		        dict = taskmanager.GetEntityFieldFromAnsaParam(ap)
		        print(dict)


	"""

def SetDOESingleAction(task_item: object, item_action: str) -> int:

	"""

	set when the action will be executed

	Parameters
	----------
	task_item : object
		The DOESingleAction task item

	item_action : str
		The action, valid values:
		"On start up" and "At the end"

	Returns
	-------
	int
		Return 0 for succes, 1 for failure

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import taskmanager
		from ansa import constants
		
		
		def main():
		    items = taskmanager.GetTaskItemsByName("OPTIMIZATION_TASK_1")
		    if len(items) == 0:
		        return 1
		
		    single_action = taskmanager.CreateTaskItem("DOESingleActions", items[0])
		    taskmanager.SetDOESingleAction(single_action, "On start up")
		    new_item = taskmanager.CreateTaskItem("User Script", single_action)
		    name = "function_name_1"
		    data = {"module_fname": "my_script.py", "function_name": name}
		    taskmanager.SetTaskUserScriptData(new_item, data)
		    taskmanager.SetTaskItemName(new_item, name)
		
		    single_action = taskmanager.CreateTaskItem("DOESingleActions", items[0])
		    taskmanager.SetDOESingleAction(single_action, "At the end")
		    new_item = taskmanager.CreateTaskItem("User Script", single_action)
		    name = "function_name_2"
		    data = {"module_fname": "my_script.py", "function_name": name}
		    taskmanager.SetTaskUserScriptData(new_item, data)
		    taskmanager.SetTaskItemName(new_item, name)
		
		
		main()


	"""

