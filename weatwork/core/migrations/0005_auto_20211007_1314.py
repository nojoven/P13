# Generated by Django 3.2.7 on 2021-10-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_auto_20211007_1313"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="current_job_start_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="next_availability_date",
            field=models.DateField(null=True),
        ),
    ]
