from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='user@csu',
                                   is_staff=False,
                                   is_superuser=False,
                                   is_active=False
                                   )

        user.set_password('qwerty')
        user.save()
