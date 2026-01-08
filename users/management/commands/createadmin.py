from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='testadmin@email.ru',
            first_name='admin',
            last_name='admin'
        )

        user.set_password('27081911')

        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'Суперпользователь с email {user.email}, успешно создан'))
