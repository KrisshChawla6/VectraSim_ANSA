from __future__ import annotations
from typing import *


def AddAssemblyRuleToAssemblyRulesGroup(rules: object, rules_group: object) -> int:
    """

    The function adds a list of assembly rules to an assembly rules group.

    Parameters
    ----------
    rules : object
            A list that contains the rules which will be added to the group.

    rules_group : object
            A group of rules.

    Returns
    -------
    int
            Returns 1 if the argument rules is of proper type, and rules_group is a valid group.
            Otherwise, 0 is returned.

    See Also
    --------
    CreateNewAssemblyRule, CreateNewAssemblyRulesGroup, CreateNewAssemblyScenario, AddAssemblyRulesGroupToAssemblyScenario

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # Creates an "Assembly Scenario2" with
                # a "Rules2" group for gum drops and
                # 2 assembly rules: "ruleA" and "ruleB"

                # Create  rules: ruleA and ruleB
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule("ruleB"))

                # Create group: Rules2 of type GumDrop_Type
                group = connections.CreateNewAssemblyRulesGroup("Rules2", "GumDrop_Type")

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario("Assembly Scenario2")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario({group}, scenario)

                # Add ruleA and ruleB to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)


    """


def AddAssemblyRulesGroupToAssemblyScenario(
    rules_groups: object, scenario: object
) -> int:
    """

    The function adds a list of groups of assembly rules to an assembly scenario.

    Parameters
    ----------
    rules_groups : object
            A list that contains groups of Assembly rules.

    scenario : object
            An Assembly Scenario.

    Returns
    -------
    int
            Returns 1 if the rules_groups list is of proper type, and scenario is a valid assembly scenario.
            Otherwise, 0 is returned.

    See Also
    --------
    CreateNewAssemblyRule, CreateNewAssemblyRulesGroup, CreateNewAssemblyScenario, AddAssemblyRuleToAssemblyRulesGroup

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # Creates an "Assembly Scenario2" with
                # a "Rules2" group for gum drops and
                # 2 assembly rules : "ruleA" and "ruleB"

                # Create  rules: ruleA and ruleB
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule("ruleB"))

                # Create group: Rules2 of type GumDrop_Type
                group = connections.CreateNewAssemblyRulesGroup("Rules2", "GumDrop_Type")

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario("Assembly Scenario2")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario([group], scenario)

                # Add ruleA and ruleB to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)


    """


def AddFilterToAssemblyRule(
    field: str,
    expression: str,
    value: str,
    session: object,
    match: str,
    case_sensitive: str,
    filter_name: str,
) -> int:
    """

    The function adds a filter to an existing assembly rule. If the rule has an active filter, a new row is added to that filter. Otherwise, a new filter is created and is set as active.
    The first, second and third arguments refer to the field, expression and value of the filter respectively. The fourth argument refers to the assembly rule.

    Parameters
    ----------
    field : str
            Field name.

    expression : str
            Expression.

    value : str
            The value of the expression.

    session : object
            The Assembly rule.

    match : str, optional
            Determines if all the filter rows must be matched. Available options are: "all" and
            "any". Default value is "all".

    case_sensitive : str, optional
            Determines if the filter will be case sensitive. Available options are "yes" and "no".
            Default value is "no".

    filter_name : str, optional
            Defines the filter name. If this filter does not exist, it is created then set as the
            active filter for the rule.

    Returns
    -------
    int
            Returns 1 if the filter was added successfully, or 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                # Create a new Assembly Rule named "Rule for A200 connections"
                rule = connections.CreateNewAssemblyRule(name="Rule for A200 connections")

                # Create a filter named "Name is A200" which becomes the active filter for the 'rule'
                connections.AddFilterToAssemblyRule(
                    field="Name",
                    expression="equals",
                    value="A200",
                    session=rule,
                    match="all",
                    case_sensitive="yes",
                    filter_name="Name is A200",
                )

                # appends a row to the active filter of the 'rule'
                connections.AddFilterToAssemblyRule(
                    field="ID", expression="is greater than", value="100", session=rule
                )


    """


def AssignConnectionSettings(connections: object, parameters: object) -> int:
    """

    AssignConnectionSettings() assigns the desired setting to the connection without creating the FE representation.

    Default settings are assigned for every setting that is not found or if it is invalid.
    AssignConnectionSettings() erases the previous FE representation of the connection
    if there was any.

    Parameters
    ----------
    connections : object
            A list of connection entities.

    parameters : object
            A dictionary of keyword/values.

    Returns
    -------
    int
            Returns 0 on error, or 1 for success.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, "SpotweldPoint_Type", filter_visible=True
                )
                vals = {
                    "SpotweldPoint_Type": "SPIDER",
                    "SpotweldPoint_SPIDER_ProjectToPerim": "y",
                    "SpotweldPoint_SPIDER_RBE2_PinFlags": "123456",
                    "SpotweldPoint_SPIDER_SearchDist": 30,
                }

                ret = connections.AssignConnectionSettings(cnctns, vals)


    """


def AutoSetConnectivityInConnections(
    connections: object,
    filter_visible: bool,
    output_mode: str,
    search_faces: bool,
    search_shells: bool,
    search_solids: bool,
    search_tubes: bool,
    search_projection: bool,
    search_holes: bool,
    use_hole_shape: bool,
    use_hole_proximity: bool,
    hole_proximity_distance: float,
    hole_proximity_angle: float,
    match_hole_params: str,
    search_distance: float,
    use_settings: bool,
    search_on_direction: bool,
    search_from: float,
    search_to: float,
    find_nearest: int,
    find_up_to: int,
    find_exactly: int,
    between_parts: bool,
    clear_connectivity: bool,
    tubes_feature_line_angle_limit: float,
    consider_part_hierarchy: bool,
):
    """

    This function clears the connectivity of each connection and then sets a new connectivity
    based on the user's parameters. It supports all connection types except hemmings and adhesive
    faces.

    Parameters
    ----------
    connections : object
            A list of connection entities.

    filter_visible : bool, optional
            Search through visible entities for PIDs or ModuleIDs within the
            search distance.
            (Default: False)

    output_mode : str, optional
            Sets if the connectivity will be assigned by "moduleid" or "pid" or "groups".
            (Default: "pid")

    search_faces : bool, optional
            Search through faces for PIDs or ModuleIDs within the
            search distance.
            (Default: True)

    search_shells : bool, optional
            Search through shells for PIDs or ModuleIDs within the
            search distance.
            (Default: True)

    search_solids : bool, optional
            Search through solids for PIDs or ModuleIDs within the
            search distance.
            (Default: False)

    search_tubes : bool, optional
            Search for tubes within the specified search area.
            Connection Type: Bolt
            (Default: False)

    search_projection : bool, optional
            Search for projection within the specified search area.
            Connection Type: Bolt
            (Default: True)

    search_holes : bool, optional
            Search for holes within the specified area.
            Connection Type: Bolt
            (Default: False)

    use_hole_shape : bool, optional
            If set to "False", ignores if the hole is rounded ellipsoeid,
            it will be recognized anyway.
            If set to "True" only rounded holes are accepted.
            Connection Type: Bolt
            (Default: True)

    use_hole_proximity : bool, optional
            If set to "True", use hole_proximity_distance and
            hole_proximity_angle to recognize a hole.
            Connection Type: Bolt
            (Default: True)

    hole_proximity_distance : float, optional
            Specifies the maximum distance between recognized holes.
            Connection Type: Bolt
            (Default: 100)

    hole_proximity_angle : float, optional
            Specifies the maximum 'angle' between holes.
            Connection Type: Bolt
            (Default: 10)

    match_hole_params : str, optional
            Each hole will be recognised if 'all' or 'any' of the hole
            criteria are matched.
            Used with 'search_holes' = 'True'
            Connection Type: Bolt
            (Default: 'any')

    search_distance : float, optional
            The search radius for parts or props
            to be assigned to connections.
            Connection Type: All
            (Default: 5)

    use_settings : bool, optional
            Use connection's search parameters to
            define the search area.
            Connection Type: Bolt
            (Default: False)

    search_on_direction : bool, optional
            If the connection has a direction, the  search can be made
            in a cylindrical area.
            Used when 'use_settings' = 'False' and
            'search_distance' is used as cylinders radius.
            Connection Type: Bolt
            (Default: False)

    search_from : float, optional
            Defines the cylinder's start point, with respect to the connection
            reference point, along with the connection's direction.
            Used when 'searcn_on_direction' = 'True'
            Connection Type: Bolt
            (Default: -1)

    search_to : float, optional
            Defines the cylinder's end point, with respect to Bolts
            connection reference point, along with the connection's direction.
            Used when 'searcn_on_direction' = 'True'
            Connection Type: Bolt
            (Default: 1)

    find_nearest : int, optional
            Assigns the 'n' nearest parts to the connections.
            (Default: 2)

    find_up_to : int, optional
            Assigns all parts if their count is less or equal to 'n',
            otherwise no parts are assigned.
            (Default: 2)

    find_exactly : int, optional
            Assigns all parts if their count is equal to 'n',
            otherwise no parts are assigned.
            (Default: 2)

    between_parts : bool, optional
            if 'True', connectivity will only be set if the connection lies
            between parts.
            Connection Type: ALL, except connection faces
            (Default: 'False')

    clear_connectivity : bool, optional
            Removes the existing connectivity information If value 'True' is set.
            Options 'find_nearest', 'find_up_to'/'find_exacty' are ignored.
            (Default: 'True')

    tubes_feature_line_angle_limit : float, optional
            Search tubes according to the feature angle
            from 0 to 90 degrees.
            (Default: 30)

    consider_part_hierarchy : bool, optional
            Search for the connectivity based on the hierarchical
            relationship between parts and connections.
            For a connection within a part, search only the parts/groups
            at the same level with the connection part (siblings parts).
            (Default: 'False')

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                connection_types = (
                    "SpotweldPoint_Type",
                    "SpotweldLine_Type",
                    "AdhesiveLine_Type",
                    "AdhesiveFace_Type",
                    "SeamLine_Type",
                    "GumDrop_Type",
                    "Hemming_Type",
                    "Bolt_Type",
                )

                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )

                connections.AutoSetConnectivityInConnections(
                    cnctns,
                    search_distance=2,
                    filter_visible=True,
                    search_faces=False,
                    output_mode="ModuleID",
                    find_up_to=3,
                )


    """


