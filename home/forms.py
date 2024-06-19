from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientDetailsForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','phone_number','address','email','username', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use")
        return email
    


class ClientLoginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
