#!/bin/bash

# Example Django entrypoint
python manage.py migrate
gunicorn -b :8000 {{name}}server.wsgi:application
