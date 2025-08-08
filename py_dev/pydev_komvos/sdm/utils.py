from __future__ import annotations
from typing import *

def CreateCurve() -> object:

	"""

	This function creates a new curve object.

	Returns
	-------
	object
		Upon success, it returns a Class object referring to the newly created curve.
		Else, None is returned.

	See Also
	--------
	utils.AddCurveData

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def ShowLog(title_string: str) -> int:

	"""

	This function opens a monitor window and waits for the user to close it. It is similar to
	OpenMonitor only this one waits for the user to close the window before it continues with
	the execution of the script. This makes it useful for displaying a process log and letting
	the user decide if he wants to continue with the execution of the script.

	Parameters
	----------
	title_string : str
		The log window title to show.

	Returns
	-------
	int
		The function returns 1 if OK is pressed and 0 if Cancel is pressed.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.PrintMonitor("User text to display")
		    utils.ShowLog("Window title")


	"""

def XlsxClose(file: object) -> int:

	"""

	Closes the defined ".xlsx" file.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns 0 if the ".xlsx" is not found, or 1 on success.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxCreate() -> object:

	"""

	Creates a new empty xlsx_file.

	Returns
	-------
	object
		Returns a reference to the xlsx_file that is created, or None on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxGetCellValue(file: object, sheet: object, row: int, column: int) -> str:

	"""

	Returns the cell value from the specified row and column, from an .xlsx file ("Sheet1, Sheet2,..").

	Parameters
	----------
	file : object
		A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet name.

	row : int
		The row of the shell.

	column : int
		The column of the cell.

	Returns
	-------
	str
		Returns the value as string, or None if the cell is empty.

	See Also
	--------
	XlsxOpen, XlsxCreate, XlsxInsertSheet, XlsxGetCellValueByName, XlsxSetCellValue, XlsxSetCellValueByName, XlsxSave, XlsxSheetsCount, XlsxMaxSheetCell, XlsxClose

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxInsertSheet(file: object) -> int:

	"""

	Inserts a new empty sheet in the xlsx_file given.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxMaxSheetCell(file: object, sheet: object) -> object:

	"""

	Gets the cell with max row-column in the defined sheet, in the defined file.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet's name.

	Returns
	-------
	object
		Returns a list with 2 elements [row, column], or None if the sheet is empty.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxOpen(filename: str) -> object:

	"""

	Opens an existing xlsx_file and gets a reference to it.

	Parameters
	----------
	filename : str
		The path to the ".xlsx" filename.

	Returns
	-------
	object
		Returns a reference to the xlsx_file object.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSave(file: object, filename: object) -> int:

	"""

	Saves all changes in an opened xlsx_file.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	filename : object, optional
		The path where the ".xlsx" file will be saved.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSetCellValue(file: object, sheet: object, row: int, column: int, value: object) -> int:

	"""

	Sets a value in a cell, in the specified row and column, from sheet ("Sheet1, Sheet2,..") in the selected .xlsx file.

	Parameters
	----------
	file : object
		A reference to the .xlsx file created by XlsxCreate or XlsxOpen.

	sheet : object
		A string with the sheet name.

	row : int
		The row of the shell.

	column : int
		The column of the shell.

	value : object
		A string with the setting value.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	See Also
	--------
	XlsxOpen, XlsxCreate, XlsxInsertSheet, XlsxGetCellValue, XlsxGetCellValueByName, XlsxSetCellValueByName, XlsxSave, XlsxSheetsCount, XlsxMaxSheetCell, XlsxClose

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSheetsCount(file: object) -> int:

	"""

	Gets the count of sheets in the file given.

	Parameters
	----------
	file : object
		A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	Returns
	-------
	int
		Returns the number of sheets, or 0 if the xlsx_file is empty.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxGetCellValueByName(file: object, sheet: object, index: object) -> Any:

	"""

	Gets value from cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..").

	Parameters
	----------
	file : object
		A reference to an ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : object
		The sheet name.

	index : object
		The cell index.

	Returns
	-------
	Any
		Returns the value as a string, or 0 if the cell is empty.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def XlsxSetCellValueByName(file: object, sheet: str, index: str, value: str) -> int:

	"""

	Sets a value in a cell with index ("A1, B2"), from sheet ("Sheet1, Sheet2,..") in the file given.

	Parameters
	----------
	file : object
		A reference to the ".xlsx" file created by XlsxCreate or XlsxOpen.

	sheet : str
		A string with the sheet name.

	index : str
		A string with the cell index.

	value : str
		A string with the setting value.

	Returns
	-------
	int
		Returns 0 on success, or 1 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_element = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # create new-empty xlsx_file
		    xl_element = utils.XlsxCreate()
		
		    # insert new empty sheet
		    utils.XlsxInsertSheet(xl_element)
		
		    # get value from cell
		    value = utils.XlsxGetCellValue(xl_element, "Sheet1", 0, 0)
		    value = utils.XlsxGetCellValueByName(xl_element, "Sheet1", "A1")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_element, "Sheet1", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_element, "Sheet1", "A1", "value")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_element, "/home/user/mysheet.xlsx")
		
		    # Get the number of sheets
		    count = utils.XlsxSheetsCount(xl_element)
		
		    # find cell in max row-column in sheet
		    mat = utils.XlsxMaxSheetCell(xl_element, "Sheet1")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_element)


	"""

def ClearMonitor() -> int:

	"""

	This function clears the monitor output.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)
		
		    utils.ClearMonitor()
		
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

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

		import sdm
		from sdm import utils
		
		
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

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def OpenMonitor(title: str) -> int:

	"""

	This function opens a monitor window.
	It can be used to redirect the output of a script, ie to create log of a job.
	The window that opens features a text editor where the script can print and then you can 
	add your comments and save the text.

	Parameters
	----------
	title : str, optional
		The title of the monitor window.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def OpenMonitorNoEdit(title: str) -> int:

	"""

	This function opens a monitor window with the edit area in readonly mode.
	It can be used to redirect output of a script, ie to create log of a job.
	The window that opens features a text editor where thescript can print but you 
	cannot add your comments to save with the text.
	There is an optional argument, the title of the monitor window.

	Parameters
	----------
	title : str
		The title of the monitor window.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitorNoEdit("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)


	"""

def PrintMonitor(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring.
	It is almost identical to the 'print' function with the addition of the three color arguments.

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
		Always returns 1.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def ReadMonitor(line: int) -> str:

	"""

	This function reads a specific line from monitor window. The line is described by its index, 
	the first line having index 0 and the last LinesOfMonitor()-1.

	Parameters
	----------
	line : int
		The line number.

	Returns
	-------
	str
		Returns the contents of the 'line' or an empty string if the index is less than 0, 
		or greater than the number of lines.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", i, ", text:", txt)


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
		Returns 1 on success and 0 on failure.

	See Also
	--------
	SaveMonitorToTxt

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", str(i), ", text:", txt)
		    utils.SaveMonitor("/home/user/file.txt")


	"""

def SelectOpenDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for input.

	Parameters
	----------
	startin : str
		The path of the starting directory.

	Returns
	-------
	str
		Returns the selected directory on success, otherwise an empty string.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    dir = utils.SelectOpenDir("/home/user/")
		    print("Selected dir: ", dir)


	"""

def SelectOpenFile(flag: int, *filters: str) -> List[str]:

	"""

	This function opens the file manager and lets the user select one or more files. 
	If the flag is 0 then a single file selection is permitted, while if it is set to 1 
	a multi selection is performed. 
	The user can also type an optional list of file types for filtering.

	Parameters
	----------
	flag : int
		If set to 0, a single file selection is allowed.
		If set to 1, a multi file selection is allowed.

	*filters : str
		File types for filtering. (See example)

	Returns
	-------
	List[str]
		Returns a list containing the file name(s) selected on success.
		On error, or if ESCAPE is pressed, returns an empty list.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    m = utils.SelectOpenFile(0, "Ansa files (*.ansa)", "Foo files (*.foo)")
		    print(m[0])


	"""

def SelectOpenFileIn(initdir: str, flag: int, filters: str) -> object:

	"""

	This function opens the file manager and lets the user select one or more files.
	You can provide the directory in which to start. 
	If you type an empty string ("") or 0 the argument is ignored and the last accessed directory is used instead.
	If flag is 0 then a single file selection is permitted, if it is set to 1 a multi selection is performed.
	The user can also type an optional list of file types for filtering

	Parameters
	----------
	initdir : str
		The initial directory where the file manager will open.
		If set to ' ', the last accessed directory will be used.

	flag : int
		If set to 0, a single file selection is allowed.
		If set to 1, a multi file selection is allowed.

	filters : str, optional
		File types for filtering. (See example)

	Returns
	-------
	object
		Returns a list containing the file name(s) selected, on success.
		On error, or if ESCAPE was pressed, returns an empty list.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    m = utils.SelectOpenFileIn("/home/userdir/", 0)
		    print(m[0])
		    m = utils.SelectOpenFileIn(
		        "/home/userdir/", 0, "Ansa files (*.ansa)", "Foo files (*.foo)"
		    )
		    print(m[0])


	"""

def SelectSaveDir(startin: str) -> str:

	"""

	This function allows the user to select a directory for output.

	Parameters
	----------
	startin : str
		The path of the starting directory.

	Returns
	-------
	str
		Returns the selected directory on success, otherwise an empty string.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    dir = utils.SelectSaveDir("/home/user/")
		    print("Selected dir: ", dir)


	"""

def SelectSaveFile(filter: str='') -> List[str]:

	"""

	This function opens the file manager and lets the user select a file name to save. 
	The 'filter' argument is optional and if provided it is used to filter the displayed files.

	Parameters
	----------
	filter : str, optional
		File types for filtering. (See example)

	Returns
	-------
	List[str]
		Returns a list containing the file name selected on success.
		On error, or if ESCAPE is pressed, returns an empty list.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    m = utils.SelectSaveFile()
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFile("*.ansa")
		    print(m[0])


	"""

def SelectSaveFileIn(init_dir: str, filter: str) -> object:

	"""

	This function opens the file manager and lets the user select a file name to save.
	The 'init_dir' argument lets you specify the directory in which the file manager will open.
	An empty string ("") or a 0 can be passed to open the file manager in the last accessed directory.
	The 'filter' argument is optional and if provided it is used to filter the displayed files.

	Parameters
	----------
	init_dir : str
		The folder to start in.

	filter : str, optional
		File types for filtering. (See example)

	Returns
	-------
	object
		Returns a list containing the file name selected, on success.
		On error, or if ESCAPE was pressed, returns an empty list.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    m = utils.SelectSaveFileIn("/home/userdir/datafiles")
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFileIn("", "*.ansa")
		    print(m[0])
		
		
		# ...or...
		
		
		def main():
		    m = utils.SelectSaveFileIn(0, "*.ansa")
		    print(m[0])


	"""

def PrintMonitorHtml(txt: str, r_int: int, g_int: int, b_int: int) -> int:

	"""

	This is an output function for script monitoring. It prints html code in 
	monitor window with the addition of the three color arguments.

	Parameters
	----------
	txt : str
		The html code to print.

	r_int : int
		Red color integer.

	g_int : int
		Green color integer.

	b_int : int
		Blue color integer.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    utils.PrintMonitorHtml("<b>some text</b>", 255, 0, 0)
		    l = utils.LinesOfMonitor()
		    print("lines in monitor window:", l)


	"""

def SaveMonitorToTxt(filename: str) -> int:

	"""

	This function saves the contents of the monitor window in plain text format.

	Parameters
	----------
	filename : str
		The path and the filename where the text will be saved.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	See Also
	--------
	SaveMonitor

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    utils.OpenMonitor("Some title")
		    utils.PrintMonitor("Lorem ipsum", 255, 0, 0)
		    utils.PrintMonitor("dolor sit amet", 0, 255, 0)
		    lines = utils.LinesOfMonitor()
		    for i in range(lines):
		        txt = utils.ReadMonitor(i)
		        print("line:", str(i), ", text:", txt)
		    utils.SaveMonitorToTxt("/home/user/file.txt")


	"""

def XlsxMergeCells(file: object, sheet: str, row1: int, column1: int, row2: int, column2: int) -> object:

	"""

	Merges the specified cells of an ".xlsx" file.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cells' sheet.

	row1 : int
		The row number of the top left cell.

	column1 : int
		The column number of the top left cell.

	row2 : int
		The row number of the bottom right cell.

	column2 : int
		The column number of the bottom right cell.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxMergeCells(file, sheet, 2, 2, 4, 4)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellBorder(file: object, sheet: str, row: int, column: int, borders: str, style: str, color: str) -> object:

	"""

	Set the borders of a cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell.

	column : int
		The column number of the cell.

	borders : str
		The specified border. The accepted values are "left", "right",
		"top", "bottom", and any combination of them by using the "|"
		(e.g. "top|bottom").

	style : str
		The style of the line. The accepted values are "dashdot",
		"dashdotdot", "dashed", "dotted", "double", "hair", "medium",
		"mediumdashdot", "mediumdashdotdot", "mediumdashed", "none",
		"thick", "thin", and "slantdashdot".

	color : str
		The RGB color of the line in comma separated string.
		(e.g. "100, 100, 100").

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBorder(file, sheet, 2, 2, "top|bottom", "double", "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellBackgroundColor(file: object, sheet: str, row: int, column: int, color: str) -> object:

	"""

	Sets the background color of a cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell.

	column : int
		The column number of the cell.

	color : str
		The RGB background color of the cell in a comma separated string.
		(e.g. "100, 100, 100").

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBackgroundColor(file, sheet, 2, 2, "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxGetSheetName(file: object, index: int) -> str:

	"""

	Gets the name of a sheet by its index.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	index : int
		The index of the sheet of the specified file.

	Returns
	-------
	str
		Returns the name of the sheet on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellBorder(file, sheet, 2, 2, "top|bottom", "double", "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAdjustRowHeight(file: object, sheet: str, row: int) -> object:

	"""

	Adjusts the height of a row.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number starting from 0.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAdjustRowHeight(file, sheet, 1)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAdjustColumnWidth(file: object, sheet: str, column: int) -> object:

	"""

	Adjusts the width of a column.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	column : int
		The column number starting from 0.

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAdjustColumnWidth(file, sheet, 1)
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellFontStyle(file: object, sheet: str, row: int, column: int, style: str) -> object:

	"""

	Sets the font style in a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	style : str
		The specified font style. The accepted values are "bold", "italic", "underline" 
		and any combination of them by using the symbol "|". (e.g. "bold|italics")

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxSetCellFontStyle(file, sheet, 1, 1, "bold|italic")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAlignCellVertically(file: object, sheet: str, row: int, column: int, alignment: str) -> object:

	"""

	Aligns vertically a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	alignment : str
		The alignment type. The accepted values are "top", "bottom" and "center".

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAlignCellVertically(file, sheet, 1, 1, "center")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxAlignCellHorizontally(file: object, sheet: str, row: int, column: int, alignment: str) -> object:

	"""

	Aligns horizontally a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	alignment : str
		The alignment type. The accepted values are "left", "right" and "center".

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxAlignCellHorizontally(file, sheet, 1, 1, "center")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def XlsxSetCellFontColor(file: object, sheet: str, row: int, column: int, color: str) -> object:

	"""

	Sets the font color in a specified cell.

	Parameters
	----------
	file : object
		The object of the ".xlsx" file.

	sheet : str
		The name of the cell's sheet.

	row : int
		The row number of the cell starting from 0.

	column : int
		The column number of the cell starting from 0.

	color : str
		The RGB font color of the cell in a comma separated string. (e.g. "100, 100, 100")

	Returns
	-------
	object
		Returns None on success and raises an exception on failure.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    filename = "/full/path/of/created/file.xlsx"
		
		    file = utils.XlsxCreate()
		    sheet = utils.XlsxGetSheetName(file, 0)
		    utils.XlsxSetCellValue(file, sheet, 1, 1, "value")
		    utils.XlsxSetCellFontColor(file, sheet, 1, 1, "100, 100, 100")
		
		    utils.XlsxSave(file, filename)
		    utils.XlsxClose(file)


	"""

def SendEmail(fields: object) -> int:

	"""

	Send an email based on the input arguments.

	Parameters
	----------
	fields : object
		This is a dictionary that contains all inputs necessary for sending the email.
		Available options for the input dictionary are:
		"email agent": The application used for sending the email, e.g. "thunderbird", "outlook" or "no email agent".
		"email agent path": The path to the application,.
		"thunderbird application path": The path to Thunderbird application.
		"outlook application path": The path to the Outlook application.
		"email attachment folder": All files in this folder will be attached to the message.
		"From:": The sender's email address.
		"To:": The recipients' email addresses.
		"Subject:": The subject of the message.
		"Body:": The actual message that will be the body.
		"signature": If you want a signature to be appended to the body.
		"use gui": If you want a GUI to popup. By default this is "no".
		
		In case of a "no email agent" the following options are needed:
		"server name": The outgoing mail server (SMTP), e.g. "smtp.gmail.com"
		"connection security": Connection security, e.g. "None", "SSL", "STARTTLS"
		"authentication type": The authentication method, e.g. "Plain", "Login", "NTLM"
		"port": The port used for the connection, e.g. 465
		
		In case of authentication, you may need to use a username/password with the "Username" and "Password" keys.

	Returns
	-------
	int
		Always return 0.

	Examples
	--------
	::

		import sdm
		
		message_to_send = {}
		message_to_send["server name"] = "localhost"
		message_to_send["connection security"] = "None"
		message_to_send["authentication type"] = "Plain"
		message_to_send["port"] = "25"
		message_to_send["email agent"] = "Custom"
		message_to_send["use gui"] = "no"
		message_to_send["Subject:"] = "Download Resulted with empty parts"
		text_for_message = "This is a list of parts with missing representations..."
		message_to_send["Body:"] = text_for_message
		message_to_send["From:"] = "user@mail.local"
		message_to_send["To:"] = "other_user@mail.local"
		sdm.utils.SendEmail(message_to_send)


	"""

def AddCurveData(curve: object, coords: object):

	"""

	This function adds coordinates data to curve. For example: 
	AddCurveData(curve, [(x1,y1), (x2,y2), (x3,y3), ...])

	Parameters
	----------
	curve : object
		This argument is the created curve.

	coords : object, optional
		This argument is a list of pairs of floats.

	See Also
	--------
	utils.CreateCurve

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def DeleteCurve(curve: object):

	"""

	This function deletes the curve given as argument.
	
	

	Parameters
	----------
	curve : object
		This argument is the curve given to be deleted.

	See Also
	--------
	utils.CreateCurve

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		run_curve = utils.CreateCurve()
		curve_coords = [(1, 0.5), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.DeleteCurve(run_curve)


	"""

def GetMaterialPalette():

	"""

	This function gets a dictionary with material names and colors as described in palettes.xml or from a hardcoded palette (if not set in xml file). Dictionary has as keys the material type string and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'N/A Material Name': [100, 100, 100], 'Composite': [255, 165, 0], 'Silicon': [208, 238, 238], 'Steel': [70, 130, 180], 'Glass': [177, 211, 231], 'Multi-Material': [255, 0, 255], 'Plastic': [255, 0, 0], 'Aluminium': [0, 128, 0], 'Rubber': [255, 20, 147], 'Magnesium': [255, 215, 0], 'N/A Material Type': [169, 169, 169]}

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		material_type = "Steel"
		r_g_b = [0, 0, 0]
		
		material_colors_map = utils.GetMaterialPalette()
		if material_type in material_colors_map:
		    r_g_b = material_colors_map[material_type]
		else:
		    if "N/A Material Type" in material_colors_map:
		        r_g_b = material_colors_map["N/A Material Type"]
		print(r_g_b)


	"""

def GetCustomAttributePalette(keyword: str):

	"""

	This function gets a color palette for the attribute given as argument. It returns a dictionary with attribute names and colors as described in palettes.xml, if available. Otherwise, for some cases, it returns a dictionary from a hardcoded palette (cases like: Subsystem, Material, Diff, Status). Dictionary has as keys the attribute names and as values a list of 3 integers (r, g, b). 
	
	For example:
	{'Doors': [105, 65, 225], 'Roof': [255, 127, 0], 'Unused': [255, 255, 205], 'Frontsystem': [0, 139, 139], 'BiW': [178, 34, 34]}

	Parameters
	----------
	keyword : str
		This argument is the custom attribute keyword for the palette.

	See Also
	--------
	utils.GetMaterialPalette

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		palette = utils.GetCustomAttributePalette("Subsystem")
		print(palette)
		
		palette = utils.GetCustomAttributePalette("Status")
		print(palette)


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
		
		import sdm
		from sdm import utils
		
		
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

def XlsxRenameSheet(file: object, current_name: str, new_name: str):

	"""

	Renames the specified sheet in the xlsx_file given.

	Parameters
	----------
	file : object
		A reference to ".xlsx" file created by XlsxCreate or XlsxOpen.

	current_name : str
		The current name of the sheet.

	new_name : str
		The new name that will be given to the sheet.

	Examples
	--------
	::

		import sdm
		from sdm import utils
		
		
		def main():
		    # open xlsx_file
		    xl_file = utils.XlsxOpen("/home/user/mysheet.xlsx")
		
		    # insert new empty sheet
		    utils.XlsxRenameSheet(xl_file, "Sheet1", "Data")
		
		    # set value in cell
		    utils.XlsxSetCellValue(xl_file, "Data", 0, 0, "value")
		    utils.XlsxSetCellValueByName(xl_file, "Data", "A2", "10")
		
		    # save xlsx_file
		    utils.XlsxSave(xl_file, "/home/user/mysheet.xlsx")
		
		    # close xlsx_file
		    utils.XlsxClose(xl_file)


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

		import sdm
		from sdm import base
		from sdm import utils
		
		
		def main():
		    qa = utils.QualityAssurance()
		
		    q1 = qa.start_process("MeshPart")
		
		    # My program to mesh a part
		    # Preparations for mesh
		
		    q2 = qa.start_process("MeshCore")
		
		    # A function that mesh the part
		
		    qa.add_new_line("mesh_data")
		    qa.add_value("elements_number", 1421)
		    qa.add_current_memory_usage_value("mem_used_after_mesh")
		
		    qa.stop_process(q2)
		    qa.stop_process(q1)

	"""


	def start_process(self, process_name: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float) -> object:

		"""

		Declare the start of a QA process.


		Parameters
		----------
		process_name : str
			The name of the process.

		run_if : bool, optional
			Condition to start the process.

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

		Set the deafault compare values for the quality assurance mechanism.


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
			Set the default upper limit for comparing integers.

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


	def add_current_memory_usage_value(self, value_name_current_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float, compare_val_absolute: float) -> float:

		"""

		Add as value the current memory usage of the program. 


		Parameters
		----------
		value_name_current_memory : str
			The name of the value.

		run_if : bool, optional
			Condition to add the value.

		compare_val : float, optional
			A custom compare ratio (decimal) for current memory value.

		down_limit : float, optional
			A custom down limit for current memory value.

		up_limit : float, optional
			A custom upper limit for current memory value.

		compare_val_absolute : float, optional
			A custom absolute compare limit for the current value

		Returns
		-------
		float
			Returns the current memory usage of the program

		"""


	def add_peak_memory_usage_value(self, value_name_peak_memory: str, run_if: bool, compare_val: float, down_limit: float, up_limit: float, compare_val_absolute: float) -> float:

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

		compare_val_absolute : float, optional
			A custom absolute compare limit for the current value

		Returns
		-------
		float
			Returns the peak memory usage of the program

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

		A clock will start to run and it will stop at stop_lap.The laps have names.When running process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps. 


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


	def start_lap_on_master(self, clock_name: str, run_if: bool):

		"""

		A clock will start to run and it will stop at stop_lap.The laps have names.When the master process is stoped all times of laps will be added as values to the process. The process will have the numer of times a lap was started and the total time of the laps.


		Parameters
		----------
		clock_name : str
			The name of the clock.

		run_if : bool, optional
			Condition to start the lap.

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
		import sdm
		
		
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

		from sdm import utils
		
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

		from sdm import utils
		
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

		import sdm
		from sdm import utils
		
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

		import sdm
		from sdm import utils
		
		
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

def AddCurveToPlot(plot: object, curve: object):

	"""

	This function adds new curves to a created plot. 
	Can be used for one curve: AddCurveToPlot(plot, curve)
	or for multiple curves at once: AddCurveToPlot(plot, [curve1, curve2, curve3...])

	Parameters
	----------
	plot : object
		This argument is the plot.

	curve : object
		This argument is the curve to be added (single one) or a list of curves (for multiple curves).

	See Also
	--------
	utils.CreateCurve, utils.CreatePlot

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		
		run_curve1 = utils.CreateCurve()
		r_g_b1 = [200, 0, 0]
		curve_coords1 = [(1, 0.6), (2, 2), (3, 3.2)]
		utils.AddCurveData(run_curve1, coords=curve_coords1)
		utils.SetCurveProperties(run_curve1, type="Bar", color=r_g_b1, offset_on=True)
		
		run_curve2 = utils.CreateCurve()
		r_g_b2 = [0, 0, 200]
		curve_coords2 = [(1, 0.2), (2, 3), (3, 2.5)]
		utils.AddCurveData(run_curve2, coords=curve_coords2)
		utils.SetCurveProperties(run_curve2, type="Bar", color=r_g_b2, offset_on=True)
		
		utils.AddCurveToPlot(plot, [run_curve1, run_curve2])
		utils.DeleteCurve(run_curve1)
		utils.DeleteCurve(run_curve2)
		
		sdm_base.ShowPlotInViewer(plot, "Plot", "Curves")
		utils.DeletePlot(plot)


	"""

def SetCurveProperties(curve: object, type: str, color: object, width: int, label: str, marker_style: str, marker_size: int, dash_style: str, offset_on: bool, curve_attributes: object, curve_points_attributes: object):

	"""

	This function sets properties to a created curve. Argument options:

	- type: Line or Bar
	- color: [r,g,b]
	- width
	- label 
	- marker_style: None, Cross, Plus, WhiteSquare, BlackSquare, Diamond, Circle, TriangleUp, TriangleDown
	- marker_size: integer 
	- dash_style: Solid, SparseShortDot, SparseDot, SparseLongDot, Dash, ThickDash, DashDot, ShortDot, Dot, LongDot, 
	        DenseShortDot, DenseDot, DenseLongDot 
	- offset: True or False
	- curve_attributes: {"Module id":"Karosseriegerippe", "CarLine":"LU",...} 
	- curve_points_attributes: { 0:attr_map_for_point0, 1:attr_map_for_point1, 2:attr_map_for_point2 ... }

	Parameters
	----------
	curve : object
		This argument is the curve to add properties to.

	type : str, optional
		This argument is the curve type.

	color : object, optional
		This argument is a list of 3 integers (0-255 for r, g, b channels) 
		to define color.

	width : int, optional
		This argument is the curve width,

	label : str, optional
		This argument is a label (to be seen in legend).

	marker_style : str, optional
		This argument is the marker style.

	marker_size : int, optional
		This argument is the marker size. Default value is 5.

	dash_style : str, optional
		This argument is the dash style.

	offset_on : bool, optional
		This argument enables or disables offset (True or False).

	curve_attributes : object, optional
		This argument is a dictionary with attribute name-values.

	curve_points_attributes : object, optional
		This argument is a dictionary with attribute name-values for curve's points. 
		Dictionary has as key an integer and as data a map of name-values.

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		run_curve = utils.CreateCurve()
		r_g_b = [0, 0, 220]
		curve_coords = [(1, 0.2), (2, 1.3), (3, 0.9), (4, 2.1)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		curve_attrs = {"Module Id": "44", "Project": "New"}
		curve_points_attrs = {
		    0: {"Id": "01", "Name": "Phase1"},
		    1: {"Id": "02", "Name": "Phase2"},
		    2: {"Id": "03", "Name": "Phase3"},
		    3: {"Id": "04", "Name": "Phase4"},
		}
		utils.SetCurveProperties(
		    run_curve,
		    type="Line",
		    color=r_g_b,
		    offset_on=True,
		    label="Line Curve",
		    dash_style="DashDot",
		    curve_attributes=curve_attrs,
		    curve_points_attributes=curve_points_attrs,
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		sdm_base.ShowPlotInViewer(plot, "Plot", "Curve")
		utils.DeletePlot(plot)


	"""

def SetYAxisProperties(plot: object, title: str, unit: str, min_max: object, num_of_steps: int, step_labels: object, show_values_on_axis: bool) -> None:

	"""

	This function sets properties for the Y axis of a plot. For example: SetYAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)

	Parameters
	----------
	plot : object
		This argument is the relevant plot.

	title : str, optional
		This argument is the title shown for Y axis.

	unit : str, optional
		This argument is the unit used for Y axis. It would be shown beside the title.

	min_max : object, optional
		This argument is a pair of 2 numbers (integers or floats) to set minimum and 
		maximum values of Y axis.

	num_of_steps : int, optional
		This argument sets the number of steps to be used.

	step_labels : object, optional
		This argument is a dictionary of integer:string pairs, where key is the step 
		index and value is the label we want to use for this step. If user hasn't set 
		the number of steps to be used, number of steps is set by the number of given 
		labels plus 1.

	show_values_on_axis : bool, optional
		This argument is used to set if values should be visible on axis (True or False).

	Returns
	-------
	None
		Always returns None.

	See Also
	--------
	utils.SetXAxisProperties

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="Bar_Curve", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		
		sdm_base.ShowPlotInViewer(plot, "Mass", "Mass Plot")


	"""

def SetXAxisProperties(plot: object, title: str, unit: str, min_max: object, num_of_steps: int, step_labels: object, show_values_on_axis: bool):

	"""

	This function sets properties for the X axis of a plot. For example: SetXAxisProperties(Plot, title="Mass", unit="kg", 
	min_max=(0,1000), num_of_steps=12, step_labels={index_of_step_1:label_at_step_1, index_of_step_2:label_at_step_2 ...}, 
	show_values_on_axis=True)

	Parameters
	----------
	plot : object
		This argument is the relevant plot.

	title : str, optional
		This argument is the title shown for X axis.

	unit : str, optional
		This argument is the unit used for X axis. It would be shown beside the title.

	min_max : object, optional
		This argument is a pair of 2 numbers (integers or floats) to set minimum and 
		maximum values of X axis.

	num_of_steps : int, optional
		This argument sets the number of steps to be used.

	step_labels : object, optional
		This argument is a dictionary of integer:string pairs, where key is the step 
		index and value is the label we want to use for this step. If user hasn't set 
		the number of steps to be used, number of steps is set by the number of given 
		labels plus 1.

	show_values_on_axis : bool, optional
		This argument is used to set if values should be visible on axis (True or False).

	See Also
	--------
	utils.SetYAxisProperties

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="Bar_Curve", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		
		sdm_base.ShowPlotInViewer(plot, "Mass", "Mass Plot")


	"""

def SetPlotProperties(plot: object, title: str, show_legend: bool, legend_position: str, show_grid: bool):

	"""

	This function sets properties for the given plot. Available values:

	- legend_position: TopRight, TopLeft, BottomRight, BottomLeft
	- show_legend: True/False
	- show_grid: True/False

	Parameters
	----------
	plot : object
		This argument is the relevant plot to set properties to.

	title : str, optional
		This argument is the title to give to the plot.

	show_legend : bool, optional
		Flag to set if legend should be shown or not (True/False). Legend is given as 
		curve label (see function utils.SetCurveProperties).

	legend_position : str, optional
		This argument sets the position of legend: TopRight, TopLeft, BottomRight, 
		BottomLeft.

	show_grid : bool, optional
		Flag to set if grid should be shown or not (True/False).

	See Also
	--------
	utils.CreatePlot

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="common", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		utils.SetPlotProperties(
		    plot,
		    title="My Mass Plot",
		    show_legend=True,
		    legend_position="TopRight",
		    show_grid=True,
		)
		
		sdm_base.ShowPlotInViewer(plot, "Mass", "Mass Plot")


	"""

def CreatePlot():

	"""

	This function creates a new plot.

	See Also
	--------
	utils.SetPlotProperties

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		# example 1: plain plot
		plot1 = utils.CreatePlot()
		sdm_base.ShowPlotInViewer(plot1, "My Plot", "Plot Page")
		utils.DeletePlot(plot1)
		
		# example 2:
		plot = utils.CreatePlot()
		
		run_curve = utils.CreateCurve()
		r_g_b = [80, 220, 250]
		curve_coords = [(1, 30), (2, 10), (3, 55), (4, 95), (5, 80), (6, 45)]
		utils.AddCurveData(run_curve, coords=curve_coords)
		utils.SetCurveProperties(
		    run_curve, type="Bar", width=10, color=r_g_b, label="common", offset_on=True
		)
		utils.AddCurveToPlot(plot, run_curve)
		utils.DeleteCurve(run_curve)
		
		steps_dict = {1: "Low", 5: "Normal", 9: "Limit"}
		utils.SetYAxisProperties(
		    plot,
		    title="Mass",
		    unit="kg",
		    min_max=(0, 100),
		    num_of_steps=10,
		    step_labels=steps_dict,
		    show_values_on_axis=True,
		)
		utils.SetXAxisProperties(plot, title="Parts", show_values_on_axis=True)
		utils.SetPlotProperties(
		    plot,
		    title="My Mass Plot",
		    show_legend=True,
		    legend_position="TopRight",
		    show_grid=True,
		)
		
		sdm_base.ShowPlotInViewer(plot, "Mass", "Mass Plot")
		utils.DeletePlot(plot)


	"""

def DeletePlot(plot: object):

	"""

	This function deletes the plot object given as argument. 

	Parameters
	----------
	plot : object
		This argument is the plot that is going to be deleted.

	See Also
	--------
	utils.CreatePlot

	Examples
	--------
	::

		import sdm
		from sdm import utils, sdm_base
		
		plot = utils.CreatePlot()
		sdm_base.ShowPlotInViewer(plot, "My Plot", "Plot Page")
		utils.DeletePlot(plot)


	"""

class ParallelJobsDispatcher():

	"""

	Objects of this class enable the dispatching of parallel python script jobs to BETA app workers.
	
	Each parallel job is depicted through a python file, either pre-existing or created just-in-time temporarily.

	Examples
	--------
	::

		from sdm import utils
		
		
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
		import sdm
		from sdm import utils
		
		
		def main():
		    dict_metrics = utils.GetProcessSystemMetrics("memory")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "KB")
		    # or dict_metrics = utils.GetProcessSystemMetrics("memory", "bytes", True)
		    for item in dict_metrics.items():
		        print(item)
		
		
		if __name__ == "__main__":
		    main()


	"""

