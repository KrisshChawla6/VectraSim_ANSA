from __future__ import annotations
from typing import *


def CheckIntersectionOfVolumes(volume1: object, volume2: object) -> object:
    """

    Calculates the volumes of two ortho-parallelepiped boxes in 3d space and the common volume of them.

    Parameters
    ----------
    volume1 : object
            A list with the coordinates of 8-corners of first ortho-parallelepiped box in 3d space.

    volume2 : object
            A list with the coordinates of 8-corners of second ortho-parallelepiped box in 3d space.

    Returns
    -------
    object
            Returns a list with three values. The first value of the list is the volume of the first box.
            The second value of the list is the volume of the second box. The last value of the list is the
            common volume of the two boxes. If the value of the common volume is equal to zero, the two boxes are
            not intersected in 3d space.

    Examples
    --------
    ::

            import ansa
            from ansa import calc
            from ansa import base
            from ansa import constants


            def main():
                # box 1
                point_a = []
                point_b = []
                xyz_a = []
                xyz_b = []
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 1))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 2))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 9))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 11))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 12))
                point_a.append(base.GetEntity(constants.NASTRAN, "POINT", 10))

                # box 2
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 5))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 6))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 7))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 8))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 14))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 15))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 16))
                point_b.append(base.GetEntity(constants.NASTRAN, "POINT", 13))

                # CREATE THE MATRIX WITH COORDINATES OF box 1
                vals = ("X", "Y", "Z")
                for i in range(8):
                    ret = base.GetEntityCardValues(constants.NASTRAN, point_a[i], vals)
                    xyz_a.append((ret["X"], ret["Y"], ret["Z"]))
                # CREATE THE MATRIX WITH COORDINATES OF box 2
                for i in range(8):
                    ret = base.GetEntityCardValues(constants.NASTRAN, point_b[i], vals)
                    xyz_b.append((ret["X"], ret["Y"], ret["Z"]))
                # CALL SCRIPT FUNCTION
                ret_mat = calc.CheckIntersectionOfVolumes(xyz_a, xyz_b)

                # PRINT THE RESULTS OF CALCULATION
                print("VOLUME OF BOX A: ", ret_mat[0])
                print("VOLUME OF BOX B: ", ret_mat[1])
                print("COMMON VOLUME OF BOXES: ", ret_mat[2])


    """


def GetCoordTransformMatrix4x3(
    deck: int, entity: object, x0: float, y0: float, z0: float
) -> object:
    """

    This function returns a transformation matrix of a coordinate system according to the global coordinate system.

    Parameters
    ----------
    deck : int
            The deck constant.

    entity : object
            The coordinate system whose transformation matrix will be calculated.

    x0 : float
            The x-coordinate of the reference point. Needed for the case of cylindrical or
            spherical coordinate system. In case of rectangular coordinate system,
            these coordinates do not influence the results.

    y0 : float
            The y-coordinate of the reference point. Needed for the case of cylindrical or
            spherical coordinate system. In case of rectangular coordinate system,
            these coordinates do not influence the results.

    z0 : float
            The z-coordinate of the reference point. Needed for the case of cylindrical or
            spherical coordinate system. In case of rectangular coordinate system,
            these coordinates do not influence the results.

    Returns
    -------
    object
            On success, it returns a list that contains the 4x3 matrix.
            The first three rows correspond to the rotation matrix and the fourth row to the translation.
            On failure, it returns None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import calc


            def test():
                cs = base.GetEntity(constants.LSDYNA, "DEFINE_COORDINATE_SYSTEM", 1)
                ret4x3 = calc.GetCoordTransformMatrix4x3(constants.LSDYNA, cs, 0, 20, 30)


    """


