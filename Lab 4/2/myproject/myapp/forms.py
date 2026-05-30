from django import forms
from .models import *

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title', 'trainer', 'category', 'level', 'duration', 'capacity', 'price']