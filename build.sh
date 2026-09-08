#!/usr/bin/env bash

set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate

if [ -f backup.json ]; then
    python manage.py loaddata backup.json
fi