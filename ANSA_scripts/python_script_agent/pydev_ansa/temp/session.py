from __future__ import annotations
from typing import *


def ApplicationInformation() -> str:
    """

    This function reports build and runtime information of the running ANSA process.

    This includes the ANSA version, its build date, and information about the
    architecture of the application and the underling operating system
    The function takes no arguments.
    The report is similar to:
    +------------------------------------------------------------
     A N S A
     version: 12.2, compiled on: Jan 11 2007, 13:02:45
     built: 64-bit
     platform: Linux x86_64 2.4.21-209-smp little-endian
    +------------------------------------------------------------

    Returns
    -------
    str
            Returns a string containing the build/runtime information.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                s = session.ApplicationInformation()
                print(s)


    """


def DeckName(deck: int) -> str:
    """

    This function returns the deck name as string, given the integer deck constant.

    Parameters
    ----------
    deck : int
            The integer deck constant.

    Returns
    -------
    str
            Returns a string of the Deck name on success. On failure, it raises a ValueError Exception.

    See Also
    --------
    CurrentDeck, constants

    Examples
    --------
    ::

            import ansa
            from ansa import session
            from ansa import constants


            def main():
                ret = session.DeckName(constants.NASTRAN)
                print(ret)  # Will print "NASTRAN"


    """


def New(option: str) -> int:
    """

    This function instructs the program to create a new file.

    Parameters
    ----------
    option : str
            Accepted values:  "blank", "discard", "active" or "all".

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                session.New("discard")


    """


def Quit(status: int) -> int:
    """

    This function quits the current file and exits the program.

    Parameters
    ----------
    status : int, optional
            The exit code status of ANSA. (Default = 0)

    Returns
    -------
    int
            Returns 0 in all cases.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                session.Quit()


    """


def defbutton(group: str, label: str, tip: str, rgb: object):
    """

    A decorator that adds a menu button.
    It must be placed above the definition of the function which you want to be executed when the created button is pressed.

    Parameters
    ----------
    group : str
            The name of the group in which the button will be created.

    label : str, optional
            The label of the button.
            (If nothing is declared, the label will be the name of function).

    tip : str, optional
            The button's tip.
            (The text that is shown when the user rolls the mouse pointer over the button)

    rgb : object, optional
            A tuple with the rgb color used as underline color in the created button e.g. (255, 0, 0) for red color.

    Examples
    --------
    ::

            import ansa


            @ansa.session.defbutton("groupName", "buttonLabel", "buttonTip")
            def myFunction():
                print("Button Pressed")


    """


def BenchmarkFPS(
    frames: int, ctrl_flag: int, shift_flag: int, times_to_press_benchmark: int
) -> object:
    """

    Returns a list of size the "times_to_press_benchmark", which contains the results of FPS,
    same as if you had pressed in ANSA Settings>Graphics>Benchmark button having checkboxes
    CTRL and SHIFT as per arguments and settings frames set 20(default value).

    Parameters
    ----------
    frames : int
            Value that sets the number of frames that will be checked.

    ctrl_flag : int
            Options are 0 and 1. Value 0 sets the ctrl flag as unchecked and
            value 1 sets the flag as checked.

    shift_flag : int
            Options are 0 and 1. Value 0 sets the shift flag as unchecked and
            value 1 sets the flag as checked.

    times_to_press_benchmark : int
            Value that sets how many times the benchmark is called.

    Returns
    -------
    object
            Returns a list of size times_to_press_benchmark with the float values of FPS.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            # The following example calls the benchmark 3 times for the open database,
            # having frames=20 and CTRL+SHIFT ON and then calculates the mean FPS value.
            def main():
                number_of_frames = 20
                ctrl_flag = 1
                shift_flag = 1
                times_to_bechmark = 3
                benchmark = session.BenchmarkFPS(
                    number_of_frames, ctrl_flag, shift_flag, times_to_bechmark
                )
                print(benchmark)


    """


