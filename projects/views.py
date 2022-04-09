
from django.shortcuts import redirect, render
from.models import Projects,Profile
from projects.forms import NewUserForm, ProfileForm, ProjectForm
import datetime as dt
from django .contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        messages.error(request,"registration Failed invalid credentials")
    form = NewUserForm()
    return render(request=request,template_name='registration/register.html',context={"register_form":form})

def login_user(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(index)
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"invalid uername or password")
    form = AuthenticationForm()
    return render(request=request,template_name="registration/login.html",context={"login_form":form})
# def date(request):
#     date=dt.date.today()
#     date = {"date":date}
#     return render(request,'index.html',date)
@login_required(login_url='login/')
def index(request):
    projects = Projects.objects.all()
    projs = {'projects':projects}
    return render(request,'index.html',projs)

@login_required(login_url='login/')
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

@login_required(login_url='login/')
def profile(request):
    profiles = Profile.objects.all()
    prof = {"profiles":profiles}
    return render(request,'all-projects/my-prof.html',prof)

@login_required(login_url='login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile  = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm()
    return render(request,'all-projects/profile.html',{"profile_form":profile_form})

@login_required(login_url='login/')
def search_project(request):
    if  request. method == 'GET':
        search_title = request.GET.get("project")
        projects_found = Projects.search_by_title(search_title).all()
        return render(request,"all-projects/search.html",{"projects":projects_found})
    else:
        message = "Found no result"
        return render(request,"all-projects/search.html",{"message":message})

def logout_user(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect('index')