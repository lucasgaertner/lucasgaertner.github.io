from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'polls/home.html')


def location(request):
    return render(request, 'polls/location.html')