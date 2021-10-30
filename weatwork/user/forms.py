from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'user_image', 'password1', 'password2']