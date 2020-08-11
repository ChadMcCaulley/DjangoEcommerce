from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import ProductLineImage
from core.serializers import ProductLineImageSerializer


class ProductLineImageFilterSet(FilterSet):
    class Meta:
        model = ProductLineImage
        fields = {}


class ProductLineImageView(viewsets.ModelViewSet):
    queryset = ProductLineImage.objects.all()
    serializer_class = ProductLineImageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductLineImageFilterSet
