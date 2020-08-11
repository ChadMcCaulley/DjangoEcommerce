from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Product
from core.serializers import ProductSerializer

class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {}


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilterSet
