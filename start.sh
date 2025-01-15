# Run the Django application
python manage.py makemigrations --no-input
python manage.py collectstatic --noinput
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8000