#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./setup_venv.sh            - create .venv in repository root and install requirements.txt
#   ./setup_venv.sh myenv      - create myenv directory and install requirements.txt
#   ./setup_venv.sh --help

ARG=${1:-}
if [[ "$ARG" == "--help" || "$ARG" == "-h" ]]; then
  cat <<'EOF'
setup_venv.sh

Creates a Python virtual environment and installs dependencies from requirements.txt.

Usage:
  ./setup_venv.sh [env_dir]

Defaults:
  env_dir=.venv

Example:
  ./setup_venv.sh .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
EOF
  exit 0
fi

ENV_DIR=${ARG:-.venv}
REQ_FILE=requirements.txt

if [[ ! -f "$REQ_FILE" ]]; then
  echo "ERROR: requirements file not found: $REQ_FILE" >&2
  exit 2
fi

PYTHON_CMD=python3.14
if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
  PYTHON_CMD=python
fi

if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
  echo "ERROR: Python not found (python3 or python)." >&2
  exit 3
fi

# venv module check
if ! "$PYTHON_CMD" -m venv --help >/dev/null 2>&1; then
  echo "ERROR: The Python installation does not support venv." >&2
  exit 4
fi

# Create virtual environment
if [[ -d "$ENV_DIR" ]]; then
  echo "Using existing virtual environment: $ENV_DIR"
else
  echo "Creating virtual environment at: $ENV_DIR"
  "$PYTHON_CMD" -m venv "$ENV_DIR"
fi

# Activate environment for this script (for pip)
source "$ENV_DIR/bin/activate"

# Upgrade pip, wheel, setuptools
python -m pip install --upgrade pip setuptools wheel
# Install dependencies
python -m pip install -r "$REQ_FILE"

cat <<EOF
✅ Virtual environment ready: $ENV_DIR
✅ Dependencies installed from $REQ_FILE

Next steps:
  source "$ENV_DIR/bin/activate"
  python your_script.py
EOF
