#!/bin/bash

# Usage :
# e.g run everyday at 4AM and 6PM : crontab -e
#   MAILTO = "sharp.imsystem@gmail.com"
#   0 4,18 * * * <PROJ_ROOT>/scripts/run_backup.sh > /tmp/sharp_backup.log

set -e

# set absolute path to project
PROJ_ROOT_DIR="$(pwd)"
VENV_ACTIVATE="${PROJ_ROOT_DIR}/venv/bin/activate"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"

echo '================================================'
echo "$(date) - Starting backup"

source "$VENV_ACTIVATE"
python3 "${MANAGE_SCRIPT}" dbbackup --clean --compress
python3 "${MANAGE_SCRIPT}" mediabackup --clean --compress
deactivate

echo "$(date) - Backup completed"
