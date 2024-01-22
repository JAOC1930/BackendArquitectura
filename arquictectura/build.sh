#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r arquictectura/requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
