from django.db import models
from core.mixins import TimeStampMixin

class OrderProduct (TimeStampMixin):
    """Joining table between orders and products"""
    class Meta:
        verbose_name_plural='Order Products'
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    order =  models.ForeignKey('Order', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
