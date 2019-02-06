import sys

import sublime_api  # type: ignore


class _LogWriter:
    def flush(self):
        pass

    def write(self, s):
        sublime_api.log_message(s)


sys.stdout = _LogWriter()  # type: ignore
sys.stderr = _LogWriter()  # type: ignore

HOVER_TEXT = 1
HOVER_GUTTER = 2
HOVER_MARGIN = 3

ENCODED_POSITION = 1
TRANSIENT = 4
FORCE_GROUP = 8
IGNORECASE = 2
LITERAL = 1
MONOSPACE_FONT = 1
KEEP_OPEN_ON_FOCUS_LOST = 2
HTML = 1
COOPERATE_WITH_AUTO_COMPLETE = 2
HIDE_ON_MOUSE_MOVE = 4
HIDE_ON_MOUSE_MOVE_AWAY = 8

DRAW_EMPTY = 1
HIDE_ON_MINIMAP = 2
DRAW_EMPTY_AS_OVERWRITE = 4
PERSISTENT = 16
# Deprecated, use DRAW_NO_FILL instead
DRAW_OUTLINED = 32
DRAW_NO_FILL = 32
DRAW_NO_OUTLINE = 256
DRAW_SOLID_UNDERLINE = 512
DRAW_STIPPLED_UNDERLINE = 1024
DRAW_SQUIGGLY_UNDERLINE = 2048
HIDDEN = 128

OP_EQUAL = 0
OP_NOT_EQUAL = 1
OP_REGEX_MATCH = 2
OP_NOT_REGEX_MATCH = 3
OP_REGEX_CONTAINS = 4
OP_NOT_REGEX_CONTAINS = 5
CLASS_WORD_START = 1
CLASS_WORD_END = 2
CLASS_PUNCTUATION_START = 4
CLASS_PUNCTUATION_END = 8
CLASS_SUB_WORD_START = 16
CLASS_SUB_WORD_END = 32
CLASS_LINE_START = 64
CLASS_LINE_END = 128
CLASS_EMPTY_LINE = 256
INHIBIT_WORD_COMPLETIONS = 8
INHIBIT_EXPLICIT_COMPLETIONS = 16

DIALOG_CANCEL = 0
DIALOG_YES = 1
DIALOG_NO = 2

UI_ELEMENT_SIDE_BAR = 1
UI_ELEMENT_MINIMAP = 2
UI_ELEMENT_TABS = 4
UI_ELEMENT_STATUS_BAR = 8
UI_ELEMENT_MENU = 16
UI_ELEMENT_OPEN_FILES = 32

LAYOUT_INLINE = 0
LAYOUT_BELOW = 1
LAYOUT_BLOCK = 2


def version():
    """Returns the version number"""
    return sublime_api.version()


def platform():
    """Returns the platform, which may be "osx", "linux" or "windows" """
    return sublime_api.platform()


def arch():
    """Returns the CPU architecture, which may be "x32" or "x64" """
    return sublime_api.architecture()


def channel():
    return sublime_api.channel()


def executable_path():
    """Returns the path to _sublime_text_ executable"""
    return sublime_api.executable_path()


def executable_hash():
    import hashlib
    return (
        version(), platform() + '_' + arch(),
        hashlib.md5(open(executable_path(), 'rb').read()).hexdigest())


def packages_path():
    """Returns the path where all the user's loose packages are located"""
    return sublime_api.packages_path()


def installed_packages_path():
    """Returns the path where all the user's _.sublime-package_ files are located"""
    return sublime_api.installed_packages_path()


def cache_path():
    """Returns the path where Sublime Text stores cache files"""
    return sublime_api.cache_path()


def status_message(msg):
    """Show a message in the status bar"""
    sublime_api.status_message(msg)


def error_message(msg):
    """Displays an error dialog to the user"""
    sublime_api.error_message(msg)


def message_dialog(msg):
    """Displays a message dialog to the user"""
    sublime_api.message_dialog(msg)


def ok_cancel_dialog(msg, ok_title=""):
    """
    Displays an <kbd>ok</kbd>  <kbd>cancel</kbd> question dialog to the user If _`ok_title`_ is
    provided, this may be used as the text on the <kbd>ok</kbd> button.
    Returns `True` if the user presses the <kbd>ok</kbd> button
    """
    return sublime_api.ok_cancel_dialog(msg, ok_title)


def yes_no_cancel_dialog(msg, yes_title="", no_title=""):
    """
    Displays a <kbd>yes</kbd>  <kbd>no</kbd>  <kbd>cancel</kbd> question dialog to the user
    If _`yes_title`_ and/or _`no_title`_ are provided, they will be used as the
    text on the corresponding buttons on some platforms. Returns `DIALOG_YES`,
    `DIALOG_NO` or `DIALOG_CANCEL`
    """
    return sublime_api.yes_no_cancel_dialog(msg, yes_title, no_title)


def run_command(cmd, args=None):
    """Runs the named `ApplicationCommand` with the (optional) given _`args`_"""
    sublime_api.run_command(cmd, args)


def get_clipboard(size_limit=16777216):
    """
    Returns the content of the clipboard, for performance reason if the size
    of the clipboard content is bigger than _`size_limit`_, an empty string will
    be returned
    """
    return sublime_api.get_clipboard(size_limit)


def set_clipboard(text):
    """Sets the contents of the clipboard"""
    return sublime_api.set_clipboard(text)


def log_commands(flag):
    """
    Controls command logging. If enabled, all commands run from key bindings
    and the menu will be logged to the console
    """
    sublime_api.log_commands(flag)


def log_input(flag):
    """
    Enables or disables input logging. This is useful to find the names of
    certain keys on the keyboard
    """
    sublime_api.log_input(flag)


def log_result_regex(flag):
    """
    Enables or disables result regex logging. This is useful when trying to
    debug _file_regex_ and _line_regex_ in build systems
    """
    sublime_api.log_result_regex(flag)


def log_indexing(flag):
    sublime_api.log_indexing(flag)


