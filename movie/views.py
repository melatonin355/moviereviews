from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requests):
    return render(requests, 'home.html', {'name': 'Bob'})

def about(requests):
    return HttpResponse('<h1>Welcome to the about page </h1>')