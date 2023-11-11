from rest_framework import generics, status
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

from . import client

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

class AlgoliaSearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        tag = request.GET.get('tag') or None
        user = None
        if request.user.is_authenticated:
            user = request.user.username

        public = str(request.GET.get('public')) != "0"
        if query:
            result = client.perform_search(query, tags=tag, user=user, public=public)
            return Response(result)
        return Response('', status=status.HTTP_400_BAD_REQUEST)