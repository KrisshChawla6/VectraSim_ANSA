from __future__ import annotations
from typing import *

def CrossProduct(vec1: object, vec2: object) -> object:

	"""

	This function calculates the cross product of the two vectors.

	Parameters
	----------
	vec1 : object
		A tuple representing vector 1.

	vec2 : object
		A tuple representing vector 2.

	Returns
	-------
	object
		Returns a new vector (list) representing the cross product.

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    m1 = (0.15, 1, 0.3)
		    m2 = (0.2, 0.54, -1)
		    m = calc.CrossProduct(m1, m2)
		    print(m)


	"""

def DotProduct(vec1: object, vec2: object) -> float:

	"""

	This function calculates the dot product of two vectors.

	Parameters
	----------
	vec1 : object
		A tuple representing Vector 1.

	vec2 : object
		A tuple representing Vector 2.

	Returns
	-------
	float
		Returns a double precision value representing the dot product.

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    m1 = (-0.3, 0.45, -0.97)
		    m2 = (0.76, 0.15, -0.39)
		
		    m = calc.DotProduct(m1, m2)
		    print(m)


	"""

def GetDoeStudyExperimentsForParams(parameters: object, algorithm: str, level: int, experiments_number: int, seed: int, taguchi_array: str, reject_duplicates: bool) -> object:

	"""

	Function to get the experiments of the input parameters 
	that are defined as named tuples with the fieldnames "min"
	and "max". For the definition of the input parameters the
	"import collections" statement is essential (look at the example).

	Parameters
	----------
	parameters : object
		list or objects of parameters defined as named 
		tuples with the fieldnames "min" and "max"

	algorithm : str
		algorithm used to generate the experiments.
		Supported algorithms are "Full Factorial", "Uniform Latin Hypercube", 
		"Optimal Latin Hypercube (ESE)", "Symmetric Optimal Latin Hypercube", 
		"Random", "Taguchi Orthogonal Arrays", 
		"Modified Extensible Lattice Sequence" and "Linear".

	level : int, optional
		integer value used for all parameters ("Full 
		Factorial" or "Taguchi Orthogonal Arrays" 
		algorithms). Default value is 2.

	experiments_number : int, optional
		the number of the generated experiments (used in 
		"Uniform Latin Hypercube", "Random" and "Linear" 
		algorithms).

	seed : int, optional
		positive number used to initialize the random number generator
		(used in "Uniform Latin Hypercube" and "Random" algorithms).

	taguchi_array : str, optional
		Taguchi array to be used for experiments generation. 
		Taguchi array is related to the level value. 
		For level = 2, supported arrays are "L4", "L8", "L12", 
		"L16", "L20", "L24", "L32", "L64", "L128", "L256".
		For level = 3, supported arrays are "L9", "L18", "L27", 
		"L36", "L54", "L81", "L108".
		For level = 4, supported arrays are "L16", "L32", "L64".
		For level = 5, supported arrays are "L25", "L50".

	reject_duplicates : bool, optional
		reject duplicate experiments in Taguchi algorithm

	Returns
	-------
	object
		Returns a list of lists (every list corresponds to a single experiment).

	Examples
	--------
	::

		import os
		import meta
		import collections
		
		
		def main():
		    Parameter = collections.namedtuple("Parameter", ["min", "max"])
		    p1 = Parameter(1.5, 2.1)
		    p2 = Parameter(1, 5.1)
		    p3 = Parameter(-2.2, 4.1)
		
		    print(p1)
		    print(p2)
		    print(p3)
		
		    params = []
		    params.append(p1)
		    params.append(p2)
		    params.append(p3)
		
		    designs1 = meta.calc.GetDoeStudyExperimentsForParams(
		        params, "Random", experiments_number=3, seed=345
		    )
		    print("DOE Study experiments = ", designs1)
		
		    designs2 = meta.calc.GetDoeStudyExperimentsForParams(
		        params, "Full Factorial", level=3
		    )
		    print("DOE Study experiments = ", designs2)
		
		    designs3 = meta.calc.GetDoeStudyExperimentsForParams(
		        params, "Uniform Latin Hypercube", seed=467, experiments_number=5
		    )
		    print("DOE Study experiments = ", designs3)
		
		    designs4 = meta.calc.GetDoeStudyExperimentsForParams(
		        parameters=params, algorithm="Taguchi Orthogonal Arrays", taguchi_array="L16"
		    )
		    print("DOE Study experiments = ", designs4)
		
		    designs5 = meta.calc.GetDoeStudyExperimentsForParams(
		        params, "Linear", experiments_number=3
		    )
		    print("DOE Study experiments = ", designs5)
		
		
		if __name__ == "__main__":
		    main()


	"""

