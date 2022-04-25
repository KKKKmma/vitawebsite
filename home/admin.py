from django.contrib import admin
from home import models


# Register your models here.
admin.site.register(models.Member),
admin.site.register(models.User),


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_number','reservation_date','stock','price','status')
#     search_fields = ('product_number',)
#     ordering = ('reservation_date',)

# admin.site.register(models.ProductAdmin)