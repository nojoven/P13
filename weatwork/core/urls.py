from django.conf.urls import url
from django.urls import path
from django.urls.conf import include

from core import views


app_name = 'core'

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    
    # /home
    path('home/', views.home, name='home'),
    
    # /showcase/uuid
    path('showcase/<uuid:user_uuid>/', views.showcase, name='showcase'),
        
    # add media file
    path('addfile/', views.add_file, name='add_file'),
    
    # add gallery
    path('addgallery/', views.add_gallery, name='add_gallery'),
    
    # edit media file
    path('editfile/<int:file_uuid>/', views.update_file, name='update_file'),
]