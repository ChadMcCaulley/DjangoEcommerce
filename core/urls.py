from django.urls import path
from rest_framework import routers
from .views import (
    OrderView,
    OrderProductView,
    ProductView,
    ProductImageView,
    ReviewView
)

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'product_images', ProductImageView)
router.register(r'products', ProductView)
router.register(r'orders', OrderView)
router.register(r'order_products', OrderView)
router.register(r'reviews', ReviewView)

urlpatterns = router.urls
