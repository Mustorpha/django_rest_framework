from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url =serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    #related_products = serializers.SerializerMethodField(read_only=True)

    #def get_related_products(self, obj):
    #    print(obj)
    #    qs = obj.product_set.all()[:5]
    #    return (UserProductInlineSerializer(qs, many=True, context=self.context).data)