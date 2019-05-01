release: python manage.py migrate

web: gunicorn cozzez_site_1.wsgi —-log-file -

worker: celery -A cozzez_site_1 worker --beat -S django

beat: celery -A cozzez_site_1 beat -S django

