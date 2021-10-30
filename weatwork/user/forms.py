from django import forms
from django.contrib.auth.forms import UserCreationForm

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