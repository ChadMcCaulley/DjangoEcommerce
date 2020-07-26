from django.conf import settings
from django.db import models
from core.mixins import AddressMixin


class ShippingAddress (AddressMixin):
    class Meta:
        verbose_name_plural='Shipping Addresses'
    friendly_name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
