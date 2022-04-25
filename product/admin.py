from django.contrib import admin

from .models import classify, Product

admin.site.register(classify)
admin.site.register(Product)
