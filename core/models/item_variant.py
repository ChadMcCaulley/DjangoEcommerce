from django.db import models
from core.datatypes import NullableDecimal
from core.mixins import TimeStampMixin

class ItemVariant(TimeStampMixin):
    class Meta:
        db_table='item_variant'
        verbose_name_plural='Item Variants'
    title = models.CharField(max_length=100)    
    price = models.DecimalField(max_digits=15, decimal_places=2)
    list_price = NullableDecimal(max_digits=15, decimal_places=2)
    per_item_price = NullableDecimal(max_digits=15, decimal_places=2)
    rating = NullableDecimal(
        max_digits=2, decimal_places=1, editable=False
    )
    num_ratings = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
