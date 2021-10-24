from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from  content.serializers import TagSerializer


TAGS_URL = reverse('content:tag-list')


class PublicTagsApiTests(TestCase):
    """Tests the publicly available tags API"""
    
    def setUp(self):
        self.client = APIClient()
    
    def  test_login_required(self):
        """Tests that login is required to fetch tags"""
        res = self.client.get(TAGS_URL)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        

class PrivateTagsApiTests(TestCase):
    """Tests the tags API when a user is authorized"""
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@md.com',
            'password1234'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        
    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(author=self.user, name='Futuristic')
        Tag.objects.create(author=self.user, name='Testival')
        
        res = self.client.get(TAGS_URL)
        
        tags = Tag.objects.all().order_by('-author')
        serializer = TagSerializer(tags, many=True) # Many argument for more than one object
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_tags_limited_to_user(self):
        """Test that tags are returned for authenticated users"""
        # Add a second user who is not authenticated
        user2 = get_user_model().objects.create_user(
            'second@md.com',
            'password9876'
        )
        
        Tag.objects.create(author=user2, name='optimal')
        
        # Creat a tag for the user 1 which is authenticated
        tag = Tag.objects.create(author=self.user, name='JobSeekersForce')
        
        res = self.client.get(TAGS_URL)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)