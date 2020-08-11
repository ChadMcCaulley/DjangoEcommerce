from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin


class UserAddress (TimeStampMixin):
    class Meta:
        verbose_name_plural='User Addresses'
    BILLING = 'B'
    SHIPPING = 'S'
    ADDRESS_TYPES = [
        (BILLING, 'Billing'),
        (SHIPPING, 'Shippping')
    ]
    friendly_name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    is_default = models.BooleanField(default=False)
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPES)
