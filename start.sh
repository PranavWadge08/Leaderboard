#!/bin/bash
# Collect static files
cd ctf
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py init_admin

# Start Daphne
daphne -p 8089 -b 0.0.0.0 ctf.asgi:application &

# Start Nginx (assuming it's configured to serve static files)
nginx -g "daemon off;"