def GetVectorsOfCord(coord: object) -> object:
    """

    The function computes the three unit-vectors of a given coordinate system.
    The vectors have coordinates at global coordinate-system.

    Parameters
    ----------
    coord : object
            The local coordinate system.

    Returns
    -------
    object
            Returns a list containing the three unit-vectors of the given coordinate system.

            The order is :
            a) The first  is (1x3) list with coordinates of the axial 'xx'.
            b) The second is (1x3) list with coordinates of the axial 'yy'.
            c) The third  is (1x3) list with coordinates of the axial 'zz'.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import calc


            def main():
                coord = base.GetEntity(ansa.constants.NASTRAN, "CORD_NODES_R", 1)
                vecs = calc.GetVectorsOfCord(coord)
                axial_X = vecs[0]
                axial_Y = vecs[1]
                axial_Z = vecs[2]

                uX = axial_X[0]
                vX = axial_X[1]
                wX = axial_X[2]
                uY = axial_Y[0]
                vY = axial_Y[1]
                wY = axial_Y[2]
                uZ = axial_Z[0]
                vZ = axial_Z[1]
                wZ = axial_Z[2]


    """


def GlobalToLocal(cord_id: int, coordinates: object, type: str) -> object:
    """

    The function converts the global-coordinates of one 'point' or 'vector' to the local-coordinates
    for one specific local-cordinate with (id_cord).

    Parameters
    ----------
    cord_id : int
            The 'id' of the local-coordinate system.

    coordinates : object
            A list with the coordinates of a 'point' or a 'vector' at the global-system.

    type : str
            The string 'point' or 'vector'.

    Returns
    -------
    object
            Returns a list with the local-coordinates of 'point' or 'vector'.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                cord_id = 1
                point_coords = (10, 10, 0)
                new_coords = calc.GlobalToLocal(1, point_coords, "point")


    """


def HelixSweep(starting_point: object, period_pitch: float, CURVE: object) -> object:
    """

    This function creates points around a main-curve as a helix.

    Parameters
    ----------
    starting_point : object
            A list with the coordinates of the starting point.

    period_pitch : float
            The step of the helix along the direction of the main-curve.

    CURVE : object
            The object of the curve entity.

    Returns
    -------
    object
            Returns a list with the following contents:
            1) At position [0], there is the number of points.
            2) At position [1], there is a list of the x-coordinates of points.
            3) At position [2], there is a list of the y-coordinates of points.
            4) At position [3], there is a list of the z-coordinates of points.

    Examples
    --------
    ::

            import ansa
            from ansa import calc
            from ansa import base
            from ansa import constants


            def main():
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 166)
                mat_res = calc.HelixSweep((100.0, 25.0, 35.0), 40.0, curve)
                for i in range(mat_res[0]):
                    base.Newpoint(mat_res[1][i], mat_res[2][i], mat_res[3][i])


    """


def LocalSystem(origin: object, point1: object, point2: object) -> object:
    """

    This function calculates the axes directions of a local coordinate system.

    Parameters
    ----------
    origin : object
            The list with the coordinates that correspond to the origin.

    point1 : object
            A list with the coordinates of a point that lies on the z-axis.

    point2 : object, optional
            A list with the coordinates of a point that lies in the x-z plane.

    Returns
    -------
    object
            Returns a tuple of three vectors representing the axis of local system.
            The output tuple is: ((Vector1_x,Vector1_y,Vector1_z), (Vector2_x,Vector2_y,Vector2_z), (Vector3_x,Vector3_y,Vector3_z)).
            The first vector (Vector1) is the local axis x, the second vector (Vector2) is the local axis y,
            and the third vector (Vector3) is the local axis z. The vectors are unit.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                m = calc.LocalSystem(
                    (1, 1, 1), (-3, 1, 1)
                )  # return tuple is : m = ((0,1,0), (0,0,-1), (-1,0,0))


    """


def LocalToGlobal(cord_id: int, coordinates: object, type: str) -> object:
    """

    Converts the local-coordinates of one 'point' or 'vector' to the global-coordinates for a specific local cordinate system.

    Parameters
    ----------
    cord_id : int
            The 'id' of the local-coordinate system.

    coordinates : object
            The list (1x3) with coordinate of 'point' or 'vector'
            at local-system. When the input data is 'vector' on spherical
            or cylindrical coordinate system, you are able to give the
            reference point (in which the vector is applied) with the
            extension of the matrix to (1x6). The three more positions
            of matrix represent the reference coordinates of local system.

    type : str
            'point' or 'vector'. In general, the return coordinates are
            different for 'point' and 'vector'.

    Returns
    -------
    object
            Returns the global-coordinates of 'point' or 'vector'.
            The output data is a list (1x3) with coordinate of 'point' or 'vector' at global-system.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point_coords = [10, 10, 0]
                new_coords = calc.LocalToGlobal(1, point_coords, "point")


    """


