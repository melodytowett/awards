from dataclasses import fields
from pyexpat import model
from.models import Profile, Projects
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["title","image","description","link"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic","user_bio","contact"]
