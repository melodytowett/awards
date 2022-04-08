import re
from django.shortcuts import redirect, render
from.models import Projects,Profile
from projects.forms import ProfileForm, ProjectForm

# Create your views here.

def index(request):
    projects = Projects.objects.all()
    projs = {'projects':projects}
    return render(request,'index.html',projs)

def my_projects(request):
    current_user = request.user
    if request.method == 'POST':
        post_form = ProjectForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        post_form = ProjectForm()
    return render(request,'all-projects/post-project.html',{"post_form":post_form})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile  = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('update_profile')
    else:
        profile_form = ProfileForm()
    return render(request,'all-projects/profile.html',{"profile_form":profile_form})
