from re import template
from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import *
from home.models import Order, Product
from product.models import Product
from home.views import login



class cart(models.Model):
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart


    @login
    def add(self,request):
        stock = Product.stock
        price = Product.price
        product_number = Product.product_name
        # 庫存量僅有1，因此先確認是否有庫存，若有，則將商品加入購物車中
        if stock is True:
            if product_number not in self.cart:
                self.cart[product_number] = {'product_number':product_number,
                                            'quantity':0,
                                            'price':price}
            self.save()
        
        else:
            return "Please check your date is unavailable."

        template = get_template('cart.vue')
        request_context = RequestContext(request)
        request_context.push(locals())
        html = template.render(request_context)
        return HttpResponse(html)

    def save(self):
        # 告訴瀏覽器狀態已變更，要保存
        self.session.modified = True     
        self.save()   

    def total(self,request):
        # 計算購物車總金額
        return sum(IntegerField(item['price']) * item['quantity'] for item in self.cart.values())

    def get_cart_list(self):
        cart_list = []
        for product_number, value in self.cart.items():
            cart_list.append({
                'id': product_number,
                'name': value['product_name'],
                'price': value['price'],
                'quantity': value['quantity'],
                })
            return cart_list
    

    def remove_from_cart(self, request):
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        product_number = str(product_number)
        if product_number in self.cart:
            del self.cart[product_number]
        self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()