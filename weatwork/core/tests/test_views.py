from django.test import TestCase, Client
from django.contrib.auth import get_user_model  # Better than importing the model itself
from django.urls import reverse

from ..models import Company, Profile, Tag, Media, Gallery, Job, Recommendation, Favorite, FeedPost
from core.constants import INDUSTRY_LIST, USERS_PROFILES

def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class ViewsTests(TestCase):
    client = Client()
    
    def setUp(self):
        self.user = create_user(
            email='maintainer@md.com',
            password='testpass',
            name='testname'
        )
    
    # Test Home View
    def test_home_page_available(self):
        """Test requesting the home page"""

        res = self.client.get('/home/')
        self.assertEqual(res.status_code, 200)
    
    # Test User View
    def test_user_page_available(self):
        """Test requesting the user page"""
        user_id = self.user.id
        res = self.client.get(f"/showcase/user/{user_id}/")
        self.assertEqual(res.status_code, 200)