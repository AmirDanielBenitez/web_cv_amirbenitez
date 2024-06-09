from django.contrib import admin
from .models import Project, ProjectContent, ProjectContentImage

# Register your models here.
class ProjectContentImageInline(admin.TabularInline):
    model = ProjectContentImage
    extra = 1

class ProjectContentInline(admin.TabularInline):
    model = ProjectContent
    extra = 1
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    list_filter = ('platform',)
    search_fields = ('name',)
    inlines = [ProjectContentInline]
    
class ProjectContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')
    inlines = [ProjectContentImageInline]

class ProjectContentImageAdmin(admin.ModelAdmin):
    list_display = ('projectContent', 'image')
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectContent, ProjectContentAdmin)
admin.site.register(ProjectContentImage, ProjectContentImageAdmin)
