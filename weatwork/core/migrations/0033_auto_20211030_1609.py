# Generated by Django 3.2.7 on 2021-10-30 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_feedpost_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileType',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='profile',
            new_name='profile_type',
        ),
    ]