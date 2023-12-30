from django.db import models

from tinymce import models as tinymce_models

class AlumniInfo(models.Model):
   
   
   INDUSTRY_CHOICES = [
        ('it_software', 'IT/Software'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('manufacturing', 'Manufacturing'),
        ('education', 'Education'),
        ('construction', 'Construction'),
        ('telecommunications', 'Telecommunications'),
        ('retail', 'Retail'),
        ('energy', 'Energy'),
        ('media', 'Media/Entertainment'),
        ('pharmaceutical', 'Pharmaceutical'),
        ('aerospace', 'Aerospace'),
        ('automotive', 'Automotive'),
        ('consulting', 'Consulting'),
        ('biotechnology', 'Biotechnology'),
        ('hospitality', 'Hospitality'),
        ('insurance', 'Insurance'),
        ('real_estate', 'Real Estate'),
        ('environmental', 'Environmental Services'),
        ('government', 'Government'),
        ('research', 'Research'),
        ('logistics', 'Logistics/Supply Chain'),
        ('sports', 'Sports'),
        ('non_profit', 'Non-profit'),
        ('other', 'Other'),
        ('fashion', 'Fashion'),
        ('marketing', 'Marketing/Advertising'),
        ('tech_startups', 'Tech Startups'),
        ('legal', 'Legal Services'),
        ('fitness', 'Fitness/Wellness'),
        ('pharmacy', 'Pharmacy'),
        ('art_design', 'Art/Design'),
        ('music', 'Music'),
        ('food_beverage', 'Food and Beverage'),
        ('tourism', 'Tourism/Travel'),
        ('e-commerce', 'E-commerce'),
        ('Other','Other'),
    # Add more industries as needed
    ]
    
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
   industry = models.CharField(max_length=255, choices=INDUSTRY_CHOICES, default='Other')
   linkedin_profile = models.URLField()
   photo = models.ImageField(upload_to='media/alumni_photos/', null=True, blank=True)
   def __str__(self):
       return self.full_name




class Activities(models.Model):
    title = models.CharField(max_length=100)
    activities_photo = models.ImageField(upload_to='media/activities_photo/', null=True, blank=True)
    text = tinymce_models.HTMLField()
    def __str__(self):
       return self.title