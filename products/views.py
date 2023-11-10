from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from api.mixins import ProductEditorPermissionMixin, UserQuerySetMixin

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = pk

ProductDetail = ProductDetailApiView.as_view()

class ProductListCreateApiView(
    UserQuerySetMixin,
    ProductEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        # email = serializer.validated_date.pop('email')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
    
    #def get_queryset(self, *args, **kwargs):
    #    qs = super().get_queryset(*args, **kwargs)
    #    request = self.request
    #    print('User:', request.user.id)
    #    print(request.user)
    #    if not request.user.is_authenticated:
    #        return Product.objects.none()
    #    return qs.filter(user=request.user)

ProductListCreate = ProductListCreateApiView.as_view()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

ProductUpdate = ProductUpdateApiView.as_view()

class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

ProductDelete = ProductDestroyApiView.as_view()

# class ProductListApiView(generics.ListAPIView):
#     """
#     NOT GOING TO USE THIS IMPLEMENTATION
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# ProductList = ProductListApiView.as_view()

class ProductMixinView(
    ProductEditorPermissionMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin, 
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        # print(args, kwargs)
        pk = kwargs.get('pk') or None
        if pk is not None:
            self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'A single view method using mixins'
        serializer.save(content=content)

product_list_mixin = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method
    pk = kwargs.get('pk') or None

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