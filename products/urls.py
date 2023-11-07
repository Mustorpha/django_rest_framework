from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreate),
    path('<int:pk>/', views.ProductDetail),
    path('<int:pk>/update', views.ProductUpdate),
    path('<int:pk>/delete', views.ProductDelete),
]