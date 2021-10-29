from django import forms
from .models import Media

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'title', 'path']