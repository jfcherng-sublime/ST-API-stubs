#!/usr/bin/env bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

rename_file_exts_in_dir() {
    local dir="$1"
    local ext_from="$2"
    local ext_to="$3"

    find "${dir}" -type f -name "*.${ext_from}" -print0 | while IFS= read -r -d '' file; do
        mv -- "${file}" "${file%."${ext_from}"}.${ext_to}"
    done
}

ci_format() {
    local dir="$1"

    autoflake --in-place "${dir}"
    black "${dir}" --preview
    isort "${dir}" --profile black
}

ci_lint() {
    local dir="$1"

    flake8 "${dir}"
    black --check --diff "${dir}"
    isort --check --diff "${dir}"
}

ACTION=${1:-"format"}

pushd "${SCRIPT_DIR}/typings" || exit

# There seems to be no way to have "black" format .pyi file in a .py way...
# So I just rename .pyi files before formatting and rename them back after that.
rename_file_exts_in_dir . pyi py

case "${ACTION}" in
    format)
        ci_format .
        ;;
    lint)
        ci_lint .
        ;;
    *)
        echo "[ERROR] Unknown action: ${ACTION}"
        ;;
esac

rename_file_exts_in_dir . py pyi

popd || exit
