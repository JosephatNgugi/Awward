from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 

        
class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'link', 'screenshot', 'description')
        widgets = {'description': forms.Textarea(attrs={'rows':4, 'cols':7,}),
        }
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review','design','usability','content']
