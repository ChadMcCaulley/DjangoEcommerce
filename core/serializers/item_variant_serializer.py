from rest_framework import serializers
from core.models import ItemVariant
from core.serializers.item_image_serializer import ItemImageSerializer


class ItemVariantSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

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