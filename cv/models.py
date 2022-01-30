from django.db import models

# Create your models here.
class profile(models.Model):
    first_name = models.CharField(max_length=100, null=False, help_text="Please enter your own given name")
    last_name = models.CharField(max_length=100, null=False, help_text="Please enter your  surname")
    state_of_origin = models.CharField(max_length=20, null=False, help_text="Please tell us your state of origin")
    date_of_birth = models.DateField(null=False)
  
