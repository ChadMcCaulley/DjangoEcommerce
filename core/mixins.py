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


class AddressMixin (models.Model):
    """
    Adds address fields to model
    """
    address = models.CharField(max_length=280)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)

    class Meta:
        abstract = True