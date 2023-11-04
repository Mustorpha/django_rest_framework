from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

ProductDetail = ProductDetailApiView.as_view()

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

ProductListCreate = ProductListCreateApiView.as_view()

class ProductListApiView(generics.ListAPIView):
    """
    NOT GOING TO USER THIS IMPLEMENTATION
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

ProductList = ProductListApiView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            serializer = ProductSerlizer(obj)
            return Response(serializer.data)

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    if method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            # serializer.save()
            # print(serializer.data)
            data = serializer.data
        return Response(data)
    return Response({"invalid":"data isn't formatted correctly"}, status=400)