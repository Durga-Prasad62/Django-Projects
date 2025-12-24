from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField(max_length=150)

class Productmodel(models.Model):
        pro_name = models.CharField(max_length=150)
        pro_price = models.IntegerField()
        pro_quantity = models.IntegerField()
