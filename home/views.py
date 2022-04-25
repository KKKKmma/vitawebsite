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
from product.models import Product
from .serializers import UserSerializer
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.template.loader import get_template
from django.http.request import HttpRequest
# 分頁
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# SMTP
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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
    message = []
    if request.method == 'POST':
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
        


# def home_page(request):
#     template = get_template('index.html')
#     # posts = Post.objects.all()
#     # html = template.render(locals())
#     try:
#         urid = request.GET['user_id']
#         urpass = request.GET['user_pass']
#     except:
#         urid = None

#     if urid != None and urpass == '12345':
#         verified = True
#     else:
#         verified = False
#     html = template.render(locals())
#     # 使用HttpResponse輸出到使用者端
#     return HttpResponse(html)
    

def index(request):
    all_products = models.Product.objects.all()
    paginator = Product(all_products,5)
    p = request.GET.get('p')
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


# from helper.helper import APIHandler
from home import payment_system


# Use this to charge
# class Url_FastLaunch_Paynow(APIView):
#     def get(self, request, charge_type, fastlaunch_no, email):
#         pay_data = FASTLAUNCH_NEWEBPAY(fastlaunch_no, email,charge_type)

#         if pay_data:
#             return render(request, 'NEWEBPAY_pay.html', {'data':pay_data})
#         else:
#             return Response({'code': '000', 'data': 'Fail'})

# Use this to accept return data
# class NEWEBPAY_Fastlaunch_ReturnData(APIView):
#     def post(self, request):
#         # Get transaction data
#         data = request.data
#         decrypt_data = NEWEBPAY_Decrypt(data['TradeInfo'])
#         newebpay_decrypt_data = decrypt_data['Result']
#         # Then do whatever you like to the return datas, like store transaction data into database
#         return Response({'code': '000', 'data': 'Whatever'})
