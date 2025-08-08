from __future__ import annotations
from typing import *

def CurrentModule() -> object:

	"""

	This function is used to get the currently executing module.

	Returns
	-------
	object
		Returns the internal reference to the current module.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    module = betascript.CurrentModule()


	"""

def ExecuteFunc(module: object, function_name: str, function_arguments: Any) -> Any:

	"""

	This function is used to run BETA Script code from within Python Code.
	This function executes a function found in a dynamically loaded BETA scripting language script.
	'module' was returned by the 'LoadModule' function.
	'function_name' is the name of the function to call, followed by the arguments you would normally pass to it.

	Parameters
	----------
	module : object
		A reference to the module.

	function_name : str
		The name of the function.

	function_arguments : Any, optional
		Arguments to be passed to the function.

	Returns
	-------
	Any
		Returns the return value of the called function. 
		It is safe to call this function even if 'LoadModule' failed.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    module = betascript.LoadModule(
		        "/home/user/scripts/some_script.bs"
		    )  # load a script file
		    result = betascript.ExecuteFunc(
		        module, "some_fun", 10, "string"
		    )  # execute a function found within it
		    print("result =", result)
		    betascript.UnloadModule(module)  # Unload the script


	"""

def LoadExecuteFunc(script_name: str, function_name: str, function_arguments: Any) -> Any:

	"""

	This function loads the 'script_name' script and calls the 'function_name' function passing it 
	the 'function_arguments' arguments and finally unloads the script. It is a simple shortcut to 
	the Load/Execute/Unload combination. This function is used to run BETA Script code from within Python Code.

	Parameters
	----------
	script_name : str
		The name of the script.

	function_name : str
		The name of the function.

	function_arguments : Any, optional
		The arguments to be passed to the function.

	Returns
	-------
	Any
		Returns whatever the invoked function returns.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    result = betascript.LoadExecuteFunc(
		        "/home/user/scripts/some_script.bs", "some_fun", 10, "string"
		    )  # execute a function found within a module
		    print("result=", result)  # print the result


	"""

def LoadModule(module_name: str) -> object:

	"""

	This function is used to load a BETA scripting language script file and/or a Python module into memory. 
	The new script is in separate memory from the executing script and the user CANNOT call functions from it. 
	You can call functions from this script using the 'ExecuteFunc' function. It is usefull 
	to have this dynamic load feature because you can decide in runtimewhich script to load
	depending on the operation you perform.

	Parameters
	----------
	module_name : str
		The name of the module to be loaded.

	Returns
	-------
	object
		Returns an object containing internal information about the loaded script, or None if it fails to load.
		This element is passed to the 'ExecuteFunc' to execute a function from that script.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    module = betascript.LoadModule(
		        "/home/user/scripts/some_script.bs"
		    )  # load a script file
		    result = betascript.ExecuteFunc(
		        module, "some_fun", 10, "string"
		    )  # execute a function found within it
		    print("result =", result)  # print the result
		    betascript.UnloadModule(module)  # Unload the script


	"""

def SetCurrentModule(module: object) -> int:

	"""

	Set the current module (the first in the loaded module list).

	Parameters
	----------
	module : object
		The module object to be set as current.

	Returns
	-------
	int
		Returns 1 on success and 0 on faillure.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    nm = betascript.LoadModule("/home/costas/from_loader.bs")
		    om = betascript.CurrentModule()
		    betascript.SetCurrentModule(nm)
		    betascript.UnloadModule(om)


	"""

def UnloadModule(module: object) -> int:

	"""

	This function is used to run BETA Script code from within Python Code.
	This function unloads a dynamically loaded BETA scripting language script from memory.
	The 'module' argument is whatever the 'LoadModule' returned when you called to load the module.
	It is safe to call this function even if 'LoadModule' failed.

	Parameters
	----------
	module : object
		A reference to the module.

	Returns
	-------
	int
		Always returns 0.

	Examples
	--------
	::

		import sdm
		from sdm import betascript
		
		
		def main():
		    module = betascript.LoadModule(
		        "/home/user/scripts/some_script.bs"
		    )  # load a script file
		    result = betascript.ExecuteFunc(
		        module, "some_fun", 10, "string"
		    )  # execute a function found within it
		    print("Result:", result)  # print the result
		    betascript.UnloadModule(module)  # Unload the script


	"""

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

		import sdm
		from sdm import betascript
		
		
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

		import sdm
		from sdm import betascript
		
		
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

		import sdm
		from sdm import betascript
		
		
		def main():
		    module = betascript.FindModule("module_name")
		    betascript.ExecuteFunc(module, "function_in_module")


	"""

