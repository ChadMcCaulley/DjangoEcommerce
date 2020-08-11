from rest_framework import serializers
from core.models import ProductLine


class RatingBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = [
            'rating_breakdown',
            'num_ratings',
            'rating'
        ]