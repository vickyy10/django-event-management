from django import forms
from .models import Events

class evetsForm(forms.models):

    model = Events
    field = '__all__'

    