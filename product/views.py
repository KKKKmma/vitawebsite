from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import request
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import Http404,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, classify
from .serializers import ProductSerializer, ClassifySerializer

import pymysql

@csrf_exempt
class ProductsAPI(APIView):
    def __init__(self, products, serializer):
        self.products = products
        self.serializer = serializer
    
    def product_request(self, request, format=None):
        if request.method == "GET":
            products = Product.objects.all()
            products_list = []
            for product in products:
                products_list.append({
                    "product_number" : Product.product_number,
                    "stock" : Product.stock,
                    "category" : Product.category,
                    "status" : Product.status,
                })
            serializer = ProductSerializer(products, many=True)
            return JsonResponse(ProductSerializer.data)
        elif request.method == "POST":
            products_data = JSONParser().parse(request)
            products_serializer = ProductSerializer(data=products_data)
            if products_serializer.is_valid():
                products_serializer.save()
                return JsonResponse("Add Successfully", safe=False)
        elif request.method == "PUT":
            products_data = JSONParser().parse(request)
            products = products.objects.get(ProductID=products_data["ProductID"])
            products_serializer = ProductSerializer(products,data=products_data)
            if products_serializer.is_valid():
                products_serializer.save()
                return JsonResponse("Update Successfully", safe=False)
            return JsonResponse("Failed to Update")
        elif request.method == "DELETE":
            products = Product.objects.get(productsID=id)
            products.delete()
            return JsonResponse("Delete Successfully", safe=False)
        


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

    def delete(self, request, pd):
        try:
            product = Product.objects.get(pd=pd)
        except:
            return HttpResponse()
        product.delete()
        return HttpResponse()

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




