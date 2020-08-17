from rest_framework import serializers
from core.models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image',
            'product',
            'created_at',
            'updated_at'
        ]