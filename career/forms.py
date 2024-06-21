from django import forms
from .models import careermodel
    



class careermodelform(forms.ModelForm):
    class Meta:
        model= careermodel
        fields='__all__'
