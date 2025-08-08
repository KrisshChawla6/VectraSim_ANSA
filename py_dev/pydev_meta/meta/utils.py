from __future__ import annotations
from typing import *

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

		import meta
		from meta import utils
		
		
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

		import meta
		from meta import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


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
		import meta
		
		
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

		import meta
		from meta import utils
		
		
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

		import meta
		from meta import utils
		
		
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
		
		import meta
		from meta import utils
		
		
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

class Messenger():

	"""

	Class for handling messages in python scripts.
	Messenger is a unique object (singleton) in the program, every messenger instance points to the same object.

	Examples
	--------
	::

		import meta
		from meta import base
		from meta import constants
		from meta import session
		from meta import utils
		
		
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
		import meta
		
		
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

		from meta import utils
		
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

		from meta import utils
		
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

		import meta
		from meta import utils
		
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

		import meta
		from meta import utils
		
		
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

def BatchMode() -> int:

	"""

	This function checks whether Meta is running in batch mode.

	Returns
	-------
	int
		It returns an integer, 1 if META is running in batch mode, or 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    if utils.BatchMode() == 1:
		        print("Meta is running in batch mode")
		    else:
		        print("Meta is not running in batch mode")
		
		
		if __name__ == "__main__":
		    main()


	"""

def CheckboxStateOfToolbar(toolbar_name: str, checkbox_name: str) -> int:

	"""

	This function gets the state (checked or not checked) of a checkbox of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	checkbox_name : str
		Name of the checkbox.

	Returns
	-------
	int
		Upon success an integer, 1 if checkbox is checked and 0 if it is not checked.
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    checkbox_name = "Checkbox 1"
		
		    state = utils.CheckboxStateOfToolbar(toolbar_name, checkbox_name)
		    if state == 1:
		        print("Checked")
		    elif state == 0:
		        print("Not checked")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurrentDirectory() -> str:

	"""

	This function retrieves information about the current directory.

	Returns
	-------
	str
		It returns a string referring to the current directory.
		Uppon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    dir = utils.CurrentDirectory()
		    print("current dir = ", dir)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DefaultSessionFileName() -> str:

	"""

	This function gets the name of the default session file.

	Returns
	-------
	str
		It returns a string referring to the name of the default session file.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    filename = utils.DefaultSessionFileName()
		    print(filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def EvalBuiltInFunction(expression: str) -> str:

	"""

	This function evaluates a given built-in function specified by a given string expression.

	Parameters
	----------
	expression : str
		A valid Built-In Expression

	Returns
	-------
	str
		It returns a string with the result of the evaluation of the expression.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    expression = "`m0s.subcase`"
		    value = utils.EvalBuiltInFunction(expression)
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetSessionFileNames(session: str, type: str) -> object:

	"""

	This function gets the filenames which are included in a session file.

	Parameters
	----------
	session : str
		Session filepath

	type : str, optional
		Refers to the type of the paths this function will return. Its possible arguments are:
		- 'Dir' : Returns the paths including only the directories (default value)
		- 'File' : Returns the paths including the base filename

	Returns
	-------
	object
		It returns a list with the strings of the corresponding paths of the filenames of the given session.
		Each member of the list is a string referring to one specific name of a file of a given session.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    session = "/home/demo/session1.ses"
		    type = "File"
		    all_paths = utils.GetSessionFileNames(session, type)
		    for path in all_paths:
		        print(path)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaCommand(command: str) -> object:

	"""

	This function executes a meta command.

	Parameters
	----------
	command : str
		Meta command to be executed

	Returns
	-------
	object
		Returns a list with the created objects, when the command:
		- Read Geometry
		- Read/Calculate Results
		- Read/Create/Calculate Curves
		- Create Annotations
		- Create Planes
		- Create Isofunctions
		In all other cases returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import models
		
		
		def main():
		    ent_list = utils.MetaCommand("read geom Nastran test.nas")
		    if ent_list:
		        for ent in ent_list:
		            print(ent)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaCommandOnlyWriteToSession(command: str) -> int:

	"""

	This function writes the meta command in the session file without executing the command.

	Parameters
	----------
	command : str
		Meta command to be written to session file.

	Returns
	-------
	int
		The return value is always integer 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    utils.MetaCommandOnlyWriteToSession("identify element 100-150")
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaGetVariable(variable_name: str) -> str:

	"""

	This function gets variable_value from variable_name.

	Parameters
	----------
	variable_name : str
		Variable name.

	Returns
	-------
	str
		The return value is a string with the variable_value. An empty string is returned if the variable does not exist.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    utils.MetaSetVariable("var1", "0.123")
		    variable_value = utils.MetaGetVariable("var1")
		    print("Variable value: ", variable_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaSetVariable(variable_name: str, variable_value: str) -> int:

	"""

	This function sets variable_name to variable_value.

	Parameters
	----------
	variable_name : str
		Variable name.

	variable_value : str
		Variable value.

	Returns
	-------
	int
		The return value is always 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    utils.MetaSetVariable("var1", "0.123")
		    variable_value = utils.MetaGetVariable("var1")
		    print("Variable value: ", variable_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def RadioStateOfToolbar(toolbar_name: str, radio_name: str) -> int:

	"""

	This function gets the state (checked or not checked) of a radio button of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	radio_name : str
		Name of the radio button.

	Returns
	-------
	int
		It returns an integer, 1 if radio button is checked and 0 if it is not checked.
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    radio_name = "Radiobutton 1"
		    state = utils.RadioStateOfToolbar(toolbar_name, radio_name)
		    if state == 1:
		        print("Enabled")
		    elif state == 0:
		        print("Disabled")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def RangeToList(range: str) -> object:

	"""

	This function converts a range used in meta commands to a corresponding list.

	Parameters
	----------
	range : str
		A range used in META commands.

	Returns
	-------
	object
		It returns a list with members referring to the values specified by the given range.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    range = "1-5/6/7,8,9/10-30-5"
		    values = utils.RangeToList(range)
		    for one_value in values:
		        print(one_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReplaceSessionFileNames(session: str, old_name: str, new_name: str) -> int:

	"""

	This function replaces the filenames which are included in a session file. Session file is specified by its path (session).

	Parameters
	----------
	session : str
		Session's filepath.

	old_name : str
		Old filename.

	new_name : str
		New filename.

	Returns
	-------
	int
		This function always returns integer 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    session = "/home/demo/session2.ses"
		    old_name = "/home/demo/door.op2"
		    new_name = "/home/demo/new_door.op2"
		    utils.ReplaceSessionFileNames(session, old_name, new_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetCurrentDirectory(dir: str) -> int:

	"""

	This function sets the current directory.

	Parameters
	----------
	dir : str
		Folder path to be used as current directory.

	Returns
	-------
	int
		It returns an integer, -1 on error and 0 on success

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    dir = utils.CurrentDirectory()
		    print("current dir = ", dir)
		    error = utils.SetCurrentDirectory("/home/user/tmp")
		    print(error)
		    dir = utils.CurrentDirectory()
		    print("current dir = ", dir)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderValueOfToolbar(toolbar_name: str, slider_name: str) -> int:

	"""

	This function gets the value of a slider of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	slider_name : str
		Name of the slider.

	Returns
	-------
	int
		It returns an integer, referring to the value of the slider of the given toolbar.
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = utils.SliderValueOfToolbar(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TextboxValueOfToolbar(toolbar_name: str, textbox_name: str) -> str:

	"""

	This function gets the text of a textbox of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	textbox_name : str
		Name of the textbox.

	Returns
	-------
	str
		It returns a string referring to the text of the textbox of the given toolbar.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    textbox_name = "Textbox 1"
		
		    text = utils.TextboxValueOfToolbar(toolbar_name, textbox_name)
		    print(text)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListToRange(values: object, type: str) -> str:

	"""

	This function converts a list with given values to a range used in meta commands. 

	Parameters
	----------
	values : object
		List that contains the values which will be included in the range.

	type : str, optional
		Optional argument 'type' refers to the data type of values that will be included in the range. It must be one of the string values:
		- 'int': Integer values (default value)
		- 'float': Floating point values

	Returns
	-------
	str
		It returns a string representing the range of the corresponding values.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    type = "float"
		    values = list()
		    for i in range(10, 0, -1):
		        values.append(i * 0.23)
		    range_string = utils.ListToRange(values, type)
		    print(range_string)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SessionMode() -> int:

	"""

	This function checks whether META is running a session file.

	Returns
	-------
	int
		It returns an integer, 1 if META is running a session file, or 0 otherwise

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    if utils.SessionMode() == 1:
		        print("Meta is running a session file")
		    else:
		        print("Meta is not running a session file")
		
		
		if __name__ == "__main__":
		    main()


	"""

def ClearMonitor() -> int:

	"""

	This function clears the monitor output.

	Returns
	-------
	int
		The return value is always 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:" + str(l))
		    utils.ClearMonitor()
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:" + str(l))
		
		
		if __name__ == "__main__":
		    main()


	"""

def OpenMonitor(title: str) -> int:

	"""

	This function opens a monitor window. It can be used to redirect output of a script, ie to create log of a job. The window that opens features a text editor where a script can print and then comments can be added and its contents can be saved.

	Parameters
	----------
	title : str, optional
		The title of the monitor window.

	Returns
	-------
	int
		The function always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:" + str(l))
		
		
		if __name__ == "__main__":
		    main()


	"""

def OpenMonitorNoEdit(title: str) -> int:

	"""

	This function opens a monitor window in read-only (non-editable) mode. It can be used to redirect output of a script, ie to create log of a job. The window that opens features a text editor where a script can print and its contents can be saved. Text contents cannot be edited manually.

	Parameters
	----------
	title : str, optional
		The title of the monitor window.

	Returns
	-------
	int
		The function always returns 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitorNoEdit(title)
		
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PrintMonitor(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring. It is almost identical to the 'print' function with the addition of the three color arguments.

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
		The return value is always 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:" + str(l))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReadMonitor(line_int: int) -> str:

	"""

	This function reads a specific line from monitor window. The line is described by its index, the first line having index 0.

	Parameters
	----------
	line_int : int
		the line number

	Returns
	-------
	str
		Returns the contents of 'line' or empty string if the index is less than 0,
		or greater than the number of lines.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    lines = utils.LinesOfMonitor()
		    print("Total lines: ", lines)
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:" + str(i) + ", text:" + txt)
		
		
		if __name__ == "__main__":
		    main()


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
		The return value is 1 on success and 0 on failure.

	See Also
	--------
	utils.SaveMonitorToTxt

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:" + str(i) + ", text:" + txt)
		    utils.SaveMonitor("/home/user/file.txt")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectOpenDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for input.

	Parameters
	----------
	startin : str
		Path of the starting directory.

	Returns
	-------
	str
		It returns the selected directory upon success, otherwise an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    startin = "/home/user/"
		    dir = utils.SelectOpenDir(startin)
		    Print("selected dir: " + dir)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectOpenFile(flag: int, filters: str) -> object:

	"""

	This function opens file manager and lets the user select one or more files.

	Parameters
	----------
	flag : int
		0 - only single file selection is permitted.
		1 - a multi file selection is permitted.

	filters : str, optional
		Extension filter for files.

	Returns
	-------
	object
		It returns a list containing the file name(s) selected. On error or if ESCAPE is pressed the list length is 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    flag = 0
		    filter_1 = "Text files (*.txt)"
		    filter_2 = "PDF files (*.pdf)"
		    m = utils.SelectOpenFile(flag, filter_1, filter_2)
		    if len(m) > 0:
		        print(m[0])
		    else:
		        print("No file selected")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectOpenFileIn(initdir: str, flag: int, filters: str) -> object:

	"""

	This function opens file manager and lets the user select one or more files. The starting directory can be provided also.

	Parameters
	----------
	initdir : str
		Starting directory. In case of an empty string ('') or 0 the argument is ignored and the last accessed directory is used instead.

	flag : int
		0 - only single file selection is permitted.
		1 - a multi file selection is permitted.

	filters : str, optional
		Extension filter for files.

	Returns
	-------
	object
		It returns a list containing the file name(s) selected. On error or if ESCAPE was pressed the list length is 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    initdir = "/home/userdir/"
		    flag = 0
		    filter_1 = "Text files (*.txt)"
		    filter_2 = "PDF files (*.pdf)"
		    m = utils.SelectOpenFileIn(initdir, flag, filter_1, filter_2)
		    if len(m) > 0:
		        print(m[0])
		    else:
		        print("No file selected")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectSaveDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for output.

	Parameters
	----------
	startin : str
		Path of the starting directory.

	Returns
	-------
	str
		It returns the selected directory upon success, otherwise an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    startin = "/home/user/"
		    dir = utils.SelectSaveDir(startin)
		    Print("selected dir: " + dir)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectSaveFile(filter: str) -> object:

	"""

	This function opens file manager and lets the user select a file name to save.

	Parameters
	----------
	filter : str, optional
		Extension filter for files.

	Returns
	-------
	object
		It returns a list containing the file name selected. On error or if ESCAPE is pressed the list length is 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    m = utils.SelectSaveFile()
		    # or
		    # filter = 'Text files (*.txt)'
		    # m = utils.SelectSaveFile(filter)
		    if len(m) > 0:
		        print(m[0])
		    else:
		        print("No file selected")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectSaveFileIn(init_dir: str, filter: str) -> object:

	"""

	This function opens file manager and lets the user select a file name to save.

	Parameters
	----------
	init_dir : str
		Path of the starting directory, in which the file manager will open. An empty string ('') or a 0 can be passed to open file manager in the last accepted directory.

	filter : str, optional
		Extension filter for files.

	Returns
	-------
	object
		It returns a list containing the file name selected. On error or if ESCAPE was pressed the list length is 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    init_dir = "/home/user/"
		    filter = "Text files (*.txt)"
		    m = utils.SelectSaveFileIn(init_dir, filter)
		    if len(m) > 0:
		        print(m[0])
		    else:
		        print("No file selected")
		
		
		if __name__ == "__main__":
		    main()


	"""

def PrintMonitorHtml(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring. It prints html code in monitor window with the addition of the three color arguments.

	Parameters
	----------
	txt : str
		The HTML code to print.

	r_int : int
		Red color integer.

	g_int : int
		Green color integer.

	b_int : int
		Blue color integer.

	Returns
	-------
	int
		The return value is always 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		    txt = "<b>some text</b>"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitorHtml(txt, r_int, g_int, b_int)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:" + str(l))
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaCommandList(command_list: object) -> int:

	"""

	This function executes a series of META commands.

	Parameters
	----------
	command_list : object
		A list with the commands.

	Returns
	-------
	int
		Upon success, the return value is 1. Upon failure, the return value is 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    utils.MetaCommandList(
		        ["read geom Nastran test1.nas", "read geom Nastran test2.nas"]
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def TogglebuttonStateOfToolbar(toolbar_name: str, togglebutton_name: str) -> int:

	"""

	This function gets the state (pushed or not pushed) of a togglebutton of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	togglebutton_name : str
		Name of the togglebutton.

	Returns
	-------
	int
		Upon success an integer, 1 if checkbox is checked and 0 if it is not checked.
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    togglebutton_name = "Togglebutton 1"
		
		    state = utils.TogglebuttonStateOfToolbar(toolbar_name, togglebutton_name)
		    if state == 1:
		        print("Pushed")
		    elif state == 0:
		        print("Not pushed")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def ShowLog():

	"""

	"""

def TranslatorLogFile():

	"""

	"""

def MetaGetVariablesByName(variable_name: str) -> object:

	"""

	This function gets a list of META variables whose names match a string expression.

	Parameters
	----------
	variable_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list with the META variables which match a specific name.
		Each member of the list is another list with 2 members.
		In position 0, internal lists contain a string referring to the variable name.
		In position 1, internal lists contain a string referring to the variable value.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    variable_name = "myvar*"
		    variables = utils.MetaGetVariablesByName(variable_name)
		    for one_var in variables:
		        var_name = one_var[0]
		        var_value = one_var[1]
		        print(var_name)
		        print(var_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SaveMonitorToTxt(filename: str) -> int:

	"""

	This function saves the contents of the monitor window in plain text format.

	Parameters
	----------
	filename : str
		The filename of the file to be saved.

	Returns
	-------
	int
		The return value is 1 on success and 0 on failure.

	See Also
	--------
	utils.SaveMonitor

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    title = "Some title"
		    utils.OpenMonitor(title)
		    txt = "Lorem ipsum"
		    r_int = 255
		    g_int = 0
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		    txt = "dolor sit amet"
		    r_int = 0
		    g_int = 255
		    b_int = 0
		    utils.PrintMonitor(txt, r_int, g_int, b_int)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:" + str(i) + ", text:" + txt)
		    utils.SaveMonitorToTxt("/home/user/file.txt")
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetRenderingMaterials() -> object:

	"""

	This function collects the rendering materials from all the available material databases.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of the rendering material and the material database where it belongs.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# This is an example of getting all the available rendering materials
		# and applying a different material on each part of the model.
		# PYTHON script
		import meta
		from meta import utils
		from meta import parts
		
		
		def main():
		    utils.MetaCommand("options session controldraw disable")
		
		    l_materials = utils.GetRenderingMaterials()
		    for mat in l_materials:
		        print(mat)
		    model_id = 0
		    window_name = "MetaPost"
		    all_parts = parts.VisibleParts(model_id, window_name)
		    j = 0
		    for p in all_parts:
		        if j >= len(l_materials):
		            j = 0
		        utils.MetaCommand("render setmaterial pid " + l_materials[j] + " " + str(p.id))
		        j += 1
		    utils.MetaCommand("options session controldraw enable")
		
		
		if __name__ == "__main__":
		    main()


	"""

def RenderingMaterialOfPart(model_id: int, part_type: int, part_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.get_rendering_materials` instead.


	This function finds the rendering materials of a part of a model with a given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	window_name : str, optional
		Name of the window of the part. If it is absent then this function will return the rendering material of the part for the first enabled window of the model of the part.

	Returns
	-------
	str
		It returns a string with the name of the rendering material of the corresponding part of the  given model for the specified window.
		Upon failure, an empty string is returned.

	See Also
	--------
	utils.SetRenderingMaterialOfPart

	Examples
	--------
	::

		# This is an example of getting the rendering material of each part
		# and writing to a csv file.
		# PYTHON script
		import os
		import meta
		from meta import parts
		from meta import utils
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    filter = "CSV files (*.csv)"
		    l_files = utils.SelectSaveFile(filter)
		    csv_file = ""
		    if len(l_files) > 0:
		        csv_file = l_files[0]
		    else:
		        print("No file selected")
		        return
		    all_parts = parts.Parts(model_id)
		
		    with open(csv_file, "w") as f:
		        f.write("# Id, Rendering Material\\n")
		        for p in all_parts:
		            rendering_material = utils.RenderingMaterialOfPart(
		                model_id, p.type, p.id, window_name
		            )
		            if rendering_material:
		                line_str = str(p.id) + "," + rendering_material
		                f.write(line_str + "\\n")
		        f.close()
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.get_rendering_materials instead.", DeprecationWarning)

def SetRenderingMaterialOfPart(model_id: int, part_type: int, part_id: int, rendering_material: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.set_rendering_material` instead.


	This function sets the defined rendering materials on the part of the model with the given id and type.

	Parameters
	----------
	model_id : int
		Id of the model.

	part_type : int
		Type of the part (META constant).

	part_id : int
		Id of the part.

	rendering_material : str
		Name of rendering material

	window_name : str, optional
		Name of the window of the model. If it is absent then this function will set the rendering material of the part of the model for the first enabled window.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	utils.RenderingMaterialOfPart

	Examples
	--------
	::

		# This is an example of setting the rendering materials on parts
		# by reading them from the csv file saved by the utils.RenderingMaterialOfPart
		# python example.
		# PYTHON script
		import os
		import meta
		from meta import parts
		from meta import utils
		
		
		def main():
		    model_id = 0
		    window_name = "MetaPost"
		    flag = 0
		    filters = "CSV files (*.csv)"
		    l_files = utils.SelectOpenFile(flag, filters)
		    csv_file = ""
		    if len(l_files) > 0:
		        csv_file = l_files[0]
		    else:
		        print("No file selected")
		        return
		    dict_pid_vs_rendermat = dict()
		    with open(csv_file, "r") as f:
		        for line in f:
		            line = line.rstrip()
		            if line.startswith("#"):
		                continue
		            l_tokens = line.split(",")
		            pid = int(l_tokens[0])
		            rendering_mat = l_tokens[1]
		            dict_pid_vs_rendermat[pid] = rendering_mat
		        f.close()
		    all_parts = parts.Parts(model_id)
		
		    utils.MetaCommand("options session controldraw disable")
		
		    for p in all_parts:
		        rendering_material = dict_pid_vs_rendermat[p.id]
		        if rendering_material:
		            utils.SetRenderingMaterialOfPart(
		                model_id, p.type, p.id, rendering_material, window_name
		            )
		    utils.MetaCommand("options session controldraw enable")
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.set_rendering_material instead.", DeprecationWarning)

def GetRenderingMaterialsOfMaterialDatabase(database_name: str) -> object:

	"""

	This function collects the rendering materials from the specified material database.

	Parameters
	----------
	database_name : str
		The name of the database.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of the rendering material and the material database where it belongs.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    database_name = "Default Materials"
		    l_materials = utils.GetRenderingMaterialsOfMaterialDatabase(database_name)
		    for mat in l_materials:
		        print(mat)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Flc(n: float, K: float, r0: float, r45: float, r90: float):

	"""

	The function calculates the forming limit curve according to the M-K method.

	Parameters
	----------
	n : float
		Strain hardening exponent according to Hollomon's Hardening Law

	K : float
		Strength coefficient according to Hollomon's Hardening Law

	r0 : float
		Lankford planar anisotropy coefficients with angle 0 degrees from the rolling direction of the sheet metal respectively.

	r45 : float
		Lankford planar anisotropy coefficients with angle 45 degrees from the rolling direction of the sheet metal respectively.

	r90 : float
		Lankford planar anisotropy coefficients with angle 90 degrees from the rolling direction of the sheet metal respectively.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import utils
		
		
		def main():
		    n = 1.0
		    K = 2.0
		    r0 = 3.0
		    r45 = 4.0
		    r90 = 5.0
		    flc = utils.Flc(n, K, r0, r45, r90)
		    print(flc)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributesListToDict(attributes: object) -> object:

	"""

	This function constructs a dictionary from a given list attributes

	Parameters
	----------
	attributes : object
		List of attributes

	Returns
	-------
	object
		It returns a dictionary whose keys are the names of the attributes and values the corresponding values.
		Upon failure, an empty dictionary is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import results
		
		
		def main():
		    model_id = 0
		    all_resultsets = results.Resultsets(model_id)
		    res = all_resultsets[1]
		
		    all_attributes = results.AttributesOfResultset(res)
		    dict = utils.AttributesListToDict(all_attributes)
		    for id, p in dict.items():
		        print(id + ": " + p)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaClearVariable(variable_name: str) -> int:

	"""

	This function deletes the variable with name variable_name.

	Parameters
	----------
	variable_name : str
		Variable name.

	Returns
	-------
	int
		Return 1, if the variable existed, and deleted, zero otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    var_name = "var1"
		    utils.MetaSetVariable(var_name, "0.123")
		    variable_value = utils.MetaGetVariable("var1")
		    print("Variable value: ", variable_value)
		
		    utils.MetaClearVariable(var_name)
		    variable_value = utils.MetaGetVariable(var_name)
		    print("Variable value, after delete: ", variable_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaClearVariablesByName(variable_name: str) -> int:

	"""

	This function deletes the META variables whose names match a string expression.

	Parameters
	----------
	variable_name : str
		A string search expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	int
		Returns the number of succesfully deleted META variables

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    var_1 = "var1"
		    var_2 = "var2"
		    utils.MetaSetVariable(var_1, "0.123")
		    utils.MetaSetVariable(var_2, "0.456")
		    value_1 = utils.MetaGetVariable(var_1)
		    value_2 = utils.MetaGetVariable(var_2)
		    print("Variable1 value: ", value_1)
		    print("Variable2 value: ", value_2)
		
		    utils.MetaClearVariablesByName("var")
		    value_1 = utils.MetaGetVariable(var_1)
		    value_2 = utils.MetaGetVariable(var_2)
		    print("Deleted Variable1 value: ", value_1)
		    print("Deleted Variable2 value: ", value_2)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetMetaWorkspaceWidth() -> float:

	"""

	Returns
	-------
	float
		Returns the width of the workspace in pixels.

	See Also
	--------
	utils.GetMetaWorkspaceHeight

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    width = utils.GetMetaWorkspaceWidth()
		    height = utils.GetMetaWorkspaceHeight()
		    print("workspace width:\\t" + str(width))
		    print("workspace height:\\t" + str(height))
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetMetaWorkspaceHeight() -> float:

	"""

	Returns
	-------
	float
		Returns the height of the workspace in pixels.

	See Also
	--------
	utils.GetMetaWorkspaceWidth

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    width = utils.GetMetaWorkspaceWidth()
		    height = utils.GetMetaWorkspaceHeight()
		    print("workspace width:\\t" + str(width))
		    print("workspace height:\\t" + str(height))
		
		
		if __name__ == "__main__":
		    main()


	"""

def get_models(specifier: str, id: int, name: str, label: str) -> object:

	"""

	This function gets the models.

	Parameters
	----------
	specifier : str, optional
		The specifier of the method. Its possible values are:
		- 'all' : gets all models.
		- 'active' : gets active models.
		The default value is 'all'.

	id : int, optional
		Id of the model. If set, the method will return the model with id equal to the given id. This argument is used when the specifier is 'all'.

	name : str, optional
		Name of the model. If set, the method will return the models that have name that matches the given pattern. This argument is used when the specifier is 'all'.

	label : str, optional
		Label of the model. If set, the method will return the models that have label that matches the given pattern. This argument is used when the specifier is 'all'.

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is an object of class Model referring to one specific model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    models = utils.get_models()
		    print(models)
		
		
		if __name__ == "__main__":
		    main()


	"""

def get_pages(specifier: str, id: int, name: str) -> object:

	"""

	This function gets pages.

	Parameters
	----------
	specifier : str, optional
		The specifier of the method. Its possible values are:
		- 'all' : gets all pages.
		- 'active' : gets active page.
		The default value is 'all'.

	id : int, optional
		Id of the page. If set, the method will return the page with id equal to the given id. This argument is used when the specifier is 'all'.

	name : str, optional
		Name of the page. If set, the method will return the pages that have name that matches the given pattern. This argument is used when the specifier is 'all'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Page referring to the corresponding page.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    pgs = utils.get_pages()
		    print(pgs)
		
		
		if __name__ == "__main__":
		    main()


	"""

def get_overlay_runs(overlay_type: str, id: int, name: str, filename: str) -> object:

	"""

	This function gets the overlay runs.

	Parameters
	----------
	overlay_type : str, optional
		Overlay run type. Possible string values:
		- 'session'
		- 'project'.

	id : int, optional
		Id of the overlay run.

	name : str, optional
		Search string for the name of the overlay run. Wildcards can also be used ("*", "?", "[...]").

	filename : str, optional
		Search string for the filename of the overlay run. Wildcards can also be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Overlay referring to one specific overlay run.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    ovrs = utils.get_overlay_runs()
		    print(ovrs)
		
		    # Or
		    overlay_type = "session"
		    id = 1
		    name = "*Test"
		    filname = "*Test_Filename"
		    ovrs = utils.get_overlay_runs(overlay_type, id, name, filname)
		    print(ovrs)
		
		
		if __name__ == "__main__":
		    main()


	"""

def get_planes(specifier: str, window: object) -> object:

	"""

	This functions gets the cut planes.

	Parameters
	----------
	specifier : str
		The specifier of the method. Its possible values are:
		- 'all' : get all the planes.
		- 'visible' : get the visible planes for the window specified in the window argument.
		- identified' : get the identified planes.

	window : object, optional
		An object of class Window. It is required when the specifier is 'visible'.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plane referring to one specific plane.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import windows
		
		
		def main():
		    specifier = "all"
		    planes = utils.get_planes(specifier)
		    print(planes)
		    # OR
		    specifier = "visible"
		    window = windows.Window("MetaPost", page_id=0)
		    planes = utils.get_planes(specifier, window)
		    print(planes)
		    # OR
		    specifier = "identified"
		    window = windows.Window("MetaPost", page_id=0)
		    planes = utils.get_planes(specifier, window)
		    print(planes)
		
		
		if __name__ == "__main__":
		    main()


	"""

def get_plot_models(id: int, deck: str) -> object:

	"""

	Parameters
	----------
	id : int, optional
		Id of the plot model.

	deck : str, optional
		Deck of the plot model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotModel referring to one specific plot_model. 
		Upon failure, an empty list is returned

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    plot_models = utils.get_plot_models()
		    print(plot_models)
		    # OR
		    id = 0
		    deck = "NASTRAN"
		    plot_models = utils.get_plot_models(id, deck)
		    print(plot_models)
		
		
		if __name__ == "__main__":
		    main()


	"""

def pick_models(message: str) -> object:

	"""

	This function allows the user to pick models from the existing windows. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.

	Parameters
	----------
	message : str
		Message displayed to the user which will be shown to the user when the function is called.

	Returns
	-------
	object
		It returns a list with Model objects where each member of the list is refers to one specific picked model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    message = "Select Models and press Enter when you are ready"
		    models = utils.pick_models(message)
		    print(models)
		
		
		if __name__ == "__main__":
		    main()


	"""

def pick_models_from_list(message: str) -> object:

	"""

	This function allows the user to select models from a given list. The execution of the script will stop and it will restart after the selection of the models from the list.

	Parameters
	----------
	message : str
		Message displayed to the user.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Model referring to one specific selected model.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    message = "Select Models and press Enter when you are ready"
		    models = utils.pick_models_from_list(message)
		    print(models)
		
		
		if __name__ == "__main__":
		    main()


	"""

def show_planes(planes: object, window: object) -> bool:

	"""

	This function allows the user to show some specific planes.

	Parameters
	----------
	planes : object
		A list with objects of class Plane.

	window : object
		An object of class window.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import windows
		
		
		def main():
		    specifier = "all"
		    planes = utils.get_planes(specifier)
		    win = windows.Window("MetaPost", 0)
		    ret = utils.show_planes(planes, win)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def hide_planes(planes: object, window: object) -> bool:

	"""

	This function allows the user to hide some planes.

	Parameters
	----------
	planes : object
		A list of objects of class Plane.

	window : object
		An object of class Window.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import windows
		
		
		def main():
		    specifier = "all"
		    planes = utils.get_planes(specifier)
		    win = windows.Window("MetaPost", 0)
		    ret = utils.hide_planes(planes, win)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def identify_planes(planes: object, window: object) -> bool:

	"""

	This function allows the user to identify some planes.

	Parameters
	----------
	planes : object
		A list of objects of class Plane.

	window : object
		An object of class Plane.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import windows
		
		
		def main():
		    specifier = "all"
		    planes = utils.get_planes(specifier)
		    win = windows.Window("MetaPost", 0)
		    ret = utils.identify_planes(planes, win)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def reset_identify_planes(planes: object, window: object) -> bool:

	"""

	This function allows the user to reset the identification of planes.

	Parameters
	----------
	planes : object
		A list with objects of class Plane.

	window : object
		An object of class Window.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import windows
		
		
		def main():
		    specifier = "all"
		    planes = utils.get_planes(specifier)
		    win = windows.Window("MetaPost", 0)
		    ok = utils.reset_identify_planes(planes, win)
		    print(ok)
		
		
		if __name__ == "__main__":
		    main()


	"""

def set_planes_settings(settings: object) -> bool:

	"""

	This function control settings of all planes.

	Parameters
	----------
	settings : object
		Settings (key-value) of the planes.
		A dictionary with string keys and string values:
		- 'toggleopts_auto': Auto Cut Geometry (0,1)
		- 'toggleopts_clip': Clip Geometry by Plane (0,1)
		- 'toggleopts_deform': Section deform (0,1)
		- 'toggleopts_hidden': Hidden section visibility (0,1)
		- 'toggleopts_pcolor': Get Part color (0,1)  
		- 'toggleopts_pcolor': Project Section on Plane (0,1)
		- 'toggleopts_sectionclip': Clip Geometry by Section (0,1)
		- 'toggleopts_showmesh': Show Mesh (0,1)
		- 'toggleopts_slice': Cut Slice (0,1)
		- 'toggleopts_stateauto': Auto Cut Geometry when load state changes (0,1)
		- 'toggleopts_thickshells': Follow thich shells style (0,1)
		- 'toggleopts_transp': Plane Transparency (0,1)
		- 'toggleopts_undeformcut': Cut undeformed Geometry (0,1)
		- 'options_cut': Cut ('all', 'autovisible', 'visible')
		- 'options_draw2plane': Section drawn in Plane (0,1)
		- 'options_follow': Plane Follow Node ('normal', 'orig', 'perpendicular')
		- 'options_fringe': Fringe Options ('enable', 'disable', 'lock', 'unlock', 'cplot', 'nplot', 'vplot', 'elemdata', 'onelement', 'onnode', 'unode', 'vnode', 'wnode', 'dnode', 'follow')
		- 'options_grid': Grid Options (0,1)
		- 'options_lock2vis': Cut only visible Parts (0,1)
		- 'options_offset': Plane Offset Value (float value)
		- 'options_onlysection': Draw only Section (0,1)
		- 'options_scale': Plane Scale factor (float value)
		- 'options_sectioncolor': Set section color ('auto', 'plane', 'pid', 'mid', 'model')
		- 'options_slicewidth': Plane Slice Width (float value)
		- 'options_solid': Solid Cut Options ('both', 'inside', 'skin')
		- 'options_style': Plane Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_undeformstyle': Plane Undeform Line Style ('cont', 'dashdotline', 'dashline', 'dotline')
		- 'options_width': Plane Line Width (float value)

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    settings = {"toggleopts_auto": "enable"}
		    ret = utils.set_planes_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetLinearCombineAddedModes(filename: str) -> object:

	"""

	Given a specific filename, returns the states that have been added for a linear combination, which belong to that file.

	Parameters
	----------
	filename : str
		The name of the file that contains the added states.

	Returns
	-------
	object
		Upon success returns a list of dictionaries, one for each state.
		Upon failure returns an empty list.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    filename = m.name
		    # Get one dictionary for each state
		    states = utils.GetLinearCombineAddedModes(filename)
		
		    for state in states:
		        # For each state, these are it's possible keys ( only the ones found will be in the dictionary )
		        possibleKeys = {
		            "Name",
		            "Subcase",
		            "State",
		            "Step",
		            "Loadstep",
		            "Time",
		            "Frequency",
		            "Mode",
		            "Eigenvalue",
		            "Cycle",
		        }
		
		        for possibleKey in possibleKeys:
		            # If the key is found, print it
		            value = state.get(possibleKey)
		            if value:
		                print(possibleKey + " : " + str(value) + "\\n")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SnapShotWindow(filename: str, image_format: str, window_title) -> int:

	"""

	The SnapShotWindow function takes a snapshot of a window and saves it as an image in the specified file.

	Parameters
	----------
	filename : str
		The filename to be saved. This argument is mandatory.
		If filename exists, it will be overwritten.

	image_format : str, optional
		One of: ['POSTSCRIPT' | 'RGB' | 'TIFF' | 'JPEG' | 'PNG' | 'BMP'].

	window_title : , optional
		The window title.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from os.path import expanduser
		from meta import guitk
		from meta import utils
		
		
		def main():
		    home = expanduser("~")
		    filename = os.path.join(home, "window.png")
		    image_format = "PNG"
		    window_title = "Example toolbar"
		    ret = utils.SnapShotWindow(filename, image_format, window_title)
		    if ret == 0:
		        print("Image saved in " + filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderMinValueOfToolbar(toolbar_name: str, slider_name: str) -> int:

	"""

	This function gets the min value of a slider of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	slider_name : str
		Name of the slider.

	Returns
	-------
	int
		It returns an integer, referring to the min value of the slider of the given 
		toolbar. Upon failure, it returns -1.

	See Also
	--------
	toolbars.SliderGetMinValue

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = utils.SliderMinValueOfToolbar(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderMaxValueOfToolbar(toolbar_name: str, slider_name: str) -> int:

	"""

	This function gets the max value of a slider of a given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	slider_name : str
		Name of the slider.

	Returns
	-------
	int
		It returns an integer, referring to the max value of the slider of the given 
		toolbar. Upon failure, it returns -1.

	See Also
	--------
	toolbars.SliderGetMaxValue

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = utils.SliderMaxValueOfToolbar(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetControlDrawStatus() -> bool:

	"""

	Returns whether drawing in META is enabled or not. The value can be set using utils.SetControlDrawStatus(status).

	Returns
	-------
	bool
		True if controldraw is enabled and False otherwise.

	See Also
	--------
	meta.utils.SetControlDrawStatus

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    controldraw = utils.GetControlDrawStatus()
		    print("controldraw status: " + str(controldraw))
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetControlDrawStatus(status: bool) -> bool:

	"""

	Sets the drawing status in META. It has the same functionality as session command "options session controldraw enable/disable". The value can be read back using utils.GetControlDrawStatus().

	Parameters
	----------
	status : bool
		True will enable controldraw and False will disable it.

	Returns
	-------
	bool
		The new controldraw status. If the operation succeeded this will be the same as the provided argument. The value is True if controldraw is enabled and False otherwise.

	See Also
	--------
	meta.utils.GetControlDrawStatus

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    status = False
		    controldraw = utils.SetControlDrawStatus(status)
		    print("controldraw status: " + str(controldraw))
		
		
		if __name__ == "__main__":
		    main()


	"""

def SaveGUISettings(filename: str) -> object:

	"""

	This function saves the current GUI settings to a file.

	Parameters
	----------
	filename : str, optional
		The filename of the XML were the settings will be saved.

	Returns
	-------
	object
		The function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    filename = "/home/MyGUI.xml"
		    utils.SaveGUISettings(filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsMetaDatabaseFile(filename: str) -> bool:

	"""

	Checks if given file is a META database.

	Parameters
	----------
	filename : str
		A filepath.

	Returns
	-------
	bool
		Returns True if the given file is a META database, and False otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    filename = "home/geom.metadb"
		    ret = utils.IsMetaDatabaseFile(filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsProjectFile(filename: str) -> bool:

	"""

	Checks if given file is a META project.

	Parameters
	----------
	filename : str
		A filepath.

	Returns
	-------
	bool
		Returns True if the given file is a META project file, and False otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    filename = "home/a_project.metadb"
		    ret = utils.IsProjectFile(filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaCommandMulti(commands: str) -> object:

	"""

	This function executes multiple meta commands in a Multi Line string.

	Parameters
	----------
	commands : str
		A Multi Line string that contains a command in each line.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    commands = read geom Nastran test.nas
		\tread onlyfun Nastran test.op2 all Stresses,MajorPrincipal,MaxofTopBottom
		\t0:options state variable "serial=1"
		\tgrstyle scalarfringe enable
		    utils.MetaCommandMulti(commands)
		
		
		if __name__ == "__main__":
		    main()


	"""

def MetaCommandMultiOnlyWriteToSession(commands: str) -> object:

	"""

	This function writes the meta commands in the session file without executing the commands.

	Parameters
	----------
	commands : str
		A Multi Line string that contains a command in each line.

	Returns
	-------
	object
		This function returns None.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    commands = read geom Nastran test.nas
		\tread onlyfun Nastran test.op2 all Stresses,MajorPrincipal,MaxofTopBottom
		\t0:options state variable "serial=1"
		\tgrstyle scalarfringe enable
		    utils.MetaCommandMultiOnlyWriteToSession(commands)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectOpenDirectories(path: str) -> object:

	"""

	This function allows the user to select directories for input.

	Parameters
	----------
	path : str, optional
		Path of the starting directory.

	Returns
	-------
	object
		It returns a list with the selected directories upon success, otherwise an empty list.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		
		
		def main():
		    path = "/home/user/"
		    dirs = utils.SelectOpenDirectories(path)
		    print(dirs)
		
		
		if __name__ == "__main__":
		    main()


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

		import meta
		from meta import utils
		
		
		def main():
		    qa = utils.QualityAssurance()
		    process_name = "MeshPart"
		    q1 = qa.start_process(process_name)
		    # My program to mesh a part
		    # Preparations for mesh
		    process_name = "MeshPart"
		    q2 = qa.start_process(process_name)
		    # A function that mesh the part
		    name = "mesh_data"
		    qa.add_new_line(name)
		    value_name = "elements_number"
		    value = 1421
		    qa.add_value(value_name, value)
		    value_name_current_memorystring = "mem_used_after_mesh"
		    qa.add_current_memory_usage_value(value_name_current_memorystring)
		    qa.stop_process(q2)
		    qa.stop_process(q1)
		
		
		if __name__ == "__main__":
		    main()

	"""


	def start_process(self, process_name: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float) -> object:

		"""

		Declare the start of a QA process.


		Parameters
		----------
		process_name : str
			The name of the process.

		run_if : bool, optional
			Condition to start the process

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

		Set the default compare values for the quality assurance mechanism.


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
			Set the default upper limit for comparing floats.

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


	def add_current_memory_usage_value(self, value_name_current_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float):

		"""

		Add as value the current memory usage of the program. 


		Parameters
		----------
		value_name_current_memory : str
			The name of the value.

		run_if : bool, optional
			Condition to add the value.

		compare_val : float, optional
			Condition to add the value.

		down_limit : float, optional
			A custom down limit for current memory value.

		up_limit : float, optional
			A custom upper limit for current memory value.

		"""


	def add_peak_memory_usage_value(self, value_name_peak_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float):

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

		A clock will start to run and it will stop at stop_lapThe laps have names.When running process is stoped all times of laps will be added as valuesto the process. The process will have the numer of times a lap was statedand the total time of the laps. 


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

class ParallelJobsDispatcher():

	"""

	Objects of this class enable the dispatching of parallel python script jobs to BETA app workers.
	
	Each parallel job is depicted through a python file, either pre-existing or created just-in-time temporarily.

	Examples
	--------
	::

		from meta import utils
		
		
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
		import meta
		from meta import utils
		
		
		def main():
		    dict_metrics = utils.GetProcessSystemMetrics("memory")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "KB")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "bytes", True)
		    for item in dict_metrics.items():
		        print(item)
		
		
		if __name__ == "__main__":
		    main()


	"""

