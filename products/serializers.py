from rest_framework import serializers
from .models import Product, ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details', 'product_id']


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'variants']

    def create(self, validated_data):
        variants_data = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)
        for variant_data in variants_data:
            ProductVariant.objects.create(product=product, **variant_data)
        return product
