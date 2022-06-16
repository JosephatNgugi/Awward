from django import forms
from .models import *

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'date_added']
        widgets = {'description': forms.Textarea(attrs={'rows':4, 'cols':7,}),
        }