def CenterConnections(connections: object) -> int:
    """

    CenterConnections moves every connection point to the center of the parts it connects.
    The function is supported only for connection points.

    Parameters
    ----------
    connections : object
            A list of connection entities.

    Returns
    -------
    int
            Return value is 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                connection_types = {"SpotweldPoint_Type", "GumDrop_Type", "Bolt_Type"}
                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )
                ok = connections.CenterConnections(cnctns)


    """


def CollectAffectedConnectionEntities(
    part: object, connection_type: str, search_option: str
) -> object:
    """

    Based on the provided arguments, the function returns a group of connections that reference the specified part in their connectivity fields.

    Parameters
    ----------
    part : object
            Group or Part referenced by the connections.

    connection_type : str
            A string that defines the type of connections that will be returned by the function.
            Available types are:
            "Connections", "Connectors", "GentBuilders", "AllEntities".

    search_option : str
            A string that specifies whether the search will be carried for internal or external.
            connections or both. Available types are:
            "Internal", "External", "AllAffected".

    Returns
    -------
    object
            Returns a list that contains all the collected entities or 0 upon failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                part = base.GetPartFromModuleId("04580467")
                ents = connections.CollectAffectedConnectionEntities(
                    part, "Connections", "AllAffected"
                )


    """


def ConnectivityStringToEnts(connectivity: str) -> object:
    """

    Returns a list of entities represented by a string, which can be found in the connectivity fields of connectors and connections.

    Parameters
    ----------
    connectivity : str
            A string that represents ANSA entities. For example "#IN1" represents
            include with id 1, "312" represents part with module id 312 etc.

    Returns
    -------
    object
            Returns a list of entities represented by the string.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                # Get entities from connectivity string
                m = connections.ConnectivityStringToEnts("#1,#10")
                print(m[0]._id, m[1]._id)

                # Get connectivity string from entities
                print(connections.EntsToConnectivityString(m))


    """


def ConvertConnections(
    connections: object, point_to: str, line_to: str, create_single_line: bool
) -> int:
    """

    ConvertConnections converts connection lines and points to another connection line type and point type correspondingly.
    Convertion can take place only in connection points if the second argument is only a point type connection. The same is
    for connection lines too.

    Parameters
    ----------
    connections : object
            A list of connection entities that will be converted
            to a different type.

    point_to : str, optional
            Converts only connection points and valid types are:
            "SpotweldPoint_Type", "GumDrop_Type", "Bolt_Type",
            "SpotweldLine_Type", "Rivet_Type", "Robscan_Type", "Screw_Type".

    line_to : str, optional
            Converts only connection lines and valid types are:
            "AdhesiveLine_Type", "SeamLine_Type", "SpotweldLine_Type",
            "Hemming_Type".

    create_single_line : bool, optional
            This option has meaning only when converting spots to a single or more lines.
            With False value connections are grouped in space and by connectivity and
            more than one lines can be created.
            (Default: True)

    Returns
    -------
    int
            Returns 0 on error, or 1 for success.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                connection_types = (
                    "SpotweldPoint_Type",
                    "AdhesiveLine_Type",
                    "SeamLine_Type",
                    "GumDrop_Type",
                    "Hemming_Type",
                )
                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )
                ok = connections.ConvertConnections(
                    cnctns,
                    point_to="Bolt_Type",
                    line_to="SpotweldLine_Type",
                    create_single_line=False,
                )

                # OR Convert only connection points
                for conn in cnctns:
                    ok = connections.ConvertConnections(conn, point_to="Bolt_Type")
                base.RedrawAll()


    """


def ConvertConnectivity(
    connections: object, connectivity_mode: str, search_nearest_dist: float
):
    """

    Converts current connectivity of connections to Parts or Properties or Groups.

    Parameters
    ----------
    connections : object
            A list with connection entities.

    connectivity_mode : str
            The new connectivity mode to convert to:
            -"PID"
            -"ModuleID"
            -"Group"
            -"subsystem": get all subsystems a part belongs
            -"instance_to_part": get all instances of part
            -"part_to_instance": get nearest instance

    search_nearest_dist : float, optional
            The search radius for the nearest properties
            of a part. If it is not given, function gets
            all properties of the part.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "SpotweldPoint_Type")
                connections.ConvertConnectivity(cnctns, "ModuleId")


    """


def ConvertFeRepToConnection(
    entities: object,
    convert_type: str,
    connectivity_mode: str,
    check_violated_elements: bool,
) -> object:
    """

    This function assigns a connection in every FE Representation element of the list.
    The connectivity can be assigned by ModuleID or PID or Group.

    Parameters
    ----------
    entities : object
            Contains the elements to convert.

    convert_type : str
            Defines the type of the connections to be created.
            Valid types are:
            -"FE To Cnctn Pts": connection points
            -"FE To Seamline": seamlines
            -"FE To Adhesive": adhesive lines
            -"FE To Adh Face":  adhesive faces
            -"FE To Bolt" : bolts

    connectivity_mode : str
            Defines the type of connectivity of the generated entity.
            Valid types are:
            -"PID"
            -"ModuleID"
            -"Group"

    check_violated_elements : bool, optional
            False : allow elements with more than 20 nodes
            to be converted to connections.
            True : Not allow elements with more than 20 nodes
            to be converted to connections.
            (Default: True)

    Returns
    -------
    object
            Returns a list containing all the created connections or None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                # Collect all CBEAM elements and assign a connection point to each of them
                elements = base.CollectEntities(constants.NASTRAN, None, "CBEAM")
                conns = connections.ConvertFeRepToConnection(
                    elements, "FE To Cnctn Pts", "PID", False
                )


    """


def ConvertTubesToConnections(
    connection_type: str,
    input_faces: object,
    connections: bool,
    matched_faces: bool,
    unmatched_faces: bool,
) -> object:
    """

    Converts tubes to connection lines.

    Parameters
    ----------
    connection_type : str
            The connection type the user wants to create, with accepted values:
            -"SpotweldLine_Type"
            -"AdhesiveLine_Type"
            -"SeamLine_Type"
            -"Hemming_Type"

    input_faces : object
            A list of faces or a string with accepted values "All" or "Visible".

    connections : bool, optional
            If True the function will return a list with references to the created connections.

    matched_faces : bool, optional
            If True the function will return a list with references to the matched faces.

    unmatched_faces : bool, optional
            If True the function will return a list with references to the unmatched faces.

    Returns
    -------
    object
            On success it returns a dictionary which includes:
            key: connections        value: a list with the references of the created connections
            key: matched_faces      value: a list with the references of the matched faces
            key: unmatched_faces    value: a list with the references of the unmatched faces

            Return None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                connections.ConvertTubesToConnections(
                    connection_type="AdhesiveLine_Type",
                    input_faces="ALL",
                    connections=True,
                    matched_faces=True,
                    unmatched_faces=True,
                )


    """


def CreateConnectionFace(
    type: str, faces: object, id: int, connectivity: object, create_new_face: bool
) -> object:
    """

    The function creates an adhesive face.

    Parameters
    ----------
    type : str
            "AdhesiveFace_Type".

    faces : object
            A list that contains the faces that describe the connection.

    id : int, optional
            Specify the ID of the connection. Set 0 to let ANSA assign an ID.

    connectivity : object, optional
            A list that contains the connectivity strings of the components that
            will be connected.

    create_new_face : bool, optional
            If set to True a new face will be created.
            (Default: False)

    Returns
    -------
    object
            Returns the connection created, or 0 on error.

    See Also
    --------
    CreateConnectionLine

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                #       Create an adhesive face of ID 222 , with height=1,
                # \tconnecting parts P1=999999, property 1 & P2=888888 using face with id=15

                # example #1: Connectivity String manual generation
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 15))

                part_ids = []
                part_ids.append("999999, #1")  # part module ids and properties matrix
                part_ids.append("888888")

                cnctn = connections.CreateConnectionFace("AdhesiveFace_Type", faces, 222, part_ids)
                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"H": 1})

                # example #2: Connectivity String generated from Entities
                faces = []
                faces.append(base.GetEntity(constants.NASTRAN, "FACE", 16))

                p1 = []
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 999999))
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "PSHELL", 1))

                p2 = []
                p2.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 888888))

                part_ids = []
                part_ids.append(connections.EntsToConnectivityString(p1))
                part_ids.append(connections.EntsToConnectivityString(p2))

                cnctn = connections.CreateConnectionFace("AdhesiveFace_Type", faces, 333, part_ids)
                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"H": 1})


    """


