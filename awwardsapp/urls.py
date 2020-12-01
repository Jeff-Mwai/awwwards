from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('',views.index, name = 'index'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('new_project/',views.new_project, name='new_project'),
    path('projects/<id>/',views.posted_projects, name='posted_projects'),
    path('search_project/',views.search_project, name='search_project'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('profile/',views.profile, name='profile'),
    path('api/projects/', views.ProjectView.as_view()),
    path('api/profile/', views.ProfileView.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
