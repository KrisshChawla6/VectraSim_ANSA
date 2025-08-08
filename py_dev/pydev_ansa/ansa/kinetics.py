from __future__ import annotations
from typing import *

def CalculateMassProperties(entity: object) -> int:

	"""

	Calculates the mass of KIN_RBODY.

	Parameters
	----------
	entity : object
		The ANSA entity (type KIN_RBODY), whose mass will be calculated.

	Returns
	-------
	int
		Returns 1 on success and 0 if an invalid entity is given.
		If the KIN_RBODY has type GROUND, then the mass can't be calculated
		(the return value will be 1 and a message will be printed).

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # calculate the mass of KIN_RBODY with id 3
		    body = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 3)
		    kinetics.CalculateMassProperties(body)
		    print("body", base.GetEntityCardValues(base.CurrentDeck(), body, ["mass"])["mass"])
		
		
		# ...or...
		
		
		def main():
		    # calculate the mass of all KIN_RBODYs
		    bodies = base.CollectEntities(base.CurrentDeck(), None, "KIN_RBODY")
		
		    for b in bodies:
		        kinetics.CalculateMassProperties(b)
		    # print the mass of each body
		    for b in bodies:
		        gen_type = base.GetEntityCardValues(base.CurrentDeck(), b, ["GEN_TYPE"])
		        if gen_type["GEN_TYPE"] != "GROUND":
		            print(b, base.GetEntityCardValues(base.CurrentDeck(), b, ["mass"])["mass"])


	"""

