from django.db import models

# Create your models here.
class Product(models.Model):
    
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.IntegerField()
    measure_unit = models.IntegerField()
    stock = models.IntegerField()
    color = models.CharField(max_length=255)
    status = models.CharField(max_length=10)