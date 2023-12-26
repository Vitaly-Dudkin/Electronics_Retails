from rest_framework.serializers import ModelSerializer
from network_management.models import Network, Product, Supplier


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class NetworkSerializer(ModelSerializer):
    supplier = SupplierSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Network
        fields = ['id', 'name', 'email', 'phone', 'country', 'city', 'street', 'house_number',
                  'debt', 'level', 'supplier', 'products']
        read_only_fields = ['debt']
