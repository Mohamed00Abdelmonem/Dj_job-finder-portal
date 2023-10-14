from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/')
    website_link = models.URLField()
    email = models.EmailField()
    address = models.TextField()
    subtitle_for_company = models.TextField()
    emp_count = models.IntegerField()

    def __str__(self):
        return self.name

JOB_NATURE_CHOICES = [
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('remote', 'Remote'),
]
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_required = models.TextField()
    education = models.CharField(max_length=100)
    posted_date = models.DateField()
    location = models.CharField(max_length=100)
    vacancy = models.PositiveIntegerField()
    job_nature = models.CharField(max_length=50, choices=JOB_NATURE_CHOICES)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    application_date = models.DateField()  

    def __str__(self):
        return self.job_title
