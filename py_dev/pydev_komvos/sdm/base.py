from __future__ import annotations
from typing import *
from . import utils

def GetDMRoot() -> str:

	"""

	Returns the path that currently points to DM.

	Returns
	-------
	str
		The function returns a string containing the current DM root.
		A string of length 0 is returned if no DM path is currently set.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    dm_root = base.GetDMRoot()
		    print(dm_root)


	"""

def NewPTInstance(tree: object, child_identifier: Any, part_identifier: Any, parent_identifier: Any, position_matrix: object, instance_attributes: object) -> int:

	"""

	Defines a new Product Tree Instance in the created product tree element.

	Parameters
	----------
	tree : object
		The object returned from a previous call to 'NewProductTree' 
		function.

	child_identifier : Any
		(string/integer) A unique id that will be used only internally from 
		the function for the interpretation of "parent-child" relationships
		(i.e. part in group, group in group)

	part_identifier : Any
		(string/integer) The part_identifier must be equal to the unique 
		part_identifier of the master part.

	parent_identifier : Any
		(string/integer) The parent identifier must be equal to the unique 
		child_identifier of the parent (as declared in NewPTInstance). 
		It is used internally for the interpretation of "parent-child"relationships 
		(i.e. part in group, group in group). If the instance is in the root of the 
		hierarchy (top-level item) then the parent identifier will be None.

	position_matrix : object
		It is the relative 4x3 transformation list that will be assigned to 
		the part/group.

	instance_attributes : object, optional
		The instance_attributes list can contain any other information 
		regarding the part instance like target mass, mesh type etc.
		The list contains other lists which specify the name and the value of 
		each attribute e.g. 
		instance_attributes[0] = ["TARGET MASS","5"]
		instance_attributes[1] = ["MESH TYPE","coarse"]

	Returns
	-------
	int
		Returns 0 on success and -1 on failure.

	See Also
	--------
	base.InputModelDefinition

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    # Create the product tree
		    tree = base.NewProductTree()
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # no parent for the top level group
		    child_identifier = 1
		    base.NewPTPart(tree, "group", "MID A", "Version A", "Top Level Group")
		    base.NewPTInstance(
		        tree, child_identifier, "group", parent_identifier, pos_matrix_group
		    )
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = child_identifier  # the part belongs to the previous group
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "1.5"]]
		    part_file_attr = [
		        ["PID", 1000],
		        ["Property Name", "Front Part"],
		        ["Material", "ES200"],
		    ]
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "Part MI", part_attr)
		    inst_attr = [["Position", "Left"]]
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part, inst_attr
		    )
		    base.NewPTModel(tree, "part1", "/home/demo/FrontPart.CATPart", part_file_attr)
		
		    # Create an instance to the previously created part
		    pos_matrix_instance = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
		    inst_attr = [["Position", "Right"]]
		    child_identifier += 1
		    base.NewPTInstance(
		        tree,
		        child_identifier,
		        "part1",
		        parent_identifier,
		        pos_matrix_instance,
		        inst_attr,
		    )
		    # Add a PID offset of 100 to the new instance
		    base.SetPTInstancePidOffset(tree, child_identifier, 100)
		
		    # Create a new tailorblanked part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "3.4"]]
		    part_file_attr = [
		        ["PID", 2000],
		        ["Property Name", "Front TB Part"],
		        ["Material", "ES220"],
		    ]
		    base.NewPTPart(tree, "part2", "MID 2", "Version AB", "Part TB", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part2", parent_identifier, pos_matrix_part
		    )
		    # Add the first CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/FrontTBPart.CATPart", part_file_attr)
		
		    part_file_attr = [
		        ["PID", 2001],
		        ["Property Name", "Rear TB Part"],
		        ["Material", "ES200"],
		    ]
		    # Add the second CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/RearTBPart.CATPart", part_file_attr)
		
		    # Launch the editor.
		    my_settings = base.InputProductTreeSettings()
		    my_settings.should_open_window = True
		    base.InputModelDefinition(product_tree=tree, settings=my_settings)


	"""

def NewPTModel(tree: object, part_identifier: Any, cad_file: str, part_file_attributes: object, part_file_position_matrix: object) -> int:

	"""

	Adds CAD or other file references to an existing Product Tree Part.

	Parameters
	----------
	tree : object
		It is the element returned from a previous call to 'NewProductTree' 
		function.

	part_identifier : Any
		(string/integer) The unique part_identifier of the part/group that 
		references the CAD files (as declared in NewPTPart).

	cad_file : str
		The filename of the CAD.

	part_file_attributes : object, optional
		The part_file_attributes list can contain any other information
		regarding the part file attributes like property id, material id etc.
		The list contains other lists which specify the name and the value of
		each attribute e.g. 
		part_file_attributes[0] = ["PID","5"]
		part_file_attributes[1] = ["MID","50"]
		If no part_file_attributes are given, then a zero value can be
		assigned.

	part_file_position_matrix : object, optional
		Exported in the download list in order to be used for the application
		of a geometric transformation on the referenced file (e.g CAD file
		during translation). This list is different than the one defined in
		NewPTInstance since the latter is passed automatically to the ANSAPART
		created upon confirmation.

	Returns
	-------
	int
		Returns 0 on success and -1 on failure.

	See Also
	--------
	base.InputModelDefinition

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    # Create the product tree
		    tree = base.NewProductTree()
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # no parent for the top level group
		    child_identifier = 1
		    base.NewPTPart(tree, "group", "MID A", "Version A", "Top Level Group")
		    base.NewPTInstance(
		        tree, child_identifier, "group", parent_identifier, pos_matrix_group
		    )
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = child_identifier  # the part belongs to the previous group
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "1.5"]]
		    part_file_attr = [
		        ["PID", 1000],
		        ["Property Name", "Front Part"],
		        ["Material", "ES200"],
		    ]
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "Part MI", part_attr)
		    inst_attr = [["Position", "Left"]]
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part, inst_attr
		    )
		    base.NewPTModel(tree, "part1", "/home/demo/FrontPart.CATPart", part_file_attr)
		
		    # Create an instance to the previously created part
		    pos_matrix_instance = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
		    inst_attr = [["Position", "Right"]]
		    child_identifier += 1
		    base.NewPTInstance(
		        tree,
		        child_identifier,
		        "part1",
		        parent_identifier,
		        pos_matrix_instance,
		        inst_attr,
		    )
		    # Add a PID offset of 100 to the new instance
		    base.SetPTInstancePidOffset(tree, child_identifier, 100)
		
		    # Create a new tailorblanked part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "3.4"]]
		    part_file_attr = [
		        ["PID", 2000],
		        ["Property Name", "Front TB Part"],
		        ["Material", "ES220"],
		    ]
		    base.NewPTPart(tree, "part2", "MID 2", "Version AB", "Part TB", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part2", parent_identifier, pos_matrix_part
		    )
		    # Add the first CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/FrontTBPart.CATPart", part_file_attr)
		
		    part_file_attr = [
		        ["PID", 2001],
		        ["Property Name", "Rear TB Part"],
		        ["Material", "ES200"],
		    ]
		    # Add the second CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/RearTBPart.CATPart", part_file_attr)
		
		    # Launch the editor.
		    my_settings = base.InputProductTreeSettings()
		    my_settings.should_open_window = True
		    base.InputModelDefinition(product_tree=tree, settings=my_settings)


	"""

