#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# There seems to be no way to have "black" format .pyi file in a .py way...
# So I just rename .pyi files before formatting and rename them back after that.

pushd "${SCRIPT_DIR}" || exit

mv "sublime.pyi" "sublime.py"
mv "sublime_plugin.pyi" "sublime_plugin.py"

black .

mv "sublime.py" "sublime.pyi"
mv "sublime_plugin.py" "sublime_plugin.pyi"

popd || exit
