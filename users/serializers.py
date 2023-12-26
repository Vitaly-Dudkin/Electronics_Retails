from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined']

    def validate_password(self, value):
        return make_password(value)