def SaveSettings() -> int:
    """
    .. deprecated:: 20.0.0
            Use :py:func:`BCSettingsWriteFile` instead.


    Saves the current settings of ANSA in the defaults file.

    Returns
    -------
    int
            It returns 0 in all cases.

    See Also
    --------
    guitk.BCSettingsWriteFile

    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.0.0. Use :py:func: BCSettingsWriteFile instead.",
        DeprecationWarning,
    )


def SaveSettingsAs(filename: str) -> int:
    """
    .. deprecated:: 20.0.0
            Use :py:func:`BCSettingsWriteFile` instead.


    This function gives the option to save the current settings used in ANSA, with a different file name.

    Parameters
    ----------
    filename : str
            the full pathname of the file where current settings (.defaults) will be saved.

    Returns
    -------
    int
            It returns 0 on success, 1 otherwise.

    See Also
    --------
    guitk.BCSettingsWriteFile

    """

    import warnings

    warnings.warn(
        "Deprecated since version 20.0.0. Use :py:func: BCSettingsWriteFile instead.",
        DeprecationWarning,
    )


def GetReadyForNewTask():
    """

    This function is invoked when the currently running ANSA instance is to be
    declared as available for running new tasks. The actual effect will depend on
    the configuration / state of the ANSA at the time. Specifically, on invocation
    of this command:
    * The currently open database is discarded
    * Python Exception with string 'ReadyForNewTask' as argument is raised. This is
      equivalent as if the following Python statement was invoked:
      raise Exception('ReadyForNewTask')

    When the execution engine detects that the script terminated with such an
    exception, then the following courses of action are possible:
    * If ANSA is not running as a worker (i.e. the listen port has not been
      configured), then the process is terminated.
    * If ANSA is running as a worker, but script execution was not triggered by the
      connected entity, then an Event Report message is sent with Event Code
      'Ready for New Task'
    * If ANSA is running as a worker and script execution was triggered by the
      connected entity, then nothing happens.


    Examples
    --------
    ::

            import ansa
            from ansa import session


            def task():
                # Execute task and then declare self as ready for new tasks
                session.GetReadyForNewTask()


    """


def PrintMemoryUsage(prefix: str) -> int:
    """
    .. deprecated:: 23.1.0
            Use :py:func:`GetProcessSystemMetrics` instead.


    Will print the application's current memory usage.

    Parameters
    ----------
    prefix : str, optional
            If the prefix argument is given, then it will precede the printed text.

    Returns
    -------
    int
            Returns 1 on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                session.PrintMemoryUsage()


    """

    import warnings

    warnings.warn(
        "Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.",
        DeprecationWarning,
    )


def ProgramArguments() -> object:
    """

    This function retrieves the command line arguments of the program.

    Returns
    -------
    object
            Returns a list containing the program arguments.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                m = session.ProgramArguments()
                print("There are ", len(m), " arguments")


    """


def GetFreePhysicalMemory() -> int:
    """
    .. deprecated:: 23.1.0
            Use :py:func:`GetProcessSystemMetrics` instead.


    Returns the free physical memory at the time of this function's call in kilobytes (1024 bytes).

    Returns
    -------
    int
            Returns the free physical memory on success and 0 on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                m = session.GetFreePhysicalMemory()
                print(m)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.",
        DeprecationWarning,
    )


def BetaClearVariable(name: str) -> bool:
    """

    This function frees the memory from the given beta variable.

    Parameters
    ----------
    name : str
            The name of the beta variable.

    Returns
    -------
    bool
            True if operation was successful, False otherwise.

    Examples
    --------
    ::

            import pickle
            import ansa
            from ansa import session


            def main():
                beta_var_name = "a"
                p = 1
                v = pickle.dumps(p)
                session.BetaSetVariable(beta_var_name, v)
                v = session.BetaGetVariable(beta_var_name)
                p = pickle.loads(v)
                print(p)
                session.BetaClearVariable(beta_var_name)
                v = session.BetaGetVariable(beta_var_name)
                if v == None:
                    print('Variable "' + beta_var_name + '" cannot be retrieved')


    """


