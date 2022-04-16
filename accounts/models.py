from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
