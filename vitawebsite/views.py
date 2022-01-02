from django.views.generic.base import View
from django.http import HttpResponse

    
def index_page(self):
    return HttpResponse('index.html')

def User(self):
    return HttpResponse('Hello World!')