def log_build_systems(flag):
    sublime_api.log_build_systems(flag)


def score_selector(scope_name, selector):
    """
    Matches the _`selector`_ against the given scope, returning a score
    A score of 0 means no match, above 0 means a match. Different selectors may
    be compared against the same scope: a higher score means the selector is a
    better match for the scope
    """
    return sublime_api.score_selector(scope_name, selector)


def load_resource(name):
    """
    Loads the given resource. The _`name`_ should be in the format
    _Packages/Default/Main.sublime-menu_
    """
    s = sublime_api.load_resource(name)
    if s is None:
        raise IOError("resource not found")
    return s


def load_binary_resource(name):
    """
    Loads the given resource. The _`name`_ should be in the format
    _Packages/Default/Main.sublime-menu_
    """
    bytes = sublime_api.load_binary_resource(name)
    if bytes is None:
        raise IOError("resource not found")
    return bytes


def find_resources(pattern):
    """Finds resources whose file name matches the given _`pattern`_"""
    return sublime_api.find_resources(pattern)


def encode_value(val, pretty=False):
    """
    Encode a JSON compatible value into a string representation
    If _`pretty`_ is set to `True`, the string will include newlines and indentation
    """
    return sublime_api.encode_value(val, pretty)


def decode_value(data):
    """
    Decodes a JSON string into an object.
    If _`data`_ is invalid, a `ValueError` will be thrown
    """
    val, err = sublime_api.decode_value(data)

    if err:
        raise ValueError(err)

    return val


def expand_variables(val, variables):
    """
    Expands any variables in the string _`value`_ using the variables defined in
    the dictionary _`variables`_
    _`value`_ may also be a `list` or `dict`, in which case the structure will be
    recursively expanded. Strings should use snippet syntax, for example:
    ```python
    expand_variables("Hello, ${name}", {"name": "Foo"})
    ```
    """
    return sublime_api.expand_variables(val, variables)


def load_settings(base_name):
    """
    Loads the named settings. The name should include a file name and extension,
    but not a path The packages will be searched for files matching the
    _`base_name`_, and the results will be collated into the settings object
    Subsequent calls to `load_settings()` with the _`base_name`_ will return the
    same object, and not load the settings from disk again
    """
    settings_id = sublime_api.load_settings(base_name)
    return Settings(settings_id)


def save_settings(base_name):
    """Flushes any in-memory changes to the named settings object to disk"""
    sublime_api.save_settings(base_name)


def set_timeout(f, timeout_ms=0):
    """
    Schedules a function to be called in the future. Sublime Text will block
    while the function is running
    """
    sublime_api.set_timeout(f, timeout_ms)


def set_timeout_async(f, timeout_ms=0):
    """
    Schedules a function to be called in the future. The function will be
    called in a worker thread, and Sublime Text will not block while the
    function is running
    """
    sublime_api.set_timeout_async(f, timeout_ms)


def active_window():
    """Returns the most recently used window"""
    return Window(sublime_api.active_window())


def windows():
    """Returns a list of all the open windows"""
    return [Window(id) for id in sublime_api.windows()]


def get_macro():
    """
    Returns a list of the commands and args that compromise the currently
    recorded macro. Each dict will contain the keys command and args
    """
    return sublime_api.get_macro()


