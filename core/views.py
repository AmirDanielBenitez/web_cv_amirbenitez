from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from resume.models import PersonalData
from contact.models import ContactData
# Create your views here.
class HomePage(TemplateView):
    template_name='core/home_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personalData = PersonalData.get_solo()
        contactData = ContactData.get_solo()
        context["name"] = f'{personalData.first_name} {personalData.last_name}'
        context["short_description"] = personalData.short_description
        context["about_me"] = personalData.about_me
        context["contact_data"] = contactData
        return context
    