from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    """Команда для создания группы пользователей"""

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана'))

        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" же существует'))


        try:
            can_unpublish = Permission.objects.get(codename='can_unpublish_product')
            can_delete = Permission.objects.get(codename='can_delete_product')

            group.permissions.add(can_unpublish, can_delete)
            self.stdout.write(self.style.SUCCESS('Права для группы "Модератор продуктов" назначены'))

        except ObjectDoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'Не существует одно из расширений {e}'))