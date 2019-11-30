from sublime import Edit, Html, Value, View, Window
from typing import Any, List, Optional, Tuple, Union


class CommandInputHandler:
    def name(self) -> str: ...
    def next_input(self, args: Dict[str, Any]) -> Optional[CommandInputHandler]: ...
    def placeholder(self) -> str: ...
    def initial_text(self) -> str: ...
    def preview(self, arg: Any) -> Union[str, Html]
    def validate(self, arg: Any) -> bool: ...
    def cancel(self) -> None: ...
    def confirm(self, arg) -> None:


class TextInputHandler(CommandInputHandler):
    def description(self, text: str) -> str: ...


class ListInputHandler(CommandInputHandler):
    def list_items(self) -> Union[List[str], List[Tuple[str, Value]]]: ...
    def description(self, v: Value, text: str) -> str: ...


class Command:
    def name(self) -> str: ...
    def is_enabled(self) -> bool: ...
    def is_visible(self) -> bool: ...
    def is_checked(self) -> bool: ...
    def description(self) -> str: ...
    def want_event(self) -> bool: ...
    def input(self, args: Dict[str, Any]) -> Optional[CommandInputHandler]: ...
    def input_description(self) -> str: ...


class ApplicationCommand(Command):
    def run(self) -> None: ...


class WindowCommand(Command):
    window: Window

    def __init__(self, window: Window) -> None: ...
    def run(self) -> None: ...


class TextCommand(Command):
    view: View

    def __init__(self, view: View) -> None: ...
    def run(self, edit: Edit) -> None: ...


class EventListener:
    ...


class ViewEventListener:
    view: View

    def __init__(self, view: View) -> None: ...
    @classmethod
    def is_applicable(cls, settings: Dict[str, Any]) -> bool: ...
    @classmethod
    def applies_to_primary_view_only(cls) -> bool: ...
