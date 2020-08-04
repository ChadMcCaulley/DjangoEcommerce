from rest_framework import serializers
from core.models import ItemVariant
from core.serializers.image_serializer import ImageSerializer


class ItemVariantSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ItemVariant
        fields = [
            'created_at',
            'id',
            'inventory',
            'images',
            'list_price',
            'num_ratings',
            'parent_item',
            'price',
            'quantity',
            'rating',
            'title',
            'updated_at',
        ]