class Window(object):
    """
    This class represents windows and provides an interface of methods to
    interact with them
    """

    def __init__(self, id):
        self.window_id = id
        self.settings_object = None
        self.template_settings_object = None

    def __eq__(self, other):
        return isinstance(other, Window) and other.window_id == self.window_id

    def __bool__(self):
        return self.window_id != 0

    def id(self):
        """Returns a number that uniquely identifies this window"""
        return self.window_id

    def is_valid(self):
        return sublime_api.window_num_groups(self.window_id) != 0

    def hwnd(self):
        """Platform specific window handle, only returns a meaningful result under Windows"""
        return sublime_api.window_system_handle(self.window_id)

    def active_sheet(self):
        """Returns the currently focused sheet"""
        sheet_id = sublime_api.window_active_sheet(self.window_id)
        if sheet_id == 0:
            return None
        else:
            return Sheet(sheet_id)

    def active_view(self):
        """Returns the currently edited view"""
        view_id = sublime_api.window_active_view(self.window_id)
        if view_id == 0:
            return None
        else:
            return View(view_id)

    def run_command(self, cmd, args=None):
        """
        Runs the named `WindowCommand` with the (optional) given _`args`_
        This method is able to run any sort of command, dispatching the
        command via input focus
        """
        sublime_api.window_run_command(self.window_id, cmd, args)

    def new_file(self, flags=0, syntax=""):
        """
        Creates a new file, The returned view will be empty, and its
        `is_loaded()` method will return `True`.
        flags must be either `0` or `TRANSIENT`
        """
        return View(sublime_api.window_new_file(self.window_id, flags, syntax))

    def open_file(self, fname, flags=0, group=-1):
        """
        Opens the named file, and returns the corresponding view. If the file is
        already opened, it will be brought to the front. Note that as file
        loading is asynchronous, operations on the returned view won't be
        possible until its `is_loading()` method returns `False`.

        The optional _`flags`_ parameter is a bitwise combination of:

        `ENCODED_POSITION`: Indicates the file_name should be searched for
        a :row or :row:col suffix
        `TRANSIENT`: Open the file as a preview only: it won't have a tab
        assigned it until modified
        `FORCE_GROUP`: don't select the file if it's opened in a different
        group
        """
        return View(sublime_api.window_open_file(self.window_id, fname, flags, group))

    def find_open_file(self, fname):
        """
        Finds the named file in the list of open files, and returns the
        corresponding `View`, or `None` if no such file is open
        """
        view_id = sublime_api.window_find_open_file(self.window_id, fname)
        if view_id == 0:
            return None
        else:
            return View(view_id)

    def num_groups(self):
        """Returns the number of view groups in the window"""
        return sublime_api.window_num_groups(self.window_id)

    def active_group(self):
        """Returns the index of the currently selected group"""
        return sublime_api.window_active_group(self.window_id)

    def focus_group(self, idx):
        """Makes the given group active"""
        sublime_api.window_focus_group(self.window_id, idx)

    def focus_sheet(self, sheet):
        """Switches to the given _`sheet`_"""
        if sheet:
            sublime_api.window_focus_sheet(self.window_id, sheet.sheet_id)

    def focus_view(self, view):
        """Switches to the given _`view`_"""
        if view:
            sublime_api.window_focus_view(self.window_id, view.view_id)

    def get_sheet_index(self, sheet):
        """
        Returns the group, and index within the group of the _`sheet`_
        Returns (-1, -1) if not found
        """
        if sheet:
            return sublime_api.window_get_sheet_index(self.window_id, sheet.sheet_id)
        else:
            return (-1, -1)

    def get_view_index(self, view):
        """
        Returns the group, and index within the group of the _`view`_
        Returns (-1, -1) if not found
        """
        if view:
            return sublime_api.window_get_view_index(self.window_id, view.view_id)
        else:
            return (-1, -1)

    def set_sheet_index(self, sheet, group, idx):
        """Moves the _`sheet`_ to the given _`group`_ and index"""
        sublime_api.window_set_sheet_index(self.window_id, sheet.sheet_id, group, idx)

    def set_view_index(self, view, group, idx):
        """Moves the _`view`_ to the given _`group`_ and index"""
        sublime_api.window_set_view_index(self.window_id, view.view_id, group, idx)

    def sheets(self):
        """Returns all open sheets in the window"""
        sheet_ids = sublime_api.window_sheets(self.window_id)
        return [Sheet(x) for x in sheet_ids]

    def views(self):
        """Returns all open views in the window"""
        view_ids = sublime_api.window_views(self.window_id)
        return [View(x) for x in view_ids]

    def active_sheet_in_group(self, group):
        """Returns the currently focused sheet in the given _`group`_"""
        sheet_id = sublime_api.window_active_sheet_in_group(self.window_id, group)
        if sheet_id == 0:
            return None
        else:
            return Sheet(sheet_id)

    def active_view_in_group(self, group):
        """Returns the currently edited view in the given _`group`_"""
        view_id = sublime_api.window_active_view_in_group(self.window_id, group)
        if view_id == 0:
            return None
        else:
            return View(view_id)

    def sheets_in_group(self, group):
        """Returns all open sheets in the given _`group`_"""
        sheet_ids = sublime_api.window_sheets_in_group(self.window_id, group)
        return [Sheet(x) for x in sheet_ids]

    def views_in_group(self, group):
        """Returns all open views in the given _`group`_"""
        view_ids = sublime_api.window_views_in_group(self.window_id, group)
        return [View(x) for x in view_ids]

    def transient_sheet_in_group(self, group):
        sheet_id = sublime_api.window_transient_sheet_in_group(self.window_id, group)
        if sheet_id != 0:
            return Sheet(sheet_id)
        else:
            return None

    def transient_view_in_group(self, group):
        view_id = sublime_api.window_transient_view_in_group(self.window_id, group)
        if view_id != 0:
            return View(view_id)
        else:
            return None

    def layout(self):
        """Returns the current layout"""
        return sublime_api.window_get_layout(self.window_id)

    def get_layout(self):
        """deprecated, use `layout()` instead"""
        return sublime_api.window_get_layout(self.window_id)

    def set_layout(self, layout):
        """Changes the tile-based panel layout of view groups"""
        sublime_api.window_set_layout(self.window_id, layout)

    def create_output_panel(self, name, unlisted=False):
        """
        Returns the view associated with the named output panel, creating it if required
        The output panel can be shown by running the _show_panel_ window command,
        with the panel argument set to the _`name`_ with an "output." prefix.

        The optional _`unlisted`_ parameter is a boolean to control if the
        output panel should be listed in the panel switcher
        """
        return View(sublime_api.window_create_output_panel(self.window_id, name, unlisted))

    def find_output_panel(self, name):
        """
        Returns the view associated with the named output panel, or `None` if
        the output panel does not exist
        """
        view_id = sublime_api.window_find_output_panel(self.window_id, name)
        return View(view_id) if view_id else None

    def destroy_output_panel(self, name):
        """Destroys the named output panel, hiding it if currently open"""
        sublime_api.window_destroy_output_panel(self.window_id, name)

    def active_panel(self):
        """
        Returns the name of the currently open panel, or `None` if no panel is open
        Will return built-in panel names (e.g. "console", "find", etc)
        in addition to output panels
        """
        name = sublime_api.window_active_panel(self.window_id)
        return name or None

    def panels(self):
        """
        Returns a list of the names of all panels that have not been marked as unlisted
        Includes certain built-in panels in addition to output panels
        """
        return sublime_api.window_panels(self.window_id)

    def get_output_panel(self, name):
        """deprecated, use `create_output_panel()`"""
        return self.create_output_panel(name)

    def show_input_panel(self, caption, initial_text, on_done, on_change, on_cancel):
        """
        Shows the input panel, to collect a line of input from the user
        _`on_done`_ and _`on_change`_, if not `None`, should both be functions
        that expect a single string argument
        _`on_cancel`_ should be a function that expects no arguments
        The view used for the input widget is returned
        """
        return View(sublime_api.window_show_input_panel(
            self.window_id, caption, initial_text, on_done, on_change, on_cancel))

    def show_quick_panel(self, items, on_select, flags=0, selected_index=-1, on_highlight=None):
        """
        Shows a quick panel, to select an item in a list.

        * _`items`_ may be a list of strings, or a list of string lists
        In the latter case, each entry in the quick panel will show multiple rows.

        * _`on_select`_ will be called once, with the index of the selected item
        If the quick panel was cancelled, _`on_select`_ will be called with an
        argument of `-1`.

        * _`flags`_ is a bitwise OR of `MONOSPACE_FONT`
        and `KEEP_OPEN_ON_FOCUS_LOST`

        * _`on_highlighted`_, if given, will be called every time the highlighted item in the quick panel is changed
        """
        items_per_row = 1
        flat_items = items
        if len(items) > 0 and isinstance(items[0], list):
            items_per_row = len(items[0])
            flat_items = []

            for i in range(len(items)):
                if isinstance(items[i], str):
                    flat_items.append(items[i])
                    for j in range(1, items_per_row):
                        flat_items.append("")
                else:
                    for j in range(items_per_row):
                        flat_items.append(items[i][j])

        sublime_api.window_show_quick_panel(
            self.window_id, flat_items, items_per_row, on_select, on_highlight,
            flags, selected_index)

    def is_sidebar_visible(self):
        """Returns `True` if the sidebar will be shown when contents are available"""
        return sublime_api.window_is_ui_element_visible(self.window_id, UI_ELEMENT_SIDE_BAR)

    def set_sidebar_visible(self, flag):
        """Sets the sidebar to be shown or hidden when contents are available"""
        sublime_api.window_set_ui_element_visible(self.window_id, UI_ELEMENT_SIDE_BAR, flag)

    def is_minimap_visible(self):
        """Returns `True` if the minimap is enabled"""
        return sublime_api.window_is_ui_element_visible(self.window_id, UI_ELEMENT_MINIMAP)

    def set_minimap_visible(self, flag):
        """Controls the visibility of the minimap"""
        sublime_api.window_set_ui_element_visible(self.window_id, UI_ELEMENT_MINIMAP, flag)

    def is_status_bar_visible(self):
        """Returns `True` if the status bar will be shown"""
        return sublime_api.window_is_ui_element_visible(self.window_id, UI_ELEMENT_STATUS_BAR)

    def set_status_bar_visible(self, flag):
        """Controls the visibility of the status bar"""
        sublime_api.window_set_ui_element_visible(self.window_id, UI_ELEMENT_STATUS_BAR, flag)

    def get_tabs_visible(self):
        """Returns `True` if tabs will be shown for open files"""
        return sublime_api.window_is_ui_element_visible(self.window_id, UI_ELEMENT_TABS)

    def set_tabs_visible(self, flag):
        """Controls if tabs will be shown for open files"""
        sublime_api.window_set_ui_element_visible(self.window_id, UI_ELEMENT_TABS, flag)

    def is_menu_visible(self):
        """Returns `True` if the menu is visible"""
        return sublime_api.window_is_ui_element_visible(self.window_id, UI_ELEMENT_MENU)

    def set_menu_visible(self, flag):
        """Controls if the menu is visible"""
        sublime_api.window_set_ui_element_visible(self.window_id, UI_ELEMENT_MENU, flag)

    def folders(self):
        """Returns a list of the currently open folders"""
        return sublime_api.window_folders(self.window_id)

    def project_file_name(self):
        """Returns name of the currently opened project file, if any"""
        name = sublime_api.window_project_file_name(self.window_id)
        if len(name) == 0:
            return None
        else:
            return name

    def project_data(self):
        """
        Returns the project data associated with the current window
        The data is in the same format as the contents of a _.sublime-project_ file
        """
        return sublime_api.window_get_project_data(self.window_id)

    def set_project_data(self, v):
        """
        Updates the project data associated with the current window
        If the window is associated with a _.sublime-project_ file, the project
        file will be updated on disk, otherwise the window will store the data
        internally
        """
        sublime_api.window_set_project_data(self.window_id, v)

    def settings(self):
        """Per-window settings, the contents are persisted in the session"""
        if not self.settings_object:
            self.settings_object = Settings(
                sublime_api.window_settings(self.window_id))

        return self.settings_object

    def template_settings(self):
        """
        Per-window settings that are persisted in the session, and duplicated
        into new windows
        """
        if not self.template_settings_object:
            self.template_settings_object = Settings(
                sublime_api.window_template_settings(self.window_id))

        return self.template_settings_object

    def lookup_symbol_in_index(self, sym):
        """
        Returns all locations where the symbol _`sym`_ is defined across files in
        the current project
        """
        return sublime_api.window_lookup_symbol(self.window_id, sym)

    def lookup_symbol_in_open_files(self, sym):
        """
        Returns all files and locations where the symbol _`sym`_ is defined, searching
        through open files
        """
        return sublime_api.window_lookup_symbol_in_open_files(self.window_id, sym)

    def lookup_references_in_index(self, sym):
        """
        Returns all files and locations where the symbol _`sym`_ is referenced,
        using the symbol index
        """
        return sublime_api.window_lookup_references(self.window_id, sym)

    def lookup_references_in_open_files(self, sym):
        """
        Returns all files and locations where the symbol _`sym`_ is referenced,
        searching through open files
        """
        return sublime_api.window_lookup_references_in_open_files(self.window_id, sym)

    def extract_variables(self):
        """
        Returns a dictionary of strings populated with contextual keys:
        _packages_, _platform_, _file_, _file_path_, _file_name_, _file_base_name_,
        _file_extension_, _folder_, _project_, _project_path_, _project_name_,
        _project_base_name_, _project_extension_
        This dict is suitable for passing to `sublime.expand_variables()`
        """
        return sublime_api.window_extract_variables(self.window_id)

    def status_message(self, msg):
        """Show a message in the status bar"""
        sublime_api.window_status_message(self.window_id, msg)