def NewPTPart(tree: object, part_identifier: Any, module_id: str, version: str, name: str, part_attributes: object, is_group: bool) -> int:

	"""

	Defines a new Product Tree Part in the created product tree.

	Parameters
	----------
	tree : object
		It is the element returned from a previous call to 'NewProductTree' 
		function.

	part_identifier : Any
		(string/integer) The part_identifier is a unique id that characterizes a product 
		tree structure item. This unique id will be later used for the 
		generation of "parent-child"relationships 
		(i.e. part in group, group in group) and the creation of multiple 
		instances (through NewPTInstance) and the addition of file 
		references(through NewPTModel).

	module_id : str
		The string that will correspond to the module id of the group/part

	version : str
		The string that will correspond to the version of the group/part.

	name : str
		The string that will correspond to the name of the group/part.

	part_attributes : object, optional
		The part_attributes list can contain any other information 
		regarding the part like target mass, mesh type etc.The list
		contains other lists which specify the name and the value of 
		each attribute e.g.
		part_attributes[0] = ["TARGET MASS","5"]
		part_attributes[1] = ["MESH TYPE","coarse"]

	is_group : bool, optional
		Flag that determines whether the created item is a part or a group. Default value is False.

	Returns
	-------
	int
		Returns 0 on success and -1 on failure.

	See Also
	--------
	base.InputModelDefinition

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    # Create the product tree
		    tree = base.NewProductTree()
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # no parent for the top level group
		    child_identifier = 1
		    base.NewPTPart(tree, "group", "MID A", "Version A", "Top Level Group")
		    base.NewPTInstance(
		        tree, child_identifier, "group", parent_identifier, pos_matrix_group
		    )
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = child_identifier  # the part belongs to the previous group
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "1.5"]]
		    part_file_attr = [
		        ["PID", 1000],
		        ["Property Name", "Front Part"],
		        ["Material", "ES200"],
		    ]
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "Part MI", part_attr)
		    inst_attr = [["Position", "Left"]]
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part, inst_attr
		    )
		    base.NewPTModel(tree, "part1", "/home/demo/FrontPart.CATPart", part_file_attr)
		
		    # Create an instance to the previously created part
		    pos_matrix_instance = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
		    inst_attr = [["Position", "Right"]]
		    child_identifier += 1
		    base.NewPTInstance(
		        tree,
		        child_identifier,
		        "part1",
		        parent_identifier,
		        pos_matrix_instance,
		        inst_attr,
		    )
		    # Add a PID offset of 100 to the new instance
		    base.SetPTInstancePidOffset(tree, child_identifier, 100)
		
		    # Create a new tailorblanked part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "3.4"]]
		    part_file_attr = [
		        ["PID", 2000],
		        ["Property Name", "Front TB Part"],
		        ["Material", "ES220"],
		    ]
		    base.NewPTPart(tree, "part2", "MID 2", "Version AB", "Part TB", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part2", parent_identifier, pos_matrix_part
		    )
		    # Add the first CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/FrontTBPart.CATPart", part_file_attr)
		
		    part_file_attr = [
		        ["PID", 2001],
		        ["Property Name", "Rear TB Part"],
		        ["Material", "ES200"],
		    ]
		    # Add the second CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/RearTBPart.CATPart", part_file_attr)
		
		    # Launch the editor.
		    my_settings = base.InputProductTreeSettings()
		    my_settings.should_open_window = True
		    base.InputModelDefinition(product_tree=tree, settings=my_settings)


	"""

def NewProductTree() -> object:

	"""

	Defines a new product tree.

	Returns
	-------
	object
		Returns a reference to the newly created product tree object.

	See Also
	--------
	base.InputModelDefinition

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    # Create the product tree
		    tree = base.NewProductTree()
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # no parent for the top level group
		    child_identifier = 1
		    base.NewPTPart(tree, "group", "MID A", "Version A", "Top Level Group")
		    base.NewPTInstance(
		        tree, child_identifier, "group", parent_identifier, pos_matrix_group
		    )
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = child_identifier  # the part belongs to the previous group
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "1.5"]]
		    part_file_attr = [
		        ["PID", 1000],
		        ["Property Name", "Front Part"],
		        ["Material", "ES200"],
		    ]
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "Part MI", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part
		    )
		    base.NewPTModel(tree, "part1", "/home/demo/FrontPart.CATPart", part_file_attr)
		
		    # Create an instance to the previously created part
		    pos_matrix_instance = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_instance
		    )
		    # Add a PID offset of 100 to the new instance
		    base.SetPTInstancePidOffset(tree, child_identifier, 100)
		
		    # Create a new tailorblanked part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "3.4"]]
		    part_file_attr = [
		        ["PID", 2000],
		        ["Property Name", "Front TB Part"],
		        ["Material", "ES220"],
		    ]
		    base.NewPTPart(tree, "part2", "MID 2", "Version AB", "Part TB", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part2", parent_identifier, pos_matrix_part
		    )
		    # Add the first CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/FrontTBPart.CATPart", part_file_attr)
		
		    part_file_attr = [
		        ["PID", 2001],
		        ["Property Name", "Rear TB Part"],
		        ["Material", "ES200"],
		    ]
		    # Add the second CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/RearTBPart.CATPart", part_file_attr)
		
		    # Launch the editor.
		    my_settings = base.InputProductTreeSettings()
		    my_settings.should_open_window = True
		    base.InputModelDefinition(product_tree=tree, settings=my_settings)


	"""

def SetDMRoot(dm_root: str, username: str, password: str, role: str) -> int:

	"""

	Sets the current DM root to the path DM_PATH.

	Parameters
	----------
	dm_root : str
		A string that describes the path of the DM root directory.

	username : str, optional
		Username (For login in the SPDRM vault).

	password : str, optional
		Password (For login in the SPDRM vault).

	role : str, optional
		User role (For setting the user's role to SPDRM).

	Returns
	-------
	int
		Returns 1 if the new DM root has been set successfully and 0 otherwise.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		# Ex.1
		def main():
		    base.SetDMRoot("C:/Users/Local_Work_files/")
		
		
		# Ex.2: Set SPDRM vault as DM Root
		def main():
		    base.SetDMRoot(
		        "http://magneto.localdomain:8080/", username="user1", password="pass1"
		    )
		    # when we want to change the user's role(when supported):
		    base.SetDMRoot(
		        "http://magneto.localdomain:8080/",
		        username="user1",
		        password="pass1",
		        role="Administrator",
		    )


	"""