def CreateConnectionLine(
    type: str, curves: object, id: int, connectivity: object
) -> object:
    """

    Creates a connection line (adhesive, seamweld, spotline or hemming).

    Parameters
    ----------
    type : str
            The type of the connection. Available types:
            -"SpotweldLine_Type"
            -"AdhesiveLine_Type"
            -"SeamLine_Type"
            -"Hemming_Type"

    curves : object
            A list that contains the curves that describe the connection.

    id : int, optional
            The ID of the connection that will be created.

    connectivity : object, optional
            A list that contains the connectivity strings of the connected components.

    Returns
    -------
    object
            Returns the connection created, or None on error.

    See Also
    --------
    CreateConnectionPoint

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # \tCreate an adhesive line of ID 100122 , with width=2 and height=1.5,
                # \tconnecting parts P1=999999, property 1 & P2=888888 using curve of id=166

                # example #1: Connectivity String manual generation
                curves = []  # Curves list
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 166))

                part_ids = []
                part_ids.append("999999, #1")  # part and property ids list
                part_ids.append("888888")

                cnctn = connections.CreateConnectionLine(
                    "AdhesiveLine_Type", curves, 100122, part_ids
                )

                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"W": 2, "H": 1.5})

                # example #2: Connectivity String generated from Entities
                curves = []  # Curves list
                curves.append(base.GetEntity(constants.NASTRAN, "CURVE", 177))

                p1 = []
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 999999))
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "PSHELL", 1))

                p2 = []
                p2.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 888888))

                part_ids = []
                part_ids.append(connections.EntsToConnectivityString(p1))
                part_ids.append(connections.EntsToConnectivityString(p2))

                cnctn = connections.CreateConnectionLine(
                    "AdhesiveLine_Type", curves, 100133, part_ids
                )

                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"W": 2, "H": 1.5})


    """


def CreateConnectionPoint(
    type: str, position: object, id: int, connectivity: object
) -> object:
    """

    Creates a connection point (spotweld, bolt or gumdrop).

    Parameters
    ----------
    type : str
            Type of Connection that will be created.
            Available types are:
            -"SpotweldPoint_Type"
            -"Bolt_Type"
            -"GumDrop_Type"
            -"Rivet_Type"
            -"Screw_Type"

    position : object
            A list that contains the coordinates of the connection point.

    id : int, optional
            The ID of the connection that will be created.

    connectivity : object, optional
            A list that contains the connectivity strings of the connected parts.

    Returns
    -------
    object
            Returns the created connection entity, or None on error.

    See Also
    --------
    CreateConnectionLine, CreateConnectionFace, EntsToConnectivityString

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # create a spotweld point of ID 100999 at (-822, 531, 259)
                # with diameter = 3, connecting parts P1=999999, property 1 & P2=888888

                # example #1: Connectivity String manual generation
                xyz = [-822.0, 531.0, 259.0]  # Coords

                part_ids = []  # Part and properties ids
                part_ids.append("999999, #1")
                part_ids.append("888888")

                cnctn = connections.CreateConnectionPoint(
                    "SpotweldPoint_Type", xyz, 100999, part_ids
                )
                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"D": 3})

                # example #2: Connectivity String generated from Entities
                xyz = [-711.0, 421.0, 148.0]  # Coords

                p1 = []
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 999999))
                p1.append(base.GetEntity(ansa.constants.NASTRAN, "PSHELL", 1))

                p2 = []
                p2.append(base.GetEntity(ansa.constants.NASTRAN, "ANSAPART", 888888))

                part_ids = []
                part_ids.append(connections.EntsToConnectivityString(p1))
                part_ids.append(connections.EntsToConnectivityString(p2))

                cnctn = connections.CreateConnectionPoint(
                    "SpotweldPoint_Type", xyz, 100100, part_ids
                )
                base.SetEntityCardValues(constants.NASTRAN, cnctn, {"D": 3})


    """


def CreateNewAssemblyRule(name: str) -> object:
    """

    This function creates a new assembly rule.

    Parameters
    ----------
    name : str, optional
            A name for the rule, if left blank an untitled rule will be created.

    Returns
    -------
    object
            Returns a reference to the newly created assembly rule.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                # Creates an "Assembly Scenario2" with
                # a "Rules2" group for gum drops and
                # 2 assembly rules: "ruleA" and  one untitled rule

                # Create  rules: ruleA and untitled rule
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule())

                # Create group: Rules2 of type GumDrop_Type
                group = connections.CreateNewAssemblyRulesGroup(
                    name="Rules2", search_for="GumDrop_Type"
                )

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario(name="Assembly Scenario2")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario([group], scenario)

                # Add ruleA and untitled rule  to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)


    """


def CreateNewAssemblyRulesGroup(name: str, search_for: str) -> object:
    """

    This function creates a new assembly rules group. To name the rules group, specify
    the pair (name="rule's name"), otherwise an untitled one is created.

    To specify the type of connections for the group, use the pair (search_for="connection_type"),
    otherwise "SpotweldPoint_Type" will be assigned.

    Parameters
    ----------
    name : str, optional
            A name for the rules group, otherwise an untitled one is created.

    search_for : str, optional
            Specify the type of connections for the group, otherwise "SpotweldPoint_Type"
            will be assigned.

    Returns
    -------
    object
            Returns a reference to the newly created assembly rules group.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                # Creates an "Assembly Scenario2" with
                # a "Rules2" group for gum drops and
                # 2 assembly rules: "ruleA" and one untitled rule

                # Create  rules: ruleA and one utitled rule
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule())

                # Create group: Rules2 of type GumDrop_Type
                group = connections.CreateNewAssemblyRulesGroup(
                    name="Rules2", search_for="GumDrop_Type"
                )

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario(name="Assembly Scenario2")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario([group], scenario)

                # Add ruleA and untitled rule to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)


    """


def CreateNewAssemblyScenario(name: str) -> object:
    """

    This function creates a new assembly scenario. A name can be assigned to the rule, if the pair
    (name = "Rule name") is specified. An untitled scenario will be created otherwise.

    Parameters
    ----------
    name : str, optional
            The name of the Assembly scenario which will be generated.

    Returns
    -------
    object
            Returns a reference to the newly created assembly scenario.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                # Create  rules: ruleA and ruleB
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule("ruleB"))

                # Create a filter named "Name is A200" which becomes the active filter for rule[0]
                connections.AddFilterToAssemblyRule(
                    field="Name",
                    expression="equals",
                    value="A200",
                    session=rule[0],
                    match="all",
                    case_sensitive="yes",
                    filter_name="Name is A200",
                )

                #   Add an existing connection template to each Assembly Rule item
                base.SetEntityCardValues(ansa.constants.NASTRAN, rule[1], {"TID": "2"})
                base.SetEntityCardValues(ansa.constants.NASTRAN, rule[0], {"TID": "1"})

                # Create a filter named "ID>100200" which becomes the active filter for rule[1]
                connections.AddFilterToAssemblyRule(
                    field="ID",
                    expression="is greater than",
                    value="100200",
                    session=rule[1],
                    match="all",
                    filter_name="ID > 100200",
                )

                # Create group: Rules2 of type SpotweldPoint_Type
                group = connections.CreateNewAssemblyRulesGroup(
                    name="Rules2", search_for="SpotweldPoint_Type"
                )

                #  Add a filter to an assembly rules group
                connections.AddFilterToAssemblyRulesGroup(
                    field="ID",
                    expression="is greater than",
                    value="100000",
                    session=group,
                    match="all",
                    filter_name="ID > 100000",
                )

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario(name="Assembly Scenario 1")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario([group], scenario)

                # Add ruleA and ruleB to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)

                # Distribute items to assembly scenario
                connections.DistributeAllItemsToAssemblyScenarios()


    """


