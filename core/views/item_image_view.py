from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import ItemImage
from core.serializers import ItemImageSerializer


class ItemImageFilterSet(FilterSet):
    class Meta:
        model = ItemImage
        fields = {}


class ItemImageView(viewsets.ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ItemImageFilterSet
