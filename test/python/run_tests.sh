#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DISPATCH_DIR="${ROOT_DIR}/dispatch"

if ! command -v python3 >/dev/null 2>&1; then
    echo "error: python3 not found" >&2
    exit 1
fi

if ! python3 -c "import antlr4" >/dev/null 2>&1; then
    echo "Installing antlr4-python3-runtime..."
    python3 -m pip install antlr4-python3-runtime
fi

export PYTHONPATH="${DISPATCH_DIR}:${PYTHONPATH:-}"

cd "${SCRIPT_DIR}"
python3 -m unittest discover -s "${SCRIPT_DIR}" -p "test_*.py" -v

echo "Python tests passed."
