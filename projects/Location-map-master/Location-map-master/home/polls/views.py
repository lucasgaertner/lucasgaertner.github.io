from django.shortcuts import render

# Create your views here.
import pandas as pd

def home(request):
    

    person= {'firstname': 'Craig', 'lastname': 'Daniels'}
    weather= "sunny"
    context= {
        'person': person,
        'weather': weather,
        }

    return render(request, 'polls/home.html', context)