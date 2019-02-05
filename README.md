## Overview
The patch aims at making sublime text API more accessible, easier and safer for usage by developpers

it does this by adding:
- docstrings describing the API
- type hints to enable static type checks

many sublime plugin developpers prefer to use static type checkers (e.g mypy) in their projects:
for many reasons including code safety and smart autocompletion so they have to create stubs for
_sublime.py_ and _sublime_plugin.py_, this patch avoids that.

Developpers would also appreciate not having to search the web every time they want
a function description, this patch makes it easy to do that using various plugins that
support function docstrings and signatures (e,g [LSP](https://packagecontrol.io/packages/LSP), [Anaconda](https://packagecontrol.io/packages/Anaconda))
