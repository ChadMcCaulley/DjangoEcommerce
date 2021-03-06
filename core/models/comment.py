from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from core.datatypes import NullableForeignKey
from core.mixins import TimeStampMixin


class Comment(TimeStampMixin):
    title = models.CharField(max_length=100)
    message = models.TextField()
    review = NullableForeignKey('Review', on_delete=models.CASCADE)
    parent_comment = NullableForeignKey(
        'Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.parent_comment is not None and \
            self.parent_comment.id == self.id:
            raise ValidationError(
                'Comments cannot be linked to themselves'
            )
        if self.parent_comment is None and self.review is None:
            raise ValidationError(
                'Comments must have a parent comment or review'
            )
        super().save(*args, **kwargs)
