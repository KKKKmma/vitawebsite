from rest_framework import serializers
from product.models import Product, classify
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = '__all__'


class ClassifySerializer(serializers.ModelSerializer):
    class Meta:
         model = classify
         fields = '__all__'