def Normalize(vec: list) -> list:

	"""

	This function normalizes a vector (ie. makes its Eucledean norm equal to 1)

	Parameters
	----------
	vec : list
		Vector to normalize.

	Returns
	-------
	list
		It returns a list, where each member is regarded as a vector component.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import calc
		
		
		def main():
		    m1 = list()
		    m1.append(1.0)
		    m1.append(2.0)
		    m1.append(3.0)
		    m = calc.Normalize(m1)
		    print(m[0], m[1], m[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def TransposeMatrix(matrix: object) -> object:

	"""

	This function is used to transpose a matrix given as a list of lists.

	Parameters
	----------
	matrix : object
		A list of vectors (lists) representing the Matrix to transpose.

	Returns
	-------
	object
		It returns a list where each member is a list representing a vector.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import calc
		
		
		def main():
		    m1 = list()
		    m1.append(1)
		    m1.append(2)
		    m1.append(3)
		
		    m2 = list()
		    m2.append(2)
		    m2.append(3)
		    m2.append(4)
		
		    m = list()
		    m.append(m1)
		    m.append(m2)
		
		    print(m[0], m[1])
		
		    k = calc.TransposeMatrix(m)
		
		    print(k[0], k[1], k[2])
		
		
		if __name__ == "__main__":
		    main()


	"""

def CartesianToSpherical(coordinates: object) -> object:

	"""

	Converts the cartesian coordinates to spherical coordinates.

	Parameters
	----------
	coordinates : object

	Returns
	-------
	object
		The return value is a list with spherical coordinates.

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    point = (1, 1, 1)
		    new_point = calc.CartesianToSpherical(point)
		    # The result is : new_point == [1.73205081,0.785398163,0.955316618]


	"""

def CylindricalToCartesian(coordinates: object):

	"""

	Converts the cylindrical coordinates to cartesian coordinates.

	Parameters
	----------
	coordinates : object
		(1x3) with cylindrical coordinates

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    point = (1.41421356, 0.785398163, 1)
		    new_point = calc.CylindricalToCartesian(point)
		
		    # The result is : new_point[1,1,1]


	"""

def CylindricalToSpherical(coordinates: object):

	"""

	Converts the cylindrical coordinates to spherical coordinates.

	Parameters
	----------
	coordinates : object
		(1x3) with cylindrical coordinates

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    point = (1.41421356, 0.785398163, 1)
		    new_point = calc.CylindricalToSpherical(point)
		    # The result is :  [1.73205081,0.785398163,0.955316618]


	"""

def NormalVec(vec: object):

	"""

	This function compute a unit normal vector of input vector 'vec'. At the end the dot product of the vectors must be 0.

	Parameters
	----------
	vec : object
		describing the vector

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    vec = (1, 0)
		    vecNrm = calc.NormalVec(m1)  # |vecNrm| == 1
		    dot = calc.DotProduct(vec, vecNrm)  # the value 'dot' is '0.'


	"""

def ProjectPointToLineSegment(line_segment_point_1: object, line_segment_point_2: object, project_point: object):

	"""

	This function computes the projection point of a point on a line segment.

	Parameters
	----------
	line_segment_point_1 : object
		a list of coordinates that define the first end point

	line_segment_point_2 : object
		a list of coordinates that define the second end point

	project_point : object
		a list of coordinates that define the point to be projected

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    m = calc.ProjectPointToLineSegment(
		        (0.0, 0.0, 10.0), (-1.0, 0.0, 0.0), (1.0, 0.0, 0.0)
		    )


	"""

def ProjectPointToTriangle(triangle_point_1: object, triangle_point_2: object, triangle_point_3: object, project_point: object):

	"""

	This function computes the projection point of a point on a triangle. The first point is the point to be projected on the triangle and the other three points are the corners of the triangle.

	Parameters
	----------
	triangle_point_1 : object
		A list with the coordinates of the 1st node of the triangle.

	triangle_point_2 : object
		A list with the coordinates of the 2nd node of the triangle.

	triangle_point_3 : object
		A list with the coordinates of the 3rd node of the triangle.

	project_point : object
		A list with the coordinates of point to be projected.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import calc
		
		
		def main():
		    triangle_p1 = (0.0, 0.0, 10.0)
		    triangle_p2 = (-1.0, -1.0, 0.0)
		    triangle_p3 = (1.0, -1.0, 0.0)
		    orig_point = (0.0, 1.0, 0.0)
		    proj_point = calc.ProjectPointToTriangle(
		        triangle_p1, triangle_p2, triangle_p3, orig_point
		    )
		    print(proj_point)
		
		
		if __name__ == "__main__":
		    main()


	"""

def SphericalToCartesian(coordinates: object):

	"""

	This function converts spherical coordinates to cartesian coordinates.

	Parameters
	----------
	coordinates : object
		(1x3) with spherical coordinates

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    point = (1.73205081, 0.785398163, 0.955316618)
		    new_point = calc.SphericalToCartesian(point)
		    # The result is : new_point == [1,1,1]


	"""

def SphericalToCylindrical(coordinates: object):

	"""

	This function converts spherical coordinates to cylindrical coordinates.

	Parameters
	----------
	coordinates : object
		The input data is a list (1x3) with spherical coordinate

	Examples
	--------
	::

		import meta
		from meta import calc
		
		
		def main():
		    point = (1.73205081, 0.785398163, 0.955316618)
		    new_point = calc.SphericalToCylindrical(point)
		    # The result is : new_point == [1.41421356,0.785398163,1]


	"""

def ConvertEulerAnglesToRotationMatrix_XYZ(RotAngles: object) -> object:

	"""

	Convert Euler angles to rotation matrix. The order of rotations is:

	- 1st rotation around original axis 'X'.
	- 2nd rotation around a new axis 'Y'.
	- 3rd rotation around a newest axis 'Z'.

	Parameters
	----------
	RotAngles : object
		A list of rotation angles in radians.

	Returns
	-------
	object
		Returns a 3d-rotation matrix (3x3) as a list. The rotation matrix relates the original coordinate system to the transformed coordinate system.

	Examples
	--------
	::

		# PYTHON script
		import math
		import meta
		from meta import calc
		
		
		def main():
		    RotAngles = list()
		    RotAngles.append(math.radians(23))
		    RotAngles.append(math.radians(37))
		    RotAngles.append(math.radians(19))
		
		    RotMatrix = calc.ConvertEulerAnglesToRotationMatrix_XYZ(RotAngles)
		
		    for row in range(0, 3):
		        for col in range(0, 3):
		            print("{:1.3f}".format(RotMatrix[row][col]), end="\\t")
		        print("\\n")
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConvertEulerAnglesToRotationMatrix_ZXZ(RotAngles: object) -> object:

	"""

	Convert Euler angles to rotation matrix. The order of rotations is:

	- 1st rotation around original axis 'Z'.
	- 2nd rotation around a new axis 'X'.
	- 3rd rotation around a newest axis 'Z'.

	Parameters
	----------
	RotAngles : object
		A list of rotation angles in radians.

	Returns
	-------
	object
		Returns a 3d-rotation matrix (3x3) as a list. The rotation matrix relates the original coordinate system to the transformed coordinate system.

	Examples
	--------
	::

		# PYTHON script
		import math
		import meta
		from meta import calc
		
		
		def main():
		    RotAngles = list()
		    RotAngles.append(math.radians(23))
		    RotAngles.append(math.radians(37))
		    RotAngles.append(math.radians(19))
		
		    RotMatrix = calc.ConvertEulerAnglesToRotationMatrix_ZXZ(RotAngles)
		
		    for row in range(0, 3):
		        for col in range(0, 3):
		            print("{:1.3f}".format(RotMatrix[row][col]), end="\\t")
		        print("\\n")
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConvertRotationMatrixToEulerAngles_XYZ(RotMatRow1: object, RotMatRow2: object, RotMatRow3: object) -> object:

	"""

	Convert the 3d-rotation matrix to the X-Y-Z combination of Euler angles. The order of rotations is:

	- 1st rotation around original axis 'X'.
	- 2nd rotation around a new axis 'Y'.
	- 3rd rotation around a newest axis 'Z'.

	Parameters
	----------
	RotMatRow1 : object
		A list with three numbers representing the first row of the rotation matrix.

	RotMatRow2 : object
		A list with three numbers representing the second row of the rotation matrix.

	RotMatRow3 : object
		A list with three numbers representing the third row of the rotation matrix.

	Returns
	-------
	object
		Returns a list with the three Euler angles of X-Y-Z combination in radians.

	Examples
	--------
	::

		# PYTHON script
		import math
		import meta
		from meta import calc
		
		
		def main():
		    RotMatRow1 = (0.755, 0.522, -0.397)
		    RotMatRow2 = (-0.260, 0.794, 0.550)
		    RotMatRow3 = (0.602, -0.312, 0.735)
		
		    AnglesEuler_XYZ = calc.ConvertRotationMatrixToEulerAngles_XYZ(
		        RotMatRow1, RotMatRow2, RotMatRow3
		    )
		
		    for Angle in AnglesEuler_XYZ:
		        print("{:1.1f}".format(math.degrees(Angle)))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConvertRotationMatrixToEulerAngles_ZXZ(RotMatRow1: object, RotMatRow2: object, RotMatRow3: object) -> object:

	"""

	Convert the 3d-rotation matrix to the Z-X-Z combination of Euler angles. The order of rotations is:

	- 1st rotation around original axis 'Z'.
	- 2nd rotation around a new axis 'X'.
	- 3rd rotation around a newest axis 'Z'.

	Parameters
	----------
	RotMatRow1 : object
		A list with three numbers representing the first row of the rotation matrix.

	RotMatRow2 : object
		A list with three numbers representing the second row of the rotation matrix.

	RotMatRow3 : object
		A list with three numbers representing the third row of the rotation matrix.

	Returns
	-------
	object
		Returns a list with the three Euler angles of Z-X-Z combination in radians.

	Examples
	--------
	::

		# PYTHON script
		import math
		import meta
		from meta import calc
		
		
		def main():
		    RotMatRow1 = (0.769, 0.609, 0.196)
		    RotMatRow2 = (-0.595, 0.568, 0.569)
		    RotMatRow3 = (0.235, -0.554, 0.799)
		
		    AnglesEuler_ZXZ = calc.ConvertRotationMatrixToEulerAngles_ZXZ(
		        RotMatRow1, RotMatRow2, RotMatRow3
		    )
		
		    for Angle in AnglesEuler_ZXZ:
		        print("{:1.1f}".format(math.degrees(Angle)))
		
		
		if __name__ == "__main__":
		    main()


	"""

