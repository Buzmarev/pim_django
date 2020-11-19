#!/bin/bash
pip install --upgrade pip && pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
chown -R 1000:1000 ./
python manage.py runserver 0.0.0.0:8000