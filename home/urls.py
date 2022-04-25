from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls import url
from .models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
# from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
urlpatterns = []

router = routers.DefaultRouter() # 處理視圖的路由器
router.register(r'user', UserViewSet) # 向路由器中註冊視圖集
urlpatterns += router.urls # 將路由器列表追加寫入django的路由列表中

# 生成Api文件
# hema_scview = get_swagger_view(title="My_docs")

urlpatterns = [
    # url(r"^docs/$", schema_view),
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
