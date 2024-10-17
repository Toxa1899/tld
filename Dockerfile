FROM python:3.11-slim

WORKDIR /app

COPY . /app/
COPY .env /app/.env.docker

RUN pip install -r requirements.txt --verbose


RUN python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input


CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "info"]
