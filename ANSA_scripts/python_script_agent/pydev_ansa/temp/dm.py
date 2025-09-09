from __future__ import annotations
from typing import *
from datetime import datetime


def ChangeIncludeRepresentation(entities: object, new_representation: str) -> object:
    """

    Changes the representation of a given list of Include entities, with a new one from the DM,
    specified by the string new_representation. This can also be the common representation by
    giving the string 'common'.

    Parameters
    ----------
    entities : object
            A list of include entities.

    new_representation : str
            The name of the new representation.

    Returns
    -------
    object
            The function returns:
            1) An empty list in the case where all the includes have changed representation successfully.
            2) A list that contains all the includes that did not change representation successfully.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                includes = base.CollectEntities(0, None, "INCLUDE")

                ret_val = dm.ChangeIncludeRepresentation(includes, "crash1")
                print(ret_val)


    """


def ChangeRepresentation(
    entities: object,
    new_representation: str,
    property_conflicts: str,
    material_conflicts: str,
    set_conflicts: str,
    rbe_option: str,
    distance: float,
    mass: float,
    deck: str,
    include_connectors: bool,
    spc_dofs: int,
    coord_conflicts: str,
    node_conflicts: str,
    propsection_confilcts: str,
) -> object:
    """

    Changes the representation of a given list of ANSA PARTS, with a new one from the DM.

    Parameters
    ----------
    entities : object
            A list of ANSA parts whose representation will change.

    new_representation : str
            The name of the new representation.

    property_conflicts : str, optional
            "Offset" creates a new entity.
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value (Default).

    material_conflicts : str, optional
            "Offset" creates a new entity.
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value (Default).

    set_conflicts : str, optional
            "Offset" creates a new entity (Default).
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value.

    rbe_option : str, optional
            String Variable that determines the type of the connecting element to be used.
            Valid types are: "RBE2", "RBE3" and only for "Lumped Mass" Representation.

    distance : float, optional
            Search distance of the respective GEB_MT, valid only for "Trim" Representation.

    mass : float, optional
            Mass field of the respective GEB_MT, valid only for "Trim" Representation.

    deck : str, optional
            A string that describes the deck, valid only for "Trim" Representation.
            (Default: Current Deck)

    include_connectors : bool, optional
            A boolean that determines if the external connectors will be included
            in the SPC Representation or the "Don't Use" Representation or the
            Lumped Mass Representation.
            (Default: False)

    spc_dofs : int, optional
            Integer that specifies the affected Degrees Of Freedom.
            Valid only for "SPC" Representation.

    coord_conflicts : str, optional
            "Offset" creates a new entity (Default).
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value.

    node_conflicts : str, optional
            "Offset" creates a new entity (Default).
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value.

    propsection_confilcts : str, optional
            "Offset" creates a new entity.
            "KeepOld" keeps the old value.
            "KeepNew" keeps the new value (Default).

    Returns
    -------
    object
            Returns a dictionary with keys: 'status' and 'session_group'.
            Under 'status' key, value 0 is returned if an invalid representation was given.
            In all other cases, value 1 is returned.
            Under 'session_group' key, a batch mesh scenario will be returned, that is assigned
            to all parts that required a new mesh.

    Examples
    --------
    ::

            # Example 1
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import batchmesh
            from ansa import dm


            def main():
                all_parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
                unupdated_parts = dm.ChangeRepresentation(all_parts, "crash10")
                ret = batchmesh.RunMeshingScenario(unupdated_parts["session_group"])


            # Example 2
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import batchmesh
            from ansa import dm


            def main():
                all_parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
                unupdated_parts = dm.ChangeRepresentation(
                    all_parts,
                    "crash10",
                    property_conflicts="KeepOld",
                    material_conflicts="KeepNew",
                    set_conflicts="Offset",
                )
                ret = batchmesh.RunMeshingScenario(unupdated_parts["session_group"])

                # Don't Use:
                parts = [base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT")]
                dm.ChangeRepresentation(parts, "Don't Use", include_connectors=True)

                # Use:
                parts = [base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT")]
                dm.ChangeRepresentation(parts, "Use")

                # Lumped Mass:
                parts = [base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT")]
                dm.ChangeRepresentation(
                    parts, "Lumped Mass", include_connectors=True, rbe_option="RBE3"
                )

                # SPC:
                parts = [base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT")]
                dm.ChangeRepresentation(parts, "SPC", include_connectors=True, spc_dofs=123456)

                # Trim:
                parts = (base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT"))
                dm.ChangeRepresentation(parts, "Trim", distance=10, mass=0.005, deck="NASTRAN")


    """


def SyncRepresentation(parts: object) -> int:
    """

    Synchronizes the representation of a given list of ANSA PARTS, to all instances of the
    given ANSA PARTS. Any entities that are included in those instances will be deleted.

    Parameters
    ----------
    parts : object
            A list that contains the parts whose instances will be synchronised.

    Returns
    -------
    int
            Returns 1 on error and 0 on success.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            def main():
                all_parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
                dm.SyncRepresentation(all_parts)


    """


def SaveRepresentation(
    ents: object,
    save_group_or_part: str,
    overwrite_opt: int,
    skip_save_for_multi_instances: bool,
    save_marked_read_only: bool,
    save_empty_groups: bool,
    conflicts_option: str,
    export_jt: bool,
    export_png: bool,
    file_type: str,
    return_server_ids: bool,
    return_value_type: str,
    backup_failed_save_folder: str,
    export_metadb: bool,
) -> int:
    """

    Saves the representation of a given list of parts, groups or includes in the DM.
    A DM Root has to be already specified.

    Parameters
    ----------
    ents : object
            A list that contains parts, groups or includes.

    save_group_or_part : str
            Determines if groups or inner parts will be saved in DM.
            Accepted values: "GROUP" or "PART".

    overwrite_opt : int
            0: In case current representation is found in DM,
            the save procedure for the particular part should be skipped.
            In this case (skip) the returned value is 1 (failure).
            1: In case current representation is found in DM,
            it should be overwritten.
            2: In case current representation is found in DM,
            Study Version or another versioning scheme counter
            (see argument: conficts_option) is spinned-up
            (only applies to parts).

    skip_save_for_multi_instances : bool, optional
            True: Do not save multi-instanciated parts.
            False (default): Save only one instance for each
            multi-instanciated part.

    save_marked_read_only : bool, optional
            True: Save representation for includes marked as read-only.
            False (default): Do not save representation for includes
            marked as read-only.

    save_empty_groups : bool, optional
            True: Save empty groups.
            False (default): Do not save empty groups.

    conflicts_option : str, optional
            The name of the versioning scheme counter attribute to be spinned-up
            (overwrite_opt = 2).
            A versioning scheme counter attribute name: a spin-up is performed
            to the value of that attribute.
            Empty: Study Version is spinned-up instead.

    export_jt : bool, optional
            True: Save jt file during saving representation of part
            False (default): Do not save jt file

    export_png : bool, optional
            True: Save png image during saving representation of part
            False (default): Do not save png image

    file_type : str, optional
            This argument determines the format of the parts representation files that are about to be saved. Acceptable values are :
            "ANSA", "Nastran", "LsDyna", "PamCrash", "Abaqus", "Radioss", "Ansys", "Fluent", "FluentD", "StarCD", "Uh3D", "Cfd++", "OpenFoam", "Permas", "Moldex3D", "TAITHER", "Sestra", "Theseus", "ScTetra", "TAU", "CGNS", "CGNS2D", "Optistruct"

    return_server_ids : bool, optional
            True: Returns a python list containing the server ids of the parts saved, in the order of their input. Parts that failed to be saved have a "0" entry.
            False: To be used in conjunction with return_value_type argument.

    return_value_type : str, optional
            "server_ids_and_error_messages" : Returns a python list where each of the input parts has a corresponding entry, listed in the order of their input.
            The parts that were successfully saved have as corresponding entry their server_id.
            The ones that failed have as corresponding entry a python list containing the error(s) that resulted to their failure to be saved.
            "server_ids" : Returns a python list containing the server ids of the parts saved, in the order of their input. Parts that failed to be saved have a "0" entry.
            Warning: This argument is overriden if return_server_ids is True.

    backup_failed_save_folder : str, optional
            Argument only for internal usage.

    export_metadb : bool, optional
            True: Save metadb file during saving representation of part
            False (default): Do not save metadb file

    Returns
    -------
    int
            0 (success): If all entities are saved in DM successfully.
            1 (failure): If the saving procedure has failed or was skipped for at least one
                         entry of the entities list.

            Warning: Return type may be different. See also arguments "return_server_ids"
            and "return_value_type" that affect the returned value.

    See Also
    --------
    GetSaveRepresentationConflictOptions

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            # ex.1 : Save group
            def main():
                all_parts = base.CollectEntities(0, None, "ANSAGROUP")
                ret = dm.SaveRepresentation(all_parts, "GROUP", 1, save_empty_groups=True)
                print(ret)


            # ex.2 : Save parts
            def main():
                all_parts = base.CollectEntities(0, None, "ANSAPART")
                ret = dm.SaveRepresentation(
                    all_parts, "PART", 1, skip_save_for_multi_instances=True
                )
                print(ret)


            # ex.3 : Save includes
            def main():
                all_parts = base.CollectEntities(0, None, "INCLUDE")
                ret = dm.SaveRepresentation(
                    all_parts,
                    "PART",
                    1,
                    skip_save_for_multi_instances=False,
                    save_marked_read_only=True,
                )
                print(ret)


    """


def OpenJtRepresentation(parts: object) -> int:
    """

    Import in ANSA the Jt image of an empty part, as it is saved in the current DM.
    If a Group is provided, all its children are traveled and their Jt images are imported.

    Parameters
    ----------
    parts : object
            A list containing parts.

    Returns
    -------
    int
            Returns 0 on error and 1 on success.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                parts = [base.GetPartFromModuleId("55"), base.GetPartFromModuleId("68FRONT")]
                dm.OpenJtRepresentation(parts)


    """


def SaveSubsystems(
    ents: object,
    conflicts_option: str,
    spin_up_attribute: str,
    save_repr_file: str,
    export_png: str,
    export_jt: str,
    export_meta_db: str,
    file_type: str,
    save_ansa_repr_file: str,
    save_include_repr_file: str,
    autofix: object,
    detailed_results: bool,
    lbr_assign_values: object,
) -> object:
    """

    Saves a given list of subsystems in the DM.
    A DM Root directory must already be specified.

    Parameters
    ----------
    ents : object
            A list that contains subsystems.

    conflicts_option : str, optional
            -'Overwrite'
            -'Skip'
            -'Spin_up' (default)

    spin_up_attribute : str, optional
            'Study Version' (default)

    save_repr_file : str, optional
            -'YES': save along with the subsystem a respective representation file.
            -'NO'
            This argument is only available for backward compatibility reasons.
            Use save_ansa_repr_file and save_include_repr_file instead.

    export_png : str, optional
            -'YES': save along with the subsystem an image in .png format.
            -'NO' (default)

    export_jt : str, optional
            -'YES': save along with the subsystem a respective jt file.
            -'NO' (default)

    export_meta_db : str, optional
            This argument is not yet supported.

    file_type : str, optional
            The file type (file extension) of a subsystem's representative
            file in the DM. The argument can either have the value "ANSA" or
            any supported deck's file name, e.g. Nastran, LsDyna, Radioss, Abaqus, etc.

    save_ansa_repr_file : str, optional
            Possible values: "monolithic" / "references" / "structure_only"
            -"monolithic" : The resulting representation file will be an ANSA database
            containing all ANSA entities.
            -"references" : The resulting representation file will be an ANSA database
            containing the hierarchy in the Model Browser, but no ANSA entities.
            -"structure_only" : No representation file will be saved.

    save_include_repr_file : str, optional
            Possible values: "monolithic" / "references" / "structure_only"
            -"monolithic" : The resulting representation file will be a Deck file according
            to file_type argument containing all ANSA entities
            -"references" : The resulting representation file will be a Deck file according
            to file_type argument containing references to the Subsystem's children Includes
            as separate files - e.g: #include "C:/home/my_inner_include.nas"
            -"structure_only" : No representation file will be saved.

    autofix : object, optional
            This argument is a List of strings. Possible values it can contain:
            "filetype_discrepancy"
            "missing_subsystem_inner_part_repr_files"
            "unapplied_numbering_rules"
            "generate_missing_solver_files"

            All its member string values will attempt to autofix in case the respective
            errors have been  encountered.

    detailed_results : bool, optional
            This argument determines whether the return value will be a list of strings
            representing the server_ids or a list of "SaveInDmObject" named tuples.
            For more information check the "Return type" field.

    lbr_assign_values : object, optional
            This argument is a Python dictionary, which accepts key-value of properties or attributes that we wish to edit right before saving the Simulation Model in DM, like {'DM/Status':'Frozen'}. It is most commonly used in the cases of DM with Lifecycle Business Rules where there is a rule that defines that certain properties/attributes are only allowed to change when a representation file is also uploaded. For these cases we use this argument and edit them simultaneously with their file upload.

    Returns
    -------
    object
            - In case the detailed_results argument does not exist or is False:
            The return value is a list with the same size as the ents list (input argument).
            Each entry of the returned list is a string with a special id of the saved subsystem.
            In case the subsystem failed to be saved, a string with zero value is returned ('0').
            - In case the detailed_results argument exists and is True:
            Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Subsystems that we attempted to save in DM.
            Each "SaveInDMObject" ret contains 4 members:
            ret.entity    : ANSA entity we tried to save(the Simulation Model)
            ret.server_id : (string) The id by which it has been saved in DM
            ret.error     : (string) A description of the reason it failed to be saved.
            ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
                                     inner SimulationModels/Subsystems/Includes that were
                                     involved in Save and have caused save failure

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            def main():
                subsystems = base.CollectEntities(constants.NASTRAN, None, "ANSA_SUBSYSTEM")

                ret = dm.SaveSubsystems(
                    ents=subsystems,
                    conflicts_option="Spin_up",
                    spin_up_attribute="Study Version",
                    save_repr_file="YES",
                    export_png="YES",
                    export_jt="YES",
                    file_type="ANSA",
                )
                for item in ret:
                    if item == "0":
                        print("Failed to save subsystem!")
                    else:
                        print("Saved! Id = ", item)


            # -------- Example demonstrating the use of the detailed_results argument ------#
            def getSpacesAsManyAsLevelsDown(levels_down):
                spaces = ""
                for i in range(0, levels_down):
                    spaces += "   "
                return spaces


            def printSaveInDMResultObjectsForInnerChildrenErrors(inner_child_object, levels_down):
                spaces = getSpacesAsManyAsLevelsDown(levels_down)
                print(spaces, "server_id=", inner_child_object.server_id)
                print(spaces, "error=", inner_child_object.error)
                print(spaces, "entity=", inner_child_object.entity)
                print(spaces, "inners=", inner_child_object.inners)
                if inner_child_object.inners != None:
                    levels_down += 1
                    for inner_object in inner_child_object.inners:
                        printSaveInDMResultObjectsForInnerChildrenErrors(inner_object, levels_down)


            def printSaveInDMResultObjects(ret_objs):
                for object in ret_objs:
                    printSaveInDMResultObjectsForInnerChildrenErrors(object, 0)


            def executeTheSavingSubsystemsReportDetailedResults(all_subsystems):
                print("Detailed results")
                ret_val = dm.SaveSubsystems(
                    ents=all_subsystems,
                    conflicts_option="Overwrite",
                    file_type=constants.NASTRAN,
                    save_include_repr_file="references",
                    autofix=["filetype_discrepancy", "missing_subsystem_inner_part_repr_files"],
                    detailed_results=True,
                )
                printSaveInDMResultObjects(ret_val)


            def executeTheSavingSubsystemsReportServerIdsOnly(all_subsystems):
                print("Server ids only")
                ret_val = dm.SaveSubsystems(
                    ents=all_subsystems,
                    conflicts_option="Overwrite",
                    file_type=constants.NASTRAN,
                    save_include_repr_file="references",
                    autofix=["filetype_discrepancy", "missing_subsystem_inner_part_repr_files"],
                )
                print(ret_val)


            def prepareForTheSaveSubsystemsInDM():
                base.SetCurrentDeck(constants.NASTRAN)
                succ = base.SetDMRoot("/home/temp_DM1")
                if succ == 0:
                    print("Something is wrong: I could not connect to the DM")
                    return None
                all_subsystems = base.CollectEntities(
                    0, containers=None, search_types="ANSA_SUBSYSTEM"
                )
                return all_subsystems


            def main():
                all_subsystems = prepareForTheSaveSubsystemsInDM()

                if all_subsystems == None:
                    return
                executeTheSavingSubsystemsReportDetailedResults(all_subsystems)

                executeTheSavingSubsystemsReportServerIdsOnly(all_subsystems)


    """


def OpenSubsystemsInNewTab(
    server_ids: object,
    subsystems: object,
    type: str,
    view: str,
    dm_system: str,
    tab_name: str,
    expand_all: bool,
    open_in_viewer: bool,
) -> bool:
    """
    .. deprecated:: 19.0.0
            Use :py:func:`OpenDMObjectsInNewTab` instead.


    This function can be used to open one or more Subsystem's hierarchy in a new tab
    in DM Browser or SDM CONSOLE.
    Specific objects can also be opened in a new tab, such as "parts", "includes" etc.

    Parameters
    ----------
    server_ids : object, optional
            A list with DM Object server ids.

    subsystems : object, optional
            A list with ANSA entities.

    type : str, optional
            The queried type needs to be defined, e.g. "Subsystems", "parts".
            When undefined, the function will return False.

    view : str, optional
            The new Tab's view, e.g. "Default", "Flat" or a user defined in the dm_views.xml.
            When undefined, the function will return False.

    dm_system : str, optional
            The DM root that will be queried.

    tab_name : str, optional
            The new tab will be given this name.

    expand_all : bool, optional
            If set to True, all items in the new tab will be expanded.

    open_in_viewer : bool, optional
            If set to True, all items in the new tab will be loaded to the meta viewer.

    Returns
    -------
    bool
            Returns True if the tab is opened succesfully, otherwise False.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                map = {"Project": "L1", "Discipline": "Crash"}
                server_id = dm.GetDMObjectId("Subsystems", map)
                if server_id:
                    list_of_ids = []
                    list_of_ids.append(server_id)
                    base.OpenSubsystemsInNewTab(
                        server_ids=list_of_ids,
                        type="Subsystems",
                        view="Default",
                        tab_name="Subsystem in question",
                    )


            # in case of Part
            def main():
                parts = [base.GetPartFromModuleId("607001"), base.GetPartFromModuleId("607002")]
                base.OpenSubsystemsInNewTab(subsystems=parts, type="parts", view="Flat")


    """

    import warnings

    warnings.warn(
        "Deprecated since version 19.0.0. Use :py:func: OpenDMObjectsInNewTab instead.",
        DeprecationWarning,
    )


def SaveSimulationRun(
    ents: object,
    conflicts_option: str,
    spin_up_attribute: str,
    file_content_loadcase: str,
    file_content_sim_model: str,
    file_type: Any,
    use_loaded_loadcase: bool,
    autofix: object,
    use_loaded_sim_model: bool,
    ansa_db_save_mode: str,
    file_content_base_modules: str,
    lbr_assign_values: object,
) -> object:
    """

    Saves the representation of a given list of simulation runs in the DM.
    The file will be saved/outputted corresponding to the file_type format. A DM Root has to be specified.

    Parameters
    ----------
    ents : object
            A list that contains Simulation Runs that the user intends to save in DM.

    conflicts_option : str, optional
            Can support 3 possible values: "Overwrite" / "Skip" / "SpinUp".
            Determines what will happen in case that a Simulation Run that is
            intented to be saved, is found already inside DM.

    spin_up_attribute : str, optional
            Any of the attributes a SimulationRun has in the current DM root and for
            which spinning up could be achieved. e.g. "Study Version".
            Note here that even though this is an optional argument, in case that
            conflicts_option="SpinUp", then this argument becomes mandatory.

    file_content_loadcase : str, optional
            Possible values: "monolithic" / "references" / "existing_setup"
            -"monolithic": The resulting Simulation Run file will contain ANSA
             entities of its loadcase.
            -"references": The resulting Simulation Run file will contain reference
              line to a separate file of its loadcase.
              e.g. #include "C:/home/my_loadcase.nas"
            -"existing_setup": The resulting Simulation Run file will either be a
              reference line to its Loadcase or its ANSA entities, depending on the
              options "ReadOnly" and "Inline" of the Loadcase's  Include.
            -"reference_inner_contents": The resulting Simulation Run file will
              contain reference lines directly to inner contents of its Loadcase.
              e.g. #include "C:/home/MyDm/Barriers/Bar1.dat

    file_content_sim_model : str, optional
            Possible values: "monolithic" / "references" / "existing_setup"
            -"monolithic" : The resulting Simulation Run file will contain ANSA
              entities of its simulation model.
            -"references" : The resulting Simulation Run file will contain
              reference line to a separate file of its simulation model.
              e.g. #include "C:/home/my_sim_model.nas"
            -"existing_setup" : The resulting Simulation Run file will either be a
              reference line to its Simulation model or its ANSA entities,
              depending on the options "ReadOnly" and "Inline"  of the Simulation
              Model's Include.
            -"reference_inner_contents": The resulting Simulation Run file will
              contain reference lines directly to inner contents of its Simulation
              Model.
              e.g. #include "C:/home/MyDm/Subsystems/Sub1.nas

    file_type : Any, optional
            One of: "ANSA", "structure_only" or constants of Decks
            (e.g. ansa.constants.NASTRAN)
            In each case:
            -"structure_only": an ".xml" file will be saved in DM for each Simulation Model,
                               containing only its hierarchy.
            -"ANSA": ANSA database
            -ansa.constants.XXXX: a deck format to Output the SimModel.

            In case the argument is ommitted, the Current Deck is used.
            Attention!! Current deck outputting is currently fully supported.

    use_loaded_loadcase : bool, optional
            This argument determines whether the Loadcase that will be outputted in the
            Simulation Run representation file will be the one currently loaded in ANSA.
            Hence:
            -True: Use Loadcase currently loaded in ANSA (which means that changes of
              the user on the current session of ANSA will affect it).
            -False:  Use Loadcase as found in the library items that it refers to, as these
              are found in DM.

    autofix : object, optional
            This argument is a List of strings. Possible values it can contain:
            -"filetype_discrepancy"
            -"missing_subsystem_includes"
            -"reduced_representations_not_ready_for_use"
            -"missing_display_include_on_FRF_output".
            -"generate_missing_solver_files".

            All its member string values will attempt to autofix in case that the
            respective errors have been encountered.

    use_loaded_sim_model : bool, optional
            This argument determines whether the SimModel that will be outputted in the
            Simulation Run representation file will be the one currently loaded in ANSA.
            Hence:
            -True: Use Loadcase currently loaded in ANSA (which means that changes of
              the user on the current session of ANSA will affect it).
            -False: Use Loadcase as found in DM.

    ansa_db_save_mode : str, optional
            This arguments controls the contents of the ansa file to be produced and uploaded
            in DM. Accepted values are the following:
            -"monolithic" : A full ansa db will be uploaded in DM
            -"empty_hierarchy" : A db containing an empty description of the selected
              Simulation Run
            -"structure_only" : No ansa db will be uploaded in DM

    file_content_base_modules : str, optional
            Possible values: "monolithic" / "references" / "existing_setup"
            -"monolithic" : Entities of Base Modules of Simulation Run
              will be written monolithically in the resulting Simulation Run file
            -"references" : The resulting Simulation Run file will contain
              reference lines to separate files of Base Modules
              e.g. #include "C:/home/my_base_module.nas"
            -"existing_setup" : Base Modules' handling will depend on
              value of "Output Option" attribute

    lbr_assign_values : object, optional
            This argument is a Python dictionary, which accepts key-value of properties or attributes that we wish to edit right before saving the Simulation Model in DM, like {'DM/Status':'Frozen'}. It is most commonly used in the cases of DM with Lifecycle Business Rules where there is a rule that defines that certain properties/attributes are only allowed to change when a representation file is also uploaded. For these cases we use this argument and edit them simultaneously with their file upload.

    Returns
    -------
    object
            Returns a list containing "SaveInDMObject" objects, corresponding to each one of the Simulation Runs
            that we attempted to save in DM.
            Each "SaveInDMObject" ret contains 3 members:
            ret.entity      : The ANSA entity we tried to save (the Simulation Run).
            ret.server_id   : (string) The id by which it has been saved in DM.
            ret.error       : (string) A description of the reason it failed to be saved.
            ret.inners      : (list) A list of "SaveInDmObject" objects corresponding to the
                                     inner SimulationModels/Subsystems/Includes that were
                                     involved in Save and have caused save failure.

    See Also
    --------
    SaveSimulationModel, SaveLoadcase

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            def getSpacesAsManyAsLevelsDown(levels_down):
                spaces = ""
                for i in range(0, levels_down):
                    spaces += "   "
                return spaces


            def printSaveInDMResultObjectsForInnerChildrenErrors(inner_child_object, levels_down):
                spaces = getSpacesAsManyAsLevelsDown(levels_down)
                print(spaces, "server_id=", inner_child_object.server_id)
                print(spaces, "error=", inner_child_object.error)
                print(spaces, "entity=", inner_child_object.entity)
                print(spaces, "inners=", inner_child_object.inners)
                if inner_child_object.inners != None:
                    levels_down += 1
                    for inner_object in inner_child_object.inners:
                        printSaveInDMResultObjectsForInnerChildrenErrors(inner_object, levels_down)


            def printSaveInDMResultObjects(ret_objs):
                for obj in ret_objs:
                    printSaveInDMResultObjectsForInnerChildrenErrors(obj, 0)


            def main():
                simruns = base.CollectEntities(constants.NASTRAN, None, "ANSA_SIMULATION_RUN")
                print("I found simulation runs = [", simruns, "] in this database")
                autofix_list = ["filetype_discrepancy", "missing_subsystem_includes"]
                ret_val = dm.SaveSimulationRun(
                    simruns,
                    conflicts_option="SpinUp",
                    spin_up_attribute="Study Version",
                    file_content_loadcase="monolithic",
                    file_content_sim_model="monolithic",
                    use_loaded_loadcase=True,
                    use_loaded_sim_model=True,
                    autofix=autofix_list,
                )
                print("Script save is over and returned = ", ret_val)
                printSaveInDMResultObjects(ret_val)


    """


