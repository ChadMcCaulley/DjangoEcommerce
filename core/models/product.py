import uuid
from django.core.validators import MinValueValidator
from django.db import models
from core.datatypes import NullableDecimal
from core.mixins import TimeStampMixin


class Product(TimeStampMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='products'
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    rating = NullableDecimal(
        max_digits=2, decimal_places=1, editable=False
    )
    num_reviews = models.PositiveIntegerField(default=0, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    list_price = NullableDecimal(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def rating_breakdown (self):
        ratings = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        if self.num_reviews == 0:
            return None
        result = {}
        for review in self.review_set.all():
            ratings[review.rating] += 1
        for rating in ratings.items():
            result[rating[0]] = round(rating[1] / self.num_reviews, 4)
        return result