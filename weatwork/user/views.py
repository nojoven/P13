from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  get_user_model
from django.contrib import messages

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

from core.models import User
from .forms import RegistrationForm, AccountForm

def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class  CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        """Fetches the authenticated user"""
        return self.request.user


def register(request):
    """Register the user"""
    if request.method == 'POST':
        user = User()
        form = RegistrationForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"Welcome ! Your account is created with your email address {email} !")
            return redirect('login')
    else:        
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

# Profile page   
def profile(request):
    """Displays the current user's profile"""
    return render(request, 'user/profile.html')


# Account management page - needs login to be accessed
@login_required  
def account(request):
    """Provides a form to edit user's details"""
    
    user = User.objects.get(email=request.user)
    form = AccountForm(request.POST or None, request.FILES or None, instance=user)
    
    if form.is_valid():
        form.save()
        messages.success(request, f"Your details have been updated successfully.")
        return redirect('profile')
       
    #context = {'current_user': user}
    return render(request, 'user/account.html', {'form': form})
    



@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, f"Your account is now deleted.")
        return redirect('core:home')