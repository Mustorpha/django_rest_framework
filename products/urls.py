from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_mixin),
    path('<int:pk>/', views.ProductDetail),
    path('<int:pk>/update', views.ProductUpdate),
    path('<int:pk>/delete', views.ProductDelete),
]