def DefineConnectionHoles(
    entities: object,
    create: str,
    output_mode: str,
    parts_proximity_for_connection_merging: float,
    maximum_length: float,
    exclude_single_part_connections: bool,
    match_hole_params: str,
    search_holes: bool,
    use_hole_shape: bool,
    use_hole_proximity: bool,
    hole_proximity_distance: float,
    hole_proximity_angle: float,
    hole_minimum_diameter: float,
    hole_maximum_diameter: float,
    tube_minimum_diameter: float,
    tube_maximum_diameter: float,
    search_tubes: bool,
    tubes_feature_line_angle_limit: float,
) -> object:
    """

    Creates connectors or bolts in the recognized holes and tubes

    Parameters
    ----------
    entities : object
            A list that contains parts, properties, includes,
            shells, faces or solids.

    create : str
            Defines the type of the connector or bolt to create.

    output_mode : str
            Accepted values: "module_ids" or "properties". Defines
            whether the connectivity will be assigned by module_ids
            or properties.

    parts_proximity_for_connection_merging : float, optional
            Holes or tubes within a tolerance distance are handled
            as one and only one Connection is created.
            (Default: 0)

    maximum_length : float, optional
            The length of the tube or the distance of the most distant
            holes is assigned to bolt. Sometimes it's large and then
            user specifies a maximum length that should be assigned.
            It is only taken into account when specified.

    exclude_single_part_connections : bool, optional
            Connections with only one part will not be created.
            (Default: False)

    match_hole_params : str, optional
            Accepted values: "any" or "all". Each hole will be
            recognized if "all" or "any" of the hole criteria are
            matched.
            (Default: "all")

    search_holes : bool, optional
            Accepted values: True or False. Set to True to create
            assembly entities in holes. All hole parameters are
            ignored if 'search_holes' is False.
            (Default: True)

    use_hole_shape : bool, optional
            Accepted values: True or False. If set to False, ignores if
            the hole is rounded or ellipsoid, it will be  recognized
            anyway. If set to True, only rounded holes are accepted.
            (Default: False)

    use_hole_proximity : bool, optional
            Accepted values: True or False. Use hole_proximity_distance
            & hole_proximity_angle with True, to recognize a hole.
            (Default: True)

    hole_proximity_distance : float, optional
            Specifies the maximum distance between recognized holes.
            (Default: 10)

    hole_proximity_angle : float, optional
            Specifies the maximum 'angle' between holes.
            (Default: 10)

    hole_minimum_diameter : float, optional
            Specifies the minimum diameter for hole recognition.

    hole_maximum_diameter : float, optional
            Specifies the maximum diameter for hole recognition.

    tube_minimum_diameter : float, optional
            Specifies the minimum diameter for tube recognition.

    tube_maximum_diameter : float, optional
            Specifies the maximum diameter for tube recognition.

    search_tubes : bool, optional
            Accepted values: True or False. Set to True, to create
            assembly entities in tubes. All tube parameters are
            ignored if 'search_tubes' is False.
            (Default: False)

    tubes_feature_line_angle_limit : float, optional
            Specify the maximum angle of the tubes feature.
            (Default: 10)

    Returns
    -------
    object
            Returns a list with the newly created assembly entities, or None on error.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                ent_types = ["FACE", "SHELL", "SOLID"]
                entities = base.CollectEntities(constants.NASTRAN, None, ent_types)

                # ...Or...

                # group_types = ["ANSAPART", "__PROPERTIES__", "INCLUDE"]
                # entities = base.CollectEntities(constants.NASTRAN, None, group_types)

                conns = connections.DefineConnectionHoles(
                    entities,
                    output_mode="properties",
                    create="Bolt_Type",
                    search_holes=True,
                    use_hole_shape=True,
                    hole_minimum_diameter=0,
                    hole_maximum_diameter=25,
                )

                if conns:
                    print("connections number = ", len(conns))
                else:
                    print("NO CONNECTIONS")


    """


def DistributeAllItemsToAssemblyScenarios() -> int:
    """

    The function distributes all connections of the current database to the existing
    assembly scenarios. It is equivalent to pressing the 'Distribute" button, and
    selecting the "All, ignoring manual status" option.

    Returns
    -------
    int
            Returns 0.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                connections.DistributeAllItemsToAssemblyScenarios()


    """


def EntsToConnectivityString(connectivity: object) -> str:
    """

    Returns a string that represents the entities in a connectivity list. This string is found in the
    connectivity fields of connectors and connections.

    Parameters
    ----------
    connectivity : object
            A list that contains entities such as parts, properties, includes etc.

    Returns
    -------
    str
            Returns a string that represents the entities in the list.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                # Get entities from connectivity string
                m = connections.ConnectivityStringToEnts("#1,#10")
                print(m[0]._id, m[1]._id)

                # Get connectivity string from entities
                print(connections.EntsToConnectivityString(m))


    """


def EraseConnectionFeRep(connections: object) -> int:
    """

    This function erases the FE representation of the specified connections. It can be applied to all connection types.

    Parameters
    ----------
    connections : object
            A list that contains the connection entities whose representation will be erased.

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
            from ansa import connections


            def main():
                connection_types = {"SpotweldPoint_Type", "SpotweldLine_Type", "AdhesiveLine_Type"}

                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )
                connections.EraseConnectionFeRep(cnctns)


    """


def FindDuplicateConnections(
    connections1: object,
    connections2: object,
    point_distance_method: str,
    connection_point_distance: float,
    average_thickness_factor: float,
    curve_face_distance: float,
    similarity: float,
    equivalent_connectivity: bool,
    same_type: bool,
    pair_results: bool,
    distance_of_projection_center: float,
) -> object:
    """

    FindDuplicateConnections matches duplicate connections from a single group or between two groups according to
    the defined matching criteria. It returns a list with the matched connections.

    Parameters
    ----------
    connections1 : object
            A list that contains the first group of connection entities.

    connections2 : object, optional
            A list that contains the second group of connection entities.

    point_distance_method : str, optional
            Defines the method to calculate the distance between connection
            points.
            The available methods are the following:
            -'use_average_thickness': distance = factor * average thickness of
              projection connectivity flanges. The center of projections is
              taken account for the measurement between connections.
            -'use_distance_between_projection_centers':  distance = the
              given value.
              The center of projections is taken account for the measurement
              between connections.
            -'use_absolute_distance': distance = the given value. The
              connection's position is taken account for the measurement between
              connections.
            (Default: 'use_average_thickness')

    connection_point_distance : float, optional
            Value must be greater or equal to 0. When "point_distance_method"
            is defined to "use_absolute_distance", then this argument is used as
            search radius within two points that are duplicates.
            (Default: 5.0)

    average_thickness_factor : float, optional
            Factor must be greater or equal to 0  when "point_distance_method"
            is defined to "use_average_thickness", then this argument is used as
            search radius.
            Radius = (flange_thick1 + flange_thick2) * factor.
            (Default: 0.5)

    curve_face_distance : float, optional
            Value must be greater or equal to 0. It is the distance between
            curves or faces that will be checked for similar geometry.
            (Default: 5.0)

    similarity : float, optional
            It is the percentage of the geometrical similarity for compared
            curves or faces that are found within the defined
            curve_face_distance.
            (Default: 75.0)

    equivalent_connectivity : bool, optional
            If True, only compare connections with equal connectivity.
            (Default: False)

    same_type : bool, optional
            Only compare same type connections.
            e.g. If True, only compare a bolt with a bolt and not a bolt
            with a spotweld.
            (Default: True)

    pair_results : bool, optional
            Choose whether the results will be pairs or groups of connections.
            (Default: True)

    distance_of_projection_center : float, optional
            Value must be greater or equal to 0. When "point_distance_method"
            is defined to "use_distance_of_projection_center" then it is used as
            search radius between two centered projection points that are
            duplicates.
            (Default: 5.0)

    Returns
    -------
    object
            If pair_results=True it returns a dict with:
            key: group1,    values: the connections found
            key: group2,    values: the connections found

            If pair_results=False it returns a dict with:
            key: groups,    values: a list with lists of grouped connections
            key: conflicts, values: a list with connections that belong to more than one group

            Return 0: User has an incorrect parameter.
            Return 1: The function has run properly but no duplicate connection found.
            Return None: The input connections parameter is incorrect

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            # 1. FindDuplicateConnections in a single group
            def main():
                xyz = [0, 0, 0]
                cnctns = []
                part_ids = [4580200, 4580216]
                cnctns.append(
                    connections.CreateConnectionPoint("SpotweldPoint_Type", xyz, 1, part_ids)
                )

                xyz = [1, 1, 1]
                cnctns.append(
                    connections.CreateConnectionPoint("SpotweldPoint_Type", xyz, 2, part_ids)
                )
                matchedConnections = connections.FindDuplicateConnections(
                    cnctns, point_distance_method="use_distance", same_type=True
                )

                if (
                    matchedConnections != 0
                    and matchedConnections != None
                    and matchedConnections != 1
                ):
                    base.DeleteEntity(matchedConnections["group1"][0], True)


            # 2. FindDuplicateConnections between 2 groups
            def main():
                xyz = [0, 0, 0]
                Group1 = []
                Group2 = []
                part_ids = [4580200, 4580216]

                Group1.append(
                    connections.CreateConnectionPoint("SpotweldPoint_Type", xyz, 1, part_ids)
                )

                xyz = [1, 1, 1]
                Group2.append(
                    connections.CreateConnectionPoint("SpotweldPoint_Type", xyz, 2, part_ids)
                )

                # pair_results = true
                matchedConnections = connections.FindDuplicateConnections(
                    Group1,
                    Group2,
                    point_distance_method="use_distance_between_projection_centers",
                    same_type=True,
                )

                if matchedConnections != []:
                    base.DeleteEntity(matchedConnections["group1"][0], True)
                # pair_results = false
                groupedConnections = connections.FindDuplicateConnections(
                    Group1,
                    Group2,
                    pair_results=False,
                    point_distance_method="use_absolute_distance",
                    same_type=True,
                )

                if doubleConnections != None and doubleConnections != 0 and doubleConnections != 1:
                    groups = doubleConnections["groups"]
                    conflicting_connections = doubleConnections["conflicts"]

                    print("The groups are:")
                    for group in groups:
                        print(group)
                    print(" ")
                    print("The following connections belong in 2 or more groups.")
                    print(conflicting_connections)


    """


def GetAllConnectionSettings(connection: object) -> object:
    """

    GetAllConnectionSettings() returns all the connections settings of a connection.

    Parameters
    ----------
    connection : object
            The connection entity whose settings will be obtained.

    Returns
    -------
    object
            Returns a dictionary of all the settings-keywords and their respective value.
            If the connection has no parameters, it returns None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                connection_types = [
                    "SpotweldPoint_Type",
                    "SpotweldLine_Type",
                    "AdhesiveLine_Type",
                    "AdhesiveFace_Type",
                    "SeamLine_Type",
                    "GumDrop_Type",
                    "Hemming_Type",
                    "Bolt_Type",
                ]

                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )

                for conn in cnctns:
                    ret = connections.GetAllConnectionSettings(conn)
                    if ret:
                        print(ret)


    """


