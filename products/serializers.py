from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title

class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'edit_url'
        ]

    #def validate_title(self, value):
    #    qs = Product.objects.filter(title__iexact)
    #    if qs.exist():
    #        raise serializers.ValidationError(f"{value} exits")
    #    return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request.is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)