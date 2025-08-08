from __future__ import annotations
from typing import *

def GetFreeTableIdModalResponse() -> int:

	"""

	This function returns a free id in the Modal Response tool tables list, in order to further use it for table definition.

	Returns
	-------
	int
		It returns a free id as integer.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    id = nvh.GetFreeTableIdModalResponse()
		    print("Free Table id for Modal Response tool : ", id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetFreeTableIdFrfAssembly() -> int:

	"""

	This function returns a free id in the Frf Assembly tool tables list, in order to further use it for table definition.

	Returns
	-------
	int
		It returns a free id as integer.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    id = nvh.GetFreeTableIdFrfAssembly()
		    print("Free Table id for Frf Assembly tool : ", id)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateTableNvh(table_type: str, table_id: int, xpoints: object, ypoints: object, parameters: object, nvh_tool: str) -> int:

	"""

	This function creates the given table with the given type and parameters in the specified NVH tool. The provided id will be used if it is free.

	Parameters
	----------
	table_type : str
		Table type (could be one of 'TABLED1', 'TABLED2', 'TABLED3', 'TABLED4', 'TABLED6' and 'TABDMP1', or their lowercase versions).

	table_id : int
		Desired id of the table. If a negative or zero value is given, the returned table id will be the first one to be found free. The specified id is not guaranteed to be used in the end, it is only used as a suggestion. The returned value is the correct table id for further reference.

	xpoints : object
		List of x coordinates of the table.

	ypoints : object
		List of y coordinates of the table. In case of TABLED6, this is a list of pairs of values, so ypoints list has twice the size of xpoints list.

	parameters : object
		Parameters depending on the type of the table.
		
		For TABLED1, parameters should be a matrix of size 2 with two string values, which could be either 'LINEAR' or 'LOG' (or their lowercase versions). For example: ['LOG','LINEAR']
		
		For TABLED2, parameters should be a matrix of size 1, containing a floating point value for the X1 parameter of the table. For example: [0.4]
		
		For TABLED3, parameters should be a matrix of size 2, containing the floating point values for the X1 and X2 parameters of the table. For example: [0.6, 1.4]
		
		For TABLED4, parameters should be a matrix of size 4, containing the floating point values for the X1, X2, X3 and X4 parameters of the table. For example: [2.1, 0.4, 5.3, -0.56]
		
		For TABLED6, parameters should be a matrix of size 1, containing one of the following strings: 'MP' or 'RI' (or their lowercase versions). For example: ['mp']
		
		For TABDMP1, parameters should be a matrix of size 1, containing one of the following strings: 'G', 'CRIT' or 'Q' (or their lowercase versions). For example: ['CRIT']

	nvh_tool : str
		The NVH tool where the table will be added to. Should be one of 'MODAL_RESPONSE', 'FRF_ASSEMBLY' or 'RANDOM_RESPONSE', or their lowercase versions

	Returns
	-------
	int
		On success, it returns the table id given to the newly inserted table. The returned id will be the same as the provided one, if it was free. Otherwise, a different id will be chosen and returned.
		On failure, the returned value is -1.

	See Also
	--------
	meta.nvh.CreateTablesNvhFromCurves

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		import math
		
		
		def main():
		    type = "TABLED1"
		    id1 = 101
		    id2 = 102
		    tool = "MODAL_RESPONSE"
		    params = list()
		    params.append("linear")
		    params.append("LOG")
		    xpoints = list()
		    y_magnitude = list()
		    y_phase = list()
		    for i in range(0, 100):
		        magnitude = 25 * i
		        phase = 2 * i
		        xpoints.append(i)
		        y_magnitude.append(magnitude)
		        y_phase.append(phase)
		    magid = nvh.CreateTableNvh(type, id1, xpoints, y_magnitude, params, tool)
		    phaseid = nvh.CreateTableNvh(type, id2, xpoints, y_phase, params, tool)
		
		    if magid == id1 and magid != -1:
		        print("Amplitude table Id:", magid)
		    elif magid != id1 and magid != -1:
		        print("Suggested amplitude table id already exists.")
		        print("Given amplitude table Id:", magid)
		    elif magid == -1:
		        print("Failed to create the amplitude table")
		    if phaseid == id2 and phaseid != -1:
		        print("Phase table Id:", magid)
		    elif phaseid != id2 and phaseid != -1:
		        print("Suggested phase table id already exists.")
		        print("Given phase table Id:", phaseid)
		    elif phaseid == -1:
		        print("Failed to create the phase table")
		    type = "TABDMP1"
		    id = 1001
		    tool = "FRF_ASSEMBLY"
		    dparams = list()
		    dparams.append("crit")
		    freqs = list()
		    damping = list()
		    for i in range(5, 200):
		        d = 0.1 / math.log(10 * i)
		        freqs.append(i)
		        damping.append(d)
		    dampingid = nvh.CreateTableNvh(type, id, freqs, damping, dparams, tool)
		
		    if dampingid == id and dampingid != -1:
		        print("Phase table Id:", dampingid)
		    elif dampingid != id and dampingid != -1:
		        print("Suggested damping table id already exists.")
		        print("Given damping table Id:", dampingid)
		    elif dampingid == -1:
		        print("Failed to create the damping table")
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetFrfAssemblyLoads() -> object:

	"""

	This function retrieves information about the loads defined in FRF Assembly tool.

	Returns
	-------
	object
		It returns a list containing the loads defined in FRF Assembly tool. Each entry of the list is an instance of  class Load.

	See Also
	--------
	nvh.ResponseNode, nvh.ResponseNodeLc, nvh.Load

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		
		def main():
		    loads = meta.nvh.GetFrfAssemblyLoads()
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent id:", l.parent_id)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        print("\\t", "load filename:", l.filename)
		
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetModalFrequencyResponseLoads(component_name: str) -> object:

	"""

	This function retrieves information about the loads defined in Modal Frequency Response tool.

	Parameters
	----------
	component_name : str
		The name of the component, whose loads will be returned.

	Returns
	-------
	object
		It returns a list containing the loads defined in Modal Frequency Response tool. Each entry of the list is an instance of class Load.

	See Also
	--------
	nvh.ResponseNode, nvh.ResponseNodeLc, nvh.ResponseElement, nvh.ResponsePanel, nvh.Load

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		
		def main():
		    component_name = "Default"
		    loads = meta.nvh.GetModalFrequencyResponseLoads(component_name)
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent id:", l.parent_id)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        print("\\t", "load filename:", l.filename)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for i, datai in enumerate(l.frequency_start_3d):
		            print(
		                "\\t",
		                "3D frequency range:",
		                l.frequency_start_3d[i],
		                ";",
		                l.frequency_end_3d[i],
		                ";",
		                l.frequency_step_3d[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		        for datan in l.response_elements:
		            print("\\t\\t", "response element: id:", datan.id)
		            print("\\t\\t", "response element: type:", datan.type)
		            print("\\t\\t", "response element: name:", datan.name)
		            print(
		                "\\t\\t",
		                "response element: coordinate_system_id:",
		                datan.coordinate_system_id,
		            )
		        for datap in l.response_panels:
		            print("\\t\\t", "response panel: name:", datap.name)
		            print("\\t\\t", "response panel: included:", datap.included)
		            elems = ""
		            for datar in datap.element_ids:
		                elems += " " + str(datar)
		            print("\\t\\t\\t", "Panel Element ids:", elems)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetModalTransientResponseLoads(component_name: str) -> object:

	"""

	This function retrieves information about the loads defined in Modal Transient Response tool.

	Parameters
	----------
	component_name : str
		The name of the component, whose loads will be returned.

	Returns
	-------
	object
		It returns a list containing the loads defined in Modal Transient Response tool. Each entry of the list is an instance of class Load.

	See Also
	--------
	nvh.ResponseNode, nvh.ResponseNodeLc, nvh.Load

	Examples
	--------
	::

		# PYTHON script
		import meta
		
		
		def main():
		    component_name = "Default"
		    loads = meta.nvh.GetModalTransientResponseLoads(component_name)
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent id:", l.parent_id)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.transient_end_time):
		            print(
		                "\\t",
		                "transient range:",
		                l.transient_end_time[i],
		                ";",
		                l.transient_output_frequency[i],
		                ";",
		                l.transient_step[i],
		            )
		        for i, datai in enumerate(l.transient_end_time_3d):
		            print(
		                "\\t",
		                "transient range:",
		                l.transient_end_time_3d[i],
		                ";",
		                l.transient_output_frequency_3d[i],
		                ";",
		                l.transient_step_3d[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetRandomResponseTable(table_id: int) -> object:

	"""

	Given the table Id, get the TABLED1 with matching Id, as it is defined in random response tool.

	Parameters
	----------
	table_id : int
		The Id of the table to be retrieved.

	Returns
	-------
	object
		If a matching table is found, a list of the following format is returned:
		[ table_id, table_name, axis_types, x_points, y_points ]
		- table_id: The id of the table
		- table_name: The name of the table
		- axis_types: A list where each string describes the type of the axis ('LOG' or 'LINEAR')
		- x_points: A list of the X coordinates of the table.
		- y_points: A list of the Y coordinates of the table.
		
		If no matching table is found, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    id = 1
		    table = nvh.GetRandomResponseTable(id)
		    if table:
		        print(table[0])
		        print(table[1])
		        print(table[2])
		        print(table[3])
		
		
		if __name__ == "__main__":
		    main()


	"""

def EditRandomResponseTable(table_parameters: object) -> int:

	"""

	Edit the TABLED1 with matching Id, as it is defined in random response tool, using the changes as they are input via the table_parameters matrix.

	Parameters
	----------
	table_parameters : object
		A matrix of the following format is expected:
		[ table_id, table_name, axis_types, x_points, y_points ]
		- table_id: The id of the table
		- table_name: The name of the table
		- axis_types: A list where each string describes the type of the axis ('LOG' or 'LINEAR')
		- x_points: A list of the X coordinates of the table.
		- y_points: A list of the Y coordinates of the table.

	Returns
	-------
	int
		Returns 1 upon success, 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    table_id = 1  # Table id must already exist
		    new_table_name = "MyTableName"
		    new_axis_types = ["LINEAR", "LOG"]
		    new_x_points = [0.1, 1.34]
		    new_y_points = [2.64, 5]
		    parameters = [table_id, new_table_name, new_axis_types, new_x_points, new_y_points]
		    ret = nvh.EditRandomResponseTable(parameters)
		    if ret:
		        print("Changed successfully")
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateRandomResponseTable(table_parameters: object) -> int:

	"""

	Given the table Id, create the corresponding TABLED1 in Random Response tool, using the parameters as they are input via the table_parameters list.

	Parameters
	----------
	table_parameters : object
		A matrix of the following format is expected:
		[ table_id, table_name, axis_types, x_points, y_points ]
		- table_id: The id of the table
		- table_name: The name of the table
		- axis_types: A list where each string describes the type of the axis ('LOG' or 'LINEAR')
		- x_points: A list of the X coordinates of the table.
		- y_points: A list of the Y coordinates of the table.

	Returns
	-------
	int
		Returns 1 upon success, 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    new_table_id = 1  # Table id must not exist
		    new_table_name = "MyTableName"
		    new_axis_types = ["LOG", "LINEAR"]
		    new_x_points = [0.1, 2.34]
		    new_y_points = [1.64, 5]
		    parameters = [
		        new_table_id,
		        new_table_name,
		        new_axis_types,
		        new_x_points,
		        new_y_points,
		    ]
		    ret = nvh.CreateRandomResponseTable(parameters)
		    if ret:
		        print("Created successfully.")
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetAllRandomResponseTables() -> object:

	"""

	Get all tables, as they are defined in random response tool.

	Returns
	-------
	object
		A list is returned, where each element is a matrix of the following form:
		[ table_id, table_name, axis_types, x_points, y_points ]
		- table_id: The id of the table
		- table_name: The name of the table
		- axis_types: A list where each string describes the type of the axis ('LOG' or 'LINEAR')
		- x_points: A list of the X coordinates of the table.
		- y_points: A list of the Y coordinates of the table.
		
		If no matching table is found, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    rr_tables = nvh.GetAllRandomResponseTables()
		    for table in rr_tables:
		        print(table[0])
		        print(table[1])
		        print(table[2])
		        print(table[3])
		        print(table[4])
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteRandomResponseTable(table_id: int) -> int:

	"""

	Delete a specific table from the random response tool.

	Parameters
	----------
	table_id : int
		The Id of the table to be deleted.

	Returns
	-------
	int
		It returns always 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    table_id = 1
		    ret = nvh.DeleteRandomResponseTable(table_id)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteAllRandomResponseTables() -> int:

	"""

	Delete all tables from the random response tool.

	Returns
	-------
	int
		It returns always 1.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    ret = nvh.DeleteAllRandomResponseTables()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetRandomResponseCorrelationTable(table_position: int) -> object:

	"""

	Get the correlation table according to position, as it is defined in the Random Response tool.

	Parameters
	----------
	table_position : int
		The sequential position of the table ( {0,1,...,N-1} for N tables ).

	Returns
	-------
	object
		Returns a list of the following form:
		[ table_name, table_data ]
		table_name: The name of the correlation table
		table_data: A 2d list containing the actual data of the table
		
		If no table was found at the requested position, an empty list is returned.

	See Also
	--------
	nvh.GetRandomResponseCorrelationTablePositionFromName

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    correlation_table = nvh.GetRandomResponseCorrelationTable(0)
		    if correlation_table:
		        print(correlation_table[0])
		        for row in correlation_table[1]:
		            print(row)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetAllRandomResponseCorrelationTables() -> object:

	"""

	Get all correlation tables, as they are defined in the Random Response tool.

	Returns
	-------
	object
		Returns a list of correlation tables where each entry is a list of the following form:
		[ table_name, table_data ]
		table_name: The name of the correlation table
		table_data: A 2d list containing the actual data of the table
		
		If no tables were found, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    correlation_tables = nvh.GetAllRandomResponseCorrelationTables()
		    if correlation_tables:
		        for correlation_table in correlation_tables:
		            print(correlation_table[0])
		            for row in correlation_table[1]:
		                print(row)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetRandomResponseCorrelationTablePositionFromName(table_name: str) -> int:

	"""

	Searches in all random response correlation table sheets, and returns the position of the sheet which matches the input name.

	Parameters
	----------
	table_name : str
		The name of the correlation table sheet.

	Returns
	-------
	int
		If the name is matched with a table, it returns it's position as an integer starting from 0.
		If the name wasn't found, -1 is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    table_position = nvh.GetRandomResponseCorrelationTablePositionFromName("Sheet1")
		    if table_position != -1:
		        print("Table found at position", table_position)
		    else:
		        print("Table not found")
		
		
		if __name__ == "__main__":
		    main()


	"""

def EditRandomResponseCorrelationTable(table_position: int) -> int:

	"""

	Edit a correlation table's definition in the Random Response tool.

	Parameters
	----------
	table_position : int
		The sequential position of the table ( {0,1,...,N-1} for N tables )

	Returns
	-------
	int
		It returns 1 on success, 0 on failure.

	See Also
	--------
	nvh.GetRandomResponseCorrelationTablePositionFromName, nvh.GetRandomResponseCorrelationTable

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    # Retrieve position of table with name 'Sheet1'
		    table_position = nvh.GetRandomResponseCorrelationTablePositionFromName("Sheet1")
		
		    # Get the actual table
		    table = nvh.GetRandomResponseCorrelationTable(table_position)
		
		    # Change the name,
		    table[0] = "NewTableSheet"
		
		    # Change some data ( Cell at first row, first column is set to 2#3. )
		    table[1][1][1] = "2#3"
		
		    # Edit the table
		    ret = nvh.EditRandomResponseCorrelationTable(table_position, table)
		    if ret:
		        print("Table was edited successfully.")
		    else:
		        print("Failed to edit table.")
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateRandomResponseCorrelationTable(table_name: str, table_data: object) -> int:

	"""

	Given an input name and a 2-dimensional list representing the correlation table data, a correlation table sheet is created.
	If the name already exists, no table is created.

	Parameters
	----------
	table_name : str
		The name of the correlation table sheet to be created.

	table_data : object
		A 2-dimensional list, representing the correlation table sheet's data.
		The list should have the following format, for an example of 3x3 list:

	Returns
	-------
	int
		Returns 1 upon successful correlation table sheet creation, 0 otherwise.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    ret = nvh.CreateRandomResponseCorrelationTable(
		        "NewTable", [["1#3,2.1#2", "-3.7#4,1.1#2"], [4.6]]
		    )
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteRandomResponseCorrelationTable(table_position: int) -> int:

	"""

	Delete a specific correlation table from the Random Response tool according to specifications.

	Parameters
	----------
	table_position : int
		The sequential position of the table ( {0,1,...,N-1} for N tables ).

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	nvh.GetRandomResponseCorrelationTablePositionFromName, nvh.DeleteAllRandomResponseCorrelationTables

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    # Delete table named 'Sheet1'
		    sheet_name = "Sheet1"
		    sheet_position = nvh.GetRandomResponseCorrelationTablePositionFromName(sheet_name)
		    if sheet_position:
		        ret = nvh.DeleteRandomResponseCorrelationTable(sheet_position)
		        if ret:
		            print(sheet_name, "was deleted")
		        else:
		            print("Unable to delete:", sheet_name)
		    else:
		        print("Failed to locate sheet with name", sheet_name)
		    # Delete sheet with position 10000 (probably doesn'y exist)
		    ret = nvh.DeleteRandomResponseCorrelationTable(10000)
		    if ret:
		        print(sheet_name, "was deleted")
		    else:
		        print("Unable to delete:", sheet_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteAllRandomResponseCorrelationTables() -> int:

	"""

	Returns
	-------
	int
		It always returns 1.

	See Also
	--------
	nvh.DeleteRandomResponseCorrelationTable

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    ret = nvh.DeleteAllRandomResponseCorrelationTables()
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReadModalMatricesFromFile(filename: str, deck: str, scan_read: str) -> object:

	"""

	This function scans the specified file, which is of the provided deck type, for modal matrices and either reports about their existence, or reads and stores them within META. The anticipated modal matrices are the modal viscous damping matrix, the modal structural damping matrix and the modal stiffness matrix.

	Parameters
	----------
	filename : str
		The name of the file that includes the modal matrices.

	deck : str
		The type of the provided filename. For instance "NASTRAN" refers to nastran type files.

	scan_read : str
		If 'scan' then the function will only scan for the existence of modal matrices and report. If 'read', the function will additionally read the matrices and store them internally in META.

	Returns
	-------
	object
		On success, it returns a list with the modal matrices found in the provided file.
		On failure, it returns an empty list.

	See Also
	--------
	DeleteModalMatricesFromFile

	Examples
	--------
	::

		import meta
		from meta import nvh
		
		
		def main():
		    filename = "results.op2"
		    deck = "NASTRAN"
		    all_matrix = nvh.ReadModalMatricesFromFile(filename, deck, "read")
		
		    print("Matrices:")
		    for one_matrix in all_matrix:
		        print(one_matrix)
		
		
		if __name__ == "__main__":
		    main()


	"""

def DeleteModalMatricesFromFile():

	"""

	This function pairs with function ReadModalMatricesFromFile. It deletes the modal matrices stored when called the latter, and frees the corresponding memory.

	See Also
	--------
	ReadModalMatricesFromFile

	Examples
	--------
	::

		import meta
		from meta import nvh
		
		
		def main():
		    filename = "results.op2"
		    deck = "NASTRAN"
		    all_matrix = nvh.ReadModalMatricesFromFile(filename, deck, "read")
		
		    print("Matrices:")
		    for one_matrix in all_matrix:
		        print(one_matrix)
		    nvh.DeleteModalMatricesFromFile()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ModalMatricesFromFile(action: str, filename: str, deck: str) -> object:

	"""

	This function scans the specified file, which is of the provided deck type, for modal matrices and either reports about their existence, or reads and stores them within META. The supported modal matrices are the modal viscous damping matrix, the modal structural damping matrix, the modal stiffness matrix and modal matrices comming from poroelastic/trim components. The function can also list the modal matrices read and delete them from META.

	Parameters
	----------
	action : str
		Specifies what action should be taken:
		scan : Scans the file and returns a list of the modal matrices found.
		read : Reads the found modal matrices from the file and stores them internally in META.
		clear : Deletes the cached modal matrices.
		list : Returns a list of the cached modal matrices, if any.

	filename : str, optional
		The name of the file that includes the modal matrices.

	deck : str, optional
		The type of the provided filename. For instance "NASTRAN" refers to nastran type files.

	Returns
	-------
	object
		A list of the modal matrices.

	Examples
	--------
	::

		import meta
		from meta import nvh
		
		
		def main():
		    filename = "results.op2"
		    deck = "NASTRAN"
		
		    all_matrix = nvh.ModalMatricesFromFile("read", filename, deck)
		    print("Matrices Read:")
		    for one_matrix in all_matrix:
		        print(one_matrix)
		    all_matrix = nvh.ModalMatricesFromFile("list")
		    print("Matrices Cached:")
		    for one_matrix in all_matrix:
		        print(one_matrix)
		    nvh.ModalMatricesFromFile("clear")
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetModalMatricesFromFile(filename: str, deck: str) -> object:

	"""

	This function scans the specified file, which is of the provided deck type, for modal matrices, reads them and returns them. The anticipated modal matrices are the modal viscous damping matrix, the modal structural damping matrix and the modal stiffness matrix. 

	Parameters
	----------
	filename : str
		The name of the file that includes the modal matrices

	deck : str
		The type of the provided filename. For instance "NASTRAN" refers to nastran type files.

	Returns
	-------
	object
		A list of the modal matrices.

	Examples
	--------
	::

		import os
		import meta
		from meta import nvh
		
		
		def main():
		    result = nvh.GetModalMatricesFromFile("example.op2", "NASTRAN")
		    for m in result:
		        print(m.name)
		        print("Rows:")
		        print(m.rows)
		        print("Columns:")
		        print(m.columns)
		        print("Form:")
		        print(m.form)
		        print("Values:")
		        print(m.values)
		
		
		if __name__ == "__main__":
		    main()


	"""

def CreateTablesNvhFromCurves(table_type: str, table_parameters: object, table_start_id: int, tool: str, window: object, curves: object, rimp: str) -> object:

	"""

	This function creates a series of tables with the given type and parameters in the specified NVH tool. The provided id will be used as the id of the first table, if it is available.

	Parameters
	----------
	table_type : str
		Table type (Could be one of 'TABLED1', 'TABLED2', 'TABLED3', 'TABLED4', 'TABLED6' and 'TABDMP1', or their lowercase versions).

	table_parameters : object
		Parameters depending on the type of the table.
		
		For TABLED1, parameters should be a list of size 2 with two string values, which could be either 'LINEAR' or 'LOG' (or their lowercase versions). For example: [ 'LOG', 'LINEAR' ]
		
		For TABLED2, parameters should be a list of size 1, containing a floating point value for the X1 parameter of the table. For example: [ 0.4 ]
		
		For TABLED3, parameters should be a list of size 2, containing the floating point values for the X1 and X2 parameters of the table. For example: [ 0.6, 1.4 ]
		
		For TABLED4, parameters should be a list of size 4, containing the floating point values for the X1, X2, X3 and X4 parameters of the table. For example: [ 2.1, 0.4, 5.3, -0.56 ]
		
		For TABLED6, parameters should be a list of size 1, containing one of the following strings: 'MP' or 'RI' (or their lowercase versions). For example: [ 'mp' ]
		
		For TABDMP1, parameters should be a list of size 1, containing one of the following strings: 'G', 'CRIT' or 'Q' (or their lowercase versions). For example: [ 'CRIT' ]

	table_start_id : int
		Desired id of the first table to be created. If a negative or zero value is given, the returned table id will be the first one to be found free. The specified id is not guaranteed to be used in the end, it is only used as a suggestion. Moreover, there is no guarantee that the rest of the tables will have successive ids, either in ascending or in descending order.

	tool : str
		The NVH tool where the table will be added to. Could be one of ('MODAL_RESPONSE', 'FRF_ASSEMBLY' and 'RANDOM_RESPONSE', or their lowercase versions)

	window : object
		The window object that contains the curves that will be used for the table creation. Alternatively, it could be a string of the name of the window.

	curves : object
		A list of the curves objects that will be used for the table creation. Instead of the curve objects, the user could provide a list of the curve ids, all belonging to the provided window.

	rimp : str
		This argument signifies which part of the curve will be considered for the table y-axis values. Should be one of 'MAG', 'PHASE', 'MAGPHASE', 'REAL', 'IMAG' and 'REALIMAG', or their lowercase versions. Depending on the combination of "table_type" and "rimp" arguments, each curve could create one or two tables at the same time.
		For example, a combination of table_type='TABLED1' and rimp='magphase' will actually create two tables, one that contains the magnitude of the provided curves and one that contains the phase of the provided curves. Of course, in this case, the provided curves should be complex curves.
		In case of table_type='TABLED6', only 'REALIMAG' and 'MAGPHASE' values for "rimp" argument are permitted.

	Returns
	-------
	object
		On success, it returns a list of the ids of the created tables.
		On failure, an invalid object is returned.

	See Also
	--------
	meta.nvh.CreateTableNvh

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import utils
		from meta import nvh
		from meta import plot2d
		from meta import windows
		
		
		def main():
		    type = "TABLED1"
		    id1 = 1
		    tool = "MODAL_RESPONSE"
		    params = list()
		    params.append("LINEAR")
		    params.append("LINEAR")
		    windowName = "Loads"
		    window = windows.Window(windowName, page_id=0)
		    rimp = "magphase"
		    curves = list()
		    curve_id = 1
		    c1 = plot2d.CurveById(windowName, curve_id)
		    curves.append(c1)
		    curve_id = 3
		    c3 = plot2d.CurveById(windowName, curve_id)
		    curves.append(c3)
		    newTableIds = nvh.CreateTablesNvhFromCurves(
		        type, params, id1, tool, window, curves, rimp
		    )
		    print("tables: " + str(newTableIds))
		    if newTableIds:
		        for i in newTableIds:
		            cmd = "response table plot " + str(i)
		            utils.MetaCommand(cmd)
		
		
		if __name__ == "__main__":
		    main()


	"""

def GetEigenAnalysisParametersFromNastranFile(filename: str) -> object:

	"""

	Reads and outputs the actually used eigen analysis parameters from a Nastran 
	result file.

	Parameters
	----------
	filename : str
		The filename to be used

	Returns
	-------
	object
		On success, it return a list of objects representing the eigen analysis parameters 
		used in

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import nvh
		
		
		def main():
		    filename = "/home/example/inputfile.op2"
		    eigrls = meta.nvh.GetEigenAnalysisParametersFromNastranFile(filename)
		    for e in eigrls:
		        print(e.type)
		        print(e.subcases)
		        print(e.SID)
		        print(e.NORM)
		        print(e.METHOD)
		        if e.type == "EIGRL":
		            print(e.V1)
		            print(e.V2)
		            print(e.ND)
		
		
		if __name__ == "__main__":
		    main()


	"""

class ResponseNode:

	"""

	Class containing information for NVH response nodes.

	See Also
	--------
	nvh.ResponseNodeLc, nvh.Load, nvh.GetFrfAssemblyLoads, nvh.GetModalFrequencyResponseLoads, nvh.GetModalTransientResponseLoads

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    loads = nvh.GetFrfAssemblyLoads()
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent index:", l.parent_index)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	The id of the response node.

	"""

	name: str = None
	"""
	The name of the response node.

	"""

	component: str = None
	"""
	The name of the component this response node belongs to.

	"""

	dofs: str = None
	"""
	The dofs of the response node. Can be any combination of the digits 1-6, eg. 1245.

	"""

	factor: float = None
	"""
	The scale factor of the response node. It is used when the node is part of a linear combination.

	"""

	coordinate_system_id: int = None
	"""
	The id of the response node coordinate system.

	"""
class ResponseNodeLc:

	"""

	Class containing information for NVH Response node linear combination.

	See Also
	--------
	nvh.ResponseNode, nvh.Load, GetFrfAssemblyLoads, nvh.Load, GetModalFrequencyResponseLoads, GetModalTransientResponseLoads

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    loads = nvh.GetFrfAssemblyLoads()
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent index:", l.parent_index)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	The id of the linear combination.

	"""

	name: str = None
	"""
	The name of the linear combination

	"""

	nodes: object = None
	"""
	A list containing objects of type ResponseNode, one for each response node and dof contributing to  the linear combination.

	"""
class Load:

	"""

	Class that contains information about NVH Loads/subloads.

	See Also
	--------
	nvh.ResponseNode, nvh.ResponseNodeLc, nvh.ResponseElement, nvh.ResponsePanel, nvh.GetFrfAssemblyLoads, nvh.GetModalFrequencyResponseLoads, nvh.GetModalTransientResponseLoads, nvh.Response

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    component_name = "Default"
		    loads = nvh.GetModalFrequencyResponseLoads(component_name)
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent id:", l.parent_id)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for i, datai in enumerate(l.frequency_start_3d):
		            print(
		                "\\t",
		                "3D frequency range:",
		                l.frequency_start_3d[i],
		                ";",
		                l.frequency_end_3d[i],
		                ";",
		                l.frequency_step_3d[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		        for datan in l.response_elements:
		            print("\\t\\t", "response element: id:", datan.id)
		            print("\\t\\t", "response element: type:", datan.type)
		            print("\\t\\t", "response element: name:", datan.name)
		            print(
		                "\\t\\t",
		                "response element: coordinate_system_id:",
		                datan.coordinate_system_id,
		            )
		        for datap in l.response_panels:
		            print("\\t\\t", "response panel: name:", datap.name)
		            print("\\t\\t", "response panel: included:", datap.included)
		            elems = ""
		            for datar in datap.element_ids:
		                elems += " " + str(datar)
		                print("\\t\\t\\t", "Panel Element ids:", elems)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	The id of the current load/subload.

	"""

	name: str = None
	"""
	The name of the current load/subload.

	"""

	parent_id: int = None
	"""
	If the current instance is a load, parent_id is -1. If current instance is a subload, it is the id of its parent load.

	"""

	type: int = None
	"""
	The type of loading described by this load/subload. Acceptable values are:
	- 0: Force
	- 1: Displacement
	- 2: Velocity
	- 3: Acceleration

	"""

	included: int = None
	"""
	Indicates if the current load is included or excluded:
	- 0: excluded
	- 1: included

	"""

	component: str = None
	"""
	The name of the component this load/subload is applied to.

	"""

	node_name: str = None
	"""
	The name of the node this load/subload is applied to.

	"""

	node_id: int = None
	"""
	The node id of the node this load/subload is applied to.

	"""

	dof: int = None
	"""
	The dof this load/subload is applied to.

	"""

	factor: float = None
	"""
	The scale factor of the current load/subload.

	"""

	amplitude_table: int = None
	"""
	The id of the amplitude table or 0 if no amplitude table specified.

	"""

	phase_table: int = None
	"""
	The id of the phase table or 0 if no amplitude table specified.

	"""

	real_table: int = None
	"""
	The id of the real table or 0 if no real table specified.

	"""

	imaginary_table: int = None
	"""
	The id of the imaginary table or 0 if no imaginary table specified.

	"""

	coordinate_system_id: int = None
	"""
	The id of the coordinate system for this load/subload.

	"""

	frequency_start: object = None
	"""
	A list containing the starts of all frequency ranges of this load.

	"""

	frequency_end: object = None
	"""
	A list containing the ends of all frequency ranges of this load.

	"""

	frequency_step: object = None
	"""
	A list containing the step of all frequency ranges of this load.

	"""

	response_nodes: object = None
	"""
	A list containing all response nodes requested by the user. Each entry of the list is a ResponseNode instance.

	"""

	response_node_lcs: object = None
	"""
	A list containing all linear combinations of response nodes requested by the user. Each entry of the list is a ResponseNodeLc instance.

	"""

	frequency_start_3d: object = None
	"""
	A list containing the start of all frequency ranges of this load, for the 3d responses.

	"""

	frequency_end_3d: object = None
	"""
	A list containing the end of all frequency ranges of this load, for the 3d responses.

	"""

	frequency_step_3d: list = None
	"""
	A list containing the step of all frequency ranges of this load, for the 3d responses.

	"""

	transient_end_time: object = None
	"""
	A list containing the end time of all time ranges in the transient analysis of this load.

	"""

	transient_output_frequency: object = None
	"""
	A list containing the output frequency of all time ranges in the transient analysis of this load.

	"""

	transient_step: object = None
	"""
	A list containing the time step of all time ranges in the transient analysis of this load.

	"""

	transient_end_time_3d: object = None
	"""
	A list containing the end time of all time ranges in the transient analysis of this load, for the 3d responses.

	"""

	transient_output_frequency_3d: object = None
	"""
	A list containing the output frequency of all time ranges in the transient analysis of this load, for the 3d responses.

	"""

	transient_step_3d: object = None
	"""
	A list containing the time step of all time ranges in the transient analysis of this load, for the 3d responses.

	"""

	response_elements: object = None
	"""
	A list containing all response elements requested by the user. Each entry of the list is a ResponseElement instance.

	"""

	response_panels: object = None
	"""
	A list containing all response panels requested by the user. Each entry of the list is a ResponsePanel instance.

	"""

	filename: str = None
	"""
	The filename where the load is originally stored

	"""

	responses: list = None
	"""
	A list of responses assigned to load

	"""

	def is_response_enabled(self, resp: object) -> bool:

		"""

		Checks if response is included in calculation


		Parameters
		----------
		resp : object
			Response object

		Returns
		-------
		bool
			Returns true if response is included

		"""

class ResponseElement:

	"""

	Class containing information for NVH response elements.

	See Also
	--------
	nvh.Load, nvh.GetModalFrequencyResponseLoads

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    component_name = "Default"
		    loads = nvh.GetModalFrequencyResponseLoads(component_name)
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent index:", l.parent_index)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for i, datai in enumerate(l.frequency_start_3d):
		            print(
		                "\\t",
		                "3D frequency range:",
		                l.frequency_start_3d[i],
		                ";",
		                l.frequency_end_3d[i],
		                ";",
		                l.frequency_step_3d[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		        for datan in l.response_elements:
		            print("\\t\\t", "response element: id:", datan.id)
		            print("\\t\\t", "response element: type:", datan.type)
		            print("\\t\\t", "response element: name:", datan.name)
		            print(
		                "\\t\\t",
		                "response element: coordinate_system_id:",
		                datan.coordinate_system_id,
		            )
		        for datap in l.response_panels:
		            print("\\t\\t", "response panel: name:", datap.name)
		            print("\\t\\t", "response panel: included:", datap.included)
		            elems = ""
		            for datar in datap.element_ids:
		                elems += " " + str(datar)
		                print("\\t\\t\\t", "Panel Element ids:", elems)
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	The id of the response element.

	"""

	type: int = None
	"""
	The type of the response element.

	"""

	name: str = None
	"""
	The name of the response element.

	"""
class ResponsePanel:

	"""

	Class containing information for NVH response panels.

	See Also
	--------
	nvh.Load, nvh.GetModalFrequencyResponseLoads

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    component_name = "Default"
		    loads = nvh.GetModalFrequencyResponseLoads(component_name)
		    for l in loads:
		        print("load id:", l.id)
		        print("\\t", "load name:", l.name)
		        print("\\t", "load parent index:", l.parent_index)
		        print("\\t", "load type:", l.type)
		        print("\\t", "load included:", l.included)
		        print("\\t", "load component:", l.component)
		        print("\\t", "load node_name:", l.node_name)
		        print("\\t", "load node_id:", l.node_id)
		        print("\\t", "load dof:", l.dof)
		        print("\\t", "load factor:", l.factor)
		        print("\\t", "load amplitude_table:", l.amplitude_table)
		        print("\\t", "load phase_table:", l.phase_table)
		        print("\\t", "load real_table:", l.real_table)
		        print("\\t", "load imaginary_table:", l.imaginary_table)
		        print("\\t", "load time_delay:", l.time_delay)
		        print("\\t", "load phase_delay:", l.phase_delay)
		        print("\\t", "load coordinate_system_id:", l.coordinate_system_id)
		        for i, datai in enumerate(l.frequency_start):
		            print(
		                "\\t",
		                "frequency range:",
		                l.frequency_start[i],
		                ";",
		                l.frequency_end[i],
		                ";",
		                l.frequency_step[i],
		            )
		        for i, datai in enumerate(l.frequency_start_3d):
		            print(
		                "\\t",
		                "3D frequency range:",
		                l.frequency_start_3d[i],
		                ";",
		                l.frequency_end_3d[i],
		                ";",
		                l.frequency_step_3d[i],
		            )
		        for dataj in l.response_nodes:
		            print("\\t\\t", "response node: id:", dataj.id)
		            print("\\t\\t", "response node: name:", dataj.name)
		            print("\\t\\t", "response node: component:", dataj.component)
		            print("\\t\\t", "response node: dofs:", dataj.dofs)
		            print("\\t\\t", "response node: factor:", dataj.factor)
		            print(
		                "\\t\\t",
		                "response node: coordinate_system_id:",
		                dataj.coordinate_system_id,
		            )
		        for datak in l.response_node_lcs:
		            print("\\t\\t", "response node LC: id:", datak.id)
		            print("\\t\\t", "response node LC: name:", datak.name)
		            print("\\t\\t", "response nodes in LC:", len(datak.nodes))
		            for datam in datak.nodes:
		                print("\\t\\t\\t", "LC node: id:", datam.id)
		                print("\\t\\t\\t", "LC node: name:", datam.name)
		                print("\\t\\t\\t", "LC node: component:", datam.component)
		                print("\\t\\t\\t", "LC node: dofs:", datam.dofs)
		                print("\\t\\t\\t", "LC node: factor:", datam.factor)
		                print(
		                    "\\t\\t\\t",
		                    "LC node: coordinate_system_id:",
		                    datam.coordinate_system_id,
		                )
		        for datan in l.response_elements:
		            print("\\t\\t", "response element: id:", datan.id)
		            print("\\t\\t", "response element: type:", datan.type)
		            print("\\t\\t", "response element: name:", datan.name)
		            print(
		                "\\t\\t",
		                "response element: coordinate_system_id:",
		                datan.coordinate_system_id,
		            )
		        for datap in l.response_panels:
		            print("\\t\\t", "response panel: name:", datap.name)
		            print("\\t\\t", "response panel: included:", datap.included)
		            elems = ""
		            for datar in datap.element_ids:
		                elems += " " + str(datar)
		                print("\\t\\t\\t", "Panel Element ids:", elems)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the response panel.

	"""

	included: int = None
	"""
	Indicates if the current panel is included or excluded:
	- 0: excluded
	- 1: included

	"""

	element_ids: object = None
	"""
	A list containing the ids of the elements included in the panel.

	"""
class ModalMatrix:

	"""

	Class that contains information about Modal Matrices.

	See Also
	--------
	nvh.GetModalMatricesFromFile

	Examples
	--------
	::

		# PYTHON script
		from meta import nvh
		
		
		def main():
		    filename = "example.op2"
		    deck = "NASTRAN"
		    result = nvh.GetModalMatricesFromFile(filename, deck)
		    for m in result:
		        print(m.name)
		        print("Rows: " + str(m.rows))
		        print("Columns: " + str(m.columns))
		        print("Form: " + m.form)
		        print("Values: " + str(m.values))
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	The name of the modal matrix. Can be ModalViscousDampingMatrix, ModalStructuralDampingMatrix, ModalStiffnessMatrix, ModalPEMTRIMMatrix.

	"""

	rows: int = None
	"""
	The number of rows of the matrix.

	"""

	columns: int = None
	"""
	The number of columns of the matrix.

	"""

	form: str = None
	"""
	The form of the matrix. Can be Diagonal, General rectangular, Identity, Lower triangular, Upper triangular, Square, Symmetric, Unknown.

	"""

	values: float = None
	"""
	The values of the matrix. Depending on the matrix, the values can be either float or complex.

	"""
class LcNode:

	"""

	A helper class that contains information about the nodes contained in a linear combination response. Usually contained in an ResponseNodeLc object.

	See Also
	--------
	nvh.GetFrfAssemblyLoads, nvh.GetModalResponseLoads, nvh.ResponseNodeLc

	Examples
	--------
	::

		# PYTHON script
		from meta import nvh
		
		
		def main():
		    loads = nvh.GetFrfAssemblyLoads()
		    for l in loads:
		        for k in l.response_node_lcs:
		            for j in k.nodes:
		                print("id: " + str(j.id))
		                print("name: " + j.name)
		                print("dofs: " + str(j.dofs))
		                print("component name: " + str(j.component))
		                print("coordinate system: " + str(j.coordinate_system_id))
		                print("factor: " + str(j.factor))
		
		
		if __name__ == "__main__":
		    main()

	"""


	id: int = None
	"""
	The id of the node.

	"""

	name: str = None
	"""
	The name of the node.

	"""

	dofs: int = None
	"""
	The degree of freedom of the node that participates in the linear combination.

	"""

	component: str = None
	"""
	The name of the component the node belongs to. Used in FRF Assemby tool.

	"""

	coordinate_system_id: int = None
	"""
	The id of the coordinate system that will be used for the node.

	"""

	factor: float = None
	"""
	The scale factor that adjusts the contribution of the node in the linear combination.

	"""
class FrfAssembly():

	"""

	Class for FrfAssembly tool.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    frfassembly = nvh.FrfAssembly()
		    if frfassembly:
		        for comp in frfassembly.components:
		            print(comp)
		        for conn in frfassembly.connections:
		            print(conn)
		        for resp in frfassembly.responses:
		            print(resp.name)
		
		
		if __name__ == "__main__":
		    main()

	"""


	components: list = None
	"""
	Components involved in the FRF Assembly analysis.

	"""

	connections: list = None
	"""
	Connections defined in the FRF Assembly analysis.

	"""

	loads: list = None
	"""
	Loads defined in the FRF Assembly analysis.

	"""

	responses: list = None
	"""
	Responses defined in the Frf Assembly analysis.

	"""

	name: str = None
	"""
	Name of Frf Assembly analysis.

	"""
class RigidConnection():

	"""

	Class for Frf Assembly connections of type Rigid

	See Also
	--------
	meta.nvh.FrfAssembly

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import nvh
		
		
		def main():
		    frfassembly = nvh.FrfAssembly()
		    if frfassembly:
		        for conn in frfassembly.connections:
		            if c.type == "RIGID":
		                print("Rigid Connection: " + c.name)
		                print("\\tPoint 1: " + str(c.point1))
		                print("\\tPoint 2: " + str(c.point2))
		                print("\\tCsys: " + str(c.csys))
		                print("\\tactiveDofs: " + str(c.activeDofs))
		                print("\\tactiveDofsInt: " + str(c.activeDofsInt))
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of connection.

	"""

	type: str = None
	"""
	Type of connection. In this case the type is 'RIGID'.

	"""

	point1: object = None
	"""
	The information about the first connection point (Component, Node id, Node name).

	"""

	point2: object = None
	"""
	The information about the second connection point (Component, Node id, Node name).

	"""

	csys: int = None
	"""
	The local coordinate system of the connection. Zero refers to GCS.

	"""

	optMin: str = None
	"""
	The minimum modification percentage of the connection values for optimization.

	"""

	optMax: str = None
	"""
	The maximum modification percentage of the connection values for optimization.

	"""

	depends: str = None
	"""
	The connection name that this connection depends on.

	"""

	activeDofs: list = None
	"""
	A list of strings representing the active dofs. The list may contain one or more of the following strings : "TX", "TY", "TZ", "RX", "RY", "RZ".

	"""

	activeDofsInt: int = None
	"""
	An integers representing the active dofs. For instance, the integer "123" means that the dofs TX, TY and TZ are active.

	"""
class Response:

	"""

	Class containing information for NVH responses

	See Also
	--------
	ResponseNodeLc, FrfAssembly, Load

	Examples
	--------
	::

		# PYTHON script
		import os
		import meta
		from meta import nvh
		
		
		def main():
		    frf_assembly = nvh.FrfAssembly()
		    if frf_assembly:
		        for c in frf_assembly.responses:
		            print("Name: " + str(c.name))
		            print("entity_type " + str(c.entity_type))
		            print("variables: " + str(c.variables))
		            print("component: " + str(c.component))
		            print("entity_name: " + str(c.entity_name))
		            print("entity_id: " + str(c.entity_id))
		            print("linear_combine: " + str(c.linear_combine))
		            print("directions: " + str(c.directions))
		            print("coordinate_system_id: " + str(c.coordinate_system_id))
		            print("on_range: " + str(c.on_range))
		            print("top_peaks: " + str(c.top_peaks))
		            print("on_responses: " + str(c.on_responses))
		            print("standard: " + str(c.standard))
		            print("participation: " + str(c.participation))
		            print("tpa: " + str(c.tpa))
		            print("sensitivity: " + str(c.sensitivity))
		            print("pathstiffnessanalysis: " + str(c.pathstiffnessanalysis))
		            print("output_type: " + str(c.output_type))
		            print("options: " + str(c.options))
		            print("options:")
		            print("\\t peaks_db_ref: " + str(c.options.peaks_db_ref))
		            print("\\t peaks_filtering: " + str(c.options.peaks_filtering))
		            print("\\t override_defaults: " + str(c.options.override_defaults))
		            print("\\t prefix: " + str(c.options.prefix))
		            print("\\t state_labels: " + str(c.options.state_labels))
		            print("\\t gpf_direction: " + str(c.options.gpf_direction))
		            print("\\t create_vector: " + str(c.options.create_vector))

	"""


	name: str = None
	"""
	Response name

	"""

	entity_type: str = None
	"""
	Response entity type

	"""

	variables: list = None
	"""
	Response variables list

	"""

	component: str = None
	"""
	Response component

	"""

	entity_name: str = None
	"""
	Response entity name

	"""

	entity_id: int = None
	"""
	Response entity id

	"""

	linear_combine: object = None
	"""
	Response linear combination node

	"""

	directions: list = None
	"""
	Response directions

	"""

	coordinate_system_id: int = None
	"""
	Response coordinate system id

	"""

	on_range: list = None
	"""
	Response calculation subrange

	"""

	top_peaks: int = None
	"""
	Response top peaks number

	"""

	on_responses: list = None
	"""
	Response list used for peak calculation

	"""

	standard: str = None
	"""
	Response standard calculation choice

	"""

	participation: str = None
	"""
	Response participation calculation choice

	"""

	tpa: str = None
	"""
	Response TPA calculation choice

	"""

	sensitivity: str = None
	"""
	Response sensitivity calculation choice

	"""

	pathstiffnessanalysis: str = None
	"""
	Response path stiffness analysis calculation choice

	"""

	output_type: str = None
	"""
	Response output type

	"""

	options: object = None
	"""
	Response options

	"""
