from rest_framework import serializers
from core.models import ProductLine
from core.serializers.product import ProductSerializer

class ProductLineSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProductLine
        fields = [
            'created_at',
            'description',
            'id',
            'title',
            'products',
            'updated_at',
        ]
        read_only_fields = (
            'rating', 'num_ratings',
        )