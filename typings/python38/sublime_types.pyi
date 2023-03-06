# This file is maintained on https://github.com/jfcherng-sublime/ST-API-stubs
# ST version: 4147

from __future__ import annotations

from typing import Any

from sublime import CompletionItem, KindId

DIP = float
Vector = tuple[DIP, DIP]
Point = int
Value = bool | str | int | float | list[Any] | dict[str, Any]
CommandArgs = dict[str, Value] | None
Kind = tuple[KindId, str, str]
Event = dict
CompletionValue = str | tuple[str, str] | CompletionItem
