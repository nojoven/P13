# Generated by Django 3.2.7 on 2021-10-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_media_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedpost',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='feedpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='media',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='media',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]