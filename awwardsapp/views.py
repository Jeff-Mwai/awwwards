from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms import RegistrationForm, UserCreationForm, ProfileForm, projectForm
from .models import Profile, Projects
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework import status, viewsets, permissions 

# Create your views here.
def index(request):
    posts = Projects.objects.all()
    
    return render(request, 'index.html',{"posts":posts})
@login_required(login_url='login')  
def profile(request):

    return render(request, 'profile.html')


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=ProfileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()
            print(username)

            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=ProfileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'registration/registration.html', params)   


@login_required(login_url='login')   
def new_project(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = projectForm(request.POST,request.FILES)
        if form.is_valid:
            newProject = form.save(commit = False)
            newProject.user = user_profile
            newProject.save()
        return redirect('index')  
    else:
        form = projectForm()
    return render(request,'new_project.html',{'form':form})     

def posted_projects(request,id):
    posts = Projects.objects.get(id = id)
    # print(posts.title)
    
    return render(request, 'projects.html',{"posts":posts})
@login_required(login_url='login')  
def search_project(request):
    if 'project' in request.GET and request.GET['project']:
        name = request.GET.get("project")
        searchResults = Projects.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any project"
    return render(request, 'search.html', {'message': message})

class ProjectView(APIView):
    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProfileView(APIView):
     def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
