from rest_framework import serializers
from core.models import Item
from core.serializers.item_variant_serializer import \
    ItemVariantSerializer

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    variants = ItemVariantSerializer(many=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'url',
            'title',
            'max_price',
            'min_price',
            'rating',
            'num_ratings',
            'variants'
        ]