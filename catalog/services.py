from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


class ProductService:

    @staticmethod
    def get_published_products():
        """Метод для получения списка опубликованных продуктов, с использованием кэша"""
        if not CACHE_ENABLED:
            return Product.objects.filter(published=True)

        queryset = cache.get("products_queryset")

        if not queryset:
            queryset = Product.objects.filter(published=True)
            cache.set("products_queryset", queryset, 60 * 15)

        return queryset

    @staticmethod
    def get_products_by_category(category_id):

        if not CACHE_ENABLED:
            return Product.objects.filter(category__id=category_id, published=True)

        cache_key = f"products_by_category_{category_id}"
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = Product.objects.filter(category__id=category_id, published=True)
            cache.set(cache_key, queryset, 60 * 15)

        return queryset
