from django.db import models
from django.db.models.fields import DateField

class User(models.Model):
    username = models.CharField(max_length = 30,null=False)
    phone_number = models.IntegerField(null=False,unique=True)
    email = models.EmailField(null=False)
    payment_state = models.BooleanField(default=False)
    order_number = models.IntegerField(max_length=8)

    def __unicode__(self):
        return self.username








    
