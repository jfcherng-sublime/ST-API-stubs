# This file is maintained on https://github.com/jfcherng-sublime/ST-API-stubs
# ST version: 4147

from __future__ import annotations

import enum
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, Reversible, Sequence, Tuple, TypeVar, overload

from _sublime_types import HasKeysMethod
from sublime_types import DIP, CommandArgs, CompletionValue, Kind, Point, Value, Vector

T_Value = TypeVar("T_Value", bound=Value | None)


class HoverZone(enum.IntEnum):
    """
    A zone in an open text sheet where the mouse may hover.

    See `EventListener.on_hover` and `ViewEventListener.on_hover`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``HOVER_`` prefix.

    .. since:: 4132 3.8
    """

    TEXT = 1
    """ The mouse is hovered over the text. """
    GUTTER = 2
    """ The mouse is hovered over the gutter. """
    MARGIN = 3
    """ The mouse is hovered in the white space to the right of a line. """


HOVER_TEXT = HoverZone.TEXT
HOVER_GUTTER = HoverZone.GUTTER
HOVER_MARGIN = HoverZone.MARGIN


class NewFileFlags(enum.IntFlag):
    """
    Flags for creating/opening files in various ways.

    See `Window.new_html_sheet`, `Window.new_file` and `Window.open_file`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    ENCODED_POSITION = 1
    """
    Indicates that the file name should be searched for a ``:row`` or
    ``:row:col`` suffix.
    """
    TRANSIENT = 4
    """
    Open the file as a preview only: it won't have a tab assigned it until
    modified.
    """
    FORCE_GROUP = 8
    """
    Don't select the file if it is open in a different group. Instead make a new
    clone of that file in the desired group.
    """
    SEMI_TRANSIENT = 16
    """
    If a sheet is newly created, it will be set to semi-transient.
    Semi-transient sheets generally replace other semi-transient sheets. This
    is used for the side-bar preview. Only valid with `ADD_TO_SELECTION` or
    `REPLACE_MRU`.

    .. since:: 4096
    """
    ADD_TO_SELECTION = 32
    """
    Add the file to the currently selected sheets in the group.

    .. since:: 4050
    """
    REPLACE_MRU = 64
    """
    Causes the sheet to replace the most-recently used sheet in the current sheet selection.

    .. since:: 4096
    """
    CLEAR_TO_RIGHT = 128
    """
    All currently selected sheets to the right of the most-recently used sheet
    will be unselected before opening the file. Only valid in combination with
    `ADD_TO_SELECTION`.

    .. since:: 4100
    """
    FORCE_CLONE = 256
    """
    Don't select the file if it is open. Instead make a new clone of that file in the desired
    group.

    .. :since:: next
    """


ENCODED_POSITION = NewFileFlags.ENCODED_POSITION
TRANSIENT = NewFileFlags.TRANSIENT
FORCE_GROUP = NewFileFlags.FORCE_GROUP
SEMI_TRANSIENT = NewFileFlags.SEMI_TRANSIENT
ADD_TO_SELECTION = NewFileFlags.ADD_TO_SELECTION
REPLACE_MRU = NewFileFlags.REPLACE_MRU
CLEAR_TO_RIGHT = NewFileFlags.CLEAR_TO_RIGHT
FORCE_CLONE = NewFileFlags.FORCE_CLONE


class FindFlags(enum.IntFlag):
    """
    Flags for use when searching through a `View`.

    See `View.find` and `View.find_all`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    IGNORECASE = 2
    """ Whether case should be considered when matching the find pattern. """
    LITERAL = 1
    """ Whether the find pattern should be matched literally or as a regex. """


IGNORECASE = FindFlags.IGNORECASE
LITERAL = FindFlags.LITERAL


class QuickPanelFlags(enum.IntFlag):
    """
    Flags for use with a quick panel.

    See `Window.show_quick_panel`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    MONOSPACE_FONT = 1
    """ Use a monospace font. """
    KEEP_OPEN_ON_FOCUS_LOST = 2
    """ Keep the quick panel open if the window loses input focus. """
    WANT_EVENT = 4
    """
    Pass a second parameter to the ``on_done`` callback, a `Event`.

    .. since:: 4096
    """


MONOSPACE_FONT = QuickPanelFlags.MONOSPACE_FONT
KEEP_OPEN_ON_FOCUS_LOST = QuickPanelFlags.KEEP_OPEN_ON_FOCUS_LOST
WANT_EVENT = QuickPanelFlags.WANT_EVENT


class PopupFlags(enum.IntFlag):
    """
    Flags for use with popups.

    See `View.show_popup`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    COOPERATE_WITH_AUTO_COMPLETE = 2
    """ Causes the popup to display next to the auto complete menu. """
    HIDE_ON_MOUSE_MOVE = 4
    """
    Causes the popup to hide when the mouse is moved, clicked or scrolled.
    """
    HIDE_ON_MOUSE_MOVE_AWAY = 8
    """
    Causes the popup to hide when the mouse is moved (unless towards the popup),
    or when clicked or scrolled.
    """
    KEEP_ON_SELECTION_MODIFIED = 16
    """
    Prevent the popup from hiding when the selection is modified.

    .. since:: 4057
    """
    HIDE_ON_CHARACTER_EVENT = 32
    """
    Hide the popup when a character is typed.

    .. since:: 4057
    """


# Deprecated
HTML = 1
COOPERATE_WITH_AUTO_COMPLETE = PopupFlags.COOPERATE_WITH_AUTO_COMPLETE
HIDE_ON_MOUSE_MOVE = PopupFlags.HIDE_ON_MOUSE_MOVE
HIDE_ON_MOUSE_MOVE_AWAY = PopupFlags.HIDE_ON_MOUSE_MOVE_AWAY
KEEP_ON_SELECTION_MODIFIED = PopupFlags.KEEP_ON_SELECTION_MODIFIED
HIDE_ON_CHARACTER_EVENT = PopupFlags.HIDE_ON_CHARACTER_EVENT


class RegionFlags(enum.IntFlag):
    """
    Flags for use with added regions. See `View.add_regions`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    DRAW_EMPTY = 1
    """ Draw empty regions with a vertical bar. By default, they aren't drawn at all. """
    HIDE_ON_MINIMAP = 2
    """ Don't show the regions on the minimap. """
    DRAW_EMPTY_AS_OVERWRITE = 4
    """ Draw empty regions with a horizontal bar instead of a vertical one. """
    PERSISTENT = 16
    """ Save the regions in the session. """
    DRAW_NO_FILL = 32
    """ Disable filling the regions, leaving only the outline. """
    HIDDEN = 128
    """ Don't draw the regions.  """
    DRAW_NO_OUTLINE = 256
    """ Disable drawing the outline of the regions. """
    DRAW_SOLID_UNDERLINE = 512
    """ Draw a solid underline below the regions. """
    DRAW_STIPPLED_UNDERLINE = 1024
    """ Draw a stippled underline below the regions. """
    DRAW_SQUIGGLY_UNDERLINE = 2048
    """ Draw a squiggly underline below the regions. """
    NO_UNDO = 8192


DRAW_EMPTY = RegionFlags.DRAW_EMPTY
HIDE_ON_MINIMAP = RegionFlags.HIDE_ON_MINIMAP
DRAW_EMPTY_AS_OVERWRITE = RegionFlags.DRAW_EMPTY_AS_OVERWRITE
PERSISTENT = RegionFlags.PERSISTENT
DRAW_NO_FILL = RegionFlags.DRAW_NO_FILL
# Deprecated, use DRAW_NO_FILL instead
DRAW_OUTLINED = DRAW_NO_FILL
DRAW_NO_OUTLINE = RegionFlags.DRAW_NO_OUTLINE
DRAW_SOLID_UNDERLINE = RegionFlags.DRAW_SOLID_UNDERLINE
DRAW_STIPPLED_UNDERLINE = RegionFlags.DRAW_STIPPLED_UNDERLINE
DRAW_SQUIGGLY_UNDERLINE = RegionFlags.DRAW_SQUIGGLY_UNDERLINE
NO_UNDO = RegionFlags.NO_UNDO
HIDDEN = RegionFlags.HIDDEN


class QueryOperator(enum.IntEnum):
    """
    Enumeration of operators able to be used when querying contexts.

    See `EventListener.on_query_context` and
    `ViewEventListener.on_query_context`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``OP_`` prefix.

    .. since:: 4132 3.8
    """

    EQUAL = 0
    NOT_EQUAL = 1
    REGEX_MATCH = 2
    NOT_REGEX_MATCH = 3
    REGEX_CONTAINS = 4
    NOT_REGEX_CONTAINS = 5


OP_EQUAL = QueryOperator.EQUAL
OP_NOT_EQUAL = QueryOperator.NOT_EQUAL
OP_REGEX_MATCH = QueryOperator.REGEX_MATCH
OP_NOT_REGEX_MATCH = QueryOperator.NOT_REGEX_MATCH
OP_REGEX_CONTAINS = QueryOperator.REGEX_CONTAINS
OP_NOT_REGEX_CONTAINS = QueryOperator.NOT_REGEX_CONTAINS


class PointClassification(enum.IntFlag):
    """
    Flags that identify characteristics about a `Point` in a text sheet. See
    `View.classify`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``CLASS_`` prefix.

    .. since:: 4132 3.8
    """

    NONE = 0
    WORD_START = 1
    """ The point is the start of a word. """
    WORD_END = 2
    """ The point is the end of a word. """
    PUNCTUATION_START = 4
    """ The point is the start of a sequence of punctuation characters. """
    PUNCTUATION_END = 8
    """ The point is the end of a sequence of punctuation characters. """
    SUB_WORD_START = 16
    """ The point is the start of a sub-word. """
    SUB_WORD_END = 32
    """ The point is the end of a sub-word. """
    LINE_START = 64
    """ The point is the start of a line. """
    LINE_END = 128
    """ The point is the end of a line. """
    EMPTY_LINE = 256
    """ The point is an empty line. """


CLASS_WORD_START = PointClassification.WORD_START
CLASS_WORD_END = PointClassification.WORD_END
CLASS_PUNCTUATION_START = PointClassification.PUNCTUATION_START
CLASS_PUNCTUATION_END = PointClassification.PUNCTUATION_END
CLASS_SUB_WORD_START = PointClassification.SUB_WORD_START
CLASS_SUB_WORD_END = PointClassification.SUB_WORD_END
CLASS_LINE_START = PointClassification.LINE_START
CLASS_LINE_END = PointClassification.LINE_END
CLASS_EMPTY_LINE = PointClassification.EMPTY_LINE


class AutoCompleteFlags(enum.IntFlag):
    """
    Flags controlling how asynchronous completions function. See
    `CompletionList`.

    For backwards compatibility these values are also available outside this
    enumeration (without a prefix).

    .. since:: 4132 3.8
    """

    NONE = 0
    INHIBIT_WORD_COMPLETIONS = 8
    """
    Prevent Sublime Text from showing completions based on the contents of the
    view.
    """
    INHIBIT_EXPLICIT_COMPLETIONS = 16
    """
    Prevent Sublime Text from showing completions based on
    :path:`.sublime-completions` files.
    """
    DYNAMIC_COMPLETIONS = 32
    """
    If completions should be re-queried as the user types.

    .. since:: 4057
    """
    INHIBIT_REORDER = 128
    """
    Prevent Sublime Text from changing the completion order.

    .. since:: 4074
    """


INHIBIT_WORD_COMPLETIONS = AutoCompleteFlags.INHIBIT_WORD_COMPLETIONS
INHIBIT_EXPLICIT_COMPLETIONS = AutoCompleteFlags.INHIBIT_EXPLICIT_COMPLETIONS
DYNAMIC_COMPLETIONS = AutoCompleteFlags.DYNAMIC_COMPLETIONS
INHIBIT_REORDER = AutoCompleteFlags.INHIBIT_REORDER


