from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreate, name="product-list"),
    path('<int:pk>/', views.ProductDetail, name="product-detail"),
    path('<int:pk>/update', views.ProductUpdate, name="product-edit"),
    path('<int:pk>/delete', views.ProductDelete, name="product-delete"),
]