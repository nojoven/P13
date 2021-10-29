from django.shortcuts import render, redirect
from .models import User
from .forms import FileUploadForm

def home(request):
    users = User.objects.all().filter(is_superuser=False, is_active=True)
    context = {
        'users_list': users,
    }
    return render(request, 'core/home.html', context)

def showcase(request, user_id):    
    user = User.objects.get(pk=user_id)
    context = {'user' : user}
    
    return render(request, 'core/showcase.html', context)

def add_file(request):
    form = FileUploadForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('core:home')
    
    return render(request, 'core/media-upload-form.html', {'form': form})