def GetConnectionProjections(connections: object, search_distance: float) -> object:
    """

    Finds the projections of connections.

    Parameters
    ----------
    connections : object
            List of connection entities.

    search_distance : float, optional
            Search distance for the projection.
            If not specified a default value will be used.

    Returns
    -------
    object
            Returns a list of Connections. Each Connection has a list of Projections. Each Projection has a list
            with two items, a list with the coordinates and the entity.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # Print Projection information of spotweld connections 100001 and 100002
                conns = []
                conns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100001))
                conns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100002))

                m_conn_projs = connections.GetConnectionProjections(conns, search_distance=100)

                # [#conn][#proj][ 0 or 1 ]

                # first connection
                c = 0  # connection index
                p = 0  # projection index
                xyz_P1_conn1 = m_conn_projs[c][p][
                    0
                ]  # Coordinates of projection 1 of Connection 100001  (list)
                shell_P1_conn1 = m_conn_projs[c][p][
                    1
                ]  # Shell entity on which the connection 100001 was projected   (shell entity)
                print("Connection 100001 Projection 1")
                print("Coords: ", xyz_P1_conn1)
                print("Entity ID: ", shell_P1_conn1._id)

                p = 1  # projection index
                xyz_P2_conn1 = m_conn_projs[c][p][
                    0
                ]  # Coordinates of projection 2 of Connection 100001  (list)
                shell_P2_conn1 = m_conn_projs[c][p][
                    1
                ]  # Shell entity on which the connection 100001 was projected   (shell entity)
                print("Connection 100001 Projection 2")
                print("Coords: ", xyz_P2_conn1)
                print("Entity ID: ", shell_P2_conn1._id)

                # second connection
                c = 1  # connection index
                p = 0  # projection index
                xyz_P1_conn2 = m_conn_projs[c][p][
                    0
                ]  # Coordinates of projection 1 of Connection 100002  (list)
                shell_P1_conn2 = m_conn_projs[c][p][
                    1
                ]  # Shell entity on which the connection 100002 was projected   (shell entity)
                print("Connection 100002 Projection 1")
                print("Coords: ", xyz_P1_conn2)
                print("Entity ID: ", shell_P1_conn2._id)


    """


def GetConnectionSettings(connection: object, parameters: object) -> object:
    """

    GetConnectionSettings() returns the connections settings of the requested parameters.

    Parameters
    ----------
    connection : object
            The connection entity whose settings will be obtained.

    parameters : object
            A list or tuple that contains the parameter keywords.

    Returns
    -------
    object
            Returns a dictionary of the keywords found and their respective value.
            Returns None if connection has no parameters.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                connection_types = [
                    "SpotweldPoint_Type",
                    "SpotweldLine_Type",
                    "AdhesiveLine_Type",
                    "AdhesiveFace_Type",
                    "SeamLine_Type",
                    "GumDrop_Type",
                    "Hemming_Type",
                    "Bolt_Type",
                ]

                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )
                for conn in cnctns:
                    ret = connections.GetConnectionSettings(
                        conn, ("SpotweldPoint_Type", "SpotweldPoint_RBE3-HEXA-RBE3_PinFlags")
                    )
                    if ret:
                        print("type = ", ret["SpotweldPoint_Type"])
                        print("PinFlags", ret["SpotweldPoint_RBE3-HEXA-RBE3_PinFlags"])


    """


def GetFirstFeRep(connections: object) -> object:
    """

    Gets a reference to the first entity of a connection.

    Parameters
    ----------
    connections : object
            A connection entity.

    Returns
    -------
    object
            Returns a reference to the entity or None if no entity is found.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                # Get Spoweld point with id: 100003
                conn = base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100003)

                # Get the first element of the Fe Representation of conn
                ent = connections.GetFirstFeRep(conn)
                while ent:
                    print(ent._id)
                    # Get next element in the Fe-Rep of conn
                    ent = connections.GetNextFeRep(conn, ent)


    """


def GetNearestPointOnBound(
    points: object, parts_props: object, search_dist: float
) -> object:
    """

    The function returns a list with the nearest points on bounds.

    Parameters
    ----------
    points : object
            A list (size N) where each entry is a set of coords [X,Y,Z], from which the function
            will find the nearest points on a bound of the parts/props.

    parts_props : object
            A list (size N) where each entry contains a list of Part/Property entities that define
            the searchfield for each point.

    search_dist : float
            A float that determines the maximum search distance.

    Returns
    -------
    object
            Returns a list (size N) with the resulting nearest points on bound:
            Each entry of the matrix is either:
            1) A matrix (size 3) whose coordinates of the point were found.
            2) 0, if such a point was not found within search_dist.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                props = []
                props.append(base.GetEntity(0, "PSHELL", 1800))  # Prop1
                props.append(base.GetEntity(0, "PSHELL", 1830))  # Prop2

                parts = [base.GetEntity(0, "ANSAPART", 38)]  # Part1

                parts_props = []
                parts_props.append(props)
                parts_props.append(parts)

                points = []
                points.append([450, -780, 250])  # Point A
                points.append([450, 780, 250])  # Point B

                close_points = connections.GetNearestPointOnBound(points, parts_props, 210)
                if close_points[0] != 0:
                    print("Nearest point of Prop1 and Prop2 on bound from Point A found")
                    print(close_points[0])
                else:
                    print("Nearest point on bound from Point A NOT found")
                if close_points[1] != 0:
                    print("Nearest point of Part1 on bound from Point B found")
                    print(close_points[1])
                else:
                    print("Nearest point on bound from Point B NOT found")


    """


def GetNearestPointOnFeature(
    points: object, parts_props: object, search_dist: float, feature_angle: float
) -> object:
    """

    The function returns a list with the nearest points on bounds.

    Parameters
    ----------
    points : object
            A list (size N) where each entry is a set of coords [X,Y,Z] from which the
            function will find the nearest points on a bound of the parts/props.

    parts_props : object
            A list (size N) where each entry contains a list of Part/Property
            entities that defines the search field for each point.

    search_dist : float
            A float that determines the maximum search distance.

    feature_angle : float
            A float that defines the feature angle in degrees.

    Returns
    -------
    object
            Returns a list (size N) with the resulting nearest points on bound found from search:
            Each entry of the matrix is either:
            1) A matrix (size 3) with the coordinates of the point found.
            2) 0, if such a point was not found within search_dist.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                props = []
                props.append(base.GetEntity(0, "PSHELL", 1800))  # Prop1
                props.append(base.GetEntity(0, "PSHELL", 1830))  # Prop2

                parts = [base.GetEntity(0, "ANSAPART", 38)]  # Part1

                parts_props = []
                parts_props.append(props)
                parts_props.append(parts)

                points = []
                points.append([450, -780, 250])  # Point A
                points.append([450, 780, 250])  # Point B

                close_points = connections.GetNearestPointOnFeature(points, parts_props, 210, 10.75)

                if close_points[0] != 0:
                    print("nearest point of Prop1 and Prop2 on Feature from Point  A found")
                    print(close_points[0])
                else:
                    print("nearest point on Feature from Point A NOT found")
                if close_points[1] != 0:
                    print("nearest point of Part1 on Feature from Point B found")
                    print(close_points[1])
                else:
                    print("nearest point on Feature from Point B NOT found")


    """


def GetNextFeRep(connection: object, entity) -> object:
    """

    Gets a reference to the next 'element' of a connection by specifing the current element.

    Parameters
    ----------
    connection : object
            A connection entity.

    entity :
            The next element in the FE representation of connection.
            Can be retreived from a call to GetFirstFeRep() or GetNextFeRep().

    Returns
    -------
    object
            Returns a reference to the entity or None when no entity is found.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                # Get Spoweld point with id: 100003
                conn = base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100003)

                # Get the first element of the Fe Representation of conn
                ent = connections.GetFirstFeRep(conn)

                while ent:
                    print(ent._id)
                    # Get next element in the Fe-Rep of conn
                    ent = connections.GetNextFeRep(conn, ent)


    """


def GetSpwDiamFromThickness(connection: object, search_distance: float) -> float:
    """

    The Connection point diameter value is calculated from the Spot Weld Thickness Diameter Map
    defined in ANSA.defaults.

    Parameters
    ----------
    connection : object
            A connection entity (Spotweld, Gumdrop, Bolt) with zero diameter.

    search_distance : float, optional
            The search distance. If not given, the connection's search distance is used.
            Should be greater than 0.

    Returns
    -------
    float
            Returns the connection diameter value calculated by Thickness to Diameter Map on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                cnctn = base.GetEntity(
                    constants.NASTRAN, "SpotweldPoint_Type", 200
                )  # spotweld id = 200
                diam_from_thick = connections.GetSpwDiamFromThickness(
                    connection=cnctn, search_distance=20
                )
                print("Diamter = ", diam_from_thick)


    """


