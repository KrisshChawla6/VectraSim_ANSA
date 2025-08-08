from __future__ import annotations
from typing import *

class TabPage():

	"""

	A class for Tab Page items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class TabPage. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A TabPage object.

		"""

class Toolbar():

	"""

	A base class that provides the necesary generic and common functionality for the main script of Python-based META Toolbars.
	This class should be inherited by a derived class in the main Toolbar script.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import tdk
		
		
		def main():
		    tb = tdk.Toolbar("mytoolbar", "My Toolbar", "my_toolbar_memory", False)
		
		
		if __name__ == "__main__":
		    main()

	"""


	_name: str = None
	"""
	The name of the Toolbar. It is marked as a read-only and private member.

	"""

	_display_name: str = None
	"""
	The display name of the Toolbar. It is marked as a read-only and private member.

	"""

	_script_file_rel_path: str = None
	"""
	The relative file path of the main Toolbar Python file with respect to the Toolbar definition file. It is marked as a read-only and private member.

	"""

	memory: object = None
	"""
	A meta.tdk.Memory object that holds information and is stored as a BETA variable. It is marked as a read-only and private member.

	"""

	_memory_name: str = None
	"""
	The name of the BETA variable where the contents of Toolbar._memory member are stored to and retrieved from. It is marked as a read-only and private member.

	"""

	_debug_mode: bool = None
	"""
	A boolean variable for the debug mode of the Toolbar class. If True, extra information is printed and more checks are executed. It is marked as a read-only and private member.

	"""

	_batch_mode: bool = None
	"""
	A boolean variable that corresponds to the batch mode of META. If True, several functions of the Toolbar class will not raise any window. It is marked as a read-only and private member.

	"""

	_session_mode: bool = None
	"""
	A boolean variable that corresponds to the session mode of META. If True, several functions of the Toolbar class will not raise any window. It is marked as a read-only and private member.

	"""

	_function_names_map: object = None
	"""
	A dictionary that maps old function names - keys - to new function names - values. It is useful when functions change names and old function names are still referred at existing sessions. It should be edited by meta.tdk.Toolbar.set_function_map() and used only by the Toolbar class or its derived class.

	"""

	def execute(self, function_name: str, *arguments: object, **keywords: object) -> object:

		"""

		Branches the execution to a function of the derived class of the Toolbar. The function accepts the name of a member function of the derived class of the Toolbar class and an uknown number of (named) arguments. It passes to the defined function all arguments passed to it in the same order - except the said function's name. It also peforms a number of internal operations (retrieve-store memory, time the execution in debug mode only, check for a redirection in self._function_names_map). It also sets the toolbar as initialized and executes the initialize function of the meta.tdk.Toolbar class or the one of the derived class that sets initial settings.


		Parameters
		----------
		function_name : str
			The name of the function of the derived class to branch to.

		*arguments : object, optional
			An arbitrary number of non-named arguments to pass to the derived class' function.

		**keywords : object, optional
			An arbitrary number of named arguments to pass to the derived class' function.

		Returns
		-------
		object
			It returns the returned variable of the derived class' function.

		"""


	def set_function_map(self, function_map: object) -> bool:

		"""

		Set the dictionary that maps old function names to new.


		Parameters
		----------
		function_map : object
			A dictionary with old function names (keys) and new function names (values).

		Returns
		-------
		bool
			It always returns True.

		"""


	def mc(self, command: str, check_for_errors: bool) -> bool:

		"""

		Execute a session command and check if it has been executed properly.


		Parameters
		----------
		command : str
			The META command to execute.

		check_for_errors : bool, optional
			If True, the function will check the Info window for errors printed during the execution of the META command.

		Returns
		-------
		bool
			It always returns True. It will raise a tdk.InvalidCommandError exception if the command was invalid. It will raise a tdk.IncompleteCommandError exception if the command was incomplete.

		"""


	def mcd(self, command: str, check_for_errors: bool) -> bool:

		"""

		Execute a META command and print it if the Toolbar is set to debug mode.


		Parameters
		----------
		command : str
			The META command to execute and conditionally print.

		check_for_errors : bool, optional
			If True, the function will check the Info window for errors printed during the execution of the META command.

		Returns
		-------
		bool
			It always returns True. It will raise a tdk.InvalidCommandError exception if the command was invalid. It will raise a tdk.IncompleteCommandError exception if the command was incomplete.

		"""


	def __init__(self, name: str, display_name: str, memory_name: str, debug_mode: bool, relative_script_path: str) -> object:

		"""

		The constructor of class Toolbar.


		Parameters
		----------
		name : str
			The Toolbar's name.

		display_name : str
			The Toolbar's display name.

		memory_name : str, optional
			The name of the BETA variable where the Toolbar's Memory object will save its contents to.
			Default value is None, which means that no Memory class and functionality will be available.

		debug_mode : bool, optional
			Sets the debug mode member attribute of the Toolbar object.

		relative_script_path : str, optional
			The main script path relative to the Toolbar definition. While TDK is capable of detecting this on its own, it adds an overhead that can easily be avoided through the use of this argument. For example, if my_toolbar.toolbar and my_toolbar.py are located in the same folder, this argument should simply be 'my_toolbar.py'.

		Returns
		-------
		object
			A Toolbar object.

		"""


	def batch_only_function(self, function: object) -> object:

		"""

		A decorator to allow the decorated function to be executed only in batch mode.


		Parameters
		----------
		function : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def write_function_call_to_session(self, func: object) -> object:

		"""

		A decorator that will record every call of the decorated function to the session, as per TDK rules for Toolbar session compatibility.


		Parameters
		----------
		func : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def interactive_only_function(self):

		"""

		A decorator to allow the decorated function to be executed only in interactive mode.


		"""


	def debug_only_function(self, func: object) -> object:

		"""

		A decorator to allow the decorated function to be executed only when the Toolbar object is set to debug mode.


		Parameters
		----------
		func : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def disabled_draw_function(self, func: object) -> object:

		"""

		Decorator used to disable drawing during the execution of the decorated function. It is useful to speed up execution of functions that require re-drawing of META windows.


		Parameters
		----------
		func : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def disabled_toolbar_function(self, func: object) -> object:

		"""

		A decorator that disables the Toolbar when a function is executed. This is useful when the Toolbar script has generated a guitk window and interaction with the Toolbar window should no longer be available.


		Parameters
		----------
		func : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def timed_function(self, func: object) -> object:

		"""

		A decorator that times the decorated function when the Toolbar is set to debug mode.


		Parameters
		----------
		func : object
			The function to be decorated.

		Returns
		-------
		object
			The decorated function.

		"""


	def disable(self) -> bool:

		"""

		Disables the Toolbar window.


		Returns
		-------
		bool
			It always returns True.

		"""


	def enable(self) -> bool:

		"""

		Enables the Toolbar window.


		Returns
		-------
		bool
			It always returns True.

		"""


	def check_batch_mode(self) -> bool:

		"""

		Checks if META is in batch or session mode.


		Returns
		-------
		bool
			It returns True if META is in batch or session mode, False otherwise.

		"""


	def check_interactive_mode(self) -> bool:

		"""

		Checks if META is in interactive mode.


		Returns
		-------
		bool
			It returns True if META is in interactive mode, False otherwise.

		"""


	def print_memory_contents(self) -> bool:

		"""

		Print the Toolbar's Memory object contents if the Toolbar is in debug mode.


		Returns
		-------
		bool
			It always returns True.

		"""


	def get_item(self, item_name: str, item_class: object) -> object:

		"""

		Get item of a Toolbar.


		Parameters
		----------
		item_name : str
			The item's name.

		item_class : object, optional
			An item class, e.g. meta.tdk.TextBox.

		Returns
		-------
		object
			It returns the respective item object.

		"""


	def print(self, *items: object) -> bool:

		"""

		Print information while prepending a specific string with the Label of the Toolbar so it can easily be recognized.


		Parameters
		----------
		*items : object
			The items to print.

		Returns
		-------
		bool
			It always returns True.

		"""


	def dprint(self, *items: object) -> bool:

		"""

		Print information only if the Toolbar is set to debug mode, while prepending a specific string with the Label of the Toolbar so it can easily be recognized.


		Parameters
		----------
		*items : object
			The items to print.

		Returns
		-------
		bool
			It always returns True.

		"""


	def show_message(self, message_type: str, message: str) -> bool:

		"""

		Show a message window (only in interactive mode) and print its message.


		Parameters
		----------
		message_type : str
			The message type:
			- 'info'
			- 'warning'
			- 'error'

		message : str
			The message to display.

		Returns
		-------
		bool
			It always returns True.

		"""


	def show_question(self, question: str) -> bool:

		"""

		Show a question window (only in interactive mode) and return True or False based on the answer.


		Parameters
		----------
		question : str
			The question to be displayed.

		Returns
		-------
		bool
			It returns True if the answer is Yes, False otherwise.

		"""

class Memory():

	"""
	.. deprecated:: 23.1.0
		Use :py:func:`GetProcessSystemMetrics` instead.


	A class that acts as non-volatile memory for Python scripts. It can stores its members to a BETA variable and then retrieve them. This class is intended to be used exclusively by the meta.tdk.Toolbar class.
	"""


	_variable_name: str = None
	"""
	The name of the BETA variable where the members of this class' objects are stored to and retrieved from. It is marked as a read-only and private member.

	"""

	def __init__(self, beta_variable_name: str) -> object:

		"""

		The constructor of the object.


		Parameters
		----------
		beta_variable_name : str
			The name of the BETA variable.

		Returns
		-------
		object
			It returns a Memory object.

		"""

		import warnings; warnings.warn("Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.", DeprecationWarning)


	def store(self) -> object:

		"""

		Serialize and store the oject to the designated BETA variable.


		Returns
		-------
		object
			It returns two variables, a boolean and an Exception object or None. If the operation was successful, the boolean variable will be True and the second variable will be None. If not, the boolean variable will be False and the second will contain an Exception object if an exception was raised.

		"""


	def retrieve(self) -> object:

		"""

		Retrieve, deserialize and return a previously saved Memory object from the designated BETA variable.


		Returns
		-------
		object
			It returns two variables, a boolean and an Exception object or None. If the operation was successful, the boolean variable will be True and the second variable will be None. If not, the boolean variable will be False and the second will contain an Exception object if an exception was raised.

		"""


	def create(self, var_name: str) -> bool:

		"""

		Create a variable in the Memory object. Its value will be None.


		Parameters
		----------
		var_name : str
			The name of the variable to be created in the Memory object.

		Returns
		-------
		bool
			Returns True if successful, False if a variable named var_name already exists.

		"""


	def set(self, var_name: str, value: object) -> bool:

		"""

		Set the value of a variable in the Memory object.


		Parameters
		----------
		var_name : str
			The name of the variable to be set in the Memory object.

		value : object
			The value of the variable to be edited in the Memory object.

		Returns
		-------
		bool
			It always returns True.

		"""


	def clear(self) -> bool:

		"""

		Clears the Memory object of any stored variables.


		Returns
		-------
		bool
			It always returns True.

		"""


	def edit(self, var_name: str, var_value: object) -> bool:

		"""

		Edit the value of a stored variable in the Memory object.


		Parameters
		----------
		var_name : str
			The name of the variable to be edited in the Memory object.

		var_value : object
			The value of the variable to be edited in the Memory object.

		Returns
		-------
		bool
			It always returns True.

		"""


	def exists(self, var_name: str) -> bool:

		"""

		Check if a variable exists in the Memory object.


		Parameters
		----------
		var_name : str
			The name of the variable to be found in the Memory object.

		Returns
		-------
		bool
			It returns True if the variable was found, False otherwise.

		"""


	def get(self, var_name: str) -> object:

		"""

		Get the value of a stored variable in the Memory object.


		Parameters
		----------
		var_name : str
			The name of the variable in the Memory object whose value will be returned.

		Returns
		-------
		object
			It returns the variable's value.

		"""

class Timer():

	"""

	A class to measure time periods like a timer watch. This class is intended to be used by the meta.tdk.Toolbar class exclusively.
	"""


	_desc: str = None
	"""
	The description of the Timer. It is marked as a read-only and private member.

	"""

	_old: float = None
	"""
	The time where the Timer was started.

	"""

	_new: float = None
	"""
	The time where the Timer was stopped.

	"""

	_diff: float = None
	"""
	The recorded time of the Timer.

	"""

	def __init__(self, description: str, start: bool) -> object:

		"""

		The constructor of the Timer class.


		Parameters
		----------
		description : str
			A description of the process the timer measures.

		start : bool, optional
			If True, it will also start the timer.
			Default value is False.

		Returns
		-------
		object
			A Timer object.

		"""


	def start(self) -> bool:

		"""

		Starts the timer.


		Returns
		-------
		bool
			True if the timer is started.False if the timer is already started.

		"""


	def resume(self) -> bool:

		"""

		Resume the timer.


		Returns
		-------
		bool
			True if the timer is resumed.False if the timer was not paused.

		"""


	def split_print(self, str_format: str) -> str:

		"""

		Print and get the timed period at the current moment.


		Parameters
		----------
		str_format : str, optional
			A python string format. It should contain only enough information to format a float number.
			Default value is '{5.3f}'.

		Returns
		-------
		str
			It prints and returns the timed period at the current moment.

		"""


	def split(self) -> object:

		"""

		Return the timed period at the current moment.


		Returns
		-------
		object
			It returns the timed period at the current moment.

		"""


	def stop(self) -> float:

		"""

		Stop the timer.


		Returns
		-------
		float
			Returns the timed period.If not started, returns None.

		"""


	def print(self, str_format: str):

		"""

		Prints the time period if the timer is stopped.


		Parameters
		----------
		str_format : str, optional
			A python string format. It should contain only enough information to format a float number.
			Default value is '{5.3f}'.

		"""


	def stop_print(self, str_format: str) -> float:

		"""

		Stops the timer and prints the timed period.


		Parameters
		----------
		str_format : str, optional
			A python string format. It should contain only enough information to format a float number.
			Default value is '{5.3f}'.

		Returns
		-------
		float
			Returns the timed period if the timer is stopped.Returns None otherwise.

		"""

class Tab():

	"""

	A class for Tab items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Tab. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A Tab object.

		"""

class Item():

	"""

	A base class for Toolbar items.
	"""


	_toolbar: object = None
	"""
	The parent Toolbar object. It is marked as a read-only and private member.

	"""

	_name: str = None
	"""
	The item name. It is marked as a read-only and private member.

	"""

	_type: str = None
	"""
	The item type. It is marked as a read-only and private member.

	"""

	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Item. This constructor should be used only byt the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			An Item object.

		"""


	def enable(self) -> bool:

		"""

		Enables the Toolbar item.


		Returns
		-------
		bool
			It always returns True.

		"""


	def disable(self) -> bool:

		"""

		Disables the Toolbar Item.


		Returns
		-------
		bool
			It always returns True.

		"""


	def show(self) -> bool:

		"""

		Shows the Toolbar Item.


		Returns
		-------
		bool
			It always returns True.

		"""


	def hide(self) -> bool:

		"""

		Hides the Toolbar Item.


		Returns
		-------
		bool
			It always returns True.

		"""


	def set_font_color(self, red: int, green: int, blue: int) -> bool:

		"""

		Sets the font color of the Item. All three color component values have to be defined or not. If they are not defined, the font color resets to its default values.


		Parameters
		----------
		red : int, optional
			A red component value from 0-255. It can be an integer or string.

		green : int, optional
			A green component value from 0-255. It can be an integer or string.

		blue : int, optional
			A blue component value from 0-255. It can be an integer or string.

		Returns
		-------
		bool
			It always returns True.

		"""


	def set_background_color(self, red: int, green: int, blue: int) -> bool:

		"""

		Sets the background color of the Item. All three color component values have to be defined or not. If they are not defined, the background color resets to its default values.


		Parameters
		----------
		red : int, optional
			A red component value from 0-255. It can be an integer or string.

		green : int, optional
			A green component value from 0-255. It can be an integer or string.

		blue : int, optional
			A blue component value from 0-255. It can be an integer or string.

		Returns
		-------
		bool
			It always returns True.

		"""

