from rest_framework import serializers
from core.models import ItemVariant
from core.serializers.image_serializer import ImageSerializer


class ItemVariantSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ItemVariant
        fields = [
            'parent_item',
            'title',
            'price',
            'list_price',
            'num_items_per_order',
            'rating',
            'created_at',
            'updated_at',
            'num_ratings',
            'images'
        ]