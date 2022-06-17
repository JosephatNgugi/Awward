from django.shortcuts import get_object_or_404, render, redirect
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

def profile(request,id):
    profile = Profile.objects.get(user = id)
    return render(request, 'user/profile.html', {"profile":profile})

@login_required(login_url='login')
def edit_profile(request):
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/edit-profile.html', {'user_form': user_form, 'prof_form':prof_form})


@login_required(login_url='/accounts/login/')
def add_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newProject = form.save(commit=False)
            newProject.user = current_user
            newProject.save()
        return redirect('home')

    else:
        form = AddProjectForm()
    return render(request, 'awwards/add-project.html', {"form":form})

def projects(request,id):
    projects = Project.objects.get(id = id)
    return render(request,'awwards/project-details.html',{"projects":projects})

@login_required(login_url='login')   
def ratings(request,id):
    project = Project.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = RatingForm()
    return render(request,"awwards/project-rating.html",{"form":form,"project":project})        
