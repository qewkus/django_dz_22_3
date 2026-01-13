from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load categories and products from fixtures'

    def handle(self, *args, **kwargs):
        # Сброс базы данных
        self.stdout.write(self.style.WARNING('Flushing the database...'))
        call_command('flush', interactive=False)

        # Загрузка категорий
        self.stdout.write(self.style.SUCCESS('Loading categories...'))
        call_command('loaddata', 'your_app/fixtures/categories.json')

        # Загрузка продуктов
        self.stdout.write(self.style.SUCCESS('Loading products...'))
        call_command('loaddata', 'your_app/fixtures/products.json')

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
