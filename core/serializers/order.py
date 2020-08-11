from rest_framework import serializers
from core.models import Order
from core.serializers.product import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'products',
            'ref_code',
            'ordered_date',
            'shipping_address',
            'billing_address',
            'payment',
            'being_delivered',
            'received',
            'refund_requested',
            'refund_granted',
        ]