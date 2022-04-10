from unicodedata import name
from django.conf import settings
from django .urls import path
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    # path("",views.date, name='date'),
    path('post-project/',views.my_projects,name='post-project'),
    path('project/',views.project_rating,name='rate_project'),
    path('profile/',views.update_profile,name='update_profile'),
    path('prof/',views.profile,name='profile'),
    path('search/',views.search_project, name='search_project'),
    path("register/",views.register_user,name='register'),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name='logout')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)