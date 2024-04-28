from django.db import models
from datetime import date
from solo.models import SingletonModel

# Create your models here.

class PersonalData(SingletonModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    nacionality = models.CharField(max_length=100, null=True)
    about_me = models.TextField(blank=True)
    class Meta:
        verbose_name = "My personal data"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    main_skill = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='media/skills/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.skill}"

class Experience(models.Model):
    job_title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    current_job = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.job_title} {self.company}"