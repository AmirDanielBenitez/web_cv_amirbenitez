from django.db import models
from datetime import date
from solo.models import SingletonModel

# Create your models here.

class PersonalData(SingletonModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    nacionality = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name = "My personal data"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age
