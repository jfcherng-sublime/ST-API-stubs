#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# There seems to be no way to have "black" format .pyi file in a .py way...
# So I just rename .pyi files before formatting and rename them back after that.

pushd "${SCRIPT_DIR}/typings" || exit

# rename *.pyi to *.py
for f in *.pyi; do
    mv -- "$f" "${f%.pyi}.py"
done

black . --preview
isort . --profile black

# rename *.py to *.pyi
for f in *.py; do
    mv -- "$f" "${f%.py}.pyi"
done

popd || exit
