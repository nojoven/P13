# Generated by Django 3.2.7 on 2021-11-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_media_media_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediatype',
            name='name',
            field=models.CharField(default='image', max_length=255, null=True, unique=True),
        ),
    ]