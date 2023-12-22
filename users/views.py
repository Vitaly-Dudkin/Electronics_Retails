from rest_framework import generics
from users.permissions import IsSuperUser
from users.models import User

from users.serializers import UserSerializer


# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.get(id=user.id)
