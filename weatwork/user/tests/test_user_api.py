from django.test import TestCase
from django.contrib.auth import  get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status # Adds readability


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')

def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class  PublicUserApiTests(TestCase):
    """Test the public users API"""
    
    def setUp(self):
        self.client = APIClient()
        
    def test_create_valid_user_successfull(self):
        """Tests creating user with valid payload is successful"""
        payload = {
            'email': 'test@md.com',
            'password': 'testpass',
            'name': 'Test'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
        user = get_user_model().objects.get(**res.data)
        
        # Test if the user dict contains a key 'password'
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
    
    
    def test_user_already_exists(self):
        """Tests if creating a anready created user fails"""
        payload = {
            'email': 'test@md.com',
            'password': 'testpass',
            'name': 'Test'
        }
        create_user(**payload)
        
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    
    def test_password_too_short(self):
        """Tests that password is longer than 5 characters"""
        payload = {
            'email': 'test@md.com',
            'password': 'pw',
            'name': 'Test'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        
        self.assertFalse(user_exists)
        
    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@md.com', 'password': 'password'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_create_token_invalid_credentials(self):
        """Tests that no token is created when credentials are invalid"""
        create_user(email='test@md.com', password='password')
        payload = {'email': 'test@md.com', 'password': 'badpass'}
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_token_with_no_user(self):
        """Tests that the token is not created if the user does not exists"""
        payload = {'email': 'test@md.com', 'password': 'password'}
        res = self.client.post(TOKEN_URL, payload)
        
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_token_missing_fields(self):
        """Tests that email and password are required"""
        res = self.client.post(
            TOKEN_URL, 
            {'email': 'test', 'password': ''}
        )
        
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_retrieve_user_unauthorized(self):
        """Tests that authentication is required for users"""
        res = self.client.get(ME_URL)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserAPITests(TestCase):
    """Tests API requests that require authentication"""
    
    def setUp(self):
        self.user = create_user(
            email='maintainer@md.com',
            password='testpass',
            name='testname'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def  test_retrieve_account_success(self):
        """Tests retrieving account for logged in user"""
        res = self.client.get(ME_URL)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            res.data,
            {
                'name': self.user.name,
                'email': self.user.email
            }
        )
    
    def test_post_not_allowed(self):
        """Tests that POST is not allowed on the me url"""
        res = self.client.post(ME_URL, {})
        
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_update_user_profile(self):
        """Test updatinf the user profile for authenticated user"""
        payload = {'name': 'new name', 'password': 'newpassword456'}
        
        res = self.client.patch(ME_URL, payload)
        
        # Update the user from the latest value in the database
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    