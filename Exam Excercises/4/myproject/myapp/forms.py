from django import forms
from .models import *

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'date_start', 'date_end', 'location', 'description']