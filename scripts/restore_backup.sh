#!/bin/bash

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


if [[ "$#" -ne 1 ]]; then
    usage
    exit 1
fi

PASSPHRASE="$1"

source "$VENV_ACTIVATE"

python3 "${MANAGE_SCRIPT}" dbrestore --decrypt --passphrase "${PASSPHRASE}" -v3
python3 "${MANAGE_SCRIPT}" mediarestore --uncompress --decrypt --passphrase "${PASSPHRASE}" -v3

deactivate


