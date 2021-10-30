import requests

from django.test import TestCase
from django.contrib.auth import  get_user_model
from django.test.client import Client
from django.urls import reverse


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
    
    # Test Register View
    def test_register_page_available(self):
        """Test requesting the register page"""
        res = self.client.get('/register/')
        self.assertEqual(res.status_code, 200)
    
    # Test Profile View
    def test_profile_page_available(self):
        """Test requesting the profile page"""
        res = self.client.get('user/{user_id}/profile/')
        self.assertEqual(res.status_code, 200)