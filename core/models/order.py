from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin


class OrderItem (TimeStampMixin):
    """Joining table between orders and items"""
    class Meta:
        db_table='order_item'
        verbose_name_plural='Order Items'
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order (TimeStampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

