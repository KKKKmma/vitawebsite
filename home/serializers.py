from home.models import Member,User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'

class classifySerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = '__all__'