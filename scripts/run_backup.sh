#!/bin/bash

set -e

# set absolute path to project
DJ_ROOT_DIR="$(pwd)"
VENV_ACTIVATE="$DJ_ROOT_DIR/venv/bin/activate"

line="================================================"

echo "$line"
echo "$(date) - Starting backup"

source "$VENV_ACTIVATE"
python3 "$DJ_ROOT_DIR/manage.py" dbbackup --clean --compress
python3 "$DJ_ROOT_DIR/manage.py" mediabackup --clean --compress
deactivate

echo "$(date) - Backup completed"
