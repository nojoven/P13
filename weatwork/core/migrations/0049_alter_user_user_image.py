# Generated by Django 3.2.7 on 2021-11-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_alter_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='female-worker-default.jpg', upload_to='media'),
        ),
    ]