class Menu():

	"""

	A class for Menu items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class TabPage. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			Returns the created TabPage object.

		"""

class group():

	"""

	A class for Group items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Group. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A Group object.

		"""


	def get_state(self) -> bool:

		"""

		Get the state of the Group.


		Returns
		-------
		bool
			It returns True if selected, False if unselected.

		"""


	def set_state(self, state: bool) -> bool:

		"""

		Set the Group's state.


		Parameters
		----------
		state : bool
			True to set it as selected, False to set it as deselected.

		Returns
		-------
		bool
			It always returns True.

		"""

class Button():

	"""

	A class for Button items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Button. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar item.

		name : str
			The name of the Button Item.

		Returns
		-------
		object
			A Button object.

		"""

class CheckBox():

	"""

	A class for CheckBox items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class CheckBox. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A CheckBox object.

		"""


	def get_state(self) -> bool:

		"""

		Get the state of the Check box.


		Returns
		-------
		bool
			It returns True if selected, False if unselected.

		"""


	def set_state(self, state: bool) -> bool:

		"""

		Set the Check box's state.


		Parameters
		----------
		state : bool
			True to set it as selected, False to set it as deselected.

		Returns
		-------
		bool
			It always returns True.

		"""

class DirectoryTextBox():

	"""

	A class for DirectoryTextBox items of Toolbars. Inherits members and functionality from the meta.tdk.TextBox and meta.tdk.Item classes.

	See Also
	--------
	meta.tdk.TextBox, meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class DirectoryTextBox. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A DirectoryTextBox object.

		"""

