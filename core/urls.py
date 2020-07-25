from django.urls import path
from rest_framework import routers
from .views import (
    ImageView,
    ItemView,
    ItemVariantView,
    OrderView
)

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'images', ImageView)
router.register(r'items', ItemView)
router.register(r'item_variants', ItemVariantView)
router.register(r'orders', OrderView)

urlpatterns = router.urls