from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from network_management.models import Supplier
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

        self.client.force_authenticate(user=self.user)

    def test_supplier_list(self):
        url = reverse('network_management:suppliers-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['name'], 'Test supplier')

    def test_supplier_detail(self):
        url = reverse('network_management:suppliers-detail', args=[self.supplier.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['name'], 'Test supplier')

    def test_supplier_delete(self):
        url = reverse('network_management:suppliers-detail', args=[self.supplier.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)