def Dz(to_marker: str, from_marker: str, along_marker: str) -> float:

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.

	Parameters
	----------
	to_marker : str
		The name or the id of the 'to_marker'.

	from_marker : str, optional
		The name or the id of the 'from_marker'.

	along_marker : str, optional
		The name or the id of the 'along_marker'.

	Returns
	-------
	float
		Returns the distance along Z (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    distance_along_z = kinetics.Dz("1", "2", "3")


	"""

def Dm(to_marker: str, from_marker: str) -> float:

	"""

	Gets the magnitude of the translational displacement vector from 'from_marker' to 'to_marker'.

	Parameters
	----------
	to_marker : str
		The name or the id of the 'to_marker'.

	from_marker : str, optional
		The name or the id of the 'from_marker'.

	Returns
	-------
	float
		Returns the magnitude of the distance (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    distance_mag = kinetics.Dm("1", "2")


	"""

def Ax(to_marker: str, from_marker: str) -> float:

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the x-axis of 'from_marker', 
	and accounts for angle wrapping.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the rotational displacement (in radians) about x-axis of 'from_marker' (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    rot_along_x2 = kinetics.Ax("1", "2")


	"""

def Ay(to_marker: str, from_marker: str) -> float:

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the y-axis of 'from_marker', and accounts for angle wrapping.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the rotational displacement (in radians) about y-axis of 'from_marker' (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    rot_along_y2 = kinetics.Ay("1", "2")


	"""

def Az(to_marker: str, from_marker: str) -> float:

	"""

	Gets the rotational displacement (in radians) of 'to_marker' about the z-axis of 'from_marker', and accounts for angle wrapping.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the rotational displacement (in radians) about z-axis of 'from_marker' (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    rot_along_z2 = kinetics.Az("1", "2")


	"""

def Vx(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the velocity along X (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    velocity_along_x3 = kinetics.Vx("1", "2", "3", "4")


	"""

def Vy(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the velocity along Y (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    velocity_along_x3 = kinetics.Vy("1", "2", "3", "4")


	"""

def Vz(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the velocity from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the velocity along Z (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    velocity_along_x3 = kinetics.Vz("1", "2", "3", "4")


	"""

def Vm(to_marker: str, from_marker: str, reference_marker: str) -> float:

	"""

	Gets the magnitude of the velocity from 'from_marker' to 'to_marker'.
	All velocities are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the velocity magnitude (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    velocity_mag = kinetics.Vm("1", "2", "4")


	"""

def Vr(to_marker: str, from_marker: str, reference_marker: str) -> float:

	"""

	Gets the radial (separation) velocity from 'from_marker' to 'to_marker'.
	All velocities are taken in the 'reference_marker' coordinate system.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the radial (separation) velocity (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    vr = kinetics.Vr("1", "2", "4")


	"""

def Wx(to_marker: str, from_marker: str, about_marker: str) -> float:

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the X direction of the 'about_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	about_marker : str, optional
		Name or id of the 'about_marker'.

	Returns
	-------
	float
		Returns the angular velocity about X (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    avel_about_x3 = kinetics.Wx("1", "2", "3")


	"""

def Wy(to_marker: str, from_marker: str, about_marker: str) -> float:

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the Y direction of the 'about_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	about_marker : str, optional
		Name or id of the 'about_marker'.

	Returns
	-------
	float
		Returns the angular velocity about Y (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    avel_about_y3 = kinetics.Wy("1", "2", "3")


	"""

def Wz(to_marker: str, from_marker: str, about_marker: str) -> float:

	"""

	Gets the angular velocity from 'from_marker' to 'to_marker' about the Z direction of the 'about_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	about_marker : str, optional
		Name or id of the 'about_marker'.

	Returns
	-------
	float
		Returns the angular velocity about Z (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    avel_about_z3 = kinetics.Wz("1", "2", "3")


	"""

def Wm(to_marker: str, from_marker: str) -> float:

	"""

	Gets the magnitude of the angular velocity from 'from_marker' to 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the angular velocity magnitude (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    avel_mag = kinetics.Wm("1", "2")


	"""

def Time() -> float:

	"""

	Gets the current simulation time.

	Returns
	-------
	float
		Returns the current simulation time (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    time = kinetics.Time()


	"""

def Mode() -> float:

	"""

	Gets the analysis mode.

	Returns
	-------
	float
		Returns an integer defining the Analysis mode:
		
		1, For Kinematics analysis.
		3, For IC.
		4, For Dynamics.
		5, For Static equilibrium.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    mode = kinetics.Mode()
		    if mode == 3:
		        print("I am in IC mode")


	"""

def AddBodyToContact(kin_contact: object, kin_body: object) -> int:

	"""

	This function adds a kinetic rigid body (KIN_RBODY) to a kinetic contact (KIN_CONTACT).

	Parameters
	----------
	kin_contact : object
		The ANSA entity (KIN_CONTACT) that the kinetic rigid body will be added to.

	kin_body : object
		The ANSA entity (KIN_RBODY) to be added to the kinetic contact.

	Returns
	-------
	int
		Returns 1 on success.
		An exception is raised if invalid entities are given.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    contact = base.CreateEntity(
		        base.CurrentDeck(), "KIN_CONTACT", {"Name": "My CONtAct"}
		    )
		
		    body1 = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 1)
		    body2 = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 3)
		
		    # add bodies with ids 1 & 3 to contact
		    kinetics.AddBodyToContact(contact, body1)
		    kinetics.AddBodyToContact(contact, body2)


	"""

def FindContact(kin_contact: object) -> object:

	"""

	This function checks collision of given kinetic contact (KIN_CONTACT) and
	returns contacts (points, normal vectors and penetration depth).
	Number of contacts found is printed in ANSA Info & command line.

	Parameters
	----------
	kin_contact : object
		ANSA entity (KIN_CONTACT) to find contacts.

	Returns
	-------
	object
		Returns a tuple of five lists (each of length equal to the number of contacts found):
		1st list element: point (belongs to one of the elements where contact was found).
		2nd list element: normal vector for point of 1st list.
		3rd list element: point (belongs to the other element where contact was found).
		4th list element: normal vector for point of 3rd list.
		5th list element: penetration depth (distance of points of 1st & 3rd list).
		For each contact found an element is added to each list.
		An exception is raised if invalid entity is given.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    contact = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 1)
		
		    point1, normal1, point2, normal2, depth = kinetics.FindContact(contact)
		
		    for i in range(len(point1)):
		        print("Point1:  ", point1[i][0], point1[i][1], point1[i][2])
		        print("Normal1: ", normal1[i][0], normal1[i][1], normal1[i][2])
		        print("Point2:  ", point2[i][0], point2[i][1], point2[i][2])
		        print("Normal2: ", normal2[i][0], normal2[i][1], normal2[i][2])
		        print("Depth:   ", depth[i])
		        print("------------------------------------------------")


	"""

def SaveAsInitialPosition(initialize_joints: bool, kin_config: object) -> int:

	"""

	Saves the current position of the model as initial position.

	Parameters
	----------
	initialize_joints : bool, optional
		True to initialize the Kinetic Joints' displacements to zero or False to not. 
		By default is False.

	kin_config : object, optional
		A KIN_CONFIG entity.
		If omitted the whole model is assumed.

	Returns
	-------
	int
		Returns 1 on success.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def test_save_initial():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator(type="Kinematic")
		
		    kin_sim.end_time = 2.0
		
		    kin_res = kin_sim.Run()
		    kinetics.MoveByResults(kin_res, 1.0)
		
		    # save current position as initial
		    kinetics.SaveAsInitialPosition()


	"""

def MoveToInitialPosition() -> int:

	"""

	Moves the model to its initial position.

	Returns
	-------
	int
		Always returns 1.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def test_move_to_initial():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator()
		
		    # run simulation and move model by results to time 1.0
		    kin_res = kin_sim.Run()
		    time_res = kinetics.MoveByResults(kin_res, 1.0)
		
		    # move to initial positional
		    kinetics.MoveToInitialPosition()


	"""

def SavePosition(kin_config: object, name: str) -> object:

	"""

	Saves the current position as KIN_POSITION entity with the given name.

	Parameters
	----------
	kin_config : object, optional
		The KIN_CONFIG object, whose bodies' positions will be saved.
		If omitted all bodies' positions will be saved.

	name : str, optional
		The name of the KIN_POSITION entity that will be created.

	Returns
	-------
	object
		Returns a reference to the newly created KIN_POSITION object.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def test_save_position():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator()
		
		    # run simulation and move model by results to time 1.0
		    kin_res = kin_sim.Run()
		    kinetics.MoveByResults(kin_res, 1.0)
		
		    # save current position
		    pos = kinetics.SavePosition(name="simulation time 1")
		
		    kinetics.MoveToInitialPosition()
		    kinetics.MoveToPosition(pos)


	"""

def MoveToPosition(kin_pos: object) -> int:

	"""

	Moves the model to a given position.

	Parameters
	----------
	kin_pos : object
		The KIN_POSITION entity where the model will be moved to.

	Returns
	-------
	int
		Returns 1 on success.
		An exception is thrown if an invalid entity is given (not KIN_POSITION).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def test_move_to_position():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator()
		
		    # run simulation and move model by results to time 1.0
		    kin_res = kin_sim.Run()
		    kinetics.MoveByResults(kin_res, 1.0)
		
		    pos = kinetics.SavePosition("simulation time 1")
		    kinetics.MoveToInitial()
		    kinetics.MoveToPosition(pos)


	"""

def MoveByResults(kin_results: object, time: float) -> float:

	"""

	Move the model by the given kin_results to the given time.

	Parameters
	----------
	kin_results : object
		The 'KIN_RESULTS' entity where data will be extracted from.

	time : float, optional
		Move to given time. The model will be moved to the iteration 
		step of the simulation, whose reference time is closest to the given time.
		If omitted, the model will be moved to the last iteration of KIN_RESULTS.

	Returns
	-------
	float
		Returns a float representing the actual time the model moved to (see time argument above).
		An exception is thrown if invalid KIN_RESULTS entity is given or invalid time 
		(negative or greater than maximum time of KIN_RESULTS).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def test_move():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator()
		
		    # run simulation and move model by results to time 1.0
		    kin_res = kin_sim.Run()
		    time_res = kinetics.MoveByResults(kin_res, 1.0)
		
		    # print actual time that model moved
		    print(time_res)


	"""

def ResultsWriteToXML(kin_result: object, file_name: str, output_adams_view: bool, adams_name: bool) -> int:

	"""

	Exports (writes) the contents of a KIN_RESULTS entity to a XML file.

	Parameters
	----------
	kin_result : object
		A kinetics result solver.

	file_name : str
		The filepath for the output.

	output_adams_view : bool, optional
		True to output the related ADAMS/View Command file or False to not. 
		By default is False.

	adams_name : bool, optional
		Modifies the kinematic entities names according to adams hierarchy rules. 
		The default option is defined in ANSA Defaults.

	Returns
	-------
	int
		Returns 1 on success, 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import constants
		from ansa import kinetics
		
		
		def main():
		    kin_results = base.CollectEntities(constants.NASTRAN, None, "KIN_RESULTS")
		
		    for i_kin_result, kin_result in enumerate(kin_results):
		        print("now writing file number: ", i_kin_result)
		        kinetics.ResultsWriteToXML(
		            kin_result, "some_prefix_" + str(i_kin_result) + ".xml"
		        )


	"""

def TableCreate(name: str, interpolation: str, items: object) -> object:

	"""

	Creates a KIN_TABLE entity and sets the table values.

	Parameters
	----------
	name : str
		The name of the KIN_TABLE.

	interpolation : str
		The type of the interpolation. Can be 'linear', 'cubic' or 'akima'.

	items : object
		A list with the table data.

	Returns
	-------
	object
		Returns the created KIN_TABLE on success, 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import session
		from ansa import kinetics
		
		
		def main():
		    # create a new model
		    session.New("discard")
		
		    # tables to be used for data set/get
		    input_data_mat = []
		    output_data_mat = []
		
		    # fill input data
		    for i in range(0, 10):
		        input_data_mat.append([i, i * i])
		    print("\\ninput data: ")
		    print(input_data_mat)
		
		    # create a table
		    print("\\ncreating kin table: ")
		    test_kin_table = kinetics.TableCreate(
		        name="new_kin_table_name", interpolation="linear", items=input_data_mat
		    )
		
		    # print something
		    print("\\nnew kin table: ")
		    print(test_kin_table)


	"""

def TableSetData(entity: object, items: object) -> int:

	"""

	Sets the data of a KIN_TABLE. Will overwrite the data using the new list.

	Parameters
	----------
	entity : object
		A reference to a KIN_TABLE.

	items : object
		A list with the table data.

	Returns
	-------
	int
		Returns 1 on success, 0 otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import session
		from ansa import kinetics
		
		
		def main():
		    # create a new model
		    session.New("discard")
		
		    # tables to be used for data set/get
		    input_data_mat = []
		    output_data_mat = []
		
		    # fill input data
		    for i in range(0, 10):
		        input_data_mat.append([i, i * i])
		    print("\\ninput data: ")
		    print(input_data_mat)
		
		    # create a table
		    print("\\ncreating kin table: ")
		    test_kin_table = kinetics.TableCreate(
		        name="new_kin_table_name", interpolation="linear", items=input_data_mat
		    )
		
		    # print something
		    print("\\nnew kin table: ")
		    print(test_kin_table)
		
		    # get data from the table
		    print("\\ngetting kin table: ")
		    output_data_mat = kinetics.TableGetData(test_kin_table)
		
		    # print something
		    print("\\ndata in kin table: ")
		    print(output_data_mat)
		
		    # modify input data
		    input_data_mat = [[x[0], x[1] + 1] for x in input_data_mat[0:-2]]
		
		    # print something
		    print("\\nmodified input_data")
		    print(input_data_mat)
		
		    ret_val = kinetics.TableSetData(test_kin_table, input_data_mat)
		
		    print("\\nreturn value is:")
		    print(ret_val)
		
		    # get data from the table
		    print("\\ngetting kin table: ")
		    output_data_mat = kinetics.TableGetData(test_kin_table)
		
		    # print something
		    print("\\ndata in kin table: ")
		    print(output_data_mat)


	"""

def TableGetData(entity: object) -> object:

	"""

	Retrieves tha data from a KIN_TABLE.

	Parameters
	----------
	entity : object
		A reference to a KIN_TABLE.

	Returns
	-------
	object
		Returns the KIN_TABLE data as a list on success.
		Returns an empty list otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import session
		from ansa import kinetics
		
		
		def main():
		    # create a new model
		    session.New("discard")
		
		    # tables to be used for data set/get
		    input_data_mat = []
		    output_data_mat = []
		
		    # fill input data
		    for i in range(0, 10):
		        input_data_mat.append([i, i * i])
		    print("\\ninput data: ")
		    print(input_data_mat)
		
		    # create a table
		    print("\\ncreating kin table: ")
		    test_kin_table = kinetics.TableCreate(
		        name="new_kin_table_name", interpolation="linear", items=input_data_mat
		    )
		
		    # print something
		    print("\\nnew kin table: ")
		    print(test_kin_table)
		
		    # get data from the table
		    print("\\ngetting kin table: ")
		    output_data_mat = kinetics.TableGetData(test_kin_table)
		
		    # print something
		    print("\\ndata in kin table: ")
		    print(output_data_mat)


	"""

def ResultsGetData(res_entity: object, kin_entity: object) -> object:

	"""

	Gets the results for a kinetics entity from a KIN_RESULTS entity.

	Parameters
	----------
	res_entity : object
		A KIN_RESULTS entity.

	kin_entity : object
		The kinetics entity for which we need the results.

	Returns
	-------
	object
		Returns a dictionary with the results of the selected entity.
		If no results are found, the dictionary will be empty.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		from ansa import base
		
		
		def main():
		    current_kin_result = base.GetEntity(constants.NASTRAN, "KIN_RESULTS", 1)
		    current_marker = base.GetEntity(constants.NASTRAN, "KIN_MARKER", 1)
		    current_marker_result = kinetics.ResultsGetData(current_kin_result, current_marker)
		
		    for key, data in current_marker_result.items():
		        print(key)
		        print(data)


	"""

def MotionDefine(entity: object, position1: object, position2: object, direction1: object, direction2: object, along_x: str, along_y: str, along_z: str, about_x: str, about_y: str, about_z: str, function_dx: str, function_dy: str, function_dz: str, function_rx: str, function_ry: str, function_rz: str, disp_ic_dx: float, disp_ic_dy: float, disp_ic_dz: float, disp_ic_rx: float, disp_ic_ry: float, disp_ic_rz: float, vel_ic_dx: float, vel_ic_dy: float, vel_ic_dz: float, vel_ic_rx: float, vel_ic_ry: float, vel_ic_rz: float) -> object:

	"""

	Defines the data of a KIN_MOTION entity. This might be an already existing KIN_MOTION entity, 
	or one that will be created according to the entities given to the 'entity' argument.

	Parameters
	----------
	entity : object
		Alternative argument:
		a) Reference to a KIN_MOTION entity, whose motion data will be set.
		b) Reference to a KIN_JOINT entity, from which a KIN_MOTION
		   entity will be created and then its motion data will be set.
		c) A sequence (list or tuple) of two (2) KIN_BODYs, from which a KIN_MOTION
		   entity will be created and then its motion data will be set.

	position1 : object, optional
		A sequence (list or tuple) of three(3) floats to determine the position
		 of the 1st marker.

	position2 : object, optional
		A sequence (list or tuple) of three(3) floats to determine the position 
		of the 2nd marker.

	direction1 : object, optional
		A sequence (list or tuple) of three(3) floats to determine the direction 
		of the 1st marker.

	direction2 : object, optional
		A sequence (list or tuple) of three(3) floats to determine the direction 
		of the 2nd marker.

	along_x : str, optional
		'DISP', 'VEL' or 'ACC' to set the x translational motion to 
		the prescribed displacement, velocity or acceleration.

	along_y : str, optional
		'DISP', 'VEL' or 'ACC' to set the y translational motion to 
		the prescribed displacement, velocity or acceleration.

	along_z : str, optional
		'DISP', 'VEL' or 'ACC' to set the z translational motion to 
		the prescribed displacement, velocity or acceleration.

	about_x : str, optional
		'DISP', 'VEL' or 'ACC' to set the x rotational motion to the
		prescribed (rotational) displacement, velocity or acceleration.

	about_y : str, optional
		'DISP', 'VEL' or 'ACC' to set the y rotational motion to the
		prescribed (rotational) displacement, velocity or acceleration.

	about_z : str, optional
		'DISP', 'VEL' or 'ACC' to set the z rotational motion to the
		prescribed (rotational) displacement, velocity or acceleration.

	function_dx : str, optional
		The function for x translational motion.

	function_dy : str, optional
		The function for y translational motion.

	function_dz : str, optional
		The function for x translational motion.

	function_rx : str, optional
		The function for x rotational motion.

	function_ry : str, optional
		The function for y rotational motion.

	function_rz : str, optional
		The function for z rotational motion.

	disp_ic_dx : float, optional
		The x component of displacement initial condition.

	disp_ic_dy : float, optional
		The y component of displacement initial condition.

	disp_ic_dz : float, optional
		The z component of displacement initial condition.

	disp_ic_rx : float, optional
		The x component of rotational initial condition.

	disp_ic_ry : float, optional
		The y component of rotational initial condition.

	disp_ic_rz : float, optional
		The z component of rotational initial condition.

	vel_ic_dx : float, optional
		The x component of initial translational velocity.

	vel_ic_dy : float, optional
		The y component of initial translational velocity.

	vel_ic_dz : float, optional
		The z component of initial translational velocity.

	vel_ic_rx : float, optional
		The x component of initial rotational velocity.

	vel_ic_ry : float, optional
		The y component of initial rotational velocity.

	vel_ic_rz : float, optional
		The z component of initial rotational velocity.

	Returns
	-------
	object
		-If a new KIN_MOTION entity was created (cases b and c of entity - 1st argument)
		 a reference to it is returned.
		-Otherwise (case a of entity - 1st argument), returns 1 on success.
		 
		In either case, if an error occurred during motion data setup, an exception is thrown.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansan import kinetics
		
		
		def edit_motion():
		    motion = base.GetEntity(base.CurrentDeck(), "KIN_MOTION", 1)
		    ret = kinetics.MotionDefine(motion, along_z="Acc", function_dz="33")
		
		
		def create_motion_by_joint():
		    joint = base.GetEntity(base.CurrentDeck(), "KIN_JOINT", 2)
		    motion = kinetics.MotionDefine(joint, about_z="Acc", function_rz="10")
		
		
		def create_motion_by_bodies():
		    body1 = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 1)
		    body3 = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 3)
		
		    motion = kinetics.MotionDefine(
		        [body1, body3],
		        position1=(1, 1, 1),
		        direction2=[2, 3, 4],
		        about_z="Disp",
		        function_rz="120d*time",
		    )


	"""

def AddToRigidBody(body: object, elements: object, remove_from_other_body: bool) -> int:

	"""

	This function adds an element or a list of elements as part of rigid body.

	Parameters
	----------
	body : object
		The rigid body where the given element will be added to.

	elements : object
		A list of elements to be added in the rigid body.

	remove_from_other_body : bool, optional
		True to remove the added element(s) from the original rigid body (if any) 
		or False to not. By default is False.

	Returns
	-------
	int
		Returns 0 if the element/list of elements was added to BODY. 
		Otherwise, if BODY is invalid, the function returns 1.

	See Also
	--------
	RemoveFromRigidBody

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def add_1elem():
		    bd = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 2)
		    sh = base.GetEntity(base.CurrentDeck(), "SHELL", 32)
		    return kinetics.AddToRigidBody(bd, sh)
		
		
		def add_list():
		    bd = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 4)
		    sh1 = base.GetEntity(base.CurrentDeck(), "SHELL", 33)
		    sh2 = base.GetEntity(base.CurrentDeck(), "SHELL", 35)
		    return kinetics.AddToRigidBody(bd, [sh1, sh2])
		
		
		def main():
		    ret_1elem = add_1elem()
		    ret_list = add_list()
		    print(ret_1elem, ret_list)


	"""

def RemoveFromRigidBody(body: object, elements: object) -> int:

	"""

	This function removes an element or a list of elements which is or are part of a rigid body.

	Parameters
	----------
	body : object
		The rigid body that the given element/list of elements will be removed from.

	elements : object
		The element or a list of elements to remove from the rigid body.

	Returns
	-------
	int
		Returns 0 if the element/list of elements was removed from the BODY.
		If body is invalid, the function returns 1.
		If element/list of elements is invalid, the return value is 2.

	See Also
	--------
	AddToRigidBody

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # remove SHELL with id 283 from rigid body with id 3
		    body = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 3)
		    shell = base.GetEntity(base.CurrentDeck(), "SHELL", 283)
		
		    kinetics.RemoveFromRigidBody(body, shell)


	"""

def ConvertToTransformation(CONFIG: object, POSITION: object) -> int:

	"""

	This function relates the current position of a given Kinematic Configuration to another Kinematic Position.

	Parameters
	----------
	CONFIG : object
		A Kinematic Configuration whose current position is to be 
		related to POSITION.

	POSITION : object
		The name of the Kinematic Position that CONFIG's current 
		position is to be related. If "Reference Position" is given as the 
		second argument, the CONFIG's current position is related to the 
		reference position.

	Returns
	-------
	int
		Returns 0 if the transformation was calculated successfully.
		In all other cases, it may return the following 
		error codes:
		1 - CONFIG is not a Kinematic Configuration entity.
		2 - CONFIG is invalid.
		3 - POSITION was not found among existing Kinematic Position.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import constants
		from ansa import kinetics
		
		
		def main():
		    config = base.GetEntity(constants.ABAQUS, "KIN_CONFIG", 1)
		
		    # "+50 degrees inclination" is the name of a saved kinematic position
		    retCode = kinetics.ConvertToTransformation(config, "+50 degrees inclination")
		
		    # Calculate the transform relative to the reference position.
		    retCode = kinetics.ConvertToTransformation(config, None)
		    kinetics.ConvertToTransformation(config, "REFERENCE POSITION")


	"""

def SetJointStatus(JOINT: object, STATUS: str) -> str:

	"""

	This function sets the current status of a kinematic joint entity to either "LOCKED", or "UNLOCKED".
	The status of a newly created joint is set to "UNLOCKED".

	Parameters
	----------
	JOINT : object
		The reference to the kinematic joint whose status is to be set.

	STATUS : str
		Defines the desired status ("LOCKED" or "UNLOCKED").

	Returns
	-------
	str
		Returns '0' if the joint's status was altered successfully.
		Returns '1' if JOINT is invalid,'2' if JOINT is not actually a joint entity, 
		'3' if the given STATUS is neither "LOCKED" nor "UNLOCKED" and '4' if the 
		STATUS argument was not a string.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import constants
		from ansa import kinetics
		
		
		def main():
		    joint = base.GetEntity(constants.LSDYNA, "KIN_JOINT", 1)
		    kinetics.SetJointStatus(joint, "LOCKED")


	"""

def AddConfigToConfig(PARENT: object, CHILD: object) -> int:

	"""

	This function adds a kinematic configuration as child to another
	kinematic configuration. In order for the operation to succeed, CHILD
	must not be already contained to PARENT. CHILD is considered to be
	contained in PARENT, if ANY of the Kinematic Joints and Kinematic
	Configurations that CHILD contains, are already contained in PARENT
	or in any Kinematic Configuration that contains PARENT.

	Parameters
	----------
	PARENT : object
		A kinematic configuration object.

	CHILD : object
		The kinematic configuration to be added to PARENT.

	Returns
	-------
	int
		Returns 0 if CHILD was added to PARENT.
		If PARENT does not exist, the function returns 1.
		If PARENT exists, but CHILD doesn't, the function returns 2.
		Finally, if CHILD cannot be added to PARENT, the return value is 3.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # add config with id 2 to config with id 1
		    config1 = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    config2 = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 2)
		
		    kinetics.AddConfigToConfig(config1, config2)


	"""

def AddJointToConfig(CONFIG: object, JOINT: object) -> int:

	"""

	This function adds a kinematic joint to a kinematic configuration. In
	order for the operation to succeed, JOINT must not be already
	contained in CONFIG. JOINT is considered to be contained in CONFIG if
	it is one of its kinematic joints or it is contained in any kinematic
	hierarchy that also contains CONFIG.

	Parameters
	----------
	CONFIG : object
		A kinematic configuration entity, where a kinematic joint will be added to.

	JOINT : object
		The kinematic joint element to be added to the CONFIG.

	Returns
	-------
	int
		Returns 0 if JOINT was added to CONFIG.
		If CONFIG does not exist, the function returns 1.
		If CONFIG exists, but JOINT doesn't, the function returns 2.
		Finally, if JOINT cannot be added to CONFIG, the return value is 3.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # add joint with id 1 to config with id 1
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    joint = base.GetEntity(base.CurrentDeck(), "KIN_JOINT", 1)
		
		    kinetics.AddJointToConfig(config, joint)


	"""

def MoveConfig() -> object:

	"""

	This function performs the actual motion of a kinematic configuration.
	The motion parameters must be set by calling the function ConfigSetParameters, before calling this function.

	Returns
	-------
	object
		If the argument move_method of the function ConfigSetParameters is 'BY JOINT' or 'BY ACTUATOR JOINT', 
		then this function returns a 6-entries list with the amount of the performed movement for each 
		dof (the first 3 entries correspond to the translational dofs and the last 3 to the rotational ones).
		If the argument move_method of the function ConfigSetParameters is 'BY TIME' or 'BY MATCHING POINTS',
		then this function returns 1 on success.
		The function returns 0 on failure for all move methods.

	See Also
	--------
	ConfigSetParameters

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    # move configuration with id 1 by time
		    ansa.kinetics.ConfigSetParameters(kin_config=1, move_method="BY TIME", end_time=1)
		    ansa.kinetics.MoveConfig()


	"""

def ConfigSetParameters(kin_config: int, move_method: str, kin_joint: int, displacement: float, angle: float, translate_x: float, translate_y: float, translate_z: float, rotate_x: float, rotate_y: float, rotate_z: float, sp: object, tp: object, motor_joint: int, end_time: float, start_at_equilibrium: bool, step_size_type: str, step_size: float, number_of_steps: int, results_file: str, max_step_size: float, translate_x_total: float, translate_y_total: float, translate_z_total: float, rotate_x_total: float, rotate_y_total: float, rotate_z_total: float, displacement_total: float, angle_total: float, lock_translate_x: bool, lock_translate_y: bool, lock_translate_z: bool, lock_rotate_x: bool, lock_rotate_y: bool, lock_rotate_z: bool, matching_points_by_actuator_joint: bool, sp_body: object) -> int:

	"""

	This function performs the setup of the kinematic parameters for kinematic configuration motion.

	Parameters
	----------
	kin_config : int
		The id of the kinematic configuration element that motion is to be applied.
		ANSA SETs to apply mass on.

	move_method : str
		One of: "BY JOINT", "BY MATCHING POINTS", "BY ACTUATOR JOINT" or "BY TIME".
		Apply motion to a kinematic joint of a kinematic configuration
		or move a kinematic configuration by matching points or move 
		a kinematic configuration by the actuator joint or move a 
		kinematic configuration by time.

	kin_joint : int
		The id of the kinematic joint of the kinematic configuration 
		that motion is to be applied.

	displacement : float
		Amount of translation to be applied to a kinematic joint. 
		Valid only if move_method = "BY JOINT" or "BY ACTUATOR JOINT" 
		and the joint has a translational dof.

	angle : float
		Amount of rotation to be applied to a kinematic joint. 
		Valid only if move_method = "BY JOINT" or "BY ACTUATOR JOINT"
		and the joint has a rotational dof.

	translate_x : float
		Translation in 'X' axis.

	translate_y : float
		Translation in 'Y' axis.

	translate_z : float
		Translation in 'Z' axis.

	rotate_x : float
		Rotation about 'X' axis.

	rotate_y : float
		Rotation about 'Y' axis.

	rotate_z : float
		Rotation about 'Z' axis.

	sp : object
		Either the id of a node to be used as a source point or an ANSA entity. 
		Valid only if move_method = "BY MATCHING POINTS".
		The node must belong to a rigid body.

	tp : object
		Either the id of a node to be used as a target point or an ANSA entity.
		Valid only if move_method = "BY MATCHING POINTS".

	motor_joint : int
		The id of the kinematic joint that will be set 
		as the actuator joint of the kinematic configuration 
		(optional). If another kinematic joint is already 
		defined as the actuator joint of the kinematic 
		configuration, this parameter will override the 
		previous selection. Valid only if 
		move_method = "BY ACTUATOR JOINT" or 
		else if move_method = "BY MATCHING POINTS" and
		matching_points_by_actuator_joint is True.

	end_time : float
		Total simulation time.
		Valid only if move_method = "BY TIME".

	start_at_equilibrium : bool
		Valid only if move_method = "BY TIME".

	step_size_type : str
		One of: "NONE", "SIZE" or "NUMBER".
		Valid only if move_method = "BY TIME".

	step_size : float
		Valid only if move_method = "BY TIME" and
		step_size_type = "SIZE"

	number_of_steps : int
		Valid only if move_method = "BY TIME" and 
		step_size_type = "NUMBER".

	results_file : str
		Desired file name (*.xml).
		Valid only if move_method = "BY TIME".

	max_step_size : float
		Maximum step size of HHT-I3 Solver.

	translate_x_total : float
		Translation in 'X' axis (total).

	translate_y_total : float
		Translation in 'Y' axis (total).

	translate_z_total : float
		Translation in 'Z' axis (total).

	rotate_x_total : float
		Rotation about 'X' axis (total).

	rotate_y_total : float
		Rotation about 'Y' axis (total).

	rotate_z_total : float
		Rotation about 'Z' axis (total).

	displacement_total : float
		Total amount of translation to be applied to a kinematic joint.
		Valid only if "MOVE METHOD" = "BY JOINT" or "BY ACTUATOR JOINT"
		and the joint has a translational dof.

	angle_total : float
		Total amount of rotation to be applied to a kinematic joint. 
		Valid only if "MOVE METHOD" = "BY JOINT" or "BY ACTUATOR JOINT"
		and the joint has a rotational dof.

	lock_translate_x : bool, optional
		Lock translational component X of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	lock_translate_y : bool, optional
		Lock translational component Y of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	lock_translate_z : bool, optional
		Lock translational component Z of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	lock_rotate_x : bool, optional
		Lock rotational component X of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	lock_rotate_y : bool, optional
		Lock rotational component Y of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	lock_rotate_z : bool, optional
		Lock rotational component Z of actuator joint.
		Valid only if "MOVE METHOD" = "BY ACTUATOR JOINT".
		(Default: False)

	matching_points_by_actuator_joint : bool, optional
		Move by actuator joint.
		Valid only if "MOVE METHOD" = "BY MATCHING POINTS".
		(Default: False)

	sp_body : object, optional
		The KIN_BODY to which the sp belongs.
		Valid only if "MOVE METHOD" = "BY MATCHING POINTS".

	Returns
	-------
	int
		Returns 0 on success.
		An exception is thrown if more than one motions are specified for method BY JOINT or BY ACTUATOR JOINT.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		# example 1: move the kinematic joint with id 7 of the kinematic
		# configuration with id 1. The joint must have a translational dof.
		def main():
		    kinetics.ConfigSetParameters(kin_config=1, move_method="BY JOINT")
		    kinetics.ConfigSetParameters(kin_joint=7, translate_z=100.0)
		    kinetics.MoveConfig()  # performs the motion.
		
		
		# example 2: move kinematic configuration with id 3, by matching points
		def main():
		    kinetics.ConfigSetParameters(kin_config=3, move_method="BY MATCHING POINTS")
		
		    # source point id: 99, target point id: 100. Any number of source-target
		    # pair can be used.
		    kinetics.ConfigSetParameters(sp=99, tp=100)
		    kinetics.MoveConfig()  # performs the actual motion.
		
		
		# example 3: move kinematic configuration with id 1, by actuator joint.
		def main():
		    kinetics.ConfigSetParameters(
		        kin_config=1, move_method="BY ACTUATOR JOINT", rotate_z=10.0
		    )
		    kinetics.MoveConfig()  # performs the motion.
		
		
		# example 4: set the kinematic joint with id 3 to be the actuator joint of the kinematic configuration
		# with id 1, and articulate by actuator joint.
		def main():
		    kinetics.ConfigSetParameters(
		        kin_config=1, move_method="BY ACTUATOR JOINT", motor_joint=3, rotate_z=10.0
		    )
		    kinetics.MoveConfig()  # performs the motion.
		
		
		# example 5: set the move method of the kinematic configuration with id 1, set the "END TIME" equal to 20,
		# set the full path filename of the results file, and articulate by time.
		def main():
		    kinetics.ConfigSetParameters(
		        kin_config=1,
		        move_method="BY TIME",
		        end_time=20,
		        results_file="/home/user/results.xml",
		    )
		    kinetics.MoveConfig()  # performs the motion.


	"""

def MotionGetData(entity: object) -> object:

	"""

	Collects all Motion Data from the KIN_MOTION entity.

	Parameters
	----------
	entity : object
		The KIN_MOTION entity.

	Returns
	-------
	object
		Returns a dictionary with the following keys:
		along_x, along_y, along_z,
		about_x, about_y, about_z,
		function_dx, function_dy, function_dz,
		function_rx, function_ry, function_rz,
		disp_ic_dx, disp_ic_dy, disp_ic_dz,
		disp_ic_rx, disp_ic_ry, disp_ic_rz,
		vel_ic_dx, vel_ic_dy, vel_ic_dz,
		vel_ic_rx, vel_ic_ry, vel_ic_rz.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # print all KIN_MOTION entities in model
		    all_kin_motions = base.CollectEntities(base.CurrentDeck(), None, "KIN_MOTION")
		
		    for kin_motion in all_kin_motions:
		        data = kinetics.MotionGetData(kin_motion)
		        print("KIN_MOTION (ID {0})".format(kin_motion._id))
		
		        for d in data:
		            print("{0:15s} : {1}".format(d, data[d]))


	"""

def RemoveBodyFromContact(kin_contact: object, kin_body: object) -> int:

	"""

	This function removes a KIN_RBODY from a KIN_CONTACT entity.

	Parameters
	----------
	kin_contact : object
		The KIN_CONTACT entity that the given KIN_RBODY will be removed from.

	kin_body : object
		The KIN_RBODY entity to remove from the KIN_CONTACT.

	Returns
	-------
	int
		Returns 1 on success.
		An exception is raised if either entity is not valid.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    cn = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 1)
		    bd = base.GetEntity(base.CurrentDeck(), "KIN_RBODY", 7)
		    kinetics.RemoveBodyFromContact(cn, bd)


	"""

def GetBodiesFromContact(kin_contact: object) -> object:

	"""

	This function returns a list of KIN_RBODYs included in the given KIN_CONTACT.

	Parameters
	----------
	kin_contact : object
		The KIN_CONTACT whose KIN_RBODYs are requested.

	Returns
	-------
	object
		Returns a list containing the requested KIN_RBODY entities, on success. 
		If none of them are included in the defined KIN_CONTACT, the function returns an empty list.
		An exception is raised if the argument is invalid.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get bodies of kin_contact with id 1 and print their IDs
		    cn = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 1)
		    bodies = kinetics.GetBodiesFromContact(cn)
		    for body in bodies:
		        print(base.GetEntityCardValues(base.CurrentDeck(), body, ["EID"])["EID"])


	"""

def AddExcludedToContact(kin_contact: object, elements: object) -> int:

	"""

	This function adds the given elements as excluded to the given KIN_CONTACT.

	Parameters
	----------
	kin_contact : object
		The KIN_CONTACT entity where elements will be added as excluded.

	elements : object
		A list of ANSA entities to be added as excluded to the KIN_CONTACT.

	Returns
	-------
	int
		Returns 1 on success. An exception is raised if either argument is invalid 
		(KIN_CONTACT & list). If any of the list items is not a valid, a warning message 
		is printed, but the procedure is continued.

	Examples
	--------
	::

		import ansa
		
		
		def main():
		    # add shells with ids 34 & 35 as excluded to contact with id 1
		    cn = ansa.base.GetEntity(ansa.base.CurrentDeck(), "KIN_CONTACT", 1)
		    sh1 = ansa.base.GetEntity(ansa.base.CurrentDeck(), "SHELL", 34)
		    sh2 = ansa.base.GetEntity(ansa.base.CurrentDeck(), "SHELL", 35)
		    ansa.kinetics.AddExcludedToContact(cn, [sh1, sh2])


	"""

def ClearContact(kin_contact: object, only_excluded: bool) -> int:

	"""

	This functions clears all the entities of a KIN_CONTACT entity, or clears only the exluded entities.
	NOTICE: the KIN_CONTACT entity is not deleted.

	Parameters
	----------
	kin_contact : object
		The KIN_CONTACT entity, whose entities will be removed.

	only_excluded : bool, optional
		If True, the function clears only the excluded entities.

	Returns
	-------
	int
		Returns 1 on success.
		An exception is raised if kin_contact (1st argument) is invalid.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def clear_all():
		    # clear all entities of KIN_CONTACT with id 1
		    cn = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 1)
		    kinetics.ClearContact(cn)
		
		
		def clear_only_excl():
		    # clear only excluded entities of KIN_CONTACT with id 2
		    cn = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 2)
		    kinetics.ClearContact(cn, True)


	"""

def ContactBodySetData(kin_contact: object, kin_body: object, shape: str, thickness: float, thickness_scale: float, smooth_subdiv_lev: int, smooth_feat_ang: float) -> int:

	"""

	This function sets the KIN_RBODY's data in a KIN_CONTACT, such as shape, thickness etc.

	Parameters
	----------
	kin_contact : object
		A reference to a 'KIN_CONTACT" object, where the "KIN_RBODY" belongs.

	kin_body : object
		A reference to the "KIN_RBODY" object, whose data will be modified.

	shape : str, optional
		The "KIN_RBODY" shape.
		Can be on eof the following:
		"Simplified Concave", "Convex", "Box", "Cylinder", 
		"Sphere", "Smooth" or "Concave".

	thickness : float, optional
		The thickness (like with ~ from GUI).

	thickness_scale : float, optional
		The thickness scale (like with no ~ from GUI).

	smooth_subdiv_lev : int, optional
		Subdivision level for smooth shape (between 1 and 10).

	smooth_feat_ang : float, optional
		Feature angle for smooth shape (between 0 and 180).

	Returns
	-------
	int
		Returns 1 on success.
		An exception is raised if any argument has invalid type or invalid values, 
		or if KIN_RBODY does not belong to KIN_CONTACT.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    cn = base.GetEntity(base.CurrentDeck(), "KIN_CONTACT", 1)
		    bodies = kinetics.GetBodiesFromContact(cn)
		    # set 1st body's thickness and set 2nd body's shape to smooth and feature angle
		    kinetics.ContactBodySetData(cn, bodies[0], thickness=2.3)
		    kinetics.ContactBodySetData(cn, bodies[1], shape="Smooth", smooth_feat_ang=80)


	"""

def GetModelInfo(kin_config: object) -> object:

	"""

	Gets the model info of Configurator or Whole Model.

	Parameters
	----------
	kin_config : object, optional
		A KIN_CONFIG entity.
		If omitted the whole model is assumed.

	Returns
	-------
	object
		This function returns a dictionary with keywords:
		    "rigid_bodies"              : number of Rigid Bodies
		    "joints"                    : number of Joints
		    "dependent_body_dofs"       : number of Dependent Body Dofs
		    "dependent_constraint_dofs" : number of Dependent Constraint Dofs
		    "redundant_constraints"     : number of Redundant Constraints
		    "independent_constraints"   : number of Independent Constraints
		    "dofs"                      : number of Dofs
		    "dofs_augment"              : number of Dofs (augment)
		
		An exception is raised if an invalid entity is given.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get model info of configurator with id 1
		    kin_config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    res1 = kinetics.GetModelInfo(kin_config)
		    print(res1)
		
		    # get model info of whole model
		    res2 = kinetics.GetModelInfo()
		    print(res2)


	"""

def GetJointsFromConfig(kin_config: object) -> object:

	"""

	This function returns a list of KIN_JOINTs included in the given KIN_CONFIG.

	Parameters
	----------
	kin_config : object
		The KIN_CONFIG whose KIN_JOINTs are requested.

	Returns
	-------
	object
		Returns a list containing references to the KIN_JOINT objects found.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get joints of kin_config with id 1 and print their IDs
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    joints = kinetics.GetJointsFromConfig(config)
		    for joint in joints:
		        print(joint._id)


	"""

def RemoveJointFromConfig(kin_config: object, kin_joint: object) -> int:

	"""

	Removes a KIN_JOINT from a KIN_CONFIG.

	Parameters
	----------
	kin_config : object
		The KIN_CONFIG object.

	kin_joint : object
		The KIN_JOINT to be removed from the KIN_CONFIG.

	Returns
	-------
	int
		Returns 1 on success.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # remove KIN_JOINT with id 2 from KIN_CONFIG with id 1
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    joint = base.GetEntity(base.CurrentDeck(), "KIN_JOINT", 2)
		
		    kinetics.RemoveJointFromConfig(config, joint)


	"""

def ConfigsJointSetStatus(kin_config: object, kin_joint: object, locked: bool) -> int:

	"""

	Sets the status (locked/unlocked) of a "KIN_JOINT" in a "KIN_CONFIG".

	Parameters
	----------
	kin_config : object
		A reference to the "KIN_CONFIG" object.

	kin_joint : object
		A reference to the "KIN_JOINT" object of the "KIN_CONFIG", 
		to set its status as locked or unlocked.

	locked : bool
		True: Set status as locked.
		False: Set status as unlocked.

	Returns
	-------
	int
		Returns 1 on success and 0 on failure.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # lock KIN_JOINT with id 3 in KIN_CONFIG with id 1
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    joint = base.GetEntity(base.CurrentDeck(), "KIN_JOINT", 3)
		
		    kinetics.ConfigsJointSetStatus(config, joint, True)


	"""

def ConfigsJointIsLocked(kin_config: object, kin_joint: object) -> bool:

	"""

	Checks if KIN_JOINT of KIN_CONFIG is locked.

	Parameters
	----------
	kin_config : object
		A reference to the "KIN_CONFIG" object to check.

	kin_joint : object
		A reference to the "KIN_JOINT" object of the defined "KIN_CONFIG".

	Returns
	-------
	bool
		Returns True if "KIN_JOINT" of "KIN_CONFIG" is locked, False otherwise.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # check if KIN_JOINT with id 3 in KIN_CONFIG with id 1 is locked
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    joint = base.GetEntity(base.CurrentDeck(), "KIN_JOINT", 3)
		
		    if kinetics.ConfigsJointIsLocked(config, joint):
		        print("KIN_JOINT is locked")
		    else:
		        print("KIN_JOINT is unlocked")


	"""

def AddForceToConfig(CONFIG: object, FORCE: object) -> int:

	"""

	This function adds a kinematic force to a kinematic configuration. In
	order for the operation to succeed, FORCE must not be already
	contained in CONFIG. FORCE is considered to be contained in CONFIG if
	it is one of its kinematic forces or it is contained in any kinematic
	hierarchy that also contains CONFIG.

	Parameters
	----------
	CONFIG : object
		A kinematic configuration entity that a kinematic force will be added to.

	FORCE : object
		The kinematic force to be added to the CONFIG.

	Returns
	-------
	int
		Returns 0 if FORCE was added to CONFIG.
		If CONFIG does not exist, the function returns 1.
		If CONFIG exists, but FORCE doesn't, the function returns 2.
		Finally, if FORCE cannot be added to CONFIG, the return value is 3.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # add force with id 1 to config with id 2
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 2)
		    force = base.GetEntity(base.CurrentDeck(), "KIN_FORCE", 1)
		
		    kinetics.AddForceToConfig(config, force)


	"""

def ConvertPosition(position: object, conversion_type: str, output_directory: str, locations_type: str, velocities_type: str, sets_type: str, use_position_name: bool, position_prefix_name: str, include_transform_file_name: str, include_trasform_full_path_names: bool, morph_nodes_file_name: str, output_kinetics: bool, deformed_bodies: object, include_transform_enable_file: bool, morph_nodes_enable_file: bool, output_parameters: bool, parameters_file_name: str, reference_position: object, output_foam_ref_geom: bool, create_folders: bool) -> int:

	"""

	The function performs the conversion of Rigid Bodies locations and initial velocities 
	to keywords that are written in deck files. It also takes into account possible 
	deformed bodies through the Dummy Seat depenetration tool as long as the corresponding 
	nodes hold initial foam keywords, and also possible morphed nodes that have been 
	produced through the Kinematics-Morph coupling of ANSA.

	Parameters
	----------
	position : object
		LSDYNA: Output *INITIAL_FOAM_REFERENCE_GEOMETRY keywords. 
		The default option is defined in ANSA Defaults.

	conversion_type : str
		The conversion type.
		Available options: 'locations', 'velocities', 'both'.

	output_directory : str
		The directory where the files will be written out.

	locations_type : str, optional
		The available options are:
		LS-DYNA:  '*DEFINE_TRANSFORMATION', '*NODE'
		PAMCRASH: 'TRSFM /', 'NODE /'.
		ABAQUS:   '*NMAP', '*NODE'
		RADIOSS:  '/TRANSFORM', '/NODE'.
		The default option is defined in ANSA Defaults.

	velocities_type : str, optional
		The available options are:
		LSDYNA: '*INITIAL_VELOCITY_SET', 
		        '*INITIAL_VELOCITY_GENERATION',
		        '*INITIAL_VELOCITY_NODE'.
		PAMCRASH: 'INVEL_SET /', 'INVEL_RIGID /', 'INVEL_NODE /'.
		ABAQUS: 'ROTVEL,SET', 'ROTATING_VELOCITY', 'ROTVEL,NODE'.
		RADIOSS: '/INIVEL_SET', '/INIVEL_NODE'.
		The default option is defined in ANSA Defaults.

	sets_type : str, optional
		The available options are:
		LSDYNA: '*SET_NODE_LIST', '*SET_NODE_GENERAL'.
		PAMCRASH: 'NODE', 'GENERAL'.
		The default option is defined in ANSA Defaults.

	use_position_name : bool, optional
		Use Position's name as prefix for the created file. 
		The default option is defined in ANSA Defaults.

	position_prefix_name : str, optional
		The prefix to be used for the created file.
		The default option is defined in ANSA Defaults.

	include_transform_file_name : str, optional
		LSDYNA: The name of the separate file to write out
		the *INCLUDE_TRANSFORM keywords. 
		The default option is defined in ANSA Defaults.

	include_trasform_full_path_names : bool, optional
		LSDYNA: If a Rigid Body contains an *INCLUDE, 
		the corresponding *INCLUDE_TRANSFORM that 
		is going to be created will written out by using 
		its FullPathName.
		The default option is defined in ANSA Defaults.

	morph_nodes_file_name : str, optional
		The name of the separate file to write out the 
		morphed nodes.
		The default option is defined in ANSA Defaults.

	output_kinetics : bool, optional
		Output as ANSA comments the participating 
		Kinetic entities.
		The default option is defined in ANSA Defaults.

	deformed_bodies : object, optional
		A list that contains the names of the Rigid 
		Bodies that have been deformed through
		the Dummy-Seat Depenetration tool and 
		their nodes hold initial foam keywords.
		For each of those nodes a set will be written 
		out and the corresponding transformation keyword.

	include_transform_enable_file : bool, optional
		LSDYNA: Output *INCLUDE_TRANSFORM 
		keywords in a separate file. In case there are 
		Rigid Bodies that contain *INCLUDEs.
		The default option is defined in ANSA Defaults.

	morph_nodes_enable_file : bool, optional
		Output Morphed Nodes in a separate file.
		The default option is defined in ANSA Defaults.

	output_parameters : bool, optional
		Output parameters for transformation keywords values.
		The default option is defined in ANSA Defaults.

	parameters_file_name : str, optional
		The name of the separate file to write out the parameters.
		The default option is defined in ANSA Defaults.

	reference_position : object, optional
		The reference position object. The conversion will be done
		relative to this.

	output_foam_ref_geom : bool, optional
		LSDYNA: Output *INITIAL_FOAM_REFERENCE_GEOMETRY keywords. 
		The default option is defined in ANSA Defaults.

	create_folders : bool, optional
		This option is only available in single KIN_POSITION selection. (default is True)

	Returns
	-------
	int
		Returns 1 on success, 0 on failure. 
		In case of a list of KIN_POSITION objects is used for the position argument, the function returns 2 when at least one KIN_POSITION is not converted successfully (partial success).

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import constants
		from ansa import kinetics
		
		
		def convert_position():
		    kin_position = base.GetEntity(constants.LSDYNA, "KIN_POSITION", 1)
		    error = kinetics.ConvertPosition(
		        position=kin_position,
		        conversion_type="locations",
		        output_directory="/home/user/tests",
		        locations_type="*DEFINE_TRANSFORMATION",
		        use_position_name=True,
		        morph_nodes_file_name="Morphed.key",
		        output_kinetics=True,
		    )
		    return error


	"""

def Dy(to_marker: str, from_marker: str, along_marker: str) -> float:

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.

	Parameters
	----------
	to_marker : str
		The name or the id of the 'to_marker'.

	from_marker : str, optional
		The name or the id of the 'from_marker'.

	along_marker : str, optional
		The name or the id of the 'along_marker'.

	Returns
	-------
	float
		Returns the distance along Y (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    distance_along_y = kinetics.Dy("1", "2", "3")


	"""

def Yaw(to_marker: str, from_marker: str) -> float:

	"""

	Gets the first angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence 
	from the coordinate system of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		The name or the id of the 'to_marker'.

	from_marker : str, optional
		The name or the id of the 'from_marker'.

	Returns
	-------
	float
		Returns the first angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    first_angle_of_euler_321_sequence = kinetics.Yaw("1", "2")


	"""

def Pitch(to_marker: str, from_marker: str) -> float:

	"""

	Gets the second angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the second angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    second_angle_of_euler_321_sequence = kinetics.Pitch("1", "2")


	"""

def Roll(to_marker: str, from_marker: str) -> float:

	"""

	Gets the third angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the third angle of a body-fixed 3-2-1 (yaw-pitch-roll) Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    third_angle_of_euler_321_sequence = kinetics.Roll("1", "2")


	"""

def Psi(to_marker: str, from_marker: str) -> float:

	"""

	Gets the first angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the first angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    first_angle_of_euler_313_sequence = kinetics.Psi("1", "2")


	"""

def Theta(to_marker: str, from_marker: str) -> float:

	"""

	Gets the second angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate 
	system of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the second angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    second_angle_of_euler_313_sequence = kinetics.Theta("1", "2")


	"""

def Phi(to_marker: str, from_marker: str) -> float:

	"""

	Gets the third angle of a body-fixed 3-1-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the third angle of a body-fixed 3-1-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    third_angle_of_euler_313_sequence = kinetics.Phi("1", "2")


	"""

def B1(to_marker: str, from_marker: str) -> float:

	"""

	Gets the first angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the first angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    first_angle_of_euler_123_sequence = kinetics.B1("1", "2")


	"""

def B2(to_marker: str, from_marker: str) -> float:

	"""

	Gets the second angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the second angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    second_angle_of_euler_123_sequence = kinetics.B2("1", "2")


	"""

def B3(to_marker: str, from_marker: str) -> float:

	"""

	Gets the third angle of a body-fixed 1-2-3 Euler rotation sequence from the coordinate system 
	of 'from_marker' to the coordinate system of 'to_marker'.

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns the third angle of a body-fixed 1-2-3 Euler rotation sequence (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    third_angle_of_euler_123_sequence = kinetics.B3("1", "2")


	"""

def Orient(orientation_system: float, component: float, to_marker: str, from_marker: str) -> float:

	"""

	Gets a rotational value between two markers, from the coordinate system of 'from_marker' 
	to the coordinate system of 'to_marker'. This value is defined with respect to the 
	selected orientation system and component.
	
	- orientation_system: 1 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-2-3 Euler rotation sequence respectively.
	- orientation_system: 2 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-3-1 Euler rotation sequence respectively.
	- orientation_system: 3 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-1-2 Euler rotation sequence respectively.
	- orientation_system: 4 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-3-2 Euler rotation sequence respectively.
	- orientation_system: 5 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-1-3 Euler rotation sequence respectively.
	- orientation_system: 6 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-2-1 Euler rotation sequence respectively.
	- orientation_system: 7 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-2-1 Euler rotation sequence respectively.
	- orientation_system: 8 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 1-3-1 Euler rotation sequence respectively.
	- orientation_system: 9 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-1-2 Euler rotation sequence respectively.
	- orientation_system: 10 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 2-3-2 Euler rotation sequence respectively.
	- orientation_system: 11 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-1-3 Euler rotation sequence respectively.
	- orientation_system: 12 - component: 1, 2, 3
	   Gets the first, second or third angle of a body-fixed 3-2-3 Euler rotation sequence respectively.
	- orientation_system: 13 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-2-3 Euler rotation sequence respectively.
	- orientation_system: 14 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-3-1 Euler rotation sequence respectively.
	- orientation_system: 15 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-1-2 Euler rotation sequence respectively.
	- orientation_system: 16 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-3-2 Euler rotation sequence respectively.
	- orientation_system: 17 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-1-3 Euler rotation sequence respectively.
	- orientation_system: 18 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-2-1 Euler rotation sequence respectively.
	- orientation_system: 19 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-2-1 Euler rotation sequence respectively.
	- orientation_system: 20 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 1-3-1 Euler rotation sequence respectively.
	- orientation_system: 21 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-1-2 Euler rotation sequence respectively.
	- orientation_system: 22 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 2-3-2 Euler rotation sequence respectively.
	- orientation_system: 23 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-1-3 Euler rotation sequence respectively.
	- orientation_system: 24 - component: 1, 2, 3
	   Gets the first, second or third angle of a space-fixed 3-2-3 Euler rotation sequence respectively.
	- orientation_system: 25 - component: 1, 2, 3
	   Gets ansa.kinetics.Ax(to_marker, from_marker), ansa.kinetics.Ay(to_marker, from_marker) or 
	   ansa.kinetics.Az(to_marker, from_marker) respectively.
	- orientation_system: 26 - component: 1, 2, 3
	   Gets ansa.kinetics.Yaw(to_marker, from_marker), ansa.kinetics.Pitch(to_marker, from_marker) or 
	   ansa.kinetics.Roll(to_marker, from_marker) respectively.
	- orientation_system: 27 - component: 1, 2, 3, 4
	   Gets the first, second, third ot fourth euler parameter respectively.
	- orientation_system: 28 - component: 1, 2, 3
	   Gets the first, second or third rodriguez parameter respectively.
	- orientation_system: 29 - component: 1, 2, 3, 4, 5, 6, 7, 8, 9
	   XiYiZi the coordinate system of 'to marker'
	   XYZ    the coordinate system of 'from marker'
	   component: 1, 2, 3: Gets the direction cosine of Xi axis with respect to X, Y, Z axis respectively. 
	   component: 4, 5, 6: Gets the direction cosine of Yi axis with respect to X, Y, Z axis respectively.
	   component: 7, 8, 9: Gets the direction cosine of Zi axis with respect to X, Y, Z axis respectively.

	Parameters
	----------
	orientation_system : float
		A value that specifies the orientation system.
		(value: between 1 - 29)

	component : float
		A value that specifies the rotation value to be computed.

	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	Returns
	-------
	float
		Returns a rotational value between 'from_marker' and 'to_marker' (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    rotation_between_two_markers = kinetics.Orient(1, 3, "1", "2")


	"""

def Accx(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Acceleration along X (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    acceleration_along_x3 = kinetics.Accx("1", "2", "3", "4")


	"""

def Accy(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the Y direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Acceleration along Y (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    acceleration_along_y3 = kinetics.Accy("1", "2", "3", "4")


	"""

def Accz(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the acceleration from 'from_marker' to 'to_marker' in the Z direction, along the 'along_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Acceleration along Z (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    acceleration_along_z3 = kinetics.Accz("1", "2", "3", "4")


	"""

def Accm(to_marker: str, from_marker: str, reference_marker: str) -> float:

	"""

	Gets the magnitude of the acceleration from 'from_marker' to 'to_marker'.
	All accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Acceleration magnitude (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    acceleration_mag = kinetics.Accm("1", "2", "4")


	"""

def Wdtx(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the X direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the angular acceleration about X (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    aacc_about_x3 = kinetics.Wdtx("1", "2", "3", "4")


	"""

def Wdty(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the Y direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the angular acceleration about Y (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    aacc_about_y3 = kinetics.Wdty("1", "2", "3", "4")


	"""

def Wdtz(to_marker: str, from_marker: str, along_marker: str, reference_marker: str) -> float:

	"""

	Gets the angular acceleration from 'from_marker' to 'to_marker' about the Z direction of the 'along_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	along_marker : str, optional
		Name or id of the 'along_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the angular acceleration about Z (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    aacc_about_z3 = kinetics.Wdtz("1", "2", "3", "4")


	"""

def Wdtm(to_marker: str, from_marker: str, reference_marker: str) -> float:

	"""

	Gets the magnitude of the angular acceleration from 'from_marker' to 'to_marker'.
	All angular accelerations are taken in the 'reference_marker' coordinate system. 

	Parameters
	----------
	to_marker : str
		Name or id of the 'to_marker'.

	from_marker : str, optional
		Name or id of the 'from_marker'.

	reference_marker : str, optional
		Name or id of the 'reference_marker'.

	Returns
	-------
	float
		Returns the angular acceleration magnitude (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    angular_acceleration_mag = kinetics.Wdtm("1", "2", "4")


	"""

def Varval(algebraic_variable: str) -> float:

	"""

	Gets the current value of a variable.

	Parameters
	----------
	algebraic_variable : str
		Name or id of the 'algebraic_variable'.

	Returns
	-------
	float
		Returns the current value of a variable (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    variable_value = kinetics.Varval("1")


	"""

def Senval(sensor: str) -> float:

	"""

	Gets the current value of a sensor.

	Parameters
	----------
	sensor : str
		Name or id of the 'sensor'.

	Returns
	-------
	float
		Returns the current value of a sensor (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    sensor_value = kinetics.Senval("1")


	"""

def Joint(joint: str, computed_at_marker: str, component: str, ref_marker: str) -> float:

	"""

	Gets the component of a JOINT force/torque as calculated in the coordinate system of marker 'ref_marker'.

	Parameters
	----------
	joint : str
		Name or id of the joint under consideration.

	computed_at_marker : str
		Value that defines the joint-marker at which the joint-force will be calculated.
		If 0: marker I
		If 1: marker J

	component : str
		Value that defines the component of the joint-force.
		If 1: FM (Force Magnitude)
		If 2: Fx
		If 3: Fy
		If 4: Fz
		If 5: TM (Torque Magnitude)
		If 6: Tx
		If 7: Ty
		If 8: Tz

	ref_marker : str
		Name or id of the 'ref_marker'.

	Returns
	-------
	float
		Returns a component of a JOINT force/torque (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    comp_of_joint_force_torque = kinetics.Joint("1", "0", "1", "0")


	"""

def Jprim(jprim: str, computed_at_marker: str, component: str, ref_marker: str) -> float:

	"""

	Gets the component of a JPRIM (Joint PRIMitive) force/torque as calculated in the coordinate system of marker 'ref_marker'.

	Parameters
	----------
	jprim : str
		Name or id of the jprim under consideration.

	computed_at_marker : str
		Value that defines the jprim-marker at which the jprim-force will be calculated.
		If 0: marker I
		If 1: marker J

	component : str
		Value that defines the component of the jprim-force.
		If 1: FM (Force Magnitude)
		If 2: Fx
		If 3: Fy
		If 4: Fz
		If 5: TM (Torque Magnitude)
		If 6: Tx
		If 7: Ty
		If 8: Tz

	ref_marker : str
		Name or id of the 'ref_marker'.

	Returns
	-------
	float
		Returns a component of a JPRIM force/torque (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    comp_of_jprim_force_torque = kinetics.Jprim("1", "0", "1", "0")


	"""

def Ptcv(ptcv: str, computed_at_marker: str, component: str, ref_marker: str) -> float:

	"""

	Gets the component of a PTCV (Point-To-Curve Constraint) force/torque as calculated in the coordinate 
	system of marker 'ref_marker'.

	Parameters
	----------
	ptcv : str
		Name or id of the ptcv under consideration.

	computed_at_marker : str
		A value that defines the ptcv-marker at which the ptcv-force will be calculated.
		If 0: marker I.
		If 1: marker J.

	component : str
		A value that defines the component of the ptcv-force.
		If 1: FM (Force Magnitude).
		If 2: Fx.
		If 3: Fy.
		If 4: Fz.
		If 5: TM (Torque Magnitude).
		If 6: Tx.
		If 7: Ty.
		If 8: Tz.

	ref_marker : str
		Name or id of the 'ref_marker'.

	Returns
	-------
	float
		Returns a component of a PTCV force/torque (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    comp_of_ptcv_force_torque = kinetics.Ptcv("1", "0", "1", "0")


	"""

def Motion(motion: str, computed_at_marker: str, component: str, ref_marker: str) -> float:

	"""

	Gets the component of a MOTION force/torque as calculated in the coordinate system of marker 'ref_marker'.

	Parameters
	----------
	motion : str
		Name or id of the motion under consideration.

	computed_at_marker : str
		A value that defines the motion-marker at which the motion-force will be calculated.
		If 0: marker I
		If 1: marker J

	component : str
		A value that defines the component of the motion-force.
		If 1: FM (Force Magnitude)
		If 2: Fx
		If 3: Fy
		If 4: Fz
		If 5: TM (Torque Magnitude)
		If 6: Tx
		If 7: Ty
		If 8: Tz

	ref_marker : str
		Name or id of the 'ref_marker'.

	Returns
	-------
	float
		Returns a component of a MOTION force/torque (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    comp_of_motion_force_torque = kinetics.Motion("1", "0", "1", "0")


	"""

def Force(force: str, computed_at_marker: str, component: str, ref_marker: str) -> float:

	"""

	Gets a component of a 'force' as calculated in the coordinate system of marker 'ref_marker'.
	The force entity can be: BEAM, BUSH, FIELD, SPRING-DAMPER, SFORCE, VFORCE, VTORQUE, GFORCE.

	Parameters
	----------
	force : str
		Name or id of the 'force' under consideration.

	computed_at_marker : str
		Value that defines the force-marker at which the force will be calculated.
		If 0: marker I.
		If 1: marker J.

	component : str
		Value that defines the component of the force.
		If 1: FM (Force Magnitude).
		If 2: Fx.
		If 3: Fy.
		If 4: Fz.
		If 5: TM (Torque Magnitude).
		If 6: Tx.
		If 7: Ty.
		If 8: Tz.

	ref_marker : str
		Name or id of the 'ref_marker'.

	Returns
	-------
	float
		Returns a component of 'force' (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    comp_of_force = kinetics.Force("1", "0", "1", "2")


	"""

def Akispl(x: float, z: float, kin_table: str, deriv_order: str) -> float:

	"""

	Applies the Akima method of interpolation on the 'kin_table' and gets the iord derivative 
	of the interpolated value. In case of a three dimensional 'kin_table', the interpolation 
	in the x-direction is of Akima type while in the z-direction is linear.

	Parameters
	----------
	x : float
		First independent variable along x-axis, according to 
		which the Akispl function interpolates y.

	z : float
		Second independent variable along z-axis, according to 
		which the Akispl function interpolates y.

	kin_table : str
		The id of the 'kin_table'.

	deriv_order : str, optional
		The order of derivation that is taken into account during the 
		interpolation of 'kin_table'. Range: 0 <= 'deriv_order' <= 2.
		Default: 0 (take no derivative).

	Returns
	-------
	float
		Returns the iord derivative of the interpolated value (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    akima_interpol_value = kinetics.Akispl(time, 0, "1", "1")


	"""

def Cubspl(x: float, z: float, kin_table: str, deriv_order: str) -> float:

	"""

	Applies the Cubic method of interpolation on the 'kin_table' and gets the iord derivative of the interpolated value.
	In case of a three dimensional 'kin_table', the interpolation in the x-direction is of Cubic type while in the z-direction is linear.

	Parameters
	----------
	x : float
		First independent variable along x-axis, according to which 
		the Cubspl function interpolates y.

	z : float
		Second independent variable along z-axis, according to which 
		the Cubspl function interpolates y.

	kin_table : str
		The id of the 'kin_table'.

	deriv_order : str, optional
		The order of derivation that is taken into account during the 
		interpolation of 'kin_table'.
		Range: 0 <= 'deriv_order' <= 2.
		(Default: 0 (takes no derivative))

	Returns
	-------
	float
		Retrusn the iord derivative of the interpolated value (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    cubic_interpol_value = kinetics.Cubspl(time, 0, "1", "1")


	"""

def Interp(time: float, degree: str, kin_table: str, deriv_order: str) -> float:

	"""

	Evaluates the iord derivative of the interpolated value of the 'kin_table' at time.
	Supports only time-series splines.
	The applied method of interpolation, depends on the value of 'degree'.

	Parameters
	----------
	time : float
		The independent variable along the x-axis of the time-series spline, 
		according to which the Interp function interpolates y.

	degree : str
		A value that specifies the degree of interpolation. 
		If 1: performs linear interpolation.
		If 3: performs cubic interpolation.

	kin_table : str
		The id of the 'kin_table'.
		The 'kin_table' must reference time-series data.

	deriv_order : str, optional
		The order of derivation that is taken into account during the 
		interpolation of the 'kin_table'.
		Range: 0 <= 'deriv_order' <= 2.
		(Default: 0 (take no derivative))

	Returns
	-------
	float
		Returns the iord derivative of the interpolated value (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    interpol_value = kinetics.Interp(time, "3", "1", "0")


	"""

def Poly(x: float, x0: float, a0: float, a1: float, a2: float, a3: float, a4: float, a5: float, a6: float, a7: float, a8: float, a9: float, a10: float, a11: float, a12: float, a13: float, a14: float, a15: float, a16: float, a17: float, a18: float, a19: float, a20: float, a21: float, a22: float, a23: float, a24: float, a25: float, a26: float, a27: float, a28: float, a29: float, a30: float) -> float:

	"""

	Evaluates a standard polynomial at a user-specified value x.
	Polynomial:
	  P(x) = a0 + a1 * (x - x0) + a2 * (x - x0)^2 + ... + a30 * (x - x0)^30

	Parameters
	----------
	x : float
		The independent variable.

	x0 : float
		A value that specifies a shift in the polynomial.

	a0 : float, optional
		1st coefficient for the polynomial series.

	a1 : float, optional
		2nd coefficient for the polynomial series.

	a2 : float, optional
		3rd coefficient for the polynomial series.

	a3 : float, optional
		4th coefficient for the polynomial series.

	a4 : float, optional
		5th coefficient for the polynomial series.

	a5 : float, optional
		6th coefficient for the polynomial series.

	a6 : float, optional
		7th coefficient for the polynomial series.

	a7 : float, optional
		8th coefficient for the polynomial series.

	a8 : float, optional
		9th coefficient for the polynomial series.

	a9 : float, optional
		10th coefficient for the polynomial series.

	a10 : float, optional
		11th coefficient for the polynomial series.

	a11 : float, optional
		12th coefficient for the polynomial series.

	a12 : float, optional
		13th coefficient for the polynomial series.

	a13 : float, optional
		14th coefficient for the polynomial series.

	a14 : float, optional
		15th coefficient for the polynomial series.

	a15 : float, optional
		16th coefficient for the polynomial series.

	a16 : float, optional
		17th coefficient for the polynomial series.

	a17 : float, optional
		18th coefficient for the polynomial series.

	a18 : float, optional
		19th coefficient for the polynomial series.

	a19 : float, optional
		20th coefficient for the polynomial series.

	a20 : float, optional
		21st coefficient for the polynomial series.

	a21 : float, optional
		22nd coefficient for the polynomial series.

	a22 : float, optional
		23rd coefficient for the polynomial series.

	a23 : float, optional
		24th coefficient for the polynomial series.

	a24 : float, optional
		25th coefficient for the polynomial series.

	a25 : float, optional
		26th coefficient for the polynomial series.

	a26 : float, optional
		27th coefficient for the polynomial series.

	a27 : float, optional
		28th coefficient for the polynomial series.

	a28 : float, optional
		29th coefficient for the polynomial series.

	a29 : float, optional
		30th coefficient for the polynomial series.

	a30 : float, optional
		31st coefficient for the polynomial series.

	Returns
	-------
	float
		Returns the value of the polynomial (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    polynomial_value = kinetics.Poly(time, 0, 1, 1)


	"""

def IncAng(first_marker: str, middle_marker: str, last_marker: str) -> float:

	"""

	Gets the included angle between the line defined by 'first_marker' and 'middle_marker' and the line 
	defined by 'middle_marker' and 'last_marker'.

	Parameters
	----------
	first_marker : str
		Name or id of the 'first_marker'.

	middle_marker : str
		Name or id of the 'middle_marker'.

	last_marker : str
		Name or id of the 'last_marker'.

	Returns
	-------
	float
		Returns an angle (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    angle = kinetics.IncAng("1", "2", "3")


	"""

def Dx(to_marker: str, from_marker: str, along_marker: str) -> float:

	"""

	Gets the distance from 'from_marker' to 'to_marker' in the X direction, along the 'along_marker'.

	Parameters
	----------
	to_marker : str
		The name or the id of the 'to_marker'.

	from_marker : str, optional
		The name or the id of the 'from_marker'.

	along_marker : str, optional
		The name or the id of the 'along_marker'.

	Returns
	-------
	float
		Returns the distance along X (scalar).

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    distance_along_x = kinetics.Dx("1", "2", "3")


	"""

def GetArticulationHistoryFromConfig(kin_config: object) -> object:

	"""

	This function returns a list of the articulation history of the given KIN_CONFIG.

	Parameters
	----------
	kin_config : object
		The KIN_CONFIG whose articulation history is requested.

	Returns
	-------
	object
		Returns a list containing the articulation history.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get articulation history of kin_config with id 1 and print it
		    config = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 1)
		    history = kinetics.GetArticulationHistoryFromConfig(config)
		    print(history)


	"""

def GetMarkers(kin_entity: object) -> object:

	"""

	This function returns a list of KIN_MARKERs of a Kinetic Entity, such as KIN_BODY, KIN_FORCE, KIN_JOINT, KIN_MOTION, KIN_GRAPHIC, KIN_MEASURE and KIN_REQUEST.

	Parameters
	----------
	kin_entity : object
		The Kinetic Entity whose KIN_MARKERs are requested.

	Returns
	-------
	object
		Returns a list containing references to the KIN_MARKER objects found.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get markers of kin_body with id 1 and print their IDs
		    body = base.GetEntity(base.CurrentDeck(), "KIN_BODY", 1)
		    markers = kinetics.GetMarkers(body)
		    for marker in markers:
		        print(marker._id)


	"""

def Aryval(array: str, component: int) -> float:

	"""

	Returns component 'compoment' of array 'array'.

	Parameters
	----------
	array : str
		The name or the id of the array.

	component : int
		The component of the array to be returned.

	Returns
	-------
	float
		Returns the component of the array that is requested.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    val_1 = kinetics.Aryval("1", 0)
		    val_2 = kinetics.Aryval("ARRAY_2", 0)


	"""

def HBMConfigMove(config: object, total_angle: float, step: float) -> bool:

	"""

	Moves a Human Body Model Kinetic Configuration 

	Parameters
	----------
	config : object
		The kinetic configuration of the HBM that will be moved.

	total_angle : float
		The total angle in degrees.

	step : float, optional
		The incremental step for applying the total angle. Default is 1.0 degree.

	Returns
	-------
	bool
		Returns True on failure and False on success.

	Examples
	--------
	::

		import os
		import ansa
		
		from ansa import base, kinetics, constants
		
		
		def moveHbm():
		    # this script will extend the Left Knee 30 degrees using a step of 1 degree
		    hbm_config = None
		    ents = ansa.base.NameToEnts("knee_extension_l")
		    for ent in ents:
		        if base.GetEntityType(constants.LSDYNA, ent) == "KIN_CONFIG":
		            hbm_config = ent
		            break
		    kinetics.HBMConfigMove(config=hbm_config, total_angle=30.0, step=1.0)


	"""

def HBMTreeJointRotate(joint: object, total_angle: float, axis: int, step: float) -> bool:

	"""

	Rotates a Human Body Model Tree Kinetic Joint using geometric transformation combined with morphing.

	Parameters
	----------
	joint : object
		The Human Body Model Kinetic Joint (it should be spherical or revolute).

	total_angle : float
		The total angle in degrees.

	axis : int
		The rotation axis as a number. R" : 1, S' : 2, T : 3.

	step : float, optional
		The incremental step for applying the total angle. Default is 1.0 degree.

	Returns
	-------
	bool
		Always returns True.

	Examples
	--------
	::

		import os
		import ansa
		
		from ansa import base, kinetics, constants
		
		
		def moveHbm():
		    # this script will extend the Left Elbow 30 degrees using a step of 1 degree
		    hbm_joint = None
		    ents = ansa.base.NameToEnts("humeroulnar_joint_tree_l")
		    for ent in ents:
		        if base.GetEntityType(constants.LSDYNA, ent) == "KIN_JOINT":
		            hbm_joint = ent
		            break
		    kinetics.HBMTreeJointRotate(joint=hbm_joint, total_angle=30.0, axis=1, step=1.0)


	"""

def AutoMech(starting_element: object, joints: object, elements_to_disregard: object, create_dummy_kin_model: bool, create_sets_with_properties: bool, create_kinetic_forces: bool, group_name: str) -> object:

	"""

	This function converts FE entities to ANSA kinetic entities by using the real connectivity of the model. 

	Parameters
	----------
	starting_element : object
		A random element that belongs to the mechanism that is going to be created.

	joints : object, optional
		A list of the FE joints that will be converted to ANSA Kinetic Joints. If it is not defined all the connecting elements of the model will be considered.

	elements_to_disregard : object, optional
		A list of FE joints that will be disregarded during conversion (e.g the symmetric joints to the joints that were added in 'joints' list).

	create_dummy_kin_model : bool, optional
		Option for creating a Dummy tree hierarchy. Note, that this function doesn't create an H-POINT Kinetic Joint, so the user has to do this manually by iterating the created kinetic entities of this function and select the appropriate Kinetic Body (e.g the Pelvis ). Default value is False.

	create_sets_with_properties : bool, optional
		Option for creating SET/GROUP(s) containing properties instead of elements, for the Kinetic Bodies contents. Default value is False.

	create_kinetic_forces : bool, optional
		Option for converting CONNECTOR(s) of BUSHING type into Kinetic Force(s). Enabled only in ABAQUS. Default value if False.

	group_name : str, optional
		Define a group name for the Kinetic Joints that will be created. Default value is ''Mechanism from AutoMech".

	Returns
	-------
	object
		Returns a list that contains all the created kinetic entities.

	Examples
	--------
	::

		import os
		import ansa
		from ansa import base, kinetics, constants
		
		
		def main():
		    starting_elem = base.GetEntity(constants.LSDYNA, "ELEMENT_SHELL", 4569)
		
		    joints_set = base.GetEntity(constants.LSDYNA, "SET", 148)
		    containers = joints_set
		    joints = base.CollectEntities(constants.LSDYNA, containers, "__ALL_ENTITIES__")
		
		    non_joints_set = base.GetEntity(constants.LSDYNA, "SET", 147)
		    containers = non_joints_set
		    non_joints = base.CollectEntities(constants.LSDYNA, containers, "__ALL_ENTITIES__")
		
		    kin_ents = kinetics.AutoMech(starting_elem, joints, non_joints)


	"""

def PositionGetBodiesJoints(kin_pos: object) -> object:

	"""

	This function returns a list of KinBodies and KinJoints of a KIN_POSITION.

	Parameters
	----------
	kin_pos : object
		The KIN_POSITION whose KinBodies and KinJoints are requested.

	Returns
	-------
	object
		Returns a list containing references to the KIN_BODY and KIN_JOINT objects found.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    # get bodies and joints of kin_pos with id 1 and print their Types and IDs
		    pos = base.GetEntity(base.CurrentDeck(), "KIN_POSITION", 1)
		    bodies_joints = kinetics.PositionGetBodiesJoints(pos)
		    for ent in bodies_joints:
		        print(base.GetEntityType(base.CurrentDeck(), ent), ent._id)


	"""

def MoveConfigInteractive(kin_config: object) -> int:

	"""

	This function performs the interactive articulation of a kinematic configuration.

	Parameters
	----------
	kin_config : object
		The KIN_CONFIG for the interactive articulation.

	Returns
	-------
	int
		Returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def main():
		    conf = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 3)
		
		    kinetics.MoveConfigInteractive(conf)


	"""

class Simulator():

	"""

	It is recommended to construct only one Simulator Object per KIN_CONFIG / whole model (otherwise python warning is thrown) in order to avoid cross-references. For example if 2 Simulator objects refer to the same KIN_CONFIG and a member is changed to one of them, the same will be changed to the other object as well.

	See Also
	--------
	Options

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def test_whole_model_simulation():
		    # create object instance for whole model
		    kin_sim = kinetics.Simulator()
		
		    # change type of simulation and parameters
		    kin_sim.type = "Kinematic"
		    kin_sim.end_time = 2.0
		    kin_sim.options.kinematics_hinit = 0.2
		
		    # run simulation and move model by results to time 1.0
		    kin_res = kin_sim.Run()
		    time_res = kinetics.MoveByResults(kin_res, 1.0)
		
		    # print actual time that model moved
		    print(time_res)
		
		    # save current position and move to initial
		    pos = kinetics.SavePosition(name="simulation time 1")
		    kinetics.MoveToInitialPosition()
		
		
		def test_kin_config_simulation():
		    # create object instance for KIN_CONFIG and set type
		    kf = base.GetEntity(base.CurrentDeck(), "KIN_CONFIG", 2)
		    kin_sim = kinetics.Simulator(kin_config=kf, type="Contact", end_time=3.0)
		
		    # get reference of KinOptions object and change parameters
		    opts = kin_sim.options
		    opts.contacts_integrator_type = "Constant Step Size"
		    opts.contacts_hinit = 0.02
		
		    # run simulation and move model by results to time 2.5
		    kin_res = kin_sim.Run()
		    time_res = kinetics.MoveByResults(kin_res, 2.5)
		
		    # save current position (default name), reload and move to saved position
		    pos = kinetics.SavePosition()
		    kinetics.MoveToInitialPosition()
		    kinetics.MoveToPosition(pos)

	"""


	type: str = None
	"""
	Solver Type: "Dynamic", "Kinematic", "NonSmooth", "Equilibrium", "Quasi Static",
	"Initial Conditions".

	"""

	output: str = None
	"""
	Output Step Size Type: "All Steps", "Step Size", "Steps", "Step Size/Contact".

	"""

	step_size: float = None
	"""
	Step size for output type 'Step Size'. (step_size > 0)

	"""

	num_steps: int = None
	"""
	Number of steps for output type 'Steps'. (num_steps > 0)

	"""

	find_equilibrium_first: bool = None
	"""
	Find equilibrium first.

	"""

	calc_from_zero: bool = None
	"""
	Always calculate from time zero.

	"""

	animate_during_calc: bool = None
	"""
	Animate during calculation.
	(If true, model's position will remain changed after simulation run)

	"""

	end_time: float = None
	"""
	End time of simulation (end_time > 0).

	"""

	options: object = None
	"""
	ansa.kinetics.Options() object. It can be accessed in order to modify its members, 
	but no modification of the object itself is permitted (exception is thrown).
	See documentation of kinetics.Options.

	"""

	def __init__(self, kin_config: object, type: str, end_time: float, find_equilibrium_first: bool, animate_during_calc: bool) -> object:

		"""

		Instance creation of Simulator object (constructor).


		Parameters
		----------
		kin_config : object
			KIN_CONFIG entity that simulation refers to. It can't be 
			changed after object's creation. If omitted whole model is 
			assumed. (optional)

		type : str
			Same as object's member.

		end_time : float
			Same as object's member.

		find_equilibrium_first : bool
			Same as object's member.

		animate_during_calc : bool
			Same as object's member.

		Returns
		-------
		object

		"""


	def Run(self, kin_sim_script: object) -> object:

		"""

		Run the simulation. A KIN_RESULTS entity (object) is created by simulation run and returned. If a simulation error occures, None is returned and a Python warning is thrown. 


		Parameters
		----------
		kin_sim_script : object, optional
			KIN_SIMULATION_SCRIPT entity that simulation executes its command(s). 
			Any previously defined option(s) (e.g. type, end_time, etc.) will be 
			overridden depending from command(s) content(s).

		Returns
		-------
		object

		"""

class FlexBody():

	"""

	The class is responsible for creating a new flex body, converting an existing body to flex, or modifying an existing flex body, depending on the defined optional arguments.
	
	To create a new flex body, only the filename argument should be defined.
	To convert an existing body to flex, the filename and the body arguments should be defined.
	To modify an existing flex body, only the body argument should be defined.
	
	The "delete_body_contents" and "align_with_body_cog" arguments are taken into account only for the converting case.
	If the class is called without arguments, it returns an error.

	Examples
	--------
	::

		import ansa
		from ansa import base
		from ansa import kinetics
		
		
		def create_flex_body():
		    fb = kinetics.FlexBody("/user/modal_file.mnf")
		    print(fb.num_nodes)
		    print(fb.num_modes)
		
		
		def convert_body_to_flex():
		    body = base.GetEntity(base.CurrentDeck(), "KIN_BODY", 4)
		    fb = kinetics.FlexBody("/user/modal_file.mnf", body, True, True)
		    print(fb.num_nodes)
		    print(fb.num_modes)
		
		
		def modify_flex_body():
		    fb = kinetics.FlexBody(body=base.GetEntity(base.CurrentDeck(), "KIN_BODY", 4))
		    fb.active_modes = [
		        "no",
		        "no",
		        "no",
		        "no",
		        "no",
		        "no",
		        "yes",
		        "no",
		        "yes",
		        "yes",
		        "yes",
		        "yes",
		    ]

	"""


	flex_body: object = None
	"""
	The flex body entity.

	"""

	modal_file: str = None
	"""
	The full path modal file that used for the flex body.

	"""

	num_nodes: int = None
	"""
	The number of the nodes specified in the modal file.

	"""

	num_interface_nodes: int = None
	"""
	The number of the interface nodes specified in the modal file.

	"""

	num_modes: int = None
	"""
	The number of the modes specified in the modal file.

	"""

	num_active_modes: int = None
	"""
	The number of the active modes.

	"""

	active_modes: object = None
	"""
	The active modes list of num_modes yes/no values.

	"""

	inertia_modeling: str = None
	"""
	The inertia modeling: 'rigid', 'constant', 'partial', 'full', 'custom'.

	"""

	invariants: object = None
	"""
	The invariants (I2, I3, I4, I5, I6, I8, I9) list of seven yes/no values.

	"""

	damping_ratio: str = None
	"""
	The damping ratio: 'off', 'default', 'user'.

	"""

	damping_ratio_user_expr: str = None
	"""
	The expression for the user damping ratio case.

	"""

	general_damping: str = None
	"""
	The general damping: 'off', 'full', 'internal_only'.

	"""

	initial_modal_displacements: object = None
	"""
	The initial modal displacements list of num_modes float values.

	"""

	initial_modal_velocities: object = None
	"""
	The initial modal velocities list of num_modes float values.

	"""

	modal_exact_coordinates: object = None
	"""
	The modal exact coordinates list of num_modes yes/no values.

	"""

	characteristic_length: float = None
	"""
	The characteristic length for the linear limit check.

	"""

	natural_frequencies: object = None
	"""
	The natural frequencies [Hz] list of num_modes float values.

	"""

	damping_ratio_values: object = None
	"""
	The damping ratio values list of num_modes float values.

	"""

	def __init__(self, filename: str, body: object, delete_body_contents: bool, align_with_body_cog: bool) -> object:

		"""


		Parameters
		----------
		filename : str, optional
			The modal file that decribes the flex properties.

		body : object, optional
			The body for convert (rigid or flex) if filename is also defined or modify (must be flex) if filename is omitted.

		delete_body_contents : bool, optional
			True to delete any existing contents of the body that converted to flex. (Default: False)

		align_with_body_cog : bool, optional
			True to align the modal file's data with the body's CoG. (Default: False)

		Returns
		-------
		object

		"""

def Configurator() -> int:

	"""

	This function launches the Kinetic Configuration Tool.

	Returns
	-------
	int
		Returns 0.

	Examples
	--------
	::

		import ansa
		from ansa import kinetics
		
		
		def main():
		    kinetics.Configurator()


	"""

def HBMReadPosFile(file: str, step: float=5.0, hbm_random_element: object=None) -> bool:

	"""

	Reads and applies an HBM positioning JSON File. 

	Parameters
	----------
	file : str
		The full path filename of the HBM positioning JSON File.

	step : float, optional
		The angular step that will be used to apply the total angle of an HBM Configuration or Kinetic Joint.

	hbm_random_element : object, optional
		In case there are more than one HBMs in the model , then a random element (Shell or Solid) of the HBM should be defined , for selecting the HBM to apply the Positioning File.

	Returns
	-------
	bool
		Zero on success.

	See Also
	--------
	HBMConfigMove, HBMTreeJointRotate

	Examples
	--------
	::

		# PYTHON script
		import os
		import ansa
		from ansa import kinetics, base
		
		
		def HBMReadJSONPosFile():
		    base.Open("/home/user/THUMS/AM50_Occ_V61/main_THUMS_AM50_V61.k.ansa")
		    kinetics.HBMReadPosFile(file="/home/user/hbm_positioning.json", step=3.0)
		    base.SaveAs("/home/user/THUMS/AM50_Occ_V61/main_THUMS_AM50_V61.k_positioned.ansa")


	"""