def SaveSimulationModel(
    ents: object,
    file_type: Any,
    conflicts_option: str,
    spin_up_attribute: str,
    file_content: str,
    export_png: bool,
    export_jt: bool,
    autofix: object,
    contents_based_spin_up_attribute: str,
    lbr_assign_values: object,
) -> object:
    """

    Saves the representation of a given list of simulation models in the DM.
    The files may be ANSA databases, simple XML files containing only hierarchy
    information or current deck output files. A DM Root has to be already specified.

    Parameters
    ----------
    ents : object
            A list that contains simulation models.

    file_type : Any, optional
            One of: "ANSA", "structure_only" or constants of Decks
            (e.g. ansa.constants.NASTRAN)
            In each case:
            -"structure_only": an ".xml" file will be saved in DM for each Simulation Model,
                               containing only its hierarchy.
            -"ANSA": ANSA database
            -ansa.constants.XXXX: a deck format to Output the SimModel.

            Attention!! Current deck outputting is currently fully supported.

    conflicts_option : str, optional
            Possible values: "Overwrite" / "Skip" / "SpinUp".
            Determines what will happen in case a Simulation Model that is intented
            to be saved, is already found inside DM.

    spin_up_attribute : str, optional
            Any of the attributes a Simulation Model has in the current DM root and for
            which spinning up could be achieved. Example: "Study Version".
            Note here that even though this is an optional argument in general,
            in case conflicts_option="SpinUp" then this argument becomes mandatory.

    file_content : str, optional
            Examine this argument in combination with the "file_type" argument.
            Assuming file_type="structure_only":
            - file_content argument is not compatible with file_type : "structure_only"

            Assuming file_type="ANSA":
            - file_content="monolithic" : The Simulation Model representation file will be
              an .ansa file containing all the ANSA entities of its subsystems, and also all
              the information regarding its hierarchy loaded in its Model Browser.
            - file_content="references": The Simulation Model representation file
              will be an .ansa file containing no ANSA entities, but only the information
              regarding its hierarchy loaded in its Model Browser.

            Assuming file_type=ansa.constants.xxx (e.g. ansa.constants.NASTRAN):
            - file_content="monolithic" : The Simulation Model representation file will be
              a file of the specified DeckCode format(e.g. a .nas file) containing all the
              ANSA entities of its subsystems, and also all the information regarding its
              hierarchy loaded in its Model Browser.
            -file_content="references" : The Simulation Model representation file
              will be a file of the specified DeckCode format (e.g. a .nas file) containing
              reference lines to the separate files of its Subsystems
            (e.g. #include "C/home/Subsystem1.nas",
                  #include "C:/home/Subsystem2.nas")

    export_png : bool, optional
            Possible values: True / False
            Determines whether a .png preview file will be created and stored in
            DM for each one of the saved Simulation Models.

    export_jt : bool, optional
            Possible values: True / False
            Determines whether a .jt light representation file will be created and
            stored in DM for each one of the saved Simulation Models.

    autofix : object, optional
            This argument is a List of strings. Possible values it can contain:
            "filetype_discrepancy"
            "missing_subsystem_includes".
            "generate_missing_solver_files"

            All its member string values will attempt to autofix in case the respective
            errors have been  encountered.

    contents_based_spin_up_attribute : str, optional
            If current DM schema supports contents based spinup of Simulation Model, specify any of the versioning scheme attributes of Simulation Model's parent DM object type.

    lbr_assign_values : object, optional
            This argument is a Python dictionary, which accepts key-value of properties or attributes that we wish to edit right before saving the Simulation Model in DM, like {'DM/Status':'Frozen'}. It is most commonly used in the cases of DM with Lifecycle Business Rules where there is a rule that defines that certain properties/attributes are only allowed to change when a representation file is also uploaded. For these cases we use this argument and edit them simultaneously with their file upload.

    Returns
    -------
    object
            Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Simulation Runs
            that we attempted to save in DM.
            Each "SaveInDMObject" ret contains 4 members:
            ret.entity    : ANSA entity we tried to save(the Simulation Model)
            ret.server_id : (string) The id by which it has been saved in DM
            ret.error     : (string) A description of the reason it failed to be saved.
            ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
                                     inner SimulationModels/Subsystems/Includes that were
                                     involved in Save and have caused save failure

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            def getSpacesAsManyAsLevelsDown(levels_down):
                spaces = ""
                for i in range(0, levels_down):
                    spaces += "   "
                return spaces


            def printSaveInDMResultObjectsForInnerChildrenErrors(inner_child_object, levels_down):
                spaces = getSpacesAsManyAsLevelsDown(levels_down)
                print(spaces, "server_id=", inner_child_object.server_id)
                print(spaces, "error=", inner_child_object.error)
                print(spaces, "entity=", inner_child_object.entity)
                print(spaces, "inners=", inner_child_object.inners)
                if inner_child_object.inners != None:
                    levels_down += 1
                    for inner_object in inner_child_object.inners:
                        printSaveInDMResultObjectsForInnerChildrenErrors(inner_object, levels_down)


            def printSaveInDMResultObjects(ret_objs):
                for object in ret_objs:
                    printSaveInDMResultObjectsForInnerChildrenErrors(object, 0)


            def main():
                simmodels = base.CollectEntities(constants.NASTRAN, None, "ANSA_SIMULATION_MODEL")
                autofix_list = ["filetype_discrepancy", "missing_subsystem_includes"]
                filecontent = "monolithic"  # or 'references'
                filetype = "ANSA"  # or constants.NASTRAN or 'structure_only'
                ret = dm.SaveSimulationModel(
                    ents=simmodels,
                    conflicts_option="SpinUp",
                    spin_up_attribute="Study Version",
                    file_type=filetype,
                    file_content=filecontent,
                    export_png=True,
                    export_jt=False,
                    autofix=autofix_list,
                )
                printSaveInDMResultObjects(ret)


    """


def CheckForUpdates(type: str, entities: object, data: object) -> object:
    """

    Search in DM for:
    1. updates of specified entities, or
    2. entities of defined ANSA type which satisfy specified filters.

    Parameters
    ----------
    type : str, optional
            The ANSA type of the entities which are searched
            in DM (2nd Use Case).

    entities : object, optional
            A list of DM objects (e.g. Parts, Subsystems, etc.)
            to check for updates in DM (1st Use Case).

    data : object
            Based on the Use Case, it can be:
            1. a dictionary to specify the Check DM Updates options, or
            2. a list to specify the filters which are applied to DM.

    Returns
    -------
    object
            Returns a dictionary with the following keys and values:
            key = 'error'
            value = 0(Success), 1(Nothing found), 2(No DM Root was set), 3(No access to DM Root),
                    4(Error in filters)
            key = 'output'
            value = A list with the results. The result can be:
                    sub-list, when updates are found for the specified entity, and
                    0, when no results are found for the specified entity

            Each one of the result entities in the sub-lists has a "DM Updates" attribute which
            describe the type of update (e.g. "Newer File", "Newer Version", etc.). These
            entities can be downloaded by using the DownloadEntities() script function.

    See Also
    --------
    DownloadEntities

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            # 1st Use Case: Check in DM for updates of specified entities
            def check_for_dm_updates():
                # Collect all the model parts
                all_parts = base.CollectEntities(0, None, "ANSAPART")
                print(len(all_parts), "parts were found in ANSA")

                # Collect the Master Instances of the parts
                master_instances = []
                for part in all_parts:
                    master_instance = base.GetMasterInstance(part)
                    if master_instance not in master_instances:
                        master_instances.append(master_instance)
                print(len(master_instances), "master instance parts were found in ANSA")

                # Get the DM updates of the Master Instances
                check_dm_updates_options = {
                    "newer_file": True,  # Newer file
                    "newer_version": [
                        True,  # Previous if no newer is found
                        True,  # Report commmon repr for newer version
                        True,
                    ],  # Report any repr for newer version
                    "newr_st_version": True,  # Newer Study Version (of Current Version)
                    "later_version": True,  # Later Version
                    "Revision": True,
                }  # An attribute of Versioning Scheme Counter type,
                # named 'Revision' and defined in dm_structure

                dm_updates = dm.CheckForUpdates(
                    entities=master_instances, data=check_dm_updates_options
                )

                # Print results
                for results in dm_updates["output"]:
                    if results == 0:  # No DM updates were found
                        continue
                    for item in results:
                        print("DM Item Id : ", item._id)
                        item_info = base.GetEntityCardValues(0, item, ["DM Updates"])
                        print("DM Update Status : ", item_info["DM Updates"])


            # 2nd Use Case: Search in DM for entities of defined ANSA type which satisfy specified filters
            def find_in_dm():
                ansa_type = "ANSAPART"
                dm_filters = [["Version", "equals", "A"], ["Representation", "contains", "crash"]]

                # Get the ANSA parts which satisfy the specified criteria
                results = dm.CheckForUpdates(type=ansa_type, data=dm_filters)

                # Print results
                if results["error"] == 0:
                    for item in results["output"][0]:
                        print("DM Item Id : ", item._id)
                        item_info = base.GetEntityCardValues(0, item, ["Version", "Representation"])
                        print("Version: ", item_info["Version"])
                        print("Representation: ", item_info["Representation"])


            # Execute a Use Case
            check_for_dm_updates()
            find_in_dm()


    """


def DoesRepresentationExist(entity: object, representation: str, deck: int) -> object:
    """

    This functions checks if the given representation exists in DM for one or more parts or includes.

    Parameters
    ----------
    entity : object
            May either be one ANSA Part or Include, or a list containing
            multiple Parts/Includes.

    representation : str
            A string describing a potential representation name.

    deck : int, optional
            The deck, in case that the entity is an Include.

    Returns
    -------
    object
            When the input to the function is one entity:
                    The function returns 1, if a representation file by the name of repr_name exists.
                    In case that PART is not a valid part or a file by the name repr_name does not exist, 0 is returned.
            When a list with entities is given as input:
                    The function returns a dictionary with the entity as the key and the return value as the value.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            # In case of Part
            def main():
                parts = [base.GetPartFromModuleId("607001"), base.GetPartFromModuleId("607002")]
                ret = dm.DoesRepresentationExist(parts[0], "FrontImpact")
                print(ret)


            # In case of Include
            def main():
                includes = base.CollectEntities(constants.NASTRAN, None, "INCLUDE")
                ret = dm.DoesRepresentationExist(includes[0], "FrontImpact", constants.NASTRAN)
                print(ret)


            # In case of multiple parts
            def main():
                parts = [base.GetPartFromModuleId("607001"), base.GetPartFromModuleId("607002")]
                ret = dm.DoesRepresentationExist(parts, "FrontImpact")
                print(ret)


    """


def DownloadEntities(
    part: object,
    property_conflicts: str,
    material_conflicts: str,
    set_conflicts: str,
    coord_conflicts: str,
    node_conflicts: int,
) -> int:
    """

    This function may only be used along with CheckForUpdates function.

    Parameters
    ----------
    part : object
            Contains DM Items which were output from
            the CheckForUpdates() function, in the same way they
            were given in the output array. Otherwise, they may be
            collected from the database and given as a list.

    property_conflicts : str, optional
            -"Offset" creates a new entity.
            -"KeepOld" keeps the old value.
            -"KeepNew" keeps the new value (Default).

    material_conflicts : str, optional
            -"Offset" creates a new entity.
            -"KeepOld" keeps the old value.
            -"KeepNew" keeps the new value (Default).

    set_conflicts : str, optional
            -"Offset" creates a new entity (Default).
            -"KeepOld" keeps the old value.
            -"KeepNew" keeps the new value.

    coord_conflicts : str, optional
            -"Offset" creates a new entity (Default).
            -"KeepOld" keeps the old value.
            -"KeepNew" keeps the new value.

    node_conflicts : int, optional
            -"Offset" creates a new entity (Default).
            -"KeepOld" keeps the old value.
            -"KeepNew" keeps the new value.

    Returns
    -------
    int
            Returns the total number of entities that were actually downloaded from DM.

    See Also
    --------
    CheckForUpdates

    Examples
    --------
    ::

            # A) If the user first wants to collect the updates from the DM:
            import ansa
            from ansa import base
            from ansa import dm


            def main():
                search = ("ANSAPART",)
                all_parts = base.CollectEntities(0, None, search)
                print(len(all_parts))

                check_dm_updates_data = {"newer_file": True}
                ret = dm.CheckForUpdates(entities=all_parts, data=check_dm_updates_data)
                print(len(ret["output"]))

                print(dm.DownloadEntities(ret["output"]))


            # B) If the user wants to collect the found updates from the database:
            def main():
                search = ("A_DM_ITEM",)
                all_items = base.CollectEntities(0, None, search, True)

                dm.DownloadEntities(all_items)


            # C) In the case of optional arguments:
            def main():
                search = ("A_DM_ITEM",)
                all_items = base.CollectEntities(0, None, search, True)

                dm.DownloadEntities(
                    all_items,
                    property_conflicts="KeepOld",
                    material_conflicts="KeepNew",
                    set_conflicts="Offset",
                )


    """


def FindMatches(parts: object, tolerance: float) -> object:
    """

    Given a parts list, this function searches the DM for matching parts, under the tolerance value.

    Parameters
    ----------
    parts : object
            A list that contains the ANSA parts for which a match will be searched in DM.

    tolerance : float
            The match tolerance value.

    Returns
    -------
    object
            Returns the list of matches that were found in DM. Otherwise it returns None.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                parts = base.GetPartFromModuleId("810")
                ret_val = dm.FindMatches(parts, 10.0)
                print(ret_val)
                dm.DownloadEntities(ret_val)


    """


def SaveUpdates(dm_items: object, dm_root: str) -> int:
    """

    This function may only be used along with CheckForUpdates function.
    It accepts the CheckForUpdates's function output.

    Parameters
    ----------
    dm_items : object
            A list that contains DM Items which were output from the CheckForUpdates()
            function, in the same way they were given in the output array.
            Otherwise, a single result may be given.

    dm_root : str, optional
            The target DM Root, where the update will be copied.
            When unspecified, the current DM is used.

    Returns
    -------
    int
            Returns the total number of DM items that were successfully uploaded to the target DM.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                dm_filters = [["Module Id", "equals", "RAIL_ROOF_SD_INR"]]
                output_array = dm.CheckForUpdates(None, data=dm_filters)
                print(output_array)
                if output_array["output"]:
                    dm.SaveUpdates(output_array["output"])


    """


def AddIncludeFile(
    filename: str,
    module_id: str,
    deck_name: str,
    st_version_conflict: str,
    entity_representation: str,
    entity_name: str,
    entity_version: str,
) -> int:
    """

    This function adds a new file in DM, under the includes directory, based on the arguments provided. The file
    specified by the string variable 'file_path' will be copied in DM, under a directory structure which will be created
    based on the string variables 'module_id', 'deck' and a number of optional ones, which can be set to define
    more accurately the save path. Varlen is the list of optional (argument name,value) pairs.

    Parameters
    ----------
    filename : str
            The include's filename.

    module_id : str
            The module id of the include file.

    deck_name : str
            A string specifying the deck, i.e. constants.

    st_version_conflict : str, optional
            Defines the action to be taken in case another entry with the
            characteristis defined above, has already been added in DM.
            In such a case you can decide either to create a new study version
            by setting the variable to 'NEW_ST_VERSION' or overwite the
            existing file in DM by setting the variable to 'OVERWRITE'.

    entity_representation : str, optional
            Defines the representation name to be used during the building of the
            DM directory structure where the new file will be added. If it is not set,
            the default representation 'common' will be used.

    entity_name : str, optional
            Defines the name to be assigned to new file to be created in DM. If this
            is not set, the name will be extracted from the string variable 'file_path'.
            The file_path's last section will be assigned as name. If this also fails,
            then the file will be assigned the default name 'Default_DM_Name'.

    entity_version : str, optional
            Defines the version name to be used during the building of the DM directory
            structure where the new file will be added. If it is not set, the default
            version 'A1' will be used.

    Returns
    -------
    int
            Returns 0 if the file has been successfully added in DM, or 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # 1st example
                dm.AddIncludeFile(
                    "/home/temp_dir/include_file.key",  # The file's path to be copied in DM
                    "10001",  # The file's corresponding module id
                    "LSDYNA",  # The file's corresponding deck
                    entity_representation="crash",  # The file's corresponding representation
                    entity_version="AB",  # The files corresponding version
                    st_version_conflict="OVERWRITE",
                )  # In case of study version conflicts, overwrite existing file in DM

                # 2nd example
                dm.AddIncludeFile(
                    "/home/temp_dir/include_file.key",  # The file's path to be copied in DM
                    "10001",  # The file's corresponding module id
                    "LSDYNA",  # The file's corresponding deck
                    entity_representation="crash",  # The file's corresponding representation
                    st_version_conflict="NEW_ST_VERSION",
                )  # In case of study version conflicts, create new study version in DM

                # 3rd example
                dm.AddIncludeFile(
                    "/home/temp_dir/include_file.key",  # The file's path to be copied in DM
                    "10001",  # The file's corresponding module id
                    "LSDYNA",
                )  # The file's corresponding deck


    """


def AddIncludes(includes: object, st_version_option: str) -> int:
    """

    This function adds new files in DM, under the includes directory, based on the DM field values of the
    specified include entities, provided in matrix includes. For each of the include entities, the file specified
    in the field 'FullPathName' will be copied in DM, under a directory structure which will be created based
    on the include's corresponding DM values. Varlen is the list of optional (argument name,value) pairs.

    Parameters
    ----------
    includes : object
            An entity or a list of include entities.

    st_version_option : str, optional
            Defines the action to be taken in case another entry with the
            attributes defined above, has already been added in DM.
            In such a case you can decide either to create a new study version
            by setting the variable to 'NEW_ST_VERSION',
            overwite the existing file in DM by setting the variable
            to 'OVERWRITE', or skip the specific include by setting the variable
            to "SKIP". The default value is 'NEW_ST_VERSION'.

    Returns
    -------
    int
            Returns 0 if the files have been successfully added in DM and 1 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm
            from ansa import constants


            def main():
                includes = base.CollectEntities(constants.NASTRAN, None, "INCLUDE")
                print(len(includes))
                print(dm.AddIncludes(includes))


    """


def GetCommonProperties() -> object:
    """

    The function will return common Properties among the "Simulation Models", "Simulation Runs" and "Loadcases" types.

    Returns
    -------
    object
            Returns a dictionary with the Property name and it's value.

    See Also
    --------
    SetCommonProperties

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("http://ektoras:7080/", username="admin", password="admin")
                common_properties = dm.GetCommonProperties()
                print(common_properties)
                # will print:  {'DM/Simulation_Model_Version': '001', 'DM/Project': 'A', 'DM/Variant': 'B', 'DM/Release': 'C'}


    """


def SetCommonProperties(names_values: object, apply_to_subsystems: bool) -> bool:
    """

    The function will set values for common Properties among the "Simulation Models",
    "Simulation Runs" and "Loadcases" types.

    Parameters
    ----------
    names_values : object
            A dictionary with the Property name and its value.

    apply_to_subsystems : bool, optional
            When True, the common Properties will be applied to all Subsystems
            existing in the current Model.

    Returns
    -------
    bool
            The function will return True if the values for common Properties were set successfully.
            Otherwise it will return False.

    See Also
    --------
    GetCommonProperties

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("http://ektoras:7080/", username="admin", password="admin")
                dm.SetCommonProperties({"Project": "X"})

                common_properties = dm.GetCommonProperties()
                print(common_properties)


    """


def GetEntityProperties(entity: object) -> object:
    """

    When connected to a DM, one may need to get an entity's DM Properties as a list.

    Parameters
    ----------
    entity : object
            The input entity whose properties will be returned.
            It may be one of the following:
            -ANSAPART
            -ANSA_SUBSYSTEM
            -ANSA_SIMULATION_MODEL
            -ANSA_CONFIGURATION
            -ANSA_SIMULATION_RUN
            -ANSA_LOADCASE
            -ANSA_LIBRARY_ITEM
            -INCLUDE

    Returns
    -------
    object
            Returns a list containing the DM Properties.
            Any properties that are ANSA Attributes, are returned with the "DM" prefix, e.g."DM/Discipline".

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                part = base.GetPartFromName("1_BIW_GROUP")
                print(dm.GetEntityProperties(part))
                subsystem = base.GetPartFromName("MODULE_1", type="ANSA_SUBSYSTEM")
                print(dm.GetEntityProperties(subsystem))


    """


def ReadComponentXml(filename: str) -> int:
    """

    Given an XML that was downloaded from DM, either for a Subsystem or a Simulation Model,
    this function will merge the hierarchy in to the current Model.

    Parameters
    ----------
    filename : str
            The xml filepath.

    Returns
    -------
    int
            Returns 1 on success.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.ReadComponentXml(
                    "C:/Users/user/AppData/Local/Temp/ansa_meta_dm_tmp_8436/WIN7_8436_7/hierarchy.xml"
                )


    """


def LoadEntities(entities: object, load: bool):
    """

    This functions loads/unloads Model Browser entities from DM.
    When in Load mode all specified entities will first be cleared of their contents and then be loaded (downloaded) from DM.
    When in Unload mode, entities will be cleared and left empty.

    Parameters
    ----------
    entities : object
            A list of Model Browser entities which can be loaded/unloaded.
            These can be Subsystems, Simulation Models, Simulation Runs,
            Library Items, or any combination of them.

    load : bool
            True: Load mode.
            False: Unload mode.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                subsystems = base.CollectEntities(0, None, "ANSA_SUBSYSTEM")
                dm.LoadEntities(subsystems, True)


    """


