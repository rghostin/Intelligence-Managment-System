#!/bin/bash

# Usage :
# * A PGP key should be set up for encryption: c.f script gen_pgp_key.py
# * A cron job should be set up:
#   e.g run everyday at 4AM and 6PM : crontab -e
#     MAILTO = "sharp.imsystem@gmail.com"
#     0 4,18 * * * <PROJ_ROOT_DIR>/scripts/run_backup.sh -r -- > /tmp/sharp_backup.log


set -e


# TO CONFIGURE - set absolute path to project
PROJ_ROOT_DIR="$(pwd)"
VENV_ACTIVATE="${PROJ_ROOT_DIR}/venv/bin/activate"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"
RCLONE="/usr/bin/rclone"
LOCAL_BACKUP_DIR="/tmp/testdbbackup/"
REMOTE_DRIVE="drive"
REMOTE_BACKUP_DIR="${REMOTE_DRIVE}:sharp_backup"


function usage {
  echo "Usage: $0 [-r : enable remote syncing ]"
}


function log {
  echo "[*] $(date) - $1"
}


REMOTE='false'
while getopts ":r" o; do
    case "${o}" in
        r)
            REMOTE='true'
            ;;
        '?')
            echo "INVALID OPTION -- ${OPTARG}" >&2
            usage
            exit 1
            ;;
        ':')
            echo "MISSING ARGUMENT for option -- ${OPTARG}" >&2
            usage
            exit 1
            ;;
        *)
            echo "UNIMPLEMENTED OPTION -- ${OPTKEY}" >&2
            usage
            exit 1
            ;;
    esac
done

shift $(( OPTIND - 1 ))
[[ "${1}" == "--" ]] && shift

if ${REMOTE}; then
  # test config
  "${RCLONE}" config show --quiet "${REMOTE_DRIVE}"
fi

echo '================================================'
log "Starting local backup"

source "$VENV_ACTIVATE"
python3 "${MANAGE_SCRIPT}" dbbackup --clean --compress --encrypt
python3 "${MANAGE_SCRIPT}" mediabackup --clean --compress --encrypt
deactivate


if ${REMOTE}; then
  log "Starting remote syncing"
  "${RCLONE}" sync --verbose --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 "${LOCAL_BACKUP_DIR}" "${REMOTE_BACKUP_DIR}"
else
  log "Remote syncing disabled"
fi

log "Backup completed"
