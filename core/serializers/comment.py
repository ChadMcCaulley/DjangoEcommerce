from rest_framework import serializers
from core.models import Comment
from core.serializers.user import OtherUserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = OtherUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'title',
            'message',
            'review',
            'user',
        ]