# Generated by Django 5.0 on 2023-12-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_alumniinfo_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniinfo',
            name='department',
            field=models.CharField(choices=[('computer_department', 'Computer Engineering'), ('electrical_department', 'Electrical Engineering'), ('electronics_department', 'Electronics Engineering'), ('automobile_department', 'Automobile Engineering'), ('mechanical_department', 'Mechanical Engineering'), ('civil_department', 'Civil Engineering')], default='computer_engineering', max_length=255),
        ),
    ]