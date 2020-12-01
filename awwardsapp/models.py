from django.db import models                   
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=300, default="My Bio", blank=True)
    contact_information = models.CharField(max_length=300, default="+254")
    

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.user

    @classmethod
    def search_by_name(cls, search_term):
        userProfile = cls.objects.filter(user__username__icontains=search_term).all()
        return userProfile

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    image = models.ImageField(default = 'default.jpg', upload_to = 'images')

    def __str__(self):
        return f'{self.user.username} userProfile'


class Projects(models.Model):
    title = models.CharField(max_length=50, default="My Project")
    description = models.TextField(max_length=300)
    screenshot = models.ImageField(upload_to = 'images/', blank=True)
    url= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    date_created= models.DateField(auto_now_add=True )
    

    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()
