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
        skills = Skill.objects.all()
        context["projects"] = projects
        context["skills"] = skills
        return context
    
    