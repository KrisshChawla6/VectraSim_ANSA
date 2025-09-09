def MidSurfAuto(
    thick: float,
    faces: object,
    handle_many_solids: bool,
    handle_as_single_solid: bool,
    length: float,
    join_distance: float,
    elem_type: int,
    exact_middle: bool,
    paste_triple_len: float,
    add_features_to_set: int,
    part: str,
    ret_ents: bool,
    property: str,
    join_distance_as_percentage: bool,
    paste_triple_len_as_percentage: bool,
    connect_weldings: bool,
    thickness_ratio: float,
    sharpen_fillets_min_radius: float,
    thickness_limit: float,
    thickness_limit_percentage: float,
    get_result_type: bool,
    steady_thickness_limit: float,
    thickness_sides_min_angle: float,
    thickness_sides_max_width: float,
    intersection_angle: float,
    get_solid_percentage: bool,
    inherit_mesh_from: str,
    reset_resolution_percentage: int,
    collapse_ribs_height: float,
    collapse_ribs_height_as_percentage: bool,
) -> object:
    """

    Creates mesh in the middle surface of solids defined by faces.
    It needs a list of (argument name, argument value) pairs.

    Parameters
    ----------
    thick : float
            The minimum thickness of the solid(s), must be > 0.

    faces : object, optional
            A list of faces and shells. (if 0 is typed then it runs for all faces and shells of the database)

    handle_many_solids : bool, optional
            Deprecated

    handle_as_single_solid : bool, optional
            If set to True, input is handled as a single solid

    length : float, optional
            The target element length must be greater than the minimum thickness.
            By default it equals to the minimum thickness.

    join_distance : float, optional
            The minimum distance where two perimeters are collapsed.

    elem_type : int, optional
            Accepted values:
            -1: QUAD
            -2: TRIA
            -3: MIXED
            -4" ORTHO_TRIA
            (Default:3)

    exact_middle : bool, optional
            If set to False, Y-Treatment is enabled.

    paste_triple_len : float, optional
            The minimum distance where two triple bounds are collapsed.

    add_features_to_set : int, optional
            Deprecated.

    part : str, optional
            Accepted values: "use_existing", "use_current", "auto_create" and "id=<integer>".

    ret_ents : bool, optional
            If set to True, a list with the created entities will be returned.

    property : str, optional
            Accepted values: "use_existing", "use_current", "auto_create" and "id=<integer>".

    join_distance_as_percentage : bool, optional
            If set to True, "join_distance" value is used as a percentage with respect to target length.

    paste_triple_len_as_percentage : bool, optional
            If set to True, "paste_triple_len" value is used as percentage with respect to target length.

    connect_weldings : bool, optional
            Is set to True, weldings are automatically connected after casting,

    thickness_ratio : float, optional
            The minimum distance where two areas are connected, expressed as a ratio of the local nodal thickness.

    sharpen_fillets_min_radius : float, optional
            The minimum radius where a fillet is sharpened.

    thickness_limit : float, optional
            The thickness limit for an area to be identified as solid.

    thickness_limit_percentage : float, optional
            The percentage of the area above a thickness_limit where a part would be identified as solid.

    get_result_type : bool, optional
            If set to True it returns the result type of each input part.

    steady_thickness_limit : float, optional
            If get_result_type is enabled it sets the limit where two areas are considered to have different thickness.

    thickness_sides_min_angle : float, optional
            Minimum angle that defines whether a face is identified as thickness side.

    thickness_sides_max_width : float, optional
            Maximum width that defines whether a face is identified as thickness side.

    intersection_angle : float, optional
            Modifies the intersection angle limit. Valid values are between 5 and 45 degrees.

    get_solid_percentage : bool, optional
            Always return solid percentage in the return list (thickness_limit must be set)

    inherit_mesh_from : str, optional
            The full path of the database which is used as a reference for inherit middle mesh.

    reset_resolution_percentage : int, optional
            Reset solid description resolution using a percentage of target element length. If set to 0 resolution is not affected. Default value is 50.

    collapse_ribs_height : float, optional
            The minimum distance under which a rib is collapsed.

    collapse_ribs_height_as_percentage : bool, optional
            If set to True, "collapse_ribs_height" value is used as percentage with respect to target length.

    Returns
    -------
    object
            Returns 0 on success or 1 on failure.
            If ret_ents is True it returns a list with the created entities, or None if no entities are created.
            If get_result_type is True it returns an object 'ret' with the following members:
            ret.type: a list of result types in the following format ["input part id", "output part id", "type", "solid percentage"] or in the following format ["part id", "failed percentage", "type", "solid percentage"] if the part has been identified as solid. Return types are "Ribs", "Steady thickness", "Variable thickness" and "Solid".
            ret.ents: (if ret_ents is True) a list with the created entities, or None if no entities are created

    Examples
    --------
    ::

            from ansa import base


            def main():
                results_list = []

                search_face = ("FACE",)
                all_faces = base.CollectEntities(0, None, search_face, False)
                result = base.MidSurfAuto(
                    faces=all_faces,
                    thick=2.0,
                    length=5.0,
                    elem_type=3,
                    join_distance=50,
                    join_distance_as_percentage=True,
                    paste_triple_len=50,
                    paste_triple_len_as_percentage=True,
                    handle_as_single_solid=False,
                    thickness_limit=5,
                    thickness_limit_percentage=25,
                    get_result_type=True,
                    part="use_current",
                    property="id=5",
                )


    """


