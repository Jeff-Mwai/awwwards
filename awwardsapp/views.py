from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .forms import RegistrationForm, UserCreationForm, ProfileForm, projectForm
from .models import Profile, Projects, Rate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Projects.objects.all()
    
    return render(request, 'index.html',{"posts":posts})


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

            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=ProfileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'registration/registration_form.html', params)   

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

def posted_projects(request):
    posts = Projects.objects.all()
    
    return render(request, 'projects.html',{"posts":posts})

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

@login_required(login_url='login')   
def ratings(request,id):
    ratings = Rate.objects.get(projects_id = id).all()
    project = Projects.objects.get(id = id)
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.projects = project
            rate.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request,"reviews.html",{"form":form,"project":project, "ratings": ratings})  