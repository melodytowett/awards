
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def save_projects(self):
        self.save()


class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user_bio = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.TextField(blank=True)

    def __str__(self):
        return self.user_bio

    def save_profile(self):
        self.save()