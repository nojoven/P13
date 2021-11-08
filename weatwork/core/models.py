import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")

        # Lower the domain part of the email address before creating the user
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of usernames"""

    email = models.EmailField(max_length=255, unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    mood = models.CharField(max_length=255, null=True, blank=True)
    user_image = models.ImageField(default="https://cdn.pixabay.com/photo/2019/07/26/20/52/man-4365597_960_720.png")
    username = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, null=True, default=None, blank=True)
    nickname = models.CharField(max_length=255, blank=True)
    linkedin_id = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    udemy = models.URLField(max_length=255, blank=True)
    quora = models.URLField(max_length=255, blank=True)
    snapchat = models.URLField(max_length=255, blank=True)
    twitch = models.URLField(max_length=255, blank=True)
    tiktok = models.URLField(max_length=255, blank=True)
    github = models.URLField(max_length=255, blank=True)
    gitlab = models.URLField(max_length=255, blank=True)
    bitbucket = models.URLField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    # phone = models.CharField(max_length=20, unique=True)
    current_job = models.CharField(max_length=255, blank=True)
    current_company_name = models.CharField(max_length=255, blank=True)
    current_company_website = models.URLField(max_length=255, blank=True)
    current_company_address = models.CharField(max_length=255, blank=True)
    current_company_activity_area = models.CharField(max_length=255, blank=True)
    current_job_start_date = models.DateField(null=True, blank=True)
    next_availability_date = models.DateField(null=True, blank=True)
    work_experience_in_months = models.IntegerField(default=0, blank=True)

    profile_type = models.ForeignKey('ProfileType', on_delete=models.SET_NULL, null=True)
    
    is_company_owner = models.BooleanField(null=True)
    is_self_employed = models.BooleanField(null=True)
    is_open_to_work = models.BooleanField(null=True)
    is_notice_period = models.BooleanField(null=True)

    is_showing_photos = models.BooleanField(default=True)
    is_showing_videos = models.BooleanField(default=True)
    is_showing_cv = models.BooleanField(default=True)
    is_showing_social_media_badges = models.BooleanField(default=True)
    is_showing_degrees = models.BooleanField(default=True)
    is_showing_certifications = models.BooleanField(default=True)
    is_showing_given_recommendations = models.BooleanField(default=True)
    is_showing_received_recommendations = models.BooleanField(default=True)
    is_showing_linkedin_data = models.BooleanField(default=True)

    is_download_allowed = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Company(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    registration_number = models.CharField(max_length=255, unique=True)
    industry = models.CharField(max_length=100, blank=True)
    headquarters_country = models.CharField(max_length=200, blank=True)
    headquarters_address = models.CharField(max_length=200, blank=True)
    headquarters_zip_code = models.CharField(max_length=200, blank=True)
    motto = models.CharField(max_length=255, blank=True)
    decription = models.TextField(blank=True)
    logo_url = models.CharField(
        max_length=500,
        default="https://cdn.pixabay.com/photo/2019/07/26/20/52/man-4365597_960_720.png",
    )
    number_of_employees = models.IntegerField(default=0)
    creation_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True, blank=True)


class ProfileType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)

class Tag(models.Model):
    def __str__(self):
        return self.name
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=70, blank=True)
    language = models.CharField(max_length=20, blank=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)

class Media(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=100, blank=True)
    media_type = models.CharField(max_length=100, blank=True)
    gallery = models.ForeignKey('Gallery', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    path = models.FileField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    
    is_active = models.BooleanField(default=True)


class MediaType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)

class Gallery(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=255, blank=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    
    is_active = models.BooleanField(default=True)


class WorkExperience(models.Model):
    def __str__(self):
        return self.name

    title = models.CharField(max_length=255, blank=True)
    worker = models.ForeignKey('User', on_delete=models.CASCADE, blank=True)
    company = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=500, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    
    is_current_job = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class Recommendation(models.Model):
    def __str__(self):
        return self.name

    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(max_length=255, blank=True)
    author = models.CharField(max_length=255, blank=True)
    recipient = models.CharField(max_length=255, blank=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    
    is_approved = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class Favorite(models.Model):
    def __str__(self):
        return self.name
    
    is_active = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)

class FeedPost(models.Model):
    def __str__(self):
        return self.name

    author = models.ForeignKey('User', on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=255, blank=True)
    publication_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid1, editable=False)
    
    is_active = models.BooleanField(default=True)