from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    # django auth urls
    path('', include('django.contrib.auth.urls')),
    # registration
    path('register/', views.register, name='register'),
    # profile
    path('edit/', views.edit, name='edit'),
]
