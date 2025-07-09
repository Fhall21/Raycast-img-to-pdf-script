#!/bin/bash
# @raycast.schemaVersion 1
# @raycast.title Images to PDF
# @raycast.packageName Utilities
# @raycast.mode fullOutput
# @raycast.icon 📄
# @raycast.description Convert images in a folder or a single image file to a PDF using Python and Pillow. If no arguments are provided, a GUI will prompt for selection.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/img_to_pdf_cli.py"
VENV_DIR="$SCRIPT_DIR/venv"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"

# Create venv if not present
if [ ! -d "$VENV_DIR" ]; then
  echo "[Raycast] Creating Python virtual environment..."
  if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required. Please install it." >&2
    exit 1
  fi
  python3 -m venv "$VENV_DIR"
  if [ $? -ne 0 ]; then
    echo "Failed to create virtualenv." >&2
    exit 1
  fi
  echo "[Raycast] Installing requirements..."
  "$VENV_DIR/bin/pip" install --upgrade pip >/dev/null 2>&1
  "$VENV_DIR/bin/pip" install -r "$REQUIREMENTS"
  if [ $? -ne 0 ]; then
    echo "Failed to install requirements." >&2
    exit 1
  fi
fi

PYTHON="$VENV_DIR/bin/python"

# If arguments are provided, pass them to the Python script. Otherwise, let Python handle all GUI selection.
if [ -n "$1" ] && [ -n "$2" ]; then
  "$PYTHON" "$PYTHON_SCRIPT" "$1" "$2"
else
  "$PYTHON" "$PYTHON_SCRIPT"
fi
