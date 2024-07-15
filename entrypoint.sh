#!/bin/sh

echo "Waiting for DB..."
while ! nc -z db 5432; do
  sleep 1
done
echo "DB ready"

echo 'Running collecstatic...'
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo 'Applying migrations...'
echo "Aplicando migraciones..."
python manage.py migrate

echo 'Running server...'
exec gunicorn --bind 0.0.0.0:$PORT web_cv_amirbenitez.wsgi:application