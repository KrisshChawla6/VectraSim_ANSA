from __future__ import annotations
from typing import *
from . import (
    constants,
    batchmesh,
    cad,
    connections,
    base,
    utils,
    morph,
    calc,
    mesh,
    session,
    taskmanager,
    kinetics,
    dm,
    vr,
    spdrm,
    analysis_tools,
    script,
    betascript,
    guitk,
)


def ImportCode(path: str) -> int:
    """

    This function imports the code from another python module (py or pyb).

    Parameters
    ----------
    path : str
            The name of the script file to import.

    Returns
    -------
    int
            Returns 0 on success, else an exception is raised.

    Examples
    --------
    ::

            import ansa

            file1 = "/home/demo/module1.pyb"
            file2 = "C:\\\\demo\\\\module2.pyb"

            ansa.ImportCode(file1)
            ansa.ImportCode(file2.replace("\\\\", "/"))


            def main():
                module1.function1()
                module2.function1()


    """


def ScriptCurrentDir() -> str:
    """

    Returns the current working directory path.

    Returns
    -------
    str
            Returns the current working directory.

    See Also
    --------
    ScriptHomeDir, ScriptUserDir

    Examples
    --------
    ::

            import ansa


            def main():
                print(ansa.ScriptCurrentDir())


    """


def ScriptHomeDir() -> str:
    """

    Returns the ANSA/META Home directory path

    Returns
    -------
    str
            Returns the ANSA/META Home directory path.

    See Also
    --------
    ScriptCurrentDir, ScriptUserDir

    Examples
    --------
    ::

            import ansa


            def main():
                print(ansa.ScriptHomeDir())


    """


def ScriptUserDir() -> str:
    """

    Returns the BetaHome directory path.

    Returns
    -------
    str
            Returns the BetaHome directory path.

    See Also
    --------
    ScriptCurrentDir, ScriptHomeDir

    Examples
    --------
    ::

            import ansa


            def main():
                print(ansa.ScriptUserDir())


    """


def CompileScript(fileInput: str, fileOutput: str, moduleName: str, mode: bool) -> int:
    """

    Creates a compiled (pyb/bsx) file from the given script path.

    Parameters
    ----------
    fileInput : str
            The path of the script that we want to compile.

    fileOutput : str
            The destination path of the created compiled file.

    moduleName : str
            The name of the module.

    mode : bool, optional
            Declares whether to include the input script's imported modules, inside the final compiled file.
            (Applicable to all the imported modules, either through the native Python "import", or through the "ansa.ImportCode" function)
            -True, to include dependencies in the compiled script. (Default)
            -False, otherwise.
            It has effect only for Python scripts.

    Returns
    -------
    int
            Returns 1 on success, 0 on failure.

    Examples
    --------
    ::

            import ansa


            def main():
                ansa.CompileScript(
                    "/home/user/scripts/some_script.py",
                    "/home/user/scripts/some_script.pyb",
                    "moduleName",
                )


            if __name__ == "__main__":
                main()


    """


def PybImport(module_name: str, script_file_path: str) -> object:
    """

    A function that imports python scripts (pyb).
    Returns the imported module.

    Parameters
    ----------
    module_name : str
            The name of the module.

    script_file_path : str
            The filepath of the script.

    Returns
    -------
    object
            Returns the imported module.

    Examples
    --------
    ::

            import ansa


            def main():
                x = ansa.PybImport("moduleName", "/module/file/path/moduleNameCompiled.pyb")
                x.funcInModuleNameCompiled()


    """


def ReadingFile() -> str:
    """

    Function that returns the currently reading physical file on disk.

    Returns
    -------
    str
            Returns the currently reading physical file on disk.

    Examples
    --------
    ::

            import ansa


            def main():
                x = ansa.ReadingFile()
                print(x)


    """
