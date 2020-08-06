from rest_framework import serializers
from core.models import ItemImage

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = [
            'id',
            'image',
            'item',
            'created_at',
            'updated_at'
        ]