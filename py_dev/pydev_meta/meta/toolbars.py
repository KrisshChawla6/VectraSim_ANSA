from __future__ import annotations
from typing import *

def ListAddColumn(toolbar_name: str, list_name: str, column_name: str) -> int:

	"""

	Adds a new column with specific title in the list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	column_name : str
		Name of the new column.

	Returns
	-------
	int
		Returns 1 if the column has been added; otherwise, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    column_name = "Time"
		    # add columns:
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		    column_name = "Distance"
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListAddKey(toolbar_name: str, list_name: str, row_key: str) -> int:

	"""

	Adds a new row with specific key in the list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key : str
		Name of the new row key.

	Returns
	-------
	int
		Returns 1 if the row has been added; otherwise, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    row_key = "T01"
		    # add row key:
		    ret = toolbars.ListAddKey(toolbar_name, list_name, row_key)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListAddRow(toolbar_name: str, list_name: str, row_key: str, value_list: object) -> int:

	"""

	Adds a new row with specific key in the list, along with a set of values.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key : str
		Name of the new row key.

	value_list : object
		List of values to be added.

	Returns
	-------
	int
		Returns 1 if the row has been added; otherwise, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    column_name = "Time"
		    # add columns:
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		    column_name = "Distance"
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		
		    toolbar_name = "Test"
		    list_name = "TestList"
		    row_key = "T02"
		    value_list = ["0.33s", "25m"]
		    # add rows:
		    ret = toolbars.ListAddRow(toolbar_name, list_name, row_key, value_list)
		    print(ret)
		
		    # data list may be smaller than column number:
		    row_key = "T03"
		    ret = toolbars.ListAddRow(toolbar_name, list_name, row_key, value_list)
		    print(ret)
		
		    # data list may contain zero-length elements:
		    row_key = "T04"
		    ret = toolbars.ListAddRow(toolbar_name, list_name, row_key, value_list)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListClear(toolbar_name: str, list_name: str) -> int:

	"""

	Clears the list. All row and column entries are removed.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	int
		Returns 1 if the list has been cleared; otherwise, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    ret = toolbars.ListClear(toolbar_name, list_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetAllKeys(toolbar_name: str, list_name: str) -> object:

	"""

	Returns an array of the row keys of the specified list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	object
		Returns a list object of the row keys.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vColumns = toolbars.ListGetColumns(toolbar_name, list_name)
		    print("List Columns: " + str(vColumns))
		
		    vKeys = toolbars.ListGetAllKeys(toolbar_name, list_name)
		    print("List Keys: " + str(vKeys))
		
		    vRows = toolbars.ListGetAllRows(toolbar_name, list_name)
		    print("List Contents: " + str(vRows))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetAllRows(toolbar_name: str, list_name: str) -> object:

	"""

	Returns the row contents of the specified list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	object
		Returns a map object of the row keys along with their row contents;
		the row contents are returned as list objects.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vRows = toolbars.ListGetAllRows(toolbar_name, list_name)
		    print("List Contents: " + str(vRows))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetColumns(toolbar_name: str, list_name: str) -> object:

	"""

	Returns an array of the list's column names.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	object
		Return a list object containing the names of the list's columns.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vColumns = toolbars.ListGetColumns(toolbar_name, list_name)
		    print("List Columns: " + str(vColumns))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetSelectedKeys(toolbar_name: str, list_name: str) -> object:

	"""

	Returns the selected row's or rows' keys of a list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	object
		Returns an arrray object containing the selected list row keys.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vSelection = toolbars.ListGetSelectedKeys(toolbar_name, list_name)
		    print("Selected IDs: " + str(vSelection))
		
		    vSelectionRows = toolbars.ListGetSelectedRows(toolbar_name, list_name)
		    print("Selected Rows: " + str(vSelectionRows))
		
		    for rowId in vSelection:
		        column_name = "Time"
		        print(
		            "Selected time: "
		            + toolbars.ListGetValue(toolbar_name, list_name, rowId, column_name)
		        )
		        column_name = "Distance"
		        print(
		            "Selected distance: "
		            + toolbars.ListGetValue(toolbar_name, list_name, rowId, column_name)
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetSelectedRows(toolbar_name: str, list_name: str) -> object:

	"""

	Returns the selected rows of the specified list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	Returns
	-------
	object
		Returns a map object of the selected row keys along with their row contents. 
		The row contents are returned as list objects.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vSelection = toolbars.ListGetSelectedKeys(toolbar_name, list_name)
		    print("Selected IDs: " + str(vSelection))
		    vSelectionRows = toolbars.ListGetSelectedRows(toolbar_name, list_name)
		    print("Selected Rows: " + str(vSelectionRows))
		    for rowId in vSelection:
		        column_name = "Time"
		        print(
		            "Selected time: "
		            + toolbars.ListGetValue(toolbar_name, list_name, rowId, "Time")
		        )
		        column_name = "Distance"
		        print(
		            "Selected distance: "
		            + toolbars.ListGetValue(toolbar_name, list_name, rowId, "Distance")
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListGetValue(toolbar_name: str, list_name: str, row_key: str, column_name: str) -> str:

	"""

	Returns the list value that is in a specific row and column combination.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key : str
		Name of the row key.

	column_name : str
		Name of the column.

	Returns
	-------
	str
		Returns the value that a list has on a specific row and column combination.
		If there is not such value, returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vSelection = toolbars.ListGetSelectedKeys(toolbar_name, list_name)
		    print("Selected IDs: " + str(vSelection))
		    vSelectionRows = toolbars.ListGetSelectedRows(toolbar_name, list_name)
		    print("Selected Rows: " + str(vSelectionRows))
		    for rowId in vSelection:
		        column_name = "Time"
		        print(
		            "Selected time: " + toolbars.ListGetValue("Test", "TestList", rowId, "Time")
		        )
		        column_name = "Distance"
		        print(
		            " Selected distance: "
		            + toolbars.ListGetValue("Test", "TestList", rowId, "Distance")
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListRemoveRow(toolbar_name: str, list_name: str, row_key: str) -> int:

	"""

	Removes the row, having the specified key, from the list.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key : str
		Name of the row key.

	Returns
	-------
	int
		Returns 1 if the row has been removed; otherwise, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    vSelection = toolbars.ListGetSelectedKeys(toolbar_name, list_name)
		    for rowId in vSelection:
		        bOk = toolbars.ListRemoveRow(toolbar_name, list_name, rowId)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListSetValue(toolbar_name: str, list_name: str, row_key: str, column_name: str, new_value: str) -> int:

	"""

	Sets a new value into the specificed row and column field.
	Any pre-existed content will be replaced.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key : str
		Name of the row key.

	column_name : str
		Name of the column.

	new_value : str
		Value to be set.

	Returns
	-------
	int
		Returns 1 if the value has been set; otherwise, returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Test"
		    list_name = "TestList"
		    column_name = "Time"
		    # add columns:
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		    column_name = "Distance"
		    ret = toolbars.ListAddColumn(toolbar_name, list_name, column_name)
		    print(ret)
		    # add row (verbose style):
		    row_key = "T01"
		    ret = toolbars.ListAddKey(toolbar_name, list_name, row_key)
		    print(ret)
		    column_name = "Time"
		    new_value = "0.11s"
		    ret = toolbars.ListSetValue(
		        toolbar_name, list_name, row_key, column_name, new_value
		    )
		    print(ret)
		    column_name = "Distance"
		    new_value = "10m"
		    ret = toolbars.ListSetValue(
		        toolbar_name, list_name, row_key, column_name, new_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CheckboxGetState(toolbar_name: str, checkbox_name: str):

	"""

	This function gets the state, checked or not checked, of a checkbox of a
	given toolbar.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	checkbox_name : str
		Name of the checkbox.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    checkbox_name = "Checkbox 1"
		
		    state = meta.toolbars.CheckboxGetState(toolbar_name, checkbox_name)
		    if state == 1:
		        print("Checked")
		    elif state == 0:
		        print("Not checked")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def RadiobuttonGetState(toolbar_name: str, radio_name: str) -> int:

	"""

	This function gets the state (checked or not checked) of a radio button of a
	given toolbar.

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
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    radio_name = "Radiobutton 1"
		    state = toolbars.RadiobuttonGetState(toolbar_name, radio_name)
		    if state == 1:
		        print("Enabled")
		    elif state == 0:
		        print("Disabled")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderGetMaxValue(toolbar_name: str, slider_name: str) -> int:

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
		It returns an integer referring to the maximum value of the slider of the given
		toolbar. Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = toolbars.SliderGetMaxValue(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderGetMinValue(toolbar_name: str, slider_name: str) -> int:

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

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = toolbars.SliderGetMinValue(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SliderGetValue(toolbar_name: str, slider_name: str) -> int:

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
		It returns an integer referring to the value of the slider of the given toolbar.
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    slider_name = "Slider 1"
		
		    slider_value = toolbars.SliderGetValue(toolbar_name, slider_name)
		    print(slider_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TextboxGetValue(toolbar_name: str, textbox_name: str) -> str:

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

	See Also
	--------
	toolbars.TextboxGetAllValues, toolbars.TextboxIsEditable

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    textbox_name = "Textbox 1"
		
		    text = toolbars.TextboxGetValue(toolbar_name, textbox_name)
		    print(text)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TogglebuttonGetState(toolbar_name: str, togglebutton_name: str) -> int:

	"""

	This function gets the state (pushed or not pushed) of a togglebutton of a given
	toolbar.

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
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    togglebutton_name = "Togglebutton 1"
		
		    state = toolbars.TogglebuttonGetState(toolbar_name, togglebutton_name)
		    if state == 1:
		        print("Pushed")
		    elif state == 0:
		        print("Not pushed")
		    elif state == -1:
		        print("Failure!")
		
		
		if __name__ == "__main__":
		    main()


	"""

def TextboxGetAllValues(toolbar_name: str, textbox_name: str) -> object:

	"""

	Returns an array of the history values contained in the specified textbox. The 
	same function may be used to retrieve the history entries of a file or directory
	textbox.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	textbox_name : str
		Name of the textbox.

	Returns
	-------
	object
		Returns a list object of the textbox entries.

	See Also
	--------
	toolbars.TextboxGetValue, toolbars.TextboxIsEditable, toolbars.FileTextboxGetAllWildcards

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "MyToolbar"
		    textbox_name = "MyTextbox"
		    vValues = toolbars.TextboxGetAllValues(toolbar_name, textbox_name)
		    print("Contents: " + str(vValues))
		
		
		if __name__ == "__main__":
		    main()


	"""

def GroupGetCheckState(toolbar_name: str, group_name: str) -> int:

	"""

	This function returns the current checked status of a user toolbar checkable 
	group.

	Parameters
	----------
	toolbar_name : str
		Name of toolbar

	group_name : str
		Name of (checkable) group

	Returns
	-------
	int
		The function returns 1 if the group is checked, 0 if unchecked. If the group is 
		not checkable or in case of failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "MyToolbar"
		    group_name = "MyGroup"
		    c = toolbars.GroupGetCheckState(toolbar_name, group_name)
		    if c == 1:
		        print("Group is checked")
		    elif c == 0:
		        print("Group is not checked")
		    elif c == -1:
		        print("Not a checkable group")
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetLabel(toolbar_name: str, item_name: str) -> str:

	"""

	This function returns the label of a user toolbar item.

	Parameters
	----------
	toolbar_name : str
		Name of toolbar

	item_name : str
		Name of item

	Returns
	-------
	str
		Returns the label string. If the item is not found, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "ToolbarLabels"
		    item_name = "MyButton"
		    # Need some documentation? Run this with F5
		    label = toolbars.GetLabel(toolbar_name, item_name)
		    print(label)
		    item_name = "MyCheckbox"
		    label = toolbars.GetLabel(toolbar_name, item_name)
		    print(label)
		    item_name = "MyTextbox"
		    label = toolbars.GetLabel(toolbar_name, item_name)
		    print(label)
		    item_name = "MyLabel"
		    label = toolbars.GetLabel(toolbar_name, item_name)
		    print(label)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListSelectRows(toolbar_name: str, list_name: str, row_key_list: object) -> int:

	"""

	Selects list rows having the specified keys. An empty row_key_list will clear
	(any) current row selections. The toolbar containing the list must be visible
	during the call of this function. 

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key_list : object
		List of keys of rows to be selected.

	Returns
	-------
	int
		Returns 1 if the selection has been applied; otherwise, it returns 0.

	See Also
	--------
	ListOnlySelectRows

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "TOOLBAR"
		    list_name = "LIST"
		    row_key_list = "A,B"
		    ret = toolbars.ListSelectRows(toolbar_name, list_name, row_key_list)
		    print(ret)
		    strSelected = str(toolbars.ListGetSelectedRows(toolbar_name, list_name))
		    print("Selected rows: " + strSelected)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ListOnlySelectRows(toolbar_name: str, list_name: str, row_key_list: object) -> int:

	"""

	Selects list rows having the specified keys without executing the associated
	user commands. An empty row_key_list will clear (any) current row selections.
	The toolbar containing the list must be visible during the call of this
	function. 

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	list_name : str
		Name of the list.

	row_key_list : object
		List of keys of rows to be selected.

	Returns
	-------
	int
		Returns 1 if the selection has been applied; otherwise, it returns 0.

	See Also
	--------
	ListSelectRows

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "TOOLBAR"
		    list_name = "LIST"
		    row_key_list = "A,B"
		    ret = toolbars.ListOnlySelectRows(toolbar_name, list_name, row_key_list)
		    print(ret)
		    strSelected = str(toolbars.ListGetSelectedRows(toolbar_name, list_name))
		    print("Selected rows: " + strSelected)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ToolbarGetDefaultsPath(toolbar_name: str) -> str:

	"""

	Returns the path of the toolbar's default's file.

	Parameters
	----------
	toolbar_name : str
		Name of toolbar

	Returns
	-------
	str
		Returns the defaults path of the toolbar. If the toolbar is not found, an empty
		string will be returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Pedestrian"
		    default_path = toolbars.ToolbarGetDefaultsPath(toolbar_name)
		    print("Defaults path: " + default_path)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TextboxIsEditable(toolbar_name: str, textbox_name: str) -> int:

	"""

	This function checks if a textbox of a given toolbar can be edited by the user.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	textbox_name : str
		Name of the textbox.

	Returns
	-------
	int
		This function returns 1 if the textbox is editable, and 0 if it's not. 
		If there is not a textbox with such name, it returns 0.

	See Also
	--------
	toolbars.TextboxGetValue, toolbars.TextboxGetAllValues

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    textbox_name = "Textbox 1"
		    isEditable = toolbars.TextboxIsEditable(toolbar_name, textbox_name)
		    print(str(isEditable))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ItemIsVisible(toolbar_name: str, item_name: str) -> int:

	"""

	This function checks the visibility status of a user toolbar item, e.g. button, 
	label, etc.

	Parameters
	----------
	toolbar_name : str
		Name of the toolbar.

	item_name : str
		Item name.

	Returns
	-------
	int
		This function returns 1 if the item has visible status, and 0 if it has not. 
		If there is not an item with such name, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "Toolbar 1"
		    item_name = "Textbox 1"
		    isVisible = toolbars.ItemIsVisible(toolbar_name, item_name)
		    print(str(isVisible))
		
		
		if __name__ == "__main__":
		    main()


	"""

def FileTextboxGetAllWildcards(toolbar_name: str, filetextbox_name: str) -> object:

	"""

	Returns an array of the wildcards (filters) set to the specified file textbox.

	Parameters
	----------
	toolbar_name : str

	filetextbox_name : str

	Returns
	-------
	object
		Returns a list containing the File Textbox wildcards.

	See Also
	--------
	toolbars.TextboxGetAllValues

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import toolbars
		
		
		def main():
		    toolbar_name = "MyToolbar"
		    filetextbox_name = "MyFileTextbox"
		    vValues = toolbars.FileTextboxGetAllWildcards(toolbar_name, filetextbox_name)
		    print("Wildcards: " + str(vValues))
		
		
		if __name__ == "__main__":
		    main()


	"""

