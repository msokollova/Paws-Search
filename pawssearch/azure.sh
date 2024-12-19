#!/bin/sh

# Enter the main directory or exit if it fails
cd pawssearch || { echo "Failed to enter pawssearch directory"; exit 1; }

# Install requirements
pip install -r requirements.txt

# Makemigrations
python manage.py makemigrations

# Migrate all tables
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

# Start the gunicorn server
gunicorn --bind=0.0.0.0 pawssearch.wsgi || { echo "Failed to start gunicorn"; exit 1; }