class FileTextBox():

	"""

	A class for FileTextBox items of Toolbars. Inherits members and functionality from the meta.tdk.TextBox and meta.tdk.Item classes.

	See Also
	--------
	meta.tdk.TextBox, meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class FileTextBox. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			the item's name.

		Returns
		-------
		object
			A FileTExtBox object.

		"""


	def get_filters(self) -> object:

		"""

		Get all defined filters that appear in the File text box's file manager.


		Returns
		-------
		object
			A list of filters as strings.

		"""


	def set_filter(self, path_filter: str) -> bool:

		"""

		Set the filter that will appear in the File text box's file manager from the already defined list of available filters.


		Parameters
		----------
		path_filter : str
			The path filter to set.

		Returns
		-------
		bool
			True if the path_filter argument exactly matches one of the defined filters, False otherwise.

		"""


	def add_filter(self, path_filter: int) -> bool:

		"""

		Add a filter to the filter list of a File text box's file manager.


		Parameters
		----------
		path_filter : int
			A filter that contains the typical filter patterns of file masks. Examples:
			- '(Text files *.txt)'
			- '*.txt'.
			META can handle a wide range of filter format in its file manager.

		Returns
		-------
		bool
			Returns True if the filter was added, False if the filter was already in the list.

		"""


	def remove_filter(self, path_filter: str) -> bool:

		"""

		Remove a filter from the File text box's file manager filter list.


		Parameters
		----------
		path_filter : str
			The filter to remove.

		Returns
		-------
		bool
			True if the filter was found in the filter list and removed, False if it was not found.

		"""


	def clear_filters(self) -> bool:

		"""

		Clear the File Text box's file manager filter list.


		Returns
		-------
		bool
			It always returns True.

		"""

