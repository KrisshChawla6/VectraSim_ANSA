from __future__ import annotations
from typing import *

def CheckBreak() -> int:

	"""

	A function to check, in execution time, if the Escape(ANSA)/Pause(META) button is pushed.

	Returns
	-------
	int
		Returns:
		0, If the specific button is not pushed.
		1, If the specific button is pushed.

	Examples
	--------
	::

		import meta
		from meta import betascript
		
		
		def main():
		    for i in range(1, 10000):
		        print(i)
		        if betascript.CheckBreak():
		            break


	"""

def RunPluginFunction(plugin_module_name: str, group_name: str, button_label: str):

	"""

	This function is used to call a plugin function from script.

	Parameters
	----------
	plugin_module_name : str
		The name of the plugin [ppl/bpl] without suffix.

	group_name : str
		The group name. An empty string if there is no group.

	button_label : str
		The label of the specified button in plugins toolbar.

	Examples
	--------
	::

		import meta
		from meta import betascript
		
		
		def myFunction():
		    betascript.RunPluginFunction("PluginModuleName", "GroupName", "PluginButtonLabel")


	"""

def FindModule(module_name: str) -> object:

	"""

	This function returns the module object of a loaded script.
	Takes as argument the name of the wanted module.

	Parameters
	----------
	module_name : str
		The name of the wanted module.

	Returns
	-------
	object
		Returns the module object with the given module name.

	Examples
	--------
	::

		import meta
		from meta import betascript
		
		
		def main():
		    module = betascript.FindModule("module_name")
		    betascript.ExecuteFunc(module, "function_in_module")


	"""

def CurrentModule():

	"""

	This function is used to get the currently executing module.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    module = betascript.CurrentModule()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ExecuteFunc(module: object, function_name: str, function_arguments: Any) -> Any:

	"""

	This function is used to run BETA Script code from within Python Code. This function executes a function found in a dynamically loaded BETA scripting language script.

	Parameters
	----------
	module : object
		An object that refers to the module, as it was returned by the 'LoadModule' function.

	function_name : str
		Name of the function.

	function_arguments : Any, optional
		Arguments to be passed to function.

	Returns
	-------
	Any
		The function returns the return value of the called function. 
		It is safe to call this function even if 'LoadModule' failed.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    module = betascript.LoadModule(
		        "/home/user/scripts/some_script.bs"
		    )  # Load a script file
		    result = betascript.ExecuteFunc(
		        module, "some_fun", 10, "string"
		    )  # Execute a function found within it
		    print("result= " + str(result))  # Print the result
		    betascript.UnloadModule(module)  # Unload the script
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadExecuteFunc(script_name: str, function_name: str, function_arguments: Any) -> Any:

	"""

	This function loads the 'script_name' script, calls the 'function_name' function passing it the 'function_arguments' arguments and finally unloads the script. It is a simple shortcut to the Load/Execute/Unload combination. This function is used to run BETA Script code from within Python Code.

	Parameters
	----------
	script_name : str
		Filepath of the script.

	function_name : str
		Name of the function.

	function_arguments : Any, optional
		Arguments to be passed to function.

	Returns
	-------
	Any
		It returns the variable that the invoked function returns.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    script_name = "/home/user/scripts/some_script.bs"
		    function_name = "some_function"
		    function_argument_1 = 10
		    function_argument_2 = "string"
		    # ....
		    # function_argument_n = 'n_argument'
		
		    result = betascript.LoadExecuteFunc(
		        script_name, function_name, function_argument_1, function_argument_2
		    )  # execute a function found within a module
		    print("result= " + str(result))
		    # print the result
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadModule(module_name: str) -> object:

	"""

	This function is used to run BETA Script code from within Python Code. This function loads a BETA scripting language script file into memory. The new script is in separate memory from the executing script and the user CANNOT call functions from it. You can call functions from this script using the 'ExecuteFunc' function. It is usefull to have this dynamic load feature because you can decide in runtime which script to load depending on the operation you perform.

	Parameters
	----------
	module_name : str
		Filepath of the script.

	Returns
	-------
	object
		The function returns an object containing internal information about the loaded script, or None if it fails to load. This element is passed to the 'ExecuteFunc' to execute a function from that script.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    module_name = "/home/user/scripts/some_script.bs"
		    module = betascript.LoadModule(module_name)  # Load a script file
		    function_name = "some_function"
		    function_argument_1 = 10
		    function_argument_2 = "string"
		    # ...
		    # function_argument_n = 'n_argument'
		
		    result = betascript.ExecuteFunc(
		        module, function_name, function_argument_1, function_argument_2
		    )  # Execute a function found within it
		    print("result= " + str(result))  # Print the result
		    betascript.UnloadModule(module)  # Unload the script
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetCurrentModule(module: object) -> int:

	"""

	Set the current module (the first in the loaded module list). When the executing script finishes this module is current.

	Parameters
	----------
	module : object
		The module object to be set as current.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    module = "/home/user/from_loader.bs"
		    nm = betascript.LoadModule(module)
		    om = betascript.CurrentModule()
		    betascript.SetCurrentModule(nm)
		    betascript.UnloadModule(om)
		
		
		if __name__ == "__main__":
		    main()


	"""

def UnloadModule(module: object) -> int:

	"""

	This function is used to run BETA Script code from within Python Code. This function unloads a dynamically loaded BETA scripting language script from memory. The 'module' argument is the object that 'LoadModule' returned when you called to load the module. It is safe to call this function even if 'LoadModule' failed.

	Parameters
	----------
	module : object
		Reference to the module.

	Returns
	-------
	int
		The function always returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import betascript
		
		
		def main():
		    module = "/home/user/scripts/some_script.bs"
		    loaded_module = betascript.LoadModule(module)  # Load a script file
		    function_name = "some_func"
		    function_argument_1 = 10
		    function_argument_2 = "string"
		    result = betascript.ExecuteFunc(
		        loaded_module, function_name, function_argument_1, function_argument_2
		    )  # Execute a function from the module
		    print("result=" + str(result))  # Print the result
		    betascript.UnloadModule(loaded_module)  # Unload the script
		
		
		if __name__ == "__main__":
		    main()


	"""

