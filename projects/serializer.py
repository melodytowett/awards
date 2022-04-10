from dataclasses import fields
from pyexpat import model
from rest_framework import serializers 
from .models import Projects,Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id','title','image','description','link','user')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','profile_pic','user_bio','contact')
