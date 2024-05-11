from django.db import models
from ckeditor.fields import RichTextField
from resume.models import Skill

# Create your models here.
class Project (models.Model):
    WEB = 'web'
    APP = 'app'
    PLATFORM_CHOICES = [
        (WEB, 'Web'),
        (APP, 'Mobile'),
    ]
    
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=150)
    description = RichTextField(blank=True)
    thumbnail = models.ImageField(upload_to='media/portfolio/', blank=True, null=True)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    skills = models.ManyToManyField(Skill)
    code_url = models.URLField(max_length=200, null=True, blank=True)
    project_url = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    