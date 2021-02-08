#!/bin/bash

# Restores the latest backup
# to restore a specific file run the command manually and c.f -i

set -e


# TOCONFIGURE - set absolute path to project
PROJ_ROOT_DIR="/app/web"
MANAGE_SCRIPT="${PROJ_ROOT_DIR}/manage.py"


function usage {
  echo "Usage: $0 <passphrase>"
}

function log {
  echo "[*] $(date) - $1"
}


echo -n 'PGP passphrase: '
read -s PASSPHRASE
echo

python3 "${MANAGE_SCRIPT}" dbrestore --decrypt --passphrase "${PASSPHRASE}" -v3
python3 "${MANAGE_SCRIPT}" mediarestore --uncompress --decrypt --passphrase "${PASSPHRASE}" -v3

echo "Done"