from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin


class Payment (TimeStampMixin):
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.FloatField()
