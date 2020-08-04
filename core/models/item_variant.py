import uuid
from django.core.validators import MinValueValidator
from django.db import models
from core.datatypes import NullableDecimal, NullablePositiveInteger
from core.mixins import TimeStampMixin


class ItemVariant(TimeStampMixin):
    class Meta:
        db_table='core_item_variant'
        verbose_name_plural='Item Variants'
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    parent_item = models.ForeignKey(
        'Item', on_delete=models.CASCADE, related_name='variants'
    )
    title = models.CharField(max_length=100)    
    price = models.DecimalField(max_digits=15, decimal_places=2)
    list_price = NullableDecimal(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    inventory = models.PositiveIntegerField(default=0)
    rating = NullableDecimal(
        max_digits=2, decimal_places=1, editable=False
    )
    num_ratings = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    @property
    def rating_breakdown (self):
        ratings = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        result = {}
        for review in self.review_set.all():
            ratings[review.rating] += 1
        for rating in ratings.items():
            result[rating[0]] = round(rating[1] / self.num_ratings, 4)
        return result