#!/bin/bash

# Usage :
# e.g run everyday at 4AM and 6PM : crontab -e
#   MAILTO = "sharp.imsystem@gmail.com"
#   0 4,18 * * * <PROJ_ROOT_DIR>/scripts/run_backup.sh > /tmp/sharp_backup.log


set -e


# TO CONFIGURE - set absolute path to project
PROJ_ROOT_DIR="$(pwd)"
VENV_ACTIVATE="${PROJ_ROOT_DIR}/venv/bin/activate"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"
RCLONE="/usr/bin/rclone"
LOCAL_BACKUP_DIR="/tmp/testdbbackup/"
REMOTE_BACKUP_DIR="drive:sharp_backup"


function assert_installed {
  if ! [ -x "$(command -v "$1")" ]; then
    echo "Error: $1 not found" >&2
    exit 1
  fi
}


function log {
  echo "[*] $(date) - $1"
}

assert_installed "${RCLONE}"

echo '================================================'
log "Starting local backup"

source "$VENV_ACTIVATE"
python3 "${MANAGE_SCRIPT}" dbbackup --clean --compress
python3 "${MANAGE_SCRIPT}" mediabackup --clean --compress
deactivate

log "Starting remote syncing"
"${RCLONE}" sync --verbose --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 "${LOCAL_BACKUP_DIR}" "${REMOTE_BACKUP_DIR}"

log "Backup completed"
