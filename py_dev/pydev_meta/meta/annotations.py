from __future__ import annotations
from typing import *

def AnnotationById(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function finds the annotation with a given id (annotation_id).

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation with the given id.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    a = annotations.AnnotationById(annotation_id)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def AnnotationGroups() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotation_groups` instead.


	This function collects all annotation groups of all windows.

	Returns
	-------
	object
		It returns a list wwhere each member of the list is an object of class AnnotationGroup referring to one specific annotation group of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_groups = annotations.AnnotationGroups()
		    for ag in annotation_groups:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotation_groups instead.", DeprecationWarning)

def AnnotationGroupsByName(group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotation_groups` instead.


	This function finds annotation groups with a given name (group_name).

	Parameters
	----------
	group_name : str
		Name of the group. Wildcards can also be used ("*", "?", "[...]").

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class AnnotationGroup referring to one specific annotation group with the given name.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    group_name = "AnnoGroup"
		    annotation_groups = annotations.AnnotationGroupsByName(group_name)
		    for ag in annotation_groups:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotation_groups instead.", DeprecationWarning)

def AnnotationGroupsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotation_groups` instead.


	This function collects all annotation groups of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class AnnotationGroup referring to one specific annotation group of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "Window1"
		    annotation_groups = annotations.AnnotationGroupsOfWindow(window_name)
		    for ag in annotation_groups:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotation_groups instead.", DeprecationWarning)

def Annotations() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function collects all annotations of all existing windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific annotation of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def AnnotationsListToDict(annotations: object) -> object:

	"""

	This function constructs a dictionary from a given list with objects of class Annotation.

	Parameters
	----------
	annotations : object
		List with objects of class Annotation.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the annotation and member is the corresponding annotation object.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON object
		import meta
		from meta import annotations
		
		
		def main():
		    all_annotations = annotations.Annotations()
		
		    dict_annots = annotations.AnnotationsListToDict(all_annotations)
		    for annot_id, a in dict_annots.items():
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def AnnotationsOfGroup(group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.AnnotationGroup.get_annotations` instead.


	This function searches for the annotations of a group with a given name in the list of the annotation groups.

	Parameters
	----------
	group_name : str
		Name of the annotation group.

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is an object of class Annotation referring to one specific annotation of the given group.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    group_name = "AnnoGroup"
		    group_annotations = annotations.AnnotationsOfGroup(group_name)
		    for a in group_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.AnnotationGroup.get_annotations instead.", DeprecationWarning)

def AnnotationsOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_annotations` instead.


	This function searches for the annotations of an overlay run.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run.

	overlay_run_type : str
		Type of the overlay run:
		- 'session'
		- 'project'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one annotation of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		
		    overlay_run_annotations = annotations.AnnotationsOfOverlayRun(
		        overlay_run_type, overlay_run_id
		    )
		    for a in overlay_run_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_annotations instead.", DeprecationWarning)

def AnnotationsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotations` instead.


	This function collects all annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific annotation of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "Window1"
		    window_annotations = annotations.AnnotationsOfWindow(window_name)
		    for a in window_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotations instead.", DeprecationWarning)

def BackgroundColorOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_background_color` instead.


	This function finds background color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a color object with the background color of the corresponding annotation.
		Else, a non valid color object is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    col = annotations.BackgroundColorOfAnnotation(annotation_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_background_color instead.", DeprecationWarning)

def BorderColorOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_border_color` instead.


	This function finds border color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a color object with the border color of the corresponding annotation.
		Else, a non valid color object is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    col = annotations.BorderColorOfAnnotation(annotation_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_border_color instead.", DeprecationWarning)

def CollectNewAnnotationsEnd() -> object:

	"""

	This function ends recording the creation of new annotations. This function should be preceded by a corresponding call to script function CollectNewAnnotationsStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific newly created annotation.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import utils
		
		
		def main():
		    annotations.CollectNewAnnotationsStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 201 "Empty Annotation"')
		    utils.MetaCommand('annotation add 202 "Empty Annotation"')
		
		    new_annotations = annotations.CollectNewAnnotationsEnd()
		    for a in new_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewAnnotationsStart() -> int:

	"""

	This function starts recording the creation of new annotations. This function should be followed by a corresponding call to script function CollectNewAnnotationsEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import utils
		
		
		def main():
		    annotations.CollectNewAnnotationsStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 201 "Empty Annotation"')
		    utils.MetaCommand('annotation add 202 "Empty Annotation"')
		
		    new_annotations = annotations.CollectNewAnnotationsEnd()
		    for a in new_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateEmptyAnnotation(window_name: str, annotation_text: str, annotation_id: int) -> object:

	"""

	This function creates an annotation on an existing 3D window.

	Parameters
	----------
	window_name : str
		Name of the window.

	annotation_text : str, optional
		Text of the annotation.

	annotation_id : int, optional
		Id of the annotation. If there is an annotation with the given id then this function will fail. If optional argument "annotation_id" is absent then an id will be chosen from the function.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the newly created annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "Window1"
		    annotation_text = "100th Annotation"
		    annotation_id = 100
		    a = annotations.CreateEmptyAnnotation(window_name, annotation_text, annotation_id)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateEmptyAnnotationOnPlot(window_name: str, plot_id: int, annotation_text: str, annotation_id: int) -> object:

	"""

	This function creates an annotation on an specified plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	annotation_text : str
		Text of the annotation.

	annotation_id : int, optional
		Id of the annotation. If there is an annotation with the given id then this function will fail. If optional argument "annotation_id" is absent then an id will be chosen from the function.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the newly created annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    text = "Annotation on plot"
		    annotation_id = 5
		    a = annotations.CreateEmptyAnnotationOnPlot(
		        window_name, plot_id, text, annotation_id
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateSomeEmptyAnnotations(window_names: object, annotation_texts: object, annotation_ids: object) -> object:

	"""

	This function creates some empty annotations on some existing 3D windows specified by their names.

	Parameters
	----------
	window_names : object
		List with names of the windows.

	annotation_texts : object
		List with texts of the annotations.

	annotation_ids : object, optional
		List with ids of the annotations. If there is an annotation with the given id then this function will fail. If argument "annotation_id" is absent then an id will be chosen from the function.

	Returns
	-------
	object
		Upon success, it returns a list with objects of class Annotation referring to the newly created annotations.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_window_name = list()
		    list_text = list()
		    list_annotation_id = list()
		
		    for i in range(100, 110, 2):
		        list_window_name.append("MetaPost")
		        list_text.append("annot_" + str(i))
		        list_annotation_id.append(i + 1)
		    print(list_window_name)
		    print(list_text)
		    print(list_annotation_id)
		
		    new_annotations = annotations.CreateSomeEmptyAnnotations(
		        list_window_name, list_text, list_annotation_id
		    )
		    for a in new_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateSomeEmptyAnnotationsOnPlot(window_names: object, plot_ids: object, annotation_texts: object, annotation_ids: object) -> object:

	"""

	This function creates some empty annotations on some existing plot2d windows.

	Parameters
	----------
	window_names : object
		List with names of the windows.

	plot_ids : object
		List with ids of the plots.

	annotation_texts : object
		List with texts of the annotations.

	annotation_ids : object, optional
		List with ids of the annotations. If argument "annotation_id" is absent then an id will be chosen from the function.

	Returns
	-------
	object
		Upon success, it returns a list with objects of class Annotation referring to the newly created annotations.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_window_name = list()
		    list_plot_id = list()
		    list_text = list()
		    list_annotation_id = list()
		
		    for i in range(100, 110, 1):
		        list_window_name.append("Window1")
		        list_plot_id.append(0)
		        list_text.append("annot" + str(i))
		        list_annotation_id.append(i + 1)
		    print(list_window_name)
		    print(list_plot_id)
		    print(list_text)
		    print(list_annotation_id)
		
		    new_annotations = annotations.CreateSomeEmptyAnnotationsOnPlot(
		        list_window_name, list_plot_id, list_text, list_annotation_id
		    )
		    for a in new_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteAnnotation(annotation_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.delete` instead.


	This function deletes an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 8
		    ret = annotations.DeleteAnnotation(annotation_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.delete instead.", DeprecationWarning)

def DeselectAnnotation(annotation_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.deselect` instead.


	This function deselects an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 8
		    ret = annotations.DeselectAnnotation(annotation_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.deselect instead.", DeprecationWarning)

def HiddenOnScreenAnnotations() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function collects hidden on screen annotations of all existing windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific hidden on screen annotation of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    hidden_annotations = annotations.HiddenOnScreenAnnotations()
		    for a in hidden_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def HiddenOnScreenAnnotationsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotations` instead.


	This function collects hidden on screen annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific hidden on screen annotation of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "MetaPost"
		    hidden_annotations = annotations.HiddenOnScreenAnnotationsOfWindow(window_name)
		    for a in hidden_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotations instead.", DeprecationWarning)

def HideAnnotation(annotation_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.hide` instead.


	This function hides an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Annotation Id.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    ret = annotations.HideAnnotation(annotation_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.hide instead.", DeprecationWarning)

def IsAnnotation(annotation: object) -> int:

	"""

	This function checks whether an object is of class Annotation.

	Parameters
	----------
	annotation : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class Annotation, or 0 if object is not of class Annotation.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    all_entities = annotations.Annotations()
		
		    for ent in all_entities:
		        if annotations.IsAnnotation(ent):
		            a = ent
		            print("This is an object of class Annotation")
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsAnnotationGroup(annotation_group: object) -> int:

	"""

	This function checks whether a struct is of type AnnotationGroup.

	Parameters
	----------
	annotation_group : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if object is of class AnnotationGroup, 0 otherwise.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    all_entities = annotations.AnnotationGroups()
		
		    for ent in all_entities:
		        if annotations.IsAnnotationGroup(ent):
		            ag = ent
		            print("This is an object of class AnnotationGroup")
		            print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PickAnnotations(message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.pick_annotations` instead.


	This function allows the user to pick annotations from all the existing windows. The execution of the script will stop and it will restart when the middle mouse button or Enter is pressed.

	Parameters
	----------
	message : str
		Argument "message" refers to the message which will be shown in the screen when the fuction is called.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific picked annotation.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    message = "Select Annotations and press Enter when you are ready"
		    picked_annotations = annotations.PickAnnotations(message)
		    for a in picked_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.pick_annotations instead.", DeprecationWarning)

def PointerColorOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_pointer_color` instead.


	This function finds pointer color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a color object with the pointer color of the corresponding annotation.
		Else, a non valid color object is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    col = annotations.PointerColorOfAnnotation(annotation_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_pointer_color instead.", DeprecationWarning)

def PositionOfAnnotationPointerEnd(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_end_pointer_position` instead.


	This function finds the position of the end of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list whose first member is the position of the end of the pointer of a given annotation in the x-axis of the screen plane and second member is for the y-axis, respectively.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    position = annotations.PositionOfAnnotationPointerEnd(annotation_id)
		    if len(position) == 2:
		        xpos = position[0]
		        print(xpos)
		        ypos = position[1]
		        print(ypos)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_end_pointer_position instead.", DeprecationWarning)

def PositionOfAnnotationPointerStart(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_start_pointer_position` instead.


	This function finds the position of the start of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list whose first member is the position of the start of the pointer of a given annotation in the x-axis of the screen plane and second member is the position in the y-axis, respectively.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    position = annotations.PositionOfAnnotationPointerStart(annotation_id)
		    if len(position) == 2:
		        xpos = position[0]
		        print(xpos)
		        ypos = position[1]
		        print(ypos)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_start_pointer_position instead.", DeprecationWarning)

def ReportNewAnnotations() -> object:

	"""

	This function collects the newly created annotations from the last call of script function CollectNewAnnotationsStart(). This function should be preceded by a corresponding call to script function CollectNewAnnotationsStart() and should be followed by a corresponding call to script function CollectNewAnnotationsEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific newly created annotation.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import utils
		
		
		def main():
		    annotations.CollectNewAnnotationsStart()
		
		    # create new annotations
		    utils.MetaCommand('annotation add 201 "Empty Annotation"')
		    utils.MetaCommand('annotation add 202 "Empty Annotation"')
		
		    new_annotations = annotations.ReportNewAnnotations()
		    for a in new_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		    annotations.CollectNewAnnotationsEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectAnnotation(annotation_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.select` instead.


	This function selects an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    ret = annotations.SelectAnnotation(annotation_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.select instead.", DeprecationWarning)

def SelectedAnnotations() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function collects selected annotations of all existing windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific selected annotation of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    selected_annotations = annotations.SelectedAnnotations()
		    for a in selected_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def SelectedAnnotationsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotations` instead.


	This function collects selected annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific selected annotation of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "MetaPost"
		
		    selected_annotations = annotations.SelectedAnnotationsOfWindow(window_name)
		    for a in selected_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotations instead.", DeprecationWarning)

def SetAnnotationPointerOn2D(x_pos: float, y_pos: float, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_2d_position` instead.


	This function sets the pointer of an annotation specified at a position on the screen plane. Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).

	Parameters
	----------
	x_pos : float
		Position in the x-axis of the screen plane in the range [0-1].

	y_pos : float
		Position in the y-axis of the screen plane in the range [0-1].

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    x_pos = 0.2
		    y_pos = 0.8
		
		    a = annotations.SetAnnotationPointerOn2D(annotation_id, x_pos, y_pos)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_2d_position instead.", DeprecationWarning)

def SetAnnotationPointerOn3D(annotation_id: int, x_coord: float, y_coord: float, z_coord: float) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_3d_position` instead.


	This function sets the pointer of an annotation at a position in space.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	x_coord : float
		X coordinate.

	y_coord : float
		Y coordinate.

	z_coord : float
		Z coordinate.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 3
		    x_coord = 0.998
		    y_coord = 1.252
		    z_coord = 1.352
		
		    a = annotations.SetAnnotationPointerOn3D(annotation_id, x_coord, y_coord, z_coord)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_3d_position instead.", DeprecationWarning)

def SetAnnotationPointerOnBoundary(boundary_id: int, boundary_type: int, model_id: int, second_id: int, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_boundary` instead.


	This function sets the pointer of an annotation on a boundary element. Boundary elements have a second id which is a number greater than or equal to zero.

	Parameters
	----------
	boundary_id : int
		Id of the boundary element.

	boundary_type : int
		Type of the boundary element (META constant).

	model_id : int
		Id of the model of the element.

	second_id : int
		Second id of the boundary element.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    model_id = 0
		    annotation_id = 1
		    boundary_type = constants.PLOAD4
		    boundary_id = 1
		    second_id = 0
		
		    a = annotations.SetAnnotationPointerOnBoundary(
		        annotation_id, model_id, boundary_type, boundary_id, second_id
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_boundary instead.", DeprecationWarning)

def SetAnnotationPointerOnCurve(curve_id: int, point_id: int, window_name: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_curve` instead.


	This function sets the pointer of an annotation on a curve of a given plot2d window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	point_id : int, optional
		Id of the point of the curve.

	window_name : str
		Name of the window.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    window_name = "Window1"
		    curve_id = 9
		    point_id = 23
		
		    a = annotations.SetAnnotationPointerOnCurve(
		        annotation_id, window_name, curve_id, point_id
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_curve instead.", DeprecationWarning)

def SetAnnotationPointerOnElement(element_id: int, element_type, model_id: int, second_id: int, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_element` instead.


	This function sets the pointer of an annotation on an element.

	Parameters
	----------
	element_id : int
		Id of the element.

	element_type : 
		Type of the element (META constant).

	model_id : int
		Id of the model of the element.

	second_id : int
		Second id of the element. Some elements may have a second id (GAP, TUBE, JOINT). For the rest types of elements, the value of second_id is -1.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation, elements.Element, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    annotation_id = 1
		    model_id = 0
		    element_type = constants.SOLID
		    element_id = 16929
		    second_id = -1
		
		    a = annotations.SetAnnotationPointerOnElement(
		        annotation_id, model_id, element_type, element_id, second_id
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_element instead.", DeprecationWarning)

def SetAnnotationPointerOnGroup(group_name: str, model_id: int, pointer_position: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_group` instead.


	This function sets the pointer of an annotation on a group.

	Parameters
	----------
	group_name : str
		Name of the group.

	model_id : int
		Id of the model of the node.

	pointer_position : str, optional
		Optional argument 'pointer_position' refers to the entity of the group to which the annotation will point. Its possible values are:
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
		If optional argument 'pointer_position' is absent, then annotation will refer to the whole group.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 5
		    model_id = 0
		    group_name = "My_Group"
		    pointer_position = "disptotmax"
		
		    a = annotations.SetAnnotationPointerOnGroup(
		        annotation_id, model_id, group_name, pointer_position
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_group instead.", DeprecationWarning)

def SetAnnotationPointerOnGroupInstance(group_instance: int, group_name: str, model_id: int, pointer_position: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_group` instead.


	This function sets the pointer of an annotation on a group instance.

	Parameters
	----------
	group_instance : int
		Instance of the group.

	group_name : str
		Name of the group.

	model_id : int
		Id of the model of the group.

	pointer_position : str, optional
		Optional argument 'pointer_position' refers to the entity of the group to which the annotation will point. Its possible values are:
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
		If optional argument 'pointer_position' is absent, then annotation will refer to the whole group.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    model_id = 0
		    group_name = "pano"
		    group_instance = 1
		    pointer_position = "disptotmax"
		
		    a = annotations.SetAnnotationPointerOnGroupInstance(
		        annotation_id, model_id, group_name, group_instance, pointer_position
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_group instead.", DeprecationWarning)

def SetAnnotationPointerOnMaterial(material_id: int, material_type, model_id: int, pointer_position: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_material` instead.


	This function sets the pointer of an annotation on a material.

	Parameters
	----------
	material_id : int
		Id of the material.

	material_type : 
		Type of the material (META keyword).

	model_id : int
		Id of the model of the material.

	pointer_position : str, optional
		Optional argument 'pointer_position' refers to the entity of the material to which the annotation will point. Its possible values are:
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
		If optional argument 'pointer_position' is absent, then annotation will point to the center of the material.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.
		A description of class Annotation can be found as "Annotation" under library category "annotations".

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    annotation_id = 1
		    model_id = 0
		    material_type = constants.MAT1
		    material_id = 1
		    pointer_position = "centrmax"
		
		    a = annotations.SetAnnotationPointerOnMaterial(
		        annotation_id, model_id, material_type, material_id, pointer_position
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_material instead.", DeprecationWarning)

def SetAnnotationPointerOnNode(model_id: int, node_id: int, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_node` instead.


	This function sets the pointer of an annotation on a node.

	Parameters
	----------
	model_id : int
		Id of the model of the node.

	node_id : int
		Id of the node.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 11
		    model_id = 0
		    node_id = 17211
		
		    a = annotations.SetAnnotationPointerOnNode(annotation_id, model_id, node_id)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_node instead.", DeprecationWarning)

def SetAnnotationPointerOnPart(model_id: int, part_id: int, part_type, pointer_position: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_part` instead.


	This function sets the pointer of an annotation on a part.

	Parameters
	----------
	model_id : int
		Id of the model of the part.

	part_id : int
		Id of the part.

	part_type : 
		Type of the part (META constant).

	pointer_position : str, optional
		Optional argument 'pointer_position' refers to the entity of the part to which the annotation will point. Its possible values are:
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
		If optional argument 'pointer_position' is absent, then annotation will point at a random node of the part.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    annotation_id = 1
		    model_id = 0
		    part_type = constants.PSOLID
		    part_id = 2
		    pointer_position = "centrmax"
		
		    a = annotations.SetAnnotationPointerOnPart(
		        annotation_id, model_id, part_type, part_id, pointer_position
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_part instead.", DeprecationWarning)

def SetAnnotationPointerOnPlane(plane_name: str, pointer_postion: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_plane` instead.


	This function sets the pointer of an annotation at an existing plane.

	Parameters
	----------
	plane_name : str
		Name of the plane.

	pointer_postion : str
		Optional argument 'pointer_position' refers to the entity of the plane to which the annotation will point. Its possible values are:
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
		If optional argument 'pointer_position' is absent, then annotation will refer to the whole plane.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 4
		    plane_name = "DEFAULT_PLANE_YZ"
		    pointer_position = "elemmax"
		
		    a = annotations.SetAnnotationPointerOnPlane(
		        annotation_id, plane_name, pointer_position
		    )
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_plane instead.", DeprecationWarning)

def SetAnnotationPointerOnWindow(window_name: str, annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_pointer_window` instead.


	This function sets the pointer of an annotation at an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, a non valid Annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    window_name = "Window1"
		
		    a = annotations.SetAnnotationPointerOnWindow(annotation_id, window_name)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_pointer_window instead.", DeprecationWarning)

def SetBackgroundColorOfAnnotation(annotation_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_background_color` instead.


	This function sets background color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	red : int
		Red color value.

	green : int
		Green color value.

	blue : int
		Blue color value.

	alpha : int
		Alpha channel value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = annotations.SetBackgroundColorOfAnnotation(
		        annotation_id, red, green, blue, alpha
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_background_color instead.", DeprecationWarning)

def SetBorderColorOfAnnotation(annotation_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_border_color` instead.


	This function sets border color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	red : int
		Red color value.

	green : int
		Green color value.

	blue : int
		Blue color value.

	alpha : int
		Alpha channel value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = annotations.SetBorderColorOfAnnotation(annotation_id, red, green, blue, alpha)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_border_color instead.", DeprecationWarning)

def SetPointerColorOfAnnotation(annotation_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_pointer_color` instead.


	This function sets pointer color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	red : int
		Red color value.

	green : int
		Green color value.

	blue : int
		Blue color value.

	alpha : int
		Alpha channel value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    red = 255
		    green = 0
		    blue = 0
		    alpha = 255
		    ret = annotations.SetPointerColorOfAnnotation(
		        annotation_id, red, green, blue, alpha
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_pointer_color instead.", DeprecationWarning)

def SetSettingsOfAllAnnotations(window_name: str, annotation_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_annotations_settings` instead.


	This function controls settings of all annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	annotation_settings : object
		Argument 'annotation_settings' is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. 'options_width,6').
		The names of the annotation settings and its possible values are:
		- 'anchor_none': Anchor none
		- 'anchor_pointer': Anchor relative to pointer (float value,float value)
		- 'anchor_scrbotleft': Anchor relative to bottom left of screen (float value,float value)
		- 'anchor_scrbotright': Anchor relative to bottom right of screen (float value,float value)
		- 'anchor_scrtopright': Anchor relative to top right pointer (float value,float value)
		- 'anchor_scrtopleft': Anchor relative to top left pointer (float value,float value)
		- 'background_auto_color': Background automatic color
		- 'background_color': Background color (string value)
		- 'background_function_color': Function used for coloring ("default", "funcval",
		- 'scalfuncval", "vecfuncval", "cmax', "cmin", "dispx", "dispy", "dispz", "disptot")
		- 'background_expression_color': Expression or annotation variable used for coloring (string value)
		- 'background_transparency': Background transparency (float value)
		- 'border_color': Border color (string value)
		- 'border_color_pident': Border pid/curve color (0,1)
		- 'border_padding': Border padding (float value)
		- 'border_width': Border width (float value)
		- 'border_rounded': Style of border corners (0,1)
		- 'hide_shadowed': Hide Shadowed Option (0,1)
		- 'line_color': Line color (string value)
		- 'line_width': Line width (float value)
		- 'model_visibility': Model dependent visibility (0,1)
		- 'planecut_height': Plane cut height (integer value)
		- 'planecut_width': Plane cut width (integer value)
		- 'planecut_rotate': Rotate plane cut (float value)
		- 'planecut_draw': Draw plane cur (0,1)
		- 'pointer_color': Pointer color (string value)
		- 'pointer_color_pident': Pointer pid/curve color (0,1)
		- 'pointer_size': Pointer size (float value)
		- 'pointer_style': Pointer style ('arrow', 'box', 'circle', 'cross', 'none', 'x')
		- 'pointer_visibility': Show pointer (0,1)
		- 'position_xy': Position (float value, float value)
		- 'size': Size (integer value)
		- 'text_align': Text alignment ('center', 'left', 'right')
		- 'text_color': Text color (string value)
		- 'text_color_pident': Text pid/curve color (0,1)
		- 'title_color': Title color (string value)
		- 'title_color_pident': Title pid/curve color
		- 'title_font': Title font (string value)
		- 'title_format': Title format ('auto', 'fixed', 'scientific')
		- 'title_htmltext': Title html text (string value)
		- 'title_precision': Title precision digits (integer value)
		- 'title_text': Title text
		- 'title_vertical': Draw vertical text (0,1)
		- 'title_visibility': Title visibility ('auto', 'on', 'off')
		- 'circular': Circular shape (0,1)
		- 'circular_size': Circular Shape Size (integer value)
		- 'circular_multiplier': Circular Shape Size Multiplier (integer value)
		- 'circular_initial': Limit to initial (0,1)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "MetaPost"
		    annotation_settings = list()
		    annotation_settings.append("border_color,yellow")
		    annotation_settings.append("text_color,blue")
		    ret = annotations.SetSettingsOfAllAnnotations(window_name, annotation_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_annotations_settings instead.", DeprecationWarning)

def SetSettingsOfAnnotation(annotation_id: int, annotation_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_settings` instead.


	This function controls settings of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	annotation_settings : object
		Argument 'annotation_settings' is a list which contains strings as elements with the name and value of each setting separated by comma (e.g. 'options_width,6').
		The names of the annotation settings and its possible values are:
		- 'anchor_none': Anchor none
		- 'anchor_pointer': Anchor relative to pointer (float value,float value)
		- 'anchor_scrbotleft': Anchor relative to bottom left of screen (float value,float value)
		- 'anchor_scrbotright': Anchor relative to bottom right of screen (float value,float value)
		- 'anchor_scrtopright': Anchor relative to top right pointer (float value,float value)
		- 'anchor_scrtopleft': Anchor relative to top left pointer (float value,float value)
		- 'background_auto_color': Background automatic color
		- 'background_color': Background color (string value)
		- 'background_function_color': Function used for coloring ('default', 'funcval', 'scalfuncval', 'vecfuncval', 'cmax', 'cmin', 'dispx', 'dispy', 'dispz', 'disptot')
		- 'background_expression_color': Expression or annotation variable used for coloring (string value)
		- 'background_transparency': Background transparency (float value, [0,1])
		- 'border_color': Border color (string value)
		- 'border_color_pident': Border pid/curve color (0,1)
		- 'border_padding': Border padding (float value)
		- 'border_width': Border width (float value)
		- 'border_rounded': Style of border corners (0,1)
		- 'hide_shadowed': Hide Shadowed Option (0,1)
		- 'line_color': Line color (string value)
		- 'line_width': Line width (float value)
		- 'model_visibility': Model dependent visibility (0,1)
		- 'planecut_height': Plane cut height (integer value)
		- 'planecut_width': Plane cut width (integer value)
		- 'planecut_rotate': Rotate plane cut (float value)
		- 'planecut_draw': Draw plane cur (0,1)
		- 'pointer_color': Pointer color (string value)
		- 'pointer_color_pident': Pointer pid/curve color (0,1)
		- 'pointer_size': Pointer size (float value)
		- 'pointer_style': Pointer style ('arrow', 'box', 'circle', 'cross', 'none', 'x')
		- 'pointer_visibility': Show pointer (0,1)
		- 'position_xy': Position (float value, float value)
		- 'size': Size (integer value)
		- 'text_align': Text alignment ('center', 'left', 'right')
		- 'text_color': Text color (string value)
		- 'text_color_pident': Text pid/curve color (0,1)
		- 'title_color': Title color (string value)
		- 'title_color_pident': Title pid/curve color
		- 'title_font': Title font (string value)
		- 'title_format': Title format ('auto', 'fixed', 'scientific')
		- 'title_htmltext': Title html text (string value)
		- 'title_precision': Title precision digits (integer value)
		- 'title_text': Title text
		- 'title_vertical': Draw vertical text (0,1)
		- 'title_visibility': Title visibility ('auto', 'on', 'off')
		- 'circular': Circular shape (0,1)
		- 'circular_size': Circular Shape Size (integer value)
		- 'circular_multiplier': Circular Shape Size Multiplier (integer value)
		- 'circular_initial': Limit to initial (0,1)

	Returns
	-------
	int
		It returns an integer, 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 7
		    annotation_settings = list()
		    annotation_settings.append("border_color,yellow")
		    annotation_settings.append("text_color,blue")
		    ret = annotations.SetSettingsOfAnnotation(annotation_id, annotation_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_settings instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOn2D(list_annotation_id: object, list_x_pos: object, list_y_pos: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_2d_positions_on_annotations` instead.


	This function sets the pointers of some annotations specified by their ids (list_annotation_id) at some positions on the screen plane. Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).

	Parameters
	----------
	list_annotation_id : object
		Ids of the annotations.

	list_x_pos : object
		List with positions in the x-axis of the screen plane in the range of [0,1].

	list_y_pos : object
		List with positions in the y-axis of the screen plane in the range of [0,1].

	Returns
	-------
	object
		Upon success, it returns a list of objects of class Annotation referring to the given annotations.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_ids = list()
		    list_x_pos = list()
		    list_y_pos = list()
		
		    all_annotations = annotations.Annotations()
		    i = 0
		    for a in all_annotations:
		        list_annotation_ids.append(a.id)
		        list_x_pos.append(20 * i)
		        list_y_pos.append(20 * i)
		        i = i + 1
		    some_annotations = annotations.SetSomeAnnotationsPointerOn2D(
		        list_annotation_ids, list_x_pos, list_y_pos
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_2d_positions_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOn3D(list_annotation_id: object, list_x_coord: object, list_y_coord: object, list_z_coord: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_3d_positions_on_annotations` instead.


	This function sets the pointers of some annotations at 3D positions in space.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotation.

	list_x_coord : object
		List with X coordinates.

	list_y_coord : object
		List with Y coordinates.

	list_z_coord : object
		List with Z coordinates.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_x_coord = list()
		    list_y_coord = list()
		    list_z_coord = list()
		
		    all_annotations = annotations.Annotations()
		    i = 0
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_x_coord.append(10 * i)
		        list_y_coord.append(10 * i)
		        list_z_coord.append(10 * i)
		        i = i + 1
		    some_annotations = annotations.SetSomeAnnotationsPointerOn3D(
		        list_annotation_id, list_x_coord, list_y_coord, list_z_coord
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_3d_positions_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnBoundary(list_annotation_id: object, list_model_id: object, list_boundary_type: object, list_boundary_id: object, list_second_id: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_boundaries_on_annotations` instead.


	This function sets the pointers of some annotations specified by their ids on some boundary elements.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the elements.

	list_boundary_type : object
		List with types of the boundary elements (META constants).

	list_boundary_id : object
		List with ids of the boundary elements.

	list_second_id : object
		List with second ids of the boundary elements.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_boundary_type = list()
		    list_boundary_id = list()
		    list_second_id = list()
		
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_boundary_type.append(constants.PLOAD4)
		        list_boundary_id.append(2)
		        list_second_id.append(0)
		    some_annotations = annotations.SetSomeAnnotationsPointerOnBoundary(
		        list_annotation_id,
		        list_model_id,
		        list_boundary_type,
		        list_boundary_id,
		        list_second_id,
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_boundaries_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnCurve(list_annotation_id: object, list_window_name: object, list_curve_id: object, list_point_id: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_curves_on_annotations` instead.


	This function sets the pointers of some annotations specified by their ids on some curves of some given plot2d windows.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations

	list_window_name : object
		List with names of the windows

	list_curve_id : object
		List with ids of the curves.

	list_point_id : object, optional
		List with ids of the points of the curves.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_window_name = list()
		    list_curve_id = list()
		    list_point_id = list()
		
		    all_annotations = annotations.Annotations()
		    i = 0
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_window_name.append("Window1")
		        list_curve_id.append(1)
		        list_point_id.append(i)
		        i = i + 1
		    some_annotations = annotations.SetSomeAnnotationsPointerOnCurve(
		        list_annotation_id, list_window_name, list_curve_id, list_point_id
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_curves_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnElement(list_annotation_id: object, list_model_id: object, list_element_type: object, list_element_id: object, list_second_id: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_elements_on_annotations` instead.


	This function sets the pointers of some annotations on some elements.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the elements.

	list_element_type : object
		List with types of the elements (META constants).

	list_element_id : object
		List with ids of the elements.

	list_second_id : object
		List with second ids types of the elements.

	Returns
	-------
	object
		Upon success, it returns alist of objects of class Annotation referring to the given annotation.
		Else, an empty list is returned.
		A description of class Annotation can be found as "Annotation" under library category "annotations".

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_element_type = list()
		    list_element_id = list()
		    list_second_id = list()
		
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_element_type.append(constants.SOLID)
		        list_element_id.append(16929)
		        list_second_id.append(-1)
		    some_annotations = annotations.SetSomeAnnotationsPointerOnElement(
		        list_annotation_id,
		        list_model_id,
		        list_element_type,
		        list_element_id,
		        list_second_id,
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_elements_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnGroup(list_annotation_id: object, list_model_id: object, list_group_name: object, list_pointer_position: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_groups_on_annotations` instead.


	This function sets the pointers of some specific annotations on some groups.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotation

	list_model_id : object
		List with ids of the model of the group.

	list_group_name : object
		List with names of the groups.

	list_pointer_position : object, optional
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
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_group_name = list()
		    list_pointer_position = list()
		
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_group_name.append("My_Group")
		        list_pointer_position.append("none")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnGroup(
		        list_annotation_id, list_model_id, list_group_name, list_pointer_position
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_groups_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnGroupInstance(list_annotation_id: object, list_model_id: object, list_group_name: object, list_group_instance: object, list_pointer_position: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_groups_on_annotations` instead.


	This function sets the pointers of some given annotations on some group instances.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the nodes.

	list_group_name : object
		List with names of the groups.

	list_group_instance : object
		List with instances of the groups.

	list_pointer_position : object
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
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_group_name = list()
		    list_group_instance = list()
		    list_pointer_position = list()
		
		    all_annotations = annotations.Annotations()
		
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_group_name.append("My_Group")
		        list_group_instance.append(1)
		        list_pointer_position.append("none")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnGroupInstance(
		        list_annotation_id,
		        list_model_id,
		        list_group_name,
		        list_group_instance,
		        list_pointer_position,
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_groups_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnMaterial(list_annotation_id: object, list_model_id: object, list_material_type: object, list_material_id: object, list_pointer_position: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_materials_on_annotations` instead.


	This function sets the pointers of some specific annotations on some materials.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the materials.

	list_material_type : object
		List with types of the materials (META constants).

	list_material_id : object
		List with ids of the materials.

	list_pointer_position : object, optional
		List with positions of the pointer on the materials.
		Pointer position refers to the entity of the group to which the annotation will point. Its possible values are:
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
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_material_type = list()
		    list_material_id = list()
		    list_pointer_position = list()
		
		    all_annotations = annotations.Annotations()
		
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_material_type.append(constants.MAT1)
		        list_material_id.append(1)
		        list_pointer_position.append("none")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnMaterial(
		        list_annotation_id,
		        list_model_id,
		        list_material_type,
		        list_material_id,
		        list_pointer_position,
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_materials_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnNode(list_annotation_id: object, list_model_id: object, list_node_id: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_nodes_on_annotations` instead.


	This function sets the pointers of some annotations on some nodes.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the nodes.

	list_node_id : object
		List with ids of the nodes.

	Returns
	-------
	object
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_node_id = list()
		
		    all_annotations = annotations.Annotations()
		
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_node_id.append(17211)
		    some_annotations = annotations.SetSomeAnnotationsPointerOnNode(
		        list_annotation_id, list_model_id, list_node_id
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_nodes_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnPart(list_annotation_id: object, list_model_id: object, list_part_type: object, list_part_id: object, list_pointer_position: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_parts_on_annotations` instead.


	This function sets the pointers of some annotations on some parts.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_model_id : object
		List with ids of the model of the parts.

	list_part_type : object
		List with types of the parts (META constants)

	list_part_id : object
		List with ids of the parts.

	list_pointer_position : object
		List with positions of the pointer on the parts.
		Optional entries of pointer positions refer to the entity of the part to which the annotation will point. Its possible values are:
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
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation, constants

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import constants
		
		
		def main():
		    list_annotation_id = list()
		    list_model_id = list()
		    list_part_type = list()
		    list_part_id = list()
		    list_pointer_position = list()
		
		    all_annotations = annotations.Annotations()
		
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_model_id.append(0)
		        list_part_type.append(constants.PSOLID)
		        list_part_id.append(2)
		        list_pointer_position.append("none")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnPart(
		        list_annotation_id,
		        list_model_id,
		        list_part_type,
		        list_part_id,
		        list_pointer_position,
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_parts_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnPlane(list_annotation_id: object, list_plane_name: object, list_pointer_postion: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_planes_on_annotations` instead.


	This function sets the pointer of some annotations at some existing planes.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_plane_name : object
		List with the names of the planes.

	list_pointer_postion : object
		List of the pointer positions.
		Optional pointer position entries refer to the entity of the plane to which the annotation will point. Their possible values are:
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
		Upon success, it returns an object of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_plane_name = list()
		    list_pointer_position = list()
		
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_plane_name.append("DEFAULT_PLANE_YZ")
		        list_pointer_position.append("none")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnPlane(
		        list_annotation_id, list_plane_name, list_pointer_position
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_planes_on_annotations instead.", DeprecationWarning)

def SetSomeAnnotationsPointerOnWindow(list_annotation_id: object, list_window_name: object) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.set_windows_on_annotations` instead.


	This function sets the pointers of some annotations.

	Parameters
	----------
	list_annotation_id : object
		List with ids of the annotations.

	list_window_name : object
		List with names of the windows.

	Returns
	-------
	object
		Upon success, it returns a list of objects of class Annotation referring to the given annotation.
		Else, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    list_annotation_id = list()
		    list_window_name = list()
		
		    all_annotations = annotations.Annotations()
		    for a in all_annotations:
		        list_annotation_id.append(a.id)
		        list_window_name.append("Window1")
		    some_annotations = annotations.SetSomeAnnotationsPointerOnWindow(
		        list_annotation_id, list_window_name
		    )
		    for a in some_annotations:
		        if a:
		            print(
		                a.id,
		                a.window_name,
		                a.page_id,
		                a.text,
		                a.origin_text,
		                a.visible,
		                a.selected,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.set_windows_on_annotations instead.", DeprecationWarning)

def SetTextColorOfAnnotation(annotation_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_text_color` instead.


	This function sets text color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	red : int
		Red color value.

	green : int
		Green color value.

	blue : int
		Blue color value.

	alpha : int
		Alpha channel value.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = annotations.SetTextColorOfAnnotation(annotation_id, red, green, blue, alpha)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_text_color instead.", DeprecationWarning)

def SetTextOnAnnotation(annotation_id: int, text: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_text` instead.


	This function sets text on an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	text : str
		Text of the annotation.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    text = "Annotation on Part 139"
		    ret = annotations.SetTextOnAnnotation(annotation_id, text)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_text instead.", DeprecationWarning)

def ShowAnnotation(annotation_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.show` instead.


	This function makes visible an annotation with a specific id.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 3
		    ret = annotations.ShowAnnotation(annotation_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.show instead.", DeprecationWarning)

def SubgroupsOfAnnotationGroup(level: int, group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.AnnotationGroup.get_subgroups` instead.


	This function searches for the subgroups of an annotation group in the list of the annotation groups. 

	Parameters
	----------
	level : int, optional
		Optional argument 'level' defines the depth of searching for subgroups (1 - one level down, 2 - two levels down, 3 - three levels down etc.). If argument level is absent, then this function will search down all levels for subgroups.

	group_name : str
		Name of the annotation group.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class AnnotationGroup referring to one subgroup of the given group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    group_name = "AnnoGroup"
		    level = ""
		    subgroups = annotations.SubgroupsOfAnnotationGroup(group_name, level)
		    for ag in subgroups:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.AnnotationGroup.get_subgroups instead.", DeprecationWarning)

def TextColorOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_text_color` instead.


	This function finds text color of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a color object with the text color of the corresponding annotation.
		Else, a non valid color object is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    col = annotations.TextColorOfAnnotation(annotation_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_text_color instead.", DeprecationWarning)

def UpdateAnnotation(annotation: object) -> object:

	"""

	This function updates the data of the given Annotation object. Update is based in the field "id" of the given Annotation object.

	Parameters
	----------
	annotation : object
		Object of class Annotation.

	Returns
	-------
	object
		Upon success, it returns the new updated annotation object.
		Else, a non valid annotation object is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    annotation_id = 1
		    a = annotations.AnnotationById(annotation_id)
		
		    # commands which alter the data of the annotation struct
		    utils.MetaCommand('annotation text 1 text "new_name"')
		
		    a = annotations.UpdateAnnotation(a)
		    if a:  # Update OK
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		    else:  # Update FAILED
		        print("This is not a valid annotation struct")
		
		
		if __name__ == "__main__":
		    main()


	"""

def VisibleAnnotations() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function collects visible annotations of all existing windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific visible annotation of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    visible_annotations = annotations.VisibleAnnotations()
		    for a in visible_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def VisibleAnnotationsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotations` instead.


	This function collects visible on screen annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific visible annotation of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "MetaPost"
		    visible_annotations = annotations.VisibleAnnotationsOfWindow(window_name)
		    for a in visible_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotations instead.", DeprecationWarning)

def VisibleOnScreenAnnotations() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_annotations` instead.


	This function collects visible on screen annotations of all existing windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific visible on screen annotation of an existing window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    visible_annotations = annotations.VisibleOnScreenAnnotations()
		    for a in visible_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_annotations instead.", DeprecationWarning)

def VisibleOnScreenAnnotationsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_annotations` instead.


	This function collects visible on screen annotations of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Annotation referring to one specific visible on screen annotation of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    window_name = "MetaPost"
		    visible_annotations = annotations.VisibleOnScreenAnnotationsOfWindow(window_name)
		    for a in visible_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_annotations instead.", DeprecationWarning)

def TypeOfAnnotationPointer(annotation_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_type` instead.


	This function finds the type of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	str
		Upon success, it returns a string referring to the type of the annotation pointer.
		Possible returned values are:
		- 'node'
		- 'element'
		- 'boundary'
		- 'part'
		- 'material'
		- 'group'
		- 'curve'
		- 'plane'
		- 'window'
		- 'selection'
		- '2d_pos'
		- '3d_pos'.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    anno_type = annotations.TypeOfAnnotationPointer(annotation_id)
		    print(anno_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_type instead.", DeprecationWarning)

def NodeOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_node` instead.


	This function finds the node of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a node object with the node of the pointer of the given annotation.
		Else, a non valid node object is returned.

	See Also
	--------
	nodes.Node

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    n = annotations.NodeOfAnnotationPointer(annotation_id)
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_node instead.", DeprecationWarning)

def ElementOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_element` instead.


	This function finds the element of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns an element object with the element of the pointer of the given annotation.
		Else, a non valid element object is returned.

	See Also
	--------
	elements.Element

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    e = annotations.ElementOfAnnotationPointer(annotation_id)
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_element instead.", DeprecationWarning)

def BoundaryOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_boundary` instead.


	This function finds the boundary element of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a boundary object with the boundary element of the pointer of the given annotation.
		Else, a non valid boundary object is returned.

	See Also
	--------
	boundaries.Boundary

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    b = annotations.BoundaryOfAnnotationPointer(annotation_id)
		    if b:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_boundary instead.", DeprecationWarning)

def PartOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_part` instead.


	This function finds the part of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a part object with the part of the pointer of the given annotation.
		Else, a non valid part object is returned.

	See Also
	--------
	parts.Part

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    p = annotations.PartOfAnnotationPointer(annotation_id)
		    if p:
		        print(
		            p.id,
		            p.type,
		            p.subtype,
		            p.visible,
		            p.name,
		            p.mat_id,
		            p.shell_thick,
		            p.model_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_part instead.", DeprecationWarning)

def MaterialOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_material` instead.


	This function finds the material of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a material object with the material of the pointer of the given annotation.
		Else, a non valid material object is returned.

	See Also
	--------
	materials.Material

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    m = annotations.MaterialOfAnnotationPointer(annotation_id)
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_material instead.", DeprecationWarning)

def GroupOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_group` instead.


	This function finds the group of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a group object with the group of the pointer of the given annotation.
		Else, a non valid group object is returned.

	See Also
	--------
	groups.Group

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    g = annotations.GroupOfAnnotationPointer(annotation_id)
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		        )
		        print(
		            g.vsc_number,
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_group instead.", DeprecationWarning)

def CurveOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_curve` instead.


	This function finds the curve of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a curve object with the curve of the pointer of the given annotation.
		Else, a non valid curve object is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    c = annotations.CurveOfAnnotationPointer(annotation_id)
		    if c:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_curve instead.", DeprecationWarning)

def PlaneOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_plane` instead.


	This function finds the plane of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a plane object with the plane of the pointer of the given annotation.
		Else, a non valid plane object is returned.

	See Also
	--------
	planes.Plane

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    pl = annotations.PlaneOfAnnotationPointer(annotation_id)
		    if pl:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_plane instead.", DeprecationWarning)

def WindowOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_pointer_window` instead.


	This function finds the window of the pointer of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a window object with the window of the pointer of the given annotation.
		Else, a non valid window object is returned.

	See Also
	--------
	windows.Window

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    w = annotations.WindowOfAnnotationPointer(annotation_id)
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_pointer_window instead.", DeprecationWarning)

def Position2DOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_2d_position` instead.


	This function finds the 2D position of the annotation pointer of annotations created on 2D Pos.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list with 2 float elements referring to 2D position of the pointer of the given annotation.
		2D position on the screen plane is identified by float numbers in the range of [0,1].
		Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    mat_pos = annotations.Position2DOfAnnotationPointer(annotation_id)
		    if len(mat_pos):
		        print(mat_pos[0], mat_pos[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_2d_position instead.", DeprecationWarning)

def Position3DOfAnnotationPointer(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_3d_position` instead.


	This function finds the 3D position of the annotation pointer of annotations created on 3D Pos.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list with 3 float elements referring to the 3D position coordinates of the pointer of the given annotation. 
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    mat_pos = annotations.Position3DOfAnnotationPointer(annotation_id)
		    if len(mat_pos):
		        print(mat_pos[0], mat_pos[1], mat_pos[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_3d_position instead.", DeprecationWarning)

def PositionOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_position` instead.


	This function finds the position of the annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list with 2 float elements referring to the position of the given annotation.
		Annotation position is identified by float numbers in the range of [0,1].
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    annot_pos = annotations.PositionOfAnnotation(annotation_id)
		    if len(annot_pos):
		        print(annot_pos[0], annot_pos[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_position instead.", DeprecationWarning)

def AnchorTypeOfAnnotation(annotation_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_anchor_type` instead.


	This function finds the anchor type of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	str
		Upon success, it returns a string referring to the type of the annotation pointer.
		Possible returned values are:
		- 'none'
		- 'scrtopleft'
		- 'scrbotleft'
		- 'scrbotright'
		- 'scrtopright'
		- 'pointer'.
		Upon failure, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    anchor_type = annotations.AnchorTypeOfAnnotation(annotation_id)
		    print(anchor_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_anchor_type instead.", DeprecationWarning)

def PositionOffsetOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_position_offset` instead.


	This function finds the offset (X,Y) of the position of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		Upon success, it returns a list whose first member is the offset of the position of a given annotation in the x-axis of the screen plane and second member is the offset of the position of a given annotation in the y-axis of the screen plane.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    offset = annotations.PositionOffsetOfAnnotation(annotation_id)
		    if len(offset) == 2:
		        xoffset = offset[0]
		        print(xoffset)
		        yoffset = offset[1]
		        print(yoffset)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_position_offset instead.", DeprecationWarning)

def SettingsOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_settings` instead.


	This function displays the settings of a given annotation.

	Parameters
	----------
	annotation_id : int
		Id of the annotation.

	Returns
	-------
	object
		It returns a list with the settings of the given annotation. Each member of the list is a string which contains as strings separated by comma the name and the value of the setting.  
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    all_settings = annotations.SettingsOfAnnotation(annotation_id)
		    for one_setting in all_settings:
		        print(one_setting)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_settings instead.", DeprecationWarning)

def SelectionOfAnnotationPointer(annotation_id: int) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_selection` instead.


	This function returns the string of the id range of a given annotation on Selection.

	Parameters
	----------
	annotation_id : int

	Returns
	-------
	str
		Upon success, it returns a string of the id range of a given annotation on Selection.
		Else, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annotation_id = 1
		    selection_str = annotations.SelectionOfAnnotationPointer(annotation_id)
		    anchor_type = annotations.TypeOfAnnotationPointer(annotation_id)
		
		    print(
		        "Annotation "
		        + str(annotation_id)
		        + " element "
		        + anchor_type
		        + " "
		        + selection_str
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_selection instead.", DeprecationWarning)

def AttributeOfAnnotation(annot_id: int, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_attribute` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	annot_id : int
		The id of the annotation

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    name = "Type"
		    annot_id = 1
		    val = annotations.AttributeOfAnnotation(annot_id, name)
		    print("Value " + val)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_attribute instead.", DeprecationWarning)

def SetAttributeOfAnnotation(annot_id: int, attribute_name: object, attribute_value: object, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given annotation. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	annot_id : int
		The id of the annotation.

	attribute_name : object
		Name of the attribute.

	attribute_value : object
		Value of the attribute. It can be either a number or a string.

	attribute_type : str, optional
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annot_id = 1
		
		    name = "test_attr"
		    val = "val"
		    annotations.SetAttributeOfAnnotation(annot_id, name, val)
		    # or
		    name = "num_attr"
		    val = 12.3
		    attribute_type = "numerical"
		    annotations.SetAttributeOfAnnotation(annot_id, name, val, attribute_type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.set_attribute instead.", DeprecationWarning)

def AttributesOfAnnotations(annot_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_attributes` instead.


	This function collects all attributes of a given annotation

	Parameters
	----------
	annot_id : int
		The id of the annotation

	Returns
	-------
	object
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	See Also
	--------
	annotations.Annotation

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    annot_id = 1
		    all_attributes = annotations.AttributesOfAnnotation(annot_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_attributes instead.", DeprecationWarning)

def ParentOfGroupAnnotation(annotation_group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.AnnotationGroup.get_parent` instead.


	Returns the parent annotation group of a given annotation group.

	Parameters
	----------
	annotation_group_name : str
		Name of annotation group

	Returns
	-------
	object
		Returns the parent annotation group of a given annotation group

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    group = annotations.GroupOfAnnotation(annotation_id=1)
		    print(group)
		    group = annotations.ParentOfGroupAnnotation(annotation_group_name=group.name)
		    if annotations.IsAnnotationGroup(group):
		        print(group)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.AnnotationGroup.get_parent instead.", DeprecationWarning)

def GroupOfAnnotation(annotation_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.annotations.Annotation.get_annotation_group` instead.


	Returns the annotation group of the annotation, if it exists.

	Parameters
	----------
	annotation_id : int
		The id of the annotation

	Returns
	-------
	object
		Returns the annotation group of the annotation, if it exists. Else returns none.

	See Also
	--------
	annotations.AnnotationGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    group = annotations.GroupOfAnnotation(annotation_id=1)
		    if group:
		        print(group)
		        group = annotations.ParentOfGroupAnnotation(annotation_group_name=group.name)
		        if annotations.IsAnnotationGroup(group):
		            print(group)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.annotations.Annotation.get_annotation_group instead.", DeprecationWarning)

class Annotation():

	"""

	Class for annotations

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    a = annotations.Annotation(id=1, page_id=0)
		    if a:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    w = ann.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    page = ann.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_node
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    n = ann.get_node()
		    if n:
		        print(n.id, n.x, n.y, n.z, n.visible, n.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_element
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    e = ann.get_element()
		    if e:
		        print(e.id, e.second_id, e.type, e.subtype, e.part_id, e.visible, e.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_boundary
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    b = ann.get_boundary()
		    if b:
		        print(b.id, b.second_id, b.type, b.subtype, b.visible, b.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_part
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    p = ann.get_part()
		    if p:
		        print(
		            p.id,
		            p.type,
		            p.subtype,
		            p.visible,
		            p.name,
		            p.mat_id,
		            p.shell_thick,
		            p.model_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_material
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    m = ann.get_material()
		    if m:
		        print(m.id, m.type, m.name, m.model_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_group
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    g = ann.get_group()
		    if g:
		        print(
		            g.name,
		            g.model_id,
		            g.module_id,
		            g.version,
		            g.representation,
		            g.study_version,
		        )
		        print(
		            g.vsc_number,
		            g.target_mass,
		            g.user_group,
		            g.pid_offset,
		            g.freeze,
		            g.type,
		            g.instance,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curve
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    c = ann.get_curve()
		    if c:
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
		# method: get_plane
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pl = ann.get_plane()
		    if pl:
		        print(pl.name, pl.clip_type)
		        print(pl.origin[0], pl.origin[1], pl.origin[2])
		        print(pl.normal_vector[0], pl.normal_vector[1], pl.normal_vector[2])
		        print(pl.edge_vector[0], pl.edge_vector[1], pl.edge_vector[2])
		
		
		if __name__ == "__main__":
		    main()
		# method: get_pointer_window
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    w = ann.get_pointer_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_annotation_group
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ag = ann.get_annotation_group()
		    if ag:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_color
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    col = ann.get_text_color()
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_border_color
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    col = ann.get_border_color()
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_pointer_color
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    col = ann.get_pointer_color()
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_background_color
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    col = ann.get_background_color()
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_start_pointer_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pos = ann.get_start_pointer_position()
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_end_pointer_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pos = ann.get_end_pointer_position()
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_anchor_type
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    type = ann.get_anchor_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position_offset
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    offset = ann.get_position_offset()
		    print(offset)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_type
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    type = ann.get_type()
		    print(type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_selection
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    selection = ann.get_selection()
		    print(selection)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_2d_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pos = ann.get_2d_position()
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_3d_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pos = ann.get_3d_position()
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    pos = ann.get_position()
		    print(pos)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    attribute_name = "Type"
		    attr = ann.get_attributes(attribute_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_number_of_pointers
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    num = ann.get_number_of_pointers()
		    print(num)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_settings
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    settings = ann.get_settings()
		    print(settings)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_marker
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    marker = ann.is_marker()
		    if marker:
		        print(annot_id, marker)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    text = ann.set_text()
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text_color
		# PYTHON script
		import meta
		from meta import annotations
		from meta import windows
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    color = windows.Color(255, 255, 0, 255)
		    ret = ann.set_text_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_border_color
		# PYTHON script
		import meta
		from meta import annotations
		from meta import windows
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    color = windows.Color(255, 255, 0, 255)
		    ret = ann.set_border_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_pointer_color
		# PYTHON script
		import meta
		from meta import annotations
		from meta import windows
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    color = windows.Color(255, 255, 0, 255)
		    ret = ann.set_pointer_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_background_color
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    color = windows.Color(255, 255, 0, 255)
		    ret = ann.set_background_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    attribute_type = "numerical"
		    attribute_name = "test"
		    attribute_value = 30
		    ret = ann.set_attribute(attribute_name, attribute_type, attribute_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_node
		# PYTHON script
		import meta
		from meta import annotations
		from meta import nodes
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    node = nodes.Node(id=100, model_id=0)
		    ret = ann.set_node(node)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_part
		# PYTHON script
		import meta
		from meta import annotations
		from meta import parts
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    part = parts.Part(id=15, model_id=0, type=constants.PSHELL)
		    ret = ann.set_part(part)
		    print(ret)
		    pointer = "dispxmin"
		    ret = ann.set_part(part, pointer)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_material
		# PYTHON script
		import meta
		from meta import annotations
		from meta import materials
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    material = materials.Material(id=23, model_id=0)
		    ret = ann.set_material(material)
		    print(ret)
		    pointer = "dispxmin"
		    ret = ann.set_material(materials, pointer)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_group
		# PYTHON script
		import meta
		from meta import annotations
		from meta import groups
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    group = groups.Group(name="group1", model_id=0)
		    ret = ann.set_group(group)
		    print(ret)
		    pointer = "dispxmin"
		    ret = ann.set_group(group, pointer)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_2d_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    position = [0.7, 0.8]
		    ret = ann.set_2d_position(position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_3d_position
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    position = [2.7, 30.5, 20.9]
		    ret = ann.set_3d_position(position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_curve
		# PYTHON script
		import meta
		from meta import annotations
		from meta import plot2d
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    curve = plot2d.Curve(id=5, window_name="Window1", page_id=0)
		    ret = ann.set_curve(curve)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_element
		# PYTHON script
		import meta
		from meta import annotations
		from meta import elements
		from meta import constants
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    element = elements.Element(id=15, second_id=-1, model_id=0, type=constants.SHELL)
		    ret = ann.set_element(element)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_boundary
		# PYTHON script
		import meta
		from meta import annotations
		from meta import boundaries
		from meta import constants
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    boundary = boundaries.Boundary(id=22, second_id=-1, model_id=0, type=constants.SPC)
		    ret = ann.set_boundary(boundary)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_plane
		# PYTHON script
		import meta
		from meta import annotations
		from meta import planes
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    plane = planes.Plane(name="plane1")
		    ann.set_plane(plane)
		    pointer = "dispxmin"
		    ret = ann.set_plane(plane, pointer)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_window
		# PYTHON script
		import meta
		from meta import annotations
		from meta import windows
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    window = windows.Window(name="Window1", page_id=0)
		    ret = ann.set_window(window)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    settings = {"border_width": "4"}
		    ret = ann.set_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ret = ann.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: deselect
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ret = ann.deselect()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ret = a.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: select
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ret = ann.select()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    ret = ann.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text_box_dimensions
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ann = annotations.Annotation(id=1, page_id=0)
		    dims = ann.get_text_box_dimensions()
		    print(dims[0])
		    print(dims[1])
		    print(dims[2])
		    print(dims[3])
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    a = annotations.Annotation(id=1, page_id=0)
		    can_use = a.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the annotation

	"""

	window_name: str = None
	"""
	Name of the window of the annotation

	"""

	text: str = None
	"""
	Displayed text of the annotation

	"""

	origin_text: str = None
	"""
	Text with variables of the annotation

	"""

	visible: int = None
	"""
	Visibility status
	- 1: visible
	- 0: non visible

	"""

	selected: int = None
	"""
	Selection status
	- 1: selected
	- 0: non selected

	"""

	page_id: int = None
	"""
	Id of the page of the annotation

	"""

	def get_window(self) -> object:

		"""

		This method gets the window of annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the annotation. Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the annotation. Upon failure, it returns None.

		"""


	def get_node(self, pointer_index: int) -> object:

		"""

		This method gets the node of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Node referring to the node of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_element(self, pointer_index: int) -> object:

		"""

		This method gets the element of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Element referring to the element of annotation's pointer.  Upon failure, it returns None.

		"""


	def get_boundary(self, pointer_index: int) -> object:

		"""

		This method gets the boundary element of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Boundary referring to the boundary element of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_part(self, pointer_index: int) -> object:

		"""

		This method gets the part of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Part referring to the part of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_material(self, pointer_index: int) -> object:

		"""

		This method gets the material of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Material referring to the material of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_group(self, pointer_index: int) -> object:

		"""

		This method gets the group of annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Group referring to the group of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_curve(self, pointer_index: int) -> object:

		"""

		This method gets the curve of the annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns an object of type Curve referring to the curve of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_plane(self) -> object:

		"""

		This method gets the plane of the annotation's pointer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Plane referring to the plane of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_pointer_window(self) -> object:

		"""

		This method gets the window of the annotation's pointer. 


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the annotation's pointer. Upon failure, it returns None.

		"""


	def get_annotation_group(self) -> object:

		"""

		This method gets the annotation group of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type AnnotationGroup referring to the annotation group of the annotation. Upon failure, it returns None.

		"""


	def get_text_color(self) -> object:

		"""

		This method gets the text color of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the text color of the annotation. Upon failure, it returns None.

		"""


	def get_border_color(self) -> object:

		"""

		This method gets the border color of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the border color of the annotation. Upon failure, it returns None.

		"""


	def get_pointer_color(self) -> object:

		"""

		This method gets the pointer color of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the pointer color of the annotation. Upon failure, it returns None.

		"""


	def get_background_color(self) -> object:

		"""

		This method gets the background color of the annotation. 


		Returns
		-------
		object
			Upon success, it returns an object of type Color referring to the background color of the annotation. Upon failure, it returns None.

		"""


	def get_start_pointer_position(self, pointer_index: int) -> object:

		"""

		This method gets the starting pointer position of the annotation. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns a list whose first member is the position of the start of the annotation's pointer in the x-axis of the screen plane and second member is the respective position in the y-axis.Upon failure, an empty list is returned.

		"""


	def get_end_pointer_position(self, pointer_index: int) -> object:

		"""

		This method gets the ending position of annotation's pointer. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		object
			Upon success, it returns a list whose first member is the position of the end of the annotation's pointer in the x-axis of the screen plane and second member is the respective position in the y-axis.Upon failure, an empty list is returned.

		"""


	def get_anchor_type(self) -> str:

		"""

		This method gets the anchor type of the annotation. 


		Returns
		-------
		str
			Upon success, it returns a string referring to the anchor type of the annotation. Upon failure, it returns None.

		"""


	def get_position_offset(self) -> object:

		"""

		This method gets the offset (X,Y) of the position of the annotation.


		Returns
		-------
		object
			Upon success, it returns a list whose first member is the offset of the position of the annotation in the x-axis of the screen plane and second member is the offset of the position of the annotation in the y-axis of the screen plane.Upon failure, an empty list is returned.

		"""


	def get_type(self) -> str:

		"""

		This method gets the type of the annotation. 


		Returns
		-------
		str
			Upon success, it returns a string referring to the type of the annotation. Upon failure, it returns None.

		"""


	def get_selection(self, pointer_index: int) -> str:

		"""

		This method gets the string of the id range of the annotation on Selection. 


		Parameters
		----------
		pointer_index : int, optional
			When the anotation has multiple pointers, it gives the entity at index provided.

		Returns
		-------
		str
			Upon success, it returns a string of the id range of the annotation on Selection.Upon failure, it returns None.

		"""


	def get_2d_position(self) -> object:

		"""

		This method gets the 2D position of the annotation's pointer created on 2D Pos.


		Returns
		-------
		object
			Upon success, it returns a list with 2 float elements referring to the 2D position of the annotation's pointer. 2D position on the screen plane is identified by float numbers in the range of [0,1].Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).Upon failure, an empty list is returned.

		"""


	def get_3d_position(self) -> object:

		"""

		This method gets the 3D position of the annotation's pointer created on 3D Pos.


		Returns
		-------
		object
			Upon success, it returns a list with 3 float elements referring to the 3D position coordinates of the annotation's pointer.   Upon failure, an empty list is returned.

		"""


	def get_position(self) -> object:

		"""

		This method gets the position of the annotation.


		Returns
		-------
		object
			Upon success, it returns a list with 2 float elements referring to the position of the annotation.Annotation position is identified by float numbers in the range of [0,1].Upon failure, an empty list is returned.

		"""


	def get_attributes(self, attribute_name: str) -> object:

		"""

		This method gets the attributes of the annotation. 


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute. Syntax 'Attribute_group.attribute_name' can be used as attribute_name to receive an attribute from an attribute group.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	def get_settings(self) -> object:

		"""

		This method gets the settings of the annotation. 


		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the settings as string and as values the value of the settings as string. Upon failure, it returns an empty dictionary.

		"""


	def set_text(self, text: str) -> bool:

		"""

		This method sets the text of the annotation.


		Parameters
		----------
		text : str
			Text of the annotation.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_text_color(self, color: object) -> bool:

		"""

		This method sets the text color of the annotation.


		Parameters
		----------
		color : object
			Object of type Color.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_border_color(self, color: object) -> bool:

		"""

		This method sets the border color of the annotation.


		Parameters
		----------
		color : object
			Object of type Color.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_pointer_color(self, color: object) -> bool:

		"""

		This method gets the pointer color of the annotation.


		Parameters
		----------
		color : object
			Object of type Color.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_background_color(self, color: object) -> bool:

		"""

		This method sets the background color of the annotation.


		Parameters
		----------
		color : object
			Object of type Color.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_settings(self, settings: object) -> bool:

		"""

		This method sets settings of the annotation.


		Parameters
		----------
		settings : object
			Settings (key-value) of the annotation.
			A dictionary with string keys and string values:
			- 'anchor_none': Anchor none
			- 'anchor_pointer': Anchor relative to pointer (float value,float value)
			- 'anchor_scrbotleft': Anchor relative to bottom left of screen (float value,float value)
			- 'anchor_scrbotright': Anchor relative to bottom right of screen (float value,float value)
			- 'anchor_scrtopright': Anchor relative to top right pointer (float value,float value)
			- 'anchor_scrtopleft': Anchor relative to top left pointer (float value,float value)
			- 'background_auto_color': Background automatic color ('on','off')
			- 'background_color': Background color (string value)
			- 'background_function_color': Function used for coloring ('default', 'funcval', 'scalfuncval', 'vecfuncval', 'cmax', 'cmin', 'dispx', 'dispy', 'dispz', 'disptot')
			- 'background_expression_color': Expression or annotation variable used for coloring (string value)
			- 'background_transparency': Background transparency (float value)
			- 'border_color': Border color (string value)
			- 'border_color_pident': Border pid/curve color (0,1)
			- 'border_padding': Border padding (float value)
			- 'border_width': Border width (float value)
			- 'border_rounded': Style of border corners (0,1)
			- 'hide_shadowed': Hide Shadowed Option (0,1)
			- 'line_color': Line color (string value)
			- 'line_width': Line width (float value)
			- 'model_visibility': Model dependent visibility (0,1)
			- 'planecut_height': Plane cut height (integer value)
			- 'planecut_width': Plane cut width (integer value)
			- 'planecut_rotate': Rotate plane cut (float value)
			- 'planecut_draw': Draw plane cur (0,1)
			- 'pointer_color': Pointer color (string value)
			- 'pointer_color_pident': Pointer pid/curve color (0,1)
			- 'pointer_size': Pointer size (0, 39)
			- 'pointer_style': Pointer style ('arrow', 'box', 'circle', 'cross', 'none', 'x')
			- 'pointer_visibility': Show pointer (0,1)
			- 'position_xy': Position (float value, float value)
			- 'size': Size (integer value)
			- 'text_align': Text alignment ('center', 'left', 'right')
			- 'text_color': Text color (string value)
			- 'text_color_pident': Text pid/curve color (0,1)
			- 'title_color': Title color (string value)
			- 'title_color_pident': Title pid/curve color
			- 'title_font': Title font (string value)
			- 'title_format': Title format ('auto', 'fixed', 'scientific')
			- 'title_html_text': Title html text (string value)
			- 'title_precision': Title precision digits (integer value)
			- 'title_text': Title text
			- 'title_vertical': Draw vertical text (0,1)
			- 'title_visibility': Title visibility ('auto', 'on', 'off')
			- 'circular': Circular shape (0,1)
			- 'circular_size': Circular Shape Size (integer value)
			- 'circular_multiplier': Circular Shape Size Multiplier (integer value)
			- 'circular_initial': Limit to initial (0,1)

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: object) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the annotation. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. 
			Its possible values are:
			'string': String
			'numerical': Number

		attribute_value : object
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_node(self, node: object, append: bool) -> object:

		"""

		This method sets the node of the annotation pointer.


		Parameters
		----------
		node : object
			Object of type Node.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		object
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_part(self, part: object, pointer: str, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on a part.


		Parameters
		----------
		part : object
			Object of type Part.

		pointer : str, optional
			It refers to the entity of the part to which the annotation will point. 
			Its possible values are:
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

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_material(self, material: object, pointer: str, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on a material.


		Parameters
		----------
		material : object
			Object of type Material.

		pointer : str, optional
			It refers to the entity of the material to which the annotation will point. 
			Its possible values are:
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
			If this argument is absent, then annotation will point to the center of the material.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_group(self, group: object, pointer: str, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on a group.


		Parameters
		----------
		group : object
			Object of type Group.

		pointer : str, optional
			It refers to the entity of the group to which the annotation will point. 
			Its possible values are:
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
			If this argument is absent, then annotation will refer to the whole group.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_2d_position(self, position: object) -> bool:

		"""

		This method sets the pointer of the annotation specified at a position on the screen plane. Down and left corner of the screen is identified by the position (x_pos = 0, y_pos = 0).


		Parameters
		----------
		position : object
			2d position of the annotation.
			A list with doubles: 
			[0]: X position
			[1]: Y position

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_3d_position(self, position: object) -> bool:

		"""

		This function sets the pointer of the annotation at a position in space.


		Parameters
		----------
		position : object
			3d position of the annotation.
			A list with doubles: 
			[0]: X coordinate
			[1]: Y coordinate
			[2]: Z coordinate

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_curve(self, curve: object, point_id: int, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on a curve.


		Parameters
		----------
		curve : object
			Object of type Curve.

		point_id : int, optional
			Id of the point.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_element(self, element: object, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on an element.


		Parameters
		----------
		element : object
			Object of type Element.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_boundary(self, boundary: object, append: bool) -> bool:

		"""

		This method sets the pointer of the annotation on a boundary element.


		Parameters
		----------
		boundary : object
			Object of type Boundary.

		append : bool, optional
			If it is used and is true, it adds the pointer at the same annotation without replacing the previous pointer.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def set_plane(self, plane: object, pointer: str) -> bool:

		"""

		This method sets the pointer of the annotation at an existing plane.


		Parameters
		----------
		plane : object
			Object of type Plane.

		pointer : str, optional
			It refers to the entity of the plane to which the annotation will point. 
			Its possible values are:
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
			If this argument is absent, then annotation will refer to the whole plane.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def set_window(self, window: object) -> bool:

		"""

		This method sets the pointer of the annotation at a given window.


		Parameters
		----------
		window : object
			Object of type Window.

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		"""


	def show(self) -> bool:

		"""

		This method shows the annotation.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def hide(self) -> bool:

		"""

		This method hides the annotation.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def select(self) -> bool:

		"""

		This method selects the annotation.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def deselect(self) -> bool:

		"""

		This method deselects the annotation.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def delete(self) -> bool:

		"""

		This method deletes the annotation.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		"""


	def is_marker(self):

		"""

		This method returns whether an annotation is marker or not


		"""


	def get_text_box_dimensions(self) -> object:

		"""

		This method gets the dimensions of the text box of the annotation.


		Returns
		-------
		object
			Upon success, it returns a list with 4 integer elements referring to the dimensions of text box  of the annotation.First element is min X in pixels.Second element is max X in pixels.Third element is min Y in pixels.Fourth element is max Y in pixels.Upon failure, an empty list is returned.

		"""


	def get_number_of_pointers(self) -> int:

		"""

		This method gets the number of the pointers of the annotation. 


		Returns
		-------
		int
			Upon success, it returns an integer for the number of the pointers of the annotation. Upon failure, it returns a zero number.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Annotation entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class AnnotationGroup():

	"""

	Class for annotation groups

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    if ag:
		        print(ag.name, ag.window_name, ag.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    w = ag.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    page = ag.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_annotations
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    group_annotations = ag.get_annotations()
		    for a in group_annotations:
		        print(
		            a.id, a.window_name, a.page_id, a.text, a.origin_text, a.visible, a.selected
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_subgroups
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    level = 2
		    ann_subgroups = ag.get_subgroups(level)
		    for sub_ag in ann_subgroups:
		        print(sub_ag.name, sub_ag.window_name, sub_ag.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_parent
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="Group1", page_id=0)
		    sub_ag = ag.get_parent()
		    if sub_ag:
		        print(sub_ag.name, sub_ag.window_name, sub_ag.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import annotations
		
		
		def main():
		    ag = annotations.AnnotationGroup(name="AnnGroup", page_id=0)
		    can_use = ag.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the annotation group

	"""

	window_name: str = None
	"""
	Name of the window

	"""

	page_id: int = None
	"""
	Id of the page of the annotation group

	"""

	def get_window(self) -> object:

		"""

		This method gets the window of the annotation group. 


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the page of the annotation group.Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the annotation group.  


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the annotation group. Upon failure, it returns None.

		"""


	def get_annotations(self) -> object:

		"""

		This method gets the annotations of the annotation group. 


		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class Annotation referring to one specific annotation of the annotation group. Upon failure, an empty list is returned.

		"""


	def get_subgroups(self, get_subgroups: object) -> object:

		"""

		This method gets the subgroups of the annotation group. 


		Parameters
		----------
		get_subgroups : object
			It defines the depth of searching for subgroups (1 - one level down, 2 - two levels down, 3 - three levels down etc.). 
			If argument level is absent, then this function will search down all levels for subgroups.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class AnnotationGroup referring to one subgroup of the annotation group.  Upon failure, an empty list is returned.

		"""


	def get_parent(self) -> object:

		"""

		This method gets the parent annotation group of the annotation group. 


		Returns
		-------
		object
			Upon success, it returns an object of type AnnotationGroup referring to the parent annotation group of the annotation group. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Annotation Group entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

