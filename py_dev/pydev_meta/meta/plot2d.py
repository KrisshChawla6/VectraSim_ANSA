from __future__ import annotations
from typing import *

def ActivatePlot(window_name: str, plot_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.activate` instead.


	This function makes active a plot of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	Returns
	-------
	object
		Upon success, it returns an object of class Plot referring to the currently activated plot.
		Else, None is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    pl = plot2d.ActivatePlot(window_name, plot_id)
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.activate instead.", DeprecationWarning)

def ActivePlotAxes() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects active plot axes of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_axes = plot2d.ActivePlotAxes()
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def ActivePlotAxesByType(axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects active plot axes of all 2d plot windows for a specific type. Argument "axis_type" refers to the type of axes. 

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis_type = "xaxis"
		    plot_axes = plot2d.ActivePlotAxesByType(axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def ActivePlotAxesOfPlot(plot_id: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects active plot axes of a given plot.

	Parameters
	----------
	plot_id : str
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_axes = plot2d.ActivePlotAxesOfPlot(window_name, plot_id)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def ActivePlotAxesOfPlotByType(axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects active plot axes of a given plot for a specific type.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    plot_axes = plot2d.ActivePlotAxesOfPlotByType(window_name, plot_id, axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def ActivePlotAxesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects active plot axes of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_axes = plot2d.ActivePlotAxesOfWindow(window_name)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def ActivePlotAxesOfWindowByType(window_name: str, axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects active plot axes of a given 2d plot window for a specific type.

	Parameters
	----------
	window_name : str
		Name of the window.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific active axis of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    axis_type = "xaxis"
		    plot_axes = plot2d.ActivePlotAxesOfWindowByType(window_name, axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def ActivePlots() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plots` instead.


	This function collects all active plots of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    active_plots = plot2d.ActivePlots()
		    for pl in active_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plots instead.", DeprecationWarning)

def ActivePlotsByType(plot_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plots` instead.


	This function collects all active plots of all 2d plot windows with a specific type. 

	Parameters
	----------
	plot_type : str
		Type of the plot. Possible values are:
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

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_type = "plain"
		    active_plots = plot2d.ActivePlotsByType(plot_type)
		    for pl in active_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plots instead.", DeprecationWarning)

def ActivePlotsOfWindow(window_name: str) -> object:

	"""

	This function collects all active plots of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    active_plots = plot2d.ActivePlotsOfWindow(window_name)
		    for pl in active_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ActivePlotsOfWindowByType(window_name: str, plot_type: str) -> object:

	"""

	This function collects all active plots of a given plot2d plot window with a specific type.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_type : str
		Type of the plot. Possible values are:
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

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_type = "plain"
		    active_plots = plot2d.ActivePlotsOfWindowByType(window_name, plot_type)
		    for pl in active_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddNameOnCurve(curve_id: int, curve_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_name` instead.


	This function defines a name for a curve of a given 2d plot window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_name : str
		Name of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_name = "Pressure 8"
		    plot2d.AddNameOnCurve(window_name, curve_id, curve_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_name instead.", DeprecationWarning)

def AdvFiltersOnCurves(window_name: str, adv_filters: object) -> object:

	"""

	This function allows the user to collect curves of a window specified by its name through some advanced filters. 

	Parameters
	----------
	window_name : str
		Name of the window.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:>=5:Keep All")
		    adv_filters.append("intersect:Curves:ymax::Max 2")
		    window_name = "Window1"
		
		    collected_curves = plot2d.AdvFiltersOnCurves(window_name, adv_filters)
		    for c in collected_curves:
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

def AdvFiltersOnCurvesWithRange(window_name: str, adv_filters: object, xmin: float, xmax: float) -> object:

	"""

	This function allows the user to collect curves of a window through an advanced filter in a given range. Range is specified by minimum and maximum x value.

	Parameters
	----------
	window_name : str
		Name of the window.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter.

	xmin : float
		Minimum x value.

	xmax : float
		Maximum x value.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:>=5:Keep All")
		    adv_filters.append("intersect:Curves:ymax::Max 2")
		    xmin = 0.01
		    xmax = 0.02
		    window_name = "Window1"
		
		    collected_curves = plot2d.AdvFiltersOnCurvesWithRange(
		        window_name, adv_filters, xmin, xmax
		    )
		    for c in collected_curves:
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

def AdvFiltersOnPoints(window_name: str, adv_filters: object, curve_type: str) -> object:

	"""

	This function allows the user to collect curve points of a window through some advanced filter.

	Parameters
	----------
	window_name : str
		Name of the window.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific curve point of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:>=5:Keep All")
		    adv_filters.append("intersect:Curves:ymax::Max 2")
		    adv_filters.append("intersect:Points:yval::Each Curve Max 1")
		    window_name = "Window1"
		    curve_type = "real"
		
		    collected_points = plot2d.AdvFiltersOnPoints(window_name, adv_filters, curve_type)
		    for pnt in collected_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AdvFiltersOnPointsWithRange(window_name: str, adv_filters: object, xmin: float, xmax: float, curve_type: str) -> object:

	"""

	This function allows the user to collect curve points of a window through some advanced filter. Range is specified by minimum and maximum x value

	Parameters
	----------
	window_name : str
		Name of the window.

	adv_filters : object
		List with the advanced filter entries as string expressions. Their syntax is the same with the commands referring to advanced filter.

	xmin : float
		Minimum x value.

	xmax : float
		Maximum x value.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific curve point of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:==1:Keep All")
		    window_name = "Window1"
		    xmin = 0.02
		    xmax = 0.03
		    curve_type = "real"
		
		    collected_points = plot2d.AdvFiltersOnPointsWithRange(
		        window_name, adv_filters, xmin, xmax, curve_type
		    )
		    for pnt in collected_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributeOfCurve(attrib_name: str, curve_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_attributes` instead.


	This function returns the value of a specific attribute referring to a given curve.

	Parameters
	----------
	attrib_name : str
		Name of the attribute.

	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    attrib_name = "Filename"
		    attrib_value = plot2d.AttributeOfCurve(window_name, curve_id, attrib_name)
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_attributes instead.", DeprecationWarning)

def CollectNewCurvesEnd() -> object:

	"""

	This function ends recording the creation of new curves. This function should be preceded by a corresponding call to script function CollectNewCurvesStart().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific newly created curve.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import plot2d
		
		
		def main():
		    plot2d.CollectNewCurvesStart()
		
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user1" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.ReportNewCurves()
		    for c in new_curves:
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
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user2" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.CollectNewCurvesEnd()
		    for c in new_curves:
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

def CollectNewCurvesStart() -> int:

	"""

	This function starts recording the creation of new curves. This function should be followed by a corresponding call to script function CollectNewCurvesEnd().

	Returns
	-------
	int
		It returns 1 upon success or 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import plot2d
		
		
		def main():
		    plot2d.CollectNewCurvesStart()
		
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user1" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.ReportNewCurves()
		    for c in new_curves:
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
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user2" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.CollectNewCurvesEnd()
		    for c in new_curves:
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

def ColorOfCurve(curve_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_color` instead.


	This function finds color of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a Color object reffering to the color of the corresponding curve.
		Else, None is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		
		    col = plot2d.ColorOfCurve(window_name, curve_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_color instead.", DeprecationWarning)

def ColorOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_color` instead.


	This function finds the color of a plot axis of a given plot with a given id.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a Color object reffering to the color of the corresponding plot axis.
		Else, None is returned.

	See Also
	--------
	windows.Color

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		
		    col = plot2d.ColorOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    if col:
		        print(col.name, col.r, col.g, col.b, col.a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_color instead.", DeprecationWarning)

def CreateCurve(window_name: str, plot_id: int, curve_name: str, xpoints: object, y_magnitude: object, y_phase: object) -> object:

	"""

	This function creates a new curve on a plot of a given 2D plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	curve_name : str
		Name of the curve.

	xpoints : object
		List with X coordinates of the points of the curve.

	y_magnitude : object
		List with Y coordinates of the points of the curve.

	y_phase : object, optional
		List of phase values of the curve.

	Returns
	-------
	object
		Upon success, it returns a Class object referring to the newly created curve of the given plot.
		Else, None is returned.

	See Also
	--------
	Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    curve_name = "Script created curve"
		    xpoints = list()
		    y_magnitude = list()
		    y_phase = list()
		    for i in range(0, 100):
		        magnitude = 2 * i
		        phase = (2 * i) / (3.5 * i + 2.2)
		        xpoints.append(i)
		        y_magnitude.append(magnitude)
		        y_phase.append(phase)
		    c = plot2d.CreateCurve(
		        window_name, plot_id, curve_name, xpoints, y_magnitude, y_phase
		    )
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

def CurveById(window_name: str, curve_id: int) -> object:

	"""
	.. deprecated:: 21.1.0
		Use `window.get_curves()` instead.


	This function finds curve of a 2d plot window with a given id.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	object
		Upon success, it returns an object of class Curve with the given id.
		Else, None is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    c = plot2d.CurveById(window_name, curve_id)
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

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use  window.get_curves() instead.", DeprecationWarning)

def CurveGroups() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_curve_groups` instead.


	This function collects all curve groups of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    AllCurveGroups = plot2d.CurveGroups()
		    for cg in AllCurveGroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_curve_groups instead.", DeprecationWarning)

def CurveGroupsByName(group_name: str, window_name: str) -> object:

	"""

	This function finds curve groups of a 2d plot window with a given name.

	Parameters
	----------
	group_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroups

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "*Gr*"
		    AllCurveGroups = plot2d.CurveGroupsByName(window_name, group_name)
		    for cg in AllCurveGroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurveGroupsOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curve_groups` instead.


	This function collects all curve groups of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    AllCurveGroups = plot2d.CurveGroupsOfPlot(window_name, plot_id)
		    for cg in AllCurveGroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curve_groups instead.", DeprecationWarning)

def CurveGroupsOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_curve_groups` instead.


	This function collects all curve groups of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the given plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    AllCurveGroups = plot2d.CurveGroupsOfWindow(window_name)
		    for cg in AllCurveGroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_curve_groups instead.", DeprecationWarning)

def Curves(all_plots: int) -> object:

	"""

	This function collects all curves of all 2d plot windows.

	Parameters
	----------
	all_plots : int, optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    all_curves = plot2d.Curves()
		    for c in all_curves:
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

def CurvesByName(window_name: str, curve_name: str, exact_match: int) -> object:

	"""
	.. deprecated:: 21.1.0
		Use `window.get_curves()` instead.


	This function finds curves of a 2d plot window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	exact_match : int, optional
		Exact match of curve name.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_name = "*HEAD*"
		    exact_match = 0
		    name_curves = plot2d.CurvesByName(window_name, curve_name, exact_match)
		    for c in name_curves:
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

	import warnings; warnings.warn("Deprecated since version 21.1.0. Use  window.get_curves() instead.", DeprecationWarning)

def CurvesFromAdvFilters(window_name: str) -> object:

	"""

	Collect curves of a 2d window specified by its name through some advanced filters. The execution of the script will stop and the Advanced Filter window will open for the user to specify the filters interactively.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curveplot2d.AdvFiltersOnCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    collected_curves = plot2d.CurvesFromAdvFilters(window_name)
		    for c in collected_curves:
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

def CurvesListToDict(list_curves: object) -> object:

	"""

	This function constructs a dictionary from a given list with Curve objects.

	Parameters
	----------
	list_curves : object
		List with Python objects of class Curve.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the curve and data the corresponding object of class Curve. If curves with the same id exist in the given list, then only the first curve will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    list_curves = plot2d.CurvesOfWindow(window_name)
		    dict_curves = plot2d.CurvesListToDict(list_curves)
		    for curve_id, curve_object in dict_curves.items():
		        print(curve_id)
		        print(
		            curve_object.id,
		            curve_object.name,
		            curve_object.plot_id,
		            curve_object.visible,
		            curve_object.selected,
		            curve_object.window_name,
		            curve_object.page_id,
		            curve_object.command,
		            curve_object.entity_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesOfGroup(group_name: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.CurveGroup.get_curves` instead.


	This function searches for the curves of a group with a given name for a given 2d plot window.

	Parameters
	----------
	group_name : str
		Name of the group.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one curve of the given group of the specified window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "MyGroup"
		    group_curves = plot2d.CurvesOfGroup(window_name, group_name)
		    for c in group_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.CurveGroup.get_curves instead.", DeprecationWarning)

def CurvesOfOverlayRun(overlay_run_id: int, overlay_run_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.overlay.Overlay.get_curves` instead.


	This function searches for the curves of an overlay run with a given type and a id.

	Parameters
	----------
	overlay_run_id : int
		Id of the overlay run

	overlay_run_type : str
		Type of the overlay run. Possible values are:
		- 'session'
		- 'project'.

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is an object of class Curve referring to one curve of the given overlay run.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    overlay_run_type = "session"
		    overlay_run_id = 1
		    overlay_run_curves = plot2d.CurvesOfOverlayRun(overlay_run_type, overlay_run_id)
		    for c in overlay_run_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.overlay.Overlay.get_curves instead.", DeprecationWarning)

def CurvesOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curves` instead.


	This function collects all curves of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_curves = plot2d.CurvesOfPlot(window_name, plot_id)
		    for c in plot_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curves instead.", DeprecationWarning)

def CurvesOfWindow(window_name: str, all_plots: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_curves` instead.


	This function collects all curves of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	all_plots : int, optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_curves = plot2d.CurvesOfWindow(window_name)
		    for c in plot_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_curves instead.", DeprecationWarning)

def CurvesTypesAbaqus(filename: str) -> object:

	"""

	This function finds curves types of an ABAQUS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with integers referring to the numbers of steps.
		In position 2, internal lists contain a list with strings referring to the ids of the the entities.
		In position 3, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesAbaqus

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Abaqus1.odb"
		    curves_types = plot2d.CurvesTypesAbaqus(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        steps = one_type[1]  # List with steps
		        for one_step in steps:  # Number of step
		            print(one_step)
		        print(
		            "----------------------------------------------------------------------------------"
		        )
		        entities = one_type[2]  # List with entities
		        for one_entity in entities:  # Id of entity
		            print(one_entity)
		        print(
		            "----------------------------------------------------------------------------------"
		        )
		        variables = one_type[3]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("#########################################")
		
		        # The results of this function can be used as arguments in function "LoadCurvesAbaqus"
		        # plot2d.LoadCurvesAbaqus('Window1',0,filename,type,steps,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesAbaqusWithNames(filename: str) -> object:

	"""

	This function finds curves types of an ABAQUS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with integers referring to the numbers of steps.
		In position 2, internal lists contain a list which contains in position 0 the id of the entity and in position 1 the name of the entity.
		In position 3, internal lists contain a list with strings referring to the variables (user defined variables are included).
		In position 4, internal lists contain a list with matrices referring to the A/LC points used.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Abaqus1.odb"
		    curves_types = plot2d.CurvesTypesAbaqusWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        steps = one_type[1]  # List with steps
		        for one_step in steps:  # Number of step
		            print(one_step)
		        entities = one_type[2]  # List with entities
		        for one_entity in entities:
		            entity_id = one_entity[0]  # Id of entity
		            print(entity_id)
		            entity_name = one_entity[1]  # Name of entity
		            print(entity_name)
		        variables = one_type[3]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        alc_points = one_type[4]  # List with A/LC Points
		        for one_alc_point in alc_points:
		            print(one_alc_point)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesAbf(filename: str) -> object:

	"""

	This function finds curves types of an ABF file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the entities (requests).
		In position 2, internal lists contain a list with strings referring to the variables (components).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesAbf

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/abf.abf"
		    curves_types = plot2d.CurvesTypesAbf(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        requests = one_type[1]  # List with entities
		        for one_request in requests:  # Entity
		            print(one_request)
		        print("-------------------------------------------------------------")
		        components = one_type[2]  # List with variables
		        for one_component in components:  # Name of component
		            print(one_component)
		        print("###############################")
		
		        # The results of this function can be used as arguments in function "LoadCurvesAbf"
		        # plot2d.LoadCurvesAbf('Window1',0,filename,type,requests,components)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesAscii(filename: str) -> object:

	"""

	This function finds curves types of a COLUMN ASCII file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain an integer referring to one data block of the file.
		In position 1, internal lists contain a list with integers referring to the possible selections for the X values.
		In position 2, internal list contain a list with integers referring to the possible selections for the Y values.
		In position 3, internal matrices contain a list with integers referring to the possible selection for the Y phase values.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesAsciiColumn, plot2d.LoadCurvesAsciiTimestep

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/csv.dat"
		    curves_types = plot2d.CurvesTypesAscii(filename)
		    for one_type in curves_types:
		        data_block = one_type[0]  # One data block
		        print(data_block)
		        print("****")
		        all_x = one_type[1]  # List with columns for X data
		        for col_x in all_x:  # X values column
		            print(col_x)
		        print("-------------------------------------------------------------")
		        all_y = one_type[2]  # List with columns for Y data
		        for col_y in all_y:  # Y values column
		            print(col_y)
		        print("-------------------------------------------------------------")
		        all_yphase = one_type[3]  # List with columns for Y phase data
		        for col_yphase in all_yphase:  # Y phase values column
		            print(col_yphase)
		        print("##############################")
		
		        # The results of this function can be used as arguments in functions "LoadCurvesAsciiColumn" and "LoadCurvesAsciiTimestep"
		        # data_blocks = list()
		        # data_blocks.append(data_block)
		        # plot2d.LoadCurvesAsciiColumn('Window1',0,filename,data_blocks,all_x[0],all_y[1],all_yphase[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesDiadem(filename: str) -> object:

	"""

	This function finds curve types of a DIAdem file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of a channel of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesDiadem

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Diadem.dat"
		    channels = plot2d.CurvesTypesDiadem(filename)
		    for channel_name in channels:
		        print(channel_name)  # Name of channel
		    # The results of this function can be used as arguments in function "LoadCurvesDiadem"
		    # plot2d.LoadCurvesDiadem('Window1',0,filename,channels)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesDyna(filename: str) -> object:

	"""

	This function finds curves types of a DYNA file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the entities.
		In position 2, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesDyna

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/binout"
		    curves_types = plot2d.CurvesTypesDyna(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        entities = one_type[1]  # List with entities ids
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "------------------------------------------------------------------------------------"
		        )
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print("##########################################")
		    # The results of this function can be used as arguments in function "LoadCurvesDyna"
		    # plot2d.LoadCurvesDyna('Window1',0,filename,type,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesDynaWithNames(filename: str) -> object:

	"""

	This function finds curves types of a DYNA file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list which contains in position 0 the id of the entity and in position 1 the name of the entity.
		In position 2, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/binout"
		    curves_types = plot2d.CurvesTypesDynaWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        entities = one_type[1]  # List with entities ids
		        for one_entity in entities:
		            entity_id = one_entity[0]  # Id of entity
		            print(entity_id)
		            entity_name = one_entity[1]  # Name of entity
		            print(entity_name)
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesHdf(filename: str) -> object:

	"""

	This function finds curves types of a HDF file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the datasets of the curves.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesHdf

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/HDF.hdf"
		    datasets = plot2d.CurvesTypesHdf(filename)
		    for one_dataset in datasets:
		        print(one_dataset)  # Dataset
		    # The results of this function can be used as arguments in function "LoadCurvesHdf"
		    # plot2d.LoadCurvesHdf('Window1',0,filename,datasets)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesIso(filename: str) -> object:

	"""

	This function finds curve types of an ISO file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the id of a channel of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesIso

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/05283.mme"
		    channels = plot2d.CurvesTypesIso(filename)
		    for channel_id in channels:
		        print(channel_id)  # Id of channel
		    # The results of this function can be used as arguments in function "LoadCurvesIso"
		    # plot2d.LoadCurvesIso('Window1',0,filename,channels)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesKeyword(filename: str) -> object:

	"""

	This function finds curves types of a KEYWORD ascii file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of a curve of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesKeyword

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/KeywordASCII.txt"
		    all_names = plot2d.CurvesTypesKeyword(filename)
		    for name in all_names:
		        print(name)  # Name of curve
		    # The results of this function can be used as arguments in function "LoadCurvesKeyword"
		    # plot2d.LoadCurvesKeyword('Window1',0,filename,all_names)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesMadymo(filename: str) -> object:

	"""

	This function finds curve types of a MADYMO file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list which contains 2 other lists with the types of curves of the given file.
		List in position 0 contains strings referring to the name of the entities.
		List in position 1 contains strings referring to the name of the variables.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesMadymo

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Madymo.dat"
		    curves_types = plot2d.CurvesTypesMadymo(filename)
		    entities = curves_types[0]  # List with entities names
		    for one_entity in entities:
		        print(one_entity)  # Name of entity
		    print("##############################################")
		    variables = curves_types[1]  # List with variables
		    for one_variable in variables:
		        print(one_variable)  # Name of variable
		    # The results of this function can be used as arguments in function "LoadCurvesMadymo"
		    # plot2d.LoadCurvesMadymo('Window1',0,filename,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesNastran(filename: str) -> object:

	"""

	This function finds curves types of a NASTRAN file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 6 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the type of data of the X axis.
		In position 2, internal lists contain a list with integers referring to the cycles of the model.
		In position 3, internal lists contain a list with integers referring to the states of the model.
		In position 4, internal lists contain a list with strings referring to the ids of the entities.
		In position 5, internal matrices contain a list with strings referring to the variables.
		In position 6, internal matrices contain a list with strings referring to the fluid grids.
		In position 7, internal matrices contain a list with strings referring to the subcase states.
		In position 8, internal matrices contain a list with matrices referring to the A/LC points used.
		Fluid grids are taken into account only for some specific types (e.g. 'panelparticipationfactors', 'fluidmodalparticipationfactors', 'structuremodalparticipationfactors', 'normalizedgridparticipationfactors').
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesNastran

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Nastran.pch"
		    curves_types = plot2d.CurvesTypesNastran(filename)
		    for one_type in curves_types:
		        type = one_type[0]
		        print(type)  # One type of curves
		        print("****")
		        all_xaxis = one_type[1]  # List with types of X axis data
		        for xaxis in all_xaxis:
		            print(xaxis)  # Type of X axis data
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        cycles = one_type[2]  # List with cycles
		        for one_cycle in cycles:
		            print(one_cycle)  # Number of cycle
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        states = one_type[3]  # List with states
		        for one_state in states:
		            print(one_state)  # Number of state
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        entities = one_type[4]  # List with entities
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        variables = one_type[5]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        fluidgrids = one_type[6]  # List with fluid grids
		        for one_fluidgrid in fluidgrids:
		            print(one_fluidgrid)
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        subcase_states = one_type[7]  # List with subcase states
		        for one_state in subcase_states:
		            print(one_state)
		        print(
		            "-------------------------------------------------------------------------------------"
		        )
		        alc_points = one_type[8]  # List with A/LC Points
		        for one_alc_point in alc_points:
		            print(one_alc_point)
		        print("###########################################")
		    # The results of this function can be used as arguments in function "LoadCurvesNastran"
		    # plot2d.LoadCurvesNastran('Window1',0,filename,all_xaxis[0],type,cycles,states,entities,variables,fluidgrids)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesNastranXYPunch(filename: str) -> object:

	"""

	This function finds curves types of a NASTRAN XY PUNCH file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to the id of a data block of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesNastranXYPunch

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/NastranXY.pch"
		    data_blocks = plot2d.CurvesTypesNastranXYPunch(filename)
		    for block_id in data_blocks:
		        print(block_id)  # Id of data block
		    # The results of this function can be used as arguments in function "LoadCurvesNastran"
		    # plot2d.LoadCurvesNastranXYPunch('Window1',0,filename,data_blocks)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesPamcrash(filename: str) -> object:

	"""

	This function finds curves types of a PAMCRASH file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the entities.
		In position 2, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesPamcrash

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/PAM.thp"
		    curves_types = plot2d.CurvesTypesPamcrash(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        entities = one_type[1]  # List with entities ids
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "----------------------------------------------------------------------------------------"
		        )
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print("############################################")
		    # The results of this function can be used as arguments in function "LoadCurvesPamcrash"
		    # plot2d.LoadCurvesPamcrash('Window1',0,filename,type,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesPamcrashWithNames(filename: str) -> object:

	"""

	This function finds curves types of a PAMCRASH file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list which contains in position 0 the id of the entity and in position 1 the name of the entity.
		In position 2, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/PAM.thp"
		    curves_types = plot2d.CurvesTypesPamcrashWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        entities = one_type[1]  # List with entities ids
		        for one_entity in entities:
		            entity_id = one_entity[0]  # Id of entity
		            print(entity_id)
		            entity_name = one_entity[1]  # Name of entity
		            print(entity_name)
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesPamview(filename: str) -> object:

	"""

	This function finds curve types of a PAMVIEW file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to the name of a curve of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesPamview

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/PamView1.pv"
		    all_names = plot2d.CurvesTypesPamview(filename)
		    for name in all_names:
		        print(name)  #  Name of curve
		    # The results of this function can be used as arguments in function "LoadCurvesPamview"
		    # plot2d.LoadCurvesPamview('Window1',0,filename,all_names)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesRadioss(filename: str) -> object:

	"""

	This function finds curves types of a RADIOSS file.

	Parameters
	----------
	filename : str
		Path to file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with integers referring to the ids of time history blocks of the entities (0 for "global" and "part").
		In position 2, internal lists contain a list with strings referring to the ids of the entities.
		In position 3, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesRadioss

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/RadiossT01"
		    curves_types = plot2d.CurvesTypesRadioss(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        time_history = one_type[1]  # Matrix with time history numbers
		        print("****")
		        for th in time_history:
		            print(th)  # Number of time history
		        print(
		            "------------------------------------------------------------------------------"
		        )
		        entities = one_type[2]  # List with entities ids
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "------------------------------------------------------------------------------"
		        )
		        variables = one_type[3]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print("#######################################")
		    # The results of this function can be used as arguments in function "LoadCurvesRadioss"
		    # plot2d.LoadCurvesRadioss('Window1',0,filename,type,time_history,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesRadiossWithNames(filename: str) -> object:

	"""

	This function finds curves types of a RADIOSS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with integers referring to the ids of time history blocks of the entities (0 for "global" and "part").
		In position 2, internal lists contain another list which contains in position 0 the id of the entity and in position 1 the name of the entity.
		In position 3, internal lists contain a list with strings referring to the variables (user defined variables are included).
		In position 4, internal lists contain a list with matrices referring to the A/LC points used.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/RadiossT01"
		    curves_types = plot2d.CurvesTypesRadiossWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        time_history = one_type[1]  # Matrix with time history numbers
		        for th in time_history:
		            print(th)  # Number of time history
		        entities = one_type[2]  # List with entities ids
		        for one_entity in entities:
		            entity_id = one_entity[0]  # Id of entity
		            print(entity_id)
		            entity_name = one_entity[1]  # Name of entity
		            print(entity_name)
		        variables = one_type[3]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        alc_points = one_type[4]  # List with A/LC Points
		        for one_alc_point in alc_points:
		            print(one_alc_point)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesRpc(filename: str) -> object:

	"""

	This function finds curve types of a RPC file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list where each member of the list is an integer referring to the id of a channel of the given file.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesRpc

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/rpc.rsp"
		    channels = plot2d.CurvesTypesRpc(filename)
		    for channel_id in channels:
		        print(channel_id)  # Id of channel
		    # The results of this function can be used as arguments in function "CurvesTypesRpc"
		    # plot2d.LoadCurvesRpc('Window1',0,filename,channels)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesUnv(filename: str) -> object:

	"""

	This function finds curves types of a UNIVERSAL file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with integers referring to the numbers of loadcases.
		In position 2, internal lists contain a list with strings referring to the reference nodes.
		In position 3, internal lists contain a list with strings referring to the response nodes.
		In position 4, internal lists contain a list with strings referring to the reference nodes names.
		In position 5, internal lists contain a list with strings referring to the response nodes names.
		In position 6, internal lists contain a list with matrices referring to the A/LC points used.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesUnv

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/unv.dat"
		    curves_types = plot2d.CurvesTypesUnv(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        loadcases = one_type[1]  # List with loadcases
		        for one_loadcase in loadcases:
		            print(one_loadcase)  # Number of loadcase
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        reference_nodes = one_type[2]  # List with reference nodes
		        for ref_node in reference_nodes:
		            print(ref_node)  # Reference node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        responce_nodes = one_type[3]  # List with responce nodes
		        for resp_node in responce_nodes:
		            print(resp_node)  # Responce node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        reference_nodes_names = one_type[4]  # List with reference nodes names
		        for ref_node_name in reference_nodes_names:
		            print(ref_node_name)  # Reference node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        responce_nodes_names = one_type[5]  # List with responce nodes names
		        for resp_node_name in responce_nodes_names:
		            print(resp_node_name)  # Responce node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        alc_points = one_type[6]  # List with A/LC Points
		        for one_alc_point in alc_points:
		            print(one_alc_point)
		        print("###############################################")
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeactivatePlot(window_name: str, plot_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.deactivate` instead.


	This function deactivates a plot of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    ret = plot2d.DeactivatePlot(window_name, plot_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.deactivate instead.", DeprecationWarning)

def DeleteCurve(window_name: str, curve_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.delete` instead.


	This function allows the user to delete a curve of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.DeleteSomeCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    ret = plot2d.DeleteCurve(window_name, curve_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.delete instead.", DeprecationWarning)

def DeleteSomeCurves(window_name: str, curve_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.delete_curves` instead.


	This function allows the user to delete some specific curves of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window

	curve_ids : object
		List with Ids of the curves.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curves = plot2d.CurvesOfWindow(window_name)
		    curve_ids = list()
		    if len(curves) >= 4:
		        for i in range(1, 3):
		            curve_ids.append(curves[i].id)
		    ret = plot2d.DeleteSomeCurves(window_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.delete_curves instead.", DeprecationWarning)

def DeselectCurve(window_name: str, curve_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.deselect` instead.


	This function allows the user to deselect a curve of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.DeselectSomeCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 5
		    ret = plot2d.DeselectCurve(window_name, curve_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.deselect instead.", DeprecationWarning)

def DeselectPoint(window_name: str, curve_id: int, point_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.deselect` instead.


	This function allows the user to deselect a point of a curve of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.DeselectSomePoints

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 10
		    point_id = 1086
		    ret = plot2d.DeselectPoint(window_name, curve_id, point_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.deselect instead.", DeprecationWarning)

def DeselectSomeCurves(window_name: str, curve_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.deselect_curves` instead.


	This function allows the user to deselect some specific curves of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_ids : object
		List with  Ids of the curves.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_ids = list()
		    for i in range(5, 15):
		        curve_ids.append(i)
		    ret = plot2d.DeselectSomeCurves(window_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.deselect_curves instead.", DeprecationWarning)

def DeselectSomePoints(window_name: str, curve_id: int, point_ids: object) -> int:

	"""

	This function allows the user to deselect some specific points of a curve of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_ids : object
		List with Ids of the points.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_ids = list()
		    all_points = plot2d.PointsOfCurve(window_name, curve_id)
		    for pnt in all_points:
		        point_ids.append(pnt.id)
		    ret = plot2d.DeselectSomePoints(window_name, curve_id, point_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def FilterPointsOfCurve(curve_id: int, curve_type: str, max_x: float, max_y: float, min_x: float, min_y: float, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.meta.plot2d.Curve.get_filtered_points` instead.


	This function collects all points of a given curve with their X and Y coordinates being among the range of values specified by the given arguments.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	max_x : float
		Maximum acceptable value for X coordinate.

	max_y : float
		Maximum acceptable value for Y coordinate.

	min_x : float
		Minimum acceptable value for X coordinate.

	min_y : float
		Minimum acceptable value for Y coordinate.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific point of the given curve.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    min_x = 0
		    max_x = 60
		    min_y = -200
		    max_y = 0
		    filtered_points = plot2d.FilterPointsOfCurve(
		        window_name, curve_id, min_x, max_x, min_y, max_y
		    )
		    for pnt in filtered_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.meta.plot2d.Curve.get_filtered_points instead.", DeprecationWarning)

def FooterOfPlot(plot_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Footer.get_text` instead.


	This function finds the footer of a given plot.

	Parameters
	----------
	plot_id : int
		Plot id.

	window_name : str
		Window name.

	Returns
	-------
	str
		Upon success, it returns the footer of the given plot.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    footer = plot2d.FooterOfPlot(window_name, plot_id)
		    print(footer)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Footer.get_text instead.", DeprecationWarning)

def GetRadiossTimeHistoryId(filename: str, entity_id_name: str, entity_type: str, variable: str) -> int:

	"""

	This function finds time history id for an entity of a RADIOSS file.

	Parameters
	----------
	filename : str
		Name of the file.

	entity_id_name : str
		Id or name of the entity.

	entity_type : str
		Type of the entity.

	variable : str
		Name of variable.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the time history id.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/RadiossT01"
		    entity_id_name = "800320"
		    entity_type = "node"
		    variable = "dz"
		    th_id = plot2d.GetRadiossTimeHistoryId(
		        filename, entity_id_name, entity_type, variable
		    )
		    print(th_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def HideCurve(window_name: str, curve_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.hide` instead.


	This function allows the user to hide a curve of a given 2d plot window .

	Parameters
	----------
	window_name : str
		Window name.

	curve_id : int
		Curve id.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.HideSomeCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    ret = plot2d.HideCurve(window_name, curve_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.hide instead.", DeprecationWarning)

def HideSomeCurves(window_name: str, curve_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.hide_curves` instead.


	This function allows the user to hide some specific curves of a 2d plot window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_ids : object
		List with Ids of the curves.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_ids = list()
		    all_curves = plot2d.CurvesOfWindow(window_name)
		    for c in all_curves:
		        curve_ids.append(c.id)
		    ret = plot2d.HideSomeCurves(window_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.hide_curves instead.", DeprecationWarning)

def IsComplexCurve(curve_id: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.is_complex` instead.


	This function checks whether a curve of a 2d plot window with a given id (curve_id) is complex.

	Parameters
	----------
	curve_id : str
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 if curve is complex, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    if plot2d.IsComplexCurve(window_name, curve_id):
		        print("This is a complex curve")
		    else:
		        print("This is NOT a complex curve")
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.is_complex instead.", DeprecationWarning)

def IsCurve(curve: object) -> int:

	"""

	This function checks whether an object is of class Curve.

	Parameters
	----------
	curve : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class Curve, 0 otherwise.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		from meta import utils
		from meta import models
		
		
		def main():
		    window_name = "Window1"
		    all_entities = list()
		    all_entities.append("A string")
		    all_entities.append(plot2d.Curves()[0])
		
		    for ent in all_entities:
		        if plot2d.IsCurve(ent):
		            c = ent
		            print("This is an object of class Curve")
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
		        else:
		            print("This is NOT an object of class Curve")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsCurveGroup(curve_group: object) -> int:

	"""

	This function checks whether an object is of class CurveGroup.

	Parameters
	----------
	curve_group : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class CurveGroup, 0 otherwise.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    CurveGroups = plot2d.CurveGroups()
		    for cg in CurveGroups:
		        if plot2d.IsCurveGroup(cg):
		            print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsPlot(plot: object) -> int:

	"""

	This function checks whether an object is of class Plot.

	Parameters
	----------
	plot : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class Plot, 0 otherwise.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_obj = plot2d.PlotById(window_name, plot_id)
		    entities = list()
		    entities.append(plot_obj)
		    entities.append("A string")
		    for ent in entities:
		        if plot2d.IsPlot(ent):
		            pl = ent
		            print("This is an object of class Plot")
		            print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		        else:
		            print("This is NOT an object of class Plot")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsPlotAxis(plot_axis: object) -> int:

	"""

	This function checks whether an object is of class PlotAxis.

	Parameters
	----------
	plot_axis : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class PlotAxis, 0 otherwise.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    ent = plot2d.PlotAxisOfPlotById(window_name, plot_id, axis_type, axis_id)
		    if plot2d.IsPlotAxis(ent):
		        plax = ent
		        print("This is an object of class PlotAxis")
		        print(
		            plax.id,
		            plax.type,
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


	"""

def IsPlotModel(plot_model: object) -> int:

	"""

	This function checks whether an object is of class PlotModel.

	Parameters
	----------
	plot_model : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class PlotModel, 0 otherwise.

	See Also
	--------
	plot2d.PlotModel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_model_id = 1
		    plot_model_deck = "DYNA"
		    ent = plot2d.PlotModelById(plot_model_id, plot_model_deck)
		    if plot2d.IsPlotModel(ent):
		        pmod = ent
		        print("This is an object of class PlotModel")
		        print(pmod.id, pmod.deck, pmod.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsPoint(point: object) -> int:

	"""

	This function checks whether an object is of class Point.

	Parameters
	----------
	point : object
		Any given object.

	Returns
	-------
	int
		It returns 1 if the given object is of class Point, 0 otherwise.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 2
		    ent = plot2d.PointById(window_name, curve_id, point_id)
		    if plot2d.IsPoint(ent):
		        pnt = ent
		        print("This is an object of class Point")
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LabelOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_label` instead.


	This function finds the label of a plot axis of a given plot with a given id.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	str
		Upon success, it returns a string referring to the label of the specified plot axis.
		Else, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    axis_label = plot2d.LabelOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(axis_label)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_label instead.", DeprecationWarning)

def LineStyleOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_line_style` instead.


	This function finds the line style of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the line style of the corresponding curve. Line style is an integer number in the range of 0 and 13, which is the same being used in META commands for changing line style of curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    line_style = plot2d.LineStyleOfCurve(window_name, curve_id)
		    print(line_style)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_line_style instead.", DeprecationWarning)

def LineWidthOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_line_width` instead.


	This function finds the line width of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the line width of the corresponding curve. Line width is an integer number in the range of 0 and 10.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    line_width = plot2d.LineWidthOfCurve(window_name, curve_id)
		    print(line_width)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_line_width instead.", DeprecationWarning)

def LoadCurvesAbaqus(window_name: str, plot_id: int, filename: str, type: str, steps: object, entities: object, variables: object) -> object:

	"""

	This function loads curves from an ABAQUS file in an existing plot of a given 2d plot window. Plot is specified by its number-id. File is specified by its path (filename). Argument "type" refers to the type of data which are going to be loaded (e.g. 'WholeModel', 'Centroid', 'SurfaceFacet', 'IntegrationPoint' etc.). Argument "steps" is a list whose memberrs are integers referring to the numbers of steps. If list "steps" contain a value equal to -1, then all steps will be loaded. If the 1st member of argument steps is 'all', then curves of all steps are loaded. Argument "entities" is a list whose members are strings referring to the ids of entities or name for 'WholeModel' (e.g. Assembly Assembly-1). If the 1st member of argument entities is 'all', then curves of all entities are loaded. Argument "variables" is a list whose members are strings referring to the variables which are going to be loaded (e.g. 'ALLQB', 'ALLWK', 'ETOTAL' 'ALLSD', 'ALLS', 'ALLVD', 'ALLCD', 'ALLJD' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data.

	steps : object
		List with steps.

	entities : object
		List with entities.

	variables : object
		List with variables.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Abaqus1.odb"
		    type = "Nodal"
		    steps = [1]
		    entities = ["18373"]
		    variables = ["U1", "U2", "U3", "UM"]
		    new_curves = plot2d.LoadCurvesAbaqus(
		        window_name, plot_id, filename, type, steps, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesAbf(window_name: str, plot_id: int, filename: str, type: str, requests: object, components: object) -> object:

	"""

	This function loads curves from a ABF file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data.

	requests : object
		List with entities. If the 1st member of argument requests is 'all', then curves of all entities are loaded.

	components : object
		List with variables. If the 1st member of argument components is 'all', then curves of all components are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/abf.abf"
		    type = "NWM"
		    requests = ["NEKU, X axis Veh1 Loc 01, #10"]
		    components = ["NWM"]
		    new_curves = plot2d.LoadCurvesAbf(
		        window_name, plot_id, filename, type, requests, components
		    )
		    for c in new_curves:
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

def LoadCurvesAsciiColumn(window_name: str, plot_id: int, filename: str, data_blocks: object, col_x: int, col_y: int, col_yphase: int) -> object:

	"""

	This function loads curves from a COLUMN ASCII file in an existing plot of a given 2d plot window.
	
	Argument "col_x" refers to the number of column from which X values will be retrieved. Argument "col_y" refers to the number of column from which Y values will be retrieved. Optional argument "col_yphase" refers to the number of column from which Y phase values will be retrieved. If optional argument "col_yphase" is absent, no complex curves will be created.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	data_blocks : object
		List with the data blocks (integers). If the 1st member of argument data_blocks is 'all', then curves of all data blocks are loaded.

	col_x : int
		Column number of X values.

	col_y : int
		Column number of Y values.

	col_yphase : int, optional
		Column number of Y phase values. If it is not specified, no complex curves will be created.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/csv.dat"
		    data_blocks = [0]
		    col_x = 1
		    col_y = 2
		    new_curves = plot2d.LoadCurvesAsciiColumn(
		        window_name, plot_id, filename, data_blocks, col_x, col_y
		    )
		    for c in new_curves:
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

def LoadCurvesAsciiTimestep(window_name: str, plot_id: int, filename: str, data_blocks: object, start_time: float, timestep: float, col_y: int, col_yphase: int) -> object:

	"""

	This function loads curves with timestep from a COLUMN ASCII file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	data_blocks : object
		List with the data blocks (integers). If the 1st member of argument data_blocks is 'all', then curves of all data blocks are loaded.

	start_time : float
		Start time.

	timestep : float
		Timestep.

	col_y : int
		Column number of Y values.

	col_yphase : int, optional
		Column number of Y phase values. If it is not specified, no complex curves will be created.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/csv.dat"
		    data_blocks = [0]
		    start_time = 0
		    timestep = 0.002
		    col_y = 2
		    new_curves = plot2d.LoadCurvesAsciiTimestep(
		        window_name, plot_id, filename, data_blocks, start_time, timestep, col_y
		    )
		    for c in new_curves:
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

def LoadCurvesDiadem(window_name: str, plot_id: int, filename: str, channels: object) -> object:

	"""

	This function loads curves from a DIAdem file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	channels : object
		List with channels. If the 1st member of argument channels is 'all', then curves of all channels are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Diadem2.dat"
		    channels = ["ArgyChannel"]
		    new_curves = plot2d.LoadCurvesDiadem(window_name, plot_id, filename, channels)
		    for c in new_curves:
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

def LoadCurvesDyna(window_name: str, plot_id: int, filename: str, type: str, entities: object, variables: object) -> object:

	"""

	This function loads curves from a LS-DYNA file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data.

	entities : object
		List with entities strings. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		List with variables strings. If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/binout"
		    type = "nodout-Node"
		    entities = ["34913", "34830"]
		    variables = ["X displacement (xd)", "Y displacement (yd)", "Z displacement (zd)"]
		    new_curves = plot2d.LoadCurvesDyna(
		        window_name, plot_id, filename, type, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesHdf(window_name: str, plot_id: int, filename: str, datasets: object) -> object:

	"""

	This function loads curves from a HDF file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	datasets : object
		List with the datasets strings to be loaded. If the 1st member of argument datasets is 'all', then curves of all datasets are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/HDF.hdf"
		    datasets = ["#Data-Set-10"]
		    new_curves = plot2d.LoadCurvesHdf(window_name, plot_id, filename, datasets)
		    for c in new_curves:
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

def LoadCurvesIso(window_name: str, plot_id: int, filename: str, channels: object) -> object:

	"""

	This function loads curves from an ISO file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	channels : object
		List of integers with channel-ids. If the 1st member of argument channels is 'all', then curves of all channels are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/05283.mme"
		    channels = [1, 2, 3, 4]
		    new_curves = plot2d.LoadCurvesIso(window_name, plot_id, filename, channels)
		    for c in new_curves:
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

def LoadCurvesKeyword(window_name: str, plot_id: int, filename: str, curves: object) -> object:

	"""

	This function loads curves from a KEYWORD ASCII file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	curves : object
		List with curves names as strings. If the 1st member of argument curves is 'all', then all curves are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/KeywordASCII.txt"
		    curves = ["Internal Energy"]
		    new_curves = plot2d.LoadCurvesKeyword(window_name, plot_id, filename, curves)
		    for c in new_curves:
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

def LoadCurvesMadymo(window_name: str, plot_id: int, filename: str, entities: object, variables: object) -> object:

	"""

	This function loads curves from a MADYMO file in an existing plot of a given 2d plot window. Argument "variables" is a list whose members are strings referring to the variables which are going to be loaded (e.g. "X-comp. displacement (m)", "Displacement (m)" etc.). 

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	entities : object
		List with entities. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		List with variables. If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Madymo.dat"
		    entities = ["Entity1", "Entity2"]
		    variables = ["all"]
		    new_curves = plot2d.LoadCurvesMadymo(
		        window_name, plot_id, filename, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesOp2(window_name: str, plot_id: int, filename: str, xaxis: str, type: str, cycles: object, states: object, entities: object, variables: object, fluid_grid: int) -> object:

	"""

	This function loads curves from a NASTRAN file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	xaxis : str
		Type of x-axis data which are going to be loaded (e.g. 'subcase', 'time', 'mode', 'frequency', 'loadstep' etc.).

	type : str
		Type of data which are going to be loaded (e.g. 'displacement', 'acceleration', 'velocity' etc.).

	cycles : object
		A list whose members are integers referring to the cycles of the model. If the 1st member of argument cycles is 'all', then curves of all cycles are loaded.

	states : object
		A list whose members are integers referring to the states of the model. If the 1st member of argument states is 'all', then curves of all cycles are loaded.

	entities : object
		A list whose members are strings referring to the ids of the entities which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		a list whose members are strings referring to the variables which are going to be loaded (e.g. 'pressure', 'dba', 'dbb', 'dbc' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	fluid_grid : int, optional
		Id of the fluid grid node. It is taken into account only for specific types (e.g. 'normalizedgridparticipationfactors', 'panelparticipationfactors', 'fluidmodalparticipationfactors', 'structuremodalparticipationfactors'). If it is absent then curves for all fluid grids will be created.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Nastran.op2"
		    type = "stresses"
		    xaxis = "frequency"
		    cycles = ["all"]
		    states = ["all"]
		    entities = ["Tetra 77937"]
		    variables = ["von_mises"]
		    new_curves = plot2d.LoadCurvesOp2(
		        window_name, plot_id, filename, xaxis, type, cycles, states, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesNastranXYPunch(window_name: str, plot_id: int, filename: str, data_blocks: object) -> object:

	"""

	This function loads curves from a NASTRAN XY PUNCH file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	data_blocks : object
		A list whose members are integers referring to the data blocks of the file which are going to be loaded. If the 1st member of argument data_blocks is 'all', then curves of all data blocks are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/NastranXY.pch"
		    data_blocks = [1, 3, 5, 7]
		    new_curves = plot2d.LoadCurvesNastranXYPunch(
		        window_name, plot_id, filename, data_blocks
		    )
		    for c in new_curves:
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

def LoadCurvesPamcrash(window_name: str, plot_id: int, filename: str, type: str, entities: object, variables: object) -> object:

	"""

	This function loads curves from a PAMCRASH file in an existing plot of a given 2d plot2d window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which to load (e.g. 'global', 'part', 'contact', 'rwall' etc.).

	entities : object
		A list whose members are strings referring to the ids of the entities which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		A list whose members are strings referring to the variables which are going to be loaded (e.g. 'Z Force (fz)', 'Time step (step)' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/PAM.thp"
		    type = "node"
		    entities = ["180023", "182212"]
		    variables = ["xacc", "yacc", "zacc"]
		    new_curves = plot2d.LoadCurvesPamcrash(
		        window_name, plot_id, filename, type, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesPamview(window_name: str, plot_id: int, filename: str, curves: object) -> object:

	"""

	This function loads curves from a PAMVIEW file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	curves : object
		A list whose members are strings referring to the curves which are going to be loaded. If the 1st member of argument curves is 'all', then all curves are loaded.

	Returns
	-------
	object
		It returns a list wwhere each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/PamView1.pv"
		    curves = ["all"]
		    new_curves = plot2d.LoadCurvesPamview(window_name, plot_id, filename, curves)
		    for c in new_curves:
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

def LoadCurvesRadioss(window_name: str, plot_id: int, filename: str, type: str, time_history: object, entities: object, variables: object) -> object:

	"""

	This function loads curves from a RADIOSS file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded (e.g. 'global', 'part', 'node', 'solid', 'shell', 'cyljoint' etc.).

	time_history : object, optional
		A list whose members are integers referring to the ids of the time history block of the entities (0 for 'global' and 'part'). If the 1st member of argument time_history is '*' or 'all', then curves of all time history blocks are loaded.

	entities : object
		A list whose members are strings referring to the ids of the entities which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		A list whose members are strings referring to the variables which are going to be loaded (e.g. 'Spring energy (se)', 'Mass (ma)', 'Z displacement (dz)', 'Normal force (f)', 'Von Mises Stress (vonm)' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/RadiossT01"
		    type = "interface"
		    time_history = ["all"]
		    entities = ["all"]
		    variables = ["X-Normal impulse (inx)"]
		    new_curves = plot2d.LoadCurvesRadioss(
		        window_name, plot_id, filename, type, time_history, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesRpc(window_name: str, plot_id: int, filename: str, channels: object) -> object:

	"""

	This function loads curves from a RPC file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	channels : object
		Argument 'entities' is a list whose members are integers referring to the ids of the channels which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/rpc.rsp"
		    channels = [48, 55, 64]
		    new_curves = plot2d.LoadCurvesRpc(window_name, plot_id, filename, channels)
		    for c in new_curves:
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

def LoadCurvesUnv(window_name: str, plot_id: int, filename: str, type: str, states: object, reference_nodes: object, response_nodes: object) -> object:

	"""

	This function loads curves from a UNIVERSAL file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded (e.g. 'TimeResponse', 'FrequencyResponseFunction', 'Coherence' etc.).

	states : object
		A list whose members are integers referring to the numbers of loadcases. If the 1st member of argument states is 'all', then curves of all states are loaded.

	reference_nodes : object
		A list whose members are strings referring to the reference nodes (e.g. '16+z', '30+x', '0scal' etc.). If the 1st member of argument reference_nodes is 'all', then curves of all reference_nodes are loaded.

	response_nodes : object
		A list whose members are strings referring to the respose nodes (e.g. '1+xt', '1+yt', '3+zt', '1scal' etc.. If the 1st member of argument response_nodes is 'all', then curves of all response_nodes are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/unv.dat"
		    type = "FrequencyResponseFunction"
		    states = [1]
		    reference_nodes = ["all"]
		    response_nodes = ["all"]
		    new_curves = plot2d.LoadCurvesUnv(
		        window_name, plot_id, filename, type, states, reference_nodes, response_nodes
		    )
		    for c in new_curves:
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

def MarkDensityOfCurve(curve_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_mark_density` instead.


	This function finds the mark density of a given curve. Mark density is an integer number in the range of 1 and 99.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns an integer referring to the mark density of the corresponding curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    mark_density = plot2d.MarkDensityOfCurve(window_name, curve_id)
		    print(mark_density)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_mark_density instead.", DeprecationWarning)

def MaxPointXOfCurve(curve_id: int, curve_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function calculates the point of a given curve with the maximum X coordinate.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a Point object referring to the corresponding point of the given curve with the maximum X coordinate.
		Upon failure None is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    max_x_pnt = plot2d.MaxPointXOfCurve(window_name, curve_id, curve_type)
		    if max_x_pnt:
		        print(
		            max_x_pnt.id,
		            max_x_pnt.x,
		            max_x_pnt.y,
		            max_x_pnt.selected,
		            max_x_pnt.curve_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def MaxPointYOfCurve(curve_id: int, curve_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function calculates the point of a given curve with the maximum Y coordinate.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str
		Name of the window

	Returns
	-------
	object
		It returns a Point object referring to the corresponding point of the given curve with the maximum Y coordinate.
		Upon failure None is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    max_y_pnt = plot2d.MaxPointYOfCurve(window_name, curve_id, curve_type)
		    if max_y_pnt:
		        print(
		            max_y_pnt.id,
		            max_y_pnt.x,
		            max_y_pnt.y,
		            max_y_pnt.selected,
		            max_y_pnt.curve_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def MaxScaleLimitOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_scale_limit` instead.


	This function finds the maximum scale limit of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		Upon success, it returns a float referring to the maximum scale limit of the specified plot axis.
		Else, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    max_scale_limit = plot2d.MaxScaleLimitOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id
		    )
		    print(max_scale_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_scale_limit instead.", DeprecationWarning)

def MaxValueOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_value` instead.


	This function finds the maximum value of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		Upon success, it returns a float referring to the maximum value of the specified plot axis.
		Else, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    max_value = plot2d.MaxValueOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(max_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_value instead.", DeprecationWarning)

def MaxValueXOfCurve(window_name: str, curve_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_limit_value_x` instead.


	This function calculates the maximum value of the X coordinates of a given curve of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	float
		It returns a float number referring to the corresponding maximum value of the X-coordinates of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    max_x = plot2d.MaxValueXOfCurve(window_name, curve_id)
		    print(max_x)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_limit_value_x instead.", DeprecationWarning)

def MaxValueYOfCurve(window_name: str, curve_id: int, curve_type: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_limit_value_y` instead.


	This function calculates the maximum value of the Y coordinates of a given curve of a certain window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	float
		It returns a float number referring to the corresponding maximum value of the Y coordinates of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    max_y = plot2d.MaxValueYOfCurve(window_name, curve_id, curve_type)
		    print(max_y)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_limit_value_y instead.", DeprecationWarning)

def MinPointXOfCurve(curve_id: int, curve_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function calculates the point of a given curve with the minimum X coordinate.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a Point object referring to the corresponding point of the given curve with the minimum X coordinate.
		Upon failure None is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    min_x_pnt = plot2d.MinPointXOfCurve(window_name, curve_id, curve_type)
		    if min_x_pnt:
		        print(
		            min_x_pnt.id,
		            min_x_pnt.x,
		            min_x_pnt.y,
		            min_x_pnt.selected,
		            min_x_pnt.curve_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def MinPointYOfCurve(curve_type: str, curve_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function calculates the point of a given curve with the minimum Y coordinate.

	Parameters
	----------
	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a Point object referring to the corresponding point of the given curve with the minimum Y coordinate.
		Upon failure None is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    min_y_pnt = plot2d.MinPointYOfCurve(window_name, curve_id, curve_type)
		    if min_y_pnt:
		        print(
		            min_y_pnt.id,
		            min_y_pnt.x,
		            min_y_pnt.y,
		            min_y_pnt.selected,
		            min_y_pnt.curve_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def MinScaleLimitOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_scale_limit` instead.


	This function finds the minimum scale limit of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		Upon success, it returns a float referring to the minimum scale limit of the specified plot axis.
		Else, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    min_scale_limit = plot2d.MinScaleLimitOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id
		    )
		    print(min_scale_limit)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_scale_limit instead.", DeprecationWarning)

def MinValueOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_value` instead.


	This function finds the minimum value of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		Upon success, it returns a float referring to the minimum value of the specified plot axis.
		Else, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    min_value = plot2d.MinValueOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(min_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_value instead.", DeprecationWarning)

def MinValueXOfCurve(curve_id: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_value_x` instead.


	This function calculates the minimum value of the X coordinates of a given curve of a specified window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float number referring to the corresponding minimum value of the X coordinates of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    min_x = plot2d.MinValueXOfCurve(window_name, curve_id)
		    print(min_x)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_value_x instead.", DeprecationWarning)

def MinValueYOfCurve(curve_id: int, curve_type: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_value_y` instead.


	This function calculates the minimum value of the Y coordinates of a given curve of a specified window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float number referring to the corresponding minimum value of the Y coordinates of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    min_y = plot2d.MinValueYOfCurve(window_name, curve_id, curve_type)
		    print(min_y)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_value_y instead.", DeprecationWarning)

def MultiplierOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_multiplier` instead.


	This function finds the multiplier of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns an integer referring to the multiplier of the specified plot axis.
		Else, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    multiplier = plot2d.MultiplierOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(multiplier)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_multiplier instead.", DeprecationWarning)

def PickCurves(window_name: str, message: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.pick_curves` instead.


	This function allows the user to pick curves from a 2d plot window specified by its name. The execution of the script will stop and it will restart when the middle button mouse or Enter is pressed.

	Parameters
	----------
	window_name : str
		Name of the window.

	message : str
		Message displayed to the user.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific picked curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    message = "Select Curves and press middle mouse button when you are ready"
		    picked_curves = plot2d.PickCurves(window_name, message)
		    for c in picked_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.pick_curves instead.", DeprecationWarning)

def PickPoints(window_name: str, message: str, curve_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.pick_points` instead.


	This function allows the user to pick points and curves from a 2d plot window. The execution of the script will stop and it will restart when Enter is pressed.
	The following actions must be performed once the selection process has begun:
	1. Left-Click on Curve to select a curve.
	2. Middle-Click to confirm selection.
	3. Middle-Click to select the points of the curve.
	4. Enter to exit the function.

	Parameters
	----------
	window_name : str
		Name of the window.

	message : str
		Message displayed to the user.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific picked point.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    message = "1. Left-Click on Curve to select a curve.\\n2. Middle-Click to confirm selection.\\n3. Middle-Click to select the points of the curve.\\n4. Enter to exit the function."
		    curve_type = "real"
		    picked_points = plot2d.PickPoints(window_name, message, curve_type)
		    for pnt in picked_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.pick_points instead.", DeprecationWarning)

def PickPointsAllCurves(window_name: str, message: str, curve_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.pick_points` instead.


	This function allows the user to pick points of all curves from a 2d plot window. The execution of the script will stop and it will restart when Enter or middle mouse button is pressed.
	The following actions must be performed once the selection process has begun:
	1. Middle-Click to select the points of the curve.
	2. Enter to exit the function.

	Parameters
	----------
	window_name : str
		Name of the window.

	message : str
		Message displayed to the user.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific picked point.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    message = "Select Points with MIDDLE-click and press the Enter key when finished."
		    curve_type = "real"
		    picked_points = plot2d.PickPointsAllCurves(window_name, message, curve_type)
		    for pnt in picked_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.pick_points instead.", DeprecationWarning)

def PlotAxes() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects all plot axes of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_axes = plot2d.PlotAxes()
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def PlotAxesById(axis_type: str, axis_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function finds plot axes of a given 2d plot window with a given id.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis_type = "yaxis"
		    axis_id = 0
		    plot_axes = plot2d.PlotAxesById(axis_type, axis_id)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def PlotAxesByType(axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects all plot axes of all 2d plot windows for a specific type.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis_type = "yaxis"
		    plot_axes = plot2d.PlotAxesByType(axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def PlotAxesOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects all plot axes of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_axes = plot2d.PlotAxesOfPlot(window_name, plot_id)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def PlotAxesOfPlotByType(axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects all plot axes of a given plot for a specific type.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    plot_axes = plot2d.PlotAxesOfPlotByType(window_name, plot_id, axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def PlotAxesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects all plot axes of a given plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_axes = plot2d.PlotAxesOfWindow(window_name)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def PlotAxesOfWindowById(window_name: str, axis_type: str, axis_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function finds the plot axes of a given 2d plot window with a given id.

	Parameters
	----------
	window_name : str
		Name of the window.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    axis_type = "yaxis"
		    axis_id = 0
		    plot_axes = plot2d.PlotAxesOfWindowById(window_name, axis_type, axis_id)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def PlotAxesOfWindowByType(window_name: str, axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects all plot axes of a given 2d plot window for a specific type.

	Parameters
	----------
	window_name : str
		Name of the window.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    axis_type = "yaxis"
		    plot_axes = plot2d.PlotAxesOfWindowByType(window_name, axis_type)
		    for plax in plot_axes:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def PlotAxisOfPlotById(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function finds plot axis of a given plot with a given id.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a PlotAxis object of the plot axis with the given id.
		Else, None is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    plax = plot2d.PlotAxisOfPlotById(window_name, plot_id, axis_type, axis_id)
		    if plax:
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def PlotById(window_name: str, plot_id: int) -> object:

	"""

	This function finds a plot of a 2d plot window with a given id.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	Returns
	-------
	object
		Upon success, it returns Plot object with the given id.
		Else, None is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    pl = plot2d.PlotById(window_name, plot_id)
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PlotModelById(plot_model_id: int, plot_model_deck: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_plot_models` instead.


	This function finds plot model with a given id for a given deck.

	Parameters
	----------
	plot_model_id : int
		Id of the plot model.

	plot_model_deck : str
		Deck of the plot model.

	Returns
	-------
	object
		Upon success, it returns PlotModel object with the given id and deck. 
		Else, None is returned.

	See Also
	--------
	plot2d.PlotModel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_model_id = 1
		    plot_model_deck = "NASTRAN"
		    pmod = plot2d.PlotModelById(plot_model_id, plot_model_deck)
		    if pmod:
		        print(pmod.id, pmod.deck, pmod.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_plot_models instead.", DeprecationWarning)

def PlotModels() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_plot_models` instead.


	This function collects all the current loaded plot models.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotModel referring to the corresponding loaded plot model.
		If no model is loaded, an empty list is returned.

	See Also
	--------
	plot2d.PlotModel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_models = plot2d.PlotModels()
		    for pmod in plot_models:
		        print(pmod.id, pmod.deck, pmod.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_plot_models instead.", DeprecationWarning)

def PlotModelsByDeck(plot_model_deck: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.utils.get_plot_models` instead.


	This function searches for the plot models of the given deck.

	Parameters
	----------
	plot_model_deck : str
		Deck of the plot model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotModel referring to one specific plot_model. 
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotModel

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_model_deck = "NASTRAN"
		    plot_models = plot2d.PlotModelsByDeck(plot_model_deck)
		    for pmod in plot_models:
		        print(pmod.id, pmod.deck, pmod.filename)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.utils.get_plot_models instead.", DeprecationWarning)

def Plots(all_plots: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plots` instead.


	This function collects all plots of all 2d plot windows.

	Parameters
	----------
	all_plots : int, optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific plot of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    all_plots = plot2d.Plots()
		    for pl in all_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plots instead.", DeprecationWarning)

def PlotsByType(plot_type: str, all_plots) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plots` instead.


	This function collects all plots of all 2d plot windows with a specific type.

	Parameters
	----------
	plot_type : str
		Type of the plot. Possible values are:
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

	all_plots : , optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_type = "plain"
		    all_plots = plot2d.PlotsByType(plot_type)
		    for pl in all_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plots instead.", DeprecationWarning)

def PlotsOfWindow(window_name: str, all_plots: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plots` instead.


	This function collects all plots of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	all_plots : int, optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    all_plots = plot2d.PlotsOfWindow(window_name)
		    for pl in all_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plots instead.", DeprecationWarning)

def PlotsOfWindowByType(window_name: str, plot_type: str, all_plots: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_plot_axes` instead.


	This function collects all plots of a given 2d plot window with a specific type.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_type : str
		Type of the plot. Possible values are:
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

	all_plots : int, optional
		All or visible plots. Possible values are:
		- 0: Visible plots (default)
		- 1: All plots

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Plot referring to one specific active plot of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Plot

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_type = "plain"
		    all_plots = plot2d.PlotsOfWindowByType(window_name, plot_type)
		    for pl in all_plots:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_plot_axes instead.", DeprecationWarning)

def PointById(curve_id: int, curve_type: str, point_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function finds a point of a curve with a given id.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	point_id : int
		Id of the point.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific picked point.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 40
		    curve_type = "real"
		    pnt = plot2d.PointById(window_name, curve_id, point_id, curve_type)
		    if pnt:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def PointMarkOfCurve(curve_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_point_mark` instead.


	This function finds the point mark of a given curve. Point mark is a string expression with no more than 5 characters.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	str
		Upon success, it returns a string referring to the point mark of the corresponding curve.
		Else, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_mark = plot2d.PointMarkOfCurve(window_name, curve_id)
		    print(point_mark)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_point_mark instead.", DeprecationWarning)

def PointPrecisionDigitsOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_point_precision_digits` instead.


	This function finds the point precision digits of a given curve. Point precision digits is an integer number in the range of 0 and 20.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the point precision digits of the corresponding curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_precision_digits = plot2d.PointPrecisionDigitsOfCurve(window_name, curve_id)
		    print(point_precision_digits)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_point_precision_digits instead.", DeprecationWarning)

def PointPrecisionOfCurve(curve_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_point_precision` instead.


	This function finds the point precision of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	str
		Upon success, it returns a string referring to the point precision of the corresponding curve. Its possible values are:
		- 'auto' : Auto
		- 'sciauto' : Auto-Scientific
		- 'scientific' : Scientific
		- 'fixed' : Fixed
		Else, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_precision = plot2d.PointPrecisionOfCurve(window_name, curve_id)
		    print(point_precision)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_point_precision instead.", DeprecationWarning)

def PointSizeOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_point_size` instead.


	This function finds the point size of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve

	window_name : str
		Name of the window

	Returns
	-------
	int
		Upon success, it returns an integer referring to the point size of the corresponding curve. Point size is an integer number in the range of 1 and 20, which is the same being used in META commands for changing point size of curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_size = plot2d.PointSizeOfCurve(window_name, curve_id)
		    print(point_size)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_point_size instead.", DeprecationWarning)

def PointStyleOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_point_style` instead.


	This function finds the point style of a given curve.

	Parameters
	----------
	curve_id : int
		Curve id.

	window_name : str
		Window name.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the point style of the corresponding curve. Point style is an integer number in the range of 0 and 8, which is the same being used in META commands for changing point style of curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_style = plot2d.PointStyleOfCurve(window_name, curve_id)
		    print(point_style)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_point_style instead.", DeprecationWarning)

def PointsFromAdvFilters(window_name: str, curve_type: str) -> object:

	"""

	This function allows the user to collect curve points of a window specified by its name through an advanced filter. The execution of the script will stop and a window will open in order to specify the advanced filter entries.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific curve point of the given window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_type = "real"
		    collected_points = plot2d.PointsFromAdvFilters(window_name, curve_type)
		    for pnt in collected_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PointsListToDict(list_points: object) -> object:

	"""

	This function constructs a dictionary from a given list with Point objects.

	Parameters
	----------
	list_points : object
		List with Point objects.

	Returns
	-------
	object
		It returns a dictionary whose key is the id of the point and data the corresponding object of class Point. If points with the same id exist in the given list, then only the first point will be saved in the dictionary.
		Upon failure, an empty dictionary is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    list_points = plot2d.PointsOfCurve(window_name, curve_id)
		    fewer_points = list_points[0 : min(10, len(list_points))]
		    dict_points = plot2d.PointsListToDict(fewer_points)
		    for point_id, point_object in dict_points.items():
		        print(point_id)
		        print(
		            point_object.id,
		            point_object.x,
		            point_object.y,
		            point_object.selected,
		            point_object.curve_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def PointsOfCurve(curve_id: int, curve_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function collects all points of a given curve of a specified window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str, optional
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific point of the given curve.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "real"
		    all_points = plot2d.PointsOfCurve(window_name, curve_id, curve_type)
		    for pnt in all_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def ReportNewCurves() -> object:

	"""

	This function collects the newly created curves from the last call of script function CollectNewCurvesStart(). This function should be preceded by a corresponding call to script function CollectNewCurvesStart() and should be followed by a corresponding call to script function CollectNewCurvesEnd().

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific newly created curve.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import plot2d
		
		
		def main():
		    plot2d.CollectNewCurvesStart()
		
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user1" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.ReportNewCurves()
		    for c in new_curves:
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
		    # create new curves
		    utils.MetaCommand(
		        'xyplot curve new_fx "Window1" "user2" "5000*sin(1000*c.x)" points "1000" "0" "0.3"'
		    )
		
		    new_curves = plot2d.CollectNewCurvesEnd()
		    for c in new_curves:
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

def SelectCurve(window_name: str, curve_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.select` instead.


	This function allows the user to select a curve of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.SelectSomeCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    ret = plot2d.SelectCurve(window_name, curve_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.select instead.", DeprecationWarning)

def SelectPoint(window_name: str, curve_id: int, point_id: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.select` instead.


	This function allows the user to select a point of a curve of a given plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	SelectSomePoints

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 10
		    ret = plot2d.SelectPoint(window_name, curve_id, point_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.select instead.", DeprecationWarning)

def SelectSomeCurves(window_name: str, curve_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.select_curves` instead.


	This function allows the user to select some specific curves of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_ids : object
		Ids of the curves.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_ids = [1, 2, 3, 4]
		    ret = plot2d.SelectSomeCurves(window_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.select_curves instead.", DeprecationWarning)

def SelectSomePoints(window_name: str, curve_id: int, point_ids: object) -> int:

	"""

	This function allows the user to select some specific points of a curve of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_ids : object
		List with ids of the points.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_ids = list()
		    all_points = plot2d.PointsOfCurve(window_name, curve_id)
		    fewer_points = all_points[0 : min(10, len(all_points))]
		    for pnt in fewer_points:
		        point_ids.append(pnt.id)
		    ret = plot2d.SelectSomePoints(window_name, curve_id, point_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SelectedCurves() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `pages.Page.get_curves()` instead.


	This function collects all selected curves of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific selected curve of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    selected_curves = plot2d.SelectedCurves()
		    for c in selected_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  pages.Page.get_curves() instead.", DeprecationWarning)

def SelectedCurvesOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curves` instead.


	This function collects all selected curves of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    selected_curves = plot2d.SelectedCurvesOfPlot(window_name, plot_id)
		    for c in selected_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curves instead.", DeprecationWarning)

def SelectedCurvesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_curves` instead.


	This function collects all selected curves of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    selected_curves = plot2d.SelectedCurvesOfWindow(window_name)
		    for c in selected_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_curves instead.", DeprecationWarning)

def SelectedPointSizeOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_selected_point_size` instead.


	This function finds the selected point size of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the selected point size of the corresponding curve. Point size is an integer number in the range of 1 and 20, which is the same being used in META commands for changing selected point size of curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_size = plot2d.SelectedPointSizeOfCurve(window_name, curve_id)
		    print(point_size)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_selected_point_size instead.", DeprecationWarning)

def SelectedPointStyleOfCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_selected_point_style` instead.


	This function finds the selected point style of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the selected point style of the corresponding curve. Point style is an integer number in the range of 0 and 8, which is the same being used in META commands for changing selected point style of curve.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_style = plot2d.SelectedPointStyleOfCurve(window_name, curve_id)
		    print(point_style)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_selected_point_style instead.", DeprecationWarning)

def SelectedPointsOfCurve(curve_id: int, curve_type: str, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points` instead.


	This function collects all selected points of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	curve_type : str
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific selected point of the given curve.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Point

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "magnitude"
		    selected_points = plot2d.SelectedPointsOfCurve(window_name, curve_id, curve_type)
		    for pnt in selected_points:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points instead.", DeprecationWarning)

def SetAbscissaDyna(file_type: str, type: str, variable: str, entity: int, entity_ip: int) -> int:

	"""

	This function sets abscissa curve for LS-DYNA files. The specified abscissa curve will refer to all the future loading of curves from an LS-DYNA file. This function should be called just before script funcion "LoadCurvesDyna" in order to specify the abscissa curve. In any other case, default 'time' will be used as abscissa curve.

	Parameters
	----------
	file_type : str
		A string referring to the type of the file (e.g. 'rbdout', 'rwforc', 'spcforc', 'nodout' etc.).

	type : str
		Type of data of the curve (e.g. 'time' (default), 'BeamIp', 'Beams', 'Global', 'Material', 'Node' etc.).

	variable : str
		A string referring to the variable (e.g. 'X displacement (xd)', 'Axial Force (af)' etc.).

	entity : int
		An integer referring to the id of the entity.

	entity_ip : int
		An integer referring to the second id of some elements (e.g. 'BeamIp'). In any other case, 'entity_ip' is equal to zero.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    file_type = "nodout"
		    type = "Node"
		    variable = "X displacement (xd)"
		    entity = 2073
		    ret = plot2d.SetAbscissaDyna(file_type, type, variable, entity)
		    print(ret)
		
		    # The above function is used before "LoadCurvesDyna" function
		    # plot2d.LoadCurvesDyna('Window1',0,filename,type,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAbscissaPamcrash(type: str, variable: str, entity: int, entity_ip: int) -> int:

	"""

	This function sets abscissa curve for PAMCRASH files. The specified abscissa curve will refer to all the future loading of curves from a PAMCRASH file. This function should be called just before script funcion 'LoadCurvesPamcrash' in order to specify the abscissa curve. In any other case, default 'time' will be used as abscissa curve. 

	Parameters
	----------
	type : str
		Type of data of the curve (e.g. 'time' (default), 'node', 'part', 'contact' etc.).

	variable : str
		A string referring to the variable (e.g. 'Z Force (fz)', 'X displacement (xd)' etc.).

	entity : int
		An integer referring to the id of the entity.

	entity_ip : int, optional
		An integer referring to the second id of some elements (e.g. 'plink'). In any other case, it is equal to zero.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    type = "Node"
		    variable = "X displacement (xd)"
		    entity = 2073
		    ret = plot2d.SetAbscissaPamcrash(type, variable, entity)
		    print(ret)
		
		    # The above function is used before "LoadCurvesPamcrash" function
		    # plot2d.LoadCurvesPamcrash('Window1', 0, filename, type, entities, variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAbscissaRadioss(type: str, variable: str, time_history: int, entity: int) -> int:

	"""

	This function sets abscissa curve for RADIOSS files. The specified abscissa curve will refer to all the future loading of curves from a RADIOSS file This function should be called just before script funcion 'LoadCurvesRadioss' in order to specify the abscissa curve. In any other case, default "time" will be used as abscissa curve.

	Parameters
	----------
	type : str
		Type of data of the curve (e.g. 'time' (default) ,'global', 'part', 'node', etc.).

	variable : str
		Variable (e.g. 'X displacement (dx)', 'Normal force (f)' etc.).

	time_history : int, optional
		The id of the time history block of the entity (0 for 'global' and 'part').

	entity : int, optional
		The id of the entity.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    type = "Node"
		    variable = "X displacement (dx)"
		    time_history = 4
		    entity = 2073
		    ret = plot2d.SetAbscissaRadioss(type, variable, time_history, entity)
		    print(ret)
		
		    # The above function is used before "LoadCurvesRadioss" function
		    # plot2d.LoadCurvesRadioss('Window1', 0, filename, type, time_history, entities, variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeOfCurve(window_name: str, curve_id: int, attrib_name: str, attrib_value: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_attribute` instead.


	This function sets the value of a specific attribute referring to a given curve. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	attrib_name : str
		Name of the attribute.

	attrib_value : str
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		
		    ret = plot2d.SetAttributeOfCurve(window_name, curve_id, attrib_name, attrib_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_attribute instead.", DeprecationWarning)

def SetColorOfCurve(window_name: str, curve_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_color` instead.


	This function sets color of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	red : int
		Red value.

	green : int
		Green value.

	blue : int
		Blue value.

	alpha : int
		Alpha channel.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = plot2d.SetColorOfCurve(window_name, curve_id, red, green, blue, alpha)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_color instead.", DeprecationWarning)

def SetColorOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, red: int, green: int, blue: int, alpha: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_color` instead.


	This function sets color of a plot axis of a given plot with a given id.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	red : int
		Red value.

	green : int
		Green value

	blue : int
		Blue value

	alpha : int
		Alpha channel.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    red = 100
		    green = 100
		    blue = 100
		    alpha = 255
		    ret = plot2d.SetColorOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id, red, green, blue, alpha
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_color instead.", DeprecationWarning)

def SetFooterOfPlot(window_name: str, plot_id: int, footer: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Footer.set_text` instead.


	This function sets the footer of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	footer : str
		Footer of the plot.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    footer = "Plot Footer"
		    ret = plot2d.SetFooterOfPlot(window_name, plot_id, footer)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Footer.set_text instead.", DeprecationWarning)

def SetLabelOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, axis_label: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_title` instead.


	This function sets label of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	axis_label : str
		Label of the axis.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    axis_label = "Time [msec]"
		    ret = plot2d.SetLabelOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id, axis_label
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_title instead.", DeprecationWarning)

def SetLineStyleOfCurve(window_name: str, curve_id: int, line_style: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_line_style` instead.


	This function sets the line style of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	line_style : int
		An integer number in the range of 0 and 13, which is the same being used in META commands for changing line style of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    line_style = 3
		    ret = plot2d.SetLineStyleOfCurve(window_name, curve_id, line_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_line_style instead.", DeprecationWarning)

def SetLineWidthOfCurve(window_name: str, curve_id: int, line_width: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_line_width` instead.


	This function sets the line width of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	line_width : int
		Line width as an integer number in the range of 0 and 10.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    line_width = 7
		    ret = plot2d.SetLineWidthOfCurve(window_name, curve_id, line_width)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_line_width instead.", DeprecationWarning)

def SetMarkDensityOfCurve(window_name: str, curve_id: int, mark_density: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_mark_density` instead.


	This function sets mark density of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	mark_density : int
		An integer number in the range of 1 and 99, which is the same being used in META commands for changing mark density of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    mark_density = 20
		    ret = plot2d.SetMarkDensityOfCurve(window_name, curve_id, mark_density)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_mark_density instead.", DeprecationWarning)

def SetMaxScaleLimitOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, max_scale_limit: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_scale_limit` instead.


	This function sets maximum scale limit of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	max_scale_limit : float
		Maximum scale limit.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    max_scale_limit = 100
		    ret = plot2d.SetMaxScaleLimitOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id, max_scale_limit
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_scale_limit instead.", DeprecationWarning)

def SetMinScaleLimitOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, min_scale_limit: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_scale_limit` instead.


	This function sets minimum scale limit of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	min_scale_limit : float
		Minimum scale limit.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    min_scale_limit = -100
		    ret = plot2d.SetMinScaleLimitOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id, min_scale_limit
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_scale_limit instead.", DeprecationWarning)

def SetMultiplierOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, multiplier: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_multiplier` instead.


	This function sets the multiplier of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	multiplier : int
		Multiplier of the axis values.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "yaxis"
		    axis_id = 0
		    multiplier = 4
		    ret = plot2d.SetMultiplierOfPlotAxis(
		        window_name, plot_id, axis_type, axis_id, multiplier
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_multiplier instead.", DeprecationWarning)

def SetPointMarkOfCurve(window_name: str, curve_id: int, point_mark: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `Curve.set_point_mark` instead.


	This function sets the point mark of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_mark : str
		A string expression with no more than 5 characters.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_mark = "OK"
		    ret = plot2d.SetPointMarkOfCurve(window_name, curve_id, point_mark)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  Curve.set_point_mark instead.", DeprecationWarning)

def SetPointPrecisionDigitsOfCurve(window_name: str, curve_id: int, point_precision_digits: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_point_precision_digits` instead.


	This function sets the point precision digits of a given curve if Curve Options > Points > Follow Window settings > Identify options format is disabled.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_precision_digits : int
		Point precision digits as an integer in the range of 0 and 20.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_precision_digits = 3
		    ret = plot2d.SetPointPrecisionDigitsOfCurve(
		        window_name, curve_id, point_precision_digits
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_point_precision_digits instead.", DeprecationWarning)

def SetPointPrecisionOfCurve(window_name: str, curve_id: int, point_precision: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_point_precision` instead.


	This function sets the point precision of a given curve if Curve Options > Points > Follow Window settings > Identify options format is disabled.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_precision : str
		A string expression referring to the type of the point precision of the curve. Its possible values are:
		- 'auto' : Auto
		- 'sciauto' : Auto-Scientific
		- 'scientific': Scientific
		- 'fixed' : Fixed

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_precision = "scientific"
		    ret = plot2d.SetPointPrecisionOfCurve(window_name, curve_id, point_precision)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_point_precision instead.", DeprecationWarning)

def SetPointSizeOfCurve(window_name: str, curve_id: int, point_size: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_point_size` instead.


	This function sets the point size of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_size : int
		An integer number in the range of 1 and 20, which is the same being used in META commands for changing point size of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_size = 10
		    ret = plot2d.SetPointSizeOfCurve(window_name, curve_id, point_size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_point_size instead.", DeprecationWarning)

def SetPointStyleOfCurve(window_name: str, curve_id: int, point_style: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_point_style` instead.


	This function sets the point style of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_style : int
		An integer number in the range of 0 and 8, which is the same being used in META commands for changing point style of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_style = 8
		    ret = plot2d.SetPointStyleOfCurve(window_name, curve_id, point_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_point_style instead.", DeprecationWarning)

def SetSelectedPointSizeOfCurve(window_name: str, curve_id: int, point_size: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_selected_point_size` instead.


	This function sets the selected point size of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_size : int
		Point size is an integer number in the range of 1 and 20, which is the same being used in META commands for changing selected point size of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_size = 15
		    ret = plot2d.SetSelectedPointSizeOfCurve(window_name, curve_id, point_size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_selected_point_size instead.", DeprecationWarning)

def SetSelectedPointStyleOfCurve(window_name: str, curve_id: int, point_style: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_selected_point_style` instead.


	This function sets the selected point style of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_style : int
		Point style is an integer number in the range of 0 and 8, which is the same being used in META commands for changing point style of curve.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_style = 8
		    ret = plot2d.SetSelectedPointStyleOfCurve(window_name, curve_id, point_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_selected_point_style instead.", DeprecationWarning)

def SetSettingsOfAllCurves(window_name: str, curve_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_curves_settings` instead.


	This function controls settings of all curves of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_settings : object
		A list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6'). The names of the curve settings and its possible values are:
		- 'assign_xaxis': Set X axis assignment (integer value)
		- 'assign_yaxis': Set Y axis assignment (integer value)
		- 'baroffset': Use X axis offset for bars (0,1)
		- 'bartype': Convert curve to bar chart (0,1)
		- 'barwidth': Bar width (integer value)
		- 'curve_color': Curve color (string value)
		- 'entity_id': Change id of entity (integer value)
		- 'entity_ip': Change integration point of entity (integer value)
		- 'entity_secid': Change secondary id of entity (integer value)
		- 'entity_type': Change entity type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe',
		- 'seatbelt', 'section', 'shell', 'solid', 'spc')
		- 'entity_sectype': Change entity secondary type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', 'force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe', 'seatbelt', 'section', 'shell', 'solid', 'spc')
		- 'fill': Fill bar type curve (0,1)
		- 'linewidth': Curve width (integer value)
		- 'mark': Curve mark (string value)
		- 'mark_number': Curve mark number (integer value)
		- 'point_precision_digits': Point precision digits (integer value)
		- 'point_precision_type': Point precision type ('auto', 'fixed', 'sciauto', 'scientific')
		- 'point_size': Point size (integer value)
		- 'follow_identify': Curve style follows identify format
		- 'point_font': Point font (string value)
		- 'point_size': Point size (integer value)
		- 'point_style': Point style (integer value)
		- 'style': Curve style (integer value)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_settings = ["curve_color,red", "linewidth,5"]
		    ret = plot2d.SetSettingsOfAllCurves(window_name, curve_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_curves_settings instead.", DeprecationWarning)

def SetSettingsOfAllPlots(window_name: str, plot_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.set_plots_settings` instead.


	This function controls settings of all plots of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_settings : object
		A list which contains strings as members with the name and value of each setting separated by comma (e.g. 'border_width,6'). The names of the plot settings and its possible values are:
		- 'border_width': Border line width (integer value)
		- 'border_color': Border color (string value)
		- 'complex_height': Complex plot height (integer value)
		- 'curves_palette': Color palette for selected curves (string value)
		- 'db_value': Decibel value (float value)
		- 'decibel': Revet y axis to decibel ('on', 'off', 'dba', 'dbb', 'dbc')
		- 'dna_palette': Palette for dna plot (string value)
		- 'mac_palette': Palette for mac plot (string value)
		- 'footer_align': Footer alignment ('center', 'left', 'right')
		- 'footer_text': Footer text (string value)
		- 'footer_font': Footer font (string value)
		- 'footer_color': Footer color (string value)
		- 'legend': Legend (0,1)
		- 'locktitles': Lock titles from read file (0,1)
		- 'lockx': Lock X axis with another plot (integer value)
		- 'locky': Lock Y axis with another plot (integer value)
		- 'margin_up': Plot up margin (float value)
		- 'margin_down': Plot down margin (float value)
		- 'margin_left': Plot left margin (float value)
		- 'margin_right': Plot right margin (float value)
		- 'plot_palette_counter': Plot palette counter
		- 'plot_type': Plot type ('plain', 'magphase', 'realimag', 'polar', 'horiz', 'dna', 'mac', 'horizontal', 'colormap', '3dmac', 'waterfall', 'nyquist')
		- 'point_show': Show model point (0,1)
		- 'polar_size': Polar size (0,1)
		- 'show_current': Show only current line (0,1)
		- 'sync_value': Show model value and sync line (0,1)
		- 'title_align': Title alignment ('center', 'left', 'right')
		- 'title_text': Title text (string value)
		- 'title_font': Title font (string value)
		- 'title_color': Title color (string value)
		- 'unlock': Unlock axes ('x', 'y')
		- 'model_value': Show model value (0,1)
		- 'xauto': Revert to auto X axis limits (0,1)
		- 'yauto': Revert to auto Y axis limits (0,1)
		- 'xlabel': X label (string value)
		- 'ylabel': Y label (string value)
		- 'xlock_values': Make current X values default (0,1)
		- 'ylock_values': Make current Y values default (0,1)
		- 'xlog': Revert X axis to log (0,1)
		- 'ylog': Revert Y axis to log (0,1)
		- 'xmax': X axis maximum value (float value)
		- 'xmin': X axis minimum value (float value)
		- 'ymax': Y axis maximum value (float value)
		- 'ymin': Y axis minimum value (float value)
		- 'zeroaxis': Show primary zero axes (0,1)
		- 'xrange': Primary X axis range values (float value, float value)
		- 'yrange': Primary Y axis range values (float value, float value)
		- 'xstep': X axis grid-line number (float value)
		- 'ystep': Y axis grid-line number (float value)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_settings = ["border_width,6", "yrange,-10,120"]
		    ret = plot2d.SetSettingsOfAllPlots(window_name, plot_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.set_plots_settings instead.", DeprecationWarning)

def SetSettingsOfCurve(window_name: str, curve_id: int, curve_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_settings` instead.


	This function adjusts settings of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	curve_settings : object
		A list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6'). The names of the curve settings and its possible values are:
		- 'assign_xaxis': Set X axis assignment (integer value)
		- 'assign_yaxis': Set Y axis assignment (integer value)
		- 'baroffset': Use X axis offset for bars (0,1)
		- 'bartype': Convert curve to bar chart (0,1)
		- 'barwidth': Bar width (integer value)
		- 'curve_color': Curve color (string value)
		- 'entity_id': Change id of entity (integer value)
		- 'entity_ip': Change integration point of entity (integer value)
		- 'entity_secid': Change secondary id of entity (integer value)
		- 'entity_type': Change entity type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe',
		- 'seatbelt', 'section', 'shell', 'solid', 'spc')
		- 'entity_sectype': Change entity secondary type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', 'force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe', 'seatbelt', 'section', 'shell', 'solid', 'spc')
		- 'fill': Fill bar type curve (0,1)
		- 'linewidth': Curve width (integer value)
		- 'mark': Curve mark (string value)
		- 'mark_number': Curve mark number (integer value)
		- 'point_precision_digits': Point precision digits (integer value)
		- 'point_precision_type': Point precision type ('auto', 'fixed', 'sciauto', 'scientific')
		- 'point_size': Point size (integer value)
		- 'follow_identify': Curve style follows identify format
		- 'point_font': Point font (string value)
		- 'point_size': Point size (integer value)
		- 'point_style': Point style (integer value)
		- 'style': Curve style (integer value)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 7
		    curve_settings = ["curve_color,blue", "linewidth,5"]
		    ret = plot2d.SetSettingsOfCurve(window_name, curve_id, curve_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_settings instead.", DeprecationWarning)

def SetSettingsOfPlot(window_name: str, plot_id: int, plot_settings: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.set_settings` instead.


	This function controls settings of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	plot_settings : object
		A list which contains strings as members with the name and value of each setting separated by comma (e.g. 'border_width,6'). The names of the plot settings and its possible values are:
		- 'border_width': Border line width (integer value)
		- 'border_color': Border color (string value)
		- 'complex_height': Complex plot height (integer value)
		- 'curves_palette': Color palette for selected curves (string value)
		- 'db_value': Decibel value (float value)
		- 'decibel': Revet y axis to decibel ('on', 'off', 'dba', 'dbb', 'dbc')
		- 'dna_palette': Palette for dna plot (string value)
		- 'mac_palette': Palette for mac plot (string value)
		- 'footer_align': Footer alignment ('center', 'left', 'right')
		- 'footer_text': Footer text (string value)
		- 'footer_font': Footer font (string value)
		- 'footer_color': Footer color (string value)
		- 'legend': Legend (0,1)
		- 'locktitles': Lock titles from read file (0,1)
		- 'lockx': Lock X axis with another plot (integer value)
		- 'locky': Lock Y axis with another plot (integer value)
		- 'margin_up': Plot up margin (float value)
		- 'margin_down': Plot down margin (float value)
		- 'margin_left': Plot left margin (float value)
		- 'margin_right': Plot right margin (float value)
		- 'plot_palette_counter': Plot palette counter
		- 'plot_type': Plot type ('plain', 'magphase', 'realimag', 'polar', 'horiz', 'dna', 'mac', 'horizontal', 'colormap', '3dmac', 'waterfall', 'nyquist')
		- 'point_show': Show model point (0,1)
		- 'polar_size': Polar size (0,1)
		- 'show_current': Show only current line (0,1)
		- 'sync_value': Show model value and sync line (0,1)
		- 'title_align': Title alignment ('center', 'left', 'right')
		- 'title_text': Title text (string value)
		- 'title_font': Title font (string value)
		- 'title_color': Title color (string value)
		- 'unlock': Unlock axes ('x', 'y')
		- 'model_value': Show model value (0,1)
		- 'xauto': Revert to auto X axis limits (0,1)
		- 'yauto': Revert to auto Y axis limits (0,1)
		- 'xlabel': X label (string value)
		- 'ylabel': Y label (string value)
		- 'xlock_values': Make current X values default (0,1)
		- 'ylock_values': Make current Y values default (0,1)
		- 'xlog': Revert X axis to log (0,1)
		- 'ylog': Revert Y axis to log (0,1)
		- 'xmax': X axis maximum value (float value)
		- 'xmin': X axis minimum value (float value)
		- 'ymax': Y axis maximum value (float value)
		- 'ymin': Y axis minimum value (float value)
		- 'zeroaxis': Show primary zero axes (0,1)
		- 'xrange': Primary X axis range values (float value, float value)
		- 'yrange': Primary Y axis range values (float value, float value)
		- 'xstep': X axis grid-line number (float value)
		- 'ystep': Y axis grid-line number (float value)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_settings = ["border_width,1", "yrange,-50,120"]
		    ret = plot2d.SetSettingsOfPlot(window_name, 0, plot_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.set_settings instead.", DeprecationWarning)

def SetStepsOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int, steps: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_steps` instead.


	This function sets the steps of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	steps : int
		Steps of the axis.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    steps = 15
		    ret = plot2d.SetStepsOfPlotAxis(window_name, plot_id, axis_type, axis_id, steps)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_steps instead.", DeprecationWarning)

def SetSubAttributeOfCurve(window_name: str, curve_id: int, group_name: str, attrib_name: str, attrib_value: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.set_attribute` instead.


	This function sets the value of a specific curve attribute of a group to a given value.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	group_name : str
		Name of the attribute group.

	attrib_name : str
		Name of the attribute. If the given attribute and group do not exist they are automatically created.

	attrib_value : str
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    group_name = "test_group"
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		    ret = plot2d.SetSubAttributeOfCurve(
		        window_name, curve_id, group_name, attrib_name, attrib_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.set_attribute instead.", DeprecationWarning)

def SetTitleOfPlot(window_name: str, plot_id: int, title: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Title.set_text` instead.


	This function sets the title of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	title : str
		Title of the plot.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    title = "Plot Title"
		    ret = plot2d.SetTitleOfPlot(window_name, plot_id, title)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Title.set_text instead.", DeprecationWarning)

def ShowCurve(curve_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.show` instead.


	This function allows the user to make visible a curve of a given 2d plot window.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	See Also
	--------
	plot2d.ShowSomeCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    plot2d.ShowCurve(window_name, curve_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.show instead.", DeprecationWarning)

def ShowSomeCurves(window_name: str, curve_ids: object) -> int:

	"""

	This function allows the user to make visible some specific curves of a 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_ids : object
		List with ids of the curves.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_ids = list()
		    selected_curves = plot2d.CurvesOfWindow(window_name)
		    for c in selected_curves:
		        curve_ids.append(c.id)
		    ret = plot2d.ShowSomeCurves(window_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def StepsOfPlotAxis(axis_id: int, axis_type: str, plot_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_steps` instead.


	This function finds the steps of a plot axis of a given plot.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns an integer referring to the steps of the specified plot axis.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    steps = plot2d.StepsOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(steps)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_steps instead.", DeprecationWarning)

def SubAttributeOfCurve(attrib_name: str, curve_id: int, group_name: str, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_attributes` instead.


	This function returns the value of a specific attribute of a group referring to a given curve.

	Parameters
	----------
	attrib_name : str
		Name of the attribute.

	curve_id : int
		Id of the curve.

	group_name : str
		Name of the attribute group.

	window_name : str
		Name of the window.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    attrib_name = "test_attribute"
		    group_name = "test_group"
		    attrib_value = plot2d.SubAttributeOfCurve(
		        window_name, curve_id, group_name, attrib_name
		    )
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_attributes instead.", DeprecationWarning)

def SubgroupsOfCurveGroup(group_name: str, level: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.CurveGroup.get_subgroups` instead.


	This function searches for the subgroups of a given curve group in the list of the curve groups of the specified window.

	Parameters
	----------
	group_name : str
		Name of the curve group.

	level : int, optional
		Depth of searching for subgroups (1 - one level down, 2 - two levels down, 3 - three levels down etc.). If it is absent, then this function will search down all levels for subgroups.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a where each member of the list is an object of class CurveGroup referring to one subgroup of the given group of the specified model.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "test_group"
		    level = 1
		    subgroups = plot2d.SubgroupsOfCurveGroup(window_name, group_name, level)
		    for cg in subgroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.CurveGroup.get_subgroups instead.", DeprecationWarning)

def SyncedModelOfCurve(curve_id: int, window_name: str) -> object:

	"""

	This function finds the synchronized model of a given curve.

	Parameters
	----------
	curve_id : int
		Id of the curve.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns the Model object of the synchronized model of the corresponding curve.
		Else, None is returned.

	See Also
	--------
	models.Model

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    mod = plot2d.SyncedModelOfCurve(window_name, curve_id)
		    if mod:
		        print(mod.id, mod.name, mod.label, mod.deck, mod.active)
		
		
		if __name__ == "__main__":
		    main()


	"""

def TitleOfPlot(plot_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Title.get_text` instead.


	This function finds the title of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	str
		Upon success, it returns the title of the given plot.
		Upon failure, it returns an empty string.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    title = plot2d.TitleOfPlot(window_name, plot_id)
		    print(title)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Title.get_text instead.", DeprecationWarning)

def UpdateCurve(curve: object) -> object:

	"""

	This function updates the attributes of a given Curve object. Update is based in the fields 'id' and 'window_name' of the given Curve object.

	Parameters
	----------
	curve : object
		Object of class type Curve.

	Returns
	-------
	object
		Upon success, it returns the new updated Curve object.
		Else, None is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		from meta import utils
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    c = plot2d.CurveById(window_name, curve_id)
		    if c:
		        # commands which alter the data of the Curve object
		        utils.MetaCommand(
		            "xyplot curve set name "
		            + window_name
		            + " "
		            + str(c.id)
		            + ' "new name for curve 1"'
		        )
		
		        c = plot2d.UpdateCurve(c)
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

def UpdatePlotAxis(plot_axis: object) -> object:

	"""

	This function updates the attributes of a given PlotAxis object. Update is based in the fields 'id', 'plot_id' and 'window_name' of the given PlotAxis object.

	Parameters
	----------
	plot_axis : object
		Object of class type PlotAxis.

	Returns
	-------
	object
		Upon success, it returns the new updated PlotAxis object.
		Else, None is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		from meta import utils
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    plax = plot2d.PlotAxisOfPlotById(window_name, plot_id, axis_type, axis_id)
		    if plax:
		        # commands which alter the data of the PlotAxis object
		        utils.MetaCommand('xyplot axisoptions axyrange "Window1" 0 0 -100 100')
		
		        plax = plot2d.UpdatePlotAxis(plax)
		        if plax:
		            print(
		                plax.id,
		                plax.type,
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


	"""

def ValueXOfCurveForY(axis_id: int, curve_id: int, y_value: float, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_x_value_from_y` instead.


	This function calculates X value for a given Y value of a given curve specified by its id and the window it belongs to.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	curve_id : int
		Id of the curve.

	y_value : float
		Y value.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float number referring to the corresponding X value of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		from meta import utils
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    axis_id = 0
		    yvalue = 100
		    xvalue = plot2d.ValueXOfCurveForY(window_name, curve_id, axis_id, yvalue)
		    print(xvalue)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_x_value_from_y instead.", DeprecationWarning)

def ValueXOfCurveForYComplex(axis_id: int, curve_id: int, y_complex: float, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_x_value_from_y_complex` instead.


	This function calculates X value for a given phase or imaginary value of a given curve. specified by its id and the window it belongs to. 

	Parameters
	----------
	axis_id : int
		Id of the axis.

	curve_id : int
		Id of the curve.

	y_complex : float
		Y complex value.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float number referring to the corresponding X value of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    axis_id = 0
		    y_complex = -1000
		    xvalue = plot2d.ValueXOfCurveForYComplex(window_name, curve_id, axis_id, y_complex)
		    print(xvalue)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_x_value_from_y_complex instead.", DeprecationWarning)

def ValueYComplexOfCurveForX(axis_id: int, curve_id: int, x_value: float, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_y_complex_value_from_x` instead.


	This function calculates Y complex value (phase or imaginary value) for a given X value of a given curve.

	Parameters
	----------
	axis_id : int
		Id of the axis.

	curve_id : int
		Id of the curve.

	x_value : float
		X value.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float number referring to the corresponding phase or imaginary value (according to the type of plot) of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    axis_id = 0
		    x_value = 350
		    y_complex = plot2d.ValueYComplexOfCurveForX(window_name, curve_id, axis_id, x_value)
		    print(y_complex)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_y_complex_value_from_x instead.", DeprecationWarning)

def ValueYOfCurveForX(window_name: str, curve_id: int, axis_id: int, xvalue: float) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_y_value_from_x` instead.


	This function calculates Y value for a given X value of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	axis_id : int
		Id of the axis.

	xvalue : float
		X value.

	Returns
	-------
	float
		It returns a float number referring to the corresponding Y value of the given curve.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    axis_id = 0
		    x_value = 0.1
		    y_value = plot2d.ValueYOfCurveForX(window_name, curve_id, axis_id, x_value)
		    print(y_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_y_value_from_x instead.", DeprecationWarning)

def VisibleCurves() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `pages.Page.get_curves()` instead.


	This function collects all visible curves of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific visible curve of an existing 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    visible_curves = plot2d.VisibleCurves()
		    for c in visible_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  pages.Page.get_curves() instead.", DeprecationWarning)

def VisibleCurvesOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curves` instead.


	This function collects all visible curves of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific visible curve of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    visible_curves = plot2d.VisibleCurvesOfPlot(window_name, plot_id)
		    for c in visible_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curves instead.", DeprecationWarning)

def VisibleCurvesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_curves` instead.


	This function collects all visible curves of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific visible curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    visible_curves = plot2d.VisibleCurvesOfWindow(window_name)
		    for c in visible_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_curves instead.", DeprecationWarning)

def VisiblePlotAxes() -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects visible plot axes of all 2d plot windows.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot_axes = plot2d.VisiblePlotAxes()
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def VisiblePlotAxesByType(axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.pages.Page.get_plot_axes` instead.


	This function collects visible plot axes of all 2d plot windows for a specific type.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis_type = "xaxis"
		    plot_axes = plot2d.VisiblePlotAxesByType(axis_type)
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.pages.Page.get_plot_axes instead.", DeprecationWarning)

def VisiblePlotAxesOfPlot(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects visible plot axes of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot_axes = plot2d.VisiblePlotAxesOfPlot(window_name, plot_id)
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def VisiblePlotAxesOfPlotByType(axis_type: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_plot_axes` instead.


	This function collects visible plot axes of a given plot for a specific type.

	Parameters
	----------
	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    plot_axes = plot2d.VisiblePlotAxesOfPlotByType(window_name, plot_id, axis_type)
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_plot_axes instead.", DeprecationWarning)

def VisiblePlotAxesOfWindow(window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects visible plot axes of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_axes = plot2d.VisiblePlotAxesOfWindow(window_name)
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def VisiblePlotAxesOfWindowByType(window_name: str, axis_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.window.Window.get_plot_axes` instead.


	This function collects visible plot axes of a given 2d plot window for a specific type.

	Parameters
	----------
	window_name : str
		Name of the window.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class PlotAxis referring to one specific visible axis of a 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.PlotAxis

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    axis_type = "yaxis"
		    plot_axes = plot2d.VisiblePlotAxesOfWindowByType(window_name, axis_type)
		    for plax in plot_axes:
		        print(
		            plax.id,
		            plax.type,
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


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.window.Window.get_plot_axes instead.", DeprecationWarning)

def CurvesTypesIsoWithNames(filename: str) -> object:

	"""

	This function finds curve types of an ISO file. File is specified by its path.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the channels of the given file. Each member of the list is another list with 2 members.
		In position 0, internal lists contain an integer referring to the id of a channel of the given file. 
		In position 1, internal lists contain a string referring to the name of a channel of the given file. 
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/05283.mme"
		    channels = plot2d.CurvesTypesIsoWithNames(filename)
		    for one_channel in channels:
		        channel_id = one_channel[0]  # Id of channel
		        print(channel_id)
		        channel_name = one_channel[1]  # Name of channel
		        print(channel_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AreaOfCurves(curve_id1: int, curve_id2: int, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_area` instead.


	This function calculates the are between two curves of a given plot2d window.

	Parameters
	----------
	curve_id1 : int
		Id of the 1st curve

	curve_id2 : int
		Id of the 2nd curve

	window_name : str
		Name of the window

	Returns
	-------
	float
		It returns a float number referring to the corresponding area between the two given curves.
		Upon failure, a zero value is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id1 = 1
		    curve_id2 = 2
		    curves_area = plot2d.AreaOfCurves(window_name, curve_id1, curve_id2)
		    print(curves_area)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_area instead.", DeprecationWarning)

def CurvePeaks(above_below: str, curve_id: int, threshold_type: str, threshold_value: object, window_name: str) -> object:

	"""

	This function finds the peaks of a curve with respect to a given threshold and returns the points that correspond to these peaks.

	Parameters
	----------
	above_below : str
		Specifies which peaks of the curve shall be returned. It must be one of the string values:
		- 'above': peaks will be the local maxima above the threshold
		- 'below': peaks will be the local minima below the threshold.

	curve_id : int
		Id of the curve.

	threshold_type : str
		The type of the threshold. It must be one of the string values:
		- 'value': threshold is a single value
		- 'curve': threshold is a curve
		- 'table': threshold is a table.

	threshold_value : object
		The actual values of the threshold, depending on the threshold_type.
		- For threshold_type 'value', it must be the single value of the threshold in a list.
		- For threshold_type 'curve', it must be the id of the curve that shall be used as threshold in a list.
		- For threshold_type 'table', it must be a list of sequentially defined (x1,y1,x2,y2) points that define the threshold curve.

	window_name : str
		Name of the plot2d window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Point referring to one specific peak of the curve of the given plot2d window. The points are returned in descending order of the difference between the peak and the specified threshold, taking into account any db filtering on the y-axis.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 3
		    print("Example 1  (local maxima above a value)")
		    peaks = plot2d.CurvePeaks(window_name, curve_id, "above", "value", [5e-8])
		    print(len(peaks))
		    for p in peaks:
		        print(p.id, p.x, p.y)
		    print("\\nExample 2  (local maxima above a curve)")
		    peaks = plot2d.CurvePeaks(window_name, 2, "above", "curve", [4])
		    print(len(peaks))
		    for p in peaks:
		        print(p.id, p.x, p.y)
		    print("\\nExample 3  (local maxima above a table-defined curve)")
		    threshold_value = [20, 1e-8, 40, 1e-8, 60, 1e-7, 80, 3e-7, 100, 1e-9, 120, 1e-9]
		    peaks = plot2d.CurvePeaks(window_name, curve_id, "above", "table", threshold_value)
		    print(len(peaks))
		    for p in peaks:
		        print(p.id, p.x, p.y)
		    print("\\nExample 4  (local minima below a curve)")
		    peaks = plot2d.CurvePeaks(window_name, curve_id, "below", "curve", [4])
		    print(len(peaks))
		    for p in peaks:
		        print(p.id, p.x, p.y)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesNastran(window_name: str, plot_id: int, filename: str, xaxis: str, type: str, cycles: object, states: object, entities: object, variables: object, fluid_grid: int) -> object:

	"""

	This function loads curves from a NASTRAN file in an existing plot of a given 2d plot window. To lad curves from an OP2 file, script function plot2d.LoadCurvesOp2 must be used. Plot is specified by its number-id. File is specified by its path (filename). 

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	xaxis : str
		Type of x-axis data which are going to be loaded (e.g. 'subcase', 'time', 'mode', 'frequency', 'loadstep' etc.).

	type : str
		Type of data which are going to be loaded (e.g. 'displacement', 'acceleration', 'velocity' etc.).

	cycles : object
		A list whose members are integers referring to the cycles of the model. If the 1st member of argument cycles is 'all', then curves of all cycles are loaded.

	states : object
		A list whose members are integers referring to the states of the model. If the 1st member of argument states is 'all', then curves of all states are loaded.

	entities : object
		A list whose members are strings referring to the ids of the entities which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		A list whose members are strings referring to the variables which are going to be loaded (e.g. 'pressure', 'dba', 'dbb', 'dbc' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	fluid_grid : int, optional
		Id of the fluid grid node and it is taken into account only for specific types (e.g. 'normalizedgridparticipationfactors', 'panelparticipationfactors', 'fluidmodalparticipationfactors', 'structuremodalparticipationfactors'). If it is absent then curves for all fluid grids will be created.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Nastran.pch"
		    type = "accelerations"
		    xaxis = "frequency"
		    cycles = ["0"]
		    states = ["2"]
		    entities = ["56369", "56384"]
		    variables = ["translational_direction-x_(tx)"]
		    new_curves = plot2d.LoadCurvesNastran(
		        window_name, plot_id, filename, xaxis, type, cycles, states, entities, variables
		    )
		    for c in new_curves:
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

def CurvesTypesRadTherm(filename: str) -> object:

	"""

	This function finds curves types of a RadTherm file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the the parts.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesRadTherm

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/RadTherm.tdf"
		    curves_types = plot2d.CurvesTypesRadTherm(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        parts = one_type[1]  # List with parts
		        for one_part in parts:  # Id of part
		            print(one_part)
		        print("---------------------------------------------------------------------")
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("#####################################################################")
		
		        # The results of this function can be used as arguments in function LoadCurvesRadTherm
		        # plot2d.LoadCurvesRadTherm('Window1',0,filename,type,parts,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesRadThermWithNames(filename: str) -> object:

	"""

	This function finds curves types of a RadTherm file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list which contains in position 0 the id of the part and in position 1 the name of the part.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/RadTherm.tdf"
		    curves_types = plot2d.CurvesTypesRadThermWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        parts = one_type[1]  # List with parts
		        for one_part in parts:
		            part_id = one_part[0]  # Id of part
		            print(part_id)
		            part_name = one_part[1]  # Name of part
		            print(part_name)
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesRadTherm(window_name: str, plot_id: int, filename: str, type: str, parts: object, variables: object) -> object:

	"""

	This function loads curves from a TAITherm file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded (e.g. 'Temperature Data', 'Conduction Data', 'Solution Case Curve Data', etc.).

	parts : object
		A list whose elements are strings representing the ids of parts. If the 1st member of argument parts is 'all', then curves of all parts are loaded.

	variables : object
		A list whose elements are strings representing the abbreviations of variables which are going to be loaded (e.g. 'm2IF', 'p7-12', etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/TAITherm.tdf"
		    type = "Conduction Data"
		    variables = ["m2IF", "mBNH", "mFOH"]
		    parts = ["all"]
		    new_curves = plot2d.LoadCurvesRadTherm(
		        window_name, plot_id, filename, type, parts, variables
		    )
		    for c in new_curves:
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

def AsamOdsConnect(server: str, port: str, args: str, id: str, kind: str, user: str, password: str) -> int:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function connects to an ASAM-ODS Server.

	Parameters
	----------
	server : str
		Corresponding ASAM-ODS Server.

	port : str
		Corresponding port.

	args : str
		CORBA init arguments.

	id : str
		Binding id.

	kind : str
		Binding kind.

	user : str
		Username.

	password : str
		User password.

	Returns
	-------
	int
		It returns 1 if successful, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    server = "192.168.199.128"
		    port = "2809"
		    args = ""
		    id = "ODS"
		    kind = "ASAM-ODS"
		    user = "user"
		    password = "password"
		    ret = plot2d.AsamOdsConnect(server, port, args, id, kind, user, password)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsDisconnect() -> int:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function disconnects from the ASAM-ODS Server.

	Returns
	-------
	int
		It returns 1 if successful, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    ret = plot2d.AsamOdsDisconnect()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsPlotAsamPath(window_name: str, AsamPath: str) -> int:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function creates the curves for the corresponding ASAM-ODS Path.

	Parameters
	----------
	window_name : str
		Name of the window.

	AsamPath : str
		The ASAM-ODS path.

	Returns
	-------
	int
		It returns the number of curves plotted.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "NewWindow_1"
		    AsamPath = "/[Environment]ODS\\/Tests;/[Test]Series;/[SubTest]Record;/[Measurement]Record;1/[Submatrix]Submatrix1;/[LocalColumn]Col1;"
		    curves = plot2d.AsamOdsPlotAsamPath(window_name, AsamPath)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def PlotLayoutOfWindow(window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.windows.Window.get_plot_layout` instead.


	This function gets the plot layout number of a given 2D window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns an integer referring to the plot layout number of the given window.   
		Upon failure, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_layout = plot2d.PlotLayoutOfWindow(window_name)
		    print(plot_layout)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.windows.Window.get_plot_layout instead.", DeprecationWarning)

def AsamOdsApplicationElementAttributes(applElem: str, aaPattern: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a matrix with all the application element attribute names.

	Parameters
	----------
	applElem : str
		The application element.

	aaPattern : str
		The application attribute pattern to match.

	Returns
	-------
	object
		A list with the application element attribute names.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "Environment"
		    aaPattern = "mime*"
		    attributes = plot2d.AsamOdsApplicationElementAttributes(applElem, aaPattern)
		    for a in attributes:
		        print(a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsApplicationElementById(aeId, arg) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a string or list depending on the second argument.

	Parameters
	----------
	aeId : 
		The application element id.

	arg : 
		Argument. If '-baseElem' the function returns the matrix and if not the string.

	Returns
	-------
	object
		It returns a string with the application element name if the second argument is blank or omitted. It returns a list containing the application element name and the base element name if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    aeId = 2
		    arg = "-baseElem"
		    ae = plot2d.AsamOdsApplicationElementById(aeId)
		    print(ae)
		    aeStruct = plot2d.AsamOdsApplicationElementById(aeId, arg)
		    if len(aeStruct):
		        print(aeStruct[0] + "\\tBaseElem:" + aeStruct[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsApplicationElementsByBaseType(aeType: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function lists elements by base type.

	Parameters
	----------
	aeType : str
		Base type argument.

	arg : str
		If "-baseElem" the function returns the 2d list and if not the 1d.

	Returns
	-------
	object
		It returns a list with the application element names if the second argument is blank or omitted. It returns a list containing pairs of application element names and base element names if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    aeType = "*"
		    arg = "-baseElem"
		
		    elems = plot2d.AsamOdsApplicationElementsByBaseType(aeType)
		    for e in elems:
		        print(e)
		    elems = plot2d.AsamOdsApplicationElementsByBaseType(aeType, arg)
		    for e in elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElementAsamOdsPath(applElem: str, instanceElem: str) -> str:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns the AsamPath of a certain instance element.

	Parameters
	----------
	applElem : str
		The application element.

	instanceElem : str
		The instance element.

	Returns
	-------
	str
		A string containing the AsamPath.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    instanceElem = "TL1A"
		    asam_path = plot2d.AsamOdsInstanceElementAsamOdsPath(applElem, instanceElem)
		    print(asam_path)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElementAttributes(applElem: str, instanceElem: str, aaPattern: str, aeType: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a list with all the instance element attribute names.

	Parameters
	----------
	applElem : str
		The application element.

	instanceElem : str
		The instance element.

	aaPattern : str
		The instance element attribute pattern to match.

	aeType : str
		Type of the attributes. Can be one of the following: APPLATTR_ONLY, INSTATTR_ONLY, ALL.

	Returns
	-------
	object
		A list with all the instance element attribute names.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "MeasurementQuantity"
		    instanceElem = "TL1A"
		    aaPattern = "version*"
		    aeType = "ALL"
		
		    attributes = plot2d.AsamOdsInstanceElementAttributes(
		        applElem, instanceElem, aaPattern, aeType
		    )
		    for a in attributes:
		        print(a)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElementAttributeValue(applElem: str, instanceElem: str, attrName: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a list with the value or values of a certain instance element.

	Parameters
	----------
	applElem : str
		The application element.

	instanceElem : str
		The instance element.

	attrName : str
		The attribute name.

	Returns
	-------
	object
		A list with the value or values of the attribute.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    instanceElem = "TL1A"
		    attrName = "id"
		    id = plot2d.AsamOdsInstanceElementAttributeValue(applElem, applElem, attrName)
		    if len(id):
		        print(id[0])
		    attrName = "name"
		    name = plot2d.AsamOdsInstanceElementAttributeValue(applElem, applElem, attrName)
		    if len(name):
		        print(name[0])
		    attrName = "values"
		    values = plot2d.AsamOdsInstanceElementAttributeValue(applElem, applElem, attrName)
		    for e in values:
		        print(e)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElementAttributeValueByBaseName(applElem: str, instanceElem: str, attrName: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a list with the value or values of a certain instance element.

	Parameters
	----------
	applElem : str
		The application element.

	instanceElem : str
		The instance element.

	attrName : str
		The base attribute name.

	Returns
	-------
	object
		A list with the value or values of the attribute.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    instanceElem = "TL1A"
		    attrName = "id"
		    id = plot2d.AsamOdsInstanceElementAttributeValueByBaseName(
		        applElem, instanceElem, attrName
		    )
		    if len(id):
		        print(id[0])
		    attrName = "name"
		    name = plot2d.AsamOdsInstanceElementAttributeValueByBaseName(
		        applElem, instanceElem, attrName
		    )
		    if len(name):
		        print(name[0])
		    attrName = "values"
		    values = plot2d.AsamOdsInstanceElementAttributeValueByBaseName(
		        applElem, instanceElem, attrName
		    )
		    for e in values:
		        print(e)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElementById(applElem: str, ieId: str) -> str:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a string with the instance element name.

	Parameters
	----------
	applElem : str
		The application element.

	ieId : str
		The instance element id.

	Returns
	-------
	str
		A string with the instance name.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "MeasurementQuantity"
		    ieId = 8
		    instanceName = plot2d.AsamOdsInstanceElementById(applElem, ieId)
		    print(instanceName)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsInstanceElements(applElem: str, aaPattern: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns instance element names, instance elements ids, application element names and base element names depending on parameters.

	Parameters
	----------
	applElem : str
		The application element name.

	aaPattern : str
		The instance element pattern to match.

	arg : str
		If '-applElem' or '-baseElem' the function returns the 2d matrix. If '-applElem -baseElem' the function returns the 3d matrix.

	Returns
	-------
	object
		It returns a list with instance element names if the last argument is blank or omitted.
		It returns a list containing pairs of instance element names and application element names if the last argument is '-applElem'.
		It returns a list containing pairs of instance element names and base element names if the last argument is '-baseElem'.
		It returns a list containing pairs of instance element names and instance elements ids if the last argument is '-ieId'.
		It returns a list containing triplets of instance element names, application element names and base element names if the last argument is '-applElem -baseElem'.
		It returns a list containing triplets of instance element names, instance elements ids and application element names if the last argument is '-ieId -applElem'.
		It returns a list containing triplets of instance element names, instance elements ids and base element names if the last argument is '-ieId -baseElem'.
		It returns a list containing quads of instance element names, instance elements ids, application element names and base element names if the last argument is '-ieId -applElem -baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    aaPattern = "*"
		    elems = plot2d.AsamOdsInstanceElements(applElem, aaPattern)
		    for e in elems:
		        print(e)
		    arg = "-applElem"
		    elems = plot2d.AsamOdsInstanceElements(applElem, aaPattern, arg)
		    for e in elems:
		        print(e[0] + "\\tApplElem:" + e[1])
		    arg = "-baseElem"
		    elems = plot2d.AsamOdsInstanceElements(applElem, aaPattern, arg)
		    for e in elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		    arg = "-ieId -applElem"
		    elems = plot2d.AsamOdsInstanceElements(applElem, aaPattern, arg)
		
		    arg = '-ieId -applElem -baseElem"'
		    for e in elems:
		        print(e[0] + "\\Id:" + e[1] + "\\tApplElem:" + e[2])
		        elems = plot2d.AsamOdsInstanceElements(applElem, aaPattern, arg)
		    for e in elems:
		        print(e[0] + "\\tId:" + e[1] + "\\tApplElem:" + e[2] + "\\tBaseElem:" + e[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsRelatedApplicationElements(applElem: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a 1d or 2d list depending on the the arguments.

	Parameters
	----------
	applElem : str
		The application element name.

	arg : str
		If '-baseElem' the function returns the 2d matrix and if not the 1d.

	Returns
	-------
	object
		It returns a list with the application element names if the second argument is blank or omitted. It returns a list containing pairs of application element names and base element names if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    elems = plot2d.AsamOdsRelatedApplicationElements(applElem)
		    for e in elems:
		        print(e)
		    arg = "-baseElem"
		    b_elems = plot2d.AsamOdsRelatedApplicationElements(applElem, arg)
		    for e in b_elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsRelatedApplicationElementsByRelationship(applElem: str, aeRelationship: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function lists related application elements according to certain relationship.

	Parameters
	----------
	applElem : str
		The application element name.

	aeRelationship : str
		The relationship type. Can be one of the following: FATHER, CHILD, INFO_TO, INFO_FROM, INFO_REL, SUPERTYPE, SUBTYPE, ALL_REL.

	arg : str
		If '-baseElem' the function returns the 2d list and if not the 1d.

	Returns
	-------
	object
		It returns a list with the application element names if the last argument is blank or omitted. It returns a list containing pairs of application element names and base element names if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    aeRelationship = "ALL_REL"
		    elems = plot2d.AsamOdsRelatedApplicationElementsByRelationship(
		        applElem, aeRelationship
		    )
		    for e in elems:
		        print(e)
		    arg = "-baseElem"
		    b_elems = plot2d.AsamOdsRelatedApplicationElementsByRelationship(
		        applElem, aeRelationship, arg
		    )
		    for e in b_elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsRelatedInstanceElementsByRelationship(applElem: str, instanceElem: str, aaPattern: str, ieRelationship: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a 1-4 dimensions matrix depending on the last argument. If 1d the output refers to all the instance element names found. If 2d then the matrix contains pairs of instance element names and instance element ids or application element names or base element names depending on the last argument. If 3d then the matrix contains triplets of instance element names and instance element ids, application element names or base element names depending on the last argument. If 4d then the matrix contains quads if instance element names, instance element ids, application element names and base element names

	Parameters
	----------
	applElem : str
		applElem = The application element name.

	instanceElem : str

	aaPattern : str
		The instance element pattern to match.

	ieRelationship : str
		The relationship type. Possible values are: FATHER, CHILD, INFO_TO, INFO_FROM, INFO_REL, SUPERTYPE, SUBTYPE, ALL_REL.

	arg : str
		If '-applElem' or if '-baseElem' the function returns the 2d list. If '-applElem -baseElem' the function returns the 3d list.

	Returns
	-------
	object
		It returns a matrix with instance element names if the last argument is blank or omitted.
		It returns a matrix containing pairs of instance element names and application element names if the last argument is '-applElem'.
		It returns a matrix containing pairs of instance element names and base element names if the last argument is '-baseElem'.
		It returns a matrix containing pairs of instance element names and instance elements ids if the last argument is '-ieId'.
		It returns a matrix containing triplets of instance element names, application element names and base element names if the last argument is '-applElem -baseElem'.
		It returns a matrix containing triplets of instance element names, instance elements ids and application element names if the last argument is '-ieId -applElem'.
		It returns a matrix containing triplets of instance element names, instance elements ids and base element names if the last argument is '-ieId -baseElem'.
		It returns a matrix containing quads of instance element names, instance elements ids, application element names and base element names if the last argument is '-ieId -applElem -baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    instanceElem = "TL1A"
		    aaPattern = "*"
		    ieRelationship = "ALL_REL"
		    elems = plot2d.AsamOdsRelatedInstanceElementsByRelationship(
		        applElem, instanceElem, aaPattern, ieRelationship
		    )
		    for e in elems:
		        print(e)
		    arg = "-applElem"
		    elems = plot2d.AsamOdsRelatedInstanceElementsByRelationship(
		        applElem, instanceElem, aaPattern, ieRelationship, arg
		    )
		    for e in elems:
		        print(e[0] + "\\tApplElem:" + e[1])
		    arg = "-baseElem"
		    elems = plot2d.AsamOdsRelatedInstanceElementsByRelationship(
		        applElem, instanceElem, aaPattern, ieRelationship, arg
		    )
		    for e in elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		    arg = "-ieId -applElem"
		    elems = plot2d.AsamOdsRelatedInstanceElementsByRelationship(
		        applElem, instanceElem, aaPattern, ieRelationship, arg
		    )
		    for e in elems:
		        print(e[0] + "\\tId:" + e[1] + "\\tApplElem:" + e[2])
		    arg = "-ieId -applElem -baseElem"
		    elems = plot2d.AsamOdsRelatedInstanceElementsByRelationship(
		        applElem, instanceElem, aaPattern, ieRelationship, arg
		    )
		    for e in elems:
		        print(e[0] + "\\tId:" + e[1] + "\\tApplElem: " + e[2] + "\\tBaseElem:" + e[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsTopLevelApplicationElements(aeType: str, args: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	List top level application arguments.

	Parameters
	----------
	aeType : str
		Base type argument. Depending on the server implementation aePattern may work as well.

	args : str
		If '-baseElem' the function returns the 2d list and if not the 1d.

	Returns
	-------
	object
		It returns a list with the application element names if the second argument is blank or omitted. It returns a list containing pairs of application element names and base element names if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    aeType = "*"
		    args = "-baseElem"
		    elems = plot2d.AsamOdsTopLevelApplicationElements(aeType)
		    for e in elems:
		        print(e)
		    b_elems = plot2d.AsamOdsTopLevelApplicationElements(aeType, args)
		    for e in b_elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsApplicationElements(aePattern: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function returns a 1d or 2d list with application elements.

	Parameters
	----------
	aePattern : str
		The application element pattern to match.

	arg : str
		If '-baseElem' the function returns the 2d matrix and if not the 1d.

	Returns
	-------
	object
		It returns a list with the application element names if the second argument is blank or omitted. It returns a list containing pairs of application element names and base element names if the second argument is '-baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    aePattern = "*"
		    arg = "-baseElem"
		    elems = plot2d.AsamOdsApplicationElements(aePattern)
		    for e in elems:
		        print(e)
		    b_elems = plot2d.AsamOdsApplicationElements(aePattern, arg)
		    for e in b_elems:
		        print(e[0] + "\\tBaseElem:" + e[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def AsamOdsFindInstanceElements(applElem: str, query: str, arg: str) -> object:

	"""
	.. deprecated:: 22.1.0
		Use `dm script functions` instead.


	This function finds instance elements.

	Parameters
	----------
	applElem : str
		The application element name that is beeing queried for its instances.

	query : str
		The instance element query to match. Right click on the statement of the Search dialog of ASAM-ODS Browser to copy the query.

	arg : str
		Argument.

	Returns
	-------
	object
		It returns a matrix with instance element names if the last argument is blank or omitted.
		It returns a matrix containing pairs of instance element names and application element names if the last argument is '-applElem'.
		It returns a matrix containing pairs of instance element names and base element names if the last argument is '-baseElem'.
		It returns a matrix containing pairs of instance element names and instance elements ids if the last argument is '-ieId'.
		It returns a matrix containing triplets of instance element names, application element names and base element names if the last argument is '-applElem -baseElem'.
		It returns a matrix containing triplets of instance element names, instance elements ids and application element names if the last argument is '-ieId -applElem'.
		It returns a matrix containing triplets of instance element names, instance elements ids and base element names if the last argument is '-ieId -baseElem'.
		It returns a matrix containing quads of instance element names, instance elements ids, application element names and base element names if the last argument is '-ieId -applElem -baseElem'.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    applElem = "LocalColumn"
		    query = 'LocalColumn.id > "10" AND LocalColumn.id < "15"'
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query)
		    for e in elems:
		        print(e)
		    print("\\n")
		
		    applElem = "LocalColumn"
		    query = "LocalColumn.id > 10 AND LocalColumn.id < 15"
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query)
		    for e in elems:
		        print(e)
		    print("\\n")
		
		    applElem = "LocalColumn"
		    query = "LocalColumn.id >= 10 AND LocalColumn.id <= 15"
		    arg = "-ieId"
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query, arg)
		    for e in elems:
		        print(e[0] + "\\t" + e[1])
		    print("\\n")
		
		    applElem = "Submatrix"
		    query = "LocalColumn.id = 10 OR NOT LocalColumn.id <> 15"
		    arg = "-ieId -applElem"
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query, arg)
		    for e in elems:
		        print(e[0] + "\\t" + e[1] + "\\t" + e[2])
		    print("\\n")
		
		    applElem = "LocalColumn"
		    query = "LocalColumn.name LIKE 'TL*' AND ( LocalColumn.name LIKE '*A' AND LocalColumn.name LIKE '*1A' )"
		    arg = "-ieId -applElem -baseElem"
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query, arg)
		    for e in elems:
		        print(e[0] + "\\t" + e[1] + "\\t" + e[2] + "\\t" + e[3])
		    print("\\n")
		
		    applElem = "LocalColumn"
		    query = "Submatrix.name LIKE 10HZ"
		    arg = "-ieId -applElem -baseElem"
		    elems = plot2d.AsamOdsFindInstanceElements(
		        "LocalColumn", "Submatrix.name LIKE 10HZ", "-ieId -applElem -baseElem"
		    )
		    for e in elems:
		        print(e[0] + "\\t" + e[1] + "\\t" + e[2] + "\\t" + e[3])
		    print("\\n")
		
		    applElem = "Test"
		    query = "Submatrix.name LIKE 10HZ"
		    arg = "-ieId -applElem -baseElem"
		    elems = plot2d.AsamOdsFindInstanceElements(applElem, query, arg)
		    for e in elems:
		        print(e[0] + "\\t" + e[1] + "\\t" + e[2] + "\\t" + e[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 22.1.0. Use  dm script functions instead.", DeprecationWarning)

def CreateEmptyCurveGroup(window_name: str, group_name: str, parent: str) -> object:

	"""

	This function creates an empty curve group in an existing plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window

	group_name : str
		Name of the group.

	parent : str
		Parent plot or group. If a group with the given name already exists then this function will fail.

	Returns
	-------
	object
		Upon success, it returns a CurveGroup object referring to the newly created group.
		Else, None is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "Group18_20"
		    parent = "0"
		
		    cg = plot2d.CreateEmptyCurveGroup(window_name, group_name, parent)
		    if cg:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AddCurvesOnCurveGroup(window_name: str, group_name: str, curve_ids: object) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.CurveGroup.get_subgroups` instead.


	This function adds some specific curves on an existing curve group of a given plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window.

	group_name : str
		Name of the group. If a group with the given name does not exist then this function will fail.

	curve_ids : object
		List with the ids of curves of the specified window.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "Group18_20"
		
		    curve_ids = list()
		    curve_ids.append(1)
		    curve_ids.append(2)
		    curve_ids.append(3)
		
		    ret = plot2d.AddCurvesOnCurveGroup(window_name, group_name, curve_ids)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.CurveGroup.get_subgroups instead.", DeprecationWarning)

def UngroupCurveGroup(window_name: str, group_name: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.CurveGroup.ungroup` instead.


	This function ungroups all curves of a given curve group of a given 2d plot window specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	group_name : int
		Name of the group.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "Group18_20"
		    ret = plot2d.UngroupCurveGroup(window_name, group_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.CurveGroup.ungroup instead.", DeprecationWarning)

def DeleteCurveGroup(window_name: str, group_name: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.CurveGroup.delete` instead.


	This function deletes all curves of a given curve group of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the window.

	group_name : int
		Name of the group.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    group_name = "Group18_20"
		    ret = plot2d.DeleteCurveGroup(window_name, group_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.CurveGroup.delete instead.", DeprecationWarning)

def CurvesOfPlotByName(curve_name: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curves` instead.


	This function finds curves of a plot with a given name.

	Parameters
	----------
	curve_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.  
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_name = "*HEAD*"
		    plot_id = 0
		    name_curves = plot2d.CurvesOfPlotByName(window_name, plot_id, curve_name)
		    for c in name_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curves instead.", DeprecationWarning)

def CurveGroupsOfPlotByName(group_name: str, plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.get_curve_groups` instead.


	This function finds curve groups of a given plot.

	Parameters
	----------
	group_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.CurveGroup

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    group_name = "*Argy*"
		    CurveGroups = plot2d.CurveGroupsOfPlotByName(window_name, plot_id, group_name)
		    for cg in CurveGroups:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.get_curve_groups instead.", DeprecationWarning)

def AdvFiltersOnCurvesByPlot(adv_filters: object, plot_id: int, window_name: str) -> object:

	"""

	This function allows the user to collect curves of a plot through some advanced filters.

	Parameters
	----------
	adv_filters : object
		List with the advanced filters as string expressions. Their syntax is the same with the commands referring to advanced filters.

	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:>=5:Keep All")
		    adv_filters.append("intersect:Curves:ymax::Max 2")
		    window_name = "Window1"
		    plot_id = 0
		
		    collected_curves = plot2d.AdvFiltersOnCurvesByPlot(
		        window_name, plot_id, adv_filters
		    )
		    for c in collected_curves:
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

def AdvFiltersOnCurvesByPlotWithRange(window_name: str, plot_id: int, adv_filters: object, xmin: float, xmax: float) -> object:

	"""

	This function allows the user to collect curves of a plot through some advanced filters in given x-axis range.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	adv_filters : object
		List with the advanced filters as string expressions. Their syntax is the same with the commands referring to advanced filters.

	xmin : float
		Minimum x value.

	xmax : float
		Maximum x value.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    adv_filters = list()
		    adv_filters.append("add:Curves:id:>=5:Keep All")
		    adv_filters.append("intersect:Curves:ymax::Max 2")
		    xmin = 0.01
		    xmax = 0.02
		    window_name = "Window1"
		    plot_id = 0
		
		    collected_curves = plot2d.AdvFiltersOnCurvesByPlotWithRange(
		        window_name, plot_id, adv_filters, xmin, xmax
		    )
		    for c in collected_curves:
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

def CurvesTypesTheseus(filename: str) -> object:

	"""

	This function finds curves types of a THESEUS-FE file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		Returns a list with the types of the curves of the given file. Each member of the list is another list with 4 elements.
		In position 0, internal lists contain a string referring to the categories of the curves.
		In position 1, internal lists contain a list with strings referring to the types of the curves.
		In position 2, internal lists contain a list with strings referring to the ids of the the entities.
		In position 3, internal lists contain a list with strings referring to the variables.
		Upon failure, a list with zero length is returned.

	See Also
	--------
	plot2d.LoadCurvesTheseus

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Theseus/Theseus.hdf"
		    curves_categories = plot2d.CurvesTypesTheseus(filename)
		    for one_category in curves_categories:
		        category = one_category[0]  # One category of curves
		        print(category)
		        print("***********")
		        types = one_category[1]  # List with types
		        for one_type in types:  # Id of type
		            print(one_type)
		        parts = one_category[2]  # List with parts
		        for one_part in parts:  # Id of part
		            print(one_part)
		        variables = one_category[3]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("######################################")
		
		        # The results of this function can be used as arguments in function LoadCurvesTheseus
		        # plot2d.LoadCurvesTheseus('Window1',0,filename,category,types,parts,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesTheseusWithNames(filename: str) -> object:

	"""

	This function finds curves types of a THESEUS-FE file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		Returns a list with the types of the curves of the given file. Each element of the list is another list with 4 elements.
		In position 0, internal lists contain a string referring to the categories of the curves.
		In position 1, internal lists contain a list with strings referring to the types of the curves.
		In position 2, internal lists contain another list which contains in position 0 the id of the entity and in position 1 the name of the entity.
		In position 3, internal lists contain a list with strings referring to the variables.
		Upon failure, a list with zero length is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Theseus/Theseus.hdf"
		    curves_categories = plot2d.CurvesTypesTheseusWithNames(filename)
		    for one_category in curves_categories:
		        category = one_category[0]  # One category of curves
		        print(category)
		        print("***********")
		        types = one_category[1]  # List with types
		        for one_type in types:  # Id of type
		            print(one_type)
		        parts = one_category[2]  # List with parts
		        for one_part in parts:  # Id of part
		            print(one_part)
		        variables = one_category[3]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("######################################")
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesTheseus(window_name: str, plot_id: int, filename: str, categories: object, types: object, parts: object, variables: object) -> object:

	"""

	This function loads curves from a THESEUS-FE file in an existing plot of a given plot2d window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	categories : object
		A list whose elements are strings representing the data categories which are going to be loaded (e.g. 'T[C]', 'FE_Energy[J]', 'lin_iter', etc.).

	types : object
		A list whose elements are strings representing the types of data which are going to be loaded (e.g. 'GROUPs', 'VOLUMEs', 'Convergence', etc.).

	parts : object
		A list whose elements are strings representing the ids of parts. If the 1st member of argument parts is 'all', then curves of all parts are loaded.

	variables : object
		A list whose elements are strings representing the abbreviations of variables which are going to be loaded (e.g. "mP" etc.). If the 1st member of argument 'variables' is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Theseus/07_SoakCycle_COMPLETED.hdf"
		    categories = ["GROUPs", "VOLUMEs"]
		    types = ["T[C]"]
		    parts = ["all"]
		    variables = ["all"]
		    new_curves = plot2d.LoadCurvesTheseus(
		        window_name, plot_id, filename, categories, types, parts, variables
		    )
		    for c in new_curves:
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

def StringFromPlotAdvFilters(initial_filter: str) -> object:

	"""

	This function allows the user to specify the advanced filter for plots. The execution of the script will stop and a window will open in order for the user to specify its advanced filter entries.

	Parameters
	----------
	initial_filter : str
		Initial advanced filter (e.g 'add:Curves:all::Keep All').

	Returns
	-------
	object
		It returns a list where each member of the list is a string referring to a selected advanced filter entry.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    model_id = 0
		    all_filters = plot2d.StringFromPlotAdvFilters(model_id)
		    for filter in all_filters:
		        print(filter)
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsLegendOfPlotVisible(plot_id: int, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Legend.get_visible` instead.


	This function gets the visibility of the legend of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		Upon success, it returns 1 if the legend is visible and 0 otherwise.
		Upon failure, it returns 0.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    legend_visible = plot2d.IsLegendOfPlotVisible(window_name, plot_id)
		    print(legend_visible)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Legend.get_visible instead.", DeprecationWarning)

def PositionOfPlotLegend(plot_id: int, window_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Legend.get_position` instead.


	This function finds the position of the legend of a given plot.

	Parameters
	----------
	plot_id : int
		Id of the plot.

	window_name : str
		Name of the window.

	Returns
	-------
	object
		Upon success, it returns a list with 2 float elements referring to the position of the legend of the given plot. 
		Else, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    legend_pos = plot2d.PositionOfPlotLegend(window_name, plot_id)
		    if len(legend_pos):
		        print(legend_pos[0], legend_pos[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Legend.get_position instead.", DeprecationWarning)

def CurvesTypesOp2(filename: str) -> object:

	"""

	This function finds curves types of a NASTRAN OP2 file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 6 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the type of data of the X axis.
		In position 2, internal lists contain a list with integers referring to the cycles of the model.
		In position 3, internal lists contain a list with integers referring to the states of the model.
		In position 4, internal lists contain a list with strings referring to the ids of the entities.
		In position 5, internal matrices contain a list with strings referring to the variables.
		In position 6, internal matrices contain a list with strings referring to the fluid grids.
		In position 7, internal matrices contain a list with strings referring to the subcase states.
		In position 8, internal matrices contain a list with matrices referring to the A/LC points used.
		Fluid grids are taken into account only for some specific types (e.g. 'panelparticipationfactors', 'fluidmodalparticipationfactors', 'structuremodalparticipationfactors', 'normalizedgridparticipationfactors').
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Nastran.op2"
		    curves_types = plot2d.CurvesTypesOp2(filename)
		    for one_type in curves_types:
		        type = one_type[0]
		        print(type)  # One type of curves
		        print("****")
		        all_xaxis = one_type[1]  # List with types of X axis data
		        for xaxis in all_xaxis:
		            print(xaxis)  # Type of X axis data
		        print(
		            "------------------------------------------------------------------------"
		        )
		        cycles = one_type[2]  # List with cycles
		        for one_cycle in cycles:
		            print(one_cycle)  # Number of cycle
		        print(
		            "------------------------------------------------------------------------"
		        )
		        states = one_type[3]  # List with states
		        for one_state in states:
		            print(one_state)  # Number of state
		        print(
		            "------------------------------------------------------------------------"
		        )
		        entities = one_type[4]  # List with entities
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "------------------------------------------------------------------------"
		        )
		        variables = one_type[5]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print(
		            "------------------------------------------------------------------------"
		        )
		        fluidgrids = one_type[6]  # List with fluid grids
		        for one_fluidgrid in fluidgrids:
		            print(one_fluidgrid)
		        print(
		            "------------------------------------------------------------------------"
		        )
		        subcase_states = one_type[7]  # List with subcase states
		        for one_state in subcase_states:
		            print(one_state)
		        print(
		            "------------------------------------------------------------------------"
		        )
		        alc_points = one_type[8]  # List with A/LC Points
		        for one_alc_point in alc_points:
		            print(one_alc_point)
		        print("#####################################")
		
		
		if __name__ == "__main__":
		    main()


	"""

def PointsXValuesOfCurve(window_name: str, curve_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points_x_values` instead.


	This function collects X values of all points of a given curve specified by its id and the window it belongs to.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	Returns
	-------
	object
		It returns a list where each member of the list is a float number referring to the X value of one specific point of the given curve.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    all_xvalues = plot2d.PointsXValuesOfCurve(window_name, curve_id)
		    for xval in all_xvalues:
		        print(xval)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points_x_values instead.", DeprecationWarning)

def PointsYValuesOfCurve(window_name: str, curve_id: int, curve_type: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points_y_values` instead.


	This function collects Y values of all points of a given curve specified by its id and the window it belongs to.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	curve_type : str, optional
		Type of the curve. Possible values are:
		- 'real' (default)
		- 'imaginary'
		- 'magnitude'
		- 'phase'

	Returns
	-------
	object
		Upon success, it returns a list where each member of the list is a float number referring to the Y value of one specific point of the given curve.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    curve_type = "magnitude"
		    all_yvalues = plot2d.PointsYValuesOfCurve(window_name, curve_id, curve_type)
		    for yval in all_yvalues:
		        print(yval)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points_y_values instead.", DeprecationWarning)

def CurvesTypesNsoft() -> object:

	"""

	This function finds curve types of a nSoft file.

	Returns
	-------
	object
		It returns a list of strings that contain the ids of the channels of the given file.
		Upon failure an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesNsoft

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/Nsoft.dac"
		    channels = plot2d.CurvesTypesNsoft(filename)
		    for channel_name in channels:
		        print(channel_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesNsoft(window_name: str, plot_id: int, filename: str, channels: object) -> object:

	"""

	This function loads curves from a nSoft file in an existing plot of a given plot2d window.

	Parameters
	----------
	window_name : str
		Name of the window. Empty string to load on Data List

	plot_id : int
		Plot id.

	filename : str, optional
		Path to file.

	channels : object
		A list of strings the correspond to the channels to be loaded. If the first element of the list is 'all', then all channels will be loaded.

	Returns
	-------
	object
		It returns a list where each element of the list is an object of type curve referring to one newly loaded curve of the given plot2d window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/Nsoft.dac"
		    channels = ["Nsoft"]
		    new_curves = plot2d.LoadCurvesNsoft(window_name, plot_id, filename, channels)
		    for c in new_curves:
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

def ValuesXOfCurveForY(window_name: str, curve_id: int, axis_id: int, yvalue: float) -> object:

	"""

	This function calculates X values for a given Y value of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window of the curve.

	curve_id : int
		Id of the curve.

	axis_id : int
		Id of the axis.

	yvalue : float
		Value of the Y-axis.

	Returns
	-------
	object
		It returns a list with float numbers that correspond to the X-values of the curve for the given Y-value.
		Upon failure an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    curve_id = 1
		    axis_id = 0
		    yvalue = 0.23
		    all_xvalues = plot2d.ValuesXOfCurveForY(window_name, curve_id, axis_id, yvalue)
		    for xvalue in all_xvalues:
		        print(xvalue)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ValuesXOfCurveForYComplex(window_name: str, curve_id: int, axis_id: int, yvalue: float) -> object:

	"""

	This function calculates X values for a given Y phase value of a given curve.

	Parameters
	----------
	window_name : str
		Name of the window of the curve.

	curve_id : int
		Id of the curve.

	axis_id : int
		Id of the axis.

	yvalue : float
		Value of the Y-axis.

	Returns
	-------
	object
		It returns a list with float numbers that correspond to the X-values of the curve for the given Y-value.
		Upon failure an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    curve_id = 1
		    axis_id = 0
		    yvalue = 335
		    all_xvalues = plot2d.ValuesXOfCurveForYComplex(
		        window_name, curve_id, axis_id, yvalue
		    )
		    for xvalue in all_xvalues:
		        print(xvalue)
		
		
		if __name__ == "__main__":
		    main()


	"""

def PointsdBValuesOfCurve(window_name: str, curve_id: int, db_filter: str, db_value: float, db_factor: float) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_points_db_values` instead.


	This function collects dB values of all points of a given curve specified by its id and the window it belongs to.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	db_filter : str, optional
		Decibel filtering. Its possible values are:
		- db (default)
		- dba
		- dbb
		- dbc
		- dbd

	db_value : float, optional
		Decibel reference value. Default value is 1.

	db_factor : float, optional
		Decibel factor. Its possible values are:
		- 10 
		- 20 (default)

	Returns
	-------
	object
		It returns a list where each member is a float number referring to the dB value of one specific point of the given curve.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    db_filter = "dba"
		    db_value = 2e-11
		    all_dbvalues = plot2d.PointsdBValuesOfCurve(
		        window_name, curve_id, db_filter, db_value
		    )
		    for dbval in all_dbvalues:
		        print(dbval)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_points_db_values instead.", DeprecationWarning)

def IncrementOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int) -> float:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_increment` instead.


	This function finds the increment of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	Returns
	-------
	float
		Upon success, it returns a float referring to the increment of the specified plot axis.
		Else, it returns -1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    increment = plot2d.IncrementOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    print(increment)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_increment instead.", DeprecationWarning)

def SetIncrementOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id, increment: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.set_increment` instead.


	This function sets the increment of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : 
		Id of the axis.

	increment : float
		Increment of the axis.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    increment = 3.5
		    plot2d.SetIncrementOfPlotAxis(window_name, plot_id, axis_type, axis_id, increment)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.set_increment instead.", DeprecationWarning)

def AttributeOfPoint(attrib_name: str, curve_id: int, point_id: int, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.get_attributes` instead.


	This function returns the value of a specific attribute referring to a given point of curve.

	Parameters
	----------
	attrib_name : str
		Name of the attribute.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	window_name : str
		Name of the window.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    attrib_name = "Filename"
		    attrib_value = plot2d.AttributeOfPoint(window_name, curve_id, point_id, attrib_name)
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.get_attributes instead.", DeprecationWarning)

def SetAttributeOfPoint(window_name: str, curve_id: int, point_id: int, attrib_name: str, attrib_value: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.set_attribute` instead.


	This function sets the value of a specific attribute referring to a given point of a curve. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	attrib_name : str
		Name of the attribute.

	attrib_value : str
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 1
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		
		    ret = plot2d.SetAttributeOfPoint(
		        window_name, curve_id, point_id, attrib_name, attrib_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.set_attribute instead.", DeprecationWarning)

def SetSubAttributeOfPoint(window_name: str, curve_id: int, point_id: int, group_name: str, attrib_name: str, attrib_value: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.set_attribute` instead.


	This function sets the value of a specific point attribute of a group to a given value.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	group_name : str
		Name of the attribute group.

	attrib_name : str
		Name of the attribute. If the given attribute and group do not exist they are automatically created.

	attrib_value : str
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 1
		    group_name = "test_group"
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		    plot2d.SetSubAttributeOfPoint(
		        window_name, curve_id, point_id, group_name, attrib_name, attrib_value
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.set_attribute instead.", DeprecationWarning)

def SubAttributeOfPoint(attrib_name: str, curve_id: int, point_id: int, group_name: str, window_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Point.get_attributes` instead.


	This function returns the value of a specific attribute of a group referring to a given point of a curve.

	Parameters
	----------
	attrib_name : str
		Name of the attribute.

	curve_id : int
		Id of the curve.

	point_id : int
		Id of the point.

	group_name : str
		Name of the attribute group.

	window_name : str
		Name of the window.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    point_id = 1
		    attrib_name = "test_attribute"
		    group_name = "test_group"
		    attrib_value = plot2d.SubAttributeOfPoint(
		        window_name, curve_id, point_id, group_name, attrib_name
		    )
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Point.get_attributes instead.", DeprecationWarning)

def AttributesOfCurve(window_name: str, curve_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Curve.get_attributes` instead.


	This function collects all attributes of a given curve of a specified window.

	Parameters
	----------
	window_name : str
		Name of the window.

	curve_id : int
		Id of the curve.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 1
		    all_attributes = plot2d.AttributesOfCurve(window_name, curve_id)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print(attrib_name)
		        print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Curve.get_attributes instead.", DeprecationWarning)

def CurvesOfPlotAxis(window_name: str, plot_id: int, axis_type: str, axis_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.PlotAxis.get_curves` instead.


	This function finds the curves of a plot axis of a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	axis_type : str
		Type of the axis. Its possible values are:
		- 'xaxis': X axis
		- 'yaxis': Y axis
		- 'zaxis': Z axis
		- 'caxis': Y complex axis

	axis_id : int
		Id of the axis.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one specific curve of a plot axis of a given plot.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    axis_type = "xaxis"
		    axis_id = 0
		    axis_curves = plot2d.CurvesOfPlotAxis(window_name, plot_id, axis_type, axis_id)
		    for c in axis_curves:
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

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.PlotAxis.get_curves instead.", DeprecationWarning)

def CurvesTypesHGdata(filename: str) -> object:

	"""

	This function finds curves types of an HGdata file.

	Parameters
	----------
	filename : str
		Name of the file

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the data.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/sample.hgdata"
		    curves_types = plot2d.CurvesTypesHGdata(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        data = one_type[1]  # List with data
		        for one_data in data:
		            print(one_data)  # Data
		        print("###############################################")
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesHGdata(window_name: str, plot_id: int, filename: str, type: str, data: object) -> object:

	"""

	This function loads curves from an HGdata file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded.

	data : object
		A list whose members are strings referring to the data. If the 1st member of argument states is 'all', then all curves will be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/sample.hgdata"
		    type = "Design Variables"
		    data = ["Design Variable        4  g7191337", "Design Variable        5  g7191341"]
		    new_curves = plot2d.LoadCurvesHGdata(window_name, plot_id, filename, type, data)
		    for c in new_curves:
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

def CurvesTypesTAITherm(filename: str) -> object:

	"""

	This function finds curves types of a TAITherm file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the the parts.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesTAITherm

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/TAITherm.tdf"
		    curves_types = plot2d.CurvesTypesTAITherm(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        parts = one_type[1]  # List with parts
		        for one_part in parts:  # Id of part
		            print(one_part)
		        print("---------------------------------------------------------------------")
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("#####################################################################")
		
		        # The results of this function can be used as arguments in function LoadCurvesTAITherm
		        # plot2d.LoadCurvesTAITherm('Window1',0,filename,type,parts,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesTAIThermWithNames(filename: str) -> object:

	"""

	This function finds curves types of a TAITherm file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list which contains in position 0 the id of the part and in position 1 the name of the part.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/TAITherm.tdf"
		    curves_types = plot2d.CurvesTypesTAIThermWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        parts = one_type[1]  # List with parts
		        for one_part in parts:
		            part_id = one_part[0]  # Id of part
		            print(part_id)
		            part_name = one_part[1]  # Name of part
		            print(part_name)
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesTAITherm(window_name: str, plot_id: int, filename: str, type: str, parts: object, variables: object) -> object:

	"""

	This function loads curves from a TAITherm file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded (e.g. 'Temperature Data', 'Conduction Data', 'Solution Case Curve Data', etc.).

	parts : object
		A list whose elements are strings representing the ids of parts. If the 1st member of argument parts is 'all', then curves of all parts are loaded.

	variables : object
		A list whose elements are strings representing the abbreviations of variables which are going to be loaded (e.g. 'm2IF', 'p7-12', etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/TAITherm.tdf"
		    type = "Conduction Data"
		    variables = ["m2IF", "mBNH", "mFOH"]
		    parts = ["all"]
		    new_curves = plot2d.LoadCurvesTAITherm(
		        window_name, plot_id, filename, type, parts, variables
		    )
		    for c in new_curves:
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

def CurvesTypesCGNS(filename: str) -> object:

	"""

	This function finds curves types of a CGNS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 4 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the the parts.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesCGNS

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/CGNS.cgns"
		    curves_types = plot2d.CurvesTypesCGNS(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        parts = one_type[1]  # List with parts
		        for one_part in parts:  # Id of part
		            print(one_part)
		        print("---------------------------------------------------------------------")
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		        print("#####################################################################")
		
		        # The results of this function can be used as arguments in function LoadCurvesCGNS
		        # plot2d.LoadCurvesCGNS('Window1',0,filename,type,parts,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesCGNSWithNames(filename: str) -> object:

	"""

	This function finds curves types of a CGNS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list which contains in position 0 the id of the part and in position 1 the name of the part.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/CGNS.cgns"
		    curves_types = plot2d.CurvesTypesCGNSWithNames(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        parts = one_type[1]  # List with parts
		        for one_part in parts:
		            part_id = one_part[0]  # Id of part
		            print(part_id)
		            part_name = one_part[1]  # Name of part
		            print(part_name)
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:  # Name of variable
		            print(one_variable)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesCGNS(window_name: str, plot_id: int, filename: str, type: str, parts: object, variables: object) -> object:

	"""

	This function loads curves from a CGNS file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded. CGNS supports only 'Convergence History' type.

	parts : object
		A list whose elements are strings representing the names of variable types (entities).

	variables : object
		A list whose elements are strings representing the names of variables which are going to be loaded (e.g. 'CoefLift, 'Pressure', etc.).

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/bump1.cgns"
		    type = "Convergence History"
		    variables = ["CoefLift"]
		    parts = ["GlobalConvergenceHistory"]
		    new_curves = plot2d.LoadCurvesCGNS(
		        window_name, plot_id, filename, type, parts, variables
		    )
		    for c in new_curves:
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

def CurvesTypesPermas(filename: str) -> object:

	"""

	This function finds curves types of a Permas file.

	Parameters
	----------
	filename : str
		Name of the file

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the ids of the entities.
		In position 2, internal lists contain a list with strings referring to the variables (user defined variables are included).
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesPermas

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/topo.post"
		    curves_types = plot2d.CurvesTypesPermas(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        entities = one_type[1]  # List with entities ids
		        for one_entity in entities:
		            print(one_entity)  # Id of entity
		        print(
		            "------------------------------------------------------------------------------------"
		        )
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		        print("##########################################")
		    # The results of this function can be used as arguments in function "LoadCurvesPermas"
		    # plot2d.LoadCurvesPermas('Window1',0,filename,type,entities,variables)
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesPermas(window_name: str, plot_id: int, filename: str, type: str, entities: object, variables: object) -> object:

	"""

	This function loads curves from a Permas file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of the data.

	entities : object
		List with entities strings. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	variables : object
		List with variables strings. If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/topo.post"
		    type = "Node"
		    entities = ["880", "881"]
		    variables = ["translational_magnitude_(tm)"]
		    new_curves = plot2d.LoadCurvesDyna(
		        window_name, plot_id, filename, type, entities, variables
		    )
		    for c in new_curves:
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

def LoadCurvesAdams(entities: object, filename: str, plot_id: int, type: str, variables: object, window_name: str) -> object:

	"""

	This function loads curves from an ADAMS file in an existing plot of a given 2d plot2d window.

	Parameters
	----------
	entities : object
		A list whose members are strings referring to the names of the entities or entities/markers which are going to be loaded. If the 1st member of argument entities is 'all', then curves of all entities are loaded.

	filename : str
		Name of the file.

	plot_id : int
		Id of the plot.

	type : str
		Type of data which to load (e.g. 'part', 'joint', 'motion' etc.).

	variables : object
		A list whose members are strings referring to the variables which are going to be loaded (e.g. 'X','Y','Z','VX' etc.). If the 1st member of argument variables is 'all', then curves of all variables are loaded.

	window_name : str
		Name of the plot2d window.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "files/ADAMS/test/test.res"
		    type = "part"
		    entities = ["PART_1/MAR_1"]
		    variables = ["Y"]
		    new_curves = plot2d.LoadCurvesAdams(
		        window_name, plot_id, filename, type, entities, variables
		    )
		    for c in new_curves:
		        print(
		            c.id,
		            c.name,
		            c.plot_id,
		            c.visible,
		            c.selected,
		            c.window_name,
		            c.page_id,
		            c.command,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesAdams(filename: str) -> list:

	"""

	This function finds curves types of an ADAMS file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	list
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the names of the entities or entities/markers.
		In position 2, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesAdams

	Examples
	--------
	::

		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "files/ADAMS/test.res"
		    curves_types = plot2d.CurvesTypesAdams(filename)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print("========================================")
		        print(type)
		        print("========================================")
		        entities = one_type[1]  # List with entities ids
		        for entity_name in entities:
		            print(entity_name)  # Name of Entity
		        variables = one_type[2]  # List with variables
		        for one_variable in variables:
		            print(one_variable)  # Name of variable
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesAtfx(filename: str, useNames: str) -> object:

	"""

	This function finds curves types of an Atfx file.

	Parameters
	----------
	filename : str
		Name of the file.

	useNames : str
		Decide if names or ids should be returned. If names not found then ids will be returned instead.
		Possible values: 'ids', 'names'

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file. Every type has 6 members:
		At position 0: a string with the type name
		At position 1: internal lists contain a list with strings referring to the available runs
		At position 2: internal lists contain a list with strings referring to the available measurements
		At position 3: internal lists contain a list referring to the available times (if any)
		At position 4: internal lists contain a list with strings referring to the available reference nodes
		At position 5: internal lists contain a list with strings referring to the available response nodes
		
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.LoadCurvesAtfx

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/example.atfx"
		    useNodeNames = "ids"
		    curves_types = plot2d.CurvesTypesAtfx(filename, useNodeNames)
		    for one_type in curves_types:
		        type = one_type[0]  # One type of curves
		        print(type)
		        print("****")
		        runs = one_type[1]  # List with runs
		        for one_run in runs:
		            print(one_run)  # Run name
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        measurements = one_type[2]  # List with measurements
		        for one_measurement in measurements:
		            print(one_measurement)  # Run measurement
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        times = one_type[3]  # List with times
		        for one_time in times:
		            print(one_time)  # Time
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        reference_nodes = one_type[4]  # List with reference nodes
		        for ref_node in reference_nodes:
		            print(ref_node)  # Reference node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        responce_nodes = one_type[5]  # List with responce nodes
		        for resp_node in responce_nodes:
		            print(resp_node)  # Responce node
		        print(
		            "---------------------------------------------------------------------------------------------"
		        )
		        print("###############################################")
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesAtfx(window_name: str, plot_id: int, filename: str, type: str, runs: object, measurements: object, times: object, reference_nodes: object, response_nodes: object) -> object:

	"""

	This function loads curves from an Atfx file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		Name of the 2d plot window.

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which are going to be loaded (e.g. 'Acceleration' etc.).

	runs : object
		A list of runs whose members are strings, referring to the name of run, or ['all'] to include all available runs in the file

	measurements : object
		A list of measurements whose members are strings, referring to the name of measurements, or ['all'] to include all available measurements in the file

	times : object
		A list of times whose members are doubles, or  ['all'] to include all available times in the file

	reference_nodes : object
		A list whose members are strings referring to the reference nodes (e.g. '16->7+Z', '30->11+Z', etc.). If the 1st member of argument reference_nodes is 'all', then curves of all reference_nodes are loaded.

	response_nodes : object
		A list whose members are strings referring to the respose nodes (e.g. '5->12+X', '22->1+Y' etc.. If the 1st member of argument response_nodes is 'all', then curves of all response_nodes are loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	See Also
	--------
	plot2d.Curve, plot2d.CurvesTypesAtfx

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "/home/examples/curves/example.atfx"
		    window_name = "Window1"
		    plot_id = 0
		    type = "Acceleration Spectrum 3D"
		    runs = ["all"]
		    measurements = ["all"]
		    times = ["all"]
		    reference_nodes = ["all"]
		    response_nodes = ["all"]
		    new_curves = plot2d.LoadCurvesAtfx(
		        window_name,
		        plot_id,
		        filename,
		        type,
		        runs,
		        measurements,
		        times,
		        reference_nodes,
		        response_nodes,
		    )
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesMetadb(window_name: str, plot_id: int, filename: str, arguments: str) -> object:

	"""

	This function loads curves from a MetaDB file in an existing plot of a given 2d plot window.

	Parameters
	----------
	window_name : str
		The name of the window. Empty string to load on Data List

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	arguments : str
		A list of arguments that specify the curves that are to be loaded.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "/home/examples/curves/curves.metadb"
		    args = ["{Page=0}{Window=Window1}{Curve id=4-10}"]
		    new_curves = plot2d.LoadCurvesMetadb(window_name, 0, filename, args)
		    for c in new_curves:
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

def DynamicTimeWarping(C, T: object):

	"""

	This function calculates the Dynamic Time Warping matrix from two arrays C,T of the same length.

	Parameters
	----------
	C : 
		Array C

	T : object
		Array T

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import plot2d
		
		
		def main():
		    T = {1, 2, 3, 4, 5}
		    C = {2, 3, 4, 5, 6}
		
		    _dtw_ = plot2d.DynamicTimeWarping(C, T)
		    print(_dtw_)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CopyPasteSomeCurves(source_window: object, curves: object, target_plot: object) -> bool:

	"""

	This function copies curves from a page and window to another page, window and plot, without activating the pages.

	Parameters
	----------
	source_window : object
		An object of class Window, from which the curves will be copied. It must be a 2d window.

	curves : object
		An object that represents which curves will be copied. This object can be a curve, a list of curves, a range of curves (as a string), or the string 'all'.

	target_plot : object
		An object of class Plot.

	Returns
	-------
	bool
		Upon success, it returns True.
		Upon Failure, it returns False.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    source = windows.Window("Window1", page_id=0)
		    target = plot2d.Plot(id=1, window_name="Window2", page_id=0)
		    curves = "all"
		
		    ok = plot2d.CopyPasteSomeCurves(source, curves, target)
		    print(ok)
		
		    
		\tThe function arguments have been changed.
		\t=========================================
		\tFrom version 21.0.0 the function is called with the above three arguments.
		\tIn older versions from v19.1.1 where the function was introduced, the function was accepting six arguments.
		\t*from_page_id       : integer        Id of the page to copy curves from.
		\t*from_window_name   : string         Name of the plot2d window to copy curves from.
		\t*curve_ids          : string         List of curves to be copied (1-6,9,10-17 etc)
		\t*to_page_id         : integer        Id of the page to copy curves to.
		\t*to_window_name     : string         Name of the plot2d window to copy curves to.
		\t*to_plot_id         : integer        Id of the plot to copy to.
		\t
		\tFor compatibility reasons if the function is given with six arguments is still functional.
		\tHowever it is recommended not to use this syntax form of the function and use the one with the three arguments instead.
		\t
		
		     
		\tfrom_page_id = 0
		\tfrom_window_name = 'Window1'
		\tcurve_ids = 'all'
		\tto_page_id = 0
		\tto_window_name = 'Window2'
		\tto_plot_id = 1
		\tok = plot2d.CopyPasteSomeCurves(from_page_id, from_window_name, curve_ids, to_page_id,to_window_name, to_plot_id)
		\tprint(ok)
		\t
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadCurvesActran(window_name: str, plot_id: int, filename: str, type: str, loadcases: object, entities: object, variables: object) -> object:

	"""

	This function loads curves from an ACTRAN file in an existing plot of a given 2d plot2d window.

	Parameters
	----------
	window_name : str
		Name of the plot2d window.

	plot_id : int
		Id of the plot.

	filename : str
		Name of the file.

	type : str
		Type of data which to load (e.g. 'DOMAIN', 'POINT_1', 'SURFACE')

	loadcases : object
		List of loadcases or "all"

	entities : object
		List of entities or "all"

	variables : object
		List of variables or "all"

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly loaded curve of the given 2d plot window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    filename = "files/ACTRAN/test.plt"
		    type = "DOMAIN"
		    loadcases = ["all"]
		    entities = ["Acoustic1"]
		    variables = ["MS_Pressure"]
		    new_curves = plot2d.LoadCurvesActran(
		        window_name, plot_id, filename, type, loadcases, entities, variables
		    )
		    for c in new_curves:
		        print(
		            c.id,
		            c.name,
		            c.plot_id,
		            c.visible,
		            c.selected,
		            c.window_name,
		            c.page_id,
		            c.command,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesActran(filename: str) -> object:

	"""

	This function finds curves types of an ACTRAN file.

	Parameters
	----------
	filename : str
		Name of the file.

	Returns
	-------
	object
		It returns a list with the types of the curves of the given file.
		Each member of the list is another list with 3 members.
		In position 0, internal lists contain a string referring to the type of the curves.
		In position 1, internal lists contain a list with strings referring to the loadcases
		In position 2, internal lists contain a list with strings referring to the names of the entities or entities/markers.
		In position 3, internal lists contain a list with strings referring to the variables.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "files/ACTRAN/test.plt"
		    curves_types = plot2d.CurvesTypesActran(filename)
		
		    for one_type in curves_types:
		        type = one_type[0]
		        print("TYPE = " + type)  # One type of curves
		        print("Loadcases--------------------------------------------")
		        loadcases = one_type[1]  # List with loadcases
		        for one_loadcase in loadcases:
		            print(one_loadcase)  # Id of loadcase
		        print("Entities--------------------------------------------")
		        entities = one_type[2]  # List with entities
		        for one_entity in entities:
		            print("\\t" + one_entity)  # Id of entity
		        print("Variables-------------------------------------------")
		        variables = one_type[3]  # List with variables
		        for one_variable in variables:
		            print("\\t" + one_variable)  # Name of variable
		
		
		if __name__ == "__main__":
		    main()


	"""

def ApplyCurveFunction(function: str, curves: object, parameters: object, replace_on: bool) -> object:

	"""

	List of functions and arguments:
	
	function         curves         parameters      replace_on
	octave          ,curve          , NULL          , boolean
	loctave         ,curve          , NULL          , boolean
	thirdoctave     ,curve          , NULL          , boolean
	thirdloctave    ,curve          , NULL          , boolean
	integr          ,curve          , NULL          , boolean
	autocorrel      ,curve          , NULL          , boolean
	srms            ,curve          , NULL          , boolean
	srss            ,curve          , NULL          , boolean
	flip            ,curve          , NULL          , boolean
	simplify        ,curve          , NULL          , boolean
	fix             ,curve          , NULL          , boolean
	inv             ,curve          , NULL          , boolean
	saecfc060       ,curve          , NULL          , boolean
	saecfc180       ,curve          , NULL          , boolean
	saecfc600       ,curve          , NULL          , boolean
	saecfc1000      ,curve          , NULL          , boolean
	cfc060          ,curve          , NULL          , boolean
	cfc180          ,curve          , NULL          , boolean
	cfc600          ,curve          , NULL          , boolean
	cfc1000         ,curve          , NULL          , boolean
	resample        ,curve          , {"type":"points"                  , "points":integer}          , boolean
	resample        ,curve          , {"type":"timestep"                , "timestep":float}          , boolean
	shift           ,curve          , {"direction":"left/right/up/down" , "shiftvalue":float}        , boolean
	newshift        ,curve          , {"direction":"left/right/up/down" , "shiftvalue":float}       , boolean
	scale           ,curve          , {"direction":"x/y/z/all"          , "scalevalue":float}       , boolean
	newscale        ,curve          , {"direction":"x/y/z/all"          , "scalevalue":float}       , boolean
	customoctave    ,curve          , {"bands":"name"                   , "nfactor":int}            , boolean
	movaver         ,curve          , {"terms":int}                                                 , boolean
	expmovaver      ,curve          , {"terms":int}                                                 , boolean
	wmovaver        ,curve          , {"terms":int}                                                 , boolean
	movingaver      ,curve          , {"terms":int, "centered":bool, "keeppoints":bool})            , boolean
	expmovingaver   ,curve          , {"terms":int, "centered":bool, "keeppoints":bool})            , boolean
	wmovingaver     ,curve          , {"terms":int, "centered":bool, "keeppoints":bool})            , boolean       
	frftrans        ,curve          , {"type":"disp2vel/disp2acc/vel2disp/vel2acc/acc2disp/acc2vel"}, boolean
	modtrim         ,curve          , {"start":float,"end":float}                                   , boolean
	trim            ,curve          , {"type":"start/end/both" , "threshold shift":float , "threshold":bool}, boolean
	differ          ,curve          , {"type":"centered/backward/forward/ecer94"}                   , boolean
	mpvalue         ,curve          , {"type":"multof/sumof/divof/diffof" , "magn":float , "phase":float}, boolean
	rivalue         ,curve          , {"type":"multof/sumof/divof/diffof" , "real":float , "imag":float}, boolean
	envcurve        ,curve          , {"type":"min/max" }                                           , boolean
	hic             ,curve          , {"interval":float }                                           , boolean
	fir100          ,curve          , {"removebias":bool }                                          , boolean
	iirfilt         ,curve          , {"cutoff":float,"attenuation":float,"stopbandfreq": float}    , boolean
	bwfilt          ,curve          , {"frequency":float}                                           , boolean
	normbwfilt      ,curve          , {"order":int , "frequency":float}                             , boolean      
	fft             ,curve          , {"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,
	                                        "window":"none/triang/hanning/welch/hamming/blackman/parzen"}, boolean  
	ifft            ,curve          , {"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,
	                                        "window":"none/triang/hanning/welch/hamming/blackman/parzen"}, boolean
	dft             ,curve          , {"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,
	                                        "window":"none/triang/hanning/welch/hamming/blackman/parzen"}, boolean
	idft            ,curve          , {"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,
	                                        "window":"none/triang/hanning/welch/hamming/blackman/parzen"}, boolean
	winft           ,curve          , {"window":"none/triang/hanning/welch/hamming/blackman/parzen"}, boolean
	levelcross      ,curve          , {"threshold":float}                                           , boolean
	timeabovelevel  ,curve          , {"limit":float}                                               , boolean
	percentile      ,curve          , {"percentage":float , "method":"method1/method2"}             , boolean
	convex          ,curve          , {"type":"upward/downward"}                                    , boolean
	histogram       ,curve          , {"type":"binwidth","binwidth":float,"method":"startend","start":float,"end":float}, boolean
	histogram       ,curve          , {"type":"binwidth" , "binwidth":float , "method":"center" , "bincenter":float}, boolean
	histogram       ,curve          , {"type":"numberofbins" , "numberofbins":int , "method":"startend" , "start":float,
	                                        "end":float}, boolean
	trendline       ,curve          , {"type":"linear" }, boolean
	trendline       ,curve          , {"type":"polynomial" , "order":int}, boolean
	idealbandpass   ,curve          , {"low":float , "high":float}, boolean
	windows         ,curve          , {"window":"triang/hanning/welch/hamming/blackman/parzen" , "terms":int , "centered":bool , "keeppoints":bool}, boolean
	saefilter1981   ,curve          , {"type":"1000channelclass/180channelclass/60channelclass/600channelclass"}, boolean
	estiff          ,curve          , {"k":float ,"freq_min":float,"freq_max":float,"ref":float}, boolean
	dbfilter        ,curve          , {"dbtype":"dba/dbb/dbc/dbd/dbn/revdba/revdbb/revdbc/revdbd/revdbn","dbvalue":float}, boolean
	dbfilter        ,curve          , {"dbtype":"dba/dbb/dbc/dbd/dbn/revdba/revdbb/revdbc/revdbd/revdbn","dbvalue":float, "factor":float}, boolean
	multof          ,list_of_curves , 0
	sumof           ,list_of_curves , 0
	rms             ,list_of_curves , 0
	rss             ,list_of_curves , 0
	minof           ,list_of_curves , 0
	maxof           ,list_of_curves , 0
	averof          ,list_of_curves , 0
	divof           ,list_of_curves , 0
	diffof          ,list_of_curves , 0
	area            ,list_of_curves , { "area_id" : int , "name" : string , "color" : string }

	Parameters
	----------
	function : str
		octave, thirdoctave, thirdloctave, loctave, movaver, expmovaver etc.

	curves : object
		curve object or list of curve objects, depending on the function (see above).

	parameters : object
		parameters of each function

	replace_on : bool
		use this to replace existing curve or produce a new one

	Returns
	-------
	object
		It returns a list with objects of class Curve.
		Upon failure, it returns an empty list.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    curve_id = 2
		    curves = plot2d.CurveById(window_name, curve_id)
		    # 1. function cfc1000 needs a curve and no parameters
		    function = "cfc1000"
		    parameters = 0
		    val = plot2d.ApplyCurveFunction(function, curves, parameters)
		
		    # 2. function resample needs a curve and parameters
		    function = "resample"
		    parameters = {"type": "points", "points": 10}
		    val = plot2d.ApplyCurveFunction(function, curves, parameters, replace_on=True)
		
		    # 3. function sumof needs a list of curves and no parameters
		    curves = plot2d.CurvesOfWindow(window_name)
		    function = "sumof"
		    parameters = 0
		    val = plot2d.ApplyCurveFunction(function, curves, parameters)
		
		    # 4. function cfc060 needs a curve and no parameters use replace_on to substitude curve
		    function = "cfc060"
		    parameters = 0
		    val = plot2d.ApplyCurveFunction(function, curves, parameters)
		
		    # 5. function area needs a list with 2 curves and all parameters are optional.
		    function = "area"
		    params = {"area_id": 4, "name": "myarea", "color": "Green"}
		    val = plot2d.ApplyCurveFunction(function, curves, parameters)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurveFunctionMulti(function: str, curve_ids: str, window: str) -> object:

	"""

	Add or multiply two or more curves, divide or subtract two curves

	Parameters
	----------
	function : str
		"multof", "sumof", "diffof", "divof"

	curve_ids : str
		in case of sumof, multof can be a range of curve ids eg. 1-4,7,8
		in case of diffof, divof can be a pair of curve ids seperated by commas eg. 1,4

	window : str
		Window the curves belong to.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly created curves of the given 2d plot window.
		Upon failure, an empty list is returned.

	"""

def CurveFunctionUserDefined(type: str, name_type: str, x_formula: str, y_formula: str, complex_formula: str, window: str) -> object:

	"""

	create a plain or complex curve using this function

	Parameters
	----------
	type : str
		"plain", "magphase", "realimag"

	name_type : str
		this formula will give the new curve name eg "new curve c1.name"

	x_formula : str
		the formula for the abscissa of the new curve eg. "c1.x+c2.x"

	y_formula : str
		the formula for the y values of the new curve eg. "sqrt(c2.y+c3.y)"

	complex_formula : str
		the formula that defines the phase or the imaginary part of a complex curve. 
		eg. "c1.yp" or "c1.yr"

	window : str
		Window the curves belong to.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Curve referring to one newly created curves of the given 2d plot window.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    type = "plain"
		    name_type = "C1 c1.name"
		    x_formula = "c1.x"
		    y_formula = "c1.y+c3.y"
		    complex_formula = ""
		    window = "Window1"
		    ret = plot2d.CurveFunctionUserDefined(
		        type, name_type, x_formula, y_formula, complex_formula, window
		    )
		    print(ret)
		
		    type = "magphase"
		    name_type = "C2 c2.name"
		    x_formula = "c1.x"
		    y_formula = "c1.y+c3.y"
		    complex_formula = "c1.yp+c3.yp"
		    ret = plot2d.CurveFunctionUserDefined(
		        type, name_type, x_formula, y_formula, complex_formula, window
		    )
		    print(ret)
		
		    type = "realimag"
		    name_type = "C3 c3.name"
		    x_formula = "c1.x"
		    y_formula = "c1.yr+c3.yr"
		    complex_formula = "c1.yi+c3.yi"
		    ret = plot2d.CurveFunctionUserDefined(
		        type, name_type, x_formula, y_formula, complex_formula, window
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def AttributeOfPlot(window_name: str, plot_id: int, attrib_name: str) -> str:

	"""

	This function returns the value of a specific attribute referring to a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the Plot.

	attrib_name : str
		Name of the attribute.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 1
		    attrib_name = "test"
		    attrib_value = plot2d.AttributeOfPlot(window_name, plot_id, attrib_name)
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeOfPlot(window_name: str, plot_id: int, attrib_name: str, attrib_value) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.set_attribute` instead.


	This function sets the value of a specific attribute referring to a given plot. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	attrib_name : str
		Name of the attribute.

	attrib_value : 
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 1
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		
		    ret = plot2d.SetAttributeOfPlot(window_name, plot_id, attrib_name, attrib_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.set_attribute instead.", DeprecationWarning)

def SetSubAttributeOfPlot(window_name: str, plot_id: int, group_name: str, attrib_name: str, attrib_value: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.plot2d.Plot.set_attribute` instead.


	This function sets the value of a specific plot attribute of a group to a given value.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	group_name : str
		Name of the attribute group.

	attrib_name : str
		Name of the attribute. If the given attribute and group do not exist they are automatically created.

	attrib_value : str
		Value of the attribute.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 1
		    group_name = "test_group"
		    attrib_name = "test_attribute"
		    attrib_value = "test_attribute_value"
		    ret = plot2d.SetSubAttributeOfPlot(
		        window_name, plot_id, group_name, attrib_name, attrib_value
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.plot2d.Plot.set_attribute instead.", DeprecationWarning)

def SubAttributeOfPlot(window_name: str, plot_id: int, group_name: str, attrib_name: str) -> str:

	"""

	This function returns the value of a specific attribute of a group referring to a given plot.

	Parameters
	----------
	window_name : str
		Name of the window.

	plot_id : int
		Id of the plot.

	group_name : str
		Name of the attribute group.

	attrib_name : str
		Name of the attribute.

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
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 1
		    attrib_name = "test_attribute"
		    group_name = "test_group"
		    attrib_value = plot2d.SubAttributeOfPlot(
		        window_name, plot_id, group_name, attrib_name
		    )
		    print(attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CurvesTypesMetadb(filename: str):

	"""

	This function finds curves types of a Metadb file.

	Parameters
	----------
	filename : str
		Name of the file.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    filename = "curves.metadb"
		    curves_types = plot2d.CurvesTypesMetadb(filename)
		    for iii in curves_types:
		        features = iii[0]
		        print(features)
		        args = [features]
		        plot2d.LoadCurvesMetadb("Window1", 0, filename, args)
		        print("****")
		
		
		if __name__ == "__main__":
		    main()


	"""

class Plot():

	"""

	Class for plots.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    pl = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: activate
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    ret = plot.activate()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: deactivate
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    ret = plot.deactivate()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curve_groups
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    group_list = plot.get_curve_groups()
		    # group_name = 'Group1'
		    # group_list = plot.get_curve_groups(group_name)
		    for cg in group_list:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "all"
		    # specifier = 'visible'
		    # specifier = 'selected'
		    curvelist = plot.get_curves(specifier)
		    # specifier = 'byname'
		    # curvelist = plot.get_curves(specifier, name = 'my_curve')
		    # specifier = 'byid'
		    # curvelist = plot.get_curves(specifier, curve_id = 1)
		    for c in curvelist:
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
		# method: get_footer
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    footer = plot.get_footer()
		    if footer:
		        print(footer.id, footer.window_name, footer.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_fringe
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    fringe = plot.get_fringe()
		    if fringe:
		        print(fringe.id, fringe.window_name, fringe.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_grid
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    grid = plot.get_grid()
		    if grid:
		        print(grid.id, grid.window_name, grid.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_legend
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    legend = plot.get_legend()
		    if legend:
		        print(legend.id, legend.window_name, legend.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    page = plot.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot_axes
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "all"
		    # specifier = 'visible'
		    # specifier = 'active'
		    axis_list = plot.get_plot_axes(specifier)
		    # specifier = 'byid'
		    # axis_list = plot.get_plot_axes(specifier, id = 0)
		    # specifier = 'bytype'
		    # axis_list = plot.get_plot_axes(specifier, type = 'xaxis')
		    # specifier = 'byidtype'
		    # axis_list = plot.get_plot_axes(specifier, type = 'xaxis', id = 0)
		    # specifier = 'visible_bytype'
		    # axis_list = plot.get_plot_axes(specifier, type = 'xaxis')
		    # specifier = 'active_bytype'
		    # axis_list = plot.get_plot_axes(specifier, type = 'xaxis')
		    for plax in axis_list:
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
		# method: get_polar_radius
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    plax = plot.get_polar_radius()
		    if plax:
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
		# method: get_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    title = plot.get_title()
		    if title:
		        print(title.get_text())
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    w = plot.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "attribute"
		    value = "15"
		    attr_name = "PlotId"
		    plot.set_attribute(specifier, value, attr_name)
		    # specifier = 'subattribute'
		    # specifier = 'groupattribute'
		    # plot.set_attribute( specifier ,value, attr_name, group_name = 'mygroup')
		    specifier = "all"
		    attr_list = plot.get_attributes(specifier)
		    print(attr_list)
		    specifier = "attribute"
		    specifier = "subattribute"
		    # attr_value = plot.get_attributes(specifier, attr_name = 'PlotId')
		    # print(attr_value)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "attribute"
		    value = "15"
		    attr_name = "PlotId"
		    plot.set_attribute(specifier, value, attr_name)
		    # specifier = 'groupattribute'
		    # plot.set_attribute(specifier, value , attr_name)
		    # specifier = 'subattribute'
		    # plot.set_attribute( specifier, value, attr_name, group_name = 'mygroup')
		    specifier = "all"
		    attr_list = plot.get_attributes(specifier)
		    print(attr_list)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_border
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    ret = plot.set_border(3)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_border_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    col = windows.Color(name="255_0_0_0", r=255, g=0, b=0, a=0)
		    ret = plot.set_border_color(col)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_complexheight
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    height = 50
		    ret = plot.set_complexheight(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_dnaline
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    onoff = True
		    ret = plot.set_dnaline(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_lockheader
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    onoff = True
		    ret = plot.set_lockheader(onoff)
		    print(re)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_locktitles
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    onoff = True
		    ret = plot.set_locktitles(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_margin
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "up"
		    # specifier = 'down'
		    # specifier = 'left'
		    # specifier = 'right'
		    margin = 100
		    ret = plot.set_margin(specifier, margin)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_palette
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    palette_name = "DemoBar"
		    ret = plot.set_palette(palette_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_plottype
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    plottype = "plain"
		    ret = plot.set_plottype(plottype)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_polar_auto
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    onoff = True
		    ret = plot.set_polar_auto(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_polarsize
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    size = 100
		    ret = plot.set_polarsize(size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_polar_specfrequency
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "on"
		    # specifier = 'off'
		    frequency = 30
		    ret = plot.set_polar_specfrequency(specifier, frequency)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    plot_settings = {"border_width": 3, "legend": 1, "border_color": "blue"}
		    ret = plot.set_settings(plot_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_sync_select
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    sync = "off"
		    ret = plot.set_sync_select(sync)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_view
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "viewiso"
		    # specifier = 'viewcenter'
		    # specifier = 'view1'
		    # specifier = 'view2'
		    # specifier = 'view3'
		    # specifier = 'view4'
		    # specifier = 'view5'
		    # specifier = 'view6'
		    ret = plot.set_view(specifier)
		    # specifier = 'viewscale'
		    # scale_factor = 2
		    # ret = plot.set_view(specifier, scale_factor)
		    # specifier = 'viewzoom'
		    # zoom_factor = 2
		    # ret = plot.set_view(specifier , zoom_factor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    pl = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    can_use = pl.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_bg_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window_1", page_id=0)
		    color = windows.Color(name="red", r=0, g=0, b=0, a=0)
		    ret = plot.set_bg_color(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_bg_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window_1", page_id=0)
		    color = plot.get_bg_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	active: int = None
	"""
	- 1 if plot is active
	- 0 if plot is not active

	"""

	type: str = None
	"""
	Type of the plot ('plain', 'realimag', 'magphase', 'polar').

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	def get_curve_groups(self, group_name: str) -> object:

		"""

		This function collects curve groups of a given plot.


		Parameters
		----------
		group_name : str, optional
			Returns all groups matching this name or all groups if left empty.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class CurveGroup referring to one specific curve group of the given plot.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_plot_axes(cls, specifier: str, type: str, id: int) -> object:

		"""

		This function returns a list containing plot axis objects of the plot.


		Parameters
		----------
		specifier : str, optional
			-'all' for all axes (default value)
			-'visible' for all visible axes
			-'active' for active axes
			-'byid' get all axes with specific id. Must be combined with argument: id.
			-'bytype' get all axes of specific type. Must be combined with argument: type.
			-'byidtype' get axis of specific type and id. Must be combined with arguments: id, type.
			-'visible_bytype' get axes by type and visibility. Must be combined with argument: type.
			-'active_bytype' get axes by type and activation. Must be combined with argument: type.

		type : str, optional
			-'xaxis'
			-'yaxis'
			-'zaxis'
			-'caxis'
			Required when specifier is 'bytype', 'byidtype', 'visible_bytype', 'active_bytype'.

		id : int, optional
			Id of axis. Required when specifier is 'byid', 'byidtype'.

		Returns
		-------
		object
			It returns a list containing PlotAxis objects of the plot.Else, empty list is returned.

		"""


	@classmethod
	def get_polar_radius(cls) -> object:

		"""

		This function returns the Radius axis of a polar plot.


		Returns
		-------
		object
			It returns a PlotAxis object of the polar plot.Else, None is returned.

		"""


	@classmethod
	def get_curves(cls, specifier: str, name: str, curve_id: int) -> object:

		"""

		This function collects curves of a given plot.


		Parameters
		----------
		specifier : str, optional
			-'all' to get all curves (default value)
			-'visible' to get all visible curves
			-'selected' to get all selected curves
			-'byname' to get all curves that match the name given by the user. Must be combined with argument: name.
			-'byid' to get a list containing the curve with the specific id. Must be combined with argument: curve_id.

		name : str, optional
			Will search for all curves containing 'name'. Required when specifier is 'byname'.

		curve_id : int, optional
			Ask for a specific curve id. Required when specifier is 'byid'.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given plot.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_legend(cls) -> object:

		"""

		This method returns the Legend object of the plot.


		Returns
		-------
		object
			Returns the Legend object of the plot.

		"""


	@classmethod
	def get_grid(cls) -> object:

		"""

		This method returns the Grid object of the plot.


		Returns
		-------
		object
			Returns the Grid object of the plot.

		"""


	@classmethod
	def get_fringe(cls) -> object:

		"""

		This method returns the Fringe object of the plot.


		Returns
		-------
		object
			Returns the Fringe object of the plot.

		"""


	@classmethod
	def get_title(cls) -> object:

		"""

		This method returns the Title object of the plot.


		Returns
		-------
		object
			Returns the Title object of the plot.

		"""


	@classmethod
	def get_footer(cls):

		"""

		This method returns the Footer object of the plot.


		"""


	@classmethod
	def set_settings(cls, plot_settings: object) -> object:

		"""

		This function controls settings of a given plot.


		Parameters
		----------
		plot_settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'border_width' : 3 , 'legend' : 1, 'border_color' : 'blue'}). The names of the plot settings and its possible values are:
			- 'border_width': Border line width (integer value)
			- 'border_color': Border color (string value)
			- 'complex_height': Complex plot height (integer value)
			- 'curves_palette': Color palette for selected curves (string value)
			- 'dna_palette': Palette for dna plot (string value)
			- 'mac_palette': Palette for mac plot (string value)
			- 'legend': Legend (0,1)
			- 'locktitles': Lock titles from read file (0,1)
			- 'margin_up': Plot up margin (float value)
			- 'margin_down': Plot down margin (float value)
			- 'margin_left': Plot left margin (float value)
			- 'margin_right': Plot right margin (float value)
			- 'plot_palette_counter': Plot palette counter
			- 'plot_type': Plot type ('plain', 'magphase', 'realimag', 'polar', 'horiz', 'dna', 'mac', 'horizontal', 'colormap', '3dmac', 'waterfall', 'nyquist')
			- 'point_show': Show model point (0,1)
			- 'polar_size': Polar size (0,1)
			- 'show_current': Show only current line (0,1)
			- 'sync_value': Show model value and sync line (0,1)
			- 'model_value': Show model value (0,1)

		Returns
		-------
		object
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def activate(cls) -> bool:

		"""

		This method activates the given plot.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def deactivate(cls) -> bool:

		"""

		This method deactivates the given plot.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_view(cls, specifier: str, zoom_factor, scale_factor: float) -> bool:

		"""

		This method applies different types of views to a 3d plot.


		Parameters
		----------
		specifier : str
			-'viewiso' Isometric view
			-'viewcenter' Center view
			-'view1' 1st default view
			-'view2' 2nd default view
			-'view3' 3rd default view
			-'view4' 4th default view 
			-'view5' 5th default view
			-'view6' 6th default view
			-'viewscale' Scale view
			-'viewzoom' Zoom in or out

		zoom_factor : 
			Positive zoom factor to zoom in, negative to zoom out.

		scale_factor : float
			Scale view

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_plottype(cls, plottype: str) -> bool:

		"""

		This method changes the plottype of the given plot.


		Parameters
		----------
		plottype : str
			-'plain'
			-'realimag'
			-'magphase'
			-'polar'
			-'dna'
			-'colormap'
			-'mac'
			-'horiz'
			-'3dmac'
			-'waterfall'
			-'nyquist'
			-'sanddune'

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_complexheight(cls, height: float) -> bool:

		"""

		This method sets the height of the complex part of the plot.


		Parameters
		----------
		height : float
			Height of the complex part of plot.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_dnaline(cls, onoff: bool) -> bool:

		"""

		This method enables or disables the dna lines of a Dna Plot.


		Parameters
		----------
		onoff : bool
			Boolean to set dna lines on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_locktitles(cls, onoff: bool) -> bool:

		"""

		This method locks the Titles of the plot. 


		Parameters
		----------
		onoff : bool
			Boolean to set locktitles on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_lockheader(cls, onoff: bool) -> bool:

		"""

		This method can Lock or unlock the header of a given plot.


		Parameters
		----------
		onoff : bool
			Boolean to set lockheader on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_attributes(cls, specifier: str, attr_name: str, group_name: str) -> object:

		"""

		This method returns a dictionary containing all attributes, or a specific attribute or subattribute value of a given plot.


		Parameters
		----------
		specifier : str
			-'all'
			-'attribute'
			-'subattribute'

		attr_name : str, optional
			Attribute or Subattribute name

		group_name : str, optional
			The name of the Group, in case of subattribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	@classmethod
	def set_attribute(cls, specifier: str, value: str, attr_name: str, group_name: str) -> bool:

		"""

		This method can be used to set an attribute or subattribute to a given plot.


		Parameters
		----------
		specifier : str
			-'attribute' in case we want to add attribute
			-'subattribute' in case we want to add subattribute
			-'groupattribute' in case we want to add group of attributes

		value : str
			Value of attribute.

		attr_name : str
			Attribute name to set.

		group_name : str, optional
			Group name in case of subattribute.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_sync_select(cls, sync: str) -> bool:

		"""

		This method is used to set the synchronisation between 3d model and the plot.


		Parameters
		----------
		sync : str
			-'value' show value.
			-'point' show point only.
			-'syncvalue' show value and time.
			-'showcurrent' show current line curve.
			-'off' do not show any synchronising.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_palette(cls, palette_name: str) -> bool:

		"""

		This method can be used to set the palette for the plot.


		Parameters
		----------
		palette_name : str
			Palette name to be applied.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_border(cls, border: int) -> bool:

		"""

		This method sets the width of the line of the border of the given plot.


		Parameters
		----------
		border : int
			Border is the width of the border line. 0 for no border

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_border_color(cls, color: object) -> bool:

		"""

		This method applies the selected Color object on the border of plot.


		Parameters
		----------
		color : object
			Color object to be applied on the given plot border.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_margin(cls, specifier: str, margin: float) -> bool:

		"""

		This method sets the margin of the plot.


		Parameters
		----------
		specifier : str
			-'up'
			-'down'
			-'left'
			-'right'

		margin : float
			Value of the margin.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_polarsize(cls, size: float) -> bool:

		"""

		This method can be used to set the polarsize. (only when given plot is polar)


		Parameters
		----------
		size : float
			Size of polar plot.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_polar_specfrequency(cls, specifier: str, frequency: float) -> bool:

		"""

		This method can be used to set specific frequency on, off or apply specific frequency on a given polar plot.


		Parameters
		----------
		specifier : str
			-'on' Set Specific frequency on
			-'off' Set Specific frequency off
			-'frequency' Apply Specific frequency.

		frequency : float
			Specific frequency to be applied.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_polar_auto(cls, onoff: bool) -> bool:

		"""

		This method can be used to set the polar radius axis auto on.


		Parameters
		----------
		onoff : bool
			Boolean to set the polar radius axis auto on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Plot.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Plot. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Plot. 


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Plot. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Plot entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""


	@classmethod
	def set_bg_color(cls, color: object) -> bool:

		"""

		This method applies the selected Color object on the background color of the plot.


		Parameters
		----------
		color : object
			Color object to be applied on the given plot border.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_bg_color(cls) -> object:

		"""

		This method returns the color of the plot background.


		Returns
		-------
		object
			Returns a color object which is the background color of the plot.

		"""

class Curve():

	"""

	Class for curves.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    c = plot2d.Curve(id=1, window_name="Window1", page_id=0)
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
		
		
		# method: apply_function
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot = plot2d.PlotById(window_name, plot_id)
		    specifier = "selected"
		    ret = plot.get_curves(specifier)
		    param1 = {"direction": "up", "shiftvalue": 100}
		    for curve in ret:
		        function = "integr"
		        curve.apply_function(function, parameters=0)
		        function = "shift"
		        curve.apply_function(function, parameters=param1)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: delete
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: deselect
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.deselect()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_area
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    c1 = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    c2 = plot2d.Curve(id=2, window_name="Window1", page_id=0)
		    curve2 = c2
		    ret = c1.get_area(curve2)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    color = curve.get_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_filtered_points
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    type = "magnitude"
		    # type = "phase"
		    # type = "real"
		    # type = "imaginary"
		    min_x = 0
		    max_x = 1
		    min_y = 0
		    max_y = 1
		    pointlist = curve.get_filtered_points(type, min_x, max_x, min_y, max_y)
		    for pnt in pointlist:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_limit_value_x
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "min"
		    # specifier = 'max'
		    ret = curve.get_limit_value_x(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_limit_value_y
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "max"
		    ret = curve.get_limit_value_y(specifier)
		    print(ret)
		    ret = curve.get_limit_value_y(specifier, type="real")
		    print(ret)
		    ret = curve.get_limit_value_y(
		        specifier, type="imaginary", range_min=0, range_max=100
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_line_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    lstyle = curve.get_line_style()
		    print(lstyle)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_line_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    lwidth = curve.get_line_width()
		    print(lwidth)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_mark_density
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_mark_density()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    page = curve.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    pl = curve.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_point_mark
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    pl = curve.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_point_precision
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_point_precision()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_point_precision_digits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_point_precision_digits()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_points
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    # specifier = 'all'
		    # specifier = 'selected'
		    # specifier = 'minx'
		    # specifier = 'miny'
		    # specifier = 'maxx'
		    # specifier = 'maxy'
		    type = "real"
		    # type = 'imag'
		    # type = 'magn'
		    # type = 'phase'
		    pointlist = curve.get_points(specifier, type, point_id=20)
		    for pnt in pointlist:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_points
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    # specifier = 'all'
		    # specifier = 'selected'
		    # specifier = 'minx'
		    # specifier = 'miny'
		    # specifier = 'maxx'
		    # specifier = 'maxy'
		    type = "real"
		    # type = 'imag'
		    # type = 'magn'
		    # type = 'phase'
		    pointlist = curve.get_points(specifier, type, point_id=20)
		    for pnt in pointlist:
		        print(pnt.id, pnt.x, pnt.y, pnt.selected, pnt.curve_id, pnt.curve_id)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_points_db_values
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "db"
		    specifier = "dba"
		    specifier = "dbb"
		    specifier = "dbc"
		    specifier = "dbd"
		    ret = curve.get_points_db_values(specifier)
		    # ret = curve.get_points_db_values(specifier,decibel_value = 2)
		    # ret = curve.get_points_db_values(specifier,decibel_value = 2 , db_factor = 10)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_point_size
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_point_size()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_point_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_point_style()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_points_x_values
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_points_x_values()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_points_y_values
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    type = "imaginary"
		    ret = curve.get_points_y_values(type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_selected_point_size
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_selected_point_size()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_selected_point_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.get_selected_point_style()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    w = curve.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_x_values_from_y
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "all"
		    # specifier = 'first'
		    yvalue = 1
		    ret = curve.get_x_values_from_y(specifier, yvalue)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_x_values_from_y_complex
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "all"
		    # specifier = 'first'
		    complex_value = 1
		    ret = curve.get_x_values_from_y_complex(specifier, complex_value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_y_values_from_x
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "all"
		    xvalue = 1
		    ret = curve.get_y_values_from_x(specifier, xvalue)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: hide
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name=" Window1", page_id=0)
		    ret = curve.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: is_complex
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name=" Window1", page_id=0)
		    ret = curve.is_complex()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: select
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name=" Window1", page_id=0)
		    ret = curve.select()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_attributes
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name=" Window1", page_id=0)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr_value = "my_curves.csv"
		    ret = curve.set_attribute(specifier, attr_name, attr_value)
		    print(ret)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr = curve.get_attributes(specifier, attr_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name=" Window1", page_id=0)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr_value = "my_curves.csv"
		    ret = curve.set_attribute(specifier, attr_name, attr_value)
		    print(ret)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr = curve.get_attributes(specifier, attr_name)
		    print(attr)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: set_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    mycolor = windows.Color(name="my_color", r=0, g=255, b=255, a=255)
		    ret = curve.set_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    line_style = 4
		    ret = curve.set_line_style(line_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_line_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    line_width = 4
		    ret = curve.set_line_width(line_width)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_mark_density
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    mark_density = 10
		    ret = curve.set_mark_density(mark_density)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_name
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    name = "my new curve name"
		    ret = curve.set_name(name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_point_mark
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    point_mark = "Tra X"
		    ret = curve.set_point_mark(point_mark)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_point_precision
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    point_precision = "fixed"
		    ret = curve.set_point_precision(point_precision)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_point_precision_digits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    precision_digits = 4
		    ret = curve.set_point_precision_digits(precision_digits)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_point_size
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    point_size = 3
		    ret = curve.set_point_size(point_size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_point_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    point_style = 3
		    ret = curve.set_point_style(point_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_selected_point_size
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    spoint_size = 3
		    ret = curve.set_selected_point_size(spoint_size)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_selected_point_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    spoint_style = 3
		    ret = curve.set_selected_point_style(spoint_style)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: set_settings
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    specifier = "all"
		    # specifier = 'visible'
		    # specifier = 'selected'
		    curvelist = plot.get_curves(specifier)
		    # specifier = 'byname'
		    # curvelist = plot.get_curves(specifier, name = 'my curve')
		    specifier = "byid"
		    curvelist = plot.get_curves(specifier, curve_id=1)
		    curve_settings = {"curve_color": "blue", "style": 3, "name": "my new curve"}
		    for curve in curvelist:
		        curve.set_settings(curve_settings)
		
		
		if __name__ == "__main__":
		    main()
		
		# method: show
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    ret = curve.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		
		
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    c = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    can_use = c.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Curve Id.

	"""

	plot_id: int = None
	"""
	Plot id of the curve.

	"""

	window_name: str = None
	"""
	Name of the 2d plot window of the curve.

	"""

	name: str = None
	"""
	Name of the curve.

	"""

	visible: int = None
	"""
	- 1 if curve is visible
	- 0 if it is not visible

	"""

	selected: int = None
	"""
	-1 if curve is selected
	- 0 if it is not selected

	"""

	page_id: int = None
	"""
	Id of the page of the curve.

	"""

	command: str = None
	"""
	mETA command from which curve has been created.

	"""

	entity_id: int = None
	"""
	Id of the corresponding entity of the curve.

	"""

	@classmethod
	def get_points(cls, specifier: str, type: str, point_id: int) -> object:

		"""

		This method collects requested points of a given curve.


		Parameters
		----------
		specifier : str
			-'byid' get a list with a single point of the requested id
			-'all' get a list with all the points of curve
			-'selected' get a list with all selected points of curve
			-'minx' get a list of points with minimum x value
			-'miny' get a list of points with minimum y value
			-'maxx' get a list of points with maximum x value
			-'maxy' get a list of points with maximum y value

		type : str
			Type of value returned. Can be:
			-'real'
			-'imag'
			-'magn'
			-'phase'

		point_id : int, optional
			Point id.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Point referring to one specific point of the given curve.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_filtered_points(cls, type: str, min_x: float, max_x: float, min_y: float, max_y: float) -> object:

		"""

		This method collects all points of a given curve with their X and Y coordinates being among the range of values specified by the given arguments.


		Parameters
		----------
		type : str
			Select the type of y values range: 
			-'magnitude'
			-'phase' 
			-'real'
			-'imaginary'

		min_x : float
			Set minimum x value.

		max_x : float
			Set maximum x value.

		min_y : float
			Set minimum y value.

		max_y : float
			Set maximum y value.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Point referring to one specific point of the given curve.Upon failure, an empty list is returned.

		"""


	@classmethod
	def is_complex(cls) -> bool:

		"""

		This method checks whether a curve is complex.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_color(cls) -> object:

		"""

		This method gets the color of a given curve.


		Returns
		-------
		object
			Upon success, it returns a Color object reffering to the color of the corresponding curve.Else, None is returned.

		"""


	@classmethod
	def get_line_style(cls) -> int:

		"""

		This method finds the line style of a given curve.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the line style of the corresponding curve. Line style is an integer number in the range of 0 and 13, which is the same being used in META commands for changing line style of curve.Else, it returns -1.

		"""


	@classmethod
	def get_line_width(cls) -> int:

		"""

		This method finds the line width of a given curve.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the line width of the corresponding curve. Line width is an integer number in the range of 0 and 10.Else, it returns -1.

		"""


	@classmethod
	def get_point_style(cls) -> object:

		"""

		This method gets the point style of a given curve.


		Returns
		-------
		object
			Upon success, it returns an integer referring to the point style of the corresponding curve. Point style is an integer number in the range of 0 and 8, which is the same being used in META commands for changing point style of curve.Else, it returns -1.

		"""


	@classmethod
	def get_point_size(cls):

		"""

		This method finds the point size of a given curve.


		"""


	@classmethod
	def get_mark_density(cls) -> int:

		"""

		This method finds the mark density of a given curve. Mark density is an integer number in the range of 1 and 99.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the mark density of the corresponding curve.Else, it returns -1.

		"""


	@classmethod
	def get_point_mark(cls) -> str:

		"""

		This method finds the point mark of a given curve. Point mark is a string expression with no more than 5 characters.


		Returns
		-------
		str
			Upon success, it returns a string referring to the point mark of the corresponding curve.Else, it returns an empty string.

		"""


	@classmethod
	def get_selected_point_style(cls) -> int:

		"""

		This method finds the selected point style of a given curve.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the selected point style of the corresponding curve. Point style is an integer number in the range of 0 and 8, which is the same being used in META commands for changing selected point style of curve.Else, it returns -1.

		"""


	@classmethod
	def get_selected_point_size(cls) -> int:

		"""

		This method finds the point size of a given curve.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the point size of the corresponding curve. Point size is an integer number in the range of 1 and 20, which is the same being used in META commands for changing point size of curve.Else, it returns -1.

		"""


	@classmethod
	def get_point_precision(cls) -> str:

		"""

		This method finds the point precision of a given curve.


		Returns
		-------
		str
			Upon success, it returns a string referring to the point precision of the corresponding curve. Its possible values are:- 'auto' : Auto- 'sciauto' : Auto-Scientific- 'scientific' : Scientific- 'fixed' : Fixed. Else, it returns an empty string.

		"""


	@classmethod
	def get_point_precision_digits(cls) -> int:

		"""

		This method finds the point precision digits of a given curve. Point precision digits is an integer number in the range of 0 and 20.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the point precision digits of the corresponding curve.Else, it returns -1.

		"""


	@classmethod
	def get_limit_value_x(cls, specifier: str) -> float:

		"""

		This method calculates the minimum or maximum value of the X coordinates of a given curve of a specified window.


		Parameters
		----------
		specifier : str
			-'min' for minimum x value
			-'max' for maximum x value

		Returns
		-------
		float
			It returns a float number referring to the corresponding minimum or maximum value of the X coordinates of the given curve.Upon failure, no value is returned.

		"""


	@classmethod
	def get_limit_value_y(cls, specifier: str, type: str, range_min: float, range_max: float) -> float:

		"""

		This method calculates the minimum or maximum values of magnitude, phase,real or imaginary of curve


		Parameters
		----------
		specifier : str
			'min' for minimum
			'max' for maximum

		type : str, optional
			-'magnitude'
			-'phase'
			-'real'
			-'imaginary'

		range_min : float, optional
			use minimum abscissa range value

		range_max : float, optional
			use maximum abscissa range value

		Returns
		-------
		float
			It returns a float number referring to the corresponding minimum or maximum value of the magnitude, phase, real or imaginary coordinates of the given curve.Upon failure, a zero value is returned.

		"""


	@classmethod
	def get_points_x_values(cls) -> object:

		"""

		This method collects X values of all points of a given curve.


		Returns
		-------
		object
			It returns a list where each member of the list is a float number referring to the X value of one specific point of the given curve.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_points_y_values(cls, type: str) -> object:

		"""

		This method collects a list of all magnitude, phase, real, imaginary values of a given curve.


		Parameters
		----------
		type : str
			-'magnitude'
			-'phase' 
			-'real' 
			-'imaginary'

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is a float number referring to the magnitude, phase, real, imaginary value of all points of the given curve.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_points_db_values(cls, specifier: str, decibel_value: float, db_factor: float) -> object:

		"""

		This method collects dB values of all points of a given curve specified by its id and the window it belongs to.


		Parameters
		----------
		specifier : str, optional
			-'db' (default)
			-'dba'
			-'dbb'
			-'dbc'
			-'dbd'

		decibel_value : float, optional
			decibel_value (default is 1)

		db_factor : float, optional
			db_factor (default is 20)

		Returns
		-------
		object
			It returns a list where each member is a float number referring to the dB value of one specific point of the given curve.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_x_values_from_y(cls, specifier: str, yvalue: float) -> object:

		"""

		This method calculates X values for a given Y value of a given curve.


		Parameters
		----------
		specifier : str
			-'first' get the first x value
			-'all' get all the x values

		yvalue : float
			Value of the Y-axis.

		Returns
		-------
		object
			It returns a list with float numbers that correspond to the X-values of the curve for the given Y-value.Upon failure an empty list is returned.

		"""


	@classmethod
	def get_x_values_from_y_complex(cls, specifier: str, complex_value: float) -> object:

		"""

		This method calculates X values for a given Y-axis value of a given curve.


		Parameters
		----------
		specifier : str
			-'first' get the first x value
			-'all' get all the x values

		complex_value : float
			Value of Y complex axis.

		Returns
		-------
		object
			It returns a list with float numbers that correspond to the X-values of the curve for the given real, imaginary or phase value.Upon failure an empty list is returned.

		"""


	@classmethod
	def get_y_values_from_x(cls, specifier: str, xvalue: float) -> object:

		"""

		This method calculates Y values for a given X value of a given curve.


		Parameters
		----------
		specifier : str
			-'first' get the first y value
			-'all' get all the y values

		xvalue : float
			Value of X axis.

		Returns
		-------
		object
			It returns a list with float numbers that correspond to the Y-values of the curve for the given X-value.Upon failure an empty list is returned.

		"""


	@classmethod
	def get_y_complex_value_from_x(cls, specifier: str, xvalue: float) -> object:

		"""

		This function calculates Y complex value for a given X value of a given curve.


		Parameters
		----------
		specifier : str
			-'first' get the first y value
			-'all' get all the y values

		xvalue : float
			X-axis value.

		Returns
		-------
		object
			It returns a list with float numbers that correspond to the real, imaginary or phase values of the curve for the given X-value.Upon failure an empty list is returned.

		"""


	@classmethod
	def get_area(cls, curve2: object) -> float:

		"""

		This method calculates the area between two curves.


		Parameters
		----------
		curve2 : object
			Curve to calculate area with.

		Returns
		-------
		float
			It returns a float number referring to the corresponding area between the two given curves.Upon failure, a zero value is returned.

		"""


	@classmethod
	def get_attributes(cls, specifier: str, attr_name: str, group_name: str) -> object:

		"""

		This method returns a dictionary with all curve attributes, specific attribute or subattributes of the given curve.


		Parameters
		----------
		specifier : str
			-'all' returns a list with all attributes
			-'attribute' returns the value of a specific attribute
			-'subattribute' returns the value of a subattribute

		attr_name : str, optional
			Requested attribute name.

		group_name : str, optional
			Group name for requested subattribute.

		Returns
		-------
		object
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	@classmethod
	def set_attribute(cls, specifier: str, attr_name: str, attr_value: str, group_name: str) -> bool:

		"""

		This method sets the value of a specific attribute or subattribute referring to a given curve. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		specifier : str
			-'attribute'
			-'subattribute'

		attr_name : str
			Attribute name.

		attr_value : str
			Attribute value.

		group_name : str, optional
			Group name if subattribute is set

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_name(cls, name: str) -> bool:

		"""

		This method defines a name for a curve.


		Parameters
		----------
		name : str
			Curve name.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_color(cls, color: object) -> bool:

		"""

		This method defines a color for a curve.


		Parameters
		----------
		color : object
			Curve color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_line_style(cls, line_style: int) -> bool:

		"""

		This method defines a line style for a curve.


		Parameters
		----------
		line_style : int
			An integer number in the range of 0 and 13, which is the same being used in META commands for changing line style of curve.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_line_width(cls, line_width: int) -> bool:

		"""

		This function defines line width for a curve.


		Parameters
		----------
		line_width : int
			Line width as an integer number in the range of 0 and 10.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_point_style(cls, point_style: int) -> bool:

		"""

		This method defines point style for a curve.


		Parameters
		----------
		point_style : int
			An integer number in the range of 0 and 8, which is the same being used in META commands for changing point style of curve.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_point_size(cls, point_size: int) -> bool:

		"""

		This method defines point size for a curve.


		Parameters
		----------
		point_size : int
			An integer number in the range of 1 and 20, which is the same being used in META commands for changing point size of curve.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_mark_density(cls, mark_density: int) -> bool:

		"""

		This method finds the mark density of a given curve. Mark density is an integer number in the range of 1 and 99.


		Parameters
		----------
		mark_density : int
			Mark density defines the times a mark of a curve will appear on screen.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_point_mark(cls, point_mark: str) -> bool:

		"""

		This method sets the point mark of a given curve.


		Parameters
		----------
		point_mark : str
			A 5 character string to be used as a mark.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_selected_point_style(cls, spoint_style: int) -> bool:

		"""

		This method sets the selected point style of a given curve.


		Parameters
		----------
		spoint_style : int
			An integer number in the range of 0 and 8, which is the same being used in META commands for changing selected point style of curve.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_selected_point_size(cls, spoint_size: int) -> bool:

		"""

		This method sets the selected point size of a given curve.


		Parameters
		----------
		spoint_size : int
			An integer number in the range of 1 and 20, which is the same being used in META commands for changing selected point size of curve.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_point_precision(cls, point_precision: str) -> bool:

		"""

		This method sets the point precision of a given curve if Curve Options > Points > Follow Window settings > Identify options format is disabled.


		Parameters
		----------
		point_precision : str
			A string expression referring to the type of the point precision of the curve. 
			Its possible values are:
			- 'auto' : Auto
			- 'sciauto' : Auto-Scientific
			- 'scientific': Scientific
			- 'fixed' : Fixed

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_point_precision_digits(cls, precision_digits: int) -> bool:

		"""

		This method sets the point precision digits of a given curve if Curve Options > Points > Follow Window settings > Identify options format is disabled.


		Parameters
		----------
		precision_digits : int
			Point precision digits as an integer in the range of 0 and 20.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def show(cls) -> bool:

		"""

		This method allows the user to make a curve visible.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def hide(cls) -> bool:

		"""

		This method allows the user hide a curve.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def select(cls) -> bool:

		"""

		This method allows the user to select a curve.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def deselect(cls) -> bool:

		"""

		This method allows the user to deselect a curve.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def delete(cls) -> bool:

		"""

		This method allows the user to delete a curve.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_settings(cls, curve_settings: object) -> bool:

		"""

		This method adjusts settings of a given curve.


		Parameters
		----------
		curve_settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'options_width' : 6 , 'assign_xaxis' : 2 , 'curve_color' : 'blue'}). The names of the curve settings and its possible values are:
			- 'assign_xaxis': Set X axis assignment (integer value)
			- 'assign_yaxis': Set Y axis assignment (integer value)
			- 'baroffset': Use X axis offset for bars (0,1)
			- 'bartype': Convert curve to bar chart (0,1)
			- 'barwidth': Bar width (integer value)
			- 'curve_color': Curve color (string value)
			- 'entity_id': Change id of entity (integer value)
			- 'entity_ip': Change integration point of entity (integer value)
			- 'entity_secid': Change secondary id of entity (integer value)
			- 'entity_type': Change entity type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe',
			- 'seatbelt', 'section', 'shell', 'solid', 'spc')
			- 'entity_sectype': Change entity secondary type of entity ('bar', 'beam', 'coord', 'cweld', 'damp', 'elas', 'element', 'force', 'gap', 'joint', 'jstiff', 'mass', 'moment', 'mpc', 'node', 'none', 'part', 'plink', 'pload', 'rbe', 'seatbelt', 'section', 'shell', 'solid', 'spc')
			- 'fill': Fill bar type curve (0,1)
			- 'linewidth': Curve width (integer value)
			- 'mark': Curve mark (string value)
			- 'mark_number': Curve mark number (integer value)
			- 'point_precision_digits': Point precision digits (integer value)
			- 'point_precision_type': Point precision type ('auto', 'fixed', 'sciauto', 'scientific')
			- 'point_size': Point size (integer value)
			- 'follow_identify': Curve style follows identify format
			- 'point_font': Point font (string value)
			- 'point_size': Point size (integer value)
			- 'point_style': Point style (integer value)
			- 'style': Curve style (integer value)

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Curve.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Curve. Upon failure, it returns None.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Curve.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Curve. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Curve.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Curve. Upon failure, it returns None.

		"""


	def apply_function(self, function: str, parameter: object) -> bool:

		"""

		This method applies a function on a curve and replaces it.


		Parameters
		----------
		function : str
			function can be:
			octave, loctave, thirdoctave, thirdloctave, integr, autocorrel, srms, srss, flip, simplify, fix, inv, saecfc060, saecfc180, saecfc600, saecfc1000, cfc060, cfc180, cfc600, cfc1000, resample, shift, newshift, scale, newscale, customoctave, movaver, expmovaver, wmovaver, movingaver, expmovingaver, wmovingaver, frftrans, trim, differ, mpvalue, rivalue, envcurve, hic, fir100, iirfilt, bwfilt, normbwfilt,fft, ifft,dft,idft, winft, levelcross, timeabovelevel, percentile, convex, histogram, trendline, idealbandpass, windows, saefilter1981, estiff, dbfilter, dbfilter

		parameter : object, optional
			parameters of each function
			function         parameters
			octave          ,NULL 
			loctave         ,NULL
			thirdoctave     ,NULL
			thirdloctave    ,NULL
			integr          ,NULL
			autocorrel      ,NULL
			srms            ,NULL
			srss            ,NULL
			flip            ,NULL
			simplify        ,NULL
			fix             ,NULL
			inv             ,NULL
			saecfc060       ,NULL
			saecfc180       ,NULL
			saecfc600       ,NULL
			saecfc1000      ,NULL
			cfc060          ,NULL
			cfc180          ,NULL
			cfc600          ,NULL
			cfc1000         ,NULL
			resample        ,{"type":"points"                  , "points":integer}
			resample        ,{"type":"timestep"                , "timestep":float}
			shift           ,{"direction":"left/right/up/down" , "shiftvalue":float}
			newshift        ,{"direction":"left/right/up/down" , "shiftvalue":float}
			scale           ,{"direction":"x/y/z/all"          , "scalevalue":float}
			newscale        ,{"direction":"x/y/z/all"          , "scalevalue":float}
			customoctave    ,{"bands":"name"                   , "nfactor":int}
			movaver         ,{"terms":int}expmovaver      ,{"terms":int}
			wmovaver        ,{"terms":int}
			movingaver      ,{"terms":int, "centered":bool, "keeppoints":bool})
			expmovingaver   ,{"terms":int, "centered":bool, "keeppoints":bool})
			wmovingaver     ,{"terms":int, "centered":bool, "keeppoints":bool})
			frftrans        ,{"type":"disp2vel/disp2acc/vel2disp/vel2acc/acc2disp/acc2vel"}
			trim            ,{"type":"start/end/both" , "threshold shift":float , "threshold":bool}
			differ          ,{"type":"centered/backward/forward/ecer94"}
			mpvalue         ,{"type":"multof/sumof/divof/diffof" , "magn":float , "phase":float}
			rivalue         ,{"type":"multof/sumof/divof/diffof" , "real":float , "imag":float}
			envcurve        ,{"type":"min/max" }
			hic             ,{"interval":float }
			fir100          ,{"removebias":bool }
			iirfilt         ,{"cutoff":float,"attenuation":float,"stopbandfreq": float}
			bwfilt          ,{"frequency":float}normbwfilt      ,{"order":int , "frequency":float}
			fft             ,{"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,"window":"none/triang/hanning/welch/hamming/blackman/parzen"}
			ifft            ,{"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,"window":"none/triang/hanning/welch/hamming/blackman/parzen"}
			dft             ,{"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,"window":"none/triang/hanning/welch/hamming/blackman/parzen"}
			idft            ,{"curvedata":"real/complex","loadresults":"magnit/phase","loadx":"index/freq/period,"window":"none/triang/hanning/welch/hamming/blackman/parzen"}
			winft           ,{"window":"none/triang/hanning/welch/hamming/blackman/parzen"}
			levelcross      ,{"threshold":float}
			timeabovelevel  ,{"limit":float}
			percentile      ,{"percentage":float , "method":"method1/method2"}
			convex          ,{"type":"upward/downward"}
			histogram       ,{"type":"binwidth","binwidth":float,"method":"startend","start":float,"end":float}
			histogram       ,{"type":"binwidth" , "binwidth":float , "method":"center" , "bincenter":float}
			histogram       ,{"type":"numberofbins" , "numberofbins":int , "method":"startend" , "start":float,"end":float}
			trendline       ,{"type":"linear" }
			trendline       ,{"type":"polynomial" , "order":int}idealbandpass   ,{"low":float , "high":float}
			windows         ,{"window":"triang/hanning/welch/hamming/blackman/parzen" , "terms":int , "centered":bool , "keeppoints":bool}
			saefilter1981   ,{"type":"1000channelclass/180channelclass/60channelclass/600channelclass"}
			estiff          ,{"k":float ,"freq_min":float,"freq_max":float,"ref":float}
			dbfilter        ,{"dbtype":"dba/dbb/dbc/dbd/dbn/revdba/revdbb/revdbc/revdbd/revdbn","dbvalue":float}
			dbfilter        ,{"dbtype":"dba/dbb/dbc/dbd/dbn/revdba/revdbb/revdbc/revdbd/revdbn","dbvalue":float, "factor":float}

		Returns
		-------
		bool
			Returns True upon success or False upon failure.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Curve entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Point():

	"""

	Class for points.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    point = plot2d.Point(
		        id=50, curve_id=1, curve_type=0, window_name="Window1", page_id=0
		    )
		    print(point)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    type = "magn"
		    pointlist = curve.get_points(specifier, type, point_id=16)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr_value = "from_filename"
		    for point in pointlist:
		        ret = point.set_attribute(specifier, attr_name, attr_value)
		        ret = point.get_attributes(specifier, attr_name)
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attribute
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    type = "magn"
		    pointlist = curve.get_points(specifier, type, point_id=16)
		    specifier = "attribute"
		    attr_name = "Filename"
		    attr_value = "from_filename"
		    for point in pointlist:
		        ret = point.set_attribute(specifier, attr_name, attr_value)
		        ret = point.get_attributes(specifier, attr_name)
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: select
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    type = "magn"
		    pointlist = curve.get_points(specifier, type, point_id=16)
		    for point in pointlist:
		        ret = point.select()
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: deselect
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    curve = plot2d.Curve(id=1, window_name="Window1", page_id=0)
		    specifier = "byid"
		    type = "magn"
		    pointlist = curve.get_points(specifier, type, point_id=16)
		    for point in pointlist:
		        ret = point.deselect()
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    point = plot2d.Point(
		        id=50, curve_id=1, curve_type=0, window_name="Window1", page_id=0
		    )
		    can_use = point.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Id of the point.

	"""

	x: float = None
	"""
	X coordinate of the point.

	"""

	y: float = None
	"""
	Y coordinate of the point.

	"""

	selected: int = None
	"""
	- 1 if point is selected
	- 0 if it is not selected

	"""

	@classmethod
	def get_attributes(cls, specifier: str, attr_name: str, group_name: str) -> str:

		"""

		This function returns a dictionary containing a specific attributes, a subattribute, or all attributes referring to a given point.


		Parameters
		----------
		specifier : str
			-'all'
			-'attribute'
			-'subattribute'

		attr_name : str, optional
			This is the name of the attribute or subattribute.

		group_name : str, optional
			Group name in case of subattribute.

		Returns
		-------
		str
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		"""


	@classmethod
	def set_attribute(cls, specifier: str, attr_name: str, attr_value: str, group_name: str) -> int:

		"""

		This method sets the value of a specific attribute referring to a given point. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		specifier : str
			-'attribute'
			-'subattribute'

		attr_name : str
			Name of the attribute.

		attr_value : str
			Value of the attribute.

		group_name : str, optional
			Name of the group.

		Returns
		-------
		int
			It returns 1 upon success and 0 upon failure.

		"""


	@classmethod
	def select(cls) -> int:

		"""

		This method selectes the given point.


		Returns
		-------
		int
			It returns 1 upon success and 0 upon failure.

		"""


	@classmethod
	def deselect(cls) -> int:

		"""

		This method deselectes the given point.


		Returns
		-------
		int
			It returns 1 upon success and 0 upon failure.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Point entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class CurveGroup():

	"""

	Class for curve groups.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    if cg:
		        print(cg.name, cg.plot_id, cg.window_name, cg.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    curvelist = cg.get_curves()
		    for c in curvelist:
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
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    page = cg.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_subgroups
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    sublist = cg.get_subgroups()
		    for g in sublist:
		        print(g.name, g.plot_id, g.window_name, g.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    w = cg.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    cg2 = plot2d.CurveGroup(name="Group_2", plot_id=0, window_name="Window1", page_id=0)
		    curvelist = cg.get_curves()
		    ret = cg2.set_curves(curvelist)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: ungroup_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    ret = cg.ungroup()
		    # ret = cg.ungroup('Group_1')
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(name="Group_1", plot_id=0, window_name="Window1", page_id=0)
		    ret = cg.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    cg = plot2d.CurveGroup(
		        name="curve_group", plot_id=0, window_name="Window1", page_id=0
		    )
		    can_use = cg.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the curve group.

	"""

	plot_id: int = None
	"""
	Plot id of the curve group.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the curve group.

	"""

	def get_curves(self, group_name: str) -> object:

		"""

		This method collects all the curves of a given group.


		Parameters
		----------
		group_name : str
			Name of the group.

		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Curve referring to one specific curve of the given group.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_subgroups(cls, group_name: str, level: int) -> object:

		"""

		This method searches for the subgroups of a given curve group.


		Parameters
		----------
		group_name : str
			Name of the curve group.

		level : int, optional
			Depth of searching for subgroups (1 - one level down, 2 - two levels down, 3 - three levels down etc.). If it is absent, then this function will search down all levels for subgroups.

		Returns
		-------
		object
			Upon success, it returns a list where each member of the list is an object of class CurveGroup referring to one subgroup of the given group.Upon failure, an empty list is returned.

		"""


	@classmethod
	def set_curves(cls, curvelist: object) -> bool:

		"""

		This method adds some specific curves on a given curve group.


		Parameters
		----------
		curvelist : object
			List of curve objects to be added on the given curve group.

		Returns
		-------
		bool
			It returns 1 upon success and 0 upon failure.

		"""


	@classmethod
	def delete(cls, group_name: str) -> bool:

		"""

		This method deletes all curves of a given group.


		Parameters
		----------
		group_name : str
			Name of the group.

		Returns
		-------
		bool
			It returns 1 upon success and 0 upon failure.

		"""


	@classmethod
	def ungroup(cls, group_name: str) -> bool:

		"""

		This method ungroups all curves of a given group.


		Parameters
		----------
		group_name : str
			Name of the group.

		Returns
		-------
		bool
			It returns 1 upon success and 0 upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the CurveGroup.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the CurveGroup. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the CurveGroup.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the CurveGroup. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META CurveGroup entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class PlotAxis():

	"""

	Class for plot axes.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plax = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    if plax:
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
		# method: add
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.add()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: control_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "or"
		    # specifier = 'not'
		    # specifier = 'and'
		    # specifier = 'select'
		    # specifier = 'deselect'
		    ret = axis.control_curves(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: data_format
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "rpm"
		    # specifier = 'frequency'
		    # specifier = 'peak2peak'
		    # specifier = 'rms'
		    # specifier = 'rad'
		    # specifier = 'deg'
		    # specifier = 'altdeg'
		    # specifier = 'phase'
		    # specifier = 'altphase'
		    # specifier = 'real'
		    # specifier = 'imag'
		    # specifier = 'rmsmagn'
		    # specifier = 'radphase'
		    # specifier = 'altradphase'
		    ret = axis.data_format(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: delete
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="Window1", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.delete()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    color = axis.get_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_curves
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    curves = axis.get_curves()
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
		# method: get_increment
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_increment()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_title()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_multiplier
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_multiplier()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    page = axis.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    pl = axis.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_scale_limit
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "max"
		    # specifier = 'min'
		    ret = axis.get_scale_limit(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_step
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_step()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_value
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "max"
		    specifier = "min"
		    ret = axis.get_value(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    w = axis.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_active
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.set_active(onoff=False)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_auto
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    # onoff = False
		    ret = axis.set_auto(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    mycolor = windows.Color(name="0_100_0_0", r=0, g=100, b=0, a=0)
		    ret = axis.set_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    title = "New Axis Label"
		    ret = axis.set_title(title)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_dbfactor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    dbfactor = 30
		    ret = axis.set_dbfactor(dbfactor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_dbvalue
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    dbfactor = 2
		    ret = axis.set_dbvalue(dbfactor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_increment
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    increment = 5
		    ret = axis.set_increment(increment)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_align
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    y_axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    align = "right"
		    # align = 'left'
		    ret = y_axis.set_values_align(align)
		    print(ret)
		    x_axis = plot2d.PlotAxis(
		        id=0, type="xaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    align = "up"
		    # align = 'down'
		    ret = x_axis.set_values_align(align)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    mycolor = windows.Color(name="255_0_0_0", r=255, g=0, b=0, a=0)
		    ret = axis.set_values_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_format
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    format = "vertical"
		    # format = 'horizontal'
		    # format = '45degrees'
		    ret = axis.set_values_format(format)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    y_axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    position = "right"
		    # position = 'left'
		    ret = y_axis.set_values_position(position)
		    print(ret)
		    x_axis = plot2d.PlotAxis(
		        id=0, type="xaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    position = "up"
		    # position = 'down'
		    ret = x_axis.set_values_position(position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_precision
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "type"
		    prec_type = "auto"
		    # prec_type = 'sciauto'
		    # prec_type = 'scientific'
		    # prec_type = 'fixed'
		    ret = axis.set_values_precision(specifier, precision_type=prec_type)
		    # specifier = 'digits'
		    # ret = axis.set_values_precision(specifier , digits = 3)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_limit
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "min"
		    # specifier = 'max'
		    value = 30
		    ret = axis.set_limit(specifier, value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_lockrange
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    # onoff = False
		    ret = axis.set_lockrange(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_locktitle
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    onoff = False
		    ret = axis.set_locktitle(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_multiplier
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    multiplier = 2
		    ret = axis.set_multiplier(multiplier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_dbfactor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    dbfactor = 40
		    ret = radius.set_radius_dbfactor(dbfactor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_dbvalue
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    dbfactor = 2
		    ret = radius.set_radius_dbvalue(dbfactor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_decibel
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    option = "db"
		    # option = 'dba'
		    # option = 'dbb'
		    # option = 'dbc'
		    # option = 'dbd'
		    # option = 'off'
		    ret = radius.set_radius_decibel("db")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_locklimits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    onoff = True
		    # onoff = False
		    ret = radius.set_radius_locklimits(True)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_locksteps
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    onoff = True
		    # onoff = False
		    ret = radius.set_radius_locksteps(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_log
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    onoff = True
		    onoff = False
		    ret = radius.set_radius_log(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_range
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    min = 40
		    max = 60
		    ret = radius.set_radius_range(min, max)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_radius_step
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window1", page_id=0)
		    radius = plot.get_polar_radius()
		    step = 6
		    ret = radius.set_radius_step(step)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_range
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    min = 30
		    max = 50
		    ret = axis.set_range(min, max)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_scale_limit
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "min"
		    # specifier = 'max'
		    ret = axis.set_scale_limit(specifier, 20)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    settings = {"range": "5,7", "label": "Velocities", "dataformat": "rms"}
		    ret = axis.set_settings(settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_show_options
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "number"
		    # specifier = 'multiplier'
		    # specifier = 'values'
		    # specifier = 'magphase'
		    # specifier = 'title'
		    # specifier = 'logdb'
		    # specifier = 'zeroaxis'
		    onoff = True
		    # onoff = False
		    ret = axis.set_show_options(specifier, onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_step
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    step = 10
		    ret = axis.set_step(step)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_step_label
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "add"
		    step = 3
		    ret = axis.set_step_label(specifier, step, label="New Lab")
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_type
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    type = "log"
		    ret = axis.set_type(type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_unitsystem
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    # onoff = False
		    axis.show_unitsystem(onoff)
		    system = "mmkms"
		    ret = axis.set_unitsystem(system)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_values_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    font = "DejaVu Sans,8,-1,5,50,0,0,0,0,0"
		    ret = axis.set_values_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_visible
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    # onoff = False
		    ret = axis.set_visible(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_zeroaxis_options
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    mycolor = windows.Color(name="Red", r=255, g=0, b=0, a=0)
		    specifier = "on"
		    specifier = "off"
		    ret = axis.set_zeroaxis_options(specifier)
		    # specifier = 'style'
		    # ret = axis.set_zeroaxis_options(specifier, style = 4)
		    # specifier = 'width'
		    # ret = axis.set_zeroaxis_options(specifier, width = 3)
		    # specifier = 'color'
		    # ret = axis.set_zeroaxis_options(specifier, color = mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_unitsystem
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    onoff = True
		    onoff = False
		    ret = axis.show_unitsystem(onoff)
		    print(ret)
		    system = "mmkms"
		    ret = axis.set_unitsystem(system)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_title_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    font = "Carlito,11,-1,5,50,0,0,0,0,0"
		    ret = axis.set_title_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_title_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    mycolor = windows.Color(name="0_100_0_0", r=0, g=100, b=0, a=0)
		    ret = axis.set_title_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_title_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    color = axis.get_title_color()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_step_label
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    specifier = "add"
		    step = 3
		    label = "New Lab"
		    ret = axis.set_step_label(specifier, step, label)
		    print(ret)
		    step = 3
		    str = axis.get_step_label(step)
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_type
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_type()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_auto
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_auto()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_lockrange
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_lockrange()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_locktitle
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_locktitle()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_lockincrement
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_lockincrement()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_lockstep
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_lockstep()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_dbvalue
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_dbvalue()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_dbfactor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_dbfactor()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_font()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_title_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_title_font()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_format
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_format()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_precision
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_precision()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_position()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_align
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_align()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_values_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_values_color()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_radius_locklimits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="zaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_radius_locklimits()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_radius_locksteps
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="zaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    str = axis.get_radius_locksteps()
		    print(str)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_radius_step
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="zaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_radius_step()
		    print(str(ret))
		
		
		if __name__ == "__main__":
		    main()
		# method: get_radius_dbvalue
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="zaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_radius_dbvalue()
		    print(str(ret))
		
		
		if __name__ == "__main__":
		    main()
		# method: get_radius_dbfactor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    axis = plot2d.PlotAxis(
		        id=0, type="zaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    ret = axis.get_radius_dbfactor()
		    print(str(ret))
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plax = plot2d.PlotAxis(
		        id=0, type="yaxis", plot_id=0, window_name="Window1", page_id=0
		    )
		    can_use = plax.is_usable()
		    print(can_use)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot axis id.

	"""

	type: str = None
	"""
	Plot axis type ('xaxis', 'yaxis', 'zaxis', 'caxis').

	"""

	plot_id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the plot2d window of the plot axis.

	"""

	active: int = None
	"""
	- 1 if plot axis is active
	- 0 if it is not active

	"""

	visible: int = None
	"""
	- 1 if plot axis is visible
	- 0 if it is not visible

	"""

	min_value: float = None
	"""
	Minimum value of plot axis.

	"""

	max_value: float = None
	"""
	Maximum value of plot axis.

	"""

	page_id: int = None
	"""
	Id of the page of the plot axis.

	"""

	log_on: bool = None
	"""
	- True if log is enabled
	- False if log is disabled

	"""

	db_type: int = None
	"""
	Decibel type option:
	 - 0 : plain
	 - 1 : db
	 - 2 : db(A)
	 - 3 : db(B)
	 - 4 : db(C)
	 - 5 : db(D)

	"""

	db_value: float = None
	"""
	Decibel value

	"""

	db_factor: float = None
	"""
	Decibel factor

	"""

	range_lock: int = None
	"""
	- 1 if range lock in enabled
	- 0 if range lock is disabled

	"""

	octave_on: bool = None
	"""
	- True if the respective axis type is enabled
	- False if not

	"""

	thirdoctave_on: bool = None
	"""
	- True if the respective axis type is enabled
	- False if not

	"""

	octavelow_on: bool = None
	"""
	- True if the respective axis type is enabled
	- False if not

	"""

	thirdoctavelow_on: bool = None
	"""
	- True if the respective axis type is enabled
	- False if not

	"""

	@classmethod
	def get_curves(cls) -> object:

		"""

		This function finds the curves of a given plot axis.


		Returns
		-------
		object
			It returns a list where each member of the list is an object of class Curve referring to one specific curve of a given plot axis.Upon failure, an empty list is returned.

		"""


	@classmethod
	def get_scale_limit(cls, specifier: str) -> float:

		"""

		This function returns the minimum or maximum limit of the given Axis.


		Parameters
		----------
		specifier : str
			-'min' for minimum axis value
			-'max' for maximum axis value

		Returns
		-------
		float
			Returns a float number corresponding to the minimum or maximum value of the axis.Upon failure, no value is returned.

		"""


	@classmethod
	def get_value(cls, specifier: str) -> float:

		"""

		This function returns the minimum or maximum value of all curves assigned to the given axis.


		Parameters
		----------
		specifier : str
			-'min' is the minimum value
			-'max' is the maximum value

		Returns
		-------
		float
			Returns a float number corresponding either the minimum or maximum value of the axis.Upon failure no value is returned.

		"""


	@classmethod
	def get_title(cls) -> str:

		"""

		This method returns the title of the given axis.


		Returns
		-------
		str
			Returns a string which is the title of the given axis.

		"""


	@classmethod
	def get_values_color(cls) -> object:

		"""

		This method returns a Color object, the color used to draw the values of the given axis.


		Returns
		-------
		object
			Returns a color object corresponding to the values axis color.

		"""


	@classmethod
	def get_multiplier(cls) -> float:

		"""

		This method returns a float number, the multiplier of the given axis.


		Returns
		-------
		float
			Returns a float number corresponding to the multiplier of the axis.

		"""


	@classmethod
	def get_step(cls) -> int:

		"""

		This method returns the step of a given axis.


		Returns
		-------
		int
			Returns an integer corresponding to the step of the given axis.

		"""


	@classmethod
	def get_increment(cls) -> float:

		"""

		This method returns the increment between two steps of the given axis.


		Returns
		-------
		float
			Returns a float number corresponding to the increment between two steps of an axis.

		"""


	@classmethod
	def set_scale_limit(cls, specifier: str) -> bool:

		"""

		This method sets the minimum and maximum values of the scale of the axis.


		Parameters
		----------
		specifier : str
			-'min' set the minimum value of the axis.
			-'max' set the maximum value of the axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_color(cls, color: object) -> bool:

		"""

		This method sets the axis color of the given axis.


		Parameters
		----------
		color : object
			Color object to set as axis color.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_title(cls, title: str) -> bool:

		"""

		This method sets the title of the given axis.


		Parameters
		----------
		title : str
			it is the title that will be assigned to the axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_type(cls, type: str) -> bool:

		"""

		This method sets the type of scale to apply on a given axis.


		Parameters
		----------
		type : str
			-'plain' to set normal scale
			-'log' to set log scale
			-'db' to set db scale
			-'dba' to set dba scale
			-'dbb' to set dbb scale
			-'dbc' to set dbc scale
			-'dbd' to set dbd scale

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_auto(cls, onoff: bool) -> bool:

		"""

		This method sets to "on" or "off" for auto calculate of the limits of the given axis.


		Parameters
		----------
		onoff : bool
			set True for auto calculate on or False to disable auto calculate.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_lockrange(cls, onoff: bool) -> bool:

		"""

		This method is used to lock or unlock the limits of the scale of a given axis.


		Parameters
		----------
		onoff : bool
			set True to lock axis value, False to unlock it.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_locktitle(cls, onoff: bool) -> bool:

		"""

		This method can be used to lock or unlock the axis title.When locked axis title does not change if the user reads a new curve from any deck.


		Parameters
		----------
		onoff : bool
			set True for locked title, False for unlocked title

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_limit(cls, specifier: str, value: float) -> bool:

		"""

		This method is used to set the minimum or maximum values of the scale of a given axis.


		Parameters
		----------
		specifier : str
			-'min' for minimum value
			-'max' for maximum value

		value : float
			float value to be set as minimum or maximum

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_range(cls, min: float, max: float) -> bool:

		"""

		This method sets the range (minimum and maximum values) of the scale of the given axis.


		Parameters
		----------
		min : float
			float to be the minimum value of the range

		max : float
			float to be the maximum value of the range

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_step(cls, step: int) -> bool:

		"""

		This method is used to set the steps of the given axis.


		Parameters
		----------
		step : int
			integer number to be the new steps of the axis

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_increment(cls, increment: float) -> bool:

		"""

		This method can be used to set the increment between two steps of the given axis.


		Parameters
		----------
		increment : float
			float number to be the new increment between two steps of an axis

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_dbvalue(cls, dbvalue: float) -> bool:

		"""

		This method can be used to set the dB value for a given axis.


		Parameters
		----------
		dbvalue : float
			float to be set as dB value

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_dbfactor(cls, dbfactor: float) -> bool:

		"""

		This method can be used to set the dB factor for a given axis.


		Parameters
		----------
		dbfactor : float
			float number to set as dB factor of an axis

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_step_label(cls, specifier: str, step: int, label: str) -> bool:

		"""

		This method can be used to set a label instead of the value at a certain step, or delete a label from a certain step of the given axis.


		Parameters
		----------
		specifier : str
			-'add'
			-'delete'

		step : int
			integer for the step to be affected

		label : str, optional
			string used to add a label on a step

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_active(cls, onoff: bool) -> bool:

		"""

		This method can be used to set a given axis active or inactive.


		Parameters
		----------
		onoff : bool
			True to set axis active, False to set it inactive

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_visible(cls, onoff: bool) -> bool:

		"""

		This method can be used to set a given axis visible or non visible.


		Parameters
		----------
		onoff : bool
			True to set axis visible, False to set it invisible

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_multiplier(cls, multiplier: float) -> bool:

		"""

		This method can be used to set the multiplier of the given axis.


		Parameters
		----------
		multiplier : float
			float number, which will be the power of the multiplier.
			eg. 2 sets multiplier to 10e2, -4 sets multiplier to 10e-4.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_show_options(cls, specifier: str, onoff: bool) -> bool:

		"""

		This method can be set to show/hide certain features from the given axis.


		Parameters
		----------
		specifier : str
			-'number' show/hide number of axis on title
			-'multiplier' show/hide multiplier
			-'values' show/hide values on steps
			-'magphase' show/hide magnitude phase on title
			-'title' show/hide title
			-logdb' show/hide log/db on title
			-'zeroaxis' show hide zero axis

		onoff : bool
			set True to enable feature visibility, set False to disable feature visibility.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_zeroaxis_options(cls, specifier: str, style: int, width: int, color: object) -> object:

		"""

		This method can be used to set options of zero axis.


		Parameters
		----------
		specifier : str
			-'on' show zero axis
			-'off' hide zero axis
			-'style' set the style of the zero axis
			-'width' set the width
			-'color' set the color

		style : int, optional
			integer number to set the line style of the zero axis.

		width : int, optional
			integer number to set the line width of the zero axis.

		color : object, optional
			Color object to be set as axis object.

		Returns
		-------
		object
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_unitsystem(cls, system: str) -> bool:

		"""

		This method can be used to set the Unit system of the given axis.


		Parameters
		----------
		system : str
			String of the name of the Unit system to be applied:
			'mks','mmks','mkms','mmkms','mmkggms','mmts','mmdats','mmgms','cgs','cgmis','c100ks','fsls','ipms','cks','ckms','ckmis','mmgs','cgms','cgmin','mmgmin','kmkh'

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_unittype(cls, type: str) -> bool:

		"""

		This method can be used to apply Unit type to every curve assigned to the given axis.


		Parameters
		----------
		type : str

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_secunittype(cls) -> bool:

		"""

		This method can be used to apply secondary unit type to every curve assigned to the given axis.


		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_format(cls, format: str) -> bool:

		"""

		This method can be used to set the axis values format.


		Parameters
		----------
		format : str
			-'vertical' use vertical format of labels
			-'horizontal' horizontal format of labels
			-'45degrees' label formatted at 45 degrees

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_precision(cls, specifier: str, precision_type: str, digits: int) -> bool:

		"""

		This method can be used to set the values precision type or precision digits of a given axis.


		Parameters
		----------
		specifier : str
			-'type' to set different precision type.
			-'digits' to set the fixed precision digits.

		precision_type : str, optional
			-'auto'
			-'sciauto'
			-'scientific'
			-'fixed'

		digits : int, optional
			integer to set as fixed precision digits.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_position(cls, position: str) -> bool:

		"""

		This method can be used to set the values position on a given axis.


		Parameters
		----------
		position : str
			-'up' or -'down' for x axis type.
			-'right' or -'left' for y axis type.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_align(cls, align: str) -> bool:

		"""

		This method can be used to set values alignment.


		Parameters
		----------
		align : str
			-'up' or -'down' for x axis type.
			-'right' or -'left' for y axis type.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_font(cls, font: str) -> bool:

		"""

		This method can be used to set the fonts for the axis values.


		Parameters
		----------
		font : str
			String to be used for font name of axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_values_color(cls, color: object) -> bool:

		"""

		This method can be used to change the values color.


		Parameters
		----------
		color : object
			color object to be used as color for values axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_range(cls, min: float, max: str) -> bool:

		"""

		This method can be used to change the range of the radius axis of polar plot.


		Parameters
		----------
		min : float
			float to be used as minimum value of the axis.

		max : str
			float to be used as maximum value of the axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_locklimits(cls, onoff: bool) -> bool:

		"""

		This method can be used to lock the range of radius axis of polar plot.


		Parameters
		----------
		onoff : bool
			Set True to lock limits of radius axis of polar plot, set False to unlock.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_locksteps(cls, onoff: bool) -> bool:

		"""

		This method can be used to set the radius axis of polar plot.


		Parameters
		----------
		onoff : bool
			Set True to lock steps of radius axis of polar plot, False to unlock.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_log(cls, onoff: bool) -> bool:

		"""

		This method can be used to set the scale of a radius axis of a polar plot to log.


		Parameters
		----------
		onoff : bool
			Set True to set scale type to log, False to set it to plain.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_decibel(cls, option: str) -> bool:

		"""

		This method can be used to set dB,dBa,dBb,dBc,dBd or plain scale of radius axis.


		Parameters
		----------
		option : str
			-'db' set radius to dB
			-'dba' set radius to dBa
			-'dbb' set radius to dBb
			-'dbc' set radius to dBc
			-'dbd' set radius to dBd
			-'off' set plain scale.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_step(cls, step: int) -> bool:

		"""

		This method can be used to set the steps of a radius axis.


		Parameters
		----------
		step : int
			Integer number used as steps for a radius axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_dbvalue(cls, dbvalue: float) -> bool:

		"""

		This method can be used to set the dB value for a radius axis.


		Parameters
		----------
		dbvalue : float
			float to be set as dB value

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_radius_dbfactor(cls, dbfactor: float) -> bool:

		"""

		This method can be used to set the dB factor for a radius axis.


		Parameters
		----------
		dbfactor : float
			float number to set as dB factor of an axis

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def add(cls) -> bool:

		"""

		This method can be used to add a secondary axis.


		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def delete(cls) -> bool:

		"""

		This method can be used to delete a secondary axis.


		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def control_curves(cls, specifier: str) -> bool:

		"""

		This method can be used to control curves of a given axis.


		Parameters
		----------
		specifier : str
			String used to define -'or' -'not' -'and' -'select' -'deselect' for the curves assigned to the given axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def data_format(cls, specifier: str) -> bool:

		"""

		This method can be used to change the data format of a given axis.If the axis is X axis type: 'order', 'rpm', or 'frequency' can be used.If it is Y axis type: 'peak2peak' or 'rms' can be used.If it is complex axis type: 'rad', 'deg', altdeg' or 'altrad' can be used.If it is Z axis type: 'magn','phase','altphase','real','imag','rmsmagn','radphase' or 'altradphase' can be used.


		Parameters
		----------
		specifier : str
			'order'
			'rpm'
			'frequency'
			
			'peak2peak' 
			'rms'
			
			'rad'
			'deg'
			'altdeg'
			'altrad'
			
			'magn'
			'phase'
			'altphase'
			'real'
			'imag'
			'rmsmagn'
			'radphase'
			'altradphase'

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def show_unitsystem(cls, onoff: bool) -> bool:

		"""

		This method can be used to set Unit system of a given axis on and off.


		Parameters
		----------
		onoff : bool
			Set True to set unit system visible, False to hide it.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_settings(cls, settings: object) -> bool:

		"""

		This function controls settings of a given axis.


		Parameters
		----------
		settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'auto' : 1 , 'zeroaxis' : 1, 'label' : 'Velocity'}). The names of the settings and its allowed values are:
			-'auto' : enable/disable auto range for axis (0,1)
			-'lock_values' : make current values default (0,1)
			-'log' : enable/disable log values (0,1)
			-'lock' : lock values of axis to primary axis of number of plot (0 to 16)
			-'zeroaxis' : show/hide zero axis (0,1)
			-'decibel' : apply decibel on axis. Value can be: 'on', 'off', 'dba', 'dbb', dbc', 'dbd'
			-'dbvalue' : dB value (float value)
			-'min' : minimum value of axis (float value)
			-'max' : maximum value of axis (float value)
			-'step' : step of axis (integer value)
			-'increment' : increment of each step (float value)
			-'label' : label of axis (string value)
			-'unlock' : unlock a locked axis. (0,1)
			-'range' : apply a range for an axis (two float values)
			-'values_font' : apply font for axis values
			-'title_font' : apply font for axis title
			-'lockstep' : apply lock on steps
			-'hidevalues' : hide values of axis
			-'hidetitle' : hide title of axis
			-'reversed' : show reversed axis from max to min
			-'multiplier' : show or hide the multiplier
			-'showlogdb' : show or hide the log or db in title
			-'valueformat' : apply format type ('auto', 'scientific', fixed', sciauto', noformat')
			-'valuedigits': decimal digits in fixed and scientific formats
			-'dataformat' : change the values shown in axis. Options are:
			x axis : 'orderdata', 'rpmdata', 'freqdata' (in case axis has frequency data)
			y axis : 'peak2peak' , 'rms' 
			complex : 'deg' (0 to 360), 'altdeg' (-180 to 180), rad (0 to 2pi), altrad (-pi to pi)

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the PlotAxis.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the PlotAxis. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the PlotAxis


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the PlotAxis. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the PlotAxis.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the PlotAxis. Upon failure, it returns None.

		"""


	def set_log(self, onoff: bool):

		"""

		Enable/disable the respective axis type


		Parameters
		----------
		onoff : bool

		"""


	def set_octave(self, onoff: bool):

		"""

		Enable/disable the respective axis type


		Parameters
		----------
		onoff : bool

		"""


	def set_thirdoctave(self, onoff: bool):

		"""

		Enable/disable the respective axis type


		Parameters
		----------
		onoff : bool

		"""


	def set_octavelow(self, onoff: bool):

		"""

		Enable/disable the respective axis type


		Parameters
		----------
		onoff : bool

		"""


	def set_thirdoctavelow(self, onoff: bool):

		"""

		Enable/disable the respective axis type


		Parameters
		----------
		onoff : bool

		"""


	@classmethod
	def set_title_font(cls, font: str) -> bool:

		"""

		This method can be used to set the fonts for the axis title.


		Parameters
		----------
		font : str
			String to be used for font name of axis.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def set_title_color(cls, color: object) -> bool:

		"""

		This method sets the axis title color of the given axis.


		Parameters
		----------
		color : object
			Color object to set as axis title color.

		Returns
		-------
		bool
			Returns true upon success and false upon failure.

		"""


	@classmethod
	def get_title_color(cls) -> object:

		"""

		This method returns a Color object, the color of the given axis title.


		Returns
		-------
		object
			This method returns a Color object, the color of the given axis title.

		"""


	@classmethod
	def get_step_label(cls, step: int) -> str:

		"""

		This method can be used to get a label from a certain step of a given axis


		Parameters
		----------
		step : int
			integer for the step of the label.

		Returns
		-------
		str
			Returns a string which is the Label of the step of the given axis, or none if it doesn't exist

		"""


	@classmethod
	def get_type(cls) -> str:

		"""

		This method returns the type of data of an axis.Can be: 'plain', 'db', 'dba', 'dbb', 'dbc', 'dbd', 'log', 'octave', 'thirdoctave', 'lowoctave', 'thirdlowoctave'


		Returns
		-------
		str
			Upon success returns a string with the type of data of the axis.

		"""


	@classmethod
	def get_auto(cls) -> bool:

		"""

		This method returns True or False when auto flag of an Axis is on or not.


		Returns
		-------
		bool
			Upon success returns True or False and represents the auto flag.

		"""


	@classmethod
	def get_lockrange(cls) -> bool:

		"""

		This method returns the state of the lockrange flag.


		Returns
		-------
		bool
			Upon success returns True or False and is the state of the lockrange flag

		"""


	@classmethod
	def get_locktitle(cls) -> bool:

		"""

		This method returns the state of the locktitle flag of the Axis


		Returns
		-------
		bool
			Upon success returns True or False and is the state of the locktitle flag

		"""


	@classmethod
	def get_lockincrement(cls) -> bool:

		"""

		This method returns the state of the lockincrement flag of an Axis


		Returns
		-------
		bool
			Upon success returns True or False as the state of the lockincrement flag

		"""


	@classmethod
	def get_lockstep(cls) -> bool:

		"""

		This method returns the state of the lockstep flag of an Axis


		Returns
		-------
		bool
			Upon success returns True or False as the state of the lockstep flag

		"""


	@classmethod
	def get_dbvalue(cls) -> float:

		"""

		This method returns the dbvalue which is applied on a value when set to db type.


		Returns
		-------
		float
			Upon success returns a float which is the dbvalue of the axis

		"""


	@classmethod
	def get_dbfactor(cls) -> float:

		"""

		This method returns the value of the dbfactor of an Axis


		Returns
		-------
		float
			Upon success returns a float which represents the dbfactor applied on an axis, when set to db

		"""


	@classmethod
	def get_values_font(cls) -> str:

		"""

		This method is used to get the font used for the values of the axis


		Returns
		-------
		str
			The name of the font of the values of the Axis

		"""


	@classmethod
	def get_title_font(cls) -> str:

		"""

		This method is used to get the font used for the title of the Axis


		Returns
		-------
		str
			The name of the font of the title of the Axis

		"""


	@classmethod
	def get_values_format(cls) -> str:

		"""

		This method is used to get the values format of the axis and has three options: 'vertical', 'horizontal' and '45degrees'


		Returns
		-------
		str
			Upon success returns a string which represents the format of the axis values.

		"""


	@classmethod
	def get_values_precision(cls) -> str:

		"""

		This method returns the precision used for the values of the Axis.Can be 'auto', 'sciauto', 'scientific' and 'fixed'


		Returns
		-------
		str
			Upon success returns the type of precision used for the values of the Axis.

		"""


	@classmethod
	def get_values_position(cls) -> str:

		"""

		This method is used to return the position of the axis, compared to the plot. Can be 'up', 'down' for X axes and 'left', 'right' for Y axes


		Returns
		-------
		str
			Upon success returns a string which represents the position of the axis compared to the plot.

		"""


	@classmethod
	def get_values_align(cls) -> str:

		"""

		This method is used to return the alignment-position of the axis compared to the border of the plot


		Returns
		-------
		str
			Upon success returns a string representing the value of the Axis align

		"""


	@classmethod
	def get_values_color(cls) -> object:

		"""

		This method returns a Color object, the color of the given axis values.


		Returns
		-------
		object
			This method returns a Color object, the color of the given axis values.

		"""


	@classmethod
	def get_radius_locklimits(cls) -> bool:

		"""

		This method returns the state of the radius locklimits flag.


		Returns
		-------
		bool
			Upon success returns True or False, the value of the radius locklimits flag

		"""


	@classmethod
	def get_radius_locksteps(cls) -> bool:

		"""

		This method returns the radius lockstep flag value


		Returns
		-------
		bool
			Upon success returnsTrue or False, the state of the radius lockstep flag

		"""


	@classmethod
	def get_radius_step(cls) -> object:

		"""

		This method returns the value of the radius steps.


		Returns
		-------
		object
			Upon success returns an integer, the value of the radius steps.

		"""


	@classmethod
	def get_radius_dbvalue(cls) -> float:

		"""

		This method returns the value of the dbvalue used for the radius when it is set to db format.


		Returns
		-------
		float
			Upon success returns a float that represents the dbvalue used on radius

		"""


	@classmethod
	def get_radius_dbfactor(cls) -> float:

		"""

		This method returns the value of the dbfactor used for the radius when it is set to db format


		Returns
		-------
		float
			Upon success returns a float which is the value of the dbfactor of the radius.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META PlotAxis entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class PlotModel():

	"""

	Class for plot models.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		class MyPlotModel(plot2d.PlotModel):
		    def __init__(self, pmod, additional_info=""):
		        super(MyPlotModel, self).__init__(pmod.id, pmod.deck, pmod.filename)
		        self.additional_info = additional_info
		
		
		def main():
		    plot_models = plot2d.PlotModels()
		    for pmod in plot_models:
		        print(pmod.id, pmod.deck, pmod.filename)
		        my_pmod = MyPlotModel(pmod, "Some additional info")
		        print(my_pmod.id, my_pmod.deck, my_pmod.filename, my_pmod.additional_info)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot model id.

	"""

	deck: str = None
	"""
	Deck name of the model.

	"""

	filename: str = None
	"""
	Filename of the model.

	"""
class Title():

	"""

	Class for plot title.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    tit = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    if tit:
		        print(tit)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    page = title.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    pl = title.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_text
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    txt = title.get_text()
		    if txt:
		        print(txt)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    w = title.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_align
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    align = "right"
		    align = "center"
		    align = "left"
		    ret = title.set_align(align)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    mycolor = windows.Color(name="0_100_0_0", r=0, g=100, b=0, a=0)
		    ret = title.set_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    font = "DejaVu Sans,11,-1,5,50,2,0,0,0,0"
		    ret = title.set_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    text = "Example"
		    ret = title.set_text(text)
		    print(ret)
		    txt = title.get_text()
		    print(txt)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    title = plot2d.Title(id=0, window_name="Window1", page_id=0)
		    ret = title.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	@classmethod
	def get_text(cls) -> str:

		"""

		This method gets the text of the given PlotTitle.


		Returns
		-------
		str
			Returns the text of the PlotTitle.

		"""


	@classmethod
	def set_text(cls, text: str) -> bool:

		"""

		This method sets the text for the given PlotTitle.


		Parameters
		----------
		text : str
			Text to be set.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_align(cls, align: str) -> bool:

		"""

		This method can be used to set the alignment of a given title.


		Parameters
		----------
		align : str
			Alignment can be:
			-'center'
			-'right'
			-'left'

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_font(cls, font: str) -> bool:

		"""

		This method can be used to set the font of a given title.


		Parameters
		----------
		font : str
			Name of the font to be set as title font.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_color(cls, color: object) -> bool:

		"""

		This method is used to set the color of a given title.


		Parameters
		----------
		color : object
			Color object to be set as title color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	def get_window(self) -> object:

		"""

		This method gets the window of the Title.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Title. Upon failure, it returns None.

		"""


	def get_page(self) -> object:

		"""

		This method gets the page of the Title.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Title. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Title.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Title. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Title entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Footer():

	"""

	Class for plot footer.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    if footer:
		        print(footer.id, footer.window_name, footer.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    page = footer.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    pl = footer.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    w = footer.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_align
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=0, window_name="Window_1", page_id=0)
		    align = "right"
		    align = "center"
		    align = "left"
		    ret = footer.set_align(align)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    mycolor = windows.Color(name="0_100_0_0", r=0, g=100, b=0, a=0)
		    ret = footer.set_color(mycolor)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=1, window_name="Window_1", page_id=0)
		    font = "DejaVu Sans,11,-1,5,50,2,0,0,0,0"
		    ret = footer.set_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_text
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    plot = plot2d.Plot(id=0, window_name="Window_1", page_id=0)
		    footer = plot.get_footer()
		    text = "Example"
		    ret = footer.set_text(text)
		    print(ret)
		    txt = footer.get_text()
		    print(txt)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    footer = plot2d.Footer(id=0, window_name="Window1", page_id=0)
		    ret = footer.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	@classmethod
	def get_text(cls) -> str:

		"""

		This method gets the text of the given PlotFooter.


		Returns
		-------
		str
			Returns the text of the PlotFooter.

		"""


	@classmethod
	def set_text(cls, text: str) -> bool:

		"""

		This method sets the text for the given PlotFooter.


		Parameters
		----------
		text : str
			Text to be set.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_align(cls, align: str) -> bool:

		"""

		This method can be used to set the alignment of a given footer


		Parameters
		----------
		align : str
			Alignment can be:
			-'center'
			-'right'
			-'left'

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_font(cls, font: str) -> bool:

		"""

		This method can be used to set the font of a given footer.


		Parameters
		----------
		font : str
			Name of the font to be set as footer font.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_color(cls, color: object) -> bool:

		"""

		This method is used to set the color of a given Footer.


		Parameters
		----------
		color : object
			Color object to be set as Footer color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Footer.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Footer. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Footer.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Footer. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Footer.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Footer. Upon failure, it returns None.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Footer entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Legend:

	"""

	Class for plot Legend.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    if legend:
		        print(legend.id, legend.window_name, legend.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_bgcolor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    color = legend.get_bgcolor()
		    if color:
		        print(color.r)  # R value
		        print(color.g)  # G value
		        print(color.b)  # B value
		        print(color.a)  # Alpha channel
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    page = legend.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    pl = legend.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_position()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_visible
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_visible()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    w = legend.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attributes_digits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    digits = 3
		    ret = legend.set_attributes_digits(digits)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_attributes_prec
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    type = "fixed"
		    ret = legend.set_attributes_prec(type)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_bgcolor
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    color = windows.Color(name="red", r=0, g=0, b=0, a=0)
		    ret = legend.set_bgcolor(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_border
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    border = 3
		    ret = legend.set_border(border)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    font = "DejaVu Sans,10,-1,5,25,0,0,0,0,0"
		    ret = legend.set_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_framecolor
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    color = windows.Color(name="green", r=0, g=0, b=0, a=0)
		    ret = legend.set_framecolor(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_height
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    height = 400
		    ret = legend.set_height(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_hook
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    hook = "up"
		    ret = legend.set_hook(hook)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_labelscolor
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    color = windows.Color(name="Blue", r=0, g=0, b=0, a=0)
		    ret = legend.set_labelscolor(color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_lockheight
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_lockheight(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_lockwidth
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_lockwidth(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    xpos = 0.5
		    ypos = 0.5
		    ret = legend.set_position(xpos, ypos)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_richtext
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    richtext = "$id $name"
		    ret = legend.set_richtext(richtext)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_show_groups
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_show_groups(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_show_selected
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_show_selected(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_spacing
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    spacing = 2
		    ret = legend.set_spacing(spacing)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_transparent
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_transparent(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_unique_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = legend.set_unique_color(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    width = 200
		    ret = legend.set_width(width)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_width()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_height
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_height()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import os
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot = plot2d.PlotById(window_name, plot_id)
		
		    legend = plot.get_legend()
		
		    legend_settings = {
		        "show": 1,
		        "transparent": 9,
		        "spacing": 4,
		        "hook": "down",
		        "hook": "vcenter",
		        "border": 3,
		        "uniquecolor": 1,
		        "axis": 1,
		        "color": "red",
		        "bgcolor": "gray80",
		        "labelscolor": "black",
		        "framecolor": "black",
		        "font": "Carlito,9,-1,5,50,0,0,0,0,0",
		    }
		    ret = legend.set_settings(legend_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_spacing
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_spacing()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_border
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_border()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_unique_color
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_unique_color()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_transparent
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_transparent()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_framecolor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_framecolor()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_labelscolor
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_labelscolor()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_font()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_richtext
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_richtext()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_hook
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    list = legend.get_hook()
		    for h in list:
		        print(h)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_show_selected
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_show_selected()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_show_groups
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_show_groups()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_lockheight
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_lockheight()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_lockwidth
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_lockwidth()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes_prec
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_attributes_prec()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_attributes_digits
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window_1", page_id=0)
		    ret = legend.get_attributes_digits()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    legend = plot2d.Legend(id=0, window_name="Window1", page_id=0)
		    ret = legend.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	@classmethod
	def get_visible(cls) -> bool:

		"""

		This function gets the visibility of the given legend.


		Returns
		-------
		bool
			Returns True for visible, False for non visible.

		"""


	@classmethod
	def get_position(cls) -> object:

		"""

		This method finds the position of the legend of a given plot.


		Returns
		-------
		object
			Upon success, it returns a list with 2 float elements referring to the position of the legend of the given plot. Else, an empty list is returned.

		"""


	@classmethod
	def show(cls) -> bool:

		"""

		This method sets the visibility of the given legend on.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def hide(cls) -> bool:

		"""

		This method sets the visibility of the given legend off.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_spacing(cls, spacing: int) -> bool:

		"""

		This method sets the spacing of a given legend.


		Parameters
		----------
		spacing : int
			Integer number to be set as legend spacing.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_position(cls, xpos: float, ypos: float) -> bool:

		"""

		This method sets the position of the given legend.


		Parameters
		----------
		xpos : float
			Float number to be set as x position.

		ypos : float
			Float number to be set as y position.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_width(cls, width: int) -> bool:

		"""

		This method sets the width of a given legend.


		Parameters
		----------
		width : int
			Integer to be set as width.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_height(cls, height: int) -> bool:

		"""

		This method is used to set height to a given legend.


		Parameters
		----------
		height : int
			Integer number to be set as height.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_border(cls, border: int) -> bool:

		"""

		This method is used to set the border of a given legend.


		Parameters
		----------
		border : int
			Integer to be set as border.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_unique_color(cls, onoff: bool) -> bool:

		"""

		This method is used to set a unique color to a given legend.


		Parameters
		----------
		onoff : bool
			Boolean to set unique color on or off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_transparent(cls, onoff: bool) -> bool:

		"""

		This method is used to set transparency of a given legend on and off.


		Parameters
		----------
		onoff : bool
			Boolean to set transparency on/off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_bgcolor(cls, color: object) -> bool:

		"""

		This method is used to set the background color of a given Legend.


		Parameters
		----------
		color : object
			Color object to be set as background color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_bgcolor(cls) -> object:

		"""

		This method is used to get the background color of a given legend.


		Returns
		-------
		object
			Returns a color object which is the background color of the legend.

		"""


	@classmethod
	def set_labelscolor(cls, color: object) -> bool:

		"""

		This method is used to set the labels color of a given Legend.


		Parameters
		----------
		color : object
			Color object to be set as labels color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_framecolor(cls, color: object) -> bool:

		"""

		This method is used to set the frame color of a given Legend.


		Parameters
		----------
		color : object
			Color object to be set as frame color.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_font(cls, font: str) -> bool:

		"""

		This method can be used to set the font of a given legend.


		Parameters
		----------
		font : str
			Name of the font to be set as labels font.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_richtext(cls, richtext: str) -> bool:

		"""

		This method can be used to set richtext for the given legend.


		Parameters
		----------
		richtext : str
			String to be used as richtext of the legend.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_hook(cls, hook: str) -> bool:

		"""

		This method can be used to set the anchored position of the legend.


		Parameters
		----------
		hook : str
			String to set the anchored position of the legend:
			-'up' aligned to the upper margin in the plot.
			-'down' aligned to the down margin, in the plot.
			-'left' aligned to the left margin, in the plot
			-'right' aligned to the right margin, inside the plot.
			-'hcenter' positioned at the horizontal center.
			-'vcenter' positioned at the vertical center.
			-'vout' positioned outside the plot vertically.
			-vin' positioned in the plot vertically.
			-'hout' positioned outside the plot horizontally.
			-'hin' positioned in the plot horizontally

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_show_selected(cls, onoff: bool) -> bool:

		"""

		This method can be used to show only the selected curves in the legend.


		Parameters
		----------
		onoff : bool
			Boolean to set the visibility of the selected curves on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_show_groups(cls, onoff: bool) -> bool:

		"""

		This method can be used to show or hide the groups from the legend.


		Parameters
		----------
		onoff : bool
			Boolean to set visibility of groups on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_lockheight(cls, onoff: bool) -> bool:

		"""

		This method can be used to set the height locked and unlocked for the given legend.


		Parameters
		----------
		onoff : bool
			Boolean to set the locking of the height of the legend on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_lockwidth(cls, onoff: bool) -> bool:

		"""

		This method can be used to set the width locked and unlocked for the given legend.


		Parameters
		----------
		onoff : bool
			Boolean to set the locking of the width of the legend on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_attributes_prec(cls, type: str) -> bool:

		"""

		This method is used to set the precision of the given legend attributes.


		Parameters
		----------
		type : str
			String which states the type of precision to be applied:
			-'auto'
			-'scientific'
			-'sciauto'
			-'fixed'
			-'noformat'

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_attributes_digits(cls, digits: int) -> bool:

		"""

		This method can be applied to set the digits of the precision.


		Parameters
		----------
		digits : int
			Integer which will state the number of digits to be applied.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Legend


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Legend. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Legend.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Legend. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Legend.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Legend. Upon failure, it returns None.

		"""


	@classmethod
	def get_width(cls) -> float:

		"""

		This method returns the width of the Legend


		Returns
		-------
		float
			Upon success returns the width of the Legend

		"""


	@classmethod
	def get_height(cls) -> float:

		"""

		This method returns the height of the legend


		Returns
		-------
		float
			Upon success returns the height of the legend.

		"""


	@classmethod
	def set_settings(cls, settings: object) -> bool:

		"""

		This function controls settings of a given Legend


		Parameters
		----------
		settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'spacing' : 4 , 'hook' : 'up , 'transparent' : 1}). The names of the settings and its allowed values are:
			-'spacing' : apply spacing between legend lines
			-'xmove' : move to x coordinate of plot (0-1)
			-'ymove' : move to y coordinate of plot (0-1)
			-'width' : apply width on legend
			-'height' : apply height on legend
			-'border' : apply line width of legend border
			-'uniquecolor' : use unique color or not (0,1)
			-'axis' : show hide assigned axes (0,1)
			-'bgcolor' : apply background color
			-'labelscolor' : apply text color
			-'framecolor' : apply border color
			-'color' : apply color on background and border
			-'font' : apply font used for legend
			-'richtext' : apply richtext to be used for every curve eg 'Curve of ${Entity type} ${Entity id} ${Variable name} $Subcase'
			-'hook' : apply special positions on legend. Options are: 
			 'up' , 'down', 'right', 'left' : position the legend on the prefered side of border
			 'hcenter', 'vcenter': position legend in the horizontal or vertical center
			 'vout', 'vin', 'hout', 'hin': position vertically or horizontally inside or outside the plot
			-'filename' : show filename in legend. options are:
			 'full' show full filename, 'short' show short filename, 'off' filename disabled, 'path' the directory of filename, 'part' part of the directory
			-'onlyid' : show hide only element id (0,1)
			-'groups' : show hide groups of curves in legend (0,1)
			-'showselonly' : show only selected curves or all curves in legend (0,1)
			-'varabbrev' : show obly variable abbreviations (0,1)
			-'lockheight' : lock legend height to current value (0,1)
			-'lockwidth' : lock legend width to current value (0,1)
			-'onlyattribs' : Show only attributes of curves (0,1)
			-'attributes' : Attributes to be applied for every curve in legend, separated by comma e.g. ('Entity id',Variable name','Subcase')
			-'attribprec' : attribute number precision ('auto', 'scientific', 'fixed' , 'sciauto' , 'noformat')
			-'attribdigits' : preferred digits, when precision allows
			-'show' : show hide the legend (0,1)

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_spacing(cls) -> int:

		"""

		This method returns the spacing used for a legend.


		Returns
		-------
		int
			Upon success returns an integer representing the spacing of the Legend.

		"""


	@classmethod
	def get_border(cls) -> int:

		"""

		This method returns the width of the border line of a Legend


		Returns
		-------
		int
			Upon success returns an integer which is the width of the border line of the Legend

		"""


	@classmethod
	def get_unique_color(cls) -> bool:

		"""

		This method returns the option for the use of unique color of the legend.


		Returns
		-------
		bool
			Upon success returns True if the unique color flag is enabled or False if it is disabled.

		"""


	@classmethod
	def get_transparent(cls) -> bool:

		"""

		This method returns the value of the transparent flag of a Legend.


		Returns
		-------
		bool
			Returns True or False value of the transparent flag.

		"""


	@classmethod
	def get_framecolor(cls) -> object:

		"""

		This method returns the color of the legend frame.


		Returns
		-------
		object
			Returns a color object which is the frame color of the legend.

		"""


	@classmethod
	def get_labelscolor(cls):

		"""

		This method returns the color used for the labels of the legend.


		"""


	@classmethod
	def get_font(cls) -> str:

		"""

		This method is used to get the font used for the legend


		Returns
		-------
		str
			The name of the font of the Legend

		"""


	@classmethod
	def get_richtext(cls) -> str:

		"""

		This method is used to get the richtext of the Legend, i.e. the pattern used to describe the curve in the Legend.


		Returns
		-------
		str
			Upon success returns a string that represents the richtext

		"""


	@classmethod
	def get_hook(cls) -> object:

		"""

		This method returns a List with the hook options of a Legend.


		Returns
		-------
		object
			Upon success returns a list containing strings describing the hook options of the Legend

		"""


	@classmethod
	def get_show_selected(cls) -> bool:

		"""

		This method is used to return the value of the show selected option of a Legend


		Returns
		-------
		bool
			Upon success returns True or False, the value of the show selected flag.

		"""


	@classmethod
	def get_show_groups(cls) -> bool:

		"""

		This method is used to return the value of the show groups option of a Legend


		Returns
		-------
		bool
			Upon success returns True or False, the value of the show groups flag.

		"""


	@classmethod
	def get_lockheight(cls) -> bool:

		"""

		This method is used to return the value of the lockheight option of a Legend


		Returns
		-------
		bool
			Upon success returns True or False the value of the lockheight flag.

		"""


	@classmethod
	def get_lockwidth(cls) -> bool:

		"""

		This method is used to return the value of the lockwidth option of a Legend


		Returns
		-------
		bool
			Upon success returns True or False, the value of the lockwidth flag.

		"""


	@classmethod
	def get_attributes_prec(cls) -> str:

		"""

		This method is used to get the attributes precision format used in the Legend.


		Returns
		-------
		str
			Upon success returns a string representing the attributes format of the Legend.

		"""


	@classmethod
	def get_attributes_digits(cls) -> int:

		"""

		This method is used to return the value of the attributes digits used for a Legend


		Returns
		-------
		int
			Upon success returns an integer which is the value of the attributes digits.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Legend entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Fringe:

	"""

	Class for plot Fringe.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    if fringe:
		        print(fringe.id, fringe.window_name, fringe.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: data_format
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    specifier = "magn"
		    # specifier ='phase'
		    # specifier ='altphase'
		    # specifier ='real'
		    # specifier ='imag'
		    # specifier ='rmsmagn'
		    # specifier ='radphase'
		    # specifier ='altradphase'
		    ret = fringe.data_format(specifier)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    page = fringe.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    w = fringe.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: hide
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.hide()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.show()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_border
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = fringe.set_border(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    font = "DejaVu Sans,10,-1,5,25,0,0,0,0,0"
		    ret = fringe.set_font(font)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_height
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    height = 200
		    ret = fringe.set_height(height)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_hook
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    hook = "left"
		    ret = fringe.set_hook(hook)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_limit
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    specifier = "min"
		    # specifier = 'max'
		    limit = 200
		    ret = fringe.set_limit(specifier, limit)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    xpos = 0.5
		    ypos = 0.5
		    ret = fringe.set_position(xpos, ypos)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    title = "new title"
		    ret = fringe.set_title(title)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    width = 200
		    ret = fringe.set_width(width)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: show_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    onoff = True
		    ret = fringe.show_title(onoff)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_hook
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_hook()
		    for h in ret:
		        print(h)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_position()
		    for h in ret:
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_width()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_height
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_height()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_font
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_font()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_border
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_border()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_title()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_show_title
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_show_title()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_limit
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		    ret = fringe.get_limit()
		    for h in ret:
		        print(h)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_data_format
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window_1", page_id=0)
		
		    ret = fringe.get_data_format()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    fringe = plot2d.Fringe(id=0, window_name="Window1", page_id=0)
		    ret = fringe.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	@classmethod
	def show(cls) -> bool:

		"""

		This method sets the visibility of the given fringe on.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def hide(cls) -> bool:

		"""

		This method sets the visibility of the given fringe off.


		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_hook(cls, hook: str) -> bool:

		"""

		This method can be used to set the anchored position of the fringe.


		Parameters
		----------
		hook : str
			String to set the anchored position of the fringe:
			-'up' aligned to the upper margin in the plot.
			-'down' aligned to the down margin, in the plot.
			-'left' aligned to the left margin, in the plot
			-'right' aligned to the right margin, inside the plot.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_position(cls, xpos: float, ypos: float) -> bool:

		"""

		This method sets the position of the given fringe.


		Parameters
		----------
		xpos : float
			Float number to be set as x position.

		ypos : float
			Float number to be set as y position.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_width(cls, width: int) -> bool:

		"""

		This method sets the width of a given fringe.


		Parameters
		----------
		width : int
			Integer to be set as width.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_height(cls, height: int) -> bool:

		"""

		This method is used to set height to a given fringe.


		Parameters
		----------
		height : int
			Integer number to be set as height.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_font(cls, font: str) -> bool:

		"""

		This method can be used to set the font of a given fringe.


		Parameters
		----------
		font : str
			Name of the font.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_border(cls, onoff: bool) -> bool:

		"""

		This method is used to set the border of a given fringe.


		Parameters
		----------
		onoff : bool
			Boolean to set border on and off.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_title(cls, title: str) -> bool:

		"""

		This method can be used to change the title of the given fringe.


		Parameters
		----------
		title : str
			String to be set as the title.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def show_title(cls, onoff: bool) -> bool:

		"""

		This method can be used to show or hide the given fringe title.


		Parameters
		----------
		onoff : bool
			Boolean to show/hide the fringe title.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_limit(cls, specifier: str, limit: float) -> bool:

		"""

		This method can be used to set the minimum or maximum value of the given fringe.


		Parameters
		----------
		specifier : str
			Can have two values:
			-'min'
			-'max'

		limit : float
			Float to be used as the min or max limit of the fringe.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def data_format(cls, specifier: str) -> bool:

		"""

		This method can be used to change the Data format of the given fringe.


		Parameters
		----------
		specifier : str
			This string describes the format of the data of the fringe:
			-'magn' use magnitude values
			-'phase' use phase values
			-'altphase' use -180 to 180 limits
			-'real' use real values
			-'imag' use imag values 
			-'rmsmagn' use rms values
			-'radphase' use 0 to 2pi limits
			-'altradphase' use -p to p limits

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Fringe.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Fringe. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Fringe.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Fringe. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Fringe.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Fringe. Upon failure, it returns None.

		"""


	@classmethod
	def get_hook(cls) -> object:

		"""

		This method returns a List with the hook options of a Fringe.


		Returns
		-------
		object
			Upon success returns a list containing strings describing the hook options of the Fringe

		"""


	@classmethod
	def get_position(cls) -> object:

		"""

		This method finds the position of the fringe of a given plot.


		Returns
		-------
		object
			Upon success, it returns a list with 2 float elements referring to the position of the fringe of the given plot. Else, an empty list is returned.

		"""


	@classmethod
	def get_width(cls) -> float:

		"""

		This method returns the width of the Fringe


		Returns
		-------
		float
			Upon success returns the width of the Fringe

		"""


	@classmethod
	def get_height(cls) -> float:

		"""

		This method returns the height of the Fringe


		Returns
		-------
		float
			Upon success returns the height of the Fringe

		"""


	@classmethod
	def get_font(cls) -> str:

		"""

		This method is used to get the font used for the Fringe


		Returns
		-------
		str
			The string of the font of the Fringe

		"""


	@classmethod
	def get_border(cls) -> bool:

		"""

		This method returns the existance of the border line of a Fringe


		Returns
		-------
		bool
			Upon success it returns True or False if the border is on or off.

		"""


	@classmethod
	def get_title(cls) -> str:

		"""

		This method returns the title of the Fringe


		Returns
		-------
		str
			Upon success returns a string representing the title of the Fringe.

		"""


	@classmethod
	def get_show_title(cls) -> bool:

		"""

		This method returns True if fringe title is visible and False if not.


		Returns
		-------
		bool
			Upon success returns True or False if the Fringe title is visible or not.

		"""


	@classmethod
	def get_limit(cls) -> object:

		"""

		This method returns a list containing two floats that represent the min and max values of the fringe.


		Returns
		-------
		object
			Upon success returns a list of two floats, else an empty list.

		"""


	@classmethod
	def get_data_format(cls) -> str:

		"""

		This method returns the type of data shown on the Fringe.


		Returns
		-------
		str
			Upon success returns a string that represents the type of data of the Fringe. Can be 'magn', 'phase', 'altphase', 'real', 'imag', 'rmsmagn', 'radphase', 'altradphase'

		"""


	def is_usable(self) -> bool:

		"""


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

class Grid:

	"""

	Class for plot Grid.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    if grid:
		        print(grid.id, grid.window_name, grid.page_id)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_page
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    page = grid.get_page()
		    if page:
		        print(page.id, page.name, page.active)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plot
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    pl = grid.get_plot()
		    if pl:
		        print(pl.id, pl.window_name, pl.page_id, pl.active, pl.type)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_window
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    w = grid.get_window()
		    if w:
		        print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_density
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    specifier = "x"
		    # specifier = 'y'
		    ret = grid.set_density(specifier, value=3)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_color
		# PYTHON script
		import meta
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    blue = windows.Color(name="blue", r=0, g=0, b=0, a=0)
		    red = windows.Color(name="red", r=0, g=0, b=0, a=0)
		    specifier = "major"
		    color = blue
		    ret = grid.set_line_color(specifier, color)
		    print(ret)
		    specifier = "minor"
		    color = red
		    ret = grid.set_line_color(specifier, color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_line_style
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    specifier = "major"
		    specifier = "minor"
		    color = windows.Color(r=255, g=255, b=0, a=255)
		    ret = grid.set_line_style(specifier, color)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_tick_length
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    specifier = "major"
		    specifier = "minor"
		    value = 15
		    ret = grid.set_tick_length(specifier, value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_tick_position
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    specifier = "major"
		    # specifier = 'minor'
		    position = "center"
		    # position = 'internal'
		    # position = 'external'
		    ret = grid.set_tick_position(specifier, position)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_tick_width
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window_1", page_id=0)
		    specifier = "major"
		    # specifier = 'minor'
		    value = 5
		    ret = grid.set_tick_width(specifier, value)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()
		# method: set_settings
		# PYTHON script
		import os
		import meta
		from meta import plot2d
		
		
		def main():
		    window_name = "Window1"
		    plot_id = 0
		    plot = plot2d.PlotById(window_name, plot_id)
		    grid = plot.get_grid()
		    grid_settings = {
		        "minor_style": "continuous",
		        "major_style": "dot1",
		        "minor_color": "gray80",
		        "major_color": "red",
		        "major_tick_width": 3,
		        "minor_tick_width": 4,
		        "minor_tick_length": 10,
		        "major_tick_length": 10,
		        "minor_tick_position": "center",
		        "major_tick_position": "external",
		        "minor_xdens": 5,
		        "minor_ydens": 2,
		    }
		    grid.set_settings(grid_settings)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import plot2d
		
		
		def main():
		    grid = plot2d.Grid(id=0, window_name="Window1", page_id=0)
		    ret = grid.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	Plot id.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	page_id: int = None
	"""
	Id of the page of the plot.

	"""

	@classmethod
	def set_density(cls, specifier: str) -> object:

		"""

		This method can be used to set the x or y axis density of gridlines of a given grid.


		Parameters
		----------
		specifier : str
			-'x' for x axis gridlines.
			-'y' for y axis gridlines.

		Returns
		-------
		object
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_line_style(cls, specifier: str, value: int) -> bool:

		"""

		This method can be used to set major or minor gridlines style of a given grid.


		Parameters
		----------
		specifier : str
			-'major' for major gridlines
			-'minor' for minor gridlines

		value : int
			Integer number that will be set as line style.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_line_color(cls, specifier: str, color: object) -> bool:

		"""

		This method can be used to set major or minor gridlines color of a given grid.


		Parameters
		----------
		specifier : str
			-'major' for major gridlines
			-'minor' for minor gridlines

		color : object
			Color object that will be set.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_tick_width(cls, specifier: str, value: int) -> bool:

		"""

		This method can be used to set major or minor ticks width of a given grid.


		Parameters
		----------
		specifier : str
			-'major' for major gridlines
			-'minor' for minor gridlines

		value : int
			Integer number that will be set as tick width.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_tick_length(cls, specifier: str, value: int) -> bool:

		"""

		This method can be used to set the tick length of a given grid.


		Parameters
		----------
		specifier : str
			-'major' for major gridlines
			-'minor' for minor gridlines

		value : int
			Integer number that will be set as tick length.

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def set_tick_position(cls, specifier: str, position: str) -> bool:

		"""

		This method can be used to set the ticks position of a given grid.


		Parameters
		----------
		specifier : str
			-'major' for major gridlines
			-'minor' for minor gridlines

		position : str
			-'center'
			-'internal'
			-'external'

		Returns
		-------
		bool
			It returns true upon success or false upon failure.

		"""


	@classmethod
	def get_window(cls) -> object:

		"""

		This method gets the window of the Grid.


		Returns
		-------
		object
			Upon success, it returns an object of type Window referring to the window of the Grid. Upon failure, it returns None.

		"""


	@classmethod
	def get_page(cls) -> object:

		"""

		This method gets the page of the Grid.


		Returns
		-------
		object
			Upon success, it returns an object of type Page referring to the page of the Grid. Upon failure, it returns None.

		"""


	@classmethod
	def get_plot(cls) -> object:

		"""

		This method gets the plot of the Grid.


		Returns
		-------
		object
			Upon success, it returns an object of type Plot referring to the plot of the Grid. Upon failure, it returns None.

		"""


	@classmethod
	def set_settings(cls, settings: object) -> object:

		"""

		This function controls settings of a given Grid


		Parameters
		----------
		settings : object
			A dictionary which contains name and value of each setting separated by colon , different settings separated by commas (e.g. {'major_style' : 4 , 'minor_tick_position' : 'center}). The names of the settings and its allowed values are:
			-'major_style' : Apply a line style for major grid lines ('continuous', 'dot1', 'dot2', 'dash1', 'dash2')
			-'minor_style' : Apply a line style for minor grid lines ('continuous', 'dot1', 'dot2', 'dash1', 'dash2')
			-'major_color' : Apply a color for major grid lines
			-'minor_color' : Apply a color for minor grid lines
			-'minor_tick_width' : Apply width for minor tick lines
			-'major_tick_width' : Apply width for major tick lines
			-'minor_tick_length' : Apply length for minor tick lines
			-'major_tick_length' : Apply length for major tick lines
			-'minor_tick_position' : Set position for minor ticks ('center', 'internal', 'external')
			-'major_tick_position' : Set position for major ticks ('center', 'internal', 'external')
			-'minor_xdens' : Set density for x axis minor grids
			-'minor_ydens' : Set density for y axis minor grids

		Returns
		-------
		object
			It returns true upon success or false upon failure.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Grid entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