def CollectEntities(
    deck: int,
    containers: Entity | Iterable | None,
    search_types: str | Iterable,
    recursive: bool = False,
    filter_visible: bool = False,
    prop_from_entities: bool = False,
    mat_from_entities: bool = False,
    model_browser_filter: dict = {},
    no_expand_types: Iterable = None,
    hidden_entities: bool = True,
) -> List[Entity]:
    """

    Creates a list with the entities of specific types, contained in the containers.

    Parameters
    ----------
    deck : int
            The deck for which the collection will take place.

    containers : Entity | Iterable | None
            A reference to a container  entity or list with references to  containers.
            Some of the containers can be of type ANSAGROUP, ANSAPART, SET,
            property, material, face,  volume, elements, task manager items etc
            If the container is None, CollectEntities will search the entire
            ANSA database.

    search_types : str | Iterable
            A string or list of strings with "ansa keywords" of the types to be
            collected. Such types can be SHELL, SOLID, GRID etc.
            Additionally, the following keywords can be used:
            "__PROPERTIES__": returns all properties in the "containers".
            "__MATERIALS__": returns all materials in the "containers".
            "__ELEMENTS__": returns all standard elements in the "containers".
            "__ALL_ENTITIES__": returns all entities in the "containers".
            "__CONNECTIONS__": returns all connections in the "containers".
            "__MBCONTAINERS__": returns the model browser containers of the model if
            used with containers=None or the model browser containers of the containers.
            "__COORD_SYSTEMS__": returns all the coordinate systems in the "containers".
            "__CONNECTION_TEMPLATES__": returns all the connection templates in the "containers".
            "__OUT_OF_MBCONTAINERS__": returns the entities of the OutOfMBContainer. Can be used along with argument model_browser_filter.
            "BATCH_MESH_SESSION_GROUP": returns the meshing scenarios of Batch Mesh
            "BATCH_MESH_VOLUME_SCENARIO": returns the volume scenarios of Batch Mesh
            "BATCH_MESH_WRAP_SCENARIO": returns the wrap scenarios of Batch Mesh
            "BATCH_MESH_LAYERS_SCENARIO": returns the layer scenarios of Batch Mesh

    recursive : bool, optional
            Recursively search any containers contained in a higher level container
            for any of the search_types. (Default: False).

    filter_visible : bool, optional
            Return only the entities that satisfy all the collection criteria,
            have visibility status, and the status is active.
            In all other cases the parameter is ignored.
            (Default: False).

    prop_from_entities : bool, optional
            In case search_type is a property, this argument controls if the property
            must be acquired from the entities referenced by the entities in the
            container or not. For example, if search_type is "PSHELL", container is
            "PART", and prop_from_entities is True, if the part contains shells, the
            corresponding PSHELL will be returned.
            Otherwise, if prop_from_entities is False, None will be returned.
            (Default: False).

    mat_from_entities : bool, optional
            In case search_type is a material, this argument controls if the material
            must be acquired from the entities referenced by the entities in the
            container or not. For example, if search_type is "MAT1", container is
            "PART", and mat_from_entities is "yes", if the part  contains elements
            with MAT1 material, the corresponding material will be returned.
            Otherwise, if mat_from_entities is False, None will be returned.
            (Default: False).

    model_browser_filter : dict, optional
            In case search_types is None, this argument controls which entities to
            collect from a Part, a Group, a Subsystem, a Simulation Model or a
            Simulation Run. 'model_browser_filter' is a dictionary with three keys:
            'container', 'collect_mode' and 'collect_depth'.Acceptable values for these keys
            vary according to the entity they are applied on.

            -When collecting entities from a Part or a Group:
            { 'container' : 'all', 'collect_mode' : 'contents' | 'part_contents_and_references' | 'part_contents_and_related'} ,  'collect_depth' key is not applicable here.

            'container' values:
            -'all' returns entities of any type

            'collect_mode' values:
            -'contents' returns entities that strictly belong to the Part or the Group.
            -'part_contents_and_references' returns the 'contents' plus their properties and
            materials.
            -'part_contents_and_related'  returns the 'contents_related' plus all entities that
            are geometrically related to it (use same nodes or are otherwise connected).
            -'contents_related' .This value is deprecated, replaced by 'part_contents_and_references'.
            -'contents_affected'. This value is deprecated, replaced by 'part_contents_and_related'.

            -When collecting entities from a Subsystem, a Simulation Model or a
            Simulation Run:
            { 'container': 'all' | 'geometry' | 'connections' | 'model_setup_entities' | 'interfaces',
            'collect_mode': 'contents' | 'missing' | 'misplaced',
            'collect_depth': 'own_level' | 'all_levels' }

            'container' values:
            -'all' returns entities of any type.
            -'geometry' returns geometry entities.
            -'connections' returns Connections & Connectors.
            -'model_setup_entities' returns Model Setup Entities
            (like RBE3s directly connected to geometry)
            -'interfaces' returns Interfaces (like A_POINTs).

            'collect_mode' values:
            -'contents' returns entities that directly belong to the 'container'.
            -'missing' returns entities that don't belong to the 'container' but should do.
            -'misplaced' returns entities that belong to the 'container' but shouldn't do.

            'collect_depth' values:
            -'own_level' returns entities that are directly under the 'container', not under its inner containers.
            -'all_levels' returns entities found at any inner level under 'container'.
            Example:
            In case we want to collect the Connections of a SimModel, only the ones that are directly under it, we use 'own_level'.On the contrary, in case we wish to collect all connections, both from the SimModel as well as the connections under its subsystems/rlis, we use 'all_levels'.

            Note that use of model_browser_filter argument demands setting 'containers' argument with a value other than 'None'.
            Note that 'missing' and 'misplaced' are not defined for the
            GEOMETRY_OUT_OF_SUBSYSTEMS Subsystem(obsolete since 22.0.0).

    no_expand_types : Iterable, optional
            A list with ANSA types which won't be expanded while collecting their
            entities. Currently it works only for SETs with recursive = False,
            no_expand_types = ('SET',) in order to get the first level SET contents.

    hidden_entities : bool, optional
            If hidden_entities = False the hidden (inactive) entities will not be collected. These are the entities that are listed in the "Inactive" category of the Database Browser (e.g entities of parts with representation="Don't Use"). Default is True.

    Returns
    -------
    List[Entity]
            Returns a list with all the collected entities.

    See Also
    --------
    base.CollectEntitiesI

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants


            def main():
                set1 = base.CreateEntity(constants.NASTRAN, "SET", {"Name": "new set 1"})

                m = []
                containers = []

                for i in range(1, 100):
                    m.append(base.GetEntity(constants.NASTRAN, "GRID", i))
                base.AddToSet(set1, m)

                prop = base.GetEntity(constants.NASTRAN, "PSHELL", 1)

                containers.append(set1)
                containers.append(prop)

                ents = base.CollectEntities(constants.NASTRAN, containers, "GRID", recursive=True)
                for ent in ents:
                    base.SetEntityCardValues(
                        constants.NASTRAN, ent, {"Name": "node of set 1 or prop 1"}
                    )


            def main():
                part = base.GetPartFromModuleId("10")

                pshells = base.CollectEntities(
                    constants.NASTRAN, part, "PSHELL", prop_from_entities=True
                )
                for pshell in pshells:
                    print("PID: ", pshell._id)
                materials = base.CollectEntities(
                    constants.NASTRAN, part, "__MATERIALS__", mat_from_entities=True
                )
                for material in materials:
                    print("MID:", material._id)


            def main():
                subsystem = base.Entity(constants.ABAQUS, 1, "ANSA_SUBSYSTEM")

                mbf = {"container": "interfaces", "collect_mode": "contents"}
                interfaces = base.CollectEntities(
                    constants.ABAQUS, subsystem, None, model_browser_filter=mbf
                )

                mbf = {"container": "connections", "collect_mode": "contents"}
                connections = base.CollectEntities(
                    constants.ABAQUS, subsystem, None, model_browser_filter=mbf
                )

                mbf = {"container": "all", "collect_mode": "contents"}
                entities = base.CollectEntities(
                    deck=0,
                    containers=None,
                    search_types="__OUT_OF_MBCONTAINERS__",
                    model_browser_filter=mbf,
                )


    """
