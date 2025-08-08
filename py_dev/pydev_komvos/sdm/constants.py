from __future__ import annotations
from typing import *

NASTRAN: int = None

"""
Defines the NASTRAN Deck.

"""

LSDYNA: int = None

"""
Defines the LSDYNA Deck.

"""

PAMCRASH: int = None

"""
Defines the PAMCRASH Deck.

"""

ABAQUS: int = None

"""
Defines the ABAQUS Deck.

"""

RADIOSS: int = None

"""
Defines the RADIOSS Deck.

"""

ANSYS: int = None

"""
Defines the ANSYS Deck.

"""

PERMAS: int = None

"""
Defines the PERMAS Deck.

"""

FLUENT: int = None

"""
Defines the FLUENT Deck.

"""

FLUENT2D: int = None

"""
Defines the FLUENT2D Deck.

"""

STAR: int = None

"""
Defines the STAR Deck.

"""

UH3D: int = None

"""
Defines the UH3D Deck.

"""

CFDPP: int = None

"""
Defines the CFDPP Deck.

"""

OPENFOAM: int = None

"""
Defines the OPENFOAM Deck.

"""

MOLDEX3D: int = None

"""
Defines the MOLDEX3D Deck.

"""

RADTHERM: int = None

"""
Defines the RADTHERM Deck.

"""

SESTRA: int = None

"""
Defines the SESTRA Deck.

"""

THESEUS: int = None

"""
Defines the THESEUS Deck.

"""

app_version: str = None

"""
This function returns the current ansa version.

"""

app_version_int: int = None

"""
This function returns the current ansa version.

"""

app_home_dir: str = None

"""
The system directory used for the configuration files.

"""

app_root_dir: str = None

"""
The system's root directory.

"""

FILENAME: int = None

"""
The name of the CAD file currently processed.

"""

FILEPATH: int = None

"""
The directory of the CAD file currently processed.

"""

FLANCH_PROPERTY_ID: int = None

PART_COORD_SYS_DX1: int = None

"""
X component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DX2: int = None

"""
X component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DX3: int = None

"""
X component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_DY1: int = None

"""
Y component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DY2: int = None

"""
Y component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DY3: int = None

"""
Y component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_DZ1: int = None

"""
Z component of X axis used for Part's transformation.

"""

PART_COORD_SYS_DZ2: int = None

"""
Z component of Y axis used for Part's transformation.

"""

PART_COORD_SYS_DZ3: int = None

"""
Z component of Z axis used for Part's transformation.

"""

PART_COORD_SYS_X: int = None

"""
X coordinate of the origin used for Part's position.

"""

PART_COORD_SYS_Z: int = None

"""
Z coordinate of the origin used for Part's position.

"""

PART_ID: int = None

"""
Module ID of current Part.

"""

PART_MASS: int = None

PART_MATERIAL_ID: int = None

"""
The Material ID that will be assigned to all entities of the Part.

"""

PART_MODEL_NAME: int = None

PART_NAME: int = None

"""
The name of the Part as appears in the Parts Manager.

"""

PART_VERSION: int = None

"""
The version of the Part as appears in the Parts Manager.

"""

PART_VSC: int = None

PART_PROPERTY_ID: int = None

"""
The Property ID that will be assigned to all entities of the Part.

"""

PART_PROPERTY_NAME: int = None

"""
The name of the Property as appears in the Properties list.

"""

PART_PROPERTY_THICKNESS: int = None

"""
The thickness of the Property.

"""

POST_TRANSL_SCRIPT: int = None

POST_TRANSL_SCRIPT_ARGS: int = None

TRANSLATIONS: int = None

"""
Default character translations, eg. " " = "_", blank space is translated into an underscore.

"""

SEPARATORS: int = None

"""
Definition of whatever is used to separate words, ( eg. , _ . )

"""

MAT_REG: int = None

SYMMETRY_PART_ID: int = None

SYMMETRY_PART_PID_OFFSET: int = None

app_temp_dir: str = None

"""
The path of the temporary directory used by the application.

"""

ENM_REGEX: int = None

"""
A regular expression match (default) for the base.NameToEnts function.

"""

ENM_EXACT: int = None

"""
An exact match for the base.NameToEnts function.

"""

ENM_SUBSTRING: int = None

"""
A sub-string match for the base.NameToEnts function.

"""

ENM_SUBSTRING_IGNORECASE: int = None

"""
A sub-string case-insensitive match for the base.NameToEnts function.

"""

decks: tuple = None

"""
Returns a tuple with all the deck constants. Useful to iterate through all the available decks.

"""

DM_STATUS_UP_TO_DATE: int = None

"""
Defines the "Up to date" value of the "DM Update Status" of an entity

"""

DM_STATUS_NOT_UP_TO_DATE: int = None

"""
Defines the "Not up to date" value of the "DM Update Status" of an entity

"""

DM_STATUS_MODIFIED: int = None

"""
Defines the "Modified" value of the "DM Update Status" of an entity

"""

DM_STATUS_ALTERNATIVE: int = None

"""
Defines the "Alternative" value of the "DM Update Status" of an entity

"""

DM_STATUS_NOT_FOUND: int = None

"""
Defines the "Not found" value of the "DM Update Status" of an entity

"""

DM_STATUS_ERROR: int = None

"""
Defines the error value when the "DM Update Status" of an entity cannot be identified

"""

REPORT_ALL: int = None

"""
Defines the debug mode to report everything.

"""

REPORT_SILENCE: int = None

"""
Defines the debug mode to report silently.

"""

