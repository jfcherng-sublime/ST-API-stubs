# version: 4081

from typing import (
    Callable,
    Dict,
    Iterable,
    List,
    ModuleType,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import TypedDict

import importlib
import io
import marshal
import os
import sys
import threading
import time
import traceback
import zipfile

import sublime

# ----- #
# types #
# ----- #

_T = TypeVar("_T")

T_CALLBACK_0 = Callable[[], None]
T_CALLBACK_1 = Callable[[_T], None]
T_COMPLETION = Union[str, List[str], Tuple[str, str], sublime.CompletionItem]
T_EXPANDABLE_VAR = TypeVar("T_EXPANDABLE_VAR", str, List[str], Dict[str, str])
T_KIND = Tuple[int, str, str]
T_LAYOUT = TypedDict(
    "T_LAYOUT",
    # fmt: off
    {
        "cols": Sequence[float],
        "rows": Sequence[float],
        "cells": Sequence[Sequence[int]],
    },
    # fmt: on
)
T_LOCATION = Tuple[str, str, Tuple[int, int]]
T_POINT = int
T_STR = str  # alias in case we have a variable named as "str"
T_VALUE = Union[Dict, Set, List, Tuple, str, int, float, bool, None]
T_VECTOR = Tuple[float, float]


# -------- #
# ST codes #
# -------- #


api_ready: bool = False

deferred_plugin_loadeds = []

application_command_classes = []
window_command_classes = []
text_command_classes = []

view_event_listener_classes = []
view_event_listeners = {}

all_command_classes = [application_command_classes, window_command_classes, text_command_classes]

all_callbacks = {
    "on_init": [],
    "on_new": [],
    "on_clone": [],
    "on_load": [],
    "on_revert": [],
    "on_reload": [],
    "on_pre_close": [],
    "on_close": [],
    "on_pre_save": [],
    "on_post_save": [],
    "on_pre_move": [],
    "on_post_move": [],
    "on_modified": [],
    "on_selection_modified": [],
    "on_activated": [],
    "on_deactivated": [],
    "on_query_context": [],
    "on_query_completions": [],
    "on_hover": [],
    "on_text_command": [],
    "on_window_command": [],
    "on_post_text_command": [],
    "on_post_window_command": [],
    "on_modified_async": [],
    "on_selection_modified_async": [],
    "on_pre_save_async": [],
    "on_post_save_async": [],
    "on_post_move_async": [],
    "on_activated_async": [],
    "on_deactivated_async": [],
    "on_new_async": [],
    "on_load_async": [],
    "on_revert_async": [],
    "on_reload_async": [],
    "on_clone_async": [],
    "on_new_buffer": [],
    "on_new_buffer_async": [],
    "on_close_buffer": [],
    "on_close_buffer_async": [],
    "on_new_project": [],
    "on_new_project_async": [],
    "on_load_project": [],
    "on_load_project_async": [],
    "on_pre_save_project": [],
    "on_post_save_project": [],
    "on_post_save_project_async": [],
    "on_pre_close_project": [],
    "on_new_window": [],
    "on_new_window_async": [],
    "on_pre_close_window": [],
    "on_exit": [],
}

pending_on_activated_async_lock = threading.Lock()

pending_on_activated_async_callbacks = {"EventListener": [], "ViewEventListener": []}

view_event_listener_excluded_callbacks = {
    "on_clone",
    "on_clone_async",
    "on_exit",
    "on_init",
    "on_load_project",
    "on_load_project_async",
    "on_new",
    "on_new_async",
    "on_new_buffer",
    "on_new_buffer_async",
    "on_close_buffer",
    "on_close_buffer_async",
    "on_new_project",
    "on_new_project_async",
    "on_new_window",
    "on_new_window_async",
    "on_post_save_project",
    "on_post_save_project_async",
    "on_post_window_command",
    "on_pre_close_project",
    "on_pre_close_window",
    "on_pre_save_project",
    "on_window_command",
}

text_change_listener_classes = []
text_change_listener_callbacks = {
    "on_text_changed",
    "on_text_changed_async",
    "on_revert",
    "on_revert_async",
    "on_reload",
    "on_reload_async",
}

profile = {}


def add_profiling(event_handler):
    """
    Decorator to measure blocking event handler methods. Also prevents
    exceptions from interrupting other events handlers.

    :param event_handler:
        The event handler method - must be an unbound method

    :return:
        The decorated method
    """

    def profiler(*args):
        global profile
        t0 = time.time()
        try:
            return event_handler(*args)
        except (Exception) as e:
            # All this to include stack frames before the call to
            # event_handler() above
            tb = traceback.extract_stack()[:-1]
            tb += traceback.extract_tb(e.__traceback__)
            out = ["Traceback (most recent call last):\n"]
            out += traceback.format_list(tb)
            out += traceback.format_exception_only(type(e), e)
            print("".join(out), end="")
        finally:
            elapsed = time.time() - t0
            mod = event_handler.__module__
            p = profile.setdefault(event_handler.__name__, {})
            p.setdefault(mod, Summary()).record(elapsed)

    # Make the method look like the original for introspection
    profiler.__doc__ = event_handler.__doc__
    profiler.__name__ = event_handler.__name__
    profiler.__module__ = event_handler.__module__
    # Follow the pattern of decorators like @classmethod and @staticmethod
    profiler.__func__ = event_handler
    return profiler


def trap_exceptions(event_handler):
    """
    Decorator to prevent exceptions from interrupting other events handlers.

    :param event_handler:
        The event handler method - must be an unbound method

    :return:
        The decorated method
    """

    def exception_handler(*args):
        try:
            return event_handler(*args)
        except (Exception) as e:
            # All this to include stack frames before the call to
            # event_handler() above
            tb = traceback.extract_stack()[:-1]
            tb += traceback.extract_tb(e.__traceback__)
            out = ["Traceback (most recent call last):\n"]
            out += traceback.format_list(tb)
            out += traceback.format_exception_only(type(e), e)
            print("".join(out), end="")

    # Make the method look like the original for introspection
    exception_handler.__doc__ = event_handler.__doc__
    exception_handler.__name__ = event_handler.__name__
    exception_handler.__module__ = event_handler.__module__
    event_handler.__name__ = "_wrapped_%s" % event_handler.__name__
    # Follow the pattern of decorators like @classmethod and @staticmethod
    exception_handler.__func__ = event_handler
    return exception_handler


def decorate_handler(cls, method_name):
    """
    Decorates an event handler method with exception trapping, and in the case
    of blocking calls, profiling.

    :param cls:
        The class object to decorate

    :param method_name:
        A unicode string of the name of the method to decorate
    """

    # We have to use __dict__ rather than getattr(), otherwise the function
    # is passed through decorators, and we can't detect @classmethod and
    # @staticmethod
    method = cls.__dict__[method_name]
    if method_name.endswith("_async"):
        wrapper = trap_exceptions
    else:
        wrapper = add_profiling
    if isinstance(method, staticmethod):
        wrapped = staticmethod(wrapper(method.__func__))
    elif isinstance(method, classmethod):
        wrapped = classmethod(wrapper(method.__func__))
    else:
        wrapped = wrapper(method)
    setattr(cls, method_name, wrapped)


def unload_module(module: ModuleType) -> None:
    ...


def unload_plugin(modulename: str) -> None:
    ...


def reload_plugin(modulename: str) -> None:
    ...


def load_module(m: ModuleType) -> None:
    ...


def synthesize_on_activated_async() -> None:
    ...


def _instantiation_error(cls, e):
    rex = RuntimeError("unable to instantiate " f"'{cls.__module__}.{cls.__name__}'")
    rex.__cause__ = e
    traceback.print_exception(None, rex, None)


def notify_application_commands() -> None:
    ...


def create_application_commands():
    cmds = []
    for cls in application_command_classes:
        try:
            o = cls()
            cmds.append((o, o.name()))
        except Exception as e:
            _instantiation_error(cls, e)
    return cmds


def create_window_commands(window_id: int):
    window = sublime.Window(window_id)
    cmds = []
    for cls in window_command_classes:
        try:
            o = cls(window)
            cmds.append((o, o.name()))
        except Exception as e:
            _instantiation_error(cls, e)
    return cmds


def create_text_commands(view_id: int):
    view = sublime.View(view_id)
    cmds = []
    for cls in text_command_classes:
        try:
            o = cls(view)
            cmds.append((o, o.name()))
        except Exception as e:
            _instantiation_error(cls, e)
    return cmds


def on_api_ready() -> None:
    ...


def is_view_event_listener_applicable(cls, view: sublime.View) -> bool:
    ...


def create_view_event_listeners(classes, view: sublime.View) -> None:
    ...


def check_view_event_listeners(view: sublime.View) -> None:
    ...


def attach_view(view: sublime.View) -> None:
    ...


check_all_view_event_listeners_scheduled: bool = False


def check_all_view_event_listeners() -> None:
    ...


def detach_view(view: sublime.View) -> None:
    ...


def find_view_event_listener(view: sublime.View, cls):
    if view.view_id in view_event_listeners:
        for vel in view_event_listeners[view.view_id]:
            if vel.__class__ == cls:
                return vel
    return None


def attach_buffer(buf: sublime.Buffer) -> None:
    ...


def plugin_module_for_obj(obj):
    # Since objects in plugins may be defined deep in a sub-module, if we want
    # to filter by a module, we must make sure we are only looking at the
    # first two module labels
    cm = obj.__class__.__module__
    if cm.count(".") > 2:
        cm = ".".join(cm.split(".", 2)[0:2])
    return cm


def el_callbacks(name, listener_only=False):
    for el in all_callbacks[name]:
        yield el if listener_only else getattr(el, name)


def vel_callbacks(v, name, listener_only=False):
    for vel in view_event_listeners.get(v.view_id, []):
        if not hasattr(vel, name):
            continue
        yield vel if listener_only else getattr(vel, name)


def run_view_callbacks(
    name: str, view_id: int, *args: T_VALUE, attach: bool = False, el_only: bool = False,
) -> None:
    ...


def run_window_callbacks(name: str, window_id: int, *args: T_VALUE) -> None:
    ...


def on_init(module: str) -> None:
    """
    Trigger the on_init() methods on EventListener and ViewEventListener
    objects. This is method that allows event listeners to run something
    once per view, even if the view is done loading before the listener
    starts listening.

    :param module:
        A unicode string of the name of a plugin module to filter listeners by
    """
    ...


def on_new(view_id: int) -> None:
    ...


def on_new_async(view_id: int) -> None:
    ...


def on_new_buffer(buffer_id: int) -> None:
    ...


def on_new_buffer_async(buffer_id: int) -> None:
    ...


def on_close_buffer(buffer_id: int) -> None:
    ...


def on_close_buffer_async(buffer_id: int) -> None:
    ...


def on_clone(view_id: int) -> None:
    ...


def on_clone_async(view_id: int) -> None:
    ...


class Summary:
    max: float
    sum: float
    count: int

    def __init__(self) -> None:
        ...

    def record(self, x: float) -> None:
        ...


def get_profiling_data() -> List[Tuple[str, str, int, float, float]]:
    ...


def on_load(view_id: int) -> None:
    ...


def on_load_async(view_id: int) -> None:
    ...


def on_revert(view_id: int) -> None:
    ...


def on_revert_async(view_id: int) -> None:
    ...


def on_reload(view_id: int) -> None:
    ...


def on_reload_async(view_id: int) -> None:
    ...


def on_pre_close(view_id: int) -> None:
    ...


def on_close(view_id) -> None:
    ...


def on_pre_save(view_id: int) -> None:
    ...


def on_pre_save_async(view_id: int) -> None:
    ...


def on_post_save(view_id: int) -> None:
    ...


def on_post_save_async(view_id: int) -> None:
    ...


def on_pre_move(view_id: int) -> None:
    ...


def on_post_move(view_id: int) -> None:
    ...


def on_post_move_async(view_id: int) -> None:
    ...


def on_modified(view_id: int) -> None:
    ...


def on_modified_async(view_id: int) -> None:
    ...


def on_selection_modified(view_id: int) -> None:
    ...


def on_selection_modified_async(view_id: int) -> None:
    ...


def on_activated(view_id: int) -> None:
    ...


def on_activated_async(view_id: int) -> None:
    ...


def on_deactivated(view_id: int) -> None:
    ...


def on_deactivated_async(view_id: int) -> None:
    ...


def on_query_context(
    view_id: int, key: str, operator: str, operand: T_VALUE, match_all: bool
) -> bool:
    ...


def normalise_completion(c):
    def split_trigger(trigger):
        idx = trigger.find("\t")
        if idx < 0:
            return (trigger, "")
        else:
            return (trigger[0:idx], trigger[idx + 1 :])

    if not isinstance(c, sublime.CompletionItem):
        if isinstance(c, str):
            trigger, annotation = split_trigger(c)
            c = sublime.CompletionItem(trigger, annotation)
        elif len(c) == 1:
            trigger, annotation = split_trigger(c[0])
            c = sublime.CompletionItem(trigger, annotation)
        elif len(c) == 2:
            trigger, annotation = split_trigger(c[0])
            c = sublime.CompletionItem.snippet_completion(
                trigger, c[1], annotation, kind=sublime.KIND_AMBIGUOUS
            )
        elif len(c) == 3:
            trigger, annotation = split_trigger(c[0])
            c = sublime.CompletionItem.snippet_completion(
                trigger, c[2], annotation, kind=sublime.KIND_AMBIGUOUS
            )
        else:
            c = sublime.CompletionItem("")

    kind, kind_letter, kind_name = c.kind

    letter = 0
    if isinstance(kind_letter, str) and kind_letter != "":
        letter = ord(kind_letter)
    return (
        c.trigger,
        c.annotation,
        c.details,
        c.completion,
        kind_name,
        letter,
        c.completion_format,
        c.flags,
        kind,
    )


class MultiCompletionList:
    def __init__(self, num_completion_lists, view_id, req_id):
        self.remaining_calls = num_completion_lists
        self.view_id = view_id
        self.req_id = req_id
        self.completions = []
        self.flags = 0

    def completions_ready(self, completions, flags) -> None:
        # what's the type?
        # self.completions += [normalise_completion(c) for c in completions]
        ...


def on_query_completions(view_id: int, req_id: int, prefix: str, locations: List[T_POINT]) -> None:
    ...


def on_hover(view_id: int, point: T_POINT, hover_zone: int) -> None:
    ...


def on_text_command(
    view_id: int, name: str, args: Optional[Dict[str, T_VALUE]]
) -> Tuple[str, Optional[Dict]]:
    ...


def on_window_command(
    window_id: int, name: str, args: Optional[Dict[str, T_VALUE]]
) -> Tuple[str, Optional[Dict]]:
    ...


def on_post_text_command(view_id: int, name: str, args: Optional[Dict[str, T_VALUE]]) -> None:
    ...


def on_post_window_command(window_id: int, name: str, args: Optional[Dict[str, T_VALUE]]) -> None:
    ...


def on_new_project(window_id: int) -> None:
    ...


def on_new_project_async(window_id: int) -> None:
    ...


def on_load_project(window_id: int) -> None:
    ...


def on_load_project_async(window_id: int) -> None:
    ...


def on_pre_save_project(window_id: int) -> None:
    ...


def on_post_save_project(window_id: int) -> None:
    ...


def on_post_save_project_async(window_id: int) -> None:
    ...


def on_pre_close_project(window_id: int) -> None:
    ...


def on_new_window(window_id: int) -> None:
    ...


def on_new_window_async(window_id: int) -> None:
    ...


def on_pre_close_window(window_id: int) -> None:
    ...


def on_exit(log_path: str) -> None:
    ...


class CommandInputHandler:
    def name(self) -> str:
        """
        The command argument name this input handler is editing.
        Defaults to `foo_bar` for an input handler named `FooBarInputHandler`.
        """
        ...

    def next_input(self, args: Dict[str, T_VALUE]) -> Optional["CommandInputHandler"]:
        """
        Returns the next input after the user has completed this one.
        May return None to indicate no more input is required,
        or `sublime_plugin.BackInputHandler()` to indicate that
        the input handler should be poped off the stack instead.
        """
        ...

    def placeholder(self) -> str:
        """
        Placeholder text is shown in the text entry box before the user has entered anything.
        Empty by default.
        """
        ...

    def initial_text(self) -> str:
        """ Initial text shown in the text entry box. Empty by default. """
        ...

    def initial_selection(self) -> List:
        """
        @todo List of what???
        """
        ...

    def preview(self, arg: Dict[str, T_VALUE]) -> Union[str, sublime.Html]:
        """
        Called whenever the user changes the text in the entry box.
        The returned value (either plain text or HTML) will be shown in the preview area of the Command Palette.
        """
        ...

    def validate(self, arg: Dict[str, T_VALUE]) -> bool:
        """
        Called whenever the user presses enter in the text entry box.
        Return False to disallow the current value.
        """
        ...

    def cancel(self) -> None:
        """ Called when the input handler is canceled, either by the user pressing backspace or escape. """
        ...

    def confirm(self, text: Dict[str, T_VALUE]) -> None:
        """ Called when the input is accepted, after the user has pressed enter and the text has been validated. """
        ...

    def create_input_handler_(self, args: Dict[str, T_VALUE]) -> Optional["CommandInputHandler"]:
        ...

    def preview_(self, v: str) -> Tuple[str, int]:
        ...

    def validate_(self, v: str) -> bool:
        ...

    def cancel_(self) -> None:
        ...

    def confirm_(self, v: str) -> None:
        ...


class BackInputHandler(CommandInputHandler):
    def name(self) -> str:
        """ The command argument name this input handler is editing. Defaults to `_Back`. """
        ...


class TextInputHandler(CommandInputHandler):
    """
    TextInputHandlers can be used to accept textual input in the Command Palette.
    Return a subclass of this from the `input()` method of a command.
    """

    def description(self, text: str) -> str:
        """
        The text to show in the Command Palette when this input handler is not at the top of the input handler stack.
        Defaults to the text the user entered.
        """
        ...

    def setup_(self, args: Dict[str, T_VALUE]) -> Tuple[list, Dict[str, str]]:
        ...

    def description_(self, v: str, text: str) -> str:
        ...


class ListInputHandler(CommandInputHandler):
    """
    ListInputHandlers can be used to accept a choice input from a list items in the Command Palette.
    Return a subclass of this from the input() method of a command.
    """

    def list_items(
        self,
    ) -> Union[
        List[str],
        List[Tuple[str, T_VALUE]],
        Tuple[Union[List[str], List[Tuple[str, T_VALUE]]], int],
    ]:
        """
        The items to show in the list. If returning a list of `(str, value)` tuples,
        then the str will be shown to the user, while the value will be used as the command argument.

        Optionally return a tuple of `(list_items, selected_item_index)` to indicate an initial selection.
        """
        ...

    def description(self, v: str, text: str) -> str:
        """
        The text to show in the Command Palette when this input handler is not at the top of the input handler stack.
        Defaults to the text of the list item the user selected.
        """
        ...

    def setup_(self, args: Dict[str, T_VALUE]) -> Tuple[List[Tuple[str, T_VALUE]], Dict[str, str]]:
        ...

    def description_(self, v: str, text: str) -> str:
        ...


class Command:
    def name(self) -> str:
        """
        The command argument name this input handler is editing.
        Defaults to `foo_bar` for an input handler named `FooBarInputHandler`.
        """
        ...

    def is_enabled_(self, args: Dict[str, T_VALUE]) -> bool:
        ...

    def is_enabled(self) -> bool:
        """
        Returns True if the command is able to be run at this time.
        The default implementation simply always returns True.
        """
        ...

    def is_visible_(self, args: Dict[str, T_VALUE]) -> bool:
        ...

    def is_visible(self) -> bool:
        """
        Returns True if the command should be shown in the menu at this time.
        The default implementation always returns True.
        """
        ...

    def is_checked_(self, args: Dict[str, T_VALUE]) -> bool:
        ...

    def is_checked(self) -> bool:
        """
        Returns True if a checkbox should be shown next to the menu item.
        The `.sublime-menu` file must have the "checkbox key set to true for this to be used.
        """
        ...

    def description_(self, args: Dict[str, T_VALUE]) -> str:
        ...

    def description(self) -> str:
        """
        Returns a description of the command with the given arguments.
        Used in the menus, and for Undo / Redo descriptions.
        Return None to get the default description.
        """
        ...

    def filter_args(self, args: Dict[str, T_VALUE]) -> Dict[str, T_VALUE]:
        """ Returns the args after without the "event" entry """
        ...

    def want_event(self) -> bool:
        """
        Return True to receive an event argument when the command is triggered by a mouse action.
        The event information allows commands to determine which portion of the view was clicked on.
        The default implementation returns False.
        """
        ...

    def input(self, args: Dict[str, T_VALUE]) -> Optional[CommandInputHandler]:
        """
        If this returns something other than None,
        the user will be prompted for an input before the command is run in the Command Palette.
        """
        ...

    def input_description(self) -> str:
        """
        Allows a custom name to be show to the left of the cursor in the input box,
        instead of the default one generated from the command name.
        """
        ...

    def create_input_handler_(self, args: Dict[str, T_VALUE]) -> Optional[CommandInputHandler]:
        ...


class ApplicationCommand(Command):
    """ ApplicationCommands are instantiated once per application. """

    def run_(self, edit_token: int, args: Dict[str, T_VALUE]) -> None:
        ...

    def run(self) -> None:
        """ Called when the command is run """
        ...


class WindowCommand(Command):
    """ WindowCommands are instantiated once per window. The Window object may be retrieved via `self.window` """

    window: sublime.Window

    def __init__(self, window: sublime.Window) -> None:
        ...

    def run_(self, edit_token: int, args: Dict[str, T_VALUE]) -> None:
        ...

    def run(self) -> None:
        """ Called when the command is run """
        ...


class TextCommand(Command):
    """ TextCommands are instantiated once per view. The View object may be retrieved via `self.view` """

    view: sublime.View

    def __init__(self, view: sublime.View) -> None:
        ...

    def run_(self, edit_token: int, args: Dict[str, T_VALUE]) -> None:
        ...

    def run(self) -> None:
        """ Called when the command is run """
        ...


class EventListener:
    pass


class ViewEventListener:
    """
    A class that provides similar event handling to EventListener, but bound to a specific view.
    Provides class method-based filtering to control what views objects are created for.

    The view is passed as a single parameter to the constructor.
    The default implementation makes the view available via `self.view`.
    """

    view: sublime.View

    @classmethod
    def is_applicable(cls, settings: sublime.Settings) -> bool:
        """
        Receives a Settings object and should return a bool
        indicating if this class applies to a view with those settings.
        """
        ...

    @classmethod
    def applies_to_primary_view_only(cls) -> bool:
        """
        Returns a bool indicating if this class applies only to the primary view for a file.
        A view is considered primary if it is the only, or first, view into a file.
        """
        ...

    def __init__(self, view: sublime.View) -> None:
        ...


class TextChangeListener:
    """ Base implementation of a text change listener.

    An instance may be added to a view using `sublime.View.add_text_listener`.

    Has the following callbacks:

    on_text_changed(changes):
        Called when text is changed in a buffer.

        :param changes:
            A list of TextChange

    on_text_changed_async(changes):
        Async version of on_text_changed_async.

    on_revert():
        Called when the buffer is reverted.

        A revert does not trigger text changes. If the contents of the buffer
        are required here use View.substr()

    on_revert_async():
        Async version of on_revert_async.

    on_reload():
        Called when the buffer is reloaded.

        A reload does not trigger text changes. If the contents of the buffer
        are required here use View.substr()

    on_reload_async():
        Async version of on_reload_async.
    """

    __key: Optional[int] = None
    buffer: Optional[sublime.Buffer] = None

    @classmethod
    def is_applicable(cls, buffer: sublime.Buffer) -> bool:
        """
        Receives a Buffer object and should return a bool
        indicating if this class applies to a view with the Buffer.
        """
        ...

    def __init__(self, buffer: sublime.Buffer) -> None:
        ...

    def remove(self) -> None:
        """
        Remove this listener from the buffer.

        Async callbacks may still be called after this, as they are queued separately.
        """
        ...

    def attach(self, buffer: sublime.Buffer) -> None:
        """ Attach this listener to a buffer. """
        ...

    def is_attached(self) -> bool:
        """
        Check whether the listener is receiving events from a buffer.
        May not be called from __init__.
        """
        ...


class MultizipImporter(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.loaders = []

    def _make_spec(self, loader, fullname):
        """
        :param loader:
            The importlib.abc.Loader to create the ModuleSpec from

        :param fullname:
            A unicode string of the module name

        :return:
            An instance of importlib.machinery.ModuleSpec()
        """

        origin, is_package = loader._spec_info(fullname)
        spec = importlib.util.spec_from_loader(
            fullname, loader, origin=origin, is_package=is_package
        )
        if is_package:
            spec.submodule_search_locations = [loader.zippath]
        return spec

    def find_spec(self, fullname, path, target=None):
        """
        :param fullname:
            A unicode string of the module name

        :param path:
            None or a list with a single unicode string of the __path__ of
            the parent module if importing a submodule

        :param target:
            Unused - extra info that importlib may provide?

        :return:
            An importlib.machinery.ModuleSpec() object
        """

        if not path:
            for l in self.loaders:
                if l.has(fullname):
                    return self._make_spec(l, fullname)

        for l in self.loaders:
            if path == [l.zippath] and l.has(fullname):
                return self._make_spec(l, fullname)

        return None


class ZipResourceReader(importlib.abc.ResourceReader):
    """
    Implements the resource reader interface introduced in Python 3.7
    """

    def __init__(self, loader, fullname):
        """
        :param loader:
            The source ZipLoader() object

        :param fullname:
            A unicode string of the module name to load resources for
        """

        self.loader = loader
        self.fullname = fullname

    def open_resource(self, resource):
        """
        :param resource:
            A unicode string of a resource name - should not contain a path
            separator

        :raises:
            FileNotFoundError - when the resource doesn't exist

        :return:
            An io.BytesIO() object
        """

        rel_zip_path = self.loader.resources.get(self.fullname, {}).get(resource)
        if not rel_zip_path:
            raise FileNotFoundError()
        with zipfile.ZipFile(self.loader.zippath, "r") as z:
            return io.BytesIO(z.read(rel_zip_path))

    def resource_path(self, resource):
        """
        :param resource:
            A unicode string of a resource name - should not contain a path
            separator

        :raises:
            FileNotFoundError - always, since there is no normal filesystem access
        """

        raise FileNotFoundError()

    def is_resource(self, name):
        """
        :param name:
            A unicode string of a file name to check if it is a resource

        :return:
            A boolean indicating if the file is a resource
        """

        return name in self.loader.resources.get(self.fullname, {})

    def contents(self):
        """
        :return:
            A list of the resources for this module
        """

        return sorted([k for k in self.loader.resources.get(self.fullname, {})])


class ZipLoader(importlib.abc.InspectLoader):
    """
    A custom Python loader that handles loading .py and .pyc files from
    .sublime-package zip files, and supports overrides where a loose file in
    the Packages/ folder of the data dir may be loaded instead of a file in
    the .sublime-package file.
    """

    def __init__(self, zippath):
        """
        :param zippath:
            A unicode string of the full filesystem path to the zip file
        """

        self.zippath = zippath
        self.name = os.path.splitext(os.path.basename(zippath))[0]
        self._scan_zip()

    def _get_name_key(self, fullname):
        """
        Converts a module name into a pair of package name and key. The
        key is used to access the various data structures in this object.

        :param fullname:
            A unicode string of a module name

        :return:
            If the fullname is not a module in this package, (None, None),
            otherwise a 2-element tuple of unicode strings. The first element
            being the package name, and the second being a sub-module, e.g.
            ("Default", "indentation").
        """

        if "." not in fullname:
            if fullname == self.name:
                return (self.name, "")
            return (None, None)

        name, key = fullname.split(".", 1)
        if name != self.name:
            return (None, None)
        return (self.name, key)

    def has(self, fullname):
        """
        Checks if the module is handled by this loader

        :param fullname:
            A unicode string of the module to check

        :return:
            A boolean if the module is handled by this loader
        """

        name, key = self._get_name_key(fullname)
        if name is None:
            return False

        # We can check this first before overrides since if this exists we
        # know at the very least it will be loaded from the zip
        if name == self.name and key in self.contents:
            return True

        rel_base = os.sep.join(fullname.split("."))
        override_file = os.path.join(override_path, rel_base + ".py")
        if os.path.isfile(override_file):
            return True

        # Here we check to see if an override dir exists, in general, even if
        # there is no __init__.py. We do this since we allow users to override
        # a sub-module without ensuring there is a perfect filesystem
        # heirarchy of __init__.py files when traversing upwards.
        override_package = os.path.join(override_path, rel_base)
        if os.path.isdir(override_package):
            return True

        return False

    def get_resource_reader(self, fullname):
        """
        :param fullname:
            A unicode string of the module name to get the resource reader for

        :return:
            None if the module is not a package, otherwise an object that
            implements the importlib.abc.ResourceReader() interface
        """

        if not self.is_package(fullname):
            return None
        return ZipResourceReader(self, fullname)

    def get_filename(self, fullname):
        """
        :param fullname:
            A unicode string of the module name

        :raises:
            ImportError - when the module has no file path

        :return:
            A unicode string of the file path to the module
        """

        info = self._spec_info(fullname)
        if info[0] is None:
            raise ImportError()
        return info[0]

    def get_code(self, fullname):
        """
        :param fullname:
            A unicode string of the module to get the code for

        :raises:
            ModuleNotFoundError - when the module is not part of this zip file
            ImportError - when there is an error loading the code

        :return:
            A code object for the module
        """

        info = self._spec_info(fullname)
        if info[0] is None:
            raise ModuleNotFoundError(f"No module named {repr(fullname)}")

        if not info[0].endswith(".pyc"):
            return importlib.abc.InspectLoader.source_to_code(
                self._load_source(fullname, info[0]), info[0]
            )

        _, key = self._get_name_key(fullname)
        data = self.contents[key]
        magic = data[0:4]
        if importlib.util.MAGIC_NUMBER != magic:
            raise ImportError(f"bad magic number in {repr(fullname)}: {repr(magic)}")
        # From importlib._bootstrap_external._code_to_timestamp_pyc()
        return marshal.loads(data[16:])

    def get_source(self, fullname):
        """
        :param fullname:
            A unicode string of the module to get the source for

        :raises:
            ModuleNotFoundError - when the module is not part of this zip file
            ImportError - when there is an error loading the source file

        :return:
            A unicode string of the source code, or None if there is no source
            for the module (i.e. a .pyc file)
        """

        info = self._spec_info(fullname)
        if info[0] is None:
            raise ModuleNotFoundError(f"No module named {repr(fullname)}")

        # If a sourceless file is loaded from the file, there is no source
        if info[0].endswith(".pyc"):
            return None

        return self._load_source(fullname, info[0])

    def _load_source(self, fullname, path):
        """
        Loads the source code to the module

        :param fullname:
            A unicode string of the module name

        :param path:
            A filesystem path to the module - may be a path into s
            .sublime-package file

        :return:
            A unicode string
        """

        if path == self.zippath or path.startswith(self.zippath + os.sep):
            _, key = self._get_name_key(fullname)
            if key in self.contents:
                return self.contents[key]
            raise ModuleNotFoundError(f"No module named {repr(fullname)}")

        if os.path.isdir(path):
            return ""

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except (Exception) as e:
            print(f"Error reading {path}: {e}")
            raise ImportError(f"Unable to load {repr(fullname)}")

    def is_package(self, fullname):
        """
        :param fullname:
            A unicode string of the module to see if it is a package

        :return:
            A boolean if the module is a package
        """

        info = self._spec_info(fullname)
        if info[1] is None:
            raise ModuleNotFoundError(f"No module named {repr(fullname)}")
        return info[1]

    def _spec_info(self, fullname):
        """
        :param fullname:
            A unicode string of the module that an
            importlib.machinery.ModuleSpec() object is going to be created for

        :return:
            A 2-element tuple of:
             - (None, None) if the loader does not know about the module
             - (unicode string, bool) of the origin and is_package params to
               pass to importlib.machinery.ModuleSpec()
        """

        rel_base = os.sep.join(fullname.split("."))
        name, key = self._get_name_key(fullname)
        if name is None:
            return (None, None)

        if key != "":
            rel_py_path = rel_base + ".py"
            override_py_file = os.path.join(override_path, rel_py_path)
            if os.path.isfile(override_py_file):
                return (override_py_file, False)

        in_zip = name == self.name and key in self.contents
        zip_filename = None if not in_zip else self.filenames[key]

        # We don't return files named __init__.py here to ensure that any
        # override that exists gets picked up instead.
        if in_zip and os.path.basename(zip_filename) != "__init__.py":
            return (os.path.join(self.zippath, zip_filename).rstrip(os.sep), key in self.packages)

        rel_init_path = rel_base + os.sep + "__init__.py"
        override_init_file = os.path.join(override_path, rel_init_path)
        if os.path.isfile(override_init_file):
            return (override_init_file, True)

        # This only handle __init__.py in the zip. It has to be placed after
        # the check for the override file.
        if in_zip:
            return (os.path.join(self.zippath, zip_filename), key in self.packages)

        # This is necessary to support overrides in a subdir of a package
        # when there is no __init__.py file in one of the parents
        override_dir = os.path.join(override_path, rel_base)
        if os.path.isdir(override_dir):
            return (override_dir, True)

        return (None, None)

    def _scan_zip(self):
        """
        Rebuild the internal cached info about the contents of the zip
        """

        self.contents = {"": ""}
        self.filenames = {"": ""}
        self.packages = {""}
        self.resources = {}
        self.refreshed = time.time()

        try:
            with zipfile.ZipFile(self.zippath, "r") as z:
                files = [i.filename for i in z.infolist()]

                for f in files:
                    base, ext = os.path.splitext(f)

                    if ext != ".py" and ext != ".pyc":
                        rmod, rname = os.path.split(f)
                        rmod = rmod.replace("/", ".").replace("\\", ".")
                        rmod = (self.name + "." + rmod).rstrip(".")
                        if rmod not in self.resources:
                            self.resources[rmod] = {}
                        self.resources[rmod][rname] = f
                        continue

                    paths = base.split("/")
                    if len(paths) > 0 and paths[len(paths) - 1] == "__init__":
                        paths.pop()
                        self.packages.add(".".join(paths))

                    pkg_path = ".".join(paths)
                    if f.endswith(".pyc"):
                        self.contents[pkg_path] = z.read(f)
                    else:
                        try:
                            self.contents[pkg_path] = z.read(f).decode("utf-8")
                        except UnicodeDecodeError:
                            print(
                                f"{os.path.join(self.zippath, f)} is not "
                                "utf-8 encoded, unable to load plugin"
                            )
                            continue
                    self.filenames[pkg_path] = f

                    while len(paths) > 1:
                        paths.pop()
                        parent = ".".join(paths)
                        if parent not in self.contents:
                            self.contents[parent] = ""
                            self.filenames[parent] = parent
                            self.packages.add(parent)
        except (Exception) as e:
            print(f"Error loading {self.zippath}: {e}")


override_path = None
multi_importer = MultizipImporter()
sys.meta_path.insert(0, multi_importer)


def update_compressed_packages(pkgs: Iterable[str]) -> None:
    ...


def set_override_path(path: str) -> None:
    ...