def OutputConnections(connections: object, filetype: str, filename: str) -> int:
    """

    Outputs a standard connection file with the given connections.

    Parameters
    ----------
    connections : object
            A list that contains the connections entities to be
            output.If you pass a zero-length matrix,
            ALL the connections are output.

    filetype : str
            A string that describes the type of the output file
            Available types:
            "XML","MCF", "VIP", "VIP(pid)", "VIP(csv)", "VIP(csv, pid)", "VIP2", "VIP2(ModuleId)",
            "xMCF 3.1", "xMCF 3.1(pid)".
            If an invalid type is entered, a list valid types will
            be suggested by ANSA.

    filename : str
            A string that describes the path and name of the
            connection file. The file will be overwritten if it
            already exists.

    Returns
    -------
    int
            Returns 0 if the filetype is wrong, or if an error occurred during the writing of the file.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import utils
            from ansa import connections
            from ansa import constants


            def main():
                # Output Connections (ids 100001 to 100003) to a file using XML format
                m = []
                m.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100001))
                m.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100002))
                m.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100003))

                file = utils.SelectOpenFile(0)
                connections.OutputConnections(m, "XML", file[0])

                # Output All Connections  to a file using XML format
                connections.OutputConnections([], "XML", "C:/Users/ASSEMBLY/conn_file.xml")


    """


def ReApplyConnections(connections: object) -> int:
    """

    Create the FE representation of a number of connections, using their current settings.

    Parameters
    ----------
    connections : object
            A list with connection entities or a single connection
            entity to will be reapplied.

    Returns
    -------
    int
            Returns 0 if no connections exists in the list, 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                # Reapply connections with IDs:100001, 100002, 100003
                cnctns = []
                cnctns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100001))
                cnctns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100002))
                cnctns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100003))

                connections.ReApplyConnections(cnctns)


    """


def ReadConnections(
    filetype: str, filename: str, group_name: str, offset_val: int
) -> int:
    """

    Reads a standard connection file and creates connections.

    Parameters
    ----------
    filetype : str
            String declaring the type of the file (ex. "XML", "VIP").
            If an invalid type is entered, a list of valid
            types will be suggested by ANSA.

    filename : str
            The path of the file.

    group_name : str, optional
            The name of the connections group that is generated.

    offset_val : int, optional
            The offset connection id.

    Returns
    -------
    int
            Returns 0 if the filetype is wrong or if the parameters are invalid.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                # Read Connections from file name conn_file.xml, assign User Group Attribute: "group 1" and offset ID: 22345
                connections.ReadConnections(
                    "XML", "C:/Users/ASSEMBLY/conn_file.xml", group_name="group1", offset_val=22345
                )
                # Read Connections from file name conn_file2.xml
                connections.ReadConnections("XML", "C:/Users/ASSEMBLY/conn_file2.xml")


    """


def RealizeConnections(connections: list, parameters: dict) -> int:
    """

    Create the FE representation of a number of connections, using either the specified values for
    each type or the default values.

    Parameters
    ----------
    connections : list
            A list of connection entities that will be
            realized.

    parameters : dict
            A dictionary with the FE Rep. Settings fields name and
            values. If a blank dictionary is specified, the default
            values of each type will be used.

    Returns
    -------
    int
            Returns 0 if all connections fail. Otherwise it returns the number of connections that
            were realized successfully.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                # Default values for Spotweld Points are:
                # SpotweldPoint_Type = RBE2"          (default pattern)
                # Default values for Adhesive Lines are:
                # AdhesiveLine_Type  = RBE3-HEXA-RBE3"    (default pattern)

                cnctns = []
                cnctns.append(base.GetEntity(constants.NASTRAN, "AdhesiveLine_Type", 100045))
                cnctns.append(base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100003))

                # Create adhesive line: RBE3-CELAS1-RBE3  (NON-default type) *
                # Set AdhesiveLine_RBE3-CELAS1-RBE3_Pinflags = 12 (NON-default type) *
                # Create spotweld point: RBAR      (NON-default type) *
                connections.RealizeConnections(
                    cnctns,
                    {
                        "AdhesiveLine_Type": "RBE3-CELAS1-RBE3",
                        "AdhesiveLine_RBE3-CELAS1-RBE3_Pinflags": "12",
                        "SpotweldPoint_Type": "RBAR",
                    },
                )
                # Alternatively connections.GetAllConnectionSettings() can be used to retrive all the connection's settings


    """


def RemoveDoubleConnections(
    connections: object,
    tolerance: float,
    equivalent_connectivity: bool,
    keep_id: str,
    move_to_middle: bool,
    action: str,
) -> int:
    """

    RemoveDoubleConnections() combines or deletes the connections which are considered double,
    deoending on a tolerance distance and their equivalent connectivity. The remaining connection
    of every double connections group can be placed to the center of gravity of each group.

    It is highly recommended to use 'FindDuplicateConnections' which matches any kind of
    connection and not only connection points like 'RemoveDoubleConnections'.
    Also more matching criteria are available.

    Parameters
    ----------
    connections : object
            A list that contains connection point entities.

    tolerance : float, optional
            The search radius.
            (Default: 5)

    equivalent_connectivity : bool, optional
            This option groups the connections if they have the same connectivity.
            (Default: False)

    keep_id : str, optional
            Accepted values: "highest", "lowest". The connection with the highest
            or lowest id from each group will be kept.
            (Default: "highest")

    move_to_middle : bool, optional
            It moves the remaining connection from each group to
            the center of gravity of the group.
            (Default: False)

    action : str, optional
            Accepted values: "delete", "combine". Select the action for the
            useless connections of each group.
            (Default: "delete")

    Returns
    -------
    int
            Return 1 on success or 0 on failure, with corresponding message.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                connection_types = ["SpotweldPoint_Type", "GumDrop_Type", "Bolt_Type"]
                cnctns = base.CollectEntities(
                    constants.NASTRAN, None, connection_types, filter_visible=True
                )
                connections.RemoveDoubleConnections(
                    cnctns,
                    action="combine",
                    tolerance=50,
                    equivalent_connectivity=False,
                    move_to_middle=False,
                    keep_id="highest",
                )
                base.RedrawAll()


    """


def RunAllAssemblyScenarios(realize_connections: bool) -> int:
    """

    The function applies all the active assembly scenarios of the database.

    Parameters
    ----------
    realize_connections : bool, optional
            Determines whether the connections will also be realized.
            (Default: False)

    Returns
    -------
    int
            Returns the number of active assembly rules (i.e. the ones that runned).

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                # Apply all the assembly scenarios and realize the connections
                connections.RunAllAssemblyScenarios(realize_connections=True)


    """


def SetConnectionDrawMode(mode: str, user_attributes: str, use_color_bar: bool) -> int:
    """

    SetConnectionDrawMode sets drawing mode for connections.

    Parameters
    ----------
    mode : str, optional
            Valid drawing modes are "Ent", "Connectivity Num", "Connectivity Parts",
            "Type", "Status", "FeRep", "Diameter", "User Attributes".

    user_attributes : str, optional
            Define the attribute to draw.
            It is used only for "User Attributes" draw mode.

    use_color_bar : bool, optional
            Numerical criteria can be drawn using the color bar
            or the default legends table.

    Returns
    -------
    int
            Returns 1 on success and 0 nailure.

    Examples
    --------
    ::

            import ansa
            from ansa import connections
            from ansa import base


            def main():
                connections.SetConnectionDrawMode("Diameter")
                connections.SetConnectionDrawMode("User Attributes", "Attribute_Name", False)
                connections.SetConnectionDrawMode("User Attributes", "Attribute_Name", True)
                connections.SetConnectionDrawMode("User Attributes", "Attribute_Name")
                connections.SetConnectionDrawMode("Ent")

                base.RedrawAll()


    """


def SetDefault(fields: object) -> int:
    """

    Changes the default Connection Manager values, stated in the ANSA.default file.
    (e.g. values for adhesive lines in ANSA.default file:
    "AdhesiveLine_Type = RBE3-HEXA-RBE3", defines RBE3-HEXA-RBE3 as the default pattern when
    realizing a connection, "AdhesiveFace_RBE3_HEXA_RBE3_RBE3PinFlags = 123456", defines
    123456 as the default pinflags value for this pattern).
    Change these values, by passing parameters to this function in pairs of:
    "param variable"-"param value"

    Parameters
    ----------
    fields : object
            A tuple, containing consecutive string pairs of: "param variable", "param value".

    Returns
    -------
    int
            Returns 0 on error, or non-zero on success.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                # Default values for Adhesive Lines are:
                # * "AdhesiveLine_Type = RBE3-HEXA-RBE3"    (default pattern)
                # * "AdhesiveFace_RBE3_HEXA_RBE3_RBE3PinFlags = 123456"
                # * "AdhesiveFace_RBE3_HEXA_RBE3_NumOfLayers = 1"

                # change the default 'nlayers' to 3
                connections.SetDefault(("AdhesiveFace_RBE3_HEXA_RBE3_NumOfLayers", "3"))

                # change the default 'nlayers' to 2 and 'pinflags' to 12
                connections.SetDefault(
                    (
                        "AdhesiveFace_RBE3_HEXA_RBE3_NumOfLayers",
                        "2",
                        "AdhesiveFace_RBE3_HEXA_RBE3_RBE3PinFlags",
                        "12",
                    )
                )


    """


def RunAssemblyScenario(scenarios: object, realize_connections: bool) -> int:
    """

    The function applies the selected assembly scenario.

    Parameters
    ----------
    scenarios : object
            The assembly scenario which will be applied.

    realize_connections : bool, optional
            Determines whether the associated connections will be realized.
            (Default: False)

    Returns
    -------
    int
            Returns the number of Assembly Rules groups that the Assembly Scenario contains.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                AssemblyScenarios = base.CollectEntities(0, None, "ASSEMBLY_SCENARIO")
                print(len(AssemblyScenarios))

                connections.RunAssemblyScenario(AssemblyScenarios[0], True)


    """


