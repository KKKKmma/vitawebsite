from django.urls import path, include

from product import views

urlpatterns = [
    path('products/search/', views.search), 
    path('products/<slug:category_slug>/', views.classifyDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('latest-products/', views.ProductsList.as_view()),
]
