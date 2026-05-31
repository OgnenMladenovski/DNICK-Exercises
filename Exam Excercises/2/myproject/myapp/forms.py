from django import forms
from .models import *

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ["destination", 'price', 'duration', 'image']