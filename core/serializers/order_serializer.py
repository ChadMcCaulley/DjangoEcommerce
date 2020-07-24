from rest_framework import serializers
from core.models import Order
from core.serializers.item_serializer import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'user',
            'items',
            'created_at',
            'updated_at',
            'ordered_date',
            'ordered',
        ]