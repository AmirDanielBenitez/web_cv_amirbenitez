#!/bin/sh

self.stdout.write('Waiting for database...')
db_conn = False

while not db_conn:
    try:
        c = connection.cursor()
        c.execute('SELECT 1')
        db_conn = True
    except OperationalError:
        self.stdout.write('Database unavailable, waiting 1 second...')
        sleep(1)

self.stdout.write(self.style.SUCCESS('Database available!'))

echo 'Running collecstatic...'
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo 'Applying migrations...'
python manage.py migrate

echo 'Running server...'
exec gunicorn --bind 0.0.0.0:$PORT web_cv_amirbenitez.wsgi:application