from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from network_management.models import Network, Supplier, Product
from users.models import User


# Create your tests here.
class NetworkTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user1@csu',
            password='qwerty',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        self.supplier = Supplier.objects.create(
            name='Test supplier',
            email='test@csu',
            country='Ukraine',
            city='Kyiv',
            street='Test street',
            house_number='1',

        )

        self.network = Network.objects.create(
            name='Test network',
            email='test@csu',
            phone='123456',
            country='Ukraine',
            city='Kyiv',
            street='Test street',
            house_number='1',
            supplier=self.supplier,
            debt=200,
            level=1,
        )

        self.product = Product.objects.create(
            name='Test product',
            model='Test model',
            release_date='2022-01-01',
            price=100,
            network=self.network,
            description='Test description',
        )

        self.client.force_authenticate(user=self.user)

    def test_product_list(self):
        url = reverse('network_management:products-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['name'], 'Test product')

    def test_product_detail(self):
        url = reverse('network_management:products-detail', args=[self.product.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['name'], 'Test product')

    def test_product_delete(self):
        url = reverse('network_management:products-detail', args=[self.product.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)