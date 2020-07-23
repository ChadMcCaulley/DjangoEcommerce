from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin

class Review(TimeStampMixin):
    title = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    item = models.ForeignKey('ItemVariant', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )