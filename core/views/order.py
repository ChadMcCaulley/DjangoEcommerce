from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Order
from core.serializers import OrderSerializer


class OrderFilterSet(FilterSet):
    class Meta:
        model = Order
        fields = {}


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = OrderFilterSet
