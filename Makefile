SHELL=/bin/bash

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver 0.0.0.0:8000

collectstatic:
	python manage.py collectstatic --noinput

gunicorn:
	exec gunicorn postmail.wsgi:application --bind 0.0.0.0:8000 --workers=2 --threads=4

install:
	pip install -r requirements.txt
