from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Review
from core.serializers import ReviewSerializer

class ReviewFilterSet(FilterSet):
    class Meta:
        model = Review
        fields = {
            'product__id': ['exact'],
            'rating': ['exact', 'gt', 'lt']
        }


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ReviewFilterSet
