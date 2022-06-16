from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    projects = Project.all_projects()
    return render(request, 'awwards/homepage.html', {"projects":projects})
