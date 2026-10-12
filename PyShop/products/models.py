from django.db import models


class Product(models.Model):
   objects = None
   name = models.CharField(max_length=255)
   price = models.FloatField()
   stock = models.IntegerField()
   image_url = models.CharField(max_length=2083)


class Offer(models.Model):
   code = models.CharField(max_length=10)
   description = models.CharField(max_length=25)
   discount = models.FloatField()

# models defines the common characteristics and behaviours and modules in a django projects
# common operations database managements is an example.



# Create your models here.
