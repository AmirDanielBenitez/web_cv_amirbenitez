from django.contrib import admin
from .models import PersonalData, Skill, Experience
from solo.admin import SingletonModelAdmin

# Register your models here.    
admin.site.register(PersonalData, SingletonModelAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'main_skill')
    list_filter = ('main_skill',)
    search_fields = ('skill',)

admin.site.register(Skill, SkillAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'finish_date', 'current_job')
    list_filter = ('current_job',)
    search_fields = ('job_title', 'company')

admin.site.register(Experience, ExperienceAdmin)