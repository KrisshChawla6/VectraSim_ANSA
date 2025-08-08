from __future__ import annotations
from typing import *

def HeightOfSlide(unit: float) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.report.Report.get_slide_size` instead.


	This function returns the height of the report slide.

	Parameters
	----------
	unit : float
		Refers to the unit of measurement of the height. Its possible values are:
		- 'mm' : Millimeters
		- 'pixel' : Pixels.

	Returns
	-------
	float
		This function returns as float the height of the report slide in the given unit of measurement.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    h_mm = report.HeightOfSlide("mm")  # The height of the report slide in millimeter
		    h_px = report.HeightOfSlide("pixel")  # The height of the report slide in pixels
		    print("The height of the slide is " + str(h_mm) + " mm or " + str(h_px) + "px.")
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.report.Report.get_slide_size instead.", DeprecationWarning)

def NamesOfAllSlides() -> object:

	"""

	This function get names of all existing slides of the report.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of an existing slide of the report.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    all_slides = report.NamesOfAllSlides()
		    for slide_name in all_slides:
		        print(slide_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TextOfReportTextbox(slide_name: str, textbox_name: str, text_type: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.report.Textbox.get_text` instead.


	This function gets the text of a textbox of a given toolbar.

	Parameters
	----------
	slide_name : str
		Name of the slide

	textbox_name : str
		Name of the textbox

	text_type : int
		If value of argument "text_type" is 0 then the text after the quantification of any variables is returned, else the original text is returned.

	Returns
	-------
	str
		Upon success, it returns a string referring to the text of the textbox of the given slide.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    slide_name = "Slide 1"
		    textbox_name = "Textbox 1"
		    text_type = 1
		
		    text = report.TextOfReportTextbox(slide_name, textbox_name, text_type)
		    print(text)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.report.Textbox.get_text instead.", DeprecationWarning)

