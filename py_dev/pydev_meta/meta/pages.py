from __future__ import annotations
from typing import *

def ActivatePage(page_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.activate` instead.


	This function makes active an existing page specified by its id.

	Parameters
	----------
	page_id : int
		Id of the page.

	Returns
	-------
	object
		Upon success, it returns an object of class Page referring to the corresponding active page.
		Else, a non valid page object is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 0
		    pg = pages.ActivatePage(page_id)
		    if pg:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.activate instead.", DeprecationWarning)

def ActivePage() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_pages` instead.


	This function searches for the currently active page.

	Returns
	-------
	object
		It returns an object of class Page referring to the currently active page.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    pg = pages.ActivePage()
		    print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_pages instead.", DeprecationWarning)

def CollectNewPagesEnd() -> object:

	"""

	This function ends recording the creation of new pages. This function should be preceded by a corresponding call to script function CollectNewPagesStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Page referring to one specific newly created page.
		Upon failure, an empty list is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		from meta import utils
		
		
		def main():
		    pages.CollectNewPagesStart()
		
		    # create new pages
		    utils.MetaCommand('page add "Page 1"')
		    utils.MetaCommand('page add "Page 2"')
		    new_pages = pages.CollectNewPagesEnd()
		    for pg in new_pages:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewPagesStart() -> int:

	"""

	This function starts recording the creation of new pages. This function should be followed by a corresponding call to script function CollectNewPagesEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		from meta import utils
		
		
		def main():
		    pages.CollectNewPagesStart()
		
		    # create new pages
		    utils.MetaCommand('page add "Page 1"')
		    utils.MetaCommand('page add "Page 2"')
		    new_pages = pages.CollectNewPagesEnd()
		    for pg in new_pages:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreatePage(page_name: str) -> object:

	"""

	This function creates a new page with a given name. The new page becomes the currently active page.

	Parameters
	----------
	page_name : str
		Name of the page

	Returns
	-------
	object
		Upon success, it returns an object of class Page referring to the newly created page.
		Upon failure, a non valid Page object will be returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_name = "Plot_Page"
		    pg = pages.CreatePage(page_name)
		    if pg:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeletePage(page_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.delete` instead.


	This function deletes an existing page specified by its id.

	Parameters
	----------
	page_id : int
		Id of the page.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 0
		    ret = pages.DeletePage(page_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.delete instead.", DeprecationWarning)

def IsPage(page: object) -> int:

	"""

	This function checks whether an object is of class Page.

	Parameters
	----------
	page : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Pagee, 0 otherwise.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		from meta import utils
		
		
		def main():
		    pages.CollectNewPagesStart()
		    # create new entities
		
		    utils.MetaCommand('page add "Page 1"')
		    utils.MetaCommand('page add "Page 2"')
		
		    all_entities = pages.CollectNewPagesEnd()
		    for ent in all_entities:
		        if pages.IsPage(ent):
		            pg = ent
		            print("This is a struct of type page")
		            print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PageById(page_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_pages` instead.


	This function searches for the page with the given id.

	Parameters
	----------
	page_id : int
		Id of the page.

	Returns
	-------
	object
		Upon success, it returns an object of class Page with the given id.
		Else, a non valid Page object is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 2
		    pg = pages.PageById(page_id)
		    if pg:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_pages instead.", DeprecationWarning)

def Pages() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_pages` instead.


	This function collects all the currently existing pages.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Page referring to the corresponding page.
		Upon failure, an empty list is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    all_pages = pages.Pages()
		    for pg in all_pages:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_pages instead.", DeprecationWarning)

def PagesByName(page_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_pages` instead.


	This function searches for the pages with the given name.

	Parameters
	----------
	page_name : str
		Argument "page_name" is a string expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Page referring to one existing page.
		Upon failure, an empty list is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_name = "Pag*"
		    collected_pages = pages.PagesByName(page_name)
		    for pg in collected_pages:
		        print(pg.id, pg.name, pg.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_pages instead.", DeprecationWarning)

def ReportNewPages() -> object:

	"""

	This function collects the newly created pages from the last call of script function CollectNewPagesStart(). This function should be preceded by a corresponding call to script function CollectNewPagesStart() and should be followed by a corresponding call to script function CollectNewPagesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Page referring to one specific newly created page.
		Upon failure, an empty list is returned.

	See Also
	--------
	pages.Page

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		from meta import utils
		
		
		def main():
		    pages.CollectNewPagesStart()
		
		    # create new pages
		    utils.MetaCommand('page add "Page 1"')
		    utils.MetaCommand('page add "Page 2"')
		
		    new_pages = pages.ReportNewPages()
		    for pg in new_pages:
		        print(pg.id, pg.name, pg.active)
		    pages.CollectNewPagesEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdatePage(page: object) -> object:

	"""

	This function updates the data of the given page struct. Update is based in the field "id" of the given page struct.

	Parameters
	----------
	page : object
		Object of class Page.

	Returns
	-------
	object
		Upon success, it returns the new updated Page object.
		Else, a non valid Page object is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		from meta import utils
		
		
		def main():
		    page_id = 0
		    pg = pages.PageById(page_id)
		
		    # commands which alter the data of the page struct
		    utils.MetaCommand('page rename 0 "new_name"')
		    pg = pages.UpdatePage(pg)
		    if pg:  # Update OK
		        print(pg.id, pg.name, pg.active)
		    else:  # Update FAILED
		        print("This is not a valid page struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def WindowsOfPage(page_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_windows` instead.


	This function collects all the currently existing windows of the specified page.

	Parameters
	----------
	page_id : int
		Id of the page.

	Returns
	-------
	object
		It returns a list where each memeber of the list is an object of class Window referring to one corresponding window of the given page.
		Upon failure, an empty list is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 0
		    page_windows = pages.WindowsOfPage(page_id)
		    for w in page_windows:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_windows instead.", DeprecationWarning)

def AttributesOfPage(page_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_attributes` instead.


	It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
	In position 0, internal lists contain a string referring to the name of the attribute.
	In position 1, internal lists contain a string referring to the value of the attributes.
	Upon failure, an empty list is returned.

	Parameters
	----------
	page_id : int
		The id of the page

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 1
		    all_attributes = pages.AttributesOfPage(page_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_attributes instead.", DeprecationWarning)

def SetAttributeOfPage(page_id: int, attrib_name: str, attrib_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given page. If the given attribute does not exist it is automatically created and its value is set

	Parameters
	----------
	page_id : int
		The id of the page.

	attrib_name : str
		Name of the attribute.

	attrib_value : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 1
		    attrib_name = "name"
		    attrib_value = "value"
		    val = pages.SetAttributeOfPage(page_id, attrib_name, attrib_value)
		    print(val)
		    # or
		    attrib_name = "n_name"
		    attrib_value = 123
		    attribute_type = "numerical"
		    val = pages.SetAttributeOfPage(page_id, attrib_name, attrib_value, attribute_type)
		    print(val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_attribute instead.", DeprecationWarning)

def AttributeOfPage(page_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	page_id : int
		The id of the page

	attrib_name : str
		The name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page_id = 1
		    name = "Name"
		    value = pages.AttributeOfPage(page_id, name)
		    print("Value " + value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_attributes instead.", DeprecationWarning)

class Page():

	"""

	Class for pages.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    # page = pages.Page(id='active')
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: activate
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    ret = page.activate()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    ret = page.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_annotation_groups
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    annot_groups = page.get_annotation_groups()
		    name = "annot_group_name"
		    annot_groups = page.get_annotation_groups(name)
		    for ag in annot_groups:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    # annots = page.get_annotations(specifier, id=1)
		    # specifier = 'visible'
		    # specifier = 'selected'
		    # specifier = 'visible_on_screen'
		    # specifier = 'hidden_on_screen'
		    # annots = page.get_annotations(specifier)
		    for a in annots:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curve_groups
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    groups = page.get_curve_groups()
		    for cg in groups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curves
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    # specifier = 'visible'
		    # specifier = 'selected'
		    curves = page.get_curves(specifier)
		    for c in curves:
		        print(
		            c.id,
		            c.name,
		            c.plot_id,
		            c.visible,
		            c.selected,
		            c.window_name,
		            c.page_id,
		            c.command,
		            c.entity_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_images
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    # specifier = 'visible'
		    # specifier = 'selected'
		    images = page.get_images(specifier)
		    for img in images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_isofunctions
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    isos = page.get_isofunctions(specifier)
		    # isos = page.get_isofunctions(specifier, name = 'iso_name')
		    # specifier = 'visible'
		    # isos = page.get_isofunctions(specifier)
		    for iso in isos:
		        print(iso.name, iso.window_name, iso.type, iso.value, iso.visible, iso.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot_axes
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    axes = page.get_plot_axes(specifier)
		    # axes = page.get_plot_axes(specifier, plot_axis_type = 'xaxis' )
		    # axes = page.get_plot_axes(specifier, plot_axis_id = 1 )
		    specifier = "visible"
		    # axes = page.get_plot_axes(specifier)
		    # specifier = 'active'
		    # axes = page.get_plot_axes(specifier)
		    for plax in axes:
		        print(
		            plax.id,
		            plax.type,
		            plax.plot_id,
		            plax.plot_id,
		            plax.window_name,
		            plax.active,
		            plax.visible,
		            plax.min_value,
		            plax.max_value,
		            plax.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plots
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    plots = page.get_plots(specifier)
		    # specifier = 'visible'
		    # plots = page.get_plots(specifier)
		    # plots = page.get_plots(specifier, plot_type  = 'plain')
		    specifier = "active"
		    # plots = page.get_plots(specifier)
		    # plots = page.get_plots(specifier, plot_type  = 'plain')
		    for pl in plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_videos
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    videos = page.get_videos(specifier)
		    # specifier = 'visible'
		    # videos = page.get_videos(specifier)
		    # specifier = 'selected'
		    # videos = page.get_videos(specifier)
		    for vid in videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_windows
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    wins = page.get_windows(specifier)
		    # wins = page.get_windows(specifier, name = 'MetaPost')
		    # specifier = 'active'
		    # specifier = 'enabled'
		    # wins = page.get_windows(specifier)
		    for w in wins:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_2d_positions_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    pos2d = [[0.93, 0.91], [0.14, 0.5]]
		    annots = annots[: len(pos2d)]
		    ret = page.set_2d_positions_on_annotations(annots, pos2d)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_3d_positions_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    pos3d = [[0, 0, 0], [100, 2000, 0]]
		    annots = annots[: len(pos3d)]
		    ret = page.set_3d_positions_on_annotations(annots, pos3d)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = page.set_attribute(attribute_name, attribute_type, attribute_value)
		    attribute_name = "new_attr"
		    attribute_type = "string"
		    attribute_value = "my_atrribute"
		    # ret = page.set_attribute('new_attr', 'string', 'my_atrribute')
		    print(ret)
		    attr = page.get_attributes(attribute_name="new_attr")
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    attribute_name = "new_attr"
		    attribute_type = "numerical"
		    attribute_value = 11.2
		    ret = page.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		    attr = page.get_attributes()
		    attribute_name = "new_attr"
		    # attr = page.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_boundaries_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    bounds = m.get_boundaries(specifier)
		    bounds = bounds[: len(annots)]
		    ret = page.set_boundaries_on_annotations(annots, bounds)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_curves_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    curves = page.get_curves(specifier)
		    curves = curves[: len(annots)]
		    point_ids = [i for i in range(len(annots))]
		
		    ret = page.set_curves_on_annotations(annots, curves, points=point_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_elements_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    elems = m.get_elements(specifier)
		    elems = elems[: len(annots)]
		
		    ret = page.set_elements_on_annotations(annots, elems)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_groups_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    groups = m.get_groups(specifier)
		    groups = groups[: len(annots)]
		    ret = page.set_groups_on_annotations(annots, groups)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_materials_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    materials = m.get_materials(specifier)
		    materials = materials[: len(annots)]
		    ret = page.set_materials_on_annotations(annots, materials)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_nodes_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    nodes = m.get_nodes(specifier)
		    nodes = nodes[: len(annots)]
		    ret = page.set_nodes_on_annotations(annots, nodes)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_parts_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    parts = m.get_parts(specifier)
		    parts = parts[: len(annots)]
		    ret = page.set_parts_on_annotations(annots, parts)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_planes_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		from meta import utils
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    planes = utils.get_planes(specifier)
		    planes = planes[: len(annots)]
		    ret = page.set_planes_on_annotations(annots, planes)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_windows_on_annotations
		# PYTHON script
		import meta
		from meta import pages
		from meta import models
		
		
		def main():
		    m = models.Model(0)
		    page = pages.Page(id=0)
		    specifier = "all"
		    annots = page.get_annotations(specifier)
		    wins = page.get_windows(specifier)
		    wins = wins[: len(annots)]
		    ret = page.set_windows_on_annotations(annots, wins)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_windows
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    message = "Pick Windows and press Enter when you are ready"
		    picked = page.pick_windows(message)
		    print(picked)
		
		
		if __name__ == "__main__":
		    main()
		# method: pick_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    page = pages.Page(id=0)
		    message = "Pick Annotations and press Enter when you are ready"
		    picked = page.pick_annotations(message)
		    print(picked)
		
		
		if __name__ == "__main__":
		    main()
		# method: save_image
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    pag = pages.Page(0)
		    file = "image.png"
		    pag.save_image(file)
		
		
		if __name__ == "__main__":
		    main()
		# method: save_video
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    pag = pages.Page(id=0)
		    file = "my_video.gif"
		    format = "gif"
		    pag.save_video(file, format)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    p = pages.Page(0)
		    annots = p.get_annotations()
		    p.show_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    p = pages.Page(0)
		    annots = p.get_annotations()
		    p.hide_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_annotations
		# PYTHON script
		import meta
		from meta import pages
		
		
		def main():
		    p = pages.Page(0)
		    annots = p.get_annotations()
		    p.delete_annotations(annots)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the page.

	"""

	name: str = None
	"""
	Name of the page.

	"""

	active: int = None
	"""
	- 1 if page is active
	- 0 if page is not active

	"""

	def get_isofunctions(self, specifier: str, name: str) -> object:

		"""

		This method gets the isofunctions of the page.


		Parameters
		----------
		specifier : str, optional
			The specifier of the method. Its possible values are:
			- 'all' : gets all the isofunctions (default value). Optionally combined with argument: name.
			- visible: gets the visible isofunctions.

		name : str, optional
			Name of the isofunction. Used only if specifier is 'all'. If this argument is set, the method will return only isofunctions that matches the pattern of the argument.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Isofunction. Upon failure, an empty list is returned

		"""


	def get_windows(self, specifier: str, name: str) -> object:

		"""

		This method gets the windows of the page.


		Parameters
		----------
		specifier : str, optional
			The specifier of the method, Its possible values are:
			- 'all' : all the windows of the page (default value). Optionally combined with argument: name.
			- 'active' : active windows of the page.
			- 'enabled' : enabled windows of the page.

		name : str, optional
			Name of the window. If set, the method will return only windows that matches the name (pattern is also accepted). This argument is used only when the specifier is 'all'.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Window. Upon failure, an empty list is returned

		"""


	def get_images(self, specifier: str) -> object:

		"""

		This method gets the images of the page.


		Parameters
		----------
		specifier : str, optional
			The specifier of the method. Its possible values are:
			- 'all' : all images (default value).
			- 'visible' : visible images.
			- 'selected' : selected images.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Image. Upon failure, an empty list is returned

		"""


	def get_videos(self, specifier: str) -> object:

		"""

		This method gets the videos of the page.


		Parameters
		----------
		specifier : str, optional
			The specifier of the method. Its possible values are:
			- 'all' : all videos (default value).
			- 'visible' : visible videos.
			- 'selected' : selected videos.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Video. Upon failure, an empty list is returned

		"""


	def get_annotations(self, specifier: str, id: int) -> object:

		"""

		This method gets the annotations of the page.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all annotations of the page (default value). Optionally combined with argument: id.
			- 'visible' : visible annotations of the page.
			- 'selected' : selected annotations of the page.
			- 'visible_on_screen' : visible on screen annotations of the page.
			- 'hidden_on_screen' : hidden on screen annotations of the page.

		id : int, optional
			If this argument is set, the method will return the annotation with the specific id. This argument is used only when the specifier is 'all'.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Annotataion. Upon failure, an empty list is returned

		"""


	def get_annotation_groups(self, name: str) -> object:

		"""

		This method gets the annotation groups of the page.


		Parameters
		----------
		name : str, optional
			If this argument is set, the method will return only the annotation groups that matches the given name. The given name can be a pattern. If absent, all annotation groups of the page will be returned.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class AnnotationGroup. Upon failure, an empty list is returned

		"""


	def get_plots(self, specifier: str, plot_type: str) -> object:

		"""

		This method gets the plots of the page.


		Parameters
		----------
		specifier : str, optional
			The specifier of the method. Its possible values are:
			- 'all' : all the plots of the page (default value).
			- 'visible' : visible plots of the page. Optionally combined with argument: plot_type.
			- 'active' : active plots of the page. Optionally combined with argument: plot_type.

		plot_type : str, optional
			The type of the plot. If set, the method will return only plots of the specified type. Possible values are:
			- 'plain'
			- 'realimag'
			- 'magphase'
			- 'polar'
			- 'dna'
			- 'mac'
			- 'horizontal'
			- 'colormap'
			- '3dmac'
			- 'waterfall'
			- 'nyquist'
			Used when the specifier is 'visible', 'active'.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Plot. Upon failure, an empty list is returned

		"""


	def get_curve_groups(self) -> object:

		"""

		This method gets the curve groups of the page.


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class CurveGroup. Upon failure, an empty list is returned

		"""


	def get_plot_axes(self, specifier: str, plot_axis_type: str, plot_axis_id: int) -> object:

		"""

		This method gets the plot axes of the page.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all plot axes of the page (default value).
			- 'visible' : visible plot axes of the page.
			- 'active' : active plot axes of the page.

		plot_axis_type : str, optional
			Type of the axis. Its possible values are:
			- 'xaxis': X axis
			- 'yaxis': Y axis
			- 'zaxis': Z axis
			- 'caxis': Y complex axis

		plot_axis_id : int, optional
			Id of the axis.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class PlotAxis. Upon failure, an empty list is returned

		"""


	def get_curves(self, specifier: str) -> object:

		"""

		This method gets the curves of the page.


		Parameters
		----------
		specifier : str, optional
			Specifier of the method. Its possible values are:
			- 'all' : all selected curves of the page (default value).
			- 'visible' : selected curves of the page.
			- 'selected' : selected curves of the page.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Curve. Upon failure, an empty list is returned

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the page.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the attribute of the page.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. Its possible values are:
			-'string': String
			-'numerical': Number

		attribute_value : object
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def activate(self) -> bool:

		"""

		This method activates the page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the page.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def pick_annotations(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick annotations from all the existing windows. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.


		Parameters
		----------
		message : str
			Argument "message" refers to the message which will be shown in the screen when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Annotation. Upon failure, an empty list is returned.

		"""


	def set_nodes_on_annotations(self, annotations: object, values: object) -> bool:

		"""

		This method sets the pointers of some annotations on some nodes.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Node.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_parts_on_annotations(self, annotations: object, values: object, pointers: object) -> object:

		"""

		This method sets the pointers of some annotations on some parts.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Part

		pointers : object, optional
			List with positions of the pointer on the parts. Optional entries of pointer positions refer to the entity of the part to which the annotation will point. Its possible values are:
			- 'dispxmin': Node with minimum X deformation
			- 'dispxmax': Node with maximum X deformation
			- 'dispymin': Node with minimum Y deformation
			- 'dispymax': Node with maximum Y deformation
			- 'dispzmin': Node with minimum Z deformation
			- 'dispzmax': Node with maximum Z deformation
			- 'disptotmin': Node with minumum total deformation
			- 'disptotmax': Node with maximum total deformation
			- 'nodalmin': Node with minumum nodal value
			- 'nodalmax': Node with maximum nodal value
			- 'centrmin': Element with minimum centroid value
			- 'centrmax': Element with maximum centroid value
			- 'cornermin': Element with minimum corner value
			- 'cornermax': Element with maximum corner value
			If they are absent, then annotation will point to the center of the part.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_materials_on_annotations(self, annotations: object, values: object, pointers: object) -> object:

		"""

		This method sets the pointers of some annotations on some materials.


		Parameters
		----------
		annotations : object
			List with objects of Class annotation.

		values : object
			List with objects of class Material.

		pointers : object, optional
			List with positions of the pointer on the materials. Pointer position refers to the entity of the group to which the annotation will point. Its possible values are:
			- 'dispxmin': Node with minimum X deformation
			- 'dispxmax': Node with maximum X deformation
			- 'dispymin': Node with minimum Y deformation
			- 'dispymax': Node with maximum Y deformation
			- 'dispzmin': Node with minimum Z deformation
			- 'dispzmax': Node with maximum Z deformation
			- 'disptotmin': Node with minumum total deformation
			- 'disptotmax': Node with maximum total deformation
			- 'nodalmin': Node with minumum nodal value
			- 'nodalmax': Node with maximum nodal value
			- 'centrmin': Element with minimum centroid value
			- 'centrmax': Element with maximum centroid value
			- 'cornermin': Element with minimum corner value
			- 'cornermax': Element with maximum corner value
			If this is absent, then annotation will point to the center of the material.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_groups_on_annotations(self, annotations: object, values: object, pointers: object) -> object:

		"""

		This method sets the pointers of some annotations on some groups.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Group.

		pointers : object, optional
			List with optional positions of the pointers on the group that refer to the entity of the group to which the annotation will point. Their possible values are:
			- 'dispxmin': Node with minimum X deformation
			- 'dispxmax': Node with maximum X deformation
			- 'dispymin': Node with minimum Y deformation
			- 'dispymax': Node with maximum Y deformation
			- 'dispzmin': Node with minimum Z deformation
			- 'dispzmax': Node with maximum Z deformation
			- 'disptotmin': Node with minumum total deformation
			- 'disptotmax': Node with maximum total deformation
			- 'nodalmin': Node with minumum nodal value
			- 'nodalmax': Node with maximum nodal value
			- 'elemmin': Element with minimum centroid value
			- 'elemmax': Element with maximum centroid value
			- 'cornermin': Element with minimum corner value
			- 'cornermax': Element with maximum corner value
			If its value is absent, then annotation will refer to the whole group.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_2d_positions_on_annotations(self, annotations: object, values: object) -> object:

		"""

		This method sets the pointers of some annotations at some positions on the screen plane. Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with the coordinates of the 2d position (X, Y).

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_3d_positions_on_annotations(self, annotations: object, values: object) -> object:

		"""

		This method sets the pointers of some annotations at 3D positions in space.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with the coordinates of the 3d position (X, Y, Z).

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_curves_on_annotations(self, annotations: object, values: object, points: object) -> object:

		"""

		This method sets the pointers of some annotations on some curves.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Curve.

		points : object, optional
			List with integers, representing point ids.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_elements_on_annotations(self, annotations: object, values: object) -> object:

		"""

		This method sets the pointers of some annotations on some elements.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Element

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_boundaries_on_annotations(self, annotations: object, values: object) -> object:

		"""

		This method sets the pointers of some annotations on some boundaries.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Boundary.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_planes_on_annotations(self, annotations: object, values: object, pointers: object) -> object:

		"""

		This method sets the pointers of some annotations on some planes.


		Parameters
		----------
		annotations : object
			List with objects of class Aannotation.

		values : object
			List with objects of class Plane.

		pointers : object, optional
			List of the pointer positions. Optional pointer position entries refer to the entity of the plane to which the annotation will point. Their possible values are:
			- 'dispxmin': Node with minimum X deformation
			- 'dispxmax': Node with maximum X deformation
			- 'dispymin': Node with minimum Y deformation
			- 'dispymax': Node with maximum Y deformation
			- 'dispzmin': Node with minimum Z deformation
			- 'dispzmax': Node with maximum Z deformation
			- 'disptotmin': Node with minumum total deformation
			- 'disptotmax': Node with maximum total deformation
			- 'nodalmin': Node with minumum nodal value
			- 'nodalmax': Node with maximum nodal value
			- 'elemmin': Element with minimum centroid value
			- 'elemmax': Element with maximum centroid value
			- 'cornermin': Element with minimum corner value
			- 'cornermax': Element with maximum corner value
			If they are absent, then annotation will refer to the whole plane.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_windows_on_annotations(self, annotations: object, values: object) -> object:

		"""

		This method sets the pointers of some annotations on some windows.


		Parameters
		----------
		annotations : object
			List with objects of class Annotation.

		values : object
			List with objects of class Window.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def pick_windows(self, message: str, settings: object) -> object:

		"""

		This method allows the user to pick windows from the page. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.


		Parameters
		----------
		message : str
			Argument "message" refers to the message which will be shown in the screen when the function is called.

		settings : object, optional
			Argument 'settings' is a dictionary with the pairs of settings for the pick action. 
			The accepted pair is:
			
			- 'one_pick', boolean : controls if the script will wait for middle click to continue.
			
			The setting is False by default.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Window. Upon failure, an empty list is returned.

		"""


	def save_image(self, file: str, format: str, size: str, orientation: str, background: str) -> object:

		"""

		This method allows the user to save the workspace of the page as an image.Works only for active Page.


		Parameters
		----------
		file : str
			The filename of the image.

		format : str, optional
			The format of the file. Accepted values are:
			- 'png'
			- 'jpeg'
			- 'gif'
			- 'bmp'
			- 'eps'
			- 'ppm'
			- 'rgb'
			- 'tiff'
			Default value is 'png'.

		size : str, optional
			The size of the image. Accepted values are:
			- any tuple of two integers as (width, height)
			- 'current_size'
			- 'A0'
			- 'A1'
			- 'A2'
			- 'A3'
			- 'A4'
			- 'A5'
			- 'Letter'
			- 'Legal'
			- 'Executive'
			- 'Tabloid'
			- 'PAL(720x576)'
			- 'NTSC(720x480'
			- strings in 'widthxheight' format.
			The default value is 'current_size'.

		orientation : str, optional
			The orientation of the image. Accepted values are:
			- portrait
			- landscape

		background : str, optional
			The color of the image background. Accepted values are:
			- transparent : transparent backgrount
			- window_color : the color of the window.
			- Color name (e.g. 'White').
			Default value is 'White'

		Returns
		-------
		object
			Returns None.

		"""


	def save_video(self, file: str, format: str, size: str, orientation: str, background: str, loop_direction: str, loops: int) -> object:

		"""

		This method allows the user to save the workspace of the page as a video. Works only for active Page.


		Parameters
		----------
		file : str
			The filename of the video.

		format : str, optional
			The format of the file. Accepted values are:
			- 'avi'
			- 'mpeg2'
			- 'mpeg4'
			- 'gif'
			Default value is 'mpeg4'.

		size : str, optional
			The size of the image. Accepted values are:
			- any tuple of two integers as (width, height)
			- 'current_size'
			- 'A0'
			- 'A1'
			- 'A2'
			- 'A3'
			- 'A4'
			- 'A5'
			- 'Letter'
			- 'Legal'
			- 'Executive'
			- 'Tabloid'
			- 'PAL(720x576)'
			- 'NTSC(720x480'
			- strings in 'widthxheight' format.
			The default value is 'current_size'.

		orientation : str, optional
			The orientation of the image. Accepted values are:
			- portrait
			- landscape

		background : str, optional
			The color of the image background. Accepted values are:
			- transparent : transparent backgrount
			- window_color : the color of the window.
			- Color name (e.g. 'White').
			Default value is 'White'

		loop_direction : str, optional
			The direction of the states loop. Accepted values are:
			- 'forward'
			- 'backward'
			- 'forward_and_backward'
			Default value is 'forward'.

		loops : int, optional
			The number of the loops of the video. Default value is 1.

		Returns
		-------
		object
			Returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Page entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	def delete_annotations(self, annotations: object) -> object:

		"""

		This methods deletes annotations.


		Parameters
		----------
		annotations : object
			The annotations that are going to be deleted.
			Acceptable values are:
			- 'all' : deletes all the annotations.
			- 'visible' : deletes the visible annotations.
			- 'selected' : deletes the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""


	def show_annotations(self, annotations: object) -> object:

		"""

		This method shows annotations.


		Parameters
		----------
		annotations : object
			The annotations that are going to be shown.
			Acceptable values are:
			- 'all' : shows all the annotations.
			- 'selected' : shows the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""


	def hide_annotations(self, annotations: object) -> object:

		"""

		This method hides annotations.


		Parameters
		----------
		annotations : object
			The annotations that are going to be hidden.
			Acceptable values are:
			- 'all' : hides all the annotations.
			- 'visible' hides the visible annotations.
			- 'selected' : hides the selected annotations.
			- range of annotation ids.
			- a list of annotations.

		Returns
		-------
		object
			This method returns None.

		"""

