from django.db import models
from solo.models import SingletonModel

# Create your models here.
class ContactData(SingletonModel):
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    linkedin = models.URLField(max_length=200)
    whatsapp_url = models.URLField(max_length=200) 
    
    def __str__(self):
        return f"Contact Data"
    
    def formatted_phone_number(self):
        digits_only = ''.join(filter(str.isdigit, self.phone_number))
        if len(digits_only) > 10:
            return f"(+{digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
        else:
            return f"{digits_only[:4]}-{digits_only[4:]}"