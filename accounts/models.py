# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
