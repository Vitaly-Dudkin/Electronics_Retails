from rest_framework import viewsets, filters
from network_management.permissions import IsActive
from network_management.models import Network, Supplier, Product
from network_management.serializers import NetworkSerializer, SupplierSerializer, ProductSerializer


# Create your views here.
class NetworkView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'city']
    permission_classes = [IsActive]


class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
    # permission_classes = [IsActive]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'model']
    permission_classes = [IsActive]
