"""vitawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from home import views
from django.views.generic import TemplateView
from vitawebsite.views import index, simple_api_view
from vitawebsite.views import home_page
# from vitawebsite.views import index_page
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index, name='index'),
    path('api/phrases/', simple_api_view, name='phrases'),
    path('admin/', admin.site.urls),
    path('api/vi/',include("djoser.urls")),
    path('api/v1/',include('djoser.urls.authtoken')),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
]