def SetPTInstancePidOffset(tree: object, child_identifier: Any, pid_offset: int) -> int:

	"""

	Defines PID offset to an existing Product Tree Instance.

	Parameters
	----------
	tree : object
		The object returned from a previous call to the 'NewProductTree' function.

	child_identifier : Any
		(string/integer) The unique id of an already defined part item.

	pid_offset : int
		The offset value of the PID for the specific instance. It can be
		a positive or negative integer. This information will be passed to 
		the ANSAPART created upon confirmation.

	Returns
	-------
	int
		Returns 0 on success and -1 on failure.

	See Also
	--------
	base.InputModelDefinition

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    # Create the product tree
		    tree = base.NewProductTree()
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # no parent for the top level group
		    child_identifier = 1
		    base.NewPTPart(tree, "group", "MID A", "Version A", "Top Level Group")
		    base.NewPTInstance(
		        tree, child_identifier, "group", parent_identifier, pos_matrix_group
		    )
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = child_identifier  # the part belongs to the previous group
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "1.5"]]
		    part_file_attr = [
		        ["PID", 1000],
		        ["Property Name", "Front Part"],
		        ["Material", "ES200"],
		    ]
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "Part MI", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part
		    )
		    base.NewPTModel(tree, "part1", "/home/demo/FrontPart.CATPart", part_file_attr)
		
		    # Create an instance to the previously created part
		    pos_matrix_instance = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_instance
		    )
		    # Add a PID offset of 100 to the new instance
		    base.SetPTInstancePidOffset(tree, child_identifier, 100)
		
		    # Create a new tailorblanked part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    child_identifier += 1
		    part_attr = [["Mesh Type", "Fine"], ["Target Mass", "3.4"]]
		    part_file_attr = [
		        ["PID", 2000],
		        ["Property Name", "Front TB Part"],
		        ["Material", "ES220"],
		    ]
		    base.NewPTPart(tree, "part2", "MID 2", "Version AB", "Part TB", part_attr)
		    base.NewPTInstance(
		        tree, child_identifier, "part2", parent_identifier, pos_matrix_part
		    )
		    # Add the first CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/FrontTBPart.CATPart", part_file_attr)
		
		    part_file_attr = [
		        ["PID", 2001],
		        ["Property Name", "Rear TB Part"],
		        ["Material", "ES200"],
		    ]
		    # Add the second CAD file to the TB part
		    base.NewPTModel(tree, "part2", "/home/demo/RearTBPart.CATPart", part_file_attr)
		
		    # Launch the editor.
		    my_settings = base.InputProductTreeSettings()
		    my_settings.should_open_window = True
		    base.InputModelDefinition(product_tree=tree, settings=my_settings)


	"""

def LoadProductTreeStatus(tree: object, status_name: str, color_name: str) -> int:

	"""

	Loads a user defined status that can be shown in Tree Editor under the column "Status".
	A new status is defined with a name and a color. 
	After loading a user defined status use the function SetPTPartStatus in order to mark this part with this status.

	Parameters
	----------
	tree : object
		The element returned from a previous call to the 'NewProductTree' function.

	status_name : str
		The uique name of the new status.

	color_name : str
		The color index of the new status. Currently, accepted values are: 
		"white", "green", "gray", "red", "orange", "blue", "magenta", "yellow".

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    tree = base.NewProductTree()
		
		    # Load here user defined status
		    base.LoadProductTreeStatus(tree, "My Orange Flag", "orange")
		    base.LoadProductTreeStatus(tree, "My Blue Flag", "blue")
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # has no parent
		    child_identifier = 1
		    group1_id = child_identifier
		    base.NewPTPart(tree, "group1", "MID A", "Version A", "My Group 1")
		    base.NewPTInstance(
		        tree, child_identifier, "group1", parent_identifier, pos_matrix_group
		    )
		    base.SetPTPartStatus(tree, "group1", "My Orange Flag")
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = group1_id  # the part belongs to the previous group
		    child_identifier += 1
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "My Part 1")
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part
		    )
		    base.NewPTModel(tree, "part1", "/../../test.CATPart")
		    base.SetPTPartStatus(tree, "part1", "My Blue Flag")
		
		    res = base.EditProductTree(tree, "")


	"""

def SetPTPartStatus(tree: object, part_identifier: Any, status: str) -> int:

	"""

	Marks a part (created with NewPTPart) with a user defined status (created with LoadProductTreeStatus).
	When opening the Tree Editor the column "Status" will be show the set status for this part.

	Parameters
	----------
	tree : object
		The element returned from a previous call to 'NewProductTree' function.

	part_identifier : Any
		(string/integer) The unique id that characterizes a product tree structure item.

	status : str
		The unique name of the loaded user defined status.

	Returns
	-------
	int
		Returns 0 on success and 1 on failure.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    tree = base.NewProductTree()
		
		    # Load here user defined status
		    base.LoadProductTreeStatus(tree, "My Orange Flag", "orange")
		    base.LoadProductTreeStatus(tree, "My Blue Flag", "blue")
		
		    # Create a group
		    pos_matrix_group = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = 0  # has no parent
		    child_identifier = 1
		    group1_id = child_identifier
		    base.NewPTPart(tree, "group1", "MID A", "Version A", "My Group 1")
		    base.NewPTInstance(
		        tree, child_identifier, "group1", parent_identifier, pos_matrix_group
		    )
		    base.SetPTPartStatus(tree, "group1", "My Orange Flag")
		
		    # Create a part
		    pos_matrix_part = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
		    parent_identifier = group1_id  # the part belongs to the previous group
		    child_identifier += 1
		    base.NewPTPart(tree, "part1", "MID 1", "Version AA", "My Part 1")
		    base.NewPTInstance(
		        tree, child_identifier, "part1", parent_identifier, pos_matrix_part
		    )
		    base.NewPTModel(tree, "part1", "/../../test.CATPart")
		    base.SetPTPartStatus(tree, "part1", "My Blue Flag")
		
		    res = base.EditProductTree(tree, "")


	"""

def ResolveFilePathAliases(path: str) -> str:

	"""

	Resolves any directory aliases used in "path" like DM or Include Path aliases.

	Parameters
	----------
	path : str
		The path to be resolved

	Returns
	-------
	str
		Returns a path with the aliases expanded (replaced with their value), or the same path if no aliases exist.

	Examples
	--------
	::

		import sdm
		from sdm import base
		from sdm import constants
		
		
		def main():
		    entity = base.GetEntity(constants.NASTRAN, "INCLUDE", 5)
		    ret = base.GetEntityCardValues(constants.NASTRAN, entity, ("FullPathName"))
		    include_fname = ret["FullPathName"]
		    resolved_fname = base.ResolveFilePathAliases(include_fname)
		    print("resolved (unaliased) filename: ", resolved_fname)


	"""

def AddFileInDM(file_name: str, type: str, attributes: object, server_id: str, dm_root: str, target_dm_root: str, add_attachments: bool, add_component_children: bool) -> int:

	"""

	Adds a file in the current DM.

	Parameters
	----------
	file_name : str
		The file path of the file to be added in DM.

	type : str
		Accepted values: 'parts', 'includes', 'Subsystems'.
		For parts an .ansa file must be provided.

	attributes : object
		A dictionary with the key DM attributes of the file. 
		The module id, version, study version, file type and representation
		must be provided. The names of the attributes must be 
		provided as they appear in Part Manager and DM Browser.

	server_id : str, optional
		Instead of the file, a server id from a source dm root can be 
		provided as source. 'file_name' and 'server_id' are mutually 
		exclusive arguments.

	dm_root : str, optional
		The  dm root server_id refers to. if not provided, the current dm is assumed.
		This option is used only if server_id is provided.

	target_dm_root : str, optional
		The dm root where the file will be added. If not provided, the current dm 
		root is assumed. This option is used only if server_id is provided.

	add_attachments : bool, optional
		Default: false. If true, any attachments of the server_id will also 
		be added in dm. This option is used only if server_id is provided.

	add_component_children : bool, optional
		This option is used only if the server_id of a Subsystem is provided.
		If True: the parts of the subsystem will also be added in target dm.
		(Default: False)

	Returns
	-------
	int
		The function returns an integer:
		        0: Success.
		        1: Add in DM failed.
		        2: Invalid dm root.
		        3: Invalid input type.
		        4: Incomplete input dictionary.
		        5: Conflict between the input dictionary and the values in the provided file.
		        6: The file has not been produced with Save Representation.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    dict1 = {}
		    dict1["Module Id"] = "23"
		    dict1["Version"] = "0"
		    dict1["Study Version"] = "0"
		    dict1["Representation"] = ""  # empty for common representation
		    dict1["File Type"] = "ANSA"
		
		    ret = base.AddFileInDM("/home/user/my_file.ansa", "parts", dict1)


	"""

