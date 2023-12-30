# Generated by Django 5.0 on 2023-12-30 10:54

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='activities_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/activities_photo/'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]