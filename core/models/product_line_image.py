from django.db import models
from core.mixins import TimeStampMixin

def get_upload_path(instance, filename):
    prodLine = instance.product_line
    return f'images/{prodLine.title}_{prodLine.id}/{filename}'


class ProductLineImage(TimeStampMixin):
    class Meta:
        verbose_name_plural='Product Line Images'
    image = models.ImageField(upload_to=get_upload_path)
    product_line = models.ForeignKey(
        'ProductLine', on_delete=models.CASCADE, related_name='images'
    )