class CompletionItemFlags(enum.IntFlag):
    """:meta private:"""

    NONE = 0
    KEEP_PREFIX = 1


COMPLETION_FLAG_KEEP_PREFIX = CompletionItemFlags.KEEP_PREFIX


class DialogResult(enum.IntEnum):
    """
    The result from a *yes / no / cancel* dialog. See `yes_no_cancel_dialog`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``DIALOG_`` prefix.

    .. since:: 4132 3.8
    """

    CANCEL = 0
    YES = 1
    NO = 2


DIALOG_CANCEL = DialogResult.CANCEL
DIALOG_YES = DialogResult.YES
DIALOG_NO = DialogResult.NO


class UIElement(enum.IntEnum):
    """:meta private:"""

    SIDE_BAR = 1
    MINIMAP = 2
    TABS = 4
    STATUS_BAR = 8
    MENU = 16
    OPEN_FILES = 32


class PhantomLayout(enum.IntEnum):
    """
    How a `Phantom` should be positioned. See `PhantomSet`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``LAYOUT_`` prefix.

    .. since:: 4132 3.8
    """

    INLINE = 0
    """
    The phantom is positioned inline with the text at the beginning of its
    `Region`.
    """
    BELOW = 1
    """
    The phantom is positioned below the line, left-aligned with the beginning of
    its `Region`.
    """
    BLOCK = 2
    """
    The phantom is positioned below the line, left-aligned with the beginning of
    the line.
    """


LAYOUT_INLINE = PhantomLayout.INLINE
LAYOUT_BELOW = PhantomLayout.BELOW
LAYOUT_BLOCK = PhantomLayout.BLOCK


class KindId(enum.IntEnum):
    """
    For backwards compatibility these values are also available outside this
    enumeration with a ``KIND_ID_`` prefix.

    .. since:: 4132 3.8
    """

    AMBIGUOUS = 0
    KEYWORD = 1
    TYPE = 2
    FUNCTION = 3
    NAMESPACE = 4
    NAVIGATION = 5
    MARKUP = 6
    VARIABLE = 7
    SNIPPET = 8

    # These should only be used for QuickPanelItem
    # and ListInputItem, not for CompletionItem
    COLOR_REDISH = 9
    COLOR_ORANGISH = 10
    COLOR_YELLOWISH = 11
    COLOR_GREENISH = 12
    COLOR_CYANISH = 13
    COLOR_BLUISH = 14
    COLOR_PURPLISH = 15
    COLOR_PINKISH = 16
    COLOR_DARK = 17
    COLOR_LIGHT = 18


KIND_ID_AMBIGUOUS = KindId.AMBIGUOUS
KIND_ID_KEYWORD = KindId.KEYWORD
KIND_ID_TYPE = KindId.TYPE
KIND_ID_FUNCTION = KindId.FUNCTION
KIND_ID_NAMESPACE = KindId.NAMESPACE
KIND_ID_NAVIGATION = KindId.NAVIGATION
KIND_ID_MARKUP = KindId.MARKUP
KIND_ID_VARIABLE = KindId.VARIABLE
KIND_ID_SNIPPET = KindId.SNIPPET
KIND_ID_COLOR_REDISH = KindId.COLOR_REDISH
KIND_ID_COLOR_ORANGISH = KindId.COLOR_ORANGISH
KIND_ID_COLOR_YELLOWISH = KindId.COLOR_YELLOWISH
KIND_ID_COLOR_GREENISH = KindId.COLOR_GREENISH
KIND_ID_COLOR_CYANISH = KindId.COLOR_CYANISH
KIND_ID_COLOR_BLUISH = KindId.COLOR_BLUISH
KIND_ID_COLOR_PURPLISH = KindId.COLOR_PURPLISH
KIND_ID_COLOR_PINKISH = KindId.COLOR_PINKISH
KIND_ID_COLOR_DARK = KindId.COLOR_DARK
KIND_ID_COLOR_LIGHT = KindId.COLOR_LIGHT

KIND_AMBIGUOUS = (KindId.AMBIGUOUS, "", "")
"""
.. since:: 4052
"""
KIND_KEYWORD = (KindId.KEYWORD, "", "")
"""
.. since:: 4052
"""
KIND_TYPE = (KindId.TYPE, "", "")
"""
.. since:: 4052
"""
KIND_FUNCTION = (KindId.FUNCTION, "", "")
"""
.. since:: 4052
"""
KIND_NAMESPACE = (KindId.NAMESPACE, "", "")
"""
.. since:: 4052
"""
KIND_NAVIGATION = (KindId.NAVIGATION, "", "")
"""
.. since:: 4052
"""
KIND_MARKUP = (KindId.MARKUP, "", "")
"""
.. since:: 4052
"""
KIND_VARIABLE = (KindId.VARIABLE, "", "")
"""
.. since:: 4052
"""
KIND_SNIPPET = (KindId.SNIPPET, "s", "Snippet")
"""
.. since:: 4052
"""


class SymbolSource(enum.IntEnum):
    """
    See `Window.symbol_locations`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``SYMBOL_SOURCE_`` prefix.

    .. since:: 4132 3.8
    """

    ANY = 0
    """
    Use any source - both the index and open files.

    .. since:: 4085
    """
    INDEX = 1
    """
    Use the index created when scanning through files in a project folder.

    .. since:: 4085
    """
    OPEN_FILES = 2
    """
    Use the open files, unsaved or otherwise.

    .. since:: 4085
    """


SYMBOL_SOURCE_ANY = SymbolSource.ANY
SYMBOL_SOURCE_INDEX = SymbolSource.INDEX
SYMBOL_SOURCE_OPEN_FILES = SymbolSource.OPEN_FILES


class SymbolType(enum.IntEnum):
    """
    See `Window.symbol_locations` and `View.indexed_symbol_regions`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``SYMBOL_TYPE_`` prefix.

    .. since:: 4132 3.8
    """

    ANY = 0
    """ Any symbol type - both definitions and references.

    .. since:: 4085
    """
    DEFINITION = 1
    """
    Only definitions.

    .. since:: 4085
    """
    REFERENCE = 2
    """
    Only references.

    .. since:: 4085
    """


SYMBOL_TYPE_ANY = SymbolType.ANY
SYMBOL_TYPE_DEFINITION = SymbolType.DEFINITION
SYMBOL_TYPE_REFERENCE = SymbolType.REFERENCE


class CompletionFormat(enum.IntEnum):
    """
    The format completion text can be in. See `CompletionItem`.

    For backwards compatibility these values are also available outside this
    enumeration with a ``COMPLETION_FORMAT_`` prefix.

    .. since:: 4132 3.8
    """

    TEXT = 0
    """
    Plain text, upon completing the text is inserted verbatim.

    .. since:: 4050
    """
    SNIPPET = 1
    """
    A snippet, with ``$`` variables. See also
    `CompletionItem.snippet_completion`.

    .. since:: 4050
    """
    COMMAND = 2
    """
    A command string, in the format returned by `format_command()`. See also
    `CompletionItem.command_completion()`.

    .. since:: 4050
    """


COMPLETION_FORMAT_TEXT = CompletionFormat.TEXT
COMPLETION_FORMAT_SNIPPET = CompletionFormat.SNIPPET
COMPLETION_FORMAT_COMMAND = CompletionFormat.COMMAND


def version() -> str:
    """
    :returns: The version number.
    """
    ...


def platform() -> Literal["osx", "linux", "windows"]:
    """
    :returns: The platform which the plugin is being run on.
    """
    ...


def arch() -> Literal["x32", "x64", "arm64"]:
    """
    :returns: The CPU architecture.
    """
    ...


def channel() -> Literal["dev", "stable"]:
    """
    :returns: The release channel of this build of Sublime Text.
    """
    ...


def executable_path() -> str:
    """
    .. since:: 4081
        This may be called at import time.

    :returns: The path to the main Sublime Text executable.
    """
    ...


def executable_hash() -> tuple[str, str, str]:
    """
    .. since:: 4081
        This may be called at import time.

    :returns: A tuple uniquely identifying the installation of Sublime Text.
    """
    ...


def packages_path() -> str:
    """
    .. since:: 4081
        This may be called at import time.

    :returns: The path to the "Packages" folder.
    """
    ...


def installed_packages_path() -> str:
    """
    .. since:: 4081
        This may be called at import time.

    :returns: The path to the "Installed Packages" folder.
    """
    ...


def cache_path() -> str:
    """
    .. since:: 4081
        This may be called at import time.

    :returns: The path where Sublime Text stores cache files.
    """
    ...


def status_message(msg: str) -> None:
    """Show a message in the status bar."""


def error_message(msg: str) -> None:
    """Display an error dialog."""


def message_dialog(msg: str) -> None:
    """Display a message dialog."""


def ok_cancel_dialog(msg: str, ok_title: str = "", title: str = "") -> bool:
    """
    Show a *ok / cancel* question dialog.

    :param msg: The message to show in the dialog.
    :param ok_title: Text to display on the *ok* button.
    :param title: Title for the dialog. Windows only. :since:`4099`

    :returns: Whether the user pressed the *ok* button.
    """
    ...


def yes_no_cancel_dialog(msg: str, yes_title: str = "", no_title: str = "", title: str = "") -> DialogResult:
    """
    Show a *yes / no / cancel* question dialog.

    :param msg: The message to show in the dialog.
    :param yes_title: Text to display on the *yes* button.
    :param no_title: Text to display on the *no* button.
    :param title: Title for the dialog. Windows only. :since:`4099`
    """
    ...


@overload
def open_dialog(
    callback: Callable[[None | Sequence[str]], None],
    file_types: Sequence[Tuple[str, Sequence[str]]],
    directory: None | str,
    multi_select: Literal[True],
    allow_folders: bool = False,
) -> None:
    ...


@overload
def open_dialog(
    callback: Callable[[None | Sequence[str]], None],
    file_types: Sequence[Tuple[str, Sequence[str]]] = [],
    directory: None | str = None,
    allow_folders: bool = False,
    *,
    multi_select: Literal[True],
) -> None:
    ...


@overload
def open_dialog(
    callback: Callable[[None | str], None],
    file_types: Sequence[Tuple[str, Sequence[str]]] = [],
    directory: None | str = None,
    multi_select: bool = False,
    allow_folders: bool = False,
) -> None:
    ...


def open_dialog(
    callback: Callable[[None | Sequence[str]], None],
    file_types: Sequence[Tuple[str, Sequence[str]]] = [],
    directory: str | None = None,
    multi_select: bool = False,
    allow_folders: bool = False,
) -> None:
    """
    Show the open file dialog.

    .. since:: 4075

    :param callback: Called with selected path(s) or ``None`` once the dialog is closed.
    :param file_types: A list of allowed file types, consisting of a description
                       and a list of allowed extensions.
    :param directory: The directory the dialog should start in.  Will use the
                      virtual working directory if not provided.
    :param multi_select: Whether to allow selecting multiple files. When ``True``
                         the callback will be called with a list.
    :param allow_folders: Whether to also allow selecting folders. Only works on
                          macOS. If you only want to select folders use
                          `select_folder_dialog`.
    """


def save_dialog(
    callback: Callable[[str | None], None],
    file_types: list[tuple[str, list[str]]] = [],
    directory: str | None = None,
    name: str | None = None,
    extension: str | None = None,
) -> None:
    """
    Show the save file dialog

    .. since:: 4075

    :param callback: Called with selected path or ``None`` once the dialog is closed.
    :param file_types: A list of allowed file types, consisting of a description
                       and a list of allowed extensions.
    :param directory: The directory the dialog should start in.  Will use the
                      virtual working directory if not provided.
    :param name: The default name of the file in the save dialog.
    :param extension: The default extension used in the save dialog.
    """


