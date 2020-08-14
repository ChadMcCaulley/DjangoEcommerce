from rest_framework import serializers
from core.models import Product


class RatingBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'rating_breakdown',
            'num_reviews',
            'rating'
        ]