def BetaGetVariable(name: str, match: int) -> object:
    """

    Ansa script can store user data and address them by a name.
    These data are NOT volatile as script variables and can be accessed either from different scripts or whenever a script is run.
    This function allows the user to retrieve data stored under a user specified name.
    Wildcards can also be used ("*", "?", "[...]").

    Parameters
    ----------
    name : str
            The name of the beta variable to be retrieved.

    match : int, optional
            Control the matching mode of the name lookup.
            Values are:
            -constants.ENM_EXACT: an exact match (default)
            -constants.ENM_WILDCARD: a wildcard match

    Returns
    -------
    object
            The function returns the Beta Variable if the variable is found. It returns None otherwise.

            If match=constants.ENM_WILDCARD is used, it returns a dictionary with key the variable name and data the variable value.
            The dictionary is empty if no variables matching the wildcard expression were found.

    See Also
    --------
    session.BetaSetVariable

    Examples
    --------
    ::

            import pickle

            import ansa
            from ansa import constants
            from ansa import session


            def main():
                p = 1
                v = pickle.dumps(p)
                session.BetaSetVariable("a", v)
                v = session.BetaGetVariable("a")
                p = pickle.loads(v)
                print(p)

                p = 2
                v = pickle.dumps(p)
                session.BetaSetVariable("AB", v)

                print("Variables matching *")
                vars = session.BetaGetVariable("*", constants.ENM_WILDCARD)  # returns all variables
                for key, value in vars.items():
                    p = pickle.loads(value)
                    print("Name: {} Value: {}".format(key, p))
                print("")

                print("Variables matching [a-z]*")
                vars = session.BetaGetVariable(
                    "[a-z]*", constants.ENM_WILDCARD
                )  # returns variables starting with lower letter
                for key, value in vars.items():
                    p = pickle.loads(value)
                    print("Name: {} Value: {}".format(key, p))


            if __name__ == "__main__":
                main()


    """


def BetaSetVariable(name: str, value: object) -> bool:
    """

    Ansa script can store user data and address them by a name.
    These data are NOT volatile as script variables and can be accessed either from
    different scripts or whenever a script is run.
    This function allows the user to store data under a user specified name.

    Parameters
    ----------
    name : str
            The name of the beta variable.

    value : object
            A bytes object of the data to store.

    Returns
    -------
    bool
            Returns True on success, or False on failure.

    See Also
    --------
    session.BetaGetVariable

    Examples
    --------
    ::

            import pickle

            import ansa
            from ansa import constants
            from ansa import session


            def main():
                p = 1
                v = pickle.dumps(p)
                session.BetaSetVariable("a", v)
                v = session.BetaGetVariable("a")
                p = pickle.loads(v)
                print(p)

                p = 2
                v = pickle.dumps(p)
                session.BetaSetVariable("AB", v)

                print("Variables matching *")
                vars = session.BetaGetVariable("*", constants.ENM_WILDCARD)  # returns all variables
                for key, value in vars.items():
                    p = pickle.loads(value)
                    print("Name: {} Value: {}".format(key, p))
                print("")

                print("Variables matching [a-z]*")
                vars = session.BetaGetVariable(
                    "[a-z]*", constants.ENM_WILDCARD
                )  # returns variables starting with lower letter
                for key, value in vars.items():
                    p = pickle.loads(value)
                    print("Name: {} Value: {}".format(key, p))


            if __name__ == "__main__":
                main()


    """


def GetMemoryUsage() -> object:
    """
    .. deprecated:: 23.1.0
            Use :py:func:`GetProcessSystemMetrics` instead.


    Returns the application's physical memory consumption in kilobytes(1024 bytes).

    Returns
    -------
    object
            Returns the application's physical memory consumption on success and None on failure.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                m = session.GetMemoryUsage()
                print(m)


    """

    import warnings

    warnings.warn(
        "Deprecated since version 23.1.0. Use :py:func: GetProcessSystemMetrics instead.",
        DeprecationWarning,
    )


