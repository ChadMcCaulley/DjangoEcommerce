import uuid
from django.db import models
from core.datatypes import NullableDecimal
from core.mixins import TimeStampMixin


class Item(TimeStampMixin):
    """
    The parent item for a set of item variants.
    Allows for multiple color options / units for order of an item with
    separate reviews. Item will display a cummulative rating, but 
    each variant will show it's rating
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=100)    
    max_price = models.DecimalField(
        max_digits=15, decimal_places=2, editable=False
    )
    min_price = models.DecimalField(
        max_digits=15, decimal_places=2, editable=False
    )
    rating = NullableDecimal(
        max_digits=2, decimal_places=1, editable=False
    )
    num_ratings = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
