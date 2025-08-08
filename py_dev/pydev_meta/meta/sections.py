from __future__ import annotations
from typing import *

def Sections(model_id: int) -> object:

	"""

	This function collects all sections of the model specified by the given id.

	Parameters
	----------
	model_id : int
		Id of the model.

	Returns
	-------
	object
		It returns a list where each member of the list is an object of class Section referring to one specific section of the model.
		Upon failure, an empty list is returned.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetSectionByName(model_id: int, sec_name: str) -> object:

	"""

	This function finds the section of a model with a given name.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name

	Returns
	-------
	object
		It returns an object of class Section.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		
		    name = "section_name"
		    section = sections.GetSectionByName(model_id, name)
		    print(section)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ElementsOfSection(model_id: int, sec_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_elements` instead.


	This function collects all elements of a given section belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name.

	Returns
	-------
	object
		It returns a list where each member is an object of class Element referring to one specific element.
		Upon failure, an empty list is returned.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		
		        elem_list = sections.ElementsOfSection(model_id, se.name)
		        for e in elem_list:
		            print(e)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_elements instead.", DeprecationWarning)

def NodesOfSection(model_id: int, sec_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_nodes` instead.


	This function collects all nodes of a given section belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name.

	Returns
	-------
	object
		It returns a list where each member is an object of class Node referring to one specific node.
		Upon failure, an empty list is returned.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		
		        node_list = sections.NodesOfSection(model_id, se.name)
		        for n in node_list:
		            print(n)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_nodes instead.", DeprecationWarning)

def ResultsetsOfSection(model_id: int, sec_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_resultsets` instead.


	This function collects all the resultsets of a given section belonging to the specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name.

	Returns
	-------
	object
		It returns a list where each member is an object of class Resultset referring to one specific resultset.
		Upon failure, an empty list is returned.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		
		        res_list = sections.ResultsetsOfSection(model_id, se.name)
		        for r in res_list:
		            print(r)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_resultsets instead.", DeprecationWarning)

def GetForceMomentOfSection(model_id: int, sec_name: str, result: object, view_mode: str, summation_mode: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_force_moment` instead.


	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name.

	result : object
		An object of class Result that refers to a Resultset of the model.

	view_mode : str
		Accepted values:
		total, current, node

	summation_mode : str
		Accepted values: 
		freebody, internal, paminternal, external, applied, contact, contanormal, contafrictional, reaction, mixed, mpc.

	Returns
	-------
	object
		When view_mode is total or node returns a list, that has as first element a list with the forces and as a second, a list with the moments.
		When view_mode is current, the function returns a list that contains the forces and moments of every node. Every Element of this list, is a list, that has as first element the node id, as second a list with the forces in this node, and as third a list with the moments in this node

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		
		        res_list = sections.ResultsetsOfSection(model_id, se.name)
		        for r in res_list:
		            print(r)
		            force_list = sections.GetForceMomentOfSection(
		                model_id, se.name, r, "total", "external"
		            )
		            print(force_list)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_force_moment instead.", DeprecationWarning)

def GetIdOfWatchNode(model_id: int, sec_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_watch_node` instead.


	This returns the id of the watch node.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section name.

	Returns
	-------
	int
		Returns the id of the watch node.
		Upon failure, returns -1

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		        id = sections.GetIdOfWatchNode(model_id, se.name)
		        print(id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_watch_node instead.", DeprecationWarning)

def PlaneOfSection(model_id: int, sec_name: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.sections.Section.get_plane` instead.


	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : int
		Section name.

	Returns
	-------
	object
		Upon success, it returns a plane object with the plane that created this section
		Else, a non valid plane object is returned.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    all_sections = sections.Sections(model_id)
		
		    for se in all_sections:
		        print(se.name)
		        plane = sections.PlaneOfSection(model_id, se.name)
		        print(plane)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.sections.Section.get_plane instead.", DeprecationWarning)

def ReadResultsOfSection(model_id: int, deck: str, file: str, states: str) -> object:

	"""

	Read Results for section forces for a specific model from specified model.

	Parameters
	----------
	model_id : int
		Id of the model.

	deck : str
		Name of the deck.

	file : str
		The file with the results

	states : str
		Range of states that will be read.

	Returns
	-------
	object
		Returns a list with all resultsets of sections for the given model

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    file = "dyna_section_results_file"
		    deck = "Dyna3d"
		    states = "all"
		    read = sections.ReadResultsOfSection(model_id, deck, file, states)
		
		    if len(read) > 0:
		        for re in read:
		            print(re)
		    else:
		        print(read)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateSectionFromVisible(model_id: int, sec_name: str) -> object:

	"""

	Creates a section from the visible entities

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section Name

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    sec_name = "from_vis"
		    se = sections.CreateSectionFromVisible(model_id, sec_name)
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateSectionFromIdentified(model_id: int, sec_name: str) -> object:

	"""

	Creates a section from the identified entities

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section Name

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    sec_name = "from_ide"
		    se = sections.CreateSectionFromIdentified(model_id, sec_name)
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateSectionFromPart(model_id: int, part_id: int) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.parts.Part.create_section` instead.


	Creates a section from the specified part

	Parameters
	----------
	model_id : int
		Id of the model.

	part_id : int
		Id of the part.

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    part_id = 30
		    se = sections.CreateSectionFromPart(model_id, part_id)
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.parts.Part.create_section instead.", DeprecationWarning)

def CreateSectionFromGroup(model_id: int, group_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.groups.Group.create_section` instead.


	Creates a section from the specified group

	Parameters
	----------
	model_id : int
		Id of the model.

	group_name : str
		Name of the group.

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    group_name = "my_group"
		    se = sections.CreateSectionFromGroup(model_id, group_name)
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.groups.Group.create_section instead.", DeprecationWarning)

def CreateSectionFromPlane(model_id: str, plane_name: str) -> object:

	"""
	.. deprecated:: 20.1.0
		Use `meta.planes.Plane.create_section` instead.


	Creates a section from the specified plane

	Parameters
	----------
	model_id : str
		Id of the model.

	plane_name : str
		Name of the group.

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    plane_name = "my_plane"
		    se = sections.CreateSectionFromPlane(model_id, plane_name)
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

	import warnings; warnings.warn("Deprecated since version 20.1.0. Use  meta.planes.Plane.create_section instead.", DeprecationWarning)

def AdvFiltersOnCreateSection(model_id: int, sec_name: str, filter_entities: str, adv_filters: object) -> object:

	"""

	This function allows the user to collect entities of a model specified by its id through some advanced filters and create a section with these entities.

	Parameters
	----------
	model_id : int
		Id of the model.

	sec_name : str
		Section Name.

	filter_entities : str
		Argument 'filter_entities' is a string which refers to the type of the entities. Its possible values are:
		- 'elements'
		- 'nodes'

	adv_filters : object
		Contains the advanced filters as a list of string expressions. Their syntax is the same with the commands referring to advanced filters.

	Returns
	-------
	object
		It returns an object of class Section, if creation was successful, otherwise None.

	See Also
	--------
	sections.Section

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    model_id = 0
		    sec_name = "elem_sec"
		    filter_entities = "elements"
		    adv_filters = [
		        "add:Elements:all::Keep All",
		        "intersect:Elements:id.range:20000-20500:Keep All",
		    ]
		
		    se = sections.AdvFiltersOnCreateSection(
		        model_id, sec_name, filter_entities, adv_filters
		    )
		    print(se)
		
		    sec_name = "node_sec"
		    filter_entities = "nodes"
		    adv_filters = ["add:Nodes:id.range:23000-23500:Keep All"]
		
		    se = sections.AdvFiltersOnCreateSection(
		        model_id, sec_name, filter_entities, adv_filters
		    )
		    print(se)
		
		
		if __name__ == "__main__":
		    main()


	"""

class Section():

	"""

	Class for sections

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    print(sec)
		    print(sec.name, sec.creation_type, sec.sum_point, sec.coord_system)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_elements
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    elems = sec.get_elements()
		    for elem in elems:
		        print(elem)
		        print(
		            elem.id,
		            elem.second_id,
		            elem.model_id,
		            elem.type,
		            elem.subtype,
		            elem.visible,
		            elem.part_id,
		        )
		
		
		if __name__ == "__main__":
		    main()
		# method: get_nodes
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    section_nodes = sec.get_nodes()
		    for n in section_nodes:
		        print(n)
		        print(n.id, n.model_id, n.x, n.y, n.z, n.visible)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_resultsets
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    section_resultsets = sec.get_resultsets()
		    for res in section_resultsets:
		        print(res)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_plane
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    pl = sec.get_plane()
		    print(pl)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_watch_node
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    n = sec.get_watch_node()
		    if n:
		        print(n)
		        print(n.id, n.model_id, n.x, n.y, n.z, n.visible)
		
		
		if __name__ == "__main__":
		    main()
		# method: get_force_moment
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    name = "section1"
		    model_id = 0
		    sec = sections.Section(name, model_id)
		    res_list = sections.ResultsetsOfSection(model_id, se.name)
		    for res in res_list:
		        force_list = sec.get_force_moment(res, "total", "external")
		        print(force_list)
		
		
		if __name__ == "__main__":
		    main()
		# method: is_usable
		# PYTHON script
		import meta
		from meta import sections
		
		
		def main():
		    sec = sections.Section(name="section1", model_id=0)
		    ret = sec.is_usable()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Section name

	"""

	creation_type: str = None

	sum_point: object = None
	"""
	A list with the x,y,z coordinates of the summation point

	"""

	coord_system: int = None
	"""
	Coordinate system of section. If the coordinate system is the global, then this variable will be -1

	"""

	def get_elements(self) -> object:

		"""

		This method gets the elements of the section. 


		Returns
		-------
		object
			Upon success, it returns a list where each member is an object of type Element referring to one specific element of the section. Upon failure, an empty list is returned.

		"""


	def get_nodes(self) -> object:

		"""

		This method gets the nodes of the section. 


		Returns
		-------
		object
			Upon success, it returns a list where each member is an object of type Node referring to one specific node of the section. Upon failure, an empty list is returned.

		"""


	def get_resultsets(self) -> object:

		"""

		This method gets the resultsets of the section. 


		Returns
		-------
		object
			Upon success, it returns a list where each member is an object of type Resultset referring to one specific resultset of the section. Upon failure, an empty list is returned.

		"""


	def get_plane(self) -> object:

		"""

		This method gets the plane of the section. 


		Returns
		-------
		object
			Upon success, it returns an object of type Plane referring to the plane which was used to create the section. Upon failure, it returns None.

		"""


	def get_watch_node(self) -> object:

		"""

		This method gets the watch node of the section. 


		Returns
		-------
		object
			Upon success, it returns an object of type Node referring to the watch node of the section. Upon failure, it returns None.

		"""


	def get_force_moment(self, resultset: object, view_mode: str, summation_mode: str) -> object:

		"""

		This method gets the force and the moment of the section. 


		Parameters
		----------
		resultset : object
			An object of class Result that refers to a Resultset of the model.

		view_mode : str
			The view mode. Accepted values are:
			'total', 'current' and 'node'.

		summation_mode : str
			The summation mode. Accepted values are:
			'freebody',
			'internal',
			'paminternal',
			'external',
			'applied',
			'contact',
			'contanormal',
			'contafrictional',
			'reaction',
			'mixed',
			'mpc'

		Returns
		-------
		object
			Upon success, if view_mode is 'total' or 'node', it returns a list which has as first element a list with the forces and as a second a list with the moments. If view_mode is 'current', the function returns a list that contains the forces and moments of every node. Every Element of this list, is a list, that has as first element the node id, as second a list with the forces in this node, and as third a list with the moments in this node. Upon failure, it returns an empty list.

		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Section entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		"""

