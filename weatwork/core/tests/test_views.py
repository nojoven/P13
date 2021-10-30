from django.test import TestCase, Client
from django.contrib.auth import get_user_model  # Better than importing the model itself
from django.urls import reverse

from ..models import Company, ProfileType, Tag, Media, Gallery, WorkExperience, Recommendation, Favorite, FeedPost
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
    
    # Test Media Upload Form View
    def test_media_upload_form_page(self):
        """Test requesting the media upload form page"""
        res = self.client.get(f"/addfile/")
        self.assertEqual(res.status_code, 200)

    # Test Media Edit Form View
    # def test_media_edit_form_page(self):
    #    """Test requesting the media edition form page"""
    #    file_id = 1
    #    res = self.client.get(f"/editfile/{file_id}/")
    #    self.assertEqual(res.status_code, 200)
    
    # Test Media Confirm Delete View
    # def test_media_confirm_delete_page(self):
    #    """Test requesting the media deletion confirm form page"""
    #    res = self.client.get(f"/delfile/1")
    #    self.assertEqual(res.status_code, 200)