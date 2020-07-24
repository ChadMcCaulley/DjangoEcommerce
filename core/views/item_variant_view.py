from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import ItemVariant
from core.serializers import ItemVariantSerializer


class ItemVariantFilterSet(FilterSet):
    class Meta:
        model = ItemVariant
        fields = {}


class ItemVariantView(viewsets.ModelViewSet):
    queryset = ItemVariant.objects.all()
    serializer_class = ItemVariantSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ItemVariantFilterSet
