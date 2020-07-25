from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin, AddressMixin
from core.datatypes import NullableURL


class Company(TimeStampMixin, AddressMixin):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    website = NullableURL()
    