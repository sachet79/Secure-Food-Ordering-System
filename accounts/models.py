from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class MyModel(models.Model):
    phone_number = PhoneNumberField()
