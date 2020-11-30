from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Projects


class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_picture', 'bio']

class projectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','description','screenshot','url']