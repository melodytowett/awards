from.models import Profile, Projects,Rating
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["title","image","description","link"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic","user_bio","contact"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["design","usability","content","creativity"]
