#!/bin/bash

# Example Django entrypoint
python manage.py migrate
gunicorn -b :8000 {{backend_name}}.wsgi:application
