from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import ItemVariant
from core.serializers import (
    ItemVariantSerializer, RatingBreakdownSerializer
)

class ItemVariantFilterSet(FilterSet):
    class Meta:
        model = ItemVariant
        fields = {}


class ItemVariantView(viewsets.ModelViewSet):
    queryset = ItemVariant.objects.all()
    serializer_class = ItemVariantSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ItemVariantFilterSet
    
    @action(detail=True, methods=['get'])
    def rating_breakdown (self, request, pk=None):
        variant = self.get_object()
        serializer = RatingBreakdownSerializer(variant)
        return Response(serializer.data)
