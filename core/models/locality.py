from django.db import models


class Locality (models.Model):
    class Meta:
        verbose_name_plural='Localities'
    name = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=10)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
