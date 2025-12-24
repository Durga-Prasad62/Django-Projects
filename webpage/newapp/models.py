import uuid
from django.db import models

# Create your models here.
class MovieDetails(models.Model):
    moviename = models.CharField(max_length=120)
    moviescreen = models.CharField(max_length=120)
    bookingid = models.CharField(max_length=120)
    theatrename = models.CharField(max_length=120)
    user_email = models.EmailField()
    showtype =  models.CharField(max_length=120)
    dateandtime =models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=120,default="INR")
    transactionid =models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