def Normalize(vec: list) -> list:
    """

    This function normalizes a vector (ie. makes it unit long).

    Parameters
    ----------
    vec : list
            A list describing the vector.

    Returns
    -------
    list
            Returns a vector (list) of length 1 pointing to the same direction as the original.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                m1 = [1, 2, 3]
                m = calc.Normalize(m1)


    """


def ProjectPointToCons(x_y_z: object, cons: int) -> object:
    """

    This function computes the projection point of one point on 'Cons'.

    Parameters
    ----------
    x_y_z : object
            A list with the coordinates of the point.

    cons : int
            The object of the CONS were the projection will take place.

    Returns
    -------
    object
            Returns a list with the result of the projection.

            The output list can be:
            i) 0 - When cons is not valid.
            ii) A list [ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z] - When the point
                to be projected is projected on 'Cons' between end points.
            iii) A list [ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z, SnapPoint_x,SnapPoint_y,SnapPoint_z] - When the
                 point to be projected is projected on extension of 'Cons', outside the end points.

    Examples
    --------
    ::

            import ansa
            from ansa import calc
            from ansa import base
            from ansa import constants


            def main():
                cons_ref = base.GetEntity(ansa.constants.NASTRAN, "CONS", 1)
                m = calc.ProjectPointToCons((0.0, 0.0, 10.0), cons_ref)


    """


def ProjectPointToContainer(coords: object, entities: object) -> object:
    """

    This function finds the projection of a point to a list of faces and shells.
    If no projection can be found the minimum distance is computed.

    Parameters
    ----------
    coords : object
            The point coordinates are given as a list of [x, y, z].

    entities : object
            The list of entities. It should contain shells, faces, parts,
            properties or set.

    Returns
    -------
    object
            Returns a list that contains:
            a) mat[0][0], mat[0][1], mat[0][2] = the projected point (x,y,z) or the point of the minimum distance.
            b) mat[1] = the found minimum distance d.
            b) mat[2][0], mat[2][1], mat[2][2] = the found minimum distances (dx, dy, dz).
            c) mat[3][0], mat[3][1], mat[3][2] = the normal vector (dx,dy,dz) at the point of projection.
            d) mat[4] = the entity (shell or face) where the projection was found .

    Examples
    --------
    ::

            import ansa
            from ansa import calc
            from ansa import base
            from ansa import constants


            def main():
                ents = [["POINT"], ["SHELL", "FACE"]]

                nodes = base.PickEntities(constants.LSDYNA, ents[0])
                print("All selected points = ", len(nodes))

                container = base.PickEntities(constants.LSDYNA, ents[1])
                print("All selected ents:", len(container))

                if len(nodes) == 1 and len(container) > 0:
                    ret_vals = base.GetEntityCardValues(constants.LSDYNA, nodes[0], ("X", "Y", "Z"))
                    print(
                        "point to be projected (x,y,z): ",
                        ret_vals["X"],
                        ", ",
                        ret_vals["Y"],
                        ", ",
                        ret_vals["Z"],
                    )
                    mat = calc.ProjectPointToContainer(
                        [ret_vals["X"], ret_vals["Y"], ret_vals["Z"]], container
                    )
                    if mat:
                        print(
                            "projected point (x,y,z): ", mat[0][0], ", ", mat[0][1], ", ", mat[0][2]
                        )
                        print(
                            "distance (d,dx,dy,dz): ",
                            mat[1],
                            ", ",
                            mat[2][0],
                            ", ",
                            mat[2][1],
                            ", ",
                            mat[2][2],
                        )
                        print(
                            "normal vector (dx,dy,dz): ",
                            mat[3][0],
                            ", ",
                            mat[3][1],
                            ", ",
                            mat[3][2],
                        )
                        if mat[4]:
                            entity = mat[4]
                            ret = base.GetEntityCardValues(
                                constants.LSDYNA, entity, ("__id__", "__type__")
                            )
                            if ret:
                                print(
                                    "projection found on entity: ",
                                    ret["__type__"],
                                    ", ",
                                    ret["__id__"],
                                )


    """


