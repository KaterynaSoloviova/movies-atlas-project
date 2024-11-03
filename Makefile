run:
	python manage.py runserver

migrate:
	python manage.py migrate movies

migrations:
	python manage.py makemigrations

format:
	flake8 movies/

black:
	black movies/