def ConvertRotationMatrixToEulerAxisAngle(RotationMatrix1: object, RotationMatrix2: object, RotationMatrix3: object) -> object:

	"""

	Convert the 3d-rotation matrix to the Euler axis and angle.

	Parameters
	----------
	RotationMatrix1 : object
		1x3 vector (list of numbers).

	RotationMatrix2 : object
		1x3 vector (list of numbers).

	RotationMatrix3 : object
		1x3 vector (list of numbers).

	Returns
	-------
	object
		Returns a tuple that has a length of two. The first item is a tuple '1x3' of floats and it represents the vector of the Euler axis. The second item is a float value of the Euler rotation angle in radians.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import calc
		
		
		def main():
		    RotMat = list()
		    RotMat.append([-0.508828, 0.0423415, 0.859826])
		    RotMat.append([-0.531775, -0.8009058, -0.2752548])
		    RotMat.append([0.6769852, -0.5972913, 0.4300396])
		
		    EulerAxisVectorAngle = calc.ConvertRotationMatrixToEulerAxisAngle(
		        RotMat[0], RotMat[1], RotMat[2]
		    )
		
		    print(
		        "EulerAxisVector: ",
		        EulerAxisVectorAngle[0][0],
		        EulerAxisVectorAngle[0][1],
		        EulerAxisVectorAngle[0][2],
		    )
		    print("EulerAxisAngle: ", EulerAxisVectorAngle[1])
		
		
		if __name__ == "__main__":
		    main()


	"""

