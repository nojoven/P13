from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path('home/', views.index, name='index'),
    # path('home/', views.CreateUserView.as_view(), name='create'),
    # path('me/', views.ManageUserView.as_view(), name='me'),
]