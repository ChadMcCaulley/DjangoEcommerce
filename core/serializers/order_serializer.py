from rest_framework import serializers
from core.models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            'url',
            'user',
            'items',
            'start_date',
            'ordered_date',
            'ordered',
        ]