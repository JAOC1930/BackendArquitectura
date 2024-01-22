#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r arquictectura/requirements.txt

python arquictectura/manage.py collectstatic --noinput
python arquictectura/manage.py migrate
