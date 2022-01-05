from django.contrib import admin
from home import models


# Register your models here.
admin.site.register(models.Member),
admin.site.register(models.User),
admin.site.register(models.Order),
admin.site.register(models.Cart),
admin.site.register(models.Payment),
admin.site.register(models.classify),

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_number','reservation_date','stock','price','status')
    search_fields = ('product_number',)
    ordering = ('reservation_date',)

admin.site.register(models.Product,ProductAdmin)