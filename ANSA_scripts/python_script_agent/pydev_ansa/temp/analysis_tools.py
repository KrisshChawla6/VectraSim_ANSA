from __future__ import annotations
from typing import *


class RunSolver:
    """

    A class that is used to create Run Solver windows

    See Also
    --------
    RunSolverTextViewer, RunSolverPlotViewer

    Examples
    --------
    ::

            from __future__ import annotations
            import os
            import re
            import shlex
            import subprocess
            from ansa import base, session, guitk, constants, analysis_tools


            _RE_FLOAT = r"[-+]?(?:(?:\\d*\\.?\\d+)|(?:\\d+\\.?\\d*))(?:[eE][-+]?\\d+)?"


            def _show_msg_win_critical(msg):
                msg_win = guitk.BCMessageWindowCreate(
                    guitk.constants.BCMessageBoxCritical, msg, False
                )
                guitk.BCMessageWindowSetRejectButtonVisible(msg_win, False)
                guitk.BCMessageWindowExecute(msg_win)


            def _show_msg_win_information(msg):
                msg_win = guitk.BCMessageWindowCreate(
                    guitk.constants.BCMessageBoxInformation, msg, False
                )
                guitk.BCMessageWindowSetRejectButtonVisible(msg_win, False)
                guitk.BCMessageWindowExecute(msg_win)


            def _show_msg_win_question(msg):
                msg_win = guitk.BCMessageWindowCreate(
                    guitk.constants.BCMessageBoxQuestion, msg, False
                )
                return guitk.BCMessageWindowExecute(msg_win) == guitk.constants.BCRetKey


            def _get_path_from_line_edit_path(ledit_path):
                file_path = guitk.BCLineEditPathLineEditText(ledit_path)
                if not file_path:
                    return ""
                return os.path.abspath(file_path)


            class AbqTextViewer(analysis_tools.RunSolverTextViewer):
                def __init__(self, run_abq: RunAbq, name, is_console=False):
                    super().__init__(
                        name=name,
                        is_console=is_console,
                        supports_errors=True,
                        supports_warnings=True,
                        supports_notes=True,
                    )
                    self._run_abq = run_abq

                def get_file_path(self):
                    dir_name = self._run_abq.get_output_dir_name()
                    job_name = self._run_abq.get_job_name()
                    file_path = os.path.join(dir_name, job_name) + "." + self.name.lower()
                    return file_path

                def has_error_in_line(self, text):
                    return text.startswith(" ***ERROR") or text.startswith("***ERROR")

                def has_warning_in_line(self, text):
                    return text.startswith(" ***WARNING") or text.startswith("***WARNING")

                def has_note_in_line(self, text):
                    return text.startswith(" ***NOTE") or text.startswith("***NOTE")


            class AbqTotalIterationsPlotViewer(analysis_tools.RunSolverPlotViewer):
                def __init__(self, run_abq: RunAbq):
                    super().__init__(name="Total Iterations")
                    self._run_abq = run_abq
                    self._numbers_pattern = (
                        r"^\\s*"
                        + 5 * (r"\\d+\\s+")
                        + r"(\\d+)\\s+"
                        + "("
                        + _RE_FLOAT
                        + ")"
                        + r"\\s+"
                        + _RE_FLOAT
                        + r"\\s+"
                        + _RE_FLOAT
                        + r"\\s*"
                    )

                def get_file_path(self):
                    return (
                        os.path.join(
                            self._run_abq.get_output_dir_name(), self._run_abq.get_job_name()
                        )
                        + ".sta"
                    )

                def set_plot_options(self):
                    self.set_axis_title(pos="yleft", title="Total Iterations")
                    self.set_axis_title(pos="xbottom", title="Total Time")

                    self.set_curve_name(name="Total Iterations")
                    self.set_curve_color(r=0, g=0, b=255)

                def file_updated(self, new_text, file_index):
                    points = []

                    for line in new_text.splitlines():
                        match = re.search(self._numbers_pattern, line)
                        if match:
                            total_iters = float(match.group(1))
                            total_time = float(match.group(2))
                            points.append((total_time, total_iters))

                    if len(points) > 0:
                        self.append_points_to_curve(points)


            class RunAbq(analysis_tools.RunSolver):
                def __init__(self):
                    super().__init__(
                        window_caption="Run Abaqus",
                        query_status_interval=1.0,
                        initial_actions="Start",
                    )
                    self._out_ledit_path = None
                    self._exec_ledit_path = None
                    self._scratch_dir = None
                    self._data_check_cbox = None
                    self._cpus_ledit = None
                    self._mem_size_ledit = None
                    self._mem_unit_combo = None
                    self._log_file = None
                    self._process = None
                    self._suspend_process = None
                    self._resume_process = None

                def _get_output_file_path(self):
                    return _get_path_from_line_edit_path(self._out_ledit_path)

                def get_output_dir_name(self):
                    return os.path.dirname(self._get_output_file_path())

                def get_job_name(self):
                    return os.path.splitext(os.path.basename(self._get_output_file_path()))[0]

                def _get_lock_file(self):
                    dir_name = self.get_output_dir_name()
                    job_name = self.get_job_name()
                    file_path = os.path.join(dir_name, job_name) + ".lck"
                    return file_path

                def _get_exec_file_path(self):
                    return _get_path_from_line_edit_path(self._exec_ledit_path)

                def _get_log_file_path(self):
                    return os.path.join(self.get_output_dir_name(), self.get_job_name()) + ".log"

                def _get_mem_size(self):
                    mem_size = guitk.BCLineEditGetText(self._mem_size_ledit).strip()
                    if not mem_size:
                        return ""

                    mem_unit = guitk.BCComboBoxCurrentText(self._mem_unit_combo)
                    return mem_size + mem_unit

                def _get_solver_args(self):
                    args = []

                    args.append(f"job={self.get_job_name()}")
                    args.append("interactive")

                    if guitk.BCCheckBoxIsChecked(self._data_check_cbox):
                        args.append("datacheck")

                    cpus_num = guitk.BCLineEditGetInt(self._cpus_ledit)
                    if cpus_num != guitk.constants.blank:
                        args.append(f"cpus={cpus_num}")

                    mem_size = self._get_mem_size()
                    if mem_size:
                        args.append(f"memory={mem_size}")

                    scratch_dir_name = _get_path_from_line_edit_path(self._scratch_dir)
                    if scratch_dir_name:
                        args.append(f"scratch={scratch_dir_name}")

                    additional_args = guitk.BCLineEditGetText(self._additional_args_ledit).strip()
                    if additional_args:
                        for arg in shlex.split(additional_args):
                            args.append(arg)

                    return args

                def _check_user_input(self):
                    if not os.path.exists(self._get_exec_file_path()):
                        _show_msg_win_critical("Executable does not exist")
                        return False

                    if not self._get_output_file_path():
                        _show_msg_win_critical("Output file is empty")
                        return False

                    return True

                def _init(self):
                    if not self._check_user_input():
                        return False

                    if os.path.exists(self._get_lock_file()):
                        ret = _show_msg_win_question("Lock file detected. Delete and continue?")
                        if not ret:
                            return False
                        os.remove(self._get_lock_file())

                    if base.OutputAbaqus(self._get_output_file_path()) == 0:
                        _show_msg_win_critical("Output failed")
                        return False

                    self._log_file = open(self._get_log_file_path(), "w")

                    return True

                def handle_action(self, action):
                    if action == "Start":
                        if not self._init():
                            return
                        self.initialize()
                        self.set_busy()

                        args = [self._get_exec_file_path()] + self._get_solver_args()
                        self._process = subprocess.Popen(
                            args,
                            cwd=self.get_output_dir_name(),
                            stdout=self._log_file,
                            stderr=subprocess.STDOUT,
                        )
                    elif action == "Terminate":
                        args = [
                            self._get_exec_file_path(),
                            "terminate",
                            f"job={self.get_job_name()}",
                        ]
                        subprocess.Popen(
                            args,
                            cwd=self.get_output_dir_name(),
                            stdout=self._log_file,
                            stderr=subprocess.STDOUT,
                        )
                    elif action == "Suspend":
                        args = [self._get_exec_file_path(), "suspend", f"job={self.get_job_name()}"]
                        self._suspend_process = subprocess.Popen(
                            args,
                            cwd=self.get_output_dir_name(),
                            stdout=self._log_file,
                            stderr=subprocess.STDOUT,
                        )
                    elif action == "Resume":
                        self.set_busy()

                        args = [self._get_exec_file_path(), "resume", f"job={self.get_job_name()}"]
                        self._resume_process = subprocess.Popen(
                            args,
                            cwd=self.get_output_dir_name(),
                            stdout=self._log_file,
                            stderr=subprocess.STDOUT,
                        )
                    else:
                        raise Exception("Invalid action:", action)

                def query_status(self):
                    if self._process is not None:
                        ret = self._process.poll()
                        if ret is not None:
                            self._process = None
                            if ret == 0:
                                return "Completed"
                            else:
                                return "Failed"

                    if self._suspend_process is not None:
                        ret = self._suspend_process.poll()
                        if ret is not None:
                            self._suspend_process = None
                            if ret == 0:
                                return "Suspended"
                            else:
                                return "Running"

                    if self._resume_process is not None:
                        ret = self._resume_process.poll()
                        if ret is not None:
                            self._resume_process = None
                            if ret == 0:
                                return "Resumed"
                            else:
                                return "Suspended"

                    return "Running"

                def status_changed(self, new_status):
                    if new_status == "Running":
                        self.show_only_actions(actions=("Terminate", "Suspend"))
                    elif new_status == "Resumed":
                        self.show_only_actions(actions=("Terminate", "Suspend"))
                    elif new_status == "Suspended":
                        self.set_idle()
                        self.show_only_actions(actions="Resume")
                    elif new_status == "Completed":
                        self.set_idle()
                        self.show_only_actions(actions="Start")

                        self._log_file.close()
                        _show_msg_win_information("Job was completed")
                    elif new_status == "Failed":
                        self.set_idle()
                        self.show_only_actions(actions="Start")

                        self._log_file.close()
                        _show_msg_win_critical("Job failed")
                    else:
                        raise Exception("Invalid new_status:", new_status)

                def create_analysis_top_frame(self, parent):
                    g_layout = guitk.BCGridLayoutCreate(parent)
                    guitk.BCGridLayoutSetColStretch(g_layout, 0, 0)
                    guitk.BCGridLayoutSetColStretch(g_layout, 1, 1)

                    label = guitk.BCLabelCreate(g_layout, "Output file")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 0, 0, guitk.constants.BCAlignAuto)

                    self._out_ledit_path = guitk.BCLineEditPathCreate(
                        g_layout,
                        guitk.constants.BCHistoryFiles,
                        "",
                        guitk.constants.BCHistorySaveAs,
                        "RunAbq_OutputPath",
                    )
                    guitk.BCLineEditPathAddFilter(self._out_ledit_path, "ABAQUS", "inp")
                    guitk.BCGridLayoutAddWidget(
                        g_layout, self._out_ledit_path, 0, 1, guitk.constants.BCAlignAuto
                    )

                def create_options_frame(self, parent):
                    g_layout = guitk.BCGridLayoutCreate(parent)
                    guitk.BCGridLayoutSetColStretch(g_layout, 0, 0)
                    guitk.BCGridLayoutSetColStretch(g_layout, 1, 1)

                    label = guitk.BCLabelCreate(g_layout, "Executable")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 0, 0, guitk.constants.BCAlignAuto)
                    self._exec_ledit_path = guitk.BCLineEditPathCreate(
                        g_layout,
                        guitk.constants.BCHistoryFiles,
                        "",
                        guitk.constants.BCHistorySelect,
                        "RunAbq_Executable",
                    )
                    guitk.BCGridLayoutAddWidget(
                        g_layout, self._exec_ledit_path, 0, 1, guitk.constants.BCAlignAuto
                    )

                    label = guitk.BCLabelCreate(g_layout, "Scratch directory")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 1, 0, guitk.constants.BCAlignAuto)
                    self._scratch_dir = guitk.BCLineEditPathCreate(
                        g_layout,
                        guitk.constants.BCHistoryFiles,
                        "",
                        guitk.constants.BCHistorySelect,
                        "RunAbq_ScratchDirectory",
                    )
                    guitk.BCGridLayoutAddWidget(
                        g_layout, self._scratch_dir, 1, 1, guitk.constants.BCAlignAuto
                    )

                    self._data_check_cbox = guitk.BCCheckBoxCreate(g_layout, "Data check")
                    guitk.BCGridLayoutAddMultiCellWidget(
                        g_layout, self._data_check_cbox, 2, 2, 0, 1, guitk.constants.BCAlignAuto
                    )

                    label = guitk.BCLabelCreate(g_layout, "Number of CPUs")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 3, 0, guitk.constants.BCAlignAuto)
                    self._cpus_ledit = guitk.BCLineEditCreateInt(g_layout)
                    guitk.BCGridLayoutAddWidget(
                        g_layout, self._cpus_ledit, 3, 1, guitk.constants.BCAlignAuto
                    )

                    label = guitk.BCLabelCreate(g_layout, "Memory size")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 4, 0, guitk.constants.BCAlignAuto)
                    frame = guitk.BCFrameCreate(g_layout)
                    h_layout = guitk.BCBoxLayoutCreate(frame, guitk.constants.BCHorizontal)
                    guitk.BCBoxLayoutSetMargin(h_layout, 0)
                    guitk.BCBoxLayoutSetSpacing(h_layout, 0)
                    self._mem_size_ledit = guitk.BCLineEditCreateInt(h_layout)
                    guitk.BCBoxLayoutSetStretchFactor(h_layout, self._mem_size_ledit, 1)
                    self._mem_unit_combo = guitk.BCComboBoxCreate(h_layout, ("MB", "GB", "%"))
                    guitk.BCBoxLayoutSetStretchFactor(h_layout, self._mem_unit_combo, 0)
                    guitk.BCGridLayoutAddWidget(g_layout, frame, 4, 1, guitk.constants.BCAlignAuto)

                    label = guitk.BCLabelCreate(g_layout, "Additional arguments")
                    guitk.BCGridLayoutAddWidget(g_layout, label, 5, 0, guitk.constants.BCAlignAuto)
                    self._additional_args_ledit = guitk.BCLineEditCreate(g_layout, "")
                    guitk.BCGridLayoutAddWidget(
                        g_layout, self._additional_args_ledit, 5, 1, guitk.constants.BCAlignAuto
                    )

                    guitk.BCSpacerCreate(parent)


            @session.defbutton("Run Abaqus", "Run Abaqus")
            def create_run_abq_win():
                run_abq = RunAbq()

                run_abq.add_viewer(AbqTextViewer(run_abq, name="LOG", is_console=True))
                run_abq.add_viewer(AbqTextViewer(run_abq, name="DAT"))
                run_abq.add_viewer(AbqTextViewer(run_abq, name="MSG"))
                run_abq.add_viewer(AbqTextViewer(run_abq, name="STA"))
                run_abq.add_viewer_group(group="Plots")
                run_abq.add_viewer(AbqTotalIterationsPlotViewer(run_abq), group="Plots")

                run_abq.add_action(action="Start", icon="run_small.svg")
                run_abq.add_action(action="Resume", icon="run_small.svg")
                run_abq.add_action_group(group="Stop", icon="rect_red_small.svg")
                run_abq.add_action(action="Terminate", icon="rect_red_small.svg", group="Stop")
                run_abq.add_action(action="Suspend", icon="media_pause.svg", group="Stop")

                run_abq.create_window()

    """

    def __init__(
        self,
        window_caption: str,
        initial_actions: object,
        query_status_interval: float = 3.0,
    ) -> object:
        """

        Object construction method.


        Parameters
        ----------
        window_caption : str
                The caption of the window

        initial_actions : object
                A string or a list of strings which contains which actions will be available when the window opens

        query_status_interval : float, optional
                Time interval in seconds. query_status() will be called by this interval when set_busy() has been called.

        Returns
        -------
        object
                Returns a RunSolver object

        """

    def add_viewer(self, viewer: object, group: str = None) -> None:
        """

        Add a viewer in the window


        Parameters
        ----------
        viewer : object
                RunSolverTextViewer or RunSolverPlotViewer

        group : str, optional
                Viewers with the same group will be grouped together under the same tab

        Returns
        -------
        None

        """

    def add_viewer_group(self, group: str) -> None:
        """

        Add a viewer group. Viewers with the same group will be grouped together under the same tab.


        Parameters
        ----------
        group : str
                Name of the group

        Returns
        -------
        None

        """

    def add_action(self, action: str, icon: str = None, group: str = None) -> None:
        """

        Add an action


        Parameters
        ----------
        action : str
                Name of the action

        icon : str, optional
                Icon of the action

        group : str, optional
                Name of the group. Actions with the same group will be grouped together under a popup menu.

        Returns
        -------
        None

        """

    def add_action_group(self, group: str, icon: str = None) -> None:
        """

        Add an action group. Actions with the same group will be grouped together under the same popup menu.


        Parameters
        ----------
        group : str
                Name of the group

        icon : str, optional
                Icon of the group

        Returns
        -------
        None

        """

    def create_window(self) -> None:
        """

        Create a Run Solver window


        Returns
        -------
        None

        """

    def create_analysis_top_frame(self, parent: object) -> None:
        """

        Override this method to create the top frame of the Analysis tab.


        Parameters
        ----------
        parent : object
                The parent widget

        Returns
        -------
        None

        """

    def create_analysis_bottom_frame(self, parent: object) -> None:
        """

        Override this method to create the bottom frame of the Analysis tab.


        Parameters
        ----------
        parent : object
                The parent widget

        Returns
        -------
        None

        """

    def create_options_frame(self, parent: object) -> None:
        """

        Override this method to create the frame of the Options tab


        Parameters
        ----------
        parent : object
                The parent widget

        Returns
        -------
        None

        """

    def initialize(self) -> None:
        """

        Initialize the window for a new job. This method must be called when a new job starts.


        Returns
        -------
        None

        """

    def set_idle(self) -> None:
        """

        Sets the window to an idle state. query_status() stops being called. All files stop being read.


        Returns
        -------
        None

        """

    def set_busy(self) -> None:
        """

        Set the window to the busy state. query_status() starts being called. All files start being read.


        Returns
        -------
        None

        """

    def show_only_actions(self, actions: object) -> None:
        """

        Show only the specified actions. All other actions are hidden.


        Parameters
        ----------
        actions : object
                An action or a list of actions

        Returns
        -------
        None

        """

    def handle_action(self, action: str) -> None:
        """

        Override this method to handle the activation of an action.


        Parameters
        ----------
        action : str
                The activated action

        Returns
        -------
        None

        """

    def query_status(self) -> str:
        """

        Override this method to return the current status of the job. This method is called every query_status_interval seconds specified in __init__().


        Returns
        -------
        str
                The current status of the job

        """

    def status_changed(self, new_status: str) -> None:
        """

        This method is called when the status returned by query_status() changes value. Override this method to handle the new status.


        Parameters
        ----------
        new_status : str
                The new status of the job return by query_status().

        Returns
        -------
        None

        """

    def ok_pressed(self) -> bool:
        """

        This method is called when OK is pressed. Override this method to set a user-defined behaviour.


        Returns
        -------
        bool
                Return True to close the window. False otherwise.

        """

    def cancel_pressed(self) -> bool:
        """

        Method called when Cancel is pressed. Override this method to set a user-defined behaviour.


        Returns
        -------
        bool
                Return True to close the window. False otherwise.

        """