def ActivateConnectionsEnts(connection_ents: object, make_active: bool) -> int:
    """

    Activates/Deactivates connections of the database. To be applied in order to control which connections will
    remain active after actions that turn the related parts to Use/Don't Use representation.

    Parameters
    ----------
    connection_ents : object
            A list with references to connection entities.

    make_active : bool
            True to activate the connections. False to deactivate them.

    Returns
    -------
    int
            Always returns 0.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                ent = base.GetEntity(constants.NASTRAN, "SpotweldPoint_Type", 100001)
                ret1 = base.IsEntityActive(ent)
                print("ret1 = ", ret1)
                ret2 = connections.ActivateConnectionsEnts(ent, True)
                print("ret2 = ", ret2)


    """


def AddFilterToAssemblyRulesGroup(
    field: str,
    expression: str,
    value: str,
    session: object,
    match: str,
    case_sensitive: str,
    filter_name: str,
) -> int:
    """

    The function adds a filter to an existing assembly rules group.

    Parameters
    ----------
    field : str
            The field name.

    expression : str
            The expression.

    value : str
            The value of the expression.

    session : object
            The assembly rules group.

    match : str, optional
            Determines if all the filter rows must be matched.
            Available options are: "all" and "any".
            (Default: "all")

    case_sensitive : str, optional
            Determines if the filter will be case sensitive.
            Available options are "yes" and "no".
            (Default: "no")

    filter_name : str, optional
            Defines the filter name. If this filter does not exist,
            it is created and set as the active filter for the rule.

    Returns
    -------
    int
            Returns 1 if the filter was added successfully, or 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                # Create  rules: ruleA and ruleB
                rule = []
                rule.append(connections.CreateNewAssemblyRule("ruleA"))
                rule.append(connections.CreateNewAssemblyRule("ruleB"))

                # Create a filter named "Name is A200" which becomes the active filter for rule[0]
                connections.AddFilterToAssemblyRule(
                    field="Name",
                    expression="equals",
                    value="A200",
                    session=rule[0],
                    match="all",
                    case_sensitive="yes",
                    filter_name="Name is A200",
                )

                # Create a filter named "ID>100200" which becomes the active filter for rule[1]
                connections.AddFilterToAssemblyRule(
                    field="ID",
                    expression="is greater than",
                    value="100200",
                    session=rule[1],
                    match="all",
                    filter_name="ID > 100200",
                )

                #   Add an existing connection template to each Assembly Rule item
                base.SetEntityCardValues(ansa.constants.NASTRAN, rule[1], {"TID": "2"})
                base.SetEntityCardValues(ansa.constants.NASTRAN, rule[0], {"TID": "1"})

                # Create group: Rules2 of type SpotweldPoint_Type
                group = connections.CreateNewAssemblyRulesGroup(
                    name="Rules2", search_for="SpotweldPoint_Type"
                )

                #  Add a filter to an assembly rules group
                connections.AddFilterToAssemblyRulesGroup(
                    field="ID",
                    expression="is greater than",
                    value="100000",
                    session=group,
                    match="all",
                    filter_name="ID > 100000",
                )

                # Create assembly scenario: AssemblyScenario2
                scenario = connections.CreateNewAssemblyScenario(name="Assembly Scenario 1")

                # Add Rules2 to Assembly Scenario2
                connections.AddAssemblyRulesGroupToAssemblyScenario([group], scenario)

                # Add ruleA and ruleB to Rules2
                connections.AddAssemblyRuleToAssemblyRulesGroup(rule, group)

                # Distribute items to assembly scenario
                connections.DistributeAllItemsToAssemblyScenarios()


    """


def OpenConnectionManager(
    connections: object, mode: str, inspection_mode: bool, confirm_to_close: bool
) -> bool:
    """

    Opens the connection manager filled with connections or empty.
    It is opened either in modal mode, with ok/cancel dialog and forces the python script to wait
    until it is closed, or in modeless mode, without ok/cancel dialog where the script continues.

    Parameters
    ----------
    connections : object, optional
            A list with connections or a single connection.

    mode : str, optional
            'mode' takes 2 values:
                    - 'modal': the script stops here and manager opens
                       with Ok/Cancel dialog.
                       It returns 1 for Ok pressed and 0 for ESC.
                       Script continues when manager closes.

                     - 'modeless': script continues and manager opens
                          without Ok/Cancel dialog. It returns always 1.
            (Default: 'modal')

    inspection_mode : bool, optional
            Set to True to open the Connection Manager in inspection mode.
            (Default: No)

    confirm_to_close : bool, optional
            If set to True, a window will ask the user to confirm to close
            the Connection Manager.
            (Default: No)

    Returns
    -------
    bool
            Modal manager returns True for Ok pressed and False for ESC or cancel.
            Modeless manager always returns True.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "SpotweldPoint_Type")

                # Manager opens filled with connections in inspection mode. Script waits here.
                ret = connections.OpenConnectionManager(
                    mode="modal", connections=cnctns, inspection_mode=True
                )
                print("ret: {}".format(ret))
                if ret == 0:
                    print("Cancel or Esc pressed")
                # Manager opens with a single connection. Script continues.
                connections.OpenConnectionManager(cnctns[0], "modeless")

                # Manager opens empty. Script waits here.
                connections.OpenConnectionManager()


    """


def OpenTemplateManager() -> object:
    """

    This function opens the Connection Template Manager and the script stops until it is closed.
    The function is executed in gui mode only.

    Returns
    -------
    object
            Always returns None.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import connections


            def main():
                connections.OpenTemplateManager()


    """


def ReplaceConnectivity(
    old_connectivity: object,
    new_connectivity: object,
    connections: object,
    connectivity_indexes: int,
):
    """

    Replace the given connections connectivity (part, prop, include, subsytem)
    by one or more parts/props/includes/subsystems to any or Pi connectivities of connections.

    Parameters
    ----------
    old_connectivity : object
            A part, a prop, an include, a subsytem or a list of them.

    new_connectivity : object
            A part, a prop, an include, a subsytem or a list of them.

    connections : object
            A connection or a list of connections.

    connectivity_indexes : int, optional
            An integer or a list of integers to define the index of Pi connectivities
            to replace the connectivity.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "SpotweldPoint_Type")
                pshell = base.GetEntity(constants.NASTRAN, "PSHELL", 11)
                part = base.GetPartFromModuleId("100")
                connections.ReplaceConnectivity(pshell, part, cnctns, 2)


    """


def GroupConnectionsByConnectivity(connections: object) -> object:
    """

    The function groups the given connections that have the same connectivity.

    Parameters
    ----------
    connections : object
            A list of connection entities

    Returns
    -------
    object
            Returns a dictionary where the key is the connectivity string and the data is a list of
            connections that have this connectivity.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "SpotweldPoint_Type")

                dict = connections.GroupConnectionsByConnectivity(cnctns)

                for connectivity_str, conn_list in dict.items():
                    print(
                        "Connectivity ", connectivity_str, " has ", len(conn_list), " connections."
                    )
                    m = connections.ConnectivityStringToEnts(connectivity_str)
                    print(m)


    """


def ConvertConnectionsToGeometry(connections: object, part: object) -> object:
    """

    ConvertConnectionsToGeometry converts connection lines and points and connection
    faces to geometry.

    Parameters
    ----------
    connections : object
            A list of connection entities that will be converted
            to geometry.

    part : object, optional
            The ANSA part that will be used for the convertion.

    Returns
    -------
    object
            Returns a list with the created entities (ie. curves, points, faces).

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                connection_types = ("AdhesiveLine_Type", "AdhesiveFace_Type")

                cnctns = base.CollectEntities(constants.NASTRAN, None, connection_types)

                connections.ConvertConnectionsToGeometry(cnctns)


    """


def FindDuplicateTemplates(templates: object) -> object:
    """

    FindDuplicateTemplates matches duplicate connection templates that are identical. It returns a list of lists with the matched templates.

    Parameters
    ----------
    templates : object
            A list that contains the templates to compare.

    Returns
    -------
    object
            Returns 0 on error, or a list of lists of duplicate Templates on success.

    Examples
    --------
    ::

            import ansa
            from ansa import *

            if __name__ == "__main__":
                allTemplates = base.CollectEntities(
                    constants.NASTRAN, None, "__CONNECTION_TEMPLATES__"
                )
                duplicateTemplates = connections.FindDuplicateTemplates(allTemplates)


    """


def SetWeldPosition(connections: object, set_method: str) -> object:
    """

    Sets Weld Positions in a list of Connections. The connections must be of "SeamLine_Type".

    Parameters
    ----------
    connections : object
            A list of ANSA "SeamLine_Type" connections

    set_method : str, optional
            {"Manual", "Automatic"}. The method with which the Weld Position will be set. Default is "Manual".

    Returns
    -------
    object
            A list of the connections that failed to set a Weld Position.
            Note. set_method = "Manual" will always return an empty list.

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                conn_list = base.CollectEntities(constants.NASTRAN, None, "SeamLine_Type")

                # Set Weld position Automatically:
                failed_cnctns = connections.SetWeldPosition(conn_list, "Automatic")

                # Set Weld position Manually:
                connections.SetWeldPosition(conn_list)  # Interaction in GUI is required here!!!


            if __name__ == "__main__":
                main()


    """


