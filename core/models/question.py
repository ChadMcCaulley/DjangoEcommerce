from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin


class Question (TimeStampMixin):
    title = models.CharField(max_length=100)
    message = models.TextField()
    num_useful = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )