from django.conf.urls import url
from django.urls import path
from django.urls.conf import include

from core import views


app_name = 'core'

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    
    # /home
    path('home/', views.home, name='home'),
    
    # /showcase/user/<int>
    path('showcase/user/<int:user_id>/', views.showcase, name='showcase'),
    
    # add media file
    path('addfile/', views.add_file, name='add_file'),
    
    # edit media file
    path('editfile/<int:file_id>/', views.update_file, name='update_file'),
]