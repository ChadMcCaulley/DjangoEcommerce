from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Item
from core.serializers import ItemSerializer


class ItemFilterSet(FilterSet):
    class Meta:
        model = Item
        fields = {}


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ItemFilterSet
