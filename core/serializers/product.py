from rest_framework import serializers
from core.models import Product
from core.serializers.product_image import ProductImageSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'category',
            'company',
            'description',
            'id',
            'inventory',
            'images',
            'list_price',
            'num_reviews',
            'price',
            'quantity',
            'rating',
            'title',
        ]