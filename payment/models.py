from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Payment(models.Model):
    order_number = models.IntegerField(max_length=8)
    payment_state = models.BooleanField(default=False)