def SplitConnectionLinesByAngle(connections: object, corner_angle: float):
    """

    This function breaks a connection line to multiple connection lines on locations where angle formed between two consecutive curves is bigger than corner angle.

    Parameters
    ----------
    connections : object
            A list with connection entities.

    corner_angle : float
            The angle formed between two consecutive curves in degrees.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                conn_list = base.CollectEntities(constants.NASTRAN, None, "SeamLine_Type")
                connections.SplitConnectionLinesByAngle(conn_list, 80.0)


    """


def CreateConnectorFromInterfacePoints(
    interface_points: object,
    match_only_identical_names: bool,
    matching_proximity: float,
    create_external_connectors_only: bool,
    representation: str,
    max_number_of_connected_points: int,
) -> object:
    """

    This function groups assembly points according the defined criteria and creates a connector per group. Only assembly points which are not already used by connectors are considered.
    The connector has connectivity, search, interface and representation assigned. Direction is assigned when the connector is defined between 2 assembly points.

    Parameters
    ----------
    interface_points : object
            A list with interface points for grouping.

    match_only_identical_names : bool, optional
            Group interface points with identical name only.
            Default: False

    matching_proximity : float, optional
            The distance where 2 or more interface points
            are grouped.
            Default: 5

    create_external_connectors_only : bool, optional
            Create connectors which assembly interface points
            which belong to different subsystems.
            Default: False

    representation : str, optional
            The representation which is assigned to each new connector.
            Default: None
            Possible values per Deck: All available representations,
            as they appear in connector entity card apart from
            'UserScript' and 'FromFile'.

    max_number_of_connected_points : int, optional
            Define maximum connected interface points. Search might find more but only the closest max_number_of_connected_points will be used.

    Returns
    -------
    object
            It returns a dictionary with key the connector and data a list with interface points from which it was created.

    Examples
    --------
    ::

            def main():
                interf_points = base.CollectEntities(
                    constants.NASTRAN, None, "A_POINT", recursive=True
                )

                connector_per_points = connections.CreateConnectorFromInterfacePoints(
                    interf_points,
                    representation="CBUSH",
                    match_only_identical_names=True,
                    matching_proximity=6,
                    create_extrenal_connectors_only=True,
                )

                if connector_per_points:
                    print(len(connector_per_points))
                    print(connector_per_points)
                    # Set representation specific settings
                    for connector in connector_per_points.keys():
                        connector.set_entity_values(constants.NASTRAN, {"pid": 100})
                else:
                    print("No connectors were created")


    """


def CollectConnectionCurves(connection: object) -> object:
    """

    Creates a list with the curves of a connection line.

    Parameters
    ----------
    connection : object
            The connection line if which curves should be returned.

    Returns
    -------
    object
            Returns a list with all the collected curves.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections


            def main():
                p_cnctn = base.GetEntity(ansa.constants.NASTRAN, "SeamLine_Type", 100001)
                ents = connections.CollectConnectionCurves(p_cnctn)


    """


def FindConnectionCharacteristics(
    connections: object, search_pattern: bool, average_angle: bool
) -> object:
    """

    Gets characteristics from a list of Connections. The connections must be of "SeamLine_Type".

    Parameters
    ----------
    connections : object
            a list of ANSA "SeamLine_Type" connections.

    search_pattern : bool, optional
            If True it will return the search pattern of the connections.

    average_angle : bool, optional
            If True it will return the average angle of the connections' connected flanges.

    Returns
    -------
    object
            A dictionary with key the connections and value an object of type FindConnectionCharacteristics.
            Each characteristic can be accessed from each returned object from its corresponding member.
            When a characteristic is not requested or it could not be calculated None will be returned.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import connections
            from ansa import constants


            def main():
                conn_list = base.CollectEntities(constants.NASTRAN, None, "SeamLine_Type")

                # All characteristics will be None.
                result = connections.FindConnectionCharacteristics(conn_list)

                # All characteristics will be returned (only if they can't be calculated None will be returned).
                result = connections.FindConnectionCharacteristics(conn_list, True, True)

                # Only search_pattern characteristic will be returned, average_angle will be None.
                result = connections.FindConnectionCharacteristics(conn_list, search_pattern=True)

                for con, obj in result.items():
                    print(
                        str(con._id)
                        + " --> "
                        + str(obj.search_pattern)
                        + ", "
                        + str(obj.average_angle)
                    )


            if __name__ == "__main__":
                main()


    """


def ChangeDensity(connection_chains: object, density_factor: float) -> object:
    """

    Increase/Decrease density of the connections in a CONNECTION_CHAIN.

    Parameters
    ----------
    connection_chains : object
            A list of CONNECTION_CHAIN entities.

    density_factor : float
            A factor by which the density of the connections in the group are to be increased, or decreased.

    Returns
    -------
    object
            Always returns None.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                conn_list = base.CollectEntities(constants.NASTRAN, None, "CONNECTION_CHAIN")
                connections.ChangeDensity(conn_list, 1.5)


    """


def FeRepSettingsConvertIDsToReferences(connections: object) -> object:
    """

    changes some fields the FE-Rep settings of given connections to use entities
    by reference instead of entity IDs. Success of this conversion requires that
    an entity exists in the database that has compatible type and same ID as the ID
    mentioned in the FE-Rep settings.

    Parameters
    ----------
    connections : object
            A list of connection entities that their settings will be
            adjusted to use references

    Returns
    -------
    object
            Returns a dict where the keys are the connection entities which were given as input
            and the values are a list of options that could not be adjusted to use
            references.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                connection_types = ("AdhesiveLine_Type", "AdhesiveFace_Type")

                cnctns = base.CollectEntities(constants.NASTRAN, None, connection_types)

                unconverted_cnctns = connections.FeRepSettingsConvertIDsToReferences(cnctns)

                for cnctn in unconverted_cnctns:
                    if len(unconverted_cnctns[cnctn]):
                        print(
                            "Options [%s] could not be converted for connection #%d"
                            % (", ".join(unconverted_cnctns[cnctn]), cnctn._id)
                        )


    """


def ApplyDensityHistogram(
    connection_chains: object, interval_params: object, densities: object
):
    """

    Reset the density of the connections in a CONNECTION_CHAIN, by providing a histogram.
    This allows to set a density that varies along the polyline of the connection chain.

    The connections along the CONNECTION_CHAIN form a polyline.
    ApplyDensityHistogram() allows you to set a density value for various intervals
    of the polyline.

    The begining of the polyline corresponds to parameter value 0.0.
    The ending of the polyline corresponds to parameter value 1.0.
    The middle of the polyline corresponds to parameter value 0.5.

    The density of the connections is the number of connections per unit length.
    Density of 0.02 means:
    0.02 connections per mm. Or 2 connections every 10cm.
    Therefore, the spacing between consecutive connections is 50mm.

    The density histogram can be defined using two lists of equal size:

      interval_params = [0.00, 0.33, 0.66]
      densities       = [0.04, 0.03, 0.02]

    This will set the following densities to each interval of the CONNECTION_CHAIN:
    length interval: 0.00 - 0.33   =>  density = 0.04
    length interval: 0.33 - 0.66   =>  density = 0.03
    length interval: 0.66 - 1.00   =>  density = 0.02

    Since the intervals are consecutive, only the begining of each interval and the
    density are required to define the histogram.

    Parameters
    ----------
    connection_chains : object
            a list of ANSA "CONNECTION_CHAIN" entities.

    interval_params : object
            a list of the intervals on the polyline of each CONNECTION_CHAIN.

    densities : object
            A list, containing the density value for each interval in the 'interval_params'

    See Also
    --------
    ChangeDensity

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                conn_list = base.CollectEntities(constants.NASTRAN, None, "CONNECTION_CHAIN")

                connections.ApplyDensityHistogram(
                    conn_list,
                    interval_params=[0.00, 0.33, 0.50, 0.66],
                    densities=[0.04, 0.03, 0.02, 0.03],
                )


    """


def SortConnectivity(connections: object) -> bool:
    """

    Sorts connectivity parts geometrically.

    Parameters
    ----------
    connections : object
            A list with connections or a single connection.

    Returns
    -------
    bool
            Always returns True.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "SpotweldPoint_Type")

                connections.SortConnectivity(cnctns)


    """


def OpenCreateConnectionsOnFlanges() -> bool:
    """

    Opens the Define Connection > Flanges window.

    Returns
    -------
    bool
            Always returns True.

    Examples
    --------
    ::

            import ansa
            from ansa import connections


            def main():
                connections.OpenCreateConnectionsOnFlanges()


    """


def CompactConnectionFaces(connections: object) -> object:
    """

    For each unrealized connection in the argument list, this function tries to
    replace its original faces with as few as possible while maintaining the same
    mesh.
    The new elements (faces, shells, nodes) created are inserted in connection's
    INCLUDE.

    Parameters
    ----------
    connections : object
            a list of ANSA "AdhesiveFace_Type" entities.

    Returns
    -------
    object
            Returns a dictionary where the key is the connection id and the value is a bool
            indicating whether the faces of connection with the same id where successfully
            reduced or not.

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import connections


            def main():
                cnctns = base.CollectEntities(constants.NASTRAN, None, "AdhesiveFace_Type")

                result = connections.CompactConnectionFaces(cnctns)


    """


def ReadAssemblyScenario(filepath: str) -> int:
    """

    ansa.connections.ReadAssemblyScenario(filepath) reads a file of .ansa type, that was previously saved as Scenario from Template Manager

    Parameters
    ----------
    filepath : str
            : The full path to the file

    Returns
    -------
    int
            Returns 1

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import connections

            ansa.connections.ReadAssemblyScenario("path_to/scenario.ansa")


    """
