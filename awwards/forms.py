from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'date_added']
        widgets = {'description': forms.Textarea(attrs={'rows':4, 'cols':7,}),
        }