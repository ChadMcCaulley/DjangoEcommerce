from rest_framework import serializers
from core.models import Order
from core.serializers.item_serializer import ItemSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'url',
            'user',
            'items',
            'created_at',
            'updated_at',
            'ordered_date',
            'ordered',
        ]