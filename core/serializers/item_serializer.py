from rest_framework import serializers
from core.models import Item
from core.serializers.item_variant_serializer import \
    ItemVariantSerializer
from core.serializers.image_serializer import ImageSerializer

class ItemSerializer(serializers.ModelSerializer):
    variants = ItemVariantSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'title',
            'max_price',
            'min_price',
            'rating',
            'num_ratings',
            'created_at',
            'updated_at',
            'variants'
        ]
        read_only_fields = (
            'max_price', 'min_price', 'rating', 'num_ratings',
        )