def ProjectPointToShell(point: object, shell: object) -> object:
    """

    This function computes the projection of a point on a shell.

    Parameters
    ----------
    point : object
            A list with the coordinates of the point to be projected.

    shell : object
            A shell object.

    Returns
    -------
    object
            Returns a tuple with the result of the projection.

            The output tuple can be :
            i) (ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z,) - When the point to be projected is projected on 'Shell' between     the boundary edges of 'Shell'.
            ii)(ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the point to be        projected is projected on extension of 'Shell', out from the boundary edges of 'Shell'.

            The 'Snap Point' is on the boundary of the 'Shell' (on edge or at corner).
            When the input shell is not a reference to a valid shell, exception is raised.

    Examples
    --------
    ::

            import ansa
            from ansa import calc
            from ansa import base
            from ansa import constants


            def main():
                shell = base.GetEntity(constants.NASTRAN, "SHELL", 1)
                m = calc.ProjectPointToShell([0.0, 0.0, 10.0], shell)


    """


def TransformPointMatrix4x3(POINT: object, TRANSF_MATRIX4x3: object) -> object:
    """

    This function transforms a point (x,y,z) according to the given TRANSF_MATRIX4x3.
    TRANSF_MATRIX4x3 is the 4x3 transformation matrix.

    Parameters
    ----------
    POINT : object
            A list with the coordinates of the points.

    TRANSF_MATRIX4x3 : object
            The 4x3 transformation matrix.

    Returns
    -------
    object
            Returns a list with 3 elements [x, y, z] on success and None on error.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                # This example creates the mirror location of a given point (10,20,30),
                # according to the XZ plane

                transf = ([1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0])
                point = (10, 20, 30)

                res = calc.TransformPointMatrix4x3(point, trasnf)
                print(res)


    """


def TransformVectorMatrix4x3(VECTOR: object, TRANSF_MATRIX4x3: object) -> object:
    """

    This function transforms a vector (dx,dy,dz) according to the given TRANSF_MATRIX4x3.
    TRANSF_MATRIX4x3 is the 4x3 transformation matrix.

    Parameters
    ----------
    VECTOR : object
            A list of the vector.

    TRANSF_MATRIX4x3 : object
            The 4x3 list of the transformation matrix.

    Returns
    -------
    object
            Returns a list with 3 elements [dx, dy, dz] on success and 0 on error.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                # This example creates the mirror location of a given point (10,20,30),
                # according to the XZ plane
                transf_matrix = [[1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, 0]]
                vector = [0, 1, 0]

                res = calc.TransformVectorMatrix4x3(vector, trasnf)
                print(res)


    """


def TransposeMatrix(matrix: object) -> object:
    """

    This function is used to transpose a list (matrix).

    Parameters
    ----------
    matrix : object
            A list that will be transposed.

    Returns
    -------
    object
            Returns the resulting list, without modifying the input list.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                m = [[1, 2, 3], [4, 5, 6]]
                k = calc.TransposeMatrix(m)  # k = [[1,4], [2,5], [3,6]]


    """


def CalcAngleOfVectors(vec_1: object, vec_2: object, vec_3: object) -> float:
    """

    This function computes the angle of two or three 3D vectors.

    Parameters
    ----------
    vec_1 : object
            A list defining the first vector.

    vec_2 : object
            A list defining the second vector.

    vec_3 : object, optional
            A list defining the third vector.

    Returns
    -------
    float
            Returns the angle of the vectors in radians (double), which is computed as follows:
            i) When the input list has two vectors, the angle is mathematically defined to be between '0' and 'PI' (inclusive).
            ii) When the input list has three vectors the angle is mathematically defined to be between '0' and '2PI' (inclusive).
            iii) When the input list is not correct the function returns the error value '-PI' .

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                calc.CalcAngleOfVectors(
                    [-17.0, 72.0, 0.0], [61.0, -43, 0.0]
                )  # The return angle in radians is '2.41668002'
                calc.CalcAngleOfVectors(
                    [-17.0, 72.0, 0.0], [61.0, -43, 0.0], [0.0, 0.0, 10.0]
                )  # The return angle in radians is '3.86650528'


    """