def select_folder_dialog(
    callback: Callable[[str | list[str] | None], None],
    directory: str | None = None,
    multi_select: bool = False,
) -> None:
    """
    Show the select folder dialog.

    .. since:: 4075

    :param callback: Called with selected path(s) or ``None`` once the dialog is closed.
    :param directory: The directory the dialog should start in.  Will use the
                      virtual working directory if not provided.
    :param multi_select: Whether to allow selecting multiple files. When ``True``
                         the callback will be called with a list.
    """


def run_command(cmd: str, args: CommandArgs = None) -> None:
    """
    Run the named `ApplicationCommand`.
    """


def format_command(cmd: str, args: CommandArgs = None) -> str:
    """
    Create a "command string" from a ``cmd`` name and ``args`` arguments. This
    is used when constructing a command-based `CompletionItem`.

    .. since:: 4075
    """
    ...


def html_format_command(cmd: str, args: CommandArgs = None) -> str:
    """
    :returns: An escaped "command string" for usage in HTML popups and sheets.

    .. since:: 4075
    """
    ...


def command_url(cmd: str, args: CommandArgs = None) -> str:
    """
    :returns: A HTML embeddable URL for a command.

    .. since:: 4075
    """
    ...


def get_clipboard_async(callback: Callable[[str], Any], size_limit: int = 16777216) -> None:
    """
    Get the contents of the clipboard in a callback.

    For performance reasons if the size of the clipboard content is bigger than
    ``size_limit``, an empty string will be passed to the callback.

    .. since:: 4075
    """


def get_clipboard(size_limit: int = 16777216) -> str:
    """
    Get the contents of the clipboard.

    For performance reasons if the size of the clipboard content is bigger than
    ``size_limit``, an empty string will be returned.

    :deprecated: Use `get_clipboard_async` instead. :since:`4075`
    """
    ...


def set_clipboard(text: str) -> None:
    """Set the contents of the clipboard."""


def log_commands(flag: bool | None = None) -> None:
    """
    Control whether commands are logged to the console when run.

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_commands() -> bool:
    """
    Get whether command logging is enabled.

    .. since:: 4099
    """
    ...


def log_input(flag: bool | None = None) -> None:
    """
    Control whether all key presses will be logged to the console. Use this to
    find the names of certain keys on the keyboard.

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_input() -> bool:
    """
    Get whether input logging is enabled.

    .. since:: 4099
    """
    ...


def log_fps(flag: bool | None = None) -> None:
    """
    Control whether rendering timings like frames per second get logged.

    .. since:: 4099

    :param flag: Whether to log. Pass ``None`` to toggle logging.
    """


def get_log_fps() -> bool:
    """
    Get whether fps logging is enabled.

    .. since:: 4099
    """
    ...


def log_result_regex(flag: bool | None = None) -> None:
    """
    Control whether result regex logging is enabled. Use this to debug
    ``"file_regex"`` and ``"line_regex"`` in build systems.

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_result_regex() -> bool:
    """
    Get whether result regex logging is enabled.

    .. since:: 4099
    """
    ...


def log_indexing(flag: bool | None = None) -> None:
    """
    Control whether indexing logs are printed to the console.

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_indexing() -> bool:
    """
    Get whether indexing logging is enabled.

    .. since:: 4099
    """
    ...


