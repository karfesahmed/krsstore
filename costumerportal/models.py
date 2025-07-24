from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    sale_price = models.FloatField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name="products")

    def is_on_sale(self):
        return self.sale_price is not None and self.sale_price<self.price

    def __str__(self):
        return f"{self.name}"

class Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to='products/')

class Color(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="colors")
    title = models.CharField(max_length=40,null=True,blank=True)
    image = models.ImageField(upload_to='color/',null=True,blank=True)
    def __str__(self):
        return f"{self.product.name}-color : {self.title}"
class Size(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="size")
    price = models.FloatField(null=True,blank=True)
    title = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return f"{self.product.name}-size : {self.title}"