def AcquireFeature(feature: str) -> int:
    """

    It registers license token found in a BETA LM license.

    Parameters
    ----------
    feature : str
            The feature to acquire license tokens for.
            The list of available feature names for a specific license server can be found
            with the command beta_lm_stat -h server. BETA CAE Systems issues license
            keys to application developers upon request.

    Returns
    -------
    int
            1: When the feature has been acquired successfully.
            -1: When an incompatible feature is given (ex: ANSA).
            -10: When an invalid feature is given.
            -12: When no credit is available.

    See Also
    --------
    ReleaseFeature

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                ret_feature = session.AcquireFeature("TEST_SCRIPT")

                if ret_feature == -12:
                    print("No credit is available")
                    return 1
                if ret_feature == -10:
                    print("This is invalid feature")
                    return 1
                even_nums = []
                for i in range(0, 100, 2):
                    even_nums.append(i)
                ret = session.ReleaseFeature("TEST_SCRIPT")
                if ret == 1:
                    print("Tokens released succesfully")


    """


def ReleaseFeature(feature: str) -> int:
    """

    Releases a previously acquired feature through session.AcquireFeature.

    Parameters
    ----------
    feature : str
            The feature to release the tokens from.

    Returns
    -------
    int
            1: When a previously acquired feature is succesfully released.
            -1: When an incompatible feature, unknown or a non acquired feature is given.

    See Also
    --------
    session.AcquireFeature

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                ret_feature = session.AcquireFeature("TEST_SCRIPT")

                if ret_feature == -12:
                    print("No credit is available")
                    return 1
                if ret_feature == -10:
                    print("This is invalid feature")
                    return 1
                even_nums = []

                for i in range(0, 100, 2):
                    even_nums.append(i)
                ret = session.ReleaseFeature("TEST_SCRIPT")
                if ret == 1:
                    print("Tokens released succesfully")


    """


def setPluginInfos(classInstance: object):
    """

    Sets an instance of a user-defined class, as plugin's information.

    Parameters
    ----------
    classInstance : object
            An Instance of a user-defined class with specific variable names.
            The main Variable names are:
            - filepath: Set as string the path of actual main file. (mandatory)
            - Buttons: A dict in which you set your buttons with key:button's label and
                       values: tuple(function name, tooltip, help, path for image of button).
            - title: Set title of plugin as string.
            - author: Set author of plugin as string.
            - hostApplication: Set host application of plugin as string.
            - minHostApplicationVersion: Set minimmum host application version of plugin as string.
            - description: Set description of plugin as string.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            class plinfos:
                def __init__(self):
                    self.title = "Title of plugin"
                    self.author = "Author of plugin"
                    self.hostApplication = "ANSA"
                    self.minHostApplicationVersion = "v16.0.0"
                    self.description = "Description of plugin"
                    self.filepath = "/file/path/of/plugin/plugin.ppl"

                    self.Buttons = {
                        "ButtonLabel": ("functionName", "tooltip", "help", "imagefilePath")
                    }


            def main():
                x = plinfos()
                session.setPluginInfos(x)


    """


def SystemInfo(format: str = "text") -> object:
    """

    This function reports system information of the machine running ANSA process.
    This includes the system name, the system version, the architecture type, the number of CPU cores etc.

    Parameters
    ----------
    format : str, optional
            The format of the returned data. Can be 'text' or 'dict'.  Default is 'text'.

    Returns
    -------
    object
            If format ='text' a string object is returned. If format = 'dict' the system information is returned as a dictionary object.

    Examples
    --------
    ::

            import ansa
            from ansa import session


            def main():
                s = session.SystemInfo(format="text")
                print(s)


    """
