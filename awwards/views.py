from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    projects = Project.all_projects()
    return render(request, 'awwards/homepage.html', {"projects":projects})

def UserRegistration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            InputPassword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=InputPassword)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def add_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.author = current_user
            form.save()
        return redirect('home')

    else:
        form = AddProjectForm()
    return render(request, 'awwards/add-project.html', {"form":form})