class Edit(object):
    """
    `Edit` objects have no functions, they exist to group buffer modifications

    `Edit` objects are passed to `TextCommands`, and can not be created by the
    user. Using an invalid `Edit` object, or an `Edit` object from a different view,
    will cause the functions that require them to fail
    """

    def __init__(self, token):
        self.edit_token = token


class Region(object):
    """Represents an area of the buffer. Empty regions, where `a == b` are valid"""
    __slots__ = ['a', 'b', 'xpos']

    def __init__(self, a, b=None, xpos=-1):
        if b is None:
            b = a
        self.a = a
        self.b = b
        self.xpos = xpos

    def __str__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ")"

    def __repr__(self):
        return "(" + str(self.a) + ", " + str(self.b) + ")"

    def __len__(self):
        return self.size()

    def __eq__(self, rhs):
        return isinstance(rhs, Region) and self.a == rhs.a and self.b == rhs.b

    def __lt__(self, rhs):
        lhs_begin = self.begin()
        rhs_begin = rhs.begin()

        if lhs_begin == rhs_begin:
            return self.end() < rhs.end()
        else:
            return lhs_begin < rhs_begin

    def empty(self):
        """Returns `True` if `begin() == end()`"""
        return self.a == self.b

    def begin(self):
        """Returns the minimum of `a` and `b`"""
        if self.a < self.b:
            return self.a
        else:
            return self.b

    def end(self):
        """Returns the maximum of `a` and `b`"""
        if self.a < self.b:
            return self.b
        else:
            return self.a

    def size(self):
        """
        deprecated, use `len()` instead
        Returns the number of characters spanned by the region. Always >= 0
        """
        return abs(self.a - self.b)

    def contains(self, x):
        """
        If `x` is a region, returns `True` if it's a subset
        If `x` is a point, returns `True` if `begin() <= x <= end()`
        """
        if isinstance(x, Region):
            return self.contains(x.a) and self.contains(x.b)
        else:
            return x >= self.begin() and x <= self.end()

    def cover(self, rhs):
        """Returns a `Region` spanning both this and the given regions"""
        a = min(self.begin(), rhs.begin())
        b = max(self.end(), rhs.end())

        if self.a < self.b:
            return Region(a, b)
        else:
            return Region(b, a)

    def intersection(self, rhs):
        """Returns the set intersection of the two regions"""
        if self.end() <= rhs.begin():
            return Region(0)
        if self.begin() >= rhs.end():
            return Region(0)

        return Region(max(self.begin(), rhs.begin()), min(self.end(), rhs.end()))

    def intersects(self, rhs):
        """
        Returns `True` if `self == rhs` or both include one or more
        positions in common
        """
        lb = self.begin()
        le = self.end()
        rb = rhs.begin()
        re = rhs.end()

        return (
            (lb == rb and le == re) or
            (rb > lb and rb < le) or (re > lb and re < le) or
            (lb > rb and lb < re) or (le > rb and le < re))


