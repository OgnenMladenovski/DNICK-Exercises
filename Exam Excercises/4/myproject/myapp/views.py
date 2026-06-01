from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'index.html', {'exhibitions' : exhibitions})

def add_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            exhibition = form.save(commit=False)
            exhibition.user = request.user

            exhibition.save()
            return redirect('index')
    form = ExhibitionForm()
    return render(request, 'add_exhibition.html', {'form' : form})
