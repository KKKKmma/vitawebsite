from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from home.serializers import UserSerializer 
from home.models import User
from .serializers import UserSerializer

class UsersView(GenericAPIView):
    queryset = User.objects.all() # 指名該視圖的查詢集
    serializer_class = UserSerializer # 指名使用的序列化器
    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)

# Create your views here.
def index(request):
    return HttpResponse("This is index page.")






