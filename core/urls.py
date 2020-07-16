from django.urls import path
from rest_framework import routers
from .views import (
    ItemView,
    OrderView
)

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'items', ItemView)
router.register(r'orders', OrderView)

urlpatterns = router.urls