from rest_framework.routers import DefaultRouter

from network_management.views import NetworkView, ProductView, SupplierView
from network_management.apps import NetworkManagementConfig

app_name = NetworkManagementConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierView, basename='suppliers')

router.register(r'networks', NetworkView, basename='networks')

router.register(r'products', ProductView, basename='products')

urlpatterns = [

    ] + router.urls
