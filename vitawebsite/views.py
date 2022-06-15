# from django.views.generic.base import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
    
# def home_page(self):
#     return HttpResponse('index.html')

def User(self):
    return HttpResponse('Hello World!')

def index(request):
    return render(request, template_name='index.html')

def home_page(request):
    template = get_template('index.html')
    # posts = Post.objects.all()
    # html = template.render(locals())
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False
    html = template.render(locals())
    # 使用HttpResponse輸出到使用者端
    return HttpResponse(html)

# Test
def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'You get an phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
        ]
    })
    return response