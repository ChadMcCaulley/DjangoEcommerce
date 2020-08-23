from rest_framework import serializers
from core.models import Order
from core.serializers.product import ProductSerializer
from core.serializers.order import OrderSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model = Order
        fields = [
            'id',
            'product',
            'order',
            'quantity',
        ]