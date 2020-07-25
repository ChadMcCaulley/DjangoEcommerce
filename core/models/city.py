from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural='Cities'
    name = models.CharField(max_length=50)


    
