#!/bin/bash

# Apply migrations if not already done. Commented out in this example because the entrypoint 
# if [ ! -f "/code/.migrations_complete" ]; then
#     echo "Applying migrations..."
#     python manage.py migrate
#     touch /code/.migrations_complete # Mark migrations as complete
# fi


# Start Gunicorn (or your preferred production server)
gunicorn learn_docker.wsgi:application --bind 0.0.0.0:8000  # replace learn_docker with your django project name

# Or if you want to use runserver for development then uncomment below line
# poetry run ./manage.py runserver 0.0.0.0:8000  # Make sure 0.0.0.0 is used for Docker

exec "$@"
