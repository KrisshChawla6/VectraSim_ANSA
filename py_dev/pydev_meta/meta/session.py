from __future__ import annotations
from typing import *

def GetFreePhysicalMemory() -> int:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`GetProcessSystemMetrics` instead.


	Returns the free physical memory at the time of this function's call in kilobytes (1024 bytes).

	Returns
	-------
	int
		Returns the free physical memory on success and 0 on failure.

	Examples
	--------
	::

		import meta
		from meta import session
		
		
		def main():
		    m = session.GetFreePhysicalMemory()
		    print(m)


	"""

	import warnings; warnings.warn("Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.", DeprecationWarning)

def AcquireFeature(feature: str) -> int:

	"""

	It registers license token found in a BETA LM license.

	Parameters
	----------
	feature : str
		The feature to acquire license tokens for. 
		The list of available feature names for a specific license server can be found 
		with the command beta_lm_stat -h server. BETA CAE Systems issues license 
		keys to application developers upon request.

	Returns
	-------
	int
		1: When the feature has been acquired successfully.
		-1: When an incompatible feature is given (ex: ANSA).
		-10: When an invalid feature is given.
		-12: When no credit is available.

	See Also
	--------
	ReleaseFeature

	Examples
	--------
	::

		import meta
		from meta import session
		
		
		def main():
		    ret_feature = session.AcquireFeature("TEST_SCRIPT")
		
		    if ret_feature == -12:
		        print("No credit is available")
		        return 1
		    if ret_feature == -10:
		        print("This is invalid feature")
		        return 1
		    even_nums = []
		    for i in range(0, 100, 2):
		        even_nums.append(i)
		    ret = session.ReleaseFeature("TEST_SCRIPT")
		    if ret == 1:
		        print("Tokens released succesfully")


	"""

def ReleaseFeature(feature: str) -> int:

	"""

	Releases a previously acquired feature through session.AcquireFeature.

	Parameters
	----------
	feature : str
		The feature to release the tokens from.

	Returns
	-------
	int
		1: When a previously acquired feature is succesfully released.
		-1: When an incompatible feature, unknown or a non acquired feature is given.

	See Also
	--------
	session.AcquireFeature

	Examples
	--------
	::

		import meta
		from meta import session
		
		
		def main():
		    ret_feature = session.AcquireFeature("TEST_SCRIPT")
		
		    if ret_feature == -12:
		        print("No credit is available")
		        return 1
		    if ret_feature == -10:
		        print("This is invalid feature")
		        return 1
		    even_nums = []
		
		    for i in range(0, 100, 2):
		        even_nums.append(i)
		    ret = session.ReleaseFeature("TEST_SCRIPT")
		    if ret == 1:
		        print("Tokens released succesfully")


	"""

def setPluginInfos(classInstance: object):

	"""

	Sets an instance of a user-defined class, as plugin's information.

	Parameters
	----------
	classInstance : object
		An Instance of a user-defined class with specific variable names.
		The main Variable names are:
		- filepath: Set as string the path of actual main file. (mandatory)
		- Buttons: A dict in which you set your buttons with key:button's label and 
		           values: tuple(function name, tooltip, help, path for image of button).
		- title: Set title of plugin as string.
		- author: Set author of plugin as string.
		- hostApplication: Set host application of plugin as string.
		- minHostApplicationVersion: Set minimmum host application version of plugin as string.
		- description: Set description of plugin as string.

	Examples
	--------
	::

		import meta
		from meta import session
		
		
		class plinfos:
		    def __init__(self):
		        self.title = "Title of plugin"
		        self.author = "Author of plugin"
		        self.hostApplication = "ANSA"
		        self.minHostApplicationVersion = "v16.0.0"
		        self.description = "Description of plugin"
		        self.filepath = "/file/path/of/plugin/plugin.ppl"
		
		        self.Buttons = {
		            "ButtonLabel": ("functionName", "tooltip", "help", "imagefilePath")
		        }
		
		
		def main():
		    x = plinfos()
		    session.setPluginInfos(x)


	"""

def ApplicationInformation() -> str:

	"""

	This function reports build and runtime information of the running MetaPost process. This includes the MetaPost version, its build date, and information about the architecture of the application and the underling operating system. Additionally, information is provided about Graphics vendor, Graphics renderer and OpenGL version. The report is similar to the information provided by Menu > Help > About META

	Returns
	-------
	str
		It returns a string containing the build/runtime information.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import session
		
		
		def main():
		    s = session.ApplicationInformation()
		    print(s)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ProgramArguments() -> object:

	"""

	This function retrieves the command line arguments of the program.

	Returns
	-------
	object
		It returns a list containing the program arguments.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import session
		
		
		def main():
		    m = session.ProgramArguments()
		    if m:
		        print(m)
		
		
		if __name__ == "__main__":
		    main()


	"""

