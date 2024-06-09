from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Project
from resume.models import Skill

# Create your views here.
class PorfolioPage(TemplateView):
    template_name='portfolio/portfolio_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context["projects"] = projects
        return context
    
class ProjectDetailPage(TemplateView):
    template_name='portfolio/project_detail_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = kwargs['id']
        project = Project.objects.get(pk=project_id)
        project_content = project.project_contents.all()
        context["project"] = project
        context["project_content"] = project_content
        return context
    
    