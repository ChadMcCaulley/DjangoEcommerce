from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import ProductLine
from core.serializers import (
    ProductLineSerializer, RatingBreakdownSerializer
)


class ProductLineFilterSet(FilterSet):
    class Meta:
        model = ProductLine
        fields = {}


class ProductLineView(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    serializer_class = ProductLineSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductLineFilterSet

    @action(detail=True, methods=['get'])
    def rating_breakdown (self, request, pk=None):
        variant = self.get_object()
        serializer = RatingBreakdownSerializer(variant)
        return Response(serializer.data)