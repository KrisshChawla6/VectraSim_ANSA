from __future__ import annotations
from typing import *


def ConvertMorphToSizeBox(
    morphs_matrix: object, max_surface_length: float, max_volume_length: float
) -> int:
    """

    Script function that converts morphing boxes to size boxes.

    Parameters
    ----------
    morphs_matrix : object
            A list that contains morphing boxes.

    max_surface_length : float, optional
            Values for surface lengthand.

    max_volume_length : float, optional
            Values for surface length.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def toSizeBox():
                m = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX")
                mtosb = morph.ConvertMorphToSizeBox(m)


    """


def DvgridStart(elements_flag: int) -> int:
    """

    Script function for creating DVGRID's.

    Parameters
    ----------
    elements_flag : int, optional
            0: For all elements.
            1: For shells.
            2: For solids.
            (Default: 0)

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def dvgrids():
                morph.DvgridStart(0)

                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 1)
                morph.MorphParam(param, 10.0)

                p_desvar = base.CreateEntity(
                    constants.NASTRAN, "DESVAR", {"XINIT": 1, "ID": 1, "LABEL": "Dv1"}
                )
                morph.DvgridStop(p_desvar, 0.005)


    """


def DvgridStop(element: object, tolerance: float, ret_ent: bool) -> object:
    """

    Script function for creating DVGRID's.

    Parameters
    ----------
    element : object
            The DESVAR entity.

    tolerance : float, optional
            Used in order to ignore very small movements.

    ret_ent : bool, optional
            If set to True, this function will return the DESVAR entity instead of its id.

    Returns
    -------
    object
            Returns the desvar id on success, 0 on failure.
            If ret_ent is set to True, it returns the desvar entity instead.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def dvgrids():
                morph.DvgridStart(0)

                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 1)
                morph.MorphParam(param, 10.0)

                p_desvar = base.CreateEntity(
                    constants.NASTRAN, "DESVAR", {"XINIT": 1, "ID": 1, "LABEL": "Dv1"}
                )
                morph.DvgridStop(p_desvar, 0.005)


    """


def FEOutputName(filename: str) -> int:
    """

    Script function to pass as argument the Output filename to the Optimization Task.

    Parameters
    ----------
    filename : str
            The path and the filename.

    Returns
    -------
    int
            Returns 1 on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.FEOutputName("/home/user/output1.nas")


    """


def InputDV(filename: str) -> int:
    """

    Script function to pass as argument the Design Variable filename to the Optimization Task.

    Parameters
    ----------
    filename : str
            The desired filename.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.InputDV("/home/user/mydvfile.txt")


    """


def MorphAdjust(hatch: object) -> int:
    """

    Script function for adjusting morph hatches.

    Parameters
    ----------
    hatch : object
            The morph hatch object, where the box will be adjusted.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def adjustMface():
                hatch = base.GetEntity(constants.NASTRAN, "MORPHFACE", 1)
                morph.MorphAdjust(hatch)


    """


def MorphAlign(
    id_curve_or_plane: int, curve_or_plane: str, mpoints: object, flag: int
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`AlignBoxPoints` instead.


    Script function for the alignment of morph control points.

    Parameters
    ----------
    id_curve_or_plane : int
            A curve or a working plane id.

    curve_or_plane : str
            The type. 'c' for curve, 'w' for working plane.

    mpoints : object
            A list of morph control point.

    flag : int
            This flag should be 1 for morphing or 0 for modifying only
            edges without FE movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def alignMpoint():
                m1 = []
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 86))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 83))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 95))
                # Align 3 morph points at working plane with id 2
                morph.MorphAlign(2, "w", m1, 1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: AlignBoxPoints instead.",
        DeprecationWarning,
    )


def MorphAlign3Grids(
    grid1: object, grid2: object, grid3: object, m1: object, flag: int
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`AlignBoxPoints` instead.


    Script function for the alignment of morph control points.

    Parameters
    ----------
    grid1 : object
            The first grid element to define a plane.

    grid2 : object
            The second grid element to define a plane.

    grid3 : object
            The third grid element to define a plane.

    m1 : object
            A list of morph control point to align.

    flag : int
            This flag should be 1 for morphing or 0 for modifying
            only edges without FE movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def align3Grids():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 86))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 83))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 95))

                a = base.GetEntity(constants.NASTRAN, "GRID", 53527)
                b = base.GetEntity(constants.NASTRAN, "GRID", 53528)
                c = base.GetEntity(constants.NASTRAN, "GRID", 53529)

                # Algn 3 morph points in matrix m to a,b,c grids
                morph.MorphAlign3Grids(a, b, c, m, 0)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: AlignBoxPoints instead.",
        DeprecationWarning,
    )


def MorphBoxDel(boxes: object) -> int:
    """

    Script function to delete morph boxes.

    Parameters
    ----------
    boxes : object
            An object or list containing the morph elements to be deleted.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def deleteBoxes():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 1))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 2))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 3))
                morph.MorphBoxDel(m)


    """


def MorphBoxUndel(morphes: object) -> int:
    """

    Script function for undelete a morph box

    Parameters
    ----------
    morphes : object
            A list containing the morph elements that will be undeleted.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def undeleteBoxes():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 1))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 2))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 3))
                morph.MorphBoxUndel(m)
                morph.MorphLoadVisib(m)


    """


def MorphByPoints(points: object, solid_type: str) -> object:
    """

    Script function for creating 3D morph boxes from existing nodes or edges, shells.

    Parameters
    ----------
    points : object
            A list with entities from where 4, 5, 6 or 8 points will be taken to
            create TETRA, PYRAMID, PENTA or HEXA box.

    solid_type : str, optional
            Defines the solid type in case that the input points could be used for the creation
            of more than one solid types. It takes the values "hexa", "penta", "tetra" or "pyramid".

    Returns
    -------
    object
            Returns a reference to the created morph on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def morphFromPoints():
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 11))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 21))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 31))
                points.append(base.GetEntity(constants.NASTRAN, "GRID", 41))

                morph.MorphByPoints(points)


    """


def MorphCalcDvgrid(morph_points: object, directory: str, entities_flag: int) -> int:
    """

    This function calculates Dvgrid values and produces the corresponding files based on unity movement of morphing points.

    Parameters
    ----------
    morph_points : object
            A list containing morph point entities.

    directory : str
            The path to the directory where the produces files will be saved.

    entities_flag : int, optional
            Select which elements types to use.

            for shells and solids select 0 (zero). Default
            for only shells select 1.
            for only solids select 2.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def addPoint():
                m1 = (base.GetEntity(constants.NASTRAN, "MORPHPOINT", 1),)
                morph.MorphCalcDvgrid(m1, directory="/home/dir2/")


    """


def MorphContents(morphes: object) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:func:`CollectEntities` instead.


    Script function for acquiring morph contents.

    Parameters
    ----------
    morphes : object
            A list containing morph entities.

    Returns
    -------
    object
            Returns a list of entities on success, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def morphContents():
                morph_boxes = base.CollectEntities(
                    constants.NASTRAN, None, "MORPHBOX", filter_visible=True
                )
                entities = morph.MorphContents(morph_boxes)

                # Print the type and id of each entity
                for ent in entities:
                    print(ent.ansa_type(constants.NASTRAN), ent._id)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:func: CollectEntities instead.",
        DeprecationWarning,
    )


def MorphConvert(convert_type: str, entities: object, options: int) -> object:
    """

    Script function for converting morph entities.

    Parameters
    ----------
    convert_type : str
            The type of the desired conversion, that can be one of these:
            "MorphToHexa", to convert morphes to HexaBoxes
            "MorphToSizeBox", to convert morphes to SizeBoxes
            "MorphFacesToGeo", to convert morphing faces to geometrical faces
            "MorphEdgesToCurve", to convert morphing edges to geometrical curves
            "Morph2DTo3D", to convert morphes from 2D to 3D
            "MorphCylindricalToOrtho", to convert morphes from Cylindrical to ortho-box
            "Unlink", unlink boxes (morphing boxes, size boxes or hexa-block boxes)
            "SizeBoxToHexa", convert size box to hexa-block box
            "ConvertToDeckBox", convert boxes (morphing boxes, size boxes or hexa-block boxes)
            to deck boxes
            "SizeBoxCylindricalToOrtho",  to convert size box from Cylindrical to ortho-box

    entities : object
            A list containing the entities to convert.

    options : int, optional
            A dictionary that contains pairs of arguments. The pairs that can be
            assigned are the following:
            1) "MorphToSizeBox": 'max_surface_length': float, 'max_volume_length': float
            2) "MorphFacesToGeo": 'paste_cons': boolean,
            'fillet_shape': 'Round' or 'Planar' or 'None' (string), 'radius': float, 'associate_faces': boolean
            3) 'MorphCylindricalToOrtho', 'Morph2DTo3D': 'delete_original': boolean

    Returns
    -------
    object
            Returns a list of entities on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def MorphCylindricalToOrtho():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX", filter_visible=True)
                new3DBoxes = morph.MorphConvert(
                    "MorphCylindricalToOrtho", m1, {"delete_original": False}
                )
                vals = ("ID",)
                if new3DBoxes:
                    for ent in new3DBoxes:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        print("Created 3D morphing box id = ", id["ID"])


            def MorphEdgesToCurve():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHEDGE", filter_visible=True)
                new3dcurve = morph.MorphConvert("MorphEdgesToCurve", m1)
                vals = ("ID",)
                if new3dcurve:
                    for ent in new3dcurve:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        print("Created 3D curve id = ", id["ID"])


            def MorphFacesToGeo():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHFACE", filter_visible=True)
                new3dface = morph.MorphConvert(
                    "MorphFacesToGeo",
                    m1,
                    {"paste_cons": True, "fillet_shape": "Round", "radius": 5},
                )
                vals = ("ID",)
                if new3dface:
                    for ent in new3dface:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        print("Created 3D face id = ", id["ID"])


            def Morph2DTo3D():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX", filter_visible=True)
                new3DBoxes = morph.MorphConvert("Morph2DTo3D", m1, {"delete_original": True})
                vals = ("ID",)
                if new3DBoxes:
                    for ent in new3DBoxes:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        print("Created 2D morph id = ", id["ID"])


            def MorphToSizeBox():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX", filter_visible=True)
                newsb = morph.MorphConvert(
                    "MorphToSizeBox", m1, {"max_surface_length": 5, "max_volume_length": 5}
                )
                vals = ("ID",)
                if newsb:
                    for ent in newsb:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        # print("Created sizebox id = ", id['ID'])


            def MorphToHexa():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX", filter_visible=True)
                newhexabox = morph.MorphConvert("MorphToHexa", m1)
                vals = ("ID",)
                if newhexabox:
                    for ent in newhexabox:
                        id = base.GetEntityCardValues(constants.NASTRAN, ent, vals)
                        # print("Created hexa_box id = ", id['ID'])


            def unlinkBoxes():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 30))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 29))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "MORPHBOX", 49))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "MORPHBOX", 46))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "MORPHBOX", 43))
                ansa.morph.MorphConvert(convert_type="Unlink", entities=boxes)


            def sizeBoxToHexaBlockBox():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 18))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 17))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 16))
                ansa.morph.MorphConvert(convert_type="SizeBoxToHexa", entities=boxes)


            def convertToDeckBox():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "MORPHBOX", 9))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "MORPHBOX", 10))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 13))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 14))
                data = {}
                data["delete_original"] = True
                ansa.morph.MorphConvert(
                    convert_type="ConvertToDeckBox", entities=boxes, options=data
                )


            def sizeBoxCylindricalToOrthoBox():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 20))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 19))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 21))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "SIZE_BOX", 22))
                data = {}
                data["delete_original"] = False
                ansa.morph.MorphConvert(
                    convert_type="SizeBoxCylindricalToOrtho", entities=boxes, options=data
                )


    """


def MorphCylindrical(
    curve: object, rad1: float, rad2: float, auto_sort: bool
) -> object:
    """

    Script function for creating a cylindrical morph box.

    Parameters
    ----------
    curve : object
            A list of CURVEs or POINTs.

    rad1 : float
            The inner radius of the cylinder.

    rad2 : float
            The outer radius of the cylinder.

    auto_sort : bool, optional
            True (default): The order of objects in curve list will be reorder
            in order to have an improved result.
            False: The order of objects in curve list will be preserved.

    Returns
    -------
    object
            Returns a reference to the newly created cylindrical morph on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def createCylindrical():
                morphes = []
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                morphes.append(morph.MorphCylindrical(curve, 10.0, 20.0))
                morph.MorphLoad(morphes, None, "Visib")


    """


def MorphDepress(curve: object, set: object, matrix: object) -> int:
    """

    Script function for the creation of depressions

    Parameters
    ----------
    curve : object
            A curve object.

    set : object
            A set object were the depression will be applied.

    matrix : object
            A list with 6 entries: Width, Height, Rows, Element length (if negative or zero average will be used),
            Type (should be one of "Box", "Triangle", "Trapezoid", "Ellipse"), Flat width.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                a = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                b = base.GetEntity(constants.NASTRAN, "SET", 1)
                morph.MorphDepress(a, b, (10.2, 12, 7, 6.2, "Box", 5))


    """


def MorphDirectFit(Origin_Target: object, Entities: object, Bounds: object) -> int:
    """

    Script function for direct morphing fit.

    Parameters
    ----------
    Origin_Target : object
            A list of origin and target curves|cons. Origin and target are kept into pairs.
            Odd index keeps the origin curve|cons and the next index keeps the target curve.

    Entities : object
            A list of entities that will be morphed.

    Bounds : object
            A list of curves/cons that will be used as bounds.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                origin_target = []
                bounds = []
                origin_target.append(base.GetEntity(constants.NASTRAN, "CURVE", 29))
                origin_target.append(base.GetEntity(constants.NASTRAN, "CURVE", 27))
                origin_target.append(base.GetEntity(constants.NASTRAN, "CURVE", 19))
                origin_target.append(base.GetEntity(constants.NASTRAN, "CURVE", 21))

                bounds.append(base.GetEntity(constants.NASTRAN, "CURVE", 187))
                bounds.append(base.GetEntity(constants.NASTRAN, "CURVE", 24))

                elements = base.CollectEntities(constants.NASTRAN, None, "FACES")
                elements.extend(
                    base.CollectEntities(constants.NASTRAN, None, "SHELL", filter_visible=True)
                )
                morph.MorphDirectFit(origin_target, elements, bounds)


    """


def MorphEdgeFit(
    origin_target: list, edge_fit_add_flag: bool, morphing_flag: bool
) -> int:
    """

    Script function for fitting morph edges on to curves.

    Parameters
    ----------
    origin_target : list
            A list of lists with morph edges - curves or a dictionary containing
            tuples of morph edges - curves.

    edge_fit_add_flag : bool, optional
            The auto insertion of morph control point.
            True to add or False for no auto insertion.

    morphing_flag : bool, optional
            True for morphing, or False for modifying only
            edges without FE movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def edgefit():
                m1 = []
                m2 = []
                m3 = []
                m4 = []

                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 11))
                m1.append(base.GetEntity(constants.NASTRAN, "CURVE", 38))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 23))
                m1.append(base.GetEntity(constants.NASTRAN, "CURVE", 30))

                m2.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 10))
                m2.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 22))
                m2.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 46))
                m2.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 58))
                m1.append(m2)

                m3.append(base.GetEntity(constants.NASTRAN, "CURVE", 29))
                m3.append(base.GetEntity(constants.NASTRAN, "CURVE", 41))
                m3.append(base.GetEntity(constants.NASTRAN, "CURVE", 32))
                m3.append(base.GetEntity(constants.NASTRAN, "CURVE", 36))
                m1.append(m3)

                m4.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 47))
                m4.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 59))
                m1.append(m4)
                m1.append(base.GetEntity(constants.NASTRAN, "CURVE", 42))

                morph.MorphEdgeFit(m1, True, False)


            def edgefit_dictionary():
                dict = {}
                dict[
                    (
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 14),
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 26),
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 3),
                    )
                ] = (
                    base.GetEntity(ansa.constants.NASTRAN, "CURVE", 2),
                    base.GetEntity(ansa.constants.NASTRAN, "CURVE", 1),
                    base.GetEntity(ansa.constants.NASTRAN, "CURVE", 5),
                )

                dict[
                    (
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 13),
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 25),
                        base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX_EDGE", 1),
                    )
                ] = (
                    base.GetEntity(ansa.constants.NASTRAN, "CURVE", 3),
                    base.GetEntity(ansa.constants.NASTRAN, "CURVE", 4),
                )

                ansa.morph.MorphEdgeFit(
                    origin_target=dict, edge_fit_add_flag=True, morphing_flag=True
                )


    """


def MorphFacesAccordingNodes(faces: object) -> int:
    """

    Script function for applying node deformations to different geometries.
    This script function is used for morphing geometry faces to a new position,
    according to the movement of their shell mesh.

    Parameters
    ----------
    faces : object
            A list of geometry faces.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def morphFaces():
                faces = base.CollectEntities(
                    constants.NASTRAN, containers, "FACE", filter_visible=True
                )
                morph.MorphFacesAccordingNodes(faces)


    """


def MorphFlagStatus(morphing_flags: str, set_morphing_flags: bool) -> int:
    """

    Script function for reporting and setting morph flags status.

    Parameters
    ----------
    morphing_flags : str
            One of the following ANSA.defaults values:
            "BOXINBOX_MORPHING", "LOAD_MORPH_POINTS", "FREEZE_CHECK",
            "MORPHING_FLAG", "LOAD_FE_MODEL", "LOAD_NODES",
            "LOAD_FACES", "LOAD_CURVES", "APPLY_TANGENCY",
            "MORPH_TRANSLATE_POINTS", "MORPH_FORCE_FROZEN_ENTS", "PRESERVE_LOCAL_SHAPE","MORPH_INNER_RADIUS", "MORPH_SPIN_ALL_EDGES", "MORPH_MOVE_ALL_INNER"
            and values that are not stored in ANSA.defaults and replace old functions
            like MorphReconstruct, MorphSmooth, MorphEdgeFitAdd:
            "AUTO_RECONSTRUCT", "AUTO_SMOOTH", "EDGE_FIT_ADD".

    set_morphing_flags : bool, optional
            Set the desired value (True or False).

    Returns
    -------
    int
            Returns the value of each flag (1: true 0: false), or -1 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def mflagStatus():
                print("BOXINBOX_MORPHING =", morph.MorphFlagStatus("BOXINBOX_MORPHING"))
                print("LOAD_MORPH_POINTS =", morph.MorphFlagStatus("LOAD_MORPH_POINTS"))
                print("FREEZE_CHECK =", morph.MorphFlagStatus("FREEZE_CHECK"))
                print("MORPHING_FLAG =", morph.MorphFlagStatus("MORPHING_FLAG"))
                print("LOAD_FE_MODEL =", morph.MorphFlagStatus("LOAD_FE_MODEL", True))
                print("LOAD_NODES =", morph.MorphFlagStatus("LOAD_NODES"))
                print("LOAD_FACES =", morph.MorphFlagStatus("LOAD_FACES"))
                print("LOAD_CURVES =", morph.MorphFlagStatus("LOAD_CURVES"), True)
                print("LOAD_COORDS =", morph.MorphFlagStatus("LOAD_COORDS"))
                print("APPLY_TANGENCY =", morph.MorphFlagStatus("APPLY_TANGENCY"))
                print(
                    "MORPH_TRANSLATE_POINTS =",
                    morph.MorphFlagStatus("MORPH_TRANSLATE_POINTS", True),
                )
                print("MORPH_FORCE_FROZEN_ENTS =", morph.MorphFlagStatus("MORPH_FROCE_FROZEN_ENTS"))
                print("AUTO_RECONSTRUCT =", morph.MorphFlagStatus("AUTO_RECONSTRUCT"))
                print("AUTO_SMOOTH =", morph.MorphFlagStatus("AUTO_SMOOTH"))
                print("EDGE_FIT_ADD =", morph.MorphFlagStatus("EDGE_FIT_ADD"))


    """


def MorphHistory() -> int:
    """

    Script function for recording history states.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphHistory()


    """


def MorphHistoryState(history_state: object) -> int:
    """

    Script function for applying morph history states.

    Parameters
    ----------
    history_state : object
            The history state to be applied.

    Returns
    -------
    int
            Returns the id on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def applyHistoryState(id):
                ent = base.GetEntity(constants.NASTRAN, "MORPH_HISTORY", id)
                morph.MorphHistoryState(ent)


    """


def MorphInner(morph: object, dist: float) -> int:
    """

    Script function for the insertion of a morphing box's inner edges.

    Parameters
    ----------
    morph : object
            The cylindrical morph.

    dist : float
            The desired position in range 0-1 (parametric).

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def insertInner(id):
                ent = base.GetEntity(constants.NASTRAN, "MORPHBOX", id)
                morph.MorphInner(ent, 0.5)


    """


def MorphInsert(pnt1: object, pnt2: object, edg: object, s: str) -> int:
    """

    Script function for the insertion of morph control points.

    Parameters
    ----------
    pnt1 : object
            The first morph control point to get direction.

    pnt2 : object
            The second morph control point to get direction.

    edg : object
            A morph edge element.

    s : str
            A parameter in the 0-1 range or an approximate distance (~distance).

    Returns
    -------
    int
            Returns the new id on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def insertPnt():
                ent1 = base.GetEntity(constants.NASTRAN, "MORPHEDGE", 39)
                ent2 = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 83)
                ent3 = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 109)
                pnt = morph.MorphInsert(ent3, ent2, ent1, "~123")
                pnt = morph.MorphInsert(ent3, ent2, ent1, "0.3")


    """


def MorphJoin(hatch: object, flag: int) -> int:
    """

    Script function for joining a morph hatch.

    Parameters
    ----------
    hatch : object
            The morph hatch element that will be joined.

    flag : int
            A flag for leaving or deleting the morph points that are left from
            joined hatches. (1 or 0)

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def join():
                ent = base.GetEntity(constants.NASTRAN, "MORPHFACE", 145)
                morph.MorphJoin(ent, 1)


    """


def MorphLoad(
    morphes_to_load: object,
    entities_to_load: object,
    db_or_visib: str,
    strict_project: bool,
    keep_loaded: bool,
) -> int:
    """

    Script function for loading elements and nodes to a morphing box.

    Parameters
    ----------
    morphes_to_load : object
            A list of target morphing boxes.

    entities_to_load : object, optional
            A list containing the elements to be loaded.

    db_or_visib : str, optional
            A string to indicate Database or Visible elements to be included.
            Accepted values: "DB" or "Visib".

    strict_project : bool, optional
            A boolean flag to exclude nodes very close, but outside the boundary of the morph box

    keep_loaded : bool, optional
            A flag to append any new entities to already existing ones

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def loadElems():
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL", filter_visible=True)
                morphes = base.CollectEntities(
                    constants.NASTRAN, None, "MORPHBOX", filter_visible=True
                )
                morph.MorphLoad(morphes, entities_to_load=shells)
                morph.MorphLoad(morphes, db_or_visib="Visib")
                morph.MorphLoad(morphes, None, "Visib")


    """


def MorphMappingDeformations(
    deformation_parameter: object,
    moved_elements: object,
    sampling_points: int,
    work_on_visible: bool,
    bound_entities: object,
    max_displacement: float,
) -> int:
    """

    Script function for applying node deformations to different geometries.
    This script function can be used in two modes:
    -Apply morphing on geometry by having defined already the "Deformation parameters".
     The initial geometry will be moved to the final position of the "Deformation parameters".
    -Move the initial Geometry on the FE(that has been morphed) according to node deformations that can been read by a text file.

    Parameters
    ----------
    deformation_parameter : object
            Can be one of the following:
            -Morphing deformation parameter.
            -Morphing History states.
            -OpenFoam Sensitivities.
            -Nastran DESVAR.
            -Text file with values (x , y , z, dx, dy, dz).

    moved_elements : object
            A list with objects to be morphed.

    sampling_points : int
            A maximum number of sampling points in order to filter very large inputs.

    work_on_visible : bool
            To work on visible items or not.

    bound_entities : object, optional
            Set to True to create auto bound or list with the bound nodes or entities.

    max_displacement : float, optional
            Set the maximum displacement for the deformation. All values will be scaled accordingly.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main(type):
                params = []
                base.Open("../sensitivities_morph.ansa")
                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL", filter_visible=True)

                if type == 1:
                    params.append(base.GetEntity(constants.NASTRAN, "PARAMETERS", 2))
                elif type == 2:
                    morph.MorphMappingDeformations("../sensitivities.txt", shells, 1000000, True)
                elif type == 3:
                    params.append(base.GetEntity(constants.NASTRAN, "MORPH_HISTORY", 1))
                    params.append(base.GetEntity(constants.NASTRAN, "MORPH_HISTORY", 2))
                elif type == 4:
                    params.append(base.GetEntity(constants.OPENFOAM, "Sensitivity", 1))
                elif type == 5:
                    params.append(base.GetEntity(constants.NASTRAN, "DESVAR", 1))
                elif type == 6:
                    morph.MorphMappingDeformations(
                        "../sensitivities.txt", shells, 1000000, True, True
                    )
                if len(params) > 0:
                    morph.MorphMappingDeformations(
                        params, shells, 1000000, True, max_displacement=10
                    )


    """


def MorphMinMax(coordinate: object, min_xyz: object, max_xyz: object) -> int:
    """

    Script function for creating a morph box from two points (min, max).

    Parameters
    ----------
    coordinate : object
            The coordinate element (None for global).

    min_xyz : object
            A list containing minimum coordinates (xmin, ymin, zmin).

    max_xyz : object
            A list containing maximum coordinates (xmax, ymax, zmax).

    Returns
    -------
    int
            Returns the newly created morph object on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                min_coord = [-100, -100, -100]
                max_coord = [100, 100, 100]

                morph.MorphMinMax(None, min_coord, max_coord)

                coord = base.GetEntity(constants.NASTRAN, "CORD_R", 1)
                morph.MorphMinMax(coord, min_coord, max_coord)


    """


def MorphMove(morph_points: object, morph_edges: object, flag: int, dist: float) -> int:
    """

    Script function for the movement (SLIDE/EXTEND) of morph control points.

    Parameters
    ----------
    morph_points : object
            A list with morph control poits.

    morph_edges : object
            A list with morph edges.

    flag : int
            Should be 1 for morphing or 0 for modifying only edges,
            without FE movement.

    dist : float
            The distance of the movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def moveMorph():
                morph_points = []
                morph_edges = []
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 74))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 83))

                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 37))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 39))
                morph.MorphMove(morph_points, morph_edges, 1, 100)


    """


def MorphMultBox(coord: object, load: object, min_flag: int, factor: float) -> object:
    """

    Script function for the creation of multiple morph boxes.

    Parameters
    ----------
    coord : object
            The coordinate element (None for global).

    load : object
            Defines if the box will contain the visible (1) or the DB(0)
            or a list of user defined elements( shells, parts etc ).

    min_flag : int
            Corresponds to the type of the created box. When min_flag equals 1,
            then the created box obeys the minimum volume contraint.
            If min_flag equals 0, then the created box is a typical orthogonal box.

    factor : float
            The scale factor.

    Returns
    -------
    object
            Returns a list with the newly created morph objects on success, or 0 on failure.

    See Also
    --------
    MorphMultBoxAbsDis

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                morph.MorphMultBox(None, 1, 1, 1)

                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "SHELL")
                morph.MorphMultBox(None, ents, 0, 1)


    """


def MorphMultBoxAbsDis(
    coord: object, load: object, min_flag: int, distance: float, boxesType: int
) -> object:
    """

    Script function for the creation of multiple morph boxes. By using this function, the
    user has two options, either to create an O-ring or a Hexa type structure of multiple
    boxes. The description of the arguments follows:

    Parameters
    ----------
    coord : object
            The coordinate element (None for global).

    load : object
            Defines if the box will contain the visible (1), the DB (0) or
            a list of user defined elements (shells, parts etc).

    min_flag : int
            Corresponds to the type of the created box. When min_flag equals 1,
            then the created box obeys the minimum volume contraint.
            If min_flag equals 0, then the created box is a typical orthogonal box.

    distance : float
            The distance from the faces of the initial morphing box, to which the multiple
            boxes are extended.

    boxesType : int
            The type of the structure. If you want an O-ring structure,
            then boxesType has to be equal to 0. If you want a Hexa structure,
            then boxesType should equal to 1.

    Returns
    -------
    object
            Returns a list with the newly created morph objects on success, or 0 on failure.

    See Also
    --------
    MorphMultBox

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                morph.MorphMultBoxAbsDis(None, 1, 1, 10, 0)

                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "SHELL")
                morph.MorphMultBoxAbsDis(None, ents, 0, 10, 1)


    """


def MorphNested(set: object, reference_grid: object) -> int:
    """

    Function for creating a morphing nested entity.

    Parameters
    ----------
    set : object
            A set of entities. The nested will use the grids of the elements of the set.

    reference_grid : object
            The grid that will be the reference grid of the nested. If this value is None,
            then the reference grid will be the center of gravity.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def nestedCreate():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                center = base.GetEntity(constants.NASTRAN, "GRID", 53128)
                morph.MorphNested(set, center)


    """


def MorphNumber(morph_edge: object, string: str) -> int:
    """

    Script function for the insertion of any number of morph control points.

    Parameters
    ----------
    morph_edge : object
            A box edge or a list of box edges.

    string : str
            A number or a symbol (+/-).

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def numberOfPoints():
                edge = base.GetEntity(constants.NASTRAN, "MORPHEDGE", 13)
                morph.MorphNumber(edge, "5")
                morph.MorphNumber(edge, "-3")
                morph.MorphNumber(edge, "+1")

                box_edges = []
                box_edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 5))
                box_edges.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_EDGE", 7))
                ansa.morph.MorphNumber(box_edges, "+3")


    """


def MorphOffset(
    morph_hatces: object, offset_value: float, flag_morphing: int
) -> object:
    """

    Script function for offsetting morph hatches.

    Parameters
    ----------
    morph_hatces : object
            A list with morph hatch elements.

    offset_value : float
            The offsetting value.

    flag_morphing : int
            1: For morphing.
            0: For modifying only edges without FE movement.

    Returns
    -------
    object
            Returns 1 on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def offsetFace():
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 21))
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 24))
                morph.MorphOffset(faces, 10, 0)


    """


def MorphOffsetBox(morph_hatches: object, offset_value: float) -> object:
    """

    Script function for creating morphing boxes by setting an offset to some morph hatches.

    Parameters
    ----------
    morph_hatches : object
            A morph hatch elements.

    offset_value : float
            The offsetting value.

    Returns
    -------
    object
            Returns a list with the newly created morph objects on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def offsetFace():
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 21))
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 24))
                morph.MorphFlagStatus("APPLY_TANGENCY", False)
                morph.MorphOffsetBox(faces, 10)
                # morph.MorphOffset(faces, 10, 0)


    """


def MorphOneDimCreate(curves_list: object, load_radius: float, part: object) -> object:
    """

    Script function for creating one dimensional morphes.

    Parameters
    ----------
    curves_list : object
            A list with curves or points to create the one dimensional morph.

    load_radius : float
            The load radius of the crated morph.

    part : object, optional
            The part to add the created morph (None for default).

    Returns
    -------
    object
            Returns the newly created morph object on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def oneDimMorph():
                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 221))
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 31))
                morph.MorphOneDimCreate(curves, 100)


    """


def MorphOrtho(
    loaded_elements: object,
    db_or_visible: str,
    coordinate: object,
    min_flag: bool,
    directions: object,
) -> object:
    """

    Script function for the creation of a morph box.

    Parameters
    ----------
    loaded_elements : object, optional
            A list with elements to be loaded in the created morph.

    db_or_visible : str, optional
            Can have values 'DB' or 'Visible' for elements to be loaded in the created morph.

    coordinate : object, optional
            A local coordinate object instead of global.

    min_flag : bool, optional
            True or False for minimum volume morph.

    directions : object, optional
            A list of 2 directions to define specific orientation for the morph box. Must be perpendicular to each other.

    Returns
    -------
    object
            Returns the newly created morph object on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def morph():
                morph.MorphOrtho(db_or_visible="DB")

                morph.MorphOrtho(db_or_visible="Visible", min_flag=True)

                shells = base.CollectEntities(constants.NASTRAN, None, "SHELL", filter_visible=True)
                morph.MorphOrtho(loaded_elements=shells, min_flag=True)

                vectors = [[0.0, 0.5, 0.5], [1.0, 0.0, 0.0]]
                morph.MorphOrtho(shells, directions=vectors)


    """


def MorphParPrj(
    dx: float, dy: float, dz: float, morph: object, morph_edge: object
) -> int:
    """

    Script function for the projection of x,y,z on a morph edge.

    Parameters
    ----------
    dx : float
            The x coordinate of the point to project.

    dy : float
            The y coordinate of the point to project.

    dz : float
            The z coordinate of the point to project.

    morph : object
            The morph box element to which the edge belongs.

    morph_edge : object
            The morph edge element.

    Returns
    -------
    int
            Returns the new id on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                a = base.GetEntity(constants.NASTRAN, "MORPHEDGE", 30)
                morph.MorphProject(2.4, 74.0, 233.0, a)
                b = base.GetEntity(constants.NASTRAN, "MORPHBOX", 3)
                morph.MorphParPrj(2.4, 74, 243, b, a)


    """


def MorphParam(param: object, dist: float) -> int:
    """

    Script function for editing morph parameters.

    Parameters
    ----------
    param : object
            The parameter element.

    dist : float
            The value that will be applied in the parameter.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def paramsScriptMove(p, val):
                a = base.GetEntity(0, "PARAMETERS", p)
                morph.MorphParam(a, val)


    """


def MorphParamCreate(name: str, type: str, arguments_list) -> int:
    """

    Script function for the creation of a morph parameter.

    It uses other script functions to create a morph parameter.

    Parameters
    ----------
    name : str
            is the desired name for the new parameter

    type : str
            type can be one of the following parameter types:
            "MorphTransl" -- it will create a Transform- Translate parameter.
            arguments_list: object is a list with 5 entries
            list morph_points
            coordinate system object
            dx, dy, dz translate vector
            "MorphTransform" -- it will create a Transform- Transform parameter.
            arguments_list: object is a list with 2 entries
            list morph_points and list transform entities (points or coordinates)
            "MorphScale" -- it will create a Transform- Scale parameter.
            arguments_list: object is list with 4 entries
            list morph_points
            scale points cordinates origin_x, origin_y, origin_z
            "MorphRotate" -- it will create a Transform- Rotate parameter.
            arguments_list: object is list with 8 entries
            list morph_points
            coordinate system object
            dx, dy, dz vector
            origin_x, origin_y, origin_z origin position
            "arguments_list: object is a list with 5 entries
            list morph_points
            "MorphAlign" == it will create an Transform -Align parameter
            arguments_list: is an object created by MorphCreateMorphAlignArgs
            "MorphUserTang" -- it will create an User Tangent parameter.
            arguments_list: object is list with 1 entry
            list morph_user_tangency
            "MorphAngle" -- it will create an Angle parameter.
            arguments_list: object is list with 1 entry
            list morph_edges in stady-moved format
            "MorphDeform" -- it will create a Deformation parameter.
            arguments_list: object is list with 1 entry
            integer flag for affected 0:All, 1: Moved
            "MorphEdgeFit" -- it will create an EdgeFit parameter.
            arguments_list: object is list with 2 entries
            list morph_edges
            list curves
            "MorphMove" -- it will create an Extend parameter.
            arguments_list: object is list with 2 entries
            list morph_points
            list morph_edges
            "MorphOffset" -- it will create an Offset parameter.
            arguments_list: object is list with 1 entry
            list of morph_faces
            "MorphRadius" -- it will create a Radius parameter.
            arguments_list: object is list with 1 entry
            list of morph_faces
            "MorphInner" -- it will create an Inner parameter.
            arguments_list: object is list with 1 entry
            list of morph_concentric_edges
            "MorphSetsAlign" -- it will create a Direct Align parameter.
            arguments_list: object is list with 5 entries
            set object of elements to be included
            set object of elements to move as rigid
            set of elements to retain position
            set of elements to align to
            align distance
            "MorphSetsOffset" -- it will create a Direct Offset parameter.
            arguments_list: object is list with 3 entries
            set of elements to be included
            set of elements to move as rigid
            set of elements to retain position
            "MorphSetsTranslate" -- it will create a Direct Translate parameter.
            arguments_list: object is list with 6 entries
            set of elements to be included
            set of elements to move as rigid
            set of elements to retain position
            dx, dy, dz
            "MorphSetsRotate" -- it will create a Direct Rotate parameter.
            arguments_list: object is list with 9 entries
            set of elements to be included
            set of elements to move as rigid
            set of elements to retain position
            dx, dy, dz, origin_x, origin_y, origin_z
            "DFMTranslate" -- it will create a DFM Translate parameter.
            arguments_list: object is list with 6 entries
            list entities or list of matrices of lists to be translated
            list [dx, dy, dz] or list of lists [dx, dy, dz] with the translate vector(s),
            list of entities to be morphed,
            list of bounds,
            C.Entities Sampling flag: 0 to disable sampling, 1 to sample points from perimeters
            Auto Bounds flag: 1 to activate automatic bounds recognition, 0 otherwise.

    arguments_list :

    Returns
    -------
    int
            Returns the id of the created parameter on success, 0 on failure.

    See Also
    --------
    NewParameterDFMFitEdges, NewParameterAngle, NewParameterDeformation, NewParameterDFMAlign, NewParameterDFMFitSurfaces, NewParameterDFMOffset, NewParameterDFMRotate, NewParameterDFMScale, NewParameterDFMTranslate, NewParameterDFMTransform, NewParameterTransform, NewParameterTranslate, NewParameterEdgeFit, NewParameterExtend, NewParameterOffset, NewParameterRadiusInner, NewParameterRadiusOuter, NewParameterRotate, NewParameterUserTangent, NewParameterScale, NewParameterSlideFeatureCurve, NewParameterSlideFeatureRotate, NewParameterSlideFeatureScale, NewParameterSlideFeatureTranslate, NewParameterTailoredBlank

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            # move
            def extendParam():
                morph_edges = []
                morph_points = []
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 25))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 28))

                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 28))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 40))

                morph.MorphParamCreate("extend_param", "MorphMove", (morph_points, morph_edges))


            # offset
            def offsetParam():
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 21))
                faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 24))
                morph.MorphParamCreate("offset_param", "MorphOffset", (faces,))


            # scale
            def scaleParam():
                morph_points = []
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 28))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 40))
                morph.MorphParamCreate("scale_param", "MorphScale", (morph_points, 1.0, 1.0, 0.0))


            # translate
            def translParam():
                morph_points = []
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 28))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 40))
                morph.MorphParamCreate(
                    "translate_param", "MorphTransl", (morph_points, None, 1.0, 1.0, 0.0)
                )


            # rotate
            def rotateParam():
                morph_points = []
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 28))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 40))
                morph.MorphParamCreate(
                    "rotate_param",
                    "MorphRotate",
                    (morph_points, None, 1.0, 1.0, 0.0, 641, 51, -162),
                )


            # angle
            def angleParam():
                morph_edges = []
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 22))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 28))
                morph.MorphParamCreate("angle_param", "MorphAngle", (morph_edges,))


            # deform
            def deformParam():
                morph.MorphParamCreate("deform_param", "MorphDeform", (0,))


            # inner
            def innerParam():
                morph_edges = []
                morph_edges.append(base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 85))
                morph.MorphParamCreate("inner_param", "MorphInner", (morph_edges,))


            # radius
            def radiusParam():
                morph_faces = []
                morph_faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 12))
                morph.MorphParamCreate("radius_param", "MorphRadius", (morph_faces,))


            # userTang
            def userTangParam():
                morph_user_tang = []
                morph_user_tang.append(base.GetEntity(constants.NASTRAN, "MORPHTANG", 1))
                morph.MorphParamCreate("userTang_param", "MorphUserTang", (morph_user_tang,))


            # edgFit
            def edgFitParam():
                morph_edges = []
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 198))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 163))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 148))
                morph_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 151))
                curves_array = []
                curves_array.append(base.GetEntity(constants.NASTRAN, "CURVE", 11))
                curves_array.append(base.GetEntity(constants.NASTRAN, "CURVE", 10))
                curves_array.append(base.GetEntity(constants.NASTRAN, "CURVE", 12))
                curves_array.append(base.GetEntity(constants.NASTRAN, "CURVE", 9))
                morph.MorphParamCreate("edgFit_param", "MorphEdgeFit", (morph_edges, curves_array))


            # setsAlign
            def setsAlignParam():
                included_shells = base.GetEntity(constants.NASTRAN, "SET", 2)
                rigid_shells = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds_shells = base.GetEntity(constants.NASTRAN, "SET", 4)
                align_to_shells = base.GetEntity(constants.NASTRAN, "SET", 5)
                morph.MorphParamCreate(
                    "setsAlign_param",
                    "MorphSetsAlign",
                    (included_shells, rigid_shells, bounds_shells, align_to_shells, 100),
                )


            # setsOffset
            def setsOffsetParam():
                included_shells = base.GetEntity(constants.NASTRAN, "SET", 2)
                rigid_shells = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds_shells = base.GetEntity(constants.NASTRAN, "SET", 4)
                morph.MorphParamCreate(
                    "setsOffset_param",
                    "MorphSetsOffset",
                    (included_shells, rigid_shells, bounds_shells),
                )


            # setsTranslate
            def setsTranslateParam():
                included_shells = base.GetEntity(constants.NASTRAN, "SET", 2)
                rigid_shells = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds_shells = base.GetEntity(constants.NASTRAN, "SET", 4)
                morph.MorphParamCreate(
                    "setsTranslate_param",
                    "MorphSetsTranslate",
                    (included_shells, rigid_shells, bounds_shells, 1.0, 1.0, 0.0),
                )


            # setsRotate
            def setsRotateParam():
                included_shells = base.GetEntity(constants.NASTRAN, "SET", 2)
                rigid_shells = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds_shells = base.GetEntity(constants.NASTRAN, "SET", 4)
                morph.MorphParamCreate(
                    "setsRotate_param",
                    "MorphSetsRotate",
                    (included_shells, rigid_shells, bounds_shells, 1.0, 1.0, 0.0, 641, 51, -162),
                )


            # DFM Translate Single list of translate item
            def dfm_translate():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set = base.GetEntity(constants.NASTRAN, "SET", 7)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the translate entities, morph entities and bounds matrices
                transf_m = base.CollectEntities(constants.NASTRAN, transf_it_set, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                # we define the translate vector
                translate_vector = (0.5, 0.5, 0.0)  # dx, dy, dz

                ret = morph.MorphParamCreate(
                    "dfm_translate_single",
                    "DFMTranslate",
                    (transf_m, translate_vector, entities_m, bounds_m, 1),
                )


            # DFM Translate  list of matrices of translate items
            def dfm_translate_list():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set1 = base.GetEntity(constants.NASTRAN, "SET", 1)
                transf_it_set2 = base.GetEntity(constants.NASTRAN, "SET", 2)
                transf_it_set3 = base.GetEntity(constants.NASTRAN, "SET", 3)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the translate entities, morph entities and bounds matrices
                transf_m1 = base.CollectEntities(constants.NASTRAN, transf_it_set1, "FACE")
                transf_m2 = base.CollectEntities(constants.NASTRAN, transf_it_set2, "FACE")
                transf_m3 = base.CollectEntities(constants.NASTRAN, transf_it_set3, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                transf_m = (transf_m1, transf_m2, transf_m3)

                # we define the translate vector, Suppose that transf_m1 should move along the same vector
                translate_vector1 = (0.5, 0.5, 0.0)  # dx, dy, dz
                translate_vector2 = (0.5, 0.5, 0.0)  # dx, dy, dz
                translate_vector3 = (0.0, 0.0, 1.0)  # dx, dy, dz

                translate_vector = (translate_vector1, translate_vector2, translate_vector3)

                # Attention: transf_m and translate_vector should have the same len

                ret = morph.MorphParamCreate(
                    "dfm_translate_multi",
                    "DFMTranslate",
                    (transf_m, translate_vector, entities_m, bounds_m, 1, 1),
                )


            # DFM Rotate Single list of translate item
            def dfm_rotate():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set = base.GetEntity(constants.NASTRAN, "SET", 7)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the rotate entities, morph entities and bounds matrices
                transf_m = base.CollectEntities(constants.NASTRAN, transf_it_set, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                # we define the rotate axis
                rotate_axis = (0.0, 0.0, 0.0, 1.0, 0.0, 0.0)  # x, y, xz, dx, dy, dz

                ret = morph.MorphParamCreate(
                    "dfm_rotate_single",
                    "DFMRotate",
                    (transf_m, rotate_axis, entities_m, bounds_m, 1, 0),
                )


            # DFM Rotate  list of matrices of translate items
            def dfm_rotate_list():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set1 = base.GetEntity(constants.NASTRAN, "SET", 1)
                transf_it_set2 = base.GetEntity(constants.NASTRAN, "SET", 2)
                transf_it_set3 = base.GetEntity(constants.NASTRAN, "SET", 3)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the translate entities, morph entities and bounds matrices
                transf_m1 = base.CollectEntities(constants.NASTRAN, transf_it_set1, "FACE")
                transf_m2 = base.CollectEntities(constants.NASTRAN, transf_it_set2, "FACE")
                transf_m3 = base.CollectEntities(constants.NASTRAN, transf_it_set3, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                transf_m = (transf_m1, transf_m2, transf_m3)

                # we define the rotate axis, Suppose that transf_m1 should move along the same vector
                rotate_axis1 = (0.0, 0.0, 0.0, 1.0, 0.0, 0.0)  # x, y, xz, dx, dy, dz
                rotate_axis2 = (0.0, 0.0, 0.0, 1.0, 0.0, 0.0)  # x, y, xz, dx, dy, dz
                rotate_axis3 = (0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # x, y, xz, dx, dy, dz

                rotate_axis = (rotate_axis1, rotate_axis2, rotate_axis3)

                # Attention: transf_m and rotate_axis should have the same len

                ret = morph.MorphParamCreate(
                    "dfm_rotate_multi",
                    "DFMRotate",
                    (transf_m, rotate_axis, entities_m, bounds_m, 1, 0),
                )


            # DFM Scale Single list of translate item
            # DFM Scale  list of matrices of translate items : look above


            # DFM Transform Single list of translform item
            def dfm_transform():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set = base.GetEntity(constants.NASTRAN, "SET", 7)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the rotate entities, morph entities and bounds matrices
                transf_m = base.CollectEntities(constants.NASTRAN, transf_it_set, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                # we define the coordinate systems
                coord = [
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    1,
                    10,
                    10,
                    10,
                    11,
                    10,
                    10,
                    10,
                    11,
                    10,
                    10,
                    10,
                    11,
                ]

                ret = morph.MorphParamCreate(
                    "dfm_transform_single",
                    "DFMTransform",
                    (transf_m, coord, entities_m, bounds_m, 1, 0),
                )


            # DFM Transform Multi list of transform item
            def dfm_transform():
                transf_it_set1 = base.GetEntity(constants.NASTRAN, "SET", 1)
                transf_it_set2 = base.GetEntity(constants.NASTRAN, "SET", 2)
                transf_it_set3 = base.GetEntity(constants.NASTRAN, "SET", 3)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the translate entities, morph entities and bounds matrices
                transf_m1 = base.CollectEntities(constants.NASTRAN, transf_it_set1, "FACE")
                transf_m2 = base.CollectEntities(constants.NASTRAN, transf_it_set2, "FACE")
                transf_m3 = base.CollectEntities(constants.NASTRAN, transf_it_set3, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                transf_m = (transf_m1, transf_m2, transf_m3)

                # we define the corresponding coordinate systems.
                coord1 = base.GetEntity(constants.NASTRAN, "COORD", 1)
                coord2 = base.GetEntity(constants.NASTRAN, "COORD", 2)
                coord3 = base.GetEntity(constants.NASTRAN, "COORD", 3)
                coord4 = base.GetEntity(constants.NASTRAN, "COORD", 4)
                coord5 = base.GetEntity(constants.NASTRAN, "COORD", 5)
                coord6 = base.GetEntity(constants.NASTRAN, "COORD", 6)

                coord_m = ((coord1, coord2), (coord3, coord4), (coord5, coord6))

                # Attention: transf_m and coord_m should have the same len

                ret = morph.MorphParamCreate(
                    "dfm_transform_multi",
                    "DFMTransform",
                    (transf_m, coord_m, entities_m, bounds_m, 1, 0),
                )


            # DFM Offset Single list of offset item
            def dfm_offset():
                # We assume that there are some predifined sets in current database. We collect these sets
                transf_it_set = base.GetEntity(constants.NASTRAN, "SET", 7)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the rotate entities, morph entities and bounds matrices
                transf_m = base.CollectEntities(constants.NASTRAN, transf_it_set, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                ret = morph.MorphParamCreate(
                    "dfm_offset_single", "DFMOffset", (transf_m, entities_m, bounds_m, 1, 0)
                )


            # DFM Offset Multi list of offset item
            def dfm_transform():
                transf_it_set1 = base.GetEntity(constants.NASTRAN, "SET", 1)
                transf_it_set2 = base.GetEntity(constants.NASTRAN, "SET", 2)
                transf_it_set3 = base.GetEntity(constants.NASTRAN, "SET", 3)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                # We create the translate entities, morph entities and bounds matrices
                transf_m1 = base.CollectEntities(constants.NASTRAN, transf_it_set1, "FACE")
                transf_m2 = base.CollectEntities(constants.NASTRAN, transf_it_set2, "FACE")
                transf_m3 = base.CollectEntities(constants.NASTRAN, transf_it_set3, "FACE")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "FACE")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "FACE")

                transf_m = (transf_m1, transf_m2, transf_m3)

                ret = morph.MorphParamCreate(
                    "dfm_offset_multi", "DFMOffset", (transf_m, entities_m, bounds_m, 1, 0)
                )


            # DFM Surface Fit Single Area
            # assume that you have a single area that you want to be fitted in a target area
            def dfm_surface_fit():
                # We assume that there are some predifined sets in current database. We collect these sets
                origin_set = base.GetEntity(constants.NASTRAN, "SET", 1)
                target_set = base.GetEntity(constants.NASTRAN, "SET", 2)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                origin_m = base.CollectEntities(constants.NASTRAN, origin_set, "SHELL")
                target_m = base.CollectEntities(constants.NASTRAN, target_set, "SHELL")
                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "SHELL")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "SHELL")

                # Now we collect corresponding nodes. Corresponding nodes should lay on area (origin or target) perimeters.
                # Origin nodes should be perimetric nodes of origin area and target nodes should be perimetric nodes of target area.

                originn1 = base.GetEntity(constants.NASTRAN, "GRID", 1)
                originn2 = base.GetEntity(constants.NASTRAN, "GRID", 2)
                originn3 = base.GetEntity(constants.NASTRAN, "GRID", 3)
                originn4 = base.GetEntity(constants.NASTRAN, "GRID", 4)

                originn = (originn1, originn2, originn3, originn4)

                targetn1 = base.GetEntity(constants.NASTRAN, "GRID", 5)
                targetn2 = base.GetEntity(constants.NASTRAN, "GRID", 6)
                targetn3 = base.GetEntity(constants.NASTRAN, "GRID", 7)
                targetn4 = base.GetEntity(constants.NASTRAN, "GRID", 8)

                targetn = (targetn1, targetn2, targetn3, targetn4)

                # originn and targetn should contain at least 3 nodes each and have the same length

                ans = morph.MorphParamCreate(
                    "dfm_surface_fit_single",
                    "DFMSurfaceFit",
                    (origin_m, target_m, originn, targetn, entities_m, bounds_m, 0),
                )


            # DFM Surface Fit Multi Area
            # Now lets assume that you have a two seperated areas that you want to be fitted into to target areas and morph a common area
            def dfm_surface_fit_multi():
                # We assume that there are some predifined sets in current database. We collect these sets
                origin_set1 = base.GetEntity(constants.NASTRAN, "SET", 1)
                target_set1 = base.GetEntity(constants.NASTRAN, "SET", 2)
                origin_set2 = base.GetEntity(constants.NASTRAN, "SET", 3)
                target_set2 = base.GetEntity(constants.NASTRAN, "SET", 4)
                entities_it_set = base.GetEntity(constants.NASTRAN, "SET", 8)
                bounds_it_set = base.GetEntity(constants.NASTRAN, "SET", 9)

                origin_m1 = base.CollectEntities(constants.NASTRAN, origin_set1, "SHELL")
                target_m1 = base.CollectEntities(constants.NASTRAN, target_set1, "SHELL")
                origin_m2 = base.CollectEntities(constants.NASTRAN, origin_set2, "SHELL")
                target_m2 = base.CollectEntities(constants.NASTRAN, target_set2, "SHELL")

                origin_m = (origin_m1, origin_m2)
                target_m = (target_m1, target_m2)

                # Attention: origin_m and target_m should have the same lenght

                entities_m = base.CollectEntities(constants.NASTRAN, entities_it_set, "SHELL")
                bounds_m = base.CollectEntities(constants.NASTRAN, bounds_it_set, "SHELL")

                # Now we collect corresponding nodes. Corresponding nodes should lay on area (origin or target) perimeters.
                # Origin nodes should be perimetric nodes of origin area and target nodes should be perimetric nodes of target area.

                # We collect the perimetric nodes of origin_m1 area
                originn11 = base.GetEntity(constants.NASTRAN, "GRID", 1)
                originn12 = base.GetEntity(constants.NASTRAN, "GRID", 2)
                originn13 = base.GetEntity(constants.NASTRAN, "GRID", 3)
                originn14 = base.GetEntity(constants.NASTRAN, "GRID", 4)

                originn1 = (originn11, originn12, originn13, originn14)

                # We collect the perimetric nodes of target_m1 area
                targetn11 = base.GetEntity(constants.NASTRAN, "GRID", 5)
                targetn12 = base.GetEntity(constants.NASTRAN, "GRID", 6)
                targetn13 = base.GetEntity(constants.NASTRAN, "GRID", 7)
                targetn14 = base.GetEntity(constants.NASTRAN, "GRID", 8)

                targetn1 = (targetn11, targetn12, targetn13, targetn14)

                # The we do the same job for the secondary areas
                originn21 = base.GetEntity(constants.NASTRAN, "GRID", 101)
                originn22 = base.GetEntity(constants.NASTRAN, "GRID", 102)
                originn23 = base.GetEntity(constants.NASTRAN, "GRID", 103)
                originn24 = base.GetEntity(constants.NASTRAN, "GRID", 104)

                originn2 = (originn21, originn22, originn23, originn24)

                targetn21 = base.GetEntity(constants.NASTRAN, "GRID", 105)
                targetn22 = base.GetEntity(constants.NASTRAN, "GRID", 106)
                targetn23 = base.GetEntity(constants.NASTRAN, "GRID", 107)
                targetn24 = base.GetEntity(constants.NASTRAN, "GRID", 108)

                targetn2 = (targetn21, targetn22, targetn23, targetn24)

                # Now we create the list of corresponding nodes matrices
                originn = (originn1, originn2)
                targetn = (targetn1, targetn2)

                # Attention: originn and targetn should have the same length with origin_m, target_m.
                # \t   Also matrices of perimetric nodes should be placed in the same position as area is placed.
                # \t   For example nodes in list which is at originn[0] are perimetric of the area list at origin_m[0]

                # originn* and targetn* should contain at least 3 nodes each and have the same length

                ans = morph.MorphParamCreate(
                    "dfm_surface_fit_multi",
                    "DFMSurfaceFit",
                    (origin_m, target_m, originn, targetn, entities_m, bounds_m, 1),
                )
                # DFM Edge Fit Single list
                # DFM Edge Fit Multi list : look DFM surface fit and ignore the step of corresponding nodes


            # Slide feature translate parameter
            def slfeature_translate():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)
                m1 = [entities]
                ans = morph.MorphParamCreate(
                    "Slide feature, Translate", "SLFeatureTranslate", (m1, 0, 1.0, 0.0, 0.0)
                )


            # Slide feature rotate parameter
            def slfeature_rotate():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)
                m1 = [entities]
                ans = morph.MorphParamCreate(
                    "Slide feature, Rotate",
                    "SLFeatureRotate",
                    (m1, 0, 10.0, 10.0, 10.0, 0.0, 0.0, 1.0),
                )


            # Slide feature scale parameter
            def slfeature_scale():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)
                m1 = [entities]
                ans = morph.MorphParamCreate(
                    "Slide feature, Scale", "SLFeatureScale", (m1, 1.0, 1.0, 0.0)
                )


            # Slide feature curve parameter
            def slfeature_curve():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                m1 = [entities]
                ans = morph.MorphParamCreate(
                    "Slide feature, Curve", "SLFeatureCurve", (m1, curve, 1)
                )


    """


def MorphPaste(hatch1: object, hatch2: object, paste_on_middle: bool) -> int:
    """

    Script function for pasting 2 free morph hatches.

    Parameters
    ----------
    hatch1 : object
            The first object of a free morph hatch.

    hatch2 : object
            The second object of a free morph hatch.

    paste_on_middle : bool, optional
            A flag that defines whether to paste on middle plane (True)
            or not (False-default value).

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                a = base.GetEntity(constants.NASTRAN, "MORPHFACE", 32)
                b = base.GetEntity(constants.NASTRAN, "MORPHFACE", 40)
                morph.MorphPaste(a, b)


    """


def MorphPntSnap(grid_point: object, morph_point: object, flag: int) -> int:
    """

    Script function for the movement of morph control points.

    Parameters
    ----------
    grid_point : object
            The grid point to get coordinates.

    morph_point : object
            The morph control point to move.

    flag : int
            Should be 1 for morphing or 0 for modifying only edges,
            without FE movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                a = base.GetEntity(constants.NASTRAN, "GRID", 1)
                b = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 13)
                morph.MorphPntSnap(a, b, 1)


    """


def MorphPointDel(morph_points: object) -> int:
    """

    Script function for the deletion of morph control points.

    Parameters
    ----------
    morph_points : object
            A list of morph control points.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import constants
            from ansa import base


            def delPoints():
                morph_points = []
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 153))
                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 154))
                morph.MorphPointDel(morph_points)


    """


def MorphProject(x: float, y: float, z: float, morph_edge: object) -> int:
    """

    Script function for the projection of x,y,z on a morph edge.

    Parameters
    ----------
    x : float
            The x global coordinate.

    y : float
            The y global coordinate.

    z : float
            The z global coordinate.

    morph_edge : object
            The morph edge element.

    Returns
    -------
    int
            Returns the id of the new Control Point on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                a = base.GetEntity(constants.NASTRAN, "MORPHEDGE", 30)
                morph.MorphProject(2.4, 74.0, 233.0, a)
                b = base.GetEntity(constants.NASTRAN, "MORPHBOX", 3)
                morph.MorphParPrj(2.4, 74, 243, b, a)


    """


def MorphRMDBL(tolerance: float) -> int:
    """

    Script function for deleting close control points in all visible morphes.

    Parameters
    ----------
    tolerance : float
            The tolerance where close points will be searched.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphRMDBL(500)


    """


def MorphRadius(morph_hatces: object, d: float, flag: int) -> int:
    """

    Script function for changing the radius of cylindrical morph hatches.

    Parameters
    ----------
    morph_hatces : object
            A list with morph hatch elements of cylindrical morphes.

    d : float
            The new radius for the hatces.

    flag : int
            1 for morphing or 0 for modifying only edges,
            without FE movement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def radiusAT(b):
                m1 = []
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", b))
                morph.MorphRadius(m1, 120, 1)


    """


def MorphRelocate(morph_edges: object) -> int:
    """

    Script function for relocating control points in morph edges.

    Parameters
    ----------
    morph_edges : object
            A list of morph edges elements, in order for their middle
            control points to be equally distributed over the edge.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                m = []
                for i in range(20):
                    m.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", i))
                morph.MorphRelocate(m)


    """


def MorphRmTang() -> int:
    """

    Script function for removing all tangency from all visible morphes.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphRmTang()


    """


def MorphScale(
    morph: object, flag: int, d1: float, d2: float, d3: float, d4: float
) -> int:
    """

    Script function for scaling a morph.

    Parameters
    ----------
    morph : object
            The morph element that will be copied.

    flag : int
            1 or 0 to morph or not the loaded elements.

    d1 : float
            The scale factor.

    d2 : float
            The x global coordinate of the base point.

    d3 : float
            The y global coordinate of the base point.

    d4 : float
            The z global coordinate of the base point.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                a = base.GetEntity(constants.NASTRAN, "MORPHBOX", 1)
                morph.MorphScale(a, 1, 10, 10, 10, 10)


    """


def MorphResult(directory: str, openfoam_gw: str, max_displacement: float) -> int:
    """

    Script function for result based morphing.

    Parameters
    ----------
    directory : str
            Output directory.

    openfoam_gw : str
            Gw openfoam filename.

    max_displacement : float
            Maximium displacement.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphResult("/home/dir2/script", "/home/dir2/Gw", 10.0)


    """


def MorphSplit(
    box_points: object,
    non_isoparam: bool,
    fit_new_skin_edges: bool,
    box_edges: object,
    number_of_splits: int,
    work_on: str,
) -> int:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`BoxSplit` instead.


    Script function for splitting morph box(es).
    The split can be performed either isoparametrically or at two different parameters in opposite edges.
    In the first case the user can provide one morphing point or a list of morphing points in which the
    split will be performed and travelled throughout the box in the same parameter. In the second case
    the user must provide a list of morphing points where each and every pair of them gives the starting
    and the ending point of the split. For example, if the user provides a list with four morphing points,
    a non-isoparametrical split (cut) will be performed for the first and the second point in the list and
    another one for the third and fourth one. If the box points list has an odd number of points, the last
    point will be ignored except for the case of a single point where isoparametrical split will be performed.

    Parameters
    ----------
    box_points : object, optional
            A box point or a list of box points, where the box(es) will be cut.

    non_isoparam : bool, optional
            For a non-isoparametrical split (cut), this value should be set to 'True'.

    fit_new_skin_edges : bool, optional
            If set to True, new skin edges will fit on the underlying model.
            Default value is False.

    box_edges : object, optional
            A box edge or a list of box edges, where the box(es) will be cut
            according to the number of splits that is defined (argument
            "number_of_splits").

    number_of_splits : int, optional
            Defines the number of splits on the input box edges (argument
            "box_edges")

    work_on : str, optional
            Defines where the projection is going to take place:
            'whole_db' fit skin edges will take place on the whole database,
            'visible'  fit skin edges will take place only on the visible elements
            If work_on is not set then whole_db will be the default argument.
            This option is only available only when fit_skin_edges is set to true.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    MorphSplitProject, MorphSplitToHexa, MorphSplitToPenta

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main(point):
                b = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 10)
                morph.MorphSplit(b)

                points = []
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 1))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 3))
                morph.MorphSplit(points)


            # ...or...


            def main():
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 1))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 2))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 3))

                morph.MorphSplit(
                    points, True
                )  # in this case, the third point will be ignored and a single cut will be performed between points 1, 2


            def main():
                edges = []
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "MORPHEDGE", 9))
                edges.append(base.GetEntity(ansa.base.CurrentDeck(), "MORPHEDGE", 21))
                ansa.morph.MorphSplit(
                    box_edges=edges, number_of_splits=3
                )  # make 3 splits in every input box edge


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: BoxSplit instead.",
        DeprecationWarning,
    )


def MorphTangent(entities: object) -> int:
    """

    Script function for the creation of tangency between morph edges or morph boxes.

    Parameters
    ----------
    entities : object
            A list of morph edges or morph boxes.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                edges = []
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 59))
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 31))
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 29))
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 9))

                edges.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 3))
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 4))
                morph.MorphTangent(edges)


    """


def MorphTopoVis(tolerance: str) -> int:
    """

    Script function for connecting all visible morphing boxes. Available option for
    the definition of topology tolerance mode.

    Parameters
    ----------
    tolerance : str, optional
            A string to define the tolerance mode, accepting
            "draft", "middle", "fine" or "extra fine".
            Default mode depends on Resolution/Tolerances/Units
            and Morph/Optimization settings.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    MorphTopo

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphTopoVis("extra fine")
                morph.MorphTopoVis()


    """


def MorphTransl(m1: object, p1: object, dx: float, dy: float, dz: float) -> int:
    """

    Script function for the translation of morph control points.

    Parameters
    ----------
    m1 : object
            A list of morph control points.

    p1 : object
            A valid coordinate element or None for global.

    dx : float
            The x component of the vector.

    dy : float
            The y component of the vector.

    dz : float
            The z component of the vector.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                b = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 13)
                c = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 22)
                m1 = (c, b)
                morph.MorphTransl(m1, None, 30.0, 0.0, 0.0)


    """


def MorphUserTangent(m1: object, dx: float, dy: float, dz: float) -> int:
    """

    Script function for the definition or modification of user tangents at morph control points.

    Parameters
    ----------
    m1 : object
            A list that contains the morph control points and edges where
            user tangents will be created. Definition of morph edges is
            necessary in cases that we want to create user tangents on
            corner points. For intermediate points, there is no need to
            define edges. In cases that we want to create user tangents on
            corner points, matrix should contain the control point,
            followed by its edge.

    dx : float
            The x component of the user defined tangent.

    dy : float
            The y component of the user defined tangent.

    dz : float
            The z component of the user defined tangent.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                pnt1 = base.Entity(ansa.constants.NASTRAN, 40, "MORPHPOINT")  # corner point
                edge1 = base.Entity(ansa.constants.NASTRAN, 109, "MORPHEDGE")
                pnt2 = base.Entity(ansa.constants.NASTRAN, 35, "MORPHPOINT")  # corner point
                edge2 = base.Entity(ansa.constants.NASTRAN, 139, "MORPHEDGE")
                pnt3 = base.Entity(
                    ansa.constants.NASTRAN, 5109, "MORPHPOINT"
                )  # intermediate point (no need to define box edge)

                ents = []
                ents.append(pnt1)
                ents.append(edge1)
                ents.append(pnt2)
                ents.append(edge2)
                ents.append(pnt3)

                ans = morph.MorphUserTangent(ents, 1, 0, 1)


    """


def PerformDoeStudy(
    opt_task_id: int,
    comb_file: str,
    dir_path: str,
    solver: str,
    solver_session_file: str,
    post_processing: str,
    meta_session_file: str,
    meta_response_file: str,
    empty_experiments_directory: bool,
    single_directory: bool,
    pre_processing: str,
    save_database: bool,
    dm_signature: object,
    sim_run_save_action: str,
    detailed_results: bool = False,
    upload_doe_study: bool = False,
    existing_doe_study: str = None,
) -> int:
    """

    Function to perform a DOE study.

    Parameters
    ----------
    opt_task_id : int
            Define the id of the optimization task you want to run.

    comb_file : str
            Define the path of the file that contains the combinations
            you want to run.

    dir_path : str
            Define the directory you want to save the experiments.
            The value "DM:" must be used in order for the Experiments to be automatically uploaded to DM

    solver : str, optional
            Defines the solver that will be used in DOE. Supported solvers
            are "NASTRAN", "LS-DYNA", "PAMCRASH", "ABAQUS", "ANSYS",
            "EPILYSIS", "FLUENT" and "FLUENT 2D".

    solver_session_file : str, optional
            The path of the session file necessary to run a solver. Session
            file is essential for running Ansys.

    post_processing : str, optional
            Defines if META will be used after running solver. Accepted
            keyword's values are "Meta" and "None".

    meta_session_file : str, optional
            The path of the session file that META requires.
            (without it, META cannot run)

    meta_response_file : str, optional
            The name of the response file that META will generate.
            This keyword is optional for running META (by default,
            response filename is "response.txt").

    empty_experiments_directory : bool, optional
            Define if experiments' directory will be emptied
            before the generation of the new experiments.
            (Default: False)

    single_directory : bool, optional
            Define if all output files are saved in a single directory.
            (Default: False)

    pre_processing : str, optional
            Accepted values are "based_on_current" and "create_experiments".
            It defines if DOE will be performed to existing experiments or it will
            create new.
            (Default: "create_experiments")

    save_database : bool, optional
            Define if ANSA database is saved for every experiment.
            (Default: False)

    dm_signature : object, optional
            The Simulation Run signature for DM, defining the Simulation_Model and LoadCase where the Runs will be stored under.
            This argument must be a dictionary with keys: "Simulation_Model" and "LoadCase"
            and values dictionaries for the respective names/values.

    sim_run_save_action : str, optional
            Specify this argument in case of "DM:". By using "DOE Iteration" value, initial state will additionally run.

    detailed_results : bool, optional
            This argument determines whether the return value will be a dictionary containing the following:
            1. a list with Experiment Server Ids with the key "sim_runs_server_ids"
            2. the Server Id of the created DOE_Study object with the key "doe_study_server_id", only if the upload_doe_study argument is True

    upload_doe_study : bool, optional
            The script function will create a DOE_Study with all the created Experiments and save it in DM.

    existing_doe_study : str, optional
            This argument is used when we need to append the new Experiments to an existing DOE_Study object. The DOE_Study's server id needs to be provided to this argument in that case.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base


            def main():
                morph.PerformDoeStudy(
                    2, "C:/tmp/users/folder/combFile.txt", "C:/tmp/users/folder/results/"
                )

                # In order to automatically upload Experiments to DM:
                ansa.dm.SetRoot("//.../DM")
                dm_signature = dict()
                model_signature = {
                    "Discipline": "durability",
                    "Model Id": "body",
                    "Model Variant": "A",
                    "Project": "suspension",
                    "Release": "1",
                    "Iteration": "001",
                    "File Type": "Nastran",
                }
                dm_signature["Simulation_Model"] = model_signature
                loadcase_signature = {"Loadcase Id": "-", "Iteration": "01", "File Type": "Nastran"}
                dm_signature["LoadCase"] = loadcase_signature
                morph.PerformDoeStudy(
                    1, "./combinations.txt", "DM:", save_database=False, dm_signature=dm_signature
                )


    """


def MorphEdgeFitOnSurfs(
    edges: object,
    surface_ents: object,
    add_pnts: int,
    search_distance: float,
    user_projection_mode_vector: object,
) -> int:
    """

    A function to fit box edges on target surface (target surface can be defined by shells and geometrical faces).

    Parameters
    ----------
    edges : object
            A list with morph edges.

    surface_ents : object
            A list of entities, parts, properties, materials, sets or macros.
            If it equals to 0, the visible shells and/or faces are collected.

    add_pnts : int
            A flag to define the auto insertion of control point on box edges.
            Set it 1 for auto insertion and 0 for no auto insertion.

    search_distance : float, optional
            A search distance for projection.

    user_projection_mode_vector : object, optional
            A list with a user projection vector [dx,dy,dz].

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def edgefitOnSurfs():
                m1 = []
                m2 = []
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 64))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 76))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 100))
                m1.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 136))
                m2.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                vec = [1.0, 0.0, 1.0]
                morph.MorphEdgeFitOnSurfs(
                    m1, m2, 1, search_distance=180, user_projection_mode_vector=vec
                )
                # morph.MorphEdgeFitOnSurfs(m1, m2, 1, user_projection_mode_vector=vec)
                # morph.MorphEdgeFitOnSurfs(m1, m2, 1, search_distance=180)


    """


def MorphParamMerge(parameters: object) -> int:
    """

    Function for merging morph parameters.

    Parameters
    ----------
    parameters : object
            A list containing morph parameters to be merged.
            (Should be of the same type)

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def paramsMerge():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "PARAMETERS", 1))
                m.append(base.GetEntity(constants.NASTRAN, "PARAMETERS", 2))
                m.append(base.GetEntity(constants.NASTRAN, "PARAMETERS", 3))
                morph.MorphParamMerge(m)


            paramsMerge()


    """


def MorphInnerMod(edge: object, morph_entities: int, ddiam: float) -> int:
    """

    Function that modifies the inner cylindrical edges of cylindrical boxes.

    Parameters
    ----------
    edge : object
            The inner cylindrical morphing edges that will be changed.

    morph_entities : int
            1 if you want the action to perform morph at the entities loaded to the box,
            0 otherwise.

    ddiam : float
            Value that will be added to the diameter of the inner edge of the box.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                edge = base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 4)
                morph.MorphInnerMod(edge, 0, 50.0)


    """


def MorphSlFeatureCurve(
    elements: object, curve: object, dist: float, orient: int, copy: int
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for sliding a feature onto a curve, following the curvature of the surface.

    Parameters
    ----------
    elements : object
            A list of connected elements.

    curve : object
            A curve to follow.

    dist : float
            The distance on curve.

    orient : int
            Set to 1 to follow the curve's orientation, or 0 to retain the initial orientation.

    copy : int
            Set to 0 to move the selected feature or define the number (steps) of new features
            that would be generated.

    Returns
    -------
    object
            Returns a list of lists on success:
                The list contains 1 list in case of move, (N+1) lists in case of copy.
                The first element of the list is a list of the initial shells (updated in case of copy).
                The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
            Returns None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                a = base.GetEntity(constants.NASTRAN, "SET", 1)
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 5)
                m = [a]
                feature = morph.MorphSlFeatureCurve(m, curve, 100.0, 1, 4)

                if feature:
                    initial_feature = feature[0]
                    n = len(feature)
                    copy = feature[1:n]

                    print("Initial feature:")
                    for shell in initial_feature:
                        vals = ("Name", "EID")
                        ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                        print("  id:", ret["EID"])
                    if copy:
                        for new_feature in copy:
                            print("New feature:")
                            for shell in new_feature:
                                vals = ("Name", "EID")
                                ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                                print("  id:", ret["EID"])


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def MorphSlFeatureRotate(
    elements: object,
    p1: object,
    angle: float,
    origin_x: float,
    origin_y: float,
    origin_z: float,
    dx: float,
    dy: float,
    dz: float,
    copy: int,
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for rotating a feature onto its surface.

    Parameters
    ----------
    elements : object
            A list of connected elements.

    p1 : object
            A valid coordinate element or None for global.

    angle : float
            The rotational angle.

    origin_x : float
            The x coordinate of the origin point.

    origin_y : float
            The y coordinate of the origin point.

    origin_z : float
            The z coordinate of the origin point.

    dx : float
            The x component of the rotational vector.

    dy : float
            The y component of the rotational vector.

    dz : float
            The z component of the rotational vector.

    copy : int
            Set to 0 to move the selected feature or define the number (steps) of new features
            that would be generated.

    Returns
    -------
    object
            Returns a list of lists on success:
                The list contains 1 list in case of move, (N+1) lists in case of copy.
                The first element of the list is a list of the initial shells (updated in case of copy).
                The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
            Returns None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                a = base.GetEntity(constants.NASTRAN, "SET", 1)
                m = [a]
                feature = morph.MorphSlFeatureRotate(m, None, 72.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 4)

                if feature:
                    initial_feature = feature[0]
                    n = len(feature)
                    copy = feature[1:n]

                    print("Initial feature:")
                    for shell in initial_feature:
                        vals = ("Name", "EID")
                        ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                        print("  id:", ret["EID"])
                    if copy:
                        for new_feature in copy:
                            print("New feature:")
                            for shell in new_feature:
                                vals = ("Name", "EID")
                                ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                                print("  id:", ret["EID"])


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def MorphSlFeatureTransl(
    elements: object,
    p1: object,
    dist: float,
    dx: float,
    dy: float,
    dz: float,
    copy: int,
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for translating a feature onto its surface.

    Parameters
    ----------
    elements : object
            A list of connected elements.

    p1 : object
            A valid coordinate element or None for global.

    dist : float
            The translational distance.

    dx : float
            The x component of the translational vector.

    dy : float
            The y component of the translational vector.

    dz : float
            The z component of the translational vector.

    copy : int
            Set to 0 to move the selected feature or define the number (steps) of new features
            that would be generated

    Returns
    -------
    object
            Returns a list of lists on success:
                The list contains 1 list in case of move, (N+1) lists in case of copy.
                The first element of the list is a list of the initial shells (updated in case of copy).
                The rest elements of the list are also lists generated only in case of copy. Each list contains a new created feature.
            Returns None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                a = base.GetEntity(constants.NASTRAN, "SET", 1)
                m = [a]
                feature = morph.MorphSlFeatureTransl(m, None, 100.0, 1.0, 0.0, 0.0, 0)

                if feature:
                    initial_feature = feature[0]
                    n = len(feature)
                    copy = feature[1:n]

                    print("Initial feature:")
                    for shell in initial_feature:
                        vals = ("Name", "EID")
                        ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                        print("  id:", ret["EID"])
                    if copy:
                        for new_feature in copy:
                            print("New feature:")
                            for shell in new_feature:
                                vals = ("Name", "EID")
                                ret = base.GetEntityCardValues(constants.NASTRAN, shell, vals)
                                print("  id:", ret["EID"])


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def MorphSweepGlide(
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

    Function for creating a morph box through extrusion. Both 'sweep' and 'glide' extrusion types are supported.

    The direction of the extrusion is defined through curves, or points, or a combination of them.
    Curves may form a connected or disconnected path (a path will be automatically created).
    Note that single points are ignored (i.e. if any points are to be used, they should be at least two).

    The user has four options in defining the cross section, one with a box face, one with curves,
    one with curves and points and, finally, one with a predefined shape.
    The box_face option expects a single box face entity (which will be pasted to the new one after creation of the box)
    The curves option expects one or more curves (unconnected ones will be automatically connected to form
    a closed cross section shape). The selected curves should contain at least 4 points, so that they can
    be adopted for the definition of the four box edges.
    The points option should only follow a previous curves-curve_entities pair, and explicitly defines the
    points to be used for the four box edges definition. These points should be part of the curve_entities provided.
    The predefined cross section includes a circular with the required radius, a square with its side
    length, a rectangular with its width and height, and a trapezoidal with its two bases' lenths and
    height. Except for the circular, these cross sections also require a vector defining the 'height'
    direction of the cross section.
    Note that several kind of edges may be used as a curve, including element edges (provided as edge sets),
    CONS, 3D curves and box edges. Similarly, grids, hot points and box edge corner points may be employed
    for any point entities.

    Parameters
    ----------
    extrusion_type : str
            One of "sweep" or "glide", denoting the type of the extrusion.

    guideline_ents : object
            A list of entities defining the direction of the extrusion
            (collection of curves and/or points).

    box_face : object, optional
            A box face entity to be used as a cross section
            (note that new face will be pasted to old).

    curves : object, optional
            A list of curve entities defining the cross section
            (they do not have to form a closed perimeter).

    points : object, optional
            A list of point entities defining the position of the box edges
            (used only in conjunction with 'curves'). Note that points should
            be among the points of the curve_entities provided above.

    section_type : str, optional
            A string specifying the predefined section type ("circular", "square",
            "rectangular", trapezoidal").
            Additional data needed per case:
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
            the x-component of the vector defining the section's height direction
            (does not need to be normalized).

    dy : float, optional
            In case of "square", "rectangular" or "trapezoidal" section_type,
            the y-component of the vector defining the section's height direction
            (does not need to be normalized).

    dz : float, optional
            In case of "square", "rectangular" or "trapezoidal" section_type,
            the z-component of the vector defining the section's height direction
            (does not need to be normalized).

    height : float, optional
            In case of "rectangular" or "trapezoidal" section_type, the height of
            the cross section.

    lower_base : float, optional
            In case of "trapezoidal" section_type, the length of the sections' lower base.

    upper_base : float, optional
            In case of "trapezoidal" section_type, the length of the sections' upper base.

    Returns
    -------
    object
            Returns a list with references to the newly created morph boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                # -Example using a morph face:
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 35))
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 37))
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 43))
                face = base.GetEntity(constants.NASTRAN, "MORPHFACE", 24)
                Box = morph.MorphSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, box_face=face
                )

                # -Example using curves:
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 14))
                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 4))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 15))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 3))
                curves.append(base.GetEntity(constants.NASTRAN, "CONS", 21))
                Box = morph.MorphSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, curves=curves
                )

                # -Example using curves and points:
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 35))
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 37))
                guide.append(base.GetEntity(constants.NASTRAN, "CONS", 43))
                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 41))
                curves.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 42))
                curves.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 43))
                curves.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 44))
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 240))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 248))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 241))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 227))
                Box = morph.MorphSweepGlide(
                    extrusion_type="glide", guideline_ents=guide, points=points, curves=curves
                )

                # -Example where shell edges are used (previously manually added in sets through GUI):
                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                guide = []
                guide = base.CollectEntities(constants.NASTRAN, set, "EDGE")
                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                curves = []
                curves = base.CollectEntities(constants.NASTRAN, set, "EDGE")
                Box = morph.MorphSweepGlide(
                    extrusion_type="sweep", guideline_ents=guide, curves=curves
                )

                # -Example with predefined cross section types:
                guide = []
                guide.append(base.GetEntity(constants.NASTRAN, "CURVE", 10))
                x = 1.0
                y = 0.0
                z = 1.0
                Box1 = morph.MorphSweepGlide(
                    extrusion_type="sweep",
                    guideline_ents=guide,
                    section_type="square",
                    width=40.0,
                    dx=x,
                    dy=y,
                    dz=z,
                )
                Box2 = morph.MorphSweepGlide(
                    extrusion_type="sweep",
                    guideline_ents=guide,
                    section_type="circular",
                    radius=20.0,
                )
                Box3 = morph.MorphSweepGlide(
                    extrusion_type="sweep",
                    guideline_ents=guide,
                    section_type="rectangular",
                    width=20.0,
                    height=10.0,
                    dx=x,
                    dy=y,
                    dz=z,
                )
                Box4 = morph.MorphSweepGlide(
                    extrusion_type="sweep",
                    guideline_ents=guide,
                    section_type="trapezoidal",
                    lower_base=10.0,
                    upper_base=20.0,
                    height=30.0,
                    dx=x,
                    dy=y,
                    dz=z,
                )


    """


def MorphCornerPoints(boxes: object) -> object:
    """

    A function that collects corner points of morphing boxes.
    Note that this function collects the corner points per box, so the common
    points (belonging to common box faces) will be collected multiple times.

    Parameters
    ----------
    boxes : object
            An object or list with the morphing box entities.

    Returns
    -------
    object
            Returns a list of entities on success, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def getCornerPoints():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 1))
                m.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 2))

                corner = morph.MorphCornerPoints(m)
                for ent in corner:
                    print("Corner point = ", ent._id)


    """


def MorphParamCreateTranslate(
    name: str, morph_points: object, coord: object, dx: float, dy: float, dz: float
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterTranslate` instead.


    Function for the creation of a tranlsate morph parameter for morph points.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_points : object
            A list of morph points.

    coord : object
            A coordinate system that the displacement vector will be defined.
            If coord is None, the global coordinate system will be used.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                mopnts = base.CollectEntities(constants.NASTRAN, None, "MORPHPOINT")
                param_id = morph.MorphParamCreateTranslate("Tranlsate", mopnts, None, 1.0, 0.0, 0.0)
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", param_id)

                morph.MorphParam(param, 100.0)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterTranslate instead.",
        DeprecationWarning,
    )


def MorphParamCreateEdgeFit(name: str, morph_edges: list, curves: list) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterEdgeFit` instead.


    Script function for the creation of an edge fit morph parameter for morph edges.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_edges : list
            A list of morph edges.

    curves : list
            A list of curves.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 8))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 18))

                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 8))
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 13))

                param = morph.MorphParamCreateEdgeFit("Edge fit", moedges, curves)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterEdgeFit instead.",
        DeprecationWarning,
    )


def MorphParamCreateExtend(name: str, morph_points: object, morph_edges: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterExtend` instead.


    Script function for the creation of an extend morph parameter for morph boxes.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_points : object
            A list of morph points.

    morph_edges : object
            A list of morph edges.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                mopnts = []
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 5))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 6))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 13))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 14))

                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 2))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 4))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 6))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 8))

                param_id = morph.MorphParamCreateExtend("Extend", mopnts, moedges)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterExtend instead.",
        DeprecationWarning,
    )


def MorphParamCreateOffset(name: str, morph_faces: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterOffset` instead.


    Script function for the creation of an offset morph parameter for morph faces.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_faces : object
            A list of morph faces.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mofaces = base.CollectEntities(constants.NASTRAN, None, "MORPHFACE")
                param_id = morph.MorphParamCreateOffset("Offset", mofaces)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterOffset instead.",
        DeprecationWarning,
    )


def MorphParamCreateRadiusOuter(name: str, morph_faces: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterRadiusOuter` instead.


    Script function for the creation of a radius outer morph parameter for cylindrical morph boxes.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_faces : object
            A list of circular faces of cylindrical morph boxes.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mofaces = []
                mofaces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 1))
                mofaces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 2))

                param_id = morph.MorphParamCreateRadiusOuter("Radius outer", mofaces)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterRadiusOuter instead.",
        DeprecationWarning,
    )


def MorphParamCreateRadiusInner(name: str, concentric_edges: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterRadiusInner` instead.


    Script function for the creation of a radius inner morph parameter for cylindrical morph boxes.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    concentric_edges : object
            A list of concentric edges.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                concentric_edge = []
                concentric_edge.append(base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 14))
                concentric_edge.append(base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 15))

                param_id = morph.MorphParamCreateRadiusInner("Radius inner", concentric_edge)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterRadiusInner instead.",
        DeprecationWarning,
    )


def MorphParamCreateSetsAlign(
    name: str,
    s_elements: object,
    s_aligned: object,
    s_retained: object,
    s_target: object,
    search_distance: float,
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterDFMAlign` instead.


    Script function for the creation of a direct align on sets morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    s_elements : object
            A set of elements that will be morphed by the parameter.

    s_aligned : object
            A set of elements that will be aligned to the s_target set.
            These elements will be used as guide for the displacement of the s_elements.

    s_retained : object
            A set of elements that will retain their position during the morphing action.
            These elements will also affect the deformation of the s_elements.

    s_target : object
            A set of elements that will be used as the target entities of the alignement action.

    search_distance : float
            The search distance of the alignment action.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                included = base.GetEntity(constants.NASTRAN, "SET", 1)
                rigid = base.GetEntity(constants.NASTRAN, "SET", 2)
                retain = base.GetEntity(constants.NASTRAN, "SET", 3)
                target = base.GetEntity(constants.NASTRAN, "SET", 4)
                param_id = morph.MorphParamCreateSetsAlign(
                    "Sets Align", included, rigid, retain, target, 34.0
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterDFMAlign instead.",
        DeprecationWarning,
    )


def MorphParamCreateSetsOffset(
    name: str, s_elements: object, s_offset: object, s_retained: object
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterDFMOffset` instead.


    Script function for the creation of a direct offset on sets morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    s_elements : object
            A set of elements that will be morphed by the parameter.

    s_offset : object
            A set of elements that will be offset.
            These elements will be used as guide for the displacement of the s_elements.

    s_retained : object
            A set of elements that will retain their position during the morphing action.
            These elements will also affect the displacement of the s_elements.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                included = base.GetEntity(constants.NASTRAN, "SET", 1)
                rigid = base.GetEntity(constants.NASTRAN, "SET", 2)
                retain = base.GetEntity(constants.NASTRAN, "SET", 3)
                param_id = morph.MorphParamCreateSetsOffset("Sets offset", included, rigid, retain)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterDFMOffset instead.",
        DeprecationWarning,
    )


def MorphParamCreateSetsTranslate(
    name: str,
    s_elements: object,
    s_translate: object,
    s_retained: object,
    dx: float,
    dy: float,
    dz: float,
) -> int:
    """

    Script function for the creation of a direct translate on sets morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    s_elements : object
            A set of elements that will be morphed by the parameter.

    s_translate : object
            A set of elements that will be translated.
            These elements will be used as guide for the displacement of the s_elements.

    s_retained : object
            A set of elements that will retain their position during the morphing action.
            These elements will also affect the displacement of the s_elements.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                included = base.GetEntity(constants.NASTRAN, "SET", 1)
                rigid = base.GetEntity(constants.NASTRAN, "SET", 2)
                retain = base.GetEntity(constants.NASTRAN, "SET", 3)
                param_id = morph.MorphParamCreateSetsTranslate(
                    "Sets offset", included, rigid, retain, 1, 0, 0
                )


    """


def MorphParamCreateSetsRotate(
    name: str,
    s_elements: object,
    s_rotate: object,
    s_retained: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterDFMRotate` instead.


    Script function for the creation of a direct rotate on sets morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    s_elements : object
            A set of elements that will be morphed by the parameter.

    s_rotate : object
            A set of elements that will be rotated.
            These elements will be used as guide for the displacement of the s_elements.

    s_retained : object
            A set of elements that will retain their position during the morphing action.
            These elements will also affect the displacement of the s_elements.

    x : float
            The x component of the origin's position vector of the rotation axis.
            double x component of the direction vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.
            double y component of the direction vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.
            double z component of the direction vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                included = base.GetEntity(constants.NASTRAN, "SET", 1)
                rigid = base.GetEntity(constants.NASTRAN, "SET", 2)
                retain = base.GetEntity(constants.NASTRAN, "SET", 3)
                param_id = morph.MorphParamCreateSetsRotate(
                    "Sets rotate", included, rigid, retain, 100, -200, 100, 0, 0, 1
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterDFMRotate instead.",
        DeprecationWarning,
    )


def MorphParamCreateAngle(name: str, morph_edges: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterAngle` instead.


    Function for the creation of an angle morph parameter for morph edges.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_edges : object
            A list of morph edges. The list must have even size.
            Morph edges in the odd indicies of the list will retain their position
            while those in even indicies will rotate.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 9))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 4))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 10))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 2))
                param = morph.MorphParamCreateAngle("Angle", moedges)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterAngle instead.",
        DeprecationWarning,
    )


def MorphParamCreateRotate(
    name: str,
    morph_points: object,
    coord: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterRotate` instead.


    Script function for the creation of a rotate morph parameter for morph points.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_points : object
            A list of morph points.

    coord : object
            A coordinate system that the rotation axis will be defined.
            If coord is None the global coordinate system will be used.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                morphes = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX")
                mopnts = morph.MorphCornerPoints(morphes)
                param_id = morph.MorphParamCreateRotate("Rotate", mopnts, None, 0, 0, 0, 0, 0, 1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterRotate instead.",
        DeprecationWarning,
    )


def MorphParamCreateDeformation(name: str, affected: str) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterDeformation` instead.


    Script function for the creation of a deformation morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    affected : str
            Indicates which entities will be recorded by the deformation parameter.
            Possible values are 'All' and 'Moved'.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.MorphParamCreateDeformation("Deformation", "Moved")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterDeformation instead.",
        DeprecationWarning,
    )


def MorphParamCreateScale(
    name: str, morph_points: object, x: float, y: float, z: float
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterScale` instead.


    Script function for the creation of a scale morph parameter for morph points.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_points : object
            A list of morph points.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                morphes = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX")
                mopnts = morph.MorphCornerPoints(morphes)
                param = morph.MorphParamCreateScale("Scale", mopnts, 0, 0, 0)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterScale instead.",
        DeprecationWarning,
    )


def MorphParamCreateUserTangent(name: str, morph_tang: object) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterUserTangent` instead.


    Script function for the creation of a user tanget morph parameter for morph edges.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_tang : object
            A list of morph tangents.

    Returns
    -------
    int
            Returns the ID of the created parameter or 0 in case of failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mtang = base.CollectEntities(constants.NASTRAN, None, "MORPHTANG")
                param = morph.MorphParamCreateUserTangent("Tangent", mtang)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterUserTangent instead.",
        DeprecationWarning,
    )


def MorphParamCreateDFMFitEdges(
    name: str, edge_fit_args: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Function for the creation of a DFM edge fit morph parameter.

    Parameters
    ----------
    name : str
            Tthe desired name for the new parameter.

    edge_fit_args : object
            A list of objects created by MorphCreateDFMFitEdgesArgs

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            An option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    See Also
    --------
    MorphCreateDFMFitEdgesArgs, morph.DFMAlign, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 2)]
                source_2 = [base.GetEntity(constants.NASTRAN, "SET", 3)]
                target_2 = [base.GetEntity(constants.NASTRAN, "SET", 4)]
                source_3 = [base.GetEntity(constants.NASTRAN, "SET", 5)]
                target_3 = [base.GetEntity(constants.NASTRAN, "SET", 6)]
                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                edge_fit_args = []
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_1, target_1))
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_2, target_2))
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_3, target_3))

                param_1 = morph.MorphParamCreateDFMFitEdges(
                    "Edge fit", edge_fit_args, elements, bounds, False
                )


    """


def MorphCreateDFMFitEdgesArgs(source: object, target: object) -> object:
    """

    Script function for the creation of an object that will be used by MorphParamCreateDFMFitEdges script function.
    This is an auxiliary function.

    Parameters
    ----------
    source : object
            A list of entities that will be used as source of DFM edge fit parameter.

    target : object
            A list of entities that will be used as target of DFM edge fit parameter.

    Returns
    -------
    object
            Returns the created object or None in case of failure.

    See Also
    --------
    MorphParamCreateDFMFitEdges

    Examples
    --------
    ::

            from ansa import base
            from ansa import morph


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 2)]
                source_2 = [base.GetEntity(constants.NASTRAN, "SET", 3)]
                target_2 = [base.GetEntity(constants.NASTRAN, "SET", 4)]
                source_3 = [base.GetEntity(constants.NASTRAN, "SET", 5)]
                target_3 = [base.GetEntity(constants.NASTRAN, "SET", 6)]
                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                edge_fit_args = []
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_1, target_1))
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_2, target_2))
                edge_fit_args.append(morph.MorphCreateDFMFitEdgesArgs(source_3, target_3))

                param_1 = morph.MorphParamCreateDFMFitEdges(
                    "Edge fit", edge_fit_args, elements, bounds, False
                )


    """


def MorphParamCreateDFMFitSurfaces(
    name: str,
    surafce_fit_args: object,
    morphed: object,
    bounds: object,
    autobounds: bool,
) -> int:
    """

    Script function for the creation of a DFM surface fit morph parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter.

    surafce_fit_args : object
            A list of objects created by MorphCreateDFMFitSurfsArgs.

    morphed : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            Option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the created parameter, or 0 in case of failure.

    See Also
    --------
    MorphCreateDFMFitSurfsArgs, morph.DFMFitSurfaces, morph.DFM

    Examples
    --------
    ::

            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 9)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 10)]
                source_2 = [base.GetEntity(constants.NASTRAN, "FACE", 6)]
                target_2 = [base.GetEntity(constants.NASTRAN, "FACE", 8)]

                src_pnts1 = []
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 4))

                trg_pnts1 = []
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 5))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 6))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 8))

                src_pnts2 = []
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 9))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 10))

                trg_pnts2 = []
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 8))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 12))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 13))

                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                surf_fit_args = []
                surf_fit_args.append(
                    morph.MorphCreateDFMFitSurfsArgs(source_1, target_1, src_pnts1, trg_pnts1)
                )
                surf_fit_args.append(
                    morph.MorphCreateDFMFitSurfsArgs(source_2, target_2, src_pnts2, trg_pnts2)
                )

                param_1 = morph.MorphParamCreateDFMFitSurfaces(
                    "Surface fit1", surf_fit_args, elements, bounds, False
                )


    """


def MorphCreateDFMFitSurfsArgs(
    source_area: object,
    target_area: object,
    source_points: object,
    target_points: object,
) -> object:
    """

    Script function for the creation of an object that will be used by MorphParamCreateDFMFitSurfaces script function.
    This is an auxiliary function.

    Parameters
    ----------
    source_area : object
            A list of entities that will be used as the source area.

    target_area : object
            A list of entities that will be used as the target area.

    source_points : object
            A list of perimetric points of the source area.

    target_points : object
            A list of perimetric points of the target area.

    Returns
    -------
    object
            Returns the created object, or None in case of failure.

    See Also
    --------
    MorphParamCreateDFMFitSurfaces

    Examples
    --------
    ::

            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 9)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 10)]
                source_2 = [base.GetEntity(constants.NASTRAN, "FACE", 6)]
                target_2 = [base.GetEntity(constants.NASTRAN, "FACE", 8)]

                src_pnts1 = []
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 4))

                trg_pnts1 = []
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 5))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 6))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 8))

                src_pnts2 = []
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 9))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 10))

                trg_pnts2 = []
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 8))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 12))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 13))

                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                surf_fit_args = []
                surf_fit_args.append(
                    morph.MorphCreateDFMFitSurfsArgs(source_1, target_1, src_pnts1, trg_pnts1)
                )
                surf_fit_args.append(
                    morph.MorphCreateDFMFitSurfsArgs(source_2, target_2, src_pnts2, trg_pnts2)
                )

                param_1 = morph.MorphParamCreateDFMFitSurfaces(
                    "Surface fit1", surf_fit_args, elements, bounds, False
                )


    """


def MorphParamCreateDFMTranslate(
    name: str, translate_arg: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Script function for the creation of a dfm translate parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter.

    translate_arg : object
            A list objects created by MorphCreateDFMTranslateArgs.

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            Option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the created parameter, or 0 in case of failure.

    See Also
    --------
    MorphCreateDFMTranslateArgs, morph.DFMTranslate, morph.DFM

    Examples
    --------
    ::

            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set2 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMTranslateArgs(set1, 0, -1, 0))
                args.append(morph.MorphCreateDFMTranslateArgs(set2, 0, 1, 0))
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                param2 = morph.MorphParamCreateDFMTranslate(
                    "Traslate 2", args, morphed, bounds, False
                )


    """


def MorphCreateDFMTranslateArgs(
    translated: object, dx: float, dy: float, dz: float
) -> object:
    """

    Script function for the creation of an object that will be used by MorphParamCreateDFMTranslate script function.
    This is an auxiliary function

    Parameters
    ----------
    translated : object
            A list of entities that will be translated.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    Returns
    -------
    object
            Returns the created object, or None in case of failure.

    See Also
    --------
    MorphParamCreateDFMTranslate

    Examples
    --------
    ::

            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set2 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMTranslateArgs(set1, 0, -1, 0))
                args.append(morph.MorphCreateDFMTranslateArgs(set2, 0, 1, 0))
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                param2 = morph.MorphParamCreateDFMTranslate(
                    "Traslate 2", args, morphed, bounds, False
                )


    """


def MorphParamCreateDFMRotate(
    name: str, rotate_args: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Script function for the creation of a dfm rotate parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter.

    rotate_args : object
            A list of objects created by MorphCreateDFMRotateArgs.

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            Option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the created parameter, or 0 in case of failure.

    See Also
    --------
    MorphCreateDFMRotateArgs, morph.DFMRotate, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMRotateArgs(set3, -100, -2, 169, 1, 0, 0))
                args.append(morph.MorphCreateDFMRotateArgs(set4, -100, -2, 169, -1, 0, 0))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]

                param_id = morph.MorphParamCreateDFMRotate(
                    "Rotate Combined", args, morphed, bounds, False
                )


    """


def MorphCreateDFMRotateArgs(
    rotated: object, x: float, y: float, z: float, dx: float, dy: float, dz: float
) -> object:
    """

    Script function for the creation of an object that will be used by MorphParamCreateDFMRotate script function.
    This is an auxiliary function

    Parameters
    ----------
    rotated : object
            A list of entities that will be rotated.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    Returns
    -------
    object
            Returns the created object, or None in case of failure.

    See Also
    --------
    MorphParamCreateDFMRotate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMRotateArgs(set3, -100, -2, 169, 1, 0, 0))
                args.append(morph.MorphCreateDFMRotateArgs(set4, -100, -2, 169, -1, 0, 0))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]

                param_id = morph.MorphParamCreateDFMRotate(
                    "Rotate Combined", args, morphed, bounds, False
                )


    """


def MorphParamCreateDFMScale(
    name: str, scale_args: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Script function for the creation of a dfm scale parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter.

    scale_args : object
            A list of objects created by MorphCreateDFMScaleArgs.

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            Option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the created parameter, or 0 in case of failure.

    See Also
    --------
    MorphCreateDFMScaleArgs, morph.DFMScale, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMScaleArgs(set3, -100, -100, 169))
                args.append(morph.MorphCreateDFMScaleArgs(set4, -100, 100, 169))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.MorphParamCreateDFMScale(
                    "Scale Combined", args, morphed, bounds, False
                )


    """


def MorphCreateDFMScaleArgs(scaled: object, x: float, y: float, z: float) -> object:
    """

    Script function for the creation of an object that will be used by MorphParamCreateDFMScale script function.
    This is an auxiliary function.

    Parameters
    ----------
    scaled : object
            A list of entities that will be scaled.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    Returns
    -------
    object
            Returns the created object, or None in case of failure.

    See Also
    --------
    MorphParamCreateDFMScale

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.MorphCreateDFMScaleArgs(set3, -100, -100, 169))
                args.append(morph.MorphCreateDFMScaleArgs(set4, -100, 100, 169))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.MorphParamCreateDFMScale(
                    "Scale Combined", args, morphed, bounds, False
                )


    """


def MorphParamCreateDFMTransform(
    name: str,
    transformed_args: object,
    entities: object,
    bounds: object,
    autobounds: bool,
) -> int:
    """

    Script function for the creation of a dfm transform parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter.

    transformed_args : object
            A list of objects created by MorphCreateDFMTransformArgs.

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            An option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    See Also
    --------
    MorphCreateDFMTransformArgs, morph.DFMTransform, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                coord3 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 1)
                coord4 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 2)
                coord5 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 4)
                coord6 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 3)

                args = []
                args.append(morph.MorphCreateDFMTransformArgs(set4, coord3, coord4))
                args.append(morph.MorphCreateDFMTransformArgs(set3, coord5, coord6))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.MorphParamCreateDFMTransform(
                    "Transform Combined", args, morphed, bounds, False
                )


    """


def MorphCreateDFMTransformArgs(
    transformed: object, src_coord: object, trg_coord: object
) -> object:
    """

    Function for the creation of an object that will be used by the MorphParamCreateDFMTransform function.
    This is an auxiliary function.

    Parameters
    ----------
    transformed : object
            A list of entities that will be transformed.

    src_coord : object
            An ANSA coordinate object that will be used as the source coordinaty system.

    trg_coord : object
            An ANSA coordinate object that will be used as the target coordinaty system.

    Returns
    -------
    object
            Returns a reference to the newly created object, or None on failure.

    See Also
    --------
    MorphParamCreateDFMTransform

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                coord3 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 1)
                coord4 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 2)
                coord5 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 4)
                coord6 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 3)

                args = []
                args.append(morph.MorphCreateDFMTransformArgs(set4, coord3, coord4))
                args.append(morph.MorphCreateDFMTransformArgs(set3, coord5, coord6))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.MorphParamCreateDFMTransform(
                    "Transform Combined", args, morphed, bounds, False
                )


    """


def MorphParamCreateDFMOffset(
    name: str, offset: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Script function for the creation of a DFM offset morph parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    offset : object
            A list of entities that will offset.

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            An option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    See Also
    --------
    morph.DFMOffset, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                set2 = base.GetEntity(constants.NASTRAN, "SET", 11)

                offset = base.CollectEntities(constants.NASTRAN, (set1, set2), "FACE")
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]

                param_id1 = morph.MorphParamCreateDFMOffset("Offset", offset, morphed, None, True)


    """


def MorphParamCreateSlideFeatureTranslate(
    name: str, elements: object, coord: object, dx: float, dy: float, dz: float
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterSlideFeatureTranslate` instead.


    Script function for the creation of a slide feature translate parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    elements : object
            A list of elements that describes the feature.

    coord : object
            A coordinate system that the displacement vector will be defined.
            If coord is None the global coordinate system will be used.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                feature = base.CollectEntities(constants.NASTRAN, set, "SHELL")
                param = morph.MorphParamCreateSlideFeatureTranslate(
                    "Feature Translate", feature, None, -1, 0, 0
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterSlideFeatureTranslate instead.",
        DeprecationWarning,
    )


def MorphParamCreateSlideFeatureRotate(
    name: str,
    elements: object,
    coord: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterSlideFeatureRotate` instead.


    Script function for the creation of a slide feature rotate parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    elements : object
            A list of elements that describes the feature.

    coord : object
            A coordinate system that the displacement vector will be defined.
            If coord is None the global coordinate system will be used.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                id = morph.MorphParamCreateSlideFeatureRotate(
                    "Feature Rotate", feature, None, 1439, -668, 12, 0, 0, 1
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterSlideFeatureRotate instead.",
        DeprecationWarning,
    )


def MorphParamCreateSlideFeatureScale(
    name: str, elements: object, x: float, y: float, z: float
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterSlideFeatureScale` instead.


    Script function for the creation of a slide feature scale parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    elements : object
            A list of elements that describes the feature.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                id = morph.MorphParamCreateSlideFeatureScale(
                    "Feature Scale", feature, 1439, -668, 12
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterSlideFeatureScale instead.",
        DeprecationWarning,
    )


def MorphParamCreateSlideFeatureCurve(
    name: str, elements: object, curve: object, follow_orientation: bool
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterSlideFeatureCurve` instead.


    Script function for the creation of a slide feature on curve parameter.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    elements : object
            A list of elements that describes the feature.

    curve : object
            An ANSA curve on which the feature will slide on.

    follow_orientation : bool
            A flag to determine if the feature will follow the curve's orientation.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                id = morph.MorphParamCreateSlideFeatureCurve("Feature Curve", feature, curve, True)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterSlideFeatureCurve instead.",
        DeprecationWarning,
    )


def MorphCreateDFMAlignArgs(
    entities: object,
    target_entities: object,
    target_axis: object,
    target_plane: object,
    include_thickness: bool,
    max_distance: float,
    user_direction: object,
) -> object:
    """

    Function for the creation of an object that will be used by the MorphParamCreateDFMAlign function.
    This is an auxiliary function.

    Parameters
    ----------
    entities : object
            A list of entities that will be aligned.

    target_entities : object, optional
            A list of entities that will be used as the target surface of alignment.

    target_axis : object, optional
            A list of doubles that describes an axis that will be used as the target axis.
            The format of this list is (x, y, z, dx, dy, dz) where x, y and z
            are the components of the origins position vector and dx, dy and dz
            are the components of the direction vector of the axis.

    target_plane : object, optional
            A list of doubles that describes a plane that will be used as the target plane.
            The format of this list is (x, y, z, dx, dy, dz) where x, y and z
            are the components of the origins position vector of the plane
            and dx, dy and dz are the components of the direction of the normal vector
            of the plane.

    include_thickness : bool, optional
            An option to determine if the thickness of the aligned and target elements
            will be included in the calculation.
            Default value is False.

    max_distance : float, optional
            Determines the maximun radial search distance where the
            aligned elements will seek
            for target entities.
            Default value is infinite.

    user_direction : object, optional
            A list of doubles that describes a user's predefined alignment direction.
            The format of this list is (dx, dy, dz) where dx, dy and dz are the
            components of the direction vector.

    Returns
    -------
    object
            Returns a reference to the newly created object, or None on failure.

    See Also
    --------
    MorphParamCreateDFMAlign

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                setsrc1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                setsrc2 = base.GetEntity(constants.NASTRAN, "SET", 11)
                settrg = [base.GetEntity(constants.NASTRAN, "SET", 13)]
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                args1 = [
                    morph.MorphCreateDFMAlignArgs(
                        entities=(setsrc1, setsrc2), target_entities=settrg
                    )
                ]

                param1 = morph.MorphParamCreateDFMAlign(
                    "Align to entities", args1, morphed, None, True
                )


            def main():
                set14 = base.GetEntity(constants.NASTRAN, "SET", 14)
                set15 = base.GetEntity(constants.NASTRAN, "SET", 15)

                args2 = []
                args2.append(
                    morph.MorphCreateDFMAlignArgs(
                        entities=(set14), target_axis=(-100, 300, 0, 0, 0, 1)
                    )
                )
                args2.append(
                    morph.MorphCreateDFMAlignArgs(
                        entities=(set15), target_plane=(-100, -300, 0, 0, -1, 0)
                    )
                )

                morphed = []
                morphed, append(base.GetEntity(constants.NASTRAN, "SET", 7))
                morphed.append(base.GetEntity(constants.NASTRAN, "FACE", 10))
                param2 = morph.MorphParamCreateDFMAlign(
                    "Align combined axis-plane", args2, morphed, None, True
                )


    """


def MorphParamCreateDFMAlign(
    name: str, align_args: object, entities: object, bounds: object, autobounds: bool
) -> int:
    """

    Function for the creation of a dfm align parameter.

    Parameters
    ----------
    name : str
            The desired name of the parameter

    align_args : object
            A list of objects returned by MorphCreateDFMAlignArgs

    entities : object
            A list of entities that will be morphed.

    bounds : object
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.

    autobounds : bool
            An option to enable the automatic bound determination.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    See Also
    --------
    MorphCreateDFMAlignArgs, morph.DFMAlign, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                setsrc1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                setsrc2 = base.GetEntity(constants.NASTRAN, "SET", 11)
                settrg = [base.GetEntity(constants.NASTRAN, "SET", 13)]
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                args1 = [
                    morph.MorphCreateDFMAlignArgs(
                        entities=(setsrc1, setsrc2), target_entities=settrg
                    )
                ]

                param1 = morph.MorphParamCreateDFMAlign(
                    "Align to entities", args1, morphed, None, True
                )


            def main():
                set14 = base.GetEntity(constants.NASTRAN, "SET", 14)
                set15 = base.GetEntity(constants.NASTRAN, "SET", 15)

                args2 = []
                args2.append(
                    morph.MorphCreateDFMAlignArgs(
                        entities=(set14), target_axis=(-100, 300, 0, 0, 0, 1)
                    )
                )
                args2.append(
                    morph.MorphCreateDFMAlignArgs(
                        entities=(set15), target_plane=(-100, -300, 0, 0, -1, 0)
                    )
                )

                morphed = []
                morphed, append(base.GetEntity(constants.NASTRAN, "SET", 7))
                morphed.append(base.GetEntity(constants.NASTRAN, "FACE", 10))
                param2 = morph.MorphParamCreateDFMAlign(
                    "Align combined axis-plane", args2, morphed, None, True
                )


    """


def MorphParamCreateTailoredBlank(
    entities: object,
    properties: object,
    lengths: object,
    origin: object,
    normal: object,
    trajectory: object,
    movement: int,
    cut_mesh: bool,
    reconstruct: bool,
    zones: int,
    name: str,
) -> int:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewParameterTailoredBlank` instead.


    Script function for the creation of a 'Tailored Blank' parameter.

    Parameters
    ----------
    entities : object
            A list of shells.

    properties : object
            A list of properties that will be applied on elements.

    lengths : object
            A list of doubles that specifies the application length for each property.

    origin : object
            A list of three doubles that specifies the position vector of the
            origin of the seperation plane.

    normal : object
            A list of three doubles that specifies the direction vector of the
            normal of the seperation plane.

    trajectory : object, optional
            A list of entities that will be used as the trajectory on which
            seperation plane will move.

    movement : int, optional
            A variable that controls the type of movement of the seperation plane.
            Possible values are:
            -0 for "Follow trajectory"
            -1 for "Sweep on trajectory"
            -2 for "Glide on trajectory"
            (Default: 0)

    cut_mesh : bool, optional
            An option that controls if plane cut will take place at each property change.
            (Default: False)

    reconstruct : bool, optional
            An option to determine if reconstruction of the affected elements
            will take place after the application of cut.
            This option is meaningfull only if "cut_mesh" is set to True.
            (Default: False)

    zones : int, optional
            An option to determine the number of zones that will be reconstructed
            around cut area.
            This option is meaningfull only if "reconstruct" is set to True.
            (Default: 0)

    name : str, optional
            The desired name for the created parameter.
            If not provided ANSA will automaticaly decide a name for the newly
            created parameter.

    Returns
    -------
    int
            Returns the ID of the newly created parameter or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)

                props = []
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 3))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 4))

                lens = []
                lens.append(1e308)
                lens.append(-1e308)
                lens.append(200)
                lens.append(-300)

                origin = (1467, -759, 597)
                normal = (0, 0, 1)

                trajectory = base.GetEntity(constants.NASTRAN, "SET", 2)
                name = "Tailored blank"

                param_id = morph.MorphParamCreateTailoredBlank(
                    entities, props, lens, origin, normal, trajectory, 2, True, True, 10, name
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewParameterTailoredBlank instead.",
        DeprecationWarning,
    )


def MorphPointProjectToContainer(
    box_points: object,
    target_entities: object,
    offset: float,
    coordinate_system: object,
    freeze_x_axis: bool,
    freeze_y_axis: bool,
    freeze_z_axis: bool,
) -> int:
    """

    Function to project control points on target feature lines or on target surface
    (target surface can be defined by shells and geometrical faces).

    Parameters
    ----------
    box_points : object
            A list of box points or a box point. The user can also define the box edges and
            the function will automatically get the correspondent control points.

    target_entities : object
            A list of entities, parts, properties, materials or sets,
            to define the target entities (feature lines or surfaces).

    offset : float, optional
            The distance to move the control points from their projection on target entities.

    coordinate_system : object, optional
            The coordinate system to work with (it is used in combination
            with the freeze options).

    freeze_x_axis : bool, optional
            True or False, to define if x axis movement is not allowed.

    freeze_y_axis : bool, optional
            True or False, to define if y axis movement is not allowed.

    freeze_z_axis : bool, optional
            True or False, to define if z axis movement is not allowed.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import base
            from ansa import constants


            def main():
                # gather box points, project them to a curve and freeze movement
                # on y axis of the global coordinate system
                box_points = []
                box_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 25))
                box_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 26))
                box_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 27))

                target_curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                morph.MorphPointProjectToContainer(box_points, target_curve, freeze_y_axis=True)

                # gather points, project them to all faces of the database by using a specific
                # coordinate system (id = 1), freezing movement on z axis of this coordinate system
                # and using offset distance equal to 10
                box_points1 = []
                box_points1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 28))
                box_points1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 29))

                surface_ents = base.CollectEntities(constants.NASTRAN, None, "FACE")
                coord = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 1)

                morph.MorphPointProjectToContainer(
                    box_points1,
                    surface_ents,
                    offset=10,
                    coordinate_system=coord,
                    freeze_z_axis=True,
                )


    """


def xyzIsInsideBox(x: float, y: float, z: float) -> object:
    """

    This function takes as arguments the coordinates of a point and checks whether this
    point is inside a box (morph, sizebox, hexablock and d-boxes),
    and returns a list of the boxes.

    Parameters
    ----------
    x : float
            The x coordinate of the point.

    y : float
            The y coordinate of the point.

    z : float
            The z coordinate of the point.

    Returns
    -------
    object
            Returns a list with the boxes or false for none.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                x = 1154.9853988457699
                y = 81.86427424695316
                z = 625.9693527866185
                morph.xyzIsInsideBox(x, y, z)


    """


def CreateStamp(
    stamp_type: str,
    stamp_entities: object,
    stamp_parameters: object,
    direction_points: object,
    invert_direction: bool,
    auto_reconstruct: object,
    add_to_set: int,
    save_morph_parameter: bool,
    return_characteristics: bool,
    top_is_width: bool,
    detached_feature: object,
    exclude_feature_recon: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`Create` instead.


    Function for the creation of circular, rectangular or free form stamps.

    Parameters
    ----------
    stamp_type : str
            The type of the stamp, values can be "Circular", "Rectangular rounded" or "Surface".

    stamp_entities : object
            A list of the entities where the stamp will be created.

    stamp_parameters : object
            A list of the stamp parameters:
            "Circular" = [Diameter, Height, Angle_A, Radius_r1, Radius_r2]
            "Rectangular rounded" = [Width_w1, Width_w2, Corner_R, Height, Angle_A, Radius_r1, Radius_r2]
            "Surface" = [Height, Angle_A, Radius_r1, Radius_r2]

    direction_points : object, optional
            A list of 2 points, to define local bead direction, when Rectangular round feature is created

    invert_direction : bool, optional
            Boolean to invert direction of the feature

    auto_reconstruct : object, optional
            Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

    add_to_set : int, optional
            Integer id of the Set, to add the create feature shells

    save_morph_parameter : bool, optional
            Boolean to save a morphing parameter on the create feature

    return_characteristics : bool, optional
            Boolean value to control the return of the function. Set it to True
            to return a Dictionary with key and value:

            { 'ALL': [ shells ] , 'TOP_FILLET': [ shells ], 'BOTTOM_FILLET': [ shells ], 'TOP': [ shells ], 'BODY': [ shells ]}

    top_is_width : bool, optional
            Set to True for parameter ANGLE_A to be width and not an angle, default False. Applicable only in Circular

    detached_feature : object, optional
            A list with 2 values (flanges with and offset distance) to create a detached feature.

    exclude_feature_recon : bool, optional
            Keep feature out from reconstruct.

    Returns
    -------
    object
            Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

    See Also
    --------
    CreateBead, CreateFlangedOpening, CreateOpening, CreateRib

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def createCircStamp():
                params = []
                params.append(10.0)
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)
                params.append(2.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                shells = morph.CreateStamp("Circular", ents, params)
                morph.MorphOrtho(loaded_elements=shells)


            def createRectStamp():
                params = []
                params.append(20.0)
                params.append(30.0)
                params.append(6.0)
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)
                params.append(2.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                arg4 = []
                arg4.append(base.GetEntity(ansa.base.CurrentDeck(), "POINT", 18))
                arg4.append(base.GetEntity(ansa.base.CurrentDeck(), "POINT", 19))
                arg6 = {}
                arg6["Reconstruct"] = 3
                shells = morph.CreateStamp(
                    "Rectangular rounded",
                    ents,
                    params,
                    direction_points=arg4,
                    invert_direction=True,
                    auto_reconstruct=arg6,
                    save_morph_parameter=True,
                )
                morph.MorphOrtho(loaded_elements=shells)


            def createSurfStamp():
                params = []
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)
                params.append(2.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7116))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7374))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7269))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7036))
                shells = morph.CreateStamp("Surface", ents, params)
                morph.MorphOrtho(loaded_elements=shells)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: Create instead.",
        DeprecationWarning,
    )


def CreateBead(
    bead_type: str,
    bead_entities: object,
    bead_parameters: object,
    invert_direction: bool,
    auto_reconstruct: object,
    add_to_set: int,
    save_morph_parameter: bool,
    direction_points: object,
    return_characteristics: bool,
    top_is_width: bool,
    detached_feature: object,
    exclude_feature_recon: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`Create` instead.


    A function for the creation of beads (straight or curved).

    Parameters
    ----------
    bead_type : str
            The type of the bead. Accepted values: "Straight", "Straight rounded",
            "Curved" or "Curved rounded".

    bead_entities : object
            A list of entities, where the bead will be created.

    bead_parameters : object
            A list of the bead parameters: [Width_w1, Height, Angle_A, Radius_r1, Radius_r2].
            Radius_r2 is optional and if given it will create a flat bottom bead,
            otherwise a rounded bottom one.

    invert_direction : bool, optional
            Boolean to invert direction of the bead

    auto_reconstruct : object, optional
            Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created bead.

    add_to_set : int, optional
            Integer id of the Set, to add the create bead shells

    save_morph_parameter : bool, optional
            Boolean to save a morphing parameter on the create bead

    direction_points : object, optional
            A list of 2 points, to define local bead direction, when X, T or L type  feature is created

    return_characteristics : bool, optional
            Boolean value to control the return of the function. Set it to True
            to return a Dictionary with key and value:

            { 'ALL': [ shells ] , 'TOP_FILLET': [ shells ], 'BOTTOM_FILLET': [ shells ], 'TOP': [ shells ], 'BODY': [ shells ], 'JUNCTION': [ shells ], 'MEMBER_1': [ shells ] ... }

    top_is_width : bool, optional
            Set to True for parameter ANGLE_A to be width and not an angle, default False.

    detached_feature : object, optional
            A list with 2 values (flanges with and offset distance) to create a detached feature.

    exclude_feature_recon : bool, optional
            Keep feature out from reconstruct.

    Returns
    -------
    object
            Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

    See Also
    --------
    CreateStamp, CreateFlangedOpening, CreateOpening, CreateRib

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def createBeads():
                params = []
                params.append(10.0)
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 24))
                shells = morph.CreateBead("Straight", ents, params, add_to_set=1)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 25))
                arg5 = {}
                arg5["Reconstruct"] = 1
                shells = morph.CreateBead(
                    "Straight rounded",
                    ents,
                    params,
                    invert_direction=True,
                    auto_reconstruct=arg5,
                    add_to_set=1,
                )

                params.append(2.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 22))
                shells = morph.CreateBead("Curved", ents, params, save_morph_parameter=True)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 23))
                shells = morph.CreateBead("Curved rounded", ents, params)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: Create instead.",
        DeprecationWarning,
    )


def CreateFlangedOpening(
    open_type: str,
    open_entities: object,
    open_parameters: object,
    direction_points: object,
    invert_direction: bool,
    auto_reconstruct: object,
    add_to_set: int,
    save_morph_parameter: bool,
    return_characteristics: bool,
    top_is_width: bool,
    detached_feature: object,
    exclude_feature_recon: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`Create` instead.


    Function for the creation of flanged openings.

    Parameters
    ----------
    open_type : str
            The type of the opening. Values can be "Circular", "Rectangular rounded",
            "Surface", "Straight", "Straight rounded", "Curved" or "Curved rounded".

    open_entities : object
            A list of entities where the opening will be created.

    open_parameters : object
            A list of the opening parameters:

            "Circular": [Diameter, Height, Angle_A, Radius_r1]
            "Rectangular rounded": [Width_w1, Width_w2, Corner_R, Height, Angle_A, Radius_r1]
            "Surface": [Height, Angle_A, Radius_r1]
            "Straight": [Width_w1, Height, Angle_A, Radius_r1]
            "Straight rounded": [Width_w1, Height, Angle_A, Radius_r1]
            "Curved": [Width_w1, Height, Angle_A, Radius_r1]
            "Curved rounded": [Width_w1, Height, Angle_A, Radius_r1]

    direction_points : object, optional
            A list of 2 points, to define local bead direction, when Rectangular round feature is created

    invert_direction : bool, optional
            Boolean to invert direction of the feature

    auto_reconstruct : object, optional
            Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

    add_to_set : int, optional
            Integer id of the Set, to add the create feature shells

    save_morph_parameter : bool, optional
            Boolean to save a morphing parameter on the create feature

    return_characteristics : bool, optional
            Boolean value to control the return of the function. Set it to True
            to return a Dictionary with key and value:

            { 'ALL': [ shells ] , 'BOTTOM_FILLET': [ shells ], 'BODY': [ shells ]}

    top_is_width : bool, optional
            Set to True for parameter ANGLE_A to be width and not an angle, default False.

    detached_feature : object, optional
            A list with 2 values (flanges with and offset distance) to create a detached feature.

    exclude_feature_recon : bool, optional
            Keep feature out from reconstruct.

    Returns
    -------
    object
            Returns the shells of the created stamp or 0 on error, use "return_characteristics" to return a dictionary

    See Also
    --------
    CreateStamp, CreateBead, CreateOpening, CreateRib

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def createflanged():
                params = []
                params.append(10.0)
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 24))
                shells = morph.CreateFlangedOpening(
                    "Straight", ents, params, invert_direction=True, add_to_set=2
                )

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 25))
                shells = morph.CreateFlangedOpening("Straight rounded", ents, params)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 22))
                arg4 = {}
                arg4["Reconstruct"] = 3
                shells = morph.CreateFlangedOpening(
                    "Curved", ents, params, auto_reconstruct=arg4, save_morph_parameter=True
                )

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 23))
                shells = morph.CreateFlangedOpening("Curved rounded", ents, params)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                shells = morph.CreateFlangedOpening("Circular", ents, params)

                # Type: "Rectangular rounded"
                params = []
                params.append(20.0)
                params.append(30.0)
                params.append(6.0)
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                arg4 = []
                arg4.append(base.GetEntity(ansa.base.CurrentDeck(), "POINT", 9))
                arg4.append(base.GetEntity(ansa.base.CurrentDeck(), "POINT", 10))
                shells = morph.CreateFlangedOpening(
                    "Rectangular rounded",
                    ents,
                    params,
                    direction_points=arg4,
                    invert_direction=True,
                )

                # Type: "Surface"
                params = []
                params.append(8.0)
                params.append(75.0)
                params.append(3.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7116))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7374))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7269))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7036))
                shells = morph.CreateFlangedOpening("Surface", ents, params)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: Create instead.",
        DeprecationWarning,
    )


def CreateOpening(
    open_type: object,
    open_entities: object,
    open_parameters: object,
    direction_points: object,
    invert_direction: bool,
    auto_reconstruct: object,
    add_to_set: int,
    save_morph_parameter: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`Create` instead.


    Function for the creation of openings.

    Parameters
    ----------
    open_type : object
            The type of the opening, values can be "Circular", "Rectangular rounded",
            "Surface", "Straight", "Straight rounded", "Curved" or "Curved rounded".

    open_entities : object
            A list of entities where the opening will be created.

    open_parameters : object
            A list of the opening parameters:
            -"Circular": [Diameter]
            -"Rectangular rounded": [Width_w1, Width_w2, Corner_R]
            -"Surface": []
            -"Straight"
            -"Straight rounded"
            -"Curved"
            -"Curved rounded": [Width_w1]

    direction_points : object, optional
            A list of 2 points, to define local bead direction, when Rectangular round feature is created

    invert_direction : bool, optional
            Boolean to invert direction of the feature

    auto_reconstruct : object, optional
            Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

    add_to_set : int, optional
            Integer id of the Set, to add the create feature shells

    save_morph_parameter : bool, optional
            Boolean to save a morphing parameter on the create feature

    Returns
    -------
    object
            Returns the nodes of the new opening or 0 on error.

    See Also
    --------
    CreateStamp, CreateBead, CreateFlangedOpening, CreateRib

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def createOpening():
                params = []
                params.append(10.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 24))
                nodes = morph.CreateOpening("Straight", ents, params)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 25))
                nodes = morph.CreateOpening("Straight rounded", ents, params)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 22))
                arg4 = {}
                arg4["Reconstruct"] = 3
                nodes = morph.CreateOpening("Curved", ents, params, auto_reconstruct=arg4)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", 23))
                nodes = morph.CreateOpening("Curved rounded", ents, params)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                nodes = morph.CreateOpening("Circular", ents, params)

                params = []
                params.append(20.0)
                params.append(6.0)
                params.append(3.0)
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                arg4 = []
                arg4.append(base.GetEntity(constants.NASTRAN, "POINT", 6))
                arg4.append(base.GetEntity(constants.NASTRAN, "POINT", 7))
                nodes = morph.CreateOpening(
                    "Rectangular rounded", ents, params, direction_points=arg4
                )

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7116))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7374))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7269))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 7036))
                params = []
                nodes = morph.CreateOpening("Surface", ents, params)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: Create instead.",
        DeprecationWarning,
    )


def CreateRib(
    rib_type: str,
    rib_entities: object,
    rib_parameters: object,
    add_to_set: int,
    auto_reconstruct: object,
    exclude_feature_recon: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`Create` instead.


    Function for the creation of ribs.

    Parameters
    ----------
    rib_type : str
            The type of the rib, values can be "Rib 3D" or "Rib 2D".

    rib_entities : object
            A list of entities where the rib will be created.

    rib_parameters : object
            A list of the rib parameters:

            - "Rib 2D": [Length], length is optional, if left blank it will be calculated
               from the points given in "rib_entities".

            - "Rib 3D": [Length, Width, Angle, "Top", value, "Bottom", value], length is optional,
               if left blank it will be calculated from the points given in "rib_entities".
               "Top" and "Bottom" are string values and can take values "Chamfer" or "Fillet" and
               the value for each one (see examples).

    add_to_set : int, optional
            Integer id of the Set, to add the created feature shells

    auto_reconstruct : object, optional
            Dictionary with Improve mesh value {'Reconstruct', 'Smooth', ' Reshape'} and a value an integer of zones around the created feature.

    exclude_feature_recon : bool, optional
            Keep feature out from reconstruct.

    Returns
    -------
    object
            Returns the shells of the created rib, or 0 on error.

    See Also
    --------
    CreateStamp, CreateBead, CreateFlangedOpening, CreateOpening

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def createRibs():
                params = []
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4382300))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4384300))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4393018))

                shells = morph.CreateRib("Rib 2D", ents, params)

                params = []
                # params.append(250.)
                params.append(7.0)
                params.append(9.0)
                params.append("Chamfer")
                params.append(2.0)
                params.append("Fillet")
                params.append(0.0)

                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4382629))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4393568))
                ents.append(base.GetEntity(constants.NASTRAN, "GRID", 4369850))

                shells = morph.CreateRib("Rib 3D", ents, params, add_to_set=1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: Create instead.",
        DeprecationWarning,
    )


def SimulateDoeWindow(
    mainitem: object,
    values: str,
    designs: int,
    algorithm: str,
    generate: bool,
    experiments_file: str,
) -> int:
    """

    Function for accessing the "Simulate-Doe" window in Optimization task.

    Parameters
    ----------
    mainitem : object
            An Optimization_Task item.

    values : str
            A filename with the values to be loaded in the window.

    designs : int
            The number of designs.

    algorithm : str
            The selected algorithm values can be:
            -'Linear'
            -'Random'
            -'Full Factorial'
            -'Uniform Latin Hypercube'

    generate : bool
            Auto generate experiments based on the previous values.

    experiments_file : str, optional
            The full path of the output file should always follow the string argument "experiments_file". This output file will contain all the experiments that the
            user created on the window's table. For more information, look at the examples.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def onlyFromFile():
                mainitem = base.GetEntity(constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                morph.SimulateDoeWindow(mainitem, "simulate_doe_values.txt")


            def fromFileAndAuto():
                str = "results_2.txt"
                mainitem = base.GetEntity(constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                morph.SimulateDoeWindow(mainitem, str, 11, "Linear", True)

                # morph.SimulateDoeWindow(mainitem, str, 9, 'Random', True)
                # morph.SimulateDoeWindow(mainitem, "", 7, 'Full Factorial', False)
                # morph.SimulateDoeWindow(mainitem, "", 8, 'Uniform Latin Hypercube', False)
                # morph.SimulateDoeWindow(mainitem, "", 11, 'Linear', True)
                # morph.SimulateDoeWindow(mainitem, str)
                # morph.SimulateDoeWindow(mainitem=mainitem, values="", designs=8, algorithm='Uniform Latin Hypercube', generate=True)


            def autoGenerateAndSaveToFile():
                str = "results_2.txt"
                mainitem = ansa.base.GetEntity(ansa.constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                ansa.morph.SimulateDoeWindow(
                    mainitem,
                    "",
                    11,
                    "Linear",
                    True,
                    "experiments_file",
                    "/home/user/DoeStudy/generated_experiments.txt",
                )


    """


def MorphConstraintPlanar(
    entities: object, morphed: object, bounds: object, autobounds: bool
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintPlanar` instead.


    Script function for creating a planar morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will
    force the constraint's 'entities' to become coplanar when the DFM executes.
    To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds'
    entities may be provided to the constraint, essentially defining a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities to become coplanar.

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining the bounds of the constraint's fitting process.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    Returns
    -------
    object
            Returns a reference to the newly created morph constraint object.

    See Also
    --------
    MorphConstraintRigid, MorphConstraintScaled, MorphConstraintDirectional, MorphConstraintPathFollower, MorphConstraintFlange, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "GRID")

                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")

                cnstr = morph.MorphConstraintPlanar(ents, morphed, bounds)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintPlanar instead.",
        DeprecationWarning,
    )


def MorphConstraintRigid(
    entities: object, morphed: object, bounds: object, autobounds: bool
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintRigid` instead.


    Script function for creating a rigid morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will force
    the constraint's 'entities' to move (translate/rotate) rigidly when the DFM executes.
    To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' entities
    may be provided to the constraint, essentially defining a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities to remain rigid.

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining the bounds of the constraint's fitting process.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    Returns
    -------
    object
            Returns the created morph constraint.

    See Also
    --------
    MorphConstraintPlanar, MorphConstraintScaled, MorphConstraintDirectional, MorphConstraintPathFollower, MorphConstraintFlange, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "GRID")

                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")

                cnstr = morph.MorphConstraintRigid(ents, morphed, bounds)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintRigid instead.",
        DeprecationWarning,
    )


def MorphConstraintScaled(
    entities: object, morphed: object, bounds: object, autobounds: bool
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintScaled` instead.


    Script function for creating a scaled morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will force
    the constraint's 'entities' to move (translate/rotate) rigidly, subject to homogeneous
    scaling, when the DFM executes. To alleviate and/or confine the effects of the constraint,
    'morphed' and 'bounds' entities may be provided to the constraint, essentially defining
    a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities to remain rigid (subject to homogeneous scaling).

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining the bounds of the constraint's fitting process.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    Returns
    -------
    object
            Returns a reference to the newly created morph constraint object.

    See Also
    --------
    MorphConstraintPlanar, MorphConstraintRigid, MorphConstraintDirectional, MorphConstraintPathFollower, MorphConstraintFlange, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "GRID")

                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")

                cnstr = morph.MorphConstraintScaled(ents, morphed, bounds)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintScaled instead.",
        DeprecationWarning,
    )


def MorphConstraintDirectional(
    entities: object,
    morphed: object,
    bounds: object,
    coordinate: object,
    x_status: str,
    y_status: str,
    z_status: str,
    autobounds: bool,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintDirectional` instead.


    A function for creating a directional morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will force
    the constraint's 'entities' to morph only along user permisible direction(s) when the DFM
    executes. To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds'
    entities may be provided to the constraint, essentially defining a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities to morph in user defined direction(s).

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining bounds of constraint's fitting process.

    coordinate : object
            A local coordinate system, defining the allowable/non-allowable morphing axes.

    x_status : str
            -'active': morphing will occur as normal in local x-axis.
            -'inactive': will freeze movement along local x-axis.

    y_status : str
            -'active': morphing will occur as normal in local y-axis.
            -'inactive': will freeze movement along local y-axis.

    z_status : str
            -'active': morphing will occur as normal in local z-axis.
            -'inactive': will freeze movement along local z-axis.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    Returns
    -------
    object
            It returns the created morph constraint.

    See Also
    --------
    MorphConstraintPlanar, MorphConstraintRigid, MorphConstraintScaled, MorphConstraintPathFollower, MorphConstraintFlange, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "GRID")

                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")

                vals = {"CID": 9, "G1": 5852, "G2": 5851, "G3": 5718}
                cs = base.CreateEntity(constants.NASTRAN, "CORD_NODES_R", vals)
                cnstr = morph.MorphConstraintDirectional(
                    ents, morphed, bounds, cs, "active", "inactive", "active"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintDirectional instead.",
        DeprecationWarning,
    )


def MorphConstraintPathFollower(
    entities: object, morphed: object, bounds: object, path: object, autobounds: bool
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintPathFollower` instead.


    A function for creating a path follower morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will force
    the constraint's 'entities' to move only along a pre-defined path when the DFM executes.
    To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds' entities
    may be provided to the constraint, essentially defining a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities [edges or points] to remain along a path.

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining bounds of constraint's fitting process.

    path : object
            A list of the entities [edges or points] defining the movement path.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    Returns
    -------
    object
            Returns the created morph constraint.

    See Also
    --------
    MorphConstraintPlanar, MorphConstraintRigid, MorphConstraintScaled, MorphConstraintDirectional, MorphConstraintFlange, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 4)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "EDGE")
                path = ents

                set = base.GetEntity(constants.NASTRAN, "SET", 5)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 6)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")

                morph.MorphConstraintPathFollower(ents, morphed, bounds, path)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintPathFollower instead.",
        DeprecationWarning,
    )


def MorphSplitProject(
    box_edge: object, points: object, fit_new_skin_edges: bool, work_on: str
) -> int:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`BoxSplit` instead.


    A function for projecting points array on an edge to split morph box(es).

    Parameters
    ----------
    box_edge : object
            The box edge that will be split (point will be projected on this edge).

    points : object
            A point (3D point, node, hot point, etc) to project on the box edge.

    fit_new_skin_edges : bool, optional
            If set to True, new skin edges will fit on the underlying model.
            Default value is False.

    work_on : str, optional
            Defines where the projection is going to take place:
            'whole_db' fit skin edges will take place on the whole database,
            'visible'  fit skin edges will take place only on the visible elements
            If work_on is not set then whole_db will be the default argument.
            This option is only available only when fit_skin_edges is set to true.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    MorphSplit, MorphSplitToHexa, MorphSplitToPenta

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                box_edge = base.GetEntity(constants.NASTRAN, "MORPHEDGE", 1)
                box_point = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 1)
                morph.MorphSplitProject(box_edge, box_point)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: BoxSplit instead.",
        DeprecationWarning,
    )


def MorphAdaptCrossections(entities: object, number_or_length: str) -> object:
    """

    A function for the creation of morphing boxes between 2 or more crossections.
    The function will create multicut crossections based on the given length or number
    and morphing boxes with length and width parameters to manipulate the crossections.

    Parameters
    ----------
    entities : object
            A list with the shell elements to cut and create crossections.

    number_or_length : str
            The number or length to cut. Use ~ to define length.

    Returns
    -------
    object
            Returns a list containing references to the newly created morphing boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                m1 = base.CollectEntities(constants.NASTRAN, None, "SET")
                for set in m1:
                    shells = base.CollectEntities(constants.NASTRAN, set, "SHELL")
                    morphes = morph.MorphAdaptCrossections(shells, "3")
                    # morphes = morph.MorphAdaptCrossections(shells, "~30")
                    morph.MorphLoad(morphes, db_or_visib="Visib")


    """


def MorphByCurves(height_edges: object, top_bottom_edges: object) -> object:
    """

    A function for creating a 3D morphing box by defining its four "height" edges
    and the "top", "bottom" edges (optionally).

    Parameters
    ----------
    height_edges : object
            A list that contains all the entities that define the four box "height" edges.

    top_bottom_edges : object, optional
            A list that contains all the entities that define the
            "top" and "bottom" edges of the new box.

    Returns
    -------
    object
            Returns a reference to the newly created box object on success, or 0 on failure.

    See Also
    --------
    MorphOrtho, MorphByPoints

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def morphByCurves():
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

                morph.MorphByCurves(height_edges, top_bottom_edges)


    """


def Morph2DCreate(
    type: str,
    entities: object,
    thickness: float,
    delete_original: bool,
    paste: bool,
    convert_to_ortho: bool,
) -> object:
    """

    A function to create a 2D morphing box using the input entities.
    Thickness of the 2D morphing box may be defined (optional argument).
    For "hatches" case, the original 3D boxes may be deleted (optional argument).
    For "wireframe" case, there is the option to paste the created 2D boxes
    (paste=True) and to convert them to orthogonal boxes (convert_to_ortho=True).
    These two arguments (paste & convert_to_ortho) are mutually exclusive.
    If they are both set "True" they will be evaluated as "False".

    Parameters
    ----------
    type : str
            A string that defines the input entities. It can have
            the values "points", "curves", "hatches" and "wireframe".

    entities : object
            A list of the entities that are used for the creation of the 2D morphing box.
            According to the "type" it takes different entities:
            -"points" - list with entities whose points will be used to create the new 2D box,
            -"curves" - list containing four lists with the input curves/cons/edges,
            -"hatches" - list containing the input box faces,
            -"wireframe" - list containing the input curves.

    thickness : float, optional
            The thickness of the 2D morphing box.

    delete_original : bool, optional
            Defines if the original boxes will be deleted.
            It is used only for the "hatches" type.

    paste : bool, optional
            Defines if the created 2D boxes will be pasted or not.
            It is used only for the "wireframe" case.
            (Default: False)

    convert_to_ortho : bool, optional
            Defines if the created 2D boxes will be converted to orthogonal boxes or not.
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


            def morph2DCreateByPoints():
                points1 = []
                points1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 74))
                points1.append(base.GetEntity(constants.NASTRAN, "GRID", 275))
                points1.append(base.GetEntity(constants.NASTRAN, "GRID", 310))
                points1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 78))
                morph1 = morph.Morph2DCreate(type="points", entities=points1, thickness=12)
                if morph1._id:
                    print("new 2D morphing box id = ", morph1._id)
                points2 = []
                points2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 98))
                points2.append(base.GetEntity(constants.NASTRAN, "GRID", 274))
                points2.append(base.GetEntity(constants.NASTRAN, "GRID", 309))
                morph2 = morph.Morph2DCreate(type="points", entities=points2, thickness=11)
                if morph2._id:
                    print("new 2D morphing box id = ", morph2._id)


            def morph2DCreateByCurves():
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
                morph2d = morph.Morph2DCreate(type="curves", entities=entities, thickness=55)

                if morph2d._id:
                    print("new 2D morphing box id = ", morph2d._id)


            def morph2DCreateByHatches():
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 1))
                m.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 2))

                newBoxes = morph.Morph2DCreate(
                    type="hatches", entities=m, delete_original=True, thickness=23
                )

                for run_box in newBoxes:
                    if run_box._id:
                        print("new 2D morphing box id = ", run_box._id)


            def morph2DCreateByCurvesWireframe():
                type = "wireframe"
                thickness = 5.0
                paste = False
                convert_to_ortho = False
                delete_original = False
                entities = base.CollectEntities(0, None, "CURVE")

                newBoxes = morph.Morph2DCreate(
                    type, entities, thickness, delete_original, paste, convert_to_ortho
                )


    """


def MorphEdgesRedistribute(
    box_edges: object, factor: float, nodal_number_redistribution: bool
) -> int:
    """

    Script function to redistribute boxes splits along input box edges.
    Splits (corner points of box edges) are redistributed within the
    original position and the equally-spaced position. Redistribution
    is applied to chains of connected box edges (input edges are classified
    to these chains).

    Parameters
    ----------
    box_edges : object
            A list containing input box edges.

    factor : float
            The redistribution factor. It takes values from 0 (original
            position) to 1 (equally-spaced position).

    nodal_number_redistribution : bool, optional
            Defines if redistribution will be applied according to
            uniform nodal distribution.

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
            from ansa import morph


            def main():
                box_edges = []
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 41))
                box_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 81))
                box_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 93))
                box_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 57))
                box_edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 69))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 17))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 29))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 9))
                morph.MorphEdgesRedistribute(
                    box_edges=box_edges, factor=0.49, nodal_number_redistribution=False
                )


    """


def MorphEdgesMatch(box_edges: object, target_edges: object, factor: float):
    """

    A function to match the shape of input box edges tothe target edges.
    Input box edges are classified to chains of connected box edges and each chain is matched separately.

    Parameters
    ----------
    box_edges : object
            A list containing the input box edges.

    target_edges : object
            A list containing the target edges.

    factor : float
            The match factor. It takes values from 0 (input edges'
            original shape) to 1 (target edges' shape).

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                box_edges = []
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 4))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 63))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 111))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 159))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 2))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 62))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 110))
                box_edges.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 158))

                target_edges = []
                target_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 1))
                target_edges.append(base.GetEntity(constants.NASTRAN, "CURVE", 4))

                morph.MorphEdgesMatch(box_edges=box_edges, target_edges=target_edges, factor=0.82)


    """


def MorphTopo(boxes: object, tolerance: str) -> int:
    """

    Script function to connect the input boxes, provided that the Control Points of their
    neighboring Box Faces, reside within the specific tolerance.

    Parameters
    ----------
    boxes : object
            A list containing the input boxes.

    tolerance : str, optional
            A string to define the tolerance mode, accepting
            "draft", "middle", "fine" or "extra fine".
            Default mode depends on Resolution/Tolerances/Units
            and Morph/Optimization settings.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    See Also
    --------
    MorphTopoVis

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                boxes = []
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 21))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 20))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 19))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 18))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 14))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 10))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 6))
                boxes.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 1))
                ansa.morph.MorphTopo(boxes)

                pair = []
                pair.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 2))
                pair.append(base.GetEntity(ansa.constants.NASTRAN, "HEXA_BOX", 5))
                ansa.morph.MorphTopo(pair, "draft")


    """


def MorphSplitToPenta(box_points: object) -> int:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`BoxSplit` instead.


    This function splits quad faces of hexahedral boxes in order to form two penta boxes.

    Parameters
    ----------
    box_points : object
            A list containing pairs of box points (two consecutive points that correspond
            to the points that split will be performed to) of quad box faces.

    Returns
    -------
    int
            Returns the number of successful splits.

    See Also
    --------
    MorphSplit, MorphSplitProject

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                points = []

                # first split to be performed
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 1029))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 592))

                # second split to be performed
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 1007))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 686))

                # third split to be performed
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 1054))
                points.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 14))

                num = morph.MorphSplitToPenta(box_points=points)
                print("number of successful splits: ", num)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: BoxSplit instead.",
        DeprecationWarning,
    )


def MorphRelease(entities: object, keep_internal_connectivity: bool) -> int:
    """

    This function releases input boxes or box faces.
    It can be used for morphing boxes, size boxes and hexa block boxes.

    Parameters
    ----------
    entities : object
            A list containing boxes or box faces to be released.

    keep_internal_connectivity : bool, optional
            Option that controls if input boxes will remain connected after release.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 10))
                boxes.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 7))
                boxes.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 4))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 16))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 13))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 12))
                morph.MorphRelease(entities=boxes)

                box_faces = []
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 121))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 115))
                box_faces.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 109))
                box_faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 49))
                box_faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 29))
                box_faces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 13))
                morph.MorphRelease(entities=box_faces)


    """


def MorphCollapse(
    box_face: object,
    box_edge: object,
    target_point: object,
    collapse_entire_topology: bool,
):
    """

    A function that generates PENTA boxes by collapsing box edges.

    Parameters
    ----------
    box_face : object
            The box face to collapse.

    box_edge : object
            The box edge (that belongs to the input box face) to collapse.

    target_point : object, optional
            A box point (corner point of input edge) to define the collapse
            direction. If it is not defined, collapse is applied to the middle
            of the input box edge.

    collapse_entire_topology : bool, optional
            Defines if all the boxes from the side of the collapsed edge
            will be collapsed.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                box_face = base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 87)
                box_edge = base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 252)
                morph.MorphCollapse(
                    box_face=box_face, box_edge=box_edge, collapse_entire_topology=True
                )

                box_face = base.GetEntity(constants.NASTRAN, "HEXA_BOX_FACE", 8)
                box_edge = base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 226)
                box_point = base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", 1664)
                morph.MorphCollapse(
                    box_face=box_face,
                    box_edge=box_edge,
                    target_point=box_point,
                    collapse_entire_topology=False,
                )


    """


def CoarseBoxTopology(
    boxes: object, box_edge: object, coarse_ratio: str, distance: float
):
    """

    Function to convert complicated Box structures to more coarse.
    The function automatically creates C- & L- type structures inside the
    buffer zone, in order to achieve the desired coarsening ratio.

    Parameters
    ----------
    boxes : object
            A list containing the input boxes to coarse.

    box_edge : object
            The box edge denoting the coarsening direction.

    coarse_ratio : str
            A string that takes the values "3-1" or "2-1" and defines the shape of
            the boxes in the buffer zone.

    distance : float
            The distance that defines how much the buffer zone will be extended.

    See Also
    --------
    MorphCollapse

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                boxes = []
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 2))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 15))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 18))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 19))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 20))
                boxes.append(base.GetEntity(constants.NASTRAN, "HEXA_BOX", 21))
                box_edge = base.GetEntity(constants.NASTRAN, "HEXA_BOX_EDGE", 159)
                morph.CoarseBoxTopology(
                    boxes=boxes, box_edge=box_edge, coarse_ratio="3-1", distance=22
                )


    """


def DCPositionApply(entity: object, distance: float) -> bool:
    """

    The function applies the distance to the given design change position entity.

    Parameters
    ----------
    entity : object
            The DC_POSITION entity.

    distance : float
            The distance that will be applied.

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    See Also
    --------
    DCCrossSectionApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                dc_position = base.GetEntity(constants.NASTRAN, "DC_POSITION", 1)
                res = morph.DCPositionApply(dc_position, 10)


    """


def DCCrossSectionApply(entity: object, width: float, height: float) -> bool:
    """

    The function will apply a width and height change to the given DC_CROSS_SECTION entity.

    Parameters
    ----------
    entity : object
            The DC_CROSS_SECTION entity.

    width : float
            Width change value.

    height : float
            Height change value.

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    See Also
    --------
    DCPositionApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                dc_cs = base.GetEntity(constants.NASTRAN, "DC_CROSS_SECTION", 1)
                res = morph.DCCrossSectionApply(dc_cs, 2.0, 0.0)


    """


def MorphParamCreateTransform(
    name: str, morph_points: object, transform_points: object
) -> int:
    """

    Function for the creation of a transform morph parameter for morph points.

    Parameters
    ----------
    name : str
            The desired name for the new parameter.

    morph_points : object
            A list of morph points.

    transform_points : object
            A list of 6 points to get transformation coordinates or 2 coordinates.

    Returns
    -------
    int
            Returns the ID of the newly created parameter, or 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                arg2 = []
                arg2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 77))
                arg2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 78))
                arg2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 81))
                arg2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 82))

                arg3 = []
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 1))
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 2))
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 5))
                arg3.append(base.GetEntity(constants.NASTRAN, "POINT", 6))

                morph.MorphParamCreateTransform("Transform param", arg2, arg3)


    """


def MorphCreateMorphAlignArgs(
    entities: object,
    target_entities: object,
    distance: float,
    offset: float,
    user_direction: object,
    align_to_midplane: bool,
    align_on_geometry: bool,
) -> object:
    """
    .. deprecated:: 17.1.0
            Use :py:func:`NewMorphAlignArgs` instead.


    Function for the creation of an object to be used in creating an Align parameter.

    Parameters
    ----------
    entities : object
            A list with morph points to align.

    target_entities : object
            A list with entities where morph points will be aligned.
            Can have either 3 points to define a plane or anything else..

    distance : float, optional
            The alignment distance.

    offset : float, optional
            Any offset value.

    user_direction : object, optional
            A list with 3 doubles to define a used defined vector.

    align_to_midplane : bool, optional
            Boolean to define if it will align to mid plane or not.

    align_on_geometry : bool, optional
            Boolean to define if it will align to geometry or not.

    Returns
    -------
    object
            Returns a reference to the newly created object, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constans
            from ansa import morph


            def main():
                set2 = []
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 87))
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 91))
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 95))
                # set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 99))

                set1 = []
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 77))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 78))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 81))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 82))

                set2 = base.GetEntity(constants.NASTRAN, "SET", 6)
                args1 = [
                    morph.MorphCreateMorphAlignArgs(
                        entities=set1, target_entities=set2, distance=1000.0, offset=0
                    )
                ]
                # ., user_direction=(-.01,0.75,0.65), align_to_midplane=True, align_on_geometry=True)]
                morph.MorphParamCreate("Align_param", "MorphAlign", args1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 17.1.0. Use :py:func: NewMorphAlignArgs instead.",
        DeprecationWarning,
    )


def NewParameterDFMFitEdges(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a DFM edge fit morph parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMFitEdgesArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'DFM_Edge_Fit')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMFitEdges, morph.DFM, NewDFMFitEdgesArgs

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 2)]
                source_2 = [base.GetEntity(constants.NASTRAN, "SET", 3)]
                target_2 = [base.GetEntity(constants.NASTRAN, "SET", 4)]
                source_3 = [base.GetEntity(constants.NASTRAN, "SET", 5)]
                target_3 = [base.GetEntity(constants.NASTRAN, "SET", 6)]
                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                edge_fit_args = []
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_1, target_1))
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_2, target_2))
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_3, target_3))

                param_1 = morph.NewParameterDFMFitEdges(
                    edge_fit_args, elements, bounds, False, "Edge fit"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewDFMFitEdgesArgs(source: object, target: object) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMFitEdges` instead.


    Function for the creation of an object that will be used by the NewParameterDFMFitEdges function.
    This is an auxiliary function.

    Parameters
    ----------
    source : object
            A list of entities that will be used as source of DFM edge fit parameter.

    target : object
            A list of entities that will be used as target of DFM edge fit parameter.

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    See Also
    --------
    morph.DFMFitEdges, morph.DFM, NewParameterDFMFitEdges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 2)]
                source_2 = [base.GetEntity(constants.NASTRAN, "SET", 3)]
                target_2 = [base.GetEntity(constants.NASTRAN, "SET", 4)]
                source_3 = [base.GetEntity(constants.NASTRAN, "SET", 5)]
                target_3 = [base.GetEntity(constants.NASTRAN, "SET", 6)]
                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                edge_fit_args = []
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_1, target_1))
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_2, target_2))
                edge_fit_args.append(morph.NewDFMFitEdgesArgs(source_3, target_3))

                param_1 = morph.NewParameterDFMFitEdges(
                    edge_fit_args, elements, bounds, False, "Edge fit"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMFitEdges instead.",
        DeprecationWarning,
    )


def NewDFMFitSurfsArgs(
    source_area: object,
    target_area: object,
    source_points: object,
    target_points: object,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMFitSurfaces` instead.


    Function for the creation of an object that will be used by the NewParameterDFMFitSurfaces function.
    This is an auxiliary function.

    Parameters
    ----------
    source_area : object
            A list of entities that will be used as the source area

    target_area : object
            A list of entities that will be used as the target area

    source_points : object
            A list of perimetric points of the source area

    target_points : object
            A list of perimetric points of the target area

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    See Also
    --------
    morph.DFMFitSurfaces, morph.DFM, NewParameterDFMFitSurfaces

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 9)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 10)]
                source_2 = [base.GetEntity(constants.NASTRAN, "FACE", 6)]
                target_2 = [base.GetEntity(constants.NASTRAN, "FACE", 8)]

                src_pnts1 = []
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 4))

                trg_pnts1 = []
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 5))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 6))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 8))

                src_pnts2 = []
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 9))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 10))

                trg_pnts2 = []
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 8))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 12))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 13))

                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                surf_fit_args = []
                surf_fit_args.append(
                    morph.NewDFMFitSurfsArgs(source_1, target_1, src_pnts1, trg_pnts1)
                )
                surf_fit_args.append(
                    morph.NewDFMFitSurfsArgs(source_2, target_2, src_pnts2, trg_pnts2)
                )

                param_1 = morph.NewParameterDFMFitSurfaces(
                    surf_fit_args, elements, bounds, False, "Surface fit1"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMFitSurfaces instead.",
        DeprecationWarning,
    )


def NewDFMTranslateArgs(translated: object, dx: float, dy: float, dz: float) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMTranslate` instead.


    Function for the creation of an object that will be used by the NewParameterDFMTranslate function.
    This is an auxiliary function.

    Parameters
    ----------
    translated : object
            A list of entities that will be translated.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    Returns
    -------
    object
            Returns a reference to the newly created object on sucess, or None on failure.

    See Also
    --------
    morph.DFMTranslate, morph.DFM, NewParameterDFMTranslate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set2 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMTranslateArgs(set1, 0, -1, 0))
                args.append(morph.NewDFMTranslateArgs(set2, 0, 1, 0))
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                param2 = morph.NewParameterDFMTranslate(args, morphed, bounds, False, "Traslate 2")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMTranslate instead.",
        DeprecationWarning,
    )


def NewDFMRotateArgs(
    rotated: object, x: float, y: float, z: float, dx: float, dy: float, dz: float
) -> object:
    """

    Function for the creation of an object that will be used by the NewParameterDFMRotate function.
    This is an auxiliary function.

    Parameters
    ----------
    rotated : object
            A list of entities to be rotated.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    See Also
    --------
    NewParameterDFMRotate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMRotateArgs(set3, -100, -2, 169, 1, 0, 0))
                args.append(morph.NewDFMRotateArgs(set4, -100, -2, 169, -1, 0, 0))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]

                param_id = morph.NewParameterDFMRotate(
                    args, morphed, bounds, False, "Rotate Combined"
                )


    """


def NewDFMScaleArgs(scaled: object, x: float, y: float, z: float) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMScale` instead.


    Function for the creation of an object that will be used by the NewParameterDFMScale function.
    This is an auxiliary function.

    Parameters
    ----------
    scaled : object
            A list of entities that will be scaled.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    See Also
    --------
    morph.DFMScale, morph.DFM, NewParameterDFMScale

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMScaleArgs(set3, -100, -100, 169))
                args.append(morph.NewDFMScaleArgs(set4, -100, 100, 169))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.NewParameterDFMScale(
                    "Scale Combined", args, morphed, bounds, False
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMScale instead.",
        DeprecationWarning,
    )


def NewDFMTransformArgs(
    transformed: object, src_coord: object, trg_coord: object
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMTransform` instead.


    Script function for the creation of an object that will be used by NewParameterDFMTransform script function.
    This is an auxiliary function

    Parameters
    ----------
    transformed : object
            a list of entities that will be transformed

    src_coord : object
            is an ANSA coordinate object that will be used as the source coordinate system.

    trg_coord : object
            is an ANSA coordinate object that will be used as the target coordinate system.

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    See Also
    --------
    morph.DFMTransform, morph.DFM, NewParameterDFMTransform

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                coord3 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 1)
                coord4 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 2)
                coord5 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 4)
                coord6 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 3)

                args = []
                args.append(morph.NewDFMTransformArgs(set4, coord3, coord4))
                args.append(morph.NewDFMTransformArgs(set3, coord5, coord6))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param_id2 = morph.NewParameterDFMTransform(
                    args, morphed, bounds, False, "Transform Combined"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMTransform instead.",
        DeprecationWarning,
    )


def NewDFMAlignArgs(
    entities: object,
    target_entities: object,
    target_axis: object,
    target_plane: object,
    include_thickness: bool,
    max_distance: float,
    user_direction: object,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFMAlign` instead.


    Function for the creation of an object that will be used by NewParameterDFMAlign script function.
    This is an auxiliary function.

    Parameters
    ----------
    entities : object
            A list of entities that will be aligned.

    target_entities : object, optional
            A list of entities that will be used as the target surface of alignment.

    target_axis : object, optional
            A list of doubles that describes an axis that will be used as the target axis.
            The format of this list is (x, y, z, dx, dy, dz) where x, y and z
            are the components of the origins position vector and dx, dy and dz
            are the components of the direction vector of the axis.

    target_plane : object, optional
            A list of doubles that describes a plane that will be used as the target plane.
            The format of this list is (x, y, z, dx, dy, dz) where x, y and z
            are the components of the origins position vector of the plane
            and dx, dy and dz are the components of the direction of the normal vector
            of the plane.

    include_thickness : bool, optional
            An option to determine if the thickness of the aligned and target elements
            will be included in the calculation.
            (Default: False)

    max_distance : float, optional
            Determines the maximun radial search distance where the
            aligned elements will seek
            for target entities.
            Default value is infinite.

    user_direction : object, optional
            A list of doubles that describes a user's predefined alignment direction.
            The format of this list is (dx, dy, dz) where dx, dy and dz are the
            components of the direction vector.

    Returns
    -------
    object
            Returns a list containing references to the newly crated objects on success, or None on failure.

    See Also
    --------
    morph.DFMAlign, morph.DFM, NewParameterDFMAlign

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                setsrc1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                setsrc2 = base.GetEntity(constants.NASTRAN, "SET", 11)
                settrg = [base.GetEntity(constants.NASTRAN, "SET", 13)]
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                args1 = [morph.NewDFMAlignArgs(entities=(setsrc1, setsrc2), target_entities=settrg)]

                param1 = morph.NewParameterDFMAlign(args1, morphed, None, True, "Align to entities")


            def main():
                set14 = base.GetEntity(constants.NASTRAN, "SET", 14)
                set15 = base.GetEntity(constants.NASTRAN, "SET", 15)

                args2 = []
                args2.append(
                    morph.NewDFMAlignArgs(entities=(set14), target_axis=(-100, 300, 0, 0, 0, 1))
                )
                args2.append(
                    morph.NewDFMAlignArgs(entities=(set15), target_plane=(-100, -300, 0, 0, -1, 0))
                )

                morphed = []
                morphed, append(base.GetEntity(constants.NASTRAN, "SET", 7))
                morphed.append(base.GetEntity(constants.NASTRAN, "FACE", 10))
                param2 = morph.NewParameterDFMAlign(
                    args2, morphed, None, True, "Align combined axis-plane"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFMAlign instead.",
        DeprecationWarning,
    )


def NewParameterAngle(morph_edges: object, name: str) -> object:
    """

    Function for the creation of an angle morph parameter for morph edges.

    Parameters
    ----------
    morph_edges : object
            A list of morph edges. The list must have even size.
            Morph edges in the odd indicies of the list will retain their position
            while those in even indicies will rotate.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Angle')

    Returns
    -------
    object
            Returns a reference to the newly created object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 9))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 4))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 10))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 2))

                param = morph.NewParameterAngle(moedges)
                if param:
                    morph.MorphParam(param, 10)


    """


def NewParameterDeformation(affected: str, name: str, entities: object) -> object:
    """

    Function for the creation of a deformation morph parameter.

    Parameters
    ----------
    affected : str, optional
            Indicates which entities will be recorded by the deformation parameter.
            Possible values are 'All' and 'Moved'.
            (Default: 'All')

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Deform')

    entities : object, optional
            An object containg MORPH_HISTORY or DESVARs to create the parameter

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                morph.NewParameterDeformation(name="Deformation", affected="Moved")


    """


def NewParameterDFMAlign(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm align parameter.

    Parameters
    ----------
    args : object
            A list of objects returned by NewDFMAlignArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_Align')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMAlign, morph.DFM, NewDFMAlignArgs

    Examples
    --------
    ::

            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                setsrc1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                setsrc2 = base.GetEntity(constants.NASTRAN, "SET", 11)
                settrg = [base.GetEntity(constants.NASTRAN, "SET", 13)]
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                args1 = [morph.NewDFMAlignArgs(entities=(setsrc1, setsrc2), target_entities=settrg)]

                param1 = morph.NewParameterDFMAlign(args1, entities=morphed, name="Align")


            def main():
                set14 = base.GetEntity(constants.NASTRAN, "SET", 14)
                set15 = base.GetEntity(constants.NASTRAN, "SET", 15)

                args2 = []
                args2.append(
                    morph.NewDFMAlignArgs(entities=(set14), target_axis=(-100, 300, 0, 0, 0, 1))
                )
                args2.append(
                    morph.NewDFMAlignArgs(entities=(set15), target_plane=(-100, -300, 0, 0, -1, 0))
                )

                morphed = []
                morphed.append(base.GetEntity(constants.NASTRAN, "SET", 7))
                morphed.append(base.GetEntity(constants.NASTRAN, "FACE", 10))
                param2 = morph.MorphParamCreateDFMAlign(
                    args2, morphed, None, True, "Align combined axis-plane"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMFitSurfaces(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a DFM surface fit morph parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMFitSurfsArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_Surface_Fit')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFM, morph.DFMFitSurfaces, NewDFMFitSurfsArgs

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                source_1 = [base.GetEntity(constants.NASTRAN, "SET", 9)]
                target_1 = [base.GetEntity(constants.NASTRAN, "SET", 10)]
                source_2 = [base.GetEntity(constants.NASTRAN, "FACE", 6)]
                target_2 = [base.GetEntity(constants.NASTRAN, "FACE", 8)]

                src_pnts1 = []
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 1))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 2))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 4))

                trg_pnts1 = []
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 5))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 6))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", 8))

                src_pnts2 = []
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 4))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 3))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 9))
                src_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 10))

                trg_pnts2 = []
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 8))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 7))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 12))
                trg_pnts2.append(base.GetEntity(constants.NASTRAN, "GRID", 13))

                elements = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                surf_fit_args = []
                surf_fit_args.append(
                    morph.NewDFMFitSurfsArgs(source_1, target_1, src_pnts1, trg_pnts1)
                )
                surf_fit_args.append(
                    morph.NewDFMFitSurfsArgs(source_2, target_2, src_pnts2, trg_pnts2)
                )

                param_1 = morph.NewParameterDFMFitSurfaces(
                    surf_fit_args, elements, bounds, False, "Surface fit1"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMOffset(
    offset_ents: object, morph_ents: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a DFM offset morph parameter.

    Parameters
    ----------
    offset_ents : object
            A list of entities that will offset.

    morph_ents : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'DFM_Offset')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMOffset, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = base.GetEntity(constants.NASTRAN, "SET", 9)
                set2 = base.GetEntity(constants.NASTRAN, "SET", 11)

                offset = base.CollectEntities(constants.NASTRAN, (set1, set2), "FACE")
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]

                param = morph.NewParameterDFMOffset(offset, morphed)
                morph.MorphParam(param, 10)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMRotate(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm rotate parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMRotateArgs

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter
            (Default: 'DFM_Rotate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMRotate, morph.DFM, NewDFMRotateArgs

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMRotateArgs(set3, -100, -2, 169, 1, 0, 0))
                args.append(morph.NewDFMRotateArgs(set4, -100, -2, 169, -1, 0, 0))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]

                param = morph.NewParameterDFMRotate(
                    args=args, entities=morphed, bounds=bounds, name="Rotate Combined"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMScale(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm scale parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMScaleArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_Scale')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMScale, morph.DFM, NewDFMScaleArgs

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set2 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMScaleArgs(set1, -100, -100, 169))
                args.append(morph.NewDFMScaleArgs(set2, -100, 100, 169))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param = morph.NewParameterDFMScale(args, morphed, bounds, False)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMTranslate(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm translate parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMTranslateArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_Translate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMTranslate, morph.DFM, NewDFMTranslateArgs

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set1 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set2 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                args = []
                args.append(morph.NewDFMTranslateArgs(set1, 0, -1, 0))
                args.append(morph.NewDFMTranslateArgs(set2, 0, 1, 0))
                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [base.GetEntity(constants.NASTRAN, "SET", 8)]

                param2 = morph.NewParameterDFMTranslate(args, morphed, bounds, False, "Traslate 2")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterDFMTransform(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm transform parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMTransformArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_Transform')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMTransform, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                set3 = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                set4 = [base.GetEntity(constants.NASTRAN, "SET", 5)]

                coord3 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 1)
                coord4 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 2)
                coord5 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 4)
                coord6 = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", 3)

                args = []
                args.append(morph.NewDFMTransformArgs(set4, coord3, coord4))
                args.append(morph.NewDFMTransformArgs(set3, coord5, coord6))

                morphed = [base.GetEntity(constants.NASTRAN, "SET", 7)]
                bounds = [
                    base.GetEntity(constants.NASTRAN, "SET", 8),
                    base.GetEntity(constants.NASTRAN, "SET", 3),
                ]
                param = morph.NewParameterDFMTransform(
                    args, morphed, bounds, False, "Transform Combined"
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewParameterTransform(
    morph_points: object, transform_points: object, name: str
) -> object:
    """

    Function for the creation of a transform morph parameter for morph points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    transform_points : object
            A list of 6 points to get transformation coordinates or 2 coordinates.

    name : str, optional
            The desired name of the parameter.
            (Default: 'Transform')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mopnts = []
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 77))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 78))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 81))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 82))

                gepnts = []
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 1))
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 2))
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 3))
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 4))
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 5))
                gepnts.append(base.GetEntity(constants.NASTRAN, "POINT", 6))

                param = morph.NewParameterTransform(mopnts, gepnts)


    """


def NewParameterTranslate(
    morph_points: object, dx: float, dy: float, dz: float, coord: object, name: str
) -> object:
    """

    Function for the creation of a tranlsate morph parameter for morph points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    coord : object, optional
            A coordinate system that the displacement vector will be defined.
            If coord is None the global coordinate system will be used.
            (Default: None)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Translate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mopnts = ansa.base.CollectEntities(ansa.constants.NASTRAN, None, "MORPHPOINT")
                param = ansa.morph.NewParameterTranslate(mopnts, 1.0, 0.0, 0.0)

                ansa.morph.MorphParam(param, 100.0)


    """


def NewParameterEdgeFit(morph_edges: object, curves: object, name: str) -> object:
    """

    Function for the creation of an edge fit morph parameter for morph edges.

    Parameters
    ----------
    morph_edges : object
            A list of morph edges.

    curves : object
            A list of curves.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Edge_Fit')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 8))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 18))

                curves = []
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 8))
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 13))

                param = morph.NewParameterEdgeFit(moedges, curves)


    """


def NewParameterExtend(morph_points: object, morph_edges: object, name: str) -> object:
    """
    .. deprecated:: 18.0.0
            Use :py:func:`NewParameterSlideBoxPoints` instead.


    Function for the creation of a parameter that slides box points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    morph_edges : object
            A list of morph edges.

    name : str, optional
            The desired name of the parameter.
            (Default: 'Slide Box Points')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                mopnts = []
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 5))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 6))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 13))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 14))

                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 2))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 4))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 6))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 8))

                param = morph.NewParameterExtend(mopnts, moedges, "Slide Box Points")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 18.0.0. Use :py:func: NewParameterSlideBoxPoints instead.",
        DeprecationWarning,
    )


def NewParameterOffset(morph_faces: object, name: str) -> object:
    """

    Function for the creation of an offset morph parameter for morph faces.

    Parameters
    ----------
    morph_faces : object
            A list of morph faces.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Offset')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on success, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mofaces = base.CollectEntities(constants.NASTRAN, None, "MORPHFACE")
                param_id = morph.NewParameterOffset(mofaces)


    """


def NewParameterRadiusInner(concentric_edges: object, name: str) -> object:
    """

    Function for the creation of a radius inner morph parameter for cylindrical morph boxes.

    Parameters
    ----------
    concentric_edges : object
            A list of concentric edges.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Radius_Inner')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                concentric_edge = []
                concentric_edge.append(base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 14))
                concentric_edge.append(base.GetEntity(constants.NASTRAN, "CONCENTRIC_EDGE", 15))

                param_id = morph.NewParameterRadiusInner(concentric_edge, "Radius inner")


    """


def NewParameterRadiusOuter(morph_faces: object, name: str) -> object:
    """

    Function for the creation of a radius outer morph parameter for cylindrical morph boxes.

    Parameters
    ----------
    morph_faces : object
            A list of circular faces of cylindrical morph boxes.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Radius_Outer')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mofaces = []
                mofaces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 1))
                mofaces.append(base.GetEntity(constants.NASTRAN, "MORPHFACE", 2))

                param_id = morph.NewParameterRadiusOuter(mofaces)


    """


def NewParameterRotate(
    morph_points: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
    coord: object,
    name: str,
) -> object:
    """

    Function for the creation of a rotate morph parameter for morph points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    coord : object, optional
            A coordinate system that the rotation axis will be defined.
            If coord is None the global coordinate system will be used.
            (Default: None)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Rotate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                morphes = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX")
                mopnts = morph.MorphCornerPoints(morphes)
                param_id = morph.NewParameterRotate(mopnts, 0, 0, 0, 0, 0, 1)


    """


def NewParameterUserTangent(morph_tang: object, name: str) -> object:
    """

    Function for the creation of a user tanget morph parameter for morph edges.

    Parameters
    ----------
    morph_tang : object
            A list of morph tangents.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'UserTangent')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                mtang = base.CollectEntities(constants.NASTRAN, None, "MORPHTANG")
                param = morph.NewParameterUserTangent(mtang)


    """


def NewParameterScale(
    morph_points: object, x: float, y: float, z: float, name: str
) -> object:
    """

    Function for the creation of a scale morph parameter for morph points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Scale')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                morphes = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX")
                mopnts = morph.MorphCornerPoints(morphes)
                param = morph.NewParameterScale(mopnts, 0, 0, 0)


    """


def NewParameterSlideFeatureCurve(
    feature: object, curves: object, follow_orientation: bool, name: str
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for the creation of a slide feature on curve parameter.

    Parameters
    ----------
    feature : object
            A list of elements that describes the feature.

    curves : object
            An ANSA curve on which the feature will slide on.

    follow_orientation : bool, optional
            A flag to determine if the feature will follow the curve's orientation.
            (Default: True)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'SF_Curve')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DCFeatureSlide, morph.DCFeatureCopy

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                param = morph.NewParameterSlideFeatureCurve(feature, curve)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def NewParameterSlideFeatureRotate(
    feature: object,
    x: float,
    y: float,
    z: float,
    dx: float,
    dy: float,
    dz: float,
    coord: object,
    name: str,
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for the creation of a slide feature rotate parameter.

    Parameters
    ----------
    feature : object
            A list of elements that describes the feature.

    x : float
            The x component of the origin's position vector of the rotation axis.

    y : float
            The y component of the origin's position vector of the rotation axis.

    z : float
            The z component of the origin's position vector of the rotation axis.

    dx : float
            The x component of the direction vector of the rotation axis.

    dy : float
            The y component of the direction vector of the rotation axis.

    dz : float
            The z component of the direction vector of the rotation axis.

    coord : object, optional
            A coordinate system that the displacement vector will be defined.
            If coord is None the global coordinate system will be used.
            (Default: None)

    name : str, optional
            The desired name for the new parameter.
            (Default: 'SF_Rotate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DCFeatureSlide, morph.DCFeatureCopy

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                id = morph.NewParameterSlideFeatureRotate(feature, 1439, -668, 12, 0, 0, 1)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def NewParameterSlideFeatureScale(
    feature: object, x: float, y: float, z: float, name: str
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for the creation of a slide feature scale parameter.

    Parameters
    ----------
    feature : object
            A list of elements that describes the feature.

    x : float
            The x component of the scale origin.

    y : float
            The y component of the scale origin.

    z : float
            The z component of the scale origin.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'SF_Scale')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DCFeatureSlide, morph.DCFeatureCopy

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                feature = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                param = morph.NewParameterSlideFeatureScale(feature, 1439, -668, 12)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def NewParameterSlideFeatureTranslate(
    feature: object, dx: float, dy: float, dz: float, coord: object, name: str
) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCFeatureSlide` instead.


    Function for the creation of a slide feature translate parameter.

    Parameters
    ----------
    feature : object
            A list of elements that describes the feature.

    dx : float
            The x component of the displacement vector.

    dy : float
            The y component of the displacement vector.

    dz : float
            The z component of the displacement vector.

    coord : object, optional
            A coordinate system that the displacement vector will be defined.
            If coord is None the global coordinate system will be used.
            (Default: 'None')

    name : str, optional
            The desired name for the new parameter.
            (Default: 'SF_Translate')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DCFeatureSlide, morph.DCFeatureCopy

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                feature = base.CollectEntities(constants.NASTRAN, set, "SHELL")
                param = morph.NewParameterSlideFeatureTranslate(feature, -1, 0, 0)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCFeatureSlide instead.",
        DeprecationWarning,
    )


def NewParameterTailoredBlank(
    entities: object,
    properties: object,
    lengths: object,
    origin: object,
    normal: object,
    trajectory: object,
    movement: int,
    cut_mesh: bool,
    reconstruct: bool,
    zones: int,
    name: str,
) -> object:
    """

    Function for the creation of a 'Tailored Blank' parameter.

    Parameters
    ----------
    entities : object
            A list of shells.

    properties : object
            A list of properties that will be applied on elements.

    lengths : object
            A list of doubles that specifies the application length for each property.

    origin : object
            A list of three doubles that specifies the position vector of the
            origin of the separation plane.

    normal : object
            A list of three doubles that specifies the direction vector of the
            normal of the separation plane.

    trajectory : object, optional
            A list of entities that will be used as the trajectory on which
            separation plane will move.
            (Default: None)

    movement : int, optional
            A variable that controls the type of movement of the seperation plane.
            Possible values are:
            0 for "Follow trajectory"
            1 for "Sweep on trajectory"
            2 for "Glide on trajectory"
            (Default: 0)

    cut_mesh : bool, optional
            An option that controls if plane cut will take place at each
            property change.
            (Default: False)

    reconstruct : bool, optional
            An option to determine if reconstruction of the affected elements
            will take place after the application of cut.
            This option is meaningful only if "cut_mesh" is set to True.
            (Default: False)

    zones : int, optional
            An option to determine the number of zones that will be reconstructed
            around cut area.
            This option is meaningful only if "reconstruct" is set to True.
            (Default: 0)

    name : str, optional
            The desired name for the created parameter.
            If not provided ANSA will automatically decide a name for the newly
            created parameter.

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                entities = base.GetEntity(constants.NASTRAN, "SET", 1)

                props = []
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 1))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 2))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 3))
                props.append(base.GetEntity(constants.NASTRAN, "PSHELL", 4))

                lens = []
                lens.append(1e308)
                lens.append(-1e308)
                lens.append(200)
                lens.append(-300)

                origin = (1467, -759, 597)
                normal = (0, 0, 1)

                trajectory = base.GetEntity(constants.NASTRAN, "SET", 2)
                name = "Tailored blank"

                param_id = morph.NewParameterTailoredBlank(
                    entities, props, lens, origin, normal, trajectory, 2, True, True, 10, name
                )


    """


def NewMorphAlignArgs(
    entities: object,
    target_entities: object,
    distance: float,
    offset: float,
    user_direction: object,
    align_to_midplane: bool,
    align_on_geometry: bool,
) -> object:
    """

    Function for the creation of an object to be used in creating an Align parameter.

    Parameters
    ----------
    entities : object
            A list with morph points to align.

    target_entities : object
            A list with entities where morph points will be aligned.
            Can have either 3 points to define a plane or anything else.

    distance : float, optional
            The alignment distance.

    offset : float, optional
            Any offset value.

    user_direction : object, optional
            A list with 3 doubles to define a used defined vector.

    align_to_midplane : bool, optional
            Boolean to define if it will align to mid plane.

    align_on_geometry : bool, optional
            Boolean to define if it will align to geometry.

    Returns
    -------
    object
            Returns a list containing references to the newly created objects on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set2 = []
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 87))
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 91))
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 95))
                set2.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 99))

                set1 = []
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 77))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 78))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 81))
                set1.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 82))

                set2 = base.GetEntity(constants.NASTRAN, "SET", 6)
                args1 = [
                    morph.NewMorphAlignArgs(
                        entities=set1, target_entities=set2, distance=1000.0, offset=0
                    )
                ]
                # user_direction=(-.01,0.75,0.65), align_to_midplane=True, align_on_geometry=True)]
                morph.MorphParamCreate("Align_param", "MorphAlign", args1)


    """


def DFMGetContents(parameter: object, category: str) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    A function that returns the entities that participate in the DFM parameter.

    Parameters
    ----------
    parameter : object
            The DFM Parameter.

    category : str, optional
            Option to define which entities should be returned:
            - "__CONTROL__" will return the control entities.
            - "__MORPHED__" will return the morphed entities.
            - "__BOUNDS__" will return the bounds.
            - "__CONSTRAINTS__" will return the constraints.

    Returns
    -------
    object
            Returns a list with the ANSA entities that participate in the DFM parameter.

    See Also
    --------
    morph.DFM, morph.DFMSetContents

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 1)

                all = morph.DFMGetContents(param)
                control = morph.DFMGetContents(param, "__CONTROL__")
                morphed = morph.DFMGetContents(param, "__MORPHED__")
                bounds = morph.DFMGetContents(param, "__BOUNDS__")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def DFMRecalculateBounds(parameter: object) -> bool:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function that auto recalculates and updates the bounds of a DFM parameter.

    Parameters
    ----------
    parameter : object
            The DFM parameter.

    Returns
    -------
    bool
            Returns True on success, or False otherwise.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 1)
                morph.DFMRecalculateBounds(param)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def DFMSetContents(
    parameter: object, category: str, entities: object, recalculate_bounds: bool
) -> bool:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function to set the entities that participate in the defined DFM parameter.

    Parameters
    ----------
    parameter : object
            The DFM Parameter.

    category : str
            An argument to define which elements will be replaced:
            -"__MORPHED__" will replace the morphed entities.
            -"__BOUNDS__" will replace the bounds.
            - "__CONSTRAINTS__" will replace the constraints.

    entities : object
            A list with the new entities.

    recalculate_bounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    See Also
    --------
    DFMGetContents, morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                param = base.GetEntity(0, "PARAMETERS", 1)
                set = base.GetEntity(0, "SET", 1)
                elems = base.CollectEntities(0, set, "SHELL")

                morph.DFMSetContents(param, "__MORPHED__", elems)
                morph.MorphParam(param, 100)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def MorphParamSetSlideContents(parameter: object, feature: object) -> bool:
    """

    Function to set entities in Slide Feature parameter.

    Parameters
    ----------
    parameter : object
            The Slide Feature parameter.

    feature : object
            A list with all the slide entities.

    Returns
    -------
    bool
            Returns True on success, False otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph


            def main():
                param = base.GetEntity(0, "PARAMETERS", 1)
                set = base.GetEntity(0, "SET", 1)
                elems = base.CollectEntities(0, set, "SHELL")

                morph.MorphParamSetSlideContents(param, elems)


    """


def BoxesByWireframe3D(
    curves: object, box_type: str, max_surf_len: float, max_vol_len: float
) -> object:
    """

    Function that generates Ortho Morphing, Hexa Block or Size boxes out of a wireframe of 3D Curves.

    Parameters
    ----------
    curves : object
            A list of 3D Curves. (ANSA Entities, type = "CURVE")

    box_type : str, optional
            Keyword in order to specify the type of the boxes to be generated.
            If no keyword or false keyword is specified, the default box type is the
            morphing box.
            - "Morph" - for morphing boxes.
            - "Hexa_Block" - for hexa block boxes.
            - "Size_Box" - for size boxes.

    max_surf_len : float, optional
            Maximum surface length. Used optionally only in the case of size boxes.
            (Default: 1)

    max_vol_len : float, optional
            Maximum volume length. Used optionally only in the case of size boxes.
            (Default: 1)

    Returns
    -------
    object
            Returns a list with the created boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph


            def main():
                entities = base.CollectEntities(0, None, "CURVE")
                max_surf_len = 2.0
                max_vol_len = 2.0

                # from the same wireframe of 3D curves, produce the morphing, hexa_block and size_boxes with different attributes.
                morph_boxes = morph.BoxesByWireframe3D(entities)
                hexa_boxes = morph.BoxesByWireframe3D(entities, "Hexa_Block")
                size_boxes = morph.BoxesByWireframe3D(entities, "Size_Box", max_surf_len)
                size_boxes_2 = morph.BoxesByWireframe3D(
                    entities, "Size_Box", max_surf_len, max_vol_len
                )


    """


def MorphAdapt(
    entities: object,
    fe_or_geom: bool,
    bounds: object,
    transform: bool,
    split: bool,
    angle: float,
    part: object,
) -> object:
    """

    A function to create a morphing box that will adapt on a selected FE or geometry area.
    There is also the option to adapt the bounding morphing faces of the box to the preselected bounds.
    The user can select 0, 1 or 2 bounds. A bound can be a morphing face, a cross-section or a working plane.
    The resulting box can be expanded in order to include all the selected entities (transform = True)
    and also can be splitted to multiple boxes (split = True) based on an angle criterion (angle: angle
    between two successive cutting planes that pass from the middle line of the selected area, in degrees).

    Parameters
    ----------
    entities : object
            A list that contain shells or solids (type : "SHELL", "SOLID") and
            geometric faces (type: "FACE"). The box will be adapted on these
            entities based on the boolean value of the next argument (fe_or_geom).

    fe_or_geom : bool
            True: The Box will adapt on shells and solids.
            False: The Box will adapt on faces.

    bounds : object, optional
            A list with zero, one or two objects, which are the bounds of the morphing box.
            These can be Morphing Faces (type: "MORPHFACE"), Cross-Sections (type: "CROSS_SECTION")
            or Working Planes(type: "WPLANE").
            The user can select two different type of bounds.
            Default Value: empty list = {}

    transform : bool, optional
            An option in order to expand the box in such a way that no red hatches
            are emerging in the 4 side morphing faces.
            (Default: False)

    split : bool, optional
            An option to split the morphing box in multiple boxes based on an angle criterion
            between successive cutting planes in the principal axis of the selection volume.
            (Default: False)

    angle : float, optional
            The angle on which the splitting of the box can be performed.
            The angle varies between 0-90 degrees.
            -90 degrees means that no split will occur (there is a tolerance of 90
             degrees turning angle).
            -0 degrees means that there is no tolerance at all and the box will split to
             as many boxes as possible.
            (Default: 90.0)

    part : object, optional
            The part where the resulting box will belong to.
            (Default: None)

    Returns
    -------
    object
            Returns a list with the resulting morphing boxes that were created.
            In all other cases, except from the enabled split option, the list will have only one member.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                entities = base.CollectEntities(constants.NASTRAN, None, "SHELL")
                bounds = base.CollectEntities(constants.NASTRAN, None, "CROSS_SECTION")

                fe_or_geom = True
                transform = False
                split = False
                angle = 90.0

                morphes = morph.MorphAdapt(entities, fe_or_geom, bounds, transform, split, angle)


    """


def AlignBoxPoints(
    entities: object,
    target_entities: object,
    distance: float,
    offset: float,
    user_direction: object,
    align_to_midplane: bool,
    align_on_geometry: bool,
) -> int:
    """

    Script function to align box points on target entities.

    Parameters
    ----------
    entities : object
            A list with box points to align.

    target_entities : object
            A list with entities where box points will be aligned. Can have either
            3 points to define a plane or anything else.

    distance : float, optional
            Maximum distance where the source nodes will be able to move for alignment
            If it is not defined, it will always calculate a projection, no matter how far.

    offset : float, optional
            Any offset value.

    user_direction : object, optional
            A list with 3 doubles to define a used defined vector.

    align_to_midplane : bool, optional
            Boolean to define if it will align to mid plane.

    align_on_geometry : bool, optional
            Boolean to define if it will align to geometry.

    Returns
    -------
    int
            Returns 1 in case of successful alignment, 0 in case of failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph


            def alignOnPointsPlane():
                box_points = []
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 26))
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 30))
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 34))
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 38))

                target_ents = []
                target_ents.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 6))
                target_ents.append(base.GetEntity(base.CurrentDeck(), "GRID", 210))
                target_ents.append(base.GetEntity(base.CurrentDeck(), "GRID", 256))

                morph.AlignBoxPoints(
                    entities=box_points, target_entities=target_ents, distance=10000, offset=100
                )


            def alignOnGeometricFace():
                box_points = []
                box_points.append(base.GetEntity(base.CurrentDeck(), "MORPHPOINT", 33))
                box_points.append(base.GetEntity(base.CurrentDeck(), "MORPHPOINT", 34))

                target_ents = []
                target_ents.append(base.GetEntity(base.CurrentDeck(), "FACE", 1))
                morph.AlignBoxPoints(
                    entities=box_points,
                    target_entities=target_ents,
                    distance=10000,
                    offset=0,
                    align_to_midplane=True,
                    align_on_geometry=True,
                )


            def alignOnBoxEdge():
                box_points = []
                box_points.append(base.GetEntity(base.CurrentDeck(), "SIZEBOXPOINT", 33))
                box_points.append(base.GetEntity(base.CurrentDeck(), "SIZEBOXPOINT", 34))

                target_ents = []
                target_ents.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_EDGE", 31))
                morph.AlignBoxPoints(
                    entities=box_points,
                    target_entities=target_ents,
                    distance=10000,
                    offset=0,
                    align_to_midplane=True,
                    align_on_geometry=True,
                )


            def alignOnShellsUserVector():
                box_points = []
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 58))
                box_points.append(base.GetEntity(base.CurrentDeck(), "HEXA_BOX_POINT", 62))

                target_ents = []
                target_ents.append(base.GetEntity(base.CurrentDeck(), "SHELL", 1))
                target_ents.append(base.GetEntity(base.CurrentDeck(), "SHELL", 2))
                target_ents.append(base.GetEntity(base.CurrentDeck(), "SHELL", 3))

                user_vec = []
                user_vec.append(0)
                user_vec.append(-1.89716e-016)
                user_vec.append(-1)

                morph.AlignBoxPoints(
                    entities=box_points,
                    target_entities=target_ents,
                    distance=10000,
                    offset=0,
                    user_direction=user_vec,
                    align_to_midplane=True,
                    align_on_geometry=True,
                )


    """


def CreateDvgridsFromParameter(
    morph_parameter: object, design_variable: object, distance: float, tolerance: float
) -> object:
    """

    Script function for creating DVGRID's from a morphing parameter movement.

    Parameters
    ----------
    morph_parameter : object
            The parameter element.

    design_variable : object, optional
            The DESVAR element. If set to None. a new one will be created.

    distance : float, optional
            The distance to move the morph parameter.
            (Default: 1)

    tolerance : float, optional
            is the tolerance to accept a movement as valid and record a dvgrid for it.
            (Default: 0)

    Returns
    -------
    object
            Returns the input or the created DESVAR object on success, None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 11)
                desvar = base.GetEntity(constants.NASTRAN, "DESVAR", 1)
                desvar = morph.CreateDvgridsFromParameter(
                    morph_parameter=param, design_variable=desvar, distance=1.0, tolerance=0.05
                )
                ents = base.ReferenceEntities(desvar)
                for ent in ents:
                    print(ent)


            def main():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", 11)
                desvar = morph.CreateDvgridsFromParameter(param)
                ents = base.ReferenceEntities(desvar)
                for ent in ents:
                    print(ent)


    """


def MorphLinks(morph_box_links: object, all_depths: bool) -> object:
    """

    A function for getting the link information of morphing boxes

    Parameters
    ----------
    morph_box_links : object
            A list of morphing boxes.

    all_depths : bool, optional
            Set to "True" to get link information for all linked morphes
            with the same "Parent".
            Set to "False" to get link information for only one level
            "Parent -> children" or "Child->Parent"
            (Default: "False")

    Returns
    -------
    object
            Returns a dictionary with key the given morphing box and data a list with linked morphing boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import morph
            from ansa import constants
            from ansa import base


            def main():
                morphes = []
                morphes.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 12))
                morphes.append(base.GetEntity(constants.NASTRAN, "MORPHBOX", 16))
                dict = morph.MorphLinks(morphes)
                print(dict)

                dict = morph.MorphLinks(morphes, True)
                print(dict)


    """


def NewParameterSlideBoxPoints(
    morph_points: object, morph_edges: object, name: str
) -> object:
    """

    Function for the creation of a parameter that slides box points.

    Parameters
    ----------
    morph_points : object
            A list of morph points.

    morph_edges : object
            A list of morph edges.

    name : str, optional
            The desired name of the parameter.
            (Default: 'Slide Box Points')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def run():
                mopnts = []
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 5))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 6))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 13))
                mopnts.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 14))

                moedges = []
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 2))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 4))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 6))
                moedges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", 8))

                param = morph.NewParameterSlideBoxPoints(mopnts, moedges, "Slide Box Points")


    """


def GetDoeStudyCurrentExperimentDir() -> object:
    """

    A function that returns the full path of the current experiment's directory.

    Returns
    -------
    object
            Returns a string that corresponds to the experiment's path on success,
            or None on failure (if DOE is not running when function is called).

    See Also
    --------
    PerformDoeStudy, GetDoeStudyExperiments, GetDoeStudyExperimentsForParams

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                print(
                    "DOE Study current experiment directory = ",
                    morph.GetDoeStudyCurrentExperimentDir(),
                )


    """


def GetDoeStudyExperiments(
    design_variables: object,
    algorithm: str,
    level: object,
    experiments_number: int,
    seed: int,
    taguchi_array: str,
    dv_taguchi_columns: object,
    reject_duplicates: bool,
    comb_file: str,
) -> object:
    """

    Function to get the experiments of the input design variables.

    Parameters
    ----------
    design_variables : object
            list or objects of design variables and/or optimization tasks
            (in case of optimization task, design variables are derived
            from them)

    algorithm : str
            algorithm used to generate the experiments.
            Supported algorithms are:
            - "Full Factorial",
            - "Uniform Latin Hypercube",
            - "Optimal Latin Hypercube (ESE)",
            - "Symmetric Optimal Latin Hypercube",
            - "Random",
            - "Taguchi Orthogonal Arrays",
            - "Modified Extensible Lattice Sequence"
            - "Linear".

    level : object, optional
            it may be a single integer value used for all design variables
            ("Full Factorial" or "Taguchi Orthogonal Arrays" algorithms) or
            a dictionary of design variable and level value (for "Full Factorial"
            every design variable may have its own level value). Default value
            is 2.

    experiments_number : int, optional
            the number of the generated experiments (used in "Uniform Latin Hypercube", "Random" and "Linear" algorithms).

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

    dv_taguchi_columns : object, optional
            dictionary with design variable and the correspondent column
            (column > 0) of the Taguchi array. By default, the first columns
            of the Taguchi array are used.

    reject_duplicates : bool, optional
            reject duplicate experiments in Taguchi algorithm

    comb_file : str, optional
            the generated combinations file that contains all
            the experiments of the input design variables

    Returns
    -------
    object
            Returns a list of lists (every list corresponds to a single experiment).

    See Also
    --------
    PerformDoeStudy, GetDoeStudyCurrentExperimentDir, GetDoeStudyExperimentsForParams

    Examples
    --------
    ::

            import os
            import ansa


            def main():
                dvs = []
                dv1 = ansa.base.GetEntity(ansa.constants.NASTRAN, "DESIGN_VARIABLE", 1)
                dv2 = ansa.base.GetEntity(ansa.constants.NASTRAN, "DESIGN_VARIABLE", 2)
                dv3 = ansa.base.GetEntity(ansa.constants.NASTRAN, "DESIGN_VARIABLE", 3)
                dv4 = ansa.base.GetEntity(ansa.constants.NASTRAN, "DESIGN_VARIABLE", 4)

                dvs.append(dv1)
                dvs.append(dv2)
                dvs.append(dv3)
                dvs.append(dv4)

                designs1 = ansa.morph.GetDoeStudyExperiments(
                    dvs, "random", experiments_number=3, seed=345
                )
                print("Random algorithm: ", designs1)

                designs2 = ansa.morph.GetDoeStudyExperiments(
                    dvs, "uniform latin hypercube", experiments_number=3, seed=345
                )
                print("Uniform Latin Hypercube algorithm: ", designs2)

                designs3 = ansa.morph.GetDoeStudyExperiments(
                    dvs,
                    "Taguchi Orthogonal Arrays",
                    level=3,
                    taguchi_array="L108",
                    reject_duplicates=True,
                    comb_file="/home/username/comb1.txt",
                )
                print("Taguchi Orthogonal Arrays: ", designs3)

                designs4 = ansa.morph.GetDoeStudyExperiments(dvs, "Linear", experiments_number=4)
                print("Linear: ", designs4)

                designs5 = ansa.morph.GetDoeStudyExperiments(
                    dvs, "Full Factorial", level=3, comb_file="/home/username/comb1.txt"
                )
                print("Full Factorial: ", designs5)

                designs6 = ansa.morph.GetDoeStudyExperiments(
                    dvs, "Full Factorial", level=3, comb_file="/home/username/comb1.txt"
                )
                print("Full Factorial - single level value: ", designs5)

                level_dict = {dv1: 2, dv2: 3, dv3: 4, dv4: 7}
                designs7 = ansa.morph.GetDoeStudyExperiments(
                    dvs, "Full Factorial", level=level_dict
                )
                print("Full Factorial different level for every design variable: ", designs7)

                optTask = ansa.base.GetEntity(ansa.constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                designs8 = ansa.morph.GetDoeStudyExperiments(
                    optTask, "uniform latin hypercube", experiments_number=34, seed=567
                )
                print("uniform latin hypercube (optimization task input): ", designs8)


            if __name__ == "__main__":
                main()


    """


def MorphDistorted():
    """

    Script function to check all morphing boxes if they are distorted.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                m1 = morph.MorphDistorted()


    """


def NewDFMSweepGlideArgs(
    entities: object, path: object, movement: str, rigid_deformable: str
) -> object:
    """

    Function for the creation of an object that will be used by the NewParameterDFMSweepGlide function.
    This is an auxiliary function.

    Parameters
    ----------
    entities : object
            A list of entities that will be moved along the path in a sweep or glide manner.

    path : object
            A list of entities that will be used to define the sweep/glide path

    movement : str, optional
            String value of movement type.
            Possible values are:
            "Sweep" [Default]
            "Glide"

    rigid_deformable : str, optional
            String value to control if the entities should move as a
            rigid or deformable body.
            Possible values:
            "Deformable body" [Default]
            "Rigid body"

    Returns
    -------
    object
            Returns a reference to the newly created object on sucess, or None on failure.

    See Also
    --------
    NewParameterDFMSweepGlide

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base, morph


            def run():
                shell1 = base.CollectEntities(0, base.GetEntity(0, "SET", 1), "SHELL")
                shell2 = base.CollectEntities(0, base.GetEntity(0, "SET", 2), "SHELL")
                curve1 = base.GetEntity(0, "CURVE", 1)
                curve2 = base.GetEntity(0, "CURVE", 2)

                args = []
                args.append(morph.NewDFMSweepGlideArgs(shell1, curve1, "Glide", "Rigid body"))
                args.append(morph.NewDFMSweepGlideArgs(shell2, curve2))
                morphed = base.CollectEntities(0, base.GetEntity(0, "SET", 3), "SHELL")

                param = morph.NewParameterDFMSweepGlide(args, morphed)
                morph.MorphParam(param, 100)


    """


def NewParameterDFMSweepGlide(
    args: object, entities: object, bounds: object, autobounds: bool, name: str
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of a dfm sweep-glide parameter.

    Parameters
    ----------
    args : object
            A list of objects created by NewDFMSweepGlideArgs.

    entities : object, optional
            A list of entities that will be morphed.
            (Default: None)

    bounds : object, optional
            A list of entities that will retain their position during the morphing action.
            These entities will also affect the deformation of the entities.
            (Default: None)

    autobounds : bool, optional
            An option to enable the automatic bound determination.
            (Default: True)

    name : str, optional
            The desired name of the parameter.
            (Default: 'DFM_SweepGlide')

    Returns
    -------
    object
            Returns a reference to the newly created parameter object on sucess, or None on failure.

    See Also
    --------
    morph.DFMSweepGlide, morph.DFM, NewDFMSweepGlideArgs

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base, morph


            def run():
                shell1 = base.CollectEntities(0, base.GetEntity(0, "SET", 1), "SHELL")
                shell2 = base.CollectEntities(0, base.GetEntity(0, "SET", 2), "SHELL")
                curve1 = base.GetEntity(0, "CURVE", 1)
                curve2 = base.GetEntity(0, "CURVE", 2)

                args = []
                args.append(morph.NewDFMSweepGlideArgs(shell1, curve1, "Glide", "Rigid body"))
                args.append(morph.NewDFMSweepGlideArgs(shell2, curve2))
                morphed = base.CollectEntities(0, base.GetEntity(0, "SET", 3), "SHELL")

                param = morph.NewParameterDFMSweepGlide(args, morphed)
                morph.MorphParam(param, 100)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def MorphIntersections(morphes: object) -> object:
    """

    Script function to collect interesecting entities

    Parameters
    ----------
    morphes : object
            morphes is a list of morphes to check

    Returns
    -------
    object
            Return a list with the intersecting elements

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                m1 = base.CollectEntities(constants.NASTRAN, None, "MORPHBOX", filter_visible=True)
                shells = morph.MorphIntersections(m1)


    """


def DeformMorphPoints(morph_points: object, dx: object, dy: object, dz: object) -> int:
    """

    Function that deforms independently a list of morph points.

    Parameters
    ----------
    morph_points : object
            a list of morph points ('MORPHPOINT')

    dx : object
            a list with the x component of the deformation vectors

    dy : object
            a list with the y component of the deformation vectors

    dz : object
            a list with the z component of the deformation vectors

    Returns
    -------
    int
            1 on success and 0 on failure

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                morph_points = []
                dx = []
                dy = []
                dz = []

                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 1))
                dx.append(-100)
                dy.append(-100)
                dz.append(100)

                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 2))
                dx.append(100)
                dy.append(-100)
                dz.append(100)

                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 3))
                dx.append(100)
                dy.append(100)
                dz.append(100)

                morph_points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", 4))
                dx.append(-100)
                dy.append(100)
                dz.append(100)

                morph.DeformMorphPoints(morph_points, dx, dy, dz)


    """


def DCFeatureSlideApply(
    entity: object,
    dx: float,
    dy: float,
    dz: float,
    rx: float,
    ry: float,
    rz: float,
    fx: float,
    fy: float,
    fz: float,
):
    """

    The function applies the deformation to the given DC_FEATURE_SLIDE entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_SLIDE entity

    dx : float
            Deformation value in local x-axis.

    dy : float
            Deformation value in local y-axis.

    dz : float
            Deformation value in local z-axis.

    rx : float
            Angle around local x-axis.

    ry : float
            Angle around local y-axis.

    rz : float
            Angle around local z-axis.

    fx : float
            Scale value in local x-axis.

    fy : float
            Scale value in local y-axis.

    fz : float
            Scale value in local z-axis.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideSurfaceApply, DCFeatureSlidePathApply, DCFeatureCopyApply, DCFeatureCopySurfaceApply, DCFeatureCopyPathApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_SLIDE", 1)
                morph.DCFeatureSlideApply(dc_feature, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)


    """


def DCFeatureSlideSurfaceApply(
    entity: object, ds: float, dt: float, rw: float, fs: float, ft: float
):
    """

    The function applies the deformation to the given DC_FEATURE_SLIDE entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_SLIDE entity.

    ds : float
            Deformation value in local s-axis.

    dt : float
            Deformation value in local t-axis.

    rw : float
            Angle around local w-axis.

    fs : float
            Scale value in local s-axis.

    ft : float
            Scale value in local t-axis.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideApply, DCFeatureSlidePathApply, DCFeatureCopyApply, DCFeatureCopySurfaceApply, DCFeatureCopyPathApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_SLIDE", 1)
                morph.DCFeatureSlideSurfaceApply(dc_feature, 10.0, 0.0, 0.0, 1.0, 1.0)


    """


def DCFeatureSlidePathApply(entity: object, dist: float):
    """

    The function applies the deformation to the given DC_FEATURE_SLIDE entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_SLIDE entity.

    dist : float
            Distance on defined path.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideApply, DCFeatureSlideSurfaceApply, DCFeatureCopyApply, DCFeatureCopySurfaceApply, DCFeatureCopyPathApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_SLIDE", 1)
                morph.DCFeatureSlidePathApply(dc_feature, 10.0)


    """


def DCFeatureCopyApply(
    entity: object,
    dx: float,
    dy: float,
    dz: float,
    rx: float,
    ry: float,
    rz: float,
    fx: float,
    fy: float,
    fz: float,
    steps: int,
):
    """

    The function applies the deformation to the given DC_FEATURE_COPY entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_COPY entity.

    dx : float
            Deformation value in local x-axis.

    dy : float
            Deformation value in local y-axis.

    dz : float
            Deformation value in local z-axis.

    rx : float
            Angle around local x-axis.

    ry : float
            Angle around local y-axis.

    rz : float
            Angle around local z-axis.

    fx : float
            Scale value in local x-axis.

    fy : float
            Scale value in local y-axis.

    fz : float
            Scale value in local z-axis.

    steps : int
            The number of new features that would be generated.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideApply, DCFeatureSlideSurfaceApply, DCFeatureSlidePathApply, DCFeatureCopySurfaceApply, DCFeatureCopyPathApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_COPY", 1)
                morph.DCFeatureCopyApply(
                    dc_feature, 30.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2
                )


    """


def DCFeatureCopySurfaceApply(
    entity: object, ds: float, dt: float, rw: float, fs: float, ft: float, steps: int
):
    """

    The function applies the deformation to the given DC_FEATURE_COPY entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_COPY entity.

    ds : float
            Deformation value in local s-axis.

    dt : float
            Deformation value in local t-axis.

    rw : float
            Angle around local w-axis.

    fs : float
            Scale value in local s-axis.

    ft : float
            Scale value in local t-axis.

    steps : int
            The number of new features that would be generated.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideApply, DCFeatureSlideSurfaceApply, DCFeatureSlidePathApply, DCFeatureCopyApply, DCFeatureCopyPathApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_COPY", 1)
                morph.DCFeatureCopySurfaceApply(dc_feature, 30.0, 0.0, 0.0, 1.0, 1.0, 2)


    """


def DCFeatureCopyPathApply(entity: object, dist: float, steps: int):
    """

    The function applies the deformation to the given DC_FEATURE_COPY entity.

    Parameters
    ----------
    entity : object
            The DC_FEATURE_COPY entity.

    dist : float
            Distance on defined path.

    steps : int
            The number of new features that would be generated.

    See Also
    --------
    DCFeatureSlide, DCFeatureCopy, DCFeatureSlideApply, DCFeatureSlideSurfaceApply, DCFeatureSlidePathApply, DCFeatureCopyApply, DCFeatureCopySurfaceApply

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dc_feature = base.GetEntity(ansa.constants.NASTRAN, "DC_FEATURE_COPY", 1)
                morph.DCFeatureCopyPathApply(dc_feature, 30.0, 2)


    """


def CheckForDuplicateBoxes(tolerance: float, check_on: str) -> object:
    """

    Function for the check of boxes duplicates. Given the tolerance, similar boxes are identified.

    Parameters
    ----------
    tolerance : float, optional
            A tolerance to define maximum value of boxes differences.
            Default value depends on node tolerance.

    check_on : str, optional
            Can have values 'all' or 'visible', for boxes to run the check.
            The default value runs a check for visible entities.

    Returns
    -------
    object
            Returns a list of duplicate box groups. Each group is implemented as a list of similar box entities.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                list1 = morph.CheckForDuplicateBoxes()
                list2 = morph.CheckForDuplicateBoxes(tolerance=0.8)
                list3 = morph.CheckForDuplicateBoxes(check_on="all")
                list4 = morph.CheckForDuplicateBoxes(0.25, "visible")
                list5 = morph.CheckForDuplicateBoxes(tolerance=0.5, check_on="all")


    """


def MorphConstraintFlange(
    entities: object,
    contacts: object,
    morphed: object,
    bounds: object,
    autobounds: bool,
    align: str,
    offset: float,
) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`ConstraintFlanges` instead.


    A function for creating a flange morph constraint.

    The generated constraint may be included in the morphed entities of a DFM, and will force
    the constraint's 'entities' to adjust on 'contacts' surface when the DFM
    executes. To alleviate and/or confine the effects of the constraint, 'morphed' and 'bounds'
    entities may be provided to the constraint, essentially defining a transition region.

    In most aspects, the constraint operates like an automatic DFM, subsequent to the main DFM.

    Parameters
    ----------
    entities : object
            A list of the entities to define flange area.

    contacts : object
            A list of the entities to define contact area.

    morphed : object
            A list of the entities to be morphed by constraint.

    bounds : object
            A list of the entities defining bounds of constraint's fitting process.

    autobounds : bool, optional
            An option to enable the automatic bounds determination.
            (Default: False)

    align : str, optional
            An option to preserve the current flange distance or align based on an offet value
            - 'preserve' : Preserve the flange distance from contact area.
            - 'thickness' : Set an offset distance from contact area.
            (Default: 'preserve')

    offset : float, optional
            User defined flange('entities') offset distance from 'contact' area.
            Enabled if 'align' argument set to 'thickness'

    Returns
    -------
    object
            It returns the created morph constraint.

    See Also
    --------
    MorphConstraintPlanar, MorphConstraintRigid, MorphConstraintScaled, MorphConstraintPathFollower, MorphConstraintDirectional, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                ents = []
                ents = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 2)
                contacts = []
                contacts = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 3)
                morphed = []
                morphed = base.CollectEntities(constants.NASTRAN, set, "SHELL")

                set = base.GetEntity(constants.NASTRAN, "SET", 4)
                bounds = []
                bounds = base.CollectEntities(constants.NASTRAN, set, "EDGE")
                # bounds could be an empty list.
                # bounds = []

                cnstr = morph.MorphConstraintFlange(ents, contacts, morphed, bounds)
                # cnstr = morph.MorphConstraintFlange(ents, contacts, morphed, bounds, False, "thickness", 0.)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: ConstraintFlanges instead.",
        DeprecationWarning,
    )


def VideoFromEntities(
    filename: str,
    parameters: object,
    initial_final: object,
    frames: int,
    duration: float,
    lock_view_time: object,
    images_per_sec: int,
):
    """

    Function for video creation using parameters for morph. Video options are provided.

    Parameters
    ----------
    filename : str
            Video will be saved at this path.
            The extension of file name determines the video format.

    parameters : object
            A list of parameters to be used for morphing.
            Could be morph parameters, design variables or an optimization task.

    initial_final : object, optional
            A list of initial and final values.
            Two values for each parameter are required.

    frames : int, optional
            Video frames per second default value at 20fps.

    duration : float, optional
            Video duration default value at 5 sec.

    lock_view_time : object, optional
            A dictionary including lock view names as keys and appearance times as values.

    images_per_sec : int, optional
            how many images should be taken per second for the video creation (increase for quality or decrease for speed), default value 4

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                items = []
                params = []
                items = ansa.taskmanager.GetTaskItemsByType("Design Variables")
                params.append(items[1])
                params.append(ansa.taskmanager.GetTaskItemsByName("DV_1"))
                params.append(base.GetEntity(ansa.base.CurrentDeck(), "PARAMETERS", 1))
                params.append(base.GetEntity(ansa.base.CurrentDeck(), "PARAMETERS", 5))
                params.append(base.GetEntity(ansa.base.CurrentDeck(), "PARAMETERS", 3))

                bounds = [-5, 5, -10, 0, 10, -5, 0, 15, -5, 10]
                lvs_time = {}
                lvs_time["view1"] = 3
                lvs_time["view2"] = 6
                ansa.morph.VideoFromEntities(
                    "/home/username/videos/morph_video.gif",
                    initial_final=bounds,
                    parameters=params,
                    duration=10,
                    frames=25,
                    lock_view_time=lvs_time,
                )

                params = []
                params = ansa.taskmanager.GetTaskItemsByName("OPTIMIZATION_TASK_1")
                ansa.morph.VideoFromEntities("/home/username/videos/morph_video.mpg", params)


    """


def GetDoeStudyCurrentExperimentId() -> int:
    """

    A function that return the active's experiment id

    Returns
    -------
    int
            Returns a integer experiment id

    Examples
    --------
    ::

            import ansa
            from ansa import morph


            def main():
                print("DOE Study current experiment id = ", morph.GetDoeStudyCurrentExperimentId())


    """


def MorphSplitToHexa(
    box_faces: object,
    tangency: str,
    preserve_local_shape: bool,
    fit_new_skin_edges: bool,
    work_on: str,
    ret_ents: bool,
) -> object:
    """

    Takes a MORPHFACE or HEXA_BLOCK_FACE list and splits the boxes that are on the
    specific faces and their opposites to hexas. Works only on pentaboxes or in
    hexaboxes.

    Parameters
    ----------
    box_faces : object
            It sets the faces of the morph that are going to be splitted to hexa boxes.

    tangency : str
            Sets the type of tangency
            'off'          is for no tangency
            'default'      is for default tangency
            'user_tangent' is for user tangency

    preserve_local_shape : bool, optional
            If set to True, it preserves the local shape of the pre-existing moedges
            after the split by inserting more points.
            This option is available only when tangency is set to 'off'.
            If tangency is different than 'off', then this argument value is irrelevant

    fit_new_skin_edges : bool, optional
            If set to True, new skin edges will fit on the underlying model.
            If fit_new_skin_edges will not be set, then the default argument is false.

    work_on : str, optional
            Sets where the projection is going to take place
            'whole_db' fit skin edges will take place the whole database
            'visible'  fit skin edges will take place only on the visible elements
            If work_on is not set then whole_db will be the default argument.
            This option is only available only when fit_skin_edges is set to true.

    ret_ents : bool, optional
            If set to true it returns the new boxes generated from the function as tuple
            or if set to false returns only if the procedure was successful.

    Returns
    -------
    object
            If 'ret_ents' argument is set to true it returns a tuple where its first argument returns true or false
            depending on the success of the procedure and for the second element it returns the new
            and modified morphes.
            If 'ret_ents' argument is set to false it returns only true or false depending on the success of the procedure.

    See Also
    --------
    MorphSplit, MorphSplitProject, MorphSplitToPenta

    Examples
    --------
    ::

            import ansa
            from ansa import base


            def main():
                arg1 = []
                arg1.append(base.GetEntity(ansa.base.CurrentDeck(), "HEXA_BOX_FACE", 130))
                (res, boxes) = ansa.morph.MorphSplitToHexa(
                    box_faces=arg1,
                    tangency="off",
                    preserve_local_shape=False,
                    fit_new_skin_edges=False,
                )
                print(res)
                print(boxes)


            if __name__ == "__main__":
                main()


    """


def NewParameterDFMSymmetry(entity: object) -> object:
    """
    .. deprecated:: 21.0.0
            Use :py:class:`DFM` instead.


    Function for the creation of DFM symmetry parameter

    Parameters
    ----------
    entity : object
            Dfm morph parameter.

    Returns
    -------
    object
            Returns a reference to the newly created dfm morph parameter

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                dfm = base.GetEntity(0, "PARAMETERS", 1)
                sym_dfm = morph.NewParameterDFMSymmetry(dfm)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.0.0. Use :py:class: DFM instead.",
        DeprecationWarning,
    )


def NewDCFeatureSlide(entities: object, coord: object):
    """

    The function creates a new DC_FEATURE_SLIDE entity.

    Parameters
    ----------
    entities : object
            A list of entities that will slide.

    coord : object
            The initial coordinate

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def main():
                coord = base.GetEntity(constants.NASTRAN, "CORD_R", 10010119)
                set = base.GetEntity(constants.NASTRAN, "SET", 1)
                entities = base.CollectEntities(0, set, "SHELL")

                morph.NewDCFeatureSlide(entities, coord)


    """


def DCSymmetry(design_change: object) -> object:
    """
    .. deprecated:: 21.1.0
            Use :py:class:`DCPosition` instead.


    Script function to create a symmetric, related to the default symmetry plane, design change entity from an existing one.

    Parameters
    ----------
    design_change : object
            DESIGN_CHANGE entity (DC_POSITION, DC_CROSS_SECTION, DC_FEATURE_COPY, DC_FEATURE_SLIDE)

    Returns
    -------
    object
            The symmetric DESIGN_CHANGE entity or None if creation fails.

    See Also
    --------
    morph.DCFeatureSlide, morph.DCFeatureCopy

    Examples
    --------
    ::

            def main():
                dcs_ents = []
                dc_sl_copy = base.CollectEntities(constants.NASTRAN, None, "DC_FEATURE_COPY")
                dc_sl_move = base.CollectEntities(constants.NASTRAN, None, "DC_FEATURE_SLIDE")
                dc_pos = base.CollectEntities(constants.NASTRAN, None, "DC_POSITION")
                dc_cs = base.CollectEntities(constants.NASTRAN, None, "DC_CROSS_SECTION")

                for dc_ent in dc_sl_copy:
                    dcs_ents.append(dc_ent)
                for dc_ent in dc_sl_move:
                    dcs_ents.append(dc_ent)
                for dc_ent in dc_pos:
                    dcs_ents.append(dc_ent)
                for dc_ent in dc_cs:
                    dcs_ents.append(dc_ent)

                for dc_ent in dcs_ents:
                    sym_dc = morph.DCSymmetry(dc_ent)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 21.1.0. Use :py:class: DCPosition instead.",
        DeprecationWarning,
    )


def OptimizationTool(
    optimization_task: object,
    load_experiments: str,
    export_file: str,
    dv_file: str,
    doe_algorithm: str,
    number_of_designs: int,
    hide_buttons: bool,
    show_deviation: bool,
    clear_table: bool,
    save_in_dm: bool,
    revert_changes: bool,
    save_ansa_db: bool,
    save_animation: bool,
    working_directory: str,
) -> int:
    """

    Function to open OptimizationTool or for creating DOE experiments.

    Parameters
    ----------
    optimization_task : object, optional
            An Optimization_Task item.

    load_experiments : str, optional
            A filename with the values to be loaded in the window.

    export_file : str, optional
            A filename to save created experiments in the table on confirmation.

    dv_file : str, optional
            A filename to import Design Variables, the format is the same as in Optimization Task - DVFile.

    doe_algorithm : str, optional
            The selected algorithm values can be:
            - 'Full Factorial'
            - 'Uniform Latin Hypercube'
            - 'Optimal Latin Hypercube (ESE)'
            - 'Symmetric Optimal Latin Hypercube'
            - 'Random'
            - 'Taguchi Orthogonal Arrays'
            - 'Modified Extensible Lattice Sequence'
            - 'Linear'

    number_of_designs : int, optional
            The number of designs to generate

    hide_buttons : bool, optional
            Simplified view of the tool, showing only the DOE-Setup page.

    show_deviation : bool, optional
            Shows the deviation from current value in the DOE table.

    clear_table : bool, optional
            Clears the table before applying any generation or importing of experiments.

    save_in_dm : bool, optional
            Flag to set the tool to work with DM, instead of local directory

    revert_changes : bool, optional
            Set this to False, to force calculations in a different Ansa.
            Default value is True

    save_ansa_db : bool, optional
            Set this to False to skip saving a db for each experiment.
            Default value is True

    save_animation : bool, optional
            Set this to False to skip saving an animation for each experiment.
            Default value is True

    working_directory : str, optional
            Define the Working folder for DOEs and Optimization

    Returns
    -------
    int
            Return 0 for success or 1 for failure, the function will wait only if hide_buttons = True.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def noargs():
                morph.OptimizationTool()


            def useTask():
                mainitem = base.GetEntity(constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                morph.OptimizationTool(optimization_task=mainitem)


            def useTaskAndGenerate():
                mainitem = base.GetEntity(constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                morph.OptimizationTool(
                    optimization_task=mainitem, doe_algorithm="Linear", number_of_designs=5
                )


            def useTaskAndGenerateClearFirst():
                mainitem = base.GetEntity(constants.NASTRAN, "OPTIMIZATION_TASK", 1)
                morph.OptimizationTool(
                    optimization_task=mainitem,
                    doe_algorithm="Linear",
                    number_of_designs=5,
                    clear_table=True,
                )


            def loadDVFileOnEmpty():
                morph.OptimizationTool(
                    hide_buttons=True,
                    dv_file="./DVFile.txt",
                    doe_algorithm="Linear",
                    number_of_designs=5,
                    show_deviation=True,
                    export_file="./export_file.txt",
                )


    """


def PMEntityGeometryUpdate(pm_entities: object) -> object:
    """

    Function that will update the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.
    It will identify any modified curves of the cross sections and will recreate the related faces, while trying not to affect the rest.

    Parameters
    ----------
    pm_entities : object
            An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

    Returns
    -------
    object
            Always returns None

    See Also
    --------
    morph.PMEntityGeometryRegenerate, morph.PMEntityGeometryDelete, morph.PMEntityGeometryRelease

    Examples
    --------
    ::

            import ansa
            from ansa import base, morph, constants


            def main():
                pm_feat = base.CollectEntities(constants.NASTRAN, None, "PM_EXTRUDE")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_SWEEP")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_LOFT")

                morph.PMEntityGeometryUpdate(pm_feat)


            if __name__ == "__main__":
                main()


    """


def PMEntityGeometryRegenerate(pm_entities: object) -> object:
    """

    Function that will regenerate the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.
    It will delete all the old faces and will create new ones.

    Parameters
    ----------
    pm_entities : object
            An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

    Returns
    -------
    object
            None

    See Also
    --------
    morph.PMEntityGeometryUpdate, morph.PMEntityGeometryRelease, morph.PMEntityGeometryDelete

    Examples
    --------
    ::

            import ansa
            from ansa import base, morph, constants


            def main():
                pm_feat = base.CollectEntities(constants.NASTRAN, None, "PM_EXTRUDE")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_SWEEP")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_LOFT")

                morph.PMEntityGeometryRegenerate(pm_feat)


            if __name__ == "__main__":
                main()


    """


def PMEntityGeometryDelete(pm_entities: object) -> object:
    """

    Function that will delete the geometry managed by PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

    Parameters
    ----------
    pm_entities : object
            An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

    Returns
    -------
    object
            None

    See Also
    --------
    morph.PMEntityGeometryUpdate, morph.PMEntityGeometryRegenerate, morph.PMEntityGeometryRelease

    Examples
    --------
    ::

            import ansa
            from ansa import base, morph, constants


            def main():
                pm_feat = base.CollectEntities(constants.NASTRAN, None, "PM_EXTRUDE")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_SWEEP")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_LOFT")

                morph.PMEntityGeometryDelete(pm_feat)


            if __name__ == "__main__":
                main()


    """


def PMEntityGeometryRelease(pm_entities) -> object:
    """

    Function that removes the association of the created faces with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities and ensures that any action further on, will not affect these faces any more.

    Parameters
    ----------
    pm_entities :
            An iterable with PM_EXTRUDE, PM_SWEEP and PM_LOFT entities.

    Returns
    -------
    object
            None

    See Also
    --------
    morph.PMEntityGeometryUpdate, morph.PMEntityGeometryRegenerate, morph.PMEntityGeometryDelete

    Examples
    --------
    ::

            import ansa
            from ansa import base, morph, constants


            def main():
                pm_feat = base.CollectEntities(constants.NASTRAN, None, "PM_EXTRUDE")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_SWEEP")
                pm_feat += base.CollectEntities(constants.NASTRAN, None, "PM_LOFT")

                morph.PMEntityGeometryRelease(pm_feat)


            if __name__ == "__main__":
                main()


    """


def SculptingSmooth(
    smooth_area: object,
    smooth_algorithm: str,
    distortion: float,
    angle: float,
    intensity: float,
    iterations: int,
    frozen_area: object,
) -> int:
    """

    Smooth area using sculpting smooth algothims

    Parameters
    ----------
    smooth_area : object
            A list of entities that will smooth

    smooth_algorithm : str
            The smooth algorithm. Should be 'Generic' or 'Feature preserve'.

    distortion : float, optional
            Distortion parameter for 'Generic' smooth algothim.  Higher values mean that the edges are not preserved at all. The value should be between 0. and 1.

    angle : float, optional
            Feature angle for 'Feature preserve' algorithm. The minimum angle for the features to be preserved. Feature angles below that value will be smoothed.

    intensity : float, optional
            The intensity of the smooth algorithm. The value should be between 0. and 1.

    iterations : int, optional
            Number of smooth iterations. Default value is 1.

    frozen_area : object, optional
            A list of frozen entities

    Returns
    -------
    int
            This function always returns 1

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base, constants, morph


            def main():
                set = [base.GetEntity(constants.NASTRAN, "SET", 1)]
                morph.SculptingSmooth(set, "Generic")
                morph.SculptingSmooth(set, "Generic", distortion=0.4, intensity=0.5, iterations=10)

                morph.SculptingSmooth(set, "Feature preserve")
                morph.SculptingSmooth(
                    set, "Feature preserve", angle=45, intensity=0.5, iterations=10
                )


            if __name__ == "__main__":
                main()


    """


def NewParameterCylindricalSpin(morph_point: object, name: str) -> object:
    """

    Function for the creation of a spin morph parameter on cylindrical morph box.

    Parameters
    ----------
    morph_point : object
            A single morph point of cylindrical morph box.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'Spin')

    Returns
    -------
    object
            Returns a reference to the newly created parameter on sucess, or None on failure.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                mopnt = base.GetEntity(constants.NASTRAN, "MORPHPOINT", 10)

                parameter = morph.NewParameterCylindricalSpin(mopnt)
                morph.MorphParam(parameter, 30)


    """


def NewParameterHoles(
    holes_2d: object, offset_type: str, movement_type: str, name: str
) -> object:
    """

    Function for the creation of a holes morph parameter.

    Parameters
    ----------
    holes_2d : object
            A list of HOLE 2D feature entities.

    offset_type : str
            A string to set the type of size offsetting. Accepts either 'Offset', 'Radial Offset' or 'Target Diameter'.

    movement_type : str
            A string to set the type of perimeters movement: either on surface or middle plane. Accepts either 'middle plane' or 'surface'.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'ParameterHoles')

    Returns
    -------
    object
            Returns a reference to the newly created parameter on sucess, or None on failure.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                holes_2d = [
                    base.GetEntity(constants.NASTRAN, "HOLE 2D", 1),
                    base.GetEntity(constants.NASTRAN, "HOLE 2D", 10),
                ]

                parameter_a = morph.NewParameterHoles(holes_2d, "Radial Offset", "surface")
                parameter_b = morph.NewParameterHoles(
                    holes_2d, "Target Diameter", "middle plane", "Name"
                )

                morph.MorphParam(parameter_a, 2.5)
                morph.MorphParam(parameter_b, 150.0)


    """


def NewParameterTubes(
    holes_3d: object, offset_type: str, movement_type: str, name: str
) -> object:
    """

    Function for the creation of a tubes morph parameter.

    Parameters
    ----------
    holes_3d : object
            A list of HOLE 3D feature entities

    offset_type : str
            A string to set the type of size offsetting. Accepts either 'Radial Offset' or 'Target Diameter'.

    movement_type : str
            A string to set the type of tubes' perimeters movement: either on radius direction or surface. Accepts either 'surface' or 'radius'.

    name : str, optional
            The desired name for the new parameter.
            (Default: 'ParameterTubes')

    Returns
    -------
    object
            Returns a reference to the newly created parameter on sucess, or None on failure.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def main():
                holes_3d = [
                    base.GetEntity(constants.NASTRAN, "HOLE 3D", 1),
                    base.GetEntity(constants.NASTRAN, "HOLE 3D", 10),
                ]

                parameter_a = morph.NewParameterTubes(holes_3d, "Radial Offset", "radius")
                parameter_b = morph.NewParameterTubes(
                    holes_3d, "Target Diameter", "surface", "Name"
                )

                morph.MorphParam(parameter_a, 2.5)
                morph.MorphParam(parameter_b, 150.0)


    """


class BoxSplit:
    """

    A class that handles all functionality related to splits of morphing, hexa-block and size boxes.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def collect_ents_from_id_type(collector, ids, type):
                for curr_id in ids:
                    curr_ent = base.GetEntity(constants.NASTRAN, type, curr_id)
                    if curr_ent:
                        collector.append(curr_ent)


            def getPointEdge():
                box_point = base.GetEntity(constants.NASTRAN, "GRID", a_grid_id)
                box_edge = base.GetEntity(constants.NASTRAN, "MORPHEDGE", a_morph_edge_id)
                return box_point, box_edge


            def split_on_points_example():
                morph_pnts_ids = [a_mopnt_id, another_mopnt_id]
                pnts = []
                collect_ents_from_id_type(pnts, morph_pnts_ids, "MORPHPOINT")
                box_split_obj = morph.BoxSplit()
                ans = box_split_obj.on_points(pnts)


            def split_project_example():
                box_point, box_edge = getPointEdge()
                box_split_obj = morph.BoxSplit()
                box_split_obj.project(box_edge, box_point)


            def split_number_example():
                edges = []
                edges.append(base.GetEntity(constants.NASTRAN, "MORPHEDGE", a_morph_edge_id))
                box_split_obj = morph.BoxSplit()
                box_split_obj.number(edges, 2)


            def split_cut_one_way():
                point1 = base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", a_morph_point_id)
                point2 = base.GetEntity(constants.NASTRAN, "HEXA_BOX_POINT", b_morph_point_id)
                box_split_obj = morph.BoxSplit()
                box_split_obj.cut(point1, point2)


            def split_cut_another_way():
                # cut will be performed from point a to b and from point c to d.
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", a_morph_point_id))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", b_morph_point_id))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", c_morph_point_id))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", d_morph_point_id))
                box_split_obj = morph.BoxSplit()
                box_split_obj.cut(points)


            def split_to_penta_example():
                points = []
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", a_morph_point_id))
                points.append(base.GetEntity(constants.NASTRAN, "MORPHPOINT", b_morph_point_id))
                box_split_obj = morph.BoxSplit()
                box_split_obj.to_penta(points)

    """

    fit_new_skin_edges: bool = None
    """
	fit new skin edges on the underlying geometry (geometric or finite elements model) , Default: False

	"""

    work_on: str = None
    """
	'all'  or 'visible',   Default: 'all'

	"""

    def on_points(self, box_points: object) -> int:
        """

        Split the boxes on existing middle box points of the same edge.


        Parameters
        ----------
        box_points : object
                An iterable containing box point entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT)

        Returns
        -------
        int
                1 on success, 0 on failure

        """

    def number(self, box_edges: object, number_of_splits: int) -> int:
        """

        Split box edges to a number of equally spaced intervals.


        Parameters
        ----------
        box_edges : object
                An iterable of box edges entities (MORPHEDGE, HEXA_BOX_EDGE, SIZEBOXEDGE)

        number_of_splits : int
                The number of splits to be performed for each box edge.

        Returns
        -------
        int
                1 on success, 0 on failure

        """

    def project(self, box_edge: object, points: object):
        """

        Split a box edge on the projections of point entities upon it.


        Parameters
        ----------
        box_edge : object
                A box edge entity (MORPHEDGE, HEXA_BOX_EDGE, SIZEBOXEDGE)

        points : object
                An iterable of point-like entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT, HOT POINT)

        """

    def to_penta(self, box_points: object) -> int:
        """

        Split boxes in half by creating two penta boxes for each box.


        Parameters
        ----------
        box_points : object
                An iterable of box point entities (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). Boxes will be split on these points. The iterable should contain an even number of points.

        Returns
        -------
        int
                1 on success, 0 on failure

        """

    def cut(self, box_points_a: object, box_point_b: object):
        """

        Split a box on two points of opposite edges


        Parameters
        ----------
        box_points_a : object
                An iterable of box point entities or a single box point entity (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). In the first case, each split uses two box points from the iterable sequentially.

        box_point_b : object, optional
                A box point entity (MORPHPOINT, HEXA_BOX_POINT, SIZEBOXPOINT). Only in case that the first argument is a single box point entity.

        """

    def __init__(self, fit_new_skin_edges: bool, work_on: str) -> object:
        """

        Constructor of class


        Parameters
        ----------
        fit_new_skin_edges : bool, optional
                The same as object's member

        work_on : str, optional
                The same as object's member

        Returns
        -------
        object

        """


class Create:
    """

    Class providing methods for the creation of features (openings, stamps, ribs, beads) in the finite elements mesh.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import morph
            from ansa import constants


            def bead_straight_example():
                pnt1 = base.GetEntity(constants.NASTRAN, "POINT", a_point_id)
                pnt2 = base.GetEntity(constants.NASTRAN, "POINT", another_point_id)
                create_obj = morph.Create(set_id=1)
                create_obj.set_improve_mesh("Smooth", 1)
                created_entities = create_obj.bead_straight(
                    bead_point1=pnt1,
                    bead_point2=pnt2,
                    width=10.0,
                    height=8.0,
                    angle=75.0,
                    radius1=3.0,
                    radius2=1,
                    straight_rounded=True,
                )


            def flanged_opening_curved_example():
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "CURVE", a_curve_id))
                create_obj = morph.Create(invert_direction=True, set_id=1)
                create_obj.flanged_opening_curved(ents, 10.0, 8.0, 75.0, 3.0)
                created_entities = create_obj.return_elements


            def opening_circular_and_stamp_rectangular_rounded_example(
                point1, point2, point3, point4
            ):
                create_obj = morph.Create(
                    invert_direction=True, save_morph_parameter=True, set_id=1
                )
                create_obj.set_direction_points(point1, point2)
                create_obj.opening_circular(point3, 20.0)
                create_obj.stamp_rectangular_rounded(point4, 20.0, 30.0, 6.0, 8.0, 75.0, 3.0, 2.0)


            def rib_3d_example(point1, point2, point3):
                create_obj = morph.Create().rib_3d(
                    point1, point2, point3, 7.0, 9.0, "Chamfer", 2.0, "Fillet", 0.0, 250.0
                )


            def stamp_rectangular_rounded_example(stamp_entity, direction_point1, direction_point2):
                create_obj = morph.Create(invert_direction=True, save_morph_parameter=True)
                create_obj.set_improve_mesh("Reconstruct", 3)
                create_obj.set_direction_points(direction_points1, direction_points2)
                created_entities = create_obj.stamp_rectangular_rounded(
                    stamp_entity, 20.0, 30.0, 6.0, 8.0, 75.0, 3.0, 2.0
                )

    """

    invert_direction: bool = None
    """
	Turn the created feature upside down. Default: False

	"""

    auto_reconstruct: object = None
    """
	A dictionary with key-value pairs as of "set_improve_mesh" method. See below. Default: None

	"""

    set_id: int = None
    """
	The id of an ANSA entity "SET" to which the created entities should be added. Default: 0

	"""

    save_morph_parameter: bool = None
    """
	Store a DC_FEATURE_SLIDE entity for the created feature. Default: False

	"""

    return_elements: bool = None
    """
	A list with the created elements. This member cannot be changed.

	"""

    def __init__(
        self,
        invert_direction: bool,
        auto_reconstruct: object,
        set_id: int,
        save_morph_parameter: bool,
    ) -> object:
        """

        Constructor of class


        Parameters
        ----------
        invert_direction : bool, optional
                The same with object's member

        auto_reconstruct : object, optional
                The same with object's member

        set_id : int, optional
                The same with object's member

        save_morph_parameter : bool, optional
                The same with object's member

        Returns
        -------
        object

        """

    def flanged_opening_surface(
        self,
        entities: object,
        height: float,
        angle: float,
        radius: float,
        return_characteristics: bool,
    ) -> object:
        """


        Parameters
        ----------
        entities : object
                list of ANSA entities

        height : float

        angle : float

        radius : float

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def flanged_opening_straight(
        self,
        opening_point1: object,
        opening_point2: object,
        width: float,
        height: float,
        angle: float,
        radius: float,
        straight_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        opening_point1 : object
                An ANSA point-like entity.

        opening_point2 : object
                An ANSA point-like entity

        width : float

        height : float

        angle : float

        radius : float

        straight_rounded : bool, optional
                True for "straight-rounded", False for "straight"

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def flanged_opening_curved(
        self,
        opening_entities: object,
        width: float,
        height: float,
        angle: float,
        radius: float,
        curved_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        opening_entities : object
                A list of ANSA entities

        width : float

        height : float

        angle : float

        radius : float

        curved_rounded : bool, optional
                True for "curved_rounded", False for "curved".

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned. A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def flanged_opening_circular(
        self,
        center_point: object,
        diameter: float,
        height: float,
        angle: float,
        radius: float,
        direction_point1: object,
        direction_point2: object,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                An ANSA point-like entity

        diameter : float

        height : float
                An ANSA point-like entity

        angle : float

        radius : float

        direction_point1 : object, optional
                An ANSA point-like entity

        direction_point2 : object, optional
                An ANSA point-like entity

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def stamp_rectangular_rounded(
        self,
        center_point: object,
        width1: float,
        width2: float,
        corner: float,
        height: float,
        angle: float,
        radius1: float,
        radius2: float,
        direction_point1: object,
        direction_point2: object,
        return_characteristics: bool,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                An ANSA point-like entity

        width1 : float

        width2 : float

        corner : float

        height : float

        angle : float

        radius1 : float

        radius2 : float

        direction_point1 : object, optional
                An ANSA point-like entity

        direction_point2 : object, optional
                An ANSA point-like entity

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def stamp_circular(
        self,
        center_point: object,
        diameter: float,
        height: float,
        angle: float,
        radius1: float,
        radius2: float,
        direction_point1: object,
        direction_point2: object,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                An ANSA point-like entity

        diameter : float

        height : float

        angle : float

        radius1 : float

        radius2 : float

        direction_point1 : object, optional
                An ANSA point-like entity

        direction_point2 : object
                An ANSA point-like entity

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def stamp_surface(
        self,
        stamp_entities: object,
        height: float,
        angle: float,
        radius1: float,
        radius2: float,
        return_characteristics: bool,
    ) -> object:
        """


        Parameters
        ----------
        stamp_entities : object
                A list of ANSA entities

        height : float

        angle : float

        radius1 : float

        radius2 : float

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def rib_3d(
        self,
        rib_top1: object,
        rib_top2: object,
        rib_height: object,
        width: float,
        angle: float,
        top_type: str,
        top_value: float,
        bottom_type: str,
        bottom_value: float,
        length: float,
    ) -> object:
        """


        Parameters
        ----------
        rib_top1 : object
                ANSA entity

        rib_top2 : object
                ANSA entity

        rib_height : object
                ANSA entity

        width : float

        angle : float

        top_type : str

        top_value : float

        bottom_type : str
                An ANSA point-like entity

        bottom_value : float

        length : float, optional

        Returns
        -------
        object
                A list of created entities

        """

    def rib_2d(
        self, rib_top1: object, rib_top2: object, rib_height: object, length: float
    ) -> object:
        """


        Parameters
        ----------
        rib_top1 : object
                ANSA entity

        rib_top2 : object
                ANSA entity

        rib_height : object
                ANSA entity

        length : float, optional

        Returns
        -------
        object
                A list of created entitites

        """

    def opening_curved(
        self, opening_entities: object, width: float, curved_rounded: bool
    ) -> object:
        """


        Parameters
        ----------
        opening_entities : object
                A list of ANSA entities

        width : float

        curved_rounded : bool, optional
                True for "curved_rounded", False for "curved"

        Returns
        -------
        object
                A list of created entities

        """

    def opening_surface(self, opening_entities: object) -> object:
        """


        Parameters
        ----------
        opening_entities : object
                A list of ANSA entities

        Returns
        -------
        object
                A list of created entities

        """

    def opening_circular(
        self,
        center_point: object,
        diameter: float,
        direction_point1: object,
        direction_point2: object,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                ANSA point-like entity

        diameter : float

        direction_point1 : object, optional
                ANSA point-like entity

        direction_point2 : object, optional
                ANSA point-like entity

        Returns
        -------
        object
                A list of created entities

        """

    def opening_straight(
        self,
        opening_point1: object,
        opening_point2: object,
        width: float,
        straight_rounded: bool,
    ) -> object:
        """


        Parameters
        ----------
        opening_point1 : object
                ANSA point-like entity

        opening_point2 : object
                ANSA point-like entity

        width : float

        straight_rounded : bool, optional
                True for "straight_rounded", False for "straight"

        Returns
        -------
        object
                A list of created entities

        """

    def opening_rectangular_rounded(
        self,
        center_point: object,
        width1: float,
        width2: float,
        corner: float,
        direction_point1: object,
        direction_point2: object,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                ANSA point-like entity

        width1 : float

        width2 : float

        corner : float

        direction_point1 : object, optional
                ANSA point-like entity

        direction_point2 : object, optional
                ANSA point-like entity

        Returns
        -------
        object
                A list of created entities

        """

    def bead_straight(
        self,
        bead_point1: object,
        bead_point2: object,
        width: float,
        height: float,
        angle: float,
        radius1: float,
        radius2: float,
        straight_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        bead_point1 : object
                ANSA point-like entity

        bead_point2 : object
                ANSA point-like entity

        width : float

        height : float

        angle : float

        radius1 : float

        radius2 : float, optional

        straight_rounded : bool, optional
                True for "straight_rounded", False for "straight"

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def bead_curved(
        self,
        bead_entities: object,
        width: float,
        height: float,
        angle: float,
        radius1: float,
        radius2: float,
        curved_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        bead_entities : object
                A list of ANSA entities

        width : float

        height : float

        angle : float

        radius1 : float

        radius2 : float, optional

        curved_rounded : bool, optional
                True for "curved_rounded", False for "curved".

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def set_improve_mesh(
        self, type: str, zones: int, exclude_feature_recon: bool = False
    ) -> None:
        """

        Select the mesh improvement method and associated zones around created feature. The "auto_reconstruct" class member shall be a corresponding dictionary with the improvement type ("type") as key and the number of zones ("zones") as value.


        Parameters
        ----------
        type : str
                "Reconstruct" or "Smooth" or "Reshape" (mesh improvement choice)

        zones : int
                Number of zones included around the created feature for mesh improvement

        exclude_feature_recon : bool, optional
                Keep feature out from improve mesh action

        Returns
        -------
        None

        """

    def set_direction_points(self, direction_point1: object, direction_point2: object):
        """

        This method enables to globally set the direction points that can be used to all of the constructive methods of the class.


        Parameters
        ----------
        direction_point1 : object
                ANSA point-like entity

        direction_point2 : object
                ANSA point-like entity

        """

    def clear_return_elems(self) -> bool:
        """

        Clears the container of created elements.


        Returns
        -------
        bool
                True

        """

    def bead_X_type(
        self,
        bead_point: object,
        width1: float,
        width2: float,
        height: float,
        angle_a: float,
        radius1: float,
        radius2: float,
        length1: float,
        length2: float,
        length3: float,
        length4: float,
        angle_b: float,
        radius_a: float,
        radius_b: float,
        X_type_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        bead_point : object
                ANSA point-like entity

        width1 : float

        width2 : float

        height : float

        angle_a : float

        radius1 : float

        radius2 : float

        length1 : float

        length2 : float

        length3 : float

        length4 : float

        angle_b : float

        radius_a : float

        radius_b : float

        X_type_rounded : bool, optional
                Set to "True" for an X type stamp with rounded edges.

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def bead_L_type(
        self,
        bead_point: object,
        width1: float,
        width2: float,
        height: float,
        angle_a: float,
        radius1: float,
        radius2: float,
        length1: float,
        length2: float,
        angle_b: float,
        radius_a: float,
        L_type_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        bead_point : object
                An ANSA point-like entity.

        width1 : float

        width2 : float

        height : float

        angle_a : float

        radius1 : float

        radius2 : float

        length1 : float

        length2 : float

        angle_b : float

        radius_a : float

        L_type_rounded : bool, optional
                Set to "True" for an L type stamp with rounded edges.

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def bead_T_type(
        self,
        bead_point: object,
        width1: float,
        width2: float,
        height: float,
        angle_a: float,
        radius1: float,
        radius2: float,
        length1: float,
        length2: float,
        length3: float,
        angle_b: float,
        radius_a: float,
        radius_b: float,
        T_type_rounded: bool,
        return_characteristics: bool,
        top_is_width: bool,
    ) -> object:
        """


        Parameters
        ----------
        bead_point : object
                An ANSA point-like entity.

        width1 : float

        width2 : float

        height : float

        angle_a : float

        radius1 : float

        radius2 : float

        length1 : float

        length2 : float

        length3 : float

        angle_b : float
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        radius_a : float

        radius_b : float

        T_type_rounded : bool, optional
                Set to "True" for a T type stamp with rounded edges.

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        top_is_width : bool, optional
                If True, the angles on the upper surface of feature will be defined by its width. If False, the top width will be defined by the angles.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """

    def flanged_opening_rectangular_rounded(
        self,
        center_point: object,
        width1: float,
        width2: float,
        corner: float,
        height: float,
        angle: float,
        radius1: float,
        direction_point1: object,
        direction_point2: object,
        return_characteristics: bool,
    ) -> object:
        """


        Parameters
        ----------
        center_point : object
                A point-like entity to define center of opening.

        width1 : float

        width2 : float

        corner : float

        height : float

        angle : float

        radius1 : float

        direction_point1 : object, optional
                A point-like entity.

        direction_point2 : object, optional
                A point-like entity.

        return_characteristics : bool, optional
                If True, a dictionary is returned with the created entities' categories and their contents. If False, the whole list of created entities is returned.

        Returns
        -------
        object
                A list of the created entities or a dictionary with the created entities in categories, depending on the call to 'return_characteristics' argument.

        """


class DFMTranslate:
    """

    Class providing methods to define a translational movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base, constants, morph


            def dfm_translate_example():
                # Declare a new instance of DFM class
                dfm_obj = morph.DFM()

                # Create an instance of DFMTranslate class.
                translated = []
                tr_shell = base.GetEntity(constants.NASTRAN, "SHELL", a_shell_to_transl_id)
                translated.append(tr_shell)
                transl_obj = morph.DFMTranslate()
                transl_obj.set_entities(translated)
                transl_obj.increase_entities_zone(1)
                transl_obj.set_value(10.0)
                transl_obj.set_translate_vector(1, 0, 0)

                # Add the DFMTranslate object to the DFM object.
                dfm_obj.add_translate(transl_obj)

                # Collect entities to be in the transition zone (morphed).
                morphed = []
                a_shell = base.GetEntity(constants.NASTRAN, "SHELL", a_shell_to_be_morphed_id)
                morphed.append(a_shell)
                dfm_obj.set_morphed(morphed)
                dfm_obj.increase_morphed_zone(1)

                # Collect or autocalculate bounds.
                dfm_obj.calculate_bounds()

                # Perform morphing actions.
                dfm_obj.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    entities: object = None
    """
	A list of entities to be translated.

	"""

    coord: object = None
    """
	Coordinate entity

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in the movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from the movement.

        """

    def clear_entities(self) -> object:
        """


        Returns
        -------
        object

        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in movement.

        """

    def set_translate_vector(self, dx: float, dy: float, dz: float):
        """


        Parameters
        ----------
        dx : float

        dy : float

        dz : float

        """

    def set_coord(self, coord: object):
        """


        Parameters
        ----------
        coord : object
                Coordinate entity

        """

    def __init__(self):
        """

        Constructor of class DFMTranslate


        """


class DFMTransform:
    """

    Class providing methods to define an euclidean transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            def dfm_transform_example(list_of_ents_to_be_transformed):
                transf_obj = morph.DFMTransform()  # declare an instance of DFMTransform class.
                transf_obj.entities = (
                    list_of_ents_to_be_transformed  # assign the entities to be transformed.
                )
                trg_coord = base.GetEntity(
                    constants.NASTRAN, "CORD_NODES_R", a_coord_id
                )  # get a coordinate entity.
                transf_obj.set_target_coord(trg_coord)  # define the coordinate entity as target.

                dfm = morph.DFM()  # declare an instance of DFM class.
                dfm.add_transform(
                    transf_obj
                )  # add the created DFMTransform object to DFM object for further use
                # see DFM class for complete example.

    """

    value: float = None
    """
	Numerical value of movement magnitude

	"""

    entities: object = None
    """
	A list of entities to be transformed

	"""

    source_coord: object = None
    """
	Coordinate entity

	"""

    target_coord: object = None
    """
	Coordinate entity

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in the movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in the movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from the movement.

        """

    def clear_entities(self) -> object:
        """

        Remove all existing entities included in movement.


        Returns
        -------
        object

        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in the movement.

        """

    def set_source_coord(self, coord: object):
        """


        Parameters
        ----------
        coord : object
                Coordinate entity

        """

    def set_target_coord(self, coord: object):
        """


        Parameters
        ----------
        coord : object
                Coordinate entity

        """

    def __init__(self):
        """

        Constructor of class MDTransform


        """


class DFMScale:
    """

    Class providing methods to define a scaling transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            def dfm_scale_example(list_of_entities_to_be_scaled, list_of_entities_to_be_morphed):
                # declare an instance of DFMScale class and configure it.
                scale_obj = morph.DFMScale()
                scale_obj.set_entities(list_of_entities_to_be_scaled)
                scale_obj.set_origin(x_of_origin, y_of_origin, z_of_origin)
                scale_obj.set_value(1.5)

                # add DFMScale object to a DFM object and perform morphing actions.
                dfm = morph.DFM()
                scale_obj = dfm.add_scale(scale_obj)
                dfm.morphed = list_of_entities_to_be_morphed
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    entities: object = None
    """
	A list of entities to be scaled.

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from movement.

        """

    def clear_entities(self):
        """

        Remove all existing entities included in movement.


        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in movement.

        """

    def set_origin(self, x: float, y: float, z: float):
        """


        Parameters
        ----------
        x : float

        y : float

        z : float

        """

    def __init__(self):
        """

        Constructor of class DFMScale


        """


class DFMOffset:
    """

    Class providing methods to define an offset movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            def dfm_offset_example(list_of_entities_to_offset, list_of_entities_to_be_morphed):
                # declare an instance of DFMScale class and configure it.
                offset_obj = morph.DFMOffset()
                offset_obj.set_entities(list_of_entities_to_be_scaled)
                offset_obj.set_value(4.0)

                # add DFMOffset object to a DFM object and perform morphing actions.
                dfm = morph.DFM()
                offset_obj = dfm.add_offset(offset_obj)
                dfm.morphed = list_of_entities_to_be_morphed
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    entities: object = None
    """
	A list of entities to offset.

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from movement.

        """

    def clear_entities(self) -> object:
        """

                  Remove all existing entities included in movement.


        Returns
        -------
        object

        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in movement.

        """

    def __init__(self):
        """

        Constructor of DFMOffset class


        """


class DFMRotate:
    """

    Class providing methods to define a rotational movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            def dfm_rotate_example(
                list_of_entities_to_be_rotated, list_of_entities_to_be_morphed, x, y, z, dx, dy, dz
            ):
                # create an instance of DFM class and of DFMRotate through the DFM object.
                dfm = morph.DFM()
                rot_obj = dfm.add_rotate()
                rot_obj.set_entities(list_of_entities_to_be_rotated)
                rot_obj.set_rotate_axis(x, y, z, dx, dy, dz)
                rot_obj.set_value(5.0)

                # configure rest DFM options and move.
                dfm.set_morphed(list_of_entities_to_be_morphed)
                dfm.calculate_bounds()
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    entities: object = None
    """
	A list of entities to be rotated.

	"""

    coord: object = None
    """
	Coordinate entity

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from movement.

        """

    def clear_entities(self):
        """

        Remove all existing entities included in movement.


        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in movement.

        """

    def set_rotate_axis(
        self, x: float, y: float, z: float, dx: float, dy: float, dz: float
    ):
        """


        Parameters
        ----------
        x : float

        y : float

        z : float

        dx : float

        dy : float

        dz : float

        """

    def set_coord(self, coord: object):
        """


        Parameters
        ----------
        coord : object
                Coordinate entity

        """

    def __init__(self):
        """

        Constructor of class DFMRotate


        """


class DFMSweepGlide:
    """

    Class providing methods to define a sweep/glide movement of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            def dfm_sweep_glide_example():
                ents = base.GetEntity(
                    constants.NASTRAN, "SET", a_set_id
                )  # collect entities to sweep/glide.
                morphed = [
                    base.GetEntity(constants.NASTRAN, "SET", another_set_id)
                ]  # collect entities in transition zone.
                path = base.GetEntity(
                    constants.NASTRAN, "CURVE", a_curve_id
                )  # curve to define the path of movement.

                # declare an instance of DFMSweepGlide class and configure it.
                sg_obj = morph.DFMSweepGlide()
                sg_obj.movement_type = "Glide"
                sg_obj.rigid_deformable = "Rigid"
                sg_obj.set_entities(ents)
                sg_obj.set_path(path)
                sg_obj.set_value(2.0)

                # use the DFMSweepGlide object within DFM class methods.
                dfm = morph.DFM()
                dfm.add_sweep_glide(sg_obj)
                dfm.set_morphed(morphed)
                dfm.calculate_bounds()
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    entities: object = None
    """
	A list of entities to sweep/glide.

	"""

    path: object = None
    """
	A list of entities to define path of movement.

	"""

    movement_type: str = None
    """
	"Glide" or "Sweep"

	"""

    rigid_deformable: str = None
    """
	"Rigid" or "Deformable"

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                list of entities to be included in movement.

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be included in movement. Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from movement.

        """

    def clear_entities(self):
        """

        Remove all existing entities included in movement.


        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from movement.

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included in movement.

        """

    def insert_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to define path of movement.

        """

    def set_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to define path of movement. Preexisting entities will be discarded.

        """

    def remove_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be excluded from path of movement.

        """

    def clear_path(self):
        """

        Remove all existing entities in path of movement.


        """

    def __init__(self):
        """

        Constructor of class DFMSweepGlide.


        """


class DFMFitEdges:
    """

    A class to define a fit-to-edges transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def dfm_fit_edges_example():
                morphed_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                steady_entities = [base.GetEntity(constants.NASTRAN, "SET", b_set_id)]

                src1 = base.GetEntity(0, "CURVE", a_src_curve_id)
                src2 = base.GetEntity(0, "CURVE", b_src_curve_id)
                trg1 = base.GetEntity(0, "CURVE", a_trg_curve_id)
                trg2 = base.GetEntity(0, "CURVE", b_trg_curve_id)

                dfm = morph.DFM()

                fit1 = dfm.add_fit_edges()
                fit1.set_source_entities(src1)
                fit1.set_target_entities(trg1)
                fit1.set_value(1.0)

                fit2 = dfm.add_fit_edges()
                fit2.set_source_entities(src2)
                fit2.set_target_entities(trg2)
                fit2.set_steady_section(steady_entities)
                fit2.set_value(1.0)

                dfm.set_morphed(morphed_entities)
                dfm.calculate_bounds()

                param = dfm.save_as_param("FitEdges")
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    source_entities: object = None
    """
	A list of entities set as source edges.

	"""

    target_entities: object = None
    """
	A list of entities set as target edges.

	"""

    steady_section_entities: object = None
    """
	A list of entities set as steady section entities.

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def set_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source edges to be included in movement. Preexisting source edges will be discarded.

        """

    def insert_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source edges to be included in movement.

        """

    def remove_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source edges to be excluded from movement.

        """

    def clear_source_entities(self):
        """

        Remove all existing source edges included in movement.


        """

    def set_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target edges to be included in movement. Preexisting target edges will be discarded.

        """

    def insert_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target edges to be included in movement.

        """

    def remove_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target edges to be excluded from movement.

        """

    def clear_target_entities(self):
        """

        Remove all target edges included in movement.


        """

    def decrease_source_zones(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source edges to be excluded from movement.

        """

    def increase_source_zones(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source edges to be included in movement.

        """

    def decrease_target_zones(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target edges to be excluded from movement.

        """

    def increase_target_zones(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target edges to be included in movement.

        """

    def __init__(self):
        """

        Constructor of class DFMFitEdges.


        """

    def set_steady_section(self, steady_section: object):
        """


        Parameters
        ----------
        steady_section : object
                A list of steady section entities to be included in movement.

        """

    def insert_steady_section(self, steady_section: object):
        """


        Parameters
        ----------
        steady_section : object
                A list of steady section entities to be included in movement. Preexisting steady section entities will be discarded.

        """

    def remove_steady_section(self, steady_section: object):
        """


        Parameters
        ----------
        steady_section : object
                A list of steady section entities to be excluded from movement.

        """

    def clear_steady_section(self):
        """

        Remove all steady section entities included in movement.


        """


class DFMFitSurfaces:
    """

    A class to define a fit-to-surfaces transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def getSrcPoints():
                src_pnts1 = []
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", src_grid_a_id))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", src_grid_b_id))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", src_grid_c_id))
                src_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", src_grid_d_id))
                return src_pnts1


            def getTrgPoints():
                trg_pnts1 = []
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", trg_grid_a_id))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", trg_grid_b_id))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", trg_grid_c_id))
                trg_pnts1.append(base.GetEntity(constants.NASTRAN, "GRID", trg_grid_d_id))
                return trg_pnts1


            def main():
                part1 = base.GetPartFromName("Initial_surface")
                part2 = base.GetPartFromName("Target_Surface")
                trg = getTrgPoints()
                src = getSrcPoints()

                dfm = morph.DFM()
                fit_surfs_obj = dfm.add_fit_surfs()  # create a DFMFitSurfaces object.

                fit_surfs_obj.set_target_entities(part2)
                fit_surfs_obj.set_source_entities(part1)
                fit_surfs_obj.set_source_target_points(src, trg)
                fit_surfs_obj.set_value(1)

                dfm.save_as_param("FitSurfsParam")
                dfm.apply()

    """

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    source_entities: object = None
    """
	A list of entities to define source surface.

	"""

    target_entities: object = None
    """
	A list of entities to define target surface.

	"""

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def set_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be included in movement. Preexisting source entities will be discarded.

        """

    def insert_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be included in movement.

        """

    def remove_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be excluded from movement.

        """

    def clear_source_entities(self):
        """

        Remove all existing source entities included in movement.


        """

    def set_target_entities(self, target_entities: object):
        """




        Parameters
        ----------
        target_entities : object
                A list of target entities to be included in movement. Preexisting target entities will be discarded.

        """

    def insert_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target entities to be included in movement.

        """

    def remove_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target entities to be excluded from movement.

        """

    def clear_target_entities(self):
        """

        Remove all target entities included in movement.


        """

    def decrease_source_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source entities to be excluded from movement.

        """

    def increase_source_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source entities to be included in movement.

        """

    def decrease_target_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target entities to be excluded from movement.

        """

    def increase_target_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target entities to be included in movement.

        """

    def set_source_target_points(self, source_points: object, target_points: object):
        """


        Parameters
        ----------
        source_points : object
                A list of points to define source surface.

        target_points : object
                A list of points to define target surface.

        """

    def __init__(self):
        """

        Constructor of class DFMFitSurfaces.


        """


class DFMAlign:
    """

    A class to define an alignment transformation of finite elements mesh or geometry entities. Instances of this class are meant to be inserted in a DFM object which handles the whole morphing action.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def dfm_align(
                list_of_entities_to_be_aligned,
                list_of_entities_to_be_morphed,
                list_of_target_entities,
            ):
                align_obj = morph.DFMAlign()
                align_obj.set_source_entities(list_of_entities_to_be_aligned)
                align_obj.set_align_on_axis()
                align_obj.set_target_plane(1289.0012, -231.286, 1081.992, 0, -1, 0)
                align_obj.set_target_axis(235.023, -100.24, 23.432, 0, 0, 1)
                align_obj.set_user_direction(0.698, 0.712, 0.067)
                align_obj.set_value(1.0)

                dfm = morph.DFM()
                dfm.add_align(align_obj)
                dfm.set_morphed(list_of_entities_to_be_morphed)
                dfm.calculate_bounds()
                dfm.apply()

    """

    source_entities: object = None
    """
	A list of entities set as source.

	"""

    target_entities: object = None
    """
	A list of entities set as target.

	"""

    max_distance: float = None

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def set_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be included in movement. Preexisting source entities will be discarded.

        """

    def insert_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be included in movement.

        """

    def remove_source_entities(self, source_entities: object):
        """


        Parameters
        ----------
        source_entities : object
                A list of source entities to be excluded from movement.

        """

    def clear_source_entities(self):
        """

        Remove all source entities included in movement.


        """

    def set_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target entities to be included in movement. Preexisting target entities will be discarded.

        """

    def insert_target_entities(self, target_entitites: object):
        """


        Parameters
        ----------
        target_entitites : object
                A list of target entities to be included in movement.

        """

    def remove_target_entities(self, target_entities: object):
        """


        Parameters
        ----------
        target_entities : object
                A list of target entities to be excluded from movement.

        """

    def clear_target_entities(self):
        """

        Remove all target entities included in movement.


        """

    def decrease_source_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source entities to be excluded from movement.

        """

    def increase_source_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around source entities to be included in movement.

        """

    def decrease_target_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target entities to be excluded from movement.

        """

    def increase_target_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around target entities to be included in movement.

        """

    def set_target_plane(
        self, x: float, y: float, z: float, dx: float, dy: float, dz: float
    ):
        """


        Parameters
        ----------
        x : float

        y : float

        z : float

        dx : float

        dy : float

        dz : float

        """

    def set_target_axis(
        self, x: float, y: float, z: float, dx: float, dy: float, dz: float
    ):
        """


        Parameters
        ----------
        x : float

        y : float

        z : float

        dx : float

        dy : float

        dz : float

        """

    def set_user_direction(self, dx: float, dy: float, dz: float):
        """


        Parameters
        ----------
        dx : float

        dy : float

        dz : float

        """

    def set_max_distance(self, max_distance: float):
        """


        Parameters
        ----------
        max_distance : float

        """

    def set_include_thickness(self, include_thickness: bool):
        """


        Parameters
        ----------
        include_thickness : bool

        """

    def set_align_on_axis(self):
        """

        Call this method if the alignment must be done on axis. This option is mutually exclusive with "set_align_on_entities".


        """

    def set_align_on_entities(self):
        """

        Call this method if alignment must be done on entities. This option is mutually exclusive with set_align_on_axis method.


        """

    def __init__(self):
        """

        Constructor of class DFMAlign.


        """


class ConstraintRigid:
    """

    Class providing methods to define a constraint of type 'Rigid' to be included in a direct morphing action. The entities belonging to such a constraint shall follow a rigid body motion during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Rigid' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def rigid_constraint_example_1(list_of_entities_in_constraint):
                # create a rigid constraint through ConstraintRigid class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                rigid_obj = morph.ConstraintRigid()
                rigid_obj.set_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(rigid_obj)


            def rigid_constraint_example_2(list_of_entities_in_constraint):
                # create a rigid constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_rigid_constraint = base, GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                rigid_obj = morph.ConstraintRigid(existing_rigid_constraint)
                rigid_obj.insert_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(rigid_obj)


            def register_constraint_example(list_of_entities_in_constraint):
                # create a new MORPH_CONSTRAINT entity through ConstraintRigid class.
                rigid_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                rigid_obj = morph.ConstraintRigid()
                rigid_obj.set_entities(list_of_entities_in_constraint)
                new_rigid_constraint = rigid_obj.reg()  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to remain rigid.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self) -> object:
        """

        Remove all entities from object's member "morphed".


        Returns
        -------
        object

        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def __init__(self, rigid_constraint: object):
        """

        Constructor of class ConstraintRigid.


        Parameters
        ----------
        rigid_constraint : object, optional
                MORPH_CONSTRAINT entity of Rigid type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintRigid object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class ConstraintPathFollower:
    """

    Class providing methods to define a constraint of type 'Path Follower' to be included in a direct morphing action. The entities belonging to such a constraint shall follow a user defined path during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Path Follower' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def path_follower_constraint_example_1(
                list_of_entities_in_constraint, list_of_entities_to_define_path
            ):
                # create a path_follower constraint through ConstraintPathFollower class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                path_follower_obj = morph.ConstraintPathFollower()
                path_follower_obj.set_entities(list_of_entities_in_constraint)
                path_follower_obj.set_path(list_of_entities_to_define_path)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(path_follower_obj)


            def path_follower_constraint_example_2(list_of_entities_in_constraint):
                # create a path_follower constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_path_follower_constraint = base, GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                path_follower_obj = morph.ConstraintPathFollower(existing_path_follower_constraint)
                path_follower_obj.insert_entities(list_of_entities_in_constraint)
                path_follower_obj.set_path(list_of_entities_to_define_path)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(path_follower_obj)


            def register_constraint_example(list_of_entities_in_constraint):
                # create a new MORPH_CONSTRAINT entity through ConstraintPathFollower class.
                path_follower_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                path_follower_obj = morph.ConstraintPathFollower()
                path_follower_obj.set_entities(list_of_entities_in_constraint)
                path_follower_obj.set_path(list_of_entities_to_define_path)
                new_path_follower_constraint = (
                    path_follower_obj.reg()
                )  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to follow a path.

	"""

    path: object = None
    """
	A list of entities that define a path.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self) -> object:
        """

                  Remove all entities from object's member "morphed".


        Returns
        -------
        object

        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be removed from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def insert_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path".

        """

    def set_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

        """

    def remove_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be removed from object's member "path".

        """

    def clear_path(self):
        """

        Remove all entities from object's member "path".


        """

    def __init__(self, path_follower_constraint: object):
        """

        Constructor of class ConstraintPathFollower


        Parameters
        ----------
        path_follower_constraint : object, optional
                MORPH_CONSTRAINT entity of Path Follower type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintPathFollower object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class ConstraintPlanar:
    """

    Class providing methods to define a constraint of type 'Planar' to be included in a direct morphing action. The entities belonging to such a constraint shall lie all on the same plane, as much as possible, during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Planar' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def planar_constraint_example_1(list_of_entities_in_constraint):
                # create a planar constraint through ConstraintPlanar class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                planar_obj = morph.ConstraintPlanar()
                planar_obj.set_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(planar_obj)


            def planar_constraint_example_2(list_of_entities_in_constraint):
                # create a planar constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_planar_constraint = base, GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                planar_obj = morph.ConstraintPlanar(existing_planar_constraint)
                planar_obj.insert_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(planar_obj)


            def register_constraint_example(list_of_entities_in_constraint):
                # create a new MORPH_CONSTRAINT entity through ConstraintPlanar class.
                planar_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                planar_obj = morph.ConstraintPlanar()
                planar_obj.set_entities(list_of_entities_in_constraint)
                new_planar_constraint = planar_obj.reg()  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to remain planar.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self) -> object:
        """

                  Remove all entities from object's member "morphed".


        Returns
        -------
        object

        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def __init__(self, planar_constraint: object):
        """

        Constructor of class ConstraintPlanar.


        Parameters
        ----------
        planar_constraint : object, optional
                MORPH_CONSTRAINT entity of Planar type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintPlanar object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class ConstraintScaled:
    """

    Class providing methods to define a constraint of type 'Scaled' to be included in a direct morphing action. The entities belonging to such a constraint shall retain their relative size ratios during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Scaled' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def scaled_constraint_example_1(list_of_entities_in_constraint):
                # create a scaled constraint through ConstraintScaled class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                scaled_obj = morph.ConstraintScaled()
                scaled_obj.set_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(scaled_obj)


            def scaled_constraint_example_2(list_of_entities_in_constraint):
                # create a scaled constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_scaled_constraint = base, GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                scaled_obj = morph.ConstraintScaled(existing_scaled_constraint)
                scaled_obj.insert_entities(list_of_entities_in_constraint)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(scaled_obj)


            def register_constraint_example(list_of_entities_in_constraint):
                # create a new MORPH_CONSTRAINT entity through ConstraintScaled class.
                scaled_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                scaled_obj = morph.ConstraintScaled()
                scaled_obj.set_entities(list_of_entities_in_constraint)
                new_scaled_constraint = scaled_obj.reg()  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to be scaled.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def __init__(self, scaled_constraint: object):
        """

        Constructor of class ConstraintScaled.


        Parameters
        ----------
        scaled_constraint : object, optional
                MORPH_CONSTRAINT entity of Scaled type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class ConstraintDirectional:
    """

    Class providing methods to define a constraint of type 'Directional' to be included in a direct morphing action. The entities belonging to such a constraint shall move on a user defined direction during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Directional' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph

            coord = base.GetEntity(0, "CORD_NODES_R", a_coord_id)


            def directional_constraint_example_1(list_of_entities_in_constraint):
                # create a directional constraint through ConstraintDirectional class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                directional_obj = morph.ConstraintDirectional()
                directional_obj.set_entities(list_of_entities_in_constraint)
                directional_obj.set_coord(coord)
                directional_obj.set_status(True, False, False)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(directional_obj)


            def directional_constraint_example_2(list_of_entities_in_constraint):
                # create a directional constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_directional_constraint = base.GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                directional_obj = morph.ConstraintDirectional(existing_directional_constraint)
                directional_obj.insert_entities(list_of_entities_in_constraint)
                directional_obj.set_coord(coord)
                directional_obj.set_status(True, False, False)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(directional_obj)


            def register_constraint_example(list_of_entities_in_constraint):
                # create a new MORPH_CONSTRAINT entity through ConstraintDirectional class.
                directional_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                directional_obj = morph.ConstraintDirectional()
                directional_obj.set_entities(list_of_entities_in_constraint)
                directional_obj.set_coord(coord)
                directional_obj.set_status(True, False, False)
                new_directional_constraint = (
                    directional_obj.reg()
                )  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to move in a direction.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

         Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def set_coord(self, coord: object):
        """


        Parameters
        ----------
        coord : object
                Coordinate entity

        """

    def set_status(self, x_status: bool, y_status: bool, z_status: bool):
        """


        Parameters
        ----------
        x_status : bool, optional
                Set active or not the x-status.

        y_status : bool, optional
                Set active or not the y-status.

        z_status : bool, optional
                Set active or not the z-status.

        """

    def set_x_active(self, status: bool):
        """


        Parameters
        ----------
        status : bool
                Set active or not the x-status.

        """

    def set_y_active(self, status: bool):
        """


        Parameters
        ----------
        status : bool
                Set active or not the y-status.

        """

    def set_z_active(self, status: bool):
        """


        Parameters
        ----------
        status : bool
                Set active or not the z-status.

        """

    def __init__(self, directional_constraint: object):
        """

        Constructor of class ConstraintDirectional.


        Parameters
        ----------
        directional_constraint : object, optional
                A MORPH_CONSTRAINT of Directional type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class ConstraintFlanges:
    """

    Class providing methods to define a constraint of type 'Flanges' to be included in a direct morphing action. The entities belonging to the flanges, shall be aligned to the defined contact area, as much as possible, during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Flanges' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def flanges_constraint_example_1(
                list_of_entities_in_constraint, list_of_contact_entities
            ):
                # create a flanges constraint through ConstraintFlanges class and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                flanges_obj = morph.ConstraintFlanges()
                flanges_obj.set_entities(list_of_entities_in_constraint)
                flanges_obj.set_contacts(list_of_contact_entities)
                flanges_obj.set_thickness_flange_gap(0.5)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(flanges_obj)


            def flanges_constraint_example_2(
                list_of_entities_in_constraint, list_of_contact_entities
            ):
                # create a flanges constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                existing_flanges_constraint = base, GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )
                flanges_obj = morph.ConstraintFlanges(existing_flanges_constraint)
                flanges_obj.insert_entities(list_of_entities_in_constraint)
                flanges_obj.set_contacts(list_of_contact_entities)
                flanges_obj.set_thickness_flange_gap(0.5)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(flanges_obj)


            def register_constraint_example(
                list_of_entities_in_constraint, list_of_contact_entities
            ):
                # create a new MORPH_CONSTRAINT entity through ConstraintFlanges class.
                flanges_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]
                flanges_obj = morph.ConstraintFlanges()
                flanges_obj.set_entities(list_of_entities_in_constraint)
                flanges_obj.set_contacts(list_of_contact_entities)
                flanges_obj.set_thickness_flange_gap(0.5)
                new_flanges_constraint = flanges_obj.reg()  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities consisting the flanges.

	"""

    contacts: object = None
    """
	A list of entities constrained to be in contact with flanges.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as fixed perimeters.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def insert_contacts(self, contacts: object):
        """


        Parameters
        ----------
        contacts : object
                A list of entities to be inserted in object's member "contacts".

        """

    def set_contacts(self, contacts: object):
        """


        Parameters
        ----------
        contacts : object
                A list of entities to be inserted in object's member "contacts". Preexisting entities will be discarded.

        """

    def remove_contacts(self, contacts: object):
        """


        Parameters
        ----------
        contacts : object
                A list of entities to be excluded from object's member "contacts".

        """

    def clear_contacts(self):
        """

        Remove all entities from object's member "contacts".


        """

    def set_thickness_flange_gap(self, offset: float):
        """


        Parameters
        ----------
        offset : float
                Flange gap thickness.

        """

    def set_preserve_flange_gap(self):
        """

        Call this method to preserve the flange gap.


        """

    def __init__(self, flanges_constraint: object):
        """

        Constructor of class ConstraintFlanges.


        Parameters
        ----------
        flanges_constraint : object, optional
                MORPH_CONSTRAINT entity of Flanges type.

        """

    def reg(self) -> object:
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintFlanges object and register it in the database.


        Returns
        -------
        object
                The created and registered MORPH_CONSTRAINT entity. Method returns None if the corresponding entity was already registered.

        """


class DCPosition:
    """

    Class providing methods for a direct morphing action identical to the one provided by Design Change Position functionality in ANSA.

    See Also
    --------
    morph.DFM

    Examples
    --------
    ::

            import ansa
            from ansa import base, constants, morph


            def dc_position_example():
                # Declare a new instance of DCPosition class
                dc_obj = morph.DCPosition()

                # Collect entities to be translated.
                ents = []
                ents.append(base.GetEntity(constants.NASTRAN, "SHELL", a_shell_id))
                dc_obj.set_entities(ents)
                dc_obj.increase_entities_zone(1)  # expand selected shells zones by 1.

                # Collect entities to be in the transition zone (morphed) and entities to bound the movement (bounds)
                dc_obj.increase_morphed_zone(
                    1
                )  # include a zone around selected entities as morphed entities.
                dc_obj.calculate_bounds()  # auto calculate bounds.

                # Collect any associated MORPH_CONSTRAINT entities
                constraints = []
                constraints.append(
                    base.GetEntity(constants.NASTRAN, "MORPH_CONSTRAINT", a_morph_constraint_id)
                )
                dc_obj.set_constraints(constraints)

                # Define movement attributes
                dc_obj.set_user_direction(1, 0, 0)
                dc_obj.set_value(20.0)

                # Perform morphing actions
                dc_obj.apply()

    """

    morphed: object = None
    """
	A list of entities to be morphed.

	"""

    bounds: object = None
    """
	A list of entities to bound the movement.

	"""

    entities: object = None
    """
	A list of entities to be translated.

	"""

    value: float = None
    """
	Numerical value of movement magnitude.

	"""

    constraints: object = None
    """
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

    defined_constraints: object = None
    """
	A list of MORPH_CONSTRAINT entities related to the contents of the movement. This object cannot be changed.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as bounds.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def decrease_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be included also in object's member "entities".

        """

    def increase_entities_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around entities to be excluded from object's member "entities".

        """

    def set_user_direction(self, dx: float, dy: float, dz: float):
        """


        Parameters
        ----------
        dx : float

        dy : float

        dz : float

        """

    def set_value(self, dist: float):
        """


        Parameters
        ----------
        dist : float

        """

    def insert_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

        """

    def set_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

        """

    def remove_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

        """

    def clear_constraints(self):
        """

        Remove all entities from object's member "constraints".


        """

    def __init__(self, dc_position: object):
        """

        Constructor of class DCPosition


        Parameters
        ----------
        dc_position : object, optional
                A "DC_POSITION" entity.

        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action.


        """

    def apply(self):
        """

        Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script.


        """

    def save_as_DC_Position(self) -> object:
        """

        Create a "DC_POSITION" entity in the ANSA database based on DCPosition object's definition.


        Returns
        -------
        object
                The created "DC_POSITION" entity or None in case of failure.

        """


class DFM:
    """

    Class providing methods for direct morphing of finite elements mesh or geometry entities.

    See Also
    --------
    morph.DFMTranslate, morph.DFMRotate, morph.DFMScale, morph.DFMTransform, morph.DFMFitEdges, morph.DFMFitSurfaces, morph.DFMAlign, morph.DFMSweepGlide, morph.ConstraintRigid, morph.ConstraintPlanar, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base, constants, morph


            def dfm_translate_example():
                # A.declare a new instance of DFM class
                dfm_obj = morph.DFM()

                # B.create an instance of DFMTranslate class to define movement type and collect entities to be translated.
                translated = []
                tr_shell = base.GetEntity(constants.NASTRAN, "SHELL", a_shell_to_transl_id)
                translated.append(tr_shell)
                transl_obj = morph.DFMTranslate()
                transl_obj.set_entities(translated)
                transl_obj.increase_entities_zone(1)
                transl_obj.set_value(10.0)
                transl_obj.set_translate_vector(1, 0, 0)

                # C. add the DFMTranslate object to the DFM object.
                dfm_obj.add_translate(transl_obj)

                # D. collect entities to be in the transition zone (morphed).
                morphed = []
                a_shell = base.GetEntity(constants.NASTRAN, "SHELL", a_shell_to_be_morphed_id)
                morphed.append(a_shell)
                dfm_obj.set_morphed(morphed)
                dfm_obj.increase_morphed_zone(1)

                # E. Collect or autocalculate bounds.
                dfm_obj.calculate_bounds()

                # F. Insert a constraint to the movement.
                constraints_list = [
                    base.GetEntity(constants.NASTRAN, "MORPH_CONSTRAINT", a_morph_constraint_id)
                ]
                dfm_obj.set_constraints(constraints_list)

                # G. Perform morphing actions.
                dfm_obj.set_performance("Accurate")
                dfm_obj.preview()
                dfm_obj.apply()

                # H. Save as a PARAMETERS entity for further use.
                param = dfm_obj.save_as_param("MyDFMTranslateParam")


            # --------------------------------------------------------------------------
            def dfm_with_existing_param():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                list_of_more_entities_to_be_moved = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]
                dfm_obj = morph.DFM(
                    param
                )  # create an instance of DFM class from an existing dfm parameter.
                dfm_obj.insert_entities(list_of_more_entities_to_be_moved)
                dfm_obj.calculate_bounds()
                move_obj = dfm_obj.move_types[0]
                move_obj.set_value(5.0)
                dfm_obj.apply()


            # ---------------------------------------------------------------------------
            def dfm_add_constraint_object():
                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                dfm_obj = morph.DFM(
                    param
                )  # create an instance of DFM class from an existing dfm parameter.
                list_of_entities_to_remain_planar = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]
                constraint_planar_obj = morph.ConstraintPlanar()
                constraint_planar_obj.set_entities(list_of_entities_to_remain_planar)
                dfm_obj.add_constraint_obj(
                    constraint_planar_obj
                )  # add the constraint to DFM object.
                dfm_obj.apply()

    """

    morphed: object = None
    """
	A list of entities to be morphed.

	"""

    bounds: object = None
    """
	A list of entities to bound the movement.

	"""

    constraints: object = None
    """
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

    defined_constraints: object = None
    """
	A list of MORPH_CONSTRAINT entities related to the contents of the movement. This object cannot be changed.

	"""

    move_types: object = None
    """
	A list of objects defining the movement types of morphing. Objects must be instances of the following classes: morph.DFMTranslate, morph.DFMRotate, morph.DFMScale, morph.DFMTransform, morph.DFMFitEdges, morph.DFMFitSurfaces, morph.DFMAlign, morph.DFMSweepGlide

	"""

    volume_finder: object = None
    """
	A list of SIZEBOX entities used as volume finders aiding the selection of entities. WARNING: The volume_finder entities are active only in CFD Decks.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self) -> object:
        """

         Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        Returns
        -------
        object
                A list of entities found as bounds.

        """

    def increase_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int) -> object:
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        Returns
        -------
        object
                A list of entities included in object's member "morphed".

        """

    def insert_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be inserted in object's member "volume_finder".

        """

    def set_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be inserted in object's member "volume_finder". Preexisting entities will be discarded.

        """

    def remove_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be removed from object's member "volume_finder".

        """

    def clear_volume_finder(self):
        """

        Remove all entities from object's member "volume_finder".


        """

    def get_move_types(self) -> object:
        """


        Returns
        -------
        object
                A list with the entities in object's member "move_types". See "move_types" member for information about the entities types.

        """

    def add_translate(self, transl_obj: object) -> object:
        """

        Add a morph.DFMTranslate object or create a new one. If no argument is given, a new instance of morph.DFMTranslate will be created.


        Parameters
        ----------
        transl_obj : object, optional
                An instance of morph.DFMTranslate class.

        Returns
        -------
        object
                The created or added morph.DFMTranslate object.

        """

    def add_rotate(self, rotate_obj: object) -> object:
        """

        Add a morph.DFMRotate object or create a new one. If no argument is given, a new instance of morph.DFMRotate will be created.


        Parameters
        ----------
        rotate_obj : object, optional
                An instance of morph.DFMRotate class.

        Returns
        -------
        object
                The created or added morph.DFMRotate object.

        """

    def add_scale(self, scale_obj: object) -> object:
        """

        Add a morph.DFMScale object or create a new one. If no argument is given, a new instance of morph.DFMScale will be created.


        Parameters
        ----------
        scale_obj : object, optional
                An instance of morph.DFMScale class.

        Returns
        -------
        object
                The created or added morph.DFMScale object.

        """

    def add_transform(self, transform_obj: object) -> object:
        """

        Add a morph.DFMTransform object or create a new one. If no argument is given, a new instance of morph.DFMTransform will be created.


        Parameters
        ----------
        transform_obj : object, optional
                An instance of morph.DFMTransform class.

        Returns
        -------
        object
                The created or added morph.DFMTransform object.

        """

    def add_fit_edges(self, fit_edges_obj: object) -> object:
        """

        Add a morph.DFMFitEdges object or create a new one. If no argument is given, a new instance of morph.DFMFitEdges will be created.


        Parameters
        ----------
        fit_edges_obj : object, optional
                An instance of morph.DFMFitEdges class.

        Returns
        -------
        object
                The created or added morph.DFMFitEdges class.

        """

    def add_fit_surfs(self, fit_surfs_obj: object) -> object:
        """

        Add a morph.DFMFitSurfaces object or create a new one. If no argument is given, a new instance of morph.DFMFitSurfaces will be created.


        Parameters
        ----------
        fit_surfs_obj : object, optional
                An instance of morph.DFMFitSurfaces class.

        Returns
        -------
        object
                The created or added morph.DFMFitSurfaces object.

        """

    def add_align(self, align_obj: object) -> object:
        """

        Add a morph.DFMAlign object or create a new one. If no argument is given, a new instance of morph.DFMAlign will be created.


        Parameters
        ----------
        align_obj : object, optional
                An instance of morph.DFMAlign class.

        Returns
        -------
        object
                The created or added morph.DFMAlign object.

        """

    def add_sweep_glide(self, sweep_glide_obj: object) -> object:
        """

        Add a morph.DFMSweepGlide object or create a new one. If no argument is given, a new instance of morph.DFMSweepGlide will be created.


        Parameters
        ----------
        sweep_glide_obj : object, optional
                An instance of morph.DFMSweepGlide class.

        Returns
        -------
        object
                The created or added morph.DFMSweepGlide object.

        """

    def save_as_param(self, name: str) -> object:
        """


        Parameters
        ----------
        name : str, optional
                The name of the parameter to create.

        Returns
        -------
        object
                A morph parameter entity (PARAMETERS).

        """

    def save_as_DVGrids(self):
        """ """

    def insert_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

        """

    def set_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

        """

    def remove_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

        """

    def clear_constraints(self):
        """

        Remove all entities from object's member "constraints".


        """

    def set_performance(self, performance_option: str) -> None:
        """

        Determin the morphing performance of DFM. Fast: only perimeters of control entities affect morphed entities. Accurate: all control entities affect morphed entities


        Parameters
        ----------
        performance_option : str
                Available options are either 'Fast' or 'Accurate'.

        Returns
        -------
        None

        """

    def set_tangency(self, tangency_option: str):
        """


        Parameters
        ----------
        tangency_option : str
                'Default' or 'Smooth'

        """

    def create_symmetric(self) -> object:
        """

        Create a symmetric DFM parameter relative to the default symmetry plane. The current morph.DFM object doesn't have to be saved as DFM Parameter.


        Returns
        -------
        object
                The created PARAMETERS entity or None if symmetry failed.

        """

    def remove_move_type(self, move_type: object):
        """

        Remove an entity from object's member "move_types".


        Parameters
        ----------
        move_type : object
                An instance of one of the classes mentioned in object's member "move_types".

        """

    def __init__(self, dfm_parameter: object):
        """

        Constructor of class DFM.


        Parameters
        ----------
        dfm_parameter : object, optional
                An entity PARAMETERS of DFM type.

        """

    def add_constraint_obj(self, constraint_obj: object):
        """

        Add an instance of morph.Constraint*** classes. This is an alternative way to insert constraints rather than inserting through "insert_constraints" and "set_constraints" methods which require to insert only ANSA entities. The corresponding MORPH_CONSTRAINT entity is inserted in member "constraints".


        Parameters
        ----------
        constraint_obj : object, optional
                An instance of one of the classes: morph.ConstraintRigid, morph.ConstraintPlanar, morph.ConstraintPathFollower, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintFlanges).

        """

    def set_improve_mesh(self, type: str, zones: int):
        """

        Define the mesh improvement action that shall take place after the main morphing action.


        Parameters
        ----------
        type : str
                Options:
                'None'
                'Reconstruct'
                'Smooth'
                'Reshape'

        zones : int, optional
                Number of zones of entities around main morphing area to be included in mesh improvement action.

        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action.


        """

    def apply(self):
        """

        Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script.


        """

    def add_offset(self, offset_obj: object):
        """

        Add a morph.DFMTranslate object or create a new one. If no argument is given, a new instance of morph.DFMTranslate will be created.


        Parameters
        ----------
        offset_obj : object, optional
                An instance of morph.DFMOffset class.

        """


class Form:
    """

    Form - a class to define bending, twisting, tapering and extending of FE or Geometry entities, while preserving the cross-section.

    Examples
    --------
    ::

            import ansa

            from ansa import morph
            from ansa import base
            from ansa import constants


            def form_default():
                obj = morph.Form()

                formed = base.GetEntity(constants.NASTRAN, "SET", a_set_id)

                constraints = []
                constraints.append(
                    base.GetEntity(constants.NASTRAN, "MORPH_CONSTRAINT", a_morph_constraint_id)
                )

                obj.set_formed(formed)
                obj.set_constraints(constraints)

                obj.set_positive_plane_angle(45.0)
                obj.set_negative_plane_angle(-38.0)
                obj.set_positive_plane_extend(1.1)
                obj.set_negative_plnae_y_taper(0.9)

                obj.set_improve_mesh("Smooth", 10)

                # default coordinate and maximum lengths will be used to perform movement
                obj.apply()


            def form_symmetrically():
                obj = morph.Form()

                formed = base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                fixed = base.GetEntity(constants.NASTRAN, "SET", b_set_id)
                coord = base.GetEntity(constants.NASTRAN, "CORD_NODES_R", a_coord_id)

                obj.set_formed(formed)

                # transition entities: 25 zones around formed entities
                obj.increase_transition_zone(25)

                # auto calculate fixed entities and add some extra
                obj.calculate_fixed()
                obj.insert_fixed(fixed)

                # use specific coordinate and align it to the principal axes
                obj.set_coordinate(coord)
                obj.align_to_principal_axes()

                # set negative plane's variables to follow those of positive plane
                obj.set_link_planes(True)

                # save definitions to a DIRECT_FORM entity
                direct_form = obj.save_as_Direct_Form()

                # build a Form object using the saved entity
                form = morph.Form(direct_form)
                form.set_positive_plane_length(250.5)
                form.set_positive_plane_angle(56.0)
                form.set_positive_plane_z_taper(1.3)
                form.apply()


            def form_setup_and_user_section():
                obj = morph.Form()

                obj.set_formed(base.GetEntity(constants.NASTRAN, "SET", a_set_id))
                obj.set_coordinate(base.GetEntity(constants.NASTRAN, "CORD_NODES_R", a_coord_id))

                # setup the initial value of positive plane bending angle
                obj.initial_positive_plane_angle(5.8)

                # define the user section as to describe better the case
                obj.set_user_section(3210.0, 235.0, 8965.45, 0.0, 0.98, 0.015)

                obj.set_positive_plane_twist(45.0)
                obj.set_interpolation("Quadratic")

                obj.apply()


            def form_set_mode():
                obj = morph.Form((base.GetEntity(0, "DIRECT_FORM", 1)))

                # bend with pinned ends by displacing the coordinate system on deflection axis
                obj.set_mode("Pinned Ends")
                obj.set_axes_displacement(0.0, -50.0)

                obj.set_link_planes(true)
                obj.set_positive_plane_y_taper(0.8)

                obj.apply()

    """

    formed: object = None
    """
	A list of entities to be forme.

	"""

    transition: object = None
    """
	A list of entities to be morphed.

	"""

    fixed: object = None
    """
	A list of entities to stay fixed and bound the transition.

	"""

    constraints: object = None
    """
	A list of MORPH_CONSTRAINT entities participating in the movement.

	"""

    volume_finder: object = None
    """
	A list of SIZEBOX entities used as volume finders aiding the selection of entities.

	"""

    coordinate: object = None
    """
	Coordinate entity defining center and direction of bending, twisting, tapering and extending. By default it is placed at formed entities CoG and aligned in to formed entities principal axes. Neutral axis is along the largest dimension and Bending axis along the second largest dimension.

	"""

    positive_plane_length: float = None
    """
	Definition of positive plane's distance from coordinate system, across neutral axis.

	"""

    negative_plane_length: float = None
    """
	Definition of negative plane's distance from coordinate system, across neutral axis.

	"""

    positive_plane_angle: float = None
    """
	Definition of the angle formed among positive plane's initial position, coordinate center and positive plane's final position.

	"""

    negative_plane_angle: float = None
    """
	Definition of the angle formed among negative plane's initial position, coordinate center and negative plane's final position.

	"""

    def set_formed(self, formed: object):
        """


        Parameters
        ----------
        formed : object
                A list of entities to be inserted in object's member "formed". Preexisting entities will be discarded.

        """

    def remove_formed(self, formed: object):
        """


        Parameters
        ----------
        formed : object
                A list of entites to be removed from object's member "formed".

        """

    def clear_formed(self):
        """

        Remove all entities from object's member "formed".


        """

    def increase_formed_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around formed entities to be included also in object's member "formed".

        """

    def decrease_formed_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around formed entities to be excluded from object's member "formed".

        """

    def insert_transition(self, transition: object):
        """


        Parameters
        ----------
        transition : object
                A list of entities to be inserted in object's member "transition".

        """

    def set_transition(self, transition: object):
        """


        Parameters
        ----------
        transition : object
                A list of entities to be inserted in object's member "transition". Preexisting entities will be discarded.

        """

    def remove_transition(self, transition: object):
        """


        Parameters
        ----------
        transition : object
                A list of entites to be removed from object's member "transition".

        """

    def clear_transition(self):
        """

        Remove all entities from object's member "transition".


        """

    def increase_transition_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around transition and formed entities to be included also in object's member "transition".

        """

    def decrease_transition_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones aroud transition entities to be excluded from object's member "transition".

        """

    def insert_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be inserted in object's member "fixed".

        """

    def set_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be inserted in object's member "fixed". Preexisting entities will be discarded.

        """

    def remove_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be removed from object's member "fixed".

        """

    def clear_fixed(self):
        """

        Remove all entities from object's member "fixed".


        """

    def calculate_fixed(self):
        """

        Automatic calculation of fixed. The result will be inserted to object's member "fixed".


        """

    def insert_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints".

        """

    def set_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be included in object's member "constraints". Preexisting entities will be discarded.

        """

    def remove_constraints(self, constraints: object):
        """


        Parameters
        ----------
        constraints : object
                A list of MORPH_CONSTRAINT entities to be excluded from object's member "constraints".

        """

    def clear_constraints(self):
        """

        Remove all entities from object's member "constraints".


        """

    def insert_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be inserted in object's member "volume_finder".

        """

    def set_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be inserted in object's member "volume_finder". Preexisting entities will be discarded.

        """

    def remove_volume_finder(self, size_boxes: object):
        """


        Parameters
        ----------
        size_boxes : object
                A list of SIZEBOX entities to be removed from object's member "volume_finder".

        """

    def clear_volume_finder(self):
        """

        Remove all entities from object's member "volume_finder".


        """

    def set_coordinate(self, coordinate: object):
        """

        Set a new entity for coordinate system. Neutral axis will be represented by X axis and Bending axis by Y.


        Parameters
        ----------
        coordinate : object
                A coordinate entity.

        """

    def move_coordinate_to_cog(self):
        """

        Move coordinate origin to the center of gravity of formed entities.


        """

    def align_to_principal_axes(self):
        """

        Align the coordinate axes to the principal axes of formed entities.


        """

    def set_positive_plane_length(self, length: float):
        """

        Define bend length in mode 'Free Ends'. If needed, change Form mode prior to this action.


        Parameters
        ----------
        length : float
                Numerical value to set the distance among positive plane and coordinate system, across neutral axis.

        """

    def set_positive_plane_angle(self, angle: float):
        """

        Define bend angle in mode 'Free Ends'. If needed, change Form mode prior to this action.


        Parameters
        ----------
        angle : float
                Numerical value to define the angle formed among positive plane's initial position, coordinate center and positive plane's final position.

        """

    def set_negative_plane_length(self, length: float):
        """

        Define bend length in mode 'Free Ends'. If needed, change Form mode prior to this action.


        Parameters
        ----------
        length : float
                Numerical value to set the distance among negative plane and coordinate system, across neutral axis.

        """

    def set_negative_plane_angle(self, angle: float):
        """

        Define bend angle in mode 'Free Ends'. If needed, change Form mode prior to this action.


        Parameters
        ----------
        angle : float
                Numerical value to define the angle formed among negative plane's initial position, coordinate center and negative plane's final position.

        """

    def reset_positive_plane_length(self):
        """

        Reset object's member "positive_plane_length" to the maximum value. This action can be performed in 'Free Ends' mode. If needed, change Form mode prior to this action.


        """

    def reset_negative_plane_length(self):
        """

        Reset object's member "negative_plane_length" to the maximum value. This action can be performed in 'Free Ends' mode. If needed, change Form mode prior to this action.


        """

    def set_link_planes(self, link_planes: bool):
        """

        Enable planes linkage to bend, twist, taper and extend identically in both ends. Positive plane's bend length and angle, twist angle, taper and extend ratios will be used as reference.


        Parameters
        ----------
        link_planes : bool
                Input True to link planes movement. Input False to disable linking feature.

        """

    def set_improve_mesh(self, type: str, expand_zones: int):
        """

        Set mesh improvement to be applied after move and accept.


        Parameters
        ----------
        type : str
                Type of mesh improvement. Only 'None', 'Reconstruct', 'Smooth', 'Reshape' inputs are acceptable.

        expand_zones : int
                Numerical input for the number of expanded zones to be included in mesh improvement.

        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action.


        """

    def apply(self):
        """

        Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script.


        """

    def create_symmetric(self) -> object:
        """

        Create a symmetric DIRECT_FORM entity relative to the default symmetry plane. The current morph.Bend object doesn't have to be saved as DIRECT_FORM entity.


        Returns
        -------
        object
                The created MD_MOVE_BEND entity or None if symmetry failed.

        """

    def save_as_Direct_Form(self, name: str):
        """


        Parameters
        ----------
        name : str, optional
                The name of the entity to create.

        """

    def set_positive_plane_twist(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to set the twisting angle of positive plane cross-section orientation, across neutral axis.

        """

    def set_negative_plane_twist(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to set the twisting angle of negative plane cross-section orientation, across neutral axis.

        """

    def set_positive_plane_extend(self, e_ratio: float):
        """


        Parameters
        ----------
        e_ratio : float
                Numerical value to set the extending ratio of positive plane's side.

        """

    def set_negative_plane_extend(self, e_ratio: float):
        """


        Parameters
        ----------
        e_ratio : float
                Numerical value to set the extending ratio of negative plane's side.

        """

    def set_negative_plane_y_taper(self, y_ratio: float):
        """


        Parameters
        ----------
        y_ratio : float
                Numerical value to set the y-tapering ratio of negative plane's side.

        """

    def set_positive_plane_y_taper(self, y_ratio: float):
        """


        Parameters
        ----------
        y_ratio : float
                Numerical value to set the y-tapering ratio of positive plane's side.

        """

    def set_positive_plane_z_taper(self, z_ratio: float):
        """


        Parameters
        ----------
        z_ratio : float
                Numerical value to set the z-tapering ratio of positive plane's side.

        """

    def set_negative_plane_z_taper(self, z_ratio: float):
        """


        Parameters
        ----------
        z_ratio : float
                Numerical value to set the z-tapering ratio of negative plane's side.

        """

    def initial_positive_plane_length(self, length: float):
        """


        Parameters
        ----------
        length : float
                Numerical value to adjust the positive plane length for the initial state.

        """

    def initial_negative_plane_length(self, length: float):
        """


        Parameters
        ----------
        length : float
                Numerical value to adjust the negative plane length for the initial state.

        """

    def initial_positive_plane_angle(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to adjust the positive plane bending angle for the initial state.

        """

    def initial_negative_plane_angle(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to adjust the negative plane bending angle for the initial state.

        """

    def initial_positive_plane_twist(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to adjust the twisting angle of positive plane for the initial state.

        """

    def initial_negative_plane_twist(self, angle: float):
        """


        Parameters
        ----------
        angle : float
                Numerical value to adjust the twisting angle of negative plane for the initial state.

        """

    def initial_positive_plane_extend(self, e_ratio: float):
        """


        Parameters
        ----------
        e_ratio : float
                Numerical value to adjust the extending ratio of positive plane's side for the initial state.

        """

    def initial_negative_plane_extend(self, e_ratio: float):
        """


        Parameters
        ----------
        e_ratio : float
                Numerical value to adjust the extending ratio of positive plane's side for the initial state.

        """

    def initial_negative_plane_y_taper(self, y_ratio: float):
        """


        Parameters
        ----------
        y_ratio : float
                Numerical value to adjust the y-tapering ratio of negative plane's side for the initial state.

        """

    def initial_positive_plane_y_taper(self, y_ratio: float):
        """


        Parameters
        ----------
        y_ratio : float
                Numerical value to adjust the y-tapering ratio of positive plane's side for the initial state.

        """

    def insert_formed(self, formed: object):
        """


        Parameters
        ----------
        formed : object
                A list of entities to be inserted in object's member "formed".

        """

    def initial_negative_plane_z_taper(self, z_ratio: float):
        """


        Parameters
        ----------
        z_ratio : float
                Numerical value to adjust the z-tapering ratio of negative plane's side for the initial state.

        """

    def initial_positive_plane_z_taper(self, z_ratio: float):
        """


        Parameters
        ----------
        z_ratio : float
                Numerical value to adjust the z-tapering ratio of positive plane's side for the initial state.

        """

    def set_user_section(
        self, x: float, y: float, z: float, dx: float, dy: float, dz: float
    ):
        """

        Define a custom plane as reference for cross-sections, to be preserved along neutral line. User Section is defined by a vector normal to its plane.


        Parameters
        ----------
        x : float
                x coordinate of normal vector's origin

        y : float
                y coordinate of normal vector's origin

        z : float
                z coordinate of normal vector's origin

        dx : float
                dx value of normal vector

        dy : float
                dy value of normal vector

        dz : float
                dz value of normal vector

        """

    def clear_user_section(self):
        """

        Clear definition of User Section. This action will enable default plane sectioning.


        """

    def set_interpolation(self, interpolation: str):
        """

        Determin interpolation method to apply Twist and Taper values


        Parameters
        ----------
        interpolation : str
                Available options are 'Linear' or 'Quadratic'

        """

    def set_mode(self, mode: str):
        """

        Set mode of forming: either 'Free Ends' or 'Pinned Ends'. Form object is set by default to 'Free Ends' mode, unless initiallization is performed according to a DIRECT_FORM entity, where the mode is predefined.This action will reset Form state to its initial setup.


        Parameters
        ----------
        mode : str
                Accepted values are 'Free Ends' or 'Pinned Ends'.

        """

    def set_axes_displacement(self, neutral_axis: float, deflection_axis: float):
        """

        Set displacement of Neutral and Deflection axes in 'Pinned Ends' mode to define bending. If needed, change Form mode prior to this action.


        Parameters
        ----------
        neutral_axis : float
                Displacement of Neutral axis.

        deflection_axis : float
                Displacement of Deflection axis.

        """


class DCFeatureSlide:
    """

    A class defining methods for sliding a feature (bead, stamp, rib, hole) consisting of finite elements.

    See Also
    --------
    morph.DCFeatureCopy

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def slide_feature_example_with_ents():
                feat_ents = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]  # e.g. a set containing SHELL entities
                slide_obj = morph.DCFeatureSlide()
                slide_obj.set_feature_area(feat_ents)
                slide_obj.set_movement_type_free()
                coord_ent = base.GetEntity(
                    constants.NASTRAN, "CORD_NODES_R", a_coord_id
                )  # entity to define local coord.system
                slide_obj.set_translation_vector(
                    10.0, 2.0, -3.0
                )  # referring to dx, dy, dz components
                slide_obj.set_improve_mesh("Smooth", 2)
                slide_obj.apply()


            def slide_feature_example_with_feature():
                feat_ents = [base.GetEntity(constants.NASTRAN, "HOLE 3D", a_3d_hole_id)]
                slide_obj = morph.DCFeatureSlide()
                slide_obj.set_feature_area(feat_ents)
                some_more_shells = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]  # e.g. a set with some SHELL entities
                slide_obj.insert_feature_area(
                    some_more_shells
                )  # insert more shells to the feature area
                slide_obj.set_movement_type_on_surface()
                slide_obj.set_translation_vector(5.0, -3.0)  # now referring to ds and dt
                slide_obj.set_projection_distance_active(True)
                slide_obj.set_projection_distance(15.0)
                slide_obj.set_improve_mesh("Reconstruct", 1)
                slide_obj.apply()


            def slide_feature_example_on_path():
                curve_to_define_path = [base.GetEntity(constants.NASTRAN, "CURVE", a_curve_id)]
                feat_ents = [base.GetEntity(constants.NASTRAN, "STAMP", a_stamp_id)]
                slide_obj = morph.DCFeatureSlide()
                slide_obj.feature_area = feat_ents  # assign directly
                slide_obj.set_movement_type_follow_path()
                slide_obj.set_path(curve_to_define_path)
                slide_obj.set_movement_on_path("Glide")
                slide_obj.set_distance_on_path(24.0)
                slide_obj.apply()
                dc_ent = (
                    slide_obj.save_as_DC_Feature()
                )  # save the definition as a "DC_FEATURE_SLIDE" enity in database.


            def slide_feature_example_existing_dc_ent():
                dc_ent = base.GetEntity(constants.NASTRAN, "DC_FEATURE_SLIDE", a_sl_feat_ent_id)
                slide_obj = morph.DCFeatureSlide(
                    dc_ent
                )  # work (edit, morph) with an existing "DC_FEATURE_SLIDE" entity.
                unwanted_shells_on_surf = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]  # containing SHELL entities.
                slide_obj.remove_surface_area(unwanted_shells_on_surf)
                slide_obj.set_movement_type_free()
                coord_ent = base.GetEntity(
                    constants.NASTRAN, "CORD_NODES_R", a_coord_id
                )  # entity to define local coord.system
                slide_obj.set_coord(coord_ent)
                slide_obj.set_translation_vector(1.0, -1.0, 0.5)
                # slide_obj.apply()  # perform or not a morphing action. Anyway, changes in DC_FEATURE_SLIDE entity are preserved.

    """

    feature_area: object = None
    """
	A list of entities that represent the features to be morphed. The type of these entities can be SHELL, SHELLEDGE or a type of FEATURE group (HOLE 2D, HOLE 3D, RIB 2D, STAMP).

	"""

    surface_area: object = None
    """
	A list of SHELL entities that represent the surface on which the feature entities will slide.

	"""

    path: object = None
    """
	A list of entities (SHELLEDGE, CURVE) that define a path for feature entities to slide on.

	"""

    movement_type: str = None
    """
	A string that defines the movement type of slide. It can be one of the following strings: 
	'Free': A free movement according to a local Cartesian coordinate system established in the COG of the feature entities. 
	'OnSurface': Feature entities shall slide only on the underlying surface. Movement is defined by a local two-dimensional coordinate system corresponding to the surface's isoparametric directions. 
	'FollowPath' : Feature entities shall slide only on a defined path.

	"""

    movement_on_path: str = None
    """
	A string that defines if the movement on path will be of type 'Sweep' or 'Glide'.

	"""

    def set_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area". Preexisting entities will be discarded.

        """

    def insert_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area".

        """

    def remove_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be removed from object's member "feature_area".

        """

    def clear_feature_area(self):
        """

        Remove all entities from object's member "feature_area".


        """

    def set_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area". Preexisting entities will be discarded.

        """

    def insert_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area".

        """

    def remove_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be removed from object's member "surface_area".

        """

    def clear_surface_area(self):
        """

        Remove all entities from object's member "surface_area".


        """

    def set_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

        """

    def insert_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path".

        """

    def remove_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be removed from object's member "path".

        """

    def clear_path(self):
        """

        Remove all entities from object's member "path".


        """

    def set_movement_type_free(self):
        """

        Set object's member "movement_type" to "Free".


        """

    def set_movement_type_on_surface(self):
        """

        Set object's member "movement_type" to "OnSurface".


        """

    def set_movement_type_follow_path(self):
        """

        Set object's member "movement_type" to "FollowPath".


        """

    def set_movement_on_path(self, type: str):
        """

        Define the type of movement on path.


        Parameters
        ----------
        type : str
                'Sweep' or 'Glide'.

        """

    def save_as_DC_Feature(self) -> object:
        """

        Save the current DC Slide Feature configuration as a "DC_FEATURE_SLIDE" entity in ANSA database. The saved entity is returned by this method.


        Returns
        -------
        object
                The created "DC_FEATURE_SLIDE" entity.

        """

    def set_translation_vector(self, dx_or_ds: float, dy_or_dt: float, dz: float):
        """

        Define the translation vector for a 'Free' or 'OnSurface' translation of feature entities.


        Parameters
        ----------
        dx_or_ds : float
                The 'dx' component of translation corresponding to local X axis for a 'Free' movement type or the 'ds' component of translation corresponding to local S axis (first isoparametric direction of the surface) for an 'OnSurface' movement type.

        dy_or_dt : float
                The 'dy' component of translation corresponding to local Y axis for a 'Free' movement type or the 'dt' component of translation corresponding to local T axis (second isoparametric direction of the surface) for an 'OnSurface' movement type.

        dz : float, optional
                The 'dz' component of translation corresponding to local Z axis, required only for a 'Free' movement type.

        """

    def set_rotation_angles(self, rx_or_r: float, ry: float, rz: float):
        """

        Define the rotation angles for a 'Free' or 'OnSurface' rotation of feature entities.


        Parameters
        ----------
        rx_or_r : float
                The 'rx' component of a rotation angles vector corresponding to local X axis for a 'Free' movement type or the angle 'r' of the rotation around the normal axis to the surface for an 'OnSurface' movement type.

        ry : float, optional
                The 'ry' component of a rotation angles vector corresponding to local Y axis only for a 'Free' movement type.

        rz : float, optional
                The 'rz' component of a rotation angles vector corresponding to local Z axis only for a 'Free' movement type.

        """

    def set_distance_on_path(self, distance: float):
        """

        Define the distance that feature entities should slide along the defined path for a 'FollowPath' movement type.


        Parameters
        ----------
        distance : float
                The distance that feature entities should slide along the defined path.

        """

    def set_frozen_perimeters(self, perimeters_entities: object):
        """


        Parameters
        ----------
        perimeters_entities : object
                A list of one-dimensional entities (SHELLEDGE) to be regarded as 'frozen' during the morphing.

        """

    def clear_frozen_perimeters(self):
        """

        Cancel the marking of any perimeters (SHELLEDGE) as 'Frozen'.


        """

    def set_improve_mesh(self, type: str, zones: int):
        """

        Define the mesh improvement action to be applied after the sliding of feature entities.


        Parameters
        ----------
        type : str
                Mesh improvement action options: 'None', 'Reconstruct', 'Smooth', 'Reshape'

        zones : int, optional
                Number of zones around feature entities to be included in the mesh improvement action. Default: 0

        """

    def snap_to_feature_lines(self, active: bool):
        """


        Parameters
        ----------
        active : bool
                If 'True', feature entities will snap to feature lines during morphing.

        """

    def set_projection_direction(self, type: str):
        """

        Define the type of projection direction.


        Parameters
        ----------
        type : str
                For movement types 'Free' or 'FollowPath' the projection direction options are:
                - 'Free'
                - 'X_Axis'
                - 'Y_Axis'
                - 'Z_Axis'
                For movement type 'OnSurface' the projection direction options are:
                - 'Free'
                - 'Normal'

        """

    def set_projection_distance(self, distance: float):
        """


        Parameters
        ----------
        distance : float
                Maximum projection distance.

        """

    def set_projection_distance_active(self, active: bool):
        """


        Parameters
        ----------
        active : bool
                If 'True', morphing will respect the maximum projection distance and direction.

        """

    def apply(self):
        """

        Perform the morphing action (sliding of the feature entities). Mesh improvement actions defined by method 'set_improve_mesh' will be applied also after the call to this method.


        """

    def __init__(self, dc_feature_slide: object):
        """

        Constructor of class DCFeatureSlide.


        Parameters
        ----------
        dc_feature_slide : object, optional
                Use this argument to construct an instance of DCFeatureSlide class from an existing "DC_FEATURE_SLIDE" entity.

        """

    def set_coord(self, coord: object):
        """

        Define the local coordinate system according to which feature entities will be transformed (translations, rotations, scalings). The method is valid only for 'free' movement type.


        Parameters
        ----------
        coord : object
                A "COORD" type entity.

        """

    def create_symmetric(self) -> object:
        """

        Create a DC_FEATURE_SLIDE entity which is symmetric to the object's one according to the default symmetry plane.


        Returns
        -------
        object
                The created "DC_FEATURE_SLIDE" entity or None if symmetry operation failed.

        """


class DCFeatureCopy:
    """

    A class defining methods for copying a feature (bead, stamp, rib, hole) consisting of finite elements, in other positions on the mesh.

    Most of the members and the methods of this class are exactly the same with that of DCFeatureSlide class. The essential difference between these two classes, is that in DCFeatureSlide class, feature entities are really sliding on a surface or on a path while in the present class, DCFeatureCopy, the pattern of the selected feature entities is copied to other positions in the FE mesh. Therefore, the term "slide" in the subsequent description does not imply an actual sliding of the feature entities but the route in which this pattern will follow in order to be copied in new position. The parent pattern can be copied an arbitrary number of times in the FE mesh and this additional option is the attribute "steps" of the present class.

    See Also
    --------
    morph.DCFeatureSlide

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def copy_feature_example_with_ents():
                feat_ents = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]  # e.g. a set containing SHELL entities
                copy_obj = morph.DCFeatureCopy()
                copy_obj.set_feature_area(feat_ents)
                copy_obj.set_movement_type_free()
                copy_obj.set_steps_x(2)
                copy_obj.set_steps_y(0)  # define the number of "children" features to be created.
                copy_obj.set_array_distance(10.0)
                copy_obj.set_improve_mesh("Smooth", 2)
                copy_obj.apply()


            def copy_feature_example_on_path():
                curve_to_define_path = [base.GetEntity(constants.NASTRAN, "CURVE", a_curve_id)]
                feat_ents = [base.GetEntity(constants.NASTRAN, "STAMP", a_stamp_id)]
                copy_obj = morph.DCFeatureCopy()
                copy_obj.feature_area = feat_ents  # assign directly
                copy_obj.set_movement_type_follow_path()
                copy_obj.set_path(curve_to_define_path)
                copy_obj.set_movement_on_path("Glide")
                copy_obj.set_distance_on_path(12.0)
                copy_obj.set_distance_type("distance")
                copy_obj.set_steps(10)
                copy_obj.apply()
                dc_ent = (
                    copy_obj.save_as_DC_Feature()
                )  # save the definition as a "DC_FEATURE_COPY" enity in database.


            def copy_feature_example_circular():
                feat_ents = [base.GetEntity(constants.NASTRAN, "HOLE_3D", a_hole_id)]
                copy_obj = morph.DCFeatureCopy()
                copy_obj.insert_feature_area(feat_ents)
                copy_obj.set_pattern_circular()
                copy_obj.set_distance_type("extent")
                coord_ent = base.GetEntity(constants.NASTRAN, "CORD_NODES_C", a_coord_id)
                copy_obj.set_coord(
                    coord_ent
                )  # origin of coord_ent is the center of circular pattern and z axis the rotation axis
                copy_obj.set_circular_angle(45)
                copy_obj.set_steps(3)
                copy_obj.apply()


            def copy_feature_example_existing_dc_ent():
                dc_ent = base.GetEntity(constants.NASTRAN, "DC_FEATURE_COPY", a_copy_feat_ent_id)
                copy_obj = morph.DCFeatureSlide(
                    dc_ent
                )  # work (edit, morph) with an existing "DC_FEATURE_COPY" entity.
                copy_obj.set_movement_type_free()
                coord_ent = base.GetEntity(
                    constants.NASTRAN, "CORD_NODES_R", a_coord_id
                )  # entity to define local coord.system
                copy_obj.set_coord(coord_ent)
                copy_obj.set_steps(5)
                # copy_obj.apply()  # perform or not a morphing action. Anyway, changes in DC_FEATURE_COPY entity are preserved.

    """

    feature_area: object = None
    """
	A list of entities that represent the features to be morphed. The type of these entities can be SHELL, SHELLEDGE or a type of FEATURE group (HOLE 2D, HOLE 3D, RIB 2D, STAMP).

	"""

    surface_area: object = None
    """
	A list of SHELL entities that represent the surface on which the feature entities will slide.

	"""

    path: object = None
    """
	A list of entities (SHELLEDGE, CURVE) that define a path for feature entities to slide on.

	"""

    movement_type: str = None
    """
	A string that defines the movement type of slide. It can be one of the following strings: 
	'Free': A free movement according to a local Cartesian coordinate system established in the COG of the feature entities. 
	'OnSurface': Feature entities shall slide only on the underlying surface. Movement is defined by a local two-dimensional coordinate system corresponding to the surface's isoparametric directions. 
	'FollowPath' : Feature entities shall slide only on a defined path.

	"""

    movement_on_path: str = None
    """
	A string that defines if the movement on path will be of type 'Sweep' or 'Glide'.

	"""

    steps: int = None
    """
	Number of copies to be created from the parent pattern i.e. the entities in "feature_area" member.

	"""

    def set_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area". Preexisting entities will be discarded.

        """

    def insert_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area".

        """

    def remove_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be removed from object's member "feature_area".

        """

    def clear_feature_area(self):
        """

        Remove all entities from object's member "feature_area".


        """

    def set_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area". Preexisting entities will be discarded.

        """

    def insert_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area".

        """

    def remove_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be removed from object's member "surface_area".

        """

    def clear_surface_area(self):
        """

        Remove all entities from object's member "surface_area".


        """

    def set_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path". Preexisting entities will be discarded.

        """

    def insert_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be inserted in object's member "path".

        """

    def remove_path(self, path_entities: object):
        """


        Parameters
        ----------
        path_entities : object
                A list of entities to be removed from object's member "path".

        """

    def clear_path(self):
        """

        Remove all entities from object's member "path".


        """

    def set_movement_on_path(self, type: str):
        """

        Define the type of movement on path.


        Parameters
        ----------
        type : str
                'Sweep' or 'Glide'.

        """

    def save_as_DC_Feature(self):
        """

        Save the current DC Slide Feature configuration as a "DC_FEATURE_COPY" entity in ANSA database. The saved entity is returned by this method.


        """

    def set_distance_on_path(self, distance: float):
        """

        Define the distance that feature entities should slide along the defined path for a 'FollowPath' movement type.


        Parameters
        ----------
        distance : float
                The distance that feature entities should slide along the defined path.

        """

    def set_improve_mesh(self, type: str, zones: int):
        """

        Define the mesh improvement action to be applied after the sliding of feature entities.


        Parameters
        ----------
        type : str
                Mesh improvement action options: 'None', 'Reconstruct', 'Smooth', 'Reshape'

        zones : int
                Number of zones around feature entities to be included in the mesh improvement action. Default: 0

        """

    def snap_to_feature_lines(self, active: bool):
        """


        Parameters
        ----------
        active : bool
                If 'True', feature entities will snap to feature lines during morphing.

        """

    def set_projection_direction(self, type: int):
        """

        Define the type of projection direction.


        Parameters
        ----------
        type : int
                For movement types 'Free' or 'FollowPath' the projection direction options are:
                - 'Free'
                - 'X_Axis'
                - 'Y_Axis'
                - 'Z_Axis'
                For movement type 'OnSurface' the projection direction options are:
                - 'Free'
                - 'Normal'

        """

    def set_projection_distance(self, distance: int):
        """


        Parameters
        ----------
        distance : int
                Maximum projection distance.

        """

    def set_projection_distance_active(self, active: bool):
        """


        Parameters
        ----------
        active : bool
                If 'True', morphing will respect the maximum projection distance and direction.

        """

    def apply(self):
        """

        Perform the morphing action (copying of the feature entities). Mesh improvement actions defined by method 'set_improve_mesh' will be applied also after the call to this method.


        """

    def set_steps(self, num_steps: int):
        """


        Parameters
        ----------
        num_steps : int
                Sets the value "num_steps" in object's member "steps".

        """

    def __init__(self, dc_feature_copy: object):
        """

        The constructor of class DCFeatureCopy.


        Parameters
        ----------
        dc_feature_copy : object, optional
                Use this argument to construct an instance of DCFeatureCopy class from an existing "DC_FEATURE_COPY" entity.

        """

    def set_coord(self, coord: object):
        """

        Define the local coordinate system according to which feature entities will be pattern copied.


        Parameters
        ----------
        coord : object
                A "COORD" type entity.

        """

    def create_symmetric(self) -> object:
        """

        Create a DC_FEATURE_COPY entity which is symmetric to the object's one according to the default symmetry plane.


        Returns
        -------
        object
                The created "DC_FEATURE_COPY" entity or None if symmetry operation failed.

        """

    def set_pattern_array(self):
        """

        Set Pattern type 'Array'


        """

    def set_pattern_circular(self):
        """

        Set Pattern type 'Circular'


        """

    def set_pattern_follow_path(self):
        """

        Set Pattern type 'Follow Path'


        """

    def set_distance_type(self, distance_type: str):
        """

        Set Distance type


        Parameters
        ----------
        distance_type : str
                A string to define distance type. Accepts either 'distance' or 'extent' for input value.

        """

    def set_array_distance(self, dx: float, dy: float):
        """

        Set 'dx' and 'dy' distances for 'Array' pettern.


        Parameters
        ----------
        dx : float
                A value for distancing in 'dx' direction

        dy : float
                A value for distancing in 'dy' direction

        """

    def set_circular_angle(self, rz: float):
        """

        Set angle value for 'Circular' pattern


        Parameters
        ----------
        rz : float
                A value to define angular distance.

        """


class ChangeHoleDiameter:
    """

    A class providing methods for changes in the diameter of ANSA hole entities.

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def change_hole_example():
                hole_a = base.GetEntity(constants.NASTRAN, "HOLE 2D", a_hole_id)
                hole_b = base.GetEntity(constants.NASTRAN, "HOLE 2D", another_hole_id)

                change_hole_obj = morph.ChangeHoleDiameter(hole_a)
                change_hole_obj.move_on_surface()
                change_hole_obj.set_target_diameter(40.0)
                change_hole_obj.apply()

                another_hole_obj = morph.ChangeHoleDiameter(hole_b)
                another_hole_obj.set_radial_offset(6.0)
                another_hole_obj.apply()
                another_hole_obj.set_offset(5.0)
                another_hole_obj.apply()
                another_hole_obj.save_as_parameter("Holes_offset")

    """

    def __init__(self, hole_2d_feature: object):
        """

        Constructor of class ChangeHoleDiameter.


        Parameters
        ----------
        hole_2d_feature : object
                A list of "HOLE 2D" entities.

        """

    def set_offset(self, offset_value: float):
        """

        Define the change in hole's diameter to be perfomed via offset of the hole's boundary edges.


        Parameters
        ----------
        offset_value : float
                The value of the offset of hole's boundary edges.

        """

    def set_radial_offset(self, radial_offset_value: float):
        """

        Define the change in hole's diameter to be perfomed via radial offset of the hole's boundary edges.


        Parameters
        ----------
        radial_offset_value : float
                The value of the radial offset of hole's boundary edges.

        """

    def set_target_diameter(self, diameter: float):
        """

        Define the absolute value of hole's diameter to be set.


        Parameters
        ----------
        diameter : float
                The target value of hole's diameter.

        """

    def move_on_middle_plane(self):
        """

        Set the morphing of the hole to be perfomed by movements in the middle plane of the hole.


        """

    def move_on_surface(self):
        """

        Set the morphing of the hole to be performed by movements on hole's surface.


        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is not called afterwards, morphing action will be canceled in the end of the script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action's result.


        """

    def apply(self):
        """

        Perform and confirm the morphing action. Unless this method has been called, the morphing action of the object will be canceled in the end of the script.


        """

    def save_as_parameter(self, name: str):
        """


        Parameters
        ----------
        name : str, optional
                The desired name of the saved parameter
                (Default:'ParameterHoles')

        """


class ConstraintSteadySection:
    """

    Class providing methods to define a constraint of type 'Steady Section' to be included in a direct morphing action. The entities belonging to such a constraint shall retain their cross section along a neutral line during the morphing action. Class can be used either to create a MORPH_CONSTRAINT entity of 'Steady Section' type or to modify an existing one.

    See Also
    --------
    morph.DFM, morph.ConstraintPlanar, morph.ConstraintRigid, morph.ConstraintScaled, morph.ConstraintDirectional, morph.ConstraintPathFollower, morph.ConstraintFlanges

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import morph


            def steady_section_constraint_example_1(
                list_of_steady_section_entities, list_of_neutral_line_entities
            ):
                # create a steady section constraint object through ConstraintSteadySection class and add it to a DFM parameter.
                steady_sec = morph.ConstraintSteadySection()
                steady_sec.set_entities(list_of_steady_section_entities)
                steady_sec.neutral_line_entities = list_of_neutral_line_entities

                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(steady_sec)


            def steady_section_constraint_example_2(
                list_of_steady_section_entities, list_of_neutral_line_entities
            ):
                # create a steady section constraint object from existing MORPH_CONSTRAINT and add it to a DFM parameter.
                existing_steady_section_constraint = base.GetEntity(
                    constants.NASTRAN, "MORPH_CONSTRAINT", constraint_id
                )

                steady_sec = morph.ConstraintSteadySection(existing_steady_section_constraint)
                steady_sec.insert_entities(list_of_steady_section_entities)
                steady_sec.set_neutral_line(list_of_neutral_line_entities)
                steady_sec.calculate_bounds()

                param = base.GetEntity(constants.NASTRAN, "PARAMETERS", parameter_id)
                dfm = morph.DFM(param)
                dfm.add_constraint_obj(steady_sec)


            def register_constraint_example(list_of_neutral_line_entities):
                # create a new MORPH_CONSTRAINT entity through ConstraintSteadySection class.
                steady_section_entities = [base.GetEntity(constants.NASTRAN, "SET", a_set_id)]

                steady_sec = morph.ConstraintSteadySection()
                steady_sec.set_entities(steady_section_entities)
                steady_sec.insert_neutral_line(list_of_neutral_line_entities)

                new_steady_section_constraint = (
                    steady_sec.reg()
                )  # retrieve the created MORPH_CONSTRAINT.

    """

    morphed: object = None
    """
	A list of entities to be in the transition zone.

	"""

    bounds: object = None
    """
	A list of entities set as fixed perimeters.

	"""

    entities: object = None
    """
	A list of entities constrained to preserve their cross section shape.

	"""

    neutral_line_entities: object = None
    """
	A list of entities to describe a neutral line across which the cross section shall be preserved.

	"""

    def insert_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed".

        """

    def set_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be inserted in object's member "morphed". Preexisting entities will be discarded.

        """

    def remove_morphed(self, morphed: object):
        """


        Parameters
        ----------
        morphed : object
                A list of entities to be removed from object's member "morphed".

        """

    def clear_morphed(self):
        """

        Remove all entities from object's member "morphed".


        """

    def insert_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds".

        """

    def set_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be inserted in object's member "bounds". Preexisting entities will be discarded.

        """

    def remove_bounds(self, bounds: object):
        """


        Parameters
        ----------
        bounds : object
                A list of entities to be removed from object's member "bounds".

        """

    def clear_bounds(self):
        """

        Remove all entities from object's member "bounds".


        """

    def calculate_bounds(self):
        """

        Automatic calculation of bounds. The result will be inserted to object's member "bounds".


        """

    def increase_morphed_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be included also in object's member "morphed".

        """

    def decrease_morphed_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                Number of zones around morphed entities to be excluded from object's member "morphed".

        """

    def insert_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities".

        """

    def set_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be inserted in object's member "entities". Preexisting entities will be discarded.

        """

    def remove_entities(self, entities: object):
        """


        Parameters
        ----------
        entities : object
                A list of entities to be excluded from object's member "entities".

        """

    def clear_entities(self):
        """

        Remove all entities from object's member "entities".


        """

    def __init__(self, steady_section_constraint: object):
        """

        Constructor of class ConstraintSteadySection.


        Parameters
        ----------
        steady_section_constraint : object, optional
                MORPH_CONSTRAINT entity of Steady Section type.

        """

    def reg(self):
        """

        Create the MORPH_CONSTRAINT entity from a ConstraintScaled object and register it in the database.


        """

    def insert_neutral_line(self, neutral_line_entities: object):
        """


        Parameters
        ----------
        neutral_line_entities : object
                A list of entities to be inserted in object's member "neutral_line_entities"

        """

    def set_neutral_line(self, neutral_line_entities: object):
        """


        Parameters
        ----------
        neutral_line_entities : object
                A list of entities to be inserted in object's member "neutral_line_entities". Preexisting entities will be discarded.

        """

    def remove_neutral_line(self, neutral_line_entities: object):
        """


        Parameters
        ----------
        neutral_line_entities : object
                A list of entities to be removed from object's member "neutral_line_entities".

        """

    def clear_neutral_line(self):
        """

        Remove all entities from object's member "neutral_line_entities".


        """


class TubesDepenetrate:
    """

     Class that facilitates the automatic fix of penetrations between tubes FE and their surroundings.

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def fix_tubes_penetrations():
                tubes_properties_ids = [20089, 13008, 3998]
                surrounding_properties_ids = [1009, 234, 135]

                tb_dp = morph.TubesDepenetrate()

                # Load tubes properties (shell or solid). Obligatory
                tubes_properties = []
                for current_id in tubes_properties_ids:
                    tubes_properties.append(base.GetEntity(constants.NASTRAN, "PSHELL", current_id))
                # Load surrounding properties (shell). Optional. If omitted, every remaining property than tubes will be loaded.
                surrounding_properties = []
                for current_id in surrounding_properties_ids:
                    surrounding_properties.append(
                        base.GetEntity(constants.NASTRAN, "PSHELL", current_id)
                    )
                # (Optional) Configure options.
                tb_dp.load_tubes_properties(tubes_properties)
                tb_dp.load_surrounding_properties(surrounding_properties)
                tb_dp.quad_projection = "split_to_2_trias"
                tb_dp.thickness_definition = "nodal_thickness"
                tb_dp.round_shell_edges = True
                tb_dp.solution_method = "transform"

                model_ready = tb_dp.validate()

                if model_ready == "READY_TO_MORPH":
                    print(
                        tb_dp
                    )  # optional. Print object's info. Contains the configuration information.
                    tb_dp.run()  # MAIN ACTION.
                    print("Initial penetration pairs")
                    print(tb_dp.get_penetration_pairs("initial"))
                    print(
                        "Initial total penetration depth:",
                        tb_dp.get_total_penetration_depth("initial"),
                    )
                    print("-------------------------")
                    print("After transform")
                    print(tb_dp.get_penetration_pairs("transform"))
                    print(
                        "After transform, total penetration depth:",
                        tb_dp.get_total_penetration_depth("transform"),
                    )
                    morph_boxes = (
                        tb_dp.build_morphing_boxes()
                    )  # get cylindrical morphing boxes for further use.
                else:
                    print("This went wrong:", model_ready)

    """

    tubes_series_separation_angle: float = None
    """
	Angle (in degrees, between 0 and 90) based on which tubes series can be separated. Default: 75.

	"""

    solution_method: str = None
    """
	Penetrations' fix method: 'transform', 'transform_and_resize'.  Default: 'transform'

	"""

    factor_distance: float = None
    """
	Penetration parametric option. Default: 1.

	"""

    check_same_pids: bool = None
    """
	Penetration parametric option. Default: FalseMembers

	"""

    allow_planar_self_proximities: bool = None
    """
	Penetration parametric option. Default: False

	"""

    round_shell_edges: bool = None
    """
	Penetration parametric option. Default: True

	"""

    edge_to_edge: str = None
    """
	Penetration parametric option: 'check_single_edges', 'check_all_edges', 'check_no_edges'. Default: 'check_single_edges'

	"""

    quad_projection: str = None
    """
	Penetration parametric option: 'preserve', 'split_to_2_trias', 'split_to_4_trias'. Default: 'preserve'

	"""

    thickness_definition: str = None
    """
	Penetration parametric option: 'segment_thickness', 'nodal_thickness', 'user_thickness'. Default: 'segment_thickness'

	"""

    calculate_nodes_thickness_from: str = None
    """
	Penetration parametric option: 'model', 'all'. Default: 'model'.

	"""

    def load_tubes_properties(self, properties: object) -> object:
        """

        Load the PROPERTY entities that represent the tubes.


        Parameters
        ----------
        properties : object
                An iterable of shell or solid PROPERTY entities.

        Returns
        -------
        object

        """

    def unload_tubes_properties(self, properties: object) -> object:
        """

        Unload the tubes PROPERTY entities from object.


        Parameters
        ----------
        properties : object
                An iterable of shell or solid PROPERTY entities.

        Returns
        -------
        object

        """

    def clear_tubes_properties(self) -> object:
        """

        Clear the selection of tubes PROPERTY entities.


        Returns
        -------
        object

        """

    def load_surrounding_properties(self, properties: object) -> object:
        """

        Load the PROPERTY entities that represent the surrounding entities which should not penetrate with tubes.In case no surrounding properties are loaded when method ".run()" is called, all the model shell properties except for the ones already included in tubes properties, shall be loaded as surrounding properties.


        Parameters
        ----------
        properties : object
                An iterable of shell PROPERTY entities.

        Returns
        -------
        object

        """

    def unload_surrounding_properties(self, properties: object) -> object:
        """

        Unload the surrounding PROPERTY entities from object.


        Parameters
        ----------
        properties : object
                An iterable of shell PROPERTY entities.

        Returns
        -------
        object

        """

    def clear_surrounding_properties(self) -> object:
        """

        Clear the selection of surrounding PROPERTY entities.


        Returns
        -------
        object

        """

    def load_dragged_elements(self, elements: object) -> object:
        """

        Load secondary elements (RBE2, RBE3, RBAR, CBUSH, CBEAM etc...) so they are dragged alongside tubes elements during morphing.


        Parameters
        ----------
        elements : object
                An iterable of standard finite elements (excluding shell and solids).

        Returns
        -------
        object

        """

    def unload_dragged_elements(self, elements: object) -> object:
        """

        Unload dragged elements (RBE2, RBE3, RBAR, CBUSH, CBEAM etc...) from object.


        Parameters
        ----------
        elements : object
                An iterable of standard finite elements excluding shells and solids.

        Returns
        -------
        object

        """

    def clear_dragged_elements(self) -> object:
        """

        Clear the selection of dragged elements.


        Returns
        -------
        object

        """

    def load_fixed_grids(self, grids: object) -> object:
        """

        Load GRIDs that should stay fixed during morphing.


        Parameters
        ----------
        grids : object
                An iterable of GRID entities.

        Returns
        -------
        object

        """

    def unload_fixed_grids(self, grids: object) -> object:
        """

        Unload fixed GRIDs from object.


        Parameters
        ----------
        grids : object
                An iterable of GRID entities.

        Returns
        -------
        object

        """

    def clear_fixed_grids(self) -> object:
        """

        Clear the selection of fixed GRIDs.


        Returns
        -------
        object

        """

    def validate(self) -> str:
        """

        Check if the object is valid for run. Use this method, optionally, before calling method ".run()" to assure that penetration fix is able to start.


        Returns
        -------
        str
                'READY_TO_MORPH' : the model is ready to apply the morphing'MORPHED': the model is already morphed'NOT_READY__EMPTY_LIST_OF_TUBES_PROPERTIES': Cannot morph. No tube property defined.

        """

    def run(self) -> object:
        """

        Run the automatic penetration fix process. This may take a while depending on the complexity of the model. After this method is called, no modifications of object's setup (tubes properties, dragged elements etc.) are allowed.


        Returns
        -------
        object

        """

    def cancel(self) -> object:
        """

        Cancel the morphing action. All GRIDs return to their initial position.


        Returns
        -------
        object

        """

    def build_morphing_boxes(self) -> object:
        """

        Build cylindrical morphing boxes out of the tubes.


        Returns
        -------
        object
                A list of MORPHBOX entities.

        """

    def get_penetration_pairs(self, state: str) -> object:
        """


        Parameters
        ----------
        state : str
                Desired state of tubes: 'initial', 'transform', 'transform_and_resize'

        Returns
        -------
        object
                A list of tuples. Each tuple contains two entities and represents a penetration pair with one entity (shell or solid) belonging to tubes and the other entity (shell) belonging to the surrounding properties.

        """

    def get_total_penetration_depth(self, state: str) -> float:
        """

        Get the total penetration depth of all penetration pairs.


        Parameters
        ----------
        state : str
                Desired state of tubes: 'initial', 'transform', 'transform_and_resize'.

        Returns
        -------
        float
                The total penetration depth as sum of all penetration pairs' depth.

        """


class ChangeTubeDiameter:
    """

    A class providing methods for changes in the diameter of ANSA HOLE 3D entities.

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def change_tube_example():
                tube_a = base.GetEntity(constants.NASTRAN, "HOLE 3D", a_tube_id)
                tube_b = base.GetEntity(constants.NASTRAN, "HOLE 3D", another_tube_id)

                change_tube_obj = morph.ChangeTubeDiameter(tube_a)
                change_tube_obj.move_hole_on_surface()
                change_tube_obj.set_target_diameter(40.0)
                change_tube_obj.apply()

                another_tube_obj = morph.ChangeTubeDiameter(tube_b)
                another_tube_obj.set_radial_offset(6.0)
                another_tube_obj.move_hole_on_radius()
                another_tube_obj.apply()
                another_tube_obj.save_as_parameter("Tubes_on_radius")

    """

    def __init__(self, hole_3d_feature: object):
        """

        Constructor of class ChangeTubeDiameter.


        Parameters
        ----------
        hole_3d_feature : object
                A list of "HOLE 3D" entities.

        """

    def set_radial_offset(self, radial_offset_value: float):
        """

        Define the change in hole's diameter to be perfomed via radial offset of the tube's entities.


        Parameters
        ----------
        radial_offset_value : float
                The value of the radial offset of tube's entities

        """

    def set_target_diameter(self, diameter: float):
        """

        Define the absolute value of tube's diameter to be set. Notice that both diameter 1 and 2 will be set to the same value.


        Parameters
        ----------
        diameter : float
                The target value of tube's diameter

        """

    def move_hole_on_radius(self):
        """

        Set the morphing of the hole perimeters at the top and bottom of the tube to be performed on the radial direction.


        """

    def move_hole_on_surface(self):
        """

        Set the morphing of the hole perimeters at the top and bottom of the tube to be performed by movements on surrounding surface.


        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is not called afterwards, morphing action will be canceled in the end of the script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action's result.


        """

    def apply(self):
        """

        Perform and confirm the morphing action. Unless this method has been called, the morphing action of the object will be canceled in the end of the script.


        """

    def save_as_parameter(self, name: str):
        """


        Parameters
        ----------
        name : str, optional
                The desired name of the saved parameter.
                (Default:'ParameterTubes')

        """


class DCCrossSection:
    """

    A class defining methods for changing the design of a cross section to morph surrounding area.

    Examples
    --------
    ::

            from ansa import base, morph, constants


            def dc_cross_section():
                dc_cross = morph.DCCrossSection()
                dc_cross.set_action_area([base.GetEntity(constants.NASTRAN, "SET", a)])
                dc_cross.set_transition([base.GetEntity(constants.NASTRAN, "SET", b)])
                dc_cross.calculate_fixed()

                dc_cross.set_cross_section(base.GetEntity(constants.NASTRAN, "CROSS_SECTION", c))
                dc_cross.align_to_principal_axes()
                dc_cross.swap_width_height_axes()

                width_rigids = [
                    base.GetEntity(constants.NASTRAN, "CROSS_CURVE", ca),
                    base.GetEntity(constants.NASTRAN, "CROSS_CURVE", 9),
                ]
                height_rigids = [base.GetEntity(constants.NASTRAN, "CROSS_CURVE", cb)]
                height_frozen = [
                    base.GetEntity(constants.NASTRAN, "CROSS_CURVE", cc),
                    base.GetEntity(constants.NASTRAN, "CROSS_CURVE", 2),
                ]

                dc_cross.width_set_rigid(width_rigids)
                dc_cross.height_set_rigid(height_rigids)
                dc_cross.height_set_frozen(height_frozen)

                dc_cross.set_width(10)
                dc_cross.set_height(10)
                dc_cross.apply()

                dc_cross.save_as_DC_CrossSection()

    """

    action_area: object = None
    """
	A list of entities that will be directly affected from the cross section design changes.

	"""

    transition_area: object = None
    """
	A list of entities that will be morphed due to design changes on cross section and action area.

	"""

    fixed: object = None
    """
	A list of entities that represent the bounds of transition area and will not be morphed.

	"""

    cross_section: object = None
    """
	The CROSS_SECTION entity on which the design changes will take place.

	"""

    def set_action_area(self, action_area: object):
        """


        Parameters
        ----------
        action_area : object
                A list of entities to be inserted in object's member "action_area".Preexisting entities will be discarded.

        """

    def insert_action_area(self, action_area: object):
        """


        Parameters
        ----------
        action_area : object
                A list of entities to be inserted in object's member "action_area".

        """

    def remove_action_area(self, action_area: object):
        """


        Parameters
        ----------
        action_area : object
                A list of entities to be removed from object's member "action_area".

        """

    def clear_action_area(self):
        """

        Remove all entities from object's member "action_aera".


        """

    def set_transition(self, transition: object):
        """


        Parameters
        ----------
        transition : object
                A list of entities to be inserted in object's member "transition_area". Preexisting entities will be discarded.

        """

    def insert_transition(self, transtition: object):
        """


        Parameters
        ----------
        transtition : object
                A list of entities to be inserted in object's member "transtion_area"

        """

    def clear_transition(self):
        """

        Remove all entities from object's member "transition_area"


        """

    def remove_transition(self, transition: object):
        """


        Parameters
        ----------
        transition : object
                A list of entities to be removed from object's member "transition_area".

        """

    def increase_action_area_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                A number of zones to increase the "action_area"

        """

    def decrease_action_area_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                A number of zones to decrease the "action_area"

        """

    def decrease_transition_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                A number of zones to decrease the "transition_area"

        """

    def increase_transition_zone(self, zones: int):
        """


        Parameters
        ----------
        zones : int
                A number of zones to increase the "transition_area"

        """

    def set_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be inserted in object's member "fixed". Preexisting entities will be discarded.

        """

    def insert_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be inserted in object's member "fixed".

        """

    def remove_fixed(self, fixed: object):
        """


        Parameters
        ----------
        fixed : object
                A list of entities to be removed from object's member "fixed".

        """

    def clear_fixed(self):
        """

        Remove all entities from object's member "fixed".


        """

    def calculate_fixed(self):
        """

        Auto calculate "fixed" entities.


        """

    def set_cross_section(self, cross_section: object):
        """


        Parameters
        ----------
        cross_section : object
                A CROSS_SECTION entity to be inserted in object's member "cross_section". Preexisting entity will be discarded.

        """

    def set_points_cross_section(self, points: object):
        """


        Parameters
        ----------
        points : object
                A list of two or three points. Points are defined by a list of three doubles representing x,y, z coordinates.

        """

    def width_insert_rigid(self, width_rigid: object):
        """


        Parameters
        ----------
        width_rigid : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the rigid components of design change across Width axis.

        """

    def width_set_rigid(self, width_rigid: object):
        """


        Parameters
        ----------
        width_rigid : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the rigid components of design change across Width axis. Preexisting entities will be discarded.

        """

    def height_insert_rigid(self, height_rigid: object):
        """


        Parameters
        ----------
        height_rigid : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the rigid components of design change across Height axis.

        """

    def height_set_rigid(self, height_rigid: object):
        """


        Parameters
        ----------
        height_rigid : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the rigid components of design change across Height axis. Preexisting entities will be discarded.

        """

    def width_insert_deformed(self, width_deformed: object):
        """


        Parameters
        ----------
        width_deformed : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the deformed components of design change across Width axis.

        """

    def width_set_deformed(self, width_deformed: object):
        """


        Parameters
        ----------
        width_deformed : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the deformed components of design change across Width axis. Preexisting entities will be discarded.

        """

    def height_insert_deformed(self, height_deformed: object):
        """


        Parameters
        ----------
        height_deformed : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the deformed components of design change across Height axis.

        """

    def height_set_deformed(self, height_deformed: object):
        """


        Parameters
        ----------
        height_deformed : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the deformed components of design change across Height axis. Preexisting entities will be discarded.

        """

    def width_insert_frozen(self, width_frozen: object):
        """


        Parameters
        ----------
        width_frozen : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the frozen components of design change across Width axis.

        """

    def width_set_frozen(self, width_frozen: object):
        """


        Parameters
        ----------
        width_frozen : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the frozen components of design change across Width axis. Preexisting entities will be discarded.

        """

    def height_insert_frozen(self, height_frozen: object):
        """


        Parameters
        ----------
        height_frozen : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the frozen components of design change across Height axis.

        """

    def height_set_frozen(self, height_frozen: object):
        """


        Parameters
        ----------
        height_frozen : object
                A list of CROSS_CURVE entities that belong to object's member "cross_section" and will be inserted to the frozen components of design change across Height axis. Preexisting entities will be discarded.

        """

    def align_to_cross_section_axes(self):
        """

        Width and Height axes will be aligned to X and Y axes of the "cross_section" member, respectively.


        """

    def align_to_principal_axes(self):
        """

        Width and Height axes will be aligned to X and Y proncipal axes of "cross_section" member respectively.


        """

    def swap_width_height_axes(self):
        """

        Swap Width and Height axes.


        """

    def save_as_DC_CrossSection(self):
        """

        Save the definition of the object under a DC_CROSS_SECTION entity


        """

    def set_width(self, width: float):
        """


        Parameters
        ----------
        width : float
                A value to set Width design change.

        """

    def set_height(self, height: float):
        """


        Parameters
        ----------
        height : float
                A value to set Height design change.

        """

    def preview(self):
        """

        Preview the result of the morphing action. WARNING: Unless method "apply" is called, the morphing action will be finally cancelled in the end of the python script.


        """

    def disable_preview(self):
        """

        Disable the preview of the morphing action.


        """

    def apply(self):
        """

        Perform the morphing action and confirm it. After the call to "apply" method, the morphing is permanent and the object is able to perform another morphing with another arbitrary configuration. WARNING: Unless a call to this method, the morphing action will be cancelled at the end of the Python script.


        """


class DCFeatureScale:
    """

    A class defining methods for scaling a feature (bead, stamp, rib, hole) consisting of finite elements or shells or lines.

    Examples
    --------
    ::

            from ansa import base, constants, morph


            def scale_feature_example_with_ents():
                feat_ents = [
                    base.GetEntity(constants.NASTRAN, "SET", a_set_id)
                ]  # e.g. a set containing SHELL entities
                scale_obj = morph.DCFeatureScale()
                scale_obj.set_feature_area(feat_ents)
                scale_obj.set_improve_mesh("Smooth", 2)
                scale_obj.set_scale_factors(1.0, 1.0, 1.9)  # non-uniform scaling at z axis
                scale_obj.apply()
                scale_dc = scale_obj.save_as_DC_Feature()

    """

    feature_area: object = None
    """
	A list of entities that represent the features to be morphed. The type of these entities can be SHELL, SHELLEDGE or a type of FEATURE group (HOLE 2D, HOLE 3D, RIB 2D, STAMP).

	"""

    surface_area: object = None
    """
	A list of SHELL entities that represent the surface on which the feature entities will slide.

	"""

    def set_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area". Preexisting entities will be discarded.

        """

    def insert_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be inserted in object's member "feature_area".

        """

    def remove_feature_area(self, feature_area_entities: object):
        """


        Parameters
        ----------
        feature_area_entities : object
                A list of entities to be removed from object's member "feature_area".

        """

    def clear_feature_area(self):
        """

        Remove all entities from object's member "feature_area".


        """

    def set_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area". Preexisting entities will be discarded.

        """

    def insert_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be inserted in object's member "surface_area".

        """

    def remove_surface_area(self, surface_area_entities: object):
        """


        Parameters
        ----------
        surface_area_entities : object
                A list of entities to be removed from object's member "surface_area".

        """

    def clear_surface_area(self):
        """

        Remove all entities from object's member "surface_area".


        """

    def save_as_DC_Feature(self):
        """

        Save the current DC Slide Feature configuration as a "DC_FEATURE_SCALE" entity in ANSA database. The saved entity is returned by this method.


        """

    def set_improve_mesh(self, type: str, zones: int):
        """

        Define the mesh improvement action to be applied after the sliding of feature entities.


        Parameters
        ----------
        type : str
                Mesh improvement action options: 'None', 'Reconstruct', 'Smooth', 'Reshape'

        zones : int, optional
                Number of zones around feature entities to be included in the mesh improvement action. Default: 0

        """

    def apply(self):
        """

        Perform the morphing action (scaling of the feature entities). Mesh improvement actions defined by method 'set_improve_mesh' will be applied also after the call to this method.


        """

    def __init__(self, dc_feature_scale: object):
        """

        Constructor of class DCFeatureScale.


        Parameters
        ----------
        dc_feature_scale : object, optional
                Use this argument to construct an instance of DCFeatureScale class from an existing "DC_FEATURE_SCALE" entity.

        """

    def snap_to_feature_lines(self, active: bool):
        """


        Parameters
        ----------
        active : bool
                If 'True', feature entities will snap to feature lines during morphing.

        """

    def set_scale_factors(self, fx: float, fy: float, fz: float):
        """


        Parameters
        ----------
        fx : float
                Value of scale factor in x axis.

        fy : float
                Value of scale factor in y axis.

        fz : float
                Value of scale factor in z axis.

        """

    def set_frozen_perimeters(self, perimeters_entities: object):
        """


        Parameters
        ----------
        perimeters_entities : object
                A list of one-dimensional entities (SHELLEDGE) to be regarded as 'frozen' during the morphing.

        """

    def set_coord(self, coord: object):
        """

        Define the local coordinate system according to which feature entities will be scaled.


        Parameters
        ----------
        coord : object
                A "COORD" type entity.

        """


class ParamConnectionChain:
    """

    Class providing methods to define a Connection Chain Morph Parameter and either apply morphing actions, or register a new parameter.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base, morph


            def main():
                param = morph.ParamConnectionChain()
                param.contents = base.GetEntity(0, "CONNECTION_CHAIN", a_id)
                param.change_density = 1
                param.force_equal_spacing = False
                param.register("connection_chain")

                param = morph.ParamConnectionChain(base.GetEntity(0, "PARAMETERS", b_id))
                param.change_density = 0
                param.apply(2)

    """

    contents: object = None
    """
	A list of CONNECTION_CHAIN entities on which the parameter will be applied.

	"""

    change_density: int = None
    """
	An integer to represent the index among the following cases:
	0: Change density by factor
	1: Set Connection Count
	2: Set Spacing

	"""

    force_equal_spacing: bool = None
    """
	A boolean representing the state of forcing equal spacing or not.
	Applys only for the first 2 modes of density change types.

	"""

    def __init__(self, connection_chain_parameter: object) -> object:
        """

        Constructor of class ParamConnectionChain


        Parameters
        ----------
        connection_chain_parameter : object, optional
                An entity PARAMETERS of CONNECTION CHAIN type.

        Returns
        -------
        object

        """

    def register(self, name: str) -> object:
        """

        Register a new PARAMETER of CONNECTION CHAIN type.


        Parameters
        ----------
        name : str, optional
                A name to give to the created parameter.

        Returns
        -------
        object
                The PARAMETER created.

        """

    def apply(self, value: float) -> Any:
        """

        Apply changes on contents, given the value of modification.


        Parameters
        ----------
        value : float
                According to the definition of change_density member, this value will represent either the factor, count or spacing to be applied.

        Returns
        -------
        Any

        """


def OptimizationToolAction() -> str:
    """

    A function that return the type of Optimization tool action (DOE_RUN, BASELINE_RUN, SIMULATE_RUN, OPTIMIZATION_RUN)

    Returns
    -------
    str
            Returns a string on success (DOE_RUN, BASELINE_RUN, SIMULATE_RUN, OPTIMIZATION_RUN),
            or None on failure (if nothing is running when function is called).

    Examples
    --------
    ::

            import ansa


            def main():
                print("OptimizationToolAction = ", ansa.morph.OptimizationToolAction())


    """


def GetDOEStudyResults(
    optimization_task: object, results_path: str, exp_prefix: str
) -> dict:
    """

    A function that returns a Dictionary with all the Design Variable and Results found in a DOE folder

    Parameters
    ----------
    optimization_task : object
            The Optimization task object

    results_path : str
            The folder to look for DOE experiments

    exp_prefix : str
            The experiment prefix, default value "Exp_"

    Returns
    -------
    dict

    Examples
    --------
    ::

            import ansa
            from ansa import taskmanager


            def main():
                items = taskmanager.GetTaskItemsByName("OPTIMIZATION_TASK_1")
                if len(items) == 0:
                    return 1

                dict = ansa.morph.GetDOEStudyResults(items[0], "./DOE_Run_001")

                print(dict)


            main()


    """
