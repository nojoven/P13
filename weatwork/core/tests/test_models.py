from django.test import TestCase
from django.contrib.auth import get_user_model  # Better than importing the model itself

from ..models import Company
from core.constants import INDUSTRY_LIST

class ModelTests(TestCase):
    
    # Test User
    def test_create_user_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = "test@maintainerdev.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))  # Because password is encrypted

    def test_new_user_email_normalized(self):
        """Tests if the email of the new user is normalized"""
        email = "test@MAINTAINERDEV.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 123)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@maintainerdev.com", "test123"
        )
        self.assertTrue(user.is_superuser)  # is_superuser() comes from PermissionsMixin
        self.assertTrue(user.is_staff)

    # Test Company
    def test_create_company(self):
        """Test creating a new user with an email is successful"""
        registration_number="0531"
        name = "The Builders"
        industry = "Software Engineering"
        company = Company.objects.create(name=name, industry=industry.lower(), registration_number=registration_number)

        self.assertEqual(company.name, name)
        self.assertEqual(company.registration_number, registration_number)
        self.assertTrue(company.industry in INDUSTRY_LIST)  # Because password is encrypted
    