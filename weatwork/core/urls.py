from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    # path('me/', views.ManageUserView.as_view(), name='me'),
]