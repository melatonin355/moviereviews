from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(requests):
    searchTerm = requests.GET.get("searchMovie")
    movies = Movie.objects.all()
    return render(requests, "home.html", {"searchTerm": searchTerm, "movies": movies})


def about(requests):
    return HttpResponse("<h1>Welcome to the about page </h1>")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})