class Selection(object):
    """
    Maintains a set of Regions, ensuring that none overlap
    The regions are kept in sorted order
    """

    def __init__(self, id):
        self.view_id = id

    def __len__(self):
        return sublime_api.view_selection_size(self.view_id)

    def __getitem__(self, index):
        r = sublime_api.view_selection_get(self.view_id, index)
        if r.a == -1:
            raise IndexError()
        return r

    def __delitem__(self, index):
        sublime_api.view_selection_erase(self.view_id, index)

    def __eq__(self, rhs):
        return rhs is not None and list(self) == list(rhs)

    def __lt__(self, rhs):
        return rhs is not None and list(self) < list(rhs)

    def __bool__(self):
        return self.view_id != 0

    def __contains__(self, region):
        return sublime_api.view_selection_contains(self.view_id, region.a, region.b)

    def is_valid(self):
        return sublime_api.view_buffer_id(self.view_id) != 0

    def clear(self):
        """Removes all regions"""
        sublime_api.view_selection_clear(self.view_id)

    def add(self, x):
        """
        Adds the given region or point. It will be merged with any intersecting
        regions already contained within the set
        """
        if isinstance(x, Region):
            sublime_api.view_selection_add_region(self.view_id, x.a, x.b, x.xpos)
        else:
            sublime_api.view_selection_add_point(self.view_id, x)

    def add_all(self, regions):
        """Adds all _`regions`_ in the given list or tuple"""
        for r in regions:
            self.add(r)

    def subtract(self, region):
        """Subtracts the _`region`_ from all regions in the set"""
        sublime_api.view_selection_subtract_region(self.view_id, region.a, region.b)

    def contains(self, region):
        """
        deprecated, use `in` instead
        Returns `True` if the given _`region`_ is a subset
        """
        return sublime_api.view_selection_contains(self.view_id, region.a, region.b)


class Sheet(object):
    """
    Represents a content container, i.e. a tab, within a window
    Sheets may contain a View, or an image preview
    """

    def __init__(self, id):
        self.sheet_id = id

    def __eq__(self, other):
        return isinstance(other, Sheet) and other.sheet_id == self.sheet_id

    def id(self):
        """Returns a number that uniquely identifies this sheet"""
        return self.sheet_id

    def window(self):
        """
        Returns the window containing the sheet. May be `None` if the sheet
        has been closed
        """
        window_id = sublime_api.sheet_window(self.sheet_id)
        if window_id == 0:
            return None
        else:
            return Window(window_id)

    def view(self):
        """
        Returns the view contained within the sheet. May be `None` if the
        sheet is an image preview, or the view has been closed
        """
        view_id = sublime_api.sheet_view(self.sheet_id)
        if view_id == 0:
            return None
        else:
            return View(view_id)


