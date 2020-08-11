from django.db import models


class State (models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=3)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
