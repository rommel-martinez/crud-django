from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['First_Name', 'Last_Name']
        widgets = {
            'First_Name' : forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'First Name'}),
            'Last_Name' : forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Last Name'})
        }