from django.db import models

# Create your models here.


class Resident(models.Model):
    name = models.CharField(max_length=255)
    DOB = models.DateField()
    species = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
