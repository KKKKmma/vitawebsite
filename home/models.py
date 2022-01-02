import re
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateField
from datetime import datetime



# 會員帳號
class Member(models.Model):
    member_name = models.CharField(max_length=50,null=False)
    member_number = models.IntegerField(null=False,unique=True,primary_key=True)
    email = models.EmailField(null=False)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_time = models.DateTimeField(auto_now_add=True) # auto_now_add: 建立時的時間，往後修改model不會更新
    modify_time = models.DateTimeField(auto_now=True) # auto_now: 每次save都更新為當前的時間
    


# 員工帳號
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_at = models.DateTimeField(auto_now_add=True)    #創建时间
    update_at = models.DateTimeField(auto_now=True)    #修改时间



# 商品資料    
class Product(models.Model):
    product_number = models.CharField(max_length=50,primary_key=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField() 
    stock = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    cover_pic = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='vitawebsite_front/scr/image/',height_field=None, width_field=None, max_length=100 ,blank=False, null=False)
    description = models.TextField()
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_user_id')


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

# 購物車狀態
class Cart(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='cart_order_number')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

# 支付狀態
class Payment(models.Model):
    payment_id = models.IntegerField()
    order_number = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment_order_number')
    price = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='payment_price')
    payment_statue = models.BooleanField(default=False) # False：未付款、Ture：已付款

# 商品分類表
class classify(models.Model):
    classify_name  = models.CharField(max_length=50,primary_key=True)
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

