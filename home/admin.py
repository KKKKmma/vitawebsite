from django.contrib import admin
from .models import Member,User,Product,Order,Cart,Payment,classify


# Register your models here.
admin.site.register(Member),
admin.site.register(User),
admin.site.register(Product),
admin.site.register(Order),
admin.site.register(Cart),
admin.site.register(Payment),
admin.site.register(classify),
