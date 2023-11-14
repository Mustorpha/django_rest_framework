from rest_framework import generics, status
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(q, user=user)
            return result
        return Product.objects.none()