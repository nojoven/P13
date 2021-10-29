from django.shortcuts import render, redirect
from .models import User, Media
from .forms import MediaForm

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
    form = MediaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('core:home')
    
    return render(request, 'core/media-form.html', {'form': form})

def update_file(request, file_id):
    media = Media.objects.get(id=file_id)
    
    form = MediaForm(request.POST or None, request.FILES or None, instance=media)
    if form.is_valid():
        form.save()
        return redirect('core:home')
    
    return render(request, 'core/media-form.html', {'form': form, 'media': media})

def delete_file(request, file_id):
    media = Media.objects.get(id=file_id)
    
    if request.method == 'POST':
        media.delete()
        return redirect('core:home')
    
    return render(request, 'core/confirm-file-delete.html', {'media': media})

   