from rest_framework import serializers
from core.models import OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = [
            'id',
            'product',
            'order',
            'quantity',
        ]