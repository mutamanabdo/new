from django import forms
from .models import client

class AddClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ('name','email','description')