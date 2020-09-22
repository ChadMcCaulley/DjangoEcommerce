from django_filters import FilterSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Order
from core.serializers import OrderSerializer


class OrderFilterSet(FilterSet):
    class Meta:
        model = Order
        fields = {
            'ordered': ['exact']
        }


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = OrderFilterSet

    @action(detail=False, methods=['get'])
    def latest(self, request, pk=None):
        user = request.user.id
        order = Order.objects.get(user=user, ordered=False)
        serializer = OrderSerializer(order)
        return Response(serializer.data)