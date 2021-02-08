#!/bin/bash

# Usage :
# * A PGP key should be set up for encryption: c.f script gen_pgp_key.py
# * A cron job should be set up:
#   e.g run everyday at 4AM and 6PM : crontab -e
#     MAILTO = "sharp.imsystem@gmail.com"
#     0 4,18 * * * <PROJ_ROOT_DIR>/scripts/run_backup.sh -r -- > /tmp/sharp_backup.log


set -e


# TOCONFIGURE - set absolute path to project
PROJ_ROOT_DIR="/home/black/WS/IMS/IMScore"
# TOCONFIGURE - set absolute path to backups
LOCAL_BACKUP_DIR="/var/backups/web"
# TOCONFIGURE * set absolute path log file
LOG_FILE="/var/log/web/backup.log"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"
RCLONE="/usr/bin/rclone"
REMOTE_DRIVE="drive"
REMOTE_BACKUP_DIR="${REMOTE_DRIVE}:web_backup"


function usage {
  echo "Usage: $0 [-r : enable remote syncing ]"
}


function log {
  echo "[*] $(date) - $1" | tee -a "${LOG_FILE}"
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
  "${RCLONE}" config show --quiet "${REMOTE_DRIVE}" > /dev/null
fi

log "Starting local backup ==========================="

# no compression of db because of some bug in the module
python3 "${MANAGE_SCRIPT}" dbbackup --clean --encrypt
python3 "${MANAGE_SCRIPT}" mediabackup --clean --compress --encrypt

if ${REMOTE}; then
  log "Starting remote syncing"
  "${RCLONE}" sync --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 "${LOCAL_BACKUP_DIR}" "${REMOTE_BACKUP_DIR}"
  if [ $? -eq 0 ]; then
      log "Cloud syncing: OK"
  else
      log "Cloud syncing: FAIL"
  fi
else
  log "Remote syncing disabled"
fi

log "Backup completed"
