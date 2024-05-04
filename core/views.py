from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from resume.models import PersonalData, Skill
from contact.models import ContactData
# Create your views here.
class HomePage(TemplateView):
    template_name='core/home_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personalData = PersonalData.get_solo()
        contactData = ContactData.get_solo()
        skills = Skill.objects.all()
        context["name"] = f'{personalData.first_name} {personalData.last_name}'
        context["personal_data"] = personalData
        context["contact_data"] = contactData
        context["skills"] = skills
        return context
    