class NotAllowedError():

	"""

	An exception raised when a performed action was not allowed. It is not meant to be caught, but as a sign of a serious error in the code. Inherits Python's base Exception class.
	"""

class ItemNameError():

	"""

	An exception raised when an item's name is not valid, does not exist or is duplicate. It is not meant to be caught, but as a sign of a serious error in the code. Inherits Python's base Exception class.
	"""

class ItemTypeError():

	"""

	An exception raised when requesting an item with specific type but another is found with a different type. It is not meant to be caught, but as a sign of a serious error in the code. Inherits Python's base Exception class.
	"""

class InvalidCommandError():

	"""

	An exception raised when executing an invalid command through meta.tdk.Toolbar.mc() or meta.tdk.Toolbar.mcd(). It is not meant to be caught, unless of course it is expected to send invalid commands to these functions. Inherits Python's base Exception class.

	See Also
	--------
	meta.tdk.Toolbar.mc, meta.tdk.Toolbar.mcd
	"""

class IncompleteCommandError():

	"""

	An exception raised when executing an incomplete command through meta.tdk.Toolbar.mc() or meta.tdk.Toolbar.mcd(). It is not meant to be caught, but as a sign of a serious error in the code as incomplete commands cannot be executed. Inherits Python's base Exception class.

	See Also
	--------
	meta.tdk.Toolbar.mc, meta.tdk.Toolbar.mcd
	"""