class View(object):
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

    def id(self):
        """Returns a number that uniquely identifies this view"""
        return self.view_id

    def buffer_id(self):
        """Returns a number that uniquely identifies the buffer underlying this view"""
        return sublime_api.view_buffer_id(self.view_id)

    def is_valid(self):
        """
        Returns `True` if the View is still a valid handle. Will return `False`
        for a closed view, for example
        """
        return sublime_api.view_buffer_id(self.view_id) != 0

    def is_primary(self):
        """
        Returns `True` if the view is the primary view into a file
        Will only be `False` if the user has opened multiple views into a file
        """
        return sublime_api.view_is_primary(self.view_id)

    def window(self):
        """Returns a reference to the window containing the view"""
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
        """The name assigned to the buffer, if any"""
        return sublime_api.view_get_name(self.view_id)

    def set_name(self, name):
        """Assigns a _`name`_ to the buffer"""
        sublime_api.view_set_name(self.view_id, name)

    def is_loading(self):
        """
        Returns `True` if the buffer is still loading from disk,
        and not ready for use
        """
        return sublime_api.view_is_loading(self.view_id)

    def is_dirty(self):
        """Returns `True` if there are any unsaved modifications to the buffer"""
        return sublime_api.view_is_dirty(self.view_id)

    def is_read_only(self):
        """Returns `True` if the buffer may not be modified"""
        return sublime_api.view_is_read_only(self.view_id)

    def set_read_only(self, read_only):
        """Sets the read only property on the buffer"""
        return sublime_api.view_set_read_only(self.view_id, read_only)

    def is_scratch(self):
        """
        Returns `True` if the buffer is a scratch buffer. Scratch buffers
        never report as being dirty
        """
        return sublime_api.view_is_scratch(self.view_id)

    def set_scratch(self, scratch):
        """
        Sets the _`scratch`_ flag on the text buffer. When a modified scratch
        buffer is closed, it will be closed without prompting to save.
        """
        return sublime_api.view_set_scratch(self.view_id, scratch)

    def encoding(self):
        """Returns the encoding currently associated with the file"""
        return sublime_api.view_encoding(self.view_id)

    def set_encoding(self, encoding_name):
        """Applies a new encoding to the file. This encoding will be used the
        next time the file is saved"""
        return sublime_api.view_set_encoding(self.view_id, encoding_name)

    def line_endings(self):
        """Returns the line endings used by the current file"""
        return sublime_api.view_line_endings(self.view_id)

    def set_line_endings(self, line_ending_name):
        """Sets the line endings that will be applied when next saving"""
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
            raise ValueError("Edit objects may not be used after the TextCommand's run method has returned")

        return sublime_api.view_insert(self.view_id, edit.edit_token, pt, text)

    def erase(self, edit, r):
        """Erases the contents of the region from the buffer"""
        if edit.edit_token == 0:
            raise ValueError("Edit objects may not be used after the TextCommand's run method has returned")

        sublime_api.view_erase(self.view_id, edit.edit_token, r)

    def replace(self, edit, r, text):
        """Replaces the contents of the region with the given string"""
        if edit.edit_token == 0:
            raise ValueError("Edit objects may not be used after the TextCommand's run method has returned")

        sublime_api.view_replace(self.view_id, edit.edit_token, r, text)

    def change_count(self):
        """
        Returns the current change count. Each time the buffer is modified,
        the change count is incremented. The change count can be used to
        determine if the buffer has changed since the last it was inspected
        """
        return sublime_api.view_change_count(self.view_id)

    def run_command(self, cmd, args=None):
        """Runs the named `TextCommand` with the (optional) given _`args`_"""
        sublime_api.view_run_command(self.view_id, cmd, args)

    def sel(self):
        """Returns a reference to the selection"""
        return self.selection

    def substr(self, x):
        """
        if _`x`_ is a region, returns it's contents as a string
        if _`x`_ is a point, returns the character to it's right
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
        Returns the first region matching the regex _`pattern`_, starting from
        _`start_pt`_, or `None` if it can't be found. The optional _`flags`_
        parameter may be `LITERAL`, `IGNORECASE`, or the two
        ORed together
        """
        return sublime_api.view_find(self.view_id, pattern, start_pt, flags)

    def find_all(self, pattern, flags=0, fmt=None, extractions=None):
        """
        Returns all (non-overlapping) regions matching the regex _`pattern`_
        The optional _`flags`_ parameter may be `LITERAL`,
        `IGNORECASE`, or the two ORed together. If a format string is
        given, then all matches will be formatted with the formatted string
        and placed into the _`extractions`_ list
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
        """Returns the syntax scope name assigned to the character at the given point"""
        return sublime_api.view_scope_name(self.view_id, pt)

    def match_selector(self, pt, selector):
        """
        Checks the _`selector`_ against the scope at the given point
        returning a bool if they match
        """
        return sublime_api.view_match_selector(self.view_id, pt, selector)

    def score_selector(self, pt, selector):
        """
        Matches the _`selector`_ against the scope at the given point, returning a score
        A score of 0 means no match, above 0 means a match. Different selectors may
        be compared against the same scope: a higher score means the selector
        is a better match for the scope
        """
        return sublime_api.view_score_selector(self.view_id, pt, selector)

    def find_by_selector(self, selector):
        """
        Finds all regions in the file matching the given _`selector`_,
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
        Accepts a string _`scope`_ and returns a dict of style information,
        include the keys _foreground_, _bold_, _italic_, _source_line_,
        _source_column_ and _source_file_.
        If the _`scope`_ has a background color set, the key _background_ will
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
        """Returns a list of lines (in sorted order) intersecting the region _`r`_"""
        return sublime_api.view_lines(self.view_id, r)

    def split_by_newlines(self, r):
        """Splits the region up such that each region returned exists on
        exactly one line"""
        return sublime_api.view_split_by_newlines(self.view_id, r)

    def line(self, x):
        """
        if _`x`_ is a region, returns a modified copy of region such that it
        starts at the beginning of a line, and ends at the end of a line
        Note that it may span several lines
        if _`x`_ is a point, returns the line that contains the point
        """
        if isinstance(x, Region):
            return sublime_api.view_line_from_region(self.view_id, x)
        else:
            return sublime_api.view_line_from_point(self.view_id, x)

    def full_line(self, x):
        """As line(), but the region includes the trailing newline character, if any"""
        if isinstance(x, Region):
            return sublime_api.view_full_line_from_region(self.view_id, x)
        else:
            return sublime_api.view_full_line_from_point(self.view_id, x)

    def word(self, x):
        """
        if _`x`_ is a region, returns a modified copy of it such that it
        starts at the beginning of a word, and ends at the end of a word
        Note that it may span several words
        if _`x`_ is a point, returns the word that contains it
        """
        if isinstance(x, Region):
            return sublime_api.view_word_from_region(self.view_id, x)
        else:
            return sublime_api.view_word_from_point(self.view_id, x)

    def classify(self, pt):
        """
        Classifies the point _`pt`_, returning a bitwise OR of zero or more of these flags:
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
        _`separators`_ may be passed in, to define what characters should be
        considered to separate words
        """
        return sublime_api.view_find_by_class(self.view_id, pt, forward, classes, separators)

    def expand_by_class(self, x, classes, separators=""):
        """
        Expands _`x`_ to the left and right, until each side lands on a location
        that matches _`classes`_. classes is a bitwise OR of the
        `CLASS_XXX` flags. _`separators`_ may be passed in, to define
        what characters should be considered to separate words
        """
        if isinstance(x, Region):
            return sublime_api.view_expand_by_class(self.view_id, x.a, x.b, classes, separators)
        else:
            return sublime_api.view_expand_by_class(self.view_id, x, x, classes, separators)

    def rowcol(self, tp):
        """Calculates the 0-based line and column numbers of the the given point"""
        return sublime_api.view_row_col(self.view_id, tp)

    def text_point(self, row, col):
        """Converts a row and column into a text point"""
        return sublime_api.view_text_point(self.view_id, row, col)

    def visible_region(self):
        """Returns the approximate visible region"""
        return sublime_api.view_visible_region(self.view_id)

    def show(self, x, show_surrounds=True):
        """Scrolls the view to reveal x, which may be a Region or point"""
        if isinstance(x, Region):
            return sublime_api.view_show_region(self.view_id, x, show_surrounds)
        if isinstance(x, Selection):
            for i in x:
                return sublime_api.view_show_region(self.view_id, i, show_surrounds)
        else:
            return sublime_api.view_show_point(self.view_id, x, show_surrounds)

    def show_at_center(self, x):
        """Scrolls the view to center on x, which may be a Region or point"""
        if isinstance(x, Region):
            return sublime_api.view_show_region_at_center(self.view_id, x)
        else:
            return sublime_api.view_show_point_at_center(self.view_id, x)

    def viewport_position(self):
        """Returns the (x, y) scroll position of the view in layout coordinates"""
        return sublime_api.view_viewport_position(self.view_id)

    def set_viewport_position(self, xy, animate=True):
        """Scrolls the view to the given position in layout coordinates"""
        sublime_api.view_set_viewport_position(self.view_id, xy, animate)

    def viewport_extent(self):
        """Returns the width and height of the viewport, in layout coordinates"""
        return sublime_api.view_viewport_extents(self.view_id)

    def layout_extent(self):
        """Returns the total height and width of the document, in layout coordinates"""
        return sublime_api.view_layout_extents(self.view_id)

    def text_to_layout(self, tp):
        """Converts a text point to layout coordinates"""
        return sublime_api.view_text_to_layout(self.view_id, tp)

    def text_to_window(self, tp):
        """Converts a text point to window coordinates"""
        return self.layout_to_window(self.text_to_layout(tp))

    def layout_to_text(self, xy):
        """Converts layout coordinates to a text point"""
        return sublime_api.view_layout_to_text(self.view_id, xy)

    def layout_to_window(self, xy):
        """Converts layout coordinates to window coordinates"""
        return sublime_api.view_layout_to_window(self.view_id, xy)

    def window_to_layout(self, xy):
        """Converts window coordinates to layout coordinates"""
        return sublime_api.view_window_to_layout(self.view_id, xy)

    def window_to_text(self, xy):
        """Converts window coordinates to a text point"""
        return self.layout_to_text(self.window_to_layout(xy))

    def line_height(self):
        """Returns the height of a line in layout coordinates"""
        return sublime_api.view_line_height(self.view_id)

    def em_width(self):
        """Returns the em-width of the current font in layout coordinates"""
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
        """Unfolds all text in the region(s), returning the unfolded regions"""
        if isinstance(x, Region):
            return sublime_api.view_unfold_region(self.view_id, x)
        else:
            return sublime_api.view_unfold_regions(self.view_id, x)

    def add_regions(self, key, regions, scope="", icon="", flags=0):
        """
        Add a set of _`regions`_ to the view. If a set of regions already exists
        with the given _`key`_, they will be overwritten. The _`scope`_ is used
        to source a color to draw the regions in, it should be the name of a
        scope, such as "comment" or "string". If the scope is empty, the
        regions won't be drawn.

        The optional _`icon`_ name, if given, will draw the named icons in the
        gutter next to each region. The _`icon`_ will be tinted using the color
        associated with the _`scope`_. Valid icon names are dot, circle and
        bookmark. The _`icon`_ name may also be a full package relative path
        such as _Packages/Theme - Default/dot.png_.

        The optional _`flags`_ parameter is a bitwise combination of:

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

        sublime_api.view_add_regions(self.view_id, key, regions, scope, icon, flags)

    def get_regions(self, key):
        """Return the regions associated with the given _`key`_, if any"""
        return sublime_api.view_get_regions(self.view_id, key)

    def erase_regions(self, key):
        """Remove the named regions"""
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
        """Deprecated, use `assign_syntax()` instead"""
        self.assign_syntax(syntax_file)

    def symbols(self):
        """Extract all the symbols defined in the buffer"""
        return sublime_api.view_symbols(self.view_id)

    def get_symbols(self):
        """Deprecated, use `symbols()`"""
        return self.symbols()

    def indexed_symbols(self):
        return sublime_api.view_indexed_symbols(self.view_id)

    def indexed_references(self):
        return sublime_api.view_indexed_references(self.view_id)

    def set_status(self, key, value):
        """
        Adds the status _`key`_ to the view. The value will be displayed in the
        status bar, in a comma separated list of all status values, ordered by key
        Setting the value to the empty string will clear the status
        """
        sublime_api.view_set_status(self.view_id, key, value)

    def get_status(self, key):
        """Returns the previously assigned value associated with the _`key`_, if any"""
        return sublime_api.view_get_status(self.view_id, key)

    def erase_status(self, key):
        """Clears the named status"""
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
        that, and so on. Positive values for _`delta`_ indicates to look in the
        redo stack for commands. If the undo / redo history doesn't extend far
        enough, then `(None, None, 0)` will be returned.

        Setting `modifying_only` to `True` will only return entries that
        modified the buffer
        """
        return sublime_api.view_command_history(self.view_id, delta, modifying_only)

    def overwrite_status(self):
        """Returns the overwrite status, which the user normally toggles via the insert key"""
        return sublime_api.view_get_overwrite_status(self.view_id)

    def set_overwrite_status(self, value):
        """Sets the overwrite status"""
        sublime_api.view_set_overwrite_status(self.view_id, value)

    def show_popup_menu(self, items, on_select, flags=0):
        """
        Shows a pop up menu at the caret, to select an item in a list. _`on_done`_
        will be called once, with the index of the selected item. If the pop up
        menu was cancelled, _`on_done`_ will be called with an argument of -1.

        _`items`_ is a list of strings.

        _`flags`_ is currently unused
        """
        return sublime_api.view_show_popup_table(self.view_id, items, on_select, flags, -1)

    def show_popup(self, content, flags=0, location=-1,
                   max_width=320, max_height=240,
                   on_navigate=None, on_hide=None):
        """
        Shows a popup displaying HTML content.

        * _`flags`_ is a bitwise combination of the following:

        `COOPERATE_WITH_AUTO_COMPLETE`: Causes the popup to display next to the auto complete menu
        `HIDE_ON_MOUSE_MOVE`: Causes the popup to hide when the mouse is moved, clicked or scrolled
        `HIDE_ON_MOUSE_MOVE_AWAY`: Causes the popup to hide when the mouse is moved
                                    (unless towards the popup), or when clicked or scrolled
        * _`location`_ sets the location of the popup, if -1 (default) will display
        the popup at the cursor, otherwise a text point should be passed.

        * _`max_width`_ and _`max_height`_ set the maximum dimensions for the popup,
        after which scroll bars will be displayed.

        * _`on_navigate`_ is a callback that should accept a string contents of the
        href attribute on the link the user clicked.

        * _`on_hide`_ is called when the popup is hidden
        """
        sublime_api.view_show_popup(
            self.view_id, location, content, flags, max_width, max_height,
            on_navigate, on_hide)

    def update_popup(self, content):
        """Updates the contents of the currently visible popup"""
        sublime_api.view_update_popup_content(self.view_id, content)

    def is_popup_visible(self):
        """Returns if the popup is currently shown"""
        return sublime_api.view_is_popup_visible(self.view_id)

    def hide_popup(self):
        """Hides the popup"""
        sublime_api.view_hide_popup(self.view_id)

    def is_auto_complete_visible(self):
        """Returns wether the auto complete menu is currently visible"""
        return sublime_api.view_is_auto_complete_visible(self.view_id)


