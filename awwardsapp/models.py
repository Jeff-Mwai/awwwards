from django.db import models                   
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact_information = models.TextField(default="+254")

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

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

RATE_CHOICES = [
(1,'1- Poor'),
(2,'2- Poor'),
(3,'3- Fair'),
(4,'4- Fair'),
(5,'5- Good'),
(6,'6- Good'),
(7,'7- Very Good'),
(8,'8- Very Good'),
(9,'9- Excellent'),
(10,'10- Excellent'),
]

class Rate(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    


    def __str__(self):
        return self.user.username