def log_build_systems(flag: bool | None = None) -> None:
    """
    Control whether build system logs are printed to the console.

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_build_systems() -> bool:
    """
    Get whether build system logging is enabled.

    .. since:: 4099
    """
    ...


def log_control_tree(flag: bool | None = None) -> None:
    """
    Control whether control tree logging is enabled. When enabled clicking with
    ctrl+alt will log the control tree under the mouse to the console.

    .. since:: 4064

    :param flag: Whether to log. :since:`Passing None toggles logging. <4099>`
    """


def get_log_control_tree() -> bool:
    """
    Get whether control tree logging is enabled.

    .. since:: 4099
    """
    ...


def ui_info() -> dict:
    """
    .. since:: 4096

    :returns: Information about the user interface including top-level keys
              ``system``, ``theme`` and ``color_scheme``.
    """
    ...


def score_selector(scope_name: str, selector: str) -> int:
    """
    Match the ``selector`` against the given ``scope_name``, returning a score for how well they match.

    A score of ``0`` means no match, above ``0`` means a match. Different
    selectors may be compared against the same scope: a higher score means the
    selector is a better match for the scope.
    """
    ...


def load_resource(name: str) -> str:
    """
    Loads the given resource. The name should be in the format "Packages/Default/Main.sublime-menu".

    :raises FileNotFoundError: if resource is not found
    """
    ...


def load_binary_resource(name: str) -> bytes:
    """
    Loads the given resource. The name should be in the format "Packages/Default/Main.sublime-menu".

    :raises FileNotFoundError: if resource is not found
    """
    ...


def find_resources(pattern: str) -> list[str]:
    """
    Finds resources whose file name matches the given glob pattern.
    """
    ...


def encode_value(value: Value | None, pretty: bool = False) -> str:
    """
    Encode a JSON compatible `Value` into a string representation.

    :param pretty: Whether the result should include newlines and be indented.
    """
    ...


def decode_value(data: str) -> Any:
    """
    Decode a JSON string into an object. Note that comments and trailing commas
    are allowed.

    :raises ValueError: If the string is not valid JSON.
    """
    # Return type "Value" is correct but annoying so use "Any"


def expand_variables(value: T_Value, variables: dict[str, str]) -> T_Value:
    """
    Expands any variables in ``value`` using the variables defined in the
    dictionary ``variables``. value may also be a list or dict, in which case the
    structure will be recursively expanded. Strings should use snippet syntax,
    for example: ``expand_variables("Hello, ${name}", {"name": "Foo"})``.
    """
    ...


def load_settings(base_name: str) -> Settings:
    """
    Loads the named settings. The name should include a file name and extension,
    but not a path. The packages will be searched for files matching the
    base_name, and the results will be collated into the settings object.

    Subsequent calls to load_settings() with the base_name will return the same
    object, and not load the settings from disk again.
    """
    ...


def save_settings(base_name: str) -> None:
    """
    Flush any in-memory changes to the named settings object to disk.
    """


def set_timeout(callback: Callable[[], Any], delay: int = 0) -> None:
    """-> None
    Run the ``callback`` in the main thread after the given ``delay``
    (in milliseconds). Callbacks with an equal delay will be run in the order
    they were added.
    """


def set_timeout_async(callback: Callable[[], Any], delay: int = 0) -> None:
    """
    Runs the callback on an alternate thread after the given delay
    (in milliseconds).
    """


def active_window() -> Window:
    """
    :returns: The most recently used `Window`.
    """
    ...


def windows() -> list[Window]:
    """
    :returns: A list of all the open windows.
    """
    ...


def get_macro() -> list[dict]:
    """
    :returns: A list of the commands and args that compromise the currently
              recorded macro. Each ``dict`` will contain the keys ``"command"``
              and ``"args"``.
    """
    ...


def project_history() -> Any:
    """
    :returns: A list of most recently opened workspaces.
              Sublime-project files with the same name are
              listed in place of sublime-workspace files.
    """


def folder_history() -> Any:
    """
    :returns: A list of recent folders added to sublime projects
    """


class Window:
    def __init__(self, id: int) -> None:
        self.window_id: int
        self.settings_object: Settings | None
        self.template_settings_object: Settings | None

    def __hash__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """
        :returns: A number that uniquely identifies this window.
        """
        ...

    def is_valid(self) -> bool:
        """
        Check whether this window is still valid. Will return ``False`` for a
        closed window, for example.
        """
        ...

    def hwnd(self) -> int:
        """
        :returns: A platform specific window handle. Windows only.
        """
        ...

    def active_sheet(self) -> Sheet | None:
        """
        :returns: The currently focused `Sheet`.
        """

    def active_view(self) -> View | None:
        """
        :returns: The currently edited `View`.
        """

    def new_html_sheet(
        self,
        name: str,
        contents: str,
        flags: NewFileFlags = NewFileFlags.NONE,
        group: int = -1,
    ) -> Sheet:
        """
        Construct a sheet with HTML contents rendered using `minihtml`.

        .. since:: 4065

        :param name: The name of the sheet to show in the tab.
        :param contents: The HTML contents of the sheet.
        :param flags: Only `NewFileFlags.TRANSIENT` and
                      `NewFileFlags.ADD_TO_SELECTION` are allowed.
        :param group: The group to add the sheet to. ``-1`` for the active group.
        """
        ...

    def run_command(self, cmd: str, args: CommandArgs = None) -> None:
        """
        Run the named `WindowCommand` with the (optional) given args. This
        method is able to run any sort of command, dispatching the command via
        input focus.
        """

    def new_file(self, flags: NewFileFlags = NewFileFlags.NONE, syntax: str = "") -> View:
        """
        Create a new empty file.

        :param flags: Either ``0``, `NewFileFlags.TRANSIENT` or `NewFileFlags.ADD_TO_SELECTION`.
        :param syntax: The name of the syntax to apply to the file.
        :returns: The view for the file.
        """
        ...

    def open_file(self, fname: str, flags=NewFileFlags.NONE, group: int = -1) -> View:
        """
        Open the named file. If the file is already opened, it will be brought
        to the front. Note that as file loading is asynchronous, operations on
        the returned view won't be possible until its ``is_loading()`` method
        returns ``False``.

        :param fname: The path to the file to open.
        :param flags: `NewFileFlags`
        :param group: The group to add the sheet to. ``-1`` for the active group.
        """
        ...

    def find_open_file(self, fname: str, group: int = -1) -> View | None:
        """
        Find a opened file by file name.

        :param fname: The path to the file to open.
        :param group: The group in which to search for the file. ``-1`` for any group.

        :returns: The `View` to the file or ``None`` if the file isn't open.
        """

    def file_history(self) -> list[str]:
        """
        Get the list of previously opened files. This is the same list
        as *File > Open Recent*.
        """
        ...

    def num_groups(self) -> int:
        """
        :returns: The number of view groups in the window.
        """
        ...

    def active_group(self) -> int:
        """
        :returns: The index of the currently selected group.
        """
        ...

    def focus_group(self, idx: int) -> None:
        """
        Focus the specified group, making it active.
        """

    def focus_sheet(self, sheet: Sheet) -> None:
        """
        Switches to the given `Sheet`.
        """

    def focus_view(self, view: View) -> None:
        """
        Switches to the given `View`.
        """

    def select_sheets(self, sheets: list[Sheet]) -> None:
        """
        Change the selected sheets for the entire window.

        .. since:: 4083
        """

    def bring_to_front(self) -> None:
        """
        Bring the window in front of any other windows.
        """

    def get_sheet_index(self, sheet: Sheet) -> tuple[int, int]:
        """
        :returns: The a tuple of the group and index within the group of the
                  given `Sheet`.
        """
        ...

    def get_view_index(self, view: View) -> tuple[int, int]:
        """
        :returns: The a tuple of the group and index within the group of the
                  given `View`.
        """
        ...

    def set_sheet_index(self, sheet: Sheet, group: int, index: int) -> None:
        """
        Move the given `Sheet` to the given ``group`` at the given ``index``.
        """

    def set_view_index(self, view: View, group: int, index: int) -> None:
        """
        Move the given `View` to the given ``group`` at the given ``index``.
        """

    def move_sheets_to_group(
        self,
        sheets: list[Sheet],
        group: int,
        insertion_idx: int = -1,
        select: bool = True,
    ) -> None:
        """
        Moves all provided sheets to specified group at insertion index
        provided. If an index is not provided defaults to last index of the
        destination group.

        .. since:: 4123

        :param sheets: The sheets to move.
        :param group: The index of the group to move the sheets to.
        :param insertion_idx: The point inside the group at which to insert the sheets.
        :param select: Whether the sheets should be selected after moving them.
        """

    def sheets(self) -> list[Sheet]:
        """
        :returns: All open sheets in the window.
        """
        ...

    def views(self, *, include_transient: bool = False) -> list[View]:
        """
        :param include_transient: Whether the transient sheet should be included.

            .. since:: 4081
        :returns: All open sheets in the window.
        """
        ...

    def selected_sheets(self) -> list[Sheet]:
        """
        .. since:: 4083

        :returns: All selected sheets in the window.
        """
        ...

    def selected_sheets_in_group(self, group: int) -> list[Sheet]:
        """
        .. since:: 4083

        :returns: All selected sheets in the specified group.
        """
        ...

    def active_sheet_in_group(self, group: int) -> Sheet | None:
        """
        :returns: The currently focused `Sheet` in the given group.
        """

    def active_view_in_group(self, group: int) -> View | None:
        """
        :returns: The currently focused `View` in the given group.
        """

    def sheets_in_group(self, group: int) -> list[Sheet]:
        """
        :returns: A list of all sheets in the specified group.
        """
        ...

    def views_in_group(self, group: int) -> list[View]:
        """
        :returns: A list of all views in the specified group.
        """
        ...

    def transient_sheet_in_group(self, group: int) -> Sheet | None:
        """
        :returns: The transient sheet in the specified group.
        """

    def transient_view_in_group(self, group: int) -> View | None:
        """
        :returns: The transient view in the specified group.
        """

    def promote_sheet(self, sheet: Sheet) -> None:
        """
        Promote the 'Sheet' parameter if semi-transient or transient.

        :since: next
        """

    def layout(self) -> dict[str, Any]:
        """
        Get the group layout of the window.
        """
        ...

    def get_layout(self) -> None:
        """
        :deprecated: Use `layout()` instead
        """

    def set_layout(self, layout: dict[str, Any]) -> None:
        """
        Set the group layout of the window.
        """

    def create_output_panel(self, name: str, unlisted: bool = False) -> View:
        """
        Find the view associated with the named output panel, creating it if
        required. The output panel can be shown by running the ``show_panel``
        window command, with the ``panel`` argument set to the name with
        an ``"output."`` prefix.

        The optional ``unlisted`` parameter is a boolean to control if the output
        panel should be listed in the panel switcher.
        """
        ...

    def find_output_panel(self, name: str) -> View | None:
        """
        :returns:
            The `View` associated with the named output panel, or ``None`` if
            the output panel does not exist.
        """

    def destroy_output_panel(self, name: str) -> None:
        """
        Destroy the named output panel, hiding it if currently open.
        """

    def active_panel(self) -> str | None:
        """
        Returns the name of the currently open panel, or None if no panel is
        open. Will return built-in panel names (e.g. ``"console"``, ``"find"``,
        etc) in addition to output panels.
        """

    def panels(self) -> list[str]:
        """
        Returns a list of the names of all panels that have not been marked as
        unlisted. Includes certain built-in panels in addition to output
        panels.
        """
        ...

    def get_output_panel(self, name: str) -> View:
        """:deprecated: Use `create_output_panel` instead."""
        ...

    def show_input_panel(
        self,
        caption: str,
        initial_text: str,
        on_done: Callable[[str], Any] | None,
        on_change: Callable[[str], Any] | None,
        on_cancel: Callable[[], Any] | None,
    ) -> View:
        """
        Shows the input panel, to collect a line of input from the user.

        :param caption: The label to put next to the input widget.
        :param initial_text: The initial text inside the input widget.
        :param on_done: Called with the final input when the user presses ``enter``.
        :param on_change: Called with the input when it's changed.
        :param on_cancel: Called when the user cancels input using ``esc``
        :returns: The `View` used for the input widget.
        """
        ...

    def show_quick_panel(
        self,
        items: list[str] | list[list[str]] | list[QuickPanelItem],
        on_select: Callable[[int], None],
        flags: QuickPanelFlags = QuickPanelFlags.NONE,
        selected_index=-1,
        on_highlight: Callable[[int], None] | None = None,
        placeholder: str | None = None,
    ) -> None:
        """
        Show a quick panel to select an item in a list. on_select will be called
        once, with the index of the selected item. If the quick panel was
        cancelled, on_select will be called with an argument of -1.

        :param items:
            May be either a list of strings, or a list of lists of strings where
            the first item is the trigger and all subsequent strings are
            details shown below.

            .. since:: 4083
                May be a `QuickPanelItem`.
        :param on_select:
            Called with the selected item's index when the quick panel is
            completed. If the panel was cancelled this is called with ``-1``.

            .. since:: 4096
                A second `Event` argument may be passed when the
                `QuickPanelFlags.WANT_EVENT` flag is present.
        :param flags: `QuickPanelFlags` controlling behavior.
        :param selected_index: The initially selected item. ``-1`` for no selection.
        :param on_highlight:
            Called every time the highlighted item in the quick panel is changed.
        :param placeholder:
            Text displayed in the filter input field before any query is typed.
            :since:`4081`
        """

    def is_sidebar_visible(self) -> bool:
        """:returns: Whether the sidebar is visible."""
        ...

    def set_sidebar_visible(self, flag: bool, animate: bool = True) -> None:
        """Hides or shows the sidebar."""
        ...

    def is_minimap_visible(self) -> bool:
        """:returns: Whether the minimap is visible."""
        ...

    def set_minimap_visible(self, flag: bool) -> None:
        """Hides or shows the minimap."""

    def is_status_bar_visible(self) -> bool:
        """:returns: Whether the status bar is visible."""
        ...

    def set_status_bar_visible(self, flag: bool) -> None:
        """Hides or shows the status bar."""

    def get_tabs_visible(self) -> bool:
        """:returns: Whether the tabs are visible."""
        ...

    def set_tabs_visible(self, flag: bool) -> None:
        """Hides or shows the tabs."""

    def is_menu_visible(self) -> bool:
        """:returns: Whether the menu is visible."""
        ...

    def set_menu_visible(self, flag: bool) -> None:
        """Hides or shows the menu."""

    def folders(self) -> list[str]:
        """:returns: A list of the currently open folders in this `Window`."""
        ...

    def project_file_name(self) -> str | None:
        """:returns: The name of the currently opened project file, if any."""

    def workspace_file_name(self) -> str | None:
        """
        .. since:: 4050

        :returns: The name of the currently opened workspace file, if any.
        """

    def project_data(self) -> dict[str, Any]:
        """
        :returns: The project data associated with the current window. The data
                  is in the same format as the contents of a
                  :path:`.sublime-project` file.
        """
        ...

    def set_project_data(self, data: Value) -> None:
        """
        Updates the project data associated with the current window. If the
        window is associated with a :path:`.sublime-project` file, the project
        file will be updated on disk, otherwise the window will store the data
        internally.
        """

    def settings(self) -> Settings:
        """
        :returns: The `Settings` object for this `Window`. Any changes to this
                  settings object will be specific to this window.
        """
        ...

    def template_settings(self) -> Settings:
        """
        :returns: Per-window settings that are persisted in the session, and
                  duplicated into new windows.
        """
        ...

    def symbol_locations(
        self,
        sym: str,
        source: SymbolSource = SymbolSource.ANY,
        type: SymbolType = SymbolType.ANY,
        kind_id: KindId = KindId.AMBIGUOUS,
        kind_letter: str = "",
    ) -> list[SymbolLocation]:
        """
        Find all locations where the symbol ``sym`` is located.

        .. since:: 4085

        :param sym: The name of the symbol.
        :param source: Sources which should be searched for the symbol.
        :param type: The type of symbol to find
        :param kind_id: The `KindId` of the symbol.
        :param kind_letter: The letter representing the kind of the symbol. See `Kind`.
        :return: the found symbol locations.
        """
        ...

    def lookup_symbol_in_index(self, symbol: str) -> list[SymbolLocation]:
        """
        :returns: All locations where the symbol is defined across files in the current project.
        :deprecated: Use `symbol_locations()` instead.
        """
        ...

    def lookup_symbol_in_open_files(self, symbol: str) -> list[SymbolLocation]:
        """
        :returns: All locations where the symbol is defined across open files.
        :deprecated: Use `symbol_locations()` instead.
        """
        ...

    def lookup_references_in_index(self, symbol: str) -> list[SymbolLocation]:
        """
        :returns: All locations where the symbol is referenced across files in the current project.
        :deprecated: Use `symbol_locations()` instead.
        """
        ...

    def lookup_references_in_open_files(self, symbol: str) -> list[SymbolLocation]:
        """
        :returns: All locations where the symbol is referenced across open files.
        :deprecated: Use `symbol_locations()` instead.
        """
        ...

    def extract_variables(self) -> dict[str, str]:
        """
        Get the ``dict`` of contextual keys of the window.

        May contain:
        * ``"packages"``
        * ``"platform"``
        * ``"file"``
        * ``"file_path"``
        * ``"file_name"``
        * ``"file_base_name"``
        * ``"file_extension"``
        * ``"folder"``
        * ``"project"``
        * ``"project_path"``
        * ``"project_name"``
        * ``"project_base_name"``
        * ``"project_extension"``

        This ``dict`` is suitable for use with `expand_variables()`.
        """
        ...

    def status_message(self, msg: str) -> None:
        """Show a message in the status bar."""


class Edit:
    """
    A grouping of buffer modifications.

    Edit objects are passed to `TextCommand`\\ s, and can not be created by the
    user. Using an invalid Edit object, or an Edit object from a different
    `View`, will cause the functions that require them to fail.
    """

    edit_token: int

    def __init__(self, token: int) -> None:
        ...

    def __repr__(self) -> str:
        ...


class Region:
    """
    A singular selection region. This region has a order - ``b`` may be before
    or at ``a``.

    Also commonly used to represent an area of the text buffer, where ordering
    and ``xpos`` are generally ignored.
    """

    __slots__ = ["a", "b", "xpos"]

    def __init__(self, a: Point, b: Point | None = None, xpos: DIP = -1) -> None:
        self.a: Point
        """ The first end of the region. """
        self.b: Point
        """
        The second end of the region. In a selection this is the location of the
        caret. May be less than ``a``.
        """
        self.xpos: DIP
        """
        In a selection this is the target horizontal position of the region.
        This affects behavior when pressing the up or down keys. Use ``-1`` if
        undefined.
        """

    def __iter__(self) -> Iterator[int]:
        """
        Iterate through all the points in the region.

        .. since:: 4023 3.8
        """
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __len__(self) -> int:
        """:returns: The size of the region."""
        ...

    def __eq__(self, rhs: object) -> bool:
        """
        :returns: Whether the two regions are identical. Ignores ``xpos``.
        """
        ...

    def __lt__(self, rhs: Region) -> bool:
        """
        :returns: Whether this region starts before the rhs. The end of the
                  region is used to resolve ties.
        """
        ...

    def __contains__(self, v: Region | Point) -> bool:
        """
        :returns: Whether the provided `Region` or `Point` is entirely contained
                  within this region.

        .. since:: 4023 3.8
        """
        ...

    def to_tuple(self) -> tuple[Point, Point]:
        """
        .. since:: 4075

        :returns: This region as a tuple ``(a, b)``.
        """
        ...

    def empty(self) -> bool:
        """:returns: Whether the region is empty, ie. ``a == b``."""
        ...

    def begin(self) -> Point:
        """:returns: The smaller of ``a`` and ``b``."""
        ...

    def end(self) -> Point:
        """:returns: The larger of ``a`` and ``b``."""
        ...

    def size(self) -> int:
        """Equivalent to `__len__`."""
        ...

    def contains(self, x: Point) -> bool:
        """Equivalent to `__contains__`."""
        ...

    def cover(self, region: Region) -> Region:
        """:returns: A `Region` spanning both regions."""
        ...

    def intersection(self, region: Region) -> Region:
        """:returns: A `Region` covered by both regions."""
        ...

    def intersects(self, region: Region) -> bool:
        """:returns: Whether the provided region intersects this region."""
        ...


class HistoricPosition:
    """
    Provides a snapshot of the row and column info for a `Point`, before changes
    were made to a `View`. This is primarily useful for replaying changes to a
    document.

    .. since:: 4050
    """

    __slots__ = ["pt", "row", "col", "col_utf16", "col_utf8"]

    def __init__(self, pt: Point, row: int, col: int, col_utf16: int, col_utf8: int) -> None:
        self.pt: Point
        """ The offset from the beginning of the `View`. """
        self.row: int
        """ The row the ``.py`` was in when the `HistoricPosition` was recorded. """
        self.col: int
        """ The column the ``.py`` was in when the `HistoricPosition` was recorded, in Unicode characters. """
        self.col_utf16: int
        """
        The value of ``.col``, but in UTF-16 code units.

        .. since:: 4075
        """
        self.col_utf8: int
        """
        The value of ``.col``, but in UTF-8 code units.

        .. since:: 4075
        """

    def __repr__(self) -> str:
        ...


class TextChange:
    """
    Represents a change that occurred to the text of a `View`. This is primarily
    useful for replaying changes to a document.

    .. since:: 4050
    """

    __slots__ = ["a", "b", "len_utf16", "len_utf8", "str"]

    def __init__(self, pa: HistoricPosition, pb: HistoricPosition, len_utf16: int, len_utf8: int, str: str) -> None:
        self.a: HistoricPosition
        """ The beginning `HistoricPosition` of the region that was modified. """
        self.b: HistoricPosition
        """ The ending `HistoricPosition` of the region that was modified. """
        self.len_utf16: int
        """
        The length of the old contents, in UTF-16 code units.

        .. since:: 4075
        """
        self.len_utf8: int
        """
        The length of the old contents, in UTF-8 code units.

        .. since:: 4075
        """
        self.str: str
        """
        A string of the *new* contents of the region specified by ``.a`` and ``.b``.

        :meta noindex:
        """

    def __repr__(self) -> str:
        ...


class Selection(Reversible[Region]):
    """
    Maintains a set of sorted non-overlapping Regions. A selection may be
    empty.

    This is primarily used to represent the textual selection.
    """

    def __init__(self, id: int) -> None:
        self.view_id: int

    def __iter__(self) -> Iterator[Region]:
        """
        Iterate through all the regions in the selection.

        .. since:: 4023 3.8
        """
        ...

    def __len__(self) -> int:
        """:returns: The number of regions in the selection."""
        ...

    def __getitem__(self, index: int) -> Region:
        """:returns: The region at the given ``index``."""
        ...

    def __delitem__(self, index: int) -> None:
        """Delete the region at the given ``index``."""

    def __eq__(self, rhs: object) -> bool:
        """:returns: Whether the selections are identical."""
        ...

    def __lt__(self, rhs: Selection | None) -> bool:
        ...

    def __bool__(self) -> bool:
        """The selection is ``True`` when not empty."""
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def is_valid(self) -> bool:
        """:returns: Whether this selection is for a valid view."""
        ...

    def clear(self) -> None:
        """Remove all regions from the selection."""

    def add(self, x: Region | Point) -> None:
        """
        Add a `Region` or `Point` to the selection. It will be merged with the
        existing regions if intersecting.
        """

    def add_all(self, regions: Iterable[Region | Point]) -> None:
        """Add all the regions from the given iterable."""

    def subtract(self, region: Region) -> None:
        """
        Subtract a region from the selection, such that the whole region is no
        longer contained within the selection.
        """

    def contains(self, region: Region) -> bool:
        """:returns: Whether the provided region is contained within the selection."""
        ...


def make_sheet(sheet_id: int) -> Sheet | None:
    ...


class Sheet:
    """
    Represents a content container, i.e. a tab, within a window. Sheets may
    contain a View, or an image preview.
    """

    def __init__(self, id: int) -> None:
        self.sheet_id: int

    def __hash__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """:returns: A number that uniquely identifies this sheet."""
        ...

    def window(self) -> Window | None:
        """
        :returns: The `Window` containing this sheet. May be ``None`` if the
                  sheet has been closed.
        """

    def view(self) -> View | None:
        """
        :returns: The `View` contained within the sheet if any.
        """

    def file_name(self) -> str | None:
        """
        :returns:
            The full name of the file associated with the sheet, or ``None``
            if it doesn't exist on disk.

        .. since:: 4088
        """

    def is_semi_transient(self) -> bool:
        """
        :returns: Whether this sheet is semi-transient.

        .. since:: 4080
        """
        ...

    def is_transient(self) -> bool:
        """
        :returns: Whether this sheet is transient.

        .. since:: 4080
        """
        ...

    def is_selected(self) -> bool:
        """
        :returns: Whether this sheet is currently selected.

        :since: next
        """
        ...

    def group(self) -> int | None:
        """
        :returns: The (layout) group that the sheet is contained within.

        .. since:: 4100
        """
        ...

    def close(self, on_close: Callable[[bool], Any] = lambda did_close: None) -> None:
        """
        Closes the sheet.

        :param on_close:

        .. since:: 4088
        """


class TextSheet(Sheet):
    """
    Specialization for sheets containing editable text, ie. a `View`.

    .. since:: 4065
    """

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """Set the name displayed in the tab. Only affects unsaved files."""


class ImageSheet(Sheet):
    """
    Specialization for sheets containing an image.

    .. since:: 4065
    """

    def __repr__(self) -> str:
        ...


class HtmlSheet(Sheet):
    """
    Specialization for sheets containing HTML.

    .. since:: 4065
    """

    def __repr__(self) -> str:
        ...

    def set_name(self, name: str) -> None:
        """Set the name displayed in the tab."""

    def set_contents(self, contents: str) -> None:
        """Set the HTML content of the sheet."""


class ContextStackFrame:
    """
    Represents a single stack frame in the syntax highlighting. See
    `View.context_backtrace`.

    .. since:: 4127
    """

    __slots__ = ["context_name", "source_file", "source_location"]

    def __init__(self, context_name: str, source_file: str, source_location: tuple[int, int]) -> None:
        self.context_name: str
        """ The name of the context. """
        self.source_file: str
        """ The name of the file the context is defined in. """
        self.source_location: tuple[int, int]
        """
        The location of the context inside the source file as a pair of row and
        column. Maybe be ``(-1, -1)`` if the location is unclear, like in
        ``tmLanguage`` based syntaxes.
        """

    def __repr__(self) -> str:
        ...


class View:
    """
    Represents a view into a text `Buffer`.

    Note that multiple views may refer to the same `Buffer`, but they have their
    own unique selection and geometry. A list of these may be gotten using
    `View.clones()` or `Buffer.views()`.
    """

    def __init__(self, id: int) -> None:
        self.view_id: int
        self.selection: Selection
        self.settings_object: Settings | None

    def __len__(self) -> int:
        ...

    def __hash__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """:returns: A number that uniquely identifies this view."""
        ...

    def buffer_id(self) -> int:
        """
        :returns: A number that uniquely identifies this view's `Buffer`.
        """
        ...

    def buffer(self) -> Buffer:
        """:returns: The `Buffer` for which this is a view."""
        ...

    def sheet_id(self) -> int:
        """
        .. since:: 4083

        :returns:
            The ID of the `Sheet` for this `View`, or ``0`` if not part of any
            sheet.
        """
        ...

    def sheet(self) -> Sheet | None:
        """
        .. since:: 4083

        :returns: The `Sheet` for this view, if displayed in a sheet.
        """

    def element(self) -> str | None:
        """
        .. since:: 4050

        :returns:
            ``None`` for normal views that are part of a `Sheet`. For views that
            comprise part of the UI a string is returned from the following
            list:

            * ``"console:input"`` - The console input.
            * ``"goto_anything:input"`` - The input for the Goto Anything.
            * ``"command_palette:input"`` - The input for the Command Palette.
            * ``"find:input"`` - The input for the Find panel.
            * ``"incremental_find:input"`` - The input for the Incremental Find panel.
            * ``"replace:input:find"`` - The Find input for the Replace panel.
            * ``"replace:input:replace"`` - The Replace input for the Replace panel.
            * ``"find_in_files:input:find"`` - The Find input for the Find in Files panel.
            * ``"find_in_files:input:location"`` - The Where input for the Find in Files panel.
            * ``"find_in_files:input:replace"`` - The Replace input for the Find in Files panel.
            * ``"find_in_files:output"`` - The output panel for Find in Files (buffer or output panel).
            * ``"input:input"`` - The input for the Input panel.
            * ``"exec:output"`` - The output for the exec command.
            * ``"output:output"`` - A general output panel.

            The console output, indexer status output and license input controls
            are not accessible via the API.
        """

    def is_valid(self) -> bool:
        """
        Check whether this view is still valid. Will return ``False`` for a
        closed view, for example.
        """
        ...

    def is_primary(self) -> bool:
        """
        :returns: Whether view is the primary view into a `Buffer`. Will only be
                  ``False`` if the user has opened multiple views into a file.
        """
        ...

    def window(self) -> Window | None:
        """
        :returns: A reference to the window containing the view, if any.
        """

    def clones(self) -> list[View]:
        """:returns: All the other views into the same `Buffer`. See `View`."""
        ...

    def file_name(self) -> str | None:
        """
        :returns: The full name of the file associated with the sheet, or
                  ``None`` if it doesn't exist on disk.
        """

    def close(self, on_close: Callable[[bool], Any] = lambda did_close: None) -> bool:
        """Closes the view."""
        ...

    def retarget(self, new_fname: str) -> None:
        """Change the file path the buffer will save to."""

    def name(self) -> str:
        """:returns: The name assigned to the buffer, if any."""
        ...

    def set_name(self, name: str) -> None:
        """
        Assign a name to the buffer. Displayed as in the tab for unsaved files.
        """

    def reset_reference_document(self) -> None:
        """
        Clears the state of the `incremental diff <incremental_diff>` for the
        view.
        """

    def set_reference_document(self, reference: str) -> None:
        """
        Uses the string reference to calculate the initial diff for the
        `incremental diff <incremental_diff>`.
        """

    def is_loading(self) -> bool:
        """
        :returns: Whether the buffer is still loading from disk, and not ready
                  for use.
        """
        ...

    def is_dirty(self) -> bool:
        """
        :returns: Whether there are any unsaved modifications to the buffer.
        """
        ...

    def is_read_only(self) -> bool:
        """:returns: Whether the buffer may not be modified."""
        ...

    def set_read_only(self, read_only: bool) -> None:
        """Set the read only property on the buffer."""

    def is_scratch(self) -> bool:
        """
        :returns: Whether the buffer is a scratch buffer. See `set_scratch()`.
        """
        ...

    def set_scratch(self, scratch: bool) -> None:
        """
        Sets the scratch property on the buffer. When a modified scratch buffer
        is closed, it will be closed without prompting to save. Scratch buffers
        never report as being dirty.
        """

    def encoding(self) -> str:
        """
        :returns: The encoding currently associated with the buffer.
        """
        ...

    def set_encoding(self, encoding_name: str) -> None:
        """
        Applies a new encoding to the file. This will be used when the file is
        saved.
        """

    def line_endings(self) -> str:
        """:returns: The encoding currently associated with the file."""
        ...

    def set_line_endings(self, line_ending_name: str) -> None:
        """Sets the line endings that will be applied when next saving."""

    def size(self) -> int:
        """:returns: The number of character in the file."""
        ...

    def begin_edit(self, edit_token: int, cmd: str, args: CommandArgs = None) -> Edit:
        ...

    def end_edit(self, edit: Edit) -> None:
        ...

    def is_in_edit(self) -> bool:
        ...

    def insert(self, edit: Edit, pt: Point, text: str) -> int:
        """
        Insert the given string into the buffer.

        :param edit: An `Edit` object provided by a `TextCommand`.
        :param point: The text point in the view where to insert.
        :param text: The text to insert.
        :returns: The actual number of characters inserted. This may differ
                  from the provided text due to tab translation.
        :raises ValueError: If the `Edit` object is in an invalid state, ie. outside of a `TextCommand`.
        """
        ...

    def erase(self, edit: Edit, region: Region) -> None:
        """Erases the contents of the provided `Region` from the buffer."""

    def replace(self, edit: Edit, region: Region, text: str) -> None:
        """Replaces the contents of the `Region` in the buffer with the provided string."""

    def change_count(self) -> int:
        """
        Each time the buffer is modified, the change count is incremented. The
        change count can be used to determine if the buffer has changed since
        the last it was inspected.

        :returns: The current change count.
        """
        ...

    def change_id(self) -> tuple[int, int, int]:
        """
        Get a 3-element tuple that can be passed to `transform_region_from()` to
        obtain a region equivalent to a region of the view in the past. This is
        primarily useful for plugins providing text modification that must
        operate in an asynchronous fashion and must be able to handle the view
        contents changing between the request and response.
        """
        ...

    def transform_region_from(self, region: Region, change_id: tuple[int, int, int]) -> Region:
        """
        Transforms a region from a previous point in time to an equivalent
        region in the current state of the View. The ``change_id`` must have
        been obtained from `change_id()` at the point in time the region is
        from.
        """
        ...

    def run_command(self, cmd: str, args: CommandArgs = None) -> None:
        """Run the named `TextCommand` with the (optional) given ``args``."""

    def sel(self) -> Selection:
        """:returns: The views `Selection`."""
        ...

    def substr(self, x: Region | Point) -> str:
        """
        :returns: The string at the `Point` or within the `Region` provided.
        """
        ...

    def find(self, pattern: str, start_pt: Point, flags: FindFlags = FindFlags.NONE) -> Region:
        """
        :param pattern: The regex or literal pattern to search by.
        :param start_pt: The `Point` to start searching from.
        :param flags: Controls various behaviors of find. See `FindFlags`.
        :returns: The first `Region` matching the provided pattern.
        """
        ...

    def find_all(
        self,
        pattern: str,
        flags: FindFlags = FindFlags.NONE,
        fmt: str | None = None,
        extractions: list[str] | None = None,
    ) -> list[Region]:
        """
        :param pattern: The regex or literal pattern to search by.
        :param flags: Controls various behaviors of find. See `FindFlags`.
        :param fmt: When not ``None`` all matches in the ``extractions`` list
                       will be formatted with the provided format string.
        :param extractions: An optionally provided list to place the contents of
                            the find results into.
        :returns: All (non-overlapping) regions matching the pattern.
        """
        ...

    def settings(self) -> Settings:
        """
        :returns: The view's `Settings` object. Any changes to it will be
                  private to this view.
        """
        ...

    def meta_info(self, key: str, pt: Point) -> Any:
        """
        Look up the preference ``key`` for the scope at the provided `Point`
        from all matching ``.tmPreferences`` files.

        Examples of keys are ``TM_COMMENT_START`` and ``showInSymbolList``.
        """
        ...

    def extract_tokens_with_scopes(self, region: Region) -> list[tuple[Region, str]]:
        """
        :param region: The region from which to extract tokens and scopes.
        :returns: A list of pairs containing the `Region` and the scope of each token.

        .. since: 3172
        """
        ...

    def extract_scope(self, pt: Point) -> Region:
        """
        :returns: The extent of the syntax scope name assigned to the character
                  at the given `Point`, narrower syntax scope names included.
        """
        ...

    def expand_to_scope(self, pt: Point, selector: str) -> Region | None:
        """
        Expand by the provided scope selector from the `Point`.

        :param pt: The point from which to expand.
        :param selector: The scope selector to match.
        :returns: The matched `Region`, if any.

        .. since: 4130
        """

    def scope_name(self, pt: Point) -> str:
        """
        :returns: The syntax scope name assigned to the character at the given point.
        """
        ...

    def context_backtrace(self, pt: Point) -> list[ContextStackFrame]:
        """Get a backtrace of `ContextStackFrame`\\ s at the provided `Point`.

        Note this function is particularly slow.

        .. since:: 4127
        """
        ...

    def match_selector(self, pt: Point, selector: str) -> bool:
        """
        :returns: Whether the provided scope selector matches the `Point`.
        """
        ...

    def score_selector(self, pt: Point, selector: str) -> int:
        """
        Equivalent to::

            sublime.score_selector(view.scope_name(pt), selector)

        See `sublime.score_selector`.
        """
        ...

    def find_by_selector(self, selector: str) -> list[Region]:
        """
        Find all regions in the file matching the given selector.

        :returns: The list of matched regions.
        """
        ...

    def style(self) -> dict[str, str]:
        """
        See `style_for_scope`.

        :returns:
            The global style settings for the view. All colors are normalized
            to the six character hex form with a leading hash, e.g.
            ``#ff0000``.

        .. since:: 3150
        """
        ...

    def style_for_scope(self, scope: str) -> dict[str, str]:
        """
        Accepts a string scope name and returns a ``dict`` of style information
        including the keys:

        * ``"foreground"``
        * ``"background"`` (only if set)
        * ``"bold"``
        * ``"italic"``
        * .. since:: 4063
            ``"glow"``
        * .. since:: 4075
            ``"underline"``
        * .. since:: 4075
            ``"stippled_underline"``
        * .. since:: 4075
            ``"squiggly_underline"``
        * ``"source_line"``
        * ``"source_column"``
        * ``"source_file"``

        The foreground and background colors are normalized to the six character
        hex form with a leading hash, e.g. ``#ff0000``.
        """
        ...

    def indented_region(self, pt: Point) -> Region:
        ...

    def indentation_level(self, pt: Point) -> int:
        ...

    def has_non_empty_selection_region(self) -> bool:
        ...

    def lines(self, region: Region) -> list[Region]:
        """
        :returns: A list of lines (in sorted order) intersecting the provided `Region`.
        """
        ...

    def split_by_newlines(self, region: Region) -> list[Region]:
        """
        Splits the region up such that each `Region` returned exists on exactly
        one line.
        """
        ...

    def line(self, x: Region | Point) -> Region:
        """
        :returns:
            The line that contains the `Point` or an expanded `Region` to the
            beginning/end of lines, excluding the newline character.
        """
        ...

    def full_line(self, x: Region | Point) -> Region:
        """
        :returns:
            The line that contains the `Point` or an expanded `Region` to the
            beginning/end of lines, including the newline character.
        """
        ...

    def word(self, x: Region | Point) -> Region:
        """
        :returns:
            The word that contains the provided `Point`. If a `Region` is
            provided it's beginning/end are expanded to word boundaries.
        """
        ...

    def classify(self, pt: Point) -> PointClassification:
        """Classify the provided `Point`. See `PointClassification`."""
        ...

    def find_by_class(
        self,
        pt: Point,
        forward: bool,
        classes: PointClassification,
        separators: str = "",
        sub_word_separators: str = "",
    ) -> Point:
        """
        Find the next location that matches the provided `PointClassification`.

        :param pt: The point to start searching from.
        :param forward: Whether to search forward or backwards.
        :param classes: The classification to search for.
        :param separators: The word separators to use when classifying.
        :param sub_word_separators:
            The sub-word separators to use when classifying. :since:`4130`
        :returns: The found point.
        """
        ...

    def expand_by_class(
        self,
        x: Region | Point,
        classes: PointClassification,
        separators: str = "",
        sub_word_separators: str = "",
    ) -> Region:
        """
        Expand the provided `Point` or `Region` to the left and right until each
        side lands on a location that matches the provided
        `PointClassification`. See `find_by_class`.

        :param classes: The classification to search by.
        :param separators: The word separators to use when classifying.
        :param sub_word_separators:
            The sub-word separators to use when classifying. :since:`4130`
        """
        ...

    def rowcol(self, tp: Point) -> tuple[int, int]:
        """
        Calculates the 0-based line and column numbers of the point. Column
        numbers are returned as number of Unicode characters.
        """
        ...

    def rowcol_utf8(self, tp: Point) -> tuple[int, int]:
        """
        Calculates the 0-based line and column numbers of the point. Column
        numbers are returned as UTF-8 code units.

        .. since:: 4069
        """
        ...

    def rowcol_utf16(self, tp: Point) -> tuple[int, int]:
        """
        Calculates the 0-based line and column numbers of the point. Column
        numbers are returned as UTF-16 code units.

        .. since:: 4069
        """
        ...

    def text_point(self, row: int, col: int, *, clamp_column: bool = False) -> Point:
        """
        Calculates the character offset of the given, 0-based, ``row`` and
        ``col``. ``col`` is interpreted as the number of Unicode characters to
        advance past the beginning of the row.

        :param clamp_column:
            Whether ``col`` should be restricted to valid values for the given
            ``row``. :since:`4075`
        """
        ...

    def text_point_utf8(self, row: int, col: int, *, clamp_column: bool = False) -> Point:
        """
        Calculates the character offset of the given, 0-based, ``row`` and
        ``col``. ``col`` is interpreted as the number of UTF-8 code units to
        advance past the beginning of the row.

        :param clamp_column:
            whether ``col`` should be restricted to valid values for the given
            ``row``. :since:`4075`
        """
        ...

    def text_point_utf16(self, row: int, col: int, *, clamp_column: bool = False) -> Point:
        """
        Calculates the character offset of the given, 0-based, ``row`` and
        ``col``. ``col`` is interpreted as the number of UTF-16 code units to
        advance past the beginning of the row.

        :param clamp_column:
            whether ``col`` should be restricted to valid values for the given
            ``row``. :since:`4075`
        """
        ...

    def visible_region(self) -> Region:
        """:returns: The currently visible area of the view."""
        ...

    def show(
        self,
        location: Region | Selection | Point,
        show_surrounds: bool = True,
        keep_to_left: bool = False,
        animate: bool = True,
    ) -> None:
        """
        Scroll the view to show the given location.

        :param location:
            The location to scroll the view to. For a `Selection` only the first
            `Region` is shown.
        :param show_surrounds:
            Whether to show the surrounding context around the location.
        :param keep_to_left:
            Whether the view should be kept to the left, if horizontal scrolling
            is possible. :since:`4075`
        :param animate:
            Whether the scrolling should be animated. :since:`4075`
        """

    def show_at_center(self, location: Region | Point, animate: bool = True) -> None:
        """
        Scroll the view to center on the location.

        :param location: Which `Point` or `Region` to scroll to.
        :param animate: Whether the scrolling should be animated. :since:`4075`
        """

    def viewport_position(self) -> Vector:
        """:returns: The offset of the viewport in layout coordinates."""
        ...

    def set_viewport_position(self, xy: Vector, animate: bool = True) -> None:
        """Scrolls the viewport to the given layout position."""

    def viewport_extent(self) -> Vector:
        """:returns: The width and height of the viewport."""
        ...

    def layout_extent(self) -> Vector:
        """:returns: The width and height of the layout."""
        ...

    def text_to_layout(self, tp: Point) -> Vector:
        """Convert a text point to a layout position."""
        ...

    def text_to_window(self, tp: Point) -> Vector:
        """Convert a text point to a window position."""
        ...

    def layout_to_text(self, xy: Vector) -> Point:
        """Convert a layout position to a text point."""
        ...

    def layout_to_window(self, xy: Vector) -> Vector:
        """Convert a layout position to a window position."""
        ...

    def window_to_layout(self, xy: Vector) -> Vector:
        """Convert a window position to a layout position."""
        ...

    def window_to_text(self, xy: Vector) -> Point:
        """Convert a window position to a text point."""
        ...

    def line_height(self) -> DIP:
        """:returns: The light height used in the layout."""
        ...

    def em_width(self) -> DIP:
        """:returns: The typical character width used in the layout."""
        ...

    def is_folded(self, region: Region) -> bool:
        """:returns: Whether the provided `Region` is folded."""
        ...

    def folded_regions(self) -> list[Region]:
        """:returns: The list of folded regions."""
        ...

    def fold(self, x: Region | list[Region]) -> bool:
        """
        Fold the provided `Region` (s).

        :returns: ``False`` if the regions were already folded.
        """
        ...

    def unfold(self, x: Region | list[Region]) -> list[Region]:
        """
        Unfold all text in the provided `Region` (s).

        :returns: The unfolded regions.
        """
        ...

    def add_regions(
        self,
        key: str,
        regions: list[Region],
        scope: str = "",
        icon: str = "",
        flags: RegionFlags = RegionFlags.NONE,
        annotations: list[str] = [],
        annotation_color: str = "",
        on_navigate: Callable[[str], Any] | None = None,
        on_close: Callable[[], Any] | None = None,
    ) -> None:
        """
        Adds visual indicators to regions of text in the view. Indicators
        include icons in the gutter, underlines under the text, borders around
        the text and annotations. Annotations are drawn aligned to the
        right-hand edge of the view and may contain HTML markup.

        :param key:
            An identifier for the collection of regions. If a set of regions
            already exists for this key they will be overridden. See
            `get_regions`.
        :param regions: The list of regions to add. These should not overlap.
        :param scope:
            An optional string used to source a color to draw the regions in.
            The scope is matched against the color scheme. Examples include:
            ``"invalid"`` and ``"string"``. See `Scope Naming <scope_naming>`
            for a list of common scopes. If the scope is empty, the regions
            won't be drawn.

            .. since:: 3148
                Also supports the following pseudo-scopes, to allow picking the
                closest color from the user‘s color scheme:

                * ``"region.redish"``
                * ``"region.orangish"``
                * ``"region.yellowish"``
                * ``"region.greenish"``
                * ``"region.cyanish"``
                * ``"region.bluish"``
                * ``"region.purplish"``
                * ``"region.pinkish"``
        :param icon:
            An optional string specifying an icon to draw in the gutter next to
            each region. The icon will be tinted using the color associated
            with the ``scope``. Standard icon names are ``"dot"``, ``"circle"`
            and ``"bookmark"``. The icon may also be a full package-relative
            path, such as ``"Packages/Theme - Default/dot.png"``.
        :param flags:
            Flags specifying how the region should be drawn, among other
            behavior. See `RegionFlags`.
        :param annotations:
            An optional collection of strings containing HTML documents to
            display along the right-hand edge of the view. There should be the
            same number of annotations as regions. See `minihtml` for supported
            HTML. :since:`4050`
        :param annotation_color:
            An optional string of the CSS color to use when drawing the left
            border of the annotation. See :ref:`minihtml Reference: Colors
            <minihtml:CSS:Colors>` for supported color formats. :since:`4050`
        :param on_navitate:
            Called when a link in an annotation is clicked. Will be passed the
            ``href`` of the link. :since:`4050`
        :param on_close:
            Called when the annotations are closed. :since:`4050`
        """

    def get_regions(self, key: str) -> list[Region]:
        """
        :returns: The regions associated with the given ``key``, if any.
        """
        ...

    def erase_regions(self, key: str) -> None:
        """
        Remove the regions associated with the given ``key``.
        """

    def add_phantom(
        self,
        key: str,
        region: Region,
        content: str,
        layout: PhantomLayout,
        on_navigate: Callable[[str], Any] | None = None,
    ) -> int:
        ...

    def erase_phantoms(self, key: str) -> None:
        ...

    def erase_phantom_by_id(self, pid: int) -> None:
        ...

    def query_phantom(self, pid: int) -> list[Region]:
        ...

    def query_phantoms(self, pids: list[int]) -> list[Region]:
        ...

    def assign_syntax(self, syntax: str | Syntax) -> None:
        """
        Changes the syntax used by the view. ``syntax`` may be a packages path
        to a syntax file, or a ``scope:`` specifier string.

        .. since:: 4080
            ``syntax`` may be a `Syntax` object.
        """

    def set_syntax_file(self, syntax_file: str) -> None:
        """:deprecated: Use `assign_syntax()` instead."""

    def syntax(self) -> Syntax | None:
        """:returns: The syntax assigned to the buffer."""

    def symbols(self) -> list[tuple[Region, str]]:
        """
        Extract all the symbols defined in the buffer.

        :deprecated: Use `symbol_regions()` instead.
        """
        ...

    def get_symbols(self) -> list[tuple[Region, str]]:
        """
        :deprecated: Use `symbol_regions()` instead.
        """
        ...

    def indexed_symbols(self) -> list[tuple[Region, str]]:
        """
        :returns: A list of the `Region` and name of symbols.
        :deprecated: Use `indexed_symbol_regions()` instead.

        .. since:: 3148
        """
        ...

    def indexed_references(self) -> list[tuple[Region, str]]:
        """
        :returns: A list of the `Region` and name of symbols.
        :deprecated: Use `indexed_symbol_regions()` instead.

        .. since:: 3148
        """
        ...

    def symbol_regions(self) -> list[SymbolRegion]:
        """
        :returns: Info about symbols that are part of the view's symbol list.

        .. since:: 4085
        """
        ...

    def indexed_symbol_regions(self, type: SymbolType = SymbolType.ANY) -> list[SymbolRegion]:
        """
        :param type: The type of symbol to return.
        :returns: Info about symbols that are indexed.

        .. since:: 4085
        """
        ...

    def set_status(self, key: str, value: str) -> None:
        """
        Add the status ``key`` to the view. The ``value`` will be displayed in the
        status bar, in a comma separated list of all status values, ordered by
        key. Setting the ``value`` to ``""`` will clear the status.
        """

    def get_status(self, key: str) -> str:
        """
        :returns: The previous assigned value associated with the given ``key``, if any.

        See `set_status()`.
        """
        ...

    def erase_status(self, key: str) -> None:
        """Clear the status associated with the provided ``key``."""

    def extract_completions(self, prefix: str, tp: Point = -1) -> list[str]:
        """
        Get a list of word-completions based on the contents of the view.

        :param prefix: The prefix to filter words by.
        :param tp: The `Point` by which to weigh words. Closer words are preferred.
        """
        ...

    def find_all_results(self) -> list[tuple[str, int, int]]:
        ...

    def find_all_results_with_text(self) -> list[tuple[str, int, int, str]]:
        ...

    def command_history(self, index: int, modifying_only: bool = False) -> tuple[str, CommandArgs, int]:
        """
        Get info on previous run commands stored in the undo/redo stack.

        :param index:
            The offset into the undo/redo stack. Positive values for index
            indicate to look in the redo stack for commands.
        :param modifying_only:
            Whether only commands that modify the text buffer are considered.
        :returns:
            The command name, command arguments and repeat count for the history
            entry. If the undo/redo history doesn't extend far enough, then
            ``(None, None, 0)`` will be returned.
        """
        ...

    def overwrite_status(self) -> bool:
        """
        :returns: The overwrite status, which the user normally toggles via the
                  insert key.
        """
        ...

    def set_overwrite_status(self, value: bool) -> None:
        """Set the overwrite status. See `overwrite_status()`."""

    def show_popup_menu(self, items: list[str], on_done: Callable[[int], Any], flags: int = 0) -> None:
        """
        Show a popup menu at the caret, for selecting an item in a list.

        :param items: The list of entries to show in the list.
        :param on_done: Called once with the index of the selected item. If the
                        popup was cancelled ``-1`` is passed instead.
        :param flags: must be ``0``, currently unused.
        """

    def show_popup(
        self,
        content: str,
        flags: PopupFlags = PopupFlags.NONE,
        location: Point = -1,
        max_width: DIP = 320,
        max_height: DIP = 240,
        on_navigate: Callable[[str], Any] | None = None,
        on_hide: Callable[[], Any] | None = None,
    ) -> None:
        """
        Show a popup displaying HTML content.

        :param content: The HTML content to display.
        :param flags: Flags controlling popup behavior. See `PopupFlags`.
        :param location: The `Point` at which to display the popup. If ``-1``
                         the popup is shown at the current postion of the caret.
        :param max_width: The maximum width of the popup.
        :param max_height: The maximum height of the popup.
        :param on_navigate:
            Called when a link is clicked in the popup. Passed the value of the
            ``href`` attribute of the clicked link.
        :param on_hide: Called when the popup is hidden.
        """

    def update_popup(self, content: str) -> None:
        """
        Update the content of the currently visible popup.
        """

    def is_popup_visible(self) -> bool:
        """
        :returns: Whether a popup is currently shown.
        """
        ...

    def hide_popup(self) -> None:
        """
        Hide the current popup.
        """

    def is_auto_complete_visible(self) -> bool:
        """
        :returns: Whether the auto-complete menu is currently visible.
        """
        ...

    def preserve_auto_complete_on_focus_lost(self) -> None:
        """
        Sets the auto complete popup state to be preserved the next time the
        `View` loses focus. When the `View` regains focus, the auto complete
        window will be re-shown, with the previously selected entry
        pre-selected.

        .. since:: 4073
        """

    def export_to_html(
        self,
        regions: Region | list[Region] | None = None,
        minihtml: bool = False,
        enclosing_tags: bool = False,
        font_size: bool = True,
        font_family: bool = True,
    ) -> str:
        """
        Generates an HTML string of the current view contents, including styling
        for syntax highlighting.

        :param regions:
            The region(s) to export. By default the whole view is exported.
        :param minihtml:
            Whether the exported HTML should be compatible with `minihtml`.
        :param enclosing_tags:
            Whether a :html:`<div>` with base-styling is added. Note that
            without this no background color is set.
        :param font_size:
            Whether to include the font size in the top level styling. Only
            applies when ``enclosing_tags`` is ``True``.
        :param font_family:
            Whether to include the font family in the top level styling. Only
            applies when ``enclosing_tags`` is ``True``.

        .. since:: 4092
        """
        ...

    def clear_undo_stack(self) -> None:
        """
        Clear the undo/redo stack.

        .. since:: 4114
        """


def _buffers() -> list[Buffer]:
    """Returns all available Buffer objects"""
    ...


class Buffer:
    """
    Represents a text buffer. Multiple `View` objects may share the same buffer.

    .. since:: 4081
    """

    def __init__(self, id: int) -> None:
        self.buffer_id: int

    def __hash__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def id(self) -> int:
        """
        Returns a number that uniquely identifies this buffer.

        .. since:: 4083
        """
        ...

    def file_name(self) -> str | None:
        """
        The full name file the file associated with the buffer, or ``None`` if
        it doesn't exist on disk.

        .. since:: 4083
        """

    def views(self) -> list[View]:
        """
        Returns a list of all views that are associated with this buffer.
        """
        ...

    def primary_view(self) -> View:
        """
        The primary view associated with this buffer.
        """
        ...


class Settings:
    """
    A ``dict`` like object that a settings hierarchy.
    """

    def __init__(self, id: int) -> None:
        self.settings_id: int

    def __getitem__(self, key: str) -> Any:
        """
        Returns the named setting.

        .. since:: 4023 3.8
        """
        ...

    def __setitem__(self, key: str, value: Value | None) -> None:
        """
        Set the named ``key`` to the provided ``value``.

        .. since:: 4023 3.8
        """

    def __delitem__(self, key: str) -> None:
        """
        Deletes the provided ``key`` from the setting. Note that a parent
        setting may also provide this key, thus deleting may not entirely
        remove a key.

        .. since:: 4078 3.8
        """

    def __contains__(self, key: str) -> bool:
        """
        Returns whether the provided ``key`` is set.

        .. since:: 4023 3.8
        """
        ...

    def __repr__(self) -> str:
        ...

    def to_dict(self) -> dict[str, Any]:
        """
        Return the settings as a dict. This is not very fast.

        .. since:: 4078 3.8
        """
        ...

    def setdefault(self, key: str, value: Value | None) -> Any:
        """
        Returns the value associated with the provided ``key``. If it's not
        present the provided ``value`` is assigned to the ``key`` and then
        returned.

        .. since:: 4023 3.8
        """
        ...

    def update(
        self,
        pairs: Mapping[str, Any] | Iterable[tuple[str, Any]] | HasKeysMethod = tuple(),
        /,
        **kwargs: Any,
    ) -> None:
        """
        Update the settings from the provided argument(s).

        Accepts:

        * A ``dict`` or other implementation of ``collections.abc.Mapping``.
        * An object with a ``keys()`` method.
        * An object that iterates over key/value pairs
        * Keyword arguments, ie. ``update(**kwargs)``.

        .. since:: 4078 3.8
        """

    def get(self, key: str, default: Value | None = None) -> Any:
        ...

    def has(self, key: str) -> bool:
        """Same as `__contains__`."""
        ...

    def set(self, key: str, value: Value | None | None) -> None:
        """Same as `__setitem__`."""

    def erase(self, key: str) -> None:
        """Same as `__delitem__`."""

    def add_on_change(self, tag: str, callback: Callable[[], Any]) -> None:
        """
        Register a callback to be run whenever a setting is changed.

        :param tag: A string associated with the callback. For use with
                    `clear_on_change`.
        :param callback: A callable object to be run when a setting is changed.
        """
        ...

    def clear_on_change(self, tag: str) -> None:
        """
        Remove all callbacks associated with the provided ``tag``. See
        `add_on_change`.
        """
        ...


class Phantom:
    """
    Represents an `minihtml`-based decoration to display non-editable content
    interspersed in a `View`. Used with `PhantomSet` to actually add the
    phantoms to the `View`. Once a `Phantom` has been constructed and added to
    the `View`, changes to the attributes will have no effect.
    """

    def __init__(
        self,
        region: Region,
        content: str,
        layout: PhantomLayout,
        on_navigate: Callable[[str], Any] | None = None,
    ) -> None:
        self.region: Region
        """
        The `Region` associated with the phantom. The phantom is displayed at
        the start of the `Region`.
        """
        self.content: str
        """ The HTML content of the phantom. """
        self.layout: PhantomLayout
        """ How the phantom should be placed relative to the ``region``. """
        self.on_navigate: Callable[[str], Any] | None
        """
        Called when a link in the HTML is clicked. The value of the ``href``
        attribute is passed.
        """
        self.id: int

    def __eq__(self, rhs: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def to_tuple(self) -> tuple[tuple[Point, Point], str, PhantomLayout, Callable[[str], Any] | None]:
        """
        Returns a tuple of this phantom containing the region, content, layout
        and callback.

        Use this to uniquely identify a phantom in a set or similar. Phantoms
        can't be used for that directly as they are mutable.
        """
        ...


class PhantomSet:
    """
    A collection that manages `Phantom` objects and the process of adding them,
    updating them and removing them from a `View`.
    """

    def __init__(self, view: View, key: str = "") -> None:
        self.view: View
        """
        The `View` the phantom set is attached to.
        """
        self.key: str
        """
        A string used to group the phantoms together.
        """
        self.phantoms: list[Phantom]

    def __del__(self) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def update(self, phantoms: Iterable[Phantom]) -> None:
        """
        Update the set of phantoms. If the `Phantom.region` of existing phantoms
        have changed they will be moved; new phantoms are added and ones not
        present are removed.
        """


class Html:
    """
    Used to indicate that a string is formatted as HTML. See
    `CommandInputHandler.preview()`.
    """

    __slots__ = ["data"]

    def __init__(self, data: str) -> None:
        self.data: str

    def __repr__(self) -> str:
        ...


class CompletionList:
    """
    Represents a list of completions, some of which may be in the process of
    being asynchronously fetched.

    .. since:: 4050
    """

    def __init__(
        self,
        completions: list[CompletionValue] | None = None,
        flags: AutoCompleteFlags = AutoCompleteFlags.NONE,
    ) -> None:
        """
        :param completions:
            If ``None`` is passed, the method `set_completions()` must be called
            before the completions will be displayed to the user.
        :param flags: Flags controlling auto-complete behavior. See `AutoCompleteFlags`.
        """

    def __repr__(self) -> str:
        ...

    def _set_target(self, target: None | Any) -> None:
        ...

    def set_completions(
        self,
        completions: list[CompletionValue],
        flags: AutoCompleteFlags = AutoCompleteFlags.NONE,
    ) -> None:
        """
        Sets the list of completions, allowing the list to be displayed to the
        user.
        """


class CompletionItem:
    """
    Represents an available auto-completion item.

    .. since:: 4050
    """

    __slots__ = ["trigger", "annotation", "completion", "completion_format", "kind", "details", "flags"]

    def __init__(
        self,
        trigger: str,
        annotation: str = "",
        completion: str = "",
        completion_format: CompletionFormat = CompletionFormat.TEXT,
        kind: Kind = KIND_AMBIGUOUS,
        details: str = "",
        flags: CompletionItemFlags = CompletionItemFlags.NONE,
    ) -> None:
        self.trigger: str
        """ Text to match against the user's input. """
        self.annotation: str
        """ A hint to draw to the right-hand side of the trigger. """
        self.completion: str
        """
        Text to insert if the completion is specified. If empty the `trigger`
        will be inserted instead.
        """
        self.completion_format: CompletionFormat
        """ The format of the completion. See `CompletionFormat`. """
        self.kind: Kind
        """ The kind of the completion. See `Kind`. """
        self.details: str
        """
        An optional `minihtml` description of the completion, shown in the
        detail pane at the bottom of the auto complete window.

        .. since:: 4073
        """
        self.flags

    def __eq__(self, rhs: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    @classmethod
    def snippet_completion(
        cls,
        trigger: str,
        snippet: str,
        annotation="",
        kind: Kind = KIND_SNIPPET,
        details: str = "",
    ) -> CompletionItem:
        """
        Specialized constructor for snippet completions. The `completion_format`
        is always `CompletionFormat.SNIPPET`.
        """
        ...

    @classmethod
    def command_completion(
        cls,
        trigger: str,
        command: str,
        args: CommandArgs = None,
        annotation: str = "",
        kind: Kind = KIND_AMBIGUOUS,
        details: str = "",
    ) -> CompletionItem:
        """
        Specialized constructor for command completions. The `completion_format`
        is always `CompletionFormat.COMMAND`.
        """
        ...


def list_syntaxes() -> list[Syntax]:
    """list all known syntaxes.

    Returns a list of Syntax.
    """
    ...


def syntax_from_path(path: str) -> Syntax | None:
    """Get the syntax for a specific path.

    Returns a Syntax or None.
    """


def find_syntax_by_name(name: str) -> list[Syntax]:
    """Find syntaxes with the specified name.

    Name must match exactly. Return a list of Syntax.
    """
    ...


def find_syntax_by_scope(scope: str) -> list[Syntax]:
    """Find syntaxes with the specified scope.

    Scope must match exactly. Return a list of Syntax.
    """
    ...


def find_syntax_for_file(path, first_line: str = "") -> Syntax | None:
    """Find the syntax to use for a path.

    Uses the file extension, various application settings and optionally the
    first line of the file to pick the right syntax for the file.

    Returns a Syntax.
    """


class Syntax:
    """
    Contains information about a syntax.

    .. since:: 4081
    """

    __slots__ = ["path", "name", "hidden", "scope"]

    def __init__(self, path: str, name: str, hidden: bool, scope: str) -> None:
        self.path: str
        """ The packages path to the syntax file. """
        self.name: str
        """ The name of the syntax. """
        self.hidden: bool
        """ If the syntax is hidden from the user. """
        self.scope: str
        """ The base scope name of the syntax. """

    def __eq__(self, other: object) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    def __repr__(self) -> str:
        ...


class QuickPanelItem:
    """
    Represents a row in the quick panel, shown via `Window.show_quick_panel()`.

    .. since:: 4083
    """

    __slots__ = ["trigger", "details", "annotation", "kind"]

    def __init__(
        self,
        trigger: str,
        details: str | list[str] | tuple[str] = "",
        annotation: str = "",
        kind: Kind = KIND_AMBIGUOUS,
    ) -> None:
        self.trigger: str
        """ Text to match against user's input. """
        self.details: str | list[str] | tuple[str]
        """
        A `minihtml` string or list of strings displayed below the trigger.
        """
        self.annotation: str
        """ Hint to draw to the right-hand side of the row. """
        self.kind: Kind
        """ The kind of the item. See `Kind`. """

    def __repr__(self) -> str:
        ...


class ListInputItem:
    """
    Represents a row shown via `ListInputHandler`.

    .. since:: 4095
    """

    __slots__ = ["text", "value", "details", "annotation", "kind"]

    def __init__(
        self,
        text: str,
        value: Any,
        details: str | list[str] | tuple[str] = "",
        annotation: str = "",
        kind: Kind = KIND_AMBIGUOUS,
    ) -> None:
        self.text: str
        """ Text to match against the user's input. """
        self.value: Any
        """ A `Value` passed to the command if the row is selected. """
        self.details: str | list[str] | tuple[str]
        """
        A `minihtml` string or list of strings displayed below the trigger.
        """
        self.annotation: str
        """ Hint to draw to the right-hand side of the row. """
        self.kind: Kind
        """ The kind of the item. See `Kind`. """

    def __repr__(self) -> str:
        ...


class SymbolRegion:
    """
    Contains information about a `Region` of a `View` that contains a symbol.

    .. since:: 4085
    """

    __slots__ = ["name", "region", "syntax", "type", "kind"]

    def __init__(self, name: str, region: Region, syntax: str, type: SymbolType, kind: Kind) -> None:
        self.name: str
        """ The name of the symbol. """
        self.region: Region
        """ The location of the symbol within the `View`. """
        self.syntax: str
        """ The name of the syntax for the symbol. """
        self.type: SymbolType
        """ The type of the symbol. See `SymbolType`. """
        self.kind: Kind
        """ The kind of the symbol. See `Kind`. """

    def __repr__(self) -> str:
        ...


class SymbolLocation:
    """
    Contains information about a file that contains a symbol.

    .. since:: 4085
    """

    __slots__ = ["path", "display_name", "row", "col", "syntax", "type", "kind"]

    def __init__(
        self,
        path: str,
        display_name: str,
        row: int,
        col: int,
        syntax: str,
        type: SymbolType,
        kind: Kind,
    ) -> None:
        self.path: str
        """ The filesystem path to the file containing the symbol. """
        self.display_name: str
        """ The project-relative path to the file containing the symbol. """
        self.row: int
        """ The row of the file the symbol is contained on. """
        self.col: int
        """ The column of the row that the symbol is contained on. """
        self.syntax: str
        """ The name of the syntax for the symbol. """
        self.type: SymbolType
        """ The type of the symbol. See `SymbolType`. """
        self.kind: Kind
        """ The kind of the symbol. See `Kind`. """

    def __repr__(self) -> str:
        ...

    def path_encoded_position(self) -> str:
        ...
