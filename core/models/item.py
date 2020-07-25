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
    title = models.CharField(max_length=100)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='products'
    )

    def __str__(self):
        return self.title
