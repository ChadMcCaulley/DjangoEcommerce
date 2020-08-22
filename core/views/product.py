from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Product
from core.serializers import (
    ProductSerializer, ProductDetailSerializer,
    RatingBreakdownSerializer
)

class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'id': ['exact', 'in']
        }


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilterSet

    @action(detail=True, methods=['get'])
    def rating_breakdown (self, request, pk=None):
        variant = self.get_object()
        serializer = RatingBreakdownSerializer(variant)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer