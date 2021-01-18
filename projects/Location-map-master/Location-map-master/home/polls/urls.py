from django.urls import path
from . import views

# Get necessary libs for preparing data
import os


urlpatterns = [
    path('', views.home, name='polls-home'),
]