# Django REST Framework Project Guide

This README provides a comprehensive step-by-step guide on how to create a Django REST Framework (DRF) project. It
covers essential topics like settings configuration, models, URLs, views, serializers, permissions, and authentication.

## Table of Contents

1. [Setting Up the Project](#setting-up-the-project)
2. [Configuring the Settings File](#configuring-the-settings-file)
3. [Creating and Using Models](#creating-and-using-models)
4. [Setting Up URLs](#setting-up-urls)
5. [Creating Views](#creating-views)
6. [Using Serializers](#using-serializers)
7. [Defining Permissions](#defining-permissions)
8. [Authentication and Permissions in Views](#authentication-and-permissions-in-views)

## Setting Up the Project

### 1. Create a Django Project

To start a new Django project, use the following command:

```bash
django-admin startproject myproject
cd myproject
```

### 2. Create a Django App

Inside your project, create a new app:

```bash
python manage.py startapp myapp
```

### 3. Install Django REST Framework

Install Django REST Framework and Simple JWT for authentication:

```bash
pip install djangorestframework djangorestframework-simplejwt
```

### 4. Project Structure

The project structure should look like this:

```markdown
myproject/
├── myproject/
│ ├── __init__.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
├── myapp/
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── permissions.py
│ ├── tests.py
│ └── migrations/
│ └── __init__.py
├── manage.py
└── requirements.txt
```

### 5. Add `rest_framework` to Installed Apps

Edit `myproject/settings.py` to include `rest_framework` and your app:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]
```

## Configuring the Settings File

### Database Configuration

Configure your database in `myproject/settings.py`. Here's an example for SQLite and PostgreSQL:

**SQLite:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**PostgreSQL:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### REST Framework Settings

Add settings for DRF in `myproject/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## Creating and Using Models

### What Are Models?

Models in Django define the structure of your database tables. They are Python classes that
subclass `django.db.models.Model`.

### Creating a Model

Define your models in `myapp/models.py`:

```python
from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def short_description(self):
        return self.description[:50]
```

### Making Migrations

After defining your models, create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Additional Model Properties

- **Fields:** Define the attributes of the model.
- **`__str__` Method:** Provides a human-readable representation of the model.
- **Properties:** Define methods that can be accessed like attributes.

```python
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def is_in_stock(self):
        return self.stock > 0

    @property
    def short_description(self):
        return self.description[:50]
```

## Setting Up URLs

### Creating a URL Configuration

Define your app-specific URLs in `myapp/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Including App URLs in Project URLs

Include your app's URLs in the project-level `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
```

## Creating Views

### What Are Views?

Views in Django handle the logic of your application and process requests to return responses.

### Types of Views in DRF

- **APIView:** Base class for all views.
- **ViewSet:** A set of views for CRUD operations.
- **ModelViewSet:** A ViewSet for handling models.
- **ObtainAuthToken:** Provides token authentication.

### Creating a ViewSet

Define a ViewSet in `myapp/views.py`:

```python
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

### Using ObtainAuthToken

Add ObtainAuthToken to your URLs for token authentication:

```python
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path

urlpatterns += [
    path('api-token-auth/', ObtainAuthToken.as_view()),
]
```

## Using Serializers

### What Are Serializers?

Serializers in DRF convert complex data types, such as querysets and model instances, into native Python datatypes and
vice versa.

### Creating a Serializer

Define a serializer in `myapp/serializers.py`:

```python
from rest_framework import serializers
from .models import MyModel


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'price', 'stock', 'is_in_stock']
        read_only_fields = ['created_at', 'updated_at', 'is_in_stock']
```

## Defining Permissions

### What Are Permissions?

Permissions in DRF control whether a user can access a particular view or perform a specific action.

### Creating Custom Permissions

Define custom permissions by subclassing `BasePermission` in `myapp/permissions.py`:

```python
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

### Applying Permissions to Views

Apply permissions in your ViewSet:

```python
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticated, IsOwner]
```

## Authentication and Permissions in Views

### Including Authentication and Permissions

Define authentication and permission classes in your ViewSet:

```python
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
```

### Configuring JWT Settings

Add JWT settings to your `myproject/settings.py`:

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
}
```

This detailed guide covers the foundational aspects of setting up a Django REST Framework project. Expand upon each
section as needed for your specific project requirements.