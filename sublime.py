import collections
import html
import json
import sys

from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    overload,
    Sequence,
    Sized,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import TypedDict


# ----- #
# types #
# ----- #

Layout = TypedDict(
    "Layout",
    # fmt: off
    {
        "cols": Sequence[float],
        "rows": Sequence[float],
        "cells": Sequence[Sequence[int]],
    },
    # fmt: on
)
Location = Tuple[str, str, Tuple[int, int]]
Point = int
Vector = Tuple[float, float]
Value = Union[dict, list, str, float, bool, None]

_T = TypeVar("_T")
Callback0 = Callable[[], None]
Callback1 = Callable[[_T], None]


# -------- #
# ST codes #
# -------- #

HOVER_TEXT: int = 1
HOVER_GUTTER: int = 2
HOVER_MARGIN: int = 3

ENCODED_POSITION: int = 1
TRANSIENT: int = 4
FORCE_GROUP: int = 8
ADD_TO_SELECTION_SEMI_TRANSIENT: int = 16
ADD_TO_SELECTION: int = 32
IGNORECASE: int = 2
LITERAL: int = 1
MONOSPACE_FONT: int = 1
KEEP_OPEN_ON_FOCUS_LOST: int = 2

HTML: int = 1
COOPERATE_WITH_AUTO_COMPLETE: int = 2
HIDE_ON_MOUSE_MOVE: int = 4
HIDE_ON_MOUSE_MOVE_AWAY: int = 8
KEEP_ON_SELECTION_MODIFIED: int = 16
HIDE_ON_CHARACTER_EVENT: int = 32

DRAW_EMPTY: int = 1
HIDE_ON_MINIMAP: int = 2
DRAW_EMPTY_AS_OVERWRITE: int = 4
PERSISTENT: int = 16
# Deprecated, use DRAW_NO_FILL instead
DRAW_OUTLINED: int = 32
DRAW_NO_FILL: int = 32
DRAW_NO_OUTLINE: int = 256
DRAW_SOLID_UNDERLINE: int = 512
DRAW_STIPPLED_UNDERLINE: int = 1024
DRAW_SQUIGGLY_UNDERLINE: int = 2048
NO_UNDO: int = 8192
HIDDEN: int = 128

OP_EQUAL: int = 0
OP_NOT_EQUAL: int = 1
OP_REGEX_MATCH: int = 2
OP_NOT_REGEX_MATCH: int = 3
OP_REGEX_CONTAINS: int = 4
OP_NOT_REGEX_CONTAINS: int = 5
CLASS_WORD_START: int = 1
CLASS_WORD_END: int = 2
CLASS_PUNCTUATION_START: int = 4
CLASS_PUNCTUATION_END: int = 8
CLASS_SUB_WORD_START: int = 16
CLASS_SUB_WORD_END: int = 32
CLASS_LINE_START: int = 64
CLASS_LINE_END: int = 128
CLASS_EMPTY_LINE: int = 256

INHIBIT_WORD_COMPLETIONS: int = 8
INHIBIT_EXPLICIT_COMPLETIONS: int = 16
DYNAMIC_COMPLETIONS: int = 32
INHIBIT_REORDER: int = 128

DIALOG_CANCEL: int = 0
DIALOG_YES: int = 1
DIALOG_NO: int = 2

UI_ELEMENT_SIDE_BAR: int = 1
UI_ELEMENT_MINIMAP: int = 2
UI_ELEMENT_TABS: int = 4
UI_ELEMENT_STATUS_BAR: int = 8
UI_ELEMENT_MENU: int = 16
UI_ELEMENT_OPEN_FILES: int = 32

LAYOUT_INLINE: int = 0
LAYOUT_BELOW: int = 1
LAYOUT_BLOCK: int = 2

KIND_ID_AMBIGUOUS: int = 0
KIND_ID_KEYWORD: int = 1
KIND_ID_TYPE: int = 2
KIND_ID_FUNCTION: int = 3
KIND_ID_NAMESPACE: int = 4
KIND_ID_NAVIGATION: int = 5
KIND_ID_MARKUP: int = 6
KIND_ID_VARIABLE: int = 7
KIND_ID_SNIPPET: int = 8

KIND_AMBIGUOUS: Tuple[int, str, str] = (KIND_ID_AMBIGUOUS, "", "")
KIND_KEYWORD: Tuple[int, str, str] = (KIND_ID_KEYWORD, "", "")
KIND_TYPE: Tuple[int, str, str] = (KIND_ID_TYPE, "", "")
KIND_FUNCTION: Tuple[int, str, str] = (KIND_ID_FUNCTION, "", "")
KIND_NAMESPACE: Tuple[int, str, str] = (KIND_ID_NAMESPACE, "", "")
KIND_NAVIGATION: Tuple[int, str, str] = (KIND_ID_NAVIGATION, "", "")
KIND_MARKUP: Tuple[int, str, str] = (KIND_ID_MARKUP, "", "")
KIND_VARIABLE: Tuple[int, str, str] = (KIND_ID_VARIABLE, "", "")
KIND_SNIPPET: Tuple[int, str, str] = (KIND_ID_SNIPPET, "s", "Snippet")

COMPLETION_FORMAT_TEXT: int = 0
COMPLETION_FORMAT_SNIPPET: int = 1
COMPLETION_FORMAT_COMMAND: int = 2

COMPLETION_FLAG_KEEP_PREFIX: int = 1


def version() -> str:
    """ Returns the version number """
    ...


def platform() -> str:
    """ Returns the platform, which may be "osx", "linux" or "windows" """
    ...


def arch() -> str:
    """ Returns the CPU architecture, which may be "x32" or "x64" """
    ...


def channel() -> str:
    """ Returns the release channel, which may be "stable" or "dev" """
    ...


def executable_path() -> str:
    """ Returns the path to the "sublime_text" executable """
    ...


def executable_hash() -> Tuple[str, str, str]:
    """
    Returns `(version_number, platform_arch, executable_hash)`
    such as `('4079', 'windows_x64', '906388de50d5233b5648200ce9d1452a')`
    """
    ...


def packages_path() -> str:
    """ Returns the path where all the user's loose packages are located """
    ...


def installed_packages_path() -> str:
    """ Returns the path where all the user's `.sublime-package` files are located """
    ...


def cache_path() -> str:
    """ Returns the path where Sublime Text stores cache files """
    ...


def status_message(msg: str) -> None:
    """ Shows a message in the status bar """
    ...


def error_message(msg: str) -> None:
    """ Displays an error dialog to the user """
    ...


def message_dialog(msg: str) -> None:
    """ Displays a message dialog to the user """
    ...


def ok_cancel_dialog(msg: str, ok_title: str = "") -> int:
    """
    Displays an <kbd>ok</kbd> <kbd>cancel</kbd> question dialog to the user If `ok_title` is
    provided, this may be used as the text on the <kbd>ok</kbd> button.
    Returns `True` if the user presses the <kbd>ok</kbd> button
    """
    ...


def yes_no_cancel_dialog(msg: str, yes_title: str = "", no_title: str = "") -> int:
    """
    Displays a <kbd>yes</kbd> <kbd>no</kbd> <kbd>cancel</kbd> question dialog to the user
    If `yes_title` and/or `no_title` are provided, they will be used as the
    text on the corresponding buttons on some platforms. Returns `DIALOG_YES`,
    `DIALOG_NO` or `DIALOG_CANCEL`
    """
    ...


def open_dialog(
    callback: Callable[[Optional[Union[str, List[str]]]], None],
    file_types: List[Tuple[str, List[str]]] = [],
    directory: Optional[str] = None,
    multi_select: bool = False,
    allow_folders: bool = False,
) -> None:
    """
    Shows the open file dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    file_types: [(str, [str])] - A list of allowed file types, consisting of a
                                 description and a list of allowed extensions.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    multi_select: bool - Whether to allow selecting multiple files. Function
                         will call `callback` with a list if this is True.
    allow_folders: bool - Whether to also allow selecting folders. Only works on
                          macOS. If you only want to select folders use
                          `select_folder_dialog`.
    """
    ...