class Label():

	"""

	A class for Label items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Label. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A Label object.

		"""

class List():

	"""

	A class for List items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class List. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A List object.

		"""


	def get_column_names(self) -> object:

		"""

		Get the column names.


		Returns
		-------
		object
			It returns a list with the column names as strings.

		"""


	def get_row_keys(self, specifier: str) -> object:

		"""

		Get a list of all row keys.


		Parameters
		----------
		specifier : str
			Select which keys will be returned:
			- 'all': row keys of all rows will be returned
			- 'selected': row keys of selected rows will be returned

		Returns
		-------
		object
			It returns a list of row keys as strings.

		"""


	def get_rows(self, specifier: str, return_type: str) -> object:

		"""

		Get the List's full row data.


		Parameters
		----------
		specifier : str
			Select which keys will be returned:
			- 'all': row keys of all rows will be returned
			- 'selected': row keys of selected rows will be returned

		return_type : str, optional
			Choose the type of values in the returned dict. It can be either a 'list' or a 'dict'. Default value is 'list'.

		Returns
		-------
		object
			It returns a dict of either lists or dicts, where the dict keys will be the row keys and the dict values will be lists or dicts per row, depending on the return_type argument. If the return_type argument is 'list' then a list of the row values will be returned. If the return argument is 'dict', then a dictionary will be returned, where the keys will be the column names and the values will be the List's values per column for that specific row. All return items are ordered the way they appear in the List.

		"""


	def get_row(self, row_key: str, return_type: str) -> object:

		"""

		Get a row's full data.


		Parameters
		----------
		row_key : str
			The row key.

		return_type : str, optional
			Choose the type of the returned object. It can be either a 'list' or a 'dict'. Default value is 'list'.

		Returns
		-------
		object
			It returns either a list or dict, depending on the return_type argument. If the return_type argument is 'list' then a list of the row values will be returned. If the return argument is 'dict', then a dictionary will be returned, where the keys will be the column names and the values will be the rows's values per column. All return items are ordered the way they appear in the List.

		"""


	def get_value(self, row_key: str, column_name: str) -> str:

		"""

		Get the value of a specific row and column.


		Parameters
		----------
		row_key : str
			The row key.

		column_name : str
			The column name.

		Returns
		-------
		str
			The value of a specific row and column.

		"""


	def set_value(self, row_key: str, column_name, value: str) -> bool:

		"""

		Set the value of a specific row and column.


		Parameters
		----------
		row_key : str
			The row key.

		column_name : 
			The column name.

		value : str
			The value to set.

		Returns
		-------
		bool
			It returns True if the specific row key and column name have been found, False otherwise.

		"""


	def add_column(self, column_name: str) -> bool:

		"""

		Add a column to the List.


		Parameters
		----------
		column_name : str
			The column name.

		Returns
		-------
		bool
			It retuns True if the column was added, False if a column with the same name already exists.

		"""


	def remove_column(self, column_name: str) -> bool:

		"""

		Remove a column from the List.


		Parameters
		----------
		column_name : str
			The column name.

		Returns
		-------
		bool
			It returns True if the column was removed, False if it was not found.

		"""


	def add_row(self, row_key: str, values: object) -> bool:

		"""

		Add a row to the List.


		Parameters
		----------
		row_key : str
			A unique row key.

		values : object
			A list of values per column or a dictionary where the keys are the column names and the values are the row values per column.

		Returns
		-------
		bool
			It returns True if the row was added, False if the row key is not unique.

		"""


	def remove_row(self, row_key: str) -> bool:

		"""

		Remove a row from the list.


		Parameters
		----------
		row_key : str
			A row key.

		Returns
		-------
		bool
			It returns True if the row has been removed, False if the row key was not found in the List.

		"""


	def clear(self) -> bool:

		"""

		Remove all rows.


		Returns
		-------
		bool
			It always returns True.

		"""


	def reset(self) -> bool:

		"""

		Remove all rows and columns.


		Returns
		-------
		bool
			It always returns True.

		"""


	def set_selected_rows(self, row_keys: object) -> bool:

		"""

		Set the selected rows exclusively.


		Parameters
		----------
		row_keys : object
			A list of the row keys as strings of the rows to be selected exclusively.

		Returns
		-------
		bool
			It returns True if all row keys were found in the list, False otherwise.

		"""


	def deselect_rows(self, row_keys: object) -> bool:

		"""

		Deselect some rows.


		Parameters
		----------
		row_keys : object
			A list of row keys as strings of rows to deselect.

		Returns
		-------
		bool
			It returns True if all row keys were found in the List, False otherwise.

		"""


	def select_rows(self, row_keys: object) -> bool:

		"""

		Select some rows inclusively.


		Parameters
		----------
		row_keys : object
			A list of row keys as strings of rows to be selected.

		Returns
		-------
		bool
			It returns True if all row keys where found in the List, False otherwise.

		"""