def CartesianToCylindrical(coordinates: object) -> object:
    """

    Converts the cartesian coordinates to cylindrical coordinates.

    Parameters
    ----------
    coordinates : object
            A list with the cartesian coordinates to convert.

    Returns
    -------
    object
            Returns a list with the respective cylindrical coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1, 1, 1)
                new_point = calc.CartesianToCylindrical(point)
                # The result is: new_point == [1.41421356, 0.785398163, 1]


    """


def CartesianToSpherical(coordinates: object) -> object:
    """

    Converts the cartesian coordinates to spherical coordinates.

    Parameters
    ----------
    coordinates : object
            A list with the cartesian coordinates to be converted.

    Returns
    -------
    object
            Returns a list with the spherical coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1, 1, 1)
                new_point = calc.CartesianToSpherical(point)
                # The result is : new_point == [1.73205081 ,0.785398163, 0.955316618]


    """


def CylindricalToCartesian(coordinates: object) -> int:
    """

    Converts the cylindrical coordinates to cartesian coordinates.

    Parameters
    ----------
    coordinates : object
            A list with the cylindrical coordinates to be converted.

    Returns
    -------
    int
            Returns a list with the converted cartesian coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1.41421356, 0.785398163, 1)
                new_point = calc.CylindricalToCartesian(point)

                # The result is : new_point = [1,1,1]


    """


def CylindricalToSpherical(coordinates: object) -> object:
    """

    Converts the cylindrical coordinates to spherical coordinates.

    Parameters
    ----------
    coordinates : object
            A list with the cylindrical coordinates to be converted.

    Returns
    -------
    object
            Returns a list with the converted spherical coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1.41421356, 0.785398163, 1)
                new_point = calc.CylindricalToSpherical(point)

                # The result is: [1.73205081, 0.785398163, 0.955316618]


    """


def NormalVec(vec: object) -> object:
    """

    This function computes a unit normal vector from the input vector 'vec'.
    At the end, the dot product of the vectors must be 0.

    Parameters
    ----------
    vec : object
            A list describing the vector.

    Returns
    -------
    object
            Returns a unit vector (list) of the input vector 'vec'.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                vec = (1, 0)
                vecNrm = calc.NormalVec(m1)  # |vecNrm| == 1
                dot = calc.DotProduct(vec, vecNrm)  # the value 'dot' is '0.'


    """


def ProjectPointToLineSegment(
    project_point: object, line_segment_point_1: object, line_segment_point_2: object
) -> object:
    """

    This function computes the projection point of a point on a line segment.

    Parameters
    ----------
    project_point : object
            A list of coordinates that define the point to be projected.

    line_segment_point_1 : object
            A list of coordinates that define the first end point.

    line_segment_point_2 : object
            A list of coordinates that define the second end point.

    Returns
    -------
    object
            Returns a tuple with the result of the projection.

            The output tuple can be:
            i) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z),) - When the point is projected on the
               line segment between end points.
            ii)((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the point
               is projected on the extension of the line segment, outside the end points.

            The 'Snap Point' is one of the two end points of the line segment.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                m = calc.ProjectPointToLineSegment(
                    (0.0, 0.0, 10.0), (-1.0, 0.0, 0.0), (1.0, 0.0, 0.0)
                )


    """


def ProjectPointToTriangle(
    project_point: object,
    triangle_point_1: object,
    triangle_point_2: object,
    triangle_point_3: object,
) -> object:
    """

    This function computes the projection point of a point on a triangle.

    The input list is of the following format:
    [ProjectPoint_x,ProjectPoint_y,ProjectPoint_z, TrianglePoint1_x,TrianglePoint1_y,TrianglePoint1_z,
    TrianglePoint2_x,TrianglePoint2_y,TrianglePoint2_z, TrianglePoint3_x,TrianglePoint3_y,TrianglePoint3_z]
    The first point is the point to be projected on the triangle and the other three points are the corners of the triangle.

    Parameters
    ----------
    project_point : object
            A list with the coordinates of point to be projected.

    triangle_point_1 : object
            A list with the coordinates of the 1st triangle node.

    triangle_point_2 : object
            A list with the coordinates of the 2nd triangle node.

    triangle_point_3 : object
            A list with the coordinates of the 3rd triangle node.

    Returns
    -------
    object
            Returns a list with the result of the projection.

            The output list can be :
            i) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z)) - When the point to
                be projected is projected in triangle.
            ii) ((ProjectedPoint_x, ProjectedPoint_y, ProjectedPoint_z), (SnapPoint_x,SnapPoint_y,SnapPoint_z)) - When the
                 point to be projected is projected outside the triangle area. The 'Snap Point' is the nearest point of the
                 triangle to the projected point.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                m = calc.ProjectPointToTriangle(
                    (0.0, 0.0, 10.0), (-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (0.0, 1.0, 0.0)
                )
                # return list is : m = (0.,0.,0.)


    """


def SphericalToCartesian(coordinates: object) -> object:
    """

    This function converts spherical coordinates to cartesian coordinates.

    Parameters
    ----------
    coordinates : object
            The input data is a list (1x3) with the spherical coordinates to be converted.

    Returns
    -------
    object
            Returns a list with the converted cartesian coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1.73205081, 0.785398163, 0.955316618)
                new_point = calc.SphericalToCartesian(point)
                # The result is : new_point == [1, 1, 1]


    """


def SphericalToCylindrical(coordinates: object) -> object:
    """

    This function converts spherical coordinates to cylindrical coordinates.

    Parameters
    ----------
    coordinates : object
            The input data is a list (1x3) with the spherical coordinates to be converted.

    Returns
    -------
    object
            Returns a list (1x3) with the converted cylindrical coordinates.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                point = (1.73205081, 0.785398163, 0.955316618)
                new_point = calc.SphericalToCylindrical(point)
                # The result is : new_point == [1.41421356, 0.785398163, 1]


    """


def ConvertEulerAnglesToRotationMatrix_XYZ(vector: object) -> object:
    """

    Converts Euler angles to a rotation matrix. The order of the rotations is as follows:
     1st) Rotation around existed axial 'X' is the first rotation.
     2nd) Rotation around a new axial 'Y' is the second rotation.
     3rd) Rotation around a newest axial 'Z' is the last rotation.

    The input data are:
     1) The first rotation angle around axial 'X' (x).
     2) The second rotation angle around new axial 'Y' (y).
     3) The third rotationa angle around newest axial 'Z' (z).

    All the above angles are in radians.

    Parameters
    ----------
    vector : object
            A series of floats.

    Returns
    -------
    object
            Returns a 3d-rotation matrix (3x3) as a list.

            ATTENTION: The rotation matrix is from the source coordinate system to the target coordinate system.

    Examples
    --------
    ::

            import math
            import ansa
            from ansa import calc


            def main():
                x = math.radians(45)
                y = math.radians(90)
                z = math.radians(30)

                v = calc.ConvertEulerAnglesToRotationMatrix_XYZ((x, y, z))
                for row in v:
                    print(", ".join("{:32}".format(x) for x in row))


    """


def ConvertEulerAnglesToRotationMatrix_ZXZ(axis: object) -> object:
    """

    Converts Euler angles to a rotation matrix. The order of the rotations is as follows:
     1st) Rotation around existed axial 'Z' is the first rotation.
     2nd) Rotation around a new axial 'X' is the second rotation.
     3rd) Rotation around a newest axial 'Z' is the last rotation.

    The input data are:
     1) The first rotation angle around axial 'Z' (zAngle1).
     2) The second rotation angle around new axial 'X' (xAngle2).
     3) The third rotationa angle around newest axial 'Z' (zAngle3).

    All the above angles are in radians.

    Parameters
    ----------
    axis : object
            A list of floats respresenting the 3 angles.

    Returns
    -------
    object
            Returns a 3d-rotation matrix (3x3) as a list.

            ATTENTION: The rotation matrix is from the source coordinate system to the target coordinate system.

    Examples
    --------
    ::

            import math
            import ansa
            from ansa import calc


            def main():
                zAngle1 = math.radians(45)
                xAngle2 = math.radians(90)
                zAngle3 = math.radians(30)

                v = calc.ConvertEulerAnglesToRotationMatrix_ZXZ((zAngle1, xAngle2, zAngle3))
                for row in v:
                    print(", ".join("{:32}".format(x) for x in row))


    """


