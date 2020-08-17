from django.db import models
from core.datatypes import NullableChar

class Address (models.Model):
    class Meta:
        verbose_name_plural='Addresses'
    street_address = models.CharField(max_length=280)
    additional_address = NullableChar(max_length=280)
    locality = models.ForeignKey('Locality', on_delete=models.CASCADE)
