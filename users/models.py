from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
    }


class User(AbstractUser):

    username = None

    email = models.EmailField(max_length=150, unique=True, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='Phone', **NULLABLE)
    city = models.CharField(max_length=50,  verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='', verbose_name='Photo', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