def BetaClearVariable(name: str) -> bool:

	"""

	This function frees the memory from the given BETA variable 

	Parameters
	----------
	name : str
		The name of the BETA variable.

	Returns
	-------
	bool
		True if operation was successful, False otherwise

	Examples
	--------
	::

		# PYTHON script
		import pickle
		import meta
		from meta import session
		
		
		def main():
		    beta_var_name = "a"
		    p = 1
		    v = pickle.dumps(p)
		    session.BetaSetVariable(beta_var_name, v)
		    v = session.BetaGetVariable(beta_var_name)
		    p = pickle.loads(v)
		    print(p)
		    session.BetaClearVariable(beta_var_name)
		    v = session.BetaGetVariable(beta_var_name)
		    if v == None:
		        print('Variable "' + beta_var_name + '" cannot be retrieved')
		
		
		if __name__ == "__main__":
		    main()


	"""

def BetaGetVariable(name: str, match: int) -> object:

	"""

	META script can store user data and address them by a name. These data are NOT volatile as script variables and can be accessed either from different scripts or whenever a script is run. This function allows the user to retrieve data stored under a user specified name. Wildcards can also be used ("*", "?", "[...]").

	Parameters
	----------
	name : str
		The name of the beta variable to be retrieved.

	match : int, optional
		Control the matching mode of the name lookup.
		Values are:
		-constants.ENM_EXACT: an exact match (default)
		-constants.ENM_WILDCARD: a wildcard match

	Returns
	-------
	object
		The function returns the Beta Variable if the variable is found. It returns None otherwise.
		
		If match=constants.ENM_WILDCARD is used it returns a dictionary with key the variable name and data the variable value. The dictionary is empty if no variables matching the wildcard expression were found.

	Examples
	--------
	::

		import pickle
		import meta
		from meta import session
		from meta import constants
		
		
		def main():
		    p = 1
		    name = "a"
		    match = pickle.dumps(p)
		    session.BetaSetVariable(name, match)
		    v = session.BetaGetVariable(name)
		    p = pickle.loads(v)
		    print(p)
		
		    p = 2
		    name = "AB"
		    match = pickle.dumps(p)
		    session.BetaSetVariable(name, match)
		
		    print("Variables matching *")
		    name = "*"
		    match = constants.ENM_WILDCARD
		    vars = session.BetaGetVariable(name, match)  # returns all variables
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		    print("")
		    print("Variables matching [a-z]*")
		    name = "[a-z]*"
		    match = constants.ENM_WILDCARD
		    vars = session.BetaGetVariable(
		        name, match
		    )  # returns variables starting with lower letter
		    for key, value in vars.items():
		        p = pickle.loads(value)
		        print("Name: {} Value: {}".format(key, p))
		
		
		if __name__ == "__main__":
		    main()


	"""

def BetaSetVariable(name: str, value: object) -> bool:

	"""

	META script can store user data and address them by a name. These data are NOT volatile as script variables and can be accessed either from different scripts or whenever a script is run. This function allows the user to store data under a user specified name.

	Parameters
	----------
	name : str
		The name of the beta variable.

	value : object
		A bytes object of the data to store.

	Returns
	-------
	bool
		The function returns True if the variable was set.
		In any other case the return value is False.

	Examples
	--------
	::

		import pickle
		import meta
		from meta import session
		
		
		def main():
		    p = 1
		    name = "a"
		    match = pickle.dumps(p)
		    session.BetaSetVariable(name, match)
		    v = session.BetaGetVariable(name)
		    p = pickle.loads(v)
		    print(p)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetMemoryUsage() -> int:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`GetProcessSystemMetrics` instead.


	Returns the application's physical memory consumption in kilobytes (1024 bytes).

	Returns
	-------
	int
		The application's physical memory consumption on success and None on failure.

	Examples
	--------
	::

		import meta
		from meta import session
		
		
		def main():
		    m = session.GetMemoryUsage()
		    print(m)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.", DeprecationWarning)

def Quit(exit_code: int) -> int:

	"""

	This function quits the current file and exits the program.

	Parameters
	----------
	exit_code : int, optional
		Exit code.

	Returns
	-------
	int
		It returns 0 in all cases.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import session
		
		
		def main():
		    exit_code = 0
		    session.Quit(exit_code)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PrintMemoryUsage(prefix: str) -> int:

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`GetProcessSystemMetrics` instead.


	It will print application's current memory usage on the shell window the program was launched from.

	Parameters
	----------
	prefix : str, optional
		If the prefix argument is given, it will precede the printed text.

	Returns
	-------
	int
		It returns 1 on success, 0 on failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		
		def main():
		    prefix = "mETA currently uses the following amount of"
		    mem = meta.session.PrintMemoryUsage(prefix)
		    print(mem)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.", DeprecationWarning)

