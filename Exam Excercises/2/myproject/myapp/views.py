from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def index(request):
    tours = Tour.objects.all()
    return render(request, 'index.html', {'tours' : tours})

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.tour_guide = request.user.tourguide

            tour.clean()
            tour.save()
            return redirect('index')
    form = TourForm()
    return render(request, 'add_tour.html', {"form" : form})