def GetDMRootsList() -> object:

	"""

	Returns the whole DM Roots list, with all the info about which DM is current or 
	is enabled for "Check DM Updates".

	Returns
	-------
	object
		Returns None in case no DM paths found or a list of dictionaries containing the information of each DM Root.
		The keys in each dictionary are shown in the following example:
		
		[{'updates_enabled': True, 'is_current': True, 'dm_root': '//mnt/DM1/'},
		 {'updates_enabled': True, 'is_current': False, 'dm_root': '//mnt/DM2/'},
		 {'updates_enabled': False, 'is_current': False, 'dm_root': 'http://dm3:8989/'}]

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    print(base.GetDMRootsList())


	"""

def AddDMObject(type: str, names_values: object, overwrite: bool, link: bool) -> str:

	"""
	.. deprecated:: 19.0.0
		Use `DMObject.add_new` instead.


	This function adds an object to the DM, if it does not already exist.

	Parameters
	----------
	type : str
		The type of the object to be added.

	names_values : object
		A dictionary which holds the object's property and attribute values.

	overwrite : bool, optional
		Set to True if the object should be overwritten, if it already exists in the DM.

	link : bool, optional
		Set to True if you wish create a link to the file that corresponds to the object.

	Returns
	-------
	str
		Returns the server id, as a string, on success, or None on failure.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    # Adds a component to the DM
		
		    # All properties MUST be present in the object's names_values dictionaries
		    names_values = {}
		    names_values["Module Id"] = "Module1"
		    names_values["Version"] = "Version1"
		    names_values["Study Version"] = "Study1"
		    names_values["Representation"] = "Representation1"
		    names_values["Name"] = "Name1"  # Attribute
		
		    component_server_id = base.AddDMObject("Component", names_values)
		
		    if component_server_id:
		        print("Component server_id: " + component_server_id)
		    else:
		        print("AddDMObject failed.")


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use  DMObject.add_new instead.", DeprecationWarning)

def GetDMObjectAttributeValues(type: str, names_values: object, server_id: str, attributes: object) -> object:

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	This function can return some specified Attribute values of a dm object. The 
	object can be identified by either its server is, or its property values.

	Parameters
	----------
	type : str
		The type of the object (required, if the names_values argument is present).

	names_values : object, optional
		A dictionary which holds the object's property values 
		(all property values must be present for the object's identification).

	server_id : str, optional
		The server id of the object, if it is already known.
		If present, the type and names_values arguments can be omitted.

	attributes : object, optional
		A list in which the user can specify Attribute names, for their values to be returned.
		If this arguments is not present, all the object's values will be returned.

	Returns
	-------
	object
		If the object was found, a dictionary will be returned with the specified attribute values. 
		If the function fails, "None" will be returned.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    property_values = {}
		    property_values["Name"] = "MyName"
		    property_values["Version"] = "A"
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", names_values=property_values, attributes=["SM_Attr"]
		        )
		    )
		
		    # if the server id of this simulation model was already known to be "5472", the function could be called like this:
		    print(base.GetDMObjectAttributeValues("Simulation_Model", server_id="5472"))
		    # or if we are just looking for a specific Attribtue:
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", server_id="5472", attributes=["Last_Edit"]
		        )
		    )


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def SetDMObjectAttributeValues(type: str, names_values: dict, server_id: str, attribute_names_values: dict, attribute_names_types: dict) -> bool:

	"""
	.. deprecated:: 19.0.0
		Use :py:class:`DMObject` instead.


	This function can change Attribute values for a dm object. If an Attribute
	doesn't exist, then this function can also trigger its creation.
	The object can be identified by either its server id, or its property values.

	Parameters
	----------
	type : str
		The type of the object (required, if the names_values argument is present).

	names_values : dict, optional
		A dictionary which holds the object's property values
		(all property values must be present for the object's identification).

	server_id : str, optional
		The server id of the object, if it is already known.
		If present, the type and names_values arguments can be omitted.

	attribute_names_values : dict, optional
		A dictionary which specifies the Attributes to change, in a names-values format.

	attribute_names_types : dict, optional
		A dictionary mapping Attribute names to types. This information will be used
		in case new Attributes will be created and the DM supports typed Attributes.

	Returns
	-------
	bool
		True : If the at least one values was set successfully.
		False: If the function failed to set any value.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    all_values = {}
		    all_values["Name"] = "MyName"
		    all_values["Version"] = "A"
		    all_values["SM_Attr"] = "SM_Attr_Value"  # Attribute
		    base.AddDMObject("Simulation_Model", all_values)
		
		    property_values = {}
		    property_values["Name"] = "MyName"
		    property_values["Version"] = "A"
		
		    base.SetDMObjectAttributeValues(
		        "Simulation_Model",
		        names_values=property_values,
		        attribute_names_values={"SM_Attr": "New_Val"},
		    )
		    # if the server id of this simulation model was already known to be "1", the function could be called like this:
		    # base.GetDMObjectAttributeValues("Simulation_Model", ref_server_id="1", attribute_names_values={"SM_Attr":"New_Val"})
		
		    print(
		        base.GetDMObjectAttributeValues(
		            "Simulation_Model", names_values=property_values, attributes=["SM_Attr"]
		        )
		    )


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def ConnectDMObjectToDMObjects(server_id: str, references: object) -> bool:

	"""

	This function connects dm objects, by referencing. After its execution, 
	the object whose server_id is given as argument, will reference
	the objects specified in the "references" dict.

	Parameters
	----------
	server_id : str
		If the server id of the first object is known, the type and names_values arguments can be ommited.

	references : object
		A dictionary which holds server_id->reference-type pairs.

	Returns
	-------
	bool
		True:  If the new references were made successfully.
		False: If the function failed to make one of the connections.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    dict1 = {}
		    dict1["Name"] = "MyName"
		    dict1["Version"] = "A"
		    dict1["SM_Attr"] = "SM_Attr_Value"  # Attribute
		    sim_model_server_id = base.AddDMObject("Simulation_Model", dict1)
		
		    dict2 = {}
		    dict2["Module Id"] = "Module1"
		    dict2["Version"] = "Version1"
		    dict2["Study Version"] = "Study1"
		    dict2["Representation"] = "Representation1"
		    dict2["Variant"] = "Variant1"
		    dict2["Name"] = "Name1"  # Attribute
		    comp_server_id = base.AddDMObject("Component", dict2)
		
		    print(
		        base.ConnectDMObjectToDMObjects(
		            sim_model_server_id, {comp_server_id: "my_component"}
		        )
		    )


	"""

def GetDMObjectId(type: str, names_values: object) -> str:

	"""

	Search in DM for a DM Object with specific properties and return its server id.
	The specified properties should describe a unique DM Object. If none or more than
	one DM Object are defined from the specified properties, None is returned.

	Parameters
	----------
	type : str
		the type of the DM Object as it is defined in the dm_structure.xml
		(e.g. 'parts', includes', 'Subsystem', etc.).

	names_values : object
		a {'Property':'Value'} dictionary which describes a unique DM Object.

	Returns
	-------
	str
		Returns the server id of the DM Object on success and None on failure.

	See Also
	--------
	ExportDMObjectHierarchy, ExportDMObject, DeleteDMObject, SetDMObjectAttributeValues, GetDMObjectAttributeValues, ConnectDMObjectToDMObjects, dm.CheckForUpdates

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    vals = {"Module Id": "100", "Version": "0", "Representation": "common"}
		    ret = base.GetDMObjectId("parts", vals)
		    if ret:
		        print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SetAttributeValueString(names_values: object, type: str, server_id: str, attribute_name: str, attribute_value: str) -> bool:

	"""

	This function can be used to set an attribute value to a DM Object.

	Parameters
	----------
	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	attribute_name : str, optional
		The Attribute's name.
		Although it's an optional argument, it needs to be defined.

	attribute_value : str, optional
		The value that will be set to the Attribute.
		Although it's an optional argument, it needs to be defined.

	Returns
	-------
	bool

	See Also
	--------
	ExportDMObjectHierarchy, ExportDMObject, DeleteDMObject, GetDMObjectId, SetDMObjectAttributeValues, GetDMObjectAttributeValues, ConnectDMObjectToDMObjects

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("parts", vals)
		    if ret:
		        base.SetAttributeValueString(
		            server_id=ret, type="parts", attribute_name="Big_part", attribute_value="NO"
		        )


	"""

def ExportDMObjectHierarchy(output_directory: str, names_values: object, type: str, server_id: str) -> str:

	"""
	.. deprecated:: 17.0.0
		Use :py:class:`DMObject` instead.


	When a DM Object can be defined by a DM Object hierarchy, e.g. a Subsystem,
	use this function to download the hierarchy and afterwards read it into ANSA.

	Parameters
	----------
	output_directory : str
		Specifies where the xml will be downloaded.

	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when the 
		names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	Returns
	-------
	str
		Returns the resulting directory on success.

	See Also
	--------
	ExportDMObject, DeleteDMObject, GetDMObjectId

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = sdm.base.GetDMObjectId("parts", vals)
		    print(ret)
		    if ret:
		        base.ExportDMObjectHierarchy("C:/home/demo/tmp", server_id=ret)


	"""

	import warnings; warnings.warn("Deprecated since version 17.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def ExportDMObject(output_directory: str, names_values: object, type: str, server_id: str, action: str) -> str:

	"""

	This function can be used to download a DM Object's Representation File from DM.

	Parameters
	----------
	output_directory : str
		Specify where the file/files will be downloaded.

	names_values : object, optional
		A dictionary defining the DM Object. When the server_id argument isn't given,
		the function will search for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when 
		the names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	action : str, optional
		The exported file from the server will be copied to the target directory by default.
		It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory. 
		Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items and Library Files.

	Returns
	-------
	str
		Returns the resulting directory on success.

	See Also
	--------
	ExportDMObjectHierarchy, DeleteDMObject, GetDMObjectId

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("parts", vals)
		    print(ret)
		    if ret:
		        base.ExportDMObject("C:/home/demo/tmp", server_id=ret)


	"""

def DeleteDMObject(names_values: object, type: str, server_id: str, only_representation_file: str) -> int:

	"""
	.. deprecated:: 19.0.0
		Use :py:class:`DMObject` instead.


	Deletes an Object from DM using this function.

	Parameters
	----------
	names_values : object, optional
		A dictionary defining the DM Object.
		When the server_id argument isn't given, the function will search 
		for the DM Object using this set of Properties/Values.

	type : str, optional
		The DM Object's type.
		Although it's an optional argument, it needs to be defined when the 
		names_values argument is used.

	server_id : str, optional
		The DM Object's server id. It can be used if already known.

	only_representation_file : str, optional
		Use "YES" when only the Representation File should be deleted and the 
		Object should be kept in the database.

	Returns
	-------
	int
		Returns 1 on success, 0 on failure.

	See Also
	--------
	ExportDMObject, ExportDMObjectHierarchy, GetDMObjectId

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    vals = {"Project": "L1", "Discipline": "Crash"}
		    ret = base.GetDMObjectId("Subsystems", vals)
		    print(ret)
		    if ret:
		        base.DeleteDMObject(server_id=ret, type="Subsystems")


	"""

	import warnings; warnings.warn("Deprecated since version 19.0.0. Use :py:class: DMObject instead.", DeprecationWarning)

def InputModelDefinition(file_name: str, file_type: str, product_tree: object, settings: object) -> int:

	"""

	Imports a model definition in ANSA.

	Parameters
	----------
	file_name : str, optional
		The name of the file to import. It can be an empty string.
		In this case, the file manager opens to select a file.

	file_type : str, optional
		The type of the file to open.
		Valid types are: "VPM", "PLMXML", "CATProduct", "AP242", "STEP", "ProE", "JT", "NX", "3DXML", "Solidworks".

	product_tree : object, optional
		A product tree created from script with the function base.NewProductTree().

	settings : object, optional
		An object of type "base.InputProductTreeSettings()" for defining the settings 
		when reading the file.

	Returns
	-------
	int
		Returns 1 on success, 0 on failure.

	See Also
	--------
	base.InputProductTreeSettings, base.ProductTree

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    my_settings = base.InputProductTreeSettings()
		    my_settings.post_actions_script_function = "MyFun"
		    my_settings.post_actions_script_path = "//home/post_actions_script.py"
		    my_settings.should_open_window = True
		
		    filename = "//home/file.xml"
		
		    base.InputModelDefinition(
		        file_name=filename, file_type="PLMXML", settings=my_settings
		    )
		
		
		# example of post_actions_script.py:
		def MyFun(product_tree, *args, **kwargs):
		    all_part_ids = product_tree.get_all_part_ids()
		
		    print("Total number of parts in product_tree: " + str(len(all_part_ids)))
		
		    for part_id in all_part_ids:
		        name = product_tree.get_part_attribute_value(part_id, "Name")
		        module_id = product_tree.get_part_attribute_value(part_id, "Module Id")
		        version = product_tree.get_part_attribute_value(part_id, "Version")
		        is_group = product_tree.get_part_attribute_value(part_id, "Is Group")
		        print("----------------------------------------------------------------")
		        print("Part with id: " + part_id)
		        print("   Name: " + name)
		        print("   Module Id: " + module_id)
		        print("   Version: " + version)
		        print("   Is Group: " + is_group)
		        print(
		            "   All Attributes: "
		            + str(product_tree.get_all_part_attribute_values(part_id))
		        )
		        print("----------------------------------------------------------------")
		
		        # fix empty versions:
		        if version == "A":
		            product_tree.set_part_attribute_value(part_id, "Version", "test")
		            print("Changed Version to Part with id: " + part_id)
		        # totally remove some parts:
		        if "SCREW" in name:
		            product_tree.remove_part(part_id)
		            print("Removed Part with id :" + part_id)


	"""

def AddDOEStudy(names_values: object, design_variables: object, responses: object, experiments_object_ids: object) -> str:

	"""

	This function adds a DOE_Study object to the DM.

	Parameters
	----------
	names_values : object
		A dictionary which holds the object's property and attribute values.

	design_variables : object, optional
		A dictionary with key the experiment id and value another dictionary which holds the design variables as name-value pairs.

	responses : object, optional
		A dictionary with key the experiment id and value another dictionary which holds the responses as name-value pairs.

	experiments_object_ids : object, optional
		A dictionary which holds the experiments server ids in DM.

	Returns
	-------
	str
		Returns the server id, as a string, on success, or None on failure.

	Examples
	--------
	::

		import sdm
		from sdm import dm
		
		
		def main():
		    dvs = {"1": {"Thickness": "1.2"}, "2": {"Thickness": "1.3"}}
		    resps = {"1": {"Displacement": "2.5"}, "2": {"Displacement": "1.2"}}
		    attributes = {"Optimization Task Name": "My_task"}
		
		    server_id = dm.AddDOEStudy(
		        names_values=attributes, design_variables=dvs, responses=resps
		    )
		
		    if server_id:
		        print("DOE_Study server_id: " + server_id)
		    else:
		        print("AddDOEStudy failed.")


	"""

class InputProductTreeSettings():

	"""

	InputProductTreeSettings is a module for defining the Product Tree Editor settings when importing a model definition with sdm.base.InputModelDefinition.

	See Also
	--------
	base.InputModelDefinition, base.ProductTree, base.GetCurrentInputProductTreeSettings

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def main():
		    my_settings = base.InputProductTreeSettings()
		    my_settings.post_actions_script_function = "MyFun"
		    my_settings.post_actions_script_path = "//home/post_actions_script.py"
		    my_settings.should_open_window = True
		
		    filename = "//home/file.xml"
		
		    base.InputModelDefinition(
		        file_name=filename, file_type="PLMXML", settings=my_settings
		    )
		
		
		# example of post_actions_script.py:
		def MyFun(product_tree, *args, **kwargs):
		    all_part_ids = product_tree.get_all_part_ids()
		
		    print("Total number of parts in product_tree: " + str(len(all_part_ids)))
		
		    for part_id in all_part_ids:
		        name = product_tree.get_part_attribute_value(part_id, "Name")
		        module_id = product_tree.get_part_attribute_value(part_id, "Module Id")
		        version = product_tree.get_part_attribute_value(part_id, "Version")
		        is_group = product_tree.get_part_attribute_value(part_id, "Is Group")
		        print("----------------------------------------------------------------")
		        print("Part with id: " + part_id)
		        print("   Name: " + name)
		        print("   Module Id: " + module_id)
		        print("   Version: " + version)
		        print("   Is Group: " + is_group)
		        print(
		            "   All Attributes: "
		            + str(product_tree.get_all_part_attribute_values(part_id))
		        )
		        print("----------------------------------------------------------------")
		
		        # fix empty versions:
		        if version == "A":
		            product_tree.set_part_attribute_value(part_id, "Version", "test")
		            print("Changed Version to Part with id: " + part_id)
		        # totally remove some parts:
		        if "SCREW" in name:
		            product_tree.remove_part(part_id)
		            print("Removed Part with id :" + part_id)

	"""


	check_for_representations: str = None
	"""
	Sets more representation names to be checked in DM, in addition to 'common'.
	For example: 'crash, nvh, dura'.
	Note that the representation 'common' will always be checked.

	"""

	relative_path: str = None
	"""
	Defines the relative path that will be used for locating relative part file 
	paths that start with '.' or './'.

	"""

	directory_of_cad_files: str = None
	"""
	Defines an additional directory path that will be used for locating 
	the part files.

	"""

	post_actions_script_path: str = None
	"""
	Defines the path of the python file that contains the post actions 
	script function.

	"""

	post_actions_script_function: str = None
	"""
	Defines a post actions script function to be applied on the input model 
	with the following prototype:
	MyFun(product_tree, *args, **kwargs),
	where product_tree is a python object of type ansa.base.ProductTree()

	"""

	use_plmxml_parser: str = None
	"""
	Selects the PLMXML parser. Valid values:
	- 'Auto': ANSA will try to recognize the correct parser according to 
	  the file format (default).
	- 'Vismockup': Force using the Vismockup parser (always the ProductDef 
	  is parsed).
	- 'Teamcenter': Force using the Teamcenter parser (ProductDef or 
	  ProductView is parsed).

	"""

	read_plmxml_structure: str = None
	"""
	Defines where to read the parts structure from, when parsing PLMXML files.
	Valid values:
	- 'ProductView': Read the parts structure from ProductView > Occurrence
	  (absolute transformation matrices) (default).
	- 'ProductDef': Read the parts structure from ProductDef > InstanceGraph 
	  > ProductInstance (relative transformation matrices).

	"""

	read_plmxml_attributes: str = None
	"""
	Defines which attributes (UserData->UserValue) should be read when 
	parsing PLMXML files. Valid values:
	- 'None': No attribute will be read (default).
	- 'All': All attributes will be read from any xml node.
	- 'Specific': Only attributes defined in 
	  'plmxml_specific_attributes_to_read' will be read.

	"""

	plmxml_specific_attributes_to_read: str = None
	"""
	Defines the attribute names that will be read when parsing PLMXML files.
	- Add attribute names with prefix (will be searched only in specific mode).
	  Example: 'Form/SubType/MyAttribute1, Occurrence/MyAttribute2, 
	  Product/MyAttribute3'.
	- Add attribute names without any prefix (will be searched in any xml node).
	  Example: 'MyAttribute1, MyAttribute2, MyAttribute3'.
	- Add only the prefix. All attributes inside these xml nodes will be read.
	  Example: 'Form/*, Form/subType/*, Occurrence/*, Product/*'.

	"""

	read_plmxml_related_properties: str = None
	"""
	In  PLMXML files some relations exist where one item points to another.
	For example: <GeneralRelation relatedRefs="#id10 #id20"> where the original item is #id10 and the related #id20.
	This member defines which property values (name, part number, version) should be kept. Valid values:
	- 'Keep original'
	- 'Keep related' (default)

	"""

	read_plmxml_related_part_files: str = None
	"""
	In  PLMXML files some relations exist where one item points to another.
	For example: <GeneralRelation relatedRefs="#id10 #id20"> where the original item is #id10 and the related #id20.
	This member defines which part files (e.g. jt) should be kept. Valid values:
	- 'Keep original'
	- 'Keep related' (default)
	- 'All'

	"""

	read_plmxml_related_attributes: str = None
	"""
	In  PLMXML files some relations exist where one item points to another.
	For example: <GeneralRelation relatedRefs="#id10 #id20"> where the original item is #id10 and the related #id20.
	This member defines which attribute values should be kept. Valid values:
	- 'Keep original'
	- 'Keep related' (default)
	- 'All'

	"""

	part_name_convert: bool = None
	"""
	If set to True, converts the part names when importing structure from 
	Product Tree Editor to ANSA. Prepends the part number and the part 
	version: PartNumber_PartVersion_PartName.
	(Default: True)

	"""

	should_open_window: bool = None
	"""
	If set to True, opens the Product Tree Editor window.
	(Default: True)

	"""

	read_part_name_from_keys: str = None
	"""
	Defines the exact xml keys with specific priority to read 'Name'. 
	e.g. 'name, Name'

	"""

	read_part_number_from_keys: str = None
	"""
	Defines the exact xml keys with specific priority to read 'Part Number'. 
	e.g. 'part number, PartNumber'

	"""

	read_part_version_from_keys: str = None
	"""
	Defines the exact xml keys with specific priority to read 'Version'.
	e.g. 'Version, version, revision'

	"""

	compress_parts: bool = None
	"""
	Delete from hierarchy all parts that have no part files.
	(Default: False)

	"""

	keep_different_versions_per_part_number: bool = None
	"""
	When the ANSA setting 'Allow Multi Version Parts' is not selected, use this setting to show in Product Tree Editor hierarchy parts with same Part Number and different Versions. 
	(Default: False)

	"""

	handle_jt_files_as_monolithic: bool = None
	"""
	Handle the attached JT files as Monolithic JT files during CAD to AnSA translation.
	(Default: True)

	"""

	ignore_part_files_on_groups: bool = None
	"""
	Remove all attached part files from groups.
	(Default: False)

	"""

	define_groups_on_empty_occurrenceRefs_value: bool = None
	"""
	When parsing Teamcenter plmxmls, if the value of the occurrenceRefs field is the empty string the Occurrence will be considered a group instead of a part.
	(Default: False)

	"""

	compress_groups: bool = None
	"""
	Delete from hierarchy all groups that have no parts and no part files. 
	(Default: False)

	"""

	merge_nested_plmxml_files: bool = None
	"""
	Merge all nested plmxml files into the main structure.
	(Default: False)

	"""

	should_open_window_in_central_tab: bool = None
	"""
	If set to True, opens the window in a tab of the central area of KOMVOS.
	(Default: False) This member is valid only in KOMVOS.

	"""
def ChangeColorModeValueForItemsInViewer(color_mode_name: str, value: str, group_name: str, model_ids: object, attributes_per_server_ids: object) -> bool:

	"""

	This function changes the value of specific items in viewer for a specific color mode.

	Parameters
	----------
	color_mode_name : str
		Color mode name.

	value : str
		New value.

	group_name : str
		Group name (not needed in case of custom color modes, use "" instead)

	model_ids : object, optional
		List of instance ids in viewer.

	attributes_per_server_ids : object, optional
		List of maps with server ids as key and attribute names and values as data.
		Used instead of model_ids.

	Returns
	-------
	bool
		Returns True for success.

	Examples
	--------
	::

		import sdm
		from sdm import base
		
		
		def changeColorModeValueInViewer(
		    target_submodel_object_id, target_module_id, attrs_per_server_ids_list
		):
		    base.ChangeColorModeValueForItemsInViewer(
		        "Subsystem",
		        target_submodel_object_id,
		        target_module_id,
		        attributes_per_server_ids=attrs_per_server_ids_list,
		    )
		
		
		# Other examples
		# base.ChangeColorModeValueForItemsInViewer("Submodel", "26", "Body Top (main)", attributes_per_server_ids=in_attrs_per_server_ids)
		# base.ChangeColorModeValueForItemsInViewer("MeshParamStatus", "8mm-OK", "", attributes_per_server_ids=in_attrs_per_server_ids_list )
		# base.ChangeColorModeValueForItemsInViewer("RepresentationStatus", "Common-WIP", "", attributes_per_server_ids=in_attrs_per_server_ids_list )
		# base.ChangeColorModeValueForItemsInViewer("SimulationModel", "62", "My test , Planstand: 21-FEB-2017 12:02:15", attributes_per_server_ids=in_attrs_per_server_ids_list )


	"""

class PartManager():

	"""

	A class that manipulates the window created to input model definition in KOMVOS

	Examples
	--------
	::

		import os
		import sdm
		from sdm import base
		
		
		# assuming the user has already imported a model definition...
		def manipulateCurrentlyDisplayed():
		    pm = base.PartManager()
		    pm.init_with_current()
		    pm.apply_template("010_powertrain_mounts_150kw.xml")
		    pm.set_all_active()
		    pm.reset_template()
		
		
		# creating a PartManager via script from scratch and manipulating it as well
		def createAndDisplayWithAnAppliedTemplate():
		    pm = base.PartManager()
		    pm.input_model_definition(
		        file_type="PLMXML",
		        file_name="//cyclop/testdata/user_dirs/m.papastavropoulou/CEVT/CAE_Structure/customer_files/CM1E_J1_Released_V2_CM1E_LHD_US_SDS_PREPARED_TRANSPORT_220423.plmxml",
		    )
		    sdm.sdm_base.PostMessageInInfoArea("ENDING..")
		    pm.apply_template("010_powertrain_mounts_150kw.xml")
		
		
		def collectAllPartsAndPartFiles():
		    pm = base.PartManager()
		    pm.init_with_current()
		
		    all_ids = pm.get_all_entities()
		
		    all_parts = []
		    all_part_files = []
		
		    for id in all_ids:
		        if pm.is_part(id):
		            all_parts.append(id)
		        elif pm.is_part_file(id):
		            all_part_files.append(id)
		
		    return all_parts, all_part_files
		
		
		def markSelectedPartsAsCurrent():
		    pm = base.PartManager()
		    pm.init_with_current()
		
		    selected_ids = pm.get_selected_entities()
		
		    for id in selected_ids:
		        if pm.is_part(id):
		            value = pm.get_attribute_value(id, "current")
		            if not value:
		                pm.create_attribute("PART", "current")
		            pm.set_attribute_value(id, "current", "Yes")
		
		
		def main():
		    createAndDisplayWithAnAppliedTemplate()
		    manipulateCurrentlyDisplayed()
		    all_parts, all_part_files = collectAllPartsAndPartFiles()
		    markSelectedPartsAsCurrent()

	"""


	def init_with_current(self):

		"""

		Initializes object using currently displayed Part Manager


		"""


	def input_model_definition(self, filetype: str, file_name: str, product_tree: object, settings: object):

		"""

		Imports a model definition


		Parameters
		----------
		filetype : str
			The type of the file to open.
			Valid types are: "VPM", "PLMXML", "CATProduct", "AP242", "STEP", "ProE", "JT", "NX", "3DXML", "Solidworks".

		file_name : str, optional
			The name of the file to import. It can be an empty string.
			In this case, the file manager opens to select a file.

		product_tree : object, optional
			A product tree created from script with the function base.NewProductTree().

		settings : object, optional
			An object of type "base.InputProductTreeSettings()" for defining the settings 
			when reading the file.

		"""


	def template(self, template: str) -> bool:

		"""

		Applies template with given name


		Parameters
		----------
		template : str
			Specify the template to be applied. 
			This may be a full path or simply the file name. The paths that shall be searched for the file name are 
			SDM_CONSOLE_HOME,
			SDM_CONSOLE_HOME/Subsystems and SDM_CONSOLE_HOME/SimulationModels
			
			In case the file was not found, an exception is thrown.

		Returns
		-------
		bool
			Returns True

		"""


	def reset_template(self):

		"""

		Resets applied template


		"""


	def set_all_active(self):

		"""

		Sets all inactive parts to active status


		"""


	def hide_inactive(self):

		"""

		Hide inactive parts in list


		"""


	def open_in_viewer(self) -> bool:

		"""

		Displays the whole model definition(product structure) in Meta Viewer.


		Returns
		-------
		bool
			Returns True on success, False on failure.

		"""


	def close(self) -> bool:

		"""

		Closes the tab of the PartManager


		Returns
		-------
		bool
			Returns True when succesfully closes the PartManager, False otherwise.

		"""


	def get_all_entities(self) -> list:

		"""

		Returns the ids of all parts and part files in Part Manager


		Returns
		-------
		list
			The list of entity ids

		"""


	def get_selected_entities(self) -> list:

		"""

		Returns the selected parts and part files and all their children


		Returns
		-------
		list
			The list of selected entities ids

		"""


	def is_part(self, id: int) -> bool:

		"""

		Checks whether the entity id belongs to a part in Part Manager


		Parameters
		----------
		id : int
			The entity id

		Returns
		-------
		bool
			Returns True if the id belongs to a part in Part Manager

		"""


	def is_part_file(self, id: int) -> bool:

		"""

		Checks whether the entity id belongs to a part file in Part Manager


		Parameters
		----------
		id : int
			The entity id

		Returns
		-------
		bool
			Returns True if the id belongs to a part file in Part Manager

		"""


	def get_part_files(self, id: int) -> list:

		"""

		Returns the part file ids of the part with specific id


		Parameters
		----------
		id : int
			The part id

		Returns
		-------
		list
			Returns the list of part file ids, or None if no part exists in Part Manager with this id

		"""


	def get_attribute_value(self, id: int, attribute: str) -> str:

		"""

		Returns the attribute value of a part or part file with specific id


		Parameters
		----------
		id : int
			The id of the part or part file

		attribute : str
			The attribute name

		Returns
		-------
		str
			Returns the attribute value or None if the attribute name does not exist

		"""


	def set_attribute_value(self, id: int, attribute: str, value: str) -> bool:

		"""

		Sets the attribute value of a part or part file with specific id


		Parameters
		----------
		id : int
			The id of the part or part file

		attribute : str
			The attribute name

		value : str
			The attribute value to set

		Returns
		-------
		bool
			Returns True on success, False on failure

		"""


	def create_attribute(self, type: str, attribute: str) -> bool:

		"""

		Creates an attribute for parts or part files


		Parameters
		----------
		type : str
			Sets whether to create a part or a part file attribute. Accepted values are: PART, PART_FILE

		attribute : str
			The name of the attribute to create

		Returns
		-------
		bool
			Returns True on success, False on failure

		"""

def GenerateSubsystemsBasedOnTemplates(subsystems_attributes: object, model_structure: str, tree_settings: object, subsystems_templates: object) -> object:

	"""

	This function will save new Subsystems by doing the following:
	* Input a PLMXML file
	* Save Subsystems by applying a Template

	Parameters
	----------
	subsystems_attributes : object
		A list of dictionaries. Each dictionary contains the name/values pairs of the Properties and Attributes of the Subsystem to be saved.

	model_structure : str
		The PLMXML file that will be read.

	tree_settings : object
		An object of type "base.InputProductTreeSettings()" for defining the settings when reading the file.

	subsystems_templates : object
		A dictionary with pairs of the following type:
		Subsystem Module Id : Subsystem Template Name
		Each Template will be applied to the Subsystem with the respective Module Id.

	Returns
	-------
	object
		Returns the list on newly created Subsystems' server ids. None is returned if something goes wrong.

	Examples
	--------
	::

		# PYTHON script
		import os
		import sdm
		from sdm import base, dm
		
		plmxml_filepath = "//cyclop/testdata/user_dirs/m.papastavropoulou/CEVT/CAE_Structure/customer_files/CM1E_J1_Released_V2_CM1E_LHD_US_SDS_PREPARED_TRANSPORT_220423.plmxml"
		
		
		def _saveComponentsAndModelinDM():
		    settings = base.InputProductTreeSettings()
		    settings.use_plmxml_parser = "Auto"
		    settings.read_plmxml_attributes = "All"
		    settings.should_open_window = False  # PTEditor
		    settings.part_name_convert = False
		    # settings.post_actions_script_path = '$DCM_GUI_HOME/cad4cae_plmxml.py'
		    # settings.post_actions_script_function = 'RunPostTreatmentAttributesForConversionService'
		    settings.compress_parts = True
		    settings.keep_different_versions_per_part_number = True
		
		    sub1_attributes = {
		        "Module Id": "1",
		        "Project": "-",
		        "Version": "stcr",
		        "Variant": "-",
		        "Discipline": "-",
		        "Discipline Version": "001",
		        "Team": "-",
		        "Team Version": "001",
		        "Study Version": "0",
		        "File Type": "ANSA",
		        "Representation": "test",
		    }
		    sub2_attributes = {
		        "Module Id": "2",
		        "Project": "-",
		        "Version": "stcr",
		        "Variant": "-",
		        "Discipline": "-",
		        "Discipline Version": "001",
		        "Team": "-",
		        "Team Version": "001",
		        "Study Version": "0",
		        "File Type": "ANSA",
		        "Representation": "test",
		    }
		
		    submodel_templates = {
		        "1": "/cyclop/testdata/scratch_files/kostasd/test_dbs/subsystem_template.xml",
		        "2": "/cyclop/testdata/scratch_files/kostasd/test_dbs/subsystem_template.xml",
		    }
		
		    subsystem_attributes_list = [sub1_attributes, sub2_attributes]
		
		    comp = base.GenerateSubsystemsBasedOnTemplates(
		        subsystems_attributes=subsystem_attributes_list,
		        model_structure=plmxml_filepath,
		        subsystems_templates=submodel_templates,
		        tree_settings=settings,
		    )
		
		    if not comp:
		        print("Failed to save Subsystem in DM")
		    else:
		        print("Successfully created Subsystem id: {}".format(comp))
		
		
		_saveComponentsAndModelinDM()


	"""

def BCSettingsGetUserDefinedValue(keyword: str) -> str:

	"""

	Returns the string value of user defined keyword with name keyword
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsSetUserDefinedValue(keyword: str, value: str) -> int:

	"""

	Sets value value to user defined keyword keyword. 
	If keyword a\ keyword doesn't exist it will be created.
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup and set the new value.

	value : str
		the new string value of the keyword

	Returns
	-------
	int
		1 if value was set successfully to keyword keyword, 0 otherwise.

	See Also
	--------
	BCSettingsGetUserDefinedValue

	"""

def BCSettingsUserDefinedKeywordExists(name: str) -> int:

	"""

	Checks if a user defined key with name name exists in BCSettingsHandler structure
	It will only search for a keyword not for a value.
	This function is not supported under VR mode.

	Parameters
	----------
	name : str
		the keyword's name to look up.

	Returns
	-------
	int
		1 if user defined keyword is found, 0 otherwise.

	See Also
	--------
	BCSettingsSetUserDefinedValue

	"""

def BCSettingsReadFile(filePath: str) -> int:

	"""

	Reads a defaults file, from path filePath.
	
	Settings that will be read from the file, will be applied
	to the running application.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		the path of defaults file

	Returns
	-------
	int
		1 if reading was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteFile(filePath: str) -> int:

	"""

	Writes a defaults file, at path filePath. If a filePath is not given,
	\the defaults file will be written in .BETA folder according to which
	\layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If the file already exists, it will be overwritten.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str, optional
		the path where the defaults file will be written.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteGroup

	"""

def BCSettingsWriteGroup(filePath: str, groupName: str) -> int:

	"""

	Writes the settings of Group named groupName, at path filePath.
	\If filePath is empty, the group will be written in defaults file located in .BETA folder
	\according to which layout ANSA was launched (e.g. ANSA.defaults, CFD.defaults)
	If file already exists, then the settings of the corresponding group will be updated.
	The rest of the file will remain intact.
	This function is not supported under VR mode.

	Parameters
	----------
	filePath : str
		the path where the defaults file will be written.

	groupName : str
		the group name, to write.

	Returns
	-------
	int
		1 if save was succesfull, 0 otherwise.

	See Also
	--------
	BCSettingsWriteFile

	"""

def BCSettingsGetDefaultValue(keyword: str) -> str:

	"""

	Returns the default value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsGetStartupValue

	"""

def BCSettingsGetStartupValue(keyword: str) -> str:

	"""

	Returns the startup value of keyword with name keyword as string
	This function is not supported under VR mode.

	Parameters
	----------
	keyword : str
		the keyword name to lookup.

	Returns
	-------
	str
		the value of the keyword, if keyword was found, otherwise returns  None.

	See Also
	--------
	BCSettingsGetDefaultValue

	"""

