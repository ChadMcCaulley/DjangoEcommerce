from rest_framework import serializers
from core.models import ItemVariant


class RatingBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariant
        fields = [
            'id',
            'rating_breakdown',
            'num_ratings'
        ]