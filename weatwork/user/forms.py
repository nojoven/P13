from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from core.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = [
            'email', 
            'username',
            'user_image', 
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class AccountForm(UserChangeForm):
    # Hide the password field
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            'user_image',
            'name',
            'first_name',
            'last_name',
            'about',
            'nickname',
            'linkedin_id',
            'linkedin',
            'instagram',
            'youtube',
            'twitter',
            'udemy',
            'quora',
            'snapchat',
            'twitch',
            'tiktok',
            'github',
            'gitlab',
            'bitbucket',
            'country',
            'region',
            'city',
            'address',
            'zip_code',
            'current_job',
            'current_company_name',
            'current_company_website',
            'current_company_address',
            'current_company_activity_area',
            'current_job_start_date',
            'next_availability_date',
            'work_experience_in_months',
            'is_company_owner',
            'is_self_employed',
            'is_open_to_work',
            'is_notice_period',
            'is_showing_photos',
            'is_showing_videos',
            'is_showing_cv',
            'is_showing_social_media_badges',
            'is_showing_degrees',
            'is_showing_certifications',
            'is_showing_given_recommendations',
            'is_showing_received_recommendations',
            'is_showing_linkedin_data',
            'is_download_allowed'
        ]