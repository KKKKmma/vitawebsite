from django.views.generic.base import View
from django.http import HttpResponse

class TemplateView(View):
    
    def get(self, request):
        return HttpResponse('index.html')

def User(self):
    return HttpResponse('Hello World!')