from rest_framework import serializers
from core.models import ProductLineImage

class ProductLineImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLineImage
        fields = [
            'id',
            'image',
            'product',
            'created_at',
            'updated_at'
        ]