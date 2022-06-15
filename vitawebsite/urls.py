from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
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
    # path('api/phrases/', simple_api_view, name='phrases'), # Test
    path('admin/', admin.site.urls), # 管理者
    path('api/vi/',include("djoser.urls")),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/product/', include('product.urls')),
    path('api-auth/', include('rest_framework.urls'))
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
