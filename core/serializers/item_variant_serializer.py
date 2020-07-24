from rest_framework import serializers
from core.models import ItemVariant

class ItemVariantSerializer(serializers.ModelSerializer):
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
        ]