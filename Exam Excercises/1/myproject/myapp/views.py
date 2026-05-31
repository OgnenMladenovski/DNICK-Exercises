from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {"events" : events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            band_input = request.POST.get('bands', '')
            band_names = [b.strip() for b in band_input.split(',') if b.strip()]

            for band_name in band_names:
                band = Band.objects.get(name=band_name)
                BandEvent.objects.create(event=event, band=band)

            return redirect('index')

    form = EventForm()
    return render(request, 'add_event.html', {'form' : form})