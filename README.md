# ikub_11_2022
Akademia IKUB kursi Python Nëntor 2022 - Shkurt 2022

# Commands
- Create new env
  - python -m venv ~/env
- Start virtual env
  - source ~/env/bin/activate
- install requirements
  - pip install -r requirements.txt
- new django project
  - django-admin startproject profiles_project .
- new django application
  - python manage.py startapp profiles_api
- run python server
  - python manage.py runserver localhost:8000
- create migration
  - python manage.py makemigrations profiles_api
- make migration
  - python manage.py migrate
- create superuser
  - python manage.py createsuperuser
