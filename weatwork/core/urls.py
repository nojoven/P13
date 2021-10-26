from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    # /home
    path('home/', views.home, name='home'),
    
    # /home/<int>
    path('user/<int:user_id>/', views.user, name='user'),
    # path('me/', views.ManageUserView.as_view(), name='me'),
]