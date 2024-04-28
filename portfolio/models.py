from django.db import models

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
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='media/portfolio/', blank=True, null=True)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    
    def __str__(self):
        return self.name
    