class RadioButton():

	"""

	A class for RadioButton items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Group. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A RadioButton object.

		"""


	def get_state(self) -> bool:

		"""

		Get the state of the Radio button.


		Returns
		-------
		bool
			It returns True if selected, False if unselected.

		"""


	def select(self) -> bool:

		"""

		Select the Radio button.


		Returns
		-------
		bool
			It always returns True.

		"""

class Slider():

	"""

	A class for Slider items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Slider. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A Slider object.

		"""


	def get_value(self) -> int:

		"""

		Get the Slider's value.


		Returns
		-------
		int
			It returns the Slider's value.

		"""


	def get_max_limit(self) -> int:

		"""

		Get the Slider's max limit.


		Returns
		-------
		int
			It returns the Slider's max limit.

		"""


	def get_min_limit(self) -> int:

		"""

		Get the Slider's min limit.


		Returns
		-------
		int
			It returns the Slider's min limit.

		"""


	def set_value(self, value: int) -> bool:

		"""

		Set the Slider's value.


		Parameters
		----------
		value : int
			The value to set the Slider to.

		Returns
		-------
		bool
			It returns True if the set value is within the Slider's min and max limits, False otherwise.

		"""


	def set_max_limit(self, max_limit: int) -> bool:

		"""

		Set the Slider's max limit.


		Parameters
		----------
		max_limit : int
			The value to set the slider's max limit to.

		Returns
		-------
		bool
			It returns True if the new max limit is smaller than the current min limit, False otherwise.

		"""


	def set_min_limit(self, min_limit: int) -> bool:

		"""

		Set the Slider's min limit.


		Parameters
		----------
		min_limit : int
			The value to set the Slider's min limit to.

		Returns
		-------
		bool
			It returns True if the new min limit is larger than the current max limit, False otherwise.

		"""


	def set_limits(self, min_limit: int, max_limit: int) -> bool:

		"""

		Set the min and max Slider limits.


		Parameters
		----------
		min_limit : int
			The value to set the Slider's min limit to.

		max_limit : int
			The value to set the Slider's max limit to.

		Returns
		-------
		bool
			It returns True if the new min limit is less than the max limit, False otherwise.

		"""