class RunSolverTextViewer:
    """

    A text viewer which is part of a Run Solver window. Used by ansa.analysis_tools.RunSolver.

    See Also
    --------
    RunSolver, RunSolverPlotViewer
    """

    name: str = None
    """
	The name of the text viewer

	"""

    def __init__(
        self,
        name: str,
        is_console: bool = False,
        supports_errors: bool = False,
        supports_warnings: bool = False,
        supports_notes: bool = False,
    ) -> object:
        """

        Object construction method


        Parameters
        ----------
        name : str
                The name of the text viewer

        is_console : bool, optional
                Set to True if the viewer displays the console output. Set to False otherwise.

        supports_errors : bool, optional
                Set to True if the viewer supports errors. Set to False otherwise.

        supports_warnings : bool, optional
                Set to True if the viewer supports warnings. Set to False otherwise.

        supports_notes : bool, optional
                Set to True if the viewer supports notes. Set to False otherwise.

        Returns
        -------
        object
                Returns a RunSolverTextViewer object

        """

    def get_file_path(self) -> object:
        """

        Override this method to return a file or a list of files to be monitored by this viewer


        Returns
        -------
        object
                A file or a list of files to be monitored

        """

    def initialize(self) -> None:
        """

        This method is automatically called and initializes the viewer. If further initialization is needed override this method, call super().initialize() and then initialize any data necessary.


        Returns
        -------
        None

        """

    def has_error_in_line(self, text: str) -> bool:
        """

        Override this method to check if an error is detected in the current line.


        Parameters
        ----------
        text : str
                The text of the current line

        Returns
        -------
        bool
                Return True if an error was detected in the line. False otherwise

        """

    def has_warning_in_line(self, text: str) -> bool:
        """

        Override this method to check if a warning is detected in the current line.


        Parameters
        ----------
        text : str
                Text of the line

        Returns
        -------
        bool
                Return True if a warning is detected. False otherwise.

        """

    def has_note_in_line(self, text: str) -> bool:
        """

        Override this method to check if a note is detected in the current line.


        Parameters
        ----------
        text : str
                The text of the current line

        Returns
        -------
        bool
                Return True if a note is detected. False otherwise.

        """

    def append_text(self, text: str) -> None:
        """

        Append text to viewer


        Parameters
        ----------
        text : str
                Text to append

        Returns
        -------
        None

        """


