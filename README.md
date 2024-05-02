# fshn_master_django

FSHN Master Django Course

# Database links

- https://youtu.be/ABwD8IYByfk
- https://youtu.be/ztHopE5Wnpc
- https://www.guru99.com/database-design.html

# Commands

- Create new env
    - python -m venv ~/env
- Start virtual env
    - source ~/env/bin/activate
- install requirements
    - create requirements.txt file
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

# Links

## Django 1

- https://docs.djangoproject.com/en/1.11/topics/db/models/
- https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user
- https://docs.djangoproject.com/en/1.11/ref/models/fields/
- https://peps.python.org/pep-0008/
- https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-AUTH_USER_MODEL
- https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
- https://docs.djangoproject.com/en/2.2/ref/models/options/#verbose-name

## Django 2

- https://www.django-rest-framework.org/api-guide/views/
- https://docs.djangoproject.com/en/1.11/topics/http/urls/
- https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include
- https://www.django-rest-framework.org/api-guide/fields/
- https://www.django-rest-framework.org/api-guide/status-codes/
- https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

## Django 3

- https://www.django-rest-framework.org/api-guide/permissions/
- Token <AUTH_TOKEN_OBTAINED_FROM_LOGIN>

# Create Project

- Github
    - create project
    - clone project on pc
- Commands 1-6
- profile_project ->
    - settings.py (INSTALLED_APPS)
    - urls.py (path('api/', include('profiles_api.urls')))
- profiles_api ->
    - models.py (each class(Models.model) is a table)
    - views.py (ModelViewSet (endpoints) <-> serializer)
    - serializer.py (validation json)
    - urls.py (endpoints map)
    - permissions (user and models rights)
    - admin (register models for admin panel)
