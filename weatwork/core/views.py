from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from  django.template import loader

def home(request):
    users = User.objects.all()
    template = loader.get_template('core/index.html')
    context = {
        'users_list': users,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    return(HttpResponse('Hello World'))