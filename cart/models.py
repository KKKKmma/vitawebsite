from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Order(models.Model):
    order_number = models.IntegerField(max_length=8)
    order_list = models.CharField(max_length=8)
    username = models.CharField(max_length = 30,null=False)
    phone_number = models.IntegerField(max_length=10,primary_key=True,null=False,unique=True)
    email = models.EmailField(null=False)