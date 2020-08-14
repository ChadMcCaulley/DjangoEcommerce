from django.urls import path
from rest_framework import routers
from .views import (
    ProductImageView,
    ProductView,
    OrderView
)

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'product_images', ProductImageView)
router.register(r'products', ProductView)
router.register(r'orders', OrderView)

urlpatterns = router.urls
