from re import T
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def all_projects(cls,title):
        project = cls.objects.filter(title__in=title)
        return project

    @classmethod
    def search_by_title(cls,search_title):
        projects = cls.objects.filter(title__icontains=search_title)
        return projects

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user_bio = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    contact = models.TextField(blank=True)

    def __str__(self):
        return self.user_bio

    def save_profile(self):
        self.save()

class Rating(models.Model):
    rating=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )
    design = models.IntegerField(choices=rating,blank=True,default=1)
    content = models.IntegerField(choices=rating,default=1,blank=True)
    usability = models.IntegerField(choices=rating,default=1,blank=True)
    creativity = models.IntegerField(choices=rating,default=1,blank=True)
    score = models.FloatField(default=0,blank=True)
    design_average = models.FloatField(default=0,blank=True)
    content_average = models.FloatField(default=0,blank=True)
    usability_average = models.FloatField(default=0,blank=True)
    creativity = models.FloatField(default=0,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='rater')
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='ratings',null=True)
    
    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls,id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project}Rating'
    