def AddSimulationRun(
    names_values: object, file_type: str, overwrite: bool, link: bool
) -> object:
    """

    Adds a Simulation Run to the DM. If the Simulation Run file contains a hierarchy
    of Includes, they will be added as well to the DM.

    Parameters
    ----------
    names_values : object
            All the attribute values of the Simulation Run.

    file_type : str, optional
            The file type of the Simulation Run file (eg. NASTRAN, LSDYNA, etc).

    overwrite : bool, optional
            When set to True, the Simulation Run will not replace an existing
            Simulation Run in the DM if it has the same primary values.
            (Default: False)

    link : bool, optional
            When set to True, files will not be copied to the DM, but hard linked.
            (Default: False)

    Returns
    -------
    object
            Returns the server id of the newly added Simulation Run, unless the addition
            fails or the overwrite flag is False and the Simulation Run already exists in
            the DM (then it returns None).

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                names_values = {}
                names_values["Name"] = []
                names_values["Simulation_Model"] = "2"
                names_values["LoadCase"] = "3"
                names_values["Main_File"] = "..."
                server_id = dm.AddSimulationRun(names_values, file_type="LSDYNA", link=True)


    """


def GetSaveRepresentationConflictOptions(
    entity: object, save_group_or_part: str
) -> object:
    """

    When trying to upload an entity to DM, one can get the conflict options when the
    entity already exists in DM.

    Parameters
    ----------
    entity : object
            The input entity.

    save_group_or_part : str, optional
            Determines if a Group or Part will be checked in DM.
            Valid values: "GROUP" or "PART".
            (Default: "PART")

    Returns
    -------
    object
            Returns a list with the available conflict options, only if the entity already
            exists in DM. Otherwise, it returns None.

    See Also
    --------
    SaveRepresentation

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                part = base.GetPartFromName("00006666")
                print(dm.GetSaveRepresentationConflictOptions(part))


    """


def UpdateEntityAttributesFromDM(entities: object) -> bool:
    """

    The function will update the values for all existing secondary Attributes
    of the input Model Browser Entities with the respective values for anything
    that is found in DM.

    Parameters
    ----------
    entities : object
            A list containing the Model Browser Containers, or a single entity.
            Accepted entities are Parts, Subsystems, Simulation_Models, etc.

    Returns
    -------
    bool
            Returns True if at least one entity's Attribute values were updated.

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa


            def main():
                all_subsystems = ansa.base.CollectEntities(
                    0, containers=None, search_types="ANSA_SUBSYSTEM"
                )

                if len(all_subsystems):
                    ansa.dm.UpdateEntityAttributesFromDM(all_subsystems)
                ent = ansa.base.GetFirstEntity(0, "ANSA_SUBSYSTEM")
                ansa.dm.UpdateEntityAttributesFromDM(ent)

                all_subsystems = ansa.base.CollectEntities(0, containers=None, search_types="SHELL")
                ansa.dm.UpdateEntityAttributesFromDM(all_subsystems)


            if __name__ == "__main__":
                main()


    """


def LoadInterfaceRepresentation(subsystems: object, detailed_results: bool) -> object:
    """

    Loads the Interface Representation of Subsystems and Library Items.

    Parameters
    ----------
    subsystems : object
            A list of containers whose Interface
            Representation is going to be loaded.

    detailed_results : bool, optional
            Return the error for each container whose Interface
            Representation failed to be loaded.
            (Default: False)

    Returns
    -------
    object
            A list of containers whose Interface Representation failed to be loaded.
            If 'detailed_results' argument is set to True, a dictionary where:
                    key: is the container which failed to be loaded
                    value: a string comment ('invalid entity'/'missing DM file'/'internal load error')

    Examples
    --------
    ::

            import ansa
            from ansa import base, dm


            def main():
                subsystems_list = base.CollectEntities(0, None, "ANSA_SUBSYSTEM")
                failed = dm.LoadInterfaceRepresentation(subsystem_list)


    """


def SaveLoadcase(
    ents: object,
    file_type: Any,
    conflicts_option: str,
    spin_up_attribute: str,
    file_content: str,
    autofix: object,
    lbr_assign_values: object,
) -> object:
    """

    Saves the representation of a given list of loadcases in the DM.
    The files may be ANSA databases, simple XML files containing only hierarchy
    information or current deck output files. A DM Root has to be already specified.

    Parameters
    ----------
    ents : object
            A list that contains Loadcases.

    file_type : Any, optional
            One of: "ANSA", "structure_only" or constants of Decks
            (e.g. ansa.constants.NASTRAN)
            In each case:
            -"structure_only": an ".xml" file will be saved in DM for each Loadcase,
                               containing only its hierarchy.
            -"ANSA": ANSA database
            -ansa.constants.XXXX: a deck format to Output the Loadcase.

    conflicts_option : str, optional
            Possible values: "Overwrite" / "Skip" / "SpinUp".
            Determines what will happen in case a Loadcase that is intented
            to be saved, is already found inside DM.

    spin_up_attribute : str, optional
            Any of the attributes a Loadcase has in the current DM root and for
            which spinning up could be achieved. Example: "Study Version".
            Note here that even though this is an optional argument in general,
            in case conflicts_option is "SpinUp" then this argument becomes mandatory.

    file_content : str, optional
            Examine this argument in combination with the "file_type" argument.
            Assuming file_type="structure_only":
            - file_content argument is not compatible with file_type : "structure_only"

            Assuming file_type="ANSA":
            - file_content="monolithic" : The Loadcase representation file will be
              an .ansa file containing all the ANSA entities of its subsystems and library
              items,and also all the information regarding its hierarchy loaded in its
              Model Browser.
            - file_content="references": The Loadcase representation file
              will be an .ansa file containing no ANSA entities, but only the information
              regarding its hierarchy loaded in its Model Browser.

            Assuming file_type=ansa.constants.xxx (e.g. ansa.constants.NASTRAN):
            - file_content="monolithic" : The Loadcase representation file will be
              a file of the specified DeckCode format(e.g. a .nas file) containing all the
              ANSA entities of its subsystems and library items, and also all the
              information regarding its hierarchy loaded in its Model Browser.
            -file_content="references" : The Loadcase representation file
              will be a file of the specified DeckCode format (e.g. a .nas file) containing
              reference lines to the separate files of its Subsystems and Library Items.
            (e.g. #include "C/home/Subsystem1.nas",
                  #include "C:/home/Subsystem2.nas")

    autofix : object, optional
            This argument is a List of strings. Possible values it can contain:
            "filetype_discrepancy"
            "missing_subsystem_includes".
            "generate_missing_solver_files"

            All its member string values will attempt to autofix in case the respective
            errors have been  encountered.

    lbr_assign_values : object, optional
            This argument is a Python dictionary, which accepts key-value of properties or attributes that we wish to edit right before saving the Simulation Model in DM, like {'DM/Status':'Frozen'}. It is most commonly used in the cases of DM with Lifecycle Business Rules where there is a rule that defines that certain properties/attributes are only allowed to change when a representation file is also uploaded. For these cases we use this argument and edit them simultaneously with their file upload.

    Returns
    -------
    object
            Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Loadcases
            that we attempted to save in DM.
            Each "SaveInDMObject" ret contains 4 members:
            ret.entity    : ANSA entity we tried to save(the Loadcase)
            ret.server_id : (string) The id by which it has been saved in DM
            ret.error     : (string) A description of the reason it failed to be saved.
            ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
                                     inner LibItems/Subsystems/Includes that were
                                     involved in Save and have caused save failure

    Examples
    --------
    ::

            import ansa
            from ansa import base, dm


            def main():
                sub1 = base.NewSubsystem(module_id="sub1")
                sub2 = base.NewSubsystem(module_id="sub2")

                loadcase1 = base.CreateEntity(0, "ANSA_LOADCASE")
                loadcase2 = base.CreateEntity(0, "ANSA_LOADCASE")

                base.AddToModelContainer(loadcase1, sub1)
                base.AddToModelContainer(loadcase2, sub2)

                subsystems = [sub1, sub2]
                loadcase_list = [loadcase1, loadcase2]

                file_type = "ANSA"
                conflicts_option = "Overwrite"
                content = "references"

                dm.SaveSubsystems(subsystems, conflicts_option, file_type=file_type)
                dm.SaveLoadcase(loadcase_list, file_type, conflicts_option, file_content=content)


            if __name__ == "__main__":
                main()


    """


def BuildModelBrowserEntities(entities: object) -> int:
    """

    This function runs the "Build" functionality on all input Model Browser Containers.

    Parameters
    ----------
    entities : object
            An array of Model Browser Containers

    Returns
    -------
    int
            the number of entities that were successfully built.

    Examples
    --------
    ::

            import ansa


            def main():
                subsystem = ansa.base.GetPartFromModuleId("Left_Middle", type="ANSA_SUBSYSTEM")
                print(ansa.dm.BuildModelBrowserEntities([subsystem]))


    """


def DownloadDMObjects(server_ids: object, type: str, hierarchy_only: bool) -> object:
    """

    Download objects from DM by providing their server ids. Optionally, the type of DM
    objects can be provided to ensure that only objects of the specified type will be
    downloaded. For Subsystems, it is possible to download only the parts hierarchy.

    Parameters
    ----------
    server_ids : object
            the server id(s) of the DM object(s) to be downloaded.
            The value be a string (for single object) or a list
            of strings (for multiple objects).

    type : str, optional
            the type of DM objects to be downloaded. When it is
            specified, only objects of this type will be downloaded.
            The specified type can be ANSA type (e.g. ANSA_LOADCASE)
            or the DM type defined through the Data Model (e.g. Loadcase).

    hierarchy_only : bool, optional
            specify whether the representation (False) or just the parts
            hierarchy (True) will be downloaded. Default value is False.
            When the value is set True, the type should also be defined
            as it is supported only for Subsystems.

    Returns
    -------
    object
            Return a list of booleans with size equal to the size of the server ids list. The
            values can be True on success or False on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            dm_objects = ["10", "20", "30"]
            ret = dm.DownloadDMObjects(server_ids=dm_objects)
            num_of_objects = len(dm_objects)
            for i in range(num_of_objects):
                if ret[i]:
                    print(
                        "The DM Object with server id "
                        + dm_objects[i]
                        + " was downloaded successfully"
                    )
                else:
                    print(
                        "The DM Object with server id " + dm_objects[i] + " failed to be downloaded"
                    )


    """


def UploadInterfaceRepresentation(
    mbcontainers: object, force_upload: bool, detailed_results: bool
) -> object:
    """

    Uploads the Interface Representation of valid Model Browser Containers to the
    connected DM.

    Parameters
    ----------
    mbcontainers : object
            A list of Model Browser Containers that their
            Interface Representation will be uploaded to
            the currently connected DM.

    force_upload : bool, optional
            If set to False, Containers which already
            have an uploaded Interface Representation file
            in DM will be skipped.
            If set to True (default), Interface Representation file
            of these containers will be overwritten.

    detailed_results : bool, optional
            Return the error for each container whose Interface
            Representation failed to be uploaded in DM
            (Default: False)

    Returns
    -------
    object
            A list of Model Browser Containers whose Interface Representation failed to be uploaded in DM.
            If 'detailed_results' argument is set to True, a dictionary where:
                    key: is the failed container
                    value: a string comment

    See Also
    --------
    dm.LoadInterfaceRepresentation

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import base, dm


            def main():
                # Assuming that a database which contains subsystems is loaded and a DM connection is established

                subsystems = base.CollectEntities(0, None, "ANSA_SUBSYSTEM")
                failed = dm.UploadInterfaceRepresentation(subsystems)
                print(failed)


            if __name__ == "__main__":
                main()


    """


def SaveLibraryItems(
    ents: object,
    conflicts_option: str,
    spin_up_attribute: str,
    autofix: object,
    lbr_assign_values: object,
) -> object:
    """

    Saves the representation of a given list of library items in the DM.
    A DM Root has to be already specified.

    Parameters
    ----------
    ents : object
            A list that contains Library Items.

    conflicts_option : str, optional
            Possible values: "Overwrite" / "Skip" / "SpinUp".
            Determines what will happen in case a Library Item that is intented
            to be saved, is already found inside DM.

    spin_up_attribute : str, optional
            Any of the attributes a Library Item has in the current DM root and for
            which spinning up could be achieved. Example: "Study Version".
            Note here that even though this is an optional argument in general,
            in case conflicts_option is "SpinUp" then this argument becomes mandatory.

    autofix : object, optional
            This argument is a List of strings. Possible values it can contain:
            "unapplied_numbering_rules"

            All its member string values will attempt to autofix in case the respective
            errors have been  encountered.

    lbr_assign_values : object, optional
            This argument is a Python dictionary, which accepts key-value of properties or attributes that we wish to edit right before saving the Simulation Model in DM, like {'DM/Status':'Frozen'}. It is most commonly used in the cases of DM with Lifecycle Business Rules where there is a rule that defines that certain properties/attributes are only allowed to change when a representation file is also uploaded. For these cases we use this argument and edit them simultaneously with their file upload.

    Returns
    -------
    object
            Returns a List containing one "SaveInDMObject" named tuple corresponding to each of the Library Items
            that we attempted to save in DM.
            Each "SaveInDMObject" ret contains 4 members:
            ret.entity    : ANSA entity we tried to save(the Library Item)
            ret.server_id : (string) The id by which it has been saved in DM
            ret.error     : (string) A description of the reason it failed to be saved.
            ret.inners    : (list)   A list of "SaveInDmObject" named tuples corresponding to the
                                     inner LibItems/Includes that were
                                     involved in Save and have caused save failure

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa
            from ansa import base
            from ansa import constants
            from ansa import dm


            def getSpacesAsManyAsLevelsDown(levels_down):
                spaces = ""
                for i in range(0, levels_down):
                    spaces += "   "
                return spaces


            def printSaveInDMResultObjectsForInnerChildrenErrors(inner_child_object, levels_down):
                spaces = getSpacesAsManyAsLevelsDown(levels_down)
                print(spaces, "server_id=", inner_child_object.server_id)
                print(spaces, "error=", inner_child_object.error)
                print(spaces, "entity=", inner_child_object.entity)
                print(spaces, "inners=", inner_child_object.inners)
                if inner_child_object.inners != None:
                    levels_down += 1
                    for inner_object in inner_child_object.inners:
                        printSaveInDMResultObjectsForInnerChildrenErrors(inner_object, levels_down)


            def printSaveInDMResultObjects(ret_objs):
                for object in ret_objs:
                    printSaveInDMResultObjectsForInnerChildrenErrors(object, 0)


            def main():
                rlis = base.CollectEntities(constants.NASTRAN, None, "ANSA_LIBRARY_ITEM")
                autofix_list = ["unapplied_numbering_rules"]
                ret = dm.SaveLibraryItems(
                    ents=rlis, conflicts_option="Overwrite", autofix=autofix_list
                )
                printSaveInDMResultObjects(ret)


            if __name__ == "__main__":
                main()


    """


def NextIteration(server_ids: object) -> object:
    """

    Create a Next Iteration of DM objects providing their server ids.
    The result is an empty hierarchy of the specified DM objects.

    Parameters
    ----------
    server_ids : object
            the server id(s) of the DM object(s) to create a Next Iteration.
            The value can be a string (for single object) or a list
            of strings (for multiple objects).

    Returns
    -------
    object
            Returns a dictionary containing pairs of:
            <Requested Server Id - Result of Next Iteration>
            Result of Next Iteration can be "Success" or "Invalid for Next Iteration"

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            # assuming that DM Objects with server ids 20 & 30 exist in DM
            dm_objects = ["20", "30"]
            results = dm.NextIteration(server_ids=dm_objects)

            for server_id in results:
                if results[server_id] != "Success":
                    print(
                        "The DM Object with server id "
                        + server_id
                        + " is not valid to create a Next Iteration from."
                    )


    """


def ShowPlotInViewer(plot: object, window_name: str, page_name: str):
    """

    This function starts META viewer for running application (if not already started),
    and shows there the created plot given as input.

    Parameters
    ----------
    plot : object
            This argument is the created plot we want to show in viewer.

    window_name : str, optional
            This argument is the window name in viewer.

    page_name : str, optional
            This argument is the name of the page added in viewer.

    See Also
    --------
    CreatePlot, SetPlotProperties, DeletePlot

    Examples
    --------
    ::

            # ANSA
            import ansa
            from ansa import dm, utils

            plot = utils.CreatePlot()
            utils.SetPlotProperties(plot, title="My plot", legend_position="TopRight")
            dm.ShowPlotInViewer(plot, window_name="Plot", page_name="Plot's page")
            utils.DeletePlot(plot)


    """


def RefreshEntriesInCurrentTab(server_ids: object, entities: object, type: str) -> bool:
    """

    This function refreshes entries as given with server ids or entities and entity type in current tab.
    Function will fail for cases like:

    - no entity type is given
    - no server ids and no entitites are given
    - couldn't collect server ids for input arguments
    - entity type does not match the type of the tab. Excluded cases: Subsystem in Simulation Model tab, Parts in any tab

    If entities list is NULL, server ids list will be used to refresh tab.

    Parameters
    ----------
    server_ids : object, optional
            This argument is a list of server ids for the entries we want to refresh in tab.

    entities : object, optional
            This argument is a list of entities we want to refresh (e.g., subsystems).

    type : str, optional
            This argument is the entity type of the entries we want to refresh.

    Returns
    -------
    bool
            Returns True for success,
                    False otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            server_ids_list = ["97"]
            ret = dm.RefreshEntriesInCurrentTab(server_ids=server_ids_list, type="Subsystems")
            print(ret)


    """


def GetChildIdsWithRelativePositions(object_id: str):
    """

    This function, given a row id, returns a dictionary with this item's children ids and the respective
    transformation matrices.

    Parameters
    ----------
    object_id : str
            This argument is the row id of the item we will get further information from
            (children row ids and transformation matrices).

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            object_id = "7"
            rel_pos = dm.GetChildIdsWithRelativePositions(object_id=object_id)
            print(rel_pos)


    """


