from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
