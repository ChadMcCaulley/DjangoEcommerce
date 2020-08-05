from rest_framework import serializers
from core.models import ItemVariant


class RatingBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVariant
        fields = [
            'rating_breakdown',
            'num_ratings',
            'rating'
        ]