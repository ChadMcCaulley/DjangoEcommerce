from django.db import models
from core.mixins import TimeStampMixin

def get_upload_path(instance, filename):
    parent = instance.product.product_line
    title = instance.product.title
    return f'images/{parent.title}_{parent.id}/{title}/{filename}'


class ProductImage(TimeStampMixin):
    class Meta:
        verbose_name_plural='Product Images'
    image = models.ImageField(upload_to=get_upload_path)
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images'
    )