def save_dialog(
    callback: Callable[[Optional[str]], None],
    file_types: List[Tuple[str, List[str]]] = [],
    directory: Optional[str] = None,
    name: Optional[str] = None,
    extension: Optional[str] = None,
) -> None:
    """
    Shows the save file dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    file_types: [(str, [str])] - A list of allowed file types, consisting of a
                                 description and a list of allowed extensions.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    name: str | None - The default name of the file in the save dialog.
    extension: str | None - The default extension used in the save dialog.
    """
    ...


def select_folder_dialog(
    callback: Callable[[Optional[Union[str, List[str]]]], None],
    directory: Optional[str] = None,
    multi_select: bool = False,
) -> None:
    """
    Show the select folder dialog.

    callback - Called with selected path or `None` once open dialog is closed.
    directory: str | None - The directory the dialog should start in. Will use
                            the virtual working directory if not provided.
    multi_select: bool - Whether to allow selecting multiple folders. Function
                         will call `callback` with a list if this is True.
    """
    ...


def run_command(cmd: str, args: Optional[Dict[str, Any]] = None) -> None:
    """ Runs the named `ApplicationCommand` with the (optional) given `args` """
    ...


def format_command(cmd: str, args: Optional[Dict[str, Any]] = None) -> str:
    """
    Creates a "command string" from a str cmd name, and an optional dict of args.
    This is used when constructing a command-based `CompletionItem`
    """
    ...


def html_format_command(cmd: str, args: Optional[Dict[str, Any]] = None) -> str:
    ...


def command_url(cmd: str, args: Optional[Dict[str, Any]] = None) -> str:
    """ Creates a `subl:` protocol URL for executing a command in a minihtml link """
    ...


def get_clipboard_async(callback: Callable[[str], None], size_limit: int = 16777216) -> None:
    """
    Calls `callback` with the contents of the clipboard. For performance reasons
    if the size of the clipboard content is bigger than `size_limit`, an empty
    string will be returned.
    """
    ...


def get_clipboard(size_limit: int = 16777216) -> str:
    """
    Warning: Deprecated in favor of `get_clipboard_async()`

    Returns the content of the clipboard. For performance reasons if the size of
    the clipboard content is bigger than size_limit, an empty string will be
    returned.
    """
    ...


def set_clipboard(text: str) -> None:
    """ Sets the contents of the clipboard """
    ...


def log_commands(flag: bool) -> None:
    """
    Controls command logging. If enabled, all commands run from key bindings
    and the menu will be logged to the console
    """
    ...


def log_input(flag: bool) -> None:
    """
    Enables or disables input logging. This is useful to find the names of
    certain keys on the keyboard
    """
    ...


def log_fps(flag: bool) -> None:
    """
    Enables or disables fps logging.
    """
    ...


def log_result_regex(flag: bool) -> None:
    """
    Enables or disables result regex logging. This is useful when trying to
    debug `file_regex` and `line_regex` in build systems
    """
    ...


def log_indexing(flag: bool) -> None:
    ...


def log_build_systems(flag: bool) -> None:
    ...


def log_control_tree(flag: bool) -> None:
    """
    When enabled, clicking with <kbd>Ctrl</kbd>+<kbd>Alt</kbd>
    will log the control tree under the mouse to the console.
    """
    ...


def score_selector(scope_name: str, selector: str) -> int:
    """
    Matches the `selector` against the given scope, returning a score
    A score of 0 means no match, above 0 means a match. Different selectors may
    be compared against the same scope: a higher score means the selector is a
    better match for the scope
    """
    ...


def load_resource(name: str) -> str:
    """
    Loads the given resource. The `name` should be in the format
    `Packages/Default/Main.sublime-menu`
    """
    ...


def load_binary_resource(name: str) -> bytes:
    """
    Loads the given resource. The `name` should be in the format
    `Packages/Default/Main.sublime-menu`
    """
    ...


def find_resources(pattern: str) -> List[str]:
    """ Finds resources whose file name matches the given `pattern` """
    ...


def encode_value(val: Value, pretty: bool = ...) -> str:
    """
    Encode a JSON compatible value into a string representation
    If `pretty` is set to `True`, the string will include newlines and indentation
    """
    ...


def decode_value(data: str) -> Value:
    """
    Decodes a JSON string into an object.
    If `data` is invalid, a `ValueError` will be thrown
    """
    ...


@overload
def expand_variables(val: str, variables: Dict[str, str]) -> str:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


@overload
def expand_variables(val: List[str], variables: Dict[str, str]) -> List[str]:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


