# This code is defining the URL patterns for a Django application.
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# The `urlpatterns` variable is a list of URL patterns for a Django application. Each `path` function
# call represents a URL pattern and maps a URL to a specific view function or class-based view.
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]