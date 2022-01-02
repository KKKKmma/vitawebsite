from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField
from .models import *
from vitawebsite.home.models import Order, Product



class cart(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='cart_order_number')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
            self.cart = cart




    def add_to_cart(self,request):
        # 庫存量僅有1，因此先確認是否有庫存，若有，則將商品加入購物車中
        if stock is True:
            if product_number not in self.cart:
                self.cart[product_number] = {'quantity':0,
                                            'price':str(product.price)}
            self.save()
        
        else:
            return "Please check your date is unavailable."

    def save(self):
        # 告訴瀏覽器狀態已變更，要保存
        self.session.modified = True        

    def total(self,request):
        # 計算購物車總金額
        return sum(IntegerField(item['price']) * item['quantity'] for item in self.cart.values())


    def remove_from_cart(self, request):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()