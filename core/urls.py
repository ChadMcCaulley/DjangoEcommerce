from django.urls import path
from rest_framework import routers
from .views import (
    ItemImageView,
    ItemView,
    ItemVariantView,
    OrderView
)

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'item_images', ItemImageView)
router.register(r'items', ItemView)
router.register(r'item_variants', ItemVariantView)
router.register(r'orders', OrderView)

urlpatterns = router.urls
