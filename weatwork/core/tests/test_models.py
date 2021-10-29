from django.test import TestCase
from django.contrib.auth import get_user_model  # Better than importing the model itself

from ..models import Company, Profile, Tag, Media, Gallery, WorkExperience, Recommendation, Favorite, FeedPost
from core.constants import INDUSTRY_LIST, USERS_PROFILES


def sample_user(email='testwork@md.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    # Test User - Create
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


    # Test User - Update
    

    # Test Company
    def test_create_company(self):
        """Test creating a new company is successful"""
        registration_number = "0531"
        name = "The Builders"
        industry = "Software Engineering"
        company = Company.objects.create(
            name=name,
            industry=industry.lower(),
            registration_number=registration_number,
        )

        company.save()

        self.assertEqual(company.name, name)
        self.assertEqual(company.registration_number, registration_number)
        self.assertTrue(
            company.industry in INDUSTRY_LIST
        )  # Because password is encrypted

    # Test Profile Type
    def test_create_profile_type(self):
        """Test creating a new profile type"""
        name = "worker"
        profile = Profile.objects.create(name=name.lower())
        profile.save()

        self.assertEqual(profile.name, name.lower())

        
    # Test Tag
    def test_create_tag(self):
        """Test creating a new tag and its string representation"""
        name = "happyworker"
        language = "FR"
        
        tag = Tag.objects.create(
            author=sample_user(),
            name=name.lower(),
            language=language.lower()
        )
        tag.save()

        self.assertEqual(str(tag), tag.name)
        self.assertEqual(tag.language, language.lower())
    
    # Test Media - Create
    def test_create_media(self):
        """Test creating a new media"""
        name = "testmedia"
        
        media = Media.objects.create(
            name=name.lower()
        )
        media.save()

        self.assertEqual(media.name, name.lower())
    
    # Test Media - Update
    

    # Test Gallery
    def test_create_gallery(self):
        """Test creating a new gallery"""
        name = "Test Gallery"
        
        gallery = Gallery.objects.create(
            name=name.lower()
        )
        gallery.save()

        self.assertEqual(gallery.name, name.lower())
    
    # Test Job
    def test_create_job(self):
        """Test creating a new job (woek experience)"""
        name = "Job Name"
        
        job = Gallery.objects.create(
            name=name.lower()
        )
        job.save()

        self.assertEqual(job.name, name.lower())
        
    # Test Recommendation
    def test_create_recommendation(self):
        """Test creating a new job (woek experience)"""
        title = "Test Title"
        text = "This test dev is genial. I endorse him."

        
        recommendation = Recommendation.objects.create(
            title=title.lower(), text=text
        )
        recommendation.save()

        self.assertEqual(recommendation.title, title.lower())
        self.assertEqual(recommendation.text, text)
