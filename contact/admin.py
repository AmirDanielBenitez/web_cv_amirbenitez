from django.contrib import admin
from .models import ContactData
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(ContactData, SingletonModelAdmin)