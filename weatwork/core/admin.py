from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

# Register your models here.
from . import models

 
class UserAdmin(BaseUserAdmin):
    ordering=['id']
    list_display=[
        'email',
        'name',
        'user_image',
        'first_name',
        'last_name',
        'about',
        'nickname',
        'linkedin_id',
        'linkedin',
        'instagram',
        'youtube',
        'twitter',
        'udemy',
        'quora',
        'snapchat',
        'twitch',
        'tiktok',
        'github',
        'gitlab',
        'bitbucket',
        'country',
        'region',
        'city',
        'address',
        'zip_code',
        'current_job',
        'current_company_name',
        'current_company_website',
        'current_company_address',
        'current_company_activity_area',
        'current_job_start_date',
        'next_availability_date',
        'work_experience_in_months',
        'is_company_owner',
        'is_self_employed',
        'is_open_to_work',
        'is_notice_period',
        'is_showing_photos',
        'is_showing_videos',
        'is_showing_cv',
        'is_showing_social_media_badges',
        'is_showing_degrees',
        'is_showing_certifications',
        'is_showing_given_recommendations',
        'is_showing_received_recommendations',
        'is_showing_linkedin_data',
        'is_download_allowed'
    ]
    
    # Fields of the edit user page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'name',
                'user_image',
                'first_name',
                'last_name',
                'about',
                'nickname',
                'linkedin_id',
                'linkedin',
                'instagram',
                'youtube',
                'twitter',
                'udemy',
                'quora',
                'snapchat',
                'twitch',
                'tiktok',
                'github',
                'gitlab',
                'bitbucket',
                'country',
                'region',
                'city',
                'address',
                'zip_code',
                'current_job',
                'current_company_name',
                'current_company_website',
                'current_company_address',
                'current_company_activity_area',
                'current_job_start_date',
                'next_availability_date',
                'work_experience_in_months',
                'is_company_owner',
                'is_self_employed',
                'is_open_to_work',
                'is_notice_period',
                'is_showing_photos',
                'is_showing_videos',
                'is_showing_cv',
                'is_showing_social_media_badges',
                'is_showing_degrees',
                'is_showing_certifications',
                'is_showing_given_recommendations',
                'is_showing_received_recommendations',
                'is_showing_linkedin_data',
                'is_download_allowed'
            )
            }),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    
    #Fields of the create user page
    add_fieldsets = (
        (None,  {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Company)
admin.site.register(models.ProfileType)
admin.site.register(models.Gallery)
admin.site.register(models.Media)
admin.site.register(models.Favorite)
admin.site.register(models.Tag)
admin.site.register(models.FeedPost)
admin.site.register(models.Recommendation)
admin.site.register(models.WorkExperience)
