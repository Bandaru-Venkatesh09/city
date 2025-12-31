!/bin/bash python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn mini_project.wsgi:application --bind 0.0.0.0:$PORT 