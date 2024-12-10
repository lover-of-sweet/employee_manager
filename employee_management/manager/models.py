from django.db import models

# Create your models here.

class Positions(models.Model):
    post = models.CharField(max_length=255)
    category = models.CharField(max_length=255)