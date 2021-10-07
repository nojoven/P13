from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")

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
    """Custom user model that supports using email instrad of usernames"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # username = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    linkedin = models.URLField(max_length=255, unique=True)
    instagram = models.URLField(max_length=255, unique=True)
    youtube = models.URLField(max_length=255, unique=True)
    twitter = models.URLField(max_length=255, unique=True)
    udemy = models.URLField(max_length=255, unique=True)
    quora = models.URLField(max_length=255, unique=True)
    snapchat = models.URLField(max_length=255, unique=True)
    twitch = models.URLField(max_length=255, unique=True)
    tiktok = models.URLField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    # phone = models.CharField(max_length=20, unique=True)
    current_job = models.CharField(max_length=255)
    current_company_name = models.CharField(max_length=255)
    current_company_website = models.URLField(max_length=255)
    current_company_address = models.CharField(max_length=255)
    current_company_activity_area = models.CharField(max_length=255)
    current_job = models.CharField(max_length=255)
    current_job_start_date = models.DateField(null=True)
    next_availability_date = models.DateField(null=True)
    work_experience_in_months = models.IntegerField(default=0)

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
    is_showing_received_recommendations = models.BooleanField(default=True)

    is_download_allowed = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
