from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    users = User.objects.all().filter(is_superuser=True, is_active=True)
    context = {
        'users_list': users,
    }
    return render(request, 'core/home.html', context)


def showcase(request, user_id):
    
    
    user = User.objects.get(pk=user_id)
    context = {'user' : user}
    
    return render(request, 'core/showcase.html', context)
