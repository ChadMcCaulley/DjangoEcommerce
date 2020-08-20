from rest_framework import serializers
from core.models import Review
from core.serializers.user import OtherUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = OtherUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'title',
            'message',
            'rating',
            'user',
        ]