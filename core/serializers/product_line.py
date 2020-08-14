from rest_framework import serializers
from core.models import ProductLine
from core.serializers.product_line_image import \
    ProductLineImageSerializer

class ProductLineSerializer(serializers.ModelSerializer):
    images = ProductLineImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductLine
        fields = [
            'category',
            'description',
            'id',
            'images',
            'title',
        ]
        read_only_fields = (
            'rating', 'num_ratings', 'updated_at', 'created_at'
        )