def SendDMObjectsToOtherDM(server_ids: object, path: str) -> object:
    """
    .. deprecated:: 22.0.0
            Use :py:func:`SendDMObjectsToDM` instead.


    Send a list of DM Objects' server ids to a specified local path.

    Parameters
    ----------
    server_ids : object
            a list of strings for the given server ids of the DM Objects.

    path : str
            the absolute path of the local DM root.

    Returns
    -------
    object
            Returns a Dictionary of type {server_id : (error_code, new_server_id, error_message)}, where:
            - server_id (String) is the server id of the checked-out item,
            - result_code (Int) can be 0 for success, 1 for failure, 2 for skip, 3 for spin-up, and 4 for next iteration,
            - new_server_id (String) is the new Server Id of the item,
            - error_message (String) is the message/reason of failure or skip.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm_path = "/absolute/path/of/loacl/dm/"
                server_ids_to_send = ["100", "200", "300"]
                dm.SendDMObjectsToOtherDM(server_ids_to_send, dm_path)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 22.0.0. Use :py:func: SendDMObjectsToDM instead.",
        DeprecationWarning,
    )


def OpenDMBrowserToSelect(type: str, query: object, server_ids: object) -> object:
    """

    OpenDMBrowserToSelect function opens DM Browser on current DM root and allows user to select DM objects.
    User can select one or multiple items and press the 'Download' button in order to get the selected DM objects
    or press ESC to close DM Browser without selecting anything.

    Parameters
    ----------
    type : str
            Give object type to open DM Browse on the respective tab

    query : object, optional
            Give query to be applied to DM Browser before launch (as used in dm.QueryDMObjects):
            * A list of [<attribute_name>, <condition>, <value>] lists which specify the query.
            * A BetaQL string

    server_ids : object, optional
            Give specific server ids to be filtered in tab (applied if 'query' is not given)

    Returns
    -------
    object
            A list with the selected DM Objects

    See Also
    --------
    dm.QueryDMObjects

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def printResults(results):
                if results != None:
                    for dm_object in results:
                        if dm_object:
                            print("DM Object Id : ", dm_object.server_id)


            def select_dm_objects():
                # Test case 1
                print("\\nTest case 1")
                dm_filters = [
                    ["Project", "contains", "venza"],
                    ["Representation", "equals", "crash_fe"],
                    ["Variant", "equals", "lhd"],
                ]
                ret = dm.OpenDMBrowserToSelect(type="Subsystems", query=dm_filters)
                printResults(ret)

                # Test case 2
                print("\\nTest case 2")
                beta_ql_query = (
                    "Project contains venza and Representation = crash_fe and Variant = lhd"
                )
                ret = dm.OpenDMBrowserToSelect(type="Subsystems", query=beta_ql_query)
                printResults(ret)

                # Test case 3
                print("\\nTest case 3")
                given_server_ids = ["5", "6", "7", "8"]
                ret = dm.OpenDMBrowserToSelect(type="Subsystems", server_ids=given_server_ids)
                printResults(ret)

                # Test case 4
                print("\\nTest case 4")
                object_type = "Simulation_Run"
                ret = dm.OpenDMBrowserToSelect(type=object_type)
                printResults(ret)


            def select_dm_objects_and_download():
                # Test case 5
                print("\\nTest case 5")
                res = dm.OpenDMBrowserToSelect(type="ANSA_SUBSYSTEM")
                server_ids = [dmo.server_id for dmo in res]
                dm.DownloadDMObjects(server_ids)


            select_dm_objects()
            select_dm_objects_and_download()


    """


def SendDMObjectsToDM(server_ids: object, path: str) -> object:
    """

    Send a list of DM Objects' server ids to a specified local path or to their source DM Path.

    Parameters
    ----------
    server_ids : object
            a list of strings for the given server ids of the DM Objects.

    path : str, optional
            the absolute path of the local DM root. When it is not specified, the DM Objects are sent to their source DM Path (they should be descendants of already transferred DM Objects).

    Returns
    -------
    object
            Returns a Dictionary of type {server_id : SendToDMResult}, where:
            - server_id (String) is the server id of the checked-out item,
            - SendToDMResult (Object) with members:
              - result (Int) can be 0 for success, 1 for failure, 2 for skip, 3 for spin-up, and 4 for next iteration,
              - new_server_id (String) is the new Server Id of the item,
              - output_path (String) is the DM Path where the DM Objects were sent,
              - result_message (String) is the message based on the result.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm_path = "/absolute/path/of/loacl/dm/"
                server_ids_to_send = ["100", "200", "300"]
                dm.SendDMObjectsToOtherDM(server_ids_to_send, dm_path)


    """


def AddAttachmentToFolder(
    entity: object,
    server_id: str,
    folder_name: str,
    filename: str,
    attribute_name: str,
    entity_type: str,
    link: bool,
) -> int:
    """

    This function can be used to:

    - add a file under a folder in the Library Items,
    - attach a file/folder under a DM Object's attribute of type Attached File/Directory
      respectively. If this attribute does not exist, it is created as Additional Attribute.
    A DM root should have been specified.

    Parameters
    ----------
    entity : object, optional
            the ANSA entity to be found in the connected
            DM root. The file/folder will be attached under
            an attribute of this object (if found in DM).

    server_id : str, optional
            the server id of the object contained to the
            connected DM root. The file/folder will be
            attached under an attribute of this object.

    folder_name : str, optional
            the name of the folder in the Library Items,
            where the specified file will be attached.
            For DM Objects in file-based DM, a sub-folder
            with this name will be created, and the file
            will be placed there.

    filename : str
            the full path of the file/folder to be attached.

    attribute_name : str, optional
            the name of the DM Object's attribute where the
            specified file/folder will be attached.

    entity_type : str, optional
            the type of the DM object.

    link : bool, optional
            enables the ability to link a folder and not copy
            its contents under a DM Object's attribute. By
            default, the contents are copied (False).

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    DeleteAttachment, DownloadAttachment

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                # 1st Use Case: Create a folder under the Library Items and attach a file to that
                create_folder = dm.CreateNewSubFolder(folder_name="batch_mesh_sessions")
                file_path = "/full/path/of/file/or/folder/to/attach/"
                attach_file = dm.AddAttachmentToFolder(
                    folder_name="batch_mesh_sessions", filename=file_path
                )

                # Alternatively, attach a file under a sub-folder
                attach_file = dm.AddAttachmentToFolder(
                    folder_name="batch_mesh_sessions/crash", filename=file_path
                )
                attach_file = dm.AddAttachmentToFolder(
                    folder_name="LIBRARY_ITEMS/batch_mesh_sessions", filename=file_path
                )

                # 2nd Use Case: File-based DM - Create a sub-folder under an attribute of DM Object
                # and place the file there.
                file_path = "/full/path/of/file/or/folder/to/attach/"
                part = base.GetPartFromModuleId("100")
                create_subfolder = base.CreateNewSubFolder(
                    entity=part, folder_name="Additional_Results", attribute_name="Results"
                )
                attach_file = dm.AddAttachmentToFolder(
                    entity=part,
                    folder_name="Additional_Results",
                    filename=file_path,
                    attribute_name="Results",
                )

                # Alternatively, the file could be placed directly under the DM Object's attribute
                attach_file = dm.AddAttachmentToFolder(
                    entity=part, filename=file_path, attribute_name="Results"
                )
                attach_file = dm.AddAttachmentToFolder(
                    server_id="200", filename=file_path, attribute_name="Results"
                )

                # 3rd Use Case: SPDRM - Attach a file/folder under an attribute of type Attached
                # File/Directory respectively. If this attribute does not exist (was not specified
                # in the dm_structure.xml), it is created as Additional Attribute.
                folder_path = "/full/path/of/file/or/folder/to/attach/"
                attach_file = dm.AddAttachmentToFolder(
                    server_id="200", filename=folder_path, attribute_name="Results"
                )


            if __name__ == "__main__":
                main()


    """


def DeleteAttachment(
    entity: object, server_id: str, folder_name: str, filename: str, entity_type: str
) -> int:
    """

    When connected to a DM, this function allows for an existing attachment to a DM object to be deleted.
    If no DM Object is specified, a library item can be deleted.

    Parameters
    ----------
    entity : object, optional
            When this argument is given, the ANSA entity will be searched in DM and if found,
            the attachment will be deleted from the corresponding DM Object.

    server_id : str, optional
            The DM Object's server id, whose attachment will be deleted.

    folder_name : str, optional
            A subfolder with this name will be deleted.

    filename : str, optional
            The filename which will be deleted.

    entity_type : str, optional
            If the server_id is given as an argument, one may define the Object's type by
            using this argument.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    AddAttachmentToFolder, DownloadAttachment

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def deleteAnAttachedFolder():
                part = base.GetPartFromModuleId("4282")
                dm.DeleteAttachment(entity=part, folder_name="VBT_Info")
                dm.DeleteAttachment(entity=part, folder_name="DA/Translated_files")
                dm.DeleteAttachment(entity=part)

                # in case we know the Object's server id:
                file_ret = dm.DeleteAttachment(server_id="100", folder_name="Folder1")
                # or:
                file_ret = dm.DeleteAttachment(
                    server_id="100", entity_type="parts", folder_name="Folder1"
                )

                # In order to delete a file under "batch_mesh_sessions" folder:
                dm.DeleteAttachment(
                    folder_name="batch_mesh_sessions", filename="example_7mm.ansa_qual"
                )


    """


def DownloadAttachment(
    entity: object,
    server_id: str,
    folder_name: str,
    output_folder: str,
    subfolder_name: str,
    filename: str,
    entity_type: str,
    attribute_name: str,
    action: str,
) -> int:
    """

    Downloads the attachments of an object contained to the defined DM root. A DM root
    should have been specified.

    Parameters
    ----------
    entity : object, optional
            the ANSA entity to be found in the connected
            DM root. The attachments of this object (if
            found in DM) will be downloaded.

    server_id : str, optional
            the server id of the object contained to the
            connected DM root. The attachments of this
            object will be downloaded.

    folder_name : str, optional
            the name of the folder which contains the
            attachments.

    output_folder : str
            the full path of the folder where the attachments
            will be downloaded.

    subfolder_name : str, optional
            the name of the subfolder to be downloaded.

    filename : str, optional
            the name of the file to be downloaded.

    entity_type : str, optional
            the type of the DM object.

    attribute_name : str, optional
            the name of attribute which contains the
            attachments.

    action : str, optional
            The exported file from the server will be copied to the target directory by default.
            It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory.
            Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items and Library Files.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    DeleteAttachment, AddAttachmentToFolder, DMObject.download_attachment

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                part = base.GetPartFromModuleId("100")
                dm.DownloadAttachment(
                    entity=part,
                    output_folder="/full/path/of/output/folder/",
                    attribute_name="Image_JT",
                )

                dm.DownloadAttachment(
                    server_id="200",
                    output_folder="/full/path/of/output/folder/",
                    attribute_name="Image_PNG",
                )

                # Download attachements from SPDRM-based DM
                dm.DownloadAttachment(
                    server_id="300",
                    subfolder_name="/relative/path/to/the/top/level/folder/",
                    output_folder="/full/path/of/output/folder/",
                    attribute_name="Results",
                )
                dm.DownloadAttachment(
                    server_id="400",
                    filename="/relative/path/to/the/top/level/folder/filename.ext",
                    output_folder="/full/path/of/output/folder/",
                    attribute_name="Results",
                )


            if __name__ == "__main__":
                main()


    """


def CreateAttachedFolder(
    entity: object, server_id: str, attribute_name: str, entity_type: str
) -> int:
    """

    Creates an empty attached folder under an existing object in DM. New files/folders
    can be added as attachments in that folder afterwards. A DM root should have been
    specified.

    Parameters
    ----------
    entity : object, optional
            the ANSA entity to be found in the connected
            DM root. The new folder will be attached under
            this object (if found in DM).

    server_id : str, optional
            the server id of the object contained to the
            connected DM root. The new folder will be
            attached under this object.

    attribute_name : str, optional
            the name of the folder to be attached.

    entity_type : str, optional
            the type of the DM object.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    CreateNewSubFolder, DeleteAttachment, DownloadAttachment, AddAttachmentToFolder

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                part = base.GetPartFromModuleId("100")
                dm.CreateAttachedFolder(entity=part, attribute_name="Info")

                dm.CreateAttachedFolder(server_id="200", attribute_name="Info")


            if __name__ == "__main__":
                main()


    """


def CreateNewSubFolder(
    entity: object,
    server_id: str,
    folder_name: str,
    attribute_name: str,
    entity_type: str,
) -> int:
    """

    Creates an empty subfolder in an existing attached folder of a DM object. New
    files/folders can be added as attachments in that subfolder afterwards. A DM root
    should have been specified. This function can also be used to create subfolders
    for library items in DM (e.g."batch_mesh_sessions").

    Parameters
    ----------
    entity : object, optional
            the ANSA entity to be found in the connected
            DM root. The new subfolder will be attached
            under this object (if found in DM).

    server_id : str, optional
            the server id of the object contained to the
            connected DM root. The new subfolder will
            be attached under this object.

    folder_name : str
            the name of the subfolder to be attached.

    attribute_name : str, optional
            the name of the parent attribute/folder where
            the new subfolder will be created. The default
            value id 'DA'.

    entity_type : str, optional
            the type of the DM object.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    CreateAttachedFolder, DeleteAttachment, DownloadAttachment, AddAttachmentToFolder

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                part = base.GetPartFromModuleId("100")
                dm.CreateNewSubFolder(
                    entity=part, folder_name="New_Subfolder", attribute_name="VIP"
                )

                dm.CreateNewSubFolder(
                    server_id="200", folder_name="New_Subfolder", attribute_name="VIP"
                )

                dm.CreateNewSubFolder(folder_name="batch_mesh_sessions")


            if __name__ == "__main__":
                main()


    """


def DownloadLibraryItem(
    library: str, output_folder: str, filename: str, action: str
) -> int:
    """

    This function is used to download a file from the DM library items, e.g. a "batch_mesh_session".

    Parameters
    ----------
    library : str
            The library item's type.

    output_folder : str, optional
            The folder where the item will be copied.
            Although it's an optional argument, it needs to be defined.

    filename : str, optional
            The library item's name.
            Although it's an optional argument, it needs to be defined.

    action : str, optional
            The exported file from the server will be copied to the target directory by default.
            It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory.
            Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    See Also
    --------
    GetAvailableLibraryItems

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                results = dm.GetAvailableLibraryItems("batch_mesh_sessions", search_for="*.ansa")
                for result in results:
                    dm.DownloadLibraryItem(
                        "batch_mesh_sessions",
                        output_folder="C:\\\\Users\\\\demo\\\\Desktop\\\\ttt\\\\",
                        filename=result,
                    )


    """


def QueryForAllResults(type: str):
    """

    Gets a list with all the items in DM for a specific type.

    Parameters
    ----------
    type : str
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_SUBSYSTEM) or the DM type defined through the Data
            Model (e.g. Subsystems). The supported DM Objects are Parts,
            Subsystems, and Configurations ('configurations').

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                all_dm = dm.QueryForAllResults("parts")
                if all_dm:
                    for item in all_dm:
                        for key in item:
                            print("attribute::", key, "value::", item[key])


    """


def CreateRootFolder(folder_name: str, dm_structure_xml: str) -> int:
    """

    This function creates a new folder which can be then used as a DM Root.
    If a dm_structure.xml file is defined, it will be copied into that new folder.

    Parameters
    ----------
    folder_name : str
            The desired folder that will be used as a DM Root.

    dm_structure_xml : str, optional
            The source dm_structure.xml that will be copied to the new DM folder.

    Returns
    -------
    int
            Returns 1 on success.
            Returns  0 on failure:
            - If the new folder exists but has no write access.
            - If the new folder can't be created.
            - If the dm_structure.xml can't be copied to the new folder.

    See Also
    --------
    SetRoot, RemoveRoot, GetRoot, GetRootsList

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def createANewDM():
                if dm.CreateRootFolder("C:\\tmp\\DM1") == 1:
                    base.SetRoot("C:\\tmp\\DM1")
                if (
                    dm.CreateRootFolder("C:\\tmp\\DM2", dm_structure_xml="C:\\tmp\\dm_structure.xml")
                    == 1
                ):
                    base.SetRoot("C:\\tmp\\DM2")


    """


def GetAvailableLibraryItems(folder_name: str, search_for: str) -> object:
    """

    This function can be used to get a list with all the items in a library in DM,
    e.g. all "batch_mesh_sessions" or specific "batch_mesh_sessions" that match a
    search pattern.

    Parameters
    ----------
    folder_name : str
            The library's name.

    search_for : str, optional
            This can be a search pattern that will be used for the query.

    Returns
    -------
    object
            Returns a list with all the library item names.

    See Also
    --------
    dm.DownloadLibraryItem

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                results = dm.GetAvailableLibraryItems("batch_mesh_sessions", search_for="*.ansa")
                if results:
                    for result in results:
                        print("Found batch_mesh_session: ", result)
                all_results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
                if all_results:
                    for result in all_results:
                        print("Found batch_mesh_session: ", result)


    """


def IsConnectionValid(dm_root: str, reconnect: bool) -> int:
    """

    The function is used to check if the connection to the url-based DM root is actually valid.
    If no arguments are given, the current DM is checked.
    If a "dm_root" argument pair is given, then that url will be checked.

    Parameters
    ----------
    dm_root : str, optional
            When this argument is given, then that url will be checked.

    reconnect : bool, optional
            Set to True, if you automatically wish to try and reconnect if the connection is invalid.

    Returns
    -------
    int
            Returns 1 if the connection is valid, or 0 if it is invalid or no DM root has been defined.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                if dm.IsConnectionValid():
                    print("Connection to current DM is valid.")
                else:
                    print("Connection to current DM is lost.")
                # OR:
                if dm.IsConnectionValid(dm_root="http://ektoras:8080/"):
                    print("Connection to http://ektoras:8080/ is valid.")
                else:
                    print("Connection to http://ektoras:8080/ is lost.")


    """


def GetRoot() -> str:
    """

    Returns the path that currently points to DM.

    Returns
    -------
    str
            Returns a string containing the current DM root.
            A string of length 0 is returned if no DM path is currently set.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm_root = dm.GetRoot()
                print(dm_root)


    """


def SetRoot(dm_root: str, username: str, password: str, role: str, ticket: str) -> int:
    """

    Sets the current DM root to the path DM_PATH.

    Parameters
    ----------
    dm_root : str
            A string that describes the path of the DM root directory.

    username : str, optional
            Username (For login to web based DMs).

    password : str, optional
            Password (For login to web based DMs).

    role : str, optional
            User role (For setting the user's role to web based DMs).

    ticket : str, optional
            Ticket (For login to web based DMs). This argument is provided
            when the connection should employ an already available ticket,
            and there is no need to authenticate with username / password.

    Returns
    -------
    int
            Returns 1 if the new DM root has been set successfully and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("C:/Users/Local_Work_files/")


            # Set SPDRM vault as DM Root
            def main():
                dm.SetRoot("http://magneto.localdomain:8080/", username="user1", password="pass1")
                # when we want to change the user's role(when supported):
                dm.SetRoot(
                    "http://magneto.localdomain:8080/",
                    username="user1",
                    password="pass1",
                    role="Administrator",
                )


    """


def RemoveRoot(dm_root: str) -> int:
    """

    Removes the specified DM path or url from the "Set DM Paths" window list.

    Parameters
    ----------
    dm_root : str
            The DM path in question.

    Returns
    -------
    int
            Returns 1 if the specified DM root has been removed successfully and 0 otherwise.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.RemoveRoot("C:/Users/Local_Work_files/")


    """


def GetRootsList() -> object:
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

    See Also
    --------
    ShowDMPathsWindow

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                print(dm.GetRootsList())


    """


def GetAcceptedValuesForAttribute(
    type: str, attribute_name: str, return_accepted_values_from_rules: bool
) -> object:
    """

    Given a type and an attribute's name, this function will return the accepted
    values, as they are defined in the dm_structure.xml or hardcoded, if they exist.

    Parameters
    ----------
    type : str
            The type whose Attribute the values are requested. The specified type
            can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
            through the Data Model (e.g. Loadcase).

    attribute_name : str
            The Attribute's name. It can either be a Primary or Secondary Attribute.

    return_accepted_values_from_rules : bool, optional
            Defines if the returned accepted values will be based on the specified rules (True) or if they will be ignored (False)
            Default value: False

    Returns
    -------
    object
            If 'return_accepted_values_from_rules' is False, the function returns a list with the accepted values as strings, if they exist, otherwise returns an empty list.
            If 'return_accepted_values_from_rules' is True, the function returns a list [accepted_values, base_object_type, base_property_name],
            where:
                'accepted_values' is a dictionary with keys the values of the property of the base object and values the accepted values according to the specified rules.
                'base_object_type' is a string with the type of the base object
                'base_property_name' is a string with the property of the base object
            If the Attribute or the Type don't exist, or if any other DM error occurs, None is returned.

    See Also
    --------
    dm.HasAttributeConditionRule, dm.IsAttributeRuleGenerated

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def example1():
                dm.SetRoot("http://ektoras:7080/", username="admin", password="admin")
                accepted_values = dm.GetAcceptedValuesForAttribute("parts", "Status")
                print(accepted_values)


            def example2():
                dm_item_type = "Module"
                attribute = "Group"

                if dm.HasAttributeConditionRule(dm_item_type, attribute):
                    ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, True)
                    print(
                        "The accepted values of the "
                        + attribute
                        + " are specified from the "
                        + ret[2]
                        + " value of the "
                        + ret[1]
                        + " as follows:"
                    )
                    for val in ret[0].keys():
                        print("------------------------------------------------------------")
                        print("When " + ret[2] + " = " + val + ", the accepted values are:")
                        for accepted_val in ret[0][val]:
                            print(accepted_val)
                else:
                    ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, False)
                    print("The accepted values of the " + attribute + " attribute are:")
                    for val in ret:
                        print(val)


    """


def GetAttachmentAttributeValues(
    server_id: str, filename: str, entity_type: str
) -> object:
    """

    This function will collect all attributes and their values for a DM Object's attachment.

    Parameters
    ----------
    server_id : str
            The DM Object's server id.

    filename : str
            The attachment's filename, relative to the DM Object.

    entity_type : str, optional
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    Returns
    -------
    object
            Returns a dictionary with attribute names/values as the key/data.
            If nothing is found, None is returned.

    See Also
    --------
    dm.SetAttachmentAttributeValues

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                result = dm.GetAttachmentAttributeValues(
                    server_id="ABy4Ww:Cuo", filename="DA/job_definition.xml"
                )
                if result:
                    print(result)


    """


def SetAttachmentAttributeValues(
    server_id: str, filename: str, entity_type: str, names_values: object
) -> int:
    """

    This function will set values for attributes for a DM Object's attachment.

    Parameters
    ----------
    server_id : str, optional
            The DM Object's server id.
            Although it's an optional argument, it needs to be defined.

    filename : str, optional
            The attachment's filename, relative to the DM Object.

    entity_type : str, optional
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    names_values : object, optional
            A dictionary which holds the attributes to be set, along with their values.

    Returns
    -------
    int
            Returns 1 on success, or 0 on failure.

    See Also
    --------
    dm.GetAttachmentAttributeValues

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                result = dm.SetAttachmentAttributeValues(
                    server_id="ABy4Ww:Cuo",
                    filename="DA/job_definition.xml",
                    names_values={"TEST": "1"},
                )
                print("Function returned: ", str(result))

                result = dm.GetAttachmentAttributeValues(
                    server_id="ABy4Ww:Cuo", filename="DA/job_definition.xml"
                )
                if result:
                    print(result)


    """


def GetAttributesFromUniqueRepresentations(
    server_id: Any, type: str, values: object, ask_sdm: bool, object_id: Any
) -> object:
    """

    This function will return all Properties/Attributes for a specific input,
    either server ids, a filter or a DM Browser window item.

    Parameters
    ----------
    server_id : Any, optional
            The server id of the DM Object, or a list with server ids, if it is already known.
            Required even though it's optional.

    type : str, optional
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    values : object, optional
            A dictionary which holds a filter (names - values)
            that will be used when no server ids or object ids are defined.

    ask_sdm : bool, optional
            In case of SDM CONSOLE, we can query the already downloaded values
            instead of querying DM. It should be used in cases where the query is expected
            to be very slow.

    object_id : Any, optional
            When this function is called through an action in DM Browser or SDM CONSOLE,
            object_id is the GUI item's id, or a list with object ids. It can be used when
            we don't know the server_id.

    Returns
    -------
    object
            Returns a list with dictionaries, with the specified attribute values.
            If the function fails, the list will be empty.

    See Also
    --------
    DMObject

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                vals = {"Project": "L1", "Discipline": "Crash"}
                ret = dm.GetObjectId("parts", vals)
                if ret:
                    list_of_dicts = dm.GetAttributesFromUniqueRepresentations(
                        server_id=ret, type="parts"
                    )
                    len_of_list_of_dicts = len(list_of_dicts)
                    for each_dict in list_of_dicts:
                        print("Representation: ", each_dict["Representation"])


    """


def GetSubHierarchyChildIds(
    names_values: object,
    server_id: str,
    child_server_id: str,
    hierarchy: str,
    get_group_ids: bool,
) -> object:
    """

    Use this function to get server ids for the children of a DM Object, but at an inner level in the hierarchy.

    Parameters
    ----------
    names_values : object, optional
            A dictionary which holds the DM Object's property values
            (all property values must be present for the object's identification).

    server_id : str, optional
            The server id of the DM Object, if it is already known.
            If present, the type and names_values arguments can be omitted.

    child_server_id : str, optional
            The child server id whose subhierarchy will be searched.
            It is used along with the 'hierarchy' argument.

    hierarchy : str, optional
            The "Hierarchy" value for the child whose subhierarchy will be searched.
            It is used along with the 'child_server_id' argument.

    get_group_ids : bool, optional
            If set to True (default), server ids for Groups will also be returned.
            Otherwise, only items that have no children will be returned.

    Returns
    -------
    object
            Returns a list with server ids for DM Objects that exist in the subhierarchy.

    See Also
    --------
    GetComponentsChildIds

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                result = dm.GetSubHierarchyChildIds(
                    server_id="ABy4Ww:Cuo",
                    child_server_id="AAQlbA:Cuo",
                    hierarchy="P4E7656_A-_10_A_F16-KOGR-4100-001-VORDERBAU-ROHKAROSSERI/",
                )
                print(str(result))
                # will print: ['AAQlbA:Cuo', 'ABwdqw:Cuo', 'ABwqjw:Cuo']


    """


def GetComponentsChildIds(
    server_id: str, get_group_ids: bool, ask_sdm: bool, object_id: int
) -> list:
    """

    Use this function to get server ids for the children of a DM Object.

    Parameters
    ----------
    server_id : str, optional
            The DM Object's server id.
            Required even though it's optional.

    get_group_ids : bool, optional
            When this is True (default), server ids for Groups will also be returned.
            Otherwise, only items that have no children will be returned.

    ask_sdm : bool, optional
            In case of SDM CONSOLE, we can query the already downloaded values
            instead of querying DM. It should be used in cases where the query is expected to be very slow.

    object_id : int, optional
            When this function is called through an action in DM Browser or SDM CONSOLE,
            object_id is the GUI item's id. It can be used when
            we don't know the server_id.

    Returns
    -------
    list
            A list with server ids for DM Objects that exist in the hierarchy.

    See Also
    --------
    dm.GetSubHierarchyChildIds

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                result = dm.GetComponentsChildIds(server_id="ABy4Ww:Cuo", get_group_ids=False)
                print(len(result))
                # will print: 55

                result = dm.GetComponentsChildIds(server_id="ABy4Ww:Cuo")
                print(len(result))
                # will print: 67


    """


def AddFile(
    file_name: str,
    type: str,
    attributes: object,
    server_id: str,
    dm_root: str,
    target_dm_root: str,
    add_attachments: bool,
    add_children: bool,
) -> int:
    """

    Adds a file in the current or target DM.

    Parameters
    ----------
    file_name : str, optional
            The file path of the file to be added in DM.

    type : str, optional
            Accepted values: 'parts', 'includes', 'Subsystems'.
            For parts an .ansa file must be provided.

    attributes : object, optional
            A dictionary with the key DM attributes of the file.
            The module id, version, study version and representation
            must be provided. The names of the attributes must be
            provided as they appear in Model Browser and DM Browser.

    server_id : str, optional
            Instead of the file, a server id from a source dm root can be provided as source.
            file_name and server_id are mutually exclusive arguments.

    dm_root : str, optional
            The  dm root server_id refers to. if not provided, the current dm is assumed.
            This option is used only if server_id is provided.

    target_dm_root : str, optional
            The dm root where the file will be added. If not provided, the current dm root
            is assumed. This option is used only if server_id is provided.

    add_attachments : bool, optional
            Default: false. If true, any attachments of the server_id will also be added in dm.
            This option is used only if server_id is provided.

    add_children : bool, optional
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

            import ansa
            from ansa import dm


            def main():
                dict1 = {}
                dict1["Module Id"] = "23"
                dict1["Version"] = "0"
                dict1["Study Version"] = "0"
                dict1["Representation"] = ""  # empty for common representation

                ret = dm.AddFile("/home/user/my_file.ansa", "parts", dict1)


    """


def ExecuteSimManagerQuery(
    query_string: str, dm_root: str, progress_bar: object
) -> List[dict]:
    """

    Runs a query using the SimManager's REST API functionality.
    It is about requesting data for a set of objects.

    Parameters
    ----------
    query_string : str
            type=[OT]&expr=[EL]&view=[VIEW1]&view=[VIEW2]&pageSize=[SIZE]&page=[PAGE]
            oid=[OID]&expr=[EL]
            query=[QUERY_SPEC]
            query=[QUERY_SPEC]&f=[EL1]&f=[EL2]

            type: Object type, Is the type of the objects on which the expression is evaluated
                  (optional, but either type, oid, or query are required).
            expr: EL expression, Is an EL expression being evaluated on the object type.
                  It's optional. If missing, "this" is assumed. The expression can be a filter
                  (e.g. [name == 'ABC*'], or a navigation expression (e.g. results.keyResults),
                  or any combination of both. Sorting is also supported.
            view: View, Is the name of a view. It defines the fields being returned for each
                  object. If multiple views are specified, then fields of the first valid view in
                  the list will be returned. It's optional. If missing, "Default" is assumed.
            pageSize: Integer, Defines the maximum number of objects to be returned.
                      It's optional. If missing, "100" is assumed.
            page: Integer, Defines the which page of the data is returned if there are more
                  than SIZE objects. It's optional. If missing, "1" is assumed.
            oid: Object id, Is the ID of an object (id:tid). It can be used instead of an object
                 type as a starting point. Then the expression will be evaluated in this object.
            query: Query, A serialized query definition
                   (optional, but either type, oid, or query are required).
            f: EL expression, Instead of providing the name of a view, fields can be specified
               defining a new "view". Those fields could be any kind of EL expression.

    dm_root : str, optional
            The target DM root(URL). If not provided, the current DM is assumed.

    progress_bar : object, optional
            The progress can be shown in a BCProgressBar,
            created with guitk.BCProgressBarCreate.

    Returns
    -------
    List[dict]
            Returns a list of dictionaries, with name/value pairs.

    See Also
    --------
    LaunchSimManagerAction, ExportFileFromSimManager, UploadFileToSimManagerVault

    Examples
    --------
    ::

            #!/usr/bin/env python
            import os


            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            def main():
                if module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                dm.SetRoot(
                    "http://sim-manager-psa:9495/cb2/", username="aroubies", password="aroubies"
                )
                results = dm.ExecuteSimManagerQuery(
                    "type=Project&expr=[name=='/CAE']&view=Detailed"
                )
                if results:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' returned "
                        + str(len(results))
                        + " total results!"
                    )
                    project_id = results[0].get("_server_id_")
                    if project_id:
                        arguments = {"project": project_id}  # AkmSDQ:AOk
                        print(
                            "LaunchSimManagerAction 'Search' in Project "
                            + str(project_id)
                            + "  returned "
                            + str(dm.LaunchSimManagerAction("Search", arguments))
                        )
                        arguments = {"project": "AkmSDQ:AOks"}
                        print(
                            "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned "
                            + str(dm.LaunchSimManagerAction("Search", arguments))
                        )
                else:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' failed!"
                    )
                results = dm.ExecuteSimManagerQuery(
                    "type=Project&expr=[name=='/CAE1']&view=Detailed"
                )
                if results:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' returned "
                        + str(len(results))
                        + " total results!"
                    )
                else:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' failed!"
                    )


    """


def LaunchSimManagerAction(
    action_name: str,
    arguments: object,
    dm_root: str,
    return_process_id: bool,
    progress_bar: object,
    json: str,
) -> Any:
    """

    Launches an Action in SimManager, using the REST API functionality.

    Parameters
    ----------
    action_name : str
            The Action's name, e.g. "Search".

    arguments : object
            A dictionary with the Action's parameters.
            The values need to be percent encoded.

    dm_root : str, optional
            The target DM root(URL). If not provided, the current DM is assumed.

    return_process_id : bool, optional
            In case you need the process id returned, this argument should be set to True.

    progress_bar : object, optional
            The progress can be shown in a BCProgressBar,
            created with guitk.BCProgressBarCreate.

    json : str, optional
            User can provide their own JSON string which will be passed to the Action.
            No validation occurs, it's up to the user to make sure the JSON is valid.

    Returns
    -------
    Any
            If the Action runs successfully, True is returned.
            Otherwise, False is returned.
            If the argument return_process_id=True, the process id is returned. If it fails,
            None will be returned.

    See Also
    --------
    ExecuteSimManagerQuery, ExportFileFromSimManager, UploadFileToSimManagerVault

    Examples
    --------
    ::

            #!/usr/bin/env python
            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            if module_exists("ansa"):
                import ansa
                from ansa import dm
            elif module_exists("ansa"):
                import ansa
                from ansa import dm
            import urllib
            from urllib import parse


            def _getObjectIdByName(objectName, objectType):
                expr = "type=" + objectType + "&expr=[name=='" + objectName + "']&f=objectId"
                results = dm.ExecuteSimManagerQuery(expr)
                objectId = ""
                if results and len(results) == 1:
                    objectId = results[0].get("Id")
                return objectId


            def _addUserToProject(user_info, project_id, role_name):
                # First get all the Users that are assigned to this Project because it's needed for the next call:
                existing_users = dm.ExecuteSimManagerQuery(
                    "type=ProjectSubject&expr=[projectDomain[domain.name == 'Default'].project.objectId=='%s' AND subject.type.name=='User' AND role.name!='Project-Visitor']&page=1&pageSize=1000&f=subject.name&f=role&f=role.objectId&f=role.type.objectId&f=subject.objectId&f=subject.type.objectId"
                    % project_id.split(":")[0]
                )
                role_id = _getObjectIdByName(role_name, "Role")
                arguments = dict()
                arguments["project"] = project_id
                arguments["projectToUpdate"] = project_id
                arguments["propagate"] = "true"
                arguments["varSets"] = "userAndRole"  # needed for the list below
                users_list = list()
                for user in existing_users:
                    user_dict = {
                        "user": user.get("User"),
                        "role": user.get("role.objectId") + ":" + user.get("role.type.objectId"),
                    }
                    users_list.append(user_dict)
                selected_user_dict = {"user": selected_user.get("Name"), "role": role_id}
                users_list.append(selected_user_dict)
                arguments["users"] = users_list
                return dm.LaunchSimManagerAction("AssignUsersToProjectSimActivity", arguments)


            def _CreateNewComment(project, parent_oid, title, text, comment_type):
                if not text or text.isspace():
                    text = "-"
                project_id = _getObjectIdByName(project, "Project")
                arguments = {
                    "project": project_id,
                    "object": parent_oid,
                    "title": urllib.parse.quote(title),
                    "text": urllib.parse.quote(text),
                    "commentType": comment_type,
                }

                return dm.LaunchSimManagerAction("CreateCommentSimActivity", arguments)


            def main():
                dm.SetRoot(
                    "http://sim-manager-psa:9495/cb2/", username="aroubies", password="aroubies"
                )
                results = dm.ExecuteSimManagerQuery(
                    "type=Project&expr=[name=='/CAE']&view=Detailed"
                )
                if results:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' returned "
                        + str(len(results))
                        + " total results!"
                    )
                    project_id = results[0].get("Id")
                    if project_id:
                        arguments = {"project": project_id}  # AkmSDQ:AOk
                        print(
                            "LaunchSimManagerAction 'Search' in Project "
                            + str(project_id)
                            + "  returned "
                            + str(dm.LaunchSimManagerAction("Search", arguments))
                        )
                        arguments = {"project": "AkmSDQ:AOks"}
                        print(
                            "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned "
                            + str(dm.LaunchSimManagerAction("Search", arguments))
                        )
                        arguments = {"project": "AkmSDQ:AOks"}
                        print(
                            "LaunchSimManagerAction 'Search' in Project AkmSDQ:AOks returned the id: "
                            + str(
                                dm.LaunchSimManagerAction(
                                    "Search", arguments, return_process_id=True
                                )
                            )
                        )
                else:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE']&view=Detailed' failed!"
                    )
                results = dm.ExecuteSimManagerQuery(
                    "type=Project&expr=[name=='/CAE1']&view=Detailed"
                )
                if results:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' returned "
                        + str(len(results))
                        + " total results!"
                    )
                else:
                    print(
                        "ExecuteSimManagerQuery  'type=Project&expr=[name=='/CAE1']&view=Detailed' failed!"
                    )
                ##########################################################################################################
                # In order to pass DynamicProperties to the Action Arguments:

                project_id = _getObjectIdByName("/Data/Car/Stamp-X-Mapping", "Project")
                phase_id = _getObjectIdByName("ALU", "ProjectPhase")
                template_id = _getObjectIdByName(
                    "DCMCrashMappingTemplate", "EnterpriseWorkRequestTemplate"
                )
                name = "TRALALA5"

                dynamic_properties_list = list()
                dynamic_property_dict = {
                    "objectTypeName": "String",
                    "AttrName": "Product Line",
                    "AttrType": "String",
                    "DynamicString": "L6",
                }
                dynamic_properties_list.append(dynamic_property_dict)
                dynamic_property_dict = {
                    "objectTypeName": "String",
                    "AttrName": "Derivat",
                    "AttrType": "String",
                    "DynamicString": "G31",
                }
                dynamic_properties_list.append(dynamic_property_dict)
                dynamic_property_dict = {
                    "objectTypeName": "DCMPartModel",
                    "AttrName": "Parts",
                    "AttrType": "DbObjectList",
                    "DynamicDbObjectList": "Aegt2g:Cuo,AegwRQ:Cuo,Aegp3Q:Cuo,AegwTg:Cuo,AegwXQ:Cuo",
                }
                dynamic_properties_list.append(dynamic_property_dict)

                arguments = {
                    "project": project_id,
                    "phase": phase_id,
                    "template": template_id,
                    "name": name,
                    "DynamicProperties": dynamic_properties_list,
                }
                dm.LaunchSimManagerAction("PublishWorkRequest", arguments)


            def main():
                json = {"name":"PublishWorkRequest","label":"Publish WorkRequest","params":{"template":{"name":"template","value":[""],"label":"Template","required":true,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestTemplate","array":false},"DynamicProperties":{"varSets":{"DynamicProperties":{"params":{"DynamicDocument":{"name":"DynamicDocument","required":false,"type":"FILE","array":false},"AttrName":{"name":"AttrName","required":false,"type":"STRING","array":false},"AttrType":{"name":"AttrType","required":false,"type":"STRING","array":false},"DynamicDbObjectList":{"name":"DynamicDbObjectList","required":false,"type":"ONE_REFERENCE","objectType":"SDMBase","array":true},"DynamicBoolean":{"name":"DynamicBoolean","required":false,"type":"BOOLEAN","array":false},"DynamicString":{"name":"DynamicString","required":false,"type":"STRING","array":false},"DynamicDbObject":{"name":"DynamicDbObject","required":false,"type":"ONE_REFERENCE","objectType":"SDMBase","array":false},"DynamicDouble":{"name":"DynamicDouble","required":false,"type":"DOUBLE","array":false},"DynamicLong":{"name":"DynamicLong","required":false,"type":"LONG","array":false},"DynamicFile":{"name":"DynamicFile","required":false,"type":"FILE","array":false},"objectTypeName":{"name":"objectTypeName","required":false,"type":"STRING","array":false},"DynamicDate":{"name":"DynamicDate","required":false,"type":"DATE","array":false}},"values":[{"AttrName":["Product Line"],"AttrType":["String"],"DynamicString":["L6"],"objectTypeName":["String"]},{"AttrName":["Derivat"],"AttrType":["String"],"DynamicString":["G31"],"objectTypeName":["String"]},{"AttrName":["Parts"],"AttrType":["DbObjectList"],"DynamicDbObjectList":["Aegt2g:Cuo","AegwRQ:Cuo","Aegp3Q:Cuo","AegwTg:Cuo","AegwXQ:Cuo"],"objectTypeName":["DCMPartModel"]}]},"DynamicMeasure":{"values":[],"params":{"MeasureName":{"name":"MeasureName","required":false,"type":"STRING","array":false},"Quantity":{"name":"Quantity","required":false,"type":"DOUBLE","array":false},"QuantityType":{"name":"QuantityType","required":false,"type":"STRING","array":false},"Unit":{"name":"Unit","required":false,"type":"STRING","array":false},"objectTypeName":{"name":"objectTypeName","required":false,"type":"STRING","array":false}}}},"name":"DynamicProperties","value":[],"label":"DynamicProperties","required":false,"type":"LIST","array":false},"startDate":{"name":"startDate","value":[],"label":"Start Date","required":false,"type":"DATE","array":false},"edit":{"name":"edit","value":[],"label":"Edited Object","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"finishDate":{"name":"finishDate","value":[],"label":"Finish Date","required":false,"type":"DATE","array":false},"parent":{"name":"parent","value":[],"label":"Parent","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"workRequest":{"name":"workRequest","value":[],"label":"Work Request","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"type":{"name":"type","value":[],"label":"Work Request Template Type","required":false,"type":"ONE_REFERENCE","objectType":"ObjectType","array":false},"phase":{"name":"phase","value":["Czw:AJk"],"label":"Phase","required":false,"type":"ONE_REFERENCE","objectType":"ProjectPhase","filter":"[isActive=='true']","array":false},"project":{"name":"project","value":[""],"label":"Project","required":true,"type":"ONE_REFERENCE","objectType":"Project","array":false},"inputs":{"name":"inputs","value":[],"label":"Inputs","required":false,"type":"ONE_REFERENCE","objectType":"SDMObject","array":true},"description":{"name":"description","value":[],"label":"Description","required":false,"type":"STRING","array":false},"name":{"name":"name","value":["TRALALA5"],"label":"Name","required":true,"type":"STRING","array":false},"copy":{"name":"copy","value":[],"label":"Copied Object","required":false,"type":"ONE_REFERENCE","objectType":"EnterpriseWorkRequestInstance","array":false},"autoRelease":{"name":"autoRelease","value":[],"label":"Auto Release","required":false,"type":"BOOLEAN","array":false}},"execution":"LocalImmediate","version":"1.5.1"}
                dm.LaunchSimManagerAction("PublishWorkRequest", json=json)


    """


def GetConnectedUsername(dm_root: str) -> str:
    """

    The function is used to return the username that was used to connect to the url-based DM.
    If no arguments are given, the current DM is checked.
    If a "dm_root" argument pair is given, then that url will be checked.

    Parameters
    ----------
    dm_root : str, optional
            When this argument is given, then that url will be checked.

    Returns
    -------
    str
            Returns the Username.
            If something goes wrong, None will be returned.

    See Also
    --------
    IsConnectionValid

    Examples
    --------
    ::

            # no imports needed in this stage


            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            def main():
                if module_exists("ansa"):
                    import ansa
                    from ansa import base, dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import base, dm
                dm.SetRoot("http://ektoras:8080/", username="aroubies", password="aroubies")
                print("Connected user: ", dm.GetConnectedUsername())


    """


def GetLogFileText() -> str:
    """

    This function assembles logging data from the current My_DM.log file, as well
    as the previously rotated, compressed archives and returns it as a single
    string.

    When the lock cannot be acquired, a Runtime exception is thrown. The reason may
    be a transient failure (other operations are running which need to lock the log
    file), or a stale lock file. Stale lock files may be remnants of abnormally
    terminated processes, whose locks have not expired yet.

    Returns
    -------
    str
            Returns a string holding all My_DM.log data.

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            try:
                log_data = dm.GetLogFileText()
                print(log_data)
            except:
                print("Couldn't get logging data from My_DM.log")


    """


def GetLibraryItemAttributeValues(library: str, filename: str) -> object:
    """

    This function will collect all attributes and their values for a library item File.
    It needs to be a generic Library Item file.

    Parameters
    ----------
    library : str
            The library's name, e.g. "batch_mesh_sessions".

    filename : str
            The file's filename, relative to the library, e.g. "test1/test2/file.txt".

    Returns
    -------
    object
            Returns a dictionary with attribute names/values as the key/data.
            If nothing is found, an empty dictionary is returned.

    See Also
    --------
    DownloadLibraryItem, GetAvailableLibraryItems

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("http://spdrm-dev:40080/", username="admin", password="admin")
                results = dm.GetAvailableLibraryItems("spdrm_scripts")
                if results:
                    print(results)
                    for result in results:
                        try:
                            print(
                                result
                                + ":   "
                                + str(dm.GetLibraryItemAttributeValues("spdrm_scripts", result))
                                + "\\n"
                            )
                        except:
                            pass
                results = dm.GetAvailableLibraryItems("tmp_library_items")
                if results:
                    print(results)
                    for result in results:
                        try:
                            print(
                                result
                                + ":   "
                                + str(dm.GetLibraryItemAttributeValues("tmp_library_items", result))
                                + "\\n"
                            )
                        except:
                            pass
                dm.SetRoot("//mnt/raid_disk/titanas/roubies/DMs/DM_BIG/")
                results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
                if results:
                    print(results)
                    for result in results:
                        try:
                            print(
                                result
                                + ":   "
                                + str(
                                    dm.GetLibraryItemAttributeValues("batch_mesh_sessions", result)
                                )
                                + "\\n"
                            )
                        except:
                            pass
                dm.SetRoot("http://sim-manager:9495/cb2/", username="admin", password="admin")
                results = dm.GetAvailableLibraryItems("batch_mesh_sessions")
                if results:
                    print(results)
                    for result in results:
                        try:
                            print(
                                result
                                + ":   "
                                + str(
                                    dm.GetLibraryItemAttributeValues("batch_mesh_sessions", result)
                                )
                                + "\\n"
                            )
                        except:
                            pass


    """


def PrintToLogFile(text: str, with_timestamp: bool):
    """

    Prints a line of text to My_DM.log.

    If 'with_timestamp' is set to 'True', additional timestamp and user data are printed along with 'text'.
    If 'with_timestamp' is set to 'False', only 'text' is printed.

    Parameters
    ----------
    text : str
            The line of text to be printed in the My_DM.log.

    with_timestamp : bool, optional
            Determines wether to print additional timestamp and user data along with 'text'.
            (Default: True)

    See Also
    --------
    GetLogFileText, ClearLogFile

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.PrintToLogFile(
                    "My text to be printed in the My_DM.log", True
                )  # print with timestamp data


    """


def ClearLogFile(clear_archived_files: bool) -> bool:
    """

    Clears the contents of the My_DM.log.

    If 'clear_archived_files' is set to True, archived log files (if any) are also deleted.
    If 'clear_archived_files' is set to False, only the contents of the current log file are cleared.
    By default, 'clear_archived_files' is True.

    Parameters
    ----------
    clear_archived_files : bool, optional
            Determines wether to clear the archived DM log files along with the current.
            (Default: True)

    Returns
    -------
    bool
            Returns:
            True: If both the current log file and the archived were successfully cleared.
            False: If any of the log files failed to be cleared.

    See Also
    --------
    GetLogFileText

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.ClearLogFile(
                    False
                )  # clears all the contents of the current My_DM.log but not the archived log files (if any)


    """


def GetDMTypeAttributes(type: str, hardcoded: bool) -> object:
    """

    Gets the secondary attributes of a particular DM object type
    (e.g. part, include etc.)

    Parameters
    ----------
    type : str
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

            In case of file-based DM with no dm_structure.xml,
            the accepted values for the argument "type" are:
            "parts", "includes", "configurations", "subsystems",
            "simulation_model", "simulation_run", "report",
            "session", "loadcase", "dm_library_item"

    hardcoded : bool, optional
            The Hardcoded Attributes are not returned by default.
            In order to retrieve those as well, this argument needs to be True.

    Returns
    -------
    object
            Returns a list of secondary attributes. Each secondary attribute in the list
            is a dictionary of key:value (strings) pairs for all the supported attribute
            member properties:

            'name': the name of the attribute
            'type': the type of the attribute
            'format': the max number of digits allowed by the attribute format, as a string
            'prefix': the prefix for the attribute value
            'default_value': the default value of the attribute
            'accepted_values': a comma seperated list of the attribute's accepted values
            'colors_for_accepted_values': a comma seperated list of accepted values colors
            'allow_null': 'YES'/'NO', whether the attribute accepts empty (null) values
            'read_only': 'YES'/'NO', whether the attribute is ReadOnly

    See Also
    --------
    dm.GetDMTypeProperties

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                sec_attributes = dm.GetDMTypeAttributes("parts")
                for attr_dict in sec_attributes:
                    print(attr_dict)


    """


def GetDMTypeProperties(type: str) -> object:
    """

    Gets the properties (primary attributes) of a particular DM object type
    (e.g. part, include etc.)

    Parameters
    ----------
    type : str
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

            In case of file-based DM with no dm_structure.xml,
            the accepted values for the argument "type" are:
            "parts", "includes", "configurations", "subsystems",
            "simulation_model", "simulation_run", "report",
            "session", "loadcase", "dm_library_item"

    Returns
    -------
    object
            Returns a list of properties. Each property in the list is a dictionary of
            key:value (strings) pairs for all the supported property member attributes:

            'name': the name of the property
            'type': the type of the property
            'format': the max number of digits allowed by the property format, as a string
            'prefix': the prefix for the property value
            'default_value': the default value of the property
            'accepted_values': a comma seperated list of the property's accepted values
            'colors_for_accepted_values': a comma seperated list of accepted values colors
            'allow_null': 'YES'/'NO', whether the property accepts empty (null) values
            'read_only': 'YES'/'NO', whether the property is ReadOnly

    See Also
    --------
    dm.GetDMTypeAttributes

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                properties = dm.GetDMTypeProperties("parts")
                for prop_dict in properties:
                    print(prop_dict)


    """


def OpenDMObjectsInNewTab(
    server_ids: object,
    entities: object,
    type: str,
    view: str,
    dm_system: str,
    tab_name: str,
    expand_all: bool,
    open_in_viewer: bool,
    open_in_reports_table: bool,
) -> bool:
    """

    This function can be used to open one or more hierarchies of any DM Object type,
    in a new tab, in DM Browser or KOMVOS.

    Parameters
    ----------
    server_ids : object, optional
            A list with DM Object server ids.

    entities : object, optional
            A list with ANSA entities.

    type : str, optional
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    view : str, optional
            The new Tab's view, e.g. "Default", "Flat" or a user defined in the dm_views.xml.
            When undefined, the function will return False.

    dm_system : str, optional
            The DM root that will be queried.

    tab_name : str, optional
            The new tab will be given this name.

    expand_all : bool, optional
            If set to True, all items in the new tab will be expanded.

    open_in_viewer : bool, optional
            If set to True, all items in the new tab will be loaded to the meta viewer.

    open_in_reports_table : bool, optional
            If set to True, Reports Table will also be launched for all  the items in the
            new tab that is opened. In case the requested Type is not supported in
            Reports Table (SimulationModel, LoadCase, SimulationRun) or no Reports
            are found in DM for the requested server_ids, the scipt function will just
            open the server_ids in a new tab and no Reports Table tabs will be opened.

    Returns
    -------
    bool
            Returns True if the tab is opened succesfully, otherwise False.

    Examples
    --------
    ::

            import ansa
            from ansa import base
            from ansa import dm


            def main():
                map = {"Project": "L1", "Discipline": "Crash"}
                server_id = dm.GetDMObjectId("Subsystems", map)
                if server_id:
                    list_of_ids = []
                    list_of_ids.append(server_id)
                    dm.OpenDMObjectsInNewTab(
                        server_ids=list_of_ids,
                        type="Subsystems",
                        view="Default",
                        tab_name="Subsystem in question",
                    )


            # in case of Part
            def main():
                parts = [base.GetPartFromModuleId("607001"), base.GetPartFromModuleId("607002")]
                dm.OpenDMObjectsInNewTab(entities=parts, type="parts", view="Flat")


    """


def ExportFileFromSimManager(
    server_id: str, expr: str, extension: str, dm_root: str, progress_bar: object
) -> str:
    """

    Exports a file using the SimManager's REST API functionality.
    This is about exporting files from the vault.
    The server transfers the file in its original format and will supply
    a MIME type based on the extension of the file name.

    Parameters
    ----------
    server_id : str
            Is the ID of an object (id:tid). It can be used instead of an object type as a starting point. Then the expression will be evaluated in this object.

    expr : str
            Is the EL epxression leading from the given object to the file to be transfered. Care has to be taken that only one file is referenced, e.g. files.model, file.pom_ExportedData.

    extension : str
            The extension that will be added to the downloaded file.
            SimManager will not add any extension, therefore it's up to the user to define it.

    dm_root : str, optional
            The target DM root(URL). If not provided, the current DM is assumed.

    progress_bar : object, optional
            The progress can be shown in a BCProgressBar,
            created with guitk.BCProgressBarCreate.

    Returns
    -------
    str
            Returns the exported filename, usually in a temporary location.
            Returns None in case of failure.

    See Also
    --------
    LaunchSimManagerAction, ExecuteSimManagerQuery, UploadFileToSimManagerVault

    Examples
    --------
    ::

            #!/usr/bin/env python
            import os


            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            def main():
                if module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                dm.SetRoot("http://sim-manager:9495/cb2/", username="aroubies", password="aroubies")
                # export file from a Model
                print(
                    dm.ExportFileFromSimManager(
                        server_id="AecJ6Q:CuE", expr="files.model", extension="ansa"
                    )
                )
                # export file from a Process
                print(
                    dm.ExportFileFromSimManager(
                        server_id="A3l8Ow:AN4", expr="file.pom", extension="xml"
                    )
                )


    """


def GetLibraryItemTypes(dm_root: str) -> object:
    """

    This function returns a list containing the names of all the Rich Library Item
    types that can exist for the DM.

    Parameters
    ----------
    dm_root : str, optional
            When this argument is given, then that DM will be used.
            Otherwise, the current DM root is used.

    Returns
    -------
    object
            Returns a list containing strings.
            An empty list is returned if no Rich Library Item types are defined.
            If something goes wrong, None is returned.

    Examples
    --------
    ::

            # PYTHON script
            import ansa
            from ansa import dm

            print(dm.GetLibraryItemTypes())
            print(dm.GetLibraryItemTypes(dm_root="C:/test/"))


    """


def GetObjectHierarchyIds(server_id: str) -> object:
    """

    This function provides hierarchy related information for all directly contained
    DM objects. With 'directly contained', it is meant that a single query on the
    Server ID provided as argument will only be done. No recursive, follow-up
    queries on children objects will be done, in order to check whether they
    contain children of their own.

    For example, when a Simulation Model gets queried with this function, all
    contained Subsystems will be returned only, without any information about
    possible groups or parts within the subsystems.

    On the other hand, when a Subsystem gets queried, all contained groups / parts
    will be returned (which may form arbitrary subhierarchies).

    Parameters
    ----------
    server_id : str
            The DM Object's server id.

    Returns
    -------
    object
            This function returns a list of tuples. For each contained DM object, a tuple of
            the form (server_id, parent_server_id) is to be found in the list.

    See Also
    --------
    dm.GetComponentsChildIds

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                hier = dm.GetObjectHierarchyIds(server_id="A2w7qg:Cuo")
                print(hier)
                # [('A2w9Sg:Cuo', 'A2w9Rw:Cuo'), ('A2w9Rw:Cuo', 'A2w7qg:Cuo'), ...]


    """


def RunDMSession(server_id: str, session_id: str):
    """

    Run a DM Session on a certain DM server id

    Parameters
    ----------
    server_id : str
            The server id on which the session will run

    session_id : str
            The id of the session

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.RunDMSession(server_id="48", session_id="79")


            if __name__ == "__main__":
                main()


    """


def HasAttributeConditionRule(type: str, attribute_name: str) -> bool:
    """

    Given a type and an attribute's name, this function will check whether a condition rule is defined.

    Parameters
    ----------
    type : str
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    attribute_name : str
            The Attribute's name. It can either be a Primary or Secondary Attribute.

    Returns
    -------
    bool
            Returns True if the attribute has a condition rule. Otherwise, it returns False.

    See Also
    --------
    dm.GetAcceptedValuesForAttribute, dm.IsAttributeRuleGenerated

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm_item_type = "Module"
                attribute = "Group"

                if dm.HasAttributeConditionRule(dm_item_type, attribute):
                    ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, True)
                    print(
                        "The accepted values of the "
                        + attribute
                        + " are specified from the "
                        + ret[2]
                        + " value of the "
                        + ret[1]
                        + " as follows:"
                    )
                    for val in ret[0].keys():
                        print("------------------------------------------------------------")
                        print("When " + ret[2] + " = " + val + ", the accepted values are:")
                        for accepted_val in ret[0][val]:
                            print(accepted_val)
                else:
                    ret = dm.GetAcceptedValuesForAttribute(dm_item_type, attribute, False)
                    print("The accepted values of the " + attribute + " attribute are:")
                    for val in ret:
                        print(val)


    """


def IsAttributeRuleGenerated(type: str, attribute_name: str) -> bool:
    """

    Given a type and an attribute's name, this function will check whether the value of this attribue is auto-generated by a rule.

    Parameters
    ----------
    type : str
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).

    attribute_name : str
            The Attribute's name. It can either be a Primary or Secondary Attribute.

    Returns
    -------
    bool
            Returns True if the attribute value is auto-generated by a rule. Otherwise, it returns False.

    See Also
    --------
    dm.GetAcceptedValuesForAttribute, dm.HasAttributeConditionRule

    """


def GetAttributeValueFromGenerationRule(
    type: str, attribute_name: str, attribute_values: object
) -> str:
    """

    Given a type, an attribute's name and the attribute values, this function will
    return the generated value that is defined by the rule in the dm_structure.xml.

    Parameters
    ----------
    type : str
            The type whose Attribute the value is requested. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

    attribute_name : str
            The Attribute' s name. It can either be a Primary or Secondary Attribute.

    attribute_values : object
            A dictionary containing the attribute name-values dictionary per attribute type that determine the value of the input attribute. e.g. {'Parts' : {'Name': 'my_name', 'Module Id':''001'}, 'Subsystems : {'Name':'subsystem_name', 'Version':A}}

    Returns
    -------
    str
            The generated attribute value.
            If the attribute is not rule generated it will return None.
            If not all required attribute values are given in 'attribute_values' the default values will be selected.
            If the argument 'attribute_values' is not a dict with dicts as value it will return None.

    See Also
    --------
    dm.IsAttributeRuleGenerated, dm.GetAttributeGenerationRule

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def main():
                attr_type = "Module"
                attribute = "Name"

                if dm.IsAttributeRuleGenerated(type=attr_type, attribute_name=attribute):
                    rule = dm.GetAttributeGenerationRule(type=attr_type, attribute_name=attribute)
                    values = {
                        "Subsystems": {"Module Id": 1000, "Version": "AAA", "Study Version": "0001"}
                    }
                    new_val = dm.GetAttributeValueFromGenerationRule(
                        type=attr_type, attribute_name=attribute, attribute_values=values
                    )


    """


def ShowDMPathsWindow() -> str:
    """

    Shows the "Set DM Paths" window.

    Returns
    -------
    str
            Returns a string containing the current DM root if it succeeds.
            Returns None in case of "Cancel" or failure to add a DM.

    See Also
    --------
    GetRoot, SetRoot, GetRootsList

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm_root = dm.ShowDMPathsWindow()
                print(dm_root)


    """


def GetAttributeGenerationRule(type: str, attribute_name: str) -> object:
    """

    Given a type and an attribute's name, this function will return the generation
    rule, if exists.

    Parameters
    ----------
    type : str
            The type whose Attribute the generation rule is requested. The specified type
            can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined
            through the Data Model (e.g. Loadcase).

    attribute_name : str
            The Attribute's name. It can either be a Primary or Secondary Attribute.

    Returns
    -------
    object
            A dictionary with key the attribute type and value a list of the attribute names
            that determine the value of the input attribute.
            e.g. {'Subsystems': ['Module Id', 'Version', 'Study Version']}
            If the attribute is not rule generated, it will return None.

    See Also
    --------
    dm.IsAttributeRuleGenerated, dm.GetAttributeValueFromGenerationRule

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def main():
                attr_type = "Module"
                attribute = "Name"

                if dm.IsAttributeRuleGenerated(type=attr_type, attribute_name=attribute):
                    rule = dm.GetAttributeGenerationRule(type=attr_type, attribute_name=attribute)
                    values = {
                        "Subsystems": {"Module Id": 1000, "Version": "AAA", "Study Version": "0001"}
                    }
                    new_val = dm.GetAttributeValueFromGenerationRule(
                        type=attr_type, attribute_name=attribute, attribute_values=values
                    )


    """


def ExportDMStructureXml(filename: str) -> bool:
    """

    Exports the current Data Model to an XML file in the user defined directory.

    Parameters
    ----------
    filename : str, optional
            The full path directory (including the filename) where the XML file will be exported.
            If filename is not defined the XML file will replace the dm_structure.xml of the current DM.

    Returns
    -------
    bool
            Funtion returns a boolean  defining the result of the function.

    Examples
    --------
    ::

            # PYTHON script
            import ansa
            from ansa import dm


            def main():
                # Save to Current DM XML file (Warning:Using the bellow function will overwrite your current dm_structure.xml)
                result = dm.ExportDMStructureXml()
                print(result)
                # Save to a user defined location
                result = dm.ExportDMStructureXml(filename="/path/to/export/your_xml_file.xml")
                print(result)


            if __name__ == "__main__":
                main()


    """


def SetAcceptedValuesForAttribute(
    type: str, attr_name: str, accepted_values: str
) -> bool:
    """

    Changes the Accepted Values of an Attribute if the Type of that specific Attribute allows it.

    Parameters
    ----------
    type : str
            The name of the object that contains the Attribute whose Accepted Values will change.

    attr_name : str
            The name of the Attribute whose Accepted Values will change.

    accepted_values : str
            The Accepted values that will be applied to the Attribute.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    GetAcceptedValuesForAttribute

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Change Accepted Values
                result = dm.SetAcceptedValuesForAttribute(
                    type="type", attr_name="attr_name", accepted_values="the,new,accepted,values"
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def SetDefaultValueForAttribute(type: str, attr_name: str, default_value: str) -> bool:
    """

    Changes the Default Value of an Attribute if the Type of that specific Attribute allows it.

    Parameters
    ----------
    type : str
            The name of the object that contains the Attribute whose Default Value will change.

    attr_name : str
            The name of the Attribute whose Default Value will change.

    default_value : str
            The Default Value that will be applied to the Attribute.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    GetDefaultValueForAttribute

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Change Default Value
                dm.SetDefaultValueForAttribute(
                    type="type", attr_name="attr_name", default_value="new_default_value"
                )


            if __name__ == "__main__":
                main()


    """


def GetDefaultValueForAttribute(type: str, attr_name: str) -> str:
    """

    Returns the current Default Value of an Attribute.

    Parameters
    ----------
    type : str
            The name of the object that contains the Attribute whose Default Value will be returned.

    attr_name : str
            The name of the Attribute whose Default Value will be returned.

    Returns
    -------
    str
            Function returns a string with the Default Value of the Attribute contained in the Object Type.

    See Also
    --------
    SetDefaultValueForAttribute

    Examples
    --------
    ::

            # PYTHON script
            import ansa
            from ansa import dm


            def main():
                def_val = dm.GetDefaultValueForAttribute(type="type", attr_name="attr_name")
                print(def_val)


            if __name__ == "__main__":
                main()


    """


def CreateGenerationRule(
    type: str,
    rule_name: str,
    disc_chars: str,
    generated_value: str,
    rejected_characters: str,
    generator_name: str,
    generator_value: str,
    trim_empty_values: bool = False,
) -> bool:
    """

    This function is used in order to create a new Generation Rule for the current DM.

    Parameters
    ----------
    type : str
            The name of the object that will contain the created Generation Rule.

    rule_name : str
            The name of the Generation Rule that will be created.

    disc_chars : str, optional
            The Discarded values of the Generation Rule.

    generated_value : str, optional
            The Generated Value of the Generation Rule.

    rejected_characters : str, optional
            The discarded characters of the Generation Rule.

    generator_name : str, optional
            The Generator Name of the Generation Rule condition.

    generator_value : str, optional
            The Generator Value of the Generation Rule condition.

    trim_empty_values : bool, optional
            If True the trailing empty sections of the Generated Value are trimmed.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    DeleteGenerationRule, SetGeneratedValueOfGenerationRule, GetGeneratedValueOfGenerationRule

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Create Generation Rule
                result = dm.CreateGenerationRule(
                    type="ANSA_SUBSYSTEM",
                    rule_name="Name",
                    generated_value="[Module Id]_[Project]_[Phase]",
                    generator_name="Discipline",
                    generator_value="CRASH",
                    trim_empty_values=True,
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def DeleteGenerationRule(
    type: str, rule_name: str, generator_name: str, generator_value: str
) -> bool:
    """

    This function is used in order to delete a Generation Rule for the current DM.

    Parameters
    ----------
    type : str
            The name of the object that contains the Generation Rule about to be deleted.

    rule_name : str
            The name of the Generation Rule that will be deleted.

    generator_name : str, optional
            The Generator Name of the Generation Rule condition.

    generator_value : str, optional
            The Generator Value of the Generation Rule condition.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    CreateGenerationRule, SetGeneratedValueOfGenerationRule, GetGeneratedValueOfGenerationRule

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Delete Generation Rule (Assuming that the object and the rule exists)
                result = dm.DeleteGenerationRule(
                    type="ANSA_SUBSYSTEM",
                    rule_name="Name",
                    generator_name="Discipline",
                    generator_value="CRASH",
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def GetGeneratedValueOfGenerationRule(
    type: str, rule_name: str, generator_name: str, generator_value: str
) -> str:
    """

    Returns the current Generated Value of a Generated Rule.

    Parameters
    ----------
    type : str
            The name of the object that contains the Generation Rule.

    rule_name : str
            The name of the Generation Rule whose Generated Value will be returned.

    generator_name : str, optional
            The Generator Name of the Generation Rule condition.

    generator_value : str, optional
            The Generator Value of the Generation Rule condition.

    Returns
    -------
    str
            Function returns a string with the Generated Value of the Generation Rule contained in the Object Type.

    See Also
    --------
    CreateGenerationRule, DeleteGenerationRule, SetGeneratedValueOfGenerationRule

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Get Generated Value of Generation Rule
                result = dm.GetGeneratedValueOfGenerationRule(
                    type="type",
                    rule_name="rule_name",
                    generator_name="Discipline",
                    generator_value="CRASH",
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def SetGeneratedValueOfGenerationRule(
    type: str,
    rule_name: str,
    generated_value: str,
    generator_name: str,
    generator_value: str,
) -> bool:
    """

    Using this function you can change the Generated Value of an existing Generation Rule.

    Parameters
    ----------
    type : str
            The name of the object that contains the Generation Rule.

    rule_name : str
            The name of the Generation Rule whose Generated Value will be modified.

    generated_value : str
            The new Generated Value of the Generation Rule.

    generator_name : str, optional
            The Generator Name of the Generation Rule condition.

    generator_value : str, optional
            The Generator Value of the Generation Rule condition.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    CreateGenerationRule, DeleteGenerationRule, GetGeneratedValueOfGenerationRule

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Set Generated Value of Generation Rule
                result = dm.SetGeneratedValueOfGenerationRule(
                    type="ANSA_SUBSYSTEM",
                    rule_name="Name",
                    generated_value="[Module Id]_[Project]_[Phase]",
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def CreateConditionRule(
    type: str,
    rule_name: str,
    generator_name: str,
    generator_value: str,
    accepted_values: str,
) -> bool:
    """

    This function is used in order to create a new Condition Rule for the current DM.

    Parameters
    ----------
    type : str
            The name of the object that will contain the created Condition Rule.

    rule_name : str
            The name of the Condition Rule that will be created.

    generator_name : str
            The Generator Name of the Condition Rule.

    generator_value : str, optional
            The Generator Value of the Condition Rule.

    accepted_values : str, optional
            The Accepted Values of the Condiition Rule.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    DeleteConditionRule, GetGeneratorValuesOfConditionRules, SetGeneratorValueOfConditionRule

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Create Condition Rule
                result = dm.CreateConditionRule(
                    type="type",
                    rule_name="rule_name",
                    generator_name="generator_name",
                    generator_value="generator_value",
                    accepted_values="accepted_values",
                )
                print(result)


            if __name__ == "__main__":
                main()


    """


def DeleteConditionRule(type: str, rule_name: str, generator_value: str) -> bool:
    """

    This function is used in order to delete a Condition Rule for the current DM.

    Parameters
    ----------
    type : str
            The name of the object that contains the Condition Rule about to be deleted.

    rule_name : str
            The name of the Condition Rule that will be deleted.

    generator_value : str
            The Generator Value of the Condition Rule.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    CreateConditionRule, GetGeneratorValuesOfConditionRules, SetGeneratorValueOfConditionRule

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Delete Condition Rule
                dm.DeleteConditionRule(
                    type="type", rule_name="rule_name", generator_value="new_generator_value"
                )


            if __name__ == "__main__":
                main()


    """


def GetGeneratorValuesOfConditionRules(type: str, rule_name: str) -> object:
    """

    This function returns all the Generator Values used by a specific rule name.
    Multiple Condition Rules can have the same rule and generator name but different generator values.

    Parameters
    ----------
    type : str
            The type of the object that will contain Condition Rules.

    rule_name : str
            The name of the Condition Rules that contain the Generator Values.

    Returns
    -------
    object
            Returns a list of strings with the generator values of the specific Condition Rule contained in the specific Object Type

    See Also
    --------
    CreateConditionRule, DeleteConditionRule, SetGeneratorValueOfConditionRule

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Get Generator Values of the Condition Rules contained in a specific type with a specific rule_name
                dm.GetGeneratorValuesOfConditionRules(
                    type="parts", rule_name="RepresentationRule01"
                )


            if __name__ == "__main__":
                main()


    """


def SetGeneratorValueOfConditionRule(
    type: str, rule_name: str, old_generator_value: str, generator_value: str
) -> bool:
    """

    This Function is used in order to change the Generator Value of a specific Condition Rule.

    Parameters
    ----------
    type : str
            The type of the object that contains the Condition Rule about to be modified.

    rule_name : str
            The name of the Condition Rule that will be modified.

    old_generator_value : str
            The old value of the Generator Value. This value is needed because multiple Condition Rules can have the same rule name.

    generator_value : str
            The new value of the Generator Value.

    Returns
    -------
    bool
            Function returns a boolean variable defining the result of the function.

    See Also
    --------
    CreateConditionRule, DeleteConditionRule, GetGeneratorValuesOfConditionRules

    Examples
    --------
    ::

            # Python Script
            import ansa
            from ansa import dm


            def main():
                # Set Generator Value of Condition Rule
                dm.SetGeneratorValueOfConditionRule(
                    type="type",
                    rule_name="rule_name",
                    old_generator_value="old_generator_value",
                    generator_value="new_generator_value",
                )


            if __name__ == "__main__":
                main()


    """


def QueryDMObjects(query: object, type: str, free_text_targets: object) -> object:
    """

    Search in DM for objects which satisfy the specified query.

    Parameters
    ----------
    query : object
            The query can be expressed in one of the following forms:
            * A list of [<attribute_name>, <condition>, <value>] lists which
              specify the query. For Attributes of Versioning Scheme Counter
              type (e.g. Team Version, Study Version, etc.) the "Latest"
              keyword is supported as follows:
              [<versioning_attribute_name>, "equals", "Latest"]
            * A BetaQL string
            * A "free text" query string

    type : str, optional
            The type of the DM Object. The specified type can be ANSA type
            (e.g. ANSA_LOADCASE) or the DM type defined through the Data
            Model (e.g. Loadcase).
            In case of SPDRM-backend, the keywords "FOLDER" or "FILE" can be used, to query for specific folders or files respectively.

    free_text_targets : object, optional
            A list of the targets used in free text search queries
            (e.g. ["All"] or ["Simulation_Run", "Report"])

    Returns
    -------
    object
            Returns a dictionary with the following keys and values:
            key = 'error'
            value = 0(Success), 1(Nothing found), 2(No DM Root was set), 3(No access to DM Root),
                    4(Error in filters)
            key = 'output'
            value = A list with the DM objects which satisfy the query.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def printQueryResults(results):
                if results["error"] == 0:
                    for dm_object in results["output"]:
                        print("DM Object Id : ", dm_object.server_id)


            def query_dm_objects():
                ansa_type = "ANSA_SUBSYSTEM"

                dm_filters = [["Project", "contains", "XX"], ["Representation", "equals", "NVH"]]
                results = dm.QueryDMObjects(query=dm_filters, type=ansa_type)
                printQueryResults(results)

                # Equivalent query to the previous one, this time expressed as a BetaQL string
                beta_ql_query = "Project contains XX and Representation = NVH"
                results = dm.QueryDMObjects(beta_ql_query, ansa_type)
                printQueryResults(results)

                # Free text query
                free_text_query = "models with project venza"
                targets_list = ["All"]
                results = dm.QueryDMObjects(query=free_text_query, free_text_targets=targets_list)
                printQueryResults(results)


            query_dm_objects()


            def queryFolder():
                text_query = (
                    '"DM Path" = "DM:/LIBRARY_ITEMS/BETA_Suite_settings/settings_profiles/"'
                )
                results = dm.QueryDMObjects(query=text_query, type="FOLDER")
                if results["error"] == 0:
                    folder_server_id = results.get("output")[0].server_id
                    print("The server_id of the queried folder is: ", folder_server_id)


            def queryFile():
                text_query = '"DM Path" = "DM:/LIBRARY_ITEMS/BETA_Suite_settings/settings_profiles/crash_LsDyna/profile_description.json"'
                results = dm.QueryDMObjects(query=text_query, type="FILE")
                if results["error"] == 0:
                    file_server_id = results.get("output")[0].server_id
                    print("The server_id of the queried file is: ", file_server_id)


    """


def UploadFileToSimManagerVault(
    file_path: str,
    sim_activity_name: str,
    file_param_name: str,
    object_type: str,
    progress_bar: object,
) -> str:
    """

    Uploads a file to the SimManager vault and retrieves the vault id.

    Parameters
    ----------
    file_path : str
            The file that will be uploaded to SimManager.

    sim_activity_name : str
            The activity's name is needed for SimManager 2014.

    file_param_name : str
            The name of the FILE parameter in the SimActivity.

    object_type : str
            The object type of the object to which the file will be attached.
            If there is no target object type, use "Project".

    progress_bar : object, optional
            The progress can be shown in a BCProgressBar,
            created with guitk.BCProgressBarCreate.

    Returns
    -------
    str
            If the file is successfully added, the vault id will be returned.
            Returns None in case of failure.

    See Also
    --------
    ExportFileFromSimManager, LaunchSimManagerAction, ExecuteSimManagerQuery

    Examples
    --------
    ::

            import ansa


            def main():
                selected_import_file = ansa.utils.SelectOpenFile(0)
                if not selected_import_file:
                    return
                selected_import_file = selected_import_file[0]

                ret_vault_id = ansa.dm.UploadFileToSimManagerVault(
                    selected_import_file, "Import", "importFile", "Project"
                )
                print(ret_vault_id)


            if __name__ == "__main__":
                main()


    """


def GetObjectTypeFromAnsaKeyword(keyword: str, dm_root: str) -> str:
    """

    This function returns the DM object type of dm_root that corresponds to the input ANSA keyword.
    If dm_root is not defined, the current DM root is used.

    Parameters
    ----------
    keyword : str
            The input ANSA keyword.

    dm_root : str, optional
            When this argument is given, then that DM will be used.
            Otherwise, the current DM root is used.

    Returns
    -------
    str
            Returns the DM object type. If no object type is found, it returns None.

    See Also
    --------
    dm.GetAnsaKeywordFromObjectType

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                ansa_keyword = "ANSAPART"
                dm_object = dm.GetObjectTypeFromAnsaKeyword(ansa_keyword)
                print("The returned dm_object is: " + dm_object)

                ansa_keyword = dm.GetAnsaKeywordFromObjectType(dm_object)
                print("The returned ansa_keyword is: " + ansa_keyword)


    """


def GetAnsaKeywordFromObjectType(type: str, dm_root: str) -> str:
    """

    This function returns the ANSA keyword that corresponds to the input DM object type of dm_root.
    If dm_root is not defined, the current DM root is used.

    Parameters
    ----------
    type : str
            The input DM object type.

    dm_root : str, optional
            When this argument is given, then that DM will be used.
            Otherwise, the current DM root is used.

    Returns
    -------
    str
            Returns the ANSA keyword. If no ANSA keyword is found, it returns None.

    See Also
    --------
    dm.GetObjectTypeFromAnsaKeyword

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                ansa_keyword = "ANSAPART"
                dm_object = dm.GetObjectTypeFromAnsaKeyword(ansa_keyword)
                print("The returned dm_object is: " + dm_object)

                ansa_keyword = dm.GetAnsaKeywordFromObjectType(dm_object)
                print("The returned ansa_keyword is: " + ansa_keyword)


    """


def GetDMReferences(
    server_id: str,
    ref_server_id: str,
    ref_type: str,
    find_sim_runs_through_contents: bool = False,
) -> object:
    """

    This function queries the DM for all references that satisfy certain criteria.
    Each of the 4 optional arguments provides a filtering criterion:
    * server_id
      Server ID of the object doing the referring (reference source). This argument
      defines the object that is using some other objects.
    * ref_server_id
      Server ID of the object being referred-to (reference target). This argument
      defines the object that is being used by some other objects.
    * ref_type
      Reference type
    * find_sim_runs_through_contents
      Flag indicating whether Simulation Runs' history references
      based on its contents should be searched.

    When multiple arguments are provided, then the corresponding criteria are
    combined with an AND logical operator.

    Parameters
    ----------
    server_id : str, optional
            When present, the DM References query will
            search for references that originate from
            the object with this specific Server ID
            (Object is user)

    ref_server_id : str, optional
            When present, the DM References query will
            search for references that point to the
            object with this specific Server ID.
            (Object is being used)

    ref_type : str, optional
            When present, the DM References query will
            search for references of the specific type.

    find_sim_runs_through_contents : bool, optional
            When True, if the Server ID refers to a Simulation Run,
            the DM References query will search for references of
            history type based on the contained Simulation Model
            and Loadcase.

    Returns
    -------
    object
            Returns the list of DMReferences that satisfy the provided criteria

    See Also
    --------
    dm.DMReference, dm.RemoveDMReference

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def removeStrongReferences():
                # Remove all manually added strong references
                strong_refs = dm.GetDMReferences(ref_type="strong")
                for ref in strong_refs:
                    print(
                        "Removing strong reference from {} to {}".format(
                            ref.server_id, ref.ref_server_id
                        )
                    )
                    dm.RemoveDMReference(ref)


            def getPreviousDMO(dmo_server_id):
                # Get the previous DM Object that have a history link with the current one
                # (Current DM Object with Id = dmo_server_id, was created based on this)

                dmo = dm.DMObject(server_id=dmo_server_id)
                if not dmo.is_valid():
                    print(
                        "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
                    )
                    return None

                refs = dm.GetDMReferences(server_id=dmo_server_id, ref_type="history")

                for ref in refs:
                    print("Current DM Object Id: ", ref.server_id)
                    print("Previous DM Object Id: ", ref.ref_server_id)


            def getNextDMOs(dmo_server_id):
                # Get the next DM Objects that have a history link with the current one
                # (DM Objects that were created from the DM Object with Id = dmo_server_id)

                dmo = dm.DMObject(server_id=dmo_server_id)
                if not dmo.is_valid():
                    print(
                        "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
                    )
                    return None

                refs = dm.GetDMReferences(ref_server_id=dmo_server_id, ref_type="history")

                for ref in refs:
                    print("Current DM Object Id: ", ref.server_id)
                    print("Next DM Object Id(s): ", ref.ref_server_id)


            def getRunAncestors(dmo_server_id):
                # Get the previous Sim Run that have a history link with the current one,
                # searching through the contents of the current Sim Run (Sim Model, Loadcase)
                # (Current Sim Run with Id = dmo_server_id, was created based on this)
                dmo = dm.DMObject(server_id=dmo_server_id)
                if not dmo.is_valid():
                    print(
                        "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
                    )
                    return None

                refs = dm.GetDMReferences(
                    server_id=dmo_server_id, ref_type="history", find_sim_runs_through_contents=True
                )
                for ref in refs:
                    print("Current Sim Run Id: ", ref.server_id)
                    print("Previous Sim Run Id: ", ref.ref_server_id)


            def getSolverFileTypeSubs(dmo_server_id):
                # Get the Solver File Type Subsystems
                # that were produced from Subsystem with ANSA File Type
                sub = dm.DMObject(server_id=dmo_server_id)
                if not sub.is_valid():
                    print(
                        "Invalid server Id or DM Object with Id %s does not exist!" % dmo_server_id
                    )
                    return None

                refs = dm.GetDMReferences(ref_server_id=dmo_server_id, ref_type="repr_derivation")
                for ref in refs:
                    print("Current Subsystem Id: ", ref.ref_server_id)
                    print("Subsystem with Solver File Type Id: ", ref.server_id)


    """


def RemoveDMReference(reference: object) -> bool:
    """

    This function deletes a Reference from the DM

    Parameters
    ----------
    reference : object
            DMReference object, describing the reference to be removed

    Returns
    -------
    bool
            Returns True when the removal operation was successful, regardless of whether an
            actual reference existed / got deleted from the DM or not. It is certain though
            that such a reference no longer exists.

    See Also
    --------
    dm.DMReference, dm.GetDMReferences

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Remove all manually added strong references
                strong_refs = dm.GetDMReferences(ref_type="strong")
                for ref in strong_refs:
                    print(
                        "Removing strong reference from {} to {}".format(
                            ref.server_id, ref.ref_server_id
                        )
                    )
                    dm.RemoveDMReference(ref)


    """


def AddClusterMember(path: str, nickname: str) -> bool:
    """

    This function inserts a new, read only member into the currently configured
    Cluster DM.

    Parameters
    ----------
    path : str
            DM Root of the DM that will be backing the new
            cluster member.

    nickname : str, optional
            String to be used as nickname for the new
            cluster member. May contain the latin letters,
            digits, the underscore and dash characters.
            If this argument is not provided, the new
            cluster member's nickname will be auto generated
            from the path argument.

    Returns
    -------
    bool
            Returns True if the new member was successfully admitted into the cluster.

    See Also
    --------
    dm.DMClusterMember, dm.GetClusterMembers, dm.RemoveClusterMember

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("cluster://home/user/DMs/main/")
                dm.AddClusterMember("/home/user/DMs/library/rlis/")
                dm.AddClusterMember("/home/user/DMs/library/subsystems/", "subs")


    """


def GetClusterMembers() -> object:
    """

    This function fetches information about all the cluster members existing in the
    currently configured Cluster DM.

    Returns
    -------
    object
            Returns all cluster members as a list of DMClusterMember objects.

    See Also
    --------
    dm.AddClusterMember, dm.DMClusterMember

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def getFlagsString(flags):
                flags_strings = []

                # Iterate through all defined flags even though all combinations are not
                # possible, e.g. a member cannot be both Primary and Read Only.
                if flags & dm.constants.PRIMARY_MEMBER:
                    flags_strings.append("Primary")
                if flags & dm.constants.READ_ONLY_MEMBER:
                    flags_strings.append("Read Only")
                return ", ".join(flags_strings)


            def main():
                # A Cluster DM is configured as current DM Root
                members = dm.GetClusterMembers()
                for member in members:
                    print("Path      :", member.path)
                    print("Nickname  :", member.nickname)
                    print("Identifier:", member.identifier)
                    print("Flags     :", getFlagsString(member.flags))


    """


def RemoveClusterMember(path: str) -> bool:
    """

    This function removes an existing, read only member from the currently
    configured Cluster DM, provided that there are no cluster level dependencies on
    it.

    Parameters
    ----------
    path : str
            DM Root of the cluster member to be removed.

    Returns
    -------
    bool
            Returns True if the member was successfully removed from the cluster.

    See Also
    --------
    dm.DMClusterMember, dm.AddClusterMember, dm.GetClusterMembers

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                dm.SetRoot("cluster://home/user/DMs/main/")
                dm.RemoveClusterMember("/home/user/DMs/library/rlis/")


    """


def GetConnectedUserRole() -> str:
    """

    Get the current role of the user who is connected to SPDRM-based DM root.

    Returns
    -------
    str
            Returns the User Role.
            None is returned in case of error (e.g. the user is not connected to DM root).

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            dm.SetRoot(
                "http://spdrm:8080/", username="analyst_01", password="analyst_01", role="Analyst"
            )
            print("The current role of the connected user is ", dm.GetConnectedUserRole())


    """


def GetUserRoles(dm_root: str, username: str, password: str) -> object:
    """

    Get the available roles of a user in an SPDRM-based DM root.

    Parameters
    ----------
    dm_root : str
            The url of the SPDRM-based DM root.

    username : str
            The username of the user.

    password : str
            The password of the user.

    Returns
    -------
    object
            Returns a list with the available user roles.
            None is returned in case of error.

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            user_roles = dm.GetUserRoles("http://spdrm:40080", "user_01", "user_01")
            print("The available roles are:")
            for role in user_roles:
                print(role)


    """


def InitializeDMForDOE(dm_root: str) -> bool:
    """

    This function initializes the Filebased DM with the necessary Properties
    and Attributes for use with DOE.
    It will only update the DM when it's empty.

    Parameters
    ----------
    dm_root : str, optional
            The function works on the current DM, unless this
            argument is specified.

    Returns
    -------
    bool
            False when the DM isn't empty.
            True if the DM is empty and the initialization is successful.

    Examples
    --------
    ::

            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            def main():
                if module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                print(dm.InitializeDMForDOE())


    """


def GetTicket(dm_root: str) -> str:
    """

    This function returns the authentication ticket that is currently being used in
    a connection to a remote, web based DM (SPDRM or SimManager).

    Parameters
    ----------
    dm_root : str, optional
            The URL of the remote, web based DM. If this argument
            is not provided, the Current DM Root will be used.

    Returns
    -------
    str
            Returns the authentication ticket as a string.

    See Also
    --------
    dm.SetRoot

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def amin():
                dm.SetRoot("http://magneto.localdomain:8080/", username="user1", password="pass1")
                ticket = dm.GetTicket()
                print("Ticket used in Current DM Connection:", ticket)


    """


def GetFeatureItemTypes(dm_root: str) -> object:
    """

    This function returns a list containing the names of all the Feature Item types
    that can exist for the DM.

    Parameters
    ----------
    dm_root : str, optional
            When this argument is given, then that DM will
            be used. Otherwise, the current DM root is used.

    Returns
    -------
    object
            Returns a list containing strings.
            An empty list is returned if no Feature Item types are defined.
            If an error occurs, None is returned.

    See Also
    --------
    dm.GetLibraryItemTypes

    Examples
    --------
    ::

            # PYTHON script
            import ansa
            from ansa import dm

            print(dm.GetFeatureItemTypes())
            print(dm.GetFeatureItemTypes(dm_root="C:/test/"))


    """


def GetMultiDMReferences(
    server_ids: object, ref_types: object, recursive: bool, returned_ents: int
) -> object:
    """

    This function queries the DM for all references that involve multiple Server IDs
    and for possibly multiple reference types. The query can be recursive and it is
    user selectable whether the query should search for the objects being used or
    are using the Server IDs provided as arguments

    Parameters
    ----------
    server_ids : object
            Sequence of strings, holding the Server IDs for
            which references will be queried.

    ref_types : object, optional
            Sequence of strings, holding the Reference Types
            for which reference will be queried. If empty,
            then all types of references will be returned.
            Default value: Empty list

    recursive : bool, optional
            This value defines whether references should be
            recursively queried, using the provided server ids
            as starting points.
            Default value: False

    returned_ents : int, optional
            This value defines whether references originating
            from or terminating into the provided Server IDs
            should be queried.
            Default value: dm.constants.DM_REF_FROM

    Returns
    -------
    object
            Returns the list of DMReferences that satisfy the provided criteria

    See Also
    --------
    dm.DMReference, dm.GetDMReferences

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            server_ids = ["main:6", "lib:3"]
            ref_types = ["history"]
            refs = dm.GetMultiDMReferences(
                server_ids, ref_types, returned_ents=dm.constants.DM_REF_FROM, recursive=True
            )

            for ref in refs:
                print(ref)


    """


def RebuildFromDisk(dm_root: str) -> bool:
    """

    The DM's database file is updated by scanning the DM directory contents.

    Parameters
    ----------
    dm_root : str, optional
            The function works on the current DM, unless this
            argument is specified.

    Returns
    -------
    bool
            False when the DM isn't Filebased.
            True if the DM is Filebased.

    Examples
    --------
    ::

            def module_exists(module_name):
                try:
                    __import__(module_name)
                except ImportError:
                    return False
                else:
                    return True


            def main():
                if module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                elif module_exists("ansa"):
                    import ansa
                    from ansa import dm
                print(dm.RebuildFromDisk())


    """


def IsIntermodularConnectivityLinksFeatureSupported() -> bool:
    """

    The function is used to check if intermodular_connectivity_links
    feature is supported by current DM schema.

    Returns
    -------
    bool
            Returns True if feature is supported, or False if not supported.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                if dm.IsIntermodularConnectivityLinksFeatureSupported():
                    print("Feature supported.")
                else:
                    print("Feature not supported.")


    """


def QueryDMTypes(rich_library_items: bool, feature_items: bool) -> object:
    """

    Collect all object types that exist in DM.
    Only the DM Schema types are returned unless the optional arguments are specified,
    in which case Rich Library Items or Feature Items will also be returned
    (if found).

    Parameters
    ----------
    rich_library_items : bool, optional
            Optional boolean argument to determine if Rich Library Items will also be returned.

    feature_items : bool, optional
            Optional boolean argument to determine if Feature Items will also be returned.

    Returns
    -------
    object
            Returns a list containing the found object types.
            None is returned when the DM is not properly initialized.

    See Also
    --------
    GetDMSchemaTypes

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            # only get the DM Schema types:
            print(dm.QueryDMTypes())

            # return also Rich Library Items and Feature Items:
            print(dm.QueryDMTypes(rich_library_items=True, feature_items=True))


    """


def GetDMSchemaTypes(dm_root: str) -> object:
    """

    Collect all the DM Schema object types that can exist for the DM.

    Parameters
    ----------
    dm_root : str, optional
            When this argument is given, then that DM will be used.
            Otherwise, the current DM root is used.

    Returns
    -------
    object
            Returns a list containing the object types.
            If something goes wrong, None is returned.
            Example return values:

            ['parts', 'includes', 'configurations', 'Subsystems', 'Simulation_Model', 'LoadCase', 'Simulation_Run', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'Report']
            ['parts', 'includes', 'configurations', 'Simulation_Model', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'Component', 'Run', 'Loadcase', 'Report']
            ['parts', 'includes', 'configurations', 'Subsystems', 'Simulation_Model', 'LoadCase', 'Simulation_Run', 'Session', 'Changeset', 'Predictor', 'Optimization_Study', 'Modular_Environment_Profile', 'CAE_Top_Node', 'Input_Deck', 'Report']

    See Also
    --------
    GetFeatureItemTypes, GetLibraryItemTypes

    Examples
    --------
    ::

            # PYTHON script
            import ansa
            from ansa import dm

            print(dm.GetDMSchemaTypes())
            print(dm.GetDMSchemaTypes(dm_root="C:/test/"))


    """


def GetLastErrorMessage() -> str:
    """

    Returns the last error message from DM operations.

    Returns
    -------
    str
            Returns a string containing the last error message.
            An empty string is returned when no error exists.

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            print(dm.GetLastErrorMessage())


    """


def CollectAllSimRunPreviousHistoryLinks_dbg(server_id: str) -> object:
    """
    .. deprecated:: 23.0.0
            Use `GetDMReferencesForSimRun_WholePath` instead.


    This function queries the DM for all previous history links of a simulation run.

    Given the server_id of a simulation run it returns a list of all the previous
    history DMReferences.

    Parameters
    ----------
    server_id : str
            The server_id of a simulation run

    Returns
    -------
    object
            Returns a list of DMReferences.

            If the are no references for a server_id, an empty list is returned.
            If an error occurs, None is returned.

    See Also
    --------
    dm.DMReference, dm.GetDMReferences, dm.RemoveDMReference

    Examples
    --------
    ::

            # PYTHON script
            import os
            import ansa

            references = ansa.dm.CollectAllSimRunPreviousHistoryLinks_dbg("1")
            for ref in references:
                print(
                    "The previous {} link of {} is: {}".format(
                        ref.ref_type, ref.ref_server_id, ref.server_id
                    )
                )


    """

    import warnings

    warnings.warn(
        "Deprecated since version 23.0.0. Use  GetDMReferencesForSimRun_WholePath instead.",
        DeprecationWarning,
    )


def GetConnectionStatus() -> int:
    """

    The function performs a ping operation on the connected SPDRM DM.
    A valid SPDRM DM root should have been specified first.

    Returns
    -------
    int
            Returns the ping value in milliseconds on success or an exception on error.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                ping_val = dm.GetConnectionStatus()
                print(ping_val)


    """


class DMObject:
    """

    A class that handles communication with DM and functionality regarding Objects in DM.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                new_dict = {
                    "Module Id": "981483828A",
                    "Version": "R1114567893_---",
                    "Study Version": "0",
                    "File Type": "ANSA",
                    "Representation": "CRASH",
                }
                new_object = dm.DMObject(names_values=new_dict, type="parts")
                print(new_object.server_id)


            # method: add_new
            import ansa
            from ansa import dm


            def main():
                # add_new (with a Representation File):
                names_values = {
                    "Module Id": "Module1",
                    "Study Version": "0",
                    "Representation": "Representation1",
                    "Name": "Name1",
                    "File Type": "Nastran",
                    "Project": "Project1",
                    "Release": "Rel1",
                    "Variant": "Var1",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_server_id = new_object.add_new(
                    filename="C:/home/demo/tmp/representation_file.nas"
                )
                if new_server_id:
                    print("New server_id: ", new_server_id)
                else:
                    print("add_new failed.")
                # add_new (with no Representation File):
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_server_id = new_object.add_new()
                if new_server_id:
                    print("New server_id: ", new_server_id)
                else:
                    print("add_new failed.")


            # method: connect
            import ansa
            from ansa import dm


            def main():
                dict2 = {
                    "Module Id": "Module1",
                    "Version": "Version1",
                    "Study Version": "0",
                    "Representation": "Representation1",
                    "Variant": "Variant1",
                    "Name": "Name1",
                }
                object2 = dm.DMObject(names_values=dict2, type="Subsystems")
                print(object2.connect({object2.server_id: "my_component"}))

                part1 = dm.DMObject(server_id="1057023", type="parts")
                part2 = dm.DMObject(server_id="1057026", type="parts")
                print(part2.connect({part1.server_id: "strict"}))


            # method: export
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_object.export("C:/home/demo/tmp")
                new_object.export("C:/home/demo/tmp", export_type="hierarchy")


            # method: get_all_values
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                values = new_object.get_all_values()
                print(values)


            # method: get_attribute_values
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_object.set_attribute_values(
                    attributes_values={"TEST": "New_Val", "TEST_NUM": "23.43"},
                    attributes_types={"TEST_NUM": "DOUBLE"},
                )
                print(new_object.get_attribute_values(attributes=["TEST", "TEST_NUM"]))


            # method: get_conflict_options
            import ansa
            from ansa import dm


            def main():
                new_dict1 = {
                    "Module Id": "PCANSAWIN7_8580_12",
                    "Version": "A1",
                    "Representation": "Connections",
                    "Project": "Training",
                    "Phase": "BBG",
                }
                new_object1 = dm.DMObject(names_values=new_dict1, type="parts")
                print(new_object1.get_conflict_options())

                new_dict2 = {
                    "Module Id": "PCANSAWIN7_8580_13",
                    "Version": "A1",
                    "Representation": "Connections",
                    "Project": "Training",
                    "Phase": "BBG",
                }
                new_object2 = dm.DMObject(names_values=new_dict2, type="parts")
                print(new_object2.get_conflict_options())

                # For conflicts with a partially deleted Object in SPDRM:
                new_vals = {
                    "Project": "BJA",
                    "File": "32_FR_LH_DOOR_BJA_ABCP_DELETED__001_001",
                    "Milestone": "ABCP",
                    "Representation_Version": "001",
                    "Representation": "DMU",
                    "File Type": "PamCrash",
                    "Study_Version": "001",
                    "Diversity": "DELETED",
                    "Purpose": "MODEL",
                    "Module Id": "32_FR_LH_DOOR",
                    "Loadcase Diversity": "-",
                }
                new_vals["Representation_Version"] = "001"
                obj = dm.DMObject(names_values=new_vals, type="Module")
                print("Partially deleted")
                print(obj.server_id)
                if not obj.server_id:
                    print(obj.ghost_id)
                    if obj.ghost_id:
                        obj = dm.DMObject(server_id=obj.ghost_id, type="Module")
                        print(obj.get_conflict_options())


            # method: get_contained_objects
            import ansa
            from ansa import dm


            def main():
                object = dm.DMObject(server_id="1082", type="Simulation_Run")
                print(str(object.get_contained_objects("Report")))
                object = dm.DMObject(server_id="2270", type="Simulation_Model")
                print(str(object.get_contained_objects("Report")))
                print(str(object.get_contained_objects("Simulation_Run")))


            # method: get_contents
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                contents = new_object.get_contents()
                print(contents)


            # method: get_references
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                ref = new_object.get_references(2)
                print(ref)


            # method: get_representation_file
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                rf = new_object.get_representation_file()
                print(rf)


            # method: get_type
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                type = new_object.get_type()
                print(type)


            # method: remove
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_object.remove()
                new_object.remove("YES")


            # method: set_attribute_values
            import ansa
            from ansa import dm


            def main():
                names_values = {
                    "Module Id": "Module2",
                    "Study Version": "0",
                    "Representation": "Representation2",
                    "Name": "Name2",
                    "File Type": "Nastran",
                    "Project": "Project2",
                    "Release": "Rel2",
                    "Variant": "Var2",
                    "Discipline": "Crash",
                }
                new_object = dm.DMObject(names_values=names_values, type="Subsystems")
                new_object.set_attribute_values(
                    attributes_values={"TEST": "New_Val", "TEST_NUM": "23.43"},
                    attributes_types={"TEST_NUM": "DOUBLE"},
                )
                print(new_object.get_attribute_values(attributes=["TEST", "TEST_NUM"]))


            # method: get_attachment_values
            import ansa
            from ansa import dm


            def main():
                simulation_model = dm.DMObject(server_id="7", type="Simulation_Model")
                attachments = simulation_model.get_attachment_values()


            if __name__ == "__main__":
                main()
            # method: is_valid
            import ansa

            dmobj = ansa.dm.DMObject(server_id="6", type="Subsystem")
            print(dmobj.is_valid())

    """

    names_values: object = None
    """
	A dictionary with DM Properties that completely defines the Object.
	It needs the Object type as well.

	"""

    type: str = None
    """
	The type of the DM Object. The specified type can be ANSA type
	(e.g. ANSA_LOADCASE) or the DM type defined through the Data
	Model (e.g. Loadcase). Required when creating an Object with
	specified "names_values".

	"""

    server_id: str = None
    """
	The Object's server id, its unique id in DM.
	If the value is empty, should the script ask for it, the DM will be queried for the 
	"names_values" and retrieve the value.

	"""

    ghost_id: str = None
    """
	When an Object is partially deleted, the server_id is None
	and the ghost_id has the Id.
	The ghost_id can be used to create a new DMObject and get
	conflict options for saving it in DM.
	When the Object doesn't exist, both the server_id and 
	ghost_id are None.
	When the Object exists, the ghost_id will be equal to
	the server_id.

	"""

    @classmethod
    def export(
        cls,
        output_directory: str,
        export_type: str,
        child_server_id: str,
        hierarchy: str,
        action: str,
        export_contents: bool,
    ) -> str:
        """

        Download the Object's Representation File or hierarchy to a XML file.


        Parameters
        ----------
        output_directory : str
                Specify where the file/files will be downloaded.

        export_type : str, optional
                Accepted values: "hierarchy", "sub_hierarchy", blank.
                When this argument is omitted, the Representation File(s)
                will be exported.
                When the argument is "hierarchy", an XML file with the Object's
                hierarchy will be exported.
                When the argument is "sub_hierarchy", an XML file with
                a subhierarchy will be exported.
                It is used along with the "child_server_id" and "hierarchy"
                arguments.

        child_server_id : str, optional
                The child server id whose subhierarchy will be exported.
                It is used along with the 'hierarchy' argument.

        hierarchy : str, optional
                The "Hierarchy" value for the child whose subhierarchy will be
                exported. It is used along with the 'child_server_id' argument.

        action : str, optional
                The exported file from the server will be copied to the target directory by default.
                It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory.
                Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items.

        export_contents : bool, optional
                Define whether the DM item's contents will be included while exporting. The default value is retrieved from the "dm_export_include_contents" keyword in ANSA Settings (by default it is set True).

        Returns
        -------
        str
                The resulting directory is returned on success.

        """

    @classmethod
    def remove(cls, only_representation_file: str) -> int:
        """

        Delete the Object from DM.


        Parameters
        ----------
        only_representation_file : str, optional
                Use "YES" when only the Representation File should be
                deleted and the Object should be kept in the database.

        Returns
        -------
        int
                1 if the function was successful.0 for failure.

        """

    @classmethod
    def set_attribute_values(
        cls, attributes_values: object, attributes_types: object
    ) -> bool:
        """

        This function can change Attribute values for the Object.


        Parameters
        ----------
        attributes_values : object
                A dictionary which specifies the Attributes to change,
                in a names-values format.

        attributes_types : object, optional
                A dictionary mapping attribute names to types. This
                information will be used in case new attributes will be
                created and the DM supports typed attributes.

        Returns
        -------
        bool
                True : If the at least one values was set successfully.False: If the function failed to set any value.

        """

    @classmethod
    def get_attribute_values(cls, attributes: object) -> object:
        """

        This function can return some specified Attribute values of a Object.


        Parameters
        ----------
        attributes : object, optional
                A list in which the user can specify Attribute names,
                for their values to be returned. If this arguments is not
                present, all the object's values will be returned.

        Returns
        -------
        object
                If the object was found, a dictionary will be returned with the specified attribute values.If the function fails, "None" will be returned.

        """

    @classmethod
    def get_all_values(cls) -> object:
        """

        This function will return all the Properties and Attributes for the Object in the form of a dictionary.


        Returns
        -------
        object
                A list with a dictionary for the Object that is actually found in DM.

        """

    @classmethod
    def connect(cls, references: object) -> bool:
        """

        This function connects DM Objects, by referencing. After its execution,the Object will reference the Objects specified in the "references" dict.Remarks:The "reference_type" values specified in the "references" dict can be any arbitrary string. However, when using SPDRM v1.4.0 or later as the data management backbone, certain values are reserved and can be used only when the conditions below are satisfied:-- adaptation      : Input/Output dependency link between a Loadcase Template (RLI) and a Loadcase (DM Item).-- creation        : Input/Output dependency link between a Session and a Report.-- repr_derivation : Lifecycle generic link between DM Items with identical properties, apart from the File Type (e.g ANSA and NASTRAN). At least one should have File Type = ANSA.                     Moreover, the following values are reserved for system generated links and should not be used as "reference_type":-- history         : System lifecycle link for DM Items of same type with different versioning properties and identical non-versioning ones.-- changeset       : System link between a changeset and a DM Item when saving a changeset from ANSA


        Parameters
        ----------
        references : object
                A dictionary which holds server_id->reference-type pairs.
                Please see the REMARKS section for more information on the "reference_type" accepted values.

        Returns
        -------
        bool
                True : If the new references were made successfully.False: If the function failed to make one of the connections.

        """

    @classmethod
    def add_new(
        cls,
        overwrite: bool,
        link: bool,
        get_repr_file_siblings: bool,
        filename: str,
        spin_up_attribute: str,
    ) -> object:
        """

        This function adds an Object to DM, if it does not already exist.


        Parameters
        ----------
        overwrite : bool, optional
                Set to True if the object should be overwritten if it
                already exists in the DM. (Default: False)

        link : bool, optional
                Set to True if you wish create a link to the file that
                corresponds to the object. (Default: False)

        get_repr_file_siblings : bool, optional
                Set to True if you wish to copy along all files that exist
                in the same directory as the representation file.
                Applicable for Subsystems, Simulation Models, Load
                Cases and Simulation Runs, when a non-ANSA file
                is set as representation file.
                (Default: False)

        filename : str, optional
                When the data model doesn't specify a "File" Property/Attribute for the Object, a Representation File can be added using this argument.
                For example, when adding a Subsystem to a Filebased DM, the file will be stored in DM by adding a filename to this method.

        spin_up_attribute : str, optional
                The primary attribute to spin-up. The 'overwrite' attribute should be set to False. By default, the 'spin_up_attribute' is not specified and the 'overwrite' = False, which means that the process will be skipped if the object already exists in DM.

        Returns
        -------
        object
                None: If an error occured.server_id string: If the object was successfully saved.

        """

    @classmethod
    def get_representation_file(cls) -> str:
        """

        This function will return the absolute file path to the DMObject's Representation File. In case of a server-based DM, e.g. SPDRM, SimManager,the file will be downloaded locally, to a temporary location, only the first time it is asked for. All following calls to the function will return the same file path, so long as the DMObject isn't updated. The temporary files deletion is handled automatically.


        Returns
        -------
        str
                If the Representation File exists and is successfully found, it's absolute file path will be returned.Otherwise, "None" will be returned.

        """

    @classmethod
    def get_conflict_options(cls) -> object:
        """

        When trying to upload an object to DM, one can get the conflict options when the object already exists in DM.


        Returns
        -------
        object
                Returns a list with the available conflict options, only if the object already exists in DM.Otherwise, it returns None.

        """

    def get_contained_objects(self, type: str) -> object:
        """

        This function will query DM and collect all Objects of the specified type contained under this DM Object.


        Parameters
        ----------
        type : str
                The type of the DM Object that will be queried for. The specified type can be ANSA type (e.g. ANSA_LOADCASE) or the DM type defined through the Data Model (e.g. Loadcase).

        Returns
        -------
        object
                Return a list of DMObject objects.

        """

    def set_contents(self, server_ids: object) -> bool:
        """

        This function sets the contents of the object (e.g. the Subsytems belonging to a Simulation Model).


        Parameters
        ----------
        server_ids : object
                The server ids identifying the objects to be set as contents.

        Returns
        -------
        bool
                True : If the object contents were set successfully. False : If the object contents couldn't be set.

        """

    def get_contents(self) -> object:
        """

        Get the list of objects that are contents of the object


        Returns
        -------
        object
                Returns the server ids of the object contents

        """

    def get_references(
        self, returned_ents: int = 0, find_sim_runs_through_contents: bool = False
    ) -> object:
        """

        Get the objects which:- use this DM Object,- are used by this DM Object,- use and are used by this DM Object.


        Parameters
        ----------
        returned_ents : int, optional
                define the requested objects:
                0 to get the objects which use this DM Object,
                1 to get the objects which are used by this DM Object,
                2 to get the objects which use and are used by this DM Object.
                By default, the objects, which use this DM Object, are returned.

        find_sim_runs_through_contents : bool, optional
                When True, if the DM Object is a Simulation Run,
                search for references of history type based
                on the contained Simulation Model and Loadcase.

        Returns
        -------
        object
                Returns a list with the requested objects.

        """

    @classmethod
    def get_type(cls) -> str:
        """

        Use this method to query DM for the DMObject's type.


        Returns
        -------
        str

        """

    @classmethod
    def download_attachment(
        cls,
        output_folder: str,
        folder_name: str,
        subfolder_name: str,
        filename: str,
        attribute_name: str,
        action: str,
    ) -> str:
        """

        Downloads an attached file/folder of the DMObject.


        Parameters
        ----------
        output_folder : str
                the full path of the folder where the attachment will be downloaded.

        folder_name : str, optional
                the name of the folder which contains the attachment.

        subfolder_name : str, optional
                the name of the sub-folder to be downloaded.

        filename : str, optional
                the name of the file to be downloaded.

        attribute_name : str, optional
                the name of attribute which contains the attachment.

        action : str, optional
                The exported file from the server will be copied to the target directory by default.
                It is possible to create a hard link in the target directory when this argument has the value "link" and the output_folder is relative to the NodeExec directory.
                Note that this is only possible when connected to a SPDRM DM and the application is launched through a Process Node and works for Subsystems, parts, Rich Library Items.

        Returns
        -------
        str
                Returns the full path of the downloaded attachment on success and None on failure.

        """

    @classmethod
    def get_attachment_values(cls) -> object:
        """

        In case of Filebased DMs, this function returns absolute paths for attachments that aren't declared in the data model and will not be returned by dm.DMObject.get_all_values. In case of SPDRM, this function may return absolute or relative paths for these attachments, depending on SPDRM configuration.


        Returns
        -------
        object
                Returns a dictionary with the attribute name as the key and the absolute file path as the value.

        """

    @classmethod
    def is_valid(cls) -> bool:
        """

        Use this method to check if the DMObject initialized with a server_id is actually valid and existing in DM.


        Returns
        -------
        bool

        """


class DMReference:
    """

    DM objects can refer to other objects within the same DM. Such relationships are
    described by 3 data fields:
    * DM Object that is doing the referring, i.e. is using another object
    * DM Object that is being referred to, i.e. is being used by another object
    * Reference type

    Instances of the DMReference class encapsulate all information needed to
    describe such a reference between DM Objects.

    Based on the reference type, references can be classified as strong / weak:
    Objects cannot be deleted if there are any outstanding strong references
    pointing to them. Weak references on the other hand do not obstruct the deletion
    of the referred-to objects.

    Even though the reference type can be any arbitrary string, there are predefined
    reference types accomodating standard use cases. The predefined reference types
    are:
    * adaptation
      Used for adapted DM objects to point to their standalone counterparts (e.g.
      LoadCases) (strong)
    * creation
      Used for DM objects to point to the DM object that triggered their creation
      (e.g. Reports pointing to the META Session) (strong)
    * history
      Used to show how objects have evolved over time and track their origins:
      recent objects point to their immediate ancestors (weak)
    * repr_derivation
      Used for automatically saved FE representation objects to point to the
      original ANSA representation objects (weak)
    * changeset
      Used for connecting an object in the DM, with the changeset that ordered its
      creation (strong)
    * training
      Used to show how data were used in ML training sessions: the generated
      predictor object points to the Simulation Run objects used during training
      (weak)
    * modular_environment_profile
      Used to show what configuration was used during the save of an object (strong)
    * strong
      Generic strong reference. Recommended for user created references
    * weak
      Generic weak reference. Recommended for user created references

    See Also
    --------
    dm.GetDMReferences, dm.RemoveDMReference

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Remove all manually added strong references
                strong_refs = dm.GetDMReferences(ref_type="strong")
                for ref in strong_refs:
                    print(
                        "Removing strong reference from {} to {}".format(
                            ref.server_id, ref.ref_server_id
                        )
                    )
                    dm.RemoveDMReference(ref)

    """

    server_id: str = None
    """
	Server ID of the object that is doing the referring,
	i.e. using the other object.

	"""

    ref_server_id: str = None
    """
	Server ID of the object that is being referred to
	i.e. is being used by the other object.

	"""

    ref_type: str = None
    """
	Field describing the type of the reference

	"""

    def __init__(self, server_id: str, ref_server_id: str, ref_type: str) -> object:
        """

        DMReference object constructor, initializing all members


        Parameters
        ----------
        server_id : str
                See respective member definition

        ref_server_id : str
                See respective member definition

        ref_type : str
                See respective member definition

        Returns
        -------
        object
                Returns the created DMReference object

        """


class DMClusterMember:
    """

    DMClusterMember objects describe a DM Cluster membership, providing information
    on which the backing DMs are and how they are employed within the cluster.

    See Also
    --------
    dm.AddClusterMember, dm.GetClusterMembers

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def getFlagsString(flags):
                flags_strings = []

                # Iterate through all defined flags even though all combinations are not
                # possible, e.g. a member cannot be both Primary and Read Only.
                if flags & dm.constants.PRIMARY_MEMBER:
                    flags_strings.append("Primary")
                if flags & dm.constants.READ_ONLY_MEMBER:
                    flags_strings.append("Read Only")
                return ", ".join(flags_strings)


            def main():
                # A Cluster DM is configured as current DM Root
                members = dm.GetClusterMembers()
                for member in members:
                    print("Path      :", member.path)
                    print("Nickname  :", member.nickname)
                    print("Identifier:", member.identifier)
                    print("Flags     :", getFlagsString(member.flags))

    """

    path: str = None
    """
	DM Root of the DM that is backing this cluster member.

	"""

    nickname: str = None
    """
	String that will be used to tag DM Object fields (e.g.
	Server IDs, Paths) in order to identify the contributing
	member.
	Can contain latin letters, digits, the underscore and dash
	characters.

	"""

    identifier: str = None
    """
	String that is fetched from the member DM the first time
	it is admitted into the cluster. Used to validate
	subsequent insertions of the DM into the cluster.

	"""

    flags: int = None
    """
	Bitfield describing properties of the cluster member. The
	supported flags are defined as constants:
	* dm.PRIMARY_MEMBER
	  This member is the primary one for the cluster (i.e.
	  used for both reading / writing)
	* dm.READ_ONLY_MEMBER
	  This member is used only for reading

	"""

    def __init__(self, path: str, nickname: str, identifier: str, flags: int) -> object:
        """

        DMClusterMember object constructor, initializing all members


        Parameters
        ----------
        path : str
                See respective member definition

        nickname : str
                See respective member definition

        identifier : str
                See respective member definition

        flags : int
                See respective member definition

        Returns
        -------
        object
                Returns the created DMClusterMember object

        """


def RefreshContents() -> None:
    """

    Refresh the side panel in DM Browser or KOMVOS,
    equivalent to the right click action "Refresh".

    Returns
    -------
    None

    Examples
    --------
    ::

            import ansa
            from ansa import dm

            dm.RefreshContents()


    """


class DMFilter:
    """

    A DMFilter object represents a query in DM for DM Objects of a specified type that fulfill a condition.
    The execution of a DM Filter results a list of DM Objects.

    See Also
    --------
    dm.GetDMFilters

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                # Create
                filter = dm.DMFilter(name="MyFilter", object_type="Subsystems")

                # Edit
                filter.name = "FirstIteration"
                filter.expression = "Iteration=001"

                # Save in DM
                filter.save()

                # Execute
                res = filter.exec()

                # Delete
                filter.delete()

                # Check existence in DM##
                filter.exists()

    """

    id: int = None
    """
	Id of the filter. (Read only)

	"""

    name: str = None
    """
	Name of the filter.

	"""

    user: str = None
    """
	The user that created the filter. (Read only)

	"""

    object_type: str = None
    """
	The type of the DM Objects to be queried.

	"""

    secondary_type: str = None
    """
	The secondary type of the DM Objects to be queried.

	"""

    expression: str = None
    """
	The condition expression the query must fulfill.

	"""

    description: str = None
    """
	The user-specified description over the filter.

	"""

    mode: int = None
    """
	DM FIlter's mode.
	  - Basic
	  - Advanced (default)

	"""

    syntax: int = None
    """
	DM FIlter's syntax.
	  - BetaQL
	  - FreeText (default)

	"""

    access: int = None
    """
	DM Filter's access from users.
	  - Private (default)
	  - ViewOnly
	  - ViewAndEdit

	"""

    creation_date: datetime = None
    """
	DM Filter's creation datetime. (Read only)

	"""

    modification_date: datetime = None
    """
	DM Filter's modification datetime. (Read only)

	"""

    last_edit_user: str = None
    """
	The last user who edited the DM Filter. (Read only)

	"""

    def __init__(self, name: str, object_type: str, secondary_type: str) -> object:
        """

        DMFilter object constructor, initializing all members


        Parameters
        ----------
        name : str
                See respective member definition

        object_type : str
                See respective member definition

        secondary_type : str, optional
                See respective member definition

        Returns
        -------
        object
                Returns the created DMFilter object

        """


def GetDMFilters(owned_only: bool = False) -> list:
    """

    This function queries the DM for either all non-private filters or only those that are created by the user.

    Parameters
    ----------
    owned_only : bool, optional
            If True, get only the DM Filters that are created by the user.

    Returns
    -------
    list
            Returns the list of DMFilter items that satisfy the provided expression.

    See Also
    --------
    dm.DMFilter

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def getOwnedOnlyDMFilters():
                dm_filters_list = dm.GetDMFilters(owned_only=True)
                for dm_filter in dm_filters_list:
                    print(dm_filter)


    """


def CreateTempFolder(folder_name: str) -> str:
    """

    The function creates a temporary folder in the user temp directory.
    The folder is deleted upon program exit.

    Parameters
    ----------
    folder_name : str
            A secondary folder to be created nested inside the temporary folder.

    Returns
    -------
    str
            Returns the path to the created folder on success, or an exception on error.

    Examples
    --------
    ::

            import ansa
            from ansa import dm


            def main():
                first_temp_folder = dm.CreateTempFolder()
                second_temp_folder = dm.CreateTempFolder("my_second_test_dir")

                print("First temp folder is: " + first_temp_folder)
                print("Second temp folder is: " + second_temp_folder)


            if __name__ == "__main__":
                main()


    """


def ActivateLBR(dm_root: str) -> bool:
    """

    Activate the LBR functionality in a given DM, or the current DM. It is used after having used deactivateLBR for that DM root.

    Parameters
    ----------
    dm_root : str, optional
            the DM root that should be activated. If ommitted, the current DM root is used.

    Returns
    -------
    bool
            True if succesful, False if not.

    See Also
    --------
    DeactivateLBR, IsLBRActivated

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def attemptAnLBRViolation():
                dm_filters = [["Status", "equals", "Draft"]]
                # dm_filters =[[]]

                results = dm.QueryDMObjects(type="Module", query=dm_filters)
                print("querying the DM resulted to ", results["error"])
                first_result = None
                if results["error"] == 0:
                    if "output" in results and len(results["output"]) > 0:
                        first_result = results["output"][0]
                else:
                    return
                if first_result != None:
                    result = first_result.set_attribute_values(
                        attributes_values={"Status": "Error"}
                    )
                    print(result)


            def checkLBRActivationStatus(my_dm_root):
                ans1 = dm.IsLBRActivated(dm_root=my_dm_root)
                if ans1:
                    print("LBR is activated")
                else:
                    print("LBR is deactivated")


            def checkLBREnableStatus(my_dm_root):
                ans = dm.IsLBREnabled(dm_root=my_dm_root)
                if ans:
                    print("LBR is enabled")
                else:
                    print("LBR is not enabled")
                return ans


            def checkLBRState(my_dm_root):
                print("-------------------------DM = ", my_dm_root, "-----------------------------")
                ans = checkLBREnableStatus(my_dm_root)

                if ans == False:
                    return

                attemptAnLBRViolation()

                print("Attempting to DEactivate LBR!!!!")
                dm.DeactivateLBR(dm_root=my_dm_root)
                checkLBRActivationStatus(my_dm_root)

                attemptAnLBRViolation()

                print("Attempting to Activate LBR!!!!")
                dm.ActivateLBR(dm_root=my_dm_root)
                checkLBRActivationStatus(my_dm_root)


            def main():
                dm_root = "http://kronos:9080/"
                checkLBRState(dm_root)


    """


def DeactivateLBR(dm_root: str) -> bool:
    """

    Deactivate the LBR functionality in a given DM, or the current DM. It is used so that only the current user in the current session may execute DM operations without LBR restrictions. Must be used with caution.

    Parameters
    ----------
    dm_root : str, optional
            the DM root that should be deactivated. If ommitted, the current DM root is used.

    Returns
    -------
    bool
            True if successful, False if not.

    See Also
    --------
    ActivateLBR, IsLBRActivated

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def attemptAnLBRViolation():
                dm_filters = [["Status", "equals", "Draft"]]
                # dm_filters =[[]]

                results = dm.QueryDMObjects(type="Module", query=dm_filters)
                print("querying the DM resulted to ", results["error"])
                first_result = None
                if results["error"] == 0:
                    if "output" in results and len(results["output"]) > 0:
                        first_result = results["output"][0]
                else:
                    return
                if first_result != None:
                    result = first_result.set_attribute_values(
                        attributes_values={"Status": "Error"}
                    )
                    print(result)


            def checkLBRActivationStatus(my_dm_root):
                ans1 = dm.IsLBRActivated(dm_root=my_dm_root)
                if ans1:
                    print("LBR is activated")
                else:
                    print("LBR is deactivated")


            def checkLBREnableStatus(my_dm_root):
                ans = dm.IsLBREnabled(dm_root=my_dm_root)
                if ans:
                    print("LBR is enabled")
                else:
                    print("LBR is not enabled")
                return ans


            def checkLBRState(my_dm_root):
                print("-------------------------DM = ", my_dm_root, "-----------------------------")
                ans = checkLBREnableStatus(my_dm_root)

                if ans == False:
                    return

                attemptAnLBRViolation()

                print("Attempting to DEactivate LBR!!!!")
                dm.DeactivateLBR(dm_root=my_dm_root)
                checkLBRActivationStatus(my_dm_root)

                attemptAnLBRViolation()

                print("Attempting to Activate LBR!!!!")
                dm.ActivateLBR(dm_root=my_dm_root)
                checkLBRActivationStatus(my_dm_root)


            def main():
                dm_root = "http://kronos:9080/"
                checkLBRState(dm_root)


    """


def IsLBRActivated(dm_root: str) -> bool:
    """

    Returns whether LBR functionality is currently enabled and active in a given DM, or the current DM. It is used after having used deactivateLBR for that DM root.

    Parameters
    ----------
    dm_root : str, optional
            The dm_root that we request whether it is activated or not. If ommitted, the current DM is used.

    Returns
    -------
    bool
            True is case the LBR is enabled and currently active for this DM, false otherwise.

    See Also
    --------
    DeactivateLBR, ActivateLBR

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def checkLBRActivationStatus(my_dm_root):
                ans1 = dm.IsLBRActivated(dm_root=my_dm_root)
                if ans1:
                    print("LBR is activated for dm root ", my_dm_root)
                else:
                    print("LBR is deactivated for dm root ", my_dm_root)


            def main():
                dm_root = "http://kronos:9080/"
                checkLBRActivationStatus(dm_root)


    """


def IsLBREnabled(dm_root: str) -> bool:
    """

    Returns a given DM, or the current DM, supports LBR functionality at all.

    Parameters
    ----------
    dm_root : str, optional
            The dm_root that we request whether it is activated or not. If ommitted, the current DM root is used.

    Returns
    -------
    bool
            True if LBR functionality is enabled, False otherwise.

    See Also
    --------
    IsLBRActivated, DeactivateLBR, ActivateLBR

    Examples
    --------
    ::

            import os
            import ansa
            from ansa import dm


            def checkLBREnableStatus(my_dm_root):
                print("-------------------------DM = ", my_dm_root, "-----------------------------")
                ans = dm.IsLBREnabled(dm_root=my_dm_root)
                if ans:
                    print("LBR is enabled")
                else:
                    print("LBR is not enabled")
                return ans


            def main():
                dm_root = "http://kronos:9080/"
                checkLBRState(dm_root)


            def main():
                dm_root = "http://kronos:9080/"
                checkLBRState(dm_root)


    """
