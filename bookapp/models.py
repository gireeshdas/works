from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=120)
    author_name=models.CharField(max_length=120)
    price = models.FloatField(null=True)
    publisher=models.CharField(max_length=120)
    qty=models.IntegerField()

class CartView(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)