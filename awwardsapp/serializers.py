from rest_framework import serializers
from .models import Projects, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'screenshot','url', 'user', 'date_created')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_picture', 'bio', 'contact_information')