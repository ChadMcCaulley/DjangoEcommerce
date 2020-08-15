from django.db import models
from core.mixins import TimeStampMixin

def get_upload_path(instance, filename):
    product = instance.product
    return f'images/{product.company.name}/{product.id}/{filename}'


class ProductImage(TimeStampMixin):
    class Meta:
        verbose_name_plural='Product Images'
    image = models.ImageField(
        upload_to=get_upload_path, max_length=300
    )
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images'
    )
