from django.db import models

# Create your models here.
class Order(models.Model):
    product = models.CharField(max_length=60)
    wilaya = models.CharField(max_length=60)
    IDwilaya = models.CharField(max_length=2)
    Name = models.CharField(max_length=60)
    Phone = models.CharField(max_length=10)
    order_type = models.CharField(max_length=1,default="0") 
    confirmed = models.CharField(max_length=1,default="0")
    delivery_type =models.CharField(max_length=1,default="0") # confirmed cancel later ....
    Address = models.CharField(max_length=255)
    Size = models.CharField(max_length=60,null=True,blank=True)
    Color = models.CharField(max_length=60,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total = models.CharField(max_length=10)
    note = models.TextField(null=True,blank=True,default="")
    
    
    def tracking_id(self):
        return f"trk-{self.pk}"


    def __str__(self):
        return f"order to {self.Name}"