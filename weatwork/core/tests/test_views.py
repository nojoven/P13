from django.test import TestCase, Client
from django.contrib.auth import get_user_model  # Better than importing the model itself
from django.urls import reverse

from ..models import Company, Profile, Tag, Media, Gallery, Job, Recommendation, Favorite, FeedPost
from core.constants import INDUSTRY_LIST, USERS_PROFILES


def sample_user(email='testwork@md.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)

class ViewsTests(TestCase):
    client = Client()
    
    # Test Home View
    def test_home_page_available(self):
        """Test requesting the home page"""

        res = self.client.get('/home/')
        self.assertEqual(res.status_code, 200)