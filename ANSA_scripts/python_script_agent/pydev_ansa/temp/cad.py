from __future__ import annotations
from typing import *


def AnnotationThickness() -> float:
    """

    This function returns the thickness value found within the annotations of CATIA files (if any).
    It can be used only in an ANSA_TRANSL file.
    Warning: The function is obsolete.

    Returns
    -------
    float
            Returns the thickness, or -1.0 if no thickness information is found in the annotations.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def CAD_Translate():
                AnnoThick = cad.AnnotationThickness()
                print(AnnoThick)


    """


def LayerThickness() -> int:
    """

    This function checks if Layer thickness lines were found in the file. It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    int
            Returns 1 if found or 0 if not found.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def CAD_Translate():
                LayerThick = cad.LayerThickness()
                print(LayerThick)


    """


def MatVecThickness() -> float:
    """

    This function returns the thickness calculated by the Material Vector. It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    float
            Returns the thickness (1.2 for example) or -1.0 if no material vector was present in the file.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def CAD_Translate():
                MatVecThick = cad.MatVecThickness()
                print(MatVecThick)


    """


def MaterialVector() -> int:
    """

    This function checks if a material vector was found in the file. It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    int
            Returns 1 if found or 0 if not found.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def CAD_Translate():
                MatVecFound = cad.MaterialVector()
                print(MatVecFound)


    """


def OrientSingleWithLine(Curve_ref: object, Face_id: int) -> float:
    """

    This function orients a single face according to the direction of a line.

    Parameters
    ----------
    Curve_ref : object
            A reference to the curve line.

    Face_id : int
            The ID of the face to be oriented.

    Returns
    -------
    float
            Returns the 1/100 of the curve's length.

    Examples
    --------
    ::

            import ansa
            from ansa import cad
            from ansa import base
            from ansa import constants


            def main():
                curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                face = base.GetEntity(constants.NASTRAN, "FACE", 1)
                success = cad.OrientSingleWithLine(curve, face._id)


    """


def OrientWithLine(curve: object, elements: object) -> float:
    """

    This function orients the faces or PIDs found in the second argument according to
    the direction of the line. The curve reference is given as the first argument.
    The orientation is applied as well to all the faces that are topologically connected
    to the face closest to the orientation vector.

    Parameters
    ----------
    curve : object
            A curve entity.

    elements : object
            A list of faces or an integer that represents a property id.

    Returns
    -------
    float
            Returns the 1/100 of the curve's length.

    Examples
    --------
    ::

            import ansa
            from ansa import cad
            from ansa import base
            from ansa import constants


            def main():
                Curve = base.GetEntity(constants.NASTRAN, "CURVE", 1)
                Faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
                curve_length = cad.OrientWithLine(Curve, Faces)
                print(curve_length)


    """


def OrientationVector() -> int:
    """

    This function checks if an orientation vector was found in the file. It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    int
            Returns 1 if found or 0 if not found.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                orientVecFound = cad.OrientationVector()
                print(orientVecFound)


    """


def PartContainsGeometry() -> int:
    """

    This function returns if there is at least one geometric element in the file.
    It counts either points, curves, surfaces, faces and shell elements.
    It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    int
            Returns 1 if at least one of the entities is found, or 0 if the resultant file is empty.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def CAD_Translate():
                GeomFound = cad.PartContainsGeometry()
                print(GeomFound)


    """


def ThinPartThickness() -> float:
    """

    This function returns the thickness value found within the Thin Part attribute of CATIA files (if any).
    It can only be used in an ANSA_TRANSL file.

    Returns
    -------
    float
            Returns the thickness value (float), or -1.0 if no Thin Part attribute was present in the file.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                ThinPartThick = cad.ThinPartThickness()
                print(ThinPartThick)


    """


def TranslatorLogFileAppend(info) -> int:
    """

    The function writes information in the translator log file.

    Parameters
    ----------
    info :
            The text to be written in the log file.

    Returns
    -------
    int
            Returns the length of the text 'info', that the user has given as argument.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                cad.TranslatorLogFileAppend("Everything is OK")


    """


def VolumesCreated() -> int:
    """

    This function returns the number of volumes created from solids during the translation process.
    It can be used only in an ANSA_TRANSL file.

    Returns
    -------
    int
            Returns the number of volumes, or 0 if no volumes were created.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                Vols = cad.VolumesCreated()
                print(Vols)


    """


def GetNextFileLine(data: str) -> int:
    """

    This function is used when 'translating' a CAD file.
    CAD files are handled in a special way which identifies the file type and performs
    the appropriate operations to read the next line and put the result in the string
    variable argument.
    It is only available when reading in a neutral CAD file (iges, step, vda).

    Parameters
    ----------
    data : str
            A string where the result will be placed.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                line = ""
                cad.GetNextFileLine(line)
                print(line)


    """


def ExtraOptions() -> object:
    """

    This function returns the extra options that are supplied through the
    "Extra options" field in the Translators settings card.

    Returns
    -------
    object
            Rreturns a list that contains the arguments specified in the field.

    Examples
    --------
    ::

            import ansa
            from ansa import cad


            def main():
                m = cad.ExtraOptions()
                print("There are ", len(m), " extra options")
                print(m)


    """
