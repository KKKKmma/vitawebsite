import re
from django.db import models
from django.db.models.base import Model
from PIL import Image
from io import BytesIO
from django.db.models.fields import BooleanField, CharField, DateField
from datetime import datetime

from django.core.files import File

# 會員帳號
class Member(models.Model):
    member_name = models.CharField(max_length=50,null=False)
    member_number = models.IntegerField(null=False,unique=True,primary_key=True)
    email = models.EmailField(null=False)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_time = models.DateTimeField(auto_now_add=True) # auto_now_add: 建立時的時間，往後修改model不會更新
    modify_time = models.DateTimeField(auto_now=True) # auto_now: 每次save都更新為當前的時間
    
    def __unicode__(self):
        return self.member_name

# 員工帳號
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_at = models.DateTimeField(auto_now_add=True)    #創建时间
    update_at = models.DateTimeField(auto_now=True)    #修改时间

    def __unicode__(self):
        return self.username

    


# 支付狀態
# class Payment(models.Model):
#     payment_id = models.IntegerField()
#     order_number = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment_order_number')
#     price = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='payment_price')
#     payment_statue = models.BooleanField(default=False) # False：未付款、Ture：已付款

#     def __unicode__(self):
#         return self.product_name



