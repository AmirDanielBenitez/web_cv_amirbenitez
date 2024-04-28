from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    list_filter = ('platform',)
    search_fields = ('name',)
    
admin.site.register(Project, ProjectAdmin)
