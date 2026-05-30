from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "index.html", {"movies" : movies})

def movie_details(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "detail.html", {"movie" : movie})