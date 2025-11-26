#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate --noinput

# Cargar datos iniciales
python manage.py loaddata datos_utf8.json || true
python manage.py loaddata admin_render.json || true

# Collect static files
python manage.py collectstatic --no-input