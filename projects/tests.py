
from django.test import TestCase

from . models import Profile,Projects
# Create your tests here.

class ProjectsTestClass(TestCase):
    def setUp(self):
        # self.user = User(username = 'melody',email="melody@gmail.com")
        self.projects = Projects(title = "Instagram",description = 'my first instagram clone project',link = "https://github.com/",image='image.jpg')
        self.projects.save_project()

    def test_project_instance(self):
        self.assertTrue(isinstance(self.projects,Projects))

    def test_save_projects(self):
        self.projects.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)
       
  
    def get_projects(self):
        my_projects = Projects.all_projects() 
        self.assertTrue(len(my_projects)>0)

    def tearDown(self):
        Projects.objects.all().delete()

 

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user_bio="things about me",contact="028293892",profile_pic="image.png")
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # def test_save_profile(self):
    #     self.profile.save_profile()
    #     profile = Profile.objects.all()
    #     self.assertTrue(len(profile)>0)
