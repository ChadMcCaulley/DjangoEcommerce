from django.db import models
from core.mixins import TimeStampMixin

def get_upload_path(instance, filename):
        return f'images/{instance.item.title}/{filename}'


class ItemImage(TimeStampMixin):
    class Meta:
        db_table='core_item_image'
        verbose_name_plural='Item Images'
    image = models.ImageField(upload_to=get_upload_path)
    item = models.ForeignKey(
        'ItemVariant', on_delete=models.CASCADE, related_name='images'
    )
