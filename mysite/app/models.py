from django.db import models

class AlumniInfo(models.Model):
    DEPARTMENT_CHOICES = [
        ('computer_department', 'Computer Engineering'),
        ('electrical_department', 'Electrical Engineering'),
        ('electronics_department', 'Electronics Engineering'),
        ('automobile_department', 'Automobile Engineering'),
        ('mechanical_department', 'Mechanical Engineering'),
        ('civil_department', 'Civil Engineering'),
        
    ]
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES, default='computer_engineering')
    graduation_year = models.PositiveIntegerField()
    contact_email = models.EmailField()
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    linkedin_profile = models.URLField()
    major = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/alumni_photos/', null=True, blank=True)
    def __str__(self):
       return self.full_name




