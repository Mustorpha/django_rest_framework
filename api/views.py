# from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

from products.models import Product
import json

# Create your views here.
@api_view(['POST'])
def api_home (request, *args, **kwargs):
    """
    DRF API VIEW
    """
    # instance = Product.objects.all().order_by("?").first()
    data = {}

    # if instance:
        # data = model_to_dict(model_data, fields=['title', 'content', 'price', 'sale_price'])
        # data = json.dumps(data)
        # data = ProductSerializer(instance).data
    # data = request.data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        # print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid":"data isn't formatted correctly"}, status=400)