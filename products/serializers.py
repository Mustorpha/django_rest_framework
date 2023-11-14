from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title

from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url =serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )

class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInlineSerializer(source='user.product_set.all', many=True, read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
        )
    title = serializers.CharField(validators=[validate_title])
    body = serializers.CharField(source='content')

    class Meta:
        model = Product
        fields = [
            'id',
            'owner',
            'title',
            'body',
            'price',
            'sale_price',
            'public',
            'url',
            'edit_url',
        ]

    #def validate_title(self, value):
    #    qs = Product.objects.filter(title__iexact)
    #    if qs.exist():
    #        raise serializers.ValidationError(f"{value} exits")
    #    return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)

    #def get_user(self, obj):
    #    return ({'username': obj.user.username})