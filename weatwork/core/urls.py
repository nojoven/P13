from django.conf.urls import url
from django.urls import path
from django.urls.conf import include

from core import views


app_name = 'core'

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    # /home
    path('home/', views.home, name='home'),
    
    # /home/<int>
    path('showcase/user/<int:user_id>/', views.showcase, name='showcase'),
    # path('me/', views.ManageUserView.as_view(), name='me'),
]