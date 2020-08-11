import uuid
from django.core.validators import MinValueValidator
from django.db import models
from core.datatypes import NullableDecimal
from core.mixins import TimeStampMixin


class Product(TimeStampMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    product_line = models.ForeignKey(
        'ProductLine', on_delete=models.CASCADE, related_name='products'
    )
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