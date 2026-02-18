from rest_framework import serializers
from .models import Product, Variation
from category.models import Category


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['variation_category', 'variation_value']


class ProductSerializer(serializers.ModelSerializer):
    variations = VariationSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = [

            'id',
            'category',
            'product_name',
            'slug',
            'description',
            'price',
            'stock',
            'is_available',
            'images',
            'variations',
        ]



