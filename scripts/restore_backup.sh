#!/bin/bash

# Restores the latest backup
# to restore a specific file run the command manually and c.f -i

set -e


# TO CONFIGURE - set absolute path to project
PROJ_ROOT_DIR="$(pwd)"
VENV_ACTIVATE="${PROJ_ROOT_DIR}/venv/bin/activate"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"


function usage {
  echo "Usage: $0 <passphrase>"
}


function log {
  echo "[*] $(date) - $1"
}


echo -n 'Password: '
read -s PASSPHRASE
echo

source "$VENV_ACTIVATE"

python3 "${MANAGE_SCRIPT}" dbrestore --decrypt --passphrase "${PASSPHRASE}" -v3
python3 "${MANAGE_SCRIPT}" mediarestore --uncompress --decrypt --passphrase "${PASSPHRASE}" -v3

deactivate


echo "Done"