class Settings(object):

    def __init__(self, id):
        self.settings_id = id

    def get(self, key, default=None):
        """
        Returns the named setting, or _`default`_ if it's not defined
        If not passed, _`default`_ will have a value of `None`
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
        """Sets the named setting. Only primitive types, lists, and dicts are accepted"""
        sublime_api.settings_set(self.settings_id, key, value)

    def erase(self, key):
        """Removes the named setting. Does not remove it from any parent Settings"""
        sublime_api.settings_erase(self.settings_id, key)

    def add_on_change(self, tag, callback):
        """Register a _`callback`_ to be run whenever a setting in this object is changed"""
        sublime_api.settings_add_on_change(self.settings_id, tag, callback)

    def clear_on_change(self, tag):
        """Remove all callbacks registered with the given _`tag`_"""
        sublime_api.settings_clear_on_change(self.settings_id, tag)


class Phantom(object):
    """
    Creates a phantom attached to a region

    * _`content`_ is HTML to be processed by _minihtml_.

    * _`layout`_ must be one of:

    - `LAYOUT_INLINE`: Display the phantom in between the region and the point following.
    - `LAYOUT_BELOW`: Display the phantom in space below the current line,
                    left-aligned with the region.
    - `LAYOUT_BLOCK`: Display the phantom in space below the current line,
    left-aligned with the beginning of the line.

    * _`on_navigate`_ is an optional callback that should accept a single string
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
        return (self.region == rhs.region and self.content == rhs.content and
                self.layout == rhs.layout and self.on_navigate == rhs.on_navigate)


