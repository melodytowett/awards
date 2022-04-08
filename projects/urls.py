from unicodedata import name
from django.conf import settings
from django .urls import path
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('post-project/',views.my_projects,name='post-project'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)