#!/bin/bash

# Apply migrations if not already done. Commented out in this example because the entrypoint 
if [ ! -f "/code/.migrations_complete" ]; then
    echo "Applying migrations..."
    python manage.py migrate
    touch /code/.migrations_complete # Mark migrations as complete
fi


# Start Gunicorn (or your preferred production server)
gunicorn learn_docker.wsgi:application --bind 0.0.0.0:8000  

# Excute command
exec "$@"
