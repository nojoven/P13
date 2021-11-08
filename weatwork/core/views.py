from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User, Media
from .forms import MediaForm, GalleryForm

def home(request):
    users = User.objects.all().filter(is_superuser=False, is_active=True)
    context = {
        'users_list': users,
    }
    return render(request, 'core/home.html', context)


@login_required
def add_gallery(request):
    form = GalleryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core:add_file')
    
    return render(request, 'core/gallery-form.html', {'form': form})


@login_required
def add_file(request):
    form = MediaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('profile')
    
    return render(request, 'core/media-form.html', {'form': form})

@login_required
def update_file(request, file_uuid):
    media = Media.objects.get(id=file_uuid)
    
    form = MediaForm(request.POST or None, request.FILES or None, instance=media)
    if form.is_valid():
        form.save()
        return redirect('profile')
    
    return render(request, 'core/media-form.html', {'form': form, 'media': media})

def delete_file(request, file_uuid):
    media = Media.objects.get(id=file_uuid)
    
    if request.method == 'POST':
        media.delete()
        return redirect('core:home')
    
    return render(request, 'core/confirm-file-delete.html', {'media': media})
