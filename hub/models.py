from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event_s(models.Model):
    title = models.CharField(max_length=200, default="Untitled Event")
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    time = models.CharField(max_length=100,null=True)
    venue = models.CharField(max_length=255,null=True)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title