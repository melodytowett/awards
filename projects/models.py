
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.CharField(max_length=300)
    link = models.TextField(max_length=200)

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user_bio = models.TextField(blank=True)
    Projects = models.ForeignKey(Projects,on_delete=models.CASCADE)
    contact = models.TextField(blank=True)