class RunSolverPlotViewer:
    """

    A plot viewer which is part of a Run Solver window. Used by ansa.analysis_tools.RunSolver.

    See Also
    --------
    RunSolver, RunSolverTextViewer
    """

    name: str = None
    """
	The name of the plot viewer

	"""

    def __init__(self, name: str, curves_num: int = 1) -> object:
        """

        Object construction method


        Parameters
        ----------
        name : str
                The name of the plot viewer

        curves_num : int, optional
                The number of curves in the plot

        Returns
        -------
        object
                Returns a RunSolverPlotViewer object

        """

    def get_file_path(self) -> object:
        """

        Override this method to return a file or a list of files to be monitored by this viewer


        Returns
        -------
        object
                A file or a list of files to be monitored

        """

    def initialize(self) -> None:
        """

        This method is automatically called and initializes the viewer. If further initialization is needed override this method, call super().initialize() and then initialize any data necessary.


        Returns
        -------
        None

        """

    def set_plot_options(self) -> None:
        """

        Override this method to set the plot options


        Returns
        -------
        None

        """

    def set_axis_title(self, pos: str, title: str) -> None:
        """

        Set the axis title


        Parameters
        ----------
        pos : str
                The axis position. Available options: "yleft", "yright", "xbottom", "xtop"

        title : str
                The axis title

        Returns
        -------
        None

        """

    def set_axes_count(self, pos: str, count: int) -> None:
        """

        Set the number of axes in a specified position


        Parameters
        ----------
        pos : str
                The axis position. Available options: "yleft", "yright", "xbottom", "xtop"

        count : int
                Number of axes

        Returns
        -------
        None

        """

    def set_scale_engine(self, pos: str, engine: str) -> None:
        """

        Set the scale engine of an axis


        Parameters
        ----------
        pos : str
                The axis position. Available options: "yleft", "yright", "xbottom", "xtop"

        engine : str
                The scale engine. Available options: "log"

        Returns
        -------
        None

        """

    def set_curve_name(self, name: str, curve_index: int = 0) -> None:
        """

        Set the name of the curve


        Parameters
        ----------
        name : str
                The name of the curve

        curve_index : int, optional
                The curve index

        Returns
        -------
        None

        """

    def set_curve_color(self, r: int, g: int, b: int, curve_index: int = 0) -> None:
        """

        Set the color of a curve


        Parameters
        ----------
        r : int
                The red value. A value between 0 and 255.

        g : int
                The green value. A value between 0 and 255.

        b : int
                The blue value. A value between 0 and 255.

        curve_index : int, optional
                The curve index

        Returns
        -------
        None

        """

    def set_curve_axes(self, x_pos: str, y_pos: str, curve_index: int = 0) -> None:
        """

        Set X and Y axes for a curve. The curve will painted according to the coordinates of its axes.


        Parameters
        ----------
        x_pos : str
                Position of the X axis. Available options: "yleft", "yright", "xbottom", "xtop".

        y_pos : str
                Position of the Y axis. Available options: "yleft", "yright", "xbottom", "xtop".

        curve_index : int, optional
                The curve index

        Returns
        -------
        None

        """

    def set_curve_line_style(self, style: str, curve_index: int = 0) -> None:
        """

        Set the style of the line of curve


        Parameters
        ----------
        style : str
                The style of the line of curve. Available options: "solid", "dash", "dot", "dash_dot", dash_dot_dot".

        curve_index : int, optional
                The curve index

        Returns
        -------
        None

        """

    def file_updated(self, new_text: str, file_index: int) -> None:
        """

        This method is called when the monitored files are upated. Override this method to append new points to curves based on the new text.


        Parameters
        ----------
        new_text : str
                The new text of the monitored file.

        file_index : int
                The index of the monitored file.

        Returns
        -------
        None

        """

    def append_points_to_curve(self, points: list, curve_index: int = 0) -> None:
        """

        Inserts a point (x, y) to the end of the point list of the curve


        Parameters
        ----------
        points : list
                A list of (x, y) tuples

        curve_index : int, optional
                The curve index

        Returns
        -------
        None

        """
