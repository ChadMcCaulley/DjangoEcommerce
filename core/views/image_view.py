from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Image
from core.serializers import ImageSerializer


class ImageFilterSet(FilterSet):
    class Meta:
        model = Image
        fields = {}


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ImageFilterSet
