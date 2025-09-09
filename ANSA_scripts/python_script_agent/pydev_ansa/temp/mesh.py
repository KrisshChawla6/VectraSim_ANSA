from __future__ import annotations
from typing import *


def AlignMeshToMesh(source_part: object, target_parts: object) -> object:
    """

    Geometrical function that aligns the entities contained into the source
    container with one of the target containers, based on geometry similarities.

    The alignment is performed by doing an 6 DOF motion on the source, in order to
    find a best match on one of the targets.

    As source_part or target_parts, any ANSA entity such as Part, Set or Property can be used.

    The user can abort the procedure by hitting the Break key,

    Parameters
    ----------
    source_part : object
            Any ANSA entity such as Part, Set or Property can be used.

    target_parts : object
            Any ANSA entity such as Part, Set or Property can be used.

    Returns
    -------
    object
            On success, the functions returns a Dictionary with the following members:
                    "matched_part"          -> the best matched part to our source.
                    "distance"              -> the distance of our source to the best matched part.
                    "transformation_matrix" -> the 4x3 transfomation matrix that aligns the source part to
                                               the best matched target.
            On failure, returns None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                trgt_props = []
                src_prop = base.GetEntity(constants.ABAQUS, "SHELL_SECTION", 1)
                trgt_props.append(base.GetEntity(constants.ABAQUS, "SHELL_SECTION", 1))
                trgt_props.append(base.GetEntity(constants.ABAQUS, "SHELL_SECTION", 2))

                results_dict = mesh.AlignMeshToMesh(src_prop, trgt_props)

                if results_dict == None:
                    print("Procedure aborted")
                    return
                else:
                    # best match on best_trg
                    print("distance = %s" % results_dict["distance"])
                elems = base.CollectEntities(constants.ABAQUS, src_prop, "SHELL", recursive=True)
                print("elems length: %d" % len(elems))
                base.TransformMatrix4x3(
                    "MOVE", 0, "SAME_PART", "NONE", results_dict["transformation_matrix"], elems
                )
                base.RedrawAll()


    """


def AspacingCFD(
    Growth_rate: float,
    Feature_angle: float,
    Min_length: float,
    Max_length: float,
    Sharp_angle_limit: float,
    Sharp_angle_length: float,
):
    """

    This function can be used to apply automatically curvature dependant Perimeter node spacing
    for CFD applications.

    Parameters
    ----------
    Growth_rate : float
            The growth rate of the mesh.

    Feature_angle : float
            The feature angle limit.

    Min_length : float
            The minimun length of the mesh.

    Max_length : float
            The maximum length of the mesh.

    Sharp_angle_limit : float
            The sharp angle limit.

    Sharp_angle_length : float
            The sharp angle length.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.AspacingCFD(1.2, 15.0, 5.0, 40.0, 15.0, 5.0)


    """


def AspacingSTL(
    chordal_deviation: Any, max_length: float, feature_angle: float, min_length: float
):
    """

    This function can be used to automatically apply curvature dependant Perimeter node spacing
    for STL meshing.

    Parameters
    ----------
    chordal_deviation : Any
            Chordal deviation. Absolute or relative value. It can be defined as a float value or
            a string, which can optionally contain the percentage symbol to indicate a relative value

    max_length : float
            Maximum length.

    feature_angle : float
            If 0 is specified then it is not active.

    min_length : float, optional
            Minimum length.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.AspacingSTL(0.1, 40.0, 0.0, 0.005)

                # or with relative chordal deviation
                mesh.AspacingSTL("15%", 20.0, 0.0, 0.05)


    """


def AutoMatch(
    visible: bool,
    shells: object,
    nodes: object,
    project_on_geometry: bool,
    project_2nd_order_nodes: bool,
    isolate: bool,
    move_to: str,
    preserve_id: str,
    distance: float,
    name: str,
) -> int:
    """

    Function that makes function Grids->Match->AUTO usable via script.

    Parameters
    ----------
    visible : bool, optional
            The function will run for every visible element of the model.

    shells : object, optional
            A list of shells.

    nodes : object, optional
            A list of nodes.

    project_on_geometry : bool, optional
            Nodes will also be projected upon geometry.

    project_2nd_order_nodes : bool, optional
            Choose whether to project upon geometry the Second order nodes or not.

    isolate : bool, optional
            Isolate the area where nodes that are going to be matched are found.

    move_to : str, optional
            Choose where the node that derives from the match procedure will be placed.
            Valid values: "average pos", "geometry pos", "FE pos".

    preserve_id : str, optional
            Choose which node id will be set on the node that derives from the match
            procedure. Valid values: "max" , "min".

    distance : float, optional
            The distance from the primary nodes that will be searched to find
            matching candidates.

    name : str, optional
            Match nodes with the given name only.

    Returns
    -------
    int
            Returns 1 upon success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                entities = base.GetEntity(constants.ABAQUS, "SET", 1)
                mesh.AutoMatch(
                    nodes=entities,
                    project_on_geometry=False,
                    project_2nd_order_nodes=False,
                    move_to="average pos",
                    distance=5,
                )


    """


def AutoPaste(
    visible: bool,
    shells: object,
    nodes: object,
    project_on_geometry: bool,
    project_2nd_order_nodes: bool,
    isolate: bool,
    move_to: str,
    preserve_id: str,
    distance: float,
    name: str,
    allow_element_collapse: bool,
) -> int:
    """

    Function that makes function Grids->Paste->AUTO usable via script.

    Parameters
    ----------
    visible : bool, optional
            The function will run on every visible element of the model.

    shells : object, optional
            A list of shells where the function will be run on.

    nodes : object, optional
            A list of nodes where the function will be run on.

    project_on_geometry : bool, optional
            If True, the nodes will also be projected on the geometry.

    project_2nd_order_nodes : bool, optional
            Choose whether to project upon geometry the Second order nodes or not.

    isolate : bool, optional
            Isolate the area where the nodes that are going to be pasted are found.

    move_to : str, optional
            Choose where the node that derives from the paste procedure will be placed.
            Valid values: "average pos", "geometry pos", "FE pos".

    preserve_id : str, optional
            Choose which node id will be set on the node that derives from the
            paste procedure. Valid values: "max" or "min"

    distance : float, optional
            The distance from the primary nodes to search in order to find the
            paste candidates.

    name : str, optional
            Paste nodes with the given name only.

    allow_element_collapse : bool, optional
            If True paste will be forced for grids that belong to the same element
            (this may result in element collapse)

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                mesh.AutoPaste(
                    visible=True,
                    project_on_geometry=True,
                    project_2nd_order_nodes=False,
                    move_to="geometry pos",
                    distance=3,
                )


            # ...or...


            def main():
                entities = base.GetEntity(constants.ABAQUS, "SET", 1)
                mesh.AutoPaste(
                    nodes=entities,
                    project_on_geometry=True,
                    project_2nd_order_nodes=False,
                    move_to="average pos",
                    distance=5,
                )


            # ...or...


            def main():
                mesh.AutoPaste(
                    visible=True,
                    project_on_geometry=True,
                    move_to="geometry pos",
                    distance=3,
                    allow_element_collapse=True,
                )


    """


def CheckShellTheta(
    shells: object, prototype_shell: object, do_fix: bool, tolerance: float
) -> object:
    """

    Function that checks the material orientation of given shells by Theta angle, using a prototype Shell.
    Although the algorithm uses the given shell as prototype, it tries to maintain a smooth regional orientation.

    Parameters
    ----------
    shells : object
            A list of shells to check material orientation.

    prototype_shell : object
            A shell prototype to check orientation by.

    do_fix : bool, optional
            If True, any shells found with different orientation will be oriented accordingly.
            (Default: False)

    tolerance : float, optional
            The angle tolerance to be used in orientation comparison.

    Returns
    -------
    object
            If no disoriented shells are found, the function returns None.
            If there are such shells, the function will return the list containing them.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                p_shell = base.GetEntity(constants.ABAQUS, "SHELL", 98)
                entities = base.CollectEntities(constants.ABAQUS, None, "SHELL", False)
                failed_shells = mesh.CheckShellTheta(entities, p_shell, do_fix=True, tolerance=15.0)


    """


def CollapseShells(COLLAPSE_TOLERANCE: float) -> int:
    """

    Collapses edges of visible elemens according to specified tolerance.

    Parameters
    ----------
    COLLAPSE_TOLERANCE : float
            The collapse tolerance.

    Returns
    -------
    int
            Returns 0 in each case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CollapseShells(0.05)


    """


def CompSkin() -> int:
    """

    Find the differences between the skin of visible tetras, pyramids and the skin of visible shells. Then remesh localy the solids to make the skins compatible.

    Returns
    -------
    int
            1: Success
            0: Failure

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CompSkin()


    """


def ConvertToPolyhedrals(
    solids: object,
    feature_angle: float,
    exclude_ANSA_layers: bool,
    ret_ents: bool,
    result_type: str,
    split_layers_at_sharp_convex_features: bool,
) -> object:
    """

    This function will convert solid elements into polyhedral and shell elements into polygons.
    Input solids and attached shells will be erased.

    Parameters
    ----------
    solids : object, optional
            A list of ansa entities (if not given all solids of the db will be converted).
            These entities may be ansa solids, parts, properties or volumes.

    feature_angle : float, optional
            Feature angle limit to be respected in conversion
            (if not given default value 20 is set).

    exclude_ANSA_layers : bool, optional
            Set True to ignore solids that belongs to ANSA layers volume from coversion.

    ret_ents : bool, optional
            If set to True a list with the created entities will be returned.

    result_type : str, optional
            Determines what the output of the conversion will be. It can be either "FE Solids", "Volumes" or "Light volume representation". Default option is "Volumes". If the conversion does not run on the whole db the result will be FE Solids.

    split_layers_at_sharp_convex_features : bool, optional
            When on the layers on convex features are split to improve quality

    Returns
    -------
    object
            Returns 0 on success and 1 on failure.
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                result = mesh.ConvertToPolyhedrals(feature_angle=10.0, exclude_ANSA_layers=True)


            def main():
                search_solids = ("SOLID",)
                all_solids = base.CollectEntities(0, None, search_solids, False)
                result = mesh.ConvertToPolyhedrals(
                    solids=all_solids, feature_angle=10.0, exclude_ANSA_layers=True
                )


            def main():
                psolid1 = base.GetEntity(ansa.constants.NASTRAN, "PSOLID", 2)
                all_solids = [psolid1]
                result = mesh.ConvertToPolyhedrals(
                    solids=all_solids, feature_angle=10.0, exclude_ANSA_layers=True
                )


    """


def ConvertHexaToMorph(entities: object) -> int:
    """

    Script function that converts hexa boxes to morphing boxes.

    Parameters
    ----------
    entities : object
            A list that contains hexa boxes.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def toHexaBox():
                hexas = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX")
                mesh.ConvertHexaToMorph(hexas)


    """


def ConvertHexaToSizeBox(
    entities: object, max_surface_length: float, max_volume_length: float
) -> int:
    """

    Script function that converts hexa boxes to size boxes.

    Parameters
    ----------
    entities : object
            A list that contains hexa boxes.

    max_surface_length : float, optional
            The maximum value for surface length.

    max_volume_length : float, optional
            The maximum value for volume length.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                box = base.GetEntity(constants.NASTRAN, "HEXA_BOX", 1)
                m = [box]
                mesh.ConvertHexaToSizeBox(m)


    """


def Convex(
    input_data: object,
    tolerance: float,
    offset_status: str,
    offset_mode: str,
    offset_value: float,
    module_id: str,
    property_id: int,
) -> object:
    """

    Creates a convex mesh for the user data.

    Parameters
    ----------
    input_data : object
            A list of convex input data. The object of input data can be
            points, curves, face, grids, elements, properties, materials, volumes, sets,
            includes, parts or groups.

    tolerance : float
            The value of tolerance for the convex function.

    offset_status : str
            The string that will allow to 'offset' the convex. This string takes two
            values "yes" or "no".

    offset_mode : str
            The string that defines the type of offset for the convex. That string takes
            two values "absolute" or "parametric".

    offset_value : float
            The value of offset.

    module_id : str
            The string for the 'module Id' of part/group. If the string is empty (""),
            the function create a default part to place the results of the convex.

    property_id : int
            The value of the 'property Id'. If the value is equal to zero or negative, the
            function creates one default property to place the results of the convex.

    Returns
    -------
    object
            Returns a list with the results of the convex.
            The list contains the elements of the convex. If the list is empty, the function is not
            able to create the convex of input data. If the data are coplanar, then a 2D convex will be created.
            Note, that the elements of 2D-convex are straight curves in sequence. In other case,
            the matrix will contain shell elements.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                s = (
                    "PSOLID",
                    "SHELL",
                    "SOLID",
                    "FACE",
                    "CURVE",
                    "SET",
                    "INCLUDE",
                    "ANSAGROUP",
                    "MAT1",
                    "POINT",
                    "SPOT",
                    "GRID",
                    "SpotweldPoint_Type",
                    "SpotweldLine_Type",
                    "AdhesiveLine_Type",
                    "AdhesiveFace_Type",
                    "SeamLine_Type",
                    "GumDrop_Type",
                    "Bolt_Type",
                    "Hemming_Type",
                )

                ent = base.CollectEntities(constants.NASTRAN, None, s, False)
                print(len(ent))

                res_convex = mesh.Convex(ent, 0.0001, "no", "absolute", 0.0, "1000", 0)
                print("length of matrix :", len(res_convex))


    """


def CreateOGridTopology(
    hexa_boxes: object,
    free_faces: object,
    offset: float,
    pattern_type: str,
    pattern_coef: float,
    branch_faces: object,
    fix_intersections: bool,
    offset_algorithm: str,
) -> int:
    """

    Script function that creates O-Grid topology for the input boxes.

    Parameters
    ----------
    hexa_boxes : object
            A list that contains boxes that will be affected when O-Grid is created.

    free_faces : object
            A list that contains the faces where no O-Grid will be generated from.

    offset : float
            The offset value of the created O-Grid topology.

    pattern_type : str
            A string that defines O-Grid topology's pattern. There are three
            types: (i) "Automatic", (ii) "Linear" and (iii) "Bell Shape".

    pattern_coef : float, optional
            A number that defines the factor of pattern  algorithm.
            It's a real number that takes values from 0 to 1.
            This parameter is used only for "Linear" and "Bell Shape" patterns.

    branch_faces : object, optional
            A list that contains branch faces of the structure. This parameter is
            used only for "Linear" and "Bell Shape" patterns.

    fix_intersections : bool, optional
            Activates a mechanism that fixes intersections.

    offset_algorithm : str, optional
            It takes the values "Absolute offset value", "Factor of local length"
            and "Parametric (0-1)".
            (Default: "Absolute offset value")

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    ModifyOGridTopology

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def createOGrid_Automatic():
                # gather O-Grid boxes
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 1))

                # gather free faces, where no O-Grid will be generated from
                free_faces = []
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 3))
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 5))

                # create O-Grid topology
                mesh.CreateOGridTopology(boxes, free_faces, 70.0, pattern_type="Automatic")


            def createOGrid_PipeBellShape():
                # gather boxes
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 22))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 23))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 24))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 27))

                # gather free faces, where no O-Grid will be generated from
                free_faces = []
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 127))
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 132))
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 141))

                # create O-Grid topology
                mesh.CreateOGridTopology(
                    boxes, free_faces, 3.0, pattern_type="Bell Shape", pattern_coef=0.7
                )


            def createOGrid_PipeLinear():
                # gather boxes
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 22))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 23))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 24))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 27))

                # gather free faces, where no O-Grid will be generated from
                free_faces = []
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 127))
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 132))
                free_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 141))

                # gather branch faces
                branch_faces = []
                branch_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 160))

                # create O-Grid topology
                mesh.CreateOGridTopology(
                    boxes, free_faces, 5.0, "Linear", pattern_coef=0.7, branch_faces=branch_faces
                )


            def createOGrid_PipeBellShapeLocalL():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 1))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 2))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 3))

                box_faces = []
                box_faces.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_FACE", 5))
                box_faces.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_FACE", 12))
                ansa.mesh.CreateOGridTopology(
                    hexa_boxes=boxes,
                    free_faces=box_faces,
                    offset=2,
                    pattern_type="Bell Shape",
                    pattern_coef=0.72,
                    fix_intersections=False,
                    offset_algorithm="Factor of local length",
                )


            def createOGrid_PipeBellShapeParametric():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 1))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 2))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 3))

                box_faces = []
                box_faces.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_FACE", 5))
                box_faces.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_FACE", 12))
                ansa.mesh.CreateOGridTopology(
                    hexa_boxes=boxes,
                    free_faces=box_faces,
                    offset=0.5,
                    pattern_type="Bell Shape",
                    pattern_coef=0.72,
                    fix_intersections=False,
                    offset_algorithm="Parametric (0-1)",
                )


    """


def CutShellsWithPlane(
    input: object,
    coordinates: object,
    target_edges_number: int,
    zones: object,
    number_of_shell_zones_affected: int,
    move_projection_to_nearest_perimeter: float,
    add_results_to_set: str,
    cut_faces_on_result_edges: bool,
    cut_faces_on_result_zones: bool,
    release_result_edges: bool,
    dont_reconstruct_mesh: bool,
    freeze_non_single_boundary: bool,
) -> int:
    """

    This function cuts shells with planes.

    Parameters
    ----------
    input : object
            Can be a single or an array of entities, parts, properties,
            materials, sets or macros. If the INPUT is 0,
            the visible shells are collected.

    coordinates : object
            A list containing 3 lists that descibe the three points that
            define the plane.

    target_edges_number : int, optional
            Greater than 0. Resulting edges number.

    zones : object, optional
            A list of zones offset.

    number_of_shell_zones_affected : int, optional
            Number of shell zones around cut to be affected.

    move_projection_to_nearest_perimeter : float, optional
            Minimum distance between projections and near perimeters.

    add_results_to_set : str, optional
            Add the results to the specified set.

    cut_faces_on_result_edges : bool, optional
            Create perimeters on resulting edges option.

    cut_faces_on_result_zones : bool, optional
            Create perimeters on resulting zones option.

    release_result_edges : bool, optional
            Release resulting edges option.

    dont_reconstruct_mesh : bool, optional
            Avoid reconstructing mesh option.

    freeze_non_single_boundary : bool, optional
            Determines whether an additional zone of elements will be added automatically so as to not have frozen edges in the initial selection.(Default=False)

    Returns
    -------
    int
            Returns 1 on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                coords_1 = (2910.760000, -515.150000, 229.853060)
                coords_2 = (2933.141800, -496.311770, 214.411620)
                coords_3 = (2948.8706, -480.3971, 211.92043)
                coords = (coords_1, coords_2, coords_3)
                zones = (2, 3)

                res = mesh.CutShellsWithPlane(
                    0,
                    coords,
                    add_results_to_set="my_set",
                    cut_faces_on_result_zones=True,
                    number_of_shell_zones_affected=3,
                    zones=zones,
                )
                print("Result: ", res)


    """


def DeleteOGridTopology(entities: object) -> int:
    """

    Script function to delete O-Grid topologies.

    Parameters
    ----------
    entities : object
            A list that contains O-Grid entities

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def deleteOGridTopology():
                ogrid_array = []
                ogrid_array.append(base.GetEntity(constants.NASTRAN, "O_GRID_TOPOLOGY", 1))
                mesh.DeleteOGridTopology(ogrid_array)


    """


def EdgesToPerimeter(SET: object) -> int:
    """

    Creates perimeters in given edges (via set).

    Parameters
    ----------
    SET : object
            The set with the edges.

    Returns
    -------
    int
            Returns -1 in case of no edges, 0 if everything is OK, 1 if an error occurs.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                ents = ("EDGE",)
                set = base.CreateEntity(constants.NASTRAN, "SET", {"Name": "new set"})
                result = base.PickEntities(constants.NASTRAN, ents)
                base.AddToSet(set, result)
                mesh.EdgesToPerimeter(set)


    """


def FEMToSurf(shells: object, delete: bool, ret_ents: bool) -> object:
    """

    This function creates Faces from each shell element of shells list.

    Parameters
    ----------
    shells : object
            A list with shell elements.

    delete : bool
            Delete shells or not.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    object
            Returns 1 on success, 0 on failure.
            If ret_ents=True it will return a list with the created entities, or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELLS")
                mesh.FEMToSurf(shells, True)


    """


def FEMToSurfArea(
    shells: object, ret_ents: bool, delete: bool, imprint: bool
) -> object:
    """

    This function creates one Face per group of shell elements. Those groups are formed by
    feature detection between the given shell elements.

    Parameters
    ----------
    shells : object
            A list of shell objects or a string with value 'visible'. If it is called
            with 'visible' it works for all the visible shell elements.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    delete : bool, optional
            If set to 'True', non-frozen shells that created macros will get deleted.

    imprint : bool, optional
            If set to 'False', shells will not get imprinted on macros.

    Returns
    -------
    object
            Returns 1 on success, 0 on failure.
            If ret_ents=True it will return a list with the created entities, or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                search_type = ("SHELL",)
                shells = base.CollectEntities(constants.NASTRAN, None, search_type)
                mesh.FEMToSurfArea(shells)


    """


def FemTopo(
    tolerance: object, shells_to_be_pasted: object, max_tolerance, steps
) -> int:
    """

    The function performs pasting of shells elements in FE models, for which the distance
    between the opposite boundary edges does not exceed the given one in the
    tolerance value. The list contains all shells which may have boundary edges
    that may or may not be pasted. If the tolerance passed as argument is equal to 0,
    the default nodes matching distance will be used instead. In case the list is
    empty or 0, FemTopo function will be applied to all visible shells. In this case a
    range of tolerances can be defined so that a series of pastings can be performed
    starting from a tolerance value of 'tolerance' up to the value set by 'max_tolerance'.
    The number of steps is declared in the 'steps' value. If max_tolerance and steps
    are set to 0, only one pasting will be performed based on the 'tolerance' value.

    Parameters
    ----------
    tolerance : object
            The tolerance value, which the distance between the opposite boundary edges
            should not exceed. If the tolerance is equal to 0, the default nodes matching
            distance will be used instead.

    shells_to_be_pasted : object
            A list that contains all shells which may have boundary edges.
            In case that the list is empty or 0, the FemTopo function will be applied to
            all the visible shells.

    max_tolerance :
            The maximum tolerance value.

    steps :
            The number of steps.

    Returns
    -------
    int
            Returns 1 on success, 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.FemTopo(5, shells, 0, 0)


    """


def FillGapFreeShells(
    SET1: object, SET2: object, RECONS: object, PART: object, PROP: object
) -> object:
    """

    Fill the gap between two sets of shells. The function, automatically, keeps the
    outer most perimeter of each set and tries to fill the gap between the two
    perimeters.

    Parameters
    ----------
    SET1 : object
            A list of entity objects (shell property, shell,set, include, ansapart or ansagroup)
            with SET objects defining the first set.

    SET2 : object
            A list of entity objects (shell property, shell,set, include, ansapart or ansagroup)
            with SET objects defining the second set.

    RECONS : object
            The reconstruction flag:
            -not equal to 0: reconstruction will take place.
            -equal to 0: no reconstruction.

    PART : object
            A part object or a part id (module_id).

    PROP : object
            A prop object or a prop id.
             If 0 a new property will be created.

    Returns
    -------
    object
            Returns a list with the results (shell elments).

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants


            def main():
                group_1 = (
                    base.GetPartFromModuleId("100"),
                    base.GetEntity(constants.NASTRAN, "PSHELL", 6),
                    base.GetPartFromModuleId("25R"),
                    base.GetEntity(constants.NASTRAN, "SET", 2),
                )

                part = base.NewPart("New_Part", "123")
                prop = base.CreateEntity(
                    constants.NASTRAN, "PSHELL", {"Name": "example", "__id__": 1000}
                )
                result = mesh.FillGapFreeShells(group_1, group_2, 0, part, prop)
                print("Total created shells of FillGapFreeShells: ", len(result))


    """


def FillHole(
    diameter: float,
    point_on_center: bool,
    convert_to_spot: bool,
    create_curve: bool,
    zones_num: int,
    part_or_property: str,
    with_stl: bool,
    force_fill_external_perimeter: bool,
) -> object:
    """

    This function fills holes on fe models or holes opened with the Open Hole function.

    Parameters
    ----------
    diameter : float
            The maximun diameter of the holes to be filled.

    point_on_center : bool
            Determines whether a 3d point will be created at the center of the hole.

    convert_to_spot : bool
            Can be used to convert the center 3d point to a connection point.

    create_curve : bool
            If set to True, a curve will be created on the hole's perimeter.

    zones_num : int
            Sets the number of shell zones around the hole to be reconstructed after the fill.

    part_or_property : str, optional
            Can be passed to set the part or property of the shells created.

    with_stl : bool, optional
            If set to True, stl type mesh will be created.

    force_fill_external_perimeter : bool, optional
            If set to True, external perimeter will be filled.

    Returns
    -------
    object
            Returns a list of the shells involved in the procedure, or None if fill hole failed.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                shells_property = base.GetEntity(constants.NASTRAN, "PSHELL", 2)
                shells_after_fill = mesh.FillHole(
                    20, point_on_center=True, convert_to_spot=False, create_curve=False, zones_num=1
                )
                print(len(shells_after_fill))


    """


def FixQualSolids(external_bounds_distance: Any) -> int:
    """

    This function moves solids nodes in order to fix mesh quality criteria problems, without altering mesh topology.
    The function works only on visible.

    Parameters
    ----------
    external_bounds_distance : Any, optional
            Defines the maximum distance from external bounds that a node is allowed to move.
            It can be defined as an integer, a float value, or an expression containing "local",
            which is the local length for every node. If not specified, the external bound distance
            will be set from Defaults ("maximum_distance_from_external_bounds").

    Returns
    -------
    int
            Returns 1 in case of valid expression for external bounds distance, otherwise 0.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.FixQualSolids("0.1*local+0.05")


    """


def GetGridsThickness(Grids: object) -> object:
    """

    A function that gets nodal thickness of given grids.

    Parameters
    ----------
    Grids : object
            A list of grid references.

    Returns
    -------
    object
            Returns a list that contains the thicknesses of the given grids. If a grid belongs to more than one shell and
            thus, has been assigned more than one nodal thickness the matrix contains the arithmetic mean of these thicknesses.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                grids = base.CollectEntities(constants.ABAQUS, None, "NODE")
                thickness = mesh.GetGridsThickness(grids)
                print("Number of thickness found = ", len(thickness))
                for i in range(len(thickness)):
                    print("thickness[" + i + "] is " + thickness[i])


    """


def GetMacroShells(macros: object) -> object:
    """

    This function gets all the shells of the given macros.

    Parameters
    ----------
    macros : object
            A list of Macro objects.

    Returns
    -------
    object
            Returns a list that contains all the shells that were found, or 0 if no shell was found.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                macros = base.GetFaceMacro(faces)
                shells = mesh.GetMacroShells(macros)
                print("all faces : " + len(faces))
                print("all macros: " + len(macros))
                print("all shells: " + len(shells))

                id = 10
                face = base.GetEntity(constants.NASTRAN, "FACE", id)
                macros = base.GetFaceMacro(face)
                if macros:
                    ret = base.GetEntityCardValues(constants.NASTRAN, macros[0], ("ID",))
                    shells = mesh.GetMacroShells(macros[0])
                    if shells:
                        print("The macro with id " + ret["id"] + " has " + len(shells) + " Shells")
                        for i in range(len(shells)):
                            ret = base.GetEntityCardValues(constants.NASTRAN, shells[i], ("EID",))
                            print(" Shell id: ", str(ret["EID"]))


    """


def GetMapVolumeBoundaries(volume: object) -> object:
    """

    This function collects the boundary of a given Map volume.

    Parameters
    ----------
    volume : object
            The volume whose boundary will be returned.

    Returns
    -------
    object
            Returns a dict with keys "master", "slave", "round". Each key has a list with entities as value.
            Returns None on error.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.GetMapVolumeBoundaries(vol)


    """


def GetReconstructAttachedSolidsValue(labels: object) -> object:
    """
    .. deprecated:: 19.0.0
            Use :py:func:`GetANSAdefaultsValues` instead.


    Gets parameter values concerning all shell mesh functions that run reconstruct
    when there are attached solids on the shells.

    Parameters
    ----------
    labels : object
            A List of string values. Accepting values are "attached solids" and "conflicting areas".

    Returns
    -------
    object
            Returns a dictionary with two items:
            -key: "attached_solids"      value: a value of {local remesh, affect only skin, freeze skin, always ask}
            -key: "conflicting_areas"    value: a value of {merge, keep larger, select, always ask}

    See Also
    --------
    SetReconstructAttachedSolidsValue

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                ret = mesh.GetReconstructAttachedSolidsValue(
                    ["attached_solids", "conflicting_areas"]
                )
                print(ret)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:func: GetANSAdefaultsValues instead.",
        DeprecationWarning,
    )


def GetShellMacro(shells: object) -> object:
    """

    This function gets the macros the given shells belong to.

    Parameters
    ----------
    shells : object
            A list of shell objects.

    Returns
    -------
    object
            Returns a list that contains all found macros or 0 if no macro could be found.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                id = 10
                shell = base.GetEntity(constants.NASTRAN, "SHELL", id)
                macros = mesh.GetShellMacro(shell)
                if len(macros) == 1:
                    ret = base.GetEntityCardValues(constants.NASTRAN, macros[0], ("ID",))
                    print(
                        "The Shell with id " + str(id) + " belongs to the macro with id ", ret["ID"]
                    )


    """


def GetSmoothAttachedSolidsValue(labels: object) -> object:
    """
    .. deprecated:: 19.0.0
            Use :py:func:`GetANSAdefaultsValues` instead.


    Gets parameter values concerning all shell mesh functions that run smooth
    when there are attached solids on the shells.

    Parameters
    ----------
    labels : object
            A List of string values. Accepting values are "attached solids" and "conflicting areas".

    Returns
    -------
    object
            Returns a dictionary with two items:
            -key: "attached_solids"      value: a value of {local remesh, affect only skin, freeze skin, always ask}
            -key: "conflicting_areas"    value: a value of {merge, keep larger, select, always ask}

    See Also
    --------
    SetSmoothAttachedSolidsValue

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                ret = mesh.GetSmoothAttachedSolidsValue(["attached_solids", "conflicting_areas"])
                print(ret)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:func: GetANSAdefaultsValues instead.",
        DeprecationWarning,
    )


def GetVolumeBoundary(volume: object) -> object:
    """

    This function collects the boundary of a given volume. The argument is the volume whose boundary elements
    will be returned.

    Parameters
    ----------
    volume : object
            A reference to a volume object, whose boundary elements will be returned.

    Returns
    -------
    object
            Returns a list with the boundary elements on success, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                ents = mesh.GetVolumeBoundary(volume)
                print("Number of elements in the boundary: ", len(ents))


    """


def GetVolumesMapParameters(volume: object) -> object:
    """

    This function returns the parameters of a given Map volume.

    Parameters
    ----------
    volume : object
            The volume whose parameters will be returned as an argument.

    Returns
    -------
    object
            Returns a list of the parameters ("Normal parts" or "Thin parts" method, number of steps)
            if the values are returned properly and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.LSDYNA, "VOLUME", 1)
                mesh.GetVolumesMapParameters(vol)


    """


def GetVolumesOffsetParameters(volume: object) -> object:
    """

    This function returns the parameters of a given Offset volume.

    Parameters
    ----------
    volume : object
            The volume object whose parameters will be returned.

    Returns
    -------
    object
            Returns a list of the offset parameters(dist, steps, middle, bias_type, bias_factor)
            if the values are returned properly and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.GetVolumesOffsetParameters(vol)


    """


def GetVolumesRotateParameters(volume: object) -> object:
    """

    This function returns the parameters of a given Rotate volume.

    Parameters
    ----------
    volume : object
            The volume object whose parameters will be returned.

    Returns
    -------
    object
            Returns a dict with keys "origin" (this is a list (x, y, z)), "vector" (this is a list (dx, dy, dz)),
            "angle", "steps", "biasing_type" and "biasing_factor".

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.LSDYNA, "VOLUME", 1)
                mesh.GetVolumesRotateParameters(vol)


    """


def GetVolumesTranslateParameters(volume: object) -> object:
    """

    This function returns the parameters of a given Rotate volume.

    Parameters
    ----------
    volume : object
            The volume object whose parameters will be returned.

    Returns
    -------
    object
            Returns a list with the following parameters parameters
            [dx", "dy", "dz", dist, steps] on success, or 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.LSDYNA, "VOLUME", 1)
                params = mesh.GetVolumesTranslateParameters(vol)


    """


def HexaBlockLength(
    edges: object, length: float, distribution: str, is_factor: bool
) -> int:
    """

    A function to define the element length on hexa box edges.

    Parameters
    ----------
    edges : object
            A list that contains hexa box edges.

    length : float
            The element length that we want to apply.

    distribution : str, optional
            A parameter used to define length on input opposite edges and
            takes the following values:
            i) "max": distribute nodes according to the edge
            with the maximum number of nodes (default value).
            ii) "min": distribute nodes according to the edge
            with the minimum number of nodes.
            iii) "average": distribute nodes according to the
            average number of nodes on opposite edges.

    is_factor : bool, optional
            If 'True', the final length is calculated by multiplying the input length by
            the existing element length. If 'False', the final length equals the input length.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def hexaBlockLength():
                # assign length on hexa box edge with id 14
                edges = base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 14)
                mesh.HexaBlockLength(edges, 2)


            def hexaBlockLength_OppositeEdges():
                # assign length on opposite hexa box edges with id 13, 14. Set distribution argument to
                # "min" in order to distribute nodes according to the edge with minimum number of nodes
                # (this edge has also the minimum curve length)
                edge1 = base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 13)
                edge2 = base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 14)

                edges = []
                edges.append(edge1)
                edges.append(edge2)
                mesh.HexaBlockLength(edges, 5, "min")


    """


def HexaBlockNumber(
    input: object,
    number: str,
    apply_multiple_number: bool,
    remesh_macros: bool,
    apply_number_of: str,
    ortho_spaced: bool,
) -> int:
    """

    This function defines a new number of edges (or nodes) on Hexa Box Edges.

    Parameters
    ----------
    input : object
            Input can be an entity or an array of entities, parts,
            hexa box faces, hexa box edges. If the input is 0, visible
            hexa box edges are collected.

    number : str
            A string which can either be a number (eg. "3"),
            or an expression to add or remove nodes (eg. "+2", "-3", "*2").

    apply_multiple_number : bool, optional
            If set to True, the function creates chains of connected
            box edges and distributes accordingly the given number
            to the chains. If deactivated (False) or missing, then all
            entities will get the same number.

    remesh_macros : bool, optional
            If set to True, the function remeshes affected hexa box faces
            after applying number. If missing (False) then the current gui
            value will be used.

    apply_number_of : str, optional
            It takes the values "edges" or "nodes", and it applies as
            INPUT as a number of edges or nodes. If missing then the
            current gui value will be used.

    ortho_spaced : bool, optional
            Defines if ortho-spaced numbering algorithm will
            be applied for input box edges. This option is valid
            only in the case that we don't apply the "multiple number" algorithm.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    NumberPerimeters

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def hexaBlockNumber():
                input = []
                input.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 2))
                input.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 10))
                ansa.mesh.HexaBlockNumber(
                    input=input,
                    number="+5",
                    apply_multiple_number=True,
                    remesh_macros=True,
                    apply_number_of="edges",
                )

                input = []
                input.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 16))
                ansa.mesh.HexaBlockNumber(
                    input=input,
                    number="8.",
                    remesh_macros=True,
                    apply_number_of="edges",
                    ortho_spaced=True,
                )


    """


def HexaBlockSpacing(
    edges: object,
    algorithm: str,
    factor: float,
    dmin: float,
    dmax: float,
    dmax_dmin_ratio: float,
    dlimit: float,
    steps: int,
    dir: str,
    factor_end: float,
    apply_to_opposite: bool,
    u_parameters: object,
    dstart: float,
    dend: float,
) -> int:
    """

    A function that distributes nodes according to a spacing algorithm.

    Parameters
    ----------
    edges : object
            A list that contains hexa box edges.

    algorithm : str
            A string that defines the spacing algorithm. There are
            five spacing algorithms: (i) "Linear", (ii) "Geometric", "Bell Curve",
            "User Defined" and "Bi-Geometric". Every spacing algorithm requires
            some specific arguments.

    factor : float, optional
            A number that defines the factor of the algorithm. For "Linear"
            and "Bell Curve" spacing it is any positive real number. For
            "Geometric" and "Bi-Geometruc" spacing, it should be greater than 1.

    dmin : float, optional
            A number that defines minimum nodal distance (>0).
            It is used only for "Geometric" spacing.

    dmax : float, optional
            A number that defines maximum nodal distance (>0).
            It is used only for "Geometric" spacing.

    dmax_dmin_ratio : float, optional
            A number that defines the ratio of maximum to minimum
            nodal distance. It is used only for "Geometric" spacing.

    dlimit : float, optional
            A number that defines the limiting nodal distance
            (when reached, the geometric series will keep it. It is
            used only for "Geometric" spacing.

    steps : int, optional
            The number of steps applied to the spacing algorithm

    dir : str, optional
            A flag that defines whether spacing will be applied
            from the start (dir="start") or end point (dir="end") of
            the hexa box edge. It is used for "Linear", "Geometric" and "Bi-Geometric"
            spacing algorithms. For "Linear" spacing, if "factor_end"
            is used, "dir" is ignored.

    factor_end : float, optional
            Defines the factor for the spacing that begins from
            the end point of box edge. If this factor is used, "Dir"
            keyword is ignored. It is only used for "Linear" spacing
            algorithm.

    apply_to_opposite : bool, optional
            Defines if spacing will be applied to all opposite
            box edges.

    u_parameters : object, optional
            List of parameters that define the position of nodes
            on box edges.

    dstart : float, optional
            A number that defines the length value (>0) at start of box edges.
            It is used only for "Bi-Geometric" spacing. If it is not defined, it is
            regarded equal to "dend".

    dend : float, optional
            A number that defines the length value (>0) at end of box edges.
            It is used only for "Bi-Geometric" spacing. If it is not defined, it is
            regarded equal to "dstart".

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            # 1. Linear algorithm
            def hexaBlockSpacing_Linear():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 1))
                mesh.HexaBlockSpacing(m, "Linear", factor=0.9, dir="start")


            # 2. Geometric algorithm
            def hexaBlockSpacing_Geometric():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 1))
                mesh.HexaBlockSpacing(m, "Geometric", dir="end", factor=1.2, dmin=20, steps=10)


            # 3. Bell Curve algorithm
            def hexaBlockSpacing_BellCurve():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 1))
                mesh.HexaBlockSpacing(m, "Bell Curve", factor=0.8)


            # 4. User Defined algorithm
            def main():
                m = []
                m.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 12))
                u_params = []
                u_params.append(0.1)
                u_params.append(0.2)
                u_params.append(0.5)
                u_params.append(0.7)
                ansa.mesh.HexaBlockSpacing(
                    edges=m,
                    algorithm="User Defined",
                    dir="end",
                    u_parameters=u_params,
                    apply_to_opposite=False,
                )


            # 5. Bi-Geometric algorithm
            def main():
                m = []
                m.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 5))
                ansa.mesh.HexaBlockSpacing(
                    edges=m,
                    algorithm="BI-GEOMETRIC",
                    factor=1.2,
                    dstart=0.1,
                    dend=0.2,
                    steps=15,
                    dir="end",
                    factor_end=2,
                    apply_to_opposite=False,
                )


    """


def HexaBlockVolSkin(volumes: object, ret_ents: bool) -> int:
    """

    Script function that generates volume skin for the specified hexa block volumes.

    Parameters
    ----------
    volumes : object
            A list that contains volumes (the volumes should be meshed).

    ret_ents : bool, optional
            If set to True a list with the created entities will be returned.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vols_array = []
                vols_array.append(base.GetEntity(constants.NASTRAN, "VOLUME", 1))
                mesh.HexaBlockVolSkin(vols_array)


    """


def HexaBlockVolumes(
    boxes: object,
    tolerance: float,
    project: bool,
    output_filename: str,
    ret_ents: bool,
    tolerance_expr: str,
    apply_surface_fit: bool,
    project_non_associated: bool,
) -> object:
    """

    A function that generates volume mesh for the specified hexa boxes.

    Parameters
    ----------
    boxes : object
            A list that contains the hexa boxes that we want
            to mesh (hexa boxes should not be meshed).

    tolerance : float, optional
            The tolerance to project on geometry.

    project : bool, optional
            A flag that defines whether to project (True) or
            not (False) on geometry.

    output_filename : str, optional
            An argument to define the full path where output of the
            generated mesh will be stored (output file contains
            information for Node Id, x, y, z, Box Id). If this argument
            is not filled, no output will be generated for these boxes.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    tolerance_expr : str, optional
            An expression to define the tolerance as a percentage of the minimum
            element length (Lmin). If expression is defined, "tolerance" is argument
            will be ignored.

    apply_surface_fit : bool, optional
            A flag that defines if surface-fit will be applied for
            fully associated box faces (box faces with points,
            edges and face association).

    project_non_associated : bool, optional
            A flag that defines if nodes of non-associated box
            faces will be projected on the geometry.

    Returns
    -------
    object
            Returns 1 on success, 0 on failure.
            If ret_ents=True it will return a list with the created entities, or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                # This script generates volume mesh for every hexa box of the database
                m = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX")
                ansa.mesh.HexaBlockVolumes(m, 0.1, True)

                ansa.mesh.HexaBlockVolumes(boxes=m, project=True, tolerance_expr="0.01*Lmin")

                boxes = []
                boxes.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1))
                ansa.mesh.HexaBlockVolumes(
                    boxes=boxes,
                    project=True,
                    tolerance_expr="0.05*Lmin",
                    apply_surface_fit=True,
                    project_non_associated=True,
                )


    """


def HexaBoxDelete(boxes: object) -> int:
    """

    Script function that deletes Hexa-Block boxes.

    Parameters
    ----------
    boxes : object
            An object or list that contains the Hexa-Block boxes to be deleted.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def deleteAllHexaBlocks():
                # Function that deletes every hexa box of the database.
                ents = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX")
                mesh.HexaBoxDelete(ents)


    """


def HexaBoxUndelete(entities: object) -> int:
    """

    Script function that "undeletes" previously deleted hexa boxes.

    Parameters
    ----------
    entities : object
            A list that contains the hexa boxes to get "undeleted".

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def undeleteBoxes():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 1))
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 2))
                mesh.HexaBoxUndelete(m)


    """


def HexaInterior(coordinate: object, maximum_length: float, volume: object) -> int:
    """

    The HexaInterior() function applies volume meshing to defined volumes, producing hexainterior.

    Parameters
    ----------
    coordinate : object
            The coordinate entity.

    maximum_length : float
            The maximum length.

    volume : object, optional
            The volume to be meshed.
            If it is not given, all volumes will be meshed.

    Returns
    -------
    int
            It returns 0 in case of success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            def main():
                coord = base.GetEntity(ansa.constants.NASTRAN, "CORD_NODES_C", 1)
                volume = base.GetEntity(ansa.constants.NASTRAN, "VOLUME", 1)
                mesh.HexaInterior(coord, 100.0, volume)


    """


def HexaInteriorbyID(volume: int, coord: int, Maxlength: float) -> int:
    """
    .. deprecated:: 18.0.0
            Use :py:func:`HexaInterior` instead.


    This function meshes a Volume in question with the algorithm HEXA-INTERIOR.

    Parameters
    ----------
    volume : int
            The Id of the volume to be meshed.

    coord : int
            The Id of the coordinate system that defines the orientation of the HEXA elements.
            If 0 is typed the orientation is defined according to the global coordinate system.

    Maxlength : float
            The maximum element length of the HEXA elements.

    Returns
    -------
    int
            It returns 0 in case of success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.HexaInteriorbyID(1, 0, 15)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 18.0.0. Use :py:func: HexaInterior instead.",
        DeprecationWarning,
    )


def InitPerimeters(
    cons: object,
    remesh_macros: bool,
    initialize_number: bool,
    initialize_spacing: bool,
    use_ansa_defaults_values: bool,
) -> int:
    """

    This function initializes the nodal spacing of perimeters.
    It works like the gui function PERIMETERs>INIT.
    The INPUT is a matrix that contains perimeters (CONS, FE perimeters).

    Parameters
    ----------
    cons : object
            A list of CONS objects.

    remesh_macros : bool, optional
            True or False. (Default: False)

    initialize_number : bool, optional
            True or False. (Default: False)

    initialize_spacing : bool, optional
            True or False. (Default: False)

    use_ansa_defaults_values : bool, optional
            If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                # This example initializes all CONS of the database:
                perimeters = base.CollectEntities(constants.NASTRAN, None, "CONS")
                perimeters.append(base.GetEntity(constants.NASTRAN, "FE PERIMETER", 3))
                ret = mesh.InitPerimeters(
                    perimeters,
                    remesh_macros=False,
                    initialize_number=True,
                    initialize_spacing=True,
                    use_ansa_defaults_values=False,
                )


    """


def IsVolumeMeshed(volume: object) -> int:
    """

    This function checks whether a volume is meshed or not.

    Parameters
    ----------
    volume : object
            A reference to the volume object.

    Returns
    -------
    int
            Returns 1 if the volume is meshed and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)

                if not mesh.IsVolumeMeshed(vol):
                    mesh.VolumesRemesh(vol)


    """


def IsolateBaffles(
    baffles_inside_volumes: bool,
    baffles_with_red_bounds: bool,
    baffles_between_two_volumes: bool,
) -> int:
    """

    This function isolates on the screen all the identified zero-thickness walls.

    Parameters
    ----------
    baffles_inside_volumes : bool, optional
            If set to True, then the function will leave visible only the baffles
            identified inside closed volumes, otherwise also elements or geometry
            that does not belong to a closed volume will remain visible.
            (Default: False)

    baffles_with_red_bounds : bool, optional
            If set to true then the baffles that do not have any red bounds are
            ignored and are not isolated.
            (Default: False)

    baffles_between_two_volumes : bool, optional
            If set to True the result will recognize as baffles faces or shells that lie on two closed volumes

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.IsolateBaffles()


    """


def IsolateFeatureShells(PARAMS: str, EXPAND_LEVEL: int) -> object:
    """

    Collect visible shells that are recognized as features that are giong to be treated, according to user defined parameters.

    Parameters
    ----------
    PARAMS : str
            Contains keywords that correspond to features to collect.
            Accepted keywords are "FILLETS", "FLANGES", "HOLES" and "VIOL".
            Fillets, flanges and holes recognition is based on PARAM fillets,
            flanges and holes treatment parameters correspondingly.
            Violating shells recognition is based on Quality Criteria.

    EXPAND_LEVEL : int
            The number of the expanding shells zones added around recognized shells.

    Returns
    -------
    object
            Returns a list that contains all the shells recognized as features.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                params = ("Fillets", "Viol")
                shells = mesh.IsolateFeatureShells(params, 0)
                num = len(shells)
                print("Recognized features shells: ", num)


    """


def JoinMacros(
    entities: object,
    keep_mesh: bool,
    auto_delete_hot_points: bool,
    use_ansa_defaults_values: bool,
) -> int:
    """

    This function joins the macros that belong to the given perimeters (Cons, FE).

    Parameters
    ----------
    entities : object
            A list that contains perimeters (Cons, FE).

    keep_mesh : bool, optional
            If the existing mesh should be kept or erased after the joining.

    auto_delete_hot_points : bool, optional
            If the hot points should be deleted after the joining or not.

    use_ansa_defaults_values : bool, optional
            If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

    Returns
    -------
    int
            Returns the number of all succeeded joinings or 0 if no joining could be performed.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                all_cons = base.CollectEntities(constants.NASTRAN, None, "CONS")
                perimeters_for_join = []
                for cons in all_cons:
                    perimeters_for_join.append(cons)
                perimeters_for_join.append(base.GetEntity(constants.NASTRAN, "FE PERIMETER", 3))
                num_of_joinings = mesh.JoinMacros(perimeters_for_join, False, True)
                print("All finally joined CONS = ", str(num_of_joinings))
                base.RedrawAll()


    """


def ApplyNewLengthToMacros(
    element_length: str, perimeters: object, use_ansa_defaults_values: bool
) -> int:
    """

    This function applies a specified element length to Perimeter Segments of Macros and FE perimeters.

    Parameters
    ----------
    element_length : str
            The element length that will be applied.

    perimeters : object, optional
            A list that contains perimeters (Cons, FE). If it is set to 0, visible perimeters will be used.

    use_ansa_defaults_values : bool, optional
            If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                # This example applies length to all perimeters of all macros:
                mesh.ApplyNewLengthToMacros("5")

                # This example applies length to specific perimeters
                perimeters_list = []
                perimeters_list.append(base.GetEntity(constants.NASTRAN, "CONS", 6))
                perimeters_list.append(base.GetEntity(constants.NASTRAN, "CONS", 11))
                perimeters_list.append(base.GetEntity(constants.NASTRAN, "FE PERIMETER", 3))
                mesh.ApplyNewLengthToMacros("*0.5", perimeters_list, use_ansa_defaults_values=True)


    """


def EraseMesh() -> int:
    """

    This function deletes the shell mesh of visible Macro Areas.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.EraseMesh()


    """


def Remesh() -> int:
    """

    This function meshes using the last used algorithm.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.Remesh()


    """


def FixQuality() -> int:
    """

    This function moves nodes in order to fix mesh quality criteria problems, without altering mesh topology.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.FixQuality()


    """


def Reconstruct() -> int:
    """

    This function is applied on an existing mesh and performs remeshing to optimize the overall quality and flow of the mesh, correct quality criteria violations and enforce special mesh treatments. The function can be applied on Macro Area mesh or FE-Model mesh. The function works only on visible macros like the GUI function Reconstruct[Visible].

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.Reconstruct()


    """


def Reshape() -> int:
    """

    This function is the most advanced quality improvement function. It can be applied on meshed Macro Areas in order to optimize the mesh quality in various aspects. Apart from leading to a high quality mesh, one of its main advantages is the fact that it eliminates to a minimum the need to manually cut, join and align Macro Areas.
    The function works only on visible entities (Macros or released FE shell elements).

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.Reshape()


    """


def Smooth() -> int:
    """

    This function is useful in order to smooth the mesh after a manual node pasting or element splitting or joining.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.Smooth()


    """


def ModifyOGridTopology(
    ogrid: object,
    offset: float,
    pattern_type: str,
    pattern_coef: float,
    fix_intersections: bool,
    offset_algorithm: str,
) -> int:
    """

    Script function that modifies the input O-Grid topology.

    Parameters
    ----------
    ogrid : object
            The O-Grid topology that will be modified.

    offset : float, optional
            The value defining the offset value of the O-Grid topology.
            It's a real number different than zero.

    pattern_type : str, optional
            Defines the O-Grid pattern type. There are three types:
            (i) "Automatic"
            (ii) "Linear"
            (iii) "Bell Shape"

    pattern_coef : float, optional
            The value defining the factor of pattern algorithm.
            It's a real number that accepts values from 0 to 1.

    fix_intersections : bool, optional
            Activates the mechanism that fixes the intersections.

    offset_algorithm : str, optional
            It accepts the values "Absolute offset value", "Factor of local length"
            and "Parametric (0-1)".

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    CreateOGridTopology

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def modifyOGridTopology():
                ent = base.GetEntity(constants.NASTRAN, "O_GRID_TOPOLOGY", 1)
                mesh.ModifyOGridTopology(ent, offset=2.23, pattern_type="Linear")


            def modifyOGrid_LinearParametric():
                ent = base.GetEntity(ansa.constants.NASTRAN, "O_GRID_TOPOLOGY", 1)
                ansa.mesh.ModifyOGridTopology(
                    ogrid=ent,
                    offset=0.5,
                    pattern_type="Linear",
                    pattern_coef=0.72,
                    fix_intersections=False,
                    offset_algorithm="Parametric (0-1)",
                )


            def modifyOGrid_BellShapeLocalL():
                ent = base.GetEntity(ansa.constants.NASTRAN, "O_GRID_TOPOLOGY", 1)
                ansa.mesh.ModifyOGridTopology(
                    ogrid=ent,
                    offset=3,
                    pattern_type="Bell Shape",
                    pattern_coef=0.72,
                    fix_intersections=False,
                    offset_algorithm="Factor of local length",
                )


            def modifyOGrid_LinearAbsoluteValue():
                ent = base.GetEntity(ansa.constants.NASTRAN, "O_GRID_TOPOLOGY", 1)
                ansa.mesh.ModifyOGridTopology(
                    ogrid=ent,
                    offset=4,
                    pattern_type="Linear",
                    pattern_coef=0.72,
                    fix_intersections=False,
                    offset_algorithm="Absolute offset value",
                )


    """


def MoveGridsToOrigin(entities: object) -> int:
    """

    Moves all incoming grids to their origin position.

    Parameters
    ----------
    entities : object
            A list of grids.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants


            def main():
                # 1. for all grids use:
                grids = base.CollectEntities(constants.NASTRAN, container, "GRID")
                mesh.MoveGridsToOrigin(grids)

                # 2. for all visible grids use:
                matrix1 = []
                map1 = base.NodesOfVisibleElements()
                for node in map1.keys():
                    matrix1.append(node)
                mesh.MoveGridsToOrigin(matrix1)

                # 3. for all selected grids use:
                ents = ("FACE",)
                grids = base.PickNodes(constants.NASTRAN, ents)
                mesh.MoveGridsToOrigin(grids)

                # 4. for a specific grid (with entity) use:
                id = 10
                grid = base.GetEntity(constants.NASTRAN, "GRID", id)
                mesh.MoveGridsToOrigin(grid)


    """


def OpenHole(
    coordinates: object,
    tolerance: float,
    number_of_zones: int,
    nodes_around_hole: int,
    hole_diameter: float,
    zone1_length: object,
    zone2_length: object,
    entities: object,
) -> object:
    """

    This function opens holes or creates spots on the whole or on certain parts of the base.
    The user can provide the function with one or more 3D points by giving their coordinates.

    Parameters
    ----------
    coordinates : object
            A list with (x, y, z) coordinates tuples.

    tolerance : float
            The tolerance value.

    number_of_zones : int
            The number of affected shell zones  during reconstruct. Limiting the number of affected zones may affect the mesh quality.

    nodes_around_hole : int
            The target number of nodes on the hole's perimeter. A value <4 is not accepted. Negative number
            means that  the value is calculated using the 'auto' calculation of Holes 2D treatment. Zero means that a spot will be created.

    hole_diameter : float
            The diameter of the hole.

    zone1_length : object
            The zone's 1 length. If a negative number is inserted no zone will be created.
            A list with floats.

    zone2_length : object
            The zone's 2 length. If a negative number is inserted no zone will be created.
            A list with floats.

    entities : object, optional
            determines where the function will search for a shell to make the
            projection. If entities[0] is a reference to a part and entities[1]
            is a reference to a material the search will be performed on the
            specified part and material. Supported references are references to
            parts, groups, properties, materials and sets. If zero is entered the search
            is performed on the whole base.

    Returns
    -------
    object
            Returns a list, where the first three elements are lists containing references to the
            nodes on the first hole's perimeter and on the first and second zone respectively.
            If an element does not exist (ex. no zone created), then zero is placed on this element.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                part = base.GetPartFromModuleId("9")
                property = base.GetEntity(constants.NASTRAN, "PSHELL", 20)
                material = base.GetEntity(constants.NASTRAN, "MAT1", 16)
                args = (
                    part,
                    property,
                    material,
                    base.GetEntity(constants.NASTRAN, "SET", 1),
                    base.GetEntity(constants.NASTRAN, "SET", 2),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                )

                coords = ((1902, -825, 485), (2018, -806, 566))
                tolerance = (0.2, 0.3)
                number_of_zones = (1, 2)
                nodes_in_hole = (0, 10)
                hole_diameter = (0, 20)
                zone1_length = (5, 10)
                zone2_length = (5, 5)

                results = mesh.OpenHole(
                    coords,
                    tolerance,
                    number_of_zones,
                    nodes_in_hole,
                    hole_diameter,
                    zone1_length,
                    zone2_length,
                    args,
                )
                for ent in results:
                    print(len(ent))


    """


def OrientVolumebyID(volume: int) -> int:
    """
    .. deprecated:: 18.0.0
            Use :py:func:`OrientVolume` instead.


    This function orients all the elements of the volume so that they all point inwards (gray side).

    Parameters
    ----------
    volume : int
            The Id of the volume that is going to be oriented.

    Returns
    -------
    int
            Returns 1 on success and 0 otherwise

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.OrientVolumebyID(1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 18.0.0. Use :py:func: OrientVolume instead.",
        DeprecationWarning,
    )


def ProjectNodesArrayOnShells(
    input: object,
    nodes_array: object,
    projection_tolerance: float,
    maximum_projections_number: int,
    user_projection_mode_vector: object,
    zones: object,
    number_of_shell_zones_affected: float,
    move_projection_to_nearest_perimeter: float,
    move_to_projected_perims: float,
    paste_projected_and_result_edges: bool,
    add_results_to_set: str,
    cut_faces_on_result_edges: bool,
    cut_faces_on_result_zones: bool,
    release_result_edges: bool,
    apply_fill_gap_on_results: bool,
    open_closed_perimeter_hole: bool,
    freeze_non_single_boundary: bool,
    is_extend: bool,
) -> int:
    """

    This function projects a polyline defined by nodes on shells.

    Parameters
    ----------
    input : object
            Can be an object, a list of objects, parts, properties,
            materials, sets or macros.
            If input is 0, the visible shells are collected.

    nodes_array : object
            A list containing node objects that define the polyline. In case of more that one polylines the list should contain lists of node objects defining each polyline. Closed polylines should contain the same first and last node

    projection_tolerance : float, optional
            Maximum distance between the projection and the
            projected entity.

    maximum_projections_number : int, optional
            Maximum number of projections.

    user_projection_mode_vector : object, optional
            A list of the vector components for the user defined
            project vector.

    zones : object, optional
            A list of zones offset. Create zones at projection. Each offset
            value must be greater than 0.

    number_of_shell_zones_affected : float, optional
            Number of shell zones around projection to be affected.

    move_projection_to_nearest_perimeter : float, optional
            Minimum distance between projections and near perimeters.

    move_to_projected_perims : float, optional
            Between 0. and 1. Parameter to move the result edges towards
            the projected perimeters.

    paste_projected_and_result_edges : bool, optional
            Paste projected and result edges.

    add_results_to_set : str, optional
            The name of the existing set. If the set doesn't exist,
            a default set will be created.

    cut_faces_on_result_edges : bool, optional
            Create perimeters on resulting edges option.

    cut_faces_on_result_zones : bool, optional
            Create perimeters on resulting zones option.

    release_result_edges : bool, optional
            Release resulting edges option.

    apply_fill_gap_on_results : bool, optional
            Applies fill gap between source and projected edges.

    open_closed_perimeter_hole : bool, optional
            Creates an opening if the projected edges form a closed perimeter.

    freeze_non_single_boundary : bool, optional
            Determines whether an additional zone of elements will be
            added automatically so as to not have frozen edges in the
            initial selection.

    is_extend : bool, optional
            If True projection vector will be in the extend direction. Works only If user_projection_mode_vector is empty.

    Returns
    -------
    int
            This function always returns 1

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                props = []
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 44))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 45))

                grids_array = []
                grids_array.append(base.GetEntity(constants.NASTRAN, "GRID", 15079))
                grids_array.append(base.GetEntity(constants.NASTRAN, "GRID", 15070))
                grids_array.append(base.GetEntity(constants.NASTRAN, "GRID", 15040))
                grids_array.append(base.GetEntity(constants.NASTRAN, "GRID", 14866))

                zones_array = (1,)

                res = mesh.ProjectNodesArrayOnShells(
                    props,
                    grids_array,
                    zones=zones_array,
                    cut_faces_on_result_edges=True,
                    maximum_projections_number=3,
                )
                print("result: ", res)


    """


def ProjectOpenHole(
    holes: object,
    add_to_set: str,
    cut_faces_on_holes_edges: bool,
    cut_faces_on_zones_edges: bool,
) -> object:
    """

    ProjectOpenHole opens holes or creates spots on parts specified for each point.

    Parameters
    ----------
    holes : object
            A list containing lists with objects that define the hole. A list for
            every hole is needed
            -coordinates: Is an array with three float numbers one for each
            corresponding coordinate of the point we need to project in order to
            create a hole on each part.
            -parts: Is an array that holds every part we need to create a hole upon.
            -parameters: Is an array that holds all the necessery parameters for
            the hole creation, these are:
            int zone_num,
            float proj_tolerance,
            int target_node_num,
            float diameter,
            float zone1_len,
            float zone2_len,
            bool quads_around_proj_point,
            bool square_holes,
            bool create_perfect_zone.

            The specified point will be projected to every part determined in
            parts with distance less than proj_tolerance.
            -proj_tolerance should be greater or equal to zero.
             A hole will be opened or a spot will be created on every projection.
            -zone_num is the number of shell zones that will be affected around
             the hole respectively. Valid values are greater than zero.
            -target_node_num is the target number of nodes on the hole's perimeter.
             Zero value means that a spot will be created instead of a hole.
             Less that zero values will assign a rundom number.
            -diameter is the diameter of the hole. Valid values are greater thar zero.
            -zone1_len and zone2_len are the desired zones' length.
             Zero value for a zone length means that the corresponding zone will not
             be created. Negative values are not valid.
            -quads_around_proj_point indicates that 4 quads will be created
             around spots, for values different than zero.
            -square_holes indicates that a square hole will be created (affects only
             holes with 8 nodes around hole), for values different than zero.
            -create_perfect_zone indicates that perfect zones will be created
             for values different than zero.

    add_to_set : str, optional
            The set's name to which new holes will be set to.
            If the set doesn't exist, a default set will be created.

    cut_faces_on_holes_edges : bool, optional
            Controls whether the faces will be cut on opened hole edges.

    cut_faces_on_zones_edges : bool, optional
            Controls whether faces will be cut on opened hole zone edges.

    Returns
    -------
    object
            Returns an array containing integers.
            For every hole of array holes and every part of array parts of each hole, the returned array contains a value.
            If the hole is created on the corresponding part, value 1 is placed in the array, otherwise 0.
            The order of the values is defined by the order of the holes and each parts.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                prop1 = base.GetEntity(constants.NASTRAN, "PSHELL", 10004)
                prop2 = base.GetEntity(constants.NASTRAN, "PSHELL", 10005)
                props = (prop1, prop2)

                coords = (476.75, 107.54, 108.13)
                points = coords

                params = (2, 20.0, 8, 4.0, 2.0, 1.0, False, False, False)

                hole = (points, props, params)

                results = mesh.ProjectOpenHole((hole,))


    """


def ProjectPerimeterOnShells(
    input: object,
    perimeters: object,
    projection_tolerance: float,
    maximum_projections_number: float,
    user_projection_mode_vector: object,
    target_edges_number: float,
    zones: object,
    number_of_shell_zones_affected: float,
    move_projection_to_nearest_perimeter: float,
    move_to_projected_perims: float,
    add_results_to_set: str,
    cut_faces_on_result_edges: bool,
    cut_faces_on_result_zones: bool,
    release_result_edges: bool,
    freeze_non_single_boundary: bool,
    apply_fill_gap_on_results: bool,
    open_closed_perimeter_hole: bool,
    is_extend: bool,
) -> int:
    """

    This function projects perimeters (curves, cons, edges, morph edges) on shells.

    Parameters
    ----------
    input : object
            Can be an object or an array of objects, parts, properties,
            materials, sets or macros.
            If the INPUT is 0, the visible shells are collected.

    perimeters : object
            It can be an object or a list of curves, cons, edges or morph edges.

    projection_tolerance : float, optional
            Maximum distance between the projection and the projected
            entity.

    maximum_projections_number : float, optional
            Maximum number of projections.

    user_projection_mode_vector : object, optional
            A list of vector components to define the user project vector.

    target_edges_number : float, optional
            Resulting edges number.

    zones : object, optional
            A list of zones offset. Create zones at projection. Each offset
            value must be greater than 0.

    number_of_shell_zones_affected : float, optional
            Number of shell zones around projection to be affected.

    move_projection_to_nearest_perimeter : float, optional
            Minimum distance between projections and near perimeters.

    move_to_projected_perims : float, optional
            Between 0. and 1. Parameter to move the result edges towards
            the projected perimeters.

    add_results_to_set : str, optional
            Name of existing set. If the set doesn't exist, a default set
            will be created.

    cut_faces_on_result_edges : bool, optional
            Create perimeters on resulting edges option.

    cut_faces_on_result_zones : bool, optional
            Create perimeters on resulting zones option.

    release_result_edges : bool, optional
            Release resulting edges option.

    freeze_non_single_boundary : bool, optional
            Determines whether an additional zone of elements will be
            added automatically so as to not have frozen edges in the
            initial selection.

    apply_fill_gap_on_results : bool, optional
            Determines whether apply gap will be applied between the
            projected and the resulting edges.

    open_closed_perimeter_hole : bool, optional
            Determines whether a hole will be opened when a closed
            perimeter is projected.

    is_extend : bool, optional
            If True projection vector will be in the extend direction. Works only If user_projection_mode_vector is empty.

    Returns
    -------
    int
            This function always returns 1

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                part = base.GetEntity(constants.NASTRAN, "PSHELL", 46)
                curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                zones = [0.75]

                res = mesh.ProjectPerimeterOnShells(
                    part,
                    curves,
                    projection_tolerance=10.0,
                    maximum_projections_number=2,
                    zones=zones,
                    number_of_shell_zones_affected=3,
                    cut_faces_on_result_edges=True,
                )
                print("result: ", res)


    """


def ReadMeshParams(FILENAME: str) -> int:
    """

    This function reads mesh parameters.

    Parameters
    ----------
    FILENAME : str
            The path to the filename containing the parameters.

    Returns
    -------
    int
            Returns 0 if file does not exist, or 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                status = mesh.ReadMeshParams("/ansa/params.ansa_mpar")


    """


def ReadQualityCriteria(FILENAME) -> int:
    """

    This function reads quality criteria.The argument is the path to the filename containing the criteria.

    Parameters
    ----------
    FILENAME :
            The path to the filename.

    Returns
    -------
    int
            Returns 0 if file does not exist, or 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                status = mesh.ReadQualityCriteria("/home/user/my_criteria.ansa_qual")


    """


def ReconstructShells(SHELLS: object) -> int:
    """

    The function perfrorms Reconstruct on shells given by the user.

    Parameters
    ----------
    SHELLS : object
            A list with the shells to be reconstructed.

    Returns
    -------
    int
            Returns 1 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.ReconstructShells(shells)


    """


def ReconstructTetra() -> int:
    """

    This function applies the IMPROVE>Reconstruct function on the visible Tetras.

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReconstructTetra()


    """


def ReconstructViolatingTetra(N: int) -> int:
    """

    This function reconstructs the violating TETRAs and N neighboring zones.

    Parameters
    ----------
    N : int
            The number of neighboring zones.

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReconstructViolatingTetra(3)


    """


def RefineElements(
    ELEMENTS_TO_BE_REFINED: object,
    EXTERNAL_TRANSITION_ZONE: int,
    MAX_REFINEMENT_STEPS: int,
    MIN_EDGE_LENGTH: float,
    NUMBER_OF_TRANSITION_ZONES: int,
    ALLOW_TRIAS_AT_REFINED_AREA: int,
    REFINEMENT_MESH_TYPE: int,
    SMOOTH_EXTERNAL_TRANS_ZONE: int,
    FREEZE_FREE_EDGES: int,
) -> int:
    """

    The function refines elements.

    Parameters
    ----------
    ELEMENTS_TO_BE_REFINED : object
            A list of shell entities.

    EXTERNAL_TRANSITION_ZONE : int
            An option that forbids the refining of the external element zone
            of the elements contained in the list.
            Set 1 to enable or 0 to disable.

    MAX_REFINEMENT_STEPS : int
            The number of the maximum possible refinement steps that are going to be applied.

    MIN_EDGE_LENGTH : float
            The minimum edge length of the refined elements.

    NUMBER_OF_TRANSITION_ZONES : int
            The number of not refined elements zones
            that lie between two successive refinement step areas.

    ALLOW_TRIAS_AT_REFINED_AREA : int
            An option that allows the existence of trias at the refined area.
            Set 1 to enable or 0 to disable.

    REFINEMENT_MESH_TYPE : int
            The type of mesh created during refinement.
            It can be defined as "MIXED", "QUAD", "RADIAL_QUAD",
            "SMOOTHED_QUAD", "MIXED 1 TO 3" and "QUAD 1 TO 3".
            However, some trias may be created at "QUAD" REFINEMENT_MESH_TYPE.

    SMOOTH_EXTERNAL_TRANS_ZONE : int
            An option that allows the smoothing of the external element zone, if this exists.
            Set 1 to enable or 0 to disable.

    FREEZE_FREE_EDGES : int
            An option that does not allow splitting single free boundaries.
            Set 1 to enable or 0 to disable.

    Returns
    -------
    int
            Returns 1 in case the list ELEMENTS_TO_BE_REFINE is valid and 0 in case it is invalid.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.RefineElements(shells, 0, 2, 0.0, 1, 0, "mixed", 0, 0)


    """


def RefineTrias(
    shells: object, number_of_transition_zones: int, preview_result: bool
) -> int:
    """

    Refines the triangles contained in a list of shells.

    Parameters
    ----------
    shells : object
            A list of shell entities.

    number_of_transition_zones : int, optional
            Expand levels of transition area to reconstruct.
            Valid values are greater than 0.
            (Default: 0)

    preview_result : bool, optional
            Preview the refinement result. Acceptable value are 'True', 'False'.
            (Default: True)

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = []
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 10809))
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 10810))
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 10814))
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 11137))
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 11138))
                shells.append(base.GetEntity(constants.NASTRAN, "SHELL", 11139))
                mesh.RefineTrias(shells, number_of_transition_zones=1)


    """


def ReleaseElements(FACES_VOLUMES_FOR_RELEASE: object) -> int:
    """

    This function detaches the shell mesh from Macros or solid mesh from Volumes and creates independent FE-Model mesh.

    Parameters
    ----------
    FACES_VOLUMES_FOR_RELEASE : object
            A list that contains faces or volumes for release.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                faces_array = base.CollectEntities(constants.NASTRAN, None, "FACE", False)

                relface_array = []
                for face in faces_array:
                    ret = base.GetEntityCardValues(constants.NASTRAN, face, ("ID",))
                    if ret["ID"] == 21:
                        relface_array.append(face)
                volumes_array = base.CollectEntities(constants.NASTRAN, None, "VOLUME", False)
                for volume in volumes_array:
                    base.GetEntityCardValues(constants.NASTRAN, volume, "ID", id)
                    if id == 3:
                        relface_array.append(volume)
                mesh.ReleaseElements(relface_array)


    """


def ReleaseMacros(
    macros: object,
    remesh_macros: bool,
    keep_mesh: bool,
    delete_hot_points: bool,
    use_ansa_defaults_values: bool,
) -> int:
    """

    This function releases joined macro area boundaries.

    Parameters
    ----------
    macros : object
            A list that can contains perimeters (CONS) or macros (FACE).

    remesh_macros : bool, optional
            Remesh the macros around the affected area.

    keep_mesh : bool, optional
            Keep the existing mesh.

    delete_hot_points : bool, optional
            Automatically delete the hot points after the release.

    use_ansa_defaults_values : bool, optional
            If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                # This example releases all CONS of the database:
                all_cons = base.CollectEntities(constants.NASTRAN, None, "CONS")
                answer = mesh.ReleaseMacros(
                    all_cons,
                    remesh_macros=False,
                    keep_mesh=False,
                    delete_hot_points=False,
                    use_ansa_defaults_values=True,
                )
                print(" All CONS for release = " + str(len(all_cons)) + " answer: " + str(answer))

                # This example releases all FACES of the database:
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                answer = mesh.ReleaseMacros(
                    all_faces,
                    remesh_macros=False,
                    keep_mesh=False,
                    delete_hot_points=False,
                    use_ansa_defaults_values=False,
                )
                print("All FACES for release = " + str(len(all_faces)) + " answer: " + str(answer))


    """


def SaveMeshParams(FILENAME: str) -> int:
    """

    This function saves mesh parameters.

    Parameters
    ----------
    FILENAME : str
            The path of the filename where the parameters will be saved.

    Returns
    -------
    int
            Returns 1 in case of successful saving of the meshing parameters
            and 0 if the meshing parameters are not saved.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                status = mesh.SaveMeshParams("/ansa/params.ansa_mpar")


    """


def SaveQualityCriteria(FILENAME: str) -> int:
    """

    This function saves quality criteria.

    Parameters
    ----------
    FILENAME : str
            The path to the filename where the parameters will be saved.

    Returns
    -------
    int
            Returns 1 in case of successful saving of the quality criteria
            and 0 if the quality criteria are not saved.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                status = mesh.SaveQualityCriteria("/ansa/qual.ansa_qual")


    """


def SealGaps(
    min_distance: float,
    max_distance: float,
    width: int,
    feat_line_angle: float,
    ret_ents: bool,
    ignore_gaps_in_the_same_pid: bool,
) -> object:
    """

    Script version of function MESH>SHELL_MESH>GILL_GAP>Seal.
    Works on visible.

    Parameters
    ----------
    min_distance : float
            Gaps with distance < min_distance will not be sealed.

    max_distance : float
            Gaps with distance > max_distance will not be sealed,
            must be min_distance < max_distance.

    width : int
            Expressed as a percentage, must be in [0,100].

    feat_line_angle : float
            The feature line angle in degrees, must be in [0,180].

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    ignore_gaps_in_the_same_pid : bool, optional
            If set to True, the function will not detect gaps within the same PID.

    Returns
    -------
    object
            Returns 1.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SealGaps(1, 10, 30, 20)


    """


def SealHoles(max_diameter: float, ret_ents: bool) -> int:
    """

    Script version of function MESH>SHELL_MESH>FILL_GAP>Seal.
    Works on visible.

    Parameters
    ----------
    max_diameter : float
            Holes with diameter > max_diameter will not be sealed.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns 1.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SealHoles(100)


    """


def SetGridsThickness(
    grids: object, thickness: object, use_original_thickness: str
) -> int:
    """

    A function that Sets nodal thickness upon given grids. The number of the given thicknesses
    must be one (1) or equal to the number of the given grids.
    The thickness list must have the exact same number of thicknesses as the Grids list.
    If a Grid is included more than once then this Grid will be assigned the last given thickness.

    Parameters
    ----------
    grids : object
            A list of grid entities.

    thickness : object
            A list of thicknesses corresponding to the list of grids.

    use_original_thickness : str, optional
            "Add" / "Multiply". Choose whether the new value should be added
            or multiplied with the original nodal thickness of each grid.

    Returns
    -------
    int
            Returns 1 on success and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def test_set_thickness():
                thickness = [9.0, 2.0, 4.0, 5.0]
                grids = []
                grids.append(base.GetEntity(constants.ABAQUS, "NODE", 100))
                grids.append(base.GetEntity(constants.ABAQUS, "NODE", 101))
                grids.append(base.GetEntity(constants.ABAQUS, "NODE", 102))
                grids.append(base.GetEntity(constants.ABAQUS, "NODE", 102))

                print("Number of grids we collected: ", len(grids))
                mesh.SetGridsThickness(grids, thickness)


    """


def SetMeshParamTargetLength(function: str, value: float) -> int:
    """

    This function sets the target element length value.

    Parameters
    ----------
    function : str
            Can have the values "init_local", "average_length", "absolute" or "free".

    value : float, optional
            Target length for "absolute", or length multiplier for "init_local" or "average_length".

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SetMeshParamTargetLength("absolute", 10.0)


    """


def SetReconstructAttachedSolidsValue(
    attached_solids: str, conflicting_areas: str
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:func:`SetANSAdefaultsValues` instead.


    Sets parameter values concerning all shell mesh functions that run reconstruct
    when there are attached solids on the shells.

    Parameters
    ----------
    attached_solids : str, optional
            One of "local remesh", "affect only skin", "freeze skin" or "always ask"
            Determines if in case of attached solids the solids will be remeshed locally along with the shells, the shell mesh will change but solid mesh will remain untouched, the shells will be frozen or ask every time how to proceed (in no gui mode "local remesh" will be used in case of "always ask")

    conflicting_areas : str, optional
            One of "merge", "keep larger", "select" or "always ask"
            Defines the behaviour of the algorithm when the shells to be reconstruct are attached on structured solids in opposite areas.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    GetReconstructAttachedSolidsValue

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SetReconstructAttachedSolidsValue("local remesh", "merge")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:func: SetANSAdefaultsValues instead.",
        DeprecationWarning,
    )


def SetSmoothAttachedSolidsValue(attached_solids: str, conflicting_areas: str) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:func:`SetANSAdefaultsValues` instead.


    Sets parameter values concerning all shell mesh functions that run smooth
    when there are attached solids on the shells.

    Parameters
    ----------
    attached_solids : str, optional
            One of "local remesh", "affect only skin", "freeze skin" or "always ask"
            Determines if in case of attached solids the solids will be remeshed locally along with the shells, the shell mesh will change but solid mesh will remain untouched, the shells will be frozen or ask every time how to proceed (in no gui mode "local remesh" will be used in case of "always ask")

    conflicting_areas : str, optional
            One of "merge", "keep larger", "select" or "always ask"
            Defines the behavior of the algorithm when the shells to be reconstruct are attached on structured solids in opposite areas.

    Returns
    -------
    int
            Always returns 1.

    See Also
    --------
    GetSmoothAttachedSolidsValue

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SetSmoothAttachedSolidsValue("affect only skin")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:func: SetANSAdefaultsValues instead.",
        DeprecationWarning,
    )


def SetVolumesMapParameters(volume: object, method: str, steps: int) -> int:
    """

    This function specifies the parameters of a given Map volume.

    Parameters
    ----------
    volume : object
            The volume object of which the parameters will be changed.

    method : str
            The meshing method, the values of which can be "Normal parts"
            or "Thin parts".

    steps : int
            The number of the steps in the round area.

    Returns
    -------
    int
            Returns 1 if the values are properly assigned and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.SetVolumesMapParameters(vol, "Normal parts", 10)


    """


def SetVolumesOffsetParameters(
    volume: object, dist: float, steps: int, middle: int, biasing: str, factor: float
) -> int:
    """

    This function specifies the parameters of a given Offset volume.

    Parameters
    ----------
    volume : object
            The volume whose parameters will be changed.

    dist : float
            The offset length.

    steps : int
            The number of the generated elements.

    middle : int
            Can be 0 if offset is normal or 1 if the elements are divided
            in the middle and are extracted in both sides of the shell elements.

    biasing : str
            The biasing type: 'Linear', 'Exponential', Bell Curve' or 'No Biasing'.

    factor : float
            The biasing factor.

    Returns
    -------
    int
            Returns 1 if the values are returned correctly and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.SetVolumesOffsetParameters(vol, 10, 5, 0, "Linear", 1.05)


    """


def SetVolumesRotateParameters(
    volume: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
    angle: float,
    steps: int,
    biasing: str,
    factor: float,
) -> int:
    """

    This function specifies the parameters of a given Offset volume.

    Parameters
    ----------
    volume : object
            The volume whose parameters will be changed.

    x : float
            The x coordinate of the origin point.

    y : float
            The y coordinate of the origin point.

    z : float
            The z coordinate of the origin point.

    dx : float
            The x component of the rotational vector.

    dy : float
            The y component of the rotational vector.

    dz : float
            The z component of the rotational vector.

    angle : float
            The rotational angle.

    steps : int
            The number of the generated elements.

    biasing : str
            The biasing type: 'Linear', 'Exponential', 'Bell Curve'or 'No Biasing'.

    factor : float
            The biasing factor.

    Returns
    -------
    int
            Returns 1 if the values are returned correctly and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.SetVolumesRotateParameters(
                    vol, x, y, z, dx, dy, dz, angle, steps, bias_type, bias_factor
                )


    """


def SetVolumesTranslateParameters(
    volume: object,
    dx: float,
    dy: float,
    dz: float,
    dist: float,
    steps: int,
    biasing: str,
    factor: float,
) -> int:
    """

    This function specifies the parameters of a given Offset volume.

    Parameters
    ----------
    volume : object
            The volume whose parameters will be changed.

    dx : float
            The x component of the translational vector.

    dy : float
            The y component of the translational vector.

    dz : float
            The z component of the translational vector.

    dist : float
            The translational distance.

    steps : int
            The number of the generated elements.

    biasing : str
            The biasing type: 'Linear', 'Exponential', 'Bell Curve' or 'No Biasing'.

    factor : float
            The biasing factor.

    Returns
    -------
    int
            Returns 1 if the values are returned correctly and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.SetVolumesTranslateParameters(
                    vol, dx, dy, dz, dist, steps, bias_type, bias_factor
                )


    """


def SimplifyMacros(
    faces: object,
    fine_draft_slider: float,
    keep_perimeters_on_symmetry_plane: bool,
    maintain_sharp_edges: bool,
    minimum_side_length: float,
    minimum_perimeter_corner_angle: float,
    freeze_meshed_macros: bool,
    test_gui_result: bool,
) -> int:
    """

    This function integrates the manual operations of JOIN Perimeter Segments,
    or CUT Perimeter Segments, in order to satisfy the minimum requirements.

    Parameters
    ----------
    faces : object
            Accepted values: A list of faces, "ALL", "VISIBLE",
            None (runs for all faces of the database).

    fine_draft_slider : float, optional
            This scale affects the number of non-feature perimeters that
            will be joined.
            Accepted values are 0 - 100.
            The closer to 100 the more perimeters will be joined.

    keep_perimeters_on_symmetry_plane : bool, optional
            If set to True, then if a perimeter is on the symmetry plane,
            it will not be joined.

    maintain_sharp_edges : bool, optional
            If set to True, then the function does not affect sharp edges.

    minimum_side_length : float, optional
            The distance, under which the function will join one perimeter and
            make a new cut so that this value is not violated.

    minimum_perimeter_corner_angle : float, optional
            The angle between two perimeters, under which the function will
            join one perimeter and make a new cut so that this value is not
            violated.

    freeze_meshed_macros : bool, optional
            If set to True, then the function does not affect meshed macros.

    test_gui_result : bool, optional
            If set to True, tests the result on GUI.

    Returns
    -------
    int
            Returns 1 on success, 0 on error.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            # 1. On all faces of the database
            def main():
                ret = mesh.SimplifyMacros(
                    "ALL",
                    fine_draft_slider=50,
                    keep_perimeters_on_symmetry_plane=True,
                    maintain_sharp_edges=True,
                    minimum_side_length=3.5,
                    minimum_perimeter_corner_angle=30,
                    freeze_meshed_macros=True,
                )
                print(ret)


            # 2. Only on visible faces
            def main():
                ret = mesh.SimplifyMacros(
                    "VISIBLE",
                    fine_draft_slider=50,
                    keep_perimeters_on_symmetry_plane=True,
                    maintain_sharp_edges=True,
                    minimum_side_length=3.5,
                    minimum_perimeter_corner_angle=30,
                    freeze_meshed_macros=True,
                )
                print(ret)


            # 3. On a list of faces
            def main():
                all_faces = base.CollectEntities(0, None, ("FACE",))
                if len(all_faces) == 0:
                    return
                ret = mesh.SimplifyMacros(
                    all_faces,
                    fine_draft_slider=50,
                    keep_perimeters_on_symmetry_plane=True,
                    maintain_sharp_edges=True,
                    minimum_side_length=3.5,
                    minimum_perimeter_corner_angle=30,
                    freeze_meshed_macros=True,
                )
                print(ret)


    """


def SmoothTetra() -> int:
    """
    .. deprecated:: 22.0.0
            Use :py:func:`SolidSmooth` instead.


    This function applies IMPROVE>SMOOTH on visible TETRA elements.

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SmoothTetra()


    """

    import warnings

    warnings.warn(
        "Deprecated since version 22.0.0. Use :py:func: SolidSmooth instead.",
        DeprecationWarning,
    )


def SplitEdges(option_for_trias: int) -> int:
    """

    This function splits all visible edges in the model in a similar way to the
    SPLIT function when edges are selected. Its argument is an integer.

    Parameters
    ----------
    option_for_trias : int
            Accepted Values are 1 and 2, where 1 determines that triangles are split so
            that they form 4 other triangles, and 2 determines that they will be split as
            to form 3 quads. Quads will be split in a way to form 4 other quads.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SplitEdges(1)


    """


def SplitElements(shells: object, ret_ents: bool) -> int:
    """

    The function splits all quad elements contained in a list, which is passed as argument.

    Parameters
    ----------
    shells : object
            A list containing all the quad elements to be splitted.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns 1 on success, otherwise 0.

            If ret_ents=True it will return a list with the created entities or an empty list if no entities were created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL", False)
                mesh.SplitElements(shells)


    """


def SplitNodes() -> int:
    """

    This function splits shells similarly to the SPLIT function with nodes selected.
    It accepts no arguments, quads are split to form two triangles and triangles are
    split to form three other triangles.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SplitNodes()


    """


def SplitPolys() -> int:
    """

    This function splits polygons to triangles. The new triangles are assigned the
    same property with the polygon, or a new default property, if the polygon is
    a polyhedral face with no property. Shells are also created to the feature lines
    between properties. The function accepts no arguments.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SplitPolys()


    """


def TetraCFD(volume: object) -> int:
    """

    The function generates tetra volume meshing of defined Volumes using the Tetra CFD algorithm.

    Parameters
    ----------
    volume : object, optional
            The volume to be meshed.
            If it is not given, all volumes will be meshed.

    Returns
    -------
    int
            Returns 0 on success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                volume = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.TetraCFD(volume)


    """


def TetraCFDbyID(Vol_ID: int) -> int:
    """
    .. deprecated:: 18.0.0
            Use :py:func:`TetraCFD` instead.


    The function generates tetra volume meshing to a Volume defined by its id, using the Tetra CFD algorithm.

    Parameters
    ----------
    Vol_ID : int
            The volume id.

    Returns
    -------
    int
            Returns 0 on success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.TetraCFDbyID(2)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 18.0.0. Use :py:func: TetraCFD instead.",
        DeprecationWarning,
    )


def TetraFEM(volume: object) -> int:
    """

    Script function for tetra volume meshing of defined Volumes using the Tetra FEM algorithm.

    Parameters
    ----------
    volume : object, optional
            The volume to be meshed.
            If it is not given, all volumes will be meshed.

    Returns
    -------
    int
            Returns 0 on success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                volume = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.TetraFEM(volume)


    """


def TetraFEMbyID(VOL_ID: int) -> int:
    """

    Script function for tetra volume meshing, defining it by its id, using the Tetra FEM algorithm.

    Parameters
    ----------
    VOL_ID : int
            The volume id.

    Returns
    -------
    int
            Returns 0 on success, non-zero on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.TetraFEMbyID(2)


    """


def UnmeshedMacros() -> int:
    """

    This function hides all the meshed macros and leaves only the unmeshed ones visible.
    It has the exact same effect as the UNMESHED>MACROs button on the FOCUS menu.

    Returns
    -------
    int
            Returns the number of the unmeshed macros.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                unmeshed_macros = mesh.UnmeshedMacros()
                if unmeshed_macros > 0:
                    print(str(unmeshed_macros), " found in the database")
                else:
                    print("No unmeshed macros found in the database")


    """


def UnmeshedVolumes(return_volumes: object) -> int:
    """

    This function hides all the meshed volumes and leaves only the unmeshed ones visible.
    It has the exact same effect as the UNMESHED>VOLUMEs button of the FOCUS menu.

    Parameters
    ----------
    return_volumes : object, optional
            If True then it returns an array with the unmeshed volume entities found

    Returns
    -------
    int
            Returns 0 if no unmeshed volumes are found and 1 if there is any unmeshed volumes.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.UnmeshedVolumes()


    """


def VolumeType(volume: object) -> str:
    """

    This function returns the type of a given volume, the values of which can be "Undefined", "Translate",
    "Rotate", "Offset", "Glide", "Sweep", "Dual Sweep", "Tetra FEM", "Tetra CFD", "Hexa Interior", "Tetra rapid",
    "Layers", "Tetra Rapid", "Map Thin", "Map" or "HexaPoly".

    Parameters
    ----------
    volume : object
            The volume object to get its type.

    Returns
    -------
    str
            Returns the type of the volume on success and blank otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                if mesh.VolumeType(vol) == "Map":
                    mesh.GetVolumesMapParameters(vol, method, steps)


    """


def VolumesDelete(volume: object) -> int:
    """

    This function deletes a given volume or an array of volumes.

    Parameters
    ----------
    volume : object
            A reference to the volume entity to be deleted or an array of volumes.

    Returns
    -------
    int
            Returns 1 on success and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.VolumesDelete(vol)


    """


def VolumesDetect(
    method_option: int, return_volumes: bool, include_facets: bool, whole_db: bool
) -> object:
    """

    This function can be used in order to detect volumes. The model must be already surface meshed.

    Parameters
    ----------
    method_option : int, optional
            A number that corresponds to the detection method.
            Its value can be:
            1: Detects all valid volumes and their sub-volumes.
            2: Detects volumes independantly from their sub_volumes.
            3: Detects volumes independantly from their sub_volumes neglecting any zero-
               thickness walls.
            (Default: 1)

    return_volumes : bool, optional
            Determines if the function will return a list with the detected volumes
            or the number of the detected volumes.

    include_facets : bool, optional
            If set to True, free solid facets will also be included in the volume detection.

    whole_db : bool, optional
            If set to True, it will search for volumes in the entire model,
            otherwise it will work on visible.

    Returns
    -------
    object
            Returns the number of volumes that have been detected, if the argument 'return_volumes' is ommited or set to False.
            Otherwise it returns a list with the detected volumes.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                ret = mesh.VolumesDetect(1)


            # ...or...


            def main():
                vols = mesh.VolumesDetect(1, return_volumes=True)


    """


def VolumesErase(volume) -> int:
    """

    This function erases the volume mesh of a given meshed volume or an array of volumes.

    Parameters
    ----------
    volume :
            A reference to the volume entity or an array of volumes.

    Returns
    -------
    int
            Returns 1 on success and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                mesh.VolumesErase(vol)


    """


def VolumesMap(
    master: object,
    slave: object,
    round: object,
    method: str,
    steps: int,
    part: str,
    prop: str,
    ret_ents: bool,
    light_volume_representation: bool,
) -> object:
    """

    This function can be used in order to define and mesh a "Map" volume.

    Parameters
    ----------
    master : object
            A list of shell objects that define the master area.

    slave : object
            A list of shell objects that define the slave area.

    round : object
            A list of shell objects that define the side area.

    method : str, optional
            The method used for the solid elements calculation, whose values
            can be "Normal parts" or "Thin parts".

    steps : int, optional
            The number of the solid steps that will be created along the round area.

    part : str, optional
            The part that will be assigned to the created volume.

    prop : str, optional
            The property that will be assigned to the created volume.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    light_volume_representation : bool, optional
            If set to True, the created volume will be of light volume representation.

    Returns
    -------
    object
            Returns 1 on success or 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                face1 = base.GetEntity(constants.NASTRAN, "FACE", 1)
                face2 = base.GetEntity(constants.NASTRAN, "FACE", 2)
                face3 = base.GetEntity(constants.NASTRAN, "FACE", 3)
                face4 = base.GetEntity(constants.NASTRAN, "FACE", 4)
                face5 = base.GetEntity(constants.NASTRAN, "FACE", 5)
                face6 = base.GetEntity(constants.NASTRAN, "FACE", 6)
                face7 = base.GetEntity(constants.NASTRAN, "FACE", 7)

                master = []
                master.append(face1)

                slave = []
                slave.append(face2)
                slave.append(face3)

                round_areas = []
                round_areas.append(face4)
                round_areas.append(face5)
                round_areas.append(face6)
                round_areas.append(face7)

                part = base.GetPartFromModuleId("200")
                prop = base.GetEntity(constants.NASTRAN, "PSOLID", 3)

                mesh.VolumesMap(master, slave, round_areas, "Normal parts", 16, part, prop)


    """


def VolumesMeshV(volume: object, mesh_type: str) -> int:
    """

    This function can be used in order to automatically mesh an already defined volume or an array of volumes.

    Parameters
    ----------
    volume : object
            The volume to be meshed or an array of volumes

    mesh_type : str
            Corresponds to the mesh generator.
            The string values for each mesh type can be:
            "TETRA RAPID", "TETRA FEM", "TETRA CFD",
            "HEXA INTERIOR" or "HEXAPOLY".

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                vol = mesh.VolumesDetect()

                ents = base.CollectEntities(constants.NASTRAN, None, "VOLUME")
                mesh.VolumesMeshV(ents, "TETRA RAPID")


    """


def VolumesOffset(
    boundary_array: object,
    dist: float,
    steps: int,
    middle: int,
    bias: str,
    factor: float,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume by offsetting a shell mesh
    along a direction specified by the normal vector of the elements.

    Parameters
    ----------
    boundary_array : object
            A list of ANSA entities that will be used as the base from which solid elements
            will be generated via offsetting.
            This list may contain:
            -FACEs.
            -Released SHELL elements that do not belong in a FACE.

    dist : float
            The offset length. Use a negative number to offset to the opposite direction.

    steps : int
            The number of generated elements along the offset direction.

    middle : int
            Defines the offset mode:
            -0: Offset normally towards positive direction.
            -1: Offset towards both directions, by splitting distance and
                steps for each direction.

    bias : str
            Define biasing in the distribution of generated elements along the offset direction.
            Possible values are:
            -'Linear'
            -'Exponential'
            -'Bell Curve'
            -'No Biasing'

    factor : float
            Factor to be used by the offset method defined in the 'bias' argument.

    part : object, optional
            The part where the entities will be placed in.
            If absent, the current part will be used.

    property : object, optional
            The property where the generated solid elements will refer to.
            If absent, a new one will be created.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base, mesh, constants


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE", False, True)
                # part = base.GetPartFromName('offset_solids')
                # property = base.GetEntity(constants.NASTRAN, 'PSOLID', 35)

                if all_faces:
                    mesh.VolumesOffset(all_faces, 30.0, 10, 0, "Exponential", 1.2)
                    # mesh.VolumesOffset(all_faces, 30., 10, 0, "Exponential", 1.2, part, property)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def VolumesParameters(
    growth_rate: float,
    max_length: float,
    criterion_type: str,
    criterion_val: float,
    geometry_checks: bool,
) -> int:
    """

    This function specifies the volume meshing parameters as they appear in the
    MESH>VOLUMEs>PARAM window.

    Parameters
    ----------
    growth_rate : float
            The maximum growth rate.

    max_length : float
            The maximum element length.

    criterion_type : str
            Containing the criterion definition.
            The values of this argument can be:
            -"NASTRAN Aspect"
            -"FLUENT Aspect"
            -"I-DEAS Stretch"
            -"ABAQUS Shape Factor"
            -"FLUENT Skewness"

    criterion_val : float
            The criterion value.

    geometry_checks : bool
            Defines if geometry checks will be performed or not.

    Returns
    -------
    int
            Returns 1 if the values are properly assigned and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.VolumesParameters(1.2, 50, "NASTRAN Aspect", 3, True)


    """


def VolumesRemesh(ENTITY: object) -> int:
    """

    This function can be used in order to automatically mesh an already defined volume or an array of volumes.

    Parameters
    ----------
    ENTITY : object
            The volume object to be meshed or an array of volumes

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                ents = base.CollectEntities(constants.NASTRAN, None, "VOLUME")
                mesh.VolumesRemesh(ents)


    """


def VolumesRotate(
    boundary_array: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
    angle: float,
    steps: int,
    bias: str,
    factor: float,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume by rotating a predefined shell mesh around an axis.

    Parameters
    ----------
    boundary_array : object
            A list of shell objects.

    x : float
            The x coordinate of the origin point.

    y : float
            The y coordinate of the origin point.

    z : float
            The z coordinate of the origin point.

    dx : float
            The x component of the rotational vector.

    dy : float
            The y component of the rotational vector.

    dz : float
            The z component of the rotational vector.

    angle : float
            The rotational angle.

    steps : int
            The number of the generated elements.

    bias : str
            One of "Linear", "Exponential", "Bell Curve" or "No Biasing".

    factor : float
            The biasing factor.

    part : object, optional
            The reference of the part where the volume will belong.

    property : object, optional
            The reference of the property that will be assigned.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                search_faces = ("FACE",)
                all_faces = base.CollectEntities(constants.NASTRAN, None, search_faces, False)
                if len(all_faces):
                    mesh.VolumesRotate(
                        all_faces, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 30.0, 5, "No Biasing", 1.2
                    )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def VolumesTranslate(
    boundary_array: object,
    dx: float,
    dy: float,
    dz: float,
    dist: float,
    steps: int,
    bias: str,
    factor: float,
    part: str,
    property: int,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume by translating a predefined shell mesh along a direction specified by a vector.

    Parameters
    ----------
    boundary_array : object
            A list of shell objects to be translated.

    dx : float
            The x component of the translational vector.

    dy : float
            The y component of the translational vector.

    dz : float
            The z component of the translational vector.

    dist : float
            The translational distance.

    steps : int
            The number of generated element steps.

    bias : str
            One of "Linear", "Exponential", "Bell Curve" or "No Biasing".

    factor : float
            The biasing factor.

    part : str, optional
            The part name.

    property : int, optional
            The property id.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import constants
            from ansa import base


            def main():
                search_faces = ("FACE",)
                all_faces = base.CollectEntities(constants.NASTRAN, None, search_faces, False)
                if len(all_faces):
                    mesh.VolumesTranslate(all_faces, 0.0, 0.0, 1.0, 20, 5, "Linear", 1.2)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def Volumize(
    entities: object,
    solid_layers: int,
    paste_tol: float,
    merge_distance: float,
    offset_mode: int,
    sharp_edges_angle: float,
    thickness_factor: float,
    thickness_averaging: str,
    delete_original_shells: bool,
    refine_single_bounds: bool,
    max_aspect: float,
    create_skin_shells: bool,
    penta_element_type: str,
    hexa_element_type: str,
) -> object:
    """

    Applies volumize function on shells.

    Parameters
    ----------
    entities : object
            A list of shell objects. If None it will run on all visible shells.

    solid_layers : int
            If '0', the function will not create any solids inside the volumize result.
            Any other number specifies the number of layers of solids inside the volumize result.

    paste_tol : float
            Will paste the volumize edges where the initial model had single edges and thickness
            under paste_tol value.

    merge_distance : float
            The function will collide flanges within this tolerance.

    offset_mode : int
            if 1, volumize will be implemented towards the 'grey' side of the source shells.
            if -1, volumize will be implemented towards the 'yellow' side of the source shells.
            if 0 volumize will be implemented towards both sides of the source shells.

    sharp_edges_angle : float, optional
            The cut-off angle that limits the movement of nodes on sharp edges.

    thickness_factor : float, optional
            Apply this factor in thickness of result entities.

    thickness_averaging : str, optional
            If "Keep average", the average offset of node-neighboring entities is used.
            If "Keep maximum", the maximum offset of node-neighboring entities is used.
            If "Keep minimum", the minimum offset of node-neighboring entities is used.

    delete_original_shells : bool, optional
            Decides whether original shells are deleted or not.

    refine_single_bounds : bool, optional
            Decides whether refinement of single bounds is enabled.

    max_aspect : float, optional
            The maximum aspect for "Refine single bounds".

    create_skin_shells : bool, optional
            It controls if a shell coating will be created from the volume elements.

    penta_element_type : str, optional
            (For the generation of high order volume elements)
            A string that describes the desired element type variation for pentas. It can be retrieved from the title of the element's edit card, where it is displayed within brackets.

    hexa_element_type : str, optional
            (For the generation of high order volume elements)
            A string that describes the desired element type variation for hexas. It can be retrieved from the title of the element's edit card, where it is displayed within brackets.

    Returns
    -------
    object
            Returns 0 if for any reason volumizing failed.
            Returns a list containing all volumized elements if volumizing succeeded.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.Volumize(
                    shells, 1, 0, 0, -1
                )  # It will generate one solid layer towards the yellow side


    """


def Wrap(
    input_data: object,
    tolerance: float,
    volume_type: str,
    wrap_style: str,
    wrap_style_argument: float,
    separate_sets_flags: str,
    separate_sets_angle: float,
    counter_volumes: int,
    part_name: str,
    property_id: int,
) -> object:
    """

    Creates a wrap mesh for the user data.

    Parameters
    ----------
    input_data : object
            A list with objects of input data of the wrap. The object can be shell, solid,
            face, property shell, property solid, volume, set, include, part or group.

    tolerance : float
            The value of tolerance for the wrap function.

    volume_type : str
            Defines the type of volume. That string takes two values "in" or "out".

    wrap_style : str
            Defines the style of the wrap. That string takes two values "tight" or "smooth".

    wrap_style_argument : float
            For the wrap style "tight" the value must be float while for the wrap style
            "smooth" it must be integer.

    separate_sets_flags : str
            Defines the creation of separate sets, (set "yes" or "no" to enable or not).

    separate_sets_angle : float
            The value of angle for the creation of separate sets.

    counter_volumes : int
            The number of volumes to be created. If it is negative or bigger
            than the number of detected volumes, the wrap function will be applied on all
            detected volumes. If the value is positive and smaller than the number of detected
            volumes, the wrap function will be applied on the specified number of volumes
            in descending order.

    part_name : str
            The 'module Id' of part/group. If the string is empty (e. ""),
            the function creates a default part to place the results of the wrap.

    property_id : int
            The value of the 'property Id'. If the value is equal to zero or negative, the
            function creates one default property to place the results of the wrap.

    Returns
    -------
    object
            Returns a list with the results of the wrap.
            The list contains two lists. The list in position '0' has the lists
            of elements for each volume. The list in position '1' is created, if the user
            set argument 'separate_sets_flags' equal to "yes" and the values of
            that are the sets for each volume. The two above lists have the same number of
            data which is equal to the number of volumes specified from the user. Also,
            there is one to one correspondence between them. Thus, the 'elements' and 'sets'
            of volume 'i' are located in position 'i' of the above lists. In these positions 'i'
            the entities are lists of 'elements' and 'sets' for volume 'i'.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                ent = (
                    base.GetEntity(constants.NASTRAN, "PSOLID", 10),
                    base.GetEntity(constants.NASTRAN, "INCLUDE", 1),
                    base.GetFirstEntity(constants.NASTRAN, "FACE"),
                    base.GetFirstEntity(constants.NASTRAN, "SET"),
                    base.GetPartFromModuleId("10"),
                    base.GetEntity(constants.NASTRAN, "PSHELL", 1),
                    base.GetEntity(constants.NASTRAN, "MAT1", 911),
                )
                print(len(ent))

                res_wrap = mesh.Wrap(ent, 7.0, "in", "tight", 0.05, "no", 10.0, -1, "1000", 0)
                print("length of outermost:", len(res_wrap))
                volume_matrix = res_wrap[0]
                print("Number of volumes:", len(volume_matrix))
                for i in range(volume_matrix):
                    print(
                        "Number of shells for volume " + str(i + 1) + " is:", len(volume_matrix[i])
                    )


    """


def xyzIsInsideVolume(x: float, y: float, z: float, return_all_volumes: bool) -> object:
    """

    This function takes as arguments the coordinates of a point and checks whether this
    point is inside a defined volume, and if yes in which.

    Parameters
    ----------
    x : float
            The x coordinate of the point.

    y : float
            The y coordinate of the point.

    z : float
            The z coordinate of the point.

    return_all_volumes : bool, optional
            If set to True, the function returns a list with all the volumes
            the point belongs to.

    Returns
    -------
    object
            If the argument "return_all_volumes" is omitted or is set to False, the function
            returns the id of the smaller volume the point belongs to or 0 if no volume found.
            If the optional argument is set to True, then a list with all the volumes the point
            belongs to is returned. In case the point is not inside a defined volume, None is returned.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.VolumesDetect()
                vol_id = mesh.xyzIsInsideVolume(0.8435135, 48.527813, -25.09305)


            # ...or...


            def main():
                mesh.VolumesDetect()
                vols = mesh.xyzIsInsideVolume(
                    0.8435135, 48.527813, -25.09305, return_all_volumes=True
                )


    """


def xyzIsInsideVolumeMatrix(
    points_coordinates: object, return_all_volumes: bool, input_vols: object
) -> object:
    """

    This function takes as argument a matrix with the coordinates of points and checks
    whether these points are inside a defined volume, and if yes in which volume.

    Parameters
    ----------
    points_coordinates : object
            A list with lists defining points.

    return_all_volumes : bool, optional
            If set to True, the function will return a list containing a list for
            every xyz point with all the volumes it belongs to.

    input_vols : object, optional
            Array of volumes on which to perform the check. If nothing is provided then the entire db is checked

    Returns
    -------
    object
            Returns a list of integers where each of them corresponds to the given points. The value can be
            either greater than 0, in case the given point is inside a defined volume and corresponds to the id
            of the volume, or 0, in case the point is not inside any defined volume.
            If the argument "return_all_volumes" is set to True, then it will return a list for each point
            containing all the volumes the point belongs to.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                xyz = (
                    (7.520866, 1.802020, 8.167846),
                    (2.982863, 4.345732, 1.956690),
                    (6.528636, 3.640289, 11.42791),
                )

                ret_vals = mesh.xyzIsInsideVolumeMatrix(xyz)
                for val in ret_vals:
                    print("Point is inside vol: ", val)


    """


def CreateBestMesh() -> int:
    """

    This function meshes the Macros with all the algorithms and keeps only the mesh with the
    best quality according to QCHECK Skewness. The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateBestMesh()


    """


def CreateCfdMesh() -> int:
    """

    This function incorporates an advanced meshing algorithm tailored made to meet CFD specs
    or other application areas where a variable size mesh is required. The algorithm meshes
    with variable element length depending on the local curvature of the underlying CAD surface,
    under tight user-controlled specifications.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateCfdMesh()


    """


def CreateFreeMesh() -> int:
    """

    This function meshes using the free algorithm. This algorithm generates as few
    elements as possible, trying to maintain the best quality possible.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateFreeMesh()


    """


def CreateGradualMesh() -> int:
    """

    This function incorporates a meshing algorithm, which generates more elements
    and its goal is to give better results to Macro Areas with uneven nodal
    distributions that require a gradual transition of the element size.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateGradualMesh()


    """


def CreateMapMesh() -> int:
    """

    This function incorporates a meshing algorithm, which generates a structured
    mesh close to quadrilateral shaped Macro Areas.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateMapMesh()


    """


def CreateSpotMesh() -> int:
    """

    This function incorporates a meshing algorithm, which generates more elements than the free
    algorithm and brings better results to Macros that have Weld or Connecting Spots on them.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateSpotMesh()


    """


def CreateStlMesh() -> int:
    """

    This function meshes using the STL algorithm. This algorithm can be used for applications where
    the quality of the elements is not very important but the exact geometry representation is.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateStlMesh()


    """


def CreateAdvFrontMesh() -> int:
    """

    The algorithm of this function generates shell elements starting from the boundaries of the Macro Areas.
    As a result the mesh follows the shape of the Perimeter Segments.
    The function works only on visible macros.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.CreateAdvFrontMesh()


    """


def NumberPerimeters(
    input: object,
    number: str,
    apply_multiple_number: bool,
    remesh_macros: bool,
    apply_number_of: str,
    use_ansa_defaults_values: bool,
) -> int:
    """

    This function defines a new number of edges (or nodes) on Macro Area's perimeter segments, FE perimeters or Hexa Box Edges.

    Parameters
    ----------
    input : object
            Can be an entity or a list of entities, parts, properties, materials,
            sets, macros, CONS, hexa box faces or hexa box edges.
            If the input is 0, visible CONS and hexa box edges are collected.

    number : str
            A string which can either be equal to a number (eg. "3"), or an expression
            to add or remove nodes (eg. "+2", "-3", "*2").

    apply_multiple_number : bool, optional
            If set to True, the function creates chains of connected Perimeters
            (or hexa box edges) and distributes accordingly the given number
            to the chains. If deactivated (False) or missing, then all the entities will
            get the same number.

    remesh_macros : bool, optional
            If set to True, the function remeshes the affected macros (or hexa box faces)
            after applying the number. If missing (False) then the current gui value
            will be used.

    apply_number_of : str, optional
            It takes the values "edges" or "nodes", and it applies as INPUT as a
            number of edges or nodes. If missing then the current gui value will be used.

    use_ansa_defaults_values : bool, optional
            If set to True, the function uses parameters from ANSA.defaults, by-passing all other arguments.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            # Example 1:
            def main():
                # Increases the current number of the perimeters in the set by 2.
                base.GetEntity(deck=constants.NASTRAN, type="SET", element_id=1)
                mesh.NumberPerimeters(ent, "+2", apply_multiple_number=False, remesh_macros=True)


            # Example 2:
            def main():
                # Multiplies current number of all visible CONS, FE perimeters and hexa box edges by 2.
                mesh.NumberPerimeters(0, "*2")


            # Example 3:
            def main():
                # Multiplies current number of all visible CONS, FE perimeters and hexa box edges by 2.
                mesh.NumberPerimeters(0, "*0.5", use_ansa_defaults_values=True)


    """


def GetCompareWorkingDirectory() -> str:
    """

    The function returns the path to the defined working directory of the Compare Tool.

    Returns
    -------
    str
            Returns a string containing the path of the working directory of the Compare Tool.

    See Also
    --------
    SetCompareWorkingDirectory

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                work_dir_path = mesh.GetCompareWorkingDirectory()
                print(work_dir_path)


    """


def SetCompareWorkingDirectory(path: str) -> int:
    """

    The function sets the path of the working directory of the Compare Tool.

    Parameters
    ----------
    path : str
            The path of the working directory.

    Returns
    -------
    int
            Returns 1 if a valid path is given, 0 otherwise.

    See Also
    --------
    GetCompareWorkingDirectory

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SetCompareWorkingDirectory("filepath/to/work_dir/")


    """


def VolumizeComposites(
    deck: int,
    entities: object,
    delete_original_shells: bool,
    stacking: str,
    fill_ply_drop_offs: bool,
    ret_ents: bool,
    create: str,
    merge_method: str,
    merge_t_tol: float,
    merge_theta_tol: float,
    drop_off_prop: object,
    force_split_woven_layers: bool,
    avoid_hanging_edges: bool,
    ret_all: object,
    rows_num: int,
) -> object:
    """

    This function creates composite solids (SOLID_LAMINATE) from composite shells (PCOMP or LAMINATE).

    Parameters
    ----------
    deck : int
            One of NASTRAN, ABAQUS or ANSYS.

    entities : object
            A list of composite shells, properties, sets or parts containing
            composite shells

    delete_original_shells : bool, optional
            A flag for deleting original shells.

    stacking : str, optional
            One of "single element" or "per ply".

    fill_ply_drop_offs : bool, optional
            A flag for filling ply drop-offs.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    create : str, optional
            One of "thick_shells" or "solids".

    merge_method : str, optional
            The method by which the layers of different properties will be merged.
            One of "by_tolerances", "by_gplyid", "by_layer_name".
            Required only for multiple properties and stacking = "per ply".

    merge_t_tol : float, optional
            The thickness tolerance by which the layers of different properties
            will be merged. Required for merge_method = "by_tolerances".

    merge_theta_tol : float, optional
            The theta tolerance by which the layers of different properties
            will be merged. Required for merge_method = "by_tolerances".

    drop_off_prop : object, optional
            The simple solid property of the ply drop-offs. If not given and
            fill_ply_drop_offs is True, then a default solid property is created.

    force_split_woven_layers : bool, optional
            If True, woven layers are split.
            If False, woven layers are not split, except from SOLID_LAMINATE
            in LSDYNA, PAMCRASH, RADIOSS and PERMAS.

    avoid_hanging_edges : bool, optional
            When stacking is "per ply" and fill_ply_drop_offs is True,
            avoid hanging edges by creating pyramids (drop-off elements)
            and by splitting hexas to pentas (layer elements).

    ret_all : object, optional
            If True the function returns a numedtuple with all the available data.
            (Default: False)

    rows_num : int, optional
            Number of rows per layer that will be created.

    Returns
    -------
    object
            Returns 0 on success.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

            If ret_all=True it will return a namedtuple 'ret' with the following members:
            ret.created_elements: a list of the created elements
            ret.property_pairs: a list of tuples: (original shell property, created thick shell or solid property)

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                deck = constants.NASTRAN
                lam = base.GetFirstEntity(deck, "LAMINATE")
                mesh.VolumizeComposites(
                    deck,
                    lam,
                    delete_original_shells=True,
                    stacking="per ply",
                    fill_ply_drop_offs=False,
                )


    """


def IntersectSolidDescription(
    input: object,
    fuse_distance: float,
    inflate_distance: float,
    ignore_same_pid: bool,
    ignore_same_part: bool,
    ignore_same_set: bool,
    ignore_same_neighour_zones: int,
    keep_separation_walls: bool,
    create_pid_for_separation_walls: bool,
    improve_mesh_quality: bool,
    trash_treatment: str,
) -> int:
    """

    This function intersects FE shells and identifies inner and outer walls,

    Parameters
    ----------
    input : object
            A single object or a list of parts, properties, materials or sets.
            If input equals to 0, the visible shells are collected.

    fuse_distance : float, optional
            See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

    inflate_distance : float, optional
            See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

    ignore_same_pid : bool, optional
            If set to True, ignores intersections within the same property.

    ignore_same_part : bool, optional
            If set to True, ignores intersections within the same part.

    ignore_same_set : bool, optional
            If set to True, ignores intersections within the same set.

    ignore_same_neighour_zones : int, optional
            If set to True, ignores intersection between shells that are
            within n zones from each other.

    keep_separation_walls : bool, optional
            If set to True, keeps primary inner walls.

    create_pid_for_separation_walls : bool, optional
            If set to True, creates pids for primary inner walls.

    improve_mesh_quality : bool, optional
            If set to True, improves the mesh quality in 1 zone around
            the intersected shells.

    trash_treatment : str, optional
            Determines the treatment of the contents of the trash list. I.e. the inner shells as shown in the trash lists of the last 2 pages of the wizard. Accepted values: "none", "add to set" and "delete". Default value is "delete".

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                parts = []
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                mesh.IntersectSolidDescription(
                    parts,
                    inflate_distance=5,
                    ignore_same_pid=True,
                    ignore_same_neighour_zones=3,
                    improve_mesh_quality=True,
                )


    """


def IntersectSkinDescription(
    input: object,
    fuse_distance: float,
    ignore_same_pid: bool,
    ignore_same_part: bool,
    ignore_same_set: bool,
    ignore_same_neighour_zones: int,
    improve_mesh_quality: bool,
) -> int:
    """

    This function intersects FE shells,

    Parameters
    ----------
    input : object
            An single object or a list of parts, properties, materials or sets.
            If input equals to 0, the visible shells are collected.

    fuse_distance : float, optional
            See tooltip at MESH>SHELL_MESH>INTERSECT>Solid description wizard.

    ignore_same_pid : bool, optional
            If set to True, ignores intersections within the same property.

    ignore_same_part : bool, optional
            If set to True, ignores intersections within the same part.

    ignore_same_set : bool, optional
            If set to True, ignores intersections within the same set.

    ignore_same_neighour_zones : int, optional
            If set to True, ignores intersection between shells that are
            within n zones from each other.

    improve_mesh_quality : bool, optional
            If set to True, improves the mesh quality in 1 zone around
            the intersected shells.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                parts = []
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                mesh.IntersectSkinDescription(
                    parts,
                    fuse_distance=0.1,
                    ignore_same_pid=True,
                    ignore_same_neighour_zones=3,
                    improve_mesh_quality=True,
                )


    """


def FillGapCoons(
    input: object,
    alternative: bool,
    improve_result_zones: int,
    result_set_id: int,
    ret_ents: bool,
) -> int:
    """

    This function creates FE shells to fill a gap defined by cons, curves or edges.
    Each call of the function fills a single gap.

    Parameters
    ----------
    input : object
            A list of cons, curves or sets of edges.

    alternative : bool, optional
            Fills with alternative option on, if available.

    improve_result_zones : int, optional
            Improves the quality of the result FE shells and [user defined] zones
            around them.

    result_set_id : int, optional
            Adds the result FE shells to a set with [user defined] id.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns the number of the created FE shells (before mesh improvement).
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Check how the syntax in each case should be
                input = []
                input.append(base.GetEntity(constants.NASTRAN, "CONS", 1923054))
                input.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                input.append(base.GetEntity(constants.NASTRAN, "SET", 1))
                mesh.FillGapCoons(input, improve_result_zones=0, result_set_id=5)


    """


def FillGapDraft(
    input: object,
    alternative: bool,
    improve_result_zones: int,
    result_set_id: int,
    ret_ents: bool,
) -> int:
    """

    This function creates FE shells to fill a gap defined by cons, curves or edges.
    Each call of the function fills a single gap.

    Parameters
    ----------
    input : object
            A list of cons, curves, sets of edges.

    alternative : bool, optional
            Fills with alternative option on, if available.

    improve_result_zones : int, optional
            Improves the quality of the result FE shells and [user defined] zones
            around them.

    result_set_id : int, optional
            Adds the result FE shells to a set with [user defined] id.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns the number of the created FE shells (before mesh improvement).
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Check how the syntax in each case should be
                input = []
                input.append(base.GetEntity(constants.NASTRAN, "CONS", 1923054))
                input.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                input.append(base.GetEntity(constants.NASTRAN, "SET", 1))
                mesh.FillGapDraft(input, improve_result_zones=0, result_set_id=5)


    """


def HexaBoxSweepGlide(
    extrusion_type: str,
    guideline_ents: object,
    box_face: object,
    curves: object,
    points: object,
    section_type: str,
    radius: float,
    width: float,
    dx: float,
    dy: float,
    dz: float,
    height: float,
    lower_base: float,
    upper_base: float,
) -> object:
    """

    Function for creating a hexa box through extrusion. Both 'sweep' and 'glide' extrusion types are supported.

    The direction of the extrusion is defined through curves, or points, or a combination of them.
    Curves may form a connected or disconnected path (a path will be automatically created).
    Note that single points are ignored (i.e. if any points are to be used, they should be at least two).

    The user has four options in defining the cross section, one with a box face, one with curves,
    one with curves and points and, finally, one with a predefined shape.
    The box_face option expects a single box face entity (which will be pasted to the new one after creation of the box).
    The curves option expects one or more curves (unconnected ones will be automatically connected
    to form a closed cross section shape). The selected curves should contain at least 4 points,
    so that they can be adopted for the definition of the four box edges.
    The points option should only follow a previous curves-curve_entities pair, and explicitly
    defines the points to be used for the four box edges definition. These points should be
    part of the curve_entities provided.
    The predefined cross section includes a circular with the required radius, a square with
    its side length, a rectangular with its width and height, and a trapezoidal with its two
    bases' lenths and height. Except for the circular, these cross sections also require a
    vector defining the 'height' direction of the cross section.
    Note that several kind of edges may be used as a curve, including element edges
    (provided as edge sets), CONS, 3D curves and box edges. Similarly, grids, hot points
    and box edge corner points may be employed for any point entities.

    Parameters
    ----------
    extrusion_type : str
            The keyword "sweep" or "glide", denoting the type of the extrusion.

    guideline_ents : object
            A list of entities defining the direction of the extrusion.
            (Collection of curves and/or points)

    box_face : object, optional
            A box face entity to be used as a cross section.
            (Note that new face will be pasted to the old)

    curves : object, optional
            Curve entities defining the  cross section.
            (They do not have to form a closed perimeter)

    points : object, optional
            Point entities defining the position of the box edges (used only in
            conjunction with 'curves'). Note that points should be among the
            points of the curve_entities provided above.

    section_type : str, optional
            A string specifying the predefined section type ("circular", "square",
            "rectangular", trapezoidal"). Additional data needed per case:
            -"circular" requires "radius".
            -"square" requires "width" and  height direction "dx","dy","dz".
            -"rectangular" requires "width", "height", and height direction "dx","dy","dz".
            -"trapezoidal" requires "lower_base", "upper_base", "height", and height
              direction "dx","dy","dz".

    radius : float, optional
            In case of "circular" section_type, the radius of the cross section.

    width : float, optional
            In case of "square" section_type, the width of the cross section.

    dx : float, optional
            In case of "square", "rectangular" or "trapezoidal" section_type,
            the x-component of the vector defining the section's height direction.
            (Does not need to be normalized)

    dy : float, optional
            In case of "square", "rectangular" or "trapezoidal" section_type,
            the y-component of the vector defining the section's height direction.
            (Does not need to be normalized)

    dz : float, optional
            In case of "square", "rectangular" or "trapezoidal" section_type,
            the z-component of the vector defining the section's height direction.
            (Does not need to be normalized)

    height : float, optional
            In case of "rectangular" or "trapezoidal" section_type, the height
            of the cross section.

    lower_base : float, optional
            In case of "trapezoidal" section_type, the length of the sections' lower base.

    upper_base : float, optional
            In case of "trapezoidal" section_type, the length of the sections' upper base.

    Returns
    -------
    object
            Returns a reference to the newly created Hexablock boxes objects.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            # -Example using a box face:
            def main():
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 907))
                face = base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 12)
                Box = mesh.HexaBoxSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, box_face=face
                )


            # -Example using curves:
            def main():
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 1069))
                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 1327))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 809))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 564))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 895))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 1325))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 931))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 573))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 837))
                Box = mesh.HexaBoxSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, curves=curves
                )


            # -Example using curves and points:
            def main():
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 813))
                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 5))
                curves.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 6))
                curves.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 7))
                curves.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 8))
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 26))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 35))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 36))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 40))
                Box = mesh.HexaBoxSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, points=points, curves=curves
                )


    """


def VoxelGeneration(
    shells_or_faces: object,
    voxel_len: float,
    allow_surface_intersection: bool,
    nth_largest: int,
    ret_ents: bool,
    different_properties_per_volume: bool,
    smooth_iterations: int,
    mesh_method: str,
    sharp_angle: float,
    coordinate_sys: object,
) -> int:
    """

    Creates a mesh around or inside a solid description of faces or shells.

    Parameters
    ----------
    shells_or_faces : object
            A list of faces/shells. If set to "visible" then it runs for all
            the visible faces/shells of the database.

    voxel_len : float
            The length of the created voxels (> 0).

    allow_surface_intersection : bool, optional
            Set to True, to capture the volume around the solid description.
            Set to False, to capture the volume on the interior.

    nth_largest : int, optional
            Create the nth largest volumes that will be detected.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    different_properties_per_volume : bool, optional
            If set to True, the algorithm will see existing ANSA volumes and
            will create separate properties per volume for the result .

    smooth_iterations : int, optional
            The number of iterations for hexas smoothing. This option is used only in "Free" mesh method.

    mesh_method : str, optional
            Defines the method for the mesh generation.
            Available options are "Free" and "Snap".
            - "Free" creates a smooth voxel mesh.
            - "Snap" creates a voxel mesh that will be snapped to the model.
            Default option is "Free"

    sharp_angle : float, optional
            Sharp angle defines a limit for the angle between two adjacent shells above which their common edge will be identified as sharp and the mesh will try to capture it. This option is used only in "Snap" mesh method.
            Set to 0 to deactivate it.
            Default value is 0.

    coordinate_sys : object, optional
            Coordinate system entity (CS) to align voxel mesh to.
            If value 'auto' is set, the voxel mesh will be alligned to an automatically calculated coordinate system.
            By default it is deactivated and global CS will be used.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                result = mesh.VoxelGeneration("visible", 5.0, True, 1, smooth_iterations=5)


    """


def RemeshShells(shells: object, mesh_generator: str) -> object:
    """

    This function runs mesh generators on shells.
    It uses mesh parameters to get critiria like mesh type and order of mesh.
    Also It seperates input shells to different areas according to geometry
    masegments or feature lines if shells are fe.

    Parameters
    ----------
    shells : object
            A list of shell objects or a string with value 'visible'.
            If it is called with 'visible' it works for all the visible shell elements.

    mesh_generator : str
            The mesh generator to run.
            Options are "CFD", "ADVFRNT", "FREE", "SPOT" or "GRADUAL".

    Returns
    -------
    object
            Returns a list containing references to all the new shell objects.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                all_shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.RemeshShells(all_shells, "FREE")


    """


def PerimetersOfMacro(faces: object) -> object:
    """

    The function collects all the Perimeters of a macro. If a face that it not a macro is
    provided, the function returns the perimeters of its macro.

    Parameters
    ----------
    faces : object
            A list of faces, parts or properties.

    Returns
    -------
    object
            Returns a list with the collected Perimeters, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Need some documentation? Run this with F5
                face = base.GetEntity(constants.NASTRAN, "FACE", 1)
                perims = mesh.PerimetersOfMacro(face)
                mesh.NumberPerimeters(perims, "*3")


    """


def FillGapFitted(
    input: object, improve_result_zones: int, result_set_id: int, ret_ents: bool
) -> int:
    """

    This function creates FE shells to fill a gap defined by cons, curves or edges.
    Each call of the function fills a single gap.

    Parameters
    ----------
    input : object
            A list of cons, curves or sets of edges.

    improve_result_zones : int, optional
            Improves the quality of the result FE shells and [user defined] zones
            around them.

    result_set_id : int, optional
            Adds the result FE shells to a set with [user defined] id.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns the number of the created FE shells (before mesh improvement).
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Check how the syntax in each case should be
                input = []
                input.append(base.GetEntity(constants.NASTRAN, "CONS", 1923054))
                input.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                input.append(base.GetEntity(constants.NASTRAN, "SET", 1))
                mesh.FillGapFitted(input, improve_result_zones=0, result_set_id=5)


    """


def FillGapPlanar(
    input: object, improve_result_zones: int, result_set_id: int, ret_ents: bool
) -> int:
    """

    This function creates FE shells to fill a gap defined by cons, curves or edges.
    Each call of the function fills a single gap.

    Parameters
    ----------
    input : object
            A list of cons, curves or sets of edges.

    improve_result_zones : int, optional
            Improves the quality of the result FE shells and [user defined] zones
            around them.

    result_set_id : int, optional
            Adds the result FE shells to a set with [user defined] id.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns the number of the created FE shells (before mesh improvement).
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Check how the syntax in each case should be
                input = []
                input.append(base.GetEntity(constants.NASTRAN, "CONS", 1923054))
                input.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                input.append(base.GetEntity(constants.NASTRAN, "SET", 1))
                mesh.FillGapPlanar(input, improve_result_zones=0, result_set_id=5)


    """


def ReconstructViolatingShells(expand_level: int) -> int:
    """

    The function perfrorms Reconstruct on violating shells.

    Parameters
    ----------
    expand_level : int, optional
            The number of zones around violating shells.
            (Default: 0)

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReconstructViolatingShells(3)


    """


def ReshapeViolatingShells(expand_level: int) -> int:
    """

    The function perfrorms Reshape on violating shells.

    Parameters
    ----------
    expand_level : int, optional
            The number of zones around violating shells.
            (Default: 0)

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReshapeViolatingShells(3)


    """


def FillSingleBoundHoles(
    max_diameter: float,
    fill_ext_perim: bool,
    point_at_center: bool,
    connection_by: str,
    curve_at_perimeter: bool,
    reshape_zones: int,
    set_id: object,
    pid_id: object,
    ret_ents: bool,
    fill_method: str,
    part: object,
    geom_fill_method: str,
) -> int:
    """

    This function identifies and fills single bound holes with FE shells or faces.
    Works on visible shells and macros.

    Parameters
    ----------
    max_diameter : float
            The maximum diameter of the holes that will be filled.

    fill_ext_perim : bool
            Fill the largest perimeter of each connectivity group.

    point_at_center : bool, optional
            Create points at hole centers.

    connection_by : str, optional
            Create connection points at hole centers. Can be "PID" or "Module_ID".

    curve_at_perimeter : bool, optional
            Create curves at hole perimeters.

    reshape_zones : int, optional
            Defines the zones of shells around the holes that will be reshaped.

    set_id : object, optional
            Adds the new shells/faces to a set. If None, a new set will be created by ANSA.

    pid_id : object, optional
            Adds the new shells/faces to a pid. If None, a new pid will be created by ANSA.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    fill_method : str, optional
            Defines the triangulation method for FE holes. Can be "draft", "planar" or "bridge".
            (Default: "draft")

    part : object, optional
            Adds the new shells/faces to a part.

    geom_fill_method : str, optional
            Defines the fill method for geom holes.
            Can be "draft", "planar", "create_new_faces" or "expand_existing_faces".
            (Default: "create_new_faces")

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                part = base.CreateEntity(constants.NASTRAN, "ANSAPART", {"Name": "new part"})
                mesh.FillSingleBoundHoles(
                    200,
                    False,
                    point_at_center=True,
                    connection_by="pid",
                    curve_at_perimeter=True,
                    reshape_zones=2,
                    set_id=1,
                    pid_id=1,
                    fill_method="planar",
                    part=part,
                    geom_fill_method="expand_existing_faces",
                )


    """


def FillSingleBoundConcavities(
    max_width: float,
    point_at_center: bool,
    curve_at_perimeter: bool,
    reshape_zones: int,
    set_id: object,
    pid_id: object,
    ret_ents: bool,
    part: object,
) -> object:
    """

    This function identifies and fills concavities along single bound perimeters.
    Works on visible FE shells and meshed macros.

    Parameters
    ----------
    max_width : float
            The maximum width of the concavities that will be filled.

    point_at_center : bool, optional
            Create points at concavity centers.

    curve_at_perimeter : bool, optional
            Create curves at concavity perimeters.

    reshape_zones : int, optional
            Defines the zones of shells around the filled concavities that will be reshaped.

    set_id : object, optional
            Adds the new shells to a set. If None, a new set will be created by ANSA.

    pid_id : object, optional
            Adds the new shells to a pid. If None, a new pid will be created by ANSA.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    part : object, optional
            Adds the new shells to a part.

    Returns
    -------
    object
            Returns 1 on success and 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                part = base.CreateEntity(constants.NASTRAN, "ANSAPART", {"Name": "part"})
                mesh.FillSingleBoundConcavities(
                    200,
                    point_at_center=True,
                    curve_at_perimeter=True,
                    reshape_zones=2,
                    set_id=1,
                    pid_id=1,
                    part=part,
                )


    """


def FillSolidHoles(
    max_diameter: float,
    feat_angle: float,
    feat_type: str,
    max_distortion: float,
    point_at_center: bool,
    curve_at_perimeter: bool,
    reshape_zones: int,
    set_id: object,
    pid_id: object,
    ret_ents: bool,
    fill_method: str,
    part: object,
    solids_set: object,
    solids_pid: object,
    solids_part: object,
    geom_fill_method: str,
) -> int:
    """

    This function identifies and fills tubes and blind concavities. Works on visible shells and solids.

    Parameters
    ----------
    max_diameter : float
            The maximum diameter of the solid holes that will be filled.

    feat_angle : float
            Defines the feature line angle.

    feat_type : str
            Defines the type of features that will be identified.
            Can be "convex" or "concave".

    max_distortion : float
            The maximum allowed distance between perimeter nodes and the hole's mid plane,
            given as a percentage of the hole's diameter.

    point_at_center : bool, optional
            Create points at hole centers.

    curve_at_perimeter : bool, optional
            Create curves at hole perimeters.

    reshape_zones : int, optional
            Defines the zones of shells around the holes that will be reshaped.

    set_id : object, optional
            Adds the new shells/faces to a set. If None, a new set will be created by ANSA.

    pid_id : object, optional
            Adds the new shells/faces to a pid. If None, a new pid will be created by ANSA.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    fill_method : str, optional
            Defines the triangulation method for FE holes. Can be "draft" or "planar".
            (Default: "draft")

    part : object, optional
            Adds the new shells/faces to a part.

    solids_set : object, optional
            Adds the new solids to a set.

    solids_pid : object, optional
            Adds the new solids to a pid.

    solids_part : object, optional
            Adds the new solids to a part.

    geom_fill_method : str, optional
            Defines the fill method for geom holes.
            Can be "draft", "planar", "create_new_faces" or "expand_existing_faces".
            (Default: "create_new_faces")

    Returns
    -------
    int
            Rreturns 1 on success and 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                shells_or_faces_part = base.CreateEntity(
                    constants.NASTRAN, "ANSAPART", {"Name": "shells part"}
                )
                solids_part = base.CreateEntity(
                    constants.NASTRAN, "ANSAPART", {"Name": "solids part"}
                )
                solids_set = base.CreateEntity(constants.NASTRAN, "SET", {"Name": "solids set"})
                solids_pid = base.CreateEntity(constants.NASTRAN, "PSOLID", {"Name": "solids pid"})
                mesh.FillSolidHoles(
                    200,
                    40,
                    "convex",
                    5,
                    point_at_center=True,
                    curve_at_perimeter=True,
                    set_id=1,
                    pid_id=1,
                    reshape_zones=2,
                    fill_method="planar",
                    part=shells_or_faces_part,
                    solids_set=solids_set,
                    solids_pid=solids_pid,
                    solids_part=solids_part,
                    geom_fill_method="expand_existing_faces",
                )


    """


def FillFeatureLineHoles(
    max_diameter: float,
    feat_angle: float,
    feat_type: str,
    max_distortion: float,
    detach_triple_perimeters: bool,
    point_at_center: bool,
    curve_at_perimeter: bool,
    reshape_zones: int,
    set_id: object,
    pid_id: object,
    ret_ents: bool,
    fill_method: str,
    part: object,
    allow_intersecting_result_shells: bool,
) -> int:
    """

    This function identifies and fills feature line holes. Works on visible FE shells and meshed macros.

    Parameters
    ----------
    max_diameter : float
            The maximum diameter of the solid holes that will be filled.

    feat_angle : float
            Defines the feature line angle.

    feat_type : str
            Defines the type of features that will be identified.
            Can be "convex" or "concave".

    max_distortion : float
            The maximum allowed distance between perimeter nodes and the
            hole's mid plane, given as a percentage of the hole's diameter.

    detach_triple_perimeters : bool, optional
            Detaches triple bounds at hole perimeters, to create a manifold result mesh.

    point_at_center : bool, optional
            Create points at hole centers.

    curve_at_perimeter : bool, optional
            Create curves at hole perimeters.

    reshape_zones : int, optional
            Defines the zones of shells around the holes that will be reshaped.

    set_id : object, optional
            Adds the new shells to a set. If None, a new set will be created by ANSA.

    pid_id : object, optional
            Adds the new shells to a pid. If None, a new pid will be created by ANSA.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    fill_method : str, optional
            Defines the triangulation method. Can be "draft" or "planar".
            (Default: "draft")

    part : object, optional
            Adds the new shells to a part.

    allow_intersecting_result_shells : bool, optional
            Option to allow intersections between the created shells and the existing shells/faces.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                part = base.CreateEntity(constants.NASTRAN, "ANSAPART", {"Name": "new part"})
                mesh.FillFeatureLineHoles(
                    200,
                    40,
                    "convex",
                    5,
                    detach_triple_perimeters=True,
                    point_at_center=True,
                    curve_at_perimeter=True,
                    reshape_zones=2,
                    set_id=1,
                    pid_id=1,
                    fill_method="planar",
                    part=part,
                )


    """


def SuppressFeatureLines(
    feature_angle_limit: float, max_dist_from_prev_pos: float, shells: object
) -> int:
    """

    SuppressFeatureLines performs suppress on the visible model.

    Parameters
    ----------
    feature_angle_limit : float
            The maximum feature angle allowed after suppress has taken place.

    max_dist_from_prev_pos : float
            The maximum node from the node's previous position.

    shells : object, optional
            The shells on which the function will work. Can be an object, a list of objects, parts, properties, materials, sets or macros. If this argument is ommitted the function is performed on the visible shells

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SuppressFeatureLines(20, -1)


    """


def ReduceMesh(
    shells: object,
    reduce_percentage: float,
    distortion: float,
    maximum_length: float,
    maximum_aspect: float,
    distortion_angle: float,
) -> int:
    """

    Reduces the number of elements by a distortion value.

    Parameters
    ----------
    shells : object
            A list of shell entities. Set 0 to work on visible.

    reduce_percentage : float
            Maximum percentage of shells number to reduce.

    distortion : float
            The distortion value.

    maximum_length : float, optional
            Maximum allowed element length.

    maximum_aspect : float, optional
            Maximum allowed element aspect.

    distortion_angle : float, optional
            The distortion angle value.

    Returns
    -------
    int
            Returns 1 on success.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReduceMesh(shells, 100.0, 0.2)


    """


def AssociateBoxEdgesToEdges(
    box_edges: object,
    target_edges: object,
    connect_to_cons: bool,
    remove_points: bool,
    box_edge_points: object,
) -> int:
    """

    Script function to associate box edges to target feature lines (curves, cons, shell edges).

    Parameters
    ----------
    box_edges : object
            A box edge or a list of box edges to be associated with the target entities.

    target_edges : object
            An entity or a list of entities, parts or sets corresponding
            to the target feature lines.

    connect_to_cons : bool, optional
            If set to True,  connect the nodes of the box edges to the associated Cons,
            after meshing the boxes.

    remove_points : bool, optional
            Remove the existing control points from the box edges.

    box_edge_points : object, optional
            A dictionary to define the number of points per box edge.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    AssociateBoxEdgesToSurfs

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def associateBoxEdgesToTargetEdges():
                edges = []
                edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 253))
                edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 254))
                edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 256))
                edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 309))

                target_edges = []
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 10))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 16))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 17))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 21))

                mesh.AssociateBoxEdgesToEdges(edges, target_edges, False)


            def associateBoxEdgesToTargetEdges_points_num():
                edges = []
                edges.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 15))
                target_edges = []
                target_edges.append(base.GetEntity(base.CurrentDeck(), "CONS", 14))
                target_edges.append(base.GetEntity(base.CurrentDeck(), "CONS", 21))
                box_edge_points = {}
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 15)] = 13
                mesh.AssociateBoxEdgesToEdges(
                    box_edges=edges,
                    target_edges=target_edges,
                    connect_to_cons=False,
                    remove_points=False,
                    box_edge_points=box_edge_points,
                )


    """


def AssociateBoxEdgesToSurfs(
    box_edges: object,
    surface_ents: object,
    user_projection_mode_vector: object,
    remove_points: bool,
    box_edge_points: object,
    cut_geometric_faces: bool,
    connect_to_cons: bool,
) -> int:
    """

    Script function to associate box edges to target surface entities (shells, geometrical faces).

    Parameters
    ----------
    box_edges : object
            A box edge or a list of box edges to be associated with target entities.

    surface_ents : object
            An entity or a list of entities, properties, materials, parts or sets
            corresponding to the target surface entities.

    user_projection_mode_vector : object, optional
            A projection vector.

    remove_points : bool, optional
            If set to True, remove existing control points from box edges.

    box_edge_points : object, optional
            A dictionary to define the number of points per box edge.

    cut_geometric_faces : bool, optional
            If it set to True, target geometric faces will be cut
            on the position of the input box edges (after projecting
            them to the geometric faces). Default value is False.

    connect_to_cons : bool, optional
            If set to True,  connect the nodes of the box edges to the
            created Cons (used only if argument cut_geometric_faces
            is set to True)

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    AssociateBoxEdgesToEdges

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                box_edges = []
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 299))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 300))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 311))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 312))

                surface_ents = base.CollectEntities(constants.NASTRAN, None, "FACE")

                vec = [0.0, 0.0, 1.0]
                mesh.AssociateBoxEdgesToSurfs(box_edges, surface_ents, vec)


            def associateBoxEdgeToSurfEnts():
                box_edges = []
                box_edges.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 17))
                surface_ents = []
                surface_ents.append(base.GetEntity(base.CurrentDeck(), "FACE", 5))
                surface_ents.append(base.GetEntity(base.CurrentDeck(), "FACE", 9))
                box_edge_points = {}
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 17)] = 11
                mesh.AssociateBoxEdgesToSurfs(
                    box_edges=box_edges,
                    surface_ents=surface_ents,
                    remove_points=False,
                    box_edge_points=box_edge_points,
                )


    """


def AssociateBoxFacesToSurfs(
    box_faces: object,
    surface_ents: object,
    user_projection_mode_vector: object,
    remove_points: bool,
    box_edge_points: object,
) -> int:
    """

    Script function to associate box faces to target surface entities (shells, geometrical faces).

    Parameters
    ----------
    box_faces : object
            A box face or a list of box faces to be associated with target entities.

    surface_ents : object
            An entity or a list of entities, properties, materials, parts or sets corresponding
            to the target surface entities.

    user_projection_mode_vector : object, optional
            A projection vector.

    remove_points : bool, optional
            If set to True, remove existing control points from box edges.

    box_edge_points : object, optional
            A dictionary to define the number of points per box edge.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 150))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 156))

                surface_ents = base.CollectEntities(constants.NASTRAN, None, "FACE")
                vec = [0.0, 0.0, 1.0]
                mesh.AssociateBoxFacesToSurfs(box_faces, surface_ents, vec)


            def associateBoxFaceToSurfEnts():
                box_faces = []
                box_faces.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_FACE", 11))
                surface_ents = []
                surface_ents.append(base.GetEntity(base.CurrentDeck(), "FACE", 5))
                surface_ents.append(base.GetEntity(base.CurrentDeck(), "FACE", 9))
                box_edge_points = {}
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 22)] = 2
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 21)] = 2
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 37)] = 13
                box_edge_points[base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 13)] = 13
                mesh.AssociateBoxFacesToSurfs(
                    box_faces=box_faces,
                    surface_ents=surface_ents,
                    remove_points=False,
                    box_edge_points=box_edge_points,
                )


    """


def AssociateBoxPointsToEdges(
    box_points: object, target_edges: object, insert_hot_point: bool
) -> int:
    """

    Script function to associate box points to target feature lines (curves, cons, shell edges).

    Parameters
    ----------
    box_points : object
            A box point or a list of box points to be associated with the target entities.

    target_edges : object
            An entity or a list of entities, parts or sets corresponding to the target feature lines.

    insert_hot_point : bool, optional
            If it set to True, hot points will be inserted on the position of
            the projection to the target Cons. Default value is False.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def associateBoxPointsToEdges():
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 780))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 781))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 888))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 889))

                target_edges = []
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 10))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 16))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 17))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CONS", 21))

                mesh.AssociateBoxPointsToEdges(points, target_edges)


    """


def AssociateBoxPointsToPoints(box_points: object, target_points: object) -> int:
    """

    Script function to associate box points to target points. The maximum number of points equals 4.

    Parameters
    ----------
    box_points : object
            A box point or a list of box points to be associated with target entities.

    target_points : object
            An entity or a list of entities, parts or sets corresponding to the target points.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 865))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 866))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 892))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 893))

                target_set = base.GetEntity(constants.NASTRAN, "SET", 3)

                mesh.AssociateBoxPointsToPoints(points, target_set)


    """


def AssociateBoxPointsToSurfs(
    box_points: object, surface_ents: object, user_projection_mode_vector: object
) -> int:
    """

    Script function to associate box points to target surface entities (shells, geometrical faces).

    Parameters
    ----------
    box_points : object
            A box point or a list of box points to be associated with target
            entities.

    surface_ents : object
            An entity or a list of entities, properties, materials, parts or sets
            corresponding to the target surface entities.

    user_projection_mode_vector : object, optional
            A projection vector.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                box_points = []
                box_points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 852))
                box_points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 869))
                box_points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 888))
                box_points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 889))

                surface_ents = base.CollectEntities(constants.NASTRAN, None, "FACE")

                vec = [0.0, 0.0, 1.0]
                mesh.AssociateBoxPointsToSurfs(box_points, surface_ents, vec)


    """


def EraseBoxEdgesAssociation(box_edges: object) -> int:
    """

    This function erases association from box edges.

    Parameters
    ----------
    box_edges : object
            A box edge or list of box edges to remove association.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def eraseBoxEdgesAssociation():
                # erase association from all database box edges
                box_edges = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX_EDGE")
                mesh.EraseBoxEdgesAssociation(box_edges)


    """


def EraseBoxFacesAssociation(box_faces: object) -> int:
    """

    This function erases association from box faces.

    Parameters
    ----------
    box_faces : object
            A box face or list of box faces to remove association.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def eraseBoxFacesAssociation():
                # erase association from all database box faces
                box_faces = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX_FACE")
                mesh.EraseBoxFacesAssociation(box_faces)


    """


def EraseBoxPointsAssociation(box_points: object) -> int:
    """

    This function erases association from box points.

    Parameters
    ----------
    box_points : object
            A box point or list of box points to remove association.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def eraseBoxPointsAssociation():
                # erase association from all database box points
                box_points = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX_POINT")
                mesh.EraseBoxPointsAssociation(box_points)


    """


def ZoneCutGradual(
    input: object,
    first_height_value: float,
    first_height_mode: str,
    growth_factor: float,
    number: int,
    max_aspect: float,
    separate_angle: float,
    connect_angle: float,
    regenerate_macro_shells: bool,
    element_type: str,
    expand_level: int,
    smooth_zones: str,
    proximity_distance_value: float,
    proximity_distance_mode: str,
    cut_faces_on_zones: bool,
    zones_set_id: int,
    join_obstructing_perimeters: bool,
) -> int:
    """

    This function creates zones with gradual width around element edges.

    Parameters
    ----------
    input : object
            A list of sets of edges, sets of CONS, and CONS.

    first_height_value : float
            The value of the first height.

    first_height_mode : str
            The type of first height, "Absolute" or "Relative".

    growth_factor : float
            The growth factor of the consecutive zones to create.

    number : int
            The number of the zones to create.

    max_aspect : float, optional
            The maximum allowed element aspect (height / base length).
            (Default: 0.4)

    separate_angle : float, optional
            The angle that determines the separation of a layer.
            (Default: 90)

    connect_angle : float, optional
            The angle that determines the connection of a layer with perimeters.
            (Default: 60)

    regenerate_macro_shells : bool, optional
            Option to regenerate macro shells. Enabled by default.

    element_type : str, optional
            "Quad" or "Tria". Option to create tria zone elements, for tria mesh only.
            (Default: "Quad")

    expand_level : int, optional
            The number of expanding shells zones added around selected edges.
            (Default: 1)

    smooth_zones : str, optional
            The option to smooth the created zones.
            Acceptable values: "Full", "Semi", "Off".
            (Default: "Full")

    proximity_distance_value : float, optional
            The  allowed distace for the proximity gap.
            (Default: 1)

    proximity_distance_mode : str, optional
            The mode of the proximity distance.
            Acceptable values: "*last height", "*local height", "*min length", " ".
            (Default: "*last height")

    cut_faces_on_zones : bool, optional
            Option to cut faces on last zone. Disabled by default.

    zones_set_id : int, optional
            Adds the result zone shells to a set with [user defined] id.
            Not used by default.

    join_obstructing_perimeters : bool, optional
            An option to join perimeters that obstruct the creation of zones.
            Disabled by default.

    Returns
    -------
    int
            Returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                input = list()
                input.append(base.GetEntity(ansa.constants.NASTRAN, "SET", 1))

                first_height_value = 0.1
                first_height_mode = "Absolute"
                growth_factor = 1.2
                number = 5

                mesh.ZoneCutGradual(
                    input,
                    first_height_value,
                    first_height_mode,
                    growth_factor,
                    number,
                    expand_level=2,
                )


    """


def ZoneCutSpecificWidth(
    input: object,
    zones_offset: object,
    radial_offset: bool,
    blended: bool,
    expand_level: int,
    smooth_zones: str,
    proximity_distance_value: float,
    proximity_distance_mode: str,
    cut_faces_on_zones: bool,
    zones_set_id: int,
    join_obstructing_perimeters: bool,
) -> int:
    """

    This function creates zones with specific width around element edges.

    Parameters
    ----------
    input : object
            A list of sets of edges, sets of CONS and CONS.

    zones_offset : object
            A list of the width of each zone to create.

    radial_offset : bool, optional
            An option to define zones width by radial distance.
            (Default: False)

    blended : bool, optional
            An option to create blended zones.
            (Default: False)

    expand_level : int, optional
            The number of expanding shells zones added around selected edges.
            (Default: 1)

    smooth_zones : str, optional
            The option to smooth the created zones.
            Acceptable values: "Full", "Semi", "Off".
            (Default: "Full")

    proximity_distance_value : float, optional
            The allowed distace for the proximity gap.
            (Default: 1)

    proximity_distance_mode : str, optional
            The mode of the proximity distance.
            Acceptable values: "*last height", "*local height", "*min length", " ".
            (Default: "*last height")

    cut_faces_on_zones : bool, optional
            An option to cut faces on last zone.
            (Default: False)

    zones_set_id : int, optional
            Adds the result zone shells to a set with [user defined] id.
            Not used by default.

    join_obstructing_perimeters : bool, optional
            An option to join perimeters that obstruct the creation of zones.
            (Default: False)

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                input = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                zones = [2, 3]

                mesh.ZoneCutSpecificWidth(input, zones, expand_level=2, cut_faces_on_zones=True)


    """


def HexaBlockDeleteVolume(boxes: object) -> int:
    """

    Script function to delete volumes of hexa block boxes.

    Parameters
    ----------
    boxes : object
            A box or a list of boxes to delete their volumes.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                # delete volume of box id 9
                box = base.GetEntity(constants.NASTRAN, "HEXA_BOX", 9)
                mesh.HexaBlockDeleteVolume(box)

                # delete volumes of all hexa block boxes of the database
                boxes = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX")
                mesh.HexaBlockDeleteVolume(boxes)


    """


def HexaBlockEraseShellMesh(box_faces: object) -> int:
    """

    Script function to erase shell mesh from box faces.

    Parameters
    ----------
    box_faces : object
            A box face or a list of box faces to erase shell mesh.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                # erase shell mesh of every hexa block face of the database
                box_faces = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX_FACE")
                mesh.HexaBlockEraseShellMesh(box_faces)


    """


def HexaBlockEraseVolumeMesh(boxes: object) -> int:
    """

    Script function to erase volume mesh from hexa block boxes.

    Parameters
    ----------
    boxes : object
            A box or a list of boxes to erase volume mesh.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                # erase volume mesh of hexa block boxes of the database
                boxes = base.CollectEntities(constants.NASTRAN, None, "HEXA_BOX")
                mesh.HexaBlockEraseVolumeMesh(boxes)


    """


def HexaBlockShellMesh(
    box_faces: object,
    tolerance: str,
    project: bool,
    generator: str,
    apply_surface_fit: bool,
    project_non_associated: bool,
) -> object:
    """

    Function to generate the shell mesh for input box_faces.

    By default, the "Map" algorithm is used for the mesh generation and "project",
    "tolerance" values are defined by ANSA defaults.

    box_faces: object Box faces or list of box faces to generate shell mesh.
    If box_faces equals 0, mesh is generated for all visible box faces.

    tolerance (optional): string String defining projection tolerance. String may contain
    a real value (eg. "0.05"), or an expression (eg. "0.05*Lmin", where Lmin is the minimum
    length defined on box edges)

    project (optional): boolean Flag that defines, whether to project (True) or not
    (False) on geometry

    Parameters
    ----------
    box_faces : object
            A box face or a list of box faces to generate the shell mesh.
            If box_faces equals to 0, mesh is generated for all visible box faces.

    tolerance : str, optional
            Defines the projection tolerance. The string may contain a
            real value (eg. "0.05"), or an expression (eg. "0.05*Lmin",
            where Lmin is the minimum length defined on box edges).

    project : bool, optional
            A flag that defines whether to project (True) or not (False) on geometry.

    generator : str, optional
            Definition of the meshing algorithm to be used.
            This value should be one of: "Map", "Free", "Spot Mesh",
            "Advancing Front" or "CFD".
            (Default: "Map"(Algorithm to be used))

    apply_surface_fit : bool, optional
            A flag that defines if surface-fit will be applied for
            fully associated box faces (box faces with points,
            edges and face association).

    project_non_associated : bool, optional
            A flag that defines if nodes of non-associated box
            faces will be projected on the geometry.

    Returns
    -------
    object
            Returns a list containing the generated shells on success, None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                # mesh hexa block face 52 with "Map" algorithm, using ANSA defaults values for projection and tolerance
                box_faces1 = []
                box_faces1.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 52))
                mesh.HexaBlockShellMesh(box_faces1)

                # mesh hexa block face 55 with "Free" algorithm, using ANSA defaults values for projection and tolerance
                box_faces2 = []
                box_faces2.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 55))
                mesh.HexaBlockShellMesh(box_faces2, generator="Free")

                # mesh hexa block face 65 with "Spot Mesh" algorithm, using projection and tolerance equal
                # to "0.01*Lmin", where Lmin is the minimum length defined on box edges
                box_faces3 = []
                box_faces3.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 65))
                mesh.HexaBlockShellMesh(
                    box_faces3, generator="Spot Mesh", project=True, tolerance="0.01*Lmin"
                )

                # mesh hexa block face 75 with "CFD" algorithm, using projection and tolerance equal to "0.01"
                box_faces4 = []
                box_faces4.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 75))
                mesh.HexaBlockShellMesh(
                    box_faces4, generator="Free", project=True, tolerance="0.01"
                )

                # mesh hexa block face 2 with "Free" algorithm, using ANSA defaults values for projection and tolerance
                box_faces5 = []
                box_faces5.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_FACE", 2))
                ansa.mesh.HexaBlockShellMesh(
                    box_faces=box_faces5,
                    generator="Free",
                    apply_surface_fit=True,
                    project_non_associated=True,
                )


    """


def VolumesGlide(
    boundary_array: object,
    guideline_array: object,
    distribution: str,
    paste_nodes: int,
    paste_distance: float,
    steps_type: str,
    steps: int,
    element_length: float,
    biasing: str,
    factor: float,
    reference_point: str,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume by gliding a predefined shell mesh along a given guideline.

    Parameters
    ----------
    boundary_array : object
            The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

    guideline_array : object
            The guideline that defines the direction of the extrusion.
            Elements could be Perimeters, Edges or curves.

    distribution : str
            Defines if the extrusion will use the guideline distribution or
            if the user will define it.
            Accepted values: "Guideline", "User defined".

    paste_nodes : int
            Defines if the created nodes along guideline will be pasted on guideline
            within a paste_distance.
            Accepted values: 0, 1.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    paste_distance : float
            The nodes along guideline and extrusion will be pasted under this tolerance.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    steps_type : str
            Defines if the user will set steps or element length for the extrusion.
            Accepted values: "Steps", "Element length".
            Works only if distribution is set to "User defined", otherwise set to zero.

    steps : int
            The number of the desired steps for the extrusion.
            Works only if distribution is set to "User defined", otherwise set to zero.

    element_length : float
            The height of the elements in every step.

    biasing : str
            Defines a biasing in the extrusion according to a factor.
            Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

    factor : float
            The factor of the biasing.

    reference_point : str
            Defines if the extrusion will start from the surface or the guideline.
            Accepted values: "On surface", "On guideline".

    part : object, optional
            Default values will be used if they are omitted.

    property : object, optional
            Default values will be used if they are omitted.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                all_curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                if len(all_faces) and len(all_curves):
                    mesh.VolumesGlide(
                        all_faces,
                        all_curves,
                        "User defined",
                        0,
                        0.0,
                        "Steps",
                        10,
                        0.0,
                        "No Biasing",
                        1.2,
                        "On surface",
                    )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def VolumesSweep(
    boundary_array: object,
    guideline_array: object,
    distribution: str,
    paste_nodes: int,
    paste_distance: float,
    steps_type: str,
    steps: int,
    element_length: float,
    biasing: str,
    factor: float,
    reference_point: str,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume by sweeping a predefined shell mesh along a given guideline.

    Parameters
    ----------
    boundary_array : object
            The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

    guideline_array : object
            The guideline that defines the direction of the extrusion.
            Elements could be Perimeters, Edges or curves.

    distribution : str
            Defines if the extrusion will use the guideline distribution or
            if the user will define it.
            Accepted values: "Guideline", "User defined".

    paste_nodes : int
            Defines if the created nodes along guideline will be pasted on guideline
            within a paste_distance.
            Accepted values: 0, 1.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    paste_distance : float
            The nodes along guideline and extrusion will be pasted under this tolerance.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    steps_type : str
            Defines if the user will set steps or element length for the extrusion.
            Accepted values: "Steps", "Element length".
            Works only if distribution is set to "User defined", otherwise set to zero.

    steps : int
            The number of the desired steps for the extrusion.
            Works only if distribution is set to "User defined", otherwise set to zero.

    element_length : float
            The height of the elements in every step.

    biasing : str
            Defines a biasing in the extrusion according to a factor.
            Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

    factor : float
            The factor of the biasing.

    reference_point : str
            Defines if the extrusion will start from the surface or the guideline.
            Accepted values: "On surface", "On guideline".

    part : object, optional
            Default values will be used if they are omitted.

    property : object, optional
            Default values will be used if they are omitted.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                all_curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                if len(all_faces) and len(all_curves):
                    mesh.VolumesSweep(
                        all_faces,
                        all_curves,
                        "User defined",
                        0,
                        0.0,
                        "Steps",
                        10,
                        0.0,
                        "No Biasing",
                        1.2,
                        "On surface",
                    )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def VolumesDualSweep(
    boundary_array: object,
    guideline1_array: object,
    guideline2_array: object,
    distribution: str,
    paste_nodes: int,
    paste_distance: float,
    steps_type: str,
    steps: int,
    element_length: float,
    biasing: str,
    factor: float,
    reference_point: str,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 19.0.0
            Use :py:class:`VolumesExtrude` instead.


    This function can be used in order to generate a volume, by sweeping a predefined shell mesh along two given guidelines.

    Parameters
    ----------
    boundary_array : object
            The shell mesh that will be extruded. Elements could be Faces, Shells or Facets.

    guideline1_array : object
            The guideline that defines the direction of the extrusion.
            Elements could be Perimeters, Edges or curves.

    guideline2_array : object
            The guideline that defines the rotation of the extrusion along the direction.
            Elements could be Perimeters, Edges or curves.

    distribution : str
            Defines if the extrusion will use the guideline distribution or
            if the user will define it.
            Accepted values: "Guideline", "User defined".

    paste_nodes : int
            Defines if the created nodes along guideline will be pasted on guideline
            within a paste_distance.
            Accepted values: 0, 1.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    paste_distance : float
            The nodes along guideline and extrusion will be pasted under this tolerance.
            Works only if distribution is set to "Guideline", otherwise set to zero.

    steps_type : str
            Defines if the user will set steps or element length for the extrusion.
            Accepted values: "Steps", "Element length".
            Works only if distribution is set to "User defined", otherwise set to zero.

    steps : int
            The number of the desired steps for the extrusion.
            Works only if distribution is set to "User defined", otherwise set to zero.

    element_length : float
            The height of the elements in every step.

    biasing : str
            Defines a biasing in the extrusion according to a factor.
            Accepted values: "Linear", "Exponential", "Bell Curve", "No Biasing".

    factor : float
            The factor of the biasing.

    reference_point : str
            Defines if the extrusion will start from the surface or the guideline.
            Accepted values: "On surface", "On guideline".

    part : object, optional
            Default values will be used if they are omitted.

    property : object, optional
            Default values will be used if they are omitted.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                guideline1 = [base.GetEntity(constants.NASTRAN, "CURVE", 58)]
                guideline2 = [base.GetEntity(constants.NASTRAN, "CURVE", 57)]

                if len(all_faces) and len(guideline1) and len(guideline2):
                    mesh.VolumesDualSweep(
                        all_faces,
                        guideline1,
                        guideline2,
                        "User defined",
                        0,
                        0.0,
                        "Steps",
                        100,
                        0.0,
                        "No Biasing",
                        1.2,
                        "On surface",
                    )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def IsolateWashers(shells: object, include_filled_connection_holes: bool) -> object:
    """

    Isolates the washers shells found at the input shells.

    Parameters
    ----------
    shells : object
            A list of shell entities. Set 0 to work on visible.

    include_filled_connection_holes : bool, optional
            Set to True, to include washers around filled connection holes.

    Returns
    -------
    object
            Returns the washers shells in a list.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                washer_shells = mesh.IsolateWashers(0)

                base.Or(washer_shells)
                container = base.CreateEntity(constants.ABAQUS, "HIGHLIGHT_CONTAINER")
                if base.AddToHighlight(container, washer_shells, "RED"):
                    base.RedrawAll()


    """


def IsolateExterior(
    input: object,
    groups_number: int,
    classification: str,
    group_entities: bool,
    separate_at_blue_bounds: bool,
    separate_at_pid_bounds: bool,
    feature_angle: float,
    feature_type: str,
    view_point: str,
) -> object:
    """
    .. deprecated:: 23.0.0
            Use :py:func:`IsolateVisibilityGroups` instead.


    The function separates the input entities to groups according to how exterior they are.

    Parameters
    ----------
    input : object
            A list that can contain faces, shells and solids.

    groups_number : int
            The number of groups in which the input entities will be categorized.

    classification : str, optional
            Specifies the way the connectivity groups will be classified.
            They can be classified by an average value by the outermost or
            the innermost entity.
            Available options are "average", "outermost" and "innermost".
            (Default: "average")

    group_entities : bool, optional
            If set to True, the entities will be isolated as whole connectivity groups.
            If set to False, each entity will be isolated separately.
            (Default: True)

    separate_at_blue_bounds : bool, optional
            If set to True, then regions connected via triple bounds are placed into
            separate connectivity groups.
            If set to False, then all connected entities are placed into the same group.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: True)

    separate_at_pid_bounds : bool, optional
            If set to True, then all entities contained in a connectivity group
            will have the same PID.
            If set to False, then each connectivity group can contain connected
            entities with different PIDs.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: True)

    feature_angle : float, optional
            The feature angle limit in degrees.
            If this value is exceeded, the groups get separated at this feature line.
            Valid values are 0 - 180.
            If set to 0, the feature line separation is disabled.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: 60.0)

    feature_type : str, optional
            Specifies the type of the feature lines in which the connectivity groups
            will be separated.
            Groups get separated at the examined bound only if feature_angle is
            exceeded and the feature type is of the specified type.
            Available options are "convex", "concave" and "convex_and_concave".
            This option is valid only when group_entities = True and feature_angle > 0.
            In case of group_entities = False or feature_angle = 0 it is ignored.
            (Default: "convex_and_concave")

    view_point : str, optional
            Specifies the view point from wich the model will be observed.
            Available options are "scan_all_around" and "normal_to_screen".
            (Default: "scan_all_around")

    Returns
    -------
    object
            Returns a list.
            This list contains lists with entities that correspond to each group on how exterior they are.
            The lists are sorted from the most interior group of entities to the most exterior.
            The first list contains the absolutely interior entities and the last the absolutely exterior.

    See Also
    --------
    IsolateVisibilityGroups

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            # separetes shells in parts depending on how exterior they are
            def main():
                shells = base.CollectEntities(0, None, "SHELL", False)
                groups = mesh.IsolateExterior(shells, 5)

                i = 0
                for group in groups:
                    part = base.NewPart("Part_" + str(i))
                    base.SetEntityPart(group, part)
                    i = i + 1


    """

    import warnings

    warnings.warn(
        "Deprecated since version 23.0.0. Use :py:func: IsolateVisibilityGroups instead.",
        DeprecationWarning,
    )


def CalculateThickness(
    middle_entities: object,
    skin_entities: object,
    maximum_thickness: float,
    keep_thickness_at_junctions: int,
    assign_thickness_to: str,
    pid_thickness_step: float,
    use_materials_from: str,
) -> int:
    """

    This function calculates the proper thickness for every node of each middle shell based on the specified skin entities and assigns it to the nodes or to the properties.

    Parameters
    ----------
    middle_entities : object
            A list that contains the entities that will get a new
            calculated thickness.

    skin_entities : object
            A list that contains the middle entities that represent
            the solid description of the model.

    maximum_thickness : float
            Determines the distance from the middle within which the
            function will begin to search for the corresponding skin.

    keep_thickness_at_junctions : int
            Determines if the thickness of the ribs will be kept while
            approaching to the junctions or not.

    assign_thickness_to : str, optional
            Determines if the calculated thicknesses will be assigned to 'nodes' or to 'properties'.
            The default value is 'nodes'.

    pid_thickness_step : float, optional
            The thickness step that will be used to create the thickness properties.
            The default value is 0.5

    use_materials_from : str, optional
            Determines if the materials of the created thickness properties will be taken from the 'middle' or the 'skin' entities.
            The default value is 'middle'.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import mesh
            from ansa import base


            def main():
                shells = base.CollectEntities(0, None, "SHELL", False)
                faces = base.CollectEntities(0, None, "FACE", False)
                mesh.CalculateThickness(shells, faces, 4.0, 1)


    """


def SplitToTetras(solids: object, improve: bool, ret_ents: bool) -> int:
    """

    This function will convert solids elements into tetrahedrals.
    The solids are given as an arguement and the they are going to be deleted.
    If improve_quality is active then any off elements that will be created will be reconstructed

    Parameters
    ----------
    solids : object
            The solids that are going to be converted.

    improve : bool
            If true, then after the spliting any off elements are going to be reconstructed.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns 0 on success and 1 on failure.
            If ret_ents=True it will return a list with the created entities,
            or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                solids = base.CollectEntities(constants.NASTRAN, None, "SOLID")
                new_ents = mesh.SplitToTetras(solids, True, True)


    """


def IntersectWeldingFE(
    input: object,
    thick_ratio: float,
    extend_distance: float,
    ignore_same_pid: bool,
    ignore_same_part: bool,
    ignore_same_set: bool,
    ignore_same_neighbour_zones: bool,
    improve_mesh_quality: bool,
) -> int:
    """

    This function extends and connects skinned FE meshes.

    Parameters
    ----------
    input : object
            A single object or a list of parts, properties, materials or sets.
            If input equals to 0, the visible shells are collected.

    thick_ratio : float, optional
            The extension limit expressed as a ratio of the local nodal thickness.
            (Default: 0.0)

    extend_distance : float, optional
            The extension limit expressed as an absolute value.
            (Default: 0.0)

    ignore_same_pid : bool, optional
            If set to True, ignores intersections within the same property.

    ignore_same_part : bool, optional
            If set to True, ignores intersections within the same part.

    ignore_same_set : bool, optional
            If set to True, ignores intersections within the same set.

    ignore_same_neighbour_zones : bool, optional
            If set to True, ignores intersection between shells that are
            within n zones from each other.

    improve_mesh_quality : bool, optional
            If set to True, improves the mesh quality in 1 zone around
            the intersected shells.

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                parts = []
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                mesh.IntersectWeldingFE(
                    parts,
                    thick_ratio=1.1,
                    ignore_same_pid=True,
                    ignore_same_neighbour_zones=3,
                    improve_mesh_quality=True,
                )


    """


def IntersectFusePanels(
    input: object,
    offset_distance: float,
    ignore_same_pid: bool,
    ignore_same_part: bool,
    ignore_same_set: bool,
    ignore_same_neighbour_zones: bool,
    improve_mesh_quality: bool,
    fuse_direction: str,
    dx: float,
    dy: float,
    dz: float,
    project_shells: object,
) -> int:
    """

    This function implements fuse parallel overlapping FE panels to create watertight mesh.

    Parameters
    ----------
    input : object
            A single object or a list of parts, properties, materials or sets.
            If input equals to 0, the visible shells are collected.

    offset_distance : float
            The offset distance between different panels, measured in the direction
            of the negative normal vector.

    ignore_same_pid : bool, optional
            If set to True, ignores intersections with the same property.

    ignore_same_part : bool, optional
            If set to True, ignores intersections within the same part.

    ignore_same_set : bool, optional
            If set to True, ignores intersections within the same set.

    ignore_same_neighbour_zones : bool, optional
            If set to True, ignores intersection between shells that are
            within n zones from each other.

    improve_mesh_quality : bool, optional
            If set to True, improves the mesh quality in 1 zone around
            the intersected shells.

    fuse_direction : str, optional
            Defines the fuse direction.
            Can be "negative_offset", "user_defined" or "project".
            (Default: "negative_offset")

    dx : float, optional
            The x-coordinate for the projection direction.
            This is taken into account only when fuse_direction = "user_defined".

    dy : float, optional
            The y-coordinate for the projection direction.
            This is taken into account only when fuse_direction = "user_defined".

    dz : float, optional
            The z-coordinate for the projection direction.
            This is taken into account only when fuse_direction = "user_defined".

    project_shells : object, optional
            A list of shells to be projected on "input" shells.
            This is taken into account only when fuse_direction = "project".

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                parts = []
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                parts.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                mesh.IntersectFusePanels(
                    parts,
                    offset_distance=10,
                    ignore_same_pid=True,
                    ignore_same_neighbour_zones=3,
                    improve_mesh_quality=True,
                    fuse_direction="user_defined",
                    dx=0,
                    dy=1,
                    dz=0,
                )


    """


def HexaBoxOrtho(
    loaded_elements: object,
    db_or_visible: str,
    coordinate: object,
    min_flag: bool,
    directions: object,
) -> object:
    """

    Function for the creation of a hexa box.

    Parameters
    ----------
    loaded_elements : object, optional
            A list with the elements to be included by the created hexa box.

    db_or_visible : str, optional
            Can have values 'DB' or 'Visible', for elements to be included
            by the created hexa box.

    coordinate : object, optional
            A local coordinate object instead of global.

    min_flag : bool, optional
            True or False for minimum volume hexa box.

    directions : object, optional
            A list of 2 directions to define specific orientation for the hexa box. Must be perpendicular to each other.

    Returns
    -------
    object
            Returns a reference to the newly created hexa box object on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                mesh.HexaBoxOrtho(db_or_visible="DB")

                mesh.HexaBoxOrtho(db_or_visible="Visible", min_flag=True)

                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL", filter_visible=True)
                mesh.HexaBoxOrtho(loaded_elements=shells, min_flag=True)

                vectors = [[0.0, 0.5, 0.5], [1.0, 0.0, 0.0]]
                mesh.HexaBoxOrtho(shells, directions=vectors)


    """


def CreateShellsOnSolidsPidSkin(solids: object, ret_ents: bool) -> object:
    """

    This function creates shells/shedras on the skin of the solid properties, while assigning
    those shells to a new pid and part with similar name
    as the solids on whose facets they were created.
    The function works with Solids of first and second order, as well as with polyhedra.

    Parameters
    ----------
    solids : object
            An array of solids/polyhedra where the solid pids will be found.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    object
            Returns 0 on success and 1 on failure.
            If ret_ents=True, then it returns a list with the created entities.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                solids = base.CollectEntities(constants.NASTRAN, None, "SOLID")
                mesh.CreateShellsOnSolidsPidSkin(solids)


    """


def ExtrudeOffset(
    source: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    direction: str,
    distance: float,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 20.1.0
            Use :py:class:`VolumesExtrude` instead.


    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). A normal vector of source
    area is used as offset vector. The user may select a Linear, Exponential or Bell Curve
    biasing function to achieve the desired volume element distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    direction : str, optional
            Direction of offset vector. Can be "default", "inverted" or "both".

    distance : float, optional
            Target distance.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeSweepGlide, ExtrudeDualSweep, ExtrudeMap, ExtrudeRotate, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                search_faces = ("FACE",)
                all_faces = base.CollectEntities(0, None, search_faces, False)
                mesh.ExtrudeOffset(
                    source=all_faces,
                    connect_source=True,
                    direction="inverted",
                    distance=10,
                    steps=5,
                    biasing="exponential",
                    factor=1.2,
                    side_treatment="snap",
                    angle=30,
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.1.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def ExtrudeProject(
    source: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """

    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). The projection of source
    area to target area leads the extrusion. The user may select a Linear, Exponential or
    Bell Curve biasing function to achieve the desired volume element distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    target : object
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeOffset, ExtrudeSweepGlide, ExtrudeDualSweep, ExtrudeMap, ExtrudeRotate, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                face1 = base.GetEntity(constants.NASTRAN, "FACE", 1)
                face2 = base.GetEntity(constants.NASTRAN, "FACE", 2)
                mesh.ExtrudeProject(
                    source=face1,
                    target=face2,
                    connect_source=False,
                    steps=5,
                    biasing="exponential",
                    factor=1.2,
                    snap_to_target=True,
                )


    """


def ExtrudeRotate(
    source: object,
    rotation_axis: object,
    rotation_angle: float,
    target: object,
    rem_source: object,
    connect_source: bool,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 20.1.0
            Use :py:class:`VolumesExtrude` instead.


    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). Source area elements are
    rotated using a rotation axis and a rotation angle. The user may select a Linear, Exponential
    or Bell Curve biasing function to achieve the desired volume element distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    rotation_axis : object
            Rotation Axis must be a list with two vectors, the first one defines the origin of the axis, the second one its direction, i.e. ((50,0,0), (0,0,1))

    rotation_angle : float
            Angle used when rotational axis has been selected as guideline.

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeSweepGlide, ExtrudeDualSweep, ExtrudeMap, ExtrudeOffset, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                mesh.ExtrudeRotate(
                    source=all_faces,
                    rotation_axis=((-35, 60, 0), (1, 0, 0)),
                    rotation_angle=180,
                    steps=10,
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.1.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def ExtrudeTranslate(
    source: object,
    translation_axis: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    distance: float,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 20.1.0
            Use :py:class:`VolumesExtrude` instead.


    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). A translation vector is
    used to create volume elements. The user may select a Linear, Exponential or Bell Curve
    biasing function to achieve the desired volume element distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    translation_axis : object
            Translation Axis must be a list with two vectors,
            i.e. ((10, 10, 10),  (5, 5, 5)).

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    distance : float, optional
            Target distance.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeSweepGlide, ExtrudeDualSweep, ExtrudeMap, ExtrudeOffset, ExtrudeRotate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                mesh.ExtrudeTranslate(
                    source=all_faces,
                    translation_axis=((-34, 60, 20), (0, 0.2, 1)),
                    distance=100,
                    steps=10,
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.1.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def ExtrudeSweepGlide(
    algorithm: str,
    source: object,
    guideline: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    guide_distribution: bool,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """
    .. deprecated:: 20.1.0
            Use :py:class:`VolumesExtrude` instead.


    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). Source area elements are
    swept or glided using Curves, Macro Areas' Perimeter segments or edges as guidelines.
    The user may select a Linear, Exponential or Bell Curve biasing function to achieve the
    desired volume element distribution.

    Parameters
    ----------
    algorithm : str
            Algorithm used for extrusion, can be "sweep" or "glide".

    source : object
            A list of shells, faces or facets which are used as source area.

    guideline : object
            Perimeters, curves or edges used as guide lines.

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    guide_distribution : bool, optional
            Use guide distribution.
            If enabled all other distribution arguments should not be used.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeOffset, ExtrudeDualSweep, ExtrudeMap, ExtrudeRotate, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                all_curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                mesh.ExtrudeSweepGlide(
                    algorithm="sweep",
                    source=all_faces,
                    guideline=all_curves,
                    biasing="exponential",
                    steps=10,
                    factor=1.2,
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.1.0. Use :py:class: VolumesExtrude instead.",
        DeprecationWarning,
    )


def ExtrudeDualSweep(
    source: object,
    guideline: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    guide_distribution: bool,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """

    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). Source area elements are swept
    along two guidelines of Curves, Macro Areas' Perimeter segments or edges. The user may select
    a Linear, Exponential or Bell Curve biasing function to achieve the desired volume element
    distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    guideline : object
            Perimeters, curves or edges used as guide lines.

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    guide_distribution : bool, optional
            Use guide distribution.
            If enabled all other distribution arguments should not be used.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeOffset, ExtrudeSweepGlide, ExtrudeMap, ExtrudeRotate, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                all_curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                mesh.ExtrudeDualSweep(source=all_faces, guideline=all_curves, steps=10)


    """


def ExtrudeMap(
    source: object,
    guideline: object,
    target: object,
    rem_source: object,
    connect_source: bool,
    guide_distribution: bool,
    steps: int,
    first_height: float,
    biasing: str,
    factor: float,
    factor_dir: str,
    side_treatment: str,
    angle: float,
    snap_to_target: bool,
    connect_to_target: bool,
    part: object,
    property: object,
) -> int:
    """

    This function generates Hexa and/or Penta volume elements, through extruding a Source area.
    Source area may consist either of Macro Areas, that do not have to be necessarily meshed,
    FE Shells or Solid Facets (or a combination of the previous). Source area elements are
    extruded using two or more guidelines of Curves, Macro Areas' Perimeter segments or edges.
    The user may select a Linear, Exponential or Bell Curve biasing function to achieve the
    desired volume element distribution.

    Parameters
    ----------
    source : object
            A list of shells, faces or facets which are used as source area.

    guideline : object
            Perimeters, curves or edges used as guide lines.

    target : object, optional
            A list of shells, faces or facets which are used as target area.

    rem_source : object, optional
            A list of shells, faces or facets which are removed from source area.

    connect_source : bool, optional
            Connect source areas.

    guide_distribution : bool, optional
            Use guide distribution.
            If enabled all other distribution arguments should not be used.

    steps : int, optional
            Number of distribution steps.

    first_height : float, optional
            The height of the first layer.

    biasing : str, optional
            Type of distribution biasing. Can be "linear", "exponential", "bell" or "no".

    factor : float, optional
            Biasing factor.

    factor_dir : str, optional
            Biasing direction. Can be "default" or "inverted".

    side_treatment : str, optional
            Side treatment can be "snap" for Snap to Side, "collapse" for Collapse
            free edges, "no" for no side treatment.

    angle : float, optional
            Angle used for side treatment.

    snap_to_target : bool, optional
            Snap to target bounds.

    connect_to_target : bool, optional
            Connect to target area.

    part : object, optional
            The part assigned to the created volume.

    property : object, optional
            The property assigned to the created volume.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    ExtrudeProject, ExtrudeOffset, ExtrudeSweepGlide, ExtrudeDualSweep, ExtrudeRotate, ExtrudeTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                all_curves = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                mesh.ExtrudeMap(source=all_faces, guideline=all_curves, steps=10)


    """


def HexaBlockInitBoxEdges(
    box_edges: object,
    remesh_box_faces: bool,
    initialize_number: bool,
    initialize_spacing: bool,
) -> int:
    """

    This function initializes the nodal spacing of hexa block edges.

    Parameters
    ----------
    box_edges : object
            A list that contains box edges to be initialized.

    remesh_box_faces : bool
            A flag to control if the box faces will be remeshed after the initialization.

    initialize_number : bool
            Initialize the nodal number of box edges.

    initialize_spacing : bool
            Initialize the spacing of box edges.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                edges = []

                # initialize nodal distribution of all box edges of the database
                ent = base.GetFirstEntity(constants.NASTRAN, "HEXA_BOX_EDGE")
                while ent:
                    edges.append(ent)
                    ent = base.GetNextEntity(constants.NASTRAN, ent)
                mesh.HexaBlockInitBoxEdges(edges, True, True, True)


    """


def HexaBlockVolumesMap(
    box_faces: object,
    boxes: object,
    tolerance: str,
    project: bool,
    apply_surface_fit: bool,
    project_non_associated: bool,
) -> int:
    """

    Script function that generates the volume mesh according to the Hexa Block "Map" generator.

    Parameters
    ----------
    box_faces : object
            A list that contains hexa box faces whose shell mesh will be used
            to generate solid elements (hexas and pentas).

    boxes : object, optional
            The boxes where the shell mesh pattern will be transmitted.

    tolerance : str, optional
            An expression to define the tolerance as a percentage of
            the minimum element length (Lmin).

    project : bool, optional
            A flag that defines whether to project (True) or not (False) on geometry.

    apply_surface_fit : bool, optional
            A flag that defines if surface-fit will be applied for
            fully associated box faces (box faces with points,
            edges and face association).

    project_non_associated : bool, optional
            A flag that defines if nodes of non-associated box
            faces will be projected on the geometry.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 3))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 5))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 7))

                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 13))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 4))

                mesh.HexaBlockVolumesMap(box_faces=box_faces, boxes=boxes, tolerance="0.001*Lmin")


            def main():
                box_faces = []
                box_faces.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_FACE", 2))
                boxes = []
                boxes.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1))
                ansa.mesh.HexaBlockVolumesMap(
                    box_faces=box_faces,
                    boxes=boxes,
                    tolerance="0.05*Lmin",
                    project=True,
                    apply_surface_fit=True,
                    project_non_associated=True,
                )


    """


def Redistribute(
    property: object,
    num_layers: object,
    layers_dir: int,
    growth_rate: float,
    modify: str,
    num_layers_applied: int,
    create_shells: bool,
) -> int:
    """

    This function changes the distribution of solid element layers that belong to a given property.

    Parameters
    ----------
    property : object
            The property of the solid layers to be redistributed.

    num_layers : object
            The number of layers.

    layers_dir : int, optional
            The direction of the layers redistribution.
            Can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

    growth_rate : float, optional
            The growth rate.

    modify : str, optional
            Determines whether changes are applied per layer or for all layers.
            It can be "per_layer" or "all_layers".

    num_layers_applied : int, optional
            If enabled, redistribution is applied only at the given number of first layers.

    create_shells : bool, optional
            If enabled, new shells are created instead of modifying existing layers.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    RedistributeMulti, ChangeHeightOfLayers, ChangeHeightOfLayersMulti

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                prop = base.GetEntity(constants.NASTRAN, "PSOLID", 10)
                mesh.Redistribute(property=prop, num_layers=3, growth_rate=1.2)


    """


def ChangeHeightOfLayers(
    property: object,
    increase_by: float,
    type: str,
    layers_dir: int,
    mod_dir: str,
    num_layers_applied: int,
) -> int:
    """

    This function modifies the height of solid element layers that belong to a given property.

    Parameters
    ----------
    property : object
            Property of solid layers to be modified

    increase_by : float
            Increase value

    type : str
            Type of increase value; can be "percentage" or "absolute"

    layers_dir : int, optional
            Direction of layers modification; can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

    mod_dir : str, optional
            Determines the direction where the height is modified; can be "up", "down" or "both"

    num_layers_applied : int, optional
            If enabled modifications are applied only at the given number of first layers

    Returns
    -------
    int
            One 1 upon success zero 0 on failure

    See Also
    --------
    ChangeHeightOfLayersMulti, Redistribute, RedistributeMulti

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                prop = base.GetEntity(constants.NASTRAN, "PSOLID", 10)
                mesh.ChangeHeightOfLayers(property=prop, increase_by=15, type="percentage")


    """


def HexaBlockOrthoSmooth(
    box_faces: object,
    feature_lines: object,
    layers_number: int,
    layers_smooth_iterations: int,
    smooth_through_boxes: bool,
    smooth_base_surface_mesh: bool,
    smooth_iterations: int,
    fix_violating_solids: bool,
    boxes: object,
) -> int:
    """

    Smooths Hexa Block Orthos.

    Parameters
    ----------
    box_faces : object
            A list of box faces where layers grow from. O-Grid topologies
            can also be used as input (in this case, O-Grid box faces will
            be used by the function).

    feature_lines : object, optional
            A list of box edges that define the model's feature lines. If no
            box edges are defined as feature lines, default feature lines
            will be used (according to the feature line angle).

    layers_number : int, optional
            The number of layers to be smoothed for orthogonality.
            If it is not defined, the default value will be used.

    layers_smooth_iterations : int, optional
            The number of iterations that control the smoothing of layers' vectors.
            More iterations result in smoother layers' vectors (they deviate more
            from surface normal vectors).
            If it is not defined, the default value will be used.

    smooth_through_boxes : bool, optional
            A flag to define if smoothing will affect the whole hexa block model.

    smooth_base_surface_mesh : bool, optional
            A flag to define if the surface mesh of the boundary box faces
            will be smoothed.

    smooth_iterations : int, optional
            The number of iterations that define the smoothing of neighboring solids
            and/or base surface mesh. More iterations result in smoother
            (shell/solid) mesh. If it is not defined, default value will be used.

    fix_violating_solids : bool, optional
            A flag to activate a mechanism that fixes solids having
            intersections or negative volume.

    boxes : object, optional
            The boxes to be smoothed by the general smoothing algorithm.
            It is used to avoid smoothing the whole hexa block model (defined
            by the flag smooth_through_boxes).

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    HexaBlockSmooth

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def example1():
                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 119))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 126))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 38))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 45))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 52))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 59))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 62))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 69))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 76))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 83))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 86))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 93))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 101))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 103))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 111))

                mesh.HexaBlockOrthoSmooth(
                    box_faces,
                    layers_number=5,
                    layers_smooth_iterations=20,
                    smooth_through_boxes=True,
                    smooth_base_surface_mesh=False,
                    smooth_iterations=10,
                )


            def example2():
                ogrid = base.GetEntity(constants.NASTRAN, "O_GRID_TOPOLOGY", 1)
                mesh.HexaBlockOrthoSmooth(ogrid, layers_number=3, smooth_base_surface_mesh=False)


    """


def MatchShellsAndSolids(shells: object, solids: object) -> object:
    """

    Returns a list of matched Shells and Solids. Every 2 instances of the list is a pair.
    It needs a list of shells and a list of solids.

    Parameters
    ----------
    shells : object
            A list of shells.

    solids : object
            A list of solids.

    Returns
    -------
    object
            Returns a list of pairs of shells and solids.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                shells = base.CollectEntities(0, None, "SHELL")
                solids = base.CollectEntities(0, None, "SOLID")
                pairs = mesh.MatchShellsAndSolids(shells, solids)


    """


def CreateFillet(
    fillet_type: str,
    edges: object,
    chamfer_width: float,
    fillet_radius: float,
    fillet_rows: int,
    ret_ents: bool,
) -> object:
    """

    This function creates fillet or chamfer on FE shells at dach areas. Givien as input
    the edges of the dach, it creates fillet/chamfer according to the rest input parameters.

    Parameters
    ----------
    fillet_type : str
            The fillet type that will be created. It can be "fillet" or "chamfer".

    edges : object
            Edges of the dach area.

    chamfer_width : float, optional
            The width of the chamfer.

    fillet_radius : float, optional
            The radius of the fillet.

    fillet_rows : int, optional
            The rows of the fillet.

    ret_ents : bool, optional
            If set to True, a list with the shells of the created fillet/chamfer will be returned.

    Returns
    -------
    object
            Returns 1 on success or 0 on failure.
            If ret_ents=True, it will return a list with the shells of the created fillet/chamfer, or None in case of error.

    See Also
    --------
    ModifyFillet

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                edges = base.CollectEntities(constants.NASTRAN, set, "EDGE", recursive=True)

                mesh.CreateFillet("fillet", edges, fillet_radius=0.2, fillet_rows=4)


    """


def ModifyFillet(
    fillet_type: str,
    shells: object,
    edges: object,
    chamfer_width: float,
    fillet_radius: float,
    fillet_rows: int,
    ret_ents: bool,
) -> object:
    """

    This function creates dach, chamfer or fillet on FE shells at chamfer/fillet areas.
    Giving as input the shells of the existing chamfer/fillet and the upper and down edges
    that define the fillet direction, it modifies it according to the rest input parameters.
    It can be used to change the existing fillet type into another or to change its parameters.
    For example change a fillet into dach, or just change a fillet's rows.

    Parameters
    ----------
    fillet_type : str
            The fillet type that the existing chamfer/fillet will be modified into.
            Can be "dach", "fillet" or "chamfer".

    shells : object
            The FE shells of the existing chamfer/fillet.

    edges : object
            The upper and down edges of the existing chamfer/fillet that
            define the fillet direction.

    chamfer_width : float, optional
            The width of the chamfer.

    fillet_radius : float, optional
            The radius of the fillet.

    fillet_rows : int, optional
            The rows of the fillet.

    ret_ents : bool, optional
            If set to True, a list with the shells of the created fillet/chamfer will be returned.

    Returns
    -------
    object
            Returns 1 on success or 0 on failure.
            If ret_ents=True, it will return a list with the shells of the created fillet/chamfer, or None in case of error.

    See Also
    --------
    CreateFillet

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                set = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                shells = base.CollectEntities(constants.NASTRAN, set, "SHELL", recursive=True)

                set = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)
                edges = base.CollectEntities(constants.NASTRAN, set, "EDGE", recursive=True)

                mesh.ModifyFillet("fillet", shells, edges, fillet_radius=0.2, fillet_rows=4)


    """


def ElementsExtrude(
    algorithm: str,
    edges: object,
    guideline1: object,
    use_edges_nodes: bool,
    distribution: str,
    ref_point: str,
    guideline2: object,
    paste_nodes: bool,
    tolerance: float,
    length: float,
    bias_type: str,
    bias_factor: float,
    point1: object,
    point2: object,
) -> int:
    """

    This function generates shell mesh through extruding the input edges based on one or two guidelines.
    Edges are swept or glided using curves, perimeters or edges as guidelines. The user may select a Linear,
    Exponential or Bell Curve biasing function to achieve the desired element distribution.
    There is also the possibility to translate the final mesh to a desired reference point.

    Parameters
    ----------
    algorithm : str
            Algorithm used for extrusion. Can be "sweep" or "glide".

    edges : object
            The edges that will be extruded.

    guideline1 : object
            Perimeters, curves or edges, used as basic guideline.

    use_edges_nodes : bool
            Use the existing nodes of the guideline if it is not curve,
            otherwise the distribution will be "user_defined".

    distribution : str
            The type of the distribution used for the extrusion,
            can be "guideline" or "user_defined".

    ref_point : str
            The reference point from where to start the extrusion,
            can be "on_edges" or "on_guideline".

    guideline2 : object, optional
            Perimeters, curves or edges, used as secondary guideline
            in case of "sweep" algorithm.

    paste_nodes : bool, optional
            Paste the nodes along the guideline, if it is not curve.

    tolerance : float, optional
            The tolerance in case of "guideline" distribution.

    length : float, optional
            The element length used in case of "user_defined" distribution.

    bias_type : str, optional
            Type of biasing in case of "user_defined" distribution.
            Can be "linear", "exponential", "bell_curve".

    bias_factor : float, optional
            Biasing factor.

    point1 : object, optional
            The first point used in case of "on_guideline" reference point.
            It should be a node of the edges given as input.
            The final result will be an extruded mesh shifted so that the point1
            will overlap point2.

    point2 : object, optional
            The second point used in case of "on_guideline" reference point.
            The final result will be an extruded mesh shifted so that the point1
            will overlap point2.

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                set = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                edges = base.CollectEntities(constants.NASTRAN, set, "EDGE", recursive=True)

                set1 = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)
                guideline_1 = base.CollectEntities(constants.NASTRAN, set1, "CURVE", recursive=True)

                set2 = base.GetEntity(ansa.constants.NASTRAN, "SET", 3)
                guideline_2 = base.CollectEntities(constants.NASTRAN, set2, "CURVE", recursive=True)

                point_1 = base.GetEntity(constants.NASTRAN, "GRID", 135189)
                point_2 = base.GetEntity(constants.NASTRAN, "POINT", 3)

                mesh.ElementsExtrude(
                    "sweep",
                    edges,
                    guideline_1,
                    True,
                    "user_defined",
                    "on_guideline",
                    guideline2=guideline_2,
                    bias_type="exponential",
                    point1=point_1,
                    point2=point_2,
                )


    """


def HexaBoxByPoints(points: object, solid_type: str) -> object:
    """

    Function for creating 3D hexa block boxes (TETRA, PENTA or HEXA boxes)
    from existing nodes, edges or shells.

    Parameters
    ----------
    points : object
            A list with entities from where 4,5,6 or 8 points will be taken to
            create TETRA, PYRAMID, PENTA or HEXA boxes.

    solid_type : str, optional
            An argument that defines the solid type in case
            that the input points could be used for the creation
            of more than one solid types. It takes the values
            "hexa", "penta", "tetra" or "pyramid".

    Returns
    -------
    object
            Returns a reference to the newly created box object on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def hexaBoxFromPoints():
                m1 = []
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 11))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 21))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 31))
                m1.append(base.GetEntity(constants.NASTRAN, "GRID", 41))
                mesh.HexaBoxByPoints(m1)


    """


def HexaBlockSaveAssociations(
    filename: str, hexa_block_entities: str, geometric_entities: str, model: str
) -> int:
    """

    This function saves the associations of the hexa block entities.

    Parameters
    ----------
    filename : str
            The path of the file where all the associations of the hexa block
            entities will be saved.

    hexa_block_entities : str, optional
            Takes the values "Id" or "Name". It defines the way that hexa
            block entities are saved in the associations file.
            (Default: "Id")

    geometric_entities : str, optional
            Takes the values "Id", "Name" or "Faces_Set_Name". It defines the
            way that geometric entities are saved in the associations file. Keyword
            "Faces_Set_Name" is used for CATIA files that are imported in ANSA.
            In this case, ANSA has the option to create a separate set for every
            geometric face and create a specific rule to save geometric entities.
            (Default: "Id")

    model : str, optional
            Takes the values "Visible" or "Whole_Database".
            (Default: "Whole_Database")

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def saveHexaBlockAssociations():
                mesh.HexaBlockSaveAssociations(
                    "C:\\\\Users\\\\username\\\\associationsFile1.txt",
                    hexa_block_entities="Id",
                    geometric_entities="Faces_Set_Name",
                    model="Visible",
                )
                mesh.HexaBlockSaveAssociations(
                    "C:\\\\Users\\\\username\\\\associationsFile2.txt",
                    hexa_block_entities="Id",
                    geometric_entities="Id",
                    model="Whole_Database",
                )
                mesh.HexaBlockSaveAssociations(
                    "C:\\\\Users\\\\username\\\\associationsFile3.txt",
                    hexa_block_entities="Name",
                    geometric_entities="Name",
                    model="Visible",
                )


    """


def HexaBlockReadAssociations(filename: str) -> int:
    """

    Reads and applies the associations of a file to the hexa block entities of the database.

    Parameters
    ----------
    filename : str
            The path of the file that contains the associations information of the hexa block entities.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def readHexaBlockAssociations():
                mesh.HexaBlockReadAssociations("C:\\\\Users\\\\username\\\\associationsFile.txt")


    """


def RedistributeMulti(
    list: object,
    num_layers: int,
    layers_dir: int,
    growth_rate: float,
    modify: str,
    num_layers_applied: bool,
    create_shells: bool,
) -> int:
    """

    This function changes the distribution of solid element layers that belong to a given list of properties or volumes.

    Parameters
    ----------
    list : object
            A list of Pids and Volumes to be redistributed.

    num_layers : int
            The number of layers.

    layers_dir : int, optional
            The direction of the layers redistribution.
            Can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers).

    growth_rate : float, optional
            The growth rate.

    modify : str, optional
            Determines whether changes are applied per layer or for all layers.
            Can be "per_layer" or "all_layers".

    num_layers_applied : bool, optional
            If enabled, redistribution is applied only at the given number of first layers.

    create_shells : bool, optional
            If enabled, new shells are created instead of modifying existing layers.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    Redistribute, ChangeHeightOfLayers, ChangeHeightOfLayersMulti

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                vol1 = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                vol2 = base.GetEntity(constants.NASTRAN, "VOLUME", 2)
                mesh.RedistributeMulti(list=[vol1, vol2], num_layers=3, growth_rate=1.2)


    """


def ChangeHeightOfLayersMulti(
    list: object,
    increase_by: float,
    type: str,
    layers_dir: int,
    mod_dir: str,
    num_layers_applied: int,
):
    """

    This function modifies the height of solid element layers that belong to a given list of properties or volumes.

    Parameters
    ----------
    list : object
            List of Pids and Volumes to be modified

    increase_by : float
            Increase value

    type : str
            Type of increase value; can be "percentage" or "absolute"

    layers_dir : int, optional
            Direction of layers modification; can be 1, 2, 3, -1, -2, -3 (Note: 1 is the direction of ANSA layers)

    mod_dir : str, optional
            Determines the direction where the height is modified; can be "up", "down" or "both"

    num_layers_applied : int, optional
            If enabled modifications are applied only at the given number of first layers

    See Also
    --------
    ChangeHeightOfLayers, Redistribute, RedistributeMulti

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                vol1 = base.GetEntity(constants.NASTRAN, "VOLUME", 1)
                vol2 = base.GetEntity(constants.NASTRAN, "VOLUME", 2)
                mesh.ChangeHeightOfLayersMulti(list=[vol1, vol2], increase_by=15, type="percentage")


    """


def Create2DEnvelopeFromShellsOnPlane(shells: object) -> object:
    """

    The function is designed to work on a list of shells that lie on the same plane.
    It creates a planar shell mesh that represents the 2d envelope of the input shells.

    Parameters
    ----------
    shells : object
            A list with references to shell elements.

    Returns
    -------
    object
            Returns a list with with the created shells of the 2d envelope.
            On error, it returns an empty list.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                all_shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                env_shells = mesh.Create2DEnvelopeFromShellsOnPlane(all_shells)
                print(len(env_shells))


    """


def SuppressNoise(
    shells: object, intensity: str, only_move_nodes: bool, movement_direction: str
) -> int:
    """

    This function will smooth and flatten anomalies that exist in FE mesh.

    Parameters
    ----------
    shells : object
            A list of shell entities.

    intensity : str, optional
            Defines how intense the suppressing of the noise will be.
            Available options are "high", "middle", "low" and "local_peaks".
            (Default: "high")

    only_move_nodes : bool, optional
            If set to True, the mesh connectivity will remain and the result will have
            the same nodes but in a new position.
            If set to False, the mesh connectivity will change and some nodes will be pasted.
            (Default: False)

    movement_direction : str, optional
            Defines the direction towards the nodes will be moved.
            Available options are "both_sides", "grey_side" or "yellow_side".
            (Default: "both_sides")

    Returns
    -------
    int
            Returns 1 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.SuppressNoise(
                    shells,
                    intensity="middle",
                    only_move_nodes=True,
                    movement_direction="both_sides",
                )


    """


def SolidsMeshV(solids: object, mesh_type: str) -> int:
    """

    This function remeshes an array of solids with a specified generator.

    Parameters
    ----------
    solids : object
            A list with the solid elements to be remeshed.

    mesh_type : str
            Corresponds to the mesh generator. The string values for each mesh type can be:
            "TETRA RAPID", "TETRA FEM", "TETRA CFD", "HEXA INTERIOR" or "HEXAPOLY".

    Returns
    -------
    int
            Returns 1 on success or 0 on failure.

    See Also
    --------
    VolumesMeshV

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                solids = base.CollectEntities(constants.NASTRAN, None, "SOLID")
                mesh.SolidsMeshV(solids, "TETRA RAPID")


    """


def HexaBoxByCurves(height_edges: object, top_bottom_edges: object) -> object:
    """

    A function for creating a hexa block box by defining its four "height" edges
    and the "top", "bottom" edges (optionally).

    Parameters
    ----------
    height_edges : object
            A list that contains all the entities that define
            the four box "height" edges.

    top_bottom_edges : object, optional
            A list that contains all the entities that define
            the "top" and "bottom" edges of the new box.

    Returns
    -------
    object
            Returns a reference to the newly created box object on success, or 0 on failure.

    See Also
    --------
    HexaBoxOrtho, HexaBoxByPoints

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def hexaBoxByCurves():
                height_edges = []
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 5))
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 6))
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 7))
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 8))
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 9))
                height_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 10))

                top_bottom_edges = []
                top_bottom_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 3))
                top_bottom_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 4))

                mesh.HexaBoxByCurves(height_edges=height_edges, top_bottom_edges=top_bottom_edges)


    """


def CavityWrap(
    entities: object,
    leak_distance: float,
    target_length: float,
    maximum_length: float,
    nth_largest: int,
    snap_nodes: bool,
    features_set: object,
) -> int:
    """

    This function creates constant length wraps suitable for inner cavities.

    Parameters
    ----------
    entities : object
            A list of input entities.

    leak_distance : float
            The maximum length gaps that the algorithm will not intrude.
            The octree voxel length.

    target_length : float
            The target length of the final wrap mesh.

    maximum_length : float
            The strict maximum length that the final wrap will not violate.

    nth_largest : int, optional
            The number of the largest inner cavities that will be wrapped.
            (Default: 1)

    snap_nodes : bool, optional
            If set to True the nodes of wrap will be snapped to the closest
            nodes of structure.
            (Default: False)

    features_set : object, optional
            The set with curves, edges or cons that will be captured by
            the wrap.

    Returns
    -------
    int
            Returns 0 if the wrap is created succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.CavityWrap(shells, 50, 30, 80, 3, False, 0)


    """


def CavityVolumeTetra(
    shells: object, maximum_length: float, growth_rate: float, sensors_set: object
) -> int:
    """

    This function creates volume meshes for cavities, consisting of tetras.

    Parameters
    ----------
    shells : object
            A list of the input shells, that will define the volume boundary.

    maximum_length : float
            The maximum element length of the created volume mesh.

    growth_rate : float, optional
            The growth rate of the created tetras towards the inner of the cavity.
            (Default: 1.5)

    sensors_set : object, optional
            The set that contains nodes that will be used also as nodes of the
            volume mesh.

    Returns
    -------
    int
            Returns 0 if the volume mesh was created succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.CavityVolumeTetra(shells, 80, 1.8, 0)


    """


def CavityVolumeHexaInterior(
    shells: object, maximum_length: float, buffer_zones: int, sensors_set: object
) -> int:
    """

    This function creates volume meshes for cavities, consisting of hexas in the interior,
    some pentas and pyramids, and a zone of tetras near the boundary.

    Parameters
    ----------
    shells : object
            A list of the input shells, that will define the volume boundary.

    maximum_length : float
            The maximum element length of the created volume mesh.

    buffer_zones : int, optional
            The number of buffer zones, that will exist in the hexa interior mesh.
            (Default: 1)

    sensors_set : object, optional
            The set that contains nodes that will be used also as nodes of the
            volume mesh.

    Returns
    -------
    int
            Returns 0 if the volume mesh was created succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.CavityVolumeHexaInterior(shells, 80, 1, 0)


    """


def CavityVolumeHexaDominant(
    shells: object,
    boundary_length: float,
    maximum_length: float,
    nth_largest: int,
    buffer_zones: int,
    sensors_set: object,
    features_set: object,
    feature_angle: float,
) -> int:
    """

    This function creates volume meshes for cavities, consisting of mostly hexas and a few pentas and tetras.

    Parameters
    ----------
    shells : object
            A list of the input shells, that will define the cavity to be
            volume meshed with HexaDominant.

    boundary_length : float
            The length of the elements of the volume near the volume
            boundary.

    maximum_length : float
            The maximum element length of the created volume mesh.
            The element length of the biggest hexas.

    nth_largest : int, optional
            The number of the largest inner cavities that will be volume meshed.
            (Default: 1)

    buffer_zones : int, optional
            The number of buffer zones, that will exist in the hexa dominant mesh.
            (Default: 1)

    sensors_set : object, optional
            The set that contains nodes that will be used also as nodes of the
            volume mesh.

    features_set : object, optional
            The set of edges, that belong to the structure, that will be captured
            by the volume.

    feature_angle : float, optional
            A limit angle for features to be captured by the volume.
            (Default: 60)

    Returns
    -------
    int
            Returns 0 if the volume mesh was created succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.CavityVolumeHexaDominant(shells, 30, 60, 1, 1, 0, 0, 70)


    """


def ConstantWrap(
    entities: object,
    type: str,
    target_length: float,
    nth_largest: int,
    smooth_factor: float,
    mode: str,
    wrap_pid: str,
    shell_type: str,
    offset_factor: int,
    coordinate_system: object,
) -> int:
    """

    This function creates constant length wraps.

    Parameters
    ----------
    entities : object
            A list of input entities.

    type : str
            Defines whether the wrap will be outer or inner.
            Available options are "outer" and "inner", respectively.

    target_length : float
            The target length of the final wrap mesh.

    nth_largest : int, optional
            The number of the largest inner cavities that will be wrapped.
            This option is valid only when type = "inner".
            In case of type = "outer" it is ignored.
            (Default: 1)

    smooth_factor : float, optional
            A value between 0.0 - 1.0, that defines how smooth the result will be.
            When set to 0.0 the result will look like the initial octree with some pasted nodes.
            When set to 1.0 the result will be very smooth.
            (Default: 0.5)

    mode : str, optional
            Defines the positioning of the wrap compared to the structure.
            Available options are "nodes_out", "nodes_tight", "nodes_on_features", "shells_out", "free" and "castellated".
            - "nodes_out" means that the wrap nodes will lie out of the structure
               shells.
            - "nodes_tight" or "nodes_on_structure" means that the wrap nodes will lie exactly on the
               structure shells.
            - "nodes_on_features" means that the wrap nodes will try to lie on features.
            - "shells_out" means that the whole shells of the wrap will lie out of the
               structure shells.
            - "free" means that the nodes will lie in the most suitable position to achieve
               better smoothness, regardless their positioning compared to the structure.
            - "castellated" means that the node will lie at the initial octree positions.
            (Default: "nodes_out")

    wrap_pid : str, optional
            Defines the PID that will be assigned to the created wrap.
            Available options are "from_structure" and "new".
            - "from_structure" means that each wrap shell will have the same PID
               with its closest structure shell.
            - "new" means that a new PID will be creates for each new wrap.
            - "new_single_per_volume" means that each separate volume will have a single new property.
            (Default: "from_structure")

    shell_type : str, optional
            Defines the shell type of the result mesh.
            Available options are "trias" and "quads".
            - "trias" for tria mesh result.
            - "quads" for quad mesh result.
            (Default: "trias")

    offset_factor : int, optional
            Option to inflate the wrap mesh away from the surface by a factor times the wrap length.

    coordinate_system : object, optional
            The coordinate system that the wrap result will be aligned with.

    Returns
    -------
    int
            Returns 0 if the wrap was created succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.ConstantWrap(shells, "inner", 30, 2, 0.5, "nodes_out", "from_structure")


    """


def IsolateSkin(
    type: str,
    leak_length: float,
    nth_largest: int,
    group_entities: bool,
    separate_at_blue_bounds: bool,
    separate_at_pid_bounds: bool,
    feature_angle: float,
    feature_type: str,
    mpar_file: str,
) -> int:
    """

    This function isolates on the screen all the inner or outer wetted entities of the visible model.

    Parameters
    ----------
    type : str
            Defines whether the entities that will be kept are outer or inner.
            Available options are "outer", "inner" and "seed_points".

    leak_length : float
            The maximum length gaps that the algorithm will not intrude.
            The octree voxel length.

    nth_largest : int, optional
            The number of the largest inner cavities that will be isolated.
            This option is valid only when type = "inner".
            In case of type = "outer" or type = "seed_points"  it is ignored.
            (Default: 1)

    group_entities : bool, optional
            If set to True, the entities will be isolated as whole connectivity groups.
            If set to False, each entity will be isolated separately.
            (Default: False)

    separate_at_blue_bounds : bool, optional
            If set to True, then regions connected via triple bounds are placed into
            separate connectivity groups.
            If set to False, then all connected entities are placed into the same group.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: True)

    separate_at_pid_bounds : bool, optional
            If set to True, then all entities contained in a connectivity group
            will have the same PID.
            If set to False, then each connectivity group can contain connected
            entities with different PIDs.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: True)

    feature_angle : float, optional
            The feature angle limit in degrees.
            If this value is exceeded, the groups get separated at this feature line.
            Valid values are 0 - 180.
            If set to 0 then feature line separation is disabled.
            This option is valid only when group_entities = True.
            In case of group_entities = False it is ignored.
            (Default: 60)

    feature_type : str, optional
            Specifies the type of the feature lines in which the connectivity
            groups will be separated.
            Groups get separated at the examined bound only if feature_angle
            is exceeded and the feature type is of the specified type.
            Available options are "convex", "concave" and "convex_and_concave".
            This option is valid only when group_entities = True and feature_angle > 0.
            In case of group_entities = False or feature_angle = 0 it is ignored.
            (Default "convex_and_concave")

    mpar_file : str, optional
            The path of the file containing the parameters. If such a file is given,
            its parameters will be consider as dominant over the given ones.
            For example, given 'type' and 'leak_length' will be replaced if the
            mpar_file contains these parameters.

    Returns
    -------
    int
            Returns 0 if the isolation is completed succesfully and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.IsolateSkin("inner", 20, 3, True, True, True, 50, "convex_and_concave")


            import ansa
            from ansa import mesh


            def main():
                mesh.IsolateSkin("seed_points", 2, mpar_file="/ansa/params.ansa_mpar")


    """


def HexaBlockAutoCFDSpacing(
    input: object,
    growth_rate: float,
    feature_angle: float,
    min_length: float,
    max_length: float,
    sharp_edges_angle_limit: float,
    convex_sharp_edges_length: float,
    convex_sharp_edges_length_mode: str,
    concave_sharp_edges_length: float,
    concave_sharp_edges_length_mode: str,
):
    """

    This function can be used to apply automatically curvature dependant
    perimeter nodal spacing for CFD applications. Algorithm works according
    to the input parameters. If parameters are not defined, default values
    are used.

    Parameters
    ----------
    input : object
            Box edges where the "Auto CFD Spacing" algorithm will be applied to.

    growth_rate : float, optional
            Geometric factor of element length growth.

    feature_angle : float, optional
            The maximum allowed angle between neighboring edges or shells,
            for the curvature resolution.

    min_length : float, optional
            The minimum length of the mesh.

    max_length : float, optional
            The maximum length of the mesh.

    sharp_edges_angle_limit : float, optional
            The sharp edges angle limit.

    convex_sharp_edges_length : float, optional
            The length on identified convex sharp edges.

    convex_sharp_edges_length_mode : str, optional
            Takes the values "absolute" or "local_length" to define the way that
            the convex sharp edges length will be calculated.

    concave_sharp_edges_length : float, optional
            The length on identified concave sharp edges.

    concave_sharp_edges_length_mode : str, optional
            Takes the values "absolute" or "local_length" to define the way that
            the concave sharp edges length will be calculated.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                box_edges = []
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 6))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 10))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 8))
                mesh.HexaBlockAutoCFDSpacing(
                    box_edges, 1.2, 20, 20, 160, 30, 10, "absolute", 10, "absolute"
                )


    """


def PointCloudMesh(points: object, algorithm: str) -> object:
    """

    This function will create shell mesh elements on a cloud of points or grids.
    Element type (Mixed, Tria, Quad, OrthoTria) will respect the mesh parameters value.

    Parameters
    ----------
    points : object
            List of reference to points or grids.

    algorithm : str, optional
            Defines the algorithm that will run.
            Options are "free", "terrain" and "manifold".

    Returns
    -------
    object
            Returns a list with the created shells on success, or None on error.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                all_points = base.CollectEntities(constants.NASTRAN, None, "POINT")
                point_cloud_shells = mesh.PointCloudMesh(all_points)
                print(len(point_cloud_shells))


    """


def CreateTransitionZones(
    boxes: object, box_faces: object, direction: str, element_ratio: object
) -> object:
    """

    This function can be used to create transition zones
    in hexa-block topology in order to coarsen the mesh.

    Parameters
    ----------
    boxes : object
            A list containing the hexa-block boxes.

    box_faces : object
            A list containing the box faces that correspond to the
            model's transition zones.

    direction : str
            Defines the direction of the transition zones and it takes
            the value "inwards" (coarsening is applied inside the input
            boxes) or "outwards" (coarsening is applied outside the
            input boxes).

    element_ratio : object
            A dictionary containing pairs of box edge and the
            element ratio (e.g. '2-1', '3-1').

    Returns
    -------
    object
            Always returns None.

    See Also
    --------
    RemoveTransitionZones, ModifyTransitionZones

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 15))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 18))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 2))

                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 121))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 115))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 109))

                ratios = {}
                ratios[base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 227)] = "2-1"
                ratios[base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 252)] = "3-1"

                ansa.mesh.CreateTransitionZones(boxes, box_faces, "outwards", ratios)


    """


def ModifyTransitionZones(element_ratio: object) -> object:
    """

    This function can be used to modify existing transition zones in hexa-block topology.

    Parameters
    ----------
    element_ratio : object
            A dictionary containing pairs of box edge objects and their element ratio ('2-1', '3-1').
            (See the example)

    Returns
    -------
    object
            Always returns None.

    See Also
    --------
    CreateTransitionZones, RemoveTransitionZones

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                ratios = {}
                ratios[base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 227)] = "2-1"
                ratios[base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 252)] = "3-1"

                mesh.ModifyTransitionZones(ratios)


    """


def RemoveTransitionZones(box_faces: object) -> object:
    """

    This function can be used to remove existing transition zones from a hexa-block topology.

    Parameters
    ----------
    box_faces : object
            A list containing the box faces to remove from the transition zones.

    Returns
    -------
    object
            Always returns None.

    See Also
    --------
    CreateTransitionZones, ModifyTransitionZones

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 121))

                ansa.mesh.RemoveTransitionZones(box_faces)


    """


def CheckSkin(
    skin: object, solid_description: object, distance: float, create_points: bool
) -> object:
    """

    This function checks how good is the result of Skin function.

    Parameters
    ----------
    skin : object
            A list of input entities that is the skin representation of the
            model (the result of the Skin function).

    solid_description : object
            A list of input entities that is the solid description of the
            model (the input of the Skin function).

    distance : float
            The maximum distance from the correct position within which
            the result will be considered good.

    create_points : bool, optional
            If set to True points will be created at areas where the result is not good.
            (Default: False)

    Returns
    -------
    object
            Returns a list with 2 values that range between 0 and 1.
            The first one represents the area percentage of the result model that is good
            according tothe middle position.
            The second one represents the perimeter percentage of the result model that is
            good according the position of the single bounds.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                pshells = base.CollectEntities(constants.NASTRAN, None, "PSHELL")
                ents_1 = base.CollectEntities(constants.NASTRAN, pshells[0], "FACE")
                ents_2 = base.CollectEntities(constants.NASTRAN, pshells[1], "FACE")
                if len(ents_1) < len(ents_2):
                    skin_ents = ents_1
                    solid_ents = ents_2
                else:
                    skin_ents = ents_2
                    solid_ents = ents_1
                ret = mesh.CheckSkin(skin_ents, solid_ents, 0.01, True)

                print("good thickness =", ret[0])
                print("good perimeter =", ret[1])


    """


def CheckMiddleSurface(
    middle_surface: object,
    solid_description: object,
    middle_deviation_value: float,
    middle_deviation_type: str,
    bounds_deviation_value: float,
    bounds_deviation_type: str,
    thickness_deviation_value: float,
    thickness_deviation_type: str,
    check_missing_middle: bool,
    exclude_near_junctions: bool,
    l_junction_angle: float,
) -> object:
    """

    This function checks if a middle surface is good compared to the solid description,
    concerning the following:
    -The positioning of the middle.
    -The positioning of the bounds.
    -The thickness.
    -The missing middle areas.
    -The missing solid description areas.
    -The volume deviation.

    Parameters
    ----------
    middle_surface : object
            A list of input entities that is the middle surface of the model.

    solid_description : object
            A list of input entities that is the solid description of the model.

    middle_deviation_value : float, optional
            The maximum distance from the exact middle position in order
            to be considered as good.
            (Default: 0.05)

    middle_deviation_type : str, optional
            Defines if the middle_deviation_value is an absolute value or a
            percentage of the thickness.
            Available options are "absolute" and "thickness_percentage".
            (Default: "thickness_percentage")

    bounds_deviation_value : float, optional
            The maximum distance from the exact position of bounds in order
            to be considered as good.
            (Default: 0.05)

    bounds_deviation_type : str, optional
            Defines if the bounds_deviation_value is an absolute value or a
            percentage of the thickness.
            Available options are "absolute" and "thickness_percentage".
            (Default: "thickness_percentage")

    thickness_deviation_value : float, optional
            The maximum difference between the current and the correct
            thickness in order to be considered as good.
            (Default: 0.05)

    thickness_deviation_type : str, optional
            Defines if the thickness_deviation_value is an absolute value or
            a percentage of the thickness.
            Available options are "absolute" and "thickness_percentage".
            (Default: "thickness_percentage")

    check_missing_middle : bool, optional
            Defines if the check is going to search for areas of missing
            middle surface.
            (Default: True)

    exclude_near_junctions : bool, optional
            Defines whether the check is going to exclude problematic areas
            that are near junctions or not.
            (Default: True)

    l_junction_angle : float, optional
            Defines the limit angle over which the bounds are going to be
            considered as L junctions.
            (Default: 60)

    Returns
    -------
    object
            Returns an object with 6 values.
            -middle_deviation_area represents the area of the model that was identified as not good,
             according to the positioning in the middle of the solid description.
            -bound_deviation_area represents the area of the model that was identified as not good,
             according to the positioning of the bound.
            -thickness_deviation_area represents the area of the model that was identified as
             not good, according to the thickness.
            -missing_middle_area represents the area of the solid description of the model
             that was identified that has no corresponding middle.
            -failed_to_check_area represents the area of the the model that failed to check.
            -volume_deviation represents the difference between the volume of the solid description
             and the volume that has the middle surface taking into acount its thickness values.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                solid_description_ents = base.CollectEntities(constants.NASTRAN, None, "FACE")
                middle_ents = base.CollectEntities(constants.NASTRAN, None, "SHELL")

                ret = mesh.CheckMiddleSurface(middle_ents, solid_description_ents)

                print("Middle deviation problematic area =", ret.middle_deviation_area)
                print("Bound deviation problematic area =", ret.bound_deviation_area)
                print("Thickness deviation problematic area =", ret.thickness_deviation_area)
                print("Missing middle area =", ret.missing_middle_area)
                print("Failed to check area =", ret.failed_to_check_area)
                print("Volume deviation =", ret.volume_deviation)


    """


def SolidSmooth(solids: object, freeze_skin: bool) -> int:
    """

    This function applies IMPROVE>SMOOTH on solid elements.

    Parameters
    ----------
    solids : object
            A list of solid objects.

    freeze_skin : bool, optional
            Freeze the volume skin.
            (Default: "True")

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                all_solids = base.CollectEntities(constants.NASTRAN, None, "SOLID")
                mesh.SolidSmooth(all_solids, False)


    """


def OrientVolume(volume: object) -> int:
    """

    This function orients all the elements of the volume so that they all point inwards (gray side).

    Parameters
    ----------
    volume : object
            The volume that is going to be oriented.

    Returns
    -------
    int
            Returns 1 on success ,0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            def main():
                volume = base.GetEntity(ansa.constants.NASTRAN, "VOLUME", 1)
                mesh.OrientVolume(volume)


    """


def SplitQuads(entities: object, method: str) -> int:
    """

    This function applies ELEMENTS>SPLIT QUADS on shells and solid facets.

    Parameters
    ----------
    entities : object
            Accepted values: A list of shells and/or solid facets, "all", "visible", 0.
            If set to 0 or "all", runs for all shells of the database.
            If set to "visible," runs for visible shells.

    method : str, optional
            Defines the split method.
            Can be: "oriented_hybrid", "oriented_1", "oriented_2", "quality_based", "violating", "split_x", "union_jack_hybrid", "union_jack_1" or "union_jack_2".
            (Default: "oriented_hybrid")

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SplitQuads("visible", "quality_based")


    """


def BatchGenerator(entities: object) -> int:
    """

    Uses the Batch generator for user input entities.

    Parameters
    ----------
    entities : object
            A list of properties, parts, shells or faces.
            If 0 is specified, the function works on visible faces.

    Returns
    -------
    int
            Always returns 0.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL", False)
                mesh.BatchGenerator(props)


    """


def ApplyOctreeFilters(octree: object) -> bool:
    """

    This function applies the defined filters, in order to load the wanted parts, groups or pids to the octree scenario.
    It also distributes them to the proper area if needed.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, RunOctree, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.ApplyOctreeFilters(octree)


    """


def RunOctree(octree: object) -> bool:
    """

    This function runs the defined octree.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.RunOctree(octree)


    """


def ApplyAutoAssociation(
    distance: float,
    box_points: object,
    box_edges: object,
    box_faces: object,
    work_on_visible: bool,
    cut_geometric_faces: bool,
    connect_to_cons: bool,
    insert_hot_points: bool,
) -> int:
    """

    A function that automatically associates the input Hexa-Block entities.

    Parameters
    ----------
    distance : float
            Maximum distance to search for geometric entities
            that will be associated to the input Hexa-Block entities.

    box_points : object, optional
            The box points to associate.

    box_edges : object, optional
            The box edges to associate.

    box_faces : object, optional
            The box faces to associate.

    work_on_visible : bool, optional
            If set to True, the function will search for geometric entities
            only in visible entities. If it is set to False (default value), the
            function will search for geometric entities in the whole database.

    cut_geometric_faces : bool, optional
            If set to True, the target geometric faces will be cut
            on the position of the input box edges (after projecting
            them to the geometric faces). It is applied to the edges
            of the input box_faces.
            (Default: False)

    connect_to_cons : bool, optional
            If set to True, connects the nodes of the box edges to
            the associated Cons, after meshing the boxes. It is applied
            to the input box_edges or to the edges of the input box_faces.
            (Default: False)

    insert_hot_points : bool, optional
            If set to True, inserts hot points on the position of edges
            start/end points (after projecting them to the geometric CONS).
            It is applied to the input box_edges.
            (Default: False)

    Returns
    -------
    int
            Always returns 1.

    Examples
    --------
    ::

            def main():
                # ---------------------------------
                arg2 = []
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 99))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 100))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 103))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 104))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 107))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 108))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 113))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 114))
                ansa.mesh.ApplyAutoAssociation(distance=1, box_points=arg2, work_on_visible=False)

                # ---------------------------------
                arg2 = []
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 37))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 38))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 39))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 40))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 41))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 42))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 43))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 44))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 45))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 46))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 47))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 48))
                ansa.mesh.ApplyAutoAssociation(
                    distance=1, box_edges=arg2, work_on_visible=False, insert_hot_points=False
                )

                # ---------------------------------
                arg2 = []
                ansa.mesh.ApplyAutoAssociation(
                    distance=1,
                    box_faces=arg2,
                    work_on_visible=False,
                    cut_geometric_faces=False,
                    connect_to_cons=False,
                )


    """


def ProjectShellsOnShells(
    source: object,
    target: object,
    projection_tolerance: float,
    maximum_projections_number: int,
    user_projection_mode_vector: object,
    number_of_shell_zones_affected: int,
    move_projection_to_nearest_perimeter: float,
    move_to_projected_shells: float,
    paste_projected_and_result_shells: int,
    add_results_to_set: str,
    join_perimeters_mode: int,
    cut_faces_on_boundary: bool,
    open_closed_perimeter_hole: bool,
    freeze_non_single_boundary: bool,
) -> int:
    """

    This function projects a group of shells on another group of shells.

    Parameters
    ----------
    source : object
            The shells that will be projected. It can be an object or an array of objects, parts, properties, materials, sets or macros.
            If the INPUT is "visible", the visible shells are collected.

    target : object
            The shells that the source shells be projected on. It can be an object or an array of objects, parts, properties, materials, sets or macros.
            If the INPUT is "visible", the visible shells are collected.

    projection_tolerance : float, optional
            Maximum distance between the projection and the projected entities.

    maximum_projections_number : int, optional
            Maximum number of projections on the target shells.

    user_projection_mode_vector : object, optional
            A list of floating point numbers to define the user project vector.

    number_of_shell_zones_affected : int, optional
            Number of shell zones around projection to be affected.

    move_projection_to_nearest_perimeter : float, optional
            Maximum distance between projections and near perimeters.

    move_to_projected_shells : float, optional
            Between 0. and 1. Parameter to move the result shells towards the projected.

    paste_projected_and_result_shells : int, optional
            Can be 1 or 2. 1 means that the nodes of the result shells and the projected will be pasted and two that their coordinates will be matched

    add_results_to_set : str, optional
            Name of existing set where the result shells will be stored. If the set doesn't exist, a default set will be created.

    join_perimeters_mode : int, optional
            Can be 0, 1 or 2. 0 means that reshape will be called and perimeters that interfere with the projectiuon will be joined to create a compatible mesh. 1 means that the algorithm will try to maintain the perimeters by snapping the projection onto them and if it fails they will be joined. 2 means that no perimeters will be joined and only snap will be performed where possible

    cut_faces_on_boundary : bool, optional
            Determines whether the result shells will cut the geometry on their boundary

    open_closed_perimeter_hole : bool, optional
            Determines whether a hole will be opened on the target shells if a red bound opening is projected on them

    freeze_non_single_boundary : bool, optional
            Determines whether an additional zone of elements will be
            added automatically so as to not have frozen edges in the
            initial selection.

    Returns
    -------
    int
            This function always returns 1

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                source_shells = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                target_shells = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)

                projection_vector = [0.474, 0.181, -0.861]

                mesh.ProjectShellsOnShells(
                    source_shells,
                    target_shells,
                    user_projection_mode_vector=projection_vector,
                    cut_faces_on_boundary=True,
                )


    """


def ProjectPointsOnShells(
    shells: object,
    points: object,
    projection_tolerance: float,
    maximum_projections_number: int,
    user_projection_mode_vector: object,
    number_of_shell_zones_affected: int,
    move_projection_to_nearest_perimeter: float,
    move_to_projected_points: float,
    paste_projected_and_result_points: int,
    add_results_to_set: str,
    mark_result_macro_grids: bool,
) -> int:
    """

    This function projects points or nodes on shells

    Parameters
    ----------
    shells : object
            It is the shells on which the points will be projected. It can be an object or an array of objects, parts, properties, materials, sets or macros.
            If the INPUT is "visible", the visible shells are collected.

    points : object
            It can be an object or a list of points or nodes

    projection_tolerance : float, optional
            Maximum distance between the projection and the projected entity.

    maximum_projections_number : int, optional
            Maximum projection number on the target shells

    user_projection_mode_vector : object, optional
            A list of vector components to define the user projection vector.

    number_of_shell_zones_affected : int, optional
            Number of shell zones around projection to be affected.

    move_projection_to_nearest_perimeter : float, optional
            Maximum distance between projections and near perimeters.

    move_to_projected_points : float, optional
            Between 0. and 1. Parameter to move the result towards the projected points

    paste_projected_and_result_points : int, optional
            Can be 1 or 2. 1 means that the projected and result nodes will be pasted and 2 that only their positions will be matched

    add_results_to_set : str, optional
            Name of an existing set to store the projected nodes. If the set doesn't exist, a default one will be created.

    mark_result_macro_grids : bool, optional
            Determines whether the result nodes will become spots if they belong to macros

    Returns
    -------
    int
            This function always returns 1

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import mesh
            from ansa import constants


            def main():
                target_shells = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)
                grids_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 3)
                grids_array = base.CollectEntities(
                    constants.NASTRAN, grids_set, "GRID", recursive=True
                )
                mesh.ProjectPointsOnShells(target_shells, grids_array, mark_result_macro_grids=True)


    """


def HexaBlockSmooth(
    boxes: object,
    feature_lines: object,
    smooth_iterations: int,
    fix_violating_solids: bool,
) -> int:
    """

    Smooth Hexa-Block boxes.

    Parameters
    ----------
    boxes : object
            The boxes to be smoothed.

    feature_lines : object, optional
            A list of box edges that define the model's feature lines. If no
            box edges are defined as feature lines, default feature lines
            will be used (according to the feature line angle).

    smooth_iterations : int, optional
            The number of iterations that define the smoothing of neighboring solids.
            More iterations result in smoother (shell/solid) mesh. If it is not defined,
            default value will be used.

    fix_violating_solids : bool, optional
            A flag to activate a mechanism that fixes solids having
            intersections or negative volume.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    HexaBlockOrthoSmooth

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def example():
                boxes = []
                boxes.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1))
                boxes.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 3))
                edges = []
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 1))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 3))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 4))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 5))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 7))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 8))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 9))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 12))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 29))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 32))
                ansa.mesh.HexaBlockSmooth(
                    boxes=boxes,
                    feature_lines=edges,
                    smooth_iterations=100,
                    fix_violating_solids=True,
                )


    """


def CheckOctreeLeaks(octree: object) -> bool:
    """

    This function builds the defined octree entity and creates curves if there are any leaks.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if there are any leaks and False otherwise

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.CheckOctreeLeaks(octree)


    """


def ConvertToLightVolumeRepresentation(volumes: object) -> int:
    """

    This function will convert volumes to Light Volume Representation.
    Input volumes must have attached shells on their boundary.

    Parameters
    ----------
    volumes : object, optional
            A list of ansa volumes (if not given all volumes of the db will be converted).

    Returns
    -------
    int
            Returns 0 on success, non zero on error, where:

            0: Success
            1: Failure: No valid volumes were found for conversion.
            2: Failure: Found volume without shells on boundary.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                volume = base.GetEntity(ansa.constants.OPENFOAM, "VOLUME", 1)
                ret = mesh.ConvertToLightVolumeRepresentation(volume)


            if __name__ == "__main__":
                main()


    """


def CollapseViolating() -> object:
    """

    Collapses violating elements.

    Returns
    -------
    object
            Always returns none.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                mesh.CollapseViolating()


            if __name__ == "__main__":
                main()


    """


def RotatingInterface(
    rotating_entities: object,
    static_entities: object,
    offset: float,
    start_x: float,
    start_y: float,
    start_z: float,
    end_x: float,
    end_y: float,
    end_z: float,
    offset_type: str,
    minimum_offset: float,
    vertical_intersection_entities: object,
    vertical_intersection_points: object,
    fill_concavities: bool,
    auto_axis_calc: bool,
    planar_external_direction: object,
    relaxation_angle_limit: float,
) -> object:
    """

    Automatic creation of the sliding interface boundary for rotating volume mesh around wheels.
    Intersections between rotating and static entities should be avoided.

    Parameters
    ----------
    rotating_entities : object
            A list of ansa entities.
            These entities must be faces or shells.

    static_entities : object
            A list of ansa entities.
            These entities must be faces or shells.

    offset : float
            Offset value of rotating interface from rotating entities.

    start_x : float
            X coordinate of rotation axis start.

    start_y : float
            Y coordinate of rotation axis start.

    start_z : float
            Z coordinate of rotation axis start.

    end_x : float
            X coordinate of rotation axis end.

    end_y : float
            Y coordinate of rotation axis end.

    end_z : float
            Z coordinate of rotation axis end.

    offset_type : str
            Offset type.
            Available options are "max_clearance" and "average_clearance" respectively.

    minimum_offset : float
            Minimum offset from rotating entities that the rotating interface should respect.

    vertical_intersection_entities : object, optional
            A list of ansa entities.
            These entities must be faces or shells.

    vertical_intersection_points : object, optional
            A list of ansa entities.
            These entities must be nodes or hotpoints.

    fill_concavities : bool, optional
            Fill concavities option.
            False disabled , True enabled.

    auto_axis_calc : bool, optional
            Automatic axis calculation option.
            False disabled , True enabled.

    planar_external_direction : object, optional
            Define external direction in case of planar interface at the external of the wheel.

    relaxation_angle_limit : float, optional
            Angle that the intersection point should deviate from 90 degrees.
            Values must be between 0-45 degrees.

    Returns
    -------
    object
            Returns an object containing the following:
            ret.status                       : (integer)  0 on succes , 1 if intersections are detected , 2 if minimum offset is
                                                violated , 3 if HOT POINTS and CONS matching distance is violated , 4 if HOT
                                                POINTS matching distance is violated , 5 if CONS matching distance is violated ,
                                                6 if offset distance is too big , 7 if axis cannot calculated automatically.
            ret.result_faces                 : (list)     A list with the created faces of the sliding interface.
            ret.errors_intersections_set     : (ANSA Set) If intersections are detected a set with the intersected shells is returned.
            ret.minimum_offset_violation_set : (ANSA set) If minimum offset violations are detected a set with the violating region is                                    returned.
            ret.minimum_offset_found         : (float) If minimum offset violations are detected the possible minimum offset is                                           returned.
            ret.points_of_rotating_interfaces: (list) Returns the 3d points of the profile of the created rotating interfaces.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                rot_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                stat_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)
                vert_int_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 3)
                vert_int_points_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 4)

                rot_ents = base.CollectEntities(constants.NASTRAN, rot_set, ["SHELL", "FACE"])
                stat_ents = base.CollectEntities(constants.NASTRAN, stat_set, ["SHELL", "FACE"])
                vert_int_ents = base.CollectEntities(
                    constants.NASTRAN, vert_int_set, ["SHELL", "FACE"]
                )
                vert_int_points = base.CollectEntities(
                    constants.NASTRAN, vert_int_points_set, ["GRID"]
                )

                ret = mesh.RotatingInterface(
                    rotating_entities=rot_ents,
                    static_entities=stat_ents,
                    offset=5,
                    start_x=1551.03,
                    start_y=-913.04,
                    start_z=901.49,
                    end_x=1551.03,
                    end_y=-745.28,
                    end_z=898.56,
                    offset_type="max_clearance",
                    minimum_offset=1,
                    vertical_intersection_entities=vert_int_ents,
                    vertical_intersection_points=vert_int_points,
                )
                print("status =", ret.status)
                print("result_num =", len(ret.result_faces))
                if ret.errors_intersections_set:
                    print("errors intersections set =", ret.errors_intersections_set._name)
                if ret.errors_minimum_offset_violation_set:
                    print(
                        "errors minimum offset violations set =",
                        ret.errors_minimum_offset_violation_set._name,
                    )
                    print("possible minimum offset smaller than ", ret.possible_minimum_offset)


    """


def Create4SidedMesh(
    entities: object,
    only_4sided: bool,
    only_aligned: bool,
    corner_angle: float,
    smooth_type: str,
    split_method: str,
    spacing: str,
    elem_type: str,
    quad_pattern: str,
) -> object:
    """

    This function uses 4 Sided mesh generator to produce 4-sided mapped mesh.
    It works for both macros and FE shells.

    Parameters
    ----------
    entities : object
            A list of faces and/or shells.
            If entities equals to 0, the visible faces and shells are used

    only_4sided : bool, optional
            If set to True, only macros identified as 4-sided are meshed.

    only_aligned : bool, optional
            If set to True, only macros with same number of nodes at opposite sides are meshed.

    corner_angle : float, optional
            The supplementary angle between perimeters used for corner identification
            If not defined, the default value is used

    smooth_type : str, optional
            Smooth type can be one of the following strings:
            - 'standard'
            - 'isoparametric'
            If not defined, the default value is used.

    split_method : str, optional
            Split quads method can be one of the following strings:
            - 'hybrid'
            - 'oriented1'
            - 'oriented2'
            - 'quality_based'
            - 'none'
            If not defined, the default value is used.

    spacing : str, optional
            Spacing option can be one of the following strings:
            - 'off'
            - 'isospace'
            - 'map_opposite_sides'
            If not defined, the default value is used.

    elem_type : str, optional
            Element type option can be one of the following strings:
            - 'mixed'
            - 'ortho_tria'
            - 'quad'
            If not defined, the global mesh parameters' value is used.

    quad_pattern : str, optional
            Quad pattern option can be one of the following strings:
            - 'radial'
            - 'directional'
            If not defined, the default value is used.

    Returns
    -------
    object
            Returns an object 'ret' with the following member:
            ret.meshed_ents: a list of successfully meshed entities (Faces and/or Shells).

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                mesh.Create4SidedMesh(
                    0,
                    only_4sided=True,
                    only_aligned=False,
                    corner_angle=60,
                    smooth_type="standard",
                    spacing="map_opposite_sides",
                )


    """


def CreateCircularMesh(
    entities: object,
    only_circular: bool,
    only_even: bool,
    radius_tol: bool,
    pattern: str,
    zones: int,
    layers: int,
    first_height: float,
    growth_factor: float,
    max_aspect: float,
) -> object:
    """

    This function uses Circular mesh generator to produce mesh patterns for circular areas.
    It works for both macros and FE shells.

    Parameters
    ----------
    entities : object
            A list of faces and/or shells.
            If entities equals to 0, the visible faces and shells are used.

    only_circular : bool, optional
            If set to True, only macros identified as circular are meshed.

    only_even : bool, optional
            If set to True, only macros with even number of perimeter nodes are meshed.

    radius_tol : bool, optional
            The maximum deviation percentage (%) between
            actual min/max radius and the radius of the equivalent circle.
            If not defined, the default value is used.

    pattern : str, optional
            Pattern can be one of the following strings:
            - 'default'
            - 'o-grid'
            - 'radial'
            If not defined, the default value is used.

    zones : int, optional
            The desired number of zones around mesh pattern.
            If not defined, the default value is used (automatic calculation).
            Pie mesh can be produced with Radial mesh pattern with zero (0) zones.

    layers : int, optional
            The desired number of layers around o-grid mesh pattern.
            If not defined, no layers will be added.
            This option is taken into account, only if pattern is o-grid.

    first_height : float, optional
            The width of the first layer zone.
            If not defined, the default value is used.
            It is taken into account, only in cases that layers option works.

    growth_factor : float, optional
            The growth factor applied on layers' width successively.
            If not defined, the default value is used.
            It is taken into account, only in cases that layers option works.

    max_aspect : float, optional
            The maximum accepted aspect of elements in layers.
            If not defined, the default value is used.
            It is taken into account, only in cases that layers option works.

    Returns
    -------
    object
            Returns an object 'ret' with the following member:
            ret.meshed_ents: a list of successfully meshed entities (Faces and/or Shells).

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import mesh


            def main():
                mesh.CreateCircularMesh(0, only_circular=True, radius_tol=10, pattern="o-grid")


    """


def VolumesCheckDefinition(volume: object) -> int:
    """

    The function checks if the volume definition is valid for mesh generation

    Parameters
    ----------
    volume : object
            The volume to be checked

    Returns
    -------
    int
            Returns 1 in case the definition is ok or 0 otherwise

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            def main():
                volume = base.GetEntity(ansa.constants.NASTRAN, "VOLUME", 1)
                mesh.VolumesCheckDefinition(volume)


    """


def AddFilterToOctreeArea(
    field: str,
    expression: str,
    value: str,
    area: object,
    match: str,
    case_sensitive: str,
    filter_name: str,
) -> int:
    """

    The function adds a filter to an existing octree entity or octree area, much like the way it is done through the Octree.
    If the area has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.

    Parameters
    ----------
    field : str
            Field Name.

    expression : str
            Expression.

    value : str
            The value that the expression will evaluate.

    area : object
            The octree area or octree entity the filter will be added into.

    match : str, optional
            Determines if all the filter rows must be matched. Use "all" or "any" to change
            the value.

    case_sensitive : str, optional
            Determines if the filter will be case sensitive. Use "yes" or "no" to change
            the value.

    filter_name : str, optional
            Give a specific name to a filter.

    Returns
    -------
    int
            Returns 1 if the filter was successfully created, or 0 otherwise.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                areas = mesh.GetAreasFromOctree(octree)
                mesh.AddFilterToOctreeArea(
                    field="visible", expression="equals", value="", match="all", area=areas[0]
                )


    """


def AddPartsToOctreeArea(entities: object, area: object) -> int:
    """

    This function adds a list of properties or parts or groups to an octree area or an otcree entity.

    Parameters
    ----------
    entities : object
            References the entities to be added to the area. The type of the entities may be a part, group or property.

    area : object
            The octree area or the octree entity the entities will be added to.

    Returns
    -------
    int
            Returns 1 if the entities and the area are valid entities, or 0 otherwise.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL")
                areas = mesh.GetAreasFromOctree(octree)
                mesh.AddPartsToOctreeArea(entities=props, area=areas[0])


    """


def GetNewOctreeArea(
    parent_octree: object,
    name: str,
    min_len: float,
    max_len: float,
    max_vol_len: float,
    part_pid_proximity: bool,
    self_proximity: bool,
    curvature_min_len: float,
) -> object:
    """

    This function adds a new octree area in an octree entity.

    Parameters
    ----------
    parent_octree : object
            References the octree entity where the area will be added.

    name : str, optional
            The name of the octree parameters of the created area.

    min_len : float, optional
            Area specific minimum length value.

    max_len : float, optional
            Area specific maximum length value.

    max_vol_len : float, optional
            Area specific maximum volume length value.

    part_pid_proximity : bool, optional
            Enables proximity refinement between different parts/properties.

    self_proximity : bool, optional
            Enables self-proximity refinement in a part/property.

    curvature_min_len : float, optional
            Area specific curvature minimum length value.

    Returns
    -------
    object
            Returns a reference to the newly created area.
            In case of an error, the function returns None.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                vals = {"Name": "new octree"}
                octree = base.CreateEntity(constants.NASTRAN, "HEXTREME OCTREE", vals)
                area = mesh.GetNewOctreeArea(octree, "new_area_params")


    """


def GetPartsFromOctreeArea(area: object) -> object:
    """

    This function collects all the parts, groups or properties that are included in a specific octree area or an  octree entity.

    Parameters
    ----------
    area : object
            The octree area or the octree entity that its items will be returned.

    Returns
    -------
    object
            Returns a list containing all the parts, groups or properties that belong to the specific octre area or octree entity.
            In case the octree area is not valid or it does not contain any parts, an empty list is returned.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddFilterToOctreeArea, GetNewOctreeArea, AddPartsToOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                parts = mesh.GetPartsFromOctreeArea(area=octree)
                print(len(parts))


    """


def GetAreasFromOctree(octree: object) -> object:
    """

    The function collects all areas belonging to a particular octree entity.

    Parameters
    ----------
    octree : object
            References the octree entity under consideration.

    Returns
    -------
    object
            Returns a list containing all the areas that belong to the specific octree entity.
            In case octree is not valid or it does not contain any areas, an empty list is returned.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddFilterToOctreeArea, GetNewOctreeArea, AddPartsToOctreeArea, GetPartsFromOctreeArea, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                oct = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                areas = mesh.GetAreasFromOctree(octree=oct)
                print(len(areas))


    """


def ReadOctreeAreaParams(area: object, mpar_file: str) -> int:
    """

    This function reads octree parameters from a specific file and assigns them to an octree area or to an octree entity.

    Parameters
    ----------
    area : object
            References the octree area or the octree entity that will get the values.

    mpar_file : str
            The path of the file containing the parameters.

    Returns
    -------
    int
            Returns 1 if area is valid and the file exists, or 0 otherwise.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddFilterToOctreeArea, GetNewOctreeArea, AddPartsToOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                ret_val = mesh.ReadOctreeAreaParams(area=octree, mpar_file="/ansa/params.ansa_mpar")
                print(ret_val)


    """


def SaveOctreeAreaParams(area: object, mpar_file: str):
    """

    This function saves octree parameters of an octree area or an octree entity to a specific file.

    Parameters
    ----------
    area : object
            References the octree area or the octree entity that will get the values.

    mpar_file : str
            The path of the file that the parameters will be saved to.

    See Also
    --------
    base.CreateEntity, RunOctree, ApplyOctreeFilters, CheckOctreeLeaks, AddFilterToOctreeArea, GetNewOctreeArea, AddPartsToOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                ret_val = mesh.SaveOctreeAreaParams(area=octree, mpar_file="/ansa/params.ansa_mpar")
                print(ret_val)


    """


def RotatingInterfaceAxis(rotating_entities: object) -> object:
    """

    Automatic calculation of the axis of rotation of wheels.
    The function calculates the axis of rotation even if the wheel is not whole usually in case of scanned wheels.

    Parameters
    ----------
    rotating_entities : object
            A list of ansa entities.
            These entities may be faces or shells.

    Returns
    -------
    object
            Returns the axis of rotation with a curve in case of success.
            Returns None in case of failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                rot_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                rot_ents = base.CollectEntities(constants.NASTRAN, rot_set, ["SHELL", "FACE"])

                mesh.RotatingInterfaceAxis(rot_ents)


    """


def HexaBlockSetIjk(box: object, origin_hb_pnt: object, i_hb_pnt: object) -> bool:
    """

    Sets to box a coordinate system by setting the origin and i hexablock point. The
    origin and i point must be on the same edge. The rest of the vectors of the
    coordinate system are calculated from the previous points. The box can be only
    HEXA.

    Parameters
    ----------
    box : object
            The HEXA_BOX which the coordinate system will be
            set. The box can be only hexahedral.

    origin_hb_pnt : object
            The HEXA_BOX_POINT from which the coordinate system
            will start.

    i_hb_pnt : object
            The HEXA_BOX_POINT to which the vector I will
            end.

    Returns
    -------
    bool
            Returns True if the operation was successful.

    See Also
    --------
    HexaBlockAlignIjk, HexaBlockResetIjk

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base


            def main():
                arg1 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 45)
                arg2 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 2960)
                arg3 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_POINT", 2920)
                print(ansa.mesh.HexaBlockSetIjk(arg1, arg2, arg3))


            if __name__ == "__main__":
                main()


    """


def HexaBlockAlignIjk(guide_box: object, boxes_to_align: object) -> bool:
    """

    Aligns HEXA_BOX entities according to guide_box. If the topology of boxes is not
    structured then no alignment will be applied.

    Parameters
    ----------
    guide_box : object
            Sets the guide box that the rest of the boxes will be
            aligned with.

    boxes_to_align : object
            List of HEXA_BOX entities that are going to be aligned with the guide box.

    Returns
    -------
    bool
            Returns true if the procedure is successful.

    See Also
    --------
    HexaBlockSetIjk, HexaBlockResetIjk

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import base


            def main():
                arg1 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 45)
                arg2 = []
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 40))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 44))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 48))
                print(ansa.mesh.HexaBlockAlignIjk(arg1, arg2))


            if __name__ == "__main__":
                main()


    """


def HexaBlockResetIjk(boxes: object):
    """

    Resets Ijk coordinate system to the default one.

    Parameters
    ----------
    boxes : object
            List of HEXA_BOX that are going to be reset.

    See Also
    --------
    HexaBlockSetIjk, HexaBlockAlignIjk

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import base


            def main():
                arg2 = []
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 40))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 44))
                arg2.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 48))
                ansa.mesh.HexaBlockResetIjk(arg2)


            if __name__ == "__main__":
                main()


    """


def LeakTool(
    mpar_file: str,
    sampling_length: float,
    group_leaks: bool,
    close_leaks: bool,
    chosen_properties: object,
    seed_points: object,
    leak_points: object,
    seal_and_wrap_inner_volumes: bool,
    accuracy: str,
) -> bool:
    """

    This function detects leaks, providing the ability to group and close them.

    Parameters
    ----------
    mpar_file : str, optional
            The path of the file containing the parameters.

    sampling_length : float, optional
            Minimum target length of octree on the surface of the model.

    group_leaks : bool, optional
            Group leaks by properties and parts.
            False disabled, True enabled. Default value: False.

    close_leaks : bool, optional
            Close detected leaks.
            False disabled, True enabled. Default value: False.

    chosen_properties : object, optional
            An array of sets of properties where leaks are biased to be identified and closed.

    seed_points : object, optional
            A list of ANSA entities.
            These entities must be points.

    leak_points : object, optional
            A list of ANSA entities.
            These entities must be points.

    seal_and_wrap_inner_volumes : bool, optional
            Seal and wrap inner detected leaked volumes.
            False disabled, True enabled. Default value: False.

    accuracy : str, optional
            Accuracy level for the leak tool.
            It can be low, medium, or high.
            Higher levels need more time but may find some leaks better.

    Returns
    -------
    bool
            Returns True if there are any leaks and False otherwise.
            Returns None if not a mpar_file exists or invalid length.

    See Also
    --------
    MergeLeakToolLeaks

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                properties_set = base.GetEntity(constants.NASTRAN, "SET", 1)
                seed_points = base.CollectEntities(constants.NASTRAN, None, "POINT")

                ret_val = mesh.LeakTool(
                    mpar_file="/ansa/params.ansa_mpar",
                    sampling_length=5.0,
                    close_leaks=True,
                    chosen_properties=properties_set,
                    seed_points=seed_points,
                    seal_and_wrap_inner_volumes=False,
                    accuracy="low",
                )
                print(ret_val)


    """


def AddContentsToSizeFieldRule(entities: object, rule: object) -> bool:
    """

    This function adds a list of entities to a SizeField rule.

    Parameters
    ----------
    entities : object
            References the entities to be added to the rule. The type of the entities may be a part, group,  property, curve, point or sizebox.

    rule : object
            The SizeFIeld rule the entities will be added to.

    Returns
    -------
    bool
            Returns True if the entities and the rule are valid entities, or False otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                close_surf = mesh.GetNewSizeFieldClosedSurfaceRule(
                    size_field=sf, name="close_surface", max_surf_len=1, max_vol_len=3
                )
                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL")

                mesh.AddContentsToSizeFieldRule(entities=props, rule=close_surf)


    """


def GetContentsFromSizeFieldRule(rule: object):
    """

    This function collects all the contents that are included in a specific SizeField rule.

    Parameters
    ----------
    rule : object
            The SizeField rule that its items will be returned.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(sf)

                contents = mesh.GetContentsFromSizeFieldRule(sf_rules[0])

                print(len(contents))


    """


def SaveSizeFieldRuleParams(rule: object, mpar_file: str):
    """

    This function saves parameters of of a SizeField rule to a specific file.

    Parameters
    ----------
    rule : object
            References the SizeField rule that will get the values.

    mpar_file : str
            The path of the file that the parameters will be saved to.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                ret_val = mesh.SaveSizeFieldRuleParams(
                    rule=sf_rules[0], mpar_file="/ansa/params.ansa_mpar"
                )
                print(ret_val)


    """


def ReadSizeFieldRuleParams(rule: object, mpar_file: str) -> bool:
    """

    This function reads parameters from a specific file and assigns them to a SizeField rule.

    Parameters
    ----------
    rule : object
            References the SizeField rule that will get the values.

    mpar_file : str
            The path of the file containing the parameters.

    Returns
    -------
    bool
            Returns True if rule is valid and the file exists, or False otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                ret_val = mesh.ReadSizeFieldRuleParams(
                    rule=sf_rules[0], mpar_file="/ansa/params.ansa_mpar"
                )
                print(ret_val)


    """


def AddFilterToSizeFieldRule(
    field: str,
    expression: str,
    value: str,
    rule: object,
    match: str,
    case_sensitive: str,
    filter_name: str,
) -> int:
    """

    The function adds a filter to an existing SizeField rule, much like the way it is done through the Octree.
    If the area has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.

    Parameters
    ----------
    field : str
            Field Name.

    expression : str
            Expression.

    value : str
            The value that the expression will evaluate.

    rule : object
            The SizeField rule the filter will be added into.

    match : str, optional
            Determines if all the filter rows must be matched. Use "all" or "any" to change

    case_sensitive : str, optional
            Determines if the filter will be case sensitive. Use "yes" or "no" to change

    filter_name : str, optional
            Give a specific name to a filter.

    Returns
    -------
    int
            Returns 1 if the filter was successfully created, or 0 otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                mesh.AddFilterToSizeFieldRule(
                    field="visible", expression="equals", value="", match="all", rule=sf_rules[0]
                )


    """


def GetRulesFromSizeField(size_field: object):
    """

    The function collects all rules belonging to a particular SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity under consideration.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(sf)


    """


def BuildSizeField(size_field: object) -> bool:
    """

    This function builds the defined SizeField.

    Parameters
    ----------
    size_field : object
            The input SizeField entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(constants.NASTRAN, "SIZE FIELD", 1)

                mesh.BuildSizeField(size_field)


    """


def GetNewSizeFieldClosedSurfaceRule(
    size_field: object, name: str, max_surf_len: float, max_vol_len: float
):
    """

    This function adds a new closed surface rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    max_surf_len : float, optional
            Rule specific maximum surface length value.

    max_vol_len : float, optional
            Rule specific maximum volume length value.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                close_surf = mesh.GetNewSizeFieldClosedSurfaceRule(
                    size_field=sf, name="close_surface", max_surf_len=1, max_vol_len=3
                )

                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL")

                mesh.AddContentsToSizeFieldRule(entities=props, rule=close_surf)


    """


def GetNewSizeFieldSurfaceOffsetRule(
    size_field: object,
    name: str,
    max_surf_len: float,
    max_vol_len: float,
    offset: float,
):
    """

    This function adds a new surface offset rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    max_surf_len : float, optional
            Rule specific maximum surface length value.

    max_vol_len : float, optional
            Rule specific maximum volume length value.

    offset : float, optional
            Rule specific offset value.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                surf_off = mesh.GetNewSizeFieldSurfaceOffsetRule(
                    size_field=sf,
                    name="surface_offset",
                    max_surf_len=100,
                    max_vol_len=300,
                    offset=10,
                )

                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL")

                mesh.AddContentsToSizeFieldRule(entities=props, rule=surf_off)


    """


def GetNewSizeFieldCylinderRule(
    size_field: object,
    name: str,
    max_surf_len: float,
    max_vol_len: float,
    radius: float,
):
    """

    This function adds a new cylinder rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    max_surf_len : float, optional
            Rule specific maximum surface length value.

    max_vol_len : float, optional
            Rule specific maximum surface length value.

    radius : float, optional
            Rule specific radius value.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                cyl = mesh.GetNewSizeFieldCylinderRule(
                    size_field=sf, name="cylinder", max_surf_len=1, max_vol_len=3, radius=10
                )

                curve = base.CollectEntities(constants.NASTRAN, None, "CURVE")

                mesh.AddContentsToSizeFieldRule(entities=curve, rule=cyl)


    """


def GetNewSizeFieldSphereRule(
    size_field: object,
    name: str,
    max_surf_len: float,
    max_vol_len: float,
    radius: float,
):
    """

    This function adds a new sphere rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    max_surf_len : float, optional
            Rule specific maximum surface length value.

    max_vol_len : float, optional
            Rule specific maximum volume length value.

    radius : float, optional
            Rule specific radius value.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                sphere = mesh.GetNewSizeFieldSphereRule(
                    size_field=sf, name="sphere", max_surf_len=1, max_vol_len=3, radius=10
                )

                point = base.CollectEntities(constants.NASTRAN, None, "POINT")

                mesh.AddContentsToSizeFieldRule(entities=point, rule=sphere)


    """


def GetNewSizeFieldSizeBoxRule(
    size_field: object, name: str, max_surf_len: float, max_vol_len: float
):
    """

    This function adds a new sizebox rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    max_surf_len : float, optional
            Rule specific maximum surface length value.

    max_vol_len : float, optional
            Rule specific maximum volume length value.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                sbox = mesh.GetNewSizeFieldSizeBoxRule(
                    size_field=sf, name="size_box", max_surf_len=1, max_vol_len=3
                )

                size_box = base.CollectEntities(constants.NASTRAN, None, "SIZE_BOX")

                mesh.AddContentsToSizeFieldRule(entities=None, rule=sbox)


    """


def SetSizeFieldRuleActive(rule: object, active: bool):
    """

    This function sets a SizeField rule active.

    Parameters
    ----------
    rule : object
            References the SizeField rule to set active.

    active : bool
            True to activate the rule, False to de-activate the rule

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, IsSizeFieldRuleActive, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                mesh.SetSizeFieldRuleActive(sf_rules[0], True)


    """


def IsSizeFieldRuleActive(rule: object) -> bool:
    """

    This function checks if a SizeField rule is active.

    Parameters
    ----------
    rule : object
            References the SizeField rule to check if active.

    Returns
    -------
    bool
            Returns True if active , False if not active
            In case of an error, the function returns None.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                print(mesh.IsSizeFieldRuleActive(sf_rules[0]))


    """


def SmoothShells(shells: object) -> int:
    """

    The function perfrorms Smooth on shells given by the user.

    Parameters
    ----------
    shells : object
            A list with the shells to be smoothed.

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                mesh.SmoothShells(shells)


    """


def TurbomachineryTemplate(parameters: str) -> bool:
    """

    A function to create a turbomachinery topology with the input parameters.

    Parameters
    ----------
    parameters : str
            A file that contains all the parameters of the template.

    Returns
    -------
    bool
            Returns True on success, False on failure.

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa


            def main():
                file = "/home/username/templates/stator_parameters.txt"
                ansa.mesh.TurbomachineryTemplate(file)


            if __name__ == "__main__":
                main()


    """


def CloseOctreeLeaks(octree: object, chosen_properties: object) -> bool:
    """

    This function closes automatically all detected octree leaks in order to make the model watertight.

    Parameters
    ----------
    octree : object
            The input octree entity.

    chosen_properties : object, optional
            An array of sets of properties where leaks are biased to be identified and closed.

    Returns
    -------
    bool
            Returns True if managed to make the model watertight.
            Returns False if did not manage to build the octree entity.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)
                properties_set = base.GetEntity(constants.NASTRAN, "SET", 1)
                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.CloseOctreeLeaks(octree, properties_set)


    """


def Outline(
    dir_x: float, dir_y: float, dir_z: float, outline_internal_detected_voids: bool
) -> object:
    """

    Creates curves from the external outilne of a projected geometry on given plane

    Parameters
    ----------
    dir_x : float
            X coordinate of plane vector

    dir_y : float
            Y coordinate of plane vector

    dir_z : float
            Z coordinate of plane vector

    outline_internal_detected_voids : bool, optional
            Option to create curves also for the detected internal voids.

    Returns
    -------
    object
            Returns an object containing the following:
            ret.frontal_area_curves :(list)A list with the created curves of skins of the projected geometries.
            ret.gaps_holes_curves   :(list)A list with the created curves of gap/hole skins of the projected geometries.
            ret.frontal_area_filled :(float)Frontal area with gap/holes filled.
            ret.frontal_area        :(float)Frontal area.
            ret.gaps_holes_area     :(float)Gaps/holes area

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                ret = mesh.Outline(1, 0, 0, outline_internal_detected_voids=True)

                print("Frontal_curves_num =", len(ret.frontal_area_curves))
                print("Gaps_curves_num =", len(ret.gaps_holes_curves))
                print("Frontal area =", ret.frontal_area)
                print("Frontal area filled =", ret.frontal_area_filled)
                print("Gaps/holes area =", ret.gaps_holes_area)


    """


def GetFEPerimeterShells(fe_perimeters: object, expand_to_macro: bool) -> object:
    """

    This function returns the shells that lie on the edges of a FE perimeter. If "expand_to_macro" option is True, then it returns all the macro shells, grouped by macro.

    Parameters
    ----------
    fe_perimeters : object
            A list that contains FE perimeters. If it is set to 0, visible FE perimeters will be used.

    expand_to_macro : bool, optional
            If it is set to True, all the macro shells will be returned.

    Returns
    -------
    object
            If "expand_to_macro" option is False, it returns a list that contains all the shells that were found. If "expand_to_macro" option is True, then it returns a list of lists, that contain the macro shells grouped by macro.

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import *


            def main():
                fe_perimeters = base.CollectEntities(constants.NASTRAN, None, "FE PERIMETER")
                fe_perimeter_shells = mesh.GetFEPerimeterShells(
                    fe_perimeters, expand_to_macro=False
                )
                print(fe_perimeter_shells)

                macros = mesh.GetFEPerimeterShells(fe_perimeters, expand_to_macro=True)
                for macro in macros:
                    print(macro)


            if __name__ == "__main__":
                main()


    """


def BuildAdaptivityField(adaptivity_field: object) -> bool:
    """

    This function builds the defined AdaptivityField.

    Parameters
    ----------
    adaptivity_field : object
            The input AdaptivityField entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    CreateNewAdaptivityField, SetAdaptivityFieldActive, IsAdaptivityFieldActive, SetAdaptivityFieldCsvPath

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                adaptivity_field = base.GetEntity(constants.NASTRAN, "SIZE FIELD", 1)

                mesh.BuildAdaptivityField(adaptivity_field)


    """


def CreateNewAdaptivityField(
    name: str,
    scale_factor: float,
    min_length: float,
    max_length: float,
    symmetry_mirror: bool,
) -> object:
    """

    This function creates a new AdaptivityField entity

    Parameters
    ----------
    name : str, optional
            Name of the newly created AdaptivityField

    scale_factor : float, optional
            Scale factor to convert units of adaptivity data

    min_length : float, optional
            Minimum length of adaptivity field

    max_length : float, optional
            Maximum length of adaptivity field

    symmetry_mirror : bool, optional
            Option to mirror adaptivity data to the default symmetry plane

    Returns
    -------
    object
            Returns the newly created AdaptivityField

    See Also
    --------
    BuildAdaptivityField, SetAdaptivityFieldActive, IsAdaptivityFieldActive, SetAdaptivityFieldCsvPath

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                adaptivity_field = mesh.CreateNewAdaptivityField()


    """


def SetAdaptivityFieldCsvPath(adaptivity_field: object, csv_file_path: str):
    """

    This function sets the path of the csv file with the adaptivity data

    Parameters
    ----------
    adaptivity_field : object
            The input AdaptivityField entity

    csv_file_path : str
            The path of the csv file with the adaptivity data

    See Also
    --------
    CreateNewAdaptivityField, BuildAdaptivityField, SetAdaptivityFieldActive, IsAdaptivityFieldActive

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                adaptivity_field = mesh.CreateNewAdaptivityField()

                mesh.SetAdaptivityFieldCsvPath(adaptivity_field, "path")


    """


def SetAdaptivityFieldActive(adaptivity_field: object, active: bool):
    """

    This function sets an AdaptivityField active.

    Parameters
    ----------
    adaptivity_field : object
            References the AdaptivityField to set active.

    active : bool
            True to activate the rule, False to de-activate the rule

    See Also
    --------
    CreateNewAdaptivityField, BuildAdaptivityField, IsAdaptivityFieldActive, SetAdaptivityFieldCsvPath

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                adaptivity_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                mesh.SetAdaptivityFieldActive(adaptivity_field, True)


    """


def IsAdaptivityFieldActive(adaptivity_field: object) -> bool:
    """

    This function checks if an AdaptivityField is active.

    Parameters
    ----------
    adaptivity_field : object
            References the AdaptivityField to check if active.

    Returns
    -------
    bool
            Returns True if active , False if not active
            In case of an error, the function returns None.

    See Also
    --------
    CreateNewAdaptivityField, BuildAdaptivityField, SetAdaptivityFieldActive, SetAdaptivityFieldCsvPath

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                adaptivity_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                print(mesh.IsAdaptivityFieldActive(adaptivity_field))


    """


def ConvertSizeBoxesToSizeField(size_boxes: object, size_field: object) -> object:
    """

    This function converts all the SizeBoxes of the database or a list of given SizeBoxes to a new or given SizeField.

    Parameters
    ----------
    size_boxes : object, optional
            List of SizeBoxes to convert to SizeField.

    size_field : object, optional
            Already existing SizeField to add the new SizeBox rules.

    Returns
    -------
    object
            Returns the SizeField that the new SizeBox rules are added to on success.
            Returns None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sb1 = base.GetEntity(constants.NASTRAN, "SIZE_BOX", 1)

                sb2 = base.GetEntity(constants.NASTRAN, "SIZE_BOX", 3)

                sbs = [sb1, sb2]

                sf = base.GetEntity(constants.NASTRAN, "SIZE FIELD", 2)

                size_field = mesh.ConvertSizeBoxesToSizeField(size_boxes=sbs, size_field=sf)


    """


def CopySizeFieldRules(rules: object, size_field: object) -> bool:
    """

    The function copies given SizeField rules to another SizeField

    Parameters
    ----------
    rules : object
            A list of the SizeField rules to be copied.

    size_field : object
            References the destination SizeField entity.

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, MoveSizeFieldRules, MergeSizeFields

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf1 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf2 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 2)

                sf_rules = mesh.GetRulesFromSizeField(sf1)

                mesh.CopySizeFieldRules(sf_rules, sf2)


    """


def MoveSizeFieldRules(rules: object, size_field: object) -> bool:
    """

    The function moves given SizeField rules to another SizeField

    Parameters
    ----------
    rules : object
            A list of the SizeField rules to be moved.

    size_field : object
            Destination SizeField entity.

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MergeSizeFields

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf1 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf2 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 2)

                sf_rules = mesh.GetRulesFromSizeField(sf1)

                mesh.MoveSizeFieldRules(sf_rules, sf2)


    """


def MergeSizeFields(size_fields: object) -> object:
    """

    The function merges a list of given SizeField entities

    Parameters
    ----------
    size_fields : object
            A list of SizeField entities to be merged.

    Returns
    -------
    object
            Returns the merged SizeField entity

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules

    Examples
    --------
    ::

            def main():
                sf1 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf2 = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 2)

                sfs = [sf1, sf2]

                mesh.MergeSizeFields(sfs)


    """


def SmoothHexaField(hexas: object, smooth_iterations: int) -> bool:
    """

    Smooths a given hexa field

    Parameters
    ----------
    hexas : object
            The hexas to be smoothed.

    smooth_iterations : int
            The number of smooth iterations

    Returns
    -------
    bool
            Returns True on success and False on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                hexas = base.CollectEntities(constants.NASTRAN, None, ["SOLID"])

                ret = mesh.SmoothHexaField(hexas, 3)


    """


def FillGapBridge(
    input: object, improve_result_zones: int, result_set: object, ret_ents: bool
) -> int:
    """

    This function creates FE shells to fill a gap defined by cons, curves or edges.
    Each call of the function fills a single gap.
    A single gap defined only by curves can not be filled.

    Parameters
    ----------
    input : object
            A list of cons, curves, sets of edges.

    improve_result_zones : int, optional
            Improves the quality of the result FE shells and [user defined] zones
            around them.

    result_set : object, optional
            Adds the result FE shells to a [user defined] set.

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    Returns
    -------
    int
            Returns the number of the created FE shells (before mesh improvement).
            If ret_ents=True it will return a list with the created entities or None if no entities are created.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                # Check how the syntax in each case should be
                input = []
                input.append(base.GetEntity(constants.NASTRAN, "CONS", 1923054))
                input.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                input.append(base.GetEntity(constants.NASTRAN, "SET", 1))
                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                mesh.FillGapBridge(input, improve_result_zones=0, result_set=set)


    """


def ApplySizeFieldFilters(size_field: object) -> bool:
    """

    This function applies the defined filters, in order to load the wanted parts, groups or pids to the size field and distribute them to the proper rule.

    Parameters
    ----------
    size_field : object
            The input size field.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sfield = base.GetEntity(constants.NASTRAN, "SIZE FIELD", 1)

                if sfield == None:
                    print("SIZE FIELD with ID 1 does not exist!")
                else:
                    mesh.ApplySizeFieldFilters(sfield)


    """


def CheckMiddleMesh(
    shells: object,
    faces: object,
    options: object,
    check_for_unconnected: bool,
    return_ents: bool,
    min_nodal_thick: float,
) -> object:
    """

    This function checks middle mesh result taking into account both align constraints (if they exist) and real solid
    description. The following checks are performed (in parentheses the option value for the respective check):

    - Align Definition:
            - Shells belonging to empty align area constraints are identified and reported (align_empty_areas).
            - Shells belonging to empty align perimeter constraints are identified and reported (align_empty_perimeters).
            - Position of shells' nodes with respect to correct middle position according to area align constraints
              (align_middle).
            - Shells' thickness with respect to thickness calculated from align constraints definition (align_thickness).
            - Position of shells' nodes with respect to correct boundary position according to perimeter align constraints
              (align_boundary).
    - Middle Surface:
            - Position of shells' nodes with respect to middle position calculated from solid description (solid_middle).
            - Shells' thickness with respect to thickness calculated from solid description (solid_middle).
            - Position of shells' nodes with respect to solid description boundaries (solid_boundary).
    - Incompatible: checks if a shell's nodes belong to 2 or more align constraints with different align positions
      (incompatible).
    - Missing Mass: identifies areas in model where middle mesh is not created for the solid description (missing_mass).
    - Unconnected: checks if there are shell mesh connectivity groups in model that are not connected properly with
      each other (check_for_unconnected).
    - Nodal Thickness: checks shells' nodal thickness with respect to a minimum value and nodal thicknesses deviation
      (gradient) inside each shell (nodal_thickness and min_nodal_thick).

    Parameters
    ----------
    shells : object
            A list of shells for which checks will be performed.

    faces : object
            A list of faces for which checks will be performed.

    options : object, optional
            A dictionary with options regarding which checks will be performed and the
            tolerance of those checks. Both key's ans value's type is string.
            Tolerance could be either absolute or a percentage of thickness values.
            For "incompatible" check the tolerance is either an absolute or a percentage
            value of mesh target length.
            For "missing_mass" check the tolerance is an option from the
            following "Strict, Mild, Loose" as they are in GUI. (default: Mild)
            For "align_empty_areas" and "align_empty_perimeters" the tolerance values
            are not used, so the user doesn't have to provide a value.
            When a tolerance value is left empty or the provided value is invalid
            the default value is used.
            (Default: all checks with default tolerance values are performed)
            Example values:
            { "align_middle" : "5%",
              "align_boundary" : "0.15",
              "align_thickness" : "5%",
              "align_empty_areas" : "",
              "align_empty_perimeters" : "",
              "nodal_thickness" : "50%",
              "incompatible" : "50%",
              "solid_middle" : "5%",
              "solid_boundary" : "5%",
              "missing_mass" : "Mild" }
            The correspondence between the above options and GUI options that don't have
            the same name is the following:
            "Constraints" check includes "align_middle", "align_thickness"
            and "align_boundary".
            "Middle Surface" check includes "solid_middle" and "solid_boundary".

    check_for_unconnected : bool, optional
            If set to True the check for unconnected shell mesh connectivity groups
            is performed. (Default: True)

    return_ents : bool, optional
            If set to True a dictionary with a list of failed entities for every check
            performed is returned. (Default: True)

    min_nodal_thick : float, optional
            Minimum nodal thickness for which shells' thickness would be checked.
            Check is performed only if a value greater than 0 is provided and
            "nodal_thickness" is defined in options dictionary. (Default: 0.0)

    Returns
    -------
    object
            if return_ents is True then a dictionary with lists of entities for every check is returned, else None is returned.
            For the "unconnected" connectivity groups a list of lists of shells is returned in dictionary as a value.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")

                options = {
                    "align_middle": "5%",
                    "align_bound": "5%",
                    "align_thickness": "5%",
                    "align_empty_areas": "",
                    "align_empty_perimeters": "",
                    "incompatible": "10%",
                    "nodal_thickness": "50%",
                    "solid_middle": "5%",
                    "solid_boundary": "5%",
                    "missing_mass": "",
                }

                ret = mesh.CheckMiddleMesh(
                    shells,
                    faces,
                    options,
                    check_for_unconnected=True,
                    return_ents=True,
                    min_nodal_thick=0.0,
                )


    """


def HexaSphere(
    sphere_center: object,
    sphere_radius: float,
    number_of_perimeter_elements: int,
    light_volume_representation: bool,
    create_skin_shells: bool,
    part: object,
    solids_property: object,
    shells_property: object,
) -> bool:
    """

    Generates pure O-Grid Hexa mesh for spherical pattern.

    Parameters
    ----------
    sphere_center : object
            The coordinates of sphere's center.

    sphere_radius : float
            The radius of sphere.

    number_of_perimeter_elements : int
            The number of peripheral edges. It must be a positive integer and
            multiple of 4.

    light_volume_representation : bool, optional
            Create light solids. Optimized for large volume meshes.
            The default value is False.

    create_skin_shells : bool, optional
            If enabled, the skin quad shells will be created. Skin quad shells
            will be always created if light_volume_representation is True.
            The default value is False.

    part : object, optional
            Part that will be assigned to all created quads and hexas.
            If not provided the current part will be used.

    solids_property : object, optional
            Property that will be assigned to all created hexas.
            Applies only when light_volume_representation is False.
            If not provided, a new one will be created.

    shells_property : object, optional
            Property that will be assigned to all created skin shells.
            If not provided, a new one will be created.

    Returns
    -------
    bool
            Returns True if process completed successfully.
            In any other case, an exception will appear.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                center = (2, 2, 2)
                mesh.HexaSphere(center, 10.0, 32, False, True)


            if __name__ == "__main__":
                main()


    """


def MapBlock(macros: object) -> object:
    """

    MapBlock will detect Map Block volumes either from the given input geometry, or all db will be considered as input if argument is ommited. It will automatically define the appropriate caps and sides and will create surface mesh according to the defined mesh parameters and quality criteria.

    Parameters
    ----------
    macros : object, optional
            A list of macros that the algorithm will use to run. If not such a list is provided,
            the algorithm will run on whole database.

    Returns
    -------
    object
            Returns a list of the detected Map Block volumes.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                prop = base.GetEntity(constants.ABAQUS, "PSHELL", 1)
                input_macros = base.CollectEntities(constants.ABAQUS, prop, "FACE")
                volumes = mesh.MapBlock(input_macros)


            if __name__ == "__main__":
                main()


    """


def ReconstructSolids(zones: int) -> int:
    """

    This function reconstructs the violating solids and N neighboring zones.

    Parameters
    ----------
    zones : int
            The number of neighboring zones.

    Returns
    -------
    int
            Returns 0 in any case.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.ReconstructSolids(3)


    """


def GetMiddleMeshQualityScore(
    shells: object, faces: object, tol_dict: object
) -> object:
    """

    This functions evaluates the quality of middle mesh taking into account solid geometry definition and align constraints (if they exist). It examines if the mesh is actually in the middle position and has the correct thickness with regard to solid definition and takes into account areas that have missing mesh representation and provide a score. Furthermore, it evaluates areas with empty area constraints and empty align perimeter constraints and provides relevant scores.

    Parameters
    ----------
    shells : object
            A list of shells that would be evaluated.

    faces : object
            A list of faces which represent the solid geometry.

    tol_dict : object, optional
            A dictionary with the tolerance values that would be used. Both key's ans value's type is
            string.
            Example:
            { "middle_surface" : "10%",
              "missing_mass" : "Mild" }
            The "middle_surface" tolerance could be either an absolute value (e.g. 0.25) or
            a percentage of shell's thickness (default: "10%").
            The "missing_mass" tolerance could take one of the following values
            ("Loose", "Mild", "Strict") (default "Mild").
            If no values are given then the default values are used.

    Returns
    -------
    object
            A dictionary with three values is returned. For example a possible output is the following:
            { "middle_surface_score" : "95.5%", "align_areas_score" : "93.4%", "align_perimeters_score" : "91.2%" }
            The score values are in the range 0-100% with 100% being the best value.
            "middle_surface_score" represents the quality of the mesh with regard to solid geometry.
            "align_areas_score" is a metric of how many empty area constraints exist.
            "align_perimeters_score" is a metric of how many empty perimeter constraints exist.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")

                tol_dict = {"middle_surface": "10%", "missing_mass": "Mild"}

                ret = mesh.GetMiddleMeshQualityScore(shells, faces, tol_dict)


    """


def SolidBuilder(
    base_elems: object,
    auto_build: bool,
    inverted_dir: bool,
    extrude_method: str,
    new_solid_height: float,
    snap_angle: float,
    create_new_nodes: bool,
    part: object,
    prop: object,
) -> object:
    """

    SolidBuilder can create solids on given shells and solid facets. The function decides which Nodes will snap and can automatically fill areas to the top.

    Parameters
    ----------
    base_elems : object
            A list of shells or facets that will form the base of the new solids.

    auto_build : bool, optional
            If set to True, solid builder will create multiple layers of solids as long as there are nodes to snap. If set to False, solid builder will create only one layer.

    inverted_dir : bool, optional
            If set to False, solids will be created on the grey side of the given shells. Otherwise, solids will be created on the yellow side.

    extrude_method : str, optional
            May be either of these: "Absolute-Height Offset", "Auto-height Offset", "Interpolation"

    new_solid_height : float, optional
            The height the new nodes should have. Extrude method may affect the final height.

    snap_angle : float, optional
            Solids snap on nodes that form an angle to their base smaller than this value.

    create_new_nodes : bool, optional
            If set to False, only snapped nodes will be used. If True, new nodes will be created where nodes have not snapped.

    part : object, optional
            The part that will be assigned to the created solids.

    prop : object, optional
            The property that will be assigned to the created solids.

    Returns
    -------
    object
            A list with the top facets of new solids

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base, constants, mesh


            def main():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL")

                new_facets = mesh.SolidBuilder(
                    base_elems=shells,
                    auto_build=False,
                    inverted_dir=False,
                    extrude_method="Interpolation",
                    new_solid_height=15.0,
                    snap_angle=40.0,
                    create_new_nodes=True,
                )

                mesh.SolidBuilder(new_facets)


            if __name__ == "__main__":
                main()


    """


def SplitToTrias(entities: object, quad_method: str) -> int:
    """

    This function applies Split2Trias on shells and solid facets.

    Parameters
    ----------
    entities : object
            Accepted values: A list of shells and/or solid facets, "all", "visible", 0.
            If set to 0 or "all", runs for all shells of the database.
            If set to "visible," runs for visible shells.

    quad_method : str, optional
            Defines the split method for the quads.
            Can be: "oriented_hybrid", "oriented_1", "oriented_2", "quality_based", "violating", "split_x", "union_jack_hybrid", "union_jack_1" or "union_jack_2".
            (Default: "oriented_hybrid")

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.SplitToTrias("visible", "quality_based")


    """


def ExternalDetection(
    input_pids: object,
    forced_internal_pids_sets: object,
    forced_external_pids_sets: object,
    bottom_cameras_angle: object,
    bottom_cameras_upper_visibility_plane: object,
    external_mark_limit: float,
    overlaping_distance: float,
    merge_area_limit: float,
    merge_elements_limit: int,
    merge_mark_limit: float,
    create_scan_results: bool,
):
    """

    1. ExternalDetection script fun will apply a 3D scan around the model and will assign a visibility weight for each shell. The value is 0-100. 0 stands for zero visibility and 100 for full visibility.
    2. Each shell is marked as external or internal based on a threshold value given by the user.
    3. Connectivity groups of external and internal shells are created (islands)
    4. A merge algorithm takes place to change the mark of trapped islands. Each island that is surrounded by an invert mark island and meets an area, or number of elements, or maximum visibility weight criterion, will be merged to the neighbor island.
    5. New copies will be created from all existing PIDs with the suffix _External, _Internal. Each shell will be assigned to the proper PID. For debug reasons the user can select to create a result for each shell that stands for the scan visibility weight. Also the function will create 2 sets with the internal and external PIDs

    Parameters
    ----------
    input_pids : object
            A list that contains properties that will be used as input.

    forced_internal_pids_sets : object, optional
            Sets with PIDs that are known a priori to be internal.

    forced_external_pids_sets : object, optional
            Sets with PIDs that are known a priori to be external.

    bottom_cameras_angle : object, optional
            An angle between 0 and 180 that will define the bottom cameras views. Scan algorithm will ignore those cameras if "bottom_cameras_visibility_plane" is "of". If "bottom_cameras_visibility_plane" is given then it will ignore all elements visible from these cameras and are positioned upper to that plane.
            Value can be set also to "off".
            Default value is "off".

    bottom_cameras_upper_visibility_plane : object, optional
            The Z parallel plane which all bottom cameras will not scan above it.
            It is set as a double value, which is the z value, above which bottom cameras will not scan above.
            Value can be set "off".
            Default value is "off".

    external_mark_limit : float, optional
            The threshold that defines what is internal and what is external.
            Values can be from 0 to 100.
            Default value is 6.

    overlaping_distance : float, optional
            Every internal shell that has distance to an external shell lower than this value will be marked as external. This should not be used on clean wrap models, but only on dirty models with lots of overlapping parts.
            Default value is 0.

    merge_area_limit : float, optional
            Each connectivity group (external or internal) with area less than this value will try to be merged and change mark if it is surrounded by an opposite mark.
            Default value is 0.

    merge_elements_limit : int, optional
            Each connectivity group (external or internal) with number of elements less than this value will try to be merged and change mark if it is surrounded by an opposite mark.
            Default value is 30.

    merge_mark_limit : float, optional
            Each connectivity group (external only) that all shells have scan visibility weight less than this value will try to be merged and change mark if it is surrounded by an opposite mark.
            Default value is 12.

    create_scan_results : bool, optional
            Create results to visualize the visibility weights on each shell.
            Default value is False.

    See Also
    --------
    IsolateVisibilityGroups

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import mesh
            from ansa import base


            def main():
                pids = base.CollectEntities(0, None, "PSHELL", False)
                fint = base.GetEntity(ansa.constants.NASTRAN, "SET", 2)
                fext = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                mesh.ExternalDetection(
                    input_pids=pids,
                    forced_internal_pids_sets=fint,
                    forced_external_pids_sets=fext,
                    bottom_cameras_angle=0.0,
                    bottom_cameras_upper_visibility_plane="off",
                    external_mark_limit=6,
                    overlaping_distance=0.0,
                    merge_area_limit=0.0,
                    merge_elements_limit=30,
                    merge_mark_limit=12.0,
                    create_scan_results=True,
                )


    """


def ReadOctreeScenarioQualityCriteria(scenario: object, qual_criteria_file: str) -> int:
    """

    This function reads quality criteria from a specific file and assigns them to an octree scenario or to an octree entity.

    Parameters
    ----------
    scenario : object
            References the octree scenario or the octree entity that will get the values.

    qual_criteria_file : str
            The path of the file containing the criteria.

    Returns
    -------
    int
            Returns 1 if scenario is valid and the file exists, or 0 otherwise.

    See Also
    --------
    SaveOctreeScenarioQualityCriteria, GetOctreeScenarioQualityCriteriaName, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)
                ret_val = mesh.ReadOctreeScenarioQualityCriteria(
                    scenario=octree, qual_criteria_file="/ansa/criteria.ansa_qual"
                )
                print(ret_val)


    """


def SaveOctreeScenarioQualityCriteria(scenario: object, qual_criteria_file: str) -> int:
    """

    This function saves quality criteria of an octree scenario or an octree entity to a specific file.

    Parameters
    ----------
    scenario : object
            References the octree scenario or the octree entity that will get the values.

    qual_criteria_file : str
            The path of the file that the criteria will be saved to.

    Returns
    -------
    int
            Returns 1 if scenario is valid and the file exists, or 0 otherwise.

    See Also
    --------
    ReadOctreeScenarioQualityCriteria, GetOctreeScenarioQualityCriteriaName, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "HEXTREME OCTREE", 1)
                ret_val = mesh.SaveOctreeScenarioQualityCriteria(
                    scenario=octree, qual_criteria_file="/ansa/criteria.ansa_qual"
                )
                print(ret_val)


    """


def GetOctreeScenarioQualityCriteriaName(scenario: object) -> str:
    """

    This function returns the quality criteria name of an octree scenario or an octree entity.

    Parameters
    ----------
    scenario : object
            References the octree scenario or the octree entity of the wanted quality criteria name.

    Returns
    -------
    str
            Returns the quality criteria name of the octree scenario or the octree entity.

    See Also
    --------
    SaveOctreeScenarioQualityCriteria, ReadOctreeScenarioQualityCriteria, ReadOctreeAreaParams, SaveOctreeAreaParams

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(ansa.constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)
                ret_val = mesh.GetOctreeScenarioQualityCriteriaName(scenario=octree)
                print(ret_val)


    """


def GetNewSizeFieldSurfaceSectionRule(
    size_field: object,
    name: str,
    dir_dx: float,
    dir_dy: float,
    dir_dz: float,
    start_x: float,
    start_y: float,
    start_z: float,
    start_surf_len: float,
    end_x: float,
    end_y: float,
    end_z: float,
    end_surf_len: float,
):
    """

    This function adds a new surface section rule in a SizeField entity.

    Parameters
    ----------
    size_field : object
            References the SizeField entity where the rule will be added.

    name : str, optional
            The name of the rule parameters of the created rule.

    dir_dx : float, optional
            The x coordinate of the direction vector of the section rule.

    dir_dy : float, optional
            The y coordinate of the direction vector of the section rule.

    dir_dz : float, optional
            The z coordinate of the direction vector of the section rule.

    start_x : float, optional
            The x coordinate of the start point of the section rule.

    start_y : float, optional
            The y coordinate of the start point of the section rule.

    start_z : float, optional
            The z coordinate of the start point of the section rule.

    start_surf_len : float, optional
            The wanted surface length at the start point of the section rule.

    end_x : float, optional
            The x coordinate of the end point of the section rule.

    end_y : float, optional
            The y coordinate of the end point of the section rule.

    end_z : float, optional
            The z coordinate of the end point of the section rule.

    end_surf_len : float, optional
            The wanted surface length at the end point of the section rule.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, CopySizeFieldRules, MoveSizeFieldRules, MergeSizeFields, ApplySizeFieldFilters

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                sf = base.CreateEntity(constants.NASTRAN, "SIZE FIELD")

                surf_sect = mesh.GetNewSizeFieldSurfaceSectionRule(
                    size_field=sf,
                    name="surface_section_rule1",
                    dir_dx=0.0,
                    dir_dy=1.0,
                    dir_dz=0.0,
                    start_x=0.0,
                    start_y=0.0,
                    start_z=0.0,
                    start_surf_len=2.0,
                    end_x=0.0,
                    end_y=100.0,
                    end_z=0.0,
                    end_surf_len=5.0,
                )

                props = base.CollectEntities(constants.NASTRAN, None, "PSHELL")

                mesh.AddContentsToSizeFieldRule(entities=props, rule=surf_sect)


    """


def BuildOctree(octree: object) -> bool:
    """

    This function builds the defined octree.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams, RunOctree, VisualizeOctree, ControlOctreeVisualization

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.BuildOctree(octree)


    """


def VisualizeOctree(octree: object) -> bool:
    """

    This function visualizes the defined octree.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.

    See Also
    --------
    base.CreateEntity, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams, BuildOctree, RunOctree, ResetOctreeVisualizationCropArea, ControlOctreeVisualization

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.VisualizeOctree(octree)


    """


def ControlOctreeVisualization(
    octree: object,
    x_cut_plane: bool,
    x_direction: str,
    x_value: float,
    y_cut_plane: bool,
    y_direction: str,
    y_value: float,
    z_cut_plane: bool,
    z_direction: str,
    z_value: float,
    structure_cut_plane: bool,
    structure_cut_plane_distance: float,
    crop_x_min: float,
    crop_y_min: float,
    crop_z_min: float,
    crop_x_max: float,
    crop_y_max: float,
    crop_z_max: float,
    show_only_skin: bool,
    size_plot: bool,
    size_plot_type: str,
) -> bool:
    """

    This function controls the visualization of the defined octree entity.

    Parameters
    ----------
    octree : object
            The input octree entity.

    x_cut_plane : bool, optional
            Enables/disables the cutting plane on the X axis.

    x_direction : str, optional
            Defines the visible side of the X cut plane.
            Available options are "-", "+" and "slice" for no visible side.

    x_value : float, optional
            Defines the x value of the cutting plane on the X axis.

    y_cut_plane : bool, optional
            Enables/disables the cutting plane on the Y axis.

    y_direction : str, optional
            Defines the visible side of the Y cut plane.
            Available options are "-", "+" and "slice" for no visible side.

    y_value : float, optional
            Defines the y value of the cutting plane on the Y axis.

    z_cut_plane : bool, optional
            Enables/disables the cutting plane on the Z axis.

    z_direction : str, optional
            Defines the visible side of the Z cut plane.
            Available options are "-", "+" and "slice" for no visible side.

    z_value : float, optional
            Defines the z value of the cutting plane on the Z axis.

    structure_cut_plane : bool, optional
            Defines if the cutting planes will cut the structure too.

    structure_cut_plane_distance : float, optional
            Defines the distance between the structure cut plane and the octree cut plane.

    crop_x_min : float, optional
            Defines the visualization crop area minimum x value.

    crop_y_min : float, optional
            Defines the visualization crop area minimum y value.

    crop_z_min : float, optional
            Defines the visualization crop area minimum z value.

    crop_x_max : float, optional
            Defines the visualization crop area maximum x value.

    crop_y_max : float, optional
            Defines the visualization crop area maximum y value.

    crop_z_max : float, optional
            Defines the visualization crop area maximum z value.

    show_only_skin : bool, optional
            Defines whether only the skin facets of the octree volume will be drawn.

    size_plot : bool, optional
            Defines whether a color size plot wil be enabled.

    size_plot_type : str, optional
            Defines the type of the size plot.
            Available options are:
            "Octree" where the octree nodes are colored depending to their size.
            "Structure" where the octree input is colored depending to the octree size on each element.
            For Hextreme octrees the options "Layers num", "Layers first height" and "Layers total height" are also available.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.
            The octree must be built and visualized using OctreeBuild and OctreeVisualize functions.

    See Also
    --------
    base.CreateEntity, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams, BuildOctree, VisualizeOctree, ResetOctreeVisualizationCropArea, RunOctree

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.ControlOctreeVisualization(octree, x_value=1000.0)


    """


def ResetOctreeVisualizationCropArea(octree: object) -> bool:
    """

    This function resets the crop area of the visualization of the octree.

    Parameters
    ----------
    octree : object
            The input octree entity.

    Returns
    -------
    bool
            Returns True if the process completed succesfully and False otherwise.
            The octree must be built and visualized using OctreeBuild and OctreeVisualize functions.

    See Also
    --------
    base.CreateEntity, ApplyOctreeFilters, CheckOctreeLeaks, AddPartsToOctreeArea, AddFilterToOctreeArea, GetNewOctreeArea, GetPartsFromOctreeArea, GetAreasFromOctree, ReadOctreeAreaParams, SaveOctreeAreaParams, BuildOctree, RunOctree, ControlOctreeVisualization, VisualizeOctree

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                octree = base.GetEntity(constants.NASTRAN, "VARIABLE WRAP OCTREE", 1)

                if octree == None:
                    print("VARIABLE WRAP OCTREE with ID 1 does not exist!")
                else:
                    mesh.ResetOctreeVisualizationCropArea(octree)


    """


def CalculateSurfaceSectionRuleParamsFromDirection(
    rule: object, calc_points: bool, calc_lenghts: bool, chordal_fraction: float
):
    """

    This function calcSurfaceSectionSizeFieldRuleParametersFromDirection - Calculates rest surface section sizefield rule parameters based on the direction and the input

    Parameters
    ----------
    rule : object
            References the surface section SizeField rule for calculation.

    calc_points : bool, optional
            Defines whether the start and end point parameters will be calculated.
            Default value is True

    calc_lenghts : bool, optional
            Defines whether the start and end length parameters will be calculated.
            Default value is True

    chordal_fraction : float, optional
            The fraction of the chord length that will be set to lengths.
            Default value is 0.01.

    See Also
    --------
    base.CreateEntity, BuildSizeField, AddFilterToSizeFieldRule, GetNewSizeFieldClosedSurfaceRule, GetNewSizeFieldSurfaceOffsetRule, GetNewSizeFieldCylinderRule, GetNewSizeFieldSphereRule, GetNewSizeFieldSizeBoxRule, AddContentsToSizeFieldRule, GetContentsFromSizeFieldRule, GetRulesFromSizeField, ReadSizeFieldRuleParams, SaveSizeFieldRuleParams, SetSizeFieldRuleActive, IsSizeFieldRuleActive, ApplySizeFieldFilters, SetSizeFieldRuleActive

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                size_field = base.GetEntity(ansa.constants.NASTRAN, "SIZE FIELD", 1)

                sf_rules = mesh.GetRulesFromSizeField(size_field)

                mesh.CalculateSurfaceSectionRuleParamsFromDirection(sf_rules[0])


    """


def IsolateVisibilityGroups(
    input: object,
    groups_number: int,
    external_visibility_limit: float,
    classification: str,
    view_point: str,
    connectivity_groups_by: str,
    forced_internal_sets: object,
    forced_external_sets: object,
    overlapping_distance: float,
    merge_area_limit: float,
    merge_elements_limit: float,
    group_by_feature_lines: bool,
    feature_angle: float,
    feature_type: str,
) -> object:
    """

    This function separates the input entities to groups according to how visible from the outer they are.

    Parameters
    ----------
    input : object
            A list that can contain faces, shells and solids.

    groups_number : int
            The number of groups in which the input entities will be categorized.

    external_visibility_limit : float
            Defines a factor of how much visible the shell should be in order to be classified as external.
            It should be between 1. and 100.

    classification : str, optional
            Specifies the way the connectivity groups will be classified.
            They can be classified by an average value by the outermost or
            the innermost entity.
            Available options are "average", "outermost" and "innermost".
            (Default: "average")

    view_point : str, optional
            Specifies the view point from wich the model will be observed.
            Available options are "scan_all_around" and "normal_to_screen".
            Default value is "scan_all_around".

    connectivity_groups_by : str, optional
            Defines how the entities will be classified.
            Avalable options:
            "Entity" each entity will be classified to a visibility group alone
            "Property" each PID region will be classified to a visibility group
            Default value is "Entity".

    forced_internal_sets : object, optional
            Sets with entities or properties that are known a priori to be absolutely interior.

    forced_external_sets : object, optional
            Sets with entities or properties that are known a priori to be absolutely exterior.

    overlapping_distance : float, optional
            Every internal entity that has distance to an absolutely exterior entity lower than this value will be marked as external. This option is useful in dirty models with lots of overlapping parts.
            Default value is 0.

    merge_area_limit : float, optional
            Each connectivity group of a certain visibility group with area less than this value will try to be merged to another visibility group that is connected to it
            Default value is 0.

    merge_elements_limit : float, optional
            Each connectivity group of a certain visibility group with elements number less than this value will try to be merged to another visibility group that is connected to it
            Default value is 30.

    group_by_feature_lines : bool, optional
            Defines if the entities will be grouped based on feeature lines or not.
            If set to True, then all entities will be grouped based on the feature lines.
            If set to False, then each entity will be a groups by itself.
            This option applies only when connectivity_groups_by = Entity.
            Otherwise it is ignored.
            Default value if False.

    feature_angle : float, optional
            The feature angle limit in degrees.
            If this value is exceeded, the groups get separated at this feature line.
            Valid values are 0 - 180.
            If set to 0, the feature line separation is disabled.
            This option applies only when connectivity_groups_by = Entity.
            Otherwise it is ignored.
            Default value is 60.

    feature_type : str, optional
            Specifies the type of the feature lines in which the connectivity groups will be separated.
            Groups get separated at the examined bound only if feature_angle is exceeded and the feature type is of the specified type.
            Available options are "convex", "concave" and "convex_and_concave".
            This option applies only when connectivity_groups_by = Entity.
            Otherwise it is ignored.
            Default value is "convex_and_concave".

    Returns
    -------
    object
            Returns a list.
            This list contains lists with entities that correspond to each group on how exterior they are.
            The lists are sorted from the most interior group of entities to the most exterior.
            The first list contains the absolutely interior entities and the last the absolutely exterior.

    See Also
    --------
    ExternalDetection

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base


            # separetes shells in parts depending on how exterior they are
            def main():
                shells = base.CollectEntities(0, None, "SHELL", False)
                groups = mesh.IsolateVisibilityGroups(
                    shells, groups_number=10, external_visibility_limit=20.0
                )

                i = 0
                for group in groups:
                    part = base.NewPart("Part_" + str(i))
                    base.SetEntityPart(group, part)
                    i = i + 1


    """


def HexaBlock2DBoxCreate(
    type: str, entities: object, delete_original: bool, paste: bool
) -> object:
    """

    A function to create a 2D Hexa-Block box using the input entities.
    For "hatches" case, the original 3D boxes may be deleted (optional argument).
    For "wireframe" case, there is the option to paste the created 2D boxes
    (paste=True).

    Parameters
    ----------
    type : str
            A string that defines the input entities. It can have
            the values "points", "curves", "hatches" and "wireframe".

    entities : object
            A list of the entities that are used for the creation of the 2D Hexa-Block box.
            According to the "type" it takes different entities:
            -"points" - list with entities whose points will be used to create the new 2D box,
            -"curves" - list containing four lists with the input curves/cons/edges (lists should be sequential),
            -"hatches" - list containing the input box faces,
            -"wireframe" - list containing the input curves.

    delete_original : bool, optional
            Defines if the original boxes will be deleted.
            It is used only for the "hatches" type.

    paste : bool, optional
            Defines if the created 2D boxes will be pasted or not.
            It is used only for the "wireframe" case.
            (Default: False)

    Returns
    -------
    object
            If "type" = "points" or "curves": Returns a reference to the newly created box object.
            If "type" = "hatches": Returns a list containing references to the newly created box objects.
            On failure, returns None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def hexaBlock2DCreateByPoints():
                points1 = []
                points1.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 74))
                points1.append(base.GetEntity(constants.NASTRAN, "GRID", 275))
                points1.append(base.GetEntity(constants.NASTRAN, "GRID", 310))
                points1.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 78))
                box1 = mesh.HexaBlock2DBoxCreate(type="points", entities=points1)
                if box1._id:
                    print("new 2D Hexa-Block box id = ", box1._id)
                points2 = []
                points2.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 98))
                points2.append(base.GetEntity(constants.NASTRAN, "GRID", 274))
                points2.append(base.GetEntity(constants.NASTRAN, "GRID", 309))
                box2 = mesh.HexaBlock2DBoxCreate(type="points", entities=points2)
                if box2._id:
                    print("new 2D Hexa-Block box id = ", box2._id)


            def hexaBlock2DCreateByCurves():
                curves1 = []
                curves1.append(base.GetEntity(constants.NASTRAN, "CURVE", 49))

                curves2 = []
                curves2.append(base.GetEntity(constants.NASTRAN, "CONS", 50))
                curves2.append(base.GetEntity(constants.NASTRAN, "CONS", 63))

                curves3 = []
                curves3.append(base.GetEntity(constants.NASTRAN, "CONS", 80))
                curves3.append(base.GetEntity(constants.NASTRAN, "CONS", 46))

                curves4 = []
                curves4.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 48))

                entities = []
                entities.append(curves1)
                entities.append(curves2)
                entities.append(curves3)
                entities.append(curves4)
                box = mesh.HexaBlock2DBoxCreate(type="curves", entities=entities)

                if box._id:
                    print("new 2D Hexa-Block box id = ", box._id)


            def hexaBlock2DCreateByHatches():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 1))
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 2))

                newBoxes = mesh.HexaBlock2DBoxCreate(
                    type="hatches", entities=m, delete_original=True
                )

                for run_box in newBoxes:
                    if run_box._id:
                        print("new 2D Hexa-Block box id = ", run_box._id)


            def hexaBlock2DCreateByCurvesWireframe():
                type = "wireframe"
                paste = False
                entities = base.CollectEntities(0, None, "CURVE")

                newBoxes = mesh.HexaBlock2DBoxCreate(type, entities, paste)


    """


class VolumesExtrude:
    """

    Class to extrude an area according to a specific rule.
    Find details about the arguments at each method e.g., mesh.VolumesExtrude.glide

    Examples
    --------
    ::

            import ansa
            from ansa import mesh
            from ansa import base
            from ansa import constants


            def main():
                source = base.CollectEntities(constants.NASTRAN, None, "FACE")
                guideline = base.CollectEntities(constants.NASTRAN, None, "CURVE")
                extrude = mesh.VolumesExtrude()

                # Sweep
                extrude.sweep(source=source, guideline=guideline, steps=10)

                # Glide
                extrude.glide(source=source, guideline=guideline, steps=10)

                # Map
                guideline1 = base.GetEntity(constants.NASTRAN, "CONS", 856)
                guideline2 = base.GetEntity(constants.NASTRAN, "CONS", 710)
                guidelines = []
                guidelines.append(guideline1)
                guidelines.append(guideline2)
                match = []
                match.append(1)
                match.append(0)
                extrude.map(source=source, guidelines=guidelines, match_guidelines=match)

                # Dual Sweep
                guideline1 = base.GetEntity(constants.NASTRAN, "CONS", 856)
                guideline2 = base.GetEntity(constants.NASTRAN, "CONS", 710)
                extrude.dual_sweep(
                    source=source, guideline1=guideline1, guideline2=guideline2, steps=10
                )

                # Offset
                extrude.offset(source=source, steps=10, distance=10.0)

                # Translate
                extrude.translate(
                    source=source,
                    axis=((-34.875, -45.240, 0.0), (0, -0.724, 0.688)),
                    steps=10,
                    distance=10.0,
                )

                # Revolute
                extrude.revolute(
                    source=source, axis=((-34.875, 59.991, 0.0), (0, -1, 0.0)), steps=10, angle=45.0
                )

                # Project
                extrude.project(source=source, target=target, steps=10, element_length=2.0)

    """

    def offset(
        self,
        source: object,
        target: object,
        side: object,
        source_remove: object,
        disconnect_from_source: bool,
        stitch_sources: bool,
        connect_target: bool,
        collapse_free_edges: bool,
        direction: str,
        biasing: str,
        factor: float,
        biasing_direction: str,
        steps: int,
        element_length: float,
        distance: float,
        part: object,
        property: object,
        last_layer_facets_set_name: str,
    ) -> int:
        """

        The shell mesh is offset by means of the normal vector of the elements.


        Parameters
        ----------
        source : object
                list of ansa entities

        target : object, optional
                list of ansa entities

        side : object, optional
                list of ansa entities

        source_remove : object, optional
                list of ansa entities

        disconnect_from_source : bool, optional
                flag to create an independent from source area volume

        stitch_sources : bool, optional
                flag to connect neighbouring unconnected source areas, otherwise volume with independant areas will be created

        connect_target : bool, optional
                flag to create compatible, mesh on target area

        collapse_free_edges : bool, optional
                flag to collapse free edges on the first layer

        direction : str, optional
                values could be "default", "inverted", "both_sides" or "both_sides_middle"

        biasing : str, optional
                values could be "no", "smooth", "arithmetic" or "geometric"

        factor : float, optional
                the biasing factor of element's lengths

        biasing_direction : str, optional
                values could be "ascending" or "descending"

        steps : int, optional
                sets the number of extruded layers

        element_length : float, optional
                sets the element's length

        distance : float, optional
                sets the length of all extruded layers

        part : object, optional
                the part that will be assigned to the volume

        property : object, optional
                the property that will be assigned to the volume

        last_layer_facets_set_name : str, optional
                creates a set with the given name that contains the last layer facets

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def translate(
        self,
        source: object,
        target: object,
        side: object,
        source_remove: object,
        disconnect_from_source: bool,
        stitch_sources: bool,
        connect_target: bool,
        collapse_free_edges: bool,
        axis: object,
        biasing: str,
        factor: float,
        biasing_direction: str,
        steps: int,
        element_length: float,
        distance: float,
        part: object,
        property: object,
        last_layer_facets_set_name: str,
    ) -> int:
        """

        The shell mesh is translated by means of a specified vector.


        Parameters
        ----------
        source : object
                list of ansa entities

        target : object, optional
                list of ansa entities

        side : object, optional
                list of ansa entities

        source_remove : object, optional
                list of ansa entities

        disconnect_from_source : bool, optional
                flag to create an independent from source area volume

        stitch_sources : bool, optional
                flag to connect neighbouring unconnected source areas, otherwise volume with independant areas will be created

        connect_target : bool, optional
                flag to create compatible, mesh on target area

        collapse_free_edges : bool, optional
                flag to collapse free edges on the first layer

        axis : object, optional
                the axis for the translation

        biasing : str, optional
                values could be "no", "smooth", "arithmetic" or "geometric"

        factor : float, optional
                the biasing factor of element's lengths

        biasing_direction : str, optional
                values could be "ascending" or "descending"

        steps : int, optional
                sets the number of extruded layers

        element_length : float, optional
                sets the element's length

        distance : float, optional
                sets the length of all extruded layers

        part : object, optional
                the part that will be assigned to the volume

        property : object, optional
                the property that will be assigned to the volume

        last_layer_facets_set_name : str, optional
                creates a set with the given name that contains the last layer facets

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def revolute(
        self,
        source: object,
        target: object,
        side: object,
        source_remove: object,
        disconnect_from_source: bool,
        stitch_sources: bool,
        connect_target: bool,
        collapse_free_edges: bool,
        axis: object,
        biasing: str,
        factor: float,
        biasing_direction: str,
        steps: int,
        element_length: float,
        angle: float,
        part: object,
        property: object,
        last_layer_facets_set_name: str,
    ) -> int:
        """

        The shell mesh is revoluted around a specified axis.


        Parameters
        ----------
        source : object
                list of ansa entities

        target : object, optional
                list of ansa entities

        side : object, optional
                list of ansa entities

        source_remove : object, optional
                list of ansa entities

        disconnect_from_source : bool, optional
                flag to create an independent from source area volume

        stitch_sources : bool, optional
                flag to connect neighbouring unconnected source areas, otherwise volume with independant areas will be created

        connect_target : bool, optional
                flag to create compatible, mesh on target area

        collapse_free_edges : bool, optional
                flag to collapse free edges on the first layer

        axis : object, optional
                the axis for the revolution

        biasing : str, optional
                values could be "no", "smooth", "arithmetic" or "geometric"

        factor : float, optional
                the biasing factor of element's lengths

        biasing_direction : str, optional
                values could be "ascending" or "descending"

        steps : int, optional
                sets the number of extruded layers

        element_length : float, optional
                sets the element's length

        angle : float, optional
                sets the angle of revolute

        part : object, optional
                the part that will be assigned to the volume

        property : object, optional
                the property that will be assigned to the volume

        last_layer_facets_set_name : str, optional
                creates a set with the given name that contains the last layer facets

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def project(
        self,
        source: object,
        target: object,
        side: object,
        source_remove: object,
        disconnect_from_source: bool,
        stitch_sources: bool,
        connect_target: bool,
        collapse_free_edges: bool,
        biasing: str,
        factor: float,
        biasing_direction: str,
        steps: int,
        element_length: float,
        part: object,
        property: object,
        last_layer_facets_set_name: str,
    ) -> int:
        """

        The shell mesh is extruded by means of the source/target project direction.


        Parameters
        ----------
        source : object
                list of ansa entities

        target : object
                list of ansa entities

        side : object, optional
                list of ansa entities

        source_remove : object, optional
                list of ansa entities

        disconnect_from_source : bool, optional
                flag to create an independent from source area volume

        stitch_sources : bool, optional
                flag to connect neighbouring unconnected source areas, otherwise volume with independant areas will be created

        connect_target : bool, optional
                flag to create compatible, mesh on target area

        collapse_free_edges : bool, optional
                flag to collapse free edges on the first layer

        biasing : str, optional
                values could be "no", "smooth", "arithmetic" or "geometric"

        factor : float, optional
                the biasing factor of element's lengths

        biasing_direction : str, optional
                values could be "ascending" or "descending"

        steps : int, optional
                sets the number of extruded layers

        element_length : float, optional
                sets the element's length

        part : object, optional
                the part that will be assigned to the volume

        property : object, optional
                the property that will be assigned to the volume

        last_layer_facets_set_name : str, optional
                creates a set with the given name that contains the last layer facets

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def sweep(self, source: object, guideline: object, match_guideline: bool) -> int:
        """

        The shell mesh is swept along the given guideline. The rest arguments same as project.


        Parameters
        ----------
        source : object
                list of ansa entities

        guideline : object
                list of ansa entities

        match_guideline : bool, optional
                flag to connect volume mesh with the nodes on the guidelines

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def glide(self, source: object, guideline: object, match_guideline: bool) -> int:
        """

        The shell mesh is glided along the given guideline.


        Parameters
        ----------
        source : object
                list of ansa entities

        guideline : object
                list of ansa entities

        match_guideline : bool, optional
                flag to connect volume mesh with the nodes on the guidelines

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def dual_sweep(
        self,
        source: object,
        guideline1: object,
        guideline2: object,
        match_guideline1: bool,
        match_guideline2: bool,
    ) -> int:
        """

        The shell mesh is swept along two given guidelines. The first one (or first match) is the master guideline. The rest arguments same as sweep.


        Parameters
        ----------
        source : object
                list of ansa entities

        guideline1 : object
                list of ansa entities

        guideline2 : object
                list of ansa entities

        match_guideline1 : bool, optional
                flag to connect volume mesh with the nodes on the guideline1

        match_guideline2 : bool, optional
                flag to connect volume mesh with the nodes on the guideline2

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """

    def map(self, source: object, guidelines: object, match_guidelines: object) -> int:
        """

        The shell mesh is extruded along two or more given guidelines. The first one (or first match) is the master guideline. The rest argumens same as sweep.


        Parameters
        ----------
        source : object
                list of ansa entities

        guidelines : object
                list of guidelines

        match_guidelines : object, optional
                list with corresponding to the guidelines list flags to connect volume mesh with the guideline nodes

        Returns
        -------
        int
                Returns 1 on success or 0 on failure.

        """


class ReplaceCavity:
    """

    ReplaceCavity will locally erase and remesh part of volume meshes contained in a box according to the existing batch mesh.

    Examples
    --------
    ::

            def main():
                box = base.GetEntity(constants.NASTRAN, "MORPHBOX", 1)
                boxes = [box]

                replace_cavity = mesh.ReplaceCavity()
                cavity_areas = replace_cavity.new(boxes)

                replace_cavity.mesh(cavity_areas)

    """

    @classmethod
    def new(cls, boxes: object) -> object:
        """

        A Cavity Area entity will be defined from the box. The solids inside the Cavity Area will be erased and boudnary shells will be created on the remaining free facets.


        Parameters
        ----------
        boxes : object
                A list of MorphBoxes or HexaBoxes to define Cavity Area.

        Returns
        -------
        object
                A list of the created Cavity Areas.

        """

    @classmethod
    def mesh(cls, cavity_areas: object) -> bool:
        """

        The Cavity Area defined from the box will be remesh according to the batch mesh and the neighboring tetra mesh. In case of success the produced volumes will be merged with the neighbouring and the Cavity Area will be deleted.


        Parameters
        ----------
        cavity_areas : object
                A list that contains the Cavity Areas.

        Returns
        -------
        bool

        """

    def create_box(self, subsystem: object) -> object:
        """

        A box will be created and will include all the patrs the subsystem contains


        Parameters
        ----------
        subsystem : object
                A subsystem to create a box around it.

        Returns
        -------
        object
                The Morph box created around the subsystem.

        """

    def create_subsystem(self, boxes: object) -> bool:
        """

        A Cavity Area subsystem will be defined from the box. The solids inside the Cavity Area will be erased and boudnary shell will be created on the remaining free facets.


        Parameters
        ----------
        boxes : object
                A list of MorphBoxes or HexaBoxes to define Cavity Area.

        Returns
        -------
        bool
                Returns true on seccess, false otherwise.

        """


class HexaBlockShellsSmooth:
    """

    Class provides smoothing for the selected box face(s).

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants


            def main():
                deck = constants.NASTRAN

                box_faces = []
                box_faces.append(base.GetEntity(deck, "HEXA_BOX_FACE", 15))
                box_faces.append(base.GetEntity(deck, "HEXA_BOX_FACE", 20))
                el_sm = ansa.mesh.HexaBlockShellsSmooth(box_faces)

                box_edges = []
                box_edges.append(base.GetEntity(deck, "HEXA_BOX_EDGE", 44))
                el_sm.add_feature_lines(box_edges)

                box_edge = base.GetEntity(deck, "HEXA_BOX_EDGE", 44)
                el_sm.set_boundary_condition(box_edge, "so")

                el_sm.finalize_feature_line_selection()
                el_sm.run(100, 0.4, True)
                print(el_sm.get_boundary_condition(arg2))
                el_sm.accept()


            if __name__ == "__main__":
                main()

    """

    @classmethod
    def __init__(cls, box_faces: object) -> object:
        """

        Constructor of the class.


        Parameters
        ----------
        box_faces : object
                A list of box face(s) to be smoothed. The box face(s) can only be meshed with the map function.

        Returns
        -------
        object
                Returns the instance of the object.

        """

    @classmethod
    def run(cls, iterations: int, relaxation: float, project_on_db: bool) -> object:
        """

        Runs the smoother.


        Parameters
        ----------
        iterations : int
                Controls the number of iterations of the solver.

        relaxation : float
                Limits the distance which a node can travel for each iteration.

        project_on_db : bool
                Instructs the smoother to project to underlying geometry. If it sets to false then the mesh will be projected to the underlying box face(s).

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    @classmethod
    def accept(cls) -> object:
        """

        When the smoother has finished its run, this method must be called. Applies the new smoothed mesh and fits the inner box edge(s) into new positions.


        Returns
        -------
        object
                Returns the instance of the object if successful

        """

    @classmethod
    def auto_detect_feature_lines(cls, feature_line_angle: float) -> object:
        """

        Auto detects feature lines.


        Parameters
        ----------
        feature_line_angle : float
                Sets the feature line angle for auto detection.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    @classmethod
    def clear_all_feature_lines(cls) -> object:
        """

        Clears all feature lines.


        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    @classmethod
    def remove_feature_lines(cls, box_edges: object) -> object:
        """

        Removes feature lines given.


        Parameters
        ----------
        box_edges : object
                List of box edge(s) to be removed from feature lines.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    @classmethod
    def add_feature_lines(cls, box_edges: object) -> object:
        """

        Adds feature lines.


        Parameters
        ----------
        box_edges : object
                List of box edge(s) to be added as feature lines.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    @classmethod
    def finalize_feature_line_selection(cls) -> object:
        """

        This function must be called after all feature lines are gathered.


        Returns
        -------
        object
                Returns the object instance if successful.

        """

    @classmethod
    def set_boundary_condition(cls, edge: object, boundary_type: str) -> object:
        """

        Sets the boundary condition for a specific box edge.


        Parameters
        ----------
        edge : object
                The box edge that its boundary condition will be set.

        boundary_type : str
                The value of the new boundary condition.
                "f"   The boundary will be fixed
                "fo" The boundary will be fixed and it will be applied
                       orthogonality to it.
                "s"  The boundary nodes will slide to the boundary.
                "so" The boundary nodes will slide to the boundary and
                        it will be applied orthogonality to it.

        Returns
        -------
        object
                Returns the object of the class if successful.

        """

    @classmethod
    def get_boundary_condition(cls, edge: object) -> object:
        """

        Returns the boundary condition and the group of the box edges which it belongs.


        Parameters
        ----------
        edge : object
                Gets the box edge.

        Returns
        -------
        object
                Returns a tuple with the group of the HEXA_BLOCK_BOX_EDGEs and the type of boundary condition

        """


def MergeLeakToolLeaks(distance_factor: float) -> bool:
    """

    The function merges the result parts and sets of Leak Tool.

    Parameters
    ----------
    distance_factor : float
            The factor by which each leak point calculated distance is multiplied to define the merge distance.

    Returns
    -------
    bool
            Returns False if no "Leaks" part exist.
            Reurns True otherwise.

    See Also
    --------
    LeakTool

    Examples
    --------
    ::

            import ansa
            from ansa import mesh


            def main():
                mesh.MergeLeakToolLeaks(4)


    """


def Mesh(entities: object) -> int:
    """

    Creates mesh for user input entities.

    Parameters
    ----------
    entities : object
            Accepted values: A list of faces, shells,  "visible".

    Returns
    -------
    int
            Returns 0 if invalid arguments were specified, 1 otherwise.

    Examples
    --------
    ::

            def main():
                base.SetANSAdefaultsValues({"mesh_change_option": "mesh"})
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 35100))
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 34760))
                mesh.Mesh(faces)


    """


def Reset(entities: object) -> int:
    """

    Reset geometry for user input entities.

    Parameters
    ----------
    entities : object
            Accepted values: A list of faces, shells,  "visible".

    Returns
    -------
    int
            Returns 0 if invalid arguments were specified, 1 otherwise.

    Examples
    --------
    ::

            def main():
                base.SetANSAdefaultsValues({"reset_level_option": "erase_mesh"})
                base.SetANSAdefaultsValues({"reset_clear_features": "true"})
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 35097))
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 2187))
                mesh.Reset(faces)


    """


class HexaBlockSolidsSmooth:
    """

    Class provides smoothing for the selected morph boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                # ansa.base.BCSettingsReadFile("")

                # ---------------------------------
                arg1 = []
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 2))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 38))
                smoother = ansa.mesh.HexaBlockSolidsSmooth(arg1)

                # ---------------------------------
                arg1 = []
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 444))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 143))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 442))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 441))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 16))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 141))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 24))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 23))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 446))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 447))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 449))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 144))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 443))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 450))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 14))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 15))
                smoother.add_feature_lines(arg1)

                # ---------------------------------
                smoother.finalize_feature_line_selection()

                # ---------------------------------
                arg1 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_FACE", 223)
                smoother.set_boundary_condition(arg1, "s")

                # ---------------------------------
                arg1 = base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_FACE", 222)
                smoother.set_boundary_condition(arg1, "fo")

                # ---------------------------------
                smoother.run(20, 0.4, True)

                # ---------------------------------
                smoother.accept()


            if __name__ == "__main__":
                main()

    """

    def __init__(self, boxes: object) -> object:
        """

        Constructor of the class.


        Parameters
        ----------
        boxes : object
                A list of box(es) to be smoothed.

        Returns
        -------
        object
                Returns the instance of the object.

        """

    @classmethod
    def run(cls, iterations: int, relaxation: float, project_on_db: bool) -> object:
        """

        Runs the smoother.
        Returns the instance of the object if successful.


        Parameters
        ----------
        iterations : int
                Controls the number of iterations of the solver.

        relaxation : float
                Limits the distance which a node can travel for each iteration.

        project_on_db : bool
                Instructs the smoother to project to underlying geometry. If it sets to false then the mesh will be projected to the underlying box face(s).

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def accept(self) -> object:
        """

        When the smoother has finished its run, this method must be called. Applies the new smoothed mesh and fits the inner box edge(s) into new positions.


        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def auto_detect_feature_lines(self, feature_line_angle: float) -> object:
        """

        Auto detects feature lines.


        Parameters
        ----------
        feature_line_angle : float
                Sets the feature line angle for auto detection.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def clear_all_feature_lines(self) -> object:
        """

        Clears all feature lines.


        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def remove_feature_lines(self, box_edges: object) -> object:
        """

        Removes feature lines given.


        Parameters
        ----------
        box_edges : object
                List of box edge(s) to be removed from feature lines.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def add_feature_lines(self, box_edges: object) -> object:
        """

        Adds feature lines.


        Parameters
        ----------
        box_edges : object
                List of box edge(s) to be added as feature lines.

        Returns
        -------
        object
                Returns the instance of the object if successful.

        """

    def finalize_feature_line_selection(self) -> object:
        """

        This function must be called after all feature lines are gathered.


        Returns
        -------
        object
                Returns the object instance if successful.

        """

    def set_boundary_condition(self, face: object, boundary_type: str) -> object:
        """

        Sets the boundary condition for a specific box face.


        Parameters
        ----------
        face : object
                The box face that its boundary condition will be set.

        boundary_type : str
                The value of the new boundary condition.
                "f"  The boundary will be fixed.
                "fo" The boundary will be fixed and it will be applied orthogonality to it.
                "s"  The boundary nodes will also be smoothed.
                "so" The boundary nodes will also be smoothed and it will be applied orthogonality to it.
                "p"  The linked periodic faces will smoothed according to their parent.

        Returns
        -------
        object
                Returns the object of the class if successful.

        """

    def get_boundary_condition(self, face: object) -> tuple:
        """

        Returns the boundary condition and the group of the box edges which it belongs.


        Parameters
        ----------
        face : object
                Gets the box face.

        Returns
        -------
        tuple
                Returns a tuple with the group of the HEXA_BLOCK_BOX_EDGEs and the type of boundary condition.

        """


def HexaBlockVolumeMesh(
    boxes: object,
    tolerance: float,
    project: bool,
    ret_ents: bool,
    tolerance_expr: str,
    apply_surface_fit: bool,
    project_non_associated: bool,
) -> object:
    """

    A function that generates volume mesh for the specified Hexa-Block boxes.

    Parameters
    ----------
    boxes : object
            A list that contains the hexa boxes that we want
            to mesh (Hexa-Block boxes should not be meshed).

    tolerance : float
            The tolerance to project on geometry.

    project : bool
            A flag that defines whether to project (True) or
            not (False) on geometry.

    ret_ents : bool
            If set to True, a list with the created entities will be returned.

    tolerance_expr : str
            An expression to define the tolerance as a percentage of the minimum
            element length (Lmin). If expression is defined, "tolerance" is argument
            will be ignored.

    apply_surface_fit : bool
            A flag that defines if surface-fit will be applied for
            fully associated box faces (box faces with points,
            edges and face association).

    project_non_associated : bool
            A flag that defines if nodes of non-associated box
            faces will be projected on the geometry.

    Returns
    -------
    object
            Returns 1 on success, 0 on failure.
            If ret_ents=True it will return a list with the created entities, or None if no entities are created.

    See Also
    --------
    ansa.mesh.HexaBlockVolumes, HexaBlockVolumesMap, HexaBlockShellMesh

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                arg1 = []
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1099))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1098))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1097))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1096))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1095))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1094))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1093))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1092))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1091))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1090))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1088))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1087))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1086))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1085))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1084))
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX", 1083))
                ansa.mesh.HexaBlockVolumeMesh(
                    boxes=arg1,
                    project=True,
                    tolerance_expr="0.05*Lmin",
                    apply_surface_fit=True,
                    project_non_associated=True,
                )


    """


def RotatingInterfaceGeneric(
    rotating_entities: object,
    offset: float,
    auto_axis_calc: bool,
    start_x: float,
    start_y: float,
    start_z: float,
    end_x: float,
    end_y: float,
    end_z: float,
) -> object:
    """

    Automatic creation of the sliding interface boundary for rotating volume mesh around wheels.
    Intersections between rotating and static entities should be avoided.

    Parameters
    ----------
    rotating_entities : object
            A list of ansa entities.
            These entities must be faces or shells.

    offset : float
            Offset value of rotating interface from rotating entities.

    auto_axis_calc : bool
            Automatic axis calculation option.
            False disabled , True enabled.

    start_x : float
            X coordinate of rotation axis start.

    start_y : float
            Y coordinate of rotation axis start.

    start_z : float
            Z coordinate of rotation axis start.

    end_x : float
            X coordinate of rotation axis end.

    end_y : float
            Y coordinate of rotation axis end.

    end_z : float
            Z coordinate of rotation axis end.

    Returns
    -------
    object
            Returns an object containing the following:
            ret.status                       : (integer)  0 on succes , 1 if HOT POINTS and CONS matching distance is violated , 2 if HOT
                                                POINTS matching distance is violated , 3 if CONS matching distance is violated ,
                                                4 if offset distance is too big , 5 if axis cannot calculated automatically.
            ret.result_faces                 : (list)     A list with the created faces of the sliding interface.
            ret.points_of_rotating_interfaces: (list) Returns the 3d points of the profile of the created rotating interfaces.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import mesh


            def main():
                rot_set = base.GetEntity(ansa.constants.NASTRAN, "SET", 1)
                rot_ents = base.CollectEntities(constants.NASTRAN, rot_set, ["SHELL", "FACE"])

                ret = mesh.RotatingInterfaceGeneric(
                    rotating_entities=rot_ents,
                    offset=5,
                    auto_axis_calc=False,
                    start_x=1551.03,
                    start_y=-913.04,
                    start_z=901.49,
                    end_x=1551.03,
                    end_y=-745.28,
                    end_z=898.56,
                )
                print("status =", ret.status)
                print("result_num =", len(ret.result_faces))


    """
