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
        
    # Test Login View
    def test_login_page_available(self):
        """Test requesting the login page"""
        res = requests.get('http://localhost:8000/login')
        self.assertEqual(res.status_code, 200)
    
    # Test Logout View
    def test_logout_page_available(self):
        """Test requesting the logout page"""
        res = requests.get('http://localhost:8000/logout')
        self.assertEqual(res.status_code, 200)