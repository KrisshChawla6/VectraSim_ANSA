from __future__ import annotations
from typing import *

def BoundingAreaOfSpreadsheet(sheet_name: str) -> object:

	"""

	This function finds the spreadsheet bounding area for a given sheet. Bounding area is described by top and bottom rows and left and right columns.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	Returns
	-------
	object
		It returns a 2x2 dimensional list which containts the bounding area for the given sheet. 
		Member at position [0][0] of list refers to top row.
		Member at position [0][1] of list refers to left column.
		Member at position [1][0] of list refers to bottom row.
		Member at position [1][1] of list refers to right column.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		
		    bounding_area = spreadsheet.BoundingAreaOfSpreadsheet(sheet_name)
		    if len(bounding_area) > 0:
		        print(bounding_area[0][0])  # top row
		        print(bounding_area[0][1])  # left column
		        print(bounding_area[1][0])  # bottom row
		        print(bounding_area[1][1])  # right column
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsSpreadsheetCell(spreadsheet_cell: object) -> int:

	"""

	This function checks whether an object is of class SpreadsheetCell.

	Parameters
	----------
	spreadsheet_cell : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class SpreadsheetCell, or 0 if object is not of class SpreadsheetCell.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    row = 1
		    column = 1
		
		    ent = spreadsheet.SpreadsheetCellByRowColumn(sheet_name, row, column)
		    if spreadsheet.IsSpreadsheetCell(ent):
		        cel = ent
		        print("This is a struct of type spreadsheet_cell")
		        print(
		            cel.row, cel.col, cel.cell_label, cel.spreadsheet, cel.text, cel.orig_text
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfAllSheets() -> object:

	"""

	This function get names of all existing sheets of the Spreadsheet Editor.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of an existing sheet of the Spreadsheet Editor.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    all_sheets = spreadsheet.NamesOfAllSheets()
		    for sheet_name in all_sheets:
		        print(sheet_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SpreadsheetCellByRowColumn(sheet_name: str, row: int, column: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.spreadsheet.Sheet.get_cell` instead.


	This function finds a spreadsheet cell at a given row and column for a given sheet.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	row : int
		Number of the row.

	column : int
		Number of the column.

	Returns
	-------
	object
		Upon success, it returns an object of class SpreadsheetCell referring to the cell of the sheet at the given row and column. 
		Else, a non valid SpreadsheetCell object is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    row = 1
		    column = 1
		
		    cel = spreadsheet.SpreadsheetCellByRowColumn(sheet_name, row, column)
		    if cel:
		        print(
		            cel.row, cel.col, cel.cell_label, cel.spreadsheet, cel.text, cel.orig_text
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.spreadsheet.Sheet.get_cell instead.", DeprecationWarning)

def SpreadsheetCellsByArea(sheet_name: str, top_row: int, left_column: int, bottom_row: int, right_column: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.spreadsheet.Sheet.get_range` instead.


	This function finds spreadsheet cells at a given area of a specific sheet. Area is described through top and bottom rows and left and right columns.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	top_row : int
		Number of the top row.

	left_column : int
		Number of the left column.

	bottom_row : int
		Number of the bottom row.

	right_column : int
		Number of the right column.

	Returns
	-------
	object
		It returns a 2-dimensional list with the SpreadsheetCell objects of the corresponding cells at the given area of the specific sheet.
		Upon failure, an empty list is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    top_row = 1
		    left_column = 1
		    bottom_row = 5
		    right_column = 5
		
		    cells = spreadsheet.SpreadsheetCellsByArea(
		        sheet_name, top_row, left_column, bottom_row, right_column
		    )
		    for row in cells:
		        for cel in row:
		            print(
		                cel.row,
		                cel.col,
		                cel.cell_label,
		                cel.spreadsheet,
		                cel.text,
		                cel.orig_text,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.spreadsheet.Sheet.get_range instead.", DeprecationWarning)

def SpreadsheetCellsByColumn(sheet_name: str, column: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.spreadsheet.Sheet.get_column` instead.


	This function finds spreadsheet cells at a given column of a specific sheet.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	column : int
		Number of the column.

	Returns
	-------
	object
		It returns a list with the SpreadsheetCell objects of the corresponding cells at the given column of the specific sheet.
		Upon failure, an empty list is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    column = 1
		    cells = spreadsheet.SpreadsheetCellsByColumn(sheet_name, column)
		    for cel in cells:
		        print(
		            cel.row, cel.col, cel.cell_label, cel.spreadsheet, cel.text, cel.orig_text
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.spreadsheet.Sheet.get_column instead.", DeprecationWarning)

def SpreadsheetCellsByLabel(sheet_name: str, label: str) -> object:

	"""

	This function finds spreadsheet cells from a given label of a specific sheet.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	label : str
		Label of the cells.

	Returns
	-------
	object
		It returns a 2-dimensional list where each member is an object of class SpreadsheetCell referring to one specific SpreadsheetCell at the given label of the given sheet. 
		Upon failure, an empty list is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    label = "A1:B3"
		
		    cells = spreadsheet.SpreadsheetCellsByLabel(sheet_name, label)
		    for row in cells:
		        for cel in row:
		            print(
		                cel.row,
		                cel.col,
		                cel.cell_label,
		                cel.spreadsheet,
		                cel.text,
		                cel.orig_text,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def SpreadsheetCellsByRow(sheet_name: str, row: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.spreadsheet.Sheet.get_row` instead.


	This function finds spreadsheet cells at a given row of a specific sheet.

	Parameters
	----------
	sheet_name : str
		Name of the sheet.

	row : int
		Number of the row.

	Returns
	-------
	object
		It returns a list with the SpreadsheetCell objects of the corresponding cells at the given row of the specific sheet.
		Upon failure, an empty list is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    row = 1
		    cells = spreadsheet.SpreadsheetCellsByRow(sheet_name, row)
		    for cel in cells:
		        print(
		            cel.row, cel.col, cel.cell_label, cel.spreadsheet, cel.text, cel.orig_text
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.spreadsheet.Sheet.get_row instead.", DeprecationWarning)

def SpreadsheetCellsListToDict(spreadsheet_cells: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class SpreadsheetCell.

	Parameters
	----------
	spreadsheet_cells : object
		List with objects of class SpreadsheetCell.

	Returns
	-------
	object
		It returns a dictionary whose key is the cell label and data is the corresponding SpreadsheetCell object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    column = 1
		    all_spreadsheet_cells = spreadsheet.SpreadsheetCellsByColumn(sheet_name, column)
		
		    dict_spreadsheet_cells = spreadsheet.SpreadsheetCellsListToDict(
		        all_spreadsheet_cells
		    )
		    for cell_label, cel in dict_spreadsheet_cells.items():
		        print(
		            cel.row, cel.col, cel.cell_label, cel.spreadsheet, cel.text, cel.orig_text
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateSpreadsheetCell(spreadsheet_cell: object) -> object:

	"""

	This function updates the data of the given spreadsheet_cell struct. Update is based in the fields "row", "col" and "spreadsheet" of the given spreadsheet_cell struct.

	Parameters
	----------
	spreadsheet_cell : object
		Object of class SpreadsheetCell.

	Returns
	-------
	object
		Upon success, it returns the new updated SpreadsheetCell object.
		Else, a non valid SpreadsheetCell object is returned.

	See Also
	--------
	spreadsheet.SpreadsheetCell

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    row = 1
		    column = 1
		    cel = spreadsheet.SpreadsheetCellByRowColumn(sheet_name, row, column)
		    if cel:
		        # commands which alter the data of the spreadsheet object
		        # .....
		        cel = spreadsheet.UpdateSpreadsheetCell(cel)
		        if cel:  # Update OK
		            print(
		                cel.row,
		                cel.col,
		                cel.cell_label,
		                cel.spreadsheet,
		                cel.text,
		                cel.orig_text,
		            )
		        else:  # Update FAILED
		            print("This is not a valid SpreadsheetCell object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectedAreaOfSpreadsheet(sheet_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.spreadsheet.Sheet.get_selection` instead.


	This function finds the selected area for a given sheet.

	Parameters
	----------
	sheet_name : str
		Name of the sheet. If given sheet is an empty string, the selections of the active sheet are found.

	Returns
	-------
	object
		It returns a triple list which containts the selected areas for the given sheet.
		Element at position [i][0][0] of matrix refers to top row of i-th selection.
		Element at position [i][0][1] of matrix refers to left column of i-th selection.
		Element at position [i][1][0] of matrix refers to bottom row of i-th selection.
		Element at position [i][1][1] of matrix refers to right column of i-th selection.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    sheet_name = "Sheet1"
		    selected_area = spreadsheet.SelectedAreaOfSpreadsheet(sheet_name)
		    for i in range(0, len(selected_area)):
		        print("Selection ", i + 1)  # Selection
		        print(
		            "From cell:", selected_area[i][0][0], selected_area[i][0][1]
		        )  # Top-left cell
		        print(
		            "To cell:", selected_area[i][1][0], selected_area[i][1][1]
		        )  # Bottom-right cell
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.spreadsheet.Sheet.get_selection instead.", DeprecationWarning)

def CreateSpreadsheet(name: str) -> object:

	"""

	Creates a spreadsheet window with the provided name, or a unique generated name if one is not provided. Returns None if a name is provided and a spreadsheet with that name already exists.

	Parameters
	----------
	name : str, optional
		Name of the new spreadsheet window.

	Returns
	-------
	object
		Upon success returns an object of type meta.spreadsheet.Spreadsheet
		Upon failure returns None.

	See Also
	--------
	spreadsheet.Spreadsheet

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    # Create new spreadsheet with autogenerated name
		    s = spreadsheet.CreateSpreadsheet()
		    print(s)
		    # Or
		    # Create new spreadsheet with user-provided name
		    name = "Spreadsheet 1"
		    s2 = spreadsheet.CreateSpreadsheet(name)
		    print(s2)
		
		    all_s = spreadsheet.Spreadsheets()
		    print(all_s)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteSpreadsheet(spreadsheet: object) -> bool:

	"""

	Deletes the specified spreadsheet window. The window is specified either by its name or the meta.spreadsheet.Spreadsheet object.

	Parameters
	----------
	spreadsheet : object
		Either a spreadsheet name as a string or a meta.spreadsheet.Spreadsheet object.

	Returns
	-------
	bool
		Upon success returns True
		Upon failure returns False.

	See Also
	--------
	spreadsheet.Spreadsheet, spreadsheet.CreateSpreadsheet

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    s = spreadsheet.CreateSpreadsheet()
		    print(s)
		
		    # Delete spreadsheet
		    ret = spreadsheet.DeleteSpreadsheet(s)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

class SpreadsheetCell:

	"""

	A cell on a spreadsheet sheet in META.

	See Also
	--------
	spreadsheet.Spreadsheet, spreadsheet.Sheet, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    cell = sheet.get_cell([2, 3])
		    # New cell using constructor
		    cell2 = spreadsheet.SpreadsheetCell(spr.name, sheet.name, [2, 3])
		    print(cell2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    text = "text"
		    ret = cell.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    ret = cell.set_text_style(
		        font_family="Monospace",
		        font_size=24,
		        bold=True,
		        underline=True,
		        horizontal_align="center",
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    height = 50
		    cell.set_row_height(height)
		    unit_value = "pt"
		    # unit_value  = 'emu'
		    # unit_value  = 'cm'
		    # unit_value  = 'mm'
		    # unit_value  = 'inch'
		    # unit_value  = 'pc'
		    # unit_value  = 'pixel'
		    # ret =  cell.set_row_height(height, unit = unit_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    width = 100
		    # unit_value ='pt'
		    # unit_value ='emu'
		    # unit_value ='cm'
		    # unit_value ='mm'
		    # unit_value ='inch'
		    # unit_value ='pc'
		    # unit_value ='pixel'
		    # ret = cell.set_column_width(width, unit = unit_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    text = "text"
		    ret = cell.set_text(text)
		    print(ret)
		    text = cell.get_text()
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = [3, 2]
		    cell = sheet.get_cell(position)
		    cell.set_text_style(
		        font_family="Monospace",
		        font_size=24,
		        bold=True,
		        underline=True,
		        horizontal_align="center",
		    )
		    style = cell.get_text_style()
		    print(style)
		    position = [3, 3]
		    cell2 = sheet.get_cell(position)
		    ret = cell2.set_text_style(str(style))
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	row: int = None
	"""
	Row number of the spreadsheet cell. Index starts at 1.

	"""

	col: int = None
	"""
	Column number of the spreadsheet cell. Index starts at 1. Same as 'column', kept for backwards compatibility.

	"""

	cell_label: str = None
	"""
	Label of the spreadsheet cell (e.g. A1).

	"""

	spreadsheet: str = None
	"""
	Name of the sheet. Same as 'sheet_name', kept for backwards compatibility.

	"""

	text: str = None
	"""
	Displayed text of the spreadsheet cell.

	"""

	orig_text: str = None
	"""
	Original (not parsed) text of the spreadsheet cell.

	"""

	sheet_name: str = None
	"""
	Sheet name.

	"""

	spreadsheet_name: str = None
	"""
	Spreadsheet name.

	"""

	column: int = None
	"""
	Column number of the spreadsheet cell. Index starts at 1.

	"""

	def set_text(self, text: str) -> bool:

		"""

		Set the text of the cell. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, cell_color: object, horizontal_align: str, vertical_align: str, wrap: bool) -> bool:

		"""

		Set text style options. All arguments are optional. Any number of them can be used.


		Parameters
		----------
		font_family : str, optional
			See corresponding setting in GUI for the available fonts.

		font_size : int, optional
			See corresponding setting in GUI for size values.

		bold : bool, optional

		italic : bool, optional

		underline : bool, optional

		strike_through : bool, optional

		superscript : bool, optional

		subscript : bool, optional

		text_color : object, optional
			meta.windows.Color

		cell_color : object, optional
			meta.windows.Color

		horizontal_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		vertical_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def set_row_height(self, height: float, unit: str) -> bool:

		"""

		Set the row height. Takes an optional unit argument.


		Parameters
		----------
		height : float
			Row height.

		unit : str, optional
			Unit of the given height.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def set_column_width(self, width: float, unit: str) -> bool:

		"""

		Set the column width. Takes an optional unit argument.


		Parameters
		----------
		width : float
			Column width.

		unit : str, optional
			Unit of the given width.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the cell, html formatted.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def get_text_style(self, position: int) -> object:

		"""

		Returns the text style in the form of a python dictionary. The dictionary contains the same keys and can be applied directly to the set_text_style function. An optional position argument can be used to return the style of a specific character in the text.


		Parameters
		----------
		position : int, optional
			Index of the character in the text whose style is returned. Indexing starts at 1. If undefined the style of the last character is returned.

		Returns
		-------
		object
			Python dictionary with the following text style options.              font_family       string              font_size         integer              bold              boolean              italic            boolean              underline         boolean              strike_through    boolean              superscript       boolean              subscript         boolean              text_color        meta.windows.Color              cell_color        meta.windows.Color              horizontal_align  string                                      'left'                                      'center'                                      'right'                                      'justify'              vertical_align    string                                      'top'                                      'middle'                                      'bottom'              wrap              boolean

		"""

class Spreadsheet:

	"""

	A spreadsheet editor in META.

	See Also
	--------
	spreadsheet.Sheet

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    # Second handler for the same spreadsheet using constructor
		    name = spr.name
		    spr2 = spreadsheet.Spreadsheet(name)
		    print(spr2.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: open
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    filepath = "spreadsheet1.xlsx"
		    ret = spr.open(filepath)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: save
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    filepath = "spreadsheet1.xlsx"
		    ret = spr.save(filepath)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    name = "Sheet1"
		    sheet = spr.get_sheet(name)
		    print(sheet, sheet.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_active_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    print(sheet.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    new_sheet = spr.add_sheet(name="New Sheet")
		    # new_sheet = spr.add_sheet(name="New Sheet", index = 2)
		    print(new_sheet, new_sheet.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    new_sheet = spr.add_sheet(name="New Sheet")
		    # new_sheet = spr.add_sheet(name="New Sheet", index = 2)
		    ret = spr.delete_sheet(new_sheet)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_sheets
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    new_sheet = spr.add_sheet(name="New Sheet")
		    new_sheet2 = spr.add_sheet(name="New Sheet 2")
		    sheets = spr.get_sheets()
		    for sheet in sheets:
		        print(sheet, sheet.name)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Spreadsheet window name.

	"""

	def open(self, filename: str) -> bool:

		"""

		Opens an xlsx file.


		Parameters
		----------
		filename : str
			Path to an xlsx file.

		Returns
		-------
		bool

		"""


	def save(self, filename: str, variables_as_values: bool) -> bool:

		"""

		Save spreadsheet to an xlsx file.


		Parameters
		----------
		filename : str
			Path to xlsx file.

		variables_as_values : bool, optional
			Whether to export variables as values. Default is True.

		Returns
		-------
		bool

		"""


	def get_sheet(self, name: str) -> object:

		"""

		Returns the sheet with the given name.


		Parameters
		----------
		name : str
			Sheet name.

		Returns
		-------
		object
			meta.spreadsheet.Sheet

		"""


	def get_active_sheet(self) -> object:

		"""

		Returns the active sheet.


		Returns
		-------
		object
			meta.spreadsheet.Sheet

		"""


	def add_sheet(self, name: str, index: int) -> object:

		"""

		Adds a sheet to the spreadsheet, optionally providing a name and an index.


		Parameters
		----------
		name : str, optional

		index : int, optional

		Returns
		-------
		object
			meta.spreadsheet.Sheet

		"""


	def delete_sheet(self, sheet: object) -> bool:

		"""

		Deletes the specified sheet.


		Parameters
		----------
		sheet : object
			Either the name of the sheet to be deleted or the meta.spreadsheet.Sheet object.

		Returns
		-------
		bool

		"""


	def get_sheets(self) -> object:

		"""

		Returns a list of the sheets in this spreadsheet.


		Returns
		-------
		object
			List of meta.spreadsheet.Sheet objects

		"""

class Sheet:

	"""

	A sheet in a spreadsheet in META.

	See Also
	--------
	spreadsheet.Spreadsheet, spreadsheet.SpreadsheetRange, spreadsheet.SpreadsheetCell, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    # Second handler for the same sheet using constructor
		    sheet2 = spreadsheet.Sheet(editor_name=spr.name, name=sheet.name)
		    print(sheet2.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_selection
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = sheet.set_selection(range)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_selection
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [6, 6]
		    bottom_right = [7, 7]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = sheet.add_selection(range)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: clear_selection
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    ret = sheet.clear_selection()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_selection
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    selection = sheet.get_selection()
		    for sel in selection:
		        print(sel)
		        print(sel.sheet_name)
		        print(sel.spreadsheet_name)
		        print(sel.min_row)
		        print(sel.min_column)
		        print(sel.max_row)
		        print(sel.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_active_selection
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    sel = sheet.get_active_selection()
		    if sel:
		        print(sel)
		        print(sel.sheet_name)
		        print(sel.spreadsheet_name)
		        print(sel.min_row)
		        print(sel.min_column)
		        print(sel.max_row)
		        print(sel.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_range
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    if range:
		        print(range)
		        print(range.sheet_name)
		        print(range.spreadsheet_name)
		        print(range.min_row)
		        print(range.min_column)
		        print(range.max_row)
		        print(range.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_row
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    row = 2
		    range = sheet.get_row(row)
		    if range:
		        print(range)
		        print(range.sheet_name)
		        print(range.spreadsheet_name)
		        print(range.min_row)
		        print(range.min_column)
		        print(range.max_row)
		        print(range.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_column
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    column = 2
		    range = sheet.get_column(column)
		    if range:
		        print(range)
		        print(range.sheet_name)
		        print(range.spreadsheet_name)
		        print(range.min_row)
		        print(range.min_column)
		        print(range.max_row)
		        print(range.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_cell
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    position = (
		        2,
		        3,
		    )
		    cell = sheet.get_cell(position)
		    if cell:
		        print(cell)
		        print(cell.row)
		        print(cell.col)
		        print(cell.cell_label)
		        print(cell.spreadsheet)
		        print(cell.text)
		        print(cell.orig_text)
		        print(cell.sheet_name)
		        print(cell.spreadsheet_name)
		        print(cell.column)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import spreadsheet
		from meta import windows
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [
		        1,
		        1,
		    ]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = sheet.set_selection(range)
		    print(ret)
		    ret = sheet.set_text_style(
		        font_family="Monospace",
		        font_size=24,
		        bold=True,
		        underline=True,
		        horizontal_align="center",
		    )
		    # ret =sheet.set_text_style(italic=True, superscript=True, strike_through=True, subscript=True, horizontal_align="center")
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret =sheet.set_text_style(cell_color =color, horizontal_align = 'left', vertical_align ='top', line_spacing = 1.0, wrap =True)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [
		        1,
		        1,
		    ]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = sheet.set_selection(range)
		    print(ret)
		    height = 50
		    ret = sheet.set_row_height(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [
		        1,
		        1,
		    ]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = sheet.set_selection(range)
		    print(ret)
		    width = 100
		    ret = sheet.set_column_width(width)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    name = "new sheet name"
		    ret = sheet.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		
		    # Add sheet with default name at default position
		    sheet = spr.add_sheet()
		
		    # Add sheet with user-specified name
		    sheet = spr.add_sheet(name="new sheet 1")
		
		    # Add sheet with user-specified name and position index
		    sheet = spr.add_sheet(name="new sheet 2", index=1)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_sheet
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.add_sheet(name="new_sheet_1")
		    print(spr.get_sheets())
		
		    # Delete sheet
		    ret = spr.delete_sheet(sheet)
		    print(ret)
		
		    sheets = spr.get_sheets()
		    for sheet in sheets:
		        print(sheet)
		        print(sheet.name)
		        print(sheet.spreadsheet_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_sheets
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.add_sheet()
		    sheet = spr.add_sheet(name="new sheet 1")
		    sheet = spr.add_sheet(name="new sheet 2", index=1)
		
		    # Print all spreadsheet sheets
		    sheets = spr.get_sheets()
		    print(sheets)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_row_group_level
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    row = 2
		    level = sheet.get_row_group_level(row)
		    print(level)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_column_group_level
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    column = 2
		    level = sheet.get_column_group_level(column)
		    print(level)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_group_level
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    row = 2
		    level = 7
		    sheet.set_row_group_level(row, level)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_group_level
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    column = 2
		    level = 7
		    sheet.set_column_group_level(column, level)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_frozen
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    rows = 2
		    columns = 7
		    sheet.set_frozen(rows, columns)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_number_of_frozen_rows
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    rows = 2
		    columns = 7
		    sheet.set_frozen(rows, columns)
		    print(sheet.get_number_of_frozen_rows())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_number_of_frozen_columns
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    rows = 2
		    columns = 7
		    sheet.set_frozen(rows, columns)
		    print(sheet.get_number_of_frozen_columns())
		
		
		if __name__ == "__main__":
		    main()
		# method: has_frozen_panes
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    rows = 2
		    columns = 7
		    sheet.set_frozen(rows, columns)
		    print(sheet.has_frozen_panes())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_summary_row_below
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    print(sheet.get_summary_row_below())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_summary_column_right
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    print(sheet.get_summary_column_right())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_summary_row_below
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    sheet.set_summary_row_below(False)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_summary_column_right
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    sheet.set_summary_column_right(False)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Sheet name.

	"""

	spreadsheet_name: str = None
	"""
	Spreadsheet name.

	"""

	def set_selection(self, range: object) -> bool:

		"""

		Sets the cell selection to the given range.


		Parameters
		----------
		range : object
			meta.spreadsheet.SpreadsheetRange

		Returns
		-------
		bool

		"""


	def add_selection(self, range: object) -> bool:

		"""

		Adds the given range  to the list of selections.


		Parameters
		----------
		range : object
			meta.spreadsheet.SpreadsheetRange

		Returns
		-------
		bool

		"""


	def clear_selection(self) -> bool:

		"""

		Clears all selected ranges.


		Returns
		-------
		bool

		"""


	def get_active_selection(self) -> object:

		"""

		Returns the last selected range, otherwise it returns None.


		Returns
		-------
		object
			meta.spreadsheet.SpreadsheetRange

		"""


	def get_selection(self) -> object:

		"""

		Returns a list of all selected ranges.


		Returns
		-------
		object
			A list of spreadsheet.SpreadsheetRange objects.

		"""


	def get_range(self, top_left: object, bottom_right: object) -> object:

		"""

		Creates a SpreadhseetRange object for the given range.


		Parameters
		----------
		top_left : object
			A list or 2-tuple with the coordinates of the top left cell of the desired range.

		bottom_right : object
			A list or 2-tuple with the coordinates of the bottom right cell of the desired range.

		Returns
		-------
		object
			meta.spreadsheet.SpreadsheetRange

		"""


	def get_row(self, row: int) -> object:

		"""

		Returns a spreadsheet.SpreadsheetRange object that represents the given row.


		Parameters
		----------
		row : int
			Row number. Index starts at 1.

		Returns
		-------
		object
			meta.spreadsheet.SpreadsheetRange

		"""


	def get_column(self, column: int) -> object:

		"""

		Returns a spreadsheet.SpreadsheetRange object that represents the given column.


		Parameters
		----------
		column : int
			Column number. Index starts at 1.

		Returns
		-------
		object
			meta.spreadsheet.SpreadsheetRange

		"""


	def get_cell(self, position: object) -> object:

		"""

		Returns a spreadsheet.SpreadsheetCell object that represents the cell at the given coordinates.


		Parameters
		----------
		position : object
			A 2-tuple with the coordinates of the desired cell. Indexing starts at 1.

		Returns
		-------
		object
			meta.spreadsheet.SpreadsheetCell

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, cell_color: object, horizontal_align: str, vertical_align: str, line_spacing: float, wrap: bool) -> bool:

		"""

		Set text style options. All arguments are optional. Any number of them can be used. The style is applied to selected cells only.


		Parameters
		----------
		font_family : str, optional
			See corresponding setting in GUI for the available fonts.

		font_size : int, optional
			See corresponding setting in GUI for size values.

		bold : bool, optional

		italic : bool, optional

		underline : bool, optional

		strike_through : bool, optional

		superscript : bool, optional

		subscript : bool, optional

		text_color : object, optional
			meta.windows.Color

		cell_color : object, optional
			meta.windows.Color

		horizontal_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		vertical_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'

		line_spacing : float, optional
			See corresponding setting in GUI for spacing values.

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def set_row_height(self, height: float, unit: str) -> bool:

		"""

		Set the row height. Takes an optional unit argument. The height is applied to the selected cells.


		Parameters
		----------
		height : float
			Row height.

		unit : str, optional
			Unit of the given height.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def set_column_width(self, width: float, unit: str) -> bool:

		"""

		Set the column width. Takes an optional unit argument. The width is applied to the selected cells.


		Parameters
		----------
		width : float
			Column width.

		unit : str, optional
			Unit of the given width.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Sets the name of the Sheet.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_row_group_level(self, row: int) -> int:

		"""

		Returns the group level of the given row.


		Parameters
		----------
		row : int
			Row index starting at 1.

		Returns
		-------
		int

		"""


	def get_column_group_level(self, column: int) -> int:

		"""

		Returns the group level of the given column.


		Parameters
		----------
		column : int
			Column index starting at 1.

		Returns
		-------
		int

		"""


	def set_row_group_level(self, row: int, level: int) -> bool:

		"""

		Sets the group level for the given row.


		Parameters
		----------
		row : int
			Row index starting at 1.

		level : int
			A value between 0 and 7 representing the desired group level.

		Returns
		-------
		bool

		"""


	def set_column_group_level(self, column: int, level: int) -> bool:

		"""

		Sets the group level for the given column.


		Parameters
		----------
		column : int
			Column index starting at 1.

		level : int
			A value between 0 and 7 representing the desired group level.

		Returns
		-------
		bool

		"""


	def set_frozen(self, rows: int, columns: int) -> bool:

		"""

		Freezes the top rows and left columns specified.


		Parameters
		----------
		rows : int
			Number of rows to be frozen.

		columns : int
			Number of columns to be frozen.

		Returns
		-------
		bool

		"""


	def get_number_of_frozen_rows(self) -> int:

		"""

		Returns the number of frozen rows.


		Returns
		-------
		int

		"""


	def get_number_of_frozen_columns(self) -> int:

		"""

		Returns the number of frozen columns.


		Returns
		-------
		int

		"""


	def has_frozen_panes(self) -> bool:

		"""

		Returns whether the sheet has frozen panes or not.


		Returns
		-------
		bool

		"""


	def get_summary_row_below(self) -> bool:

		"""

		Returns the value of the corresponding GUI checkbox.


		Returns
		-------
		bool

		"""


	def get_summary_column_right(self) -> bool:

		"""

		Returns the value of the corresponding GUI checkbox.


		Returns
		-------
		bool

		"""


	def set_summary_row_below(self, value: bool) -> bool:

		"""

		Controls the corresponding GUI checkbox. The default value is True.


		Parameters
		----------
		value : bool

		Returns
		-------
		bool

		"""


	def set_summary_column_right(self, value: bool) -> bool:

		"""

		Controls the corresponding GUI checkbox. The default value is True.


		Parameters
		----------
		value : bool

		Returns
		-------
		bool

		"""

class SpreadsheetRange:

	"""

	A range of cells on a spreadsheet sheet in META. The range is a contiguous rectangle of cells. It is represented by the minimum row and column of the cells (top left corner), and the maximum row and column (bottom right corner).

	See Also
	--------
	spreadsheet.Spreadsheet, spreadsheet.Sheet, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    # New range using constructor
		    range2 = spreadsheet.SpreadsheetRange(spr.name, sheet.name, [1, 1], [5, 5])
		    print(range2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    text = "text"
		    ret = range.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import spreadsheet
		from meta import windows
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = range.set_text_style(
		        font_family="Monospace",
		        font_size=24,
		        bold=True,
		        underline=True,
		        horizontal_align="center",
		    )
		    # ret = range.set_text_style(italic=True, font_size=24, strike_through=True, superscript=True, subscript=True, )
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = range.set_text_style(text_color = color, cell_color = color, horizontal_align = 'left', vertical_align = 'top', wrap = True)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    height = 50
		    ret = range.set_row_height(height)
		    # u = 'emu'
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # ret = range.set_row_height(height, unit = u)
		
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    width = 100
		    ret = range.set_column_width(width)
		    # u = 'emu'
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # unit = u
		    # ret = range.set_column_width(width, unit = u)
		
		
		if __name__ == "__main__":
		    main()
		# method: merge
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = range.merge()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: split
		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    spr = spreadsheet.CreateSpreadsheet()
		    sheet = spr.get_active_sheet()
		    top_left = [1, 1]
		    bottom_right = [5, 5]
		    range = sheet.get_range(top_left, bottom_right)
		    ret = range.split()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	sheet_name: str = None
	"""
	Sheet name.

	"""

	spreadsheet_name: str = None
	"""
	Spreadsheet name.

	"""

	min_row: int = None

	min_column: int = None

	max_row: int = None

	max_column: int = None

	def set_text(self, text: str) -> bool:

		"""

		Set the text of every cell in the range. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, cell_color: object, horizontal_align: str, vertical_align: str, line_spacing: float, wrap: bool) -> bool:

		"""

		Set text style options. All arguments are optional. Any number of them can be used.


		Parameters
		----------
		font_family : str, optional
			See corresponding setting in GUI for the available fonts.

		font_size : int, optional
			See corresponding setting in GUI for size values.

		bold : bool, optional

		italic : bool, optional

		underline : bool, optional

		strike_through : bool, optional

		superscript : bool, optional

		subscript : bool, optional

		text_color : object, optional
			meta.windows.Color

		cell_color : object, optional
			meta.windows.Color

		horizontal_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		vertical_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'

		line_spacing : float, optional
			See corresponding setting in GUI for spacing values.

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def set_row_height(self, height: float, unit: str) -> bool:

		"""

		Set the row height. Takes an optional unit argument.


		Parameters
		----------
		height : float
			Row height.

		unit : str, optional
			Unit of the given height.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def set_column_width(self, width: float, unit: str) -> bool:

		"""

		Set the column width. Takes an optional unit argument.


		Parameters
		----------
		width : float
			Column width.

		unit : str, optional
			Unit of the given width.
			Available values are listed below. The default value is 'pt'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def merge(self) -> bool:

		"""

		Merge the cells that belong to this range.


		Returns
		-------
		bool

		"""


	def split(self) -> bool:

		"""

		Split the cells that belong to this range if they have been merged.


		Returns
		-------
		bool

		"""

