from django.db import models

# Create your models here.

class WilayaInfo(models.Model):
    IDWilaya = models.IntegerField()
    name = models.CharField(max_length=20)
    delivery_home = models.IntegerField(null=True)
    delivery_office = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.name}'