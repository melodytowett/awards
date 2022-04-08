import re
from django.shortcuts import redirect, render

from projects.forms import ProjectForm

# Create your views here.

def index(request):
    return render(request,'index.html')

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
