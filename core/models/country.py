from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name_plural='Countries'
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)


    
