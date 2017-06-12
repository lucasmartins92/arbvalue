web: gunicorn arbvalue.wsgi --log-file
worker: celery -A tasks worker -B --loglevel=info