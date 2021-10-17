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

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null = True, default=None)
    nickname = models.CharField(max_length=255)
    linkedin = models.URLField(max_length=255, unique=True, blank=True)
    instagram = models.URLField(max_length=255, unique=True, blank=True)
    youtube = models.URLField(max_length=255, unique=True, blank=True)
    twitter = models.URLField(max_length=255, unique=True, blank=True)
    udemy = models.URLField(max_length=255, unique=True, blank=True)
    quora = models.URLField(max_length=255, unique=True, blank=True)
    snapchat = models.URLField(max_length=255, unique=True, blank=True)
    twitch = models.URLField(max_length=255, unique=True, blank=True)
    tiktok = models.URLField(max_length=255, unique=True, blank=True)
    github = models.URLField(max_length=255, unique=True, blank=True)
    gitlab = models.URLField(max_length=255, unique=True, blank=True)
    bitbucket = models.URLField(max_length=255, unique=True, blank=True)
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


class Company(models.Model):
    def __str__(self):
            return self.name
                    
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=255, unique=True)
    industry = models.CharField(max_length=100)
    headquarters_country = models.CharField(max_length=200)
    headquarters_address = models.CharField(max_length=200)
    headquarters_zip_code = models.CharField(max_length=200)
    motto = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=500, default="https://cdn.pixabay.com/photo/2019/07/26/20/52/man-4365597_960_720.png")
    number_of_employees = models.IntegerField(default=0)
    creation_date = models.DateField(null=True)
    
    is_active = models.BooleanField(default=True)
    
    
class Profile(models.Model):
    def __str__(self):
            return self.name
                    
    name = models.CharField(max_length=100, unique=True)