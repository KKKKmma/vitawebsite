from django.shortcuts import render
from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, classify
from .serializers import ProductSerializer, ClassifySerializer

import pymysql

class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class classifyDetail(APIView):
    def get_object(self, category_slug):
            try:
                return classify.objects.get(slug=category_slug)
            except classify.DoesNotExist:
                raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = ClassifySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})

class HandleDB:

    def __init__(self):
        # 讀取配置檔案的資料庫資訊
        self.con = pymysql.connect(host=pymysql.get_str("mysql", "localhost"),
                                   user=pymysql.get_str("mysql", "emma"),
                                   password=pymysql.get_str("mysql", "AS098890emma"),
                                   port=pymysql.get_int("mysql", "8000"),
                                   charset="utf8"
                                   )
        self.cur = self.con.cursor()


    def create_product(self):
        pass

    def increase_product(self):
        pass

    def update_product(self):
        pass

    def delete_product(self):
        pass




    def close(self):
        self.cur.close()	 # 關閉遊標物件
        self.con.close()	# 斷開連線