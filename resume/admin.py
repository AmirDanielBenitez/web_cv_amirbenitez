from django.contrib import admin
from .models import PersonalData
from solo.admin import SingletonModelAdmin

# Register your models here.    
admin.site.register(PersonalData, SingletonModelAdmin)