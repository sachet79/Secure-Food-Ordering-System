web: gunicorn Foods_Ordering.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate