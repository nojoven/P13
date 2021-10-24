from  django.urls import path, include
from  rest_framework.routers import DefaultRouter

from content import views

# Router formats the url for us
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'content'

urlpatterns = [
    path('', include(router.urls))
]