class PhantomSet(object):
    """
    A collection that manages Phantoms and the process of adding them, updating
    them and removing them from the View.
    """

    def __init__(self, view, key=""):
        # deprecated
        self.view = view
        self.__view_id = view.view_id
        self.key = key
        self.phantoms = []

    def __del__(self):
        for p in self.phantoms:
            self.view.erase_phantom_by_id(p.id)

    def update(self, new_phantoms):
        """
        _`new_phantoms`_ should be a list of phantoms
        The `region` attribute of each existing phantom in the set will be updated
        New phantoms will be added to the view and phantoms not in phantoms list
        will be deleted
        """
        # Update the list of phantoms that exist in the text buffer with their
        # current location
        regions = self.view.query_phantoms([p.id for p in self.phantoms])
        for i in range(len(regions)):
            self.phantoms[i].region = regions[i]

        for p in new_phantoms:
            try:
                # Phantom already exists, copy the id from the current one
                idx = self.phantoms.index(p)
                p.id = self.phantoms[idx].id
            except ValueError:
                p.id = self.view.add_phantom(
                    self.key, p.region, p.content, p.layout, p.on_navigate)

        for p in self.phantoms:
            # if the region is -1, then it's already been deleted, no need to
            # call erase
            if p not in new_phantoms and p.region != Region(-1):
                self.view.erase_phantom_by_id(p.id)

        self.phantoms = new_phantoms


class Html(object):
    __slots__ = ['data']

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "Html(" + str(self.data) + ")"
