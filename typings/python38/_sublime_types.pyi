# This file is maintained on https://github.com/jfcherng-sublime/ST-API-stubs

from __future__ import annotations

from typing import Any, Iterable, Protocol, TypedDict

# ----- #
# types #
# ----- #


class Layout(TypedDict):
    cols: list[float]
    rows: list[float]
    cells: list[list[int]]


class EventDict(TypedDict):
    x: float
    y: float
    modifier_keys: EventModifierKeysDict


class EventModifierKeysDict(TypedDict, total=False):
    primary: bool
    ctrl: bool
    alt: bool
    altgr: bool
    shift: bool
    super: bool


class ExtractVariablesDict(TypedDict):
    file: str
    file_base_name: str
    file_extension: str
    file_name: str
    file_path: str
    folder: str
    packages: str
    platform: str
    project: str
    project_base_name: str
    project_extension: str
    project_name: str
    project_path: str


class ScopeStyleDict(TypedDict, total=False):
    foreground: str
    background: str
    bold: bool
    italic: bool
    glow: bool
    underline: bool
    stippled_underline: bool
    squiggly_underline: bool
    source_line: int
    source_column: int
    source_file: str


class CommandArgsDict(TypedDict):
    command: str
    args: None | dict[str, Any]


class HasKeysMethod(Protocol):
    def keys(self) -> Iterable[str]: ...
