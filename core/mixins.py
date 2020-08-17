from django.db import models
from django.utils.timezone import now


class TimeStampMixin(models.Model):
    """
    Enables created_at and updated_at for all models taht use the mixin
    """
    created_at = models.DateTimeField(
        null=True, blank=True, editable=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        null=True, blank=True, auto_now=True
    )

    class Meta:
        abstract = True