class Spacer():

	"""

	A class for Spacer items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class Group. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : str
			The item's name.

		Returns
		-------
		object
			A Spacer object.

		"""

class TextBox():

	"""

	A class for TextBox items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: int) -> object:

		"""

		The constructor of class Group. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar object.

		name : int
			The item's name.

		Returns
		-------
		object
			A TextBox object.

		"""


	def is_editable(self) -> bool:

		"""

		Determine if the Text box is editable.


		Returns
		-------
		bool
			It returns True if it is editable, False otherwise.

		"""


	def get_text(self) -> str:

		"""

		Get the Text box's current text.


		Returns
		-------
		str
			It returns the Text box's current text.

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the Text box's text.


		Parameters
		----------
		text : str
			The text to set the Text box to.

		Returns
		-------
		bool
			If the Text box is editable, it always return True.If the Text box is not editable and the new text value matches one of the Text box's History value then it returns True, False otherwise.

		"""


	def get_history(self) -> object:

		"""

		Get the Text box History.


		Returns
		-------
		object
			It returns a list of the Text box's History values as strings.

		"""


	def add_to_history(self, text: str) -> bool:

		"""

		Add a value to the Text box's History.


		Parameters
		----------
		text : str
			The text to add to the Text box's History.

		Returns
		-------
		bool
			It returns True if the text has been added to the Text box's History.It returns False if the text already exists in the History, or if it is blank or consists only of spaces.

		"""


	def remove_from_history(self, text: str) -> bool:

		"""

		Remove a value from the Text box's History.


		Parameters
		----------
		text : str
			The text to remove from the Text box's History.

		Returns
		-------
		bool
			It returns True if the text has been found in the Text box's History and has been deleted, False otherwise.

		"""


	def clear_history(self) -> bool:

		"""

		Clear the Text box's History.


		Returns
		-------
		bool
			It always returns True.

		"""


	def set_state(self, state: bool) -> bool:

		"""

		Set the state of the Text box. A state of a Text box is a notion that reflects if its text is a valid value or not. For example, if a Text box is supposed to hold a positive integer but its callback function checks that the current value is not a positive integer, then it can subsequently set the Text box's state to False. A normal state (True) is depicted with white background and black font colors. An erroneous state (False) is depicted with red background and white font colors.


		Parameters
		----------
		state : bool
			True if the state is normal, False if it is erroneous.

		Returns
		-------
		bool
			It always returns True.

		"""

class ToggleButton():

	"""

	A class for Toggle Button items of Toolbars. Inherits members and functionality from the meta.tdk.Item class.

	See Also
	--------
	meta.tdk.Item
	"""


	def __init__(self, toolbar: object, name: str) -> object:

		"""

		The constructor of class ToggleButton. This constructor should be used only by the Toolbar class.


		Parameters
		----------
		toolbar : object
			The parent Toolbar item.

		name : str
			The name of the Toggle button Item.

		Returns
		-------
		object
			A ToggleButton item.

		"""


	def get_state(self) -> bool:

		"""

		Get the state of the Toggle button.


		Returns
		-------
		bool
			It returns True if switched on, False if switched off.

		"""


	def set_state(self, state: bool) -> bool:

		"""

		Set the Toggle button state.


		Parameters
		----------
		state : bool
			True to set it as switched on, False to set it as switched off.

		Returns
		-------
		bool
			It always returns True.

		"""

