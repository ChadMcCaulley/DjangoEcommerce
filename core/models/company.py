from django.conf import settings
from django.db import models
from core.mixins import TimeStampMixin
from core.datatypes import NullableURL


class Company(TimeStampMixin):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    website = NullableURL()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    