def WidthOfSlide(unit: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.report.Report.get_slide_size` instead.


	This function returns the width of the report slide.

	Parameters
	----------
	unit : str
		Refers to the unit of measurement of the width. Its possible values are:
		- "mm" : Millimeters
		- "pixel" : Pixels.

	Returns
	-------
	float
		This function returns as float the width of the report slide in the given unit of measurement.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    w_mm = report.WidthOfSlide("mm")  # The width of the report slide in millimeter
		    w_px = report.WidthOfSlide("pixel")  # The width of the report slide in pixels
		    print("The width of the slide is " + str(w_mm) + " mm or " + str(w_px) + "px.")
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.report.Report.get_slide_size instead.", DeprecationWarning)

def RectOfSlideElement(slide: str, element: str, unit: str) -> float:

	"""

	This function returns the rectangle of a shape in a slide.

	Parameters
	----------
	slide : str
		The name of the slide.

	element : str
		The name of the element.

	unit : str
		The units of measurement. The possible values are:
		-'mm': Millimeters
		-'norm': Normalized values 
		-'pixel': Pixels.
		If unit does not match one of the valid values, then the function will return the rectangle in pixels.

	Returns
	-------
	float
		This function returns the rectangle of the shape in the given unit of measurement.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    # Normalized values
		    slide = "Slide 1"
		    element = "Image 1"
		    unit = "norm"
		    rect = report.RectOfSlideElement(slide, element, unit)
		    print('Rect of "Image 1" in normalized values')
		    print("===================")
		    print("X: ", rect[0])
		    print("Y: ", rect[1])
		    print("Width: ", rect[2])
		    print("Height: ", rect[3])
		
		    # Values in millimeters
		    unit = "mm"
		    rect = report.RectOfSlideElement(slide, element, unit)
		    print('\\nRect of "Image 1" in millimeters')
		    print("===================")
		    print("X: ", rect[0])
		    print("Y: ", rect[1])
		    print("Width: ", rect[2])
		    print("Height: ", rect[3])
		
		    # if unit is not set to one of the above values, then the size in pixels will be returned
		    # unit can also be explicitly set to 'pixel'
		    unit = "pixel"
		    rect = report.RectOfSlideElement(slide, element, unit)
		    print('\\nRect of "Image 1" in pixels')
		    print("===================")
		    print("X: ", rect[0])
		    print("Y: ", rect[1])
		    print("Width: ", rect[2])
		    print("Height: ", rect[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

def WidthOfSpreadsheetColumns(slide_name: str, table_name: str, sheet_name: str, columns: object, unit: str) -> object:

	"""

	This function returns the width of the specified columns for a given Excel table in the specified unit.

	Parameters
	----------
	slide_name : str
		Name of the slide.

	table_name : str
		Name of the table.

	sheet_name : str
		Name of the sheet.

	columns : object
		A list with the numbers of the columns of interest (Numbering starts from 0).

	unit : str
		The unit of interest:
		-pt
		-mm
		-pixel

	Returns
	-------
	object
		The function returns a list that contains columns' width.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    slide_name = "Slide 1"
		    table_name = "Table 1"
		    sheet_name = "Sheet1"
		    columns = [0, 1, 3]
		    unit = "pt"
		
		    columns_width = report.WidthOfSpreadsheetColumns(
		        slide_name, table_name, sheet_name, columns, unit
		    )
		    print(columns_width)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfAllShapes(slide_name: str) -> object:

	"""

	This function returns a map containing the names of the shapes in the given slide, grouped by shape type.

	Parameters
	----------
	slide_name : str
		Name of the slide

	Returns
	-------
	object
		It returns a map which contains, the shape types as keys, and lists of shape names as values.
		Upon failure, an empty map is returned.

	See Also
	--------
	NamesOfAllSlides

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    slide_name = "Slide 1"
		
		    all_shapes = report.NamesOfAllShapes(slide_name)
		    for shape_type in all_shapes:
		        print(shape_type[0])
		        for shape in shape_type[1]:
		            print(shape)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateReport(name: str) -> object:

	"""

	Creates a report composer window with the provided name, or a unique generated name if one is not provided. Returns None if a name is provided and a report with that name already exists.

	Parameters
	----------
	name : str, optional
		Name of the new report composer window.

	Returns
	-------
	object
		Upon success returns an object of type meta.report.Report
		Upon failure returns None.

	See Also
	--------
	report.Report, report.Reports

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    # Create new report
		    r = report.CreateReport()
		    print(r)
		    # Or
		    name = "Report 1"
		    r = report.CreateReport(name)
		    print(r)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetReportNames() -> object:

	"""

	Returns the names of all report composer windows.

	Returns
	-------
	object
		Returns a list of strings with the names of all report composer windows.

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import report
		
		
		def main():
		    # Create new report
		    r = report.CreateReport()
		    print(r)
		    # Or
		    name = "Report 1"
		    r = report.CreateReport(name)
		    print(r)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Reports() -> object:

	"""

	Returns all report composer windows.

	Returns
	-------
	object
		Returns a list of meta.report.Report objects that correspond to all report composer windows.

	See Also
	--------
	report.CreateReport, report.Report

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import report
		
		
		def main():
		    # Create new report
		    r = report.CreateReport()
		    print(r)
		    # Or
		    name = "Report 1"
		    r = report.CreateReport(name)
		    print(r)
		
		    all_r = report.Reports()
		    print(all_r)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteReport(report: object) -> bool:

	"""

	Deletes the given report from META. This action invalidates the object.

	Parameters
	----------
	report : object
		Either a report name as a string or a meta.report.Report object.

	Returns
	-------
	bool
		Upon success returns True
		Upon failure returns False.

	See Also
	--------
	report.Report, report.CreateReport, report.Reports

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    # Create new report
		    r = report.CreateReport()
		    # Delete report
		    ret = report.DeleteReport(r)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Spreadsheets() -> object:

	"""

	Returns all spreadsheet windows.

	Returns
	-------
	object
		Returns a list of meta.spreadsheet.Spreadsheet objects that correspond to all spreadsheet windows.

	See Also
	--------
	spreadsheet.CreateSpreadsheet, spreadsheet.Spreadsheet

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import spreadsheet
		
		
		def main():
		    # Create new spreadsheet
		    s = spreadsheet.CreateSpreadsheet()
		    print(s)
		    # OR
		    name = "Spreadsheet 2"
		    s2 = spreadsheet.CreateSpreadsheet(name)
		    print(s2)
		    # Get all spreadsheets
		    all_s = spreadsheet.Spreadsheets()
		    print(all_s)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateReportTag(name: str, value: str) -> object:

	"""

	Creates a report tag.

	Parameters
	----------
	name : str

	value : str

	Returns
	-------
	object
		meta.report.ReportTag

	See Also
	--------
	report.ReportTag

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    print(tag)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateReportFilter(type: str, name: str, operator: str, value: str, value2: str) -> object:

	"""

	Creates a report filter.

	Parameters
	----------
	type : str
		Available values are listed below. Note that the 'tag' type also requires the rest of the arguments to be specified, a name, operator, and at least one value (depending on the operator).
		 'presentation'
		 'slide'
		 'element'
		 'tag'

	name : str, optional
		The tag name to search for.

	operator : str, optional
		Available values are listed below, note that some operators require a value2 argument as well.
		 'equal'
		 'less'
		 'greater'
		 'less_equal'
		 'greater_equal'
		 'not_equal'
		 'between'
		 'not_between'
		 'contains'
		 'not_contains'
		 'starts_with'
		 'not_starts_with'
		 'ends_with'
		 'not_ends_with'
		 'reg_expression'
		 'not_reg_expression'

	value : str, optional
		The tag value that is matched against the value of the tags in the report files using the specified operator.

	value2 : str, optional
		A second optional value required by operators  'between' and 'not_between'.

	Returns
	-------
	object
		meta.report.ReportFilter

	See Also
	--------
	report.ReportFilter

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    directory = "../"
		    type = "presentation"
		    presFilter = report.CreateReportFilter("presentation")
		    # OR
		    type = "tag"
		    name = "tag1"
		    operator = "equal"
		    value = "value1"
		    tagFilter = report.CreateReportFilter(type, name, operator, value)
		
		    presFilter.add_child(tagFilter)
		    print(presFilter)
		    print(presFilter.get_children())
		    print(presFilter.search(directory))
		
		
		if __name__ == "__main__":
		    main()


	"""

class Report:

	"""

	A report composer window in META. It can be used to create and edit reports.
	
	Reports can be loaded from and exported to pptx files.

	See Also
	--------
	report.CreateReport, report.DeleteReport, report.Reports, report.Slide

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    # Second handler for the same report using constructor
		    rep2 = report.Report(name=rep.name)
		    print(rep2.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: open
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    filepath = "pres1.pptx"
		    rep.open(filepath)
		
		
		if __name__ == "__main__":
		    main()
		# method: save
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    filepath = "pres1.pptx"
		    rep.save(filepath)
		
		
		if __name__ == "__main__":
		    main()
		# method: reset
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    ret = rep.reset()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = "Slide 1"
		    slide = rep.get_slide(slide)
		    if slide:
		        print(slide)
		        print(slide.name, slide.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slides
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.add_slide()
		    slide = rep.add_slide()
		    slides = rep.get_slides()
		    for s in slides:
		        print(s)
		        print(s.name, s.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.add_slide()
		    slide_name = slide.name
		    print(slide_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: move_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.add_slide()
		    index = 2
		    ret = rep.move_slide(slide, index)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: duplicate_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.add_slide()
		    dup_slide = rep.duplicate_slide(slide)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.add_slide()
		    ret = rep.delete_slide(slide)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_slide_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    size = (200, 100)
		    ret = rep.set_slide_size(size)
		    # ret = rep.set_slide_size(size, unit = 'mm')
		    # ret = rep.set_slide_size(size, unit = 'mm', type = 'ao')
		    # ret = rep.set_slide_size(size, unit = 'mm', type = 'ao', orientation = 'portrait')
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide_size = rep.get_slide_size()
		    if slide_size:
		        print("Width: " + str(slide_size[0]))
		        print("Height: " + str(slide_size[1]))
		
		
		if __name__ == "__main__":
		    main()
		# method: add_page
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    ret = rep.add_page(id=0)
		    # ret = rep.add_page(name = 'Page Name')
		    # ret = rep.add_page(title = 'Slide title')
		    # ret = rep.add_page(add_title = True)
		    # ret = rep.add_page(vectorized_image = True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    rep.add_tag(tag)
		    rep.add_tag(tag2)
		    tags = rep.get_tags()
		    for t in tags:
		        print(t)
		        print(t.name, t.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = rep.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    rep.add_tag(tag)
		    rep.add_tag(tag2)
		    ret = rep.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Report composer window name.

	"""

	def open(self, filename: str, load_shape_names: bool, load_slide_names: bool) -> bool:

		"""

		Loads a report from the specified pptx file.


		Parameters
		----------
		filename : str
			Path to pptx file.

		load_shape_names : bool, optional
			Whether to load the shape names from the pptx file or not. Default value is True.

		load_slide_names : bool, optional
			Whether to load the slide, layout, and master names from the pptx file or not. Default value is True.

		Returns
		-------
		bool

		"""


	def save(self, filename: str, options: object) -> bool:

		"""

		Export the report to a pptx file.


		Parameters
		----------
		filename : str
			Path to pptx file.

		options : object, optional
			Dictionary with string keys. Each key corresponds to an option. The available keys are listed below along with the type of value that is expected.
			'redraw_excel_tables' : boolean
			'excel_snapshots' : boolean
			'vbscript_redraw' : boolean
			'shrink_autofit' : boolean
			'excel_2003_compatibility' : boolean
			'excel_xls_compatibility' : boolean
			'output_unparsed_text' : boolean
			'compress_images_ppi' : integer (supported values: 220, 150, 96)

		Returns
		-------
		bool

		"""


	def reset(self) -> bool:

		"""

		Clears the report composer leaving only one empty slide.


		Returns
		-------
		bool

		"""


	def get_slide(self, slide: object) -> object:

		"""

		Returns the slide specified either by its name or its id.


		Parameters
		----------
		slide : object
			Either the name of the slide as a string or the position of the slide as an integer. Slide numbering starts from 1.

		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_slides(self) -> object:

		"""

		Returns a list of the slides in this report.


		Returns
		-------
		object
			List of meta.report.Slide objects.

		"""


	def add_slide(self, name: str, index: int) -> object:

		"""

		Adds a new slide to the report. Optional name and index for the new slide can be provided. The new slide is returned.


		Parameters
		----------
		name : str, optional
			Slide name.

		index : int, optional
			Slide index. Slide numbering starts at 1. If not specified the new slide will be added at the end of the report.

		Returns
		-------
		object
			meta.report.Slide

		"""


	def move_slide(self, slide: object, index: int) -> bool:

		"""

		Move the given slide to the specified index.


		Parameters
		----------
		slide : object
			meta.report.Slide

		index : int
			New slide index. Numbering starts at 1.

		Returns
		-------
		bool

		"""


	def duplicate_slide(self, slide: object, name: str, index: int) -> object:

		"""

		Create a copy of the given slide. Optional name and index for the new slide can be provided. The new slide is returned.


		Parameters
		----------
		slide : object
			meta.report.Slide to be duplicated.

		name : str, optional
			New slide name

		index : int, optional
			Index of the new slide.

		Returns
		-------
		object
			meta.report.Slide

		"""


	def delete_slide(self, slide: object) -> bool:

		"""

		Deletes the specified slide.


		Parameters
		----------
		slide : object
			Either the name of the slide as a string or the meta.report.Slide object.

		Returns
		-------
		bool

		"""


	def set_slide_size(self, size: object, unit: str, type: str, orientation: str) -> bool:

		"""

		Sets the slide width and height either using the 'size' argument or by selecting one of the predefined sizes with the combination of 'type' and 'orientation' arguments. If 'size' is used an optional unit can be provided.


		Parameters
		----------
		size : object, optional
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'mm'.
			'emu'
			'cm'
			'mm'
			'inch'
			'pt'
			'pc'
			'pixel'

		type : str, optional
			When using this option an orientation must also be provided. Available values are:
			'a0'  :  841 x 1189 mm
			'a1'  :  594 x 841 mm
			'a2'  :  420 x 594 mm
			'a3'  :  297 x 420 mm
			'a4'  :  210 x 297 mm, 8.26 x 11.69 inches
			'a5'  :  148 x 210 mm
			'a6'  :  105 x 148 mm
			'a7'  :  74 x 105 mm
			'a8'  :  52 x 74 mm
			'a9'  :  37 x 52 mm
			'b0'  :  1000 x 1414 mm
			'b1'  :  707 x 1000 mm
			'b2'  :  500 x 707 mm
			'b3'  :  353 x 500 mm
			'b4'  :  250 x 353 mm
			'b5'  :  176 x 250 mm, 6.93 x 9.84 inches
			'b6'  :  125 x 176 mm
			'b7'  :  88 x 125 mm
			'b8'  :  62 x 88 mm
			'b9'  :  33 x 62 mm
			'b10'  :  31 x 44 mm
			'c5e'  :  163 x 229 mm
			'comm10e'  :  105 x 241 mm, u.s. common 10 envelope
			'dle'  :  110 x 220 mm
			'executive'  :  190.5 x 254 mm, 7.5 x 10 inches,
			'folio'  :  210 x 330 mm
			'ledger'  :  431.8 x 279.4 mm
			'legal'  :  215.9 x 355.6 mm, 8.5 x 14 inches,
			'letter'  :  215.9 x 279.4 mm, 8.5 x 11 inches,
			'tabloid'  :  279.4 x 431.8 mm
			'film35mm'  :  36 x 24 mm
			'screen16_9'  :  254 x 143.002 mm, 10 x 5.63 in
			'screen16_10'  :  254 x 158.75 mm, 10 x 6.25 in
			'screen4_3'  :	 254 x 190.5 mm, 10 x 7.5 in

		orientation : str, optional
			Either 'portrait' or 'landscape'.

		Returns
		-------
		bool

		"""


	def get_slide_size(self, unit: str) -> object:

		"""

		Returns the width and height of a slide.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'mm'.
			'emu'
			'cm'
			'mm'
			'inch'
			'pt'
			'pc'
			'pixel'

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def add_page(self, name: str, id: int, title: str, add_title: bool, vectorized_image: bool) -> bool:

		"""

		Creates a slide with the image of each window in the specified META page. The page is specified either by its name or its id.


		Parameters
		----------
		name : str, optional
			Page name.

		id : int, optional
			Page id.

		title : str, optional
			Slide title text.

		add_title : bool, optional
			Whether to add a title to the new slides or not. The default value is False.

		vectorized_image : bool, optional
			Whether to drop the window image as a vectorized image. The default value is False. This option is valid only for 2D Plot windows.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the report tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the report.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the report.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""

class Slide:

	"""

	A slide in a report in META.

	See Also
	--------
	report.Report, report.Textbox, report.ShapeGroup, report.ExcelTable, report.Picture, report.Line, report.Rectangle, report.Ellipse, report.Triangle, report.Table, report.Model3D, report.VideoShape, report.Audio, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    # Second handler for the same slide using constructor
		    slide2 = report.Slide(report_name=rep.name, slide_name=slide.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    name = "slide name"
		    ret = slide.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    r = slide.get_report()
		    print(r, r.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shape
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    textbox = slide.add_textbox()
		    print(line)
		    print(line.name, line.slide_name, line.report_name)
		
		    # Second handler for line
		    name = line.name
		    line2 = slide.get_shape(name)
		    print(line2)
		    print(line2.name, line2.slide_name, line2.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shapes
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ret = slide.add_line()
		    print(ret)
		    ret = slide.add_textbox()
		    print(ret)
		    shapes = slide.get_shapes()
		    for s in shapes:
		        print(s)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_group
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    textbox = slide.add_textbox()
		    group = slide.add_group([line, textbox])
		    print(group)
		    print(group.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_excel_table
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    # filename = './example.xlsx'
		    # name = 'MyShape'
		    # table = slide.add_excel_table(filename, name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_textbox
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    textbox = slide.add_textbox()
		    position = (0.3, 0.3)
		    textbox.set_position(position)
		    text = "some text"
		    textbox.set_text(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_shapes
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    textbox = slide.add_textbox()
		    ret = slide.delete_shapes([line])
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_picture
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    path = "example/path/to/image.png"
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    picture = slide.add_picture(path)
		    print(picture)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_table
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 5
		    table = slide.add_table(rows, columns)
		    print(table)
		    print(table.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_line
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = (0.2, 0.5)
		    line.set_p1_position(position)
		    position = (0.7, 0.5)
		    unit = "norm"
		    unit = "emu"
		    unit = "cm"
		    unit = "mm"
		    unit = "inch"
		    unit = "pt"
		    unit = "pc"
		    unit = "pixel"
		    unit = "norm"
		    line.set_p2_position(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_rectangle
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    size = (0.4, 0.3)
		    ret = rectangle.set_size(size)
		    print(ret)
		    position = (0.3, 0.3)
		    ret = rectangle.set_position(position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_ellipse
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    size = (0.4, 0.3)
		    ret = ellipse.set_size(size)
		    print(ret)
		    position = (0.3, 0.3)
		    ret = ellipse.set_position(position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_triangle
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    size = (0.3, 0.3)
		    triangle.set_size(size)
		    position = (0.3, 0.3)
		    triangle.set_position(position)
		    # unit = 'norm'
		    # unit = 'emu'
		    # unit = 'cm'
		    # unit = 'mm'
		    # unit = 'inch'
		    # unit = 'pt'
		    # unit = 'pc'
		    # unit = 'pixel'
		    # triangle.set_position(position, unit)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    visibility = slide.set_visibility(False)
		    print(visibility)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ret = slide.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_layout
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    master = "Default Slide Master"
		    layout = "Layout 1"
		    ret = slide.set_layout(master, layout)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_layout_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    layout_name = slide.get_layout_name()
		    print(layout_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_master_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    master_name = slide.get_master_name()
		    print(master_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_background
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "no_fill"
		    slide.set_background(fill, color=c)
		    # fill="solid_fill"
		    # color=c
		    # slide.set_background(fill="solid_fill", color=c)
		    # fill="picture_fill"
		    # filename = './image.png'
		    # slide.set_background(fill, filename)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = slide.add_tag(tag)
		    print(ret)
		    ret = slide.get_tags()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    slide.add_tag(tag)
		    slide.add_tag(tag2)
		    slide.remove_tag(tag)
		    tag = slide.get_tags()
		    print(tag, tag.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    slide.add_tag(tag)
		    slide.add_tag(tag2)
		    tags = slide.get_tags()
		    for tag in tags:
		        print(tag, tag.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_freeform
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    points = [(0.4, 0.4), (0.2, 0.6), (0.5, 0.6)]
		    freeform.set_points(points)
		    # unit ='emu'
		    # unit = 'cm'
		    # unit = 'mm'
		    # unit = 'inch'
		    # unit = 'pt'
		    # unit = 'pc'
		    # unit = 'pixel'
		    # unit = 'norm'
		    # freeform.set_points(points, unit)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_3dmodel
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    path = "example/path/to/model.glb"
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_3dmodel(path)
		    print(model)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_video
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    path = "example/path/to/video"
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_video(path)
		    print(shape)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_audio
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    path = "example/path/to/audio"
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_audio(path)
		    print(shape)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this slide belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def add_textbox(self, text: str, name: str) -> object:

		"""

		Create a new textbox in this slide. The new textbox is returned.


		Parameters
		----------
		text : str
			The text to be displayed in the textbox. It may be plain text or HTML formatted.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Textbox

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility of the slide.


		Parameters
		----------
		visibility : bool

		Returns
		-------
		bool

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility of the slide.


		Returns
		-------
		bool
			Visibility of the slide.

		"""


	def get_shapes(self) -> object:

		"""

		Returns a list of the shapes (textboxes, tables, images, lines, etc) in this slide.


		Returns
		-------
		object
			List of meta.report.Rectangle, meta.report.Triangle, meta.report.Line, meta.report.ShapeGroup, meta.report.Textbox, meta.report.Table etc. objects.

		"""


	def add_picture(self, filename: str, name: str) -> object:

		"""

		Creates a new picture in this slide. The new picture is returned.


		Parameters
		----------
		filename : str
			Path to an image file.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Picture

		"""


	def add_table(self, rows: int, columns: int, name: str) -> object:

		"""

		Creates a new table in this slide. The new table is returned.


		Parameters
		----------
		rows : int
			Number of rows.

		columns : int
			Number of columns.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Table

		"""


	def set_layout(self, master: str, layout: str) -> bool:

		"""

		Sets the layout for this slide.


		Parameters
		----------
		master : str
			Master name.

		layout : str
			Layout name.

		Returns
		-------
		bool

		"""


	def get_layout_name(self) -> str:

		"""

		Returns layout name of this slide.


		Returns
		-------
		str
			Layout name.

		"""


	def get_master_name(self) -> str:

		"""

		Returns the master name of this slide.


		Returns
		-------
		str
			Master layout name.

		"""


	def add_group(self, shapes: object, name: str) -> object:

		"""

		Create a new group with the given shapes. The new group is returned.


		Parameters
		----------
		shapes : object
			A list of shape objects such as meta.report.Rectangle, meta.report.Textbox, meta.report.Table etc.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.ShapeGroup

		"""


	def add_excel_table(self, filename: str, name: str) -> object:

		"""

		Creates a new excel table in the slide. The new table is returned.


		Parameters
		----------
		filename : str, optional
			Path to an .xlsx file.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.ExcelTable

		"""


	def delete_shapes(self, shapes: object) -> bool:

		"""

		Deletes the specified shapes from the slide.


		Parameters
		----------
		shapes : object
			Either the name of a shape as a string, a list of shape names, a shape object, or a list of shape objects.

		Returns
		-------
		bool

		"""


	def get_shape(self, name: str) -> object:

		"""

		Returns the shape with the specified name.


		Parameters
		----------
		name : str
			Shape name.

		Returns
		-------
		object
			Shape object such as meta.report.Textbox, meta.report.Table etc.

		"""


	def add_rectangle(self, name: str) -> object:

		"""

		Creates a new rectangle in the slide. The new recctangle is returned.


		Parameters
		----------
		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Rectangle

		"""


	def add_ellipse(self, name: str) -> object:

		"""

		Create a new ellipse in the slide. The new ellipse is returned.


		Parameters
		----------
		name : str, optional
			Shape name

		Returns
		-------
		object
			meta.report.Ellipse

		"""


	def add_triangle(self, name: str) -> object:

		"""

		Create a new triangle in the slide. The new triangle is returned.


		Parameters
		----------
		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Triangle

		"""


	def set_background(self, fill: str, color: object, filename: str) -> bool:

		"""

		Sets the slide background. Either to a solid color or an image according to the specifed arguments.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fil'
			'picture_fill'

		color : object, optional
			meta.windows.Color. Used when the fill option is 'solid_fill'.

		filename : str, optional
			Path to an image file. Used when the fill option is 'picture_fill'.

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Sets the slide name.


		Parameters
		----------
		name : str
			Slide name.

		Returns
		-------
		bool

		"""


	def add_line(self, name: str) -> object:

		"""

		Create a new line in the slide. The new line is returned.


		Parameters
		----------
		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Line

		"""


	def get_tags(self) -> object:

		"""

		Returns the slide tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the slide.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the slide.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def add_freeform(self, points: object, unit: str, name: str) -> object:

		"""

		Creates a new freeform shape in the slide. The new shape is returned.


		Parameters
		----------
		points : object
			A non-empty list of pairs of x, y coordinates.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Freeform

		"""


	def add_3dmodel(self, filename: str, name: str) -> object:

		"""

		Creates a new 3D model shape in this slide. The new shape is returned.


		Parameters
		----------
		filename : str
			Path to a .glb model file.

		name : str, optional
			Shape name.

		Returns
		-------
		object
			meta.report.Model3D

		"""


	def add_video(self, filename: str, name: str, embed: bool) -> object:

		"""

		Creates a new video shape in this slide. The new shape is returned.


		Parameters
		----------
		filename : str
			Path to a video file.

		name : str, optional
			Shape name.

		embed : bool, optional
			Whether the file will be embedded or linked on export. The default value is True.

		Returns
		-------
		object
			meta.report.VideoShape

		"""


	def add_audio(self, filename: str, name: str, embed: bool) -> object:

		"""

		Creates a new audio shape in this slide. The new shape is returned.


		Parameters
		----------
		filename : str
			Path to an audio file.

		name : str, optional
			Shape name.

		embed : bool, optional
			Whether the file will be embedded or linked on export. The default value is True.

		Returns
		-------
		object
			meta.report.Audio

		"""

class Textbox:

	"""

	A textbox in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    textbox = slide.add_textbox()
		    # Second handler for the same textbox using constructor
		    textbox2 = report.Textbox(rep.name, slide.name, textbox.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    textbox = slide.add_textbox()
		    name = "textbox name"
		    ret = textbox.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    rep = shape.get_report()
		    print(rep, rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    sld = shape.get_slide()
		    print(sld, sld.name, sld.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    pos = shape.get_position()
		    # unit = 'emu'
		    # unit = 'cm'
		    # unit = 'mm'
		    # unit = 'inch'
		    # unit = 'pt'
		    # unit = 'pc'
		    # unit = 'pixel'
		    # unit = 'norm'
		    # pos = shape.get_position(unit )
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    position = (0.5, 0.5)
		    ret = shape.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    textbox = slide.add_textbox()
		    text = "some_text"
		    textbox.set_text(text)
		    size = textbox.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    size = (0.25, 0.25)
		    ret = shape.set_size(size)  # A quarter of the size of the slide
		    # unit = 'emu'
		    # unit = 'cm'
		    # unit = 'mm'
		    # unit = 'inch'
		    # unit = 'pt'
		    # unit = 'pc'
		    # unit = 'pixel'
		    # unit = 'norm'
		    # ret = shape.set_size(size, unit)   # A quarter of the size of the slide
		    return ret
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    angle = 90
		    ret = shape.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    rotation = shape.get_rotation()
		    print(rotation)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = "Textbox 1"
		    shape.set_text(text)
		    c = Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = shape.set_line_style(fill="solid_line", color=c)
		    # ret =shape.set_line_style(fill="solid_line", color=c, width = 10.1, dash = 'solid_line')
		    # ret =shape.set_line_style(fill="solid_line", color=c, width = 10.1, dash = 'solid_line', custom_dash_pattern = '111000')
		    # ret =shape.set_line_style(cap = 'flat_cap', join = 'bevel_join' )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = "Textbox 1"
		    shape.set_text(text)
		    fill = "no_fill"
		    # fill="solid_fill"
		    # fill="picture_fill"
		    ret = shape.set_fill(fill)
		    # c = Color(name = "color1", r = 255, g = 0, b = 0, a = 50)
		    # ret = shape.set_fill(fill, color=c)
		    ret = shape.set_fill(fill, filename="/home/image.png")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = "some text"
		    ret = shape.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = shape.get_text()
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = shape.set_text_style(italic=True, strike_through=True, superscript = True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = shape.set_text_style(text_color = color, text_align = 'left', line_spacing = 'top')
		    # ret = shape.set_text_style(autofit = 'shrink_text_on_overflow', wrap = True)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.set_margins(left=10, top=10)
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pixel'
		    # ret = shape.set_margins(right=10, bottom=10, unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag.value, tag.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = shape.set_text_style(italic=True, strike_through=True, superscript = True, subscript = True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = shape.set_text_style(text_color = color, text_align = 'left', line_spacing = 1.2, shape_align = 'middle', autofir = 'no_autofit', wrap =True)
		    print(ret)
		    style = shape.get_text_style()
		    print(style)
		    shape2 = slide.add_textbox()
		    shape2.set_text_style(**style)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = "some_text"
		    shape.set_text(text)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    text = "some_text"
		    shape.set_text(text)
		    ret = shape.set_visibility(False)
		    print(ret)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_textbox()
		    ret = shape.set_margins(left=10, top=10)
		    # ret = shape.set_margins(right=10, bottom=10)
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pixel'
		    # ret = shape.set_margins(unit = u)
		    margins = shape.get_margins()
		    # margins = shape.get_margins(unit = u)
		    print(margins)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the textbox. The text is html formatted.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts plain and html formatted text.


		Parameters
		----------
		text : str
			The text to be displayed in the textbox. It may be plain text or HTML formatted.

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the textbox.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the textbox.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape as a list.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the textbox width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str, optional
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def set_margins(self, left: float, right: float, top: float, bottom: float, unit: str) -> bool:

		"""

		Sets the margin between the text and the edges of the textbox.


		Parameters
		----------
		left : float, optional
			Left margin.

		right : float, optional
			Right margin.

		top : float, optional
			Top margin.

		bottom : float, optional
			Bottom margin.

		unit : str, optional
			Unit of the given margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.font_family     stringfont_size       integerbold            booleanitalic          booleanunderline       booleanstrike_through  booleansuperscript     booleansubscript       booleantext_color      meta.windows.Colortext_align      string                        'left'                        'center'                        'right'                        'justify'shape_align     string                        'top'                        'middle'                        'bottom'                        'top_center'                        'middle_center'                        'bottom_center'autofit         string                        'no_autofit'                        'shrink_text_on_overflow'                        'resize_shape_to_fit_text'wrap            boolean

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""


	def get_margins(self, unit: str) -> object:

		"""

		Returns the margin between the text and the edges of the textbox.


		Parameters
		----------
		unit : str, optional
			Unit of the returned margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		object
			Array of floats with the respective margin [left, right, top, bottom]

		"""

class Line:

	"""

	A line in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    # Second handler for the same textbox using constructor
		    line2 = report.Line(
		        report_name=rep.name, slide_name=slide.name, shape_name=line.name
		    )
		    print(line2)
		    print(line2.name, line2.slide_name, line2.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    name = "line name"
		    ret = line.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    rep = line.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    slide = line.get_slide()
		    print(slide)
		    print(slide.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = line.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = (0.5, 0.5)
		    ret = line.set_position(position)  # Middle of the slide
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # ret = line.set_position(position, unit = u)   # Middle of the slide
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    size = line.get_size()
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # size = line.get_size(unit = u)
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    size = (0.25, 0.25)
		    ret = line.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    angle = 90
		    ret = line.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    rot = line.get_rotation()
		    print(rot)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    c = windows.Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = line.set_line_style(fill="solid_line", color=c, width=1.0, dash="solid_line")
		    # ret = line.set_line_style(custom_dash_pattern = '111000', cap = 'round_cap', join = 'bevel_join')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_p1_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = line.get_p1_position()
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # position = line.get_p1_position(unit = u)
		    print(posistion)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_p2_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = line.get_p2_position()
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # position = line.get_p2_position(unit = u)
		    print(posistion)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_p1_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = (0.25, 0.25)
		    ret = line.set_p1_position(position)
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # ret = line.set_p1_position(unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_p2_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    position = (0.25, 0.25)
		    ret = line.set_p2_position(position)
		    # u =  'emu'
		    # u =  'cm'
		    # u = 'mm'
		    # u =  'inch'
		    # u =  'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u =  'norm'
		    # ret = line.set_p2_position(unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_p1_arrow_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.set_p1_arrow_style(type="stealth", width="large", length="large")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_p2_arrow_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    ret = line.set_p2_arrow_style(type="stealth", width="large", length="large")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: connect_p1
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    rect = slide.add_rectangle()
		    shape = rect
		    ret = line.connect_p1(shape, position="top")
		    ret = line.connect_p1(shape, position="top", connector=1)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: connect_p2
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    line = slide.add_line()
		    rect = slide.add_rectangle()
		    shape = rect
		    ret = line.connect_p2(rect, position="top")
		    ret = line.connect_p2(rect, position="top", connector=1)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_line()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    tags = shape.get_tags()
		    for t in tags:
		        print(t)
		        print(t.name, t.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_line()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    tag2 = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.add_tag(tag2)
		    print(ret)
		    ret = shape.remove_tag(tag)
		    print(ret)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		        print(tag.name)
		        print(tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_line()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.add_tag(tag2)
		    print(ret)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		        print(tag.name)
		        print(tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_line()
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_line()
		    shape.set_visibility(False)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x an y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of the shape in degrees.


		Returns
		-------
		float

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of the shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def get_p1_position(self, unit: str) -> object:

		"""

		Return the coordinates of the first point of the line.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def get_p2_position(self, unit: str) -> object:

		"""

		Return the coordinates of the second point of the line.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_p1_position(self, position: object, unit: str) -> bool:

		"""

		Sets the position of the first point of the line.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_p2_position(self, position: object, unit: str) -> bool:

		"""

		Sets the position of the second point of the line.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_p1_arrow_style(self, type: str, width: str, length: str) -> bool:

		"""

		Provides arrow styling options.


		Parameters
		----------
		type : str, optional
			The following values are supported:
			'no_arrow'
			'line_arrow'
			'diamond'
			'oval'
			'stealth'
			'triangle'

		width : str, optional
			The following values are supported:
			'small'
			'medium'
			'large'

		length : str, optional
			The following values are supported:
			'small'
			'medium'
			'large'

		Returns
		-------
		bool

		"""


	def set_p2_arrow_style(self, type: str, width: str, length: str) -> bool:

		"""

		Provides arrow styling options.


		Parameters
		----------
		type : str, optional
			The following values are supported:
			'no_arrow'
			'line_arrow'
			'diamond'
			'oval'
			'stealth'
			'triangle'

		width : str, optional
			The following values are supported:
			'small'
			'medium'
			'large'

		length : str, optional
			The following values are supported:
			'small'
			'medium'
			'large'

		Returns
		-------
		bool

		"""


	def connect_p1(self, shape: object, position: str, connector: int) -> bool:

		"""

		Connects the first point of the line to the given shape. The specific connection can either be selected using the "position" argument or the "connector" argument.


		Parameters
		----------
		shape : object
			The shape on which to connect the line. One of the shape types provided in the report module.

		position : str, optional
			The following values are accepted. Only a subset of the available options is supported for each shape type.
			'top'
			'right'
			'bottom'
			'left'
			'top_left'
			'top_right'
			'bottom_right'
			'bottom_left'

		connector : int, optional
			Index of connection.

		Returns
		-------
		bool

		"""


	def connect_p2(self, shape: object, position: str, connector: int) -> bool:

		"""

		Connects the second point of the line to the given shape. The specific connection can either be selected using the "position" argument or the "connector" argument.


		Parameters
		----------
		shape : object
			The shape on which to connect the line. One of the shape types provided in the report module.

		position : str, optional
			The following values are accepted. Only a subset of the available options is supported for each shape type.
			'top'
			'right'
			'bottom'
			'left'
			'top_left'
			'top_right'
			'bottom_right'
			'bottom_left'

		connector : int, optional
			Index of connection.

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Picture:

	"""

	A picture in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    # picture = slide.add_picture(filename, name = 'Image 1')
		    # Second handler for the same picture using constructor
		    picture2 = report.Picture(
		        report_name=rep.name, slide_name=slide.name, name=picture.name
		    )
		    print(picture2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    name = "picture name"
		    ret = picture.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    rep = picture.get_report()
		    if rep:
		        print(rep)
		        print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    slide = picture.get_slide()
		    print(slide)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    position = picture.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    position = (0.5, 0.5)
		    ret = picture.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    size = picture.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    size = (0.25, 0.25)
		    ret = picture.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    ret = picture.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    ret = picture.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    ret = picture.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    ret = picture.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    angle = 90
		    ret = picture.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    rotation = picture.get_rotation()
		    print(rotation)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    c = windows.Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = picture.set_line_style(
		        fill="solid_line",
		        color=c,
		        width=1.0,
		        dash="solid_line",
		        custom_dash_pattern="111000",
		        cap="flat_cap",
		        join="bevel_join",
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    c = windows.Color(name="color1", r=255, g=0, b=0, a=50)
		    ret = picture.set_fill(fill="solid_fill", color=c, filename="image1.png")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_image
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    filename = "image2.png"
		    ret = picture.set_image("image2.png")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_transparent_background
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    picture = slide.add_picture("image1.png")
		    c = Color(name="color1", r=255, g=255, b=255, a=255)  # white
		    transparent = True
		    ret = picture.set_transparent_background(transparent, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_original_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    picture = slide.add_picture(filename)
		    ret = picture.get_original_size()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    shape = slide.add_picture(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = '"image1.png"'
		    shape = slide.add_picture(filename)
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    shape = slide.add_picture(filename)
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		        print(tag.name)
		        print(tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    shape = slide.add_picture(filename)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "image1.png"
		    shape = slide.add_picture(filename)
		    visibility = False
		    ret = shape.set_visibility(visibility)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x an y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str, optional
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def set_image(self, filename: str) -> bool:

		"""

		Set the displayed image.


		Parameters
		----------
		filename : str
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_transparent_background(self, transparent: bool, color: object) -> bool:

		"""

		Toggle the transparent background option and select which color to make transparent.


		Parameters
		----------
		transparent : bool

		color : object, optional
			meta.windows.Color

		Returns
		-------
		bool

		"""


	def get_original_size(self, unit: str) -> object:

		"""

		Returns the original width and height of the image in this shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Table:

	"""

	A table in a report in META.

	See Also
	--------
	report.Report, report.Slide, report.TableRange, report.TableCell, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    # Second handler for the same textbox using constructor
		    table2 = report.Table(
		        report_name=rep.name, slide_name=slide.name, shape_name=table.name
		    )
		    print(table2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    name = "table name"
		    ret = table.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    rep = table.get_report()
		    if rep:
		        print(rep)
		        print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    slide = table.get_slide()
		    if slide:
		        print(slide)
		        print(slide.name)
		        print(slide.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = table.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = (0.5, 0.5)
		    ret = table.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    size = table.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    size = (0.25, 0.25)
		    ret = table.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    ret = table.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    ret = table.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    ret = table.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    ret = table.send_backward()
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_table(3, 2)
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "solid_fill"
		    ret = table.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    text = "text"
		    ret = table.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    color = windows.Color(r=255, g=255, b=0, a=255)
		    ret = table.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = table.set_text_style(italic=True, underline= True, strike_through=True, superscript=True, subscript = True)
		    # ret = table.set_text_style(text_color = color, text_align = 'left', line_spacing = 1.2, shape_align = 'top', autofit = 'no_autofit', wrap = True)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_cell
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = (1, 2)
		    cell = table.get_cell(position)
		    print(cell.shape_name)
		    print(cell.slide_name)
		    print(cell.report_name)
		    print(cell.row)
		    print(cell.column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_range
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_row
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    row = 2
		    range = table.get_row(row)
		    if range:
		        print(range)
		        print(range.shape_name)
		        print(range.slide_name)
		        print(range.report_name)
		        print(range.min_row)
		        print(range.min_column)
		        print(range.max_row)
		        print(range.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_column
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    column = 2
		    range = table.get_column(column)
		    if range:
		        print(range)
		        print(range.shape_name)
		        print(range.slide_name)
		        print(range.report_name)
		        print(range.min_row)
		        print(range.min_column)
		        print(range.max_row)
		        print(range.max_column)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    height = 0.3
		    ret = table.set_row_height(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    width = 0.2
		    ret = table.set_column_width(width)
		    # u = 'emu'
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u = 'norm'
		    # ret = table.set_column_width(width, unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_table_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    rows = 4
		    columns = 4
		    ret = table.set_table_size(rows, columns)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_table(3, 2)
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_table(3, 2)
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    shape.add_tag(tag)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_table(3, 2)
		    tag = report.CreateReportTag("tag_name", "tag_value")
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		        print(tag.name)
		        print(tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_table_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    rows = 4
		    columns = 3
		    ret = table.set_table_size(rows, columns)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    ret = table.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    visibility = False
		    ret = table.set_visibility(visibility)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    text = "text"
		    ret = table.set_text(text)
		    print(ret)
		
		    ret = table.set_margins(left=2, top=2)
		    u = "cm"
		    u = "mm"
		    u = "inch"
		    u = "pt"
		    u = "pixel"
		    ret = table.set_margins(right=2, bottom=2, unit=u)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text of every cell in the table. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		Returns
		-------
		bool

		"""


	def get_cell(self, position: object) -> object:

		"""

		Return a specific cell of this table.


		Parameters
		----------
		position : object
			A list or 2-tuple with the row and column of the desired cell. Index starts at 1.

		Returns
		-------
		object
			meta.report.TableCell

		"""


	def get_range(self, top_left: object, bottom_right: object) -> object:

		"""

		Return a specific range on this table. The range is a rectangle of cells and is specified by the row and column of the top left and bottom right corners.


		Parameters
		----------
		top_left : object
			A list or 2-tuple with the row and column of the top left corner of the desired range. Index starts at 1.

		bottom_right : object
			A list or 2-tuple with the row and column of the bottom right corner of the desired range. Index starts at 1.

		Returns
		-------
		object
			meta.report.TableRange

		"""


	def get_row(self, row: int) -> object:

		"""

		Returns a range that represents the desired row on this table.


		Parameters
		----------
		row : int
			The desired row. Index starts at 1.

		Returns
		-------
		object
			meta.report.TableRange

		"""


	def get_column(self, column: int) -> object:

		"""

		Returns a range that represents the desired column on this table.


		Parameters
		----------
		column : int
			The desired column. Index starts at 1.

		Returns
		-------
		object
			meta.report.TableRange

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
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

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
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_table_size(self, rows: int, columns: int) -> bool:

		"""

		Set the number of rows and columns of the table.


		Parameters
		----------
		rows : int
			Number of rows.

		columns : int
			Number of columns.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_table_size(self) -> object:

		"""

		Returns the number of rows and columns in the table as a list.


		Returns
		-------
		object
			A list where the first element is the number of rows and the second the number of columns.

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""


	def set_margins(self, left: float, right: float, top: float, bottom: float, unit: str) -> bool:

		"""

		Sets the margin between the text and the edges of each cell, for all the cells in the table.


		Parameters
		----------
		left : float, optional
			Left margin.

		right : float, optional
			Right margin.

		top : float, optional
			Top margin.

		bottom : float, optional
			Bottom margin.

		unit : str, optional
			Unit of the given margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		bool

		"""

class ExcelTable:

	"""

	An excel table in a report in META.

	See Also
	--------
	report.Report, report.Slide, spreadsheet.Spreadsheet

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    print(table.name)
		    print(table.slide_name)
		    print(table.report_name)
		    # Second handler for the same shape using constructor
		    table2 = report.ExcelTable(
		        report_name=rep.name, slide_name=slide.name, shape_name=table.name
		    )
		    print(table2)
		    print(table2.name)
		    print(table2.slide_name)
		    print(table2.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = table.add_tag(tag)
		    print(ret)
		    tags = table.get_tags()
		    for t in tags:
		        print(t.name, t.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    pos = table.get_position()
		    # pos = table.get_position(unit = 'pixel')
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    r = table.get_report()
		    print(r)
		    print(r.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    size = table.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		
		    slide = table.get_slide()
		    print(slide)
		    print(slide.name)
		    print(slide.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_spreadsheet
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    s = table.get_spreadsheet()
		    print(s)
		    print(s.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    table.add_tag(tag)
		    table.add_tag(tag2)
		    tags = table.get_tags()
		    for t in tags:
		        print(t.name, t.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    table.add_tag(tag)
		    ret = table.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.set_name("table name")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		
		    pos = (0.5, 0.5)
		    ret = table.set_position(pos)  # Middle of the slide
		    # u# = 'emu'
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pc'
		    # u = 'pixel'
		    # u = 'norm'
		    # ret = table.set_position(pos, unit = 'mm')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    size = (0.25, 0.25)
		    ret = table.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		    size = (200, 400)
		    ret = table.set_size(size, unit="pixel")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    ret = table.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_excel_table()
		    table.set_visibility(False)
		    ret = table.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_spreadsheet(self) -> object:

		"""

		Returns the spreadsheet behind this shape.


		Returns
		-------
		object
			meta.spreadsheet.Spreadsheet

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class ShapeGroup:

	"""

	A shape group in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    # Second handler for the same group using constructor
		    group2 = report.ShapeGroup(rep.name, slide.name, group.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    name = "group name"
		    ret = group.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    rep = group.get_report()
		    if rep:
		        print(rep)
		        print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    slide = group.get_slide()
		    print(slide)
		    print(slide.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    position = group.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    position = (0.5, 0.5)
		    ret = group.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    size = group.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    size = (0.25, 0.25)
		    ret = group.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    angle = 90
		    ret = group.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    position = group.get_rotation()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    c = Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = group.set_line_style(fill="solid_line", color=c)
		    ret = group.set_line_style(
		        width=1.1,
		        dash="solid_line",
		        custom_dash_pattern="111000",
		        cap="flat_cap",
		        join="bevel_join",
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "no_fill"
		    # fill="solid_fill"
		    # fill="picture_fill"
		    ret = group.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: ungroup
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.ungroup()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    shape = slide.add_group([rect1, rect2, rect3])
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    shape.add_tag(tag)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag.name)
		        print(tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    shape = slide.add_group([rect1, rect2, rect3])
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    shape = slide.add_group([rect1, rect2, rect3])
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.add_tag(tag2)
		    print(ret)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag.name, tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shapes
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    shapes = group.get_shapes()
		    for shape in shapes:
		        print(shape)
		        print(shape.name)
		        print(shape.slide_name)
		        print(shape.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    ret = group.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rect1 = slide.add_rectangle()
		    rect2 = slide.add_rectangle()
		    rect3 = slide.add_rectangle()
		    group = slide.add_group([rect1, rect2, rect3])
		    group.set_visibility(False)
		    ret = group.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x an y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Filename pointing to an image file.

		Returns
		-------
		bool

		"""


	def ungroup(self) -> bool:

		"""

		Resolves the group into the shapes it consists of. Invalidates this object.


		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_shapes(self) -> object:

		"""

		Returns the shapes (textboxes, tables, images, lines, etc) that belong to this group.


		Returns
		-------
		object
			List of meta.report.Rectangle, meta.report.Triangle, meta.report.Line, meta.report.ShapeGroup, meta.report.Textbox, meta.report.Table etc. objects.

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Rectangle:

	"""

	A rectangle in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    print(rectangle)
		    # Second handler for the same rectangle using constructor
		    rectangle2 = report.Rectangle(
		        report_name=rep.name, slide_name=slide.name, shape_name=rectangle.name
		    )
		    print(rectangle2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    name = "rectangle name"
		    ret = rectangle.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    rep = rectangle.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    slide = rectangle.get_slide()
		    print(slide.name)
		    print(slide.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    position = rectangle.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    position = (0.5, 0.5)
		    ret = rectangle.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    size = rectangle.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    size = (0.25, 0.25)
		    ret = rectangle.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    ret = rectangle.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    ret = rectangle.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    ret = rectangle.send_to_back()
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    ret = rectangle.send_backward()
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    angle = 90
		    ret = rectangle.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    rotation = rectangle.get_rotation()
		    print(rotation)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    c = Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = rectangle.set_line_style(
		        fill="solid_line",
		        color=c,
		        width=1.2,
		        dash="solid_line",
		        custom_dash_pattern="111000",
		        cap="flat_cap",
		        join="bevel_join",
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "no_fill"
		    # fill="solid_fill"
		    # fill="picture_fill"
		    ret = rectangle.set_fill(fill, color=c, filename="image.png")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    size = (0.25, 0.25)
		    ret = rectangle.set_size(size)
		    text = "text"
		    ret = rectangle.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    text = rectangle.get_text()
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rectangle = slide.add_rectangle()
		    ret = rectangle.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = rectangle.set_text_style(italic= True, underline= True, bold=True, strike_through=True, superscript = True, subscript = True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = rectangle.set_text_style(text_color = color,  text_align = 'left', line_spacing = 1.1, shape_align = 'top', autofit = 'no_autofit', wrap = True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		        print(tag.name, tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # shape.set_text_style(italic=True, strike_through=True, superscript=True, subscript=True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # shape.set_text_style(text_color = color, text_align = 'left', line_spacing = 1.2, space_align = 'top', autofit = 'no_autofit', wrap =True)
		    style = shape.get_text_style()
		    print(style)
		
		    shape2 = slide.add_rectangle()
		    shape2.set_text_style(**style)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_rectangle()
		    shape.set_visibility(False)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the shape.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.font_family     stringfont_size       integerbold            booleanitalic          booleanunderline       booleanstrike_through  booleansuperscript     booleansubscript       booleantext_color      meta.windows.Colortext_align      string                        'left'                        'center'                        'right'                        'justify'shape_align     string                        'top'                        'middle'                        'bottom'                        'top_center'                        'middle_center'                        'bottom_center'autofit         string                        'no_autofit'                        'shrink_text_on_overflow'                        'resize_shape_to_fit_text'wrap            boolean

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Ellipse:

	"""

	An ellipse in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    # name = 'Ellipse 1'
		    # ellipse = slide.add_ellipse(name)
		    print(ellipse)
		    # Second handler for the same ellipse using constructor
		    ellipse2 = report.Ellipse(
		        report_name=rep.name, slide_name=slide.name, shape_name=ellipse.name
		    )
		    print(ellipse2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    name = "ellipse name"
		    ret = ellipse.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    r = ellipse.get_report()
		    print(r.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    slide = ellipse.get_slide()
		    print(slide.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    pos = ellipse.get_position()
		    # pos = ellipse.get_position(unit = 'pixel')
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    pos = (0.5, 0.5)
		    ret = ellipse.set_position(pos)  # Middle of the slide
		    print(ret)
		
		    pos = (50, 20)
		    ret = ellipse.set_position(pos, unit="mm")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    size = ellipse.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    size = (0.25, 0.25)
		    ret = ellipse.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		    size = (200, 400)
		    ret = ellipse.set_size(size, unit="pixel")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    ret = ellipse.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    ret = ellipse.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    ret = ellipse.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    ret = ellipse.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    angle = 90
		    ret = ellipse.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    rot = ellipse.get_rotation()
		    print(rot)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    fill = "no_line"
		    # fill = 'solid_line'
		    ret = ellipse.set_line_style(fill)
		    print(ret)
		    c = windows.Color(name="color1", r=0, g=255, b=0, a=255)
		    ret = ellipse.set_line_style(fill, color=c)
		    # ret = ellipse.set_line_style(fill, color=c, width = 10)
		    # ret = ellipse.set_line_style(fill, color=c, width = 10, dash = 'sys_dash_dot_dot_line')
		    # ret = ellipse.set_line_style(fill, color=c, width = 10, dash = 'custom_dash_line', custom_dash_pattern = '111000')
		    # ret = ellipse.set_line_style(fill, color=c, width = 10, dash = 'custom_dash_line', custom_dash_pattern = '111000', cap = 'round_cap')
		    # ret = ellipse.set_line_style(fill, color=c, width = 10, dash = 'custom_dash_line', custom_dash_pattern = '111000', cap = 'round_cap', join = 'miter_join')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    fill = "no_fill"
		    # fill = 'solid_fill'
		    # fill = 'picture_fill'
		    ret = ellipse.set_fill(fill)
		    print(ret)
		    c = windows.Color(name="color1", r=255, g=0, b=0, a=50)
		    ret = ellipse.set_fill(fill, color=c)
		    # ret = ellipse.set_fill("picture_fill", filename = "/home/images/Image1.png")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    pos = (0.25, 0.25)
		    ellipse.set_size(pos)
		    text = "my_text"
		    ret = ellipse.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    text = "my_text"
		    ret = ellipse.set_text(text)
		    print(ret)
		    text = ellipse.get_text()
		    # text = ellipse.get_text(html = True)
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		
		    pos = (0.25, 0.25)
		    ellipse.set_size(pos)
		    text = "my_text"
		    ret = ellipse.set_text(text)
		    ret = ellipse.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = ellipse.set_text_style(italic=True, underline=Tru, superscript=True, strike_through=True, subscript = True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = ellipse.set_text_style(text_color = color, text_align = 'left', line_spacing = 1.2, shape_align = 'top', autofit = 'no_autofit', wrap = True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = ellipse.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    tag = report.CreateReportTag("tag_name", "tag_value")
		    ellipse.add_tag(tag)
		    ret = ellipse.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    ellipse = slide.add_ellipse()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    ellipse.add_tag(tag)
		    ellipse.add_tag(tag2)
		    tags = ellipse.get_tags()
		    for t in tags:
		        print(t.name, t.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_ellipse()
		    shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    shape.set_text_style(
		        italic=True,
		        underline=True,
		        strike_through=True,
		        superscript=True,
		        subscript=True,
		    )
		    color = windows.Color(r=255, g=255, b=0, a=255)
		    shape.set_text_style(
		        text_color=color,
		        text_align="left",
		        shape_align="top",
		        autofit="no_autofit",
		        wrap=True,
		    )
		    style = shape.get_text_style()
		    print(style)
		
		    shape2 = slide.add_ellipse()
		    shape2.set_text_style(**style)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_ellipse()
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_ellipse()
		    shape.set_visibility(False)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the ellipse name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this ellipse belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this ellipse belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the ellipse.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the ellipse.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the ellipse width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the ellipse.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place ellipse in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place ellipse in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place ellipse behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place ellipse behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this ellipse in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this ellipse in degrees.


		Returns
		-------
		float

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the ellipse.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the ellipse tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the ellipse.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the ellipse.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.font_family     stringfont_size       integerbold            booleanitalic          booleanunderline       booleanstrike_through  booleansuperscript     booleansubscript       booleantext_color      meta.windows.Colortext_align      string                        'left'                        'center'                        'right'                        'justify'shape_align     string                        'top'                        'middle'                        'bottom'                        'top_center'                        'middle_center'                        'bottom_center'autofit         string                        'no_autofit'                        'shrink_text_on_overflow'                        'resize_shape_to_fit_text'wrap            boolean

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Triangle:

	"""

	A triangle in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    print(triangle)
		    # Second handler for the same triangle using constructor
		    triangle2 = report.Triangle(
		        report_name=rep.name, slide_name=slide.name, shape_name=triangle.name
		    )
		    print(triangle2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    name = "triangle name"
		    ret = triangle.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    rep = triangle.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    slide = triangle.get_slide()
		    print(slide)
		    print(slide.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    position = triangle.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    position = (0.5, 0.5)
		    ret = triangle.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    size = triangle.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    size = (0.25, 0.25)
		    ret = triangle.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    ret = triangle.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    ret = triangle.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    ret = triangle.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    ret = triangle.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    angle = 90
		    ret = triangle.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    rotation = triangle.get_rotation()
		    print(rotation)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    # c = Color(name = "color1", r = 0, g = 255, b = 0, a = 255)
		    fill = "no_line"
		    # fill = 'solid_line'
		    ret = triangle.set_line_style(fill)
		    # ret = triangle.set_line_style(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "no_fill"
		    # fill = 'no_fill'
		    # fill = 'picture_fill'
		    ret = triangle.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    size = (0.25, 0.25)
		    ret = triangle.set_size(size)
		    text = "text"
		    ret = triangle.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    text = triangle.get_text()
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    triangle = slide.add_triangle()
		    triangle.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    shape.add_tag(tag)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    name = "tag_name"
		    value = "tag_value"
		    tag = report.CreateReportTag(name, value)
		    name = "tag_name2"
		    value = "tag_value2"
		    tag2 = report.CreateReportTag(name, value)
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    style = shape.get_text_style()
		    print(style)
		
		    shape2 = slide.add_triangle()
		    shape2.set_text_style(**style)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_triangle()
		    shape.set_visibility(False)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the shape.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.font_family     stringfont_size       integerbold            booleanitalic          booleanunderline       booleanstrike_through  booleansuperscript     booleansubscript       booleantext_color      meta.windows.Colortext_align      string                        'left'                        'center'                        'right'                        'justify'shape_align     string                        'top'                        'middle'                        'bottom'                        'top_center'                        'middle_center'                        'bottom_center'autofit         string                        'no_autofit'                        'shrink_text_on_overflow'                        'resize_shape_to_fit_text'wrap            boolean

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class TableRange:

	"""

	A range of cells on a table in a report in META. The range is a contiguous rectangle of cells. It is represented by the minimum row and column of the cells (top left corner), and the maximum row and column (bottom right corner).

	See Also
	--------
	report.Report, report.Slide, report.Table, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    # Second handler for the same textbox using constructor
		    range2 = report.TableRange(rep.name, slide.name, table.name, [1, 1], [2, 2])
		    print(range2)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    rep = range.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    slide = range.get_slide()
		    print(slide)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shape
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    table_range = range.get_shape()
		    print(table_range)
		    print(table_range.name)
		    print(table_range.slide_name)
		    print(table_range.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    text = "text"
		    ret = range.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    ret = range.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = range.set_text_style(italic = True, underline = True, strike_through=True, superscript=True, subscript = True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = range.set_text_style(text_color = color, text_align  = 'left', shape_align = 'top', autofit = 'no_autofit', wrap = True )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    height = 0.3
		    ret = range.set_row_height(height)
		    # u = 'emu'
		    # ret = range.set_row_height(height, unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    width = 0.3
		    ret = range.set_column_width(width)
		    # u = 'emu'
		    # ret = range.set_column_width(width, unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: merge
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    ret = range.merge()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: split
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    ret = range.split()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "solid_fill"
		    ret = range.set_fill(fill)
		    # ret =range.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    top_left = [1, 1]
		    bottom_right = [2, 2]
		    range = table.get_range(top_left, bottom_right)
		    text = "text"
		    ret = range.set_text(text)
		    print(ret)
		    ret = range.set_margins(left=2, top=2)
		    ret = range.set_margins(right=2, bottom=2)
		    # u = 'cm'
		    # u = 'mm'
		    # u = 'inch'
		    # u = 'pt'
		    # u = 'pixel'
		    # ret = range.set_margins(right=2, bottom=2, unit  = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	min_row: int = None

	min_column: int = None

	max_row: int = None

	max_column: int = None

	def set_text(self, text: str) -> bool:

		"""

		Set the text for every cell in the range. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, line_spacing: float, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		line_spacing : float, optional
			See corresponding setting in GUI for spacing values.

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

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


	def set_row_height(self, height: float, unit: str) -> bool:

		"""

		Set the row height. Takes an optional unit argument.


		Parameters
		----------
		height : float
			Row height.

		unit : str, optional
			Unit of the given height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

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
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_shape(self) -> object:

		"""

		Return the table that this range belongs to.


		Returns
		-------
		object
			meta.report.Table

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_margins(self, left: float, right: float, top: float, bottom: float, unit: str) -> bool:

		"""

		Sets the margin between the text and the edges of each cell, for all cells in the range.


		Parameters
		----------
		left : float, optional
			Left margin.

		right : float, optional
			Right margin.

		top : float, optional
			Top margin.

		bottom : float, optional
			Bottom margin.

		unit : str, optional
			Unit of the given margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		bool

		"""

class TableCell:

	"""

	A cell on a table in a report in META.

	See Also
	--------
	report.Report, report.Slide, report.Table, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    # Second handler for the same textbox using constructor
		    cell2 = report.TableCell(rep.name, slide.name, table.name, [1, 1])
		    print(cell2)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    rep = cell.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell([1, 1])
		    slide = cell.get_slide()
		    print(slide)
		    print(slide.name)
		    print(slide.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_shape
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    print(cell)
		    print(cell.slide_name, cell.report_name, cell.row, cell.column)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    text = "text"
		    ret = cell.set_text(text)
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    text = "some text"
		    ret = cell.set_text(text)
		    text = cell.get_text()
		    print(text)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    table = slide.add_table(3, 2)
		    cell = table.get_cell([1, 1])
		    ret = cell.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = cell.set_text_style(italic=True, underline=True, strike_through=True, superscript=True, subscript =True)
		    # ret = cell.set_text_style(italic=True, underline=True, strike_through=True, superscript=True, subscript =True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = cell.set_text_style(text_color = color, text_align = 'left', shape_align = 'top')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_row_height
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    height = 0.3
		    ret = cell.set_row_height(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_column_width
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    width = 0.3
		    ret = cell.set_column_width(width)
		    # u = 'emu'
		    # ret = cell.set_column_width(width, unit = u)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "no_fill"
		    ret = cell.set_fill(fill)
		    # ret = cell.set_fill(fill, color=c)
		    # ret = cell.set_fill(fill, filaname = '/home/image.png')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    ret = cell.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    # ret = cell.set_text_style(italic=True, underline=True, bold=True, strike_through=True, superscript =True, subscript =True)
		    # color = windows.Color(r = 255, g = 255, b = 0, a = 255)
		    # ret = cell.set_text_style(text_color = color, text_align = 'left', shape_align = 'top')
		    style = cell.get_text_style()
		    print(style)
		    position = [1, 2]
		    cell2 = table.get_cell(position)
		    ret = cell2.set_text_style(**style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    text = "text"
		    ret = cell.set_text(text)
		    print(ret)
		    ret = cell.set_margins(left=2, top=2)
		    ret = cell.set_margins(right=2, bottom=2)
		    ret = cell.set_margins(right=2, bottom=2, unit="cm")
		    print(ret)
		    u = "cm"
		    margins = cell.get_margins(unit=u)
		    print(margins)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_margins
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    rows = 3
		    columns = 2
		    table = slide.add_table(rows, columns)
		    position = [1, 1]
		    cell = table.get_cell(position)
		    text = "text"
		    ret = cell.set_text(text)
		    left = 2
		    top = 2
		    ret = cell.set_margins(left, top)
		    # ret = cell.set_margins(right, bottom)
		    # u = 'cm'
		    # ret = cell.set_margins(right, bottom, unit = u)
		    margins = cell.get_margins()
		    # margins = cell.get_margins(unit = u)
		    print(margins)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	row: int = None

	column: int = None

	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the cell.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

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
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

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
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_shape(self) -> object:

		"""

		Return the table that this cell belongs to.


		Returns
		-------
		object
			meta.report.Table

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.              font_family     string              font_size       integer              bold            boolean              italic          boolean              underline       boolean              strike_through  boolean              superscript     boolean              subscript       boolean              text_color      meta.windows.Color              text_align      string                                    'left'                                    'center'                                    'right'                                    'justify'              shape_align     string                                    'top'                                    'middle'                                    'bottom'                                    'top_center'                                    'middle_center'                                    'bottom_center'              autofit         string                                    'no_autofit'                                    'shrink_text_on_overflow'                                    'resize_shape_to_fit_text'              wrap            boolean

		"""


	def set_margins(self, left: float, right: float, top: float, bottom: float, unit: str) -> bool:

		"""

		Sets the margin between the text and the edges of the cell.


		Parameters
		----------
		left : float, optional
			Left margin.

		right : float, optional
			Right margin.

		top : float, optional
			Top margin.

		bottom : float, optional
			Bottom margin.

		unit : str, optional
			Unit of the given margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		bool

		"""


	def get_margins(self, unit: str) -> object:

		"""

		Returns the margin between the text and the edges of the cell.


		Parameters
		----------
		unit : str, optional
			Unit of the returned margins.
			Available values are listed below. The default value is 'mm'.
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pixel'

		Returns
		-------
		object
			Array of floats with the respective margin [left, right, top, bottom]

		"""

class ReportFilter:

	"""

	A ReportFilter object is used to find pptx files based on their tags. There are four possible types of ReportFilter objects (as specified by the first argument in the constructor): 'presentation', 'slide', 'element', and 'tag'.
	
	ReportFilter objects of type 'tag' that specify a tag name, an operator such as 'equal', and a value represent specific rules by which to match tags. The other three types of ReportFilter objects, namely 'presentation', 'slide', and 'element' specify whether the search should match presentation tags, slide tags or element tags accordingly. This is achieved by adding the desired 'tag' object as a child of the corresponding 'presentation', 'slide', or 'element' object. 
	
	The tree structure can be expanded to achieve more complex matching rules.
	
	Constructor Arguments
	
	type      string                Available values are listed below. Note that the 'tag' type also requires the rest of the arguments to be specified, a name, operator, and at least one value (depending on the operator).
	                                 'presentation'
	                                 'slide'
	                                 'element'
	                                 'tag'
	name      string    (optional)  The tag name to search for.
	operator  string    (optional)  Available values are listed below, note that some operators require a value2 argument as well.
	                                 'equal'
	                                 'less'
	                                 'greater'
	                                 'less_equal'
	                                 'greater_equal'
	                                 'not_equal'
	                                 'between'
	                                 'not_between'
	                                 'contains'
	                                 'not_contains'
	                                 'starts_with'
	                                 'not_starts_with'
	                                 'ends_with'
	                                 'not_ends_with'
	                                 'reg_expression'
	                                 'not_reg_expression'
	value     string    (optional)  The tag value that is matched against the value of the tags in the report files using the specified operator.
	value2    string    (optional)  A second optional value required by operators  'between' and 'not_between'.

	See Also
	--------
	report.ReportTag

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    type = "presentation"
		    # type = 'slide'
		    # type = 'element'
		    # type = 'tag'
		    presFilter = report.ReportFilter(type)
		    tagFilter = report.ReportFilter(
		        type="tag", name="tag1", operator="equal", value="value1"
		    )
		    report_filter = presFilter.add_child(tagFilter)
		    if report_filter:
		        print(report_filter)
		
		
		if __name__ == "__main__":
		    main()
		# method: search
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    directory = "../"
		    type = "presentation"
		    # type = 'slide'
		    # type = 'element'
		    # type = 'tag'
		    presFilter = report.ReportFilter(type)
		    tagFilter = report.ReportFilter(
		        type="tag", name="tag1", operator="equal", value="value1"
		    )
		    presFilter.add_child(tagFilter)
		    print(presFilter.search(directory))
		
		
		if __name__ == "__main__":
		    main()
		# method: get_children
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    presFilter = report.ReportFilter(type="presentation")
		    tagFilter = report.ReportFilter(
		        type="tag", name="tag1", operator="equal", value="value1"
		    )
		    tagFilter2 = report.ReportFilter(
		        type="tag", name="tag2", operator="equal", value="value2"
		    )
		    presFilter.add_child(tagFilter)
		    presFilter.add_child(tagFilter2)
		    print(presFilter.get_children())
		
		
		if __name__ == "__main__":
		    main()
		# method: add_child
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    presFilter = report.ReportFilter(type="presentation")
		    tagFilter = report.ReportFilter(
		        type="tag", name="tag1", operator="equal", value="value1"
		    )
		    tagFilter2 = report.ReportFilter(
		        type="tag", name="tag2", operator="equal", value="value2"
		    )
		    presFilter.add_child(tagFilter)
		    presFilter.add_child(tagFilter2)
		    print(presFilter.get_children())
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_child
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    presFilter = report.ReportFilter(type="presentation")
		    tagFilter = report.ReportFilter(
		        type="tag", name="tag1", operator="equal", value="value1"
		    )
		    tagFilter2 = report.ReportFilter(
		        type="tag", name="tag2", operator="equal", value="value2"
		    )
		    presFilter.add_child(tagFilter)
		    presFilter.add_child(tagFilter2)
		    presFilter.remove_child(tagFilter)
		    print(presFilter.get_children())
		
		
		if __name__ == "__main__":
		    main()

	"""


	def search(self, directory: str, folder_filter: str, file_filter: str, search_in_subfolders: bool) -> object:

		"""

		Finds pptx files whose tags match this filter, in the specified folder. Files can also be optionally filtered by their name using the file_filter option. Subfolders can be optionally search and filtered as well using the corresponding options.


		Parameters
		----------
		directory : str
			Search directory.

		folder_filter : str, optional
			A string to filter the sub-folders by their name. An '*' corresponds to any sub-string in the folder name. This argument is used only when search_in_subfolders is True. As an example a value of 'arp*' will match folders whose name begins with 'arp'.

		file_filter : str, optional
			A string to filter the pptx files based on their name. An '*' corresponds to any sub-string in the file name. As an example a value of 'arp*' will match files whose name begins with 'arp'.

		search_in_subfolders : bool, optional
			Whether to search sub-folders. Default value is False.

		Returns
		-------
		object
			List of matching pptx file-paths

		"""


	def get_children(self) -> object:

		"""

		Returns a list with the children of this filter.


		Returns
		-------
		object
			List of report.ReportFilter objects

		"""


	def add_child(self, filter: object) -> bool:

		"""

		Adds a child to this filter.


		Parameters
		----------
		filter : object
			report.ReportFilter object

		Returns
		-------
		bool

		"""


	def remove_child(self, filter: object) -> bool:

		"""

		Removes the specified child.


		Parameters
		----------
		filter : object
			report.ReportFilter object

		Returns
		-------
		bool

		"""

class ReportTag:

	"""

	Represents a report tag. Tags can be added to presentations, slides, and slide elements. Tags have a tree structure. Each tag can contain other tags as children. Each tag is defined by its name and value.

	See Also
	--------
	report.Report, report.Slide, report.ReportFilter

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    tag = report.ReportTag(name="tag_name", value="tag_value")
		    print(tag)
		    print(tag.name, tag.value)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_children
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    tag = report.ReportTag(name="tag_name", value="tag_value")
		    child1 = report.ReportTag(name="child_tag_name", value="child_tag_value")
		    tag.add_child(child1)
		    print(tag.get_children())
		
		
		if __name__ == "__main__":
		    main()
		# method: add_child
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    tag = report.ReportTag(name="tag_name", value="tag_value")
		    child1 = report.ReportTag(name="child_tag_name", value="child_tag_value")
		    tag.add_child(child1)
		    print(tag.get_children())
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_child
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    tag = report.ReportTag(name="tag_name", value="tag_value")
		    child1 = report.ReportTag(name="tag_name2", value="tag_value2")
		    child2 = report.ReportTag(name="tag_name3", value="tag_value3")
		    tag.add_child(child1)
		    tag.add_child(child2)
		    tag.remove_child(child2)
		    print(tag.get_children())
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None

	value: str = None

	def get_children(self) -> object:

		"""

		Returns a list with the children of this tag.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_child(self, tag: object) -> bool:

		"""

		Adds a child to this tag.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_child(self, tag: object) -> bool:

		"""

		Removes the specified child.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""

class Freeform:

	"""

	A freeform shape in a report in META.

	See Also
	--------
	report.Report, report.Slide, windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    # Second handler for the same freeform shape using constructor
		    freeform2 = report.Freeform(
		        report_name=rep.name, slide_name=slide.name, shape_name=freeform.name
		    )
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    name = "freeform name"
		    ret = freeform.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    name = "freeform name"
		    ret = freeform.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    print(freeform)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    print(freeform)
		    print(freeform.name)
		    print(freeform.slide_name)
		    print(freeform.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    position = (0.5, 0.5)
		    ret = freeform.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    print(freeform)
		    print(freeform.name)
		    print(freeform.slide_name)
		    print(freeform.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    size = (0.25, 0.25)
		    ret = freeform.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    ret = freeform.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    ret = freeform.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    ret = freeform.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    ret = freeform.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    angle = 90
		    ret = freeform.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    print(freeform)
		    print(freeform.name)
		    print(freeform.slide_name)
		    print(freeform.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    c = Color(name="color1", r=0, g=255, b=0, a=255)
		    fill = "solid_line"
		    ret = freeform.set_line_style(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "solid_fill"
		    ret = freeform.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    size = (0.25, 0.25)
		    ret = freeform.set_size(size)
		    text = "text"
		    ret = freeform.set_text(text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    print(freeform)
		    print(freeform.name)
		    print(freeform.slide_name)
		    print(freeform.report_name)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_style
		# PYTHON script
		import meta
		from meta import report
		from meta import windows
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    freeform = slide.add_freeform()
		    ret = freeform.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    ret = freeform.set_text_style(
		        italic=True,
		        underline=True,
		        strike_through=True,
		        superscript=True,
		        subscript=True,
		    )
		    color = windows.Color(r=255, g=255, b=0, a=255)
		    ret = freeform.set_text_style(
		        text_color=color, text_align="left", shape_align="top", autofit="no_autofit"
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    tag2 = report.CreateReportTag(name="tag_name2", value="tag_value2")
		    ret = shape.add_tag(tag)
		    ret = shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_points
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    points = [[0.1, 0.1], [0.9, 0.9]]
		    shape.set_points(points)
		    points = shape.get_points()
		    print(points)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_points
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    points = [[0.1, 0.1], [0.9, 0.9]]
		    ret = shape.set_points(points)
		    print(ret)
		    points = shape.get_points()
		    print(points)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_style
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    shape.set_text_style(
		        font_family="Monospace", font_size=24, bold=True, underline=True
		    )
		    style = shape.get_text_style()
		    print(style)
		    shape2 = slide.add_freeform()
		    shape2.set_text_style(**style)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_freeform()
		    shape.set_visibility(False)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_line_style(self, fill: str, color: object, width: float, dash: str, custom_dash_pattern: str, cap: str, join: str) -> bool:

		"""

		Set various line style options. All arguments are optional, any number of them can be used. The result is visible only when fill is 'solid_line'.


		Parameters
		----------
		fill : str, optional
			The available values are:
			- 'no_line'
			- 'solid_line'

		color : object, optional
			meta.windows.Color

		width : float, optional
			Line width.

		dash : str, optional
			One of the following predefined dash patterns:
			'solid_line'
			'dash_line'
			'dot_line'
			'dash_dot_line'
			'lg_dash_line'
			'lg_dash_dot_line'
			'lg_dash_dot_dot_line'
			'sys_dash_line'
			'sys_dash_dot_line'
			'sys_dash_dot_dot_line'
			'sys_dot_line'
			'custom_dash_line'

		custom_dash_pattern : str, optional
			A series of 1's and 0's describing a dash pattern. For example '111000'.

		cap : str, optional
			One of the following:
			'flat_cap'
			'round_cap'
			'square_cap'

		join : str, optional
			One of the following:
			'bevel_join'
			'miter_join'
			'round_join'

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_text(self, text: str) -> bool:

		"""

		Set the text. Accepts html for formatting.


		Parameters
		----------
		text : str

		Returns
		-------
		bool

		"""


	def get_text(self, html: bool) -> str:

		"""

		Returns the text of the shape.


		Parameters
		----------
		html : bool, optional
			When True the text is returned in html formatting. The default value is False.

		Returns
		-------
		str

		"""


	def set_text_style(self, font_family: str, font_size: int, bold: bool, italic: bool, underline: bool, strike_through: bool, superscript: bool, subscript: bool, text_color: object, text_align: str, shape_align: str, autofit: str, wrap: bool) -> bool:

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

		text_align : str, optional
			The following values are supported:
			'left'
			'center'
			'right'
			'justify'

		shape_align : str, optional
			The following values are supported:
			'top'
			'middle'
			'bottom'
			'top_center'
			'middle_center'
			'bottom_center'

		autofit : str, optional
			The following values are supported:
			'no_autofit'
			'shrink_text_on_overflow'
			'resize_shape_to_fit_text'

		wrap : bool, optional
			Wrap text option.

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def get_points(self, unit: str) -> object:

		"""

		Returns a list of the points of this shape. The points are optionally converted to the desired unit.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list of x, y pairs in the requested units.

		"""


	def set_points(self, points: object, unit: str) -> bool:

		"""

		Set the points of this shape.


		Parameters
		----------
		points : object
			A non-empty list of pairs of x, y coordinates.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

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
			Python dictionary with the following text style options.font_family     stringfont_size       integerbold            booleanitalic          booleanunderline       booleanstrike_through  booleansuperscript     booleansubscript       booleantext_color      meta.windows.Colortext_align      string                        'left'                        'center'                        'right'                        'justify'shape_align     string                        'top'                        'middle'                        'bottom'                        'top_center'                        'middle_center'                        'bottom_center'autofit         string                        'no_autofit'                        'shrink_text_on_overflow'                        'resize_shape_to_fit_text'wrap            boolean

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Model3D:

	"""

	A 3d model in a report in META.

	See Also
	--------
	report.Report, report.Slide

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    # Second handler for the same model using constructor
		    model2 = report.Model3D(rep.name, slide.name, model.name)
		    print(model2)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.set_name("model name")
		    print(model.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    print(model.get_report())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    print(model.get_slide())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    print(model.get_position())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.set_position((0.5, 0.5))  # Middle of the slide
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    print(model.get_size())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.set_size((0.25, 0.25))  # A quarter of the size of the slide
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.bring_to_front()
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.bring_forward()
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.send_to_back()
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.send_backward()
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.set_rotation(90)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    print(model.get_rotation())
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_model("model.glb")
		    tag = report.CreateReportTag("tag_name", "tag_value")
		    shape.add_tag(tag)
		    print(shape.get_tags())
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_model("model.glb")
		    tag = report.CreateReportTag("tag_name", "tag_value")
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    shape.remove_tag(tag)
		    print(shape.get_tags())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_model("model.glb")
		    tag = report.CreateReportTag("tag_name", "tag_value")
		    tag2 = report.CreateReportTag("tag_name2", "tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    print(shape.get_tags())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_model("model.glb")
		    model.set_file("model2.glb")
		    print(model.get_file())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    model = slide.add_3dmodel("model.glb")
		    print(model.get_file())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_3dmodel("model.glb")
		    print(shape.get_visibility())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_3dmodel("model.glb")
		    shape.set_visibility(False)
		    print(shape.get_visibility())
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x an y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def get_file(self) -> str:

		"""

		Returns the path of the underlying model file.


		Returns
		-------
		str

		"""


	def set_file(self, filename: str) -> bool:

		"""

		Sets the underlying model file.


		Parameters
		----------
		filename : str
			Path to a .glb model file.

		Returns
		-------
		bool

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class VideoShape:

	"""

	A video shape in a report in META.

	See Also
	--------
	report.Report, report.Slide

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    # Second handler for the same video using constructor
		    video2 = report.VideoShape(
		        report_name=rep.name, slide_name=slide.name, shape_name=video.name
		    )
		    print(video2)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    rep = video.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    slide = video.get_slide()
		    print(slide)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    position = video.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    position = (0.5, 0.5)
		    ret = video.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    print(video.get_size())
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video.avi"
		    video = slide.add_video(filename)
		    size = (0.25, 0.25)
		    ret = video.set_size(size)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video.avi"
		    video = slide.add_video(filename)
		    ret = video.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    ret = video.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    ret = video.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    ret = video.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    rotation = video.get_rotation()
		    print(rotation)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_rotation
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    angle = 90
		    ret = video.set_rotation(angle)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    name = "video name"
		    ret = video.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    shape = slide.add_video(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    shape = slide.add_video(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    shape = slide.add_video(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    tag2 = report.CreateReportTag(name="tag_name2", value="tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_fill
		# PYTHON script
		import meta
		from meta import report
		from meta.windows import Color
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    c = Color(name="color1", r=255, g=0, b=0, a=50)
		    fill = "solid_fill"
		    ret = video.set_fill(fill, color=c)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    ret = video.set_file(filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    file = video.get_file()
		    print(file)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_embed
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    embed = False
		    ret = video.set_embed(embed)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_embed
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    video = slide.add_video(filename)
		    embed = video.get_embed()
		    print(embed)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    shape = slide.add_video(filename)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "video1.avi"
		    shape = slide.add_video(filename)
		    visibility = False
		    ret = shape.set_visibility(visibility)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def get_rotation(self) -> float:

		"""

		Return the angle of rotation of this shape in degrees.


		Returns
		-------
		float

		"""


	def set_rotation(self, angle: float) -> bool:

		"""

		Set the angle of rotation of this shape in degrees.


		Parameters
		----------
		angle : float
			The angle in degrees.

		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def set_fill(self, fill: str, color: object, filename: str) -> bool:

		"""

		Background fill options. Fill can be either empty ('no_fill'), have a solid color fill ('solid_fill'), or have a background image ('picture_fill'). The solid color option requires a valid color argument while the background image option requires a valid filename argument.


		Parameters
		----------
		fill : str, optional
			Supported values are:
			'no_fill'
			'solid_fill'
			'picture_fill'

		color : object, optional
			meta.windows.Color

		filename : str, optional
			Path to an image file.

		Returns
		-------
		bool

		"""


	def set_file(self, filename: str) -> bool:

		"""

		Set the displayed video.


		Parameters
		----------
		filename : str
			Path to a video file.

		Returns
		-------
		bool

		"""


	def get_file(self) -> str:

		"""

		Return the video file used by this shape.


		Returns
		-------
		str
			Path to the video file.

		"""


	def set_embed(self, embed: bool) -> bool:

		"""

		Define whether the video file will be embedded or linked on export.


		Parameters
		----------
		embed : bool
			True if the video file is embedded. False if the video file is linked.

		Returns
		-------
		bool

		"""


	def get_embed(self) -> bool:

		"""

		Whether the video is embedded or linked.


		Returns
		-------
		bool
			True if the video file is embedded. False if the video file is linked.

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

class Audio:

	"""

	An audio shape in a report in META.

	See Also
	--------
	report.Report, report.Slide

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    # Second handler for the same audio using constructor
		    audio2 = report.Audio(
		        report_name=rep.name, slide_name=slide.name, shape_name=audio.shape_name
		    )
		    print(audio2)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_report
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    rep = audio.get_report()
		    print(rep)
		    print(rep.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_slide
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    slide = audio.get_slide()
		    print(slide)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    position = audio.get_position()
		    print(position)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    position = (0.5, 0.5)
		    ret = audio.set_position(position)  # Middle of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    size = audio.get_size()
		    print(size)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_size
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    position = (0.25, 0.25)
		    ret = audio.set_size(position)  # A quarter of the size of the slide
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_to_front
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    ret = audio.bring_to_front()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: bring_forward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    ret = audio.bring_forward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_to_back
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    ret = audio.send_to_back()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: send_backward
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    ret = audio.send_backward()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_name
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    name = "audio name"
		    ret = audio.set_name(name)
		    print(ret)
		    print(audio.name)
		
		
		if __name__ == "__main__":
		    main()
		# method: add_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    shape = slide.add_audio(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    ret = shape.add_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: remove_tag
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    shape = slide.add_audio("audio1.mp2")
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    shape.add_tag(tag)
		    ret = shape.remove_tag(tag)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_tags
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    shape = slide.add_audio(filename)
		    tag = report.CreateReportTag(name="tag_name", value="tag_value")
		    tag2 = report.CreateReportTag(name="tag_name2", value="tag_value2")
		    shape.add_tag(tag)
		    shape.add_tag(tag2)
		    tags = shape.get_tags()
		    for tag in tags:
		        print(tag)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    ret = audio.set_file(filename)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_file
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    file = audio.get_file()
		    print(file)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_embed
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    embed = False
		    ret = audio.set_embed(embed)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_embed
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    audio = slide.add_audio(filename)
		    embed = audio.get_embed()
		    print(embed)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    shape = slide.add_audio(filename)
		    ret = shape.get_visibility()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visibility
		# PYTHON script
		import meta
		from meta import report
		
		
		def main():
		    rep = report.CreateReport()
		    slide = rep.get_slides()[0]
		    filename = "audio1.mp2"
		    shape = slide.add_audio(filename)
		    visibility = False
		    ret = shape.set_visibility(visibility)
		    print(ret)
		    visibility = shape.get_visibility()
		    print(visibility)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Shape name.

	"""

	slide_name: str = None
	"""
	Slide name.

	"""

	report_name: str = None
	"""
	Report Composer window name.

	"""

	def get_report(self) -> object:

		"""

		Return the report that this shape belongs to.


		Returns
		-------
		object
			meta.report.Report

		"""


	def get_slide(self) -> object:

		"""

		Return the slide that this shape belongs to.


		Returns
		-------
		object
			meta.report.Slide

		"""


	def get_position(self, unit: str) -> object:

		"""

		Return the coordinates of the top left corner of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			List that contains the x and y coordinates.

		"""


	def set_position(self, position: object, unit: str) -> bool:

		"""

		Set the top left corner position of the shape.


		Parameters
		----------
		position : object
			Either a list or 2-tuple that contains the desired coordinates of the top left corner of the shape.

		unit : str, optional
			Unit of the given coordinates.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def get_size(self, unit: str) -> object:

		"""

		Returns the width and height of the shape.


		Parameters
		----------
		unit : str, optional
			Unit of the returned width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		object
			A list that contains the width and height in the requested units.

		"""


	def set_size(self, size: object, unit: str) -> bool:

		"""

		Set the shape width and height.


		Parameters
		----------
		size : object
			Either a list or 2-tuple that contains the width and height.

		unit : str, optional
			Unit of the given width and height.
			Available values are listed below. The default value is 'norm'.
			- 'emu'
			- 'cm'
			- 'mm'
			- 'inch'
			- 'pt'
			- 'pc'
			- 'pixel'
			- 'norm' : Values normalized to slide dimensions

		Returns
		-------
		bool

		"""


	def bring_to_front(self) -> bool:

		"""

		Place shape in front of the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def bring_forward(self) -> bool:

		"""

		Place shape in front of the shape immediately in front of it.


		Returns
		-------
		bool

		"""


	def send_to_back(self) -> bool:

		"""

		Place shape behind the other shapes in the slide.


		Returns
		-------
		bool

		"""


	def send_backward(self) -> bool:

		"""

		Place shape behind the shape immediately behind it.


		Returns
		-------
		bool

		"""


	def set_name(self, name: str) -> bool:

		"""

		Set the shape name.


		Parameters
		----------
		name : str

		Returns
		-------
		bool

		"""


	def get_tags(self) -> object:

		"""

		Returns the shape tags.


		Returns
		-------
		object
			List of report.ReportTag objects

		"""


	def add_tag(self, tag: object) -> bool:

		"""

		Adds a tag to the shape.


		Parameters
		----------
		tag : object
			report.ReportTag object

		Returns
		-------
		bool

		"""


	def remove_tag(self, tag: object) -> bool:

		"""

		Removes the given tag from the shape.


		Parameters
		----------
		tag : object
			Either a report.ReportTag object or a tag name.

		Returns
		-------
		bool

		"""


	def set_file(self, filename: str) -> bool:

		"""

		Set the displayed audio file.


		Parameters
		----------
		filename : str
			Path to an audio file.

		Returns
		-------
		bool

		"""


	def get_file(self) -> str:

		"""

		Return the audio file used by this shape.


		Returns
		-------
		str
			Path to the audio file.

		"""


	def set_embed(self, embed: bool) -> bool:

		"""

		Define whether the audio file will be embedded or linked on export.


		Parameters
		----------
		embed : bool
			True if the audio file is embedded. False if the audio file is linked.

		Returns
		-------
		bool

		"""


	def get_embed(self) -> bool:

		"""

		Whether the audio is embedded or linked.


		Returns
		-------
		bool
			True if the audio file is embedded. False if the audio file is linked.

		"""


	def get_visibility(self) -> bool:

		"""

		Returns the visibility status of the shape.


		Returns
		-------
		bool
			Returns True if the shape is visible and False otherwise.

		"""


	def set_visibility(self, visibility: bool) -> bool:

		"""

		Sets the visibility status of the shape.


		Parameters
		----------
		visibility : bool
			True makes the shape visible. False makes the shape hidden.

		Returns
		-------
		bool

		"""

