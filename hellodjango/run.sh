#!/bin/bash

set -e

VENV="/opt/venv-hellodjango"

# Create database if missing
if [ ! -f /data/db.sqlite3 ]; then
    $VENV/bin/python manage.py makemigrations
    $VENV/bin/python manage.py migrate
fi

# Launch WSGI app with multiple Gunicorn workers
$VENV/bin/gunicorn -w4 -b 0.0.0.0:8000 hellodjango.wsgi:application
