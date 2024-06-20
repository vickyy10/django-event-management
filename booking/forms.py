from django import forms

from .models import bookingDetails

class bookingDetailsForm(forms.ModelForm):
    
    class Meta:
        model = bookingDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['event_type'].empty_label = 'Select'