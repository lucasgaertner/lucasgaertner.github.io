from django.urls import path
from . import views

# Get necessary libs for preparing data
import os
import pandas as pd

urlpatterns = [
    path('', views.home, name='polls-home'),
]



# print(os.getcwd())
file = pd.read_csv('countries.csv', 'r', encoding="utf-8", delimiter="\t")

countries = []
for countrie in file['name']:
    print("path('/" + str(countrie) + "' " + "views.location ),")
    urlpatterns.append(path(str(countrie), views.location ),)