def ConvertRotationMatrixToEulerAngles_XYZ(
    rotationMatrix1: object, rotationMatrix2: object, rotationMatrix3: object
) -> object:
    """

    Converts a 3d-rotation matrix to the combination x-y-z of Euler angles. The order of rotations is as follows:
     1st) Rotation around existing axial 'X' is the first rotation.
     2nd) Rotation around a new axial 'Y' is the second rotation.
     3rd) Rotation around a newest axial 'Z' is the last rotation.

    Parameters
    ----------
    rotationMatrix1 : object
            A list with the coordinates of the first rotation matrix.

    rotationMatrix2 : object
            A list with the coordinates of the second rotation matrix.

    rotationMatrix3 : object
            A list with the coordinates of the third rotation matrix.

    Returns
    -------
    object
            Returns a list containing the three Euler angles of the combination x-y-z.
            The first item of the returned list is the Euler angle of rotation around the existing axial 'X'.
            The second item of the returned list is the Euler angle of rotation around the new axial 'Y'.
            The third item of the returned list is the Euler angle of rotation around the newest axial 'Z'.
            All the above angles are in radians.

    Examples
    --------
    ::

            import math
            import ansa
            from ansa import calc


            def main():
                rotMat1 = (-0.5088281, 0.04234156, 0.8598262)
                rotMat2 = (-0.53177536, -0.8009058, -0.275254)
                rotMat3 = (0.6769852, -0.59729135, 0.43003967)

                anglesEuler_XYZ = calc.ConvertRotationMatrixToEulerAngles_XYZ(
                    rotMat1, rotMat2, rotMat3
                )

                anglesEuler_XYZ_0 = math.radians(anglesEuler_XYZ[0])
                anglesEuler_XYZ_1 = math.radians(anglesEuler_XYZ[1])
                anglesEuler_XYZ_2 = math.radians(anglesEuler_XYZ[2])

                print(anglesEuler_XYZ_0, anglesEuler_XYZ_1, anglesEuler_XYZ_2)


    """


def ConvertRotationMatrixToEulerAngles_ZXZ(
    rotationMatrix1: object, rotationMatrix2: object, rotationMatrix3: object
) -> object:
    """

    Converts a 3d-rotation matrix to the combination z-x-z of Euler angles. The order of rotations is as follows:
     1st) Rotation around the existing axial 'Z' is the first rotation.
     2nd) Rotation around a new axial 'X' is the second rotation.
     3rd) Rotation around a newest axial 'Z' is the last rotation.

    Parameters
    ----------
    rotationMatrix1 : object
            A list with the coordinates of the first rotation matrix.

    rotationMatrix2 : object
            A list with the coordinates of the first rotation matrix.

    rotationMatrix3 : object
            A list with the coordinates of the first rotation matrix.

    Returns
    -------
    object
            Returns a list containing the three Euler angles of the combination z-x-z.
            The first item of the list is the Euler angle of rotation around the existing axial 'Z'.
            The second item of the list is the Euler angle of rotation around the new axial 'X'.
            The third item of the list is the Euler angle of rotation around the newest axial 'Z'.
            All the above angles are in radians.

    Examples
    --------
    ::

            import math
            import ansa
            from ansa import calc


            def main():
                rotMat1 = (-0.5088281, 0.04234156, 0.8598262)
                rotMat2 = (-0.53177536, -0.8009058, -0.275254)
                rotMat3 = (0.6769852, -0.59729135, 0.43003967)

                anglesEuler_ZXZ = calc.ConvertRotationMatrixToEulerAngles_ZXZ(
                    rotMat1, rotMat2, rotMat3
                )

                anglesEuler_ZXZ_0 = math.radians(anglesEuler_ZXZ[0])
                anglesEuler_ZXZ_1 = math.radians(anglesEuler_ZXZ[1])
                anglesEuler_ZXZ_2 = math.radians(anglesEuler_ZXZ[2])

                print(anglesEuler_ZXZ_0, anglesEuler_ZXZ_1, anglesEuler_ZXZ_2)


    """


