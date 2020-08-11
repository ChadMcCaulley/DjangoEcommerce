from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import ProductImage
from core.serializers import ProductImageSerializer


class ProductImageFilterSet(FilterSet):
    class Meta:
        model = ProductImage
        fields = {}


class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductImageFilterSet
