from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Merchandise(models.Model):
    merchandise_number = models.CharField(max_length=8,primary_key=True)
    reservation_date =  models.DateField(auto_now=False, auto_now_add=False)
    reservation_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    stock = models.BooleanField(default=True)