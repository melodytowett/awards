
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import projects
from.models import Projects,Profile, Rating,User
from projects.forms import NewUserForm, ProfileForm, ProjectForm, RatingForm
import datetime as dt
from django .contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .serializer import ProfileSerializer,ProjectsSerializer
from projects import serializer
from .permission import IsAdminOrReadOnly
from projects import permission
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

@login_required(login_url='login/')
def index(request):
    projects = Projects.objects.all()
    profiles = Profile.objects.all()
    profs = {"profiles":profiles}
    projs = {'projects':projects}
    return render(request,'index.html',projs)

@login_required(login_url='login/')
def project_rating(request,project):
    project = Projects.objects.get(title=project)
    ratings = Rating.objects.filter(user=request.user, project=project).first()
    rating_status = None
    current_user=request.user
    if request.method == "POST":
        project_form = ProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()
            # return redirect("index")
            return HttpResponseRedirect(reverse("index"))
    else:
        project_form = ProjectForm()
    
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate_result = form.save(commit=False)
            rate_result.user = request.user
            rate_result.project = project
            rate_result.save()
            project_ratings = Rating.objects.filter(project=project)

            design_rate = [d.design for d in project_ratings]
            design_avg = sum(design_rate) / len(design_rate)

            usability_rate = [us.usability for us in project_ratings]
            usability_avg = sum(usability_rate) / len(usability_rate)

            content_rate = [content.content for content in project_ratings]
            content_avg = sum(content_rate) / len(content_rate)

            creativity_rate = [create.creativity for create in project_ratings]
            creativity_avg = sum(creativity_rate)/len(creativity_rate)

            score = (design_avg + usability_avg + content_avg + creativity_avg)/4

            print(score)
            rate_result.design_average = round(design_avg, 2)
            rate_result.usability_average = round(usability_avg, 2)
            rate_result.content_average = round(content_avg, 2)
            rate_result.creativity_average = round(creativity_avg,2)
            rate_result.score = round(score, 2)
            rate_result.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingForm()
    return render(request, 'all-projects/project.html', {'project': project,'rating_form': form,'rating_status': rating_status,'current_user':current_user,'project_form':project_form})

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
def update_profile(request,username):
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
    user_prof = get_object_or_404(User,username=username)
    if request.user == user_prof:
        return redirect('profile',username=request.user.username)
    user_profs = user_prof.projects.all()
    return render(request,'all-projects/profile.html',{"profile_form":profile_form,"user_prof":user_prof,"userprofs":user_profs})

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

class ProjViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all().order_by('id')
    serializer_class = ProjectsSerializer
  
class ProfViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
