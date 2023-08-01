# This code is importing the `admin` module from the `django.contrib` package and the `Room` model
# from the current directory's `models` module.
from django.contrib import admin

from .models import Room

admin.site.register(Room)