@overload
def expand_variables(val: Dict[str, str], variables: Dict[str, str]) -> Dict[str, str]:
    """
    Expands any variables in the string `value` using the variables defined in
    the dictionary `variables`
    `value` may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    ...


def list_syntaxes() -> List[Dict[str, Any]]:
    """
    Returns a list of all available syntaxes.
    Each dict will have the keys "path", "name", "hidden" and "scope"
    """
    ...


def find_syntax(fname: str, first_line: Optional[str] = None) -> Optional[str]:
    """
    Returns the path to the syntax that will be used when opening a file with the name fname.
    The first_line of file contents may also be provided if available.
    """
    ...


def load_settings(base_name: str) -> "Settings":
    """
    Loads the named settings. The name should include a file name and extension,
    but not a path The packages will be searched for files matching the
    `base_name`, and the results will be collated into the settings object
    Subsequent calls to `load_settings()` with the `base_name` will return the
    same object, and not load the settings from disk again
    """
    ...


def save_settings(base_name: str) -> None:
    """ Flushes any in-memory changes to the named settings object to disk """
    ...


def set_timeout(f: Callback0, timeout_ms: int = 0) -> None:
    """
    Schedules a function to be called in the future. Sublime Text will block
    while the function is running
    """
    ...


def set_timeout_async(f: Callback0, timeout_ms: int = 0) -> None:
    """
    Schedules a function to be called in the future. The function will be
    called in a worker thread, and Sublime Text will not block while the
    function is running
    """
    ...


def active_window() -> "Window":
    """ Returns the most recently used window """
    ...


def windows() -> "List[Window]":
    """ Returns a list of all the open windows """
    ...


def get_macro() -> List[Dict[str, Any]]:
    """
    Returns a list of the commands and args that compromise the currently recorded macro.
    Each dict will contain the keys "command" and "args".
    """
    ...


class Window:
    """ This class represents windows and provides an interface of methods to interact with them """

    window_id: int
    settings_object: "Optional[Settings]"
    template_settings_object: "Optional[Settings]"

    def __init__(self, id: int) -> None:
        ...

    def __eq__(self, other: Any) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """ Returns a number that uniquely identifies this window """
        ...

    def is_valid(self) -> bool:
        """ Determines if this `Window` object is still valid """
        ...

    def hwnd(self) -> int:
        """ Platform specific window handle, only returns a meaningful result under Windows """
        ...

    def active_sheet(self) -> "Optional[Sheet]":
        """ Returns the currently focused sheet """
        ...

    def active_view(self) -> "Optional[View]":
        """ Returns the currently edited view """
        ...

    def new_html_sheet(self, name: str, contents: str, flags: int = 0, group: int = -1) -> "Sheet":
        """
        Constructs a sheet with HTML contents rendered using minihtml.

        name: A unicode string of the sheet name, shown in tab and Open Files

        contents: A unicode string of the HTML contents

        flags: A bitwise combination of:
        `sublime.TRANSIENT`: If the sheet should be transient
        `sublime.ADD_TO_SELECTION`: Add the file to the currently selected sheets in this group

        group: An integer of the group to add the sheet to, -1 for the active group
        """
        ...

    def run_command(self, cmd: str, args: Optional[Dict[str, Any]] = ...) -> None:
        """
        Runs the named `WindowCommand` with the (optional) given `args`
        This method is able to run any sort of command, dispatching the
        command via input focus
        """
        ...

    def new_file(self, flags: int = 0, syntax: str = "") -> "View":
        """
        Creates a new file, The returned view will be empty, and its
        `is_loaded()` method will return `True`. Flags must be either `0` or `TRANSIENT`
        """
        ...

    def open_file(self, fname: str, flags: int = 0, group: int = -1) -> "View":
        """
        Opens the named file, and returns the corresponding view. If the file is
        already opened, it will be brought to the front. Note that as file
        loading is asynchronous, operations on the returned view won't be
        possible until its `is_loading()` method returns `False`.

        The optional `flags` parameter is a bitwise combination of:

        `ENCODED_POSITION`: Indicates the file_name should be searched for
        a :row or :row:col suffix
        `TRANSIENT`: Open the file as a preview only: it won't have a tab
        assigned it until modified
        `FORCE_GROUP`: don't select the file if it's opened in a different group
        """
        ...

    def find_open_file(self, fname: str) -> "Optional[View]":
        """
        Finds the named file in the list of open files, and returns the
        corresponding `View`, or `None` if no such file is open
        """
        ...

    def num_groups(self) -> int:
        """ Returns the number of view groups in the window """
        ...

    def active_group(self) -> int:
        """ Returns the index of the currently selected group """
        ...

    def focus_group(self, idx: int) -> None:
        """ Makes the given group active """
        ...

    def focus_sheet(self, sheet: "Sheet") -> None:
        """ Switches to the given `sheet` """
        ...

    def focus_view(self, view: "View") -> None:
        """ Switches to the given `view` """
        ...

    def bring_to_front(self) -> None:
        """ Brings the window in front of any other windows """
        ...

    def get_sheet_index(self, sheet: "Sheet") -> Tuple[int, int]:
        """
        Returns the group, and index within the group of the `sheet`
        Returns (-1, -1) if not found
        """
        ...

    def get_view_index(self, view: "View") -> Tuple[int, int]:
        """
        Returns the group, and index within the group of the `view`
        Returns (-1, -1) if not found
        """
        ...

    def set_sheet_index(self, sheet: "Sheet", group: int, idx: int) -> None:
        """ Moves the `sheet` to the given `group` and index """
        ...

    def set_view_index(self, view: "View", group: int, idx: int) -> None:
        """ Moves the `view` to the given `group` and index """
        ...

    def sheets(self) -> "List[Sheet]":
        """ Returns all open sheets in the window """
        ...

    def views(self) -> "List[View]":
        """ Returns all open views in the window """
        ...

    def active_sheet_in_group(self, group: int) -> "Optional[Sheet]":
        """ Returns the currently focused sheet in the given `group` """
        ...

    def active_view_in_group(self, group: int) -> "Optional[View]":
        """ Returns the currently edited view in the given `group` """
        ...

    def sheets_in_group(self, group: int) -> "List[Sheet]":
        """ Returns all open sheets in the given `group` """
        ...

    def views_in_group(self, group: int) -> "List[View]":
        """ Returns all open views in the given `group` """
        ...

    def transient_sheet_in_group(self, group: int) -> "Optional[Sheet]":
        """ Returns the transient `Sheet` in the given `group` if any """
        ...

    def transient_view_in_group(self, group: int) -> "Optional[View]":
        """ Returns the transient `View` in the given `group` if any """
        ...

    def layout(self) -> Layout:
        """ Returns the current layout """
        ...

    def get_layout(self) -> Layout:
        """ Deprecated, use `layout()` """
        ...

    def set_layout(self, layout: Layout) -> None:
        """ Changes the tile-based panel layout of view groups """
        ...

    def create_output_panel(self, name: str, unlisted: bool = False) -> "View":
        """
        Returns the view associated with the named output panel, creating it if required
        The output panel can be shown by running the _show_panel_ window command,
        with the panel argument set to the `name` with an "output." prefix.

        The optional `unlisted` parameter is a boolean to control if the
        output panel should be listed in the panel switcher
        """
        ...

    def find_output_panel(self, name: str) -> "Optional[View]":
        """
        Returns the view associated with the named output panel, or `None` if
        the output panel does not exist
        """
        ...

    def destroy_output_panel(self, name: str) -> None:
        """ Destroys the named output panel, hiding it if currently open """
        ...

    def active_panel(self) -> Optional[str]:
        """
        Returns the name of the currently open panel, or `None` if no panel is open
        Will return built-in panel names (e.g. "console", "find", etc)
        in addition to output panels
        """
        ...

    def panels(self) -> List[str]:
        """
        Returns a list of the names of all panels that have not been marked as unlisted
        Includes certain built-in panels in addition to output panels
        """
        ...

    def get_output_panel(self, name: str) -> "View":
        """ deprecated, use `create_output_panel()` """
        ...

    def show_input_panel(
        self,
        caption: str,
        initial_text: str,
        on_done: Optional[Callback1[str]],
        on_change: Optional[Callback1[str]],
        on_cancel: Callback0,
    ) -> "View":
        """
        Shows the input panel, to collect a line of input from the user
        `on_done` and `on_change`, if not `None`, should both be functions
        that expect a single string argument
        `on_cancel` should be a function that expects no arguments
        The view used for the input widget is returned
        """
        ...

    def show_quick_panel(
        self,
        items: Union[Sequence[str], Sequence[Sequence[str]]],
        on_select: Callback1[int],
        flags: int = 0,
        selected_index: int = -1,
        on_highlight: Optional[Callback1[int]] = None,
    ) -> None:
        """
        Shows a quick panel, to select an item in a list.

        * `items` may be a list of strings, or a list of string lists
        In the latter case, each entry in the quick panel will show multiple rows.

        * `on_select` will be called once, with the index of the selected item
        If the quick panel was cancelled, `on_select` will be called with an
        argument of `-1`.

        * `flags` is a bitwise OR of `MONOSPACE_FONT`
        and `KEEP_OPEN_ON_FOCUS_LOST`

        * `on_highlighted`, if given, will be called every time the highlighted item in the quick panel is changed
        """
        ...

    def is_sidebar_visible(self) -> bool:
        """ Returns `True` if the sidebar will be shown when contents are available """
        ...

    def set_sidebar_visible(self, flag: bool) -> None:
        """ Sets the sidebar to be shown or hidden when contents are available """
        ...

    def is_minimap_visible(self) -> bool:
        """ Returns `True` if the minimap is enabled """
        ...

    def set_minimap_visible(self, flag: bool) -> None:
        """ Controls the visibility of the minimap """
        ...

    def is_status_bar_visible(self) -> bool:
        """ Returns `True` if the status bar will be shown """
        ...

    def set_status_bar_visible(self, flag: bool) -> None:
        """ Controls the visibility of the status bar """
        ...

    def get_tabs_visible(self) -> bool:
        """ Returns `True` if tabs will be shown for open files """
        ...

    def set_tabs_visible(self, flag: bool) -> None:
        """ Controls if tabs will be shown for open files """
        ...

    def is_menu_visible(self) -> bool:
        """ Returns `True` if the menu is visible """
        ...

    def set_menu_visible(self, flag: bool) -> None:
        """ Controls if the menu is visible """
        ...

    def folders(self) -> List[str]:
        """ Returns a list of the currently open folders """
        ...

    def project_file_name(self) -> str:
        """ Returns name of the currently opened project file, if any """
        ...

    def project_data(self) -> Optional[Dict[str, Value]]:
        """
        Returns the project data associated with the current window
        The data is in the same format as the contents of a _.sublime-project_ file
        """
        ...

    def set_project_data(self, v: Dict[str, Value]) -> None:
        """
        Updates the project data associated with the current window
        If the window is associated with a _.sublime-project_ file, the project
        file will be updated on disk, otherwise the window will store the data
        internally
        """
        ...

    def workspace_file_name(self) -> Optional[str]:
        """ Returns the workspace filename of the current `Window` if possible """
        ...

    def settings(self) -> "Settings":
        """ Per-window settings, the contents are persisted in the session """
        ...

    def template_settings(self) -> "Settings":
        """
        Per-window settings that are persisted in the session, and duplicated
        into new windows
        """
        ...

    def lookup_symbol_in_index(self, sym: str) -> List[Location]:
        """ Finds all files and locations where sym is defined, using the symbol index """
        ...

    def lookup_symbol_in_index_by_kind(self, sym: str, kind: int) -> List[Location]:
        """ Finds all files and locations where sym is defined, using the symbol index """
        ...

    def lookup_symbol_in_open_files(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is defined, searching
        through open files
        """
        ...

    def lookup_symbol_in_open_files_by_kind(self, sym: str, kind: int) -> List[Location]:
        """ Finds all files and locations where sym is defined, searching through open files """
        ...

    def lookup_references_in_index(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is referenced,
        using the symbol index
        """
        ...

    def lookup_references_in_open_files(self, sym: str) -> List[Location]:
        """
        Returns all files and locations where the symbol `sym` is referenced,
        searching through open files
        """
        ...

    def extract_variables(self) -> Dict[str, str]:
        """
        Returns a dictionary of strings populated with contextual keys:
        `packages`, `platform`, `file`, `file_path`, `file_name`, `file_base_name`,
        `file_extension`, `folder`, `project`, `project_path`, `project_name`,
        `project_base_name`, `project_extension`
        This dict is suitable for passing to `sublime.expand_variables()`
        """
        ...

    def status_message(self, msg: str) -> None:
        """ Show a message in the status bar """
        ...


class Edit:
    """
    `Edit` objects have no functions, they exist to group buffer modifications

    `Edit` objects are passed to `TextCommands`, and can not be created by the
    user. Using an invalid `Edit` object, or an `Edit` object from a different view,
    will cause the functions that require them to fail
    """

    edit_token: int

    def __init__(self, token: int) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Region:
    """ Represents an area of the buffer. Empty regions, where `a == b` are valid """

    a: int
    b: int
    xpos: int

    def __init__(self, a: int, b: Optional[int] = None, xpos: int = -1) -> None:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, rhs: Any) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __lt__(self, rhs: "Region") -> bool:
        ...

    def __contains__(self, v: Union["Region", Point]) -> bool:
        ...

    def to_tuple(self) -> Tuple[Point, Point]:
        """ Returns a tuple of this region (excluding xpos).

        Use this to uniquely identify a region in a set or similar. Regions
        can't be used for that directly as they may be mutated.
        """
        ...

    def empty(self) -> bool:
        """ Returns `True` if `begin() == end()` """
        ...

    def begin(self) -> int:
        """ Returns the minimum of `a` and `b` """
        ...

    def end(self) -> int:
        """ Returns the maximum of `a` and `b` """
        ...

    def size(self) -> int:
        """
        deprecated, use `len()` instead
        Returns the number of characters spanned by the region. Always >= 0
        """
        ...

    def contains(self, x: Union["Region", Point]) -> bool:
        """
        If `x` is a region, returns `True` if it's a subset
        If `x` is a point, returns `True` if `begin() <= x <= end()`
        """
        ...

    def cover(self, rhs: "Region") -> "Region":
        """ Returns a `Region` spanning both this and the given regions """
        ...

    def intersection(self, rhs: "Region") -> "Region":
        """ Returns the set intersection of the two regions """
        ...

    def intersects(self, rhs: "Region") -> bool:
        """
        Returns `True` if `self == rhs` or both include one or more
        positions in common
        """
        ...


class HistoricPosition:
    """
    Provides a snapshot of the row and column info for a point, before changes were made to a `View`.
    This is primarily useful for replaying changes to a document.
    """

    pt: Point
    row: int
    col: int
    col_utf16: int
    col_utf8: int

    def __init__(self, pt: Point, row: int, col: int, col_u16: int, col_u8: int) -> None:
        ...

    def __repr__(self) -> str:
        ...


class TextChange:
    """
    Represents a change that occured to the text of a `View`.
    This is primarily useful for replaying changes to a document.
    """

    a: HistoricPosition
    b: HistoricPosition
    len_utf16: int
    len_utf8: int
    str: str

    def __init__(self, pa: HistoricPosition, pb: HistoricPosition, s: str) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Selection:
    """
    Maintains a set of Regions, ensuring that none overlap
    The regions are kept in sorted order
    """

    view_id: int

    def __init__(self, id: int) -> None:
        ...

    def __iter__(self) -> Iterator:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, index: int) -> Region:
        ...

    def __delitem__(self, index: int) -> None:
        ...

    def __eq__(self, rhs: Any) -> bool:
        ...

    def __lt__(self, rhs: "Selection") -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def is_valid(self) -> bool:
        """ Determines if this `Selection` object is still valid """
        ...

    def clear(self) -> None:
        """ Removes all regions """
        ...

    def add(self, x: Union[Region, Point]) -> None:
        """
        Adds the given region or point. It will be merged with any intersecting
        regions already contained within the set
        """
        ...

    def add_all(self, regions: Sequence[Union[Region, Point]]) -> None:
        """ Adds all `regions` in the given list or tuple """
        ...

    def subtract(self, region: Region) -> None:
        """ Subtracts the `region` from all regions in the set """
        ...

    def contains(self, region: Region) -> None:
        """
        Deprecated, use `in` instead.

        Returns `True` if the given `region` is a subset
        """
        ...


def make_sheet(sheet_id: int) -> "Sheet":
    """ Create a `Sheet` object with the given ID """


class Sheet:
    """
    Represents a content container, i.e. a tab, within a window
    Sheets may contain a View, or an image preview
    """

    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __eq__(self, other: Any) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """ Returns a number that uniquely identifies this sheet """
        ...

    def window(self) -> Optional[Window]:
        """
        Returns the window containing the sheet. May be `None` if the sheet
        has been closed
        """
        ...

    def view(self) -> "Optional[View]":
        """
        Returns the view contained within the sheet. May be `None` if the
        sheet is an image preview, or the view has been closed
        """
        ...

    def file_name(self) -> Optional[str]:
        """
        The full name file the file associated with the buffer,
        or None if it doesn't exist on disk.
        """
        ...


class TextSheet(Sheet):
    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """ Sets the name of this `Sheet` """
        ...


class ImageSheet(Sheet):
    sheet_id: int

    def __repr__(self) -> str:
        ...


class HtmlSheet(Sheet):
    sheet_id: int

    def __init__(self, id: int) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """ Sets the name of this `Sheet` """
        ...

    def set_contents(self, contents: str) -> None:
        """ Sets the content of this `Sheet` """
        ...


class View:
    """
    Represents a view into a text buffer. Note that multiple views may refer to
    the same buffer, but they have their own unique selection and geometry
    """

    def __init__(self, id):
        self.view_id = id
        self.selection = Selection(id)
        self.settings_object = None

    def __len__(self):
        return self.size()

    def __eq__(self, other):
        return isinstance(other, View) and other.view_id == self.view_id

    def __bool__(self):
        return self.view_id != 0

    def __repr__(self):
        return f"View({self.view_id!r})"

    def id(self):
        """ Returns a number that uniquely identifies this view """
        return self.view_id

    def buffer_id(self):
        """ Returns a number that uniquely identifies the buffer underlying this view """
        return sublime_api.view_buffer_id(self.view_id)

    def element(self):
        e = sublime_api.view_element(self.view_id)
        if e == "":
            return None
        return e

    def is_valid(self):
        """ Returns true if the View is still a valid handle. Will return False for a closed view, for example. """
        return sublime_api.view_buffer_id(self.view_id) != 0

    def is_primary(self):
        """
        Returns `True` if the view is the primary view into a file
        Will only be `False` if the user has opened multiple views into a file
        """
        return sublime_api.view_is_primary(self.view_id)

    def window(self):
        """ Returns a reference to the window containing the view """
        window_id = sublime_api.view_window(self.view_id)
        if window_id == 0:
            return None
        else:
            return Window(window_id)

    def file_name(self):
        """
        The full name file the file associated with the buffer, or `None` if it
        doesn't exist on disk
        """
        name = sublime_api.view_file_name(self.view_id)
        if len(name) == 0:
            return None
        else:
            return name

    def close(self):
        window_id = sublime_api.view_window(self.view_id)
        return sublime_api.window_close_file(window_id, self.view_id)

    def retarget(self, new_fname):
        sublime_api.view_retarget(self.view_id, new_fname)

    def name(self):
        """ The name assigned to the buffer, if any """
        return sublime_api.view_get_name(self.view_id)

    def set_name(self, name):
        """ Assigns a `name` to the buffer """
        sublime_api.view_set_name(self.view_id, name)

    def reset_reference_document(self):
        sublime_api.view_reset_reference_document(self.view_id)

    def set_reference_document(self, reference):
        sublime_api.view_set_reference_document(self.view_id, reference)

    def is_loading(self):
        """
        Returns `True` if the buffer is still loading from disk,
        and not ready for use
        """
        return sublime_api.view_is_loading(self.view_id)

    def is_dirty(self):
        """ Returns `True` if there are any unsaved modifications to the buffer """
        return sublime_api.view_is_dirty(self.view_id)

    def is_read_only(self):
        """ Returns `True` if the buffer may not be modified """
        return sublime_api.view_is_read_only(self.view_id)

    def set_read_only(self, read_only):
        """ Sets the read only property on the buffer """
        return sublime_api.view_set_read_only(self.view_id, read_only)

    def is_scratch(self):
        """
        Returns `True` if the buffer is a scratch buffer. Scratch buffers
        never report as being dirty
        """
        return sublime_api.view_is_scratch(self.view_id)

    def set_scratch(self, scratch):
        """
        Sets the scratch flag on the text buffer. When a modified scratch buffer
        is closed, it will be closed without prompting to save.
        """
        return sublime_api.view_set_scratch(self.view_id, scratch)

    def encoding(self):
        """ Returns the encoding currently associated with the file """
        return sublime_api.view_encoding(self.view_id)

    def set_encoding(self, encoding_name):
        """Applies a new encoding to the file. This encoding will be used the
        next time the file is saved"""
        return sublime_api.view_set_encoding(self.view_id, encoding_name)

    def line_endings(self):
        """ Returns the line endings used by the current file """
        return sublime_api.view_line_endings(self.view_id)

    def set_line_endings(self, line_ending_name):
        """ Sets the line endings that will be applied when next saving """
        return sublime_api.view_set_line_endings(self.view_id, line_ending_name)

    def size(self):
        """
        deprecated, use `len()` instead
        Returns the number of character in the file
        """
        return sublime_api.view_size(self.view_id)

    def begin_edit(self, edit_token, cmd, args=None):
        sublime_api.view_begin_edit(self.view_id, edit_token, cmd, args)
        return Edit(edit_token)

    def end_edit(self, edit):
        sublime_api.view_end_edit(self.view_id, edit.edit_token)
        edit.edit_token = 0

    def is_in_edit(self):
        return sublime_api.view_is_in_edit(self.view_id)

    def insert(self, edit, pt, text):
        """
        Inserts the given string in the buffer at the specified point
        Returns the number of characters inserted, this may be different if
        tabs are being translated into spaces in the current buffer
        """
        if edit.edit_token == 0:
            raise ValueError(
                "Edit objects may not be used after the TextCommand's run method has returned"
            )

        return sublime_api.view_insert(self.view_id, edit.edit_token, pt, text)

    def erase(self, edit, r):
        """ Erases the contents of the region from the buffer """
        if edit.edit_token == 0:
            raise ValueError(
                "Edit objects may not be used after the TextCommand's run method has returned"
            )

        sublime_api.view_erase(self.view_id, edit.edit_token, r)

    def replace(self, edit, r, text):
        """ Replaces the contents of the region with the given string """
        if edit.edit_token == 0:
            raise ValueError(
                "Edit objects may not be used after the TextCommand's run method has returned"
            )

        sublime_api.view_replace(self.view_id, edit.edit_token, r, text)

    def change_count(self):
        """
        Returns the current change count. Each time the buffer is modified,
        the change count is incremented. The change count can be used to
        determine if the buffer has changed since the last it was inspected
        """
        return sublime_api.view_change_count(self.view_id)

    def change_id(self):
        """ Returns a token that represents the current state of the buffer """
        return sublime_api.view_change_id(self.view_id)

    def transform_region_from(self, r, when):
        """ Given a Region, and a change_id() that describes what version of
        the buffer the region is in relation to, transforms the region into
        the current state of the buffer """
        return sublime_api.view_transform_region_from(self.view_id, r, when)

    def run_command(self, cmd, args=None):
        """ Runs the named `TextCommand` with the (optional) given `args` """
        sublime_api.view_run_command(self.view_id, cmd, args)

    def sel(self):
        """ Returns a reference to the selection """
        return self.selection

    def substr(self, x):
        """
        if `x` is a region, returns it's contents as a string
        if `x` is a point, returns the character to it's right
        """
        if isinstance(x, Region):
            return sublime_api.view_cached_substr(self.view_id, x.a, x.b)
        else:
            s = sublime_api.view_cached_substr(self.view_id, x, x + 1)
            # S2 backwards compat
            if len(s) == 0:
                return "\x00"
            else:
                return s

    def find(self, pattern, start_pt, flags=0):
        """
        Returns the first region matching the regex `pattern`, starting from
        `start_pt`, or `None` if it can't be found. The optional `flags`
        parameter may be `LITERAL`, `IGNORECASE`, or the two
        ORed together
        """
        return sublime_api.view_find(self.view_id, pattern, start_pt, flags)

    def find_all(self, pattern, flags=0, fmt=None, extractions=None):
        """
        Returns all (non-overlapping) regions matching the regex `pattern`
        The optional `flags` parameter may be `LITERAL`,
        `IGNORECASE`, or the two ORed together. If a format string is
        given, then all matches will be formatted with the formatted string
        and placed into the `extractions` list
        """
        if fmt is None:
            return sublime_api.view_find_all(self.view_id, pattern, flags)
        else:
            results = sublime_api.view_find_all_with_contents(self.view_id, pattern, flags, fmt)
            ret = []
            for region, contents in results:
                ret.append(region)
                extractions.append(contents)
            return ret

    def settings(self):
        """
        Returns a reference to the view's settings object. Any changes to this
        settings object will be private to this view
        """
        if not self.settings_object:
            self.settings_object = Settings(sublime_api.view_settings(self.view_id))

        return self.settings_object

    def meta_info(self, key, pt):
        return sublime_api.view_meta_info(self.view_id, key, pt)

    def extract_tokens_with_scopes(self, r):
        return sublime_api.view_extract_tokens_with_scopes(self.view_id, r.begin(), r.end())

    def extract_scope(self, pt):
        """
        Returns the extent of the syntax scope name assigned to the
        character at the given point
        """
        return sublime_api.view_extract_scope(self.view_id, pt)

    def scope_name(self, pt):
        """ Returns the syntax scope name assigned to the character at the given point """
        return sublime_api.view_scope_name(self.view_id, pt)

    def match_selector(self, pt, selector):
        """
        Checks the `selector` against the scope at the given point
        returning a bool if they match
        """
        return sublime_api.view_match_selector(self.view_id, pt, selector)

    def score_selector(self, pt, selector):
        """
        Matches the `selector` against the scope at the given point, returning a score
        A score of 0 means no match, above 0 means a match. Different selectors may
        be compared against the same scope: a higher score means the selector
        is a better match for the scope
        """
        return sublime_api.view_score_selector(self.view_id, pt, selector)

    def find_by_selector(self, selector):
        """
        Finds all regions in the file matching the given `selector`,
        returning them as a list
        """
        return sublime_api.view_find_by_selector(self.view_id, selector)

    def style(self):
        """
        Returns a dict of the global style settings for the view
        All colors are normalized to the six character hex form with
        a leading hash, e.g. _#ff0000_
        """
        return sublime_api.view_style(self.view_id)

    def style_for_scope(self, scope):
        """
        Accepts a string `scope` and returns a dict of style information,
        include the keys _foreground_, _bold_, _italic_, _source_line_,
        _source_column_ and _source_file_.
        If the `scope` has a background color set, the key _background_ will
        be present. The foreground and background colors are normalized to the
        six character hex form with a leading hash, e.g. _#ff0000_
        """
        return sublime_api.view_style_for_scope(self.view_id, scope)

    def indented_region(self, pt):
        return sublime_api.view_indented_region(self.view_id, pt)

    def indentation_level(self, pt):
        return sublime_api.view_indentation_level(self.view_id, pt)

    def has_non_empty_selection_region(self):
        return sublime_api.view_has_non_empty_selection_region(self.view_id)

    def lines(self, r):
        """ Returns a list of lines (in sorted order) intersecting the region `r` """
        return sublime_api.view_lines(self.view_id, r)

    def split_by_newlines(self, r):
        """Splits the region up such that each region returned exists on
        exactly one line"""
        return sublime_api.view_split_by_newlines(self.view_id, r)

    def line(self, x):
        """
        if `x` is a region, returns a modified copy of region such that it
        starts at the beginning of a line, and ends at the end of a line
        Note that it may span several lines
        if `x` is a point, returns the line that contains the point
        """
        if isinstance(x, Region):
            return sublime_api.view_line_from_region(self.view_id, x)
        else:
            return sublime_api.view_line_from_point(self.view_id, x)

    def full_line(self, x):
        """ As line(), but the region includes the trailing newline character, if any """
        if isinstance(x, Region):
            return sublime_api.view_full_line_from_region(self.view_id, x)
        else:
            return sublime_api.view_full_line_from_point(self.view_id, x)

    def word(self, x):
        """
        if `x` is a region, returns a modified copy of it such that it
        starts at the beginning of a word, and ends at the end of a word
        Note that it may span several words
        if `x` is a point, returns the word that contains it
        """
        if isinstance(x, Region):
            return sublime_api.view_word_from_region(self.view_id, x)
        else:
            return sublime_api.view_word_from_point(self.view_id, x)

    def classify(self, pt):
        """
        Classifies the point `pt`, returning a bitwise OR of zero or more of these flags:
        `CLASS_WORD_START`
        `CLASS_WORD_END`
        `CLASS_PUNCTUATION_START`
        `CLASS_PUNCTUATION_END`
        `CLASS_SUB_WORD_START`
        `CLASS_SUB_WORD_END`
        `CLASS_LINE_START`
        `CLASS_LINE_END`
        `CLASS_EMPTY_LINE`
        """
        return sublime_api.view_classify(self.view_id, pt)

    def find_by_class(self, pt, forward, classes, separators=""):
        """
        Finds the next location after point that matches the given classes
        If forward is `False`, searches backwards instead of forwards.
        classes is a bitwise OR of the `CLASS_XXX` flags
        `separators` may be passed in, to define what characters should be
        considered to separate words
        """
        return sublime_api.view_find_by_class(self.view_id, pt, forward, classes, separators)

    def expand_by_class(self, x, classes, separators=""):
        """
        Expands `x` to the left and right, until each side lands on a location
        that matches `classes`. classes is a bitwise OR of the
        `CLASS_XXX` flags. `separators` may be passed in, to define
        what characters should be considered to separate words
        """
        if isinstance(x, Region):
            return sublime_api.view_expand_by_class(self.view_id, x.a, x.b, classes, separators)
        else:
            return sublime_api.view_expand_by_class(self.view_id, x, x, classes, separators)

    def rowcol(self, tp):
        """ Calculates the 0-based line and column numbers of the the given point """
        return sublime_api.view_row_col(self.view_id, tp)

    def rowcol_utf8(self, tp):
        return sublime_api.view_row_col_utf8(self.view_id, tp)

    def rowcol_utf16(self, tp):
        return sublime_api.view_row_col_utf16(self.view_id, tp)

    def text_point(self, row, col, *, clamp_column=False):
        """ Converts a row and column into a text point """
        return sublime_api.view_text_point(self.view_id, row, col, clamp_column)

    def text_point_utf8(self, row, col_utf8, *, clamp_column=False):
        return sublime_api.view_text_point_utf8(self.view_id, row, col_utf8, clamp_column)

    def text_point_utf16(self, row, col_utf16, *, clamp_column=False):
        return sublime_api.view_text_point_utf16(self.view_id, row, col_utf16, clamp_column)

    def visible_region(self):
        """ Returns the approximate visible region """
        return sublime_api.view_visible_region(self.view_id)

    def show(self, x, show_surrounds=True, keep_to_left=False, animate=True):
        """ Scrolls the view to reveal x, which may be a Region or point """
        if isinstance(x, Region):
            return sublime_api.view_show_region(
                self.view_id, x, show_surrounds, keep_to_left, animate
            )
        if isinstance(x, Selection):
            for i in x:
                return sublime_api.view_show_region(
                    self.view_id, i, show_surrounds, keep_to_left, animate
                )
        else:
            return sublime_api.view_show_point(
                self.view_id, x, show_surrounds, keep_to_left, animate
            )

    def show_at_center(self, x):
        """ Scrolls the view to center on x, which may be a Region or point """
        if isinstance(x, Region):
            return sublime_api.view_show_region_at_center(self.view_id, x)
        else:
            return sublime_api.view_show_point_at_center(self.view_id, x)

    def viewport_position(self):
        """ Returns the (x, y) scroll position of the view in layout coordinates """
        return sublime_api.view_viewport_position(self.view_id)

    def set_viewport_position(self, xy, animate=True):
        """ Scrolls the view to the given position in layout coordinates """
        return sublime_api.view_set_viewport_position(self.view_id, xy, animate)

    def viewport_extent(self):
        """ Returns the width and height of the viewport, in layout coordinates """
        return sublime_api.view_viewport_extents(self.view_id)

    def layout_extent(self):
        """ Returns the total height and width of the document, in layout coordinates """
        return sublime_api.view_layout_extents(self.view_id)

    def text_to_layout(self, tp):
        """ Converts a text point to layout coordinates """
        return sublime_api.view_text_to_layout(self.view_id, tp)

    def text_to_window(self, tp):
        """ Converts a text point to window coordinates """
        return self.layout_to_window(self.text_to_layout(tp))

    def layout_to_text(self, xy):
        """ Converts layout coordinates to a text point """
        return sublime_api.view_layout_to_text(self.view_id, xy)

    def layout_to_window(self, xy):
        """ Converts layout coordinates to window coordinates """
        return sublime_api.view_layout_to_window(self.view_id, xy)

    def window_to_layout(self, xy):
        """ Converts window coordinates to layout coordinates """
        return sublime_api.view_window_to_layout(self.view_id, xy)

    def window_to_text(self, xy):
        """ Converts window coordinates to a text point """
        return self.layout_to_text(self.window_to_layout(xy))

    def line_height(self):
        """ Returns the height of a line in layout coordinates """
        return sublime_api.view_line_height(self.view_id)

    def em_width(self):
        """ Returns the em-width of the current font in layout coordinates """
        return sublime_api.view_em_width(self.view_id)

    def is_folded(self, sr):
        return sublime_api.view_is_folded(self.view_id, sr)

    def folded_regions(self):
        return sublime_api.view_folded_regions(self.view_id)

    def fold(self, x):
        if isinstance(x, Region):
            return sublime_api.view_fold_region(self.view_id, x)
        else:
            return sublime_api.view_fold_regions(self.view_id, x)

    def unfold(self, x):
        """ Unfolds all text in the region(s), returning the unfolded regions """
        if isinstance(x, Region):
            return sublime_api.view_unfold_region(self.view_id, x)
        else:
            return sublime_api.view_unfold_regions(self.view_id, x)

    def add_regions(
        self,
        key,
        regions,
        scope="",
        icon="",
        flags=0,
        annotations=[],
        annotation_color="",
        on_navigate=None,
        on_close=None,
    ):
        """
        Add a set of `regions` to the view. If a set of regions already exists
        with the given `key`, they will be overwritten. The `scope` is used
        to source a color to draw the regions in, it should be the name of a
        scope, such as "comment" or "string". If the scope is empty, the
        regions won't be drawn.

        The optional `icon` name, if given, will draw the named icons in the
        gutter next to each region. The `icon` will be tinted using the color
        associated with the `scope`. Valid icon names are dot, circle and
        bookmark. The `icon` name may also be a full package relative path
        such as _Packages/Theme - Default/dot.png_.

        The optional `flags` parameter is a bitwise combination of:

        `DRAW_EMPTY`: Draw empty regions with a vertical bar
        By default, they aren't drawn at all.
        `HIDE_ON_MINIMAP`: Don't show the regions on the minimap.
        `DRAW_EMPTY_AS_OVERWRITE`: Draw empty regions with a horizontal
        bar instead of a vertical one.
        `DRAW_NO_FILL`: Disable filling the regions, leaving only the outline.
        `DRAW_NO_OUTLINE`: Disable drawing the outline of the regions.
        `DRAW_SOLID_UNDERLINE`: Draw a solid underline below the regions.
        `DRAW_STIPPLED_UNDERLINE`: Draw a stippled underline below the regions.
        `DRAW_SQUIGGLY_UNDERLINE`: Draw a squiggly underline below the regions.
        `PERSISTENT`: Save the regions in the session.
        `HIDDEN`: Don't draw the regions.
        The underline styles are exclusive, either zero or one of them should
        be given. If using an underline, DRAW_NO_FILL and
        `DRAW_NO_OUTLINE` should generally be passed in
        """
        # S2 has an add_regions overload that accepted flags as the 5th
        # positional argument, however this usage is no longer supported
        if not isinstance(icon, "".__class__):
            raise ValueError("icon must be a string")

        if not isinstance(annotations, list):
            raise ValueError("annotations must be a list")

        if len(annotations) != 0 and len(annotations) != len(regions):
            raise ValueError("region and annotation length mismatch")

        if on_close is not None:
            flags = flags | 16384

        sublime_api.view_add_regions(
            self.view_id,
            key,
            regions,
            scope,
            icon,
            flags,
            annotations,
            annotation_color,
            on_navigate,
            on_close,
        )

    def get_regions(self, key):
        """ Return the regions associated with the given `key`, if any """
        return sublime_api.view_get_regions(self.view_id, key)

    def erase_regions(self, key):
        """ Remove the named regions """
        sublime_api.view_erase_regions(self.view_id, key)

    def add_phantom(self, key, region, content, layout, on_navigate=None):
        return sublime_api.view_add_phantom(self.view_id, key, region, content, layout, on_navigate)

    def erase_phantoms(self, key):
        sublime_api.view_erase_phantoms(self.view_id, key)

    def erase_phantom_by_id(self, pid):
        sublime_api.view_erase_phantom(self.view_id, pid)

    def query_phantom(self, pid):
        return sublime_api.view_query_phantoms(self.view_id, [pid])

    def query_phantoms(self, pids):
        return sublime_api.view_query_phantoms(self.view_id, pids)

    def assign_syntax(self, syntax_file):
        sublime_api.view_assign_syntax(self.view_id, syntax_file)

    def set_syntax_file(self, syntax_file):
        """ Deprecated, use `assign_syntax()` instead """
        self.assign_syntax(syntax_file)

    def symbols(self):
        """ Extract all the symbols defined in the buffer """
        return sublime_api.view_symbols(self.view_id)

    def get_symbols(self):
        """ Deprecated, use `symbols()` instead """
        return self.symbols()

    def indexed_symbols(self):
        return sublime_api.view_indexed_symbols(self.view_id)

    def indexed_references(self):
        return sublime_api.view_indexed_references(self.view_id)

    def set_status(self, key, value):
        """
        Adds the status `key` to the view. The value will be displayed in the
        status bar, in a comma separated list of all status values, ordered by key
        Setting the value to the empty string will clear the status
        """
        sublime_api.view_set_status(self.view_id, key, value)

    def get_status(self, key):
        """ Returns the previously assigned value associated with the `key`, if any """
        return sublime_api.view_get_status(self.view_id, key)

    def erase_status(self, key):
        """ Clears the named status """
        sublime_api.view_erase_status(self.view_id, key)

    def extract_completions(self, prefix, tp=-1):
        return sublime_api.view_extract_completions(self.view_id, prefix, tp)

    def find_all_results(self):
        return sublime_api.view_find_all_results(self.view_id)

    def find_all_results_with_text(self):
        return sublime_api.view_find_all_results_with_text(self.view_id)

    def command_history(self, delta, modifying_only=False):
        """
        Returns the command name, command arguments, and repeat count for the
        given history entry, as stored in the undo / redo stack.

        Index 0 corresponds to the most recent command, -1 the command before
        that, and so on. Positive values for `delta` indicates to look in the
        redo stack for commands. If the undo / redo history doesn't extend far
        enough, then `(None, None, 0)` will be returned.

        Setting `modifying_only` to `True` will only return entries that
        modified the buffer
        """
        return sublime_api.view_command_history(self.view_id, delta, modifying_only)

    def overwrite_status(self):
        """ Returns the overwrite status, which the user normally toggles via the insert key """
        return sublime_api.view_get_overwrite_status(self.view_id)

    def set_overwrite_status(self, value):
        """ Sets the overwrite status """
        sublime_api.view_set_overwrite_status(self.view_id, value)

    def show_popup_menu(self, items, on_select, flags=0):
        """
        Shows a pop up menu at the caret, to select an item in a list. `on_done`
        will be called once, with the index of the selected item. If the pop up
        menu was cancelled, `on_done` will be called with an argument of -1.

        `items` is a list of strings.

        `flags` is currently unused
        """
        return sublime_api.view_show_popup_table(self.view_id, items, on_select, flags, -1)

    def show_popup(
        self,
        content,
        flags=0,
        location=-1,
        max_width=320,
        max_height=240,
        on_navigate=None,
        on_hide=None,
    ):
        """
        Shows a popup displaying HTML content.

        * `flags` is a bitwise combination of the following:

        `COOPERATE_WITH_AUTO_COMPLETE`: Causes the popup to display next to the auto complete menu
        `HIDE_ON_MOUSE_MOVE`: Causes the popup to hide when the mouse is moved, clicked or scrolled
        `HIDE_ON_MOUSE_MOVE_AWAY`: Causes the popup to hide when the mouse is moved
                                    (unless towards the popup), or when clicked or scrolled
        * `location` sets the location of the popup, if -1 (default) will display
        the popup at the cursor, otherwise a text point should be passed.

        * `max_width` and `max_height` set the maximum dimensions for the popup,
        after which scroll bars will be displayed.

        * `on_navigate` is a callback that should accept a string contents of the
        href attribute on the link the user clicked.

        * `on_hide` is called when the popup is hidden
        """
        sublime_api.view_show_popup(
            self.view_id, location, content, flags, max_width, max_height, on_navigate, on_hide
        )

    def update_popup(self, content):
        """ Updates the contents of the currently visible popup """
        sublime_api.view_update_popup_content(self.view_id, content)

    def is_popup_visible(self):
        """ Returns if the popup is currently shown """
        return sublime_api.view_is_popup_visible(self.view_id)

    def hide_popup(self):
        """ Hides the popup """
        sublime_api.view_hide_popup(self.view_id)

    def is_auto_complete_visible(self):
        """ Returns wether the auto complete menu is currently visible """
        return sublime_api.view_is_auto_complete_visible(self.view_id)

    def preserve_auto_complete_on_focus_lost(self):
        sublime_api.view_preserve_auto_complete_on_focus_lost(self.view_id)


class Settings:
    def __init__(self, id):
        self.settings_id = id

    def __getitem__(self, key):
        res = sublime_api.settings_get(self.settings_id, key)
        if res is None and not sublime_api.settings_has(self.settings_id, key):
            raise KeyError(repr(key))
        return res

    def __setitem__(self, key, value):
        sublime_api.settings_set(self.settings_id, key, value)

    def __delitem__(self, key):
        sublime_api.settings_erase(self.settings_id, key)

    def __contains__(self, key):
        return sublime_api.settings_has(self.settings_id, key)

    def __repr__(self):
        return f"Settings({self.settings_id!r})"

    def to_dict(self):
        """
        Return the settings as a dict. This is not very fast.
        """
        return sublime_api.settings_to_dict(self.settings_id)

    def setdefault(self, key, value):
        if sublime_api.settings_has(self.settings_id, key):
            return sublime_api.settings_get(self.settings_id, key)
        sublime_api.settings_set(self.settings_id, key, value)
        return value

    def update(self, other=(), /, **kwargs):
        if isinstance(other, collections.abc.Mapping):
            for key in other:
                self[key] = other[key]
        elif hasattr(other, "keys"):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value

        for key, value in kwargs.items():
            self[key] = value

    def get(self, key, default=None):
        """
        Returns the named setting, or `default` if it's not defined
        If not passed, `default` will have a value of `None`
        """
        if default is not None:
            return sublime_api.settings_get_default(self.settings_id, key, default)
        else:
            return sublime_api.settings_get(self.settings_id, key)

    def has(self, key):
        """
        Returns `True` if the named option exists in this set of Settings or
        one of its parents
        """
        return sublime_api.settings_has(self.settings_id, key)

    def set(self, key, value):
        """ Sets the named setting. Only primitive types, lists, and dicts are accepted """
        sublime_api.settings_set(self.settings_id, key, value)

    def erase(self, key):
        """ Removes the named setting. Does not remove it from any parent Settings """
        sublime_api.settings_erase(self.settings_id, key)

    def add_on_change(self, tag, callback):
        """ Register a `callback` to be run whenever a setting in this object is changed """
        sublime_api.settings_add_on_change(self.settings_id, tag, callback)

    def clear_on_change(self, tag):
        """ Remove all callbacks registered with the given `tag` """
        sublime_api.settings_clear_on_change(self.settings_id, tag)


class Phantom:
    """
    Creates a phantom attached to a region

    * `content` is HTML to be processed by _minihtml_.

    * `layout` must be one of:

    - `LAYOUT_INLINE`: Display the phantom in between the region and the point following.
    - `LAYOUT_BELOW`: Display the phantom in space below the current line,
                    left-aligned with the region.
    - `LAYOUT_BLOCK`: Display the phantom in space below the current line,
    left-aligned with the beginning of the line.

    * `on_navigate` is an optional callback that should accept a single string
    parameter, that is the _href_ attribute of the link clicked.
    """

    def __init__(self, region, content, layout, on_navigate=None):
        self.region = region
        self.content = content
        self.layout = layout
        self.on_navigate = on_navigate
        self.id = None

    def __eq__(self, rhs):
        # Note that self.id is not considered
        return (
            self.region == rhs.region
            and self.content == rhs.content
            and self.layout == rhs.layout
            and self.on_navigate == rhs.on_navigate
        )

    def __repr__(self):
        return (
            f"Phantom({self.region!r}, {self.content!r}, "
            f"{self.layout!r}, on_navigate={self.on_navigate!r})"
        )

    def to_tuple(self):
        """ Returns a tuple of this phantom.

        Use this to uniquely identify a phantom in a set or similar. Phantoms
        can't be used for that directly as they may be mutated.

        The phantom's range will also be returned as a tuple.
        """
        return (self.region.to_tuple(), self.content, self.layout, self.on_navigate)


class PhantomSet:
    def __init__(self, view, key=""):
        self.view = view
        self.key = key
        self.phantoms = []

    def __del__(self):
        for p in self.phantoms:
            self.view.erase_phantom_by_id(p.id)

    def __repr__(self):
        return f"PhantomSet({self.view!r}, key={self.key!r})"

    def update(self, new_phantoms):
        new_phantoms = {p.to_tuple(): p for p in new_phantoms}

        # Update the list of phantoms that exist in the text buffer with their
        # current location
        regions = self.view.query_phantoms([p.id for p in self.phantoms])
        for phantom, region in zip(self.phantoms, regions):
            phantom.region = region

        current_phantoms = {p.to_tuple(): p for p in self.phantoms}

        for key, p in new_phantoms.items():
            try:
                # Phantom already exists, copy the id from the current one
                p.id = current_phantoms[key].id
            except KeyError:
                p.id = self.view.add_phantom(self.key, p.region, p.content, p.layout, p.on_navigate)

        new_phantom_ids = set([p.id for p in new_phantoms.values()])

        for p in self.phantoms:
            # if the region is -1, then it's already been deleted, no need to
            # call erase
            if p.id not in new_phantom_ids and p.region != Region(-1):
                self.view.erase_phantom_by_id(p.id)

        self.phantoms = [p for p in new_phantoms.values()]


class Html:
    __slots__ = ["data"]

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Html({self.data})"


class CompletionList:
    def __init__(self, completions=None, flags=0):
        self.target = None
        self.completions = completions
        self.flags = flags

    def __repr__(self):
        return f"CompletionList(completions={self.completions!r}, flags={self.flags!r})"

    def _set_target(self, target):
        if self.completions is not None:
            target.completions_ready(self.completions, self.flags)
        else:
            self.target = target

    def set_completions(self, completions, flags=0):
        assert self.completions is None
        assert flags is not None

        self.completions = completions
        self.flags = flags

        if self.target is not None:
            self.target.completions_ready(completions, flags)


class CompletionItem:
    def __init__(
        self,
        trigger,
        annotation="",
        completion="",
        completion_format=COMPLETION_FORMAT_TEXT,
        kind=KIND_AMBIGUOUS,
        details="",
    ):

        self.trigger = trigger
        self.annotation = annotation
        self.completion = completion
        self.completion_format = completion_format
        self.kind = kind
        self.details = details
        self.flags = 0

    def __eq__(self, rhs):
        if self.trigger != rhs.trigger:
            return False
        if self.annotation != rhs.annotation:
            return False
        if self.completion != rhs.completion:
            return False
        if self.completion_format != rhs.completion_format:
            return False
        if tuple(self.kind) != tuple(rhs.kind):
            return False
        if self.details != rhs.details:
            return False
        if self.flags != rhs.flags:
            return False
        return True

    def __repr__(self):
        return (
            f"CompletionItem({self.trigger!r}, "
            f"annotation={self.annotation!r}, "
            f"completion={self.completion!r}, "
            f"completion_format={self.completion_format!r}, "
            f"kind={self.kind!r}, details={self.details!r})"
        )

    @classmethod
    def snippet_completion(cls, trigger, snippet, annotation="", kind=KIND_SNIPPET, details=""):

        return CompletionItem(
            trigger, annotation, snippet, COMPLETION_FORMAT_SNIPPET, kind, details
        )

    @classmethod
    def command_completion(
        cls, trigger, command, args={}, annotation="", kind=KIND_AMBIGUOUS, details=""
    ):

        completion = command + " " + encode_value(args)

        return CompletionItem(
            trigger, annotation, completion, COMPLETION_FORMAT_COMMAND, kind, details
        )
