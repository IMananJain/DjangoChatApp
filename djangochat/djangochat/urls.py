# This code is defining the URL patterns for a Django project.
from django.contrib import admin
from django.urls import path, include

# The `urlpatterns` variable is a list of URL patterns for a Django project. Each `path` function call
# specifies a URL pattern and the corresponding view or URL configuration to be used.
urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
]
