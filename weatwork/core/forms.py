from django import forms
from .models import Media, MediaType

class MediaForm(forms.ModelForm):
    name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    path = forms.FileField(required=True)
    
    media_type = forms.ModelChoiceField(queryset=MediaType.objects.all(), to_field_name='name', required=True)
    class Meta:
        model = Media
        fields = ['name', 'title', 'path', 'media_type']