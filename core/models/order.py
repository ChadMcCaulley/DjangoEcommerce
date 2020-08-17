import uuid
from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin
from core.datatypes import NullableDateTime
from core.models.order_product import OrderProduct


class Order (TimeStampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField('Product', through=OrderProduct)
    ref_code = models.UUIDField(default=uuid.uuid4)
    ordered_date = NullableDateTime()
    shipping_address = models.ForeignKey(
        'UserAddress',
        on_delete=models.PROTECT,
        related_name="shipping_address"
    )
    billing_address = models.ForeignKey(
        'UserAddress',
        on_delete=models.PROTECT,
        related_name="billing_address"
    )
    payment = models.DecimalField(max_digits=12, decimal_places=2)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.id}_{self.ref_code}'

