import os
import sys

import django
import gnupg
from django.conf import settings

confirm = input('Are you sure you want to generate new PGP keys ? This might override old keys (yes) : ')
if confirm.strip() != "yes":
    print('Aborting')
    exit(0)

# TOCONFIGURE - set absolute path to project
PROJ_ROOT_DIR = "."
if PROJ_ROOT_DIR not in sys.path:
    sys.path.append(PROJ_ROOT_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IMS.settings')
django.setup()

# dummy
NAME = settings.ADMINS[0][0]
EMAIL = settings.ADMINS[0][1]
PASSPHRASE = settings.DBBACKUP_GPG_PASSPHRASE


gpg = gnupg.GPG()

input_data = gpg.gen_key_input(
    key_type="RSA",
    key_length=2048,
    name_real=NAME,
    name_email=EMAIL,
    passphrase=PASSPHRASE
)
print(input_data)
key = gpg.gen_key(input_data)

# ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
# ascii_armored_private_keys = gpg.export_keys(
#     keyids=key.fingerprint,
#     secret=True,
#     passphrase=PASSPHRASE,
# )
#
# print(ascii_armored_public_keys)
# print(ascii_armored_private_keys)