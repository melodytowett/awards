
import email
from email.mime import image
from django.test import TestCase
from django.contrib.auth.models import User
import projects
from . models import Profile,Projects
# Create your tests here.

class ProjectsTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'melody',email="melody@gmail.com")
        self.projects = Projects(title = "Instagram",description = 'my first instagram clone project',link = "https://github.com/",image='image.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Projects))

    def test_save_projects(self):
        self.projects.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    # def test_search_project(self):
    #     self.projects.save()
    #     projects = Projects.all_projects()
    #     self.assertTrue(len(projects)>0)

