from django.db import models

# Create your models here.

class Zr(models.Model):
    token = models.TextField()
    key = models.TextField()