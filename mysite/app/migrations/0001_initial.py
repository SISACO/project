# Generated by Django 3.2.23 on 2023-12-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('graduation_year', models.PositiveIntegerField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('linkedin_profile', models.URLField()),
                ('major', models.CharField(max_length=255)),
            ],
        ),
    ]
