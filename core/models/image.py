from django.db import models
from core.mixins import TimeStampMixin

class Image(TimeStampMixin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    item = models.ForeignKey('ItemVariant', on_delete=models.CASCADE)