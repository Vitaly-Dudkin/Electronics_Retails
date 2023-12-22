# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class SuperUserTestCase(APITestCase):

    def setUp(self) -> None:
        """Prepare data"""

        self.superuser = User.objects.create(
            id=3,
            email='superuser@user.com',
            password='qwerty',
            city='Kyiv',
            phone='123456',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )
        self.client.force_authenticate(user=self.superuser)

    def test_superuser_get_users(self):
        """Test superuser"""

        url = reverse('users:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            id=5,
            email='user5@user.com',
            password='qwerty',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        self.client.force_authenticate(user=self.user)

    def test_user_get_users(self):
        """Test user"""

        url = reverse('users:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_get_users_detail(self):
        """Test user"""

        url = reverse('users:detail_update_delete', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
