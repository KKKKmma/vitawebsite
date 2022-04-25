from django.db import models
from PIL import Image
from io import BytesIO
from home.models import Member,User
from product.models import Product
from django.core.files import File

# 訂單狀態
class Order(models.Model):
    order_number = models.IntegerField()
    order_list = models.CharField(max_length=50)
    member_name = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='order_member_name')
    phone_number = models.ForeignKey(Member,on_delete=models.CASCADE,related_name='order_phone_number')
    reserver_date = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_reserver_date')
    email = models.ForeignKey(Member,on_delete=models.CASCADE)
    payment_statue = models.BooleanField(default=False) # False：未付款、Ture：已付款
    send_mail = models.BooleanField(default=False) # False：未發送、Ture：已發送

    def __unicode__(self):
        return self.product_name

    def Meta(self):
        ordering = ['-created_at',]             

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id