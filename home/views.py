from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from home import models, forms

from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from home.serializers import UserSerializer 
from home.models import User
from .serializers import UserSerializer
from django.contrib import messages
from django.contrib.sessions.models import Session


# SMTP
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
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


def login(request):
    if request.method =='POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['member_name'].strip()
            phone_number = request.POST['phone_number']
            if phone_number is not None:
                if phone_number.is_active:
                    message.add_message(request, message.SUCCESS, '登入成功')
                    return redirect('/')
                else:
                    message.add_message(request, message.WARNING, '登入失敗')
            else:
                message.add_message(request, message.WARNING, '請檢查輸入欄位')
        else:
            login_form = forms.LoginForm() # GET初始化LoginForm
        


def home_page(request):
    # template = get_template('index.html')
    # posts = Post.objects.all()
    # html = template.render(locals())

    # 使用HttpResponse輸出到使用者端
    # return HttpResponse()
    pass






