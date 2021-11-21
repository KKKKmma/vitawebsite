from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateField
from datetime import datetime

# 會員帳號
class Member(models.Model):
    member_name = models.CharField(max_length=50,null=False)
    phone_number = models.IntegerField(null=False,unique=True)
    email = models.EmailField(null=False)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_time = models.DateTimeField(default=datetime.now)
    modify_time = models.DateTimeField(default=datetime.now)
    


    


# 員工帳號
class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间



# 商品資料    
class Product(models.Model):
    product_number = models.CharField(max_length=50)
    reservation_date = models.DateField()
    reservation_time = models.TimeField() 
    stock = models.BooleanField(default=1)
    category_id = models.IntegerField()
    cover_pic = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(default=datetime.now)
    modify_time = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField()


# 訂單狀態
class Order(models.Model):
    order_number = models.IntegerField()
    order_list = CharField(max_length=50)
    member_name = models.CharField(max_length=50,null=False)
    phone_number = models.IntegerField(null=False,unique=True)
    email = models.EmailField(null=False)
    payment_statue = models.BooleanField(default=0) # 0：未付款、1：已付款
    send_mail = models.BooleanField(default=0) # 0：未發送、1：已發送


# 支付狀態
class Payment(models.Model):
    payment_id = models.IntegerField()
    order_number = models.IntegerField()
    member_name = models.CharField(max_length=50,null=False)
    phone_number = models.IntegerField(null=False,unique=True)
    price = models.IntegerField()
    payment_statue = models.BooleanField(default=0) # 0：未付款、1：已付款

# 商品分類表
class classify(models.Model):
    classify_name  = models.CharField(max_length=50)
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(default=datetime.now)
    modify_time = models.DateTimeField(default=datetime.now)