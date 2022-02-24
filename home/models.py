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

# 商品資料    
class Product(models.Model):
    product_number = models.CharField(max_length=50,primary_key=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField() 
    stock = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    cover_pic = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='vitawebsite_front/scr/image/',blank=False, null=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField()
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_user_id')

    class Meta:
        ordering = ('-modify_time',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnai(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

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

# 購物車狀態
class Cart(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='cart_order_number')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.product_name

# 支付狀態
class Payment(models.Model):
    payment_id = models.IntegerField()
    order_number = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment_order_number')
    price = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='payment_price')
    payment_statue = models.BooleanField(default=False) # False：未付款、Ture：已付款

    def __unicode__(self):
        return self.product_name

# 商品分類表
class classify(models.Model):
    classify_name  = models.CharField(max_length=50,primary_key=True)
    status = models.IntegerField(default=1) #狀態:1正常/2停售/9删除
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-classify_name',)

    def __unicode__(self):
        return self.product_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