def ConvertRotationMatrixToEulerAxisAngle(
    rotationMatrix1: object, rotationMatrix2: object, rotationMatrix3: object
) -> object:
    """

    Converts a 3d-rotation matrix to the Euler axis and angle.

    Parameters
    ----------
    rotationMatrix1 : object
            A list with the coordinates of the first rotation matrix.

    rotationMatrix2 : object
            A list with the coordinates of the first rotation matrix.

    rotationMatrix3 : object
            A list with the coordinates of the first rotation matrix.

    Returns
    -------
    object
            Returns a tuple that has a length of two. The first item is a tuple containing 3 floats
            and it represents the vector of Euler axis. The second item is a float value representing
            the Euler rotation angle in radians.

    Examples
    --------
    ::

            import ansa
            from ansa import calc


            def main():
                rotMat = (
                    (-0.5088281, 0.04234156, 0.8598262),
                    (-0.53177536, -0.8009058, -0.275254),
                    (0.6769852, -0.59729135, 0.43003967),
                )

                eAxisAngle = calc.ConvertRotationMatrixToEulerAxisAngle(
                    rotMat[0], rotMat[1], rotMat[2]
                )

                print("axis:", ", ".join(map(str, eAxisAngle[0])))
                print("angle:", eAxisAngle[1])


    """


def ProjectPointsToElements(
    coordinates: list, entities: list, tolerance: float, direction: list = []
) -> list:
    """

    Projects a list of points on a list of elements in a given tolerance and gets the projected point,
    the distance and the projection element.

    It works with SHELL, SOLID, SEGMENT, ELSURFACE, RIGID, ACOUSTIC, CAABSF3/4, ASI3D elements.

    Parameters
    ----------
    coordinates : list
            A list with (x, y, z) coordinates of the points to be projected.

    entities : list
            A list with the elements to check for projection.

    tolerance : float
            The tolerance in which the function checks for a projection.

    direction : list, optional
            A list with the coordinates of the direction vector along which
            the projection is going to take place.
            Search with direction works with SHELL and SOLID elements.

    Returns
    -------
    list
            Returns a list containing objects with the following attributes: projection, distance and entity.
            If no projection is found, entity is None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants


            def main():
                entities = base.CollectEntities(constants.ABAQUS, None, "SHELL")

                points = []
                for ent in entities:
                    (x, y, z) = base.Cog(ent)
                    points.append((x, y, 2))
                ret = calc.ProjectPointsToElements(points, entities, 2.5)

                for proj in ret:
                    if proj is not None:
                        print(proj.projection)
                        print(proj.distance)
                        print(proj.entity)


    """


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

            import ansa
            from ansa import calc


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

            import ansa
            from ansa import calc


            def main():
                m1 = (-0.3, 0.45, -0.97)
                m2 = (0.76, 0.15, -0.39)

                m = calc.DotProduct(m1, m2)
                print(m)


    """


def GetDoeStudyExperimentsForParams(
    parameters: object,
    algorithm: str,
    level: int,
    experiments_number: int,
    seed: int,
    taguchi_array: str,
    reject_duplicates: bool,
) -> object:
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
            import ansa
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

                designs1 = ansa.calc.GetDoeStudyExperimentsForParams(
                    params, "Random", experiments_number=3, seed=345
                )
                print("DOE Study experiments = ", designs1)

                designs2 = ansa.calc.GetDoeStudyExperimentsForParams(
                    params, "Full Factorial", level=3
                )
                print("DOE Study experiments = ", designs2)

                designs3 = ansa.calc.GetDoeStudyExperimentsForParams(
                    params, "Uniform Latin Hypercube", seed=467, experiments_number=5
                )
                print("DOE Study experiments = ", designs3)

                designs4 = ansa.calc.GetDoeStudyExperimentsForParams(
                    parameters=params, algorithm="Taguchi Orthogonal Arrays", taguchi_array="L16"
                )
                print("DOE Study experiments = ", designs4)

                designs5 = ansa.calc.GetDoeStudyExperimentsForParams(
                    params, "Linear", experiments_number=3
                )
                print("DOE Study experiments = ", designs5)


            if __name__ == "__main__":
                main()


    """
