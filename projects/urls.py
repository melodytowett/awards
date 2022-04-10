
from django.conf import settings
from django .urls import path,include,re_path
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects',views.ProjViewSet)
router.register('profile',views.ProfViewSet)
urlpatterns=[
    path('',views.index,name = 'index'),
    # path("",views.date, name='date'),
    path('post-project/',views.my_projects,name='post-project'),
    re_path(r'^project/<project_id>',views.project_rating,name='rate_project'),
    path('profile/',views.update_profile,name='update_profile'),
    path('prof/',views.profile,name='profile'),
    path('search/',views.search_project, name='search_project'),
    path("register/",views.register_user,name='register'),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name='logout'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/',include(router.urls),name='api')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)