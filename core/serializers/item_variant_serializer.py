from rest_framework import serializers
from core.models import ItemVariant

class ItemVariantSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ItemVariant
        fields = [
            'url',
            'parent_item',
            'title',
            'price',
            'list_price',
            'num_items_per